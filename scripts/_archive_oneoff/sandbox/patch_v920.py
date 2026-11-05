#!/usr/bin/env python3
"""
Patch v9.19 -> v9.20.
9 точечных исправлений согласно аудиту SkyNet_PROMPT_v9.19_AUDIT_WORKFLOWS.md
"""

import re
from pathlib import Path

SRC = Path("/home/z/my-project/download/SkyNet_PROMPT_v9.20.md")
text = SRC.read_text(encoding="utf-8")
orig_len = len(text)

# ===== ИСПРАВЛЕНИЕ 1: Заголовок v9.17 -> v9.20 =====
text = text.replace(
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.17",
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.20"
)

old_header_block = """> **Ключевые изменения v9.17 (поверх v9.16):**
>
> 🔴 **СЖАТИЕ ПРОМПТА БЕЗ ПОТЕРИ ДАННЫХ (Уровень 2):**
>
> Промпт сжат с **8881 до ~5888 строк (-34%)** через вынос в 4 отдельных файла:"""

new_header_block = """> **Ключевые изменения v9.20 (поверх v9.19):**
>
> 🔴 **АУДИТ v9.19 + ВНЕДРЕНИЕ WORKFLOWS:**
>
> На основе аудита `SkyNet_PROMPT_v9.19_AUDIT_WORKFLOWS.md` исправлено 9 багов:
> 1. Заголовок и YAML `agent.version` синхронизированы с фактической версией (v9.20)
> 2. Добавлен §0 «CRITICAL: SkyNet repo state check» — первый раздел, ДО §1
> 3. §17 Этап 0.5 помечен как обязательный шаг 0 (не fallback)
> 4. §9 Phase 5: добавлена альтернатива — GitHub Actions `pre-commit-checks.yml` на push
> 5. §9.0 AI-46: добавлено исключение «критические блокеры требуют уточнения»
> 6. Alice assets вынесены в `требования к ии/_alice_assets.yaml` (ссылка в 4 местах)
> 7. §19: `${SKYNET_REPO}` -> `os.environ.get("SKYNET_REPO", ...)`
> 8. §13 M37: добавлен триггер «GitHub Actions cron каждые 5 мин»
> 9. §1: `file_system` — путь определяется environment variable
>
> 🟢 **WORKFLOWS (впервые):**
>
> Добавлены 6 workflow-файлов в `.github/workflows/`:
> - `phase0-init.yml` — Phase 0 PAT-валидация + sync
> - `pre-commit-checks.yml` — 49 F-метрик на push/PR
> - `batch-process.yml` — §9.1 batch processing каждые 6 часов
> - `sync-check.yml` — F47 GitHub sync verification
> - `telemetry-update.yml` — M37 telemetry каждые 5 мин
> - `sync-alice-concepts.yml` — §17 Этап 0.6 weekly sync концепций
>
> 🔵 **СЖАТИЕ ПРОМПТА (унаследовано из v9.17/v9.19, Уровень 2):**
>
> Промпт сжат с **8881 до ~5888 строк (-34%)** через вынос в 4 отдельных файла:"""

assert old_header_block in text, "Не найден блок 'Ключевые изменения v9.17'"
text = text.replace(old_header_block, new_header_block)

text = text.replace(
    "## 5 столпов архитектуры v9.17",
    "## 5 столпов архитектуры v9.20"
)

text = text.replace(
    "agent:\n  name: SkyNet_engineer\n  version: 9.17",
    "agent:\n  name: SkyNet_engineer\n  version: 9.20"
)

# ===== ИСПРАВЛЕНИЕ 9: §1 file_system — path from env =====
text = text.replace(
    "    file_system: ${WORK_DIR}/  # v9.14: рабочая директория (по умолчанию /home/z/my-project/)",
    "    file_system: ${WORK_DIR}/  # v9.20: path from environment; sandbox=/home/z/my-project, GitHub Actions runner=/home/runner/work/SkyNet/SkyNet"
)

# ===== ИСПРАВЛЕНИЕ 6: Alice assets в _alice_assets.yaml =====
ALICE_LONG = "43 HTML + 143 файла (~120 уникальных версий схем + 19 дубликатов + 4 спец-версии + 2 файла-оболочки archive_empty/archive_shell)"
ALICE_SHORT = "43 HTML + 143 файла (см. `требования к ии/_alice_assets.yaml`)"
count_before = text.count(ALICE_LONG)
text = text.replace(ALICE_LONG, ALICE_SHORT)
ALICE_LONG_V2 = "(43 HTML + 143 файла (~120 уникальных версий схем + 19 дубликатов + 4 спец-версии + 2 файла-оболочки archive_empty/archive_shell))"
ALICE_SHORT_V2 = "(43 HTML + 143 файла — см. `требования к ии/_alice_assets.yaml`)"
text = text.replace(ALICE_LONG_V2, ALICE_SHORT_V2)

