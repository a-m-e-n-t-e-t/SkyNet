#!/usr/bin/env python3
"""Patch v9.29 -> v9.30: Issues integration (полный переход)."""

from pathlib import Path

SRC = Path("/home/z/my-project/download/SkyNet_PROMPT_v9.30.md")
text = SRC.read_text(encoding="utf-8")

# ===== 1. ШАПКА =====
text = text.replace(
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.29",
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.30"
)
text = text.replace(
    '> **Версия:** 9.29\n> **Дата:** 2026-11-03\n> **Базируется на:** v9.28 + T-X гибридная (liquid metal=маскировка) + _decisions.log enforcement',
    '> **Версия:** 9.30\n> **Дата:** 2026-11-03\n> **Базируется на:** v9.29 + полная интеграция GitHub Issues как очередь задач'
)
text = text.replace("  version: 9.29", "  version: 9.30")
text = text.replace("## 5 столпов архитектуры v9.29", "## 5 столпов архитектуры v9.30")

# ===== 2. CHANGELOG =====
old_end = """> 🔵 **СЖАТИЕ ПРОМПТА (унаследовано из v9.17/v9.19, Уровень 2):**"""
new_end = """> 🔴 **v9.30: GITHUB ISSUES КАК ОСНОВА ПРОЦЕССА**
>
> **Принцип:** Каждая задача = GitHub Issue. AI читает Issues, выполняет, закрывает. Коммиты ссылаются на Issues (`closes #N`).
>
> **Изменения в §9:**
> - Phase 0: проверка открытых Issues с меткой `todo`
> - Phase 1: задача из Issue ИЛИ из чата (AI создаёт Issue при чат-запросе)
> - Phase 7: закрыть Issue после выполнения
> - §9.8: Issues как очередь задач (метки: todo → in_progress → done)
> - §9.9: авто-создание Issues при F-метрика FAIL
>
> **Обновлённые скрипты:**
> - `pipeline.py`: Phase 0 вызывает `check_open_issues()`
> - `pre-commit-hook.py`: при FAIL создаёт Issue с меткой `bug`
> - `batch-process.yml`: берёт задачи из Issues по приоритету
>
> **Новые метрики:**
> - F89: `доля_задач_выполненных_через_Issues` ≥ 0.80
> - P086: Issues как основа процесса
>
> 📊 **ИТОГО v9.30:**
>
> | Метрика | v9.29 | v9.30 | Δ |
> |---|---:|---:|---|
> | Принципов | 85 | 86 | +1 (P086) |
> | Метрик | 138 | 139 | +1 (F89) |
>
> 🔵 **СЖАТИЕ ПРОМПТА (унаследовано из v9.17/v9.19, Уровень 2):**"""
assert old_end in text
text = text.replace(old_end, new_end)
print("✓ Шапка + changelog обновлены")

# ===== 3. §9.0 Phase 0 — добавить проверку Issues =====
# Найти "0.6 Если pipeline.py отсутствует" и добавить шаг 0.7
old_06 = "  0.6 Если pipeline.py отсутствует → Этап 0.5 §17 (первичная инициализация)"
new_06 = """  0.6 Если pipeline.py отсутствует → Этап 0.5 §17 (первичная инициализация)
  0.7 **v9.30: Проверить открытые Issues с меткой `todo`** (через GitHub API)
      - GET /repos/a-m-e-n-t-e-t/SkyNet/issues?state=open&labels=todo&sort=created&direction=asc
      - Если есть → предложить выполнить первую `todo` задачу
      - Записать количество в telemetry: `open_issues_todo: N`
  0.8 **v9.30: Если есть Issues с меткой `blocked`** → проверить, может ли AI разрешить
      - Если да → изменить метку `blocked → in_progress`, выполнить
      - Если нет → оставить, сообщить пользователю"""
text = text.replace(old_06, new_06)
print("✓ §9.0 Phase 0 — добавлена проверка Issues (0.7, 0.8)")

# ===== 4. §9.1 — добавить Issues как источник для batch =====
old_batch = """  priority_order:
    1: "canon модели первыми (простые, меньше метрик)"
    2: "canon_realizable (средние)"
    3: "real модели последними (сложные, все метрики)\""""
