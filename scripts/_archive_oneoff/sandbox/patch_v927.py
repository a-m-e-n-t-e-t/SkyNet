#!/usr/bin/env python3
"""Patch v9.26 -> v9.27: F70h enum validation + improved YAML parsing + F81-F88 enforcement."""

from pathlib import Path

SRC = Path("/home/z/my-project/download/SkyNet_PROMPT_v9.27.md")
text = SRC.read_text(encoding="utf-8")

# ===== 1. ШАПКА =====
text = text.replace(
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.26",
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.27"
)
text = text.replace(
    '> **Версия:** 9.26\n> **Дата:** 2026-11-03\n> **Базируется на:** v9.25 + общее правило: schema-driven validation',
    '> **Версия:** 9.27\n> **Дата:** 2026-11-03\n> **Базируется на:** v9.26 + F70h enum validation + F81-F88 enforcement'
)
text = text.replace("  version: 9.26", "  version: 9.27")
text = text.replace("## 5 столпов архитектуры v9.26", "## 5 столпов архитектуры v9.27")

# ===== 2. CHANGELOG =====
old_end = """> 🔵 **СЖАТИЕ ПРОМПТА (унаследовано из v9.17/v9.19, Уровень 2):**"""
new_end = """> 🔴 **v9.27: ENUM VALIDATION + ENFORCEMENT**
>
> **Проблема v9.26:** F70g = 22/22 PASS — но это **ложноположительный** результат:
> - `тип_модели = combat_infiltrator` для ВСЕХ моделей (должно быть `гуманоидный`, `воздушный`, и т.д.)
> - `canon_with_real_analogue` не переименован в `canon_realizable`
> - `многослойная_броня` не найдена парсером как обязательная
> - F81-F88 функции существуют, но **не вызываются** в main()
>
> **Решение v9.27:**
>
> 1. **F70h (новая):** валидация enum-значений — не только наличие поля, но и что значение из допустимого списка
>    - `тип_модели` ∈ {гуманоидный, воздушный, наземный_гусеничный, наземный_колёсный, водный_надводный, водный_подводный, стационарный}
>    - `статус_реальности` ∈ {canon, canon_realizable, real}
>    - `подтип_модели` ∈ {стандартный, жидкий_металл, прочее} (опционально)
>
> 2. **Улучшенный парсинг схемы:** `read_required_fields_from_prompt()` использует `yaml.safe_load()` вместо regex
>
> 3. **F81-F88 enforcement:** функции вызываются в `pre-commit-hook.py main()`
>
> 📊 **ИТОГО v9.27:**
>
> | Метрика | v9.26 | v9.27 | Δ |
> |---|---:|---:|---|
> | Принципов | 81 | 82 | +1 (P082) |
> | Метрик | 134 | 135 | +1 (F70h) |
>
> 🔵 **СЖАТИЕ ПРОМПТА (унаследовано из v9.17/v9.19, Уровень 2):**"""
assert old_end in text
text = text.replace(old_end, new_end)
print("✓ Шапка + changelog обновлены")

# ===== 3. §0.2 — ENUM VALIDATION =====
S0_1_END = "## §0. CRITICAL: SKYNET REPO STATE CHECK"
S0_2_BLOCK = """## §0.2 ENUM VALIDATION (v9.27 НОВОЕ)

> **Урок из v9.26:** F70g проверяла НАЛИЧИЕ полей — AI добавил `тип_модели: combat_infiltrator` (поле есть!), но значение НЕ из enum §11.0.1. F70g дала ложноположительный PASS.

**Правило (P082):** Определённые поля имеют фиксированный набор допустимых значений (enum). Валидация проверяет не только наличие, но и соответствие значения enum.

**Поля с enum-валидацией:**

| Поле | Схема | Enum (допустимые значения) | Метрика |
|---|---|---|---|
| `тип_модели` | §12.4 | гуманоидный, воздушный, наземный_гусеничный, наземный_колёсный, водный_надводный, водный_подводный, стационарный | F70h |
| `статус_реальности` | §12.1-§12.5 | canon, canon_realizable, real | F70h |
| `подтип_модели` | §12.4 | стандартный, жидкий_металл (опционально — если есть, проверяется) | F70h |
| `кристаллическая_структура` | §12.3 | монокристаллический, поликристаллический, аморфный, композиционный, не_определён | F70h |

**Алгоритм:**
```python
ENUM_VALUES = {
    'тип_модели': ['гуманоидный', 'воздушный', 'наземный_гусеничный',
                   'наземный_колёсный', 'водный_надводный',
                   'водный_подводный', 'стационарный', 'прочее'],
    'статус_реальности': ['canon', 'canon_realizable', 'real'],
    'подтип_модели': ['стандартный', 'жидкий_металл', 'прочее'],
    'кристаллическая_структура': ['монокристаллический', 'поликристаллический',
                                   'аморфный', 'композиционный', 'не_определён'],
}

def check_F70h(filepath):
    \"\"\"F70h: валидация enum-значений.\"\"\"
    yaml_data = read_yaml_frontmatter(filepath)
    violations = []
    for field, allowed in ENUM_VALUES.items():
        val = yaml_data.get(field)
        if val and val not in allowed:
            violations.append(f"{field}='{val}' не из enum {allowed}")
    return violations
```

**Примеры:**
- `тип_модели: combat_infiltrator` → ❌ FAIL (нет в enum)
- `тип_модели: гуманоидный` → ✅ PASS
- `статус_реальности: canon_with_real_analogue` → ❌ FAIL (нет в enum, должно быть canon_realizable)
- `статус_реальности: canon_realizable` → ✅ PASS

"""