# ===== ИСПРАВЛЕНИЕ 5: §9.0 AI-46 — исключение для критических блокеров =====
AI46_OLD = """**Правило AI-46 (запрет уточнений):** Все параметры — по умолчанию. Если параметр неизвестен:
1. Веб-поиск
2. Расчёт
3. Пропорциональная генерация (для однотипных)
4. Пометка [требует верификации] + запись в результаты/_требуют_верификации.md"""

AI46_NEW = """**Правило AI-46 (запрет уточнений):** Все параметры — по умолчанию. Если параметр неизвестен:
1. Веб-поиск
2. Расчёт
3. Пропорциональная генерация (для однотипных)
4. Пометка [требует верификации] + запись в результаты/_требуют_верификации.md

**v9.20: ИСКЛЮЧЕНИЕ для критических блокеров:**
AI-46 НЕ применяется к критическим блокерам. В этих случаях AI ОБЯЗАН запросить уточнение у пользователя — это обработка форс-мажора, не нарушение AI-46:
- PAT недействителен (после 3 попыток скачивания с Яндекс.Диска)
- SkyNet репозиторий недоступен (404/403 после 3 попыток)
- Яндекс.Диск недоступен (для PAT и для концепций Alice)
- Конфликт schema↔archive, который нельзя разрешить автоматически

Критические блокеры логируются в `результаты/_decisions.log` с пометкой `force_majeure: true` перед запросом уточнения."""

assert AI46_OLD in text, "Не найден блок AI-46"
text = text.replace(AI46_OLD, AI46_NEW)

# ===== ИСПРАВЛЕНИЕ 7: §19 — ${SKYNET_REPO} -> os.environ.get =====
state_check_pattern = re.compile(
    r'(def check_current_state\(\) -> dict:\n.*?return \{[\s\S]*?\n    \})',
    re.MULTILINE
)
match = state_check_pattern.search(text)
if match:
    block = match.group(1)
    # Простая замена: обернуть все os.path.exists("${SKYNET_REPO}/...") в f-строку
    new_block = block.replace(
        'os.path.exists("${SKYNET_REPO}/',
        'os.path.exists(f"{SKYNET_REPO}/'
    )
    # Заменить ${SKYNET_REPO} внутри f-строк — нужно убрать $
    new_block = new_block.replace('{SKYNET_REPO}/', '{SKYNET_REPO}/')  # no-op
    # Фактически os.path.exists("${SKYNET_REPO}/.git") → os.path.exists(f"{SKYNET_REPO}/.git")
    # Это валидный Python: f"{SKYNET_REPO}/.git" использует переменную SKYNET_REPO
    # Но SKYNET_REPO должна быть определена — добавим импорт в начале функции
    new_block = new_block.replace(
        'def check_current_state() -> dict:\n    """Проверка фактического состояния перед запуском pipeline."""\n    return {',
        'def check_current_state() -> dict:\n    """Проверка фактического состояния перед запуском pipeline."""\n    import os\n    SKYNET_REPO = os.environ.get("SKYNET_REPO", "/home/z/my-project/SkyNet")  # v9.20: env var\n    return {'
    )
    # Теперь нужно убедиться что f-строки корректны: было os.path.exists("${SKYNET_REPO}/.git") 
    # стало os.path.exists(f"{SKYNET_REPO}/.git") — синтаксис валиден, но нужно закрыть f-string }
    # После нашей замены: os.path.exists(f"{SKYNET_REPO}/.git") — это валидная f-string с одной {}
    # Однако мы заменили "${SKYNET_REPO}/ на f"{SKYNET_REPO}/ — закрывающая скобка } осталась после .git
    # Проверим: оригинал os.path.exists("${SKYNET_REPO}/.git") 
    #          после     os.path.exists(f"{SKYNET_REPO}/.git")  ← валидно, f-string завершена "
    # Да, валидно, если в исходной строке ${SKYNET_REPO}/.git" — кавычка закрывает f-string
    # Также read_yaml_safe, is_repo_empty, и т.д.
    new_block = new_block.replace(
        'is_repo_empty("${SKYNET_REPO}',
        'is_repo_empty(f"{SKYNET_REPO}'
    )
    new_block = new_block.replace(
        'git_log_count("${SKYNET_REPO}',
        'git_log_count(f"{SKYNET_REPO}'
    )
    new_block = new_block.replace(
        'count_files("${SKYNET_REPO}',
        'count_files(f"{SKYNET_REPO}'
    )
    new_block = new_block.replace(
        'read_yaml_safe("${SKYNET_REPO}',
        'read_yaml_safe(f"{SKYNET_REPO}'
    )
    new_block = new_block.replace(
        'len(glob.glob("${SKYNET_REPO}/',
        'len(glob.glob(f"{SKYNET_REPO}/'
    )
    # Также обрабатываем os.path.exists с многострочным вариантом
    new_block = new_block.replace(
        'os.path.exists(\n                "${SKYNET_REPO}/',
        'os.path.exists(\n                f"{SKYNET_REPO}/'
    )
    new_block = new_block.replace(
        'os.path.exists(\n            "${SKYNET_REPO}/',
        'os.path.exists(\n            f"{SKYNET_REPO}/'
    )
    
    text = text.replace(block, new_block)

