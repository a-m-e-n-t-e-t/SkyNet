# SkyNet Scripts Catalog

Реестр всех скриптов в `scripts/` и их привязка к метрикам F*/P* спецификации
`SkyNet_PROMPT_v9.31.md`. Каталог является источником правды для графа 3
(`graphs/graph3_traceability.json`): генератор `scripts/generate_graphs.py`
читает таблицы ниже и строит рёбра `validated_by` / `enforces_contract`.

Согласованность (по состоянию на 2026-11-05, v9.36):

* 17 файлов `.py` на диске (включая `__init__.py`, `_helpers.py`, `_stubs.py`)
* 12 функций-заглушек в `_stubs.py` (см. раздел "Stubs")
* v9.36: в `_helpers.py` добавлены `MODEL_FILENAMES`, `yaml_serialize_value`, `write_atomic` — единый источник правды для будущих скриптов
* v9.37: добавлен `TransactionBatch` для транзакционной multi-file записи; 3 отработавших one-shot миграции перенесены в `_archive_oneoff/` (17 файлов вместо 22)

---

## Реальные скрипты Python

| Скрипт | Назначение | Метрики | Контракты (fc_*) |
|---|---|---|---|
| `__init__.py` | Пакет Python для `scripts/` (импорт как модуль) | — | — |
| `_helpers.py` | Общие хелперы: кэш YAML-frontmatter, проверка schema-consistency (F70), pattern-matching для метрик; v9.37: `write_atomic`, `TransactionBatch`; v9.37.1: `yaml_serialize_block` (единый сериализатор вместо 3 копий) | F70, F71, F72, F73, F74, F75, F79, F80, F86, F87 | — |
| `_stubs.py` | Реестр нереализованных функций (см. раздел Stubs) | — | — |
| `capture_dialog.py` | Захват диалога в `диалог/*.md` для аудита решений | E1, E2, E3, E4 | — |
| `check_model_completeness.py` | Проверка ≥1 изделия на каждую expected_subsystem модели | F86 | — |
| `classify_subsystem.py` | Классификация 13 подсистем + тип_модели | F3, F75 | fc_изделие_подсистема, fc_модель_тип |
| `decompose_all_izdeliya.py` | Декомпозиция всех изделий на части (batch); v9.35: поддержка поля количество=N; v9.37: TransactionBatch (parent+children атомарно); v9.37.1: serialize_value из _helpers | B07, B09 | — |
| `generate_decomposition.py` | Генерация stub-файлов декомпозиции; v9.35: CANON_DECOMP использует count=2 для paired parts; v9.37.1: serialize_value из _helpers | B07 | — |
| `generate_graphs.py` | Генератор graph1/2/3 + Mermaid-рендеры + fill-backrefs | F36, F37, F38 | — |
| `generate_wrapper_izdeliya.py` | Генерация wrapper-файлов изделия (cover page); v9.37: `write_atomic` | B05 | — |
| `pipeline.py` | Оркестратор фаз 0-8 batch-обработки | F37, F38, F39, F40, F46, F47 | — |
| `pre-commit-hook.py` | Pre-commit: path-type-status + F3-F36, F70, F81-F88, регенерация графов; v9.35: F26 warning | F3, F4, F5, F8-F36, F70, F81, F82, F83, F84, F85, F86, F87, F88 | — |
| `real_decomposition.py` | Декомпозиция реальных изделий (live data); v9.35: per-parent уникальные dims для крепёж и основной_элемент; v9.36: исправлен баг `description` → `описание`; v9.37: `write_atomic` | B07, B09 | — |
| `validate_decomposition.py` | Главный валидатор: F12a-F26, F70 (schema consistency), F18 (jsonschema); v9.35: добавлена F26 + поле количество в schema; v9.36: F12a O(n²)→O(n), F22/F19/F23 cache reuse | F12a, F13, F14, F15a, F15b, F15d, F15g, F16, F17, F18, F19, F20, F21, F22, F23, F24, F25, F26, F70 | — |
| `validate_field_contracts.py` | Бидирекциональная проверка fc_* (спецификация ↔ данные) | F56, F58, F59, F60, F70 | fc_материал_кристалл_структура, fc_материал_оптимальная_структура, fc_изделие_стандарты, fc_материал_предел_текучести, fc_модель_applied_patterns, fc_реализация_покрытие_функций, fc_изделие_масса |
| `web_verify.py` | **v9.38 CLI-раннер веб-верификации** (замена one-shot v9.31, заархивирован в `_archive_oneoff/web_verify_one_shot_v9.31.py`): `check` — критерии F22/F23/F25* для cron-шага 5 (exit 0 = issue устарел), `apply` — транзакционное применение web_search-данных (шаг 6), анти-фабрикация-гарды (отказ generic-материалов, шаблонных габаритов, не-URL), `--dry-run` | F22, F23, F25 | — |

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

