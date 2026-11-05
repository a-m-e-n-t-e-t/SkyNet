# SkyNet Scripts Catalog

Реестр всех скриптов в `scripts/` и их привязка к метрикам F*/P* спецификации
`SkyNet_PROMPT_v9.31.md`. Каталог является источником правды для графа 3
(`graphs/graph3_traceability.json`): генератор `scripts/generate_graphs.py`
читает таблицы ниже и строит рёбра `validated_by` / `enforces_contract`.

Согласованность (по состоянию на 2026-11-05, v9.36):

* 22 файла `.py` на диске (включая `__init__.py`, `_helpers.py`, `_stubs.py`)
* 12 функций-заглушек в `_stubs.py` (см. раздел "Stubs")
* v9.36: в `_helpers.py` добавлены `MODEL_FILENAMES`, `yaml_serialize_value`, `write_atomic` — единый источник правды для будущих скриптов

---

## Реальные скрипты Python

| Скрипт | Назначение | Метрики | Контракты (fc_*) |
|---|---|---|---|
| `__init__.py` | Пакет Python для `scripts/` (импорт как модуль) | — | — |
| `_helpers.py` | Общие хелперы: кэш YAML-frontmatter, проверка schema-consistency (F70), pattern-matching для метрик | F70, F71, F72, F73, F74, F75, F79, F80, F86, F87 | — |
| `_stubs.py` | Реестр нереализованных функций (см. раздел Stubs) | — | — |
| `capture_dialog.py` | Захват диалога в `диалог/*.md` для аудита решений | E1, E2, E3, E4 | — |
| `check_model_completeness.py` | Проверка ≥1 изделия на каждую expected_subsystem модели | F86 | — |
| `classify_subsystem.py` | Классификация 13 подсистем + тип_модели | F3, F75 | fc_изделие_подсистема, fc_модель_тип |
| `decompose_all_izdeliya.py` | Декомпозиция всех изделий на части (batch); v9.35: поддержка поля количество=N | B07, B09 | — |
| `generate_decomposition.py` | Генерация stub-файлов декомпозиции; v9.35: CANON_DECOMP использует count=2 для paired parts | B07 | — |
| `generate_graphs.py` | Генератор graph1/2/3 + Mermaid-рендеры + fill-backrefs | F36, F37, F38 | — |
| `generate_wrapper_izdeliya.py` | Генерация wrapper-файлов изделия (cover page) | B05 | — |
| `migrate_dedup_quantity.py` | v9.35 НОВОЕ — объединение within-product дубликатов (левая+правая, _1+_2) в один файл с количество=N (one-shot: запущен 2026-11-05, 19 пар объединено) | F26, P085 | — |
| `migrate_parts_into_parents.py` | Миграция частей в родительский `_index.md` (one-shot: выполнено) | B09 | — |
| `restore_missing_parts.py` | v9.35 НОВОЕ — восстановление 4 случайно удалённых часть_* файлов после d35e893 (one-shot: выполнено 2026-11-05) | F12a | — |
| `pipeline.py` | Оркестратор фаз 0-8 batch-обработки | F37, F38, F39, F40, F46, F47 | — |
| `pipeline_engine.py` | Engine цикла batch — СТАБ (5 строк, `execute_phase` pass). Запланирован к реализации в v9.37 | F37, F38 | — |
| `pre-commit-hook.py` | Pre-commit: path-type-status + F3-F36, F70, F81-F88, регенерация графов; v9.35: F26 warning | F3, F4, F5, F8-F36, F70, F81, F82, F83, F84, F85, F86, F87, F88 | — |
| `real_decomposition.py` | Декомпозиция реальных изделий (live data); v9.35: per-parent уникальные dims для крепёж и основной_элемент; v9.36: исправлен баг `description` → `описание` | B07, B09 | — |
| `validate_decomposition.py` | Главный валидатор: F12a-F26, F70 (schema consistency), F18 (jsonschema); v9.35: добавлена F26 + поле количество в schema; v9.36: F12a O(n²)→O(n), F22/F19/F23 cache reuse | F12a, F13, F14, F15a, F15b, F15d, F15g, F16, F17, F18, F19, F20, F21, F22, F23, F24, F25, F26, F70 | — |
| `validate_field_contracts.py` | Бидирекциональная проверка fc_* (спецификация ↔ данные) | F56, F58, F59, F60, F70 | fc_материал_кристалл_структура, fc_материал_оптимальная_структура, fc_изделие_стандарты, fc_материал_предел_текучести, fc_модель_applied_patterns, fc_реализация_покрытие_функций, fc_изделие_масса |
| `web_verify.py` | Веб-верификация: web_search → заполнение `источник_url`, материала, габаритов | F22, F23, F24, F25 | — |