assert S0_1_END in text
text = text.replace(S0_1_END, S0_2_BLOCK + S0_1_END)
print("✓ §0.2 добавлен (enum validation)")

# ===== 4. §13.18 — F70h =====
S13_RESUME = "### §13.6 Резюме реестра (v9.16: сжато)"
F70H_BLOCK = """### §13.18 Метрика v9.27 F70h (enum validation)

> **v9.27 НОВОЕ:** 1 новая метрика. Валидация enum-значений — не только наличие поля, но и соответствие значения допустимому списку.

| ID | Метрика | Порог | Исполнитель | Действие при FAIL |
|---|---|---|---|---|
| **F70h** | доля_файлов_с_enum_валидными_значениями | **=1.00** | pre-commit-hook.py | **БЛОКИРОВКА** (значение поля не из enum §0.2) |

**Поля с enum:**

| Поле | Enum | Источник |
|---|---|---|
| `тип_модели` | 7 типов + прочее | §11.0.1 |
| `статус_реальности` | canon, canon_realizable, real | §12.1-§12.5 |
| `подтип_модели` | стандартный, жидкий_металл | §12.4 (опционально) |
| `кристаллическая_структура` | 5 значений | §12.3 |

**Алгоритм:**
```python
def check_F70h(repo_path):
    ENUM = {
        'тип_модели': {'гуманоидный', 'воздушный', 'наземный_гусеничный',
                        'наземный_колёсный', 'водный_надводный',
                        'водный_подводный', 'стационарный', 'прочее'},
        'статус_реальности': {'canon', 'canon_realizable', 'real'},
        'подтип_модели': {'стандартный', 'жидкий_металл', 'прочее'},
    }
    total = 0; valid = 0; violations = []
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in ['.git', '.cache', '__pycache__']]
        for f in files:
            if not f.endswith('.md') or f.startswith('_'):
                continue
            filepath = os.path.join(root, f)
            yaml_data = read_yaml_frontmatter(filepath)
            if not yaml_data or 'тип' not in yaml_data:
                continue
            total += 1
            file_ok = True
            for field, allowed in ENUM.items():
                val = yaml_data.get(field)
                if val and val not in allowed:
                    violations.append(f"{filepath}: {field}='{val}' не из enum")
                    file_ok = False
            if file_ok:
                valid += 1
    ratio = valid / max(1, total)
    return {'total': total, 'valid': valid, 'ratio': ratio,
            'pass': ratio >= 1.0, 'violations': violations}
```

"""
assert S13_RESUME in text
text = text.replace(S13_RESUME, F70H_BLOCK + S13_RESUME)
print("✓ §13.18 с F70h добавлен")

# ===== 5. §18.7 — P082 =====
S18_1_HEADER = "### §18.1 Требования v9.1-v9.13 (111-153) — см. §15 для полных текстов"
P082_BLOCK = """### §18.7 Требование v9.27 (164) — enum validation

> **v9.27 НОВОЕ:** 1 новое требование (P082).

164. **Enum validation** (P082) — определённые поля (`тип_модели`, `статус_реальности`, `подтип_модели`, `кристаллическая_структура`) имеют фиксированный набор допустимых значений; F70h = 1.0 БЛОКИРОВКА. См. §0.2. Урок из v9.26: `тип_модели: combat_infiltrator` (не из enum) — F70g дала ложноположительный PASS, потому что проверяла только наличие поля, а не значение.

"""
assert S18_1_HEADER in text
text = text.replace(S18_1_HEADER, P082_BLOCK + S18_1_HEADER)
print("✓ §18.7 с P082 добавлен")

# ===== 6. Обновить expected =====
text = text.replace(
    '"expected": "9.26",  # v9.26',
    '"expected": "9.27",  # v9.27'
)
text = text.replace(
    "5. Финальный коммит: `docs(результаты): финальная сводка SkyNet v9.26`.",
    "5. Финальный коммит: `docs(результаты): финальная сводка SkyNet v9.27`."
)
text = text.replace(
    "После создания скелета — **коммит инициализации**: `chore(скелет): SkyNet v9.26 + schema-driven validation (F70g, P081)`.",
    "После создания скелета — **коммит инициализации**: `chore(скелет): SkyNet v9.27 + F70h enum validation + F81-F88 enforcement`."
)

# ===== 7. Сохранить =====
SRC.write_text(text, encoding="utf-8")
print(f"\nv9.27 готов: {len(text)} символов, {text.count(chr(10))+1} строк")

# Проверки
checks = [
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.27",
    "version: 9.27",
    "§0.2 ENUM VALIDATION",
    "F70h",
    "P082",
    "§13.18",
    "§18.7",
    '"expected": "9.27"',
]
print("\n=== Проверка ===")
for c in checks:
    print(f"  {'✓' if c in text else '✗'} {c[:60]}")
