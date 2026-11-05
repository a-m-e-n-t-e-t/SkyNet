#!/usr/bin/env python3
"""Patch v9.25 -> v9.26: schema-driven validation (общее правило)."""

from pathlib import Path

SRC = Path("/home/z/my-project/download/SkyNet_PROMPT_v9.26.md")
text = SRC.read_text(encoding="utf-8")

# ===== 1. ШАПКА =====
text = text.replace(
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.25",
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.26"
)
text = text.replace(
    '> **Версия:** 9.25\n> **Дата:** 2026-11-03\n> **Базируется на:** v9.24 + уточнение структуры папок + разделение galinstan/mimetic_polyalloy',
    '> **Версия:** 9.26\n> **Дата:** 2026-11-03\n> **Базируется на:** v9.25 + общее правило: schema-driven validation'
)
text = text.replace("  version: 9.25", "  version: 9.26")
text = text.replace("## 5 столпов архитектуры v9.25", "## 5 столпов архитектуры v9.26")

# ===== 2. CHANGELOG =====
old_end = """> 🔵 **СЖАТИЕ ПРОМПТА (унаследовано из v9.17/v9.19, Уровень 2):**"""
new_end = """> 🔴 **ОБЩЕЕ ПРАВИЛО v9.26: SCHEMA-DRIVEN VALIDATION**
>
> **Проблема:** В v9.22 добавили `тип_модели`, в v9.24 — `canon_realizable`, в v9.25 — `вдохновлён_реальным`. Но `pre-commit-hook.py` проверял hardcoded список полей и не знал о новых. AI не добавлял новые поля — и скрипт не ловил это.
>
> **Урок из реализации v9.25:** 9 из 18 проверок FAIL. Причина: AI не добавил `тип_модели`, `canon_realizable`, `многослойная_броню` — потому что скрипт их не проверял.
>
> **Решение (общее, не конкретное):**
>
> `pre-commit-hook.py` динамически читает схему §12.X из промпта и валидирует ВСЕ обязательные поля, определённые в схеме — а не hardcoded список.
>
> ```python
> # Было (конкретное, v9.25):
> if not yaml_data.get('тип_модели'):
>     violations.append("нет тип_модели")
> # Каждое новое поле — ручное обновление скрипта
>
> # Стало (общее, v9.26):
> schema = read_required_fields_from_prompt("§12.4")
> for field in schema.required_fields:
>     if field not in yaml_data:
>         violations.append(f"отсутствует: {field}")
> # Новое поле в схеме → автоматически проверяется
> ```
>
> Это устраняет класс проблем: «AI не добавил поле, потому что скрипт его не проверял».
> Новое поле в §12.X → автоматически валидируется без обновления скрипта.
>
> **Реализация:**
> - `_helpers.py::read_required_fields_from_prompt()` — читает промпт, извлекает обязательные поля
> - `pre-commit-hook.py::validate_against_schema()` — валидирует файл против схемы
> - F70g: `доля_файлов_со_всеми_обязательными_полями_схемы` = 1.0 БЛОКИРОВКА
>
> 📊 **ИТОГО v9.26:**
>
> | Метрика | v9.25 | v9.26 | Δ |
> |---|---:|---:|---|
> | Принципов | 80 | 81 | +1 (P081) |
> | Метрик | 133 | 134 | +1 (F70g) |
>
> 🔵 **СЖАТИЕ ПРОМПТА (унаследовано из v9.17/v9.19, Уровень 2):**"""
assert old_end in text
text = text.replace(old_end, new_end)
print("✓ Шапка + changelog обновлены")

