# SkyNet Scripts Catalog
# Реестр всех скриптов с executes_field_contracts[] (§20.2 bidirectional integrity)
# v9.24: 3 аудита v9.17 — F81-F87, P077-P079, canon_realizable

## Скрипты Python (19 + __init__.py + _helpers.py = 21 файлов)

| Скрипт | Назначение | Метрики | executes_field_contracts[] |
|---|---|---|---|
| pipeline.py | Оркестратор фаз 0-8 | B1, F37-F50, F71-F75 (v9.22) | — |
| pipeline_engine.py | Engine (импортируется pipeline.py) | — | — |
| autosync_helper.py | Drift detection | F46 | — |
| pre-commit-hook.py | Path-type-status + F3-F75 | F3, F4, F5, F8-F36, F70, **F71-F75** (v9.22) | — |
| extract_from_sources.py | Извлечение из канона | A1-A2 | fc_изделие_стандарты, fc_материал_предел_текучести |
| decompose_components.py | Декомпозиция изделий | B07, B09 | — |
| classify_subsystem.py | Классификация 13 подсистем + тип_модели (v9.22) | F3, **F75** (v9.22) | fc_изделие_подсистема, fc_модель_тип |
| apply_weakest_link.py | Восходящее наследование | G2 | — |
| apply_field_inheritance.py | Наследование полей | G2 | — |
| verify_models.py | Верификация моделей | G3, G4, **F71-F74** (v9.22), **F79** (v9.23) | — |
| compute_model_parameters.py | Расчёт параметров | C3 | fc_изделие_масса, fc_реализация_покрытие_функций |
| update_readme.py | Обновление README | — | — |
| update_indexes.py | Обновление индексов | D2 | — |
| capture_dialog.py | Захват диалога | E1-E4 | — |
| validate_patterns.py | Валидация pattern-определений | F51, F53, F54, F55 | — |
| check_applied_patterns.py | Проверка applied_patterns | F52 | fc_модель_applied_patterns |
| validate_field_contracts.py | Bidirectional + F56-F70 | F56, F58-F60, F70 | fc_материал_кристалл_структура, fc_материал_оптимальная_структура |
| check_provenance.py | Provenance completeness | F57, F67, F68 | — |
| _helpers.py | F70 хелпер-функции + F71-F75 + F79-F80 хелперы (v9.22-v9.23) | F70, F71-F75, F79, F80 | — |

## v9.22 НОВОЕ: типы моделей и многослойная броня

### Типы моделей (§11.0)

| Скрипт | Что читает | Метрика |
|---|---|---|
| classify_subsystem.py | `требования к ии/_типы_моделей.yaml` | F75 (тип_модели указан) |
| pre-commit-hook.py | `требования к ии/_типы_моделей.yaml` | F74 (тип брони ↔ тип модели) |
| verify_models.py | `требования к ии/_типы_моделей.yaml` | F71 (многослойная броня), F72 (верификация материалов) |

### Многослойная броня (§11.6)

| Скрипт | Что делает | Метрика |
|---|---|---|
| pre-commit-hook.py | Проверяет ≥3 слоя для real/canon_with_real_analogue | F71 |
| pre-commit-hook.py | Проверяет verification для каждого слоя | F72 |
| verify_models.py | Сравнивает тип брони с типом модели (§11.6.2) | F74 |

## GitHub Actions Workflows (11 файлов — без изменений от v9.21)