## Stubs (`scripts/_stubs.py`)

Функции, которые концептуально выделены в отдельные «скрипты» в v9.22-v9.24,
но физически пока живут в одном модуле `_stubs.py`. Генератор графа 3
добавляет для каждого stub'а узел `stub:<name>` с ребром `hosted_in → script:_stubs.py`.
Когда функция будет реализована — она переедет в собственный `.py`, а запись
перейдёт в таблицу «Реальные скрипты Python» выше.

| Stub | Назначение | Метрики | Контракты (fc_*) |
|---|---|---|---|
| `apply_field_inheritance` | Наследование полей от родителя к дочерним частям | G2 | — |
| `apply_weakest_link` | Восходящее наследование (MIN propagation) | G2 | — |
| `autosync_helper` | Drift detection между локальным и remote | F46 | — |
| `check_applied_patterns` | Проверка applied_patterns в моделях | F52 | fc_модель_applied_patterns |
| `check_provenance` | Provenance completeness | F57, F67, F68 | — |
| `compute_model_parameters` | Расчёт параметров модели | C3 | fc_изделие_масса, fc_реализация_покрытие_функций |
| `decompose_components` | Декомпозиция изделий на неделимые части | B07, B09 | — |
| `extract_from_sources` | Извлечение данных из источников | A1, A2 | fc_изделие_стандарты, fc_материал_предел_текучести |
| `update_indexes` | Обновление INDEX-файлов | D2 | — |
| `update_readme` | Обновление README.md | — | — |
| `validate_patterns` | Валидация pattern-определений | F51, F53, F54, F55 | — |
| `verify_models` | Верификация моделей | G3, G4, F71, F72, F73, F74, F79 | — |

## GitHub Actions Workflows

12 файлов в `.github/workflows/`. Подробности — в `.github/workflows/README.md`
(если присутствует) или в комментариях в каждом workflow.

v9.36: исправления в `verify_decomposition.yml` — добавлена обработка F26
в auto-close шаге (раньше F26 issues не попадали в currentKeys и ложно
закрывались как stale), добавлена пагинация для existingIssues
(раньше при >100 issues дедуп-проверка теряла старые ключи).

## Использование

### Полная регенерация графов

```bash
python3 scripts/generate_graphs.py --all --force  # все 3 графа + Mermaid, игнор кэша
python3 scripts/generate_graphs.py --all          # инкрементально (по fingerprint)
python3 scripts/generate_graphs.py --graph 3      # только traceability-граф
```

### Проверка модели

```bash
python3 scripts/pre-commit-hook.py               # все метрики
python3 scripts/pre-commit-hook.py --check F25    # конкретная метрика
python3 scripts/check_model_completeness.py      # F86 — покрытие подсистем
```

### Полный batch pipeline

```bash
python3 scripts/pipeline.py --phase 0            # init
python3 scripts/pipeline.py --batch --max-models 3 --priority-order canon_first
python3 scripts/pre-commit-hook.py                # финальная валидация + регенерация графов
```