# ===== ИСПРАВЛЕНИЕ 8: §13 M37 — триггер GitHub Actions cron =====
M37_OLD = "| M37 | telemetry_freshness_min | ≤5 | pipeline.py | **не проверяется** при неактивной сессии |"
M37_NEW = "| M37 | telemetry_freshness_min | ≤5 | pipeline.py + GitHub Actions cron `*/5 * * * *` | **v9.20:** проверяется GitHub Actions workflow `telemetry-update.yml` каждые 5 минут; при `last_telemetry_update > 5 min` создаётся ISSUE в репо с меткой `stale-telemetry` |"

assert M37_OLD in text, "Не найдена метрика M37"
text = text.replace(M37_OLD, M37_NEW)

# ===== ИСПРАВЛЕНИЕ 2: Добавить §0 перед §A =====
S0_INSERT = """# LAYER 1 — ОСНОВНОЙ ПРОМПТ

## §0. CRITICAL: SKYNET REPO STATE CHECK (v9.20 — обязательный первый шаг)

> **v9.20 НОВОЕ:** Перед любым действием AI ОБЯЗАН проверить фактическое состояние SkyNet через GitHub Contents API. Если репо пуст или не содержит скелета v9.20 → **Этап 0.5 §17 — обязательный шаг 0**, не fallback.

### §0.1 Что проверять (через GitHub REST API с PAT)

```python
def check_skynet_state(pat: str) -> dict:
    '''v9.20: Первая функция, вызывается ДО §1 download_pat и ДО §9 Phase 0.'''
    import urllib.request, urllib.error, json
    headers = {
        "Authorization": f"Bearer {pat}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    # 1. Проверить что SkyNet доступен
    req = urllib.request.Request(
        "https://api.github.com/repos/a-m-e-n-t-e-t/SkyNet",
        headers=headers,
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        repo = json.load(r)
    # 2. Проверить что .github/workflows/ существует (v9.20: индикатор скелета)
    has_workflows = False
    try:
        req2 = urllib.request.Request(
            "https://api.github.com/repos/a-m-e-n-t-e-t/SkyNet/contents/.github/workflows",
            headers=headers,
        )
        with urllib.request.urlopen(req2, timeout=10) as r2:
            workflows = json.load(r2)
        has_workflows = isinstance(workflows, list) and any(
            f.get("name", "").endswith(".yml") for f in workflows
        )
    except urllib.error.HTTPError:
        has_workflows = False
    # 3. Проверить scripts/pipeline.py
    has_pipeline = False
    try:
        req3 = urllib.request.Request(
            "https://api.github.com/repos/a-m-e-n-t-e-t/SkyNet/contents/scripts/pipeline.py",
            headers=headers,
        )
        with urllib.request.urlopen(req3, timeout=10) as r3:
            has_pipeline = r3.status == 200
    except urllib.error.HTTPError:
        has_pipeline = False
    return {
        "repo_accessible": repo.get("full_name") == "a-m-e-n-t-e-t/SkyNet",
        "is_empty": repo.get("size", 0) < 10,  # почти пустой
        "has_workflows_dir": has_workflows,
        "has_pipeline_py": has_pipeline,
        "needs_skeleton_init": not (has_workflows and has_pipeline),
    }
```

### §0.2 Решение по результатам проверки

| Состояние | Действие |
|---|---|
| `repo_accessible: true` AND `needs_skeleton_init: false` | ✅ Продолжить с §1 (нормальный запуск) |
| `repo_accessible: true` AND `needs_skeleton_init: true` | 🔴 **ОБЯЗАТЕЛЬНЫЙ Этап 0.5 §17** (создать скелет + 6 workflow-файлов) |
| `repo_accessible: false` | 🔴 Критический блокер (§16 Plan B: запросить у пользователя) — v9.20: не подпадает под AI-46 |

### §0.3 Связь с §19

`check_skynet_state()` — это **v9.20 упрощённая версия** `check_current_state()` из §19. Первая вызывается ДО загрузки SkyNet в sandbox (через Contents API); вторая — ПОСЛЕ локального git clone. Обе должны возвращать совместимые результаты.

"""

