# SkyNet — графы связей репозитория

Три направленных графа, описывающих связи внутри репозитория.

Source of truth — `*.json` файлы; Mermaid `.md` рендеры — генерируются автоматически из JSON и предназначены для чтения человеком.

## Граф 1: Граф данных

Связи между сущностями предметной области.

**Вершины:**
| Тип | Источник | Префикс id | Кол-во |
|---|---|---|---|
| `izdelie` | `реальные данные/изделия/<подсистема>/<изделие>/_index.md` (тип: изделие, уровень_номер: 1) | `izdelie_*` | 128 |
| `chast` | `реальные данные/изделия/<подсистема>/<изделие>/часть_*/_index.md` (уровень_номер: 2) | `часть_*` | 644 |
| `material` | `реальные данные/материалы/*.md` | `material_*` | 142 |
| `tekhnologia` | `реальные данные/технологии/*.md` | `tekhnologia_*` | 50+ |
| `standart` | `реальные данные/стандарты/*.md` | `standart_*` | 50+ |
| `issledovatelskaya_gruppa` | `реальные данные/исследовательские_группы/*.md` | `group_*` | 10+ |

**Рёбра (направленные):**
| Тип | Из → в | Поле-источник |
|---|---|---|
| `has_part` | izdelie → chast | `дочерние_части[]` |
| `child_of` | chast → izdelie | `родитель` |
| `uses_material` | {izdelie, chast} → material | `материалы_частей[].материал` |
| `complies_with` | {izdelie, chast, material, tekhnologia} → standart | `стандарты[]` |
| `researched_by` | {izdelie, chast, material, tekhnologia} → issledovatelskaya_gruppa | `исследовательская_группа` |

Обратные рёбра (`used_in`, `referenced_in`) синтезируются генератором и **также проставляются в файлах** (разделы `## Применение в изделиях`, `## Связанные изделия`, и т.д.).

Файлы:
- `graphs/graph1_data.json` — полный граф (source of truth)
- `graphs/mermaid/graph1_<подсистема>.md` — рендеры по подсистемам
- `graphs/mermaid/graph1_materials.md` — рендер графа материалов
- `graphs/mermaid/graph1_overview.md` — сводный граф подсистем

## Граф 2: Мета-граф

Связи между артефактами репозитория — кодом, спецификацией, схемами, документацией.

**Вершины:**
| Тип | Пример |
|---|---|
| `script` | `scripts/validate_decomposition.py` |
| `spec` | `SkyNet_PROMPT_v9.31.md` |
| `spec_section` | `§11.1 13 подсистем` (строка 2174 в spec) |
| `catalog` | `scripts/_CATALOG.md` |
| `index` | `реальные данные/изделия/_иерархия_изделий.md` |
| `readme` | `README.md` |
| `concept_doc` | `концепции/*.md`, `гипотезы/*.md`, `улучшения/*.md` |

**Рёбра:**
| Тип | Из → в | Источник |
|---|---|---|
| `imports` | script → script | `from X import Y` / `import X` |
| `implements` | script → spec_section | docstring и `executes_field_contracts[]` |
| `generates` | script → index | статический анализ (rglob, write_text) |
| `references` | script → catalog | `scripts/_CATALOG.md` |
| `documents` | readme → script | `README.md` |
| `describes` | concept_doc → script/spec | документ описывает скрипт/метрику |

Файлы:
- `graphs/graph2_meta.json`
- `graphs/mermaid/graph2_meta.md`

## Граф 3: Traceability (метрика → код → файл)

Граф прослеживаемости требований: какие требования спецификации реализуются какими скриптами и проверяются на каких файлах.

**Вершины:**
| Тип | Пример |
|---|---|
| `metric` | `F12a`, `F22`, `F25`, `P062` |
| `spec_section` | `§11.1 13 подсистем` |
| `script` | `scripts/validate_decomposition.py` |
| `file_pattern` | `реальные данные/изделия/**/_index.md` |
| `field_contract` | `fc_материал_кристалл_структура` |

**Рёбра:**
| Тип | Из → в | Источник |
|---|---|---|
| `defined_in` | metric → spec_section | парсинг спецификации |
| `validated_by` | metric → script | docstring / `_CATALOG.md` |
| `checks_files` | script → file_pattern | статический анализ |
| `enforces_contract` | script → field_contract | `_CATALOG.md` |
| `triggers_metric` | script → metric | обратное к `validated_by` |

Файлы:
- `graphs/graph3_traceability.json`
- `graphs/mermaid/graph3_traceability.md`

## Генерация

```bash
python3 scripts/generate_graphs.py --all           # все три графа + Mermaid
python3 scripts/generate_graphs.py --graph 1       # только граф 1
python3 scripts/generate_graphs.py --graph 1 --mermaid  # граф 1 + рендеры
python3 scripts/generate_graphs.py --fill-backrefs  # заполнить обратные рёбра в файлах
```