8 файлов в `.github/workflows/` (v9.36.1: удалены мёртвые `_download-pat.yml`, `batch-process.yml`, `phase0-init.yml`, `release-creator.yml`; `scripts/_dedup_keys.js` — общий модуль dedup-ключей для verify_decomposition.yml). Подробности — в `.github/workflows/README.md`
(если присутствует) или в комментариях в каждом workflow.

v9.36: исправления в `verify_decomposition.yml` — добавлена обработка F26
в auto-close шаге (раньше F26 issues не попадали в currentKeys и ложно
закрывались как stale), добавлена пагинация для existingIssues
(раньше при >100 issues дедуп-проверка теряла старые ключи).

## Использование

### Веб-верификация через CLI (v9.38 НОВОЕ)

```bash
# Шаг 5 cron-протокола: проверка «issue устарел?»
python3 scripts/web_verify.py check --file "реальные данные/.../_index.md"
python3 scripts/web_verify.py check --file ... --json   # machine-readable

# Шаг 6: применение результатов реального web_search (транзакционно)
python3 scripts/web_verify.py apply --file "реальные данные/.../_index.md" \
    --url https://... --material <id> --dims L,W,H [--mass 0.42] \
    [--standards "ASTM F136; ISO 5832-3"] [--desc "..."] [--principle "..."] \
    [--dry-run]
```

`apply` отклоняет (exit 3): generic-материалы (`GENERIC_MATERIALS` из валидатора),
шаблонные габариты 100×100×50 / 100×50×20, не-URL источники. Запись через
`write_atomic`. Критерии `check` синхронизированы с F22/F23/F25 валидатора —
выход 0 означает «нарушение исправлено, issue можно закрыть как stale».

### Установка локального pre-commit hook (v9.37 НОВОЕ)

```bash
bash scripts/install_hooks.sh   # ставит .git/hooks/pre-commit
```

Запускает `scripts/pre-commit-hook.py` **до** git commit. Блокирует плохой
коммит на этапе набора (CI ловит с задержкой 5-10 мин). Path-filter:
запускается только для коммитов, затрагивающих `реальные данные/`,
`фантастические данные/`, `scripts/`, `требования_к_ии/`, `graphs/`.
Bypass: `git commit --no-verify` (не рекомендуется).

### Транзакционный cron-цикл (v9.37 НОВОЕ)

```bash
bash scripts/cron_run.sh <issue_number> <file_path>...
# пример:
bash scripts/cron_run.sh 146 "реальные данные/изделия/прочее/X/_index.md"
```

Обёртка cron-агента: проверка in-progress lock → взятие лока → `git add` →
`git commit` → `git push` (rebase) → комментарий к issue → закрытие →
снятие метки. На EXIT/INT/TERM — cleanup: orphaned edits сохраняются для
следующего цикла (НЕ `git restore`). Устраняет баг 11:37/12:07 — цикл падает
между edit и commit, валидные данные пропадают.

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

---

## Конвенция классификации каталога (v9.46)

Каталог `реальные данные/` делит все сущности на 3 категории по директории
и полю `тип` в front matter:

