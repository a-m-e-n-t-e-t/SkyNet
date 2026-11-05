#!/usr/bin/env python3
"""Patch v9.28 -> v9.29: T-X гибридная (liquid metal = маскировка, не броня) + _decisions.log enforcement."""

from pathlib import Path

SRC = Path("/home/z/my-project/download/SkyNet_PROMPT_v9.29.md")
text = SRC.read_text(encoding="utf-8")

# ===== 1. ШАПКА =====
text = text.replace(
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.28",
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.29"
)
text = text.replace(
    '> **Версия:** 9.28\n> **Дата:** 2026-11-03\n> **Базируется на:** v9.27 + обязательный run_all_checks + усиление декомпозиции + многослойная_броня в схеме',
    '> **Версия:** 9.29\n> **Дата:** 2026-11-03\n> **Базируется на:** v9.28 + T-X гибридная (liquid metal = маскировка) + _decisions.log enforcement'
)
text = text.replace("  version: 9.28", "  version: 9.29")
text = text.replace("## 5 столпов архитектуры v9.28", "## 5 столпов архитектуры v9.29")

# ===== 2. CHANGELOG =====
old_end = """> 🔵 **СЖАТИЕ ПРОМПТА (унаследовано из v9.17/v9.19, Уровень 2):**"""
new_end = """> 🔴 **v9.29: T-X ГИБРИДНАЯ + _decisions.log ENFORCEMENT**
>
> **Проблема v9.28:** 2 проблемы остались:
> 1. T-X `подтип_модели: жидкий_металл` — неправильно. T-X имеет endoskeleton (T-900) + liquid metal coating. Liquid metal = **маскировка** (shapeshifting), не замена брони. T-X нуждается во всех подсистемах.
> 2. `_decisions.log` отсутствует — P037 нарушен (AI не вёл audit log)
>
> **Решение v9.29:**
>
> 1. **`гибридная` — новый подтип (T-X):**
>    - 0 exempted подсистем (все обязательны)
>    - `многослойная_броня` обяз (F71) — броня есть
>    - `маскировка` обяз (F13) — liquid metal coating = shapeshifting
>    - Добавлена в ENUM_VALUES `подтип_модели`
>
> 2. **_decisions.log enforcement (P084, F70j):**
>    - §5 усилено: AI ОБЯЗАН создать `результаты/_decisions.log` при первой записи
>    - F70j: `доля_сессий_с_записями_в_decisions_log` = 1.0 БЛОКИРОВКА
>    - Проверяет: файл существует и содержит ≥1 запись
>
> 📊 **ИТОГО v9.29:**
>
> | Метрика | v9.28 | v9.29 | Δ |
> |---|---:|---:|---|
> | Принципов | 83 | 85 | +2 (P084, P085) |
> | Метрик | 136 | 138 | +2 (F70j, F90) |
>
> 🔵 **СЖАТИЕ ПРОМПТА (унаследовано из v9.17/v9.19, Уровень 2):**"""
assert old_end in text
text = text.replace(old_end, new_end)
print("✓ Шапка + changelog обновлены")

# ===== 3. §11.0.3 — обновить правила подтипов =====
old_tx_rule = """6. **v9.28: T-X правило** — T-X (Terminatrix) имеет liquid metal coating → `подтип_модели: жидкий_металл` (как T-1000). T-X не exempted от каркаса (у неё есть endoskeleton), НО exempted от `броня` (liquid metal заменяет броню).
   - T-1000: `подтип_модели: жидкий_металл`, exempted: [каркас, броня, приводная_система, система_передвижения]
   - T-X: `подтип_модели: жидкий_металл`, exempted: [броня] (но НЕ каркас — у T-X есть endoskeleton)"""

new_tx_rule = """6. **v9.29: подтип_модели правила (обновлено):**
   - `стандартный` (T-600, T-800, HK-Aerial, HK-Tank): exempted: [] (все подсистемы обяз)
   - `жидкий_металл` (T-1000): exempted: [каркас, броня, приводная_система, система_передвижения, многослойная_броня] (полностью жидкий, нет endoskeleton)
   - `гибридная` (T-X): exempted: [] — **0 exempted!** T-X имеет endoskeleton T-900 + liquid metal coating (маскировка, не броня). Все подсистемы обязательны:
     - каркас: обяз (endoskeleton T-900)
     - броня: обяз (традиционная броня поверх endoskeleton)
     - многослойная_броня: обяз (F71)
     - маскировка: обяз (F13) — liquid metal coating = shapeshifting для инфильтрации
     - приводная_система: обяз (конечности)
     - система_передвижения: обяз (ходит ногами)

   **Liquid metal у T-X = маскировка, не броня.** T-X — полностью функциональная модель со всеми подсистемами."""

assert old_tx_rule in text
text = text.replace(old_tx_rule, new_tx_rule)
print("✓ §11.0.3 обновлён (гибридная: 0 exempted)")

# ===== 4. §0.2 — добавить гибридная в ENUM =====
old_enum = "    'подтип_модели': {'стандартный', 'жидкий_металл', 'прочее'},"
new_enum = "    'подтип_модели': {'стандартный', 'жидкий_металл', 'гибридная', 'прочее'},"
text = text.replace(old_enum, new_enum)
print("✓ §0.2 ENUM обновлён (гибридная)")