| # | Workflow | Триггер | Метрики | Функция |
|---|---|---|---|---|
| 1 | phase0-init.yml | workflow_dispatch, repository_dispatch, push на себя | §0 check_skynet_state, §9 Phase 0 | Phase 0: PAT + SkyNet state check |
| 2 | pre-commit-checks.yml | push на любую ветку, PR на main | B01-B10, M11-M19, F1-F30, F34, F43-F44, F46, F48, F52, F70, **F71-F75** (v9.22) | 49+5 F-метрик |
| 3 | batch-process.yml | schedule: 0 4,10,16,22 * * *, workflow_dispatch | §9.1 batch processing | §9.1 batch (max 3 models per session) |
| 4 | sync-check.yml | push на любую ветку | F47 синхронизация_github | F47 GitHub sync verification |
| 5 | telemetry-update.yml | schedule: */5 * * * * | M37 telemetry_freshness_min | M37 telemetry update каждые 5 мин |
| 6 | sync-alice-concepts.yml | schedule: 0 3 * * 1, workflow_dispatch | F41, F42 Alice specs | §17 Этап 0.6 weekly sync концепций |
| 7 | issue-triage.yml | issues: [opened, edited, labeled], workflow_dispatch | §9.2 разбор типа запроса | v9.21: авто-парсинг issues с моделями → создание файлов |
| 8 | pages-deploy.yml | push на main с changes в models/, workflow_dispatch | §9 Phase 6.3 article | v9.21: публикация статьи на GitHub Pages |
| 9 | branch-protection-setup.yml | workflow_dispatch, schedule: daily | §9 Phase 5 enforcement | v9.21: Branch Protection + drift detection |
| 10 | release-creator.yml | push tags v*, workflow_dispatch | §15a.2 Conventional Commits | v9.21: авто-релизы на тегах |
| 11 | codeql-analysis.yml | push на main в scripts/, PR, schedule: weekly | F16 кибербезопасность, P026 | v9.21: статический security-анализ |

## GitHub Configs (7 файлов + 1 config.yml — без изменений от v9.21)

| # | Файл | Назначение |
|---|---|---|
| 1 | .github/dependabot.yml | Авто-обновление pip + github-actions deps |
| 2 | .github/CODEOWNERS | Auto-assign reviewer (28 path-правил) |
| 3 | .github/PULL_REQUEST_TEMPLATE.md | Шаблон PR с чек-листом метрик |
| 4-7 | .github/ISSUE_TEMPLATE/{model-request,bug-report,hypothesis,q-and-a}.md | Шаблоны issues |
| + | .github/ISSUE_TEMPLATE/config.yml | Контактные ссылки |

## Использование

### Проверка типа модели

```bash
# Проверить что все модели имеют тип_модели (F75)
python scripts/pre-commit-hook.py --check F75

# Проверить что тип брони соответствует типу модели (F74)
python scripts/pre-commit-hook.py --check F74
```

### Полный pipeline

```bash
python scripts/pipeline.py --phase 0  # init
python scripts/pipeline.py --batch --max-models 3 --priority-order canon_first
python scripts/pre-commit-hook.py     # все метрики
```

## v9.23 НОВОЕ: тип-специфичный subset подсистем

| Скрипт | Что делает | Метрика |
|---|---|---|
| classify_subsystem.py | Читает `требования к ии/_типы_моделей.yaml` для определения subset per тип | F75 (тип указан) |
| pre-commit-hook.py | Проверяет что все mandatory подсистемы присутствуют (F79) | F79 |
| pre-commit-hook.py | Проверяет что not_applicable подсистемы отсутствуют (F80) | F80 |

### Пример проверки F80 (отсутствие неприменимых)

```python
def check_F80(model) -> bool:
    '''Проверяет что not_applicable подсистемы для типа модели ОТСУТСТВУЮТ.'''
    тип = model.тип_модели
    not_applicable = load_yaml("_типы_моделей.yaml").types[тип].not_applicable_subsystems
    actual = set(извлечить_подсистемы_модели(model))
    forbidden = set(not_applicable) & actual
    return len(forbidden) == 0

# Пример: стационарная модель с 'система_передвижения' → F80 FAIL
```


## v9.24 НОВОЕ: check_model_completeness.py (F86)

| Скрипт | Что делает | Метрика |
|---|---|---|
| check_model_completeness.py | Проверяет что все expected_subsystems имеют хотя бы 1 изделие в реализация_промышленная ИЛИ реализация_ии | F86 (доля_моделей_с_100%_покрытием_подсистем = 1.0 БЛОКИРОВКА) |

Урок из v9.17: AI не делал эту проверку сам — пользователь должен был попросить
«проверь содержат ли подсистемы каждой модели все необходимые изделия».
После этого нашлось 3 пробела: маскировка, навигация, система_связи.

Теперь скрипт запускается ПОСЛЕ каждого batch автоматически (§9.5 авто-отчёт).

### Использование

```bash
python scripts/check_model_completeness.py
# Exit code 0 = все модели полные (F86 = 1.0)
# Exit code 1 = есть неполные модели (F86 < 1.0, БЛОКИРОВКА)
```