| Директория       | Поле `тип`     | Префикс `id`     | Семантика                                  |
|---|---|---|---|
| `материалы/`     | `материал`     | `material_*`     | Вещество (по составу/структуре/свойствам) |
| `изделия/`       | `изделие`      | `izdelie_*` / `часть_*` | Форма выпуска, товар, сборочная единица |
| `технологии/`    | `технология`   | `tekhnologia_*`   | Процесс обработки/нанесения/сборки        |

### Когда сущность — материал, а когда — изделие

**Материал** описывает вещество и его свойства (состав, кристаллическая
структура, ρ, k, E, проводимость). Пример: `material_copper` = Cu-ETP C11000
как металл (состав, ГЦК-поликристалл, ρ 8940 кг/м³, E 117 ГПа, σ 5.8×10⁷ См/м).
**Стандарты материала** описывают состав + форму поставки одновременно
(ASTM B152 = composition + sheet/bar; ASTM B194 = BeCu composition + sheet).

**Изделие** описывает товарную позицию или сборочную единицу, изготовленную
из материала. Имеет `материалы_частей` (BOM), ссылающийся на материалы.
Пример: `izdelie_mednyi_provod` = медный провод как товар (проволока
ASTM B1/B2/B3, temper'ы Soft/Hard/Spring) — её материал-основа
`material_copper` указан в `материалы_частей` с долей массы 1.0.

**Признак реклассификации (материал → изделие):**
- все стандарты в front matter — это спецификации **формы выпуска**
  (ASTM B1/B2/B3 = проволока; B280/B306 = труба; B209 = лист), а не
  стандарты состава;
- `варианты_по_применению` перечисляют товарные применения
  (жилы кабелей, обмотки, воздушные линии), а не свойства вещества;
- нет собственных свойств состава, которые не покрыты существующим
  материалом в `материалы/`.

Реклассификация состоит из 4 шагов (см. коммит c72f553 + #751 v2):
1. Создать новый файл в `изделия/<подсистема>/<id>/_index.md` с `тип: изделие`
   и `материалы_частей: [{материал: material_<основа>, доля_массы: 1.0}]`.
2. Во всех файлах с BOM-ссылкой на старый материал заменить
   `материал: <старый>` → `материал: <основа>` (напр. `mednyi_provod` →
   `copper`), и поправить markdown-ссылки `[<старый>.md]` → `[<основа>.md]`.
3. Удалить старый файл из `материалы/`.
4. Если старая пара была в `f32_fp_exclude` (check_F32) или `DUPLICATE_PAIRS`
   (migrate_aliases.py) — убрать, т.к. после реклассификации F32 их больше
   не сравнивает (разные категории).

### Одинаковые названия в разных категориях — норма

Разные каталожные сущности могут иметь одинаковое **человекочитаемое имя**
(id без префикса): `parylene_c` (вещество-полимер vs CVD-технология),
`pcm` (Phase-Change Material vs Phase-Change Memory chip). Это онтологическая
двойственность, не дубликат — ID-префикс как namespace отличает их.

`check_F33` находит такие коллизии автоматически и помечает как violation,
если имя не в `f33_known_collisions_set` (см. `validate_decomposition.py`).
При добавлении новой коллизии: проверьте, что это действительно разные
сущности (не дубликат), и добавьте имя в whitelist с кратким объяснением.

### v9.46 — что нового

* `validate_decomposition.py`: новая метрика **F33** (тип↔директория +
  коллизии имён между категориями). WARNING-метрика (pass при ratio=1.0,
  но violations видны в `--json-out`).
* Реклассификация `material_mednyi_provod` → `izdelie_mednyi_provod`
  (см. `изделия/система_питания/mednyi_provod/_index.md`).
* Очистка `f32_fp_exclude` от пары `{material_copper, material_mednyi_provod}`
  (F32 их больше не сравнивает — они в разных категориях).
* 6 файлов изделий с BOM-ссылкой на `mednyi_provod` переведены на `copper`
  (`материал: mednyi_provod` → `материал: copper`, markdown-ссылки обновлены).