# ===== 5. §5 — усиление _decisions.log =====
old_s5 = "### §5. ПРОЗРАЧНОСТЬ РЕШЕНИЙ (audit log)"
new_s5 = """### §5. ПРОЗРАЧНОСТЬ РЕШЕНИЙ (audit log)

> **v9.29 ВАЖНО:** `_decisions.log` — ОБЯЗАТЕЛЬНЫЙ файл. F70j = 1.0 БЛОКИРОВКА. Если файл отсутствует или пустой при наличии коммитов → FAIL. Урок из v9.28: AI не создал _decisions.log — P037 нарушен."""

text = text.replace(old_s5, new_s5)
print("✓ §5 усилен (_decisions.log enforcement)")

# ===== 6. §13.20 — F70j + F90 =====
S13_RESUME = "### §13.6 Резюме реестра (v9.16: сжато)"
F70J_BLOCK = """### §13.20 Метрики v9.29 F70j + F90 (decisions.log + маскировка для гибридной)

> **v9.29 НОВОЕ:** 2 новые метрики.

| ID | Метрика | Порог | Исполнитель | Действие при FAIL |
|---|---|---|---|---|
| **F70j** | доля_сессий_с_записями_в_decisions_log | **=1.00** | pre-commit-hook.py | **БЛОКИРОВКА** (_decisions.log отсутствует или пустой при наличии коммитов) |
| **F90** | доля_гибридных_моделей_с_маскировкой | **=1.00** | pre-commit-hook.py | **БЛОКИРОВКА** (T-X с подтип_модели: гибридная не имеет блока маскировка) |

**Алгоритм F70j:**
```python
def check_F70j(repo_path):
    \"\"\"F70j: _decisions.log существует и содержит ≥1 запись.\"\"\"
    log_path = os.path.join(repo_path, "результаты", "_decisions.log")
    if not os.path.exists(log_path):
        return {'pass': False, 'reason': '_decisions.log не существует'}
    with open(log_path, 'r') as f:
        content = f.read().strip()
    if not content:
        return {'pass': False, 'reason': '_decisions.log пустой'}
    # Проверить что есть хотя бы 1 запись (строка с timestamp)
    if 'timestamp' not in content:
        return {'pass': False, 'reason': 'нет записей с timestamp'}
    return {'pass': True}
```

**Алгоритм F90:**
```python
def check_F90(models_dir):
    \"\"\"F90: гибридные модели имеют маскировку.\"\"\"
    violations = []
    for f in glob(f"{models_dir}/*.md"):
        yaml_data = read_yaml_frontmatter(f)
        if not yaml_data:
            continue
        podtip = yaml_data.get('подтип_модели', '')
        if podtip == 'гибридная':
            if 'маскировка' not in yaml_data:
                violations.append(f"{f}: гибридная без маскировки (liquid metal coating)")
    return violations
```

"""
assert S13_RESUME in text
text = text.replace(S13_RESUME, F70J_BLOCK + S13_RESUME)
print("✓ §13.20 с F70j + F90 добавлен")

# ===== 7. §18.9 — P084 + P085 =====
S18_1_HEADER = "### §18.1 Требования v9.1-v9.13 (111-153) — см. §15 для полных текстов"
P084_BLOCK = """### §18.9 Требования v9.29 (166-167) — _decisions.log + гибридная

> **v9.29 НОВОЕ:** 2 новых требования.

166. **_decisions.log обязательный** (P084) — AI обязан создать `результаты/_decisions.log` и вести его при каждом нетривиальном решении; F70j = 1.0 БЛОКИРОВКА. См. §5. Урок из v9.28: _decisions.log отсутствовал — P037 нарушен.

167. **Гибридная маскировка** (P085) — T-X с `подтип_модели: гибридная` обязан иметь блок `маскировка` (liquid metal coating = shapeshifting); F90 = 1.0 БЛОКИРОВКА. Liquid metal у гибридов = маскировка, не броня.

"""
assert S18_1_HEADER in text
text = text.replace(S18_1_HEADER, P084_BLOCK + S18_1_HEADER)
print("✓ §18.9 с P084 + P085 добавлен")

# ===== 8. Обновить expected =====
text = text.replace(
    '"expected": "9.28",  # v9.28',
    '"expected": "9.29",  # v9.29'
)
text = text.replace(
    "5. Финальный коммит: `docs(результаты): финальная сводка SkyNet v9.28`.",
    "5. Финальный коммит: `docs(результаты): финальная сводка SkyNet v9.29`."
)
text = text.replace(
    "После создания скелета — **коммит инициализации**: `chore(скелет): SkyNet v9.28 + run_all_checks enforcement + декомпозиция + многослойная_броня`.",
    "После создания скелета — **коммит инициализации**: `chore(скелет): SkyNet v9.29 + T-X гибридная + _decisions.log enforcement`."
)

# ===== 9. Сохранить =====
SRC.write_text(text, encoding="utf-8")
print(f"\nv9.29 готов: {len(text)} символов, {text.count(chr(10))+1} строк")
print(f"Δ от v9.28: {len(text) - 386937:+d} символов")

# Проверки
checks = [
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.29",
    "version: 9.29",
    "гибридная",
    "Liquid metal у T-X = маскировка, не броня",
    "F70j",
    "F90",
    "P084",
    "P085",
    "§13.20",
    "§18.9",
    '"expected": "9.29"',
]
print("\n=== Проверка ===")
for c in checks:
    print(f"  {'✓' if c in text else '✗'} {c[:60]}")