new_batch = """  priority_order:
    # v9.30: приоритет по Issues меткам
    1: "Issues с меткой bug (F-метрика FAIL) — критичные"
    2: "Issues с меткой audit (F86 полнота)"
    3: "Issues с меткой model-request"
    4: "Issues с меткой hypothesis"
    5: "Issues с меткой question"
    6: "canon модели первыми (если нет Issues)"
    7: "canon_realizable (средние)"
    8: "real модели последними (сложные)\""""
text = text.replace(old_batch, new_batch)
print("✓ §9.1 — приоритет по Issues меткам")

# ===== 5. §9.8 — Issues как очередь задач =====
S10_HEADER = "## §D. YAML-СХЕМЫ (§12)"
S9_8_BLOCK = """### §9.8 Issues как очередь задач (v9.30 НОВОЕ — полная интеграция)

> **Принцип (P086):** Каждая задача = GitHub Issue. AI читает Issues, выполняет, закрывает. Коммиты ссылаются на Issues.

**Мет labels (статусы задач):**

| Метка | Смысл | Кто ставит | Действие AI |
|---|---|---|---|
| `todo` | Задача в очереди | Пользователь или AI | Взять следующую `todo` |
| `in_progress` | AI начал работу | AI | Выполнить, закрыть |
| `blocked` | Нужна WebSearch или уточнение | AI | Запросить у пользователя |
| `done` | Выполнена | AI | Закрыть Issue |
| `bug` | F-метрика FAIL | pre-commit-hook.py | Исправить и закрыть |
| `audit` | Аудит полноты (F86) | check_model_completeness.py | Дополнить и закрыть |
| `model-request` | Запрос новой модели | Пользователь | Создать файлы модели |
| `hypothesis` | Гипотеза (P003) | Пользователь | Протестировать → accepted/rejected |
| `heuristic_applied` | Применена эвристика (F85) | AI | Требует ручной проверки |

**Алгоритм работы (если запрос через Issue):**
1. AI читает Issue (текст + метки)
2. Меняет метку `todo → in_progress` (через GitHub API)
3. Выполняет задачу (создаёт файлы, исправляет баг, и т.д.)
4. Коммит с `closes #N` в сообщении
5. Закрывает Issue (метка `in_progress → done`)
6. Авто-отчёт (§9.5) с указанием закрытых Issues

**Алгоритм работы (если запрос через чат):**
1. AI создаёт Issue с соответствующей меткой (через GitHub API)
2. Меняет метку `todo → in_progress`
3. Выполняет задачу
4. Коммит с `closes #N`
5. Закрывает Issue

**Создание Issue при FAIL (§9.9):**
При F-метрика FAIL → `pre-commit-hook.py` автоматически создаёт Issue:
```python
def create_issue_for_failure(metric_id, value, threshold, details):
    title = f"🔴 {metric_id} FAIL: {value} (порог: {threshold})"
    body = f"Метрика {metric_id} не прошла проверку..."
    gh_api_create_issue(title=title, body=body, labels=["bug", metric_id.lower(), "auto-generated"])
```

**F89: доля_задач_выполненных_через_Issues ≥ 0.80**
- Проверяет: ≥80% коммитов содержат `closes #N` или `fixes #N`
- Алгоритм: `git log --oneline | grep -c "closes #\\|fixes #"` / `git log --oneline | wc -l`

### §9.9 Авто-создание Issues при FAIL (v9.30 НОВОЕ)

> При любой F-метрике FAIL → автоматически создаётся Issue с меткой `bug`.

**Метрики, создающие Issues:**

| Метрика | Метка Issue | Когда |
|---|---|---|
| F4 (path-type-status) | `bug`, `f4` | pre-commit-hook.py |
| F31 (баланс массы) | `bug`, `f31` | pipeline.py |
| F70g (schema presence) | `bug`, `f70g` | pre-commit-hook.py |
| F70h (enum validation) | `bug`, `f70h` | pre-commit-hook.py |
| F81 (чистота пром) | `bug`, `f81` | pre-commit-hook.py |
| F86 (полнота подсистем) | `audit`, `f86` | check_model_completeness.py |
| F87 (статус_реальности) | `bug`, `f87` | pre-commit-hook.py |
| F88 (смешение материалов) | `bug`, `f88` | pre-commit-hook.py |

"""
assert S10_HEADER in text
text = text.replace(S10_HEADER, S9_8_BLOCK + S10_HEADER)
print("✓ §9.8 + §9.9 добавлены (Issues очередь + авто-создание)")