text = text.replace(
    "# LAYER 1 — ОСНОВНОЙ ПРОМПТ\n\n## §A. ОПЕРАЦИОННАЯ МОДЕЛЬ",
    S0_INSERT + "## §A. ОПЕРАЦИОННАЯ МОДЕЛЬ"
)

# ===== ИСПРАВЛЕНИЕ 3: §17 Этап 0.5 — пометить как обязательный =====
E05_OLD = """### Этап 0. Первичная инициализация (однократно, из пустого репо)

| Шаг | Статус | Детали |
|---|---|---|
| 0.1 Скачать PAT при первой сессии | ⚠️ | С Яндекс.Диска через REST API; локально НЕ сохраняется |
| 0.2 git clone SkyNet | ⚠️ | `${SKYNET_REPO}` — **пустой репозиторий, 0 коммитов** |
| 0.3 .gitignore SkyNet | ❌ | Требуется создать: `*.env`, `token*`, `.cache/`, `концепции/_semantic_cache.json` (v9.7: добавлен _semantic_cache.json) |
| 0.4 Создать структуру папок | ❌ | Все папки из §10 (включая подпапки подсистем в шаблоне) |
| 0.5 Создать scripts/pipeline.py + download_pat() | ❌ | Требуется создать |
| 0.6 Создать scripts/pre-commit-hook.py + path-type-status check | ❌ | Требуется создать |
| 0.7 Создать требования к ии/_принципы.md + _версия_правил.yaml + _классификация_подсистем.md | ❌ | Требуется создать |
| 0.8 Создать .gitignore, диалог/_counter.txt (init: 0) | ❌ | Требуется создать |
| 0.9 Коммит инициализации | ❌ | `chore(скелет): инициализация структуры SkyNet v9.19` |

**Этап 0.5 (первичная инициализация, v9.8 — детализировано):**"""

E05_NEW = """### Этап 0. Первичная инициализация (ОБЯЗАТЕЛЬНЫЙ ШАГ 0, не fallback — v9.20)

> **v9.20 ВАЖНО:** Ранее Этап 0 описывался как fallback для пустого репо. Это НЕправильно.
> §0 (v9.20) устанавливает, что любая новая сессия начинает с проверки `check_skynet_state()`.
> Если репо пустой или не содержит скелета v9.20 → Этап 0 — **обязательный**, не опциональный.
> Без него §9 Phase 0 упадёт на `pipeline.py exists?` → `False` → циклическая зависимость.

| Шаг | Статус | Детали |
|---|---|---|
| 0.1 Скачать PAT при первой сессии | ⚠️ | С Яндекс.Диска через REST API; локально НЕ сохраняется |
| 0.2 git clone SkyNet | ⚠️ | `${SKYNET_REPO}` — **пустой репозиторий, 0 коммитов** |
| 0.3 .gitignore SkyNet | ❌ | Требуется создать: `*.env`, `token*`, `.cache/`, `концепции/_semantic_cache.json` (v9.7: добавлен _semantic_cache.json) |
| 0.4 Создать структуру папок | ❌ | Все папки из §10 (включая подпапки подсистем в шаблоне) |
| 0.5 Создать scripts/pipeline.py + download_pat() | ❌ | Требуется создать |
| 0.6 Создать scripts/pre-commit-hook.py + path-type-status check | ❌ | Требуется создать |
| 0.7 Создать требования к ии/_принципы.md + _версия_правил.yaml + _классификация_подсистем.md + _alice_assets.yaml (v9.20) | ❌ | Требуется создать |
| 0.8 Создать .gitignore, диалог/_counter.txt (init: 0) | ❌ | Требуется создать |
| 0.9 **Создать `.github/workflows/` (6 файлов, v9.20 НОВОЕ)** | ❌ | `phase0-init.yml`, `pre-commit-checks.yml`, `batch-process.yml`, `sync-check.yml`, `telemetry-update.yml`, `sync-alice-concepts.yml` — см. Layer 3 §W (v9.20) |
| 0.10 Коммит инициализации | ❌ | `chore(скелет): инициализация структуры SkyNet v9.20 + Workflows` |

**Этап 0.5 (первичная инициализация, v9.8 — детализировано; v9.20 — обязательно):**"""