# ===== 3. §0.1 — Общее правило: schema-driven validation =====
S0_HEADER = "## §0. CRITICAL: SKYNET REPO STATE CHECK"
S0_1_BLOCK = """## §0.1 ОБЩЕЕ ПРАВИЛО: SCHEMA-DRIVEN VALIDATION (v9.26 НОВОЕ)

> **Принцип:** Промпт — это source of truth. Скрипты не должны hardcoded-ить конкретные поля. Они должны динамически читать схему из промпта и валидировать все обязательные поля.

**Правило (P081):** Для каждого файла с YAML frontmatter, `pre-commit-hook.py` динамически определяет обязательные поля, читая соответствующую схему из промпта (§12.1-§12.5), и проверяет что ВСЕ обязательные поля присутствуют и заполнены.

**Алгоритм:**
```python
def validate_against_schema(filepath, prompt_path):
    \"\"\"Общее правило: валидация файла против схемы из промпта.\"\"\"
    yaml_data = read_yaml_frontmatter(filepath)
    if not yaml_data:
        return []  # нет YAML — нет проверки

    тип = yaml_data.get('тип', '')
    # Определить какая схема применяется
    if тип == 'модель_SkyNet':
        schema_section = '§12.4'
    elif тип == 'изделие':
        schema_section = '§12.1'
    elif тип == 'материал':
        schema_section = '§12.3'
    elif тип == 'технология':
        schema_section = '§12.2'
    else:
        return []  # неизвестный тип — пропустить

    # Динамически читать обязательные поля из промпта
    required = read_required_fields_from_prompt(prompt_path, schema_section)
    missing = [f for f in required if f not in yaml_data or not yaml_data[f]]
    return missing
```

**`read_required_fields_from_prompt()` — как работает:**

1. Читает `требования к ии/SkyNet_PROMPT_v9.26.md`
2. Находит секцию `§12.4` (или §12.1, §12.2, §12.3)
3. Парсит YAML-схему из секции
4. Извлекает поля с пометкой `required: true` или без `optional: true`
5. Возвращает список обязательных полей

**Это гарантирует:**
- Новое поле добавлено в §12.X → автоматически проверяется
- Никакого hardcoded списка полей в скриптах
- AI не может «забыть» поле — скрипт проверяет все

**F70g (новая подметрика F70):**
- `доля_файлов_со_всеми_обязательными_полями_схемы` = 1.0 БЛОКИРОВКА
- Для каждого файла: `validate_against_schema()` → если missing → FAIL

**Урок из v9.25:** 9 из 18 проверок FAIL. Причина: AI не добавил `тип_модели`, `canon_realizable`, `многослойная_броню` — потому что скрипт их не проверял. С общим правилом это невозможно.

"""

assert S0_HEADER in text
text = text.replace(S0_HEADER, S0_1_BLOCK + S0_HEADER)
print("✓ §0.1 добавлен (schema-driven validation)")

# ===== 4. Расширить F70 — добавить F70g =====
# Найти где F70 описана и добавить F70g
old_f70_text = "Интегрируется в `pre-commit-hook.py` через `validate_field_contracts.py`."
new_f70_text = """Интегрируется в `pre-commit-hook.py` через `validate_field_contracts.py`.

**F70g (v9.26 НОВОЕ): доля_файлов_со_всеми_обязательными_полями_схемы = 1.0 БЛОКИРОВКА**

> **Общее правило (P081):** скрипт динамически читает схему из промпта и валидирует все обязательные поля.
> Новое поле в §12.X → автоматически проверяется. Никакого hardcoded списка.

| Подметрика | Что проверяет | Алгоритм |
|---|---|---|
| **F70g** | Все файлы имеют обязательные поля своей схемы | `validate_against_schema()` для каждого файла; `read_required_fields_from_prompt()` извлекает обязательные поля из промпта |

Алгоритм:
```python
def check_F70g(repo):
    \"\"\"Доля файлов со всеми обязательными полями схемы.\"\"\"
    prompt_path = f"{repo}/требования к ии/SkyNet_PROMPT_v9.26.md"
    total = 0
    valid = 0
    for root, dirs, files in os.walk(repo):
        for f in files:
            if not f.endswith('.md'):
                continue
            filepath = os.path.join(root, f)
            yaml_data = read_yaml_frontmatter(filepath)
            if not yaml_data or 'тип' not in yaml_data:
                continue  # нет типа — не проверяем
            total += 1
            missing = validate_against_schema(filepath, prompt_path)
            if not missing:
                valid += 1
    return valid / max(1, total)
```"""

text = text.replace(old_f70_text, new_f70_text)
print("✓ F70g добавлена (schema-driven validation)")