# ===== 6. §13.21 — F89 =====
S13_RESUME = "### §13.6 Резюме реестра (v9.16: сжато)"
F89_BLOCK = """### §13.21 Метрика v9.30 F89 (Issues integration)

> **v9.30 НОВОЕ:** 1 новая метрика.

| ID | Метрика | Порог | Исполнитель | Действие при FAIL |
|---|---|---|---|---|
| **F89** | доля_задач_выполненных_через_Issues | **≥0.80** | pipeline.py | warning (≥80% коммитов с `closes #N`) |

**Алгоритм:**
```python
def check_F89(repo_path):
    \"\"\"F89: >=80% коммитов ссылаются на Issues.\"\"\"
    import subprocess
    total = int(subprocess.check_output(
        ["git", "-C", repo_path, "rev-list", "--count", "HEAD"]
    ).strip())
    with_issues = int(subprocess.check_output(
        ["git", "-C", repo_path, "log", "--oneline", "--grep", "closes #"]
    ).strip().split("\\n").count("") - 1)
    # also check fixes #
    with_issues += int(subprocess.check_output(
        ["git", "-C", repo_path, "log", "--oneline", "--grep", "fixes #"]
    ).strip().split("\\n").count("") - 1)
    ratio = with_issues / max(1, total)
    return ratio >= 0.80, ratio
```

"""
assert S13_RESUME in text
text = text.replace(S13_RESUME, F89_BLOCK + S13_RESUME)
print("✓ §13.21 с F89 добавлен")

# ===== 7. §18.10 — P086 =====
S18_1_HEADER = "### §18.1 Требования v9.1-v9.13 (111-153) — см. §15 для полных текстов"
P086_BLOCK = """### §18.10 Требование v9.30 (168) — Issues как основа процесса

> **v9.30 НОВОЕ:** 1 новое требование (P086).

168. **Issues как основа процесса** (P086) — каждая задача = GitHub Issue; AI читает Issues, выполняет, закрывает; коммиты ссылаются на Issues (`closes #N`); F89 ≥ 0.80. См. §9.8, §9.9. При F-метрика FAIL → автоматически создаётся Issue с меткой `bug`.

"""
assert S18_1_HEADER in text
text = text.replace(S18_1_HEADER, P086_BLOCK + S18_1_HEADER)
print("✓ §18.10 с P086 добавлен")

# ===== 8. Обновить expected =====
text = text.replace(
    '"expected": "9.29",  # v9.29',
    '"expected": "9.30",  # v9.30'
)
text = text.replace(
    "5. Финальный коммит: `docs(результаты): финальная сводка SkyNet v9.29`.",
    "5. Финальный коммит: `docs(результаты): финальная сводка SkyNet v9.30`."
)
text = text.replace(
    "После создания скелета — **коммит инициализации**: `chore(скелет): SkyNet v9.29 + T-X гибридная + _decisions.log enforcement`.",
    "После создания скелета — **коммит инициализации**: `chore(скелет): SkyNet v9.30 + Issues integration (F89, P086)`."
)

# ===== 9. Сохранить =====
SRC.write_text(text, encoding="utf-8")
print(f"\nv9.30 готов: {len(text)} символов, {text.count(chr(10))+1} строк")
print(f"Δ от v9.29: {len(text) - 390896:+d} символов")

# Проверки
checks = [
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.30",
    "version: 9.30",
    "§9.8 Issues как очередь задач",
    "§9.9 Авто-создание Issues",
    "F89",
    "P086",
    "closes #N",
    "check_open_issues",
    "create_issue_for_failure",
    "§13.21",
    "§18.10",
    '"expected": "9.30"',
]
print("\n=== Проверка ===")
for c in checks:
    print(f"  {'✓' if c in text else '✗'} {c[:60]}")