assert E05_OLD in text, "Не найден блок Этап 0"
text = text.replace(E05_OLD, E05_NEW)

# ===== ИСПРАВЛЕНИЕ 4: §9 Phase 5 — GitHub Actions alternative =====
PHASE5_OLD = """ФАЗА 5 — ТРАНЗАКЦИОННЫЕ ПРОВЕРКИ (APPLY → PROPAGATE → VERIFY)
  5.1 pre-commit hook: все метрики (см. §13 для актуального счёта)
  5.2 Path-Type-Status consistency check (§10.1)
  5.3 Если метрика < порога → БЛОКИРОВКА + диагностика
      - Запись в riss.json с указанием метрики, значения, порога, причины
  5.4 telemetry update
  5.5 Если FAIL → откат к checkpoint предыдущей успешной фазы
  → checkpoint phase_5.json"""

PHASE5_NEW = """ФАЗА 5 — ТРАНЗАКЦИОННЫЕ ПРОВЕРКИ (APPLY → PROPAGATE → VERIFY)
  5.1 pre-commit hook: все метрики (см. §13 для актуального счёта)
      v9.20: ДВА пути исполнения:
        (a) Локально (sandbox): python scripts/pre-commit-hook.py перед git commit
        (b) GitHub Actions: .github/workflows/pre-commit-checks.yml на push/pull_request
            — запускается ПОСЛЕ push, блокирует merge при FAIL (Branch Protection)
            — NB: Contents API push НЕ вызывает client-side hooks, поэтому (b) — основная защита
  5.2 Path-Type-Status consistency check (§10.1)
  5.3 Если метрика < порога → БЛОКИРОВКА + диагностика
      - Запись в riss.json с указанием метрики, значения, порога, причины
      - v9.20: при локальном FAIL → отменить коммит (git reset HEAD~1); при GitHub Actions FAIL → создать ISSUE с меткой `pre-commit-failed`
  5.4 telemetry update
  5.5 Если FAIL → откат к checkpoint предыдущей успешной фазы
  → checkpoint phase_5.json
  → v9.20: GitHub Actions workflow `pre-commit-checks.yml` автоматически сработает на push"""

assert PHASE5_OLD in text, "Не найден блок Phase 5"
text = text.replace(PHASE5_OLD, PHASE5_NEW)

# ===== Запись результата =====
SRC.write_text(text, encoding="utf-8")
new_len = len(text)
diff = new_len - orig_len
print(f"v9.20 готов: {new_len} символов (Δ {diff:+d} от v9.19)")
print(f"Строк: {text.count(chr(10)) + 1}")

# Проверки замен
checks = [
    ("# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.20", "Заголовок v9.20"),
    ("version: 9.20", "YAML agent.version 9.20"),
    ("5 столпов архитектуры v9.20", "5 столпов v9.20"),
    ("v9.20: path from environment", "§1 file_system env"),
    ("ИСКЛЮЧЕНИЕ для критических блокеров", "AI-46 исключение"),
    ("check_skynet_state(pat: str)", "§0 check_skynet_state"),
    ("ОБЯЗАТЕЛЬНЫЙ ШАГ 0", "§17 Этап 0 обязательный"),
    ("v9.20: ДВА пути исполнения", "Phase 5 два пути"),
    ("telemetry-update.yml каждые 5 минут", "M37 cron триггер"),
    ("_alice_assets.yaml", "Alice assets вынесены"),
    ("os.environ.get(\"SKYNET_REPO\"", "§19 env var"),
]
print("\n=== Проверка применённых исправлений ===")
for needle, desc in checks:
    ok = "✓" if needle in text else "✗"
    print(f"  {ok} {desc}: '{needle[:60]}'")

alice_replaced = count_before
print(f"\n=== Alice assets: заменено {alice_replaced} вхождений длинной формы ===")
