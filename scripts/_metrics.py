"""SkyNet — единый реестр метрик (v9.35).

Источник истины для списка метрик, используемых в:
  - validate_decomposition.py (--json-out payload)
  - pre-commit-hook.py (WARNING_METRICS — какие не блокируют)
  - .github/workflows/verify_decomposition.yml (summary lists, auto-close dict)
  - scripts/_dedup_keys.js (legacy regex — генерируется отдельно)

Раньше список метрик дублировался в 5 местах (copy-rot risk):
  1. workflow summary loop (2 места: print + info)
  2. workflow auto-close dict
  3. validate_decomposition.py --json-out payload
  4. pre-commit-hook.py WARNING_METRICS set
  5. _dedup_keys.js legacy regex

Теперь все они читают ALL_METRICS из этого файла.

Использование:
  from _metrics import ALL_METRICS, SOFT_METRICS, METRIC_DESCRIPTIONS
"""

# Все метрики, которые валидируются и попадают в --json-out.
# Порядок = порядок round-robin в workflow (важно для приоритета issue-создания).
ALL_METRICS: tuple[str, ...] = (
    'F15b', 'F15d', 'F15g', 'F15h',
    'F22', 'F25',
    'F27', 'F27b', 'F27c', 'F27d', 'F27e', 'F27f', 'F27g',
    'F28', 'F29', 'F31', 'F33', 'F34',
    'F-scal',           # v9.32 / P087 §12.6 — опциональное поле масштабируемость
    'F-ai-lineage',     # v9.32 / §12.7 — предок+улучшения+real_check для версия: ии-улучшенная
    'F-fant-children',  # v9.34 — ссылки модели → изделия для фантастических моделей
)

# SOFT-метрики: pass=True всегда, не блокируют pre-commit, но создают verify-task issues.
# Жёсткие метрики (не в этом множестве) при pass=False → БЛОКИРУЮТ коммит.
SOFT_METRICS: frozenset[str] = frozenset({
    'F13', 'F15b', 'F15d', 'F15g', 'F15h', 'F16',
    'F22', 'F25',
    'F27', 'F27b', 'F27c', 'F27d', 'F27e', 'F27f', 'F27g',
    'F28', 'F29', 'F31', 'F34',
    'F-scal', 'F-ai-lineage', 'F-fant-children',
})

# Короткое описание для каждой метрики (для логов и workflow summary).
METRIC_DESCRIPTIONS: dict[str, str] = {
    'F13': 'соответствие типу модели',
    'F15b': 'выработка_тепла_W родителя ≥ Σ(дочерних) — тепло-баланс',
    'F15d': 'выработка_энергии_W родителя ≤ Σ(дочерних) — энергобаланс',
    'F15g': 'габариты/объём — все части помещаются в родителя',
    'F15h': 'lifetime родителя ≤ MIN(дочерних)',
    'F16': 'иерархия уровней — ребёнок = родитель + 1',
    'F22': 'верификация источника (URL/stub/schema-completeness)',
    'F25': 'уникальность параметров',
    'F27': 'незаполненные материалы-заглушки',
    'F27b': 'битые ссылки на материалы',
    'F27c': 'битые ссылки на технологии',
    'F27d': 'битые ссылки в материалы_для_процесса',
    'F27e': 'обязательность технологии_частей для частей с материалы_частей',
    'F27f': 'материалы_для_процесса внутри технологии_частей',
    'F27g': 'битые ссылки в материалы_для_процесса',
    'F28': 'альтернативные формы материалов',
    'F29': 'форма материала в части (BOM)',
    'F31': 'дедупликация материалов/технологий (syntactic+semantic)',
    'F33': 'классификационная консистентность (тип↔каталог)',
    'F34': 'глубина декомпозиции',
    'F-scal': 'опциональное поле масштабируемость (P087 §12.6)',
    'F-ai-lineage': 'предок+улучшения+real_check для версия: ии-улучшенная (§12.7)',
    'F-fant-children': 'ссылки модели → изделия (фантастические модели)',
}


def get_metrics_for_json_out() -> tuple[str, ...]:
    """Метрики, попадающие в --json-out payload (для workflow)."""
    return ALL_METRICS


def is_soft(metric: str) -> bool:
    """Является ли метрика SOFT (pass=True всегда, не блокирует pre-commit)."""
    return metric in SOFT_METRICS


def get_legacy_regex_pattern() -> str:
    """Сгенерировать regex-паттерн для legacyMetricFromTitle в _dedup_keys.js.

    Пример: 'F2[2-9](?:[a-z])?|F3[0-2]|F-scal|F-ai-lineage|F-fant-children'
    (без внешних скобок — они добавляются в JS-коде: match(/\\[(PATTERN)\\]/))

    Включает числовые диапазоны (F22-F32) + явно перечисленные named-метрики.
    Синхронизирован с regex в _dedup_keys.js (integrity-чек в pre-commit-hook.py).
    """
    # Числовые F-метрики из ALL_METRICS
    numeric_metrics = [m for m in ALL_METRICS if re.match(r'^F\d+', m)]
    # Названные soft-метрики (F-scal, F-ai-lineage, F-fant-children)
    named_metrics = [m for m in ALL_METRICS if not re.match(r'^F\d+', m)]

    # F22-F32: как один диапазон (F2[2-9](?:[a-z])? | F3[0-2])
    parts = ['F2[2-9](?:[a-z])?', 'F3[0-2]']
    # Добавить named-метрики (с экранированием дефиса)
    for m in named_metrics:
        parts.append(m.replace('-', r'-'))
    return '|'.join(parts)


# Импорты для безопасного re-использования
import re