# ===== 5. §13.17 — F70g =====
S13_RESUME = "### §13.6 Резюме реестра (v9.16: сжато)"
F70G_BLOCK = """### §13.17 Метрика v9.26 F70g (schema-driven validation)

> **v9.26 НОВОЕ:** 1 новая подметрика. Общее правило: скрипт читает схему из промпта и валидирует все обязательные поля.

| ID | Метрика | Порог | Исполнитель | Действие при FAIL |
|---|---|---|---|---|
| **F70g** | доля_файлов_со_всеми_обязательными_полями_схемы | **=1.00** | pre-commit-hook.py | **БЛОКИРОВКА** (файл отсутствует обязательное поле из схемы §12.X) |

**Алгоритм:**
```python
def check_F70g(repo, prompt_path):
    \"\"\"F70g: все файлы имеют обязательные поля своей схемы.\"\"\"
    total = 0
    valid = 0
    for root, dirs, files in os.walk(repo):
        for f in files:
            if not f.endswith('.md'):
                continue
            filepath = os.path.join(root, f)
            yaml_data = read_yaml_frontmatter(filepath)
            if not yaml_data or 'тип' not in yaml_data:
                continue
            total += 1
            missing = validate_against_schema(filepath, prompt_path)
            if not missing:
                valid += 1
            else:
                print(f"  ✗ {filepath}: отсутствуют: {', '.join(missing)}")
    ratio = valid / max(1, total)
    return ratio >= 1.0, ratio
```

**Примеры:**
- Модель без `тип_модели` → ❌ FAIL (обязательное поле §12.4)
- Модель без `статус_реальности` → ❌ FAIL (обязательное поле §12.4)
- Материал без `кристаллическая_структура` → ❌ FAIL (обязательное поле §12.3)
- Модель со всеми полями §12.4 → ✅ PASS

**Преимущество:** когда в будущей версии добавят новое обязательное поле в §12.X, F70g автоматически начнёт его проверять — без обновления скрипта.

"""
assert S13_RESUME in text
text = text.replace(S13_RESUME, F70G_BLOCK + S13_RESUME)
print("✓ §13.17 с F70g добавлен")

# ===== 6. §18.6 — P081 =====
S18_1_HEADER = "### §18.1 Требования v9.1-v9.13 (111-153) — см. §15 для полных текстов"
P081_BLOCK = """### §18.6 Требование v9.26 (163) — schema-driven validation

> **v9.26 НОВОЕ:** 1 новое требование (P081). Полный текст в `требования к ии/_принципы.md`.

163. **Schema-driven validation** (P081) — `pre-commit-hook.py` динамически читает схему §12.X из промпта и валидирует ВСЕ обязательные поля, определённые в схеме; F70g = 1.0 БЛОКИРОВКА. См. §0.1. Урок из v9.25: 9 из 18 проверок FAIL — AI не добавил `тип_модели`, `canon_realizable`, `многослойная_броню` — потому что скрипт их не проверял. Общее правило устраняет этот класс проблем навсегда: новое поле в схеме → автоматически валидируется.

"""
assert S18_1_HEADER in text
text = text.replace(S18_1_HEADER, P081_BLOCK + S18_1_HEADER)
print("✓ §18.6 с P081 добавлен")

# ===== 7. Обновить expected и коммит =====
text = text.replace(
    '"expected": "9.25",  # v9.25',
    '"expected": "9.26",  # v9.26'
)
text = text.replace(
    "После создания скелета — **коммит инициализации**: `chore(скелет): инициализация SkyNet v9.25 + расширенная структура фантастические данные/ + F88 + разделение galinstan/mimetic_polyalloy`.",
    "После создания скелета — **коммит инициализации**: `chore(скелет): SkyNet v9.26 + schema-driven validation (F70g, P081)`."
)
text = text.replace(
    "5. Финальный коммит: `docs(результаты): финальная сводка SkyNet v9.25`.",
    "5. Финальный коммит: `docs(результаты): финальная сводка SkyNet v9.26`."
)

# ===== 8. Сохранить =====
SRC.write_text(text, encoding="utf-8")

print(f"\nv9.26 готов: {len(text)} символов, {text.count(chr(10))+1} строк")
print(f"Δ от v9.25: {len(text) - 368190:+d} символов")

# Проверки
checks = [
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.26",
    "version: 9.26",
    "§0.1 ОБЩЕЕ ПРАВИЛО",
    "F70g",
    "P081",
    "schema-driven validation",
    "validate_against_schema",
    "read_required_fields_from_prompt",
    "§13.17",
    "§18.6",
    '"expected": "9.26"',
]
print("\n=== Проверка ===")
for c in checks:
    ok = c in text
    print(f"  {'✓' if ok else '✗'} {c[:60]}")

# Validate Python §0 and §19
import re as re2
m0 = re2.search(r'```python\n(def check_skynet_state.*?return \{.*?\n    \})\n```', text, re2.DOTALL)
if m0:
    try:
        compile(m0.group(1), '<§0>', 'exec')
        print("\n✓ §0 check_skynet_state компилируется")
    except SyntaxError as e:
        print(f"\n✗ §0: {e}")
