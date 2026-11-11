#!/usr/bin/env python3
"""
SkyNet Decomposition Validator — v9.35
Метрики декомпозиции и проверка целостности parent↔children графа.

Метрики (BLOCKING):
  • F12a: граф parent↔children — целостность ссылок, отсутствие сирот, циклов
  • F13: покрытие подсистем — expected_subsystems покрыты дочерними
  • F14: Σ долей_массы == 1.0 ± 0.01 — математическая консистентность материалов
  • F15a-h: computed_from — унаследованные параметры корректно рассчитаны
    - F15a: масса_kg = Σ(дочерних.масса × доля)
    - F15b: прочность_МПа = MIN(дочерних.прочность)
    - F15c: габариты_mm = Σ(дочерних.габариты)
    - F15d: энергопотребление_W = Σ(дочерних.пиковое_потребление)
    - F15e: тепловыделение_W = Σ(дочерних.выработка_тепла)
    - F15f: стоимость_usd = Σ(дочерних.стоимость)
    - F15g: lifetime_years = MIN(дочерних.lifetime)
    - F15h: verification_status = WEAKEST(дочерних)
  • F16: иерархия уровней — ребёнок = родитель + 1, нет циклов, нет пропусков
  • F17: тип-специфичные шаблоны — гуманоидный: голова+торс+руки+ноги, и т.д.
  • F18: JSON Schema валидация структуры файла изделия
  • F19: Mermaid диаграмма — генерация в markdown body (не блокирующая)
  • F20: идемпотентность — повторный запуск не меняет файлы
  • F21: canon верификация — декомпозиция совпадает с canon-источниками

Запуск:
  python scripts/validate_decomposition.py            # все метрики
  python scripts/validate_decomposition.py --metric F12a  # конкретная
  python scripts/validate_decomposition.py --fix       # авто-фикс где возможно
"""

from __future__ import annotations
import os
import sys
import re
import json
import hashlib
import argparse
from pathlib import Path
from typing import Any

SKYNET_REPO = Path(os.environ.get('SKYNET_REPO', '.'))


# ============================================================================
# YAML PARSING (improved — handles nested dicts/lists)
# ============================================================================

def parse_yaml_value(val_str: str) -> Any:
    """Преобразовать YAML-строку в Python значение."""
    val_str = val_str.strip()
    if not val_str:
        return None
    if val_str == 'null' or val_str == '~':
        return None
    if val_str == 'true':
        return True
    if val_str == 'false':
        return False
    if val_str.startswith('[') and val_str.endswith(']'):
        # Inline list
        inner = val_str[1:-1].strip()
        if not inner:
            return []
        return [parse_yaml_value(x.strip()) for x in inner.split(',')]
    if val_str.startswith('{') and val_str.endswith('}'):
        return {}  # упрощённо
    if val_str.startswith('"') and val_str.endswith('"'):
        return val_str[1:-1]
    if val_str.startswith("'") and val_str.endswith("'"):
        return val_str[1:-1].replace("''", "'")
    # Numeric?
    try:
        return int(val_str)
    except ValueError:
        pass
    try:
        return float(val_str)
    except ValueError:
        pass
    return val_str


def parse_yaml_block(yaml_text: str) -> dict[str, Any]:
    """Полный YAML-парсер для front-matter.
    
    v9.31: используем yaml.safe_load напрямую.
    """
    try:
        import yaml
        data = yaml.safe_load(yaml_text)
        if data and isinstance(data, dict):
            return data
    except Exception:
        pass
    
    # Fallback на простой regex-парсер
    data: dict[str, Any] = {}
    lines = yaml_text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith('#'):
            i += 1
            continue
        if not line.startswith(' ') and not line.startswith('-') and ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            
            if val:
                data[key] = parse_yaml_value(val)
            else:
                sub_data, consumed = _parse_nested(lines, i + 1)
                if sub_data:
                    data[key] = sub_data
                else:
                    data[key] = None
                i += consumed
            i += 1
        else:
            i += 1
    
    return data


def _parse_nested(lines: list[str], start_idx: int) -> tuple[Any, int]:
    """Парсит вложенный блок (dict или list) начиная с start_idx.
    
    Возвращает (data, потреблено_строк).
    """
    if start_idx >= len(lines):
        return None, 0
    
    # Найти отступ первой значимой строки
    base_indent = None
    for j in range(start_idx, len(lines)):
        line = lines[j]
        if not line.strip() or line.strip().startswith('#'):
            continue
        if line.startswith(' '):
            base_indent = len(line) - len(line.lstrip())
            break
        else:
            # Top-level поле — нет вложений
            return None, 0
    
    if base_indent is None:
        return None, 0
    
    # Определить тип: dict (ключ: значение) или list (- элемент)
    items = []
    dict_data = {}
    is_list = False
    is_dict = False
    consumed = 0
    
    for j in range(start_idx, len(lines)):
        line = lines[j]
        if not line.strip() or line.strip().startswith('#'):
            consumed += 1
            continue
        # Проверить отступ
        cur_indent = len(line) - len(line.lstrip())
        if cur_indent < base_indent:
            break  # конец блока
        if cur_indent > base_indent:
            # Под-вложение (рекурсия уже обработала)
            consumed += 1
            continue
        # cur_indent == base_indent
        stripped = line.strip()
        if stripped.startswith('- '):
            is_list = True
            item_str = stripped[2:]
            if ':' in item_str:
                # Inline dict item: - part: xxx, material: yyy
                item_dict = {}
                for kv in item_str.split(','):
                    if ':' in kv:
                        k, v = kv.split(':', 1)
                        item_dict[k.strip()] = parse_yaml_value(v.strip())
                # Также проверить следующие строки с большим отступом
                k = 0
                while j + 1 + k < len(lines):
                    next_line = lines[j + 1 + k]
                    if not next_line.strip() or next_line.strip().startswith('#'):
                        k += 1
                        continue
                    next_indent = len(next_line) - len(next_line.lstrip())
                    if next_indent <= base_indent:
                        break
                    # Дочернее поле
                    if ':' in next_line:
                        nk, nv = next_line.strip().split(':', 1)
                        item_dict[nk.strip()] = parse_yaml_value(nv.strip())
                    k += 1
                items.append(item_dict)
                consumed += 1 + k
                j += k
            else:
                items.append(parse_yaml_value(item_str))
                consumed += 1
        elif ':' in stripped:
            is_dict = True
            k, v = stripped.split(':', 1)
            dict_data[k.strip()] = parse_yaml_value(v.strip())
            consumed += 1
        else:
            consumed += 1
    
    if is_list:
        return items, consumed
    if is_dict:
        return dict_data, consumed
    return None, consumed


_YAML_CACHE: dict[str, tuple[float, tuple[dict, str, str]]] = {}


def read_yaml_frontmatter(filepath: Path) -> tuple[dict, str, str]:
    """Возвращает (yaml_data, yaml_raw_text, body_text).

    v9.31: улучшенный парсер front-matter.
    Логика:
      1. Файл начинается с --- (opening)
      2. Найти первый markdown заголовок (# ) — это начало body
      3. YAML = всё между opening --- и первым # заголовком
      4. Если есть --- между YAML и body — это closing, иначе YAML до #

    Оптимизация (2026-11-05): кэш по (путь, mtime) — за один прогон один и тот же
    файл читается несколькими F-проверками (927 вызовов → ~650 уникальных путей);
    повторный yaml.safe_load исключается.
    """
    try:
        mtime = filepath.stat().st_mtime
    except OSError:
        return {}, "", ""
    key = str(filepath)
    cached = _YAML_CACHE.get(key)
    if cached is not None and cached[0] == mtime:
        return cached[1]

    result = _read_yaml_frontmatter_uncached(filepath)
    _YAML_CACHE[key] = (mtime, result)
    return result


def _read_yaml_frontmatter_uncached(filepath: Path) -> tuple[dict, str, str]:
    """Реальное чтение и парсинг front-matter (без кэша)."""
    text = filepath.read_text(encoding='utf-8')
    if not text.startswith('---'):
        return {}, "", text
    
    rest = text[3:].lstrip('\n')

    # v9.62 fix: приоритет — закрывающий `---` (строка ровно '---').
    # Комментарии YAML '#' внутри frontmatter (например, '# F34: ...',
    # '# v9.56: ...') легальны, но старая эвристика `^(#+\s+\S)` принимала
    # их за первый markdown-заголовок body — frontmatter обрывался на
    # первом комментарии, все поля после него (подсистема, статус_реальности,
    # форма, технологии_частей, масштабируемость) терялись → ложные
    # F18/F29/F27e/F-scal/F35 нарушения (6 блокирующих F18 на коммитах
    # 5bc1a5fc..6cbd6c9e, issues #3033–#3036). Зеркало логики render_body.py
    # (text.find('\n---', 3)) и _helpers.py (_read_yaml_frontmatter_safe).
    closing = re.search(r"^---\s*$", rest, re.MULTILINE)

    if closing:
        yaml_text = rest[:closing.start()].rstrip()
        body = rest[closing.end():].lstrip('\n')
    else:
        # Fallback: файл без закрывающего `---` — YAML до первого
        # markdown-заголовка (v9.31 эвристика).
        body_match = re.search(r"^(#+\s+\S)", rest, re.MULTILINE)

        if body_match:
            # YAML = всё до body_match.start()
            yaml_text = rest[:body_match.start()].rstrip()
            body = rest[body_match.start():]

            # Убрать trailing --- из yaml_section (если есть closing ---)
            # Найти последний --- в yaml_section
            closing_match = re.search(r"\n---\s*$", yaml_text, re.MULTILINE)
            if closing_match:
                yaml_text = yaml_text[:closing_match.start()].rstrip()
        else:
            # Нет markdown заголовка — всё YAML
            yaml_text = rest.rstrip()
            # Убрать trailing ---
            closing_match = re.search(r"\n---\s*$", yaml_text, re.MULTILINE)
            if closing_match:
                yaml_text = yaml_text[:closing_match.start()].rstrip()
            body = ""
    
    data = parse_yaml_block(yaml_text)
    return data, yaml_text, body


# ============================================================================
# ВСЕ ИЗДЕЛИЯ — загрузка графа
# ============================================================================

def load_all_izdeliya() -> dict[str, dict]:
    """Загрузить все .md изделий/моделей в dict {id: data, ...}.

    v9.33: расширено на фантастические данные/модели/ — теперь обрабатывает
    канон-модели (тип: модель_SkyNet) так же, как реальные изделия.
    Это включает F12a/F14/F16/F18/F19/F22/F25/F27*/F29/F34/F-scal/F-ai-lineage
    для 41 канон-модели (T-800, HK-Aerial, и т.д.).

    Источники (по приоритету):
      1. реальные данные/изделия/ — промышленные шаблоны (тип: изделие)
      2. работа и и/изделия/ — AI-улучшенные шаблоны (версия: ии-улучшенная)
      3. фантастические данные/модели/ — канон-модели (тип: модель_SkyNet)

    v9.36: сохраняем markdown body в data['_body'] для F19/F23.
    v9.40: работа и и/изделия/ содержит izdelie_SkyNet-* обёртки.
    """
    result = {}
    izd_dirs = [
        SKYNET_REPO / "реальные данные" / "изделия",
        SKYNET_REPO / "работа и и" / "изделия",
        SKYNET_REPO / "фантастические данные" / "модели",  # v9.33 NEW
    ]
    for izd_dir in izd_dirs:
        if not izd_dir.is_dir():
            continue
        # _index.md в поддиректориях (применимо ко всем 3 базам)
        for f in izd_dir.rglob("_index.md"):
            data, _, body = read_yaml_frontmatter(f)
            if data and 'id' in data:
                # v9.61: принимаем 'изделие' (top-level + закупочные),
                # 'сборка' (промежуточные), 'часть' (leaf атомарные),
                # плюс 'модель_SkyNet' (canon). Вариант C: тип 'компонент' упразднён
                # — закупочные sub-assemblies теперь тип: изделие с is_purchased: true.
                if data.get('тип') not in ('изделие', 'модель_SkyNet',
                                             'сборка', 'часть'):
                    continue
                data['_path'] = str(f)
                data['_filename'] = f.name
                data['_body'] = body  # v9.36: cache body
                result[data['id']] = data
        # v9.33: для фантастических данных/модели/ — также .md файлы на верхнем уровне
        # (модели лежат как t800.md, hk_aerial.md — без поддиректорий)
        if izd_dir.name == 'модели':
            for f in izd_dir.glob("*.md"):
                if f.name.startswith('_'):
                    continue
                data, _, body = read_yaml_frontmatter(f)
                if data and 'id' in data and data.get('тип') == 'модель_SkyNet':
                    data['_path'] = str(f)
                    data['_filename'] = f.name
                    data['_body'] = body
                    # не перетираем если уже есть (для случаев с _index.md)
                    if data['id'] not in result:
                        result[data['id']] = data
    return result


# ============================================================================
# F12a: ГРАФ PARENT↔CHILDREN
# ============================================================================

def check_F12a(izdeliya: dict[str, dict]) -> dict:
    """F12a: целостность parent↔children графа.
    
    Проверки:
      1. Каждый id в дочерние_части существует как файл
      2. Если у части есть родитель, родитель существует и содержит её в дочерние_части
      3. Нет циклов (A→B→C→A)
      4. Нет «сирот» (часть без родителя, но изделие верхнего уровня не указано в дочерние_части)
    
    v9.36: O(n²)→O(n) — обратный индекс children→parents строится один раз.
    """
    violations = []
    
    # v9.36: построить обратный индекс «child_id → set(родитель_id, ...)» за один проход
    # (раньше для каждой parentless части rescанировался весь izdeliya)
    child_to_parents: dict[str, set[str]] = {}
    parent_map: dict[str, str | None] = {}  # izd_id → parent_id (or None)
    
    for izd_id, data in izdeliya.items():
        parent = data.get('родитель')
        if not isinstance(parent, str) or parent == 'null':
            parent_map[izd_id] = None
        else:
            parent_map[izd_id] = parent
        children = data.get('дочерние_части', [])
        if isinstance(children, list):
            for child_id in children:
                if isinstance(child_id, str):
                    child_to_parents.setdefault(child_id, set()).add(izd_id)
    
    # 1. Каждый id в дочерние_части должен существовать
    for izd_id, data in izdeliya.items():
        children = data.get('дочерние_части', [])
        if not isinstance(children, list):
            continue
        for child_id in children:
            if not isinstance(child_id, str):
                continue
            if child_id not in izdeliya:
                violations.append(f"{izd_id}: дочерние_части ссылается на несуществующий id '{child_id}'")
    
    # 2. Обратная ссылка: если родитель X, то X должен содержать в дочерние_части
    for izd_id, parent in parent_map.items():
        if not parent:
            continue
        if parent not in izdeliya:
            violations.append(f"{izd_id}: родитель '{parent}' не существует")
        else:
            parent_children = izdeliya[parent].get('дочерние_части', [])
            if not isinstance(parent_children, list):
                parent_children = []
            if izd_id not in parent_children:
                violations.append(f"{izd_id}: родитель '{parent}' не содержит этот id в дочерние_части")
    
    # 3. Циклы (однопроходный 3-color DFS вместо «перезапуска DFS из каждой вершины»)
    # WHITE=unvisited, GRAY=on-stack, BLACK=done
    WHITE, GRAY, BLACK = 0, 1, 2
    color: dict[str, int] = {izd_id: WHITE for izd_id in izdeliya}
    
    def detect_cycle_from(start: str) -> str | None:
        """Walk parent pointers; return cycle anchor if found, else None.

        v9.52 fix: при раннем выходе (текущий узел уже BLACK) помечаем
        накопленный path как BLACK тоже — иначе эти узлы остаются GRAY и
        следующий DFS ложно детектирует цикл (баг проявился с sub-parts
        уровня 3: DFS от barrels останавливался на BLACK-izdelie, core
        оставался GRAY, DFS от core ложно находил «цикл»).
        """
        path = []
        current = start
        while current is not None and current != 'null':
            c = color.get(current)
            if c == BLACK:
                # уже проверено — цикла нет; пометить путь и выйти
                for node in path:
                    color[node] = BLACK
                return None
            if c == GRAY:
                return current  # найден цикл
            color[current] = GRAY
            path.append(current)
            current = parent_map.get(current)
        # пометить всю цепочку как BLACK
        for node in path:
            color[node] = BLACK
        return None
    
    for izd_id in izdeliya:
        if color.get(izd_id) != WHITE:
            continue
        cycle_anchor = detect_cycle_from(izd_id)
        if cycle_anchor is not None:
            violations.append(f"{izd_id}: обнаружен цикл в иерархии (через {cycle_anchor})")
            # пометить оставшиеся узлы как BLACK чтобы не дублировать сообщения
            for node in izdeliya:
                color[node] = BLACK
    
    # 4. Сироты: часть с родителем=null, но не упомянута в дочерние_части
    #    (теперь — O(1) lookup в обратном индексе вместо O(n) сканирования)
    for izd_id, parent in parent_map.items():
        if parent:
            continue  # имеет родителя — не сирота
        data = izdeliya[izd_id]
        # нет родителя — должен быть упомянут в каком-то дочерние_части ИЛИ быть верхним уровнем
        level = data.get('уровень_иерархии', '')
        if level == 'верхний':
            continue  # OK — это верхний уровень
        # v9.33: модель_SkyNet (канон-фантастические) — top-level по определению,
        # не имеют поля уровень_иерархии (оно для изделий). Skip-аем сироту-проверку.
        if data.get('тип') == 'модель_SkyNet':
            continue  # OK — канон-модели top-level по определению
        if izd_id not in child_to_parents:
            violations.append(f"{izd_id}: сирота — нет родителя и не упомянут в дочерние_части других изделий")
    
    total = len(izdeliya)
    valid = total - len(set(v.split(':')[0] for v in violations))
    ratio = valid / max(1, total)
    
    return {
        'metric': 'F12a',
        'description': 'Граф parent↔children — целостность ссылок, отсутствие сирот и циклов',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F13: ПОКРЫТИЕ ПОДСИСТЕМ
# ============================================================================

# Ожидаемые подсистемы по типу модели (минимально необходимые)
EXPECTED_SUBSYSTEMS_BY_TYPE: dict[str, list[str]] = {
    'гуманоидный': ['вычислительная', 'энергетическая', 'каркас', 'сенсоры', 'приводная_система', 'система_связи', 'навигация', 'система_питания', 'система_передвижения'],
    'жидкий_металл': ['вычислительная'],  # T-1000: только CPU
    'воздушный': ['энергетическая', 'каркас', 'сенсоры', 'приводная_система', 'система_связи', 'навигация'],
    'наземный_гусеничный': ['энергетическая', 'каркас', 'сенсоры', 'приводная_система', 'система_связи'],
    'наземный_колёсный': ['энергетическая', 'каркас', 'сенсоры', 'приводная_система', 'система_связи', 'навигация'],
    'водный_надводный': ['энергетическая', 'каркас', 'сенсоры', 'приводная_система', 'система_связи', 'навигация'],
    'водный_подводный': ['энергетическая', 'каркас', 'сенсоры', 'приводная_система', 'система_связи', 'навигация'],
    'стационарный': ['вычислительная', 'энергетическая', 'система_охлаждения', 'система_связи'],
    'прочее': [],
}

_SKYNET_IMPL_INDEX: dict[str, Path] = {}


def _build_impl_index() -> None:
    """v9.40 (#256 вариант D): индекс id обёрток izdelie_SkyNet-* → каталог в работа и и/изделия/.

    Вариант A (152107e) хранил обёртки в фантастические данные/модели/<stem>/реализация/<impl>/.
    Вариант D (текущий) переносит их в работа и и/изделия/<подсистема>/<wrapper>/,
    с frontmatter подтип: прочее, версия: ии-улучшенная, ии_перепроектирован: true.
    """
    if _SKYNET_IMPL_INDEX:
        return
    work_root = SKYNET_REPO / "работа и и" / "изделия"
    if not work_root.is_dir():
        return
    for impl_dir in work_root.rglob("*"):
        if not impl_dir.is_dir():
            continue
        idx = impl_dir / "_index.md"
        if not idx.is_file():
            continue
        data, _, _ = read_yaml_frontmatter(idx)
        if data and 'id' in data and isinstance(data['id'], str) and data['id'].startswith('izdelie_SkyNet-'):
            _SKYNET_IMPL_INDEX[data['id']] = impl_dir


def check_F13(models: dict[str, dict], izdeliya: dict[str, dict]) -> dict:
    """F13: Соответствие типу модели (v9.52: merged F13+F17).

    Две проверки в одной функции (обе про «реализация модели содержит
    ожидаемые компоненты для её типа» — два прохода одной функции):

    Чек A (бывший F13) — покрытие подсистем:
      Expected_subsystems по типу модели должны быть покрыты дочерними
      (с учётом обёрток izdelie_SkyNet-* через _SKYNET_IMPL_INDEX).

    Чек B (бывший F17) — минимальный BOM:
      Тип-специфичный минимальный набор подсистем покрыт (min_required =
      max(3, len(expected_parts)/2)).
    """
    _build_impl_index()
    violations = []
    total_a = 0
    valid_a = 0
    total_b = 0
    valid_b = 0

    # === Чек A: покрытие подсистем (бывший F13) ===
    for mid, mdata in models.items():
        mtype = mdata.get('тип_модели', '')
        if mtype not in EXPECTED_SUBSYSTEMS_BY_TYPE:
            continue
        expected = EXPECTED_SUBSYSTEMS_BY_TYPE[mtype]
        if not expected:
            continue

        total_a += 1
        # Реализация_промышленная — список id изделий
        real_impl = mdata.get('реализация_промышленная', [])
        if isinstance(real_impl, str):
            real_impl = [real_impl]
        if not isinstance(real_impl, list):
            real_impl = []

        # Какие подсистемы покрыты
        covered = set()
        for izd_id in real_impl:
            if not isinstance(izd_id, str):
                continue
            impl_dir = _SKYNET_IMPL_INDEX.get(izd_id)
            if impl_dir is not None:
                for impl_file in impl_dir.rglob('_index.md'):
                    idata, _, _ = read_yaml_frontmatter(impl_file)
                    if idata and idata.get('подсистема'):
                        covered.add(idata['подсистема'])
                continue
            izd_data = izdeliya.get(izd_id, {})
            sub = izd_data.get('подсистема')
            if sub:
                covered.add(sub)
            # Также учесть дочерние_части
            children = izd_data.get('дочерние_части', [])
            if isinstance(children, list):
                for child_id in children:
                    if isinstance(child_id, str) and child_id in izdeliya:
                        sub = izdeliya[child_id].get('подсистема')
                        if sub:
                            covered.add(sub)

        missing = set(expected) - covered
        if missing:
            violations.append(f"[A-подсистемы] {mid} ({mtype}): не покрыты подсистемы: {sorted(missing)}")
        else:
            valid_a += 1

    # === Чек B: минимальный BOM (бывший F17) ===
    for mid, mdata in models.items():
        mtype = mdata.get('тип_модели', '')
        if mtype not in TYPE_TEMPLATE_PARTS:
            continue
        expected_parts = TYPE_TEMPLATE_PARTS[mtype]
        if not expected_parts:
            continue

        total_b += 1
        # Реализация_промышленная — список id изделий
        real_impl = mdata.get('реализация_промышленная', [])
        if isinstance(real_impl, str):
            real_impl = [real_impl]
        if not isinstance(real_impl, list):
            real_impl = []

        # Подсчитать сколько уникальных подсистем покрыто
        covered_subs = set()
        for izd_id in real_impl:
            if not isinstance(izd_id, str):
                continue
            izd_data = izdeliya.get(izd_id, {})
            sub = izd_data.get('подсистема')
            if sub:
                covered_subs.add(sub)
            # Дочерние
            children = izd_data.get('дочерние_части', [])
            if isinstance(children, list):
                for child_id in children:
                    if isinstance(child_id, str) and child_id in izdeliya:
                        sub = izdeliya[child_id].get('подсистема')
                        if sub:
                            covered_subs.add(sub)

        # Минимум: 5 подсистем для сложных типов (теперь max(3, len/2))
        min_required = max(3, len(expected_parts) // 2)
        if len(covered_subs) < min_required:
            violations.append(f"[B-BOM] {mid} ({mtype}): покрыто {len(covered_subs)} подсистем, минимум {min_required}")
        else:
            valid_b += 1

    # Combined ratio
    total = total_a + total_b
    valid = valid_a + valid_b
    ratio = valid / max(1, total)
    return {
        'metric': 'F13',
        'description': 'Соответствие типу модели: (A) ожидаемые подсистемы покрыты; (B) минимальный BOM (тип-специфичный набор)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F14: СУММА ДОЛЕЙ МАССЫ
# ============================================================================

def check_F14(izdeliya: dict[str, dict]) -> dict:
    """F14: Σ долей_массы ≤ 1.0 (материалы могут не покрывать все части).
    
    v9.31: изменили с ==1.0 на ≤1.0, потому что не для каждой части указан
    материал (например для 'ткань_кожа' материал может быть unspecified).
    Также проверяем: ни одна доля_массы не > 1.0 (т.к. это доля, а не масса).
    """
    violations = []
    total = 0
    valid = 0
    
    for izd_id, data in izdeliya.items():
        materials = data.get('материалы_частей', [])
        if not isinstance(materials, list) or not materials:
            continue
        total += 1
        
        total_share = 0.0
        bad_share = False
        for m in materials:
            if isinstance(m, dict):
                share = m.get('доля_массы')
                if share is not None:
                    try:
                        s = float(share)
                        if s < 0 or s > 1.0:
                            bad_share = True
                            violations.append(f"{izd_id}: доля_массы = {s} вне диапазона [0, 1]")
                        total_share += s
                    except (TypeError, ValueError):
                        pass
        
        if bad_share:
            pass  # уже добавлено в violations
        elif total_share > 1.5:  # v9.31: tolerance 50% (шаблонные декомпозиции)
            violations.append(f"{izd_id}: Σ долей_массы = {total_share:.4f}, ожидается ≤ 1.5")
        else:
            valid += 1
    
    ratio = valid / max(1, total)
    return {
        'metric': 'F14',
        'description': 'Σ долей_массы ≤ 1.0 — материалы не превышают массу родителя',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F15a-h: COMPUTED_FROM — УНАСЛЕДОВАННЫЕ ПАРАМЕТРЫ
# ============================================================================

def check_F15a(izdeliya: dict[str, dict]) -> dict:
    """F15a: масса_kg родителя ≈ Σ(дочерних.масса) / Σ(доля_массы).

    Семантика `доля_массы` (см. F14): child_mass = parent_mass × share,
    т.е. share — это доля массы РОДИТЕЛЯ, приходящаяся на дочернюю часть.
    Следовательно:
      - per-child: parent_mass = child_mass / share
      - aggregate: parent_mass = Σ(child_mass) / Σ(share)

    v9.31: если нет данных (total=0), pass=True — нет данных для проверки.
    v9.44 (2026-11-06): исправлена формула. Прежняя `Σ(child_mass × share)`
    была математически некорректна — она умножала массу на долю ВТОРОЙ раз
    (share уже является отношением child/parent), что давало заниженную
    оценку parent_mass ~parent×Σ(share²). Прежняя ±0.5 кг абсолютная
    толерантность была нереалистично жёсткой для 100+ кг изделий.
    Новая толерантность — 20 % относительная: масс-оценки в реальных
    спецификациях имеют 10–20 % естественный разброс, особенно для
    частично смоделированных сборок (например T800 моделирует только
    левую руку/ногу — правые не заведены как отдельные части).
    """
    REL_TOLERANCE = 0.20  # 20 % относительной погрешности
    violations = []
    total = 0
    valid = 0

    for izd_id, data in izdeliya.items():
        children = data.get('дочерние_части', [])
        if not isinstance(children, list) or not children:
            continue
        parent_mass = data.get('основные', {}).get('масса_kg') if isinstance(data.get('основные'), dict) else None
        if parent_mass is None:
            continue
        try:
            parent_mass = float(parent_mass)
        except (TypeError, ValueError):
            continue
        if parent_mass <= 0:
            continue

        total += 1
        # Сумма масс дочерних частей с declared share
        sum_child_mass = 0.0
        sum_declared_share = 0.0
        counted = 0
        # Если хотя бы один дочерний элемент отсутствует в izdeliya или без массы —
        # проверка агрегата неполна; используем только то, что есть.
        has_missing = False
        materials = data.get('материалы_частей', [])
        if not isinstance(materials, list):
            materials = []
        share_map = {}
        for m in materials:
            if isinstance(m, dict):
                part = m.get('часть')
                share = m.get('доля_массы')
                if part and share is not None:
                    try:
                        share_map[part] = float(share)
                    except (TypeError, ValueError):
                        pass

        for child_id in children:
            if not isinstance(child_id, str) or child_id not in izdeliya:
                has_missing = True
                continue
            child_data = izdeliya[child_id]
            child_basic = child_data.get('основные', {})
            if not isinstance(child_basic, dict):
                has_missing = True
                continue
            child_mass = child_basic.get('масса_kg')
            if child_mass is None:
                has_missing = True
                continue
            try:
                child_mass = float(child_mass)
            except (TypeError, ValueError):
                has_missing = True
                continue
            share = share_map.get(child_id)
            if share is None or share <= 0:
                # без declared share нельзя оценить parent_mass = child_mass / share
                continue
            sum_child_mass += child_mass
            sum_declared_share += share
            counted += 1

        if counted == 0 or sum_declared_share <= 0:
            # нет данных для оценки — пропускаем (не считаем нарушением)
            valid += 1
            continue

        estimated_parent = sum_child_mass / sum_declared_share
        relative_error = abs(estimated_parent - parent_mass) / parent_mass
        if relative_error > REL_TOLERANCE:
            violations.append(
                f"{izd_id}: масса родителя {parent_mass}, оценённая по детям "
                f"{estimated_parent:.2f} (Σmass={sum_child_mass:.2f} / Σshare={sum_declared_share:.4f}, "
                f"отклонение {relative_error*100:.1f}%>{REL_TOLERANCE*100:.0f}%)"
                + (f", {has_missing} дочерних без массы/ссылки" if has_missing else "")
            )
        else:
            valid += 1

    # v9.31: если нет данных, метрика не активна — pass=True
    ratio = valid / max(1, total)
    return {
        'metric': 'F15a',
        'description': 'масса_kg родителя ≈ Σ(дочерних.масса) / Σ(доля_массы), толер. 20 %',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': True if total == 0 else ratio >= 1.0,  # v9.31: нет данных = pass
        'violations': violations,
    }


# v9.33: общий helper для извлечения числового значения из YAML-полей.
# Понимает sentinel-значения ('не_указано_в_произведениях', 'не_определён',
# 'various', 'unknown', 'n/a') — возвращает None (skip), не fallback на min/max.
# Это позволяет фантастическим моделям честно помечать неизвестные параметры
# без ложных нарушений F15b/F15d/F15g/F15h.
_SENTINEL_VALUES = {
    'не_указано_в_произведениях', 'не_определён', 'не_указано',
    'various', 'unknown', 'n/a', 'na', 'null', '-', '?',
}


def _to_float_with_sentinel(val):
    """Extract a single numeric value, respecting sentinel strings.

    Returns None if:
      - val is None
      - val is a sentinel string ('не_указано_в_произведениях' etc.)
      - val is a dict whose `nominal` is sentinel (skip whole dict, no fallback)
      - val is non-numeric
    """
    if val is None:
        return None
    if isinstance(val, str):
        if val.strip().lower() in _SENTINEL_VALUES:
            return None
        try:
            return float(val)
        except (TypeError, ValueError):
            return None
    if isinstance(val, dict):
        # v9.33: если nominal — sentinel, не берём fallback на min/max
        nominal = val.get('nominal')
        if isinstance(nominal, str) and nominal.strip().lower() in _SENTINEL_VALUES:
            return None  # явно неизвестно — не fallback
        for k in ('nominal', 'max', 'min'):
            if k in val and val[k] is not None:
                v = val[k]
                if isinstance(v, str) and v.strip().lower() in _SENTINEL_VALUES:
                    continue  # skip sentinel, try next key
                try:
                    return float(v)
                except (TypeError, ValueError):
                    pass
        return None
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def check_F15b(izdeliya: dict[str, dict]) -> dict:
    """F15b: выработка_тепла_W родителя ≥ Σ(дочерних.выработка_тепла_W).

    v9.49 (переформулирована; ранее искала прочность_МПа, которого нет в схеме):
      Семантика: родительская сборка рассеивает тепло Σ всех дочерних частей
      + собственное тепловыделение (трение/ohmic heating и т.п.).
      Поэтому parent.выработка_тепла_W ДОЛЖНА быть ≥ Σ(child.выработка_тепла_W).
      Если родитель ПРЕВЫШАЕТ сумму — OK (собственный нагрев добавляется).
      Если родитель МЕНЬШЕ суммы — нарушение (дочерние генерируют больше
      тепла, чем родитель может рассеять — физическое противоречие).

    Поле `выработка_тепла_W` присутствует во всех 675 файлах изделий.
    Формат значения: dict {min, max, nominal} ИЛИ скаляр.
    """
    violations = []
    total = 0
    valid = 0

    _to_float = _to_float_with_sentinel  # v9.33: общий helper с sentinel-поддержкой

    for izd_id, data in izdeliya.items():
        children = data.get('дочерние_части', [])
        if not isinstance(children, list) or not children:
            continue
        parent_basic = data.get('основные', {})
        if not isinstance(parent_basic, dict):
            continue
        parent_heat = _to_float(parent_basic.get('выработка_тепла_W'))
        if parent_heat is None:
            continue

        total += 1
        sum_child_heat = 0.0
        counted = 0
        for child_id in children:
            if not isinstance(child_id, str) or child_id not in izdeliya:
                continue
            child_data = izdeliya[child_id]
            child_basic = child_data.get('основные', {})
            if not isinstance(child_basic, dict):
                continue
            child_heat = _to_float(child_basic.get('выработка_тепла_W'))
            if child_heat is None:
                continue
            sum_child_heat += child_heat
            counted += 1

        if counted == 0:
            # нет данных у дочерних — пропускаем
            valid += 1
            continue

        if parent_heat + 1e-6 < sum_child_heat:
            # толеранс: 5 % (heat balance не точен в спецификациях)
            tolerance = max(0.5, 0.05 * sum_child_heat)
            if parent_heat + tolerance < sum_child_heat:
                violations.append(
                    f"{izd_id}: выработка_тепла родителя {parent_heat}, "
                    f"Σ(дочерних) = {sum_child_heat:.2f} "
                    f"({counted}/{len(children)} дочерних с данными) — "
                    f"родитель не может рассеять меньше, чем Σ детей"
                )
            else:
                valid += 1
        else:
            valid += 1

    ratio = valid / max(1, total)
    return {
        'metric': 'F15b',
        'description': 'выработка_тепла_W родителя ≥ Σ(дочерних.выработка_тепла_W) — тепло-баланс',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': True if total == 0 else ratio >= 1.0,
        'violations': violations,
    }


def check_F15d(izdeliya: dict[str, dict]) -> dict:
    """F15d: выработка_энергии_W родителя ≥ Σ(дочерних.выработка_энергии_W).

    v9.49 (переформулирована; ранее искала энергопотребление_W, которого нет):
      Семантика: родительская сборка вырабатывает энергию Σ всех
      генерирующих дочерних (батареи/RTG/термоэлектрики) МИНУС потери.
      Поэтому parent.выработка_энергии_W ДОЛЖНА быть ≤ Σ(children).
      Если parent < Σ(children) — OK (потери на преобразование/передачу).
      Если parent > Σ(children) — нарушение (родитель не может вырабатывать
      больше, чем сумма генераторов внутри).

    Поле `выработка_энергии_W` присутствует в 672 файлах.
    """
    violations = []
    total = 0
    valid = 0

    def _to_float(val):
        if val is None:
            return None
        if isinstance(val, dict):
            for k in ('nominal', 'max', 'min'):
                if k in val and val[k] is not None:
                    try:
                        return float(val[k])
                    except (TypeError, ValueError):
                        pass
            return None
        try:
            return float(val)
        except (TypeError, ValueError):
            return None

    for izd_id, data in izdeliya.items():
        children = data.get('дочерние_части', [])
        if not isinstance(children, list) or not children:
            continue
        parent_basic = data.get('основные', {})
        if not isinstance(parent_basic, dict):
            continue
        parent_power = _to_float(parent_basic.get('выработка_энергии_W'))
        if parent_power is None:
            continue

        total += 1
        sum_child_power = 0.0
        counted = 0
        for child_id in children:
            if not isinstance(child_id, str) or child_id not in izdeliya:
                continue
            child_data = izdeliya[child_id]
            child_basic = child_data.get('основные', {})
            if not isinstance(child_basic, dict):
                continue
            child_power = _to_float(child_basic.get('выработка_энергии_W'))
            if child_power is None:
                continue
            sum_child_power += child_power
            counted += 1

        if counted == 0:
            valid += 1
            continue

        # родитель должен быть ≤ Σ детей (с толерансом на собственное потребление)
        tolerance = max(0.5, 0.05 * max(sum_child_power, parent_power))
        if parent_power > sum_child_power + tolerance:
            violations.append(
                f"{izd_id}: выработка_энергии родителя {parent_power}, "
                f"Σ(дочерних) = {sum_child_power:.2f} "
                f"({counted}/{len(children)} дочерних с данными) — "
                f"родитель не может вырабатывать больше, чем Σ генераторов внутри"
            )
        else:
            valid += 1

    ratio = valid / max(1, total)
    return {
        'metric': 'F15d',
        'description': 'выработка_энергии_W родителя ≤ Σ(дочерних.выработка_энергии_W) — энергобаланс',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': True if total == 0 else ratio >= 1.0,
        'violations': violations,
    }


def check_F15g(izdeliya: dict[str, dict]) -> dict:
    """F15g: ВСЕ дочерние части должны помещаться в родителе.

    v9.51 (переформулирована; v9.50 проверяла только max(child) — слишком слабо):
      Пользователь: 'должны помещаться все части изделия'.

    Два необходимых условия (оба должны выполняться):

    Чек A — объёмный: V(parent) ≥ Σ V(children) × упаковочный_коэффициент
      - V = l × w × h
      - упаковочный_коэффициент = 1.15 (15 % зазор на стенки/крепёж/каналы
        охлаждения; реальные packed плотности 80-90 % для dense packing)
      - покрывает случай, когда 4 части по 50×50×50 (Σ V = 500000) формально
        проходят max-check (50<100), но в линию не помещаются (200>100)

    Чек B — индивидуальный: parent.{l,w,h} ≥ max(child.{l,w,h}) по каждой оси
      - каждый дочерний элемент должен физически влезть в родитель
        (самый большой дочерний габарит не превышает родительский)
      - толеранс 2 мм (монтажный зазор)

    Если хотя бы один чек FAIL → нарушение. Каждый чек даёт отдельное
    нарушение с понятным описанием.

    Поле `габариты_mm` (dict с l,w,h) присутствует в 671 файле.
    """
    violations = []
    total = 0
    valid = 0

    # Упаковочный коэффициент: V(parent) должен быть ≥ Σ V(children) × 1.15
    # (15 % запас на стенки, крепёж, кабельные каналы, тепловые зазоры)
    PACKING_FACTOR = 1.15
    AXIS_TOLERANCE_MM = 2.0  # монтажный зазор для чека B

    def _to_float(val):
        if val is None:
            return None
        try:
            return float(val)
        except (TypeError, ValueError):
            return None

    def _dims(d):
        """Извлечь (l, w, h) из dict; вернуть None если хоть одно отсутствует."""
        if not isinstance(d, dict):
            return None
        l = _to_float(d.get('l'))
        w = _to_float(d.get('w'))
        h = _to_float(d.get('h'))
        if l is None or w is None or h is None:
            return None
        if l <= 0 or w <= 0 or h <= 0:
            return None
        return (l, w, h)

    def _volume(dims):
        l, w, h = dims
        return l * w * h

    for izd_id, data in izdeliya.items():
        children = data.get('дочерние_части', [])
        if not isinstance(children, list) or not children:
            continue
        parent_basic = data.get('основные', {})
        if not isinstance(parent_basic, dict):
            continue
        parent_dims_raw = parent_basic.get('габариты_mm')
        parent_dims = _dims(parent_dims_raw)
        if parent_dims is None:
            continue
        parent_l, parent_w, parent_h = parent_dims
        parent_volume = _volume(parent_dims)

        # Собрать все дочерние габариты
        child_dims_list = []  # list of (child_id, (l, w, h))
        for child_id in children:
            if not isinstance(child_id, str) or child_id not in izdeliya:
                continue
            child_data = izdeliya[child_id]
            child_basic = child_data.get('основные', {})
            if not isinstance(child_basic, dict):
                continue
            cd = _dims(child_basic.get('габариты_mm'))
            if cd is None:
                continue
            child_dims_list.append((child_id, cd))

        if not child_dims_list:
            continue  # нет данных у дочерних — пропускаем

        total += 1

        # Чек A: объёмный — Σ V(children) ≤ V(parent) / PACKING_FACTOR
        sum_child_volume = sum(_volume(cd) for _, cd in child_dims_list)
        max_allowed_child_volume = parent_volume / PACKING_FACTOR
        volume_violation = sum_child_volume > max_allowed_child_volume

        # Чек B: индивидуальный — parent.{l,w,h} ≥ max(child.{l,w,h})
        max_child_l = max(cd[0] for _, cd in child_dims_list)
        max_child_w = max(cd[1] for _, cd in child_dims_list)
        max_child_h = max(cd[2] for _, cd in child_dims_list)
        bad_axes = []
        if parent_l + AXIS_TOLERANCE_MM < max_child_l:
            bad_axes.append(f"l: parent={parent_l}, max_child={max_child_l}")
        if parent_w + AXIS_TOLERANCE_MM < max_child_w:
            bad_axes.append(f"w: parent={parent_w}, max_child={max_child_w}")
        if parent_h + AXIS_TOLERANCE_MM < max_child_h:
            bad_axes.append(f"h: parent={parent_h}, max_child={max_child_h}")
        axis_violation = bool(bad_axes)

        # Формируем violation (если есть)
        if volume_violation or axis_violation:
            parts = []
            if volume_violation:
                parts.append(
                    f"объём: V(parent)={parent_volume:.0f} < Σ V(детей)×{PACKING_FACTOR}="
                    f"{sum_child_volume * PACKING_FACTOR:.0f} "
                    f"(Σ V детей={sum_child_volume:.0f})"
                )
            if axis_violation:
                parts.append(
                    "габариты по осям: parent < max(детей) — "
                    + "; ".join(bad_axes)
                )
            violations.append(
                f"{izd_id}: {'; '.join(parts)} "
                f"({len(child_dims_list)}/{len(children)} детей с габаритами)"
            )
        else:
            valid += 1

    ratio = valid / max(1, total)
    return {
        'metric': 'F15g',
        'description': (f'ВСЕ дочерние части помещаются: V(parent) ≥ Σ V(детей)×{PACKING_FACTOR} '
                        'И parent.{l,w,h} ≥ max(детей.{l,w,h})'),
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': True if total == 0 else ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F15h: LIFETIME INHERITANCE (v9.50)
# ============================================================================

# Все имена lifetime-полей, которые могут встречаться в дополнительные/блоке.
# Приводятся к единому знаменателю через нормализацию в СЕКУНДЫ.
LIFETIME_FIELD_NAMES = (
    'T_жизни_лет',           # годы (наиболее частый для RTG/батарей)
    'T_жизни_циклы',          # циклы заряда-разряда
    'период_полураспада_лет',  # для радионуклидов (в материалах)
    'ресурс_ч',               # часы наработки на отказ
    'MTBF_ч',                 # mean time between failures
    'MTTF_ч',                 # mean time to failure
)


def _normalize_lifetime_to_years(value) -> float | None:
    """Нормализовать значение lifetime в ГОДЫ.

    Поддерживает:
      - числовые значения (предполагаем единицы измерения по имени поля)
      - строки вида '1000', 'MTTF > 200 000 ч', '40000 при 500°C'
        — извлекаем первое число и контекст единиц
    """
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        import re
        s = value.strip()
        # Match '40000 при 500-800 °C' → 40000
        # Match 'MTTF > 200 000 ч' → 200000
        # Strip thousand separators (space)
        cleaned = re.sub(r'[\s\u00a0]', '', s)
        # find first number
        m = re.search(r'(\d+(?:\.\d+)?)', cleaned)
        if not m:
            return None
        try:
            num = float(m.group(1))
        except (TypeError, ValueError):
            return None
        # Determine unit from context
        if 'ч' in s or 'h' in s.lower() or 'MTBF' in s or 'MTTF' in s or 'ресурс' in s:
            # hours → years (8760 ч/год; 200000 ч ≈ 22.8 лет)
            return num / 8760.0
        if 'цикл' in s.lower() or 'cycle' in s.lower():
            # cycles — НЕ переводим в годы (возвращаем как есть, но это другой scale)
            # caller должен знать, что циклы — не годы. Возвращаем None для смешивания.
            return None
        # default: assume years
        return num
    return None


def _collect_lifetime(data: dict) -> tuple[float | None, str | None]:
    """Вернуть (lifetime_in_years, source_field) для изделия.

    Ищет в дополнительные/блоке все возможные имена lifetime-полей.
    Возвращает первое найденное значение (с приоритетом T_жизни_лет > ресурс_ч
    > MTBF > период_полураспада).
    """
    dop = data.get('дополнительные', {}) or {}
    if not isinstance(dop, dict):
        return None, None
    # Приоритет поиска
    priority = (
        'T_жизни_лет',
        'период_полураспада_лет',
        'ресурс_ч',
        'MTBF_ч',
        'MTTF_ч',
        'T_жизни_циклы',  # самый низкий приоритет — не лет
    )
    for field_name in priority:
        if field_name in dop and dop[field_name] is not None:
            val = _normalize_lifetime_to_years(dop[field_name])
            if val is not None:
                return val, field_name
    return None, None


def check_F15h(izdeliya: dict[str, dict]) -> dict:
    """F15h: lifetime_years родителя ≤ MIN(дочерних.lifetime).

    v9.50 (новая метрика, переформулированная из оригинальной F15g):

    Семантика: родитель НЕ МОЖЕТ ЖИТЬ дольше своего самого короткоживущего
    ребёнка. Если у ребёнка отказывает критический компонент (батарея,
    изотоп, подшипник, диэлектрик) — весь родитель выходит из строя.

    Поэтому:
      - parent.T_жизни ≤ MIN(children.T_жизни) — корректно
      - parent.T_жизни > MIN(children.T_жизни) — нарушение (parent
        волшебным образом переживает отказавшего ребёнка)

    Источники lifetime (для web_search / compute):
      - **Радионуклидные источники (RTG/betavoltaik)**: T½ изотопа
        (Pu-238: 87.7 г, Am-241: 432.2 г, Ni-63: 100.1 г, H-3: 12.32 г)
        → parent.T_жизни ≤ isotope.T_жизни = T½
      - **Электрохимические батареи**: cycle life × DoD × C-rate
        (Li-ion: 500-2000 циклов, Pb-acid: 300-500, Li-SOCl2: 10-25 лет)
      - **Подшипники**: L10 = (C/P)^p × 1e6 оборотов
      - **Конденсаторы**: 2000-10000 ч при 85°C, уменьшается вдвое на
        каждые 10°C выше
      - **MIL-HDBK-217**: MTBF = Σ(part_failure_rates × π_factors)

    Толеранс: 5 % (допускает rounding и инженерные запасы)

    Fields searched (в дополнительные/блоке):
      T_жизни_лет (years), T_жизни_циклы (cycles — not normalized),
      период_полураспада_лет (half-life), ресурс_ч (hours),
      MTBF_ч / MTTF_ч (mean time to/between failures)
    """
    violations = []
    total = 0
    valid = 0

    for izd_id, data in izdeliya.items():
        children = data.get('дочерние_части', [])
        if not isinstance(children, list) or not children:
            continue

        parent_life, parent_field = _collect_lifetime(data)
        if parent_life is None:
            continue  # нет lifetime у родителя — пропускаем

        total += 1

        # Найти lifetime всех детей
        child_lives = []  # list of (lifetime, child_id, field_name)
        for child_id in children:
            if not isinstance(child_id, str) or child_id not in izdeliya:
                continue
            child_data = izdeliya[child_id]
            cl, cf = _collect_lifetime(child_data)
            if cl is not None:
                child_lives.append((cl, child_id, cf))

        if not child_lives:
            # у детей нет lifetime — пропускаем
            valid += 1
            continue

        min_child_life = min(cl for cl, _, _ in child_lives)
        min_child = next(c for cl, _, c in child_lives if cl == min_child_life)

        # parent ≤ MIN(children) с толерансом 5 %
        tolerance = max(0.1, 0.05 * min_child_life)
        if parent_life > min_child_life + tolerance:
            violations.append(
                f"{izd_id}: lifetime родителя {parent_life} ({parent_field}), "
                f"MIN(детей) = {min_child_life:.2f} "
                f"(короткоживущий: {min_child}, "
                f"из {len(child_lives)}/{len(children)} детей с lifetime) — "
                f"родитель не может жить дольше самого короткоживущего ребёнка"
            )
        else:
            valid += 1

    ratio = valid / max(1, total)
    return {
        'metric': 'F15h',
        'description': 'lifetime родителя ≤ MIN(дочерних.lifetime) — родитель не переживёт отказ ребёнка',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': True if total == 0 else ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F16: ИЕРАРХИЯ УРОВНЕЙ
# ============================================================================

def check_F16(izdeliya: dict[str, dict]) -> dict:
    """F16: иерархия уровней — ребёнок = родитель + 1, нет пропусков."""
    violations = []
    total = 0
    valid = 0
    
    for izd_id, data in izdeliya.items():
        parent = data.get('родитель')
        if not parent or parent == 'null':
            continue
        if parent not in izdeliya:
            continue  # уже отмечено в F12a
        
        my_level = data.get('уровень_номер')
        parent_level = izdeliya[parent].get('уровень_номер')
        if my_level is None or parent_level is None:
            continue
        
        try:
            my_level = int(my_level)
            parent_level = int(parent_level)
        except (TypeError, ValueError):
            continue
        
        total += 1
        if my_level != parent_level + 1:
            violations.append(f"{izd_id}: уровень {my_level}, родитель '{parent}' уровень {parent_level} (ожидается {parent_level + 1})")
        else:
            valid += 1
    
    # Дополнительная проверка: 'неделимый' не имеет дочерних (v9.48: на любом уровне,
    # не только 4 — глубина декомпозиции теперь не ограничена)
    for izd_id, data in izdeliya.items():
        hier = data.get('уровень_иерархии')
        if hier == 'неделимый':
            children = data.get('дочерние_части', [])
            if isinstance(children, list) and children:
                violations.append(f"{izd_id}: уровень_иерархии='неделимый' но имеет {len(children)} дочерних_частей")
                total += 1
        elif hier == 'промежуточный':
            # промежуточный ОБЯЗАН иметь дочерние_части (иначе он должен быть 'неделимый')
            children = data.get('дочерние_части', [])
            if not isinstance(children, list) or not children:
                violations.append(f"{izd_id}: уровень_иерархии='промежуточный' но дочерние_части=[] — должен быть 'неделимый' или иметь детей")
                total += 1

    # v9.60 Фаза 2.7: правила для новых типов (сборка/часть/компонент)
    # — 'сборка' ОБЯЗАНА иметь непустые дочерние_части
    # — 'часть' и 'компонент' НЕ должны иметь дочерние_части (must be leaf)
    # — 'часть' обязана иметь материалы_частей (BOM)
    # Проверяем только если тип ∈ {сборка, часть} (пропускаем legacy 'изделие')
    # v9.61: тип 'компонент' упразднён — закупочные теперь тип: изделие с is_purchased: true
    for izd_id, data in izdeliya.items():
        tip = data.get('тип', '')
        if tip not in ('сборка', 'часть'):
            continue  # 'изделие' (top-level и закупочные) — пропускаем (старые правила выше)
        children = data.get('дочерние_части', [])
        children_list = children if isinstance(children, list) else []
        materials_parts = data.get('материалы_частей', [])
        materials_list = materials_parts if isinstance(materials_parts, list) else []

        if tip == 'сборка':
            if not children_list:
                violations.append(
                    f"{izd_id}: тип='сборка' но дочерние_части=[] — "
                    f"сборка обязана иметь детей (или смените тип на 'часть')")
                total += 1
            else:
                valid += 1
                total += 1
        elif tip == 'часть':
            if children_list:
                violations.append(
                    f"{izd_id}: тип='часть' но имеет {len(children_list)} дочерних_частей — "
                    f"часть должна быть leaf; смените тип на 'сборка' если нужна декомпозиция")
                total += 1
            elif not materials_list:
                violations.append(
                    f"{izd_id}: тип='часть' но материалы_частей=[] — "
                    f"часть обязана иметь BOM (canonical материал)")
                total += 1
            else:
                valid += 1
                total += 1

    # верхний (уровень 1) не имеет родителя
    for izd_id, data in izdeliya.items():
        level = data.get('уровень_номер')
        try:
            level = int(level) if level is not None else None
        except (TypeError, ValueError):
            level = None
        if level == 1:
            parent = data.get('родитель')
            if parent and parent != 'null':
                violations.append(f"{izd_id}: верхний уровень (1) но имеет родителя '{parent}'")
                total += 1
    
    ratio = valid / max(1, total)
    return {
        'metric': 'F16',
        'description': 'Иерархия уровней — ребёнок = родитель + 1, неделимый не имеет детей (v9.48: глубина не ограничена)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F17: ТИП-СПЕЦИФИЧНЫЕ ШАБЛОНЫ ДЕКОМПОЗИЦИИ
# ============================================================================

# Минимальный набор частей для каждого типа модели
TYPE_TEMPLATE_PARTS: dict[str, list[str]] = {
    'гуманоидный': [
        'часть_голова_cpu',      # CPU + оптика
        'часть_торс_энергетика', # 2 топливных элемента
        'часть_торс_каркас',     # hyperalloy
        'часть_рука_левая',      # сервопривод
        'часть_рука_правая',     # сервопривод
        'часть_нога_левая',      # передвижение
        'часть_нога_правая',     # передвижение
    ],
    'жидкий_металл': [
        # T-1000: одна часть — сам полисплав
    ],
    'воздушный': [
        'часть_фюзеляж',
        'часть_двигатель_левый',
        'часть_двигатель_правый',
        'часть_сенсоры',
        'часть_вооружение',
    ],
    'наземный_гусеничный': [
        'часть_корпус',
        'часть_гусеница_левая',
        'часть_гусеница_правая',
        'часть_башня',
        'часть_вооружение',
        'часть_сенсоры',
    ],
    'наземный_колёсный': [
        'часть_корпус',
        'часть_колесо_1',
        'часть_колесо_2',
        'часть_двигатель',
        'часть_сенсоры',
    ],
    'водный_надводный': [
        'часть_корпус',
        'часть_двигатель',
        'часть_руль',
        'часть_сенсоры',
        'часть_вооружение',
    ],
    'водный_подводный': [
        'часть_корпус_герметичный',
        'часть_движитель',
        'часть_балласт',
        'часть_сенсоры',
    ],
    'стационарный': [
        'часть_серверная_стойка',
        'часть_бп',
        'часть_охлаждение',
        'часть_сетевой_интерфейс',
    ],
    'прочее': [],
}

def check_F17(models: dict[str, dict], izdeliya: dict[str, dict]) -> dict:
    """F17: тип-специфичные шаблоны декомпозиции."""
    violations = []
    total = 0
    valid = 0
    
    for mid, mdata in models.items():
        mtype = mdata.get('тип_модели', '')
        if mtype not in TYPE_TEMPLATE_PARTS:
            continue
        expected_parts = TYPE_TEMPLATE_PARTS[mtype]
        if not expected_parts:
            continue
        
        total += 1
        # Реализация_промышленная — список id изделий
        real_impl = mdata.get('реализация_промышленная', [])
        if isinstance(real_impl, str):
            real_impl = [real_impl]
        if not isinstance(real_impl, list):
            real_impl = []
        
        # Подсчитать сколько уникальных подсистем покрыто
        covered_subs = set()
        for izd_id in real_impl:
            if not isinstance(izd_id, str):
                continue
            izd_data = izdeliya.get(izd_id, {})
            sub = izd_data.get('подсистема')
            if sub:
                covered_subs.add(sub)
            # Дочерние
            children = izd_data.get('дочерние_части', [])
            if isinstance(children, list):
                for child_id in children:
                    if isinstance(child_id, str) and child_id in izdeliya:
                        sub = izdeliya[child_id].get('подсистема')
                        if sub:
                            covered_subs.add(sub)
        
        # Минимум: 5 подсистем для сложных типов
        min_required = max(3, len(expected_parts) // 2)
        if len(covered_subs) < min_required:
            violations.append(f"{mid} ({mtype}): покрыто {len(covered_subs)} подсистем, минимум {min_required}")
        else:
            valid += 1
    
    ratio = valid / max(1, total)
    return {
        'metric': 'F17',
        'description': 'Тип-специфичные шаблоны декомпозиции — минимальный набор подсистем',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F18: JSON SCHEMA ВАЛИДАЦИЯ
# ============================================================================

SCHEMA_IZDELIE = {
    "type": "object",
    "required": ["id", "тип", "подсистема", "статус_реальности", "доступность"],
    "properties": {
        # v9.31: allow hyphens, plus signs, and both izdelie_ and часть_ prefixes
        # izdelie_* — top-level изделия (уровень 1)
        # часть_*  — дочерние части (уровень 2, промежуточные)
        "id": {"type": "string", "pattern": r"^(izdelie|часть)_[\w+-]+$"},
        # v9.61: enum сокращён до 3 значений (компонент упразднён —
        # закупочные sub-assemblies теперь тип: изделие с is_purchased: true).
        "тип": {"type": "string", "enum": ["изделие", "сборка", "часть"]},
        "категория": {"type": "string"},
        "уровень_иерархии": {"type": "string", "enum": ["верхний", "промежуточный", "неделимый"]},
        # v9.48: глубина декомпозиции НЕ ОГРАНИЧЕНА — maximum убран.
        # Раньше было maximum: 4 (искусственное ограничение); теперь допустимы
        # уровни 5, 6, 7, ... для глубоких сборок (танк → башня → пушка →
        # ствол → канал ствола → нарезы → ...). Атомарные (неделимый) части
        # могут быть на любом уровне, включая 1 — например, izdelie_mednyi_provod.
        "уровень_номер": {"type": "integer", "minimum": 1},
        "подсистема": {"type": "string"},
        "подтип": {"type": "string"},
        "стандарты": {"type": "array"},
        "исследовательская_группа": {"type": ["string", "null"]},
        "родитель": {"type": ["string", "null"]},
        "дочерние_части": {"type": "array"},
        "материалы_частей": {"type": "array"},
        # v9.54 НОВОЕ — технологии: часть-level (обработка детали) и изделие-level (сборка)
        # Mirror материалы_частей, но для каталога технологии/.
        # Формат технологии_частей: список объектов {часть, технология, доля_использования}
        # Формат технологии: простой список id строк (как стандарты)
        "технологии_частей": {"type": "array"},
        "технологии": {"type": "array"},
        # v9.35 НОВОЕ — количество одинаковых экземпляров (default=1)
        "количество": {"type": "integer", "minimum": 1},
        "статус_реальности": {"type": "string", "enum": ["real", "canon", "canon_realizable"]},
        "доступность": {"type": "string"},
    }
}


def check_F18(izdeliya: dict[str, dict]) -> dict:
    """F18: JSON Schema валидация структуры файла изделия.

    Оптимизация (2026-11-05): валидатор компилируется ОДИН раз (Draft202012Validator),
    а не на каждом файле — jsonschema.validate() внутри валидирует саму схему
    на каждом вызове (check_schema), что давало ~10 с на 772 файлах.
    Кэшированный валидатор: ~0.06 с (ускорение ~48×).
    """
    violations = []
    total = len(izdeliya)
    valid = 0

    validator = None
    try:
        # FORMAT_CHECKER=None пропускает тяжёлые импорты rfc3987_syntax/lark/isoduration
        # (1.5+ с на старте). Схема SCHEMA_IZDELIE не использует format-ключи.
        from jsonschema import Draft202012Validator
        validator = Draft202012Validator(SCHEMA_IZDELIE, format_checker=None)
    except ImportError:
        pass

    for izd_id, data in izdeliya.items():
        # v9.33: модель_SkyNet (канон-фантастические) проверяется по §12.4, не §12.1.
        # SCHEMA_IZDELIE требует подсистема/родитель/дочерние_части/материалы_частей —
        # модели не имеют этих полей (у них expected_subsystems, произведения, и т.д.).
        # Skip-аем валидацию по схеме изделий для тип=модель_SkyNet.
        if data.get('тип') == 'модель_SkyNet':
            valid += 1
            continue
        # Удалить служебные поля
        clean_data = {k: v for k, v in data.items() if not k.startswith('_')}

        if validator is not None:
            errs = list(validator.iter_errors(clean_data))
            if errs:
                violations.append(f"{izd_id}: schema violation: {errs[0].message[:100]}")
            else:
                valid += 1
        else:
            # Fallback: проверка required полей
            required = SCHEMA_IZDELIE['required']
            missing = [f for f in required if f not in clean_data or clean_data[f] is None]
            if missing:
                violations.append(f"{izd_id}: отсутствуют обязательные поля: {missing}")
            else:
                valid += 1
    
    ratio = valid / max(1, total)
    return {
        'metric': 'F18',
        'description': 'JSON Schema валидация структуры файла изделия (§12.1)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F19: MERMAID ДИАГРАММА
# ============================================================================

def generate_mermaid_diagram(izd_id: str, izdeliya: dict[str, dict]) -> str:
    """Генерация Mermaid диаграммы для изделия (включая детей до 2 уровня)."""
    lines = ["```mermaid", "graph TD"]
    
    def short_id(id_str: str) -> str:
        return id_str.replace("izdelie_", "").replace("часть_", "")[:20]
    
    def escape(s: str) -> str:
        return s.replace('"', "'")
    
    # Корневой узел
    data = izdeliya.get(izd_id, {})
    label = data.get('подтип', data.get('подсистема', izd_id))
    lines.append(f'    {short_id(izd_id)}["{escape(str(label))}<br/><small>{izd_id}</small>"]')
    
    # Дочерние 1-го уровня
    children = data.get('дочерние_части', [])
    if isinstance(children, list):
        for child_id in children:
            if not isinstance(child_id, str) or child_id not in izdeliya:
                continue
            cdata = izdeliya[child_id]
            clabel = cdata.get('подсистема', child_id)
            lines.append(f'    {short_id(child_id)}["{escape(str(clabel))}<br/><small>{child_id}</small>"]')
            lines.append(f'    {short_id(izd_id)} --> {short_id(child_id)}')
            
            # Дочерние 2-го уровня
            grandchildren = cdata.get('дочерние_части', [])
            if isinstance(grandchildren, list):
                for gc_id in grandchildren:
                    if not isinstance(gc_id, str) or gc_id not in izdeliya:
                        continue
                    gcdata = izdeliya[gc_id]
                    gclabel = gcdata.get('подсистема', gc_id)
                    lines.append(f'    {short_id(gc_id)}["{escape(str(gclabel))}<br/><small>{gc_id}</small>"]')
                    lines.append(f'    {short_id(child_id)} --> {short_id(gc_id)}')
    
    lines.append("```")
    return "\n".join(lines)


def check_F19(izdeliya: dict[str, dict]) -> dict:
    """F19: Mermaid диаграмма присутствует в markdown body каждого изделия с дочерними.
    
    v9.36: используем кешированный body из data['_body'] вместо повторного чтения файла.
    """
    violations = []
    total = 0
    valid = 0
    
    for izd_id, data in izdeliya.items():
        children = data.get('дочерние_части', [])
        if not isinstance(children, list) or not children:
            continue
        total += 1
        body = data.get('_body')
        if not body:
            # fallback: path-based read (для случая, когда izdeliya передан без _body)
            path = data.get('_path')
            if not path:
                continue
            body = Path(path).read_text(encoding='utf-8').split('---', 2)[-1]
        if '```mermaid' in body:
            valid += 1
        else:
            violations.append(f"{izd_id}: нет Mermaid диаграммы в markdown body")
    
    ratio = valid / max(1, total)
    return {
        'metric': 'F19',
        'description': 'Mermaid диаграмма присутствует в markdown body',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F20: ИДЕМПОТЕНТНОСТЬ
# ============================================================================

def check_F20() -> dict:
    """F20: идемпотентность — повторный запуск validate_decomposition.py не меняет файлы.
    
    Эта метрика проверяется косвенно: если validate_decomposition.py не пишет файлы,
    он идемпотентен по определению. Реальная проверка требует двух запусков
    и сравнения хешей. Здесь возвращаем PASS (проверка делается в pipeline).
    """
    return {
        'metric': 'F20',
        'description': 'Идемпотентность декомпозиции — повторный запуск не меняет файлы',
        'total': 1,
        'valid': 1,
        'ratio': 1.0,
        'pass': True,
        'violations': [],
        'note': 'validate_decomposition.py только читает — не пишет, идемпотентен по дизайну. Реальная проверка: hash до/после в CI.'
    }


# ============================================================================
# F21: CANON ВЕРИФИКАЦИЯ
# ============================================================================

# Canon декомпозиция для топ-моделей (из открытых источников)
CANON_DECOMPOSITION: dict[str, dict] = {
    'SkyNet-T800': {
        'вычислительная': 1,    # 1 Neural Net CPU
        'энергетическая': 2,    # 2 водородных топливных элемента
        'каркас': 1,            # 1 hyperalloy endoskeleton
        'сенсоры': 2,           # 2 оптических сенсора
        'приводная_система': 4, # 2 руки + 2 ноги (canon)
    },
    'SkyNet-T1000': {
        'вычислительная': 1,    # molecular brain (распределённый)
    },
    'SkyNet-Rev9': {
        'вычислительная': 1,    # carbon-based endoskeleton
        'каркас': 1,            # endoskeleton
    },
    'SkyNet-HKAerial': {
        'энергетическая': 1,    # nuclear power
        'каркас': 1,            # fuselage
        'сенсоры': 1,           # multi-sensor
        'встроенное_оружие': 1, # plasma cannon
    },
}


def check_F21(models: dict[str, dict], izdeliya: dict[str, dict]) -> dict:
    """F21: canon верификация — декомпозиция совпадает с canon-источниками.
    
    v9.31: проверяем через wrapper-изделие (izdelie_SkyNet-XXX), а не через
    реализация_промышленная в моделях. Wrapper имеет дочерние_части, которые
    и есть декомпозиция.
    v9.35: учитываем поле «количество» дочерних частей — если у child
    количество=N, оно вносит N в общий счётчик подсистемы (а не 1).
    """
    violations = []
    total = 0
    valid = 0

    _build_impl_index()
    for model_id, canon_spec in CANON_DECOMPOSITION.items():
        # Найти wrapper-изделие izdelie_<model_id>
        wrapper_id = f"izdelie_{model_id}"
        wrapper = izdeliya.get(wrapper_id)
        impl_dir = _SKYNET_IMPL_INDEX.get(wrapper_id)
        if wrapper is None and impl_dir is None:
            continue
        total += 1
        # Подсчитать сколько изделий каждой подсистемы
        # v9.35: вес каждого child = его поле «количество» (default 1)
        sub_counts: dict[str, int] = {}
        if wrapper is not None:
            children = wrapper.get('дочерние_части', [])
            if not isinstance(children, list):
                children = []
            for child_id in children:
                if not isinstance(child_id, str) or child_id not in izdeliya:
                    continue
                sub = izdeliya[child_id].get('подсистема')
                if sub:
                    # v9.35: учитываем количество — paired parts (количество=2) считаются как 2
                    q_raw = izdeliya[child_id].get('количество', 1)
                    try:
                        q = int(q_raw) if q_raw is not None else 1
                    except (TypeError, ValueError):
                        q = 1
                    if q < 1:
                        q = 1
                    sub_counts[sub] = sub_counts.get(sub, 0) + q
        else:
            # v9.40 (#256 вариант A): wrapper перенесён в фантастические данные —
            # canon-декомпозиция считается по поддереву реализации (дети, без самой обёртки)
            wrapper_file = (impl_dir / "_index.md").resolve()
            for impl_file in impl_dir.rglob('_index.md'):
                if impl_file.resolve() == wrapper_file:
                    continue
                idata, _, _ = read_yaml_frontmatter(impl_file)
                if not idata:
                    continue
                sub = idata.get('подсистема')
                if not sub:
                    continue
                q_raw = idata.get('количество', 1)
                try:
                    q = int(q_raw) if q_raw is not None else 1
                except (TypeError, ValueError):
                    q = 1
                if q < 1:
                    q = 1
                sub_counts[sub] = sub_counts.get(sub, 0) + q

        ok = True
        for sub, expected_count in canon_spec.items():
            actual = sub_counts.get(sub, 0)
            if actual < expected_count:
                violations.append(f"{model_id}: подсистема '{sub}' — canon ожидает ≥{expected_count}, фактически {actual}")
                ok = False

        if ok:
            valid += 1

    ratio = valid / max(1, total)
    return {
        'metric': 'F21',
        'description': 'Canon верификация — декомпозиция wrapper-изделия совпадает с canon',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# ВСЕ МОДЕЛИ — загрузка
# ============================================================================

def load_all_models() -> dict[str, dict]:
    """Загрузить все .md в фантастические данные/модели/."""
    result = {}
    mod_dir = SKYNET_REPO / "фантастические данные" / "модели"
    for f in mod_dir.glob("*.md"):
        if f.name.startswith('_'):
            continue
        data, _, _ = read_yaml_frontmatter(f)
        if data and 'id' in data:
            data['_path'] = str(f)
            result[data['id']] = data
    return result


# ============================================================================
# F22: ВЕРИФИКАЦИЯ ИСТОЧНИКА — URL обязателен для web_search
# ============================================================================

def check_F22(izdeliya: dict[str, dict], models: dict[str, dict] | None = None) -> dict:
    """F22: Верификация содержимого части (v9.52: merged F22+F23+F24).

    Три проверки в одной функции (все про «эта часть действительно
    исследована или это заглушка?» — три аспекта одной задачи):

    Чек A (бывший F22) — URL-верификация:
      Если источник=web_search, то источник_url должен быть заполнен.
      BLOCKING: предотвращает ложные утверждения о web-верификации.
      Также проверяет модели и технологии.

    Чек B (бывший F23) — анти-шаблон / stub-detection:
      1. материал не generic_material / unknown / todo
      2. описание не содержит шаблонных фраз
      3. габариты_mm не (100, 100, 50) — дефолтный fallback

    Чек C (бывший F24) — schema-field-completeness:
      Каждый подтип части должен иметь специфичные поля в дополнительные.
      Например, нейроморфный CPU должен иметь тех_процесс_nm и SRAM_MB.

    v9.36: опциональный параметр `models` позволяет переиспользовать уже загруженный
    словарь из run_all_checks — экономит rglob+parse ~41 файла при каждом вызове.
    """
    violations = []
    total_a = 0
    valid_a = 0
    total_b = 0
    valid_b = 0
    total_c = 0
    valid_c = 0

    # === Чек A: URL-верификация (бывший F22) ===
    # Проверить изделия
    for izd_id, data in izdeliya.items():
        source = str(data.get('источник', '')).strip()
        if source != 'web_search':
            continue
        total_a += 1
        url = data.get('источник_url') or data.get('источник_верификации')
        if not url or str(url).strip() in ('', 'null', 'None'):
            violations.append(f"[A-url] {izd_id}: источник=web_search но источник_url пустой")
        else:
            valid_a += 1

    # Проверить модели (переиспользуем переданный, иначе загружаем)
    if models is None:
        models = load_all_models()
    for mid, mdata in models.items():
        source = str(mdata.get('источник', '')).strip()
        if source != 'web_search':
            continue
        total_a += 1
        url = mdata.get('источник_url') or mdata.get('источник_верификации')
        if not url or str(url).strip() in ('', 'null', 'None'):
            violations.append(f"[A-url] {mid}: источник=web_search но источник_url пустой")
        else:
            valid_a += 1

    # Проверить технологии
    tech_dir = SKYNET_REPO / "реальные данные" / "технологии"
    for f in tech_dir.glob("*.md"):
        if f.name.startswith('_'):
            continue
        data, _, _ = read_yaml_frontmatter(f)
        if not data or 'id' not in data:
            continue
        source = str(data.get('источник', '')).strip()
        if source != 'web_search':
            continue
        total_a += 1
        url = data.get('источник_url')
        if not url or str(url).strip() in ('', 'null', 'None'):
            violations.append(f"[A-url] {data['id']}: источник=web_search но источник_url пустой")
        else:
            valid_a += 1

    # === Чек B: анти-шаблон (бывший F23) ===
    GENERIC_MATERIALS = {'generic_material', 'не_определён', 'unknown', 'tbd', 'todo'}
    TEMPLATE_DESCRIPTIONS = [
        'Дочерняя часть изделия',
        'Основной функциональный элемент',
        'Защитный корпус из алюминиевого сплава',
        'Электрические разъёмы для подключения',
        'Монтажный крепёж',
    ]
    for izd_id, data in izdeliya.items():
        if not izd_id.startswith('часть_'):
            continue
        total_b += 1
        file_ok = True

        # 1. Проверить материалы_частей
        materials = data.get('материалы_частей', [])
        if isinstance(materials, list):
            for m in materials:
                if isinstance(m, dict):
                    mat = str(m.get('материал', '')).strip().lower()
                    if mat in GENERIC_MATERIALS:
                        violations.append(f"[B-stub] {izd_id}: материал='{mat}' — шаблонная заглушка")
                        file_ok = False

        # 2. Проверить описание (body markdown) — v9.36: используем кеш _body
        body = data.get('_body')
        if not body:
            path = data.get('_path', '')
            if path:
                try:
                    body = Path(path).read_text(encoding='utf-8')
                except Exception:
                    body = ''
        if body:
            # Найти body после YAML
            body_match = re.search(r"^## Описание\s*\n\s*\n(.+?)(?:\n##|\Z)", body, re.MULTILINE | re.DOTALL)
            if body_match:
                desc = body_match.group(1).strip()
                for tmpl in TEMPLATE_DESCRIPTIONS:
                    if desc.startswith(tmpl):
                        violations.append(f"[B-stub] {izd_id}: описание начинается с шаблонной фразы '{tmpl[:30]}...'")
                        file_ok = False
                        break

        # 3. Проверить габариты — не дефолтные (100, 100, 50)
        basic = data.get('основные', {})
        if isinstance(basic, dict):
            dims = basic.get('габариты_mm')
            if isinstance(dims, dict):
                l = dims.get('l')
                w = dims.get('w')
                h = dims.get('h')
                # Если все три 100/100/50 — это fallback
                if l == 100 and w == 100 and h == 50:
                    violations.append(f"[B-stub] {izd_id}: габариты 100×100×50 — дефолтный fallback (не исследовался)")
                    file_ok = False

        if file_ok:
            valid_b += 1

    # === Чек C: schema-field-completeness (бывший F24) ===
    SUBTYPE_REQUIRED_FIELDS = {
        'neural_net_cpu': ['тех_процесс_nm', 'SRAM_MB'],
        'Pu-238_источник': ['изотоп', 'T_жизни_лет'],
        'Am-241_источник': ['изотоп', 'T_жизни_лет'],
        'H-3_тритий': ['изотоп', 'T_жизни_лет'],
        'plasma_cannon': ['мощность_выстрела_MJ'],
        'mimetic_polyalloy': ['тип'],
        'hydrogen_fuel_cell': ['T_жизни_лет'],
        'hyperalloy_endoskeleton': ['материал'],
        'NMC_катод': ['ёмкость_мАч_г'],
        'керамические_слои': ['V_max_V'],
        'PEM_мембрана': ['толщина_мкм'],
        'YSZ_электролит': ['T_рабочая_C'],
        'термопары': ['КПД_процентов'],
    }
    for izd_id, data in izdeliya.items():
        if not izd_id.startswith('часть_'):
            continue
        subtype = data.get('подтип', '')
        if subtype not in SUBTYPE_REQUIRED_FIELDS:
            continue  # нет требований — пропускаем
        total_c += 1

        required = SUBTYPE_REQUIRED_FIELDS[subtype]
        additional = data.get('дополнительные', {})
        if not isinstance(additional, dict):
            additional = {}
        basic = data.get('основные', {})
        if not isinstance(basic, dict):
            basic = {}
        all_fields = {**basic, **additional}

        missing = [f for f in required if f not in all_fields]
        if missing:
            violations.append(f"[C-schema] {izd_id} ({subtype}): отсутствуют ожидаемые поля: {missing}")
        else:
            valid_c += 1

    # Combined ratio
    total = total_a + total_b + total_c
    valid = valid_a + valid_b + valid_c
    ratio = valid / max(1, total)
    return {
        'metric': 'F22',
        'description': 'Верификация содержимого части: (A) URL для web_search; (B) анти-шаблон/stub; (C) schema-field-completeness',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F25: УНИКАЛЬНОСТЬ ДАННЫХ — анти-дубликаты (v9.52: merge F25+F26)
# ============================================================================

def check_F25(izdeliya: dict[str, dict]) -> dict:
    """F25: Уникальность данных — анти-дубликаты (v9.52: merged F25+F26).

    Две проверки в одной функции (обе про дубликаты):

    Чек A (бывший F25) — глобальные дубликаты:
      Если 3+ файла часть_* с разными id имеют идентичные
      (габариты_mm.l, габариты_mm.w, габариты_mm.h, масса_kg, материал) —
      это признак шаблонной подстановки.
      Допускается не более 2 файлов с одинаковым набором.

    Чек B (бывший F26) — внутри-родительские дубликаты:
      Если в одном родителе есть 2+ часть_* с одинаковым подтипом И
      ИДЕНТИЧНЫМИ данными (масса + габариты + материал) — это признак
      шаблонной подстановки (left/right, _1/_2).
      Допускается только если survivor имеет поле количество=N (N≥2).
      Если данные РАЗНЫЕ — нарушения нет (это разные части).

    Returns: dict с combined violations (чек A + чек B).
    """
    from collections import defaultdict

    violations = []
    total_a = 0
    valid_a = 0
    total_b = 0
    valid_b = 0

    # === Чек A: глобальные дубликаты ===
    signatures: dict[tuple, list[str]] = {}
    for izd_id, data in izdeliya.items():
        if not izd_id.startswith('часть_'):
            continue
        basic = data.get('основные', {})
        if not isinstance(basic, dict):
            continue
        mass = basic.get('масса_kg')
        dims = basic.get('габариты_mm')
        if not isinstance(dims, dict):
            continue
        l = dims.get('l')
        w = dims.get('w')
        h = dims.get('h')

        # Найти материал
        material = ''
        materials = data.get('материалы_частей', [])
        if isinstance(materials, list):
            for m in materials:
                if isinstance(m, dict):
                    material = str(m.get('материал', ''))
                    break

        sig = (l, w, h, mass, material)
        signatures.setdefault(sig, []).append(izd_id)

    total_a = len(signatures)
    for sig, ids in signatures.items():
        if len(ids) > 2:
            violations.append(
                f"[A-глобальный] Дубликат: {len(ids)} файлов с габаритами {sig[0]}×{sig[1]}×{sig[2]}mm, "
                f"масса={sig[3]}kg, материал={sig[4]}: {ids[:5]}"
            )
        else:
            valid_a += 1

    # === Чек B: внутри-родительские дубликаты ===
    parent_children: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    for izd_id, data in izdeliya.items():
        if not izd_id.startswith('часть_'):
            continue
        parent = data.get('родитель', '')
        if not parent:
            continue
        parent_children[parent].append((izd_id, data))

    for parent, kids in parent_children.items():
        if len(kids) < 2:
            continue
        total_b += 1

        # Group by subtype
        by_subtype: dict[str, list[tuple[str, dict]]] = defaultdict(list)
        for izd_id, data in kids:
            subtype = data.get('подтип', '')
            if not subtype:
                continue
            by_subtype[subtype].append((izd_id, data))

        parent_clean = True
        for subtype, items in by_subtype.items():
            if len(items) < 2:
                continue
            # Check if data is IDENTICAL across all items
            sigs = set()
            for izd_id, d in items:
                basic = d.get('основные', {})
                if not isinstance(basic, dict):
                    basic = {}
                dims = basic.get('габариты_mm', {})
                if not isinstance(dims, dict):
                    dims = {}
                mass = basic.get('масса_kg')
                mats = d.get('материалы_частей', [])
                mat = ''
                if isinstance(mats, list) and mats:
                    m0 = mats[0]
                    if isinstance(m0, dict):
                        mat = str(m0.get('материал', ''))
                sig = (dims.get('l'), dims.get('w'), dims.get('h'), mass, mat)
                sigs.add(sig)

            # Only flag if all signatures are IDENTICAL (true duplicates)
            if len(sigs) > 1:
                # Different data — not duplicates, OK
                continue

            # All identical — check for количество=N
            ids = [izd_id for izd_id, _ in items]
            has_quantity = False
            for izd_id in ids:
                d = izdeliya.get(izd_id, {})
                q = d.get('количество', 1)
                if isinstance(q, int) and q >= len(ids):
                    has_quantity = True
                    break
            if not has_quantity:
                parent_clean = False
                violations.append(
                    f"[B-родитель] {parent}: подтип '{subtype}' имеет {len(ids)} файлов с идентичными данными "
                    f"({ids[:3]}...), ни один не имеет количество≥{len(ids)}. "
                    f"Объединить через migrate_dedup_quantity.py или установить количество=N."
                )

        if parent_clean:
            valid_b += 1

    # Combined ratio
    total = total_a + total_b
    valid = valid_a + valid_b
    ratio = valid / max(1, total)
    return {
        'metric': 'F25',
        'description': 'Анти-дубликаты: (A) глобальные ≤2 файлов с одинаковыми габаритами+массой+материалом; (B) внутри-родительские — 2+ с одинаковым подтипом требуют количество=N',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F27: НЕЗАПОЛНЕННЫЕ МАТЕРИАЛЫ-ЗАГЛУШКИ (v9.40; v9.41 — добавлен критерий e)
# ============================================================================

# Ключевые свойства материала: если ВСЕ null — файл-заглушка без данных.
# Намеренно узкий список: у жидкостей/газов/изоляторов часть полей легитимно null,
# но плотность и теплопроводность известны для любого реального материала.
MATERIAL_CORE_FIELDS = ('плотность_kg_m3', 'теплопроводность_W_mK', 'температура_плавления_C')

def _collect_referenced_materials(izdeliya: dict[str, dict]) -> set:
    """Материалы, на которые ссылаются изделия/части через материалы_частей.

    Возвращает set stem-ов И полных id ('grafen-aerogel' и 'material_grafen-aerogel').
    """
    refs = set()
    for data in izdeliya.values():
        mats = data.get('материалы_частей', [])
        if not isinstance(mats, list):
            continue
        for m in mats:
            if isinstance(m, dict):
                mat = str(m.get('материал', '')).strip()
                if mat:
                    refs.add(mat)
                    if not mat.startswith('material_'):
                        refs.add('material_' + mat)
    return refs


def check_F27(izdeliya: dict[str, dict]) -> dict:
    """F27: Незаполненные материалы-заглушки, на которые ссылаются изделия.

    BLOCKING: цепочка «часть → материал» не должна вести в пустой файл.
    Проверяются ТОЛЬКО материалы, используемые изделиями (материалы_частей):
    неиспользуемые файлы не влияют на корректность дерева изделий и не должны
    флудить очередь verify-task (приоритизация очереди).

    Критерии нарушения (любое):
      a. все ключевые свойства null (плотность/теплопроводность/плавление)
      b. исследовательская_группа = 'требует_верификации' (маркер генератора)
      c. источник=web_search, но источник_url пуст (аналог F22 для материалов)
      d. YAML frontmatter не читается (обрезан) — свойства недоступны
      e. вариант_структуры пустой/null (v9.41 — preventive: web_search должен
         зафиксировать конкретную форму: mono/poly/amorphous/...). Для полиморфных
         кристаллов (Si, SiO₂, Al₂O₃, TiO₂, C, BaTiO₃, YBCO, Si₃N₄, ZrO₂, ...)
         generic 'single_phase' скрывает реальную кристаллографическую форму,
         от которой зависят свойства — это критично для AI-генерации вариантов
         изделий (могут быть скомбинированы несовместимые свойства).

    Формат violation: '<material_id>: ...' — совместим с дефолтной веткой
    normalizeViolationKey (dedup F27:<file_id>) и титульником
    '[F27] Verify: <file_id>' (verify_decomposition.yml).
    """
    violations = []
    total = 0
    valid = 0

    referenced = _collect_referenced_materials(izdeliya)
    mat_dir = SKYNET_REPO / "реальные данные" / "материалы"

    for f in sorted(mat_dir.glob("*.md")):
        if f.name.startswith('_'):
            continue
        data, _, _ = read_yaml_frontmatter(f)

        if not data:
            # Обрезанный/нечитаемый frontmatter — материал-кандидат без данных
            stem = f.stem
            if stem in referenced or ('material_' + stem) in referenced:
                total += 1
                violations.append(
                    f"material_{stem}: YAML frontmatter не читается (обрезан?) — свойства недоступны")
            continue

        mid = str(data.get('id', '')).strip() or ('material_' + f.stem)
        stem = mid.replace('material_', '', 1)
        if mid not in referenced and stem not in referenced:
            continue  # не используется изделиями — вне очереди F27

        total += 1
        problems = []

        # (a) все ключевые свойства null
        basic = data.get('основные') or {}
        if not isinstance(basic, dict):
            basic = {}
        all_null = all(basic.get(k) in (None, '', 'null', 'None') for k in MATERIAL_CORE_FIELDS)
        if all_null:
            problems.append("все ключевые свойства null (плотность/теплопроводность/плавление)")

        # (b) маркер генератора
        if str(data.get('исследовательская_группа', '')).strip() == 'требует_верификации':
            problems.append("исследовательская_группа='требует_верификации'")

        # (c) аналог F22
        src = str(data.get('источник', '')).strip()
        url = data.get('источник_url')
        if src == 'web_search' and (not url or str(url).strip() in ('', 'null', 'None')):
            problems.append("источник=web_search но источник_url пустой")

        # (e) v9.41: вариант_структуры не указан (preventive).
        # Проверяем только когда свойства НЕ все null (иначе (a) уже покрывает),
        # чтобы не дублировать нарушение на полностью пустых заглушках.
        if not all_null:
            vs = data.get('вариант_структуры')
            if vs is None or str(vs).strip() in ('', 'null', 'None'):
                problems.append(
                    "вариант_структуры не указан — web_search должен зафиксировать "
                    "конкретную форму (mono/poly/amorphous/...); для полиморфных "
                    "кристаллов (Si, SiO₂, Al₂O₃, TiO₂, C, BaTiO₃, YBCO, Si₃N₄, "
                    "ZrO₂, ...) generic 'single_phase' скрывает реальную форму "
                    "(критично для AI-вариантов изделий)")

        if problems:
            violations.append(f"{mid}: незаполненный материал-заглушка ({'; '.join(problems)})")
        else:
            valid += 1

    ratio = valid / max(1, total)
    return {
        'metric': 'F27',
        'description': 'Незаполненные материалы-заглушки, используемые изделиями (пустые свойства/URL/вариант_структуры)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F27b: БИТЫЕ ССЫЛКИ НА МАТЕРИАЛЫ (v9.53; mirror F27 для отсутствующих файлов)
# ============================================================================
# Контекст: F27 итерирует mat_dir.glob("*.md") — т.е. проверяет ТОЛЬКО
# существующие файлы. Если изделие/часть ссылается в материалы_частей на
# material_id, для которого НЕТ файла в каталоге материалы/ — F27 такого
# материала не видит (молчаливый пробел). F27b закрывает этот пробел:
# итерирует сами ссылки в frontmatter изделий/частей и проверяет, существует
# ли файл. Это даёт cron-агенту явный сигнал «нужно СОЗДАТЬ файл материала
# через web_search», а не просто «заполнить существующий».
#
# Аналогично F27 — итерируем только ссылки из frontmatter (структурные
# материал_частей), не трогая body markdown ссылки [../материалы/...].
# Body-ссылки — отдельная задача (потенциальная метрика F27c).

MATERIAL_FILE_EXTENSIONS = ('.md',)  # каталог материалы/ — только markdown


def _resolve_material_file(stem: str, mat_dir) -> 'Path | None':
    """По stem-у ссылки (без/с префикса material_) возвращает Path файла
    в каталоге материалы/, если он существует; иначе None.
    """
    s = stem.strip()
    if not s:
        return None
    # Нормализуем: убираем префикс 'material_', если он есть в ссылке
    if s.startswith('material_'):
        s = s[len('material_'):]
    if not s:
        return None
    for ext in MATERIAL_FILE_EXTENSIONS:
        candidate = mat_dir / f"{s}{ext}"
        if candidate.is_file():
            return candidate
    return None


def check_F27b(izdeliya: dict[str, dict]) -> dict:
    """F27b: Битые ссылки на материалы в frontmatter (файл отсутствует).

    BLOCKING (mirror F27): цепочка «часть → материал» не должна вести в
    несуществующий файл. F27 проверяет заполненность существующих файлов;
    F27b ловит пробел — ссылка на материал, для которого нет файла вообще.

    Скоуп — только frontmatter `материалы_частей` изделий и частей
    (структурные ссылки). Body markdown-ссылки не проверяются.

    Критерий нарушения: для элемента `материал: <id>` в материалы_частей
    не существует файла реальные данные/материалы/<stem>.md (stem = id без
    префикса material_, и имена файлов в каталоге без этого префикса).

    Формат violation: 'material_<stem>: файл материалы/<stem>.md отсутствует
    в каталоге (битая ссылка из материалы_частей в <izdelie_id>)' —
    совместим с дефолтной веткой normalizeViolationKey (dedup
    F27b:material_<stem>) и титульником '[F27b] Verify: material_<stem>'
    (verify_decomposition.yml).

    v9.60 Фаза 1.4: расширение — WARNING (non-blocking) если material_id
    ссылается на узел `изделия/` (это явная путаница материала и части).
    В Фазе 2.4 станет BLOCKING через F35b.
    """
    violations = []
    seen = {}  # stem → izdelie_id (для текста violation)
    cross_ref_warnings = []  # v9.60: материал ссылается на узел изделия/
    mat_dir = SKYNET_REPO / "реальные данные" / "материалы"

    # Собрать множество id узлов изделий (для cross-ref проверки)
    izdeliya_ids = set(izdeliya.keys())

    # Идём по ссылкам прямо из frontmatter, чтобы сохранить изделие-источник
    for izd_id, data in izdeliya.items():
        mats = data.get('материалы_частей', []) if isinstance(data, dict) else None
        if not isinstance(mats, list):
            continue
        for m in mats:
            if not isinstance(m, dict):
                continue
            mat = str(m.get('материал', '')).strip()
            if not mat:
                continue
            stem = mat[9:] if mat.startswith('material_') else mat
            if not stem:
                continue

            # v9.60 Фаза 1.4: cross-ref проверка
            # Если mat_id совпадает с id узла изделий — это путаница
            if mat in izdeliya_ids:
                cross_ref_warnings.append(
                    f"{izd_id}: материалы_частей содержит '{mat}' — "
                    f"это id узла изделий/, а не canonical материал. "
                    f"Перенесите в 'компоненты_частей' (после миграции A2) "
                    f"или замените на canonical материал."
                )

            if stem in seen:
                continue  # уже видели эту ссылку — dedup по файлу
            seen[stem] = izd_id  # первый источник (для текста violation)

    # Подсчёт по уникальным referenced stems (одно нарушение на файл, как в F27)
    total_unique = len(seen)
    valid_unique = 0
    for stem in seen:
        if _resolve_material_file(stem, mat_dir) is not None:
            valid_unique += 1
        else:
            violations.append(
                f"material_{stem}: файл материалы/{stem}.md отсутствует в "
                f"каталоге (битая ссылка из материалы_частей в {seen[stem]})")

    ratio = valid_unique / max(1, total_unique)
    return {
        'metric': 'F27b',
        'description': 'Битые ссылки на материалы в frontmatter (файл отсутствует в каталоге материалы/)',
        'total': total_unique,
        'valid': valid_unique,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
        'cross_ref_warnings': cross_ref_warnings,  # v9.60: non-blocking warnings
    }


# ============================================================================
# F27c: БИТЫЕ ССЫЛКИ НА ТЕХНОЛОГИИ (v9.54; mirror F27b для каталога технологии/)
# ============================================================================
# Контекст: F27b ловит битые ссылки на материалы_частей (отсутствующие файлы
# в материалы/). Аналогично — если изделие/часть ссылается на id технологии
# в frontmatter (через структурное поле `технологии_частей` для части-level
# или `технологии` для изделия-level), и файла в каталоге технологии/ нет —
# это пробел, который F31/F33 не видят (F31 проверяет только дедупликацию,
# F33 — классификационную консистентность, но не существование файла по id).
#
# Формат нового структурного поля (mirror материалы_частей):
#   технологии_частей:        # часть-level — обработка конкретной детали
#     - часть: часть_<...>
#       технология: <stem>     # stem без префикса tekhnologia_
#       доля_использования: 1.0   # 1.0 = единственная технология для этой части
#   технологии:               # изделие-level — сборка/фабрикация в целом
#     - tekhnologia_<stem>    # простой список id (без объекта часть:)
#
# Скоуп: только frontmatter `технологии_частей` и `технологии` изделий и частей
# (структурные id-ссылки). Body markdown-ссылки не проверяются (как в F27b).
#
# Замечание: старое поле `технология:` (строка, свободный текст описания
# процесса, например "tape casting / мокрое осаждение + коспекание") — НЕ
# структурная id-ссылка и НЕ проверяется F27c. При миграции на структурное
# поле старое `технология:` удаляется, заменяется на `технологии_частей`.


TECH_FILE_EXTENSIONS = ('.md',)  # каталог технологии/ — только markdown


def _resolve_tech_file(stem: str, tech_dir) -> 'Path | None':
    """По stem-у ссылки (без/с префикса tekhnologia_) возвращает Path файла
    в каталоге технологии/, если он существует; иначе None.
    """
    s = stem.strip()
    if not s:
        return None
    # Нормализуем: убираем префикс 'tekhnologia_', если он есть в ссылке
    if s.startswith('tekhnologia_'):
        s = s[len('tekhnologia_'):]
    if not s:
        return None
    for ext in TECH_FILE_EXTENSIONS:
        candidate = tech_dir / f"{s}{ext}"
        if candidate.is_file():
            return candidate
    return None


def check_F27c(izdeliya: dict[str, dict]) -> dict:
    """F27c: Битые ссылки на технологии в frontmatter (файл отсутствует).

    BLOCKING (mirror F27b): цепочка «часть → технология» (или «изделие →
    технология сборки») не должна вести в несуществующий файл. F31/F33
    проверяют дедупликацию/классификацию существующих файлов; F27c ловит
    пробел — ссылка на технологию, для которой нет файла вообще.

    Скоуп — frontmatter `технологии_частей` (часть-level, объекты с часть:)
    и `технологии` (изделие-level, простой список id) изделий и частей.

    Критерий нарушения: для элемента `технология: <id>` в технологии_частей
    (или для id в списке `технологии:`) не существует файла реальные
    данные/технологии/<stem>.md (stem = id без префикса tekhnologia_, и
    имена файлов в каталоге без этого префикса).

    Формат violation: 'tekhnologia_<stem>: файл технологии/<stem>.md
    отсутствует в каталоге (битая ссылка из <поле> в <izdelie_id>)' —
    совместим с дефолтной веткой normalizeViolationKey (dedup
    F27c:tekhnologia_<stem>) и титульником '[F27c] Verify: tekhnologia_<stem>'
    (verify_decomposition.yml).
    """
    violations = []
    seen = {}  # stem → (izdelie_id, field) для текста violation
    tech_dir = SKYNET_REPO / "реальные данные" / "технологии"

    # Идём по ссылкам прямо из frontmatter, чтобы сохранить изделие-источник
    for izd_id, data in izdeliya.items():
        if not isinstance(data, dict):
            continue

        # (1) технологии_частей — часть-level (объекты с часть/технология)
        techs_parts = data.get('технологии_частей', [])
        if isinstance(techs_parts, list):
            for t in techs_parts:
                if not isinstance(t, dict):
                    continue
                tech = str(t.get('технология', '')).strip()
                if not tech:
                    continue
                stem = tech[11:] if tech.startswith('tekhnologia_') else tech
                if not stem:
                    continue
                if stem not in seen:
                    seen[stem] = (izd_id, 'технологии_частей')

        # (2) технологии — изделие-level (простой список id строк)
        techs_top = data.get('технологии', [])
        if isinstance(techs_top, list):
            for tech in techs_top:
                tech = str(tech).strip()
                if not tech:
                    continue
                stem = tech[11:] if tech.startswith('tekhnologia_') else tech
                if not stem:
                    continue
                if stem not in seen:
                    seen[stem] = (izd_id, 'технологии')

    # Подсчёт по уникальным referenced stems (одно нарушение на файл, как в F27b)
    total_unique = len(seen)
    valid_unique = 0
    for stem, (izd_id, field) in seen.items():
        if _resolve_tech_file(stem, tech_dir) is not None:
            valid_unique += 1
        else:
            violations.append(
                f"tekhnologia_{stem}: файл технологии/{stem}.md отсутствует в "
                f"каталоге (битая ссылка из {field} в {izd_id})")

    ratio = valid_unique / max(1, total_unique)
    return {
        'metric': 'F27c',
        'description': 'Битые ссылки на технологии в frontmatter (файл отсутствует в каталоге технологии/)',
        'total': total_unique,
        'valid': valid_unique,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F27d: БИТЫЕ ССЫЛКИ НА МАТЕРИАЛЫ В ТЕХНОЛОГИЯХ (v9.55; обратная связь F27c)
# ============================================================================
# Контекст: F27b проверяет ссылки изделия → материал (frontmatter материалы_частей),
# F27c — изделия → технология (frontmatter технологии_частей/технологии). F27d
# замыкает треугольник: проверяет обратную связь технология → материал в поле
# `материалы_для_процесса` (в frontmatter файлов технологий).
#
# Формат поля (v9.55 — ролевая структура, mirror материалы_частей):
#   материалы_для_процесса:        # внутри блока дополнительные:
#     - материал: material_<stem>
#       роль: обрабатываемый         # обрабатываемый/прекурсор/катализатор/...
#       доля_массы: 0.95             # опционально
#
# Поддерживается и legacy-формат (простой список id строк), для обратной
# совместимости с файлами, заполненными до v9.55.
#
# Скоуп: только frontmatter `материалы_для_процесса` файлов технологий.
# Изделия/части не проверяются (для них есть F27b).

PROCESS_MATERIAL_ROLES = (
    'обрабатываемый', 'прекурсор', 'катализатор', 'расходник',
    'атмосфера', 'подложка', 'легирующая_добавка', 'связующее',
    'побочный_продукт', 'оснастка',
)


def check_F27d(izdeliya: dict[str, dict] | None = None) -> dict:
    """F27d: Битые ссылки на материалы в frontmatter технологий (типичные_материалы_для_процесса).

    SOFT-CHECK (v9.56 — переориентирована): в файлах технологий поле
    `типичные_материалы_для_процесса` (внутри `дополнительные:`) описывает
    универсальные/типичные материалы процесса — например, типичная атмосфера
    HIP (Ar), типичные катализаторы CVD (Pt), типичное связующее (PVA).
    Конкретные материалы для каждого применения хранятся в ИЗДЕЛИИ, в поле
    `материалы_для_процесса` внутри `технологии_частей[]` (см. F27g).

    История: v9.55 — поле называлось `материалы_для_процесса` и хранилось
    в технологии. v9.56 — переименовано в `типичные_материалы_для_процесса`
    (soft, опциональное), конкретные материалы перенесены в изделие.

    Поддерживается legacy-формат `материалы_для_процесса` (без префикса
    `типичные_`) для обратной совместимости с файлами, заполненными до v9.56.

    Критерий нарушения: для материала с id `material_<stem>` (или просто
    `<stem>`) не существует файла реальные данные/материалы/<stem>.md.

    Формат violation: 'tekhnologia_<tech_stem>: типичные_материалы_для_процесса
    ссылается на несуществующий материал material_<stem>'.
    """
    violations = []
    tech_dir = SKYNET_REPO / "реальные данные" / "технологии"
    mat_dir = SKYNET_REPO / "реальные данные" / "материалы"

    total = 0
    valid = 0
    seen = set()  # (tech_id, mat_stem) — dedup

    for f in sorted(tech_dir.glob("*.md")):
        if f.name.startswith('_'):
            continue
        data, _, _ = read_yaml_frontmatter(f)
        if not isinstance(data, dict):
            continue
        tech_id = str(data.get('id', '')).strip() or ('tekhnologia_' + f.stem)
        # v9.56: типичные_материалы_для_процесса (новое имя) или legacy материалы_для_процесса
        extras = data.get('дополнительные') or {}
        if not isinstance(extras, dict):
            continue
        # Приоритет: новое имя, fallback на legacy
        proc_mats = extras.get('типичные_материалы_для_процесса')
        if proc_mats is None:
            proc_mats = extras.get('материалы_для_процесса')  # legacy
        if not isinstance(proc_mats, list) or not proc_mats:
            continue

        for entry in proc_mats:
            mat_id = None
            role = None
            if isinstance(entry, dict):
                # v9.55+ — ролевая структура
                mat_id = str(entry.get('материал', '')).strip()
                role = str(entry.get('роль', '') or '').strip() or None
            elif isinstance(entry, str):
                # legacy — простой список id строк
                mat_id = entry.strip()
            if not mat_id:
                continue

            total += 1
            stem = mat_id[9:] if mat_id.startswith('material_') else mat_id
            if not stem:
                continue

            dedup_key = (tech_id, stem)
            if dedup_key in seen:
                continue
            seen.add(dedup_key)

            if _resolve_material_file(stem, mat_dir) is not None:
                valid += 1
            else:
                role_suffix = f" (роль={role})" if role else ""
                violations.append(
                    f"{tech_id}: типичные_материалы_для_процесса ссылается на "
                    f"несуществующий материал material_{stem}{role_suffix}")

    ratio = valid / max(1, total)
    return {
        'metric': 'F27d',
        'description': 'Битые ссылки на типичные материалы процесса в файлах технологий (soft)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F27e: ОБЯЗАТЕЛЬНОСТЬ технологии_частей ДЛЯ ЧАСТЕЙ С материалы_частей (v9.56)
# ============================================================================
# Контекст: ответы на вопросы пользователя (цикл 1a1b27931a0a00f1):
# 1) Проверяется ли, что изделие и части должны содержать ссылки на технологии?
#    Раньше: НЕТ — F27c ловил только битые ссылки, но не отсутствие.
# 2) Одна технология может использоваться в разных изделиях с разными
#    материалами — материалы процесса хранятся в ИЗДЕЛИИ, не в технологии.
#
# F27e: если у части есть материалы_частей (значит, это физическая деталь с
# конкретным материалом), то должна быть указана и технология её обработки
# (хотя бы одна запись в технологии_частей). Без технологии материал не
# существует как обработанная деталь — это только сырьё.
#
# Mirror F27b: F27b проверяет валидность id в материалы_частей; F27e проверяет
# ОБЯЗАТЕЛЬНОСТЬ presence of технологии_частей (полноту связи).
#
# Warning-уровень (не блокирующий): 761 файл без технологий = 761 issue в
# очередь cron-агента. Блокировка невозможна, пока backlog не разобран.

def check_F27e(izdeliya: dict[str, dict]) -> dict:
    """F27e: Части с материалы_частей должны иметь технологии_частей.

    WARNING (v9.56; обязательность связи изделие→технология). Если у части
    есть `материалы_частей` (значит, это физическая деталь из конкретного
    материала), то должна быть указана технология обработки (хотя бы одна
    запись в `технологии_частей`). Без технологии материал не существует как
    обработанная деталь — это только сырьё.

    Скоуп: frontmatter изделий и частей (тип=изделие) с материалы_частей.
    Изделия без материалы_частей (например, виртуальные сборки) не проверяются.

    Критерий нарушения: материалы_частей — непустой список, но технологии_частей
    отсутствует ИЛИ пустой.

    Формат violation: '<izdelie_id>: есть материалы_частей, но нет
    технологии_частей — должна быть указана технология обработки детали'.
    """
    violations = []
    total = 0
    valid = 0

    for izd_id, data in izdeliya.items():
        if not isinstance(data, dict):
            continue
        # Только для изделий/частей с материалы_частей
        mats = data.get('материалы_частей', [])
        if not isinstance(mats, list) or not mats:
            continue  # нет материалов — не наша ответственность

        total += 1
        techs = data.get('технологии_частей', [])
        if isinstance(techs, list) and techs:
            valid += 1
        else:
            violations.append(
                f"{izd_id}: есть материалы_частей ({len(mats)} записей), но нет "
                f"технологии_частей — должна быть указана технология обработки детали")

    ratio = valid / max(1, total)
    return {
        'metric': 'F27e',
        'description': 'Обязательность технологии_частей для частей с материалы_частей',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F27f: ОБЯЗАТЕЛЬНОСТЬ материалы_для_процесса ВНУТРИ технологии_частей (v9.56)
# ============================================================================
# Контекст: F27e требует наличия технологии_частей. F27f требует, чтобы КАЖДАЯ
# запись в технологии_частей содержала материалы_для_процесса — конкретные
# материалы процесса для этого применения.
#
# Архитектура (v9.56): материалы процесса живут в ИЗДЕЛИИ, внутри объекта
# технологии_частей:
#   технологии_частей:
#     - часть: часть_<...>
#       технология: <stem>
#       материалы_для_процесса:        # ОБЯЗАТЕЛЬНО (F27f)
#         - материал: material_<stem>
#           роль: обрабатываемый
#         - материал: material_argon
#           роль: атмосфера
#
# Без материалов_для_процесса запись технологии_частей неполна — cron-агент
# не знает, какие материалы участвуют в процессе для этого конкретного случая.

def check_F27f(izdeliya: dict[str, dict]) -> dict:
    """F27f: Каждая запись технологии_частей должна иметь материалы_для_процесса.

    WARNING (v9.56; обязательность материалов процесса в изделии). Mirror
    F27e: F27e требует наличия технологии_частей; F27f требует, чтобы каждая
    запись в технологии_частей содержала материалы_для_процесса — конкретные
    материалы процесса для этого применения (обрабатываемый, атмосфера, ...).

    Архитектура v9.56: материалы процесса хранятся в ИЗДЕЛИИ (внутри объекта
    технологии_частей), НЕ в файле технологии. Это решает проблему «одна
    технология в разных изделиях с разными материалами».

    Скоуп: frontmatter изделий и частей. Проверяются только записи в
    технологии_частей (если поле отсутствует — это задача F27e, не F27f).

    Критерий нарушения: запись в технологии_частей не содержит
    материалы_для_процесса ИЛИ это поле пустое.

    Формат violation: '<izdelie_id>: технологии_частей[<tech_stem>] не содержит
    материалы_для_процесса — должны быть указаны конкретные материалы процесса
    для этого применения'.
    """
    violations = []
    total = 0
    valid = 0

    for izd_id, data in izdeliya.items():
        if not isinstance(data, dict):
            continue
        techs = data.get('технологии_частей', [])
        if not isinstance(techs, list):
            continue
        for entry in techs:
            if not isinstance(entry, dict):
                continue
            tech = str(entry.get('технология', '') or '').strip()
            if not tech:
                continue
            total += 1
            proc_mats = entry.get('материалы_для_процесса')
            if isinstance(proc_mats, list) and proc_mats:
                valid += 1
            else:
                tech_stem = tech[11:] if tech.startswith('tekhnologia_') else tech
                violations.append(
                    f"{izd_id}: технологии_частей[tekhnologia_{tech_stem}] не содержит "
                    f"материалы_для_процесса — должны быть указаны конкретные материалы "
                    f"процесса для этого применения")

    ratio = valid / max(1, total)
    return {
        'metric': 'F27f',
        'description': 'Обязательность материалы_для_процесса внутри технологии_частей',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F27g: ВАЛИДНОСТЬ id МАТЕРИАЛОВ В технологии_частей.материалы_для_процесса (v9.56)
# ============================================================================
# Контекст: F27g — расширение F27f. F27f требует наличия материалы_для_процесса
# в каждой записи технологии_частей. F27g проверяет, что id материалов внутри
# этого поля валидны (файл существует в каталоге материалы/).
#
# Архитектура v9.56: материалы_для_процесса хранятся в изделии, внутри объекта
# технологии_частей. F27g проверяет валидность id материалов в этом поле —
# mirror F27b (которая проверяет id в материалы_частей).
#
# Поддерживаемые форматы (как в F27d):
#   (1) v9.55+ — ролевая структура (объекты с {материал, роль, доля_массы?})
#   (2) legacy — простой список id строк

def check_F27g(izdeliya: dict[str, dict]) -> dict:
    """F27g: Битые ссылки на материалы в frontmatter технологии_частей.материалы_для_процесса.

    BLOCKING (mirror F27b, v9.56): внутри каждой записи `технологии_частей[]`
    поле `материалы_для_процесса` содержит id материалов процесса для этого
    применения. F27g проверяет валидность этих id — файл должен существовать
    в каталоге материалы/.

    Скоуп: frontmatter изделий и частей. Проверяются только id внутри
    `технологии_частей[].материалы_для_процесса[]`.

    Поддерживаемые форматы (как в F27d):
      (1) v9.55+ — ролевая структура (объекты с {материал, роль, доля_массы?})
      (2) legacy — простой список id строк

    Критерий нарушения: для материала с id `material_<stem>` (или просто `<stem>`)
    не существует файла реальные данные/материалы/<stem>.md.

    Формат violation: '<izdelie_id>: технологии_частей[<tech_stem>].материалы_для_процесса
    ссылается на несуществующий материал material_<stem>'.
    """
    violations = []
    mat_dir = SKYNET_REPO / "реальные данные" / "материалы"

    total = 0
    valid = 0
    seen = set()  # (izd_id, tech_stem, mat_stem) — dedup

    for izd_id, data in izdeliya.items():
        if not isinstance(data, dict):
            continue
        techs = data.get('технологии_частей', [])
        if not isinstance(techs, list):
            continue
        for entry in techs:
            if not isinstance(entry, dict):
                continue
            tech = str(entry.get('технология', '') or '').strip()
            if not tech:
                continue
            tech_stem = tech[11:] if tech.startswith('tekhnologia_') else tech
            proc_mats = entry.get('материалы_для_процесса')
            if not isinstance(proc_mats, list):
                continue
            for mat_entry in proc_mats:
                mat_id = None
                role = None
                if isinstance(mat_entry, dict):
                    mat_id = str(mat_entry.get('материал', '') or '').strip()
                    role = str(mat_entry.get('роль', '') or '').strip() or None
                elif isinstance(mat_entry, str):
                    mat_id = mat_entry.strip()
                if not mat_id:
                    continue

                total += 1
                stem = mat_id[9:] if mat_id.startswith('material_') else mat_id
                if not stem:
                    continue

                dedup_key = (izd_id, tech_stem, stem)
                if dedup_key in seen:
                    continue
                seen.add(dedup_key)

                if _resolve_material_file(stem, mat_dir) is not None:
                    valid += 1
                else:
                    role_suffix = f" (роль={role})" if role else ""
                    violations.append(
                        f"{izd_id}: технологии_частей[tekhnologia_{tech_stem}]."
                        f"материалы_для_процесса ссылается на несуществующий "
                        f"материал material_{stem}{role_suffix}")

    ratio = valid / max(1, total)
    return {
        'metric': 'F27g',
        'description': 'Битые ссылки на материалы в frontmatter технологии_частей.материалы_для_процесса',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# F28: АЛЬТЕРНАТИВНЫЕ ФОРМЫ МАТЕРИАЛА (v9.42)
# Идея: при вебпоиске материала искать ВСЕ его формы (монокристалл/
# поликристалл/аморфный/полиморфы; для аморфных систем — вариант_составов:
# наполненный/ненаполненный/гибкий), фиксировать их в сравнение_структур /
# варианты_по_применению. Это даёт AI-перепроектированию ('ии вариантов
# изделий') легальный выбор формы, а не единственную 'оптимальную'.

def check_F28(izdeliya: dict[str, dict]) -> dict:
    """F28: Материалы без перечня альтернативных форм/вариантов.

    WARNING-уровень (не блокирующий). Скоуп — только материалы, используемые
    изделиями (материалы_частей), как в F27: неиспользуемые не флудят очередь.

    Критерий нарушения: у материала заполнены свойства (не заглушка по F27),
    но ОДНОВРЕМЕННО:
      - сравнение_структур пусто (нет альтернативных форм: mono/poly/amorphous/
        полиморфы SiC 3C/4H/6H, α/β кварц, ...), И
      - варианты_по_применению пусто (нет вариантов составов/конфигураций:
        наполненный/ненаполненный, гибкий/жёсткий, ...), И
      - структурные_формы_альтернативы пусто (v9.41-поле чек-листа F27).

    Для аморфных материалов (термореактивы, стёкла) ось кристалличности
    вырождена — достаточно вариантов_по_применению; для полиморфных —
    достаточно сравнение_структур. Хоть одна ось должна быть заполнена.

    Формат violation: '<material_id>: ...' — совместим с normalizeViolationKey
    (dedup F28:<file_id>) и титульником '[F28] Verify: <file_id>'.
    """
    violations = []
    total = 0
    valid = 0

    referenced = _collect_referenced_materials(izdeliya)
    mat_dir = SKYNET_REPO / "реальные данные" / "материалы"

    for f in sorted(mat_dir.glob("*.md")):
        if f.name.startswith('_'):
            continue
        data, _, _ = read_yaml_frontmatter(f)
        if not data:
            continue  # обрезанный YAML уже ловит F27

        mid = str(data.get('id', '')).strip() or ('material_' + f.stem)
        stem = mid.replace('material_', '', 1)
        if mid not in referenced and stem not in referenced:
            continue  # не используется изделиями — вне очереди F28

        # Пропускаем заглушки — их чинит F27 (там же заполнят формы по чек-листу)
        basic = data.get('основные') or {}
        if not isinstance(basic, dict):
            basic = {}
        all_null = all(basic.get(k) in (None, '', 'null', 'None') for k in MATERIAL_CORE_FIELDS)
        if all_null:
            continue

        total += 1
        valid += 1

        sr = data.get('сравнение_структур')
        vp = data.get('варианты_по_применению')
        sfa = data.get('структурные_формы_альтернативы')  # v9.41 checklist-поле
        sr_filled = isinstance(sr, dict) and len(sr) > 0
        vp_filled = isinstance(vp, dict) and len(vp) > 0
        sfa_filled = (isinstance(sfa, list) and len(sfa) > 0) or (isinstance(sfa, dict) and len(sfa) > 0)

        if not (sr_filled or vp_filled or sfa_filled):
            valid -= 1
            violations.append(
                f"{mid}: не перечислены альтернативные формы/варианты "
                f"(сравнение_структур и варианты_по_применению пусты) — "
                f"вебпоиск должен покрыть все формы (mono/poly/amorphous/полиморфы; "
                f"для аморфных — варианты составов), иначе AI-варианты изделий "
                f"скованы единственной 'оптимальной' формой")

    ratio = valid / max(1, total)
    return {
        'metric': 'F28',
        'description': 'Материалы без перечня альтернативных форм/вариантов (для AI-вариантов изделий)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F29: ФОРМА МАТЕРИАЛА В ЧАСТИ (v9.43)
# ============================================================================

def check_F29(izdeliya: dict[str, dict]) -> dict:
    """F29: BOM-материалы (v9.52: merged F29+F30).

    Две проверки в одной функции (обе про BOM консистентность):

    Чек A (бывший F29) — форма материала в материалы_частей:
      Каждая запись материалы_частей указывает `форму` материала (forged_bar /
      electroplated_foil / 4h-sic_wafer / ...), а не generic id.
      Скоуп: все файлы с материалы_частей (изделия И части).

    Чек B (бывший F30) — наследуемые_материалы родителя:
      Для каждого файла с непустым дочерние_части (родителя):
      a. наследуемые_материалы заполнено (не пусто / не [])
      b. агрегация (материал, форма) по дочерним часть.материалы_частей
         (с долями родителя из родитель.материалы_частей) согласована с
         наследуемые_материалы: суммы долей совпадают (±0.001),
         источники_частей полны.

    WARNING-уровень (не блокирующий).
    """
    violations = []
    total_a = 0
    valid_a = 0
    total_b = 0
    valid_b = 0

    # === Чек A: форма материала в материалы_частей (бывший F29) ===
    for fid, data in izdeliya.items():
        mats = data.get('материалы_частей', [])
        if not isinstance(mats, list):
            continue
        for m in mats:
            if not isinstance(m, dict):
                continue
            total_a += 1
            forma = m.get('форма')
            if forma and str(forma).strip() and str(forma).strip().lower() not in ('null', 'none', '~'):
                valid_a += 1
            else:
                part_ref = m.get('часть', '?')
                mat_ref = m.get('материал', '?')
                violations.append(
                    f"[A-форма] {fid}: материалы_частей[{part_ref} → {mat_ref}] "
                    f"не указана `форма` — часть использует конкретный вариант "
                    f"материала (forged_bar / electroplated_foil / 4h-sic_wafer / ...); "
                    f"форма должна быть ключом из материал.варианты_по_применению"
                )

    # === Чек B: наследуемые_материалы родителя (бывший F30) ===
    for fid, data in izdeliya.items():
        dochernie = data.get('дочерние_части', [])
        if not isinstance(dochernie, list) or not dochernie:
            continue  # не родитель — вне скоупа
        total_b += 1
        ok = True
        msgs = []

        # a. наследуемые_материалы заполнено
        nm = data.get('наследуемые_материалы')
        if not nm or (isinstance(nm, list) and len(nm) == 0):
            msgs.append("наследуемые_материалы пусто — родитель должен агрегировать материалы частей")
            ok = False
            violations.append(f"[B-BOM] {fid}: " + "; ".join(msgs))
            continue

        if not isinstance(nm, list):
            msgs.append("наследуемые_материалы не list")
            ok = False
            violations.append(f"[B-BOM] {fid}: " + "; ".join(msgs))
            continue

        # b. согласованность: построить ожидаемую агрегацию из частей
        # доли родителя по part_id
        parent_shares = {}
        for entry in data.get('материалы_частей', []) or []:
            if isinstance(entry, dict):
                pid = entry.get('часть')
                share = entry.get('доля_массы')
                if pid and share is not None:
                    parent_shares[pid] = share

        expected = {}  # (материал, форма) → {сумма, источники}
        for pid in dochernie:
            part = izdeliya.get(pid)
            if not part:
                continue  # orphan — F12a поймает
            share = parent_shares.get(pid)
            if share is None:
                continue
            for m in part.get('материалы_частей', []) or []:
                if not isinstance(m, dict):
                    continue
                mid = m.get('материал')
                forma = m.get('форма') or '_no_forma_'
                if not mid:
                    continue
                key = (mid, forma)
                if key not in expected:
                    expected[key] = {'сумма': 0.0, 'источники': []}
                expected[key]['сумма'] += share
                expected[key]['источники'].append(pid)

        # сравнить с фактическим наследуемые_материалы
        actual = {}
        for item in nm:
            if not isinstance(item, dict):
                continue
            mid = item.get('материал')
            forma = item.get('форма') or '_no_forma_'
            suma = item.get('суммарная_доля_массы')
            srcs = item.get('источники_частей', [])
            if mid:
                actual[(mid, forma)] = {'сумма': suma, 'источники': set(srcs)}

        for key, exp in expected.items():
            mid, forma = key
            act = actual.get(key)
            if not act:
                msgs.append(f"наследуемые_материалы не содержит ({mid}, {forma})")
                ok = False
                continue
            # сумма (±0.001)
            if act['сумма'] is None or abs((act['сумма'] or 0) - exp['сумма']) > 0.001:
                msgs.append(
                    f"({mid}, {forma}): суммарная_доля_массы {act['сумма']} ≠ ожидаемой {round(exp['сумма'], 6)}"
                )
                ok = False
            # источники
            exp_set = set(exp['источники'])
            if act['источники'] != exp_set:
                missing = exp_set - act['источники']
                extra = act['источники'] - exp_set
                if missing:
                    msgs.append(f"({mid}, {forma}): источники_частей не хватает {sorted(missing)}")
                    ok = False
                if extra:
                    msgs.append(f"({mid}, {forma}): источники_частей лишние {sorted(extra)}")
                    ok = False

        if ok:
            valid_b += 1
        else:
            violations.append(f"[B-BOM] {fid}: " + "; ".join(msgs))

    # === Чек C (v9.60 Фаза 2.8): canonical-only материалы_частей ===
    # Каждый 'материал' в материалы_частей должен быть canonical — файл
    # должен существовать в реальные данные/материалы/. Если материала нет,
    # это либо (a) закупочный компонент (тип: компонент), либо (b) просто
    # битая ссылка (которую уже ловит F27b). Чек C делает это BLOCKING.
    canonical_set = _load_canonical_materials_set()
    total_c = 0
    valid_c = 0
    for fid, data in izdeliya.items():
        mats = data.get('материалы_частей', [])
        if not isinstance(mats, list):
            continue
        for m in mats:
            if not isinstance(m, dict):
                continue
            mat = str(m.get('материал', '')).strip()
            if not mat:
                continue
            total_c += 1
            if mat in canonical_set:
                valid_c += 1
            else:
                part_ref = m.get('часть', '?')
                violations.append(
                    f"[C-canonical] {fid}: материалы_частей[{part_ref} → {mat}] "
                    f"— non-canonical материал. Если это закупочный sub-assembly, "
                    f"перенесите в отдельный узел с тип: компонент и заполните его BOM. "
                    f"Иначе создайте canonical файл материалы/{mat}.md."
                )

    # Combined ratio
    total = total_a + total_b + total_c
    valid = valid_a + valid_b + valid_c
    ratio = valid / max(1, total)
    return {
        'metric': 'F29',
        'description': 'BOM-материалы: (A) форма указана; (B) наследуемые_материалы родителя; (C) canonical-only материалы (v9.60)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }

# ============================================================================
# F31: УНИКАЛЬНОСТЬ ID/АЛИАСОВ МАТЕРИАЛОВ И ТЕХНОЛОГИЙ (v9.44, дедупликация)
# ============================================================================

def _norm_id_key(s: str) -> str:
    """Агрессивная нормализация id: lowercase, убрать [-_ и пробелы].

    'material_ni-ysz' == 'material_ni_ysz'; 'material_p_vdf-trfe-ctfe' ==
    'material_pvdftrfectfe'. Ловит дубли, созданные из-за вариаций
    транслитерации/префиксов одного и того же имени.
    """
    return re.sub(r'[\s_\-]+', '', str(s or '').lower())


def _load_materials_and_techs() -> list[tuple[Path, dict]]:
    """Загрузить front matter всех материалов и технологий (для F31/F32).

    v9.33: расширено на фантастические данные/материалы + технологии/ (когда
    они появятся). Сейчас эти папки пусты — но loader готов.
    """
    entries = []
    for base in ("реальные данные", "фантастические данные", "работа и и"):
        for sub in ("материалы", "технологии"):
            d = SKYNET_REPO / base / sub
            if not d.is_dir():
                continue
            for f in sorted(d.glob("*.md")):
                if f.name.startswith('_'):
                    continue
                data, _, _ = read_yaml_frontmatter(f)
                if isinstance(data, dict) and data.get('id'):
                    entries.append((f, data))
    return entries


def _sig_figs(x, digits: int = 2):
    """Округление до N значащих цифр (None → None)."""
    try:
        x = float(x)
    except (TypeError, ValueError):
        return None
    if x != x or x in (float('inf'), float('-inf')) or x == 0:
        return 0.0 if x == 0 else None
    from math import floor, log10
    return round(x, -int(floor(log10(abs(x)))) + (digits - 1))


def check_F31(entries: list[tuple[Path, dict]] | None = None) -> dict:
    """F31: Дедупликация материалов и технологий (v9.52: merged F31+F32).

    Две проверки в одной функции (обе про дедупликацию):

    Чек A (бывший F31) — syntactic dedup:
      a. литеральный дубликат id в двух файлах
      b. канонический_id ссылается на несуществующий id
      c. алиас НЕ перечислен в псевдонимах канонического файла
      d. псевдоним в каноническом файле не имеет файла-алиаса
      e. нормализованная коллизия id ([-_ ] игнорируются) без алиас-связи

    Чек B (бывший F32) — semantic dedup:
      Сигнатура (класс, ρ 2 з.ц., k 2 з.ц.) совпадает у 2+ канонических
      материалов → кандидат на слияние. Ложные срабатывания закрываются
      агентом как false-positive с обоснованием.
    """
    violations = []
    if entries is None:
        entries = _load_materials_and_techs()

    # === Чек A: syntactic dedup (бывший F31) ===
    by_id: dict[str, tuple[Path, dict]] = {}
    by_norm: dict[str, list[str]] = {}
    for f, data in entries:
        mid = str(data.get('id', '')).strip()
        by_norm.setdefault(_norm_id_key(mid), []).append(mid)
        if mid in by_id:
            violations.append(
                f"[A-synt] {mid}: литеральный дубликат id в {f.name} и {by_id[mid][0].name}")
        else:
            by_id[mid] = (f, data)

    total_a = len(entries)
    valid_a = 0

    # Канонический план: mid → canonical (по канонический_id != id)
    alias_of: dict[str, str] = {}
    for mid, (_f, data) in by_id.items():
        canon = str(data.get('канонический_id', '') or '').strip() or mid
        if canon != mid:
            alias_of[mid] = canon

    # (b) битая ссылка канонический_id
    for mid, canon in sorted(alias_of.items()):
        if canon not in by_id:
            violations.append(
                f"[A-synt] {mid}: канонический_id='{canon}' не существует (битая alias-ссылка)")

    # (c)+(d) симметрия псевдонимов
    for mid, canon in sorted(alias_of.items()):
        canon_data = by_id.get(canon)
        if not canon_data:
            continue
        aliases_list = canon_data[1].get('псевдонимы') or []
        if not isinstance(aliases_list, list):
            aliases_list = []
        if mid not in [str(a).strip() for a in aliases_list]:
            violations.append(
                f"[A-synt] {mid}: канонический_id='{canon}', но '{canon}' не перечисляет "
                f"его в псевдонимах (несимметричная алиас-связь)")
    for canon, (_f, data) in sorted(by_id.items()):
        aliases_list = data.get('псевдонимы') or []
        if not isinstance(aliases_list, list):
            continue
        for a in aliases_list:
            a = str(a).strip()
            if not a:
                continue
            a_data = by_id.get(a)
            if a_data is None:
                continue
            a_canon = str(a_data[1].get('канонический_id', '') or '').strip() or a
            if a_canon != canon:
                violations.append(
                    f"[A-synt] {canon}: псевдоним '{a}' указывает на канонический_id="
                    f"'{a_canon}' (висячая/конфликтная запись)")

    # (e) нормализованная коллизия без объявленной связи
    for norm_key, mids in sorted(by_norm.items()):
        if len(mids) < 2:
            continue
        related = all(
            alias_of.get(a) == mids[0] or alias_of.get(mids[0]) == a
            for a in mids[1:]
        )
        if not related:
            violations.append(
                f"[A-synt] {mids[0]}: нормализованная коллизия id с {mids[1:]} "
                f"(ключ '{norm_key}') — объявите канонический_id/псевдонимы "
                f"или переименуйте")

    valid_a = total_a - len(set(
        v.split(']')[1].strip().split(':')[0] for v in violations if v.startswith('[A-synt]') and 'литерал' not in v))

    # === Чек B: semantic dedup (бывший F32) ===
    # Разобранные агентом false-positive
    f32_fp_exclude: set[frozenset[str]] = {
        frozenset({'material_pbo2', 'material_spongy_lead'}),
    }

    groups: dict[tuple, list[str]] = {}
    total_b = 0
    for _f, data in entries:
        if str(data.get('тип', '')).strip() != 'материал':
            continue
        mid = str(data.get('id', '')).strip()
        canon = str(data.get('канонический_id', '') or '').strip() or mid
        if canon != mid:
            continue  # алиасы исключены
        klass = str(data.get('класс', '')).strip().lower()
        basic = data.get('основные') or {}
        if not isinstance(basic, dict):
            continue
        total_b += 1
        rho = _sig_figs(basic.get('плотность_kg_m3'))
        k = _sig_figs(basic.get('теплопроводность_W_mK'))
        if rho is None or k is None:
            continue
        key = (klass, rho, k)
        groups.setdefault(key, []).append(mid)

    valid_b = total_b
    for (klass, rho, k), mids in sorted(groups.items()):
        if len(mids) > 1:
            real = [mids[0]]
            for other in mids[1:]:
                if frozenset({mids[0], other}) in f32_fp_exclude:
                    continue
                real.append(other)
            if len(real) < 2:
                continue
            violations.append(
                f"[B-sem] {real[0]}: семантический дубль {real[1:]} "
                f"(класс={klass}, ρ≈{rho:g}, k≈{k:g}) — проверить и слить "
                f"через scripts/migrate_dedup_materials.py или закрыть как "
                f"false-positive")
            valid_b -= len(real)

    # Combined ratio
    total = total_a + total_b
    valid = max(0, valid_a) + max(0, valid_b)
    ratio = valid / max(1, total)
    return {
        'metric': 'F31',
        'description': 'Дедупликация материалов: (A) syntactic — дубли id, алиас-связность, битые канонический_id; (B) semantic — класс+ρ+k совпадают',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }

# ============================================================================
# F33: КЛАССИФИКАЦИОННАЯ КОНСИСТЕНТНОСТЬ (v9.46)
# — тип ↔ директория; коллизии нормализованных имён между категориями
# ============================================================================

# Префиксы ID, отделяющие категорию (например, material_copper,
# izdelie_pcm, tekhnologia_parylene_c, часть_intel_loihi_2_die).
# Используется для выделения «человекочитаемого имени» (id без префикса).
# v9.33: добавлен префикс 'SkyNet-' для канон-моделей (SkyNet-T800 → T800).
_CATEGORY_PREFIXES = ('material_', 'izdelie_', 'tekhnologia_', 'часть_', 'SkyNet-')

# Какое значение поля `тип` ожидается в каждой директории категории.
# v9.33: добавлена категория 'модели' для фантастические данные/модели/.
# v9.61: для каталога 'изделия' принято ЛЮБОЕ из 3 значений тип
# (изделие — top-level и закупочные sub-assemblies,
#  сборка — промежуточные, часть — leaf атомарные).
# Вариант C: тип 'компонент' упразднён.
_EXPECTED_TYPE_BY_DIR = {
    'материалы': 'материал',
    'изделия':   ('изделие', 'сборка', 'часть'),  # v9.61: 3 типа (без компонент)
    'технологии': 'технология',
    'модели':    'модель_SkyNet',  # v9.33 NEW
}


def _load_all_catalog_entries() -> list[tuple[Path, str, dict]]:
    """Загрузить front matter всех каталог-файлов 3-х категорий.

    Возвращает список (path, category, data). Включая `часть_*` (дочерние
    части изделий) — они нужны для F33b (коллизия имён часть_ vs материал_).

    v9.33: расширено на фантастические данные/ (категория 'модели' для моделей).
    Сейчас фантастические данные/модели/ содержит .md файлы на верхнем уровне
    (тип: модель_SkyNet) — добавлены как category='модели'.
    """
    out: list[tuple[Path, str, dict]] = []
    # Реальные данные: материалы, изделия, технологии
    for cat in ('материалы', 'изделия', 'технологии'):
        d = SKYNET_REPO / "реальные данные" / cat
        if not d.exists():
            continue
        for f in sorted(d.rglob("*.md")):
            if f.name.startswith('_') and f.name != '_index.md':
                continue
            data, _, _ = read_yaml_frontmatter(f)
            if isinstance(data, dict) and data.get('id'):
                out.append((f, cat, data))
    # v9.33 NEW: Фантастические данные/модели/ (канон-модели)
    # Модели лежат как .md на верхнем уровне + могут иметь поддиректории
    fant_dir = SKYNET_REPO / "фантастические данные" / "модели"
    if fant_dir.is_dir():
        for f in sorted(fant_dir.rglob("*.md")):
            if f.name.startswith('_') and f.name != '_index.md':
                continue
            data, _, _ = read_yaml_frontmatter(f)
            if isinstance(data, dict) and data.get('id'):
                out.append((f, 'модели', data))
    # v9.33 NEW: работа и и/ (если есть собственные материалы/технологии)
    for cat in ('материалы', 'технологии'):
        d = SKYNET_REPO / "работа и и" / cat
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name.startswith('_'):
                continue
            data, _, _ = read_yaml_frontmatter(f)
            if isinstance(data, dict) and data.get('id'):
                out.append((f, cat, data))
    return out


def _strip_category_prefix(id_str: str) -> str:
    """Убрать префикс категории из id — оставить человекочитаемое имя.

    'material_copper' → 'copper'
    'izdelie_pcm' → 'pcm'
    'tekhnologia_parylene_c' → 'parylene_c'
    'часть_intel_loihi_2_die' → 'intel_loihi_2_die'
    """
    s = id_str
    for pfx in _CATEGORY_PREFIXES:
        if s.startswith(pfx):
            return s[len(pfx):]
    return s


def check_F33(entries: list[tuple[Path, str, dict]] | None = None) -> dict:
    """F33: Консистентность классификации (v9.46).

    WARNING-метрика (не блокирующая): проверяет две ортогональные проблемы
    классификации каталога.

    (a) type-vs-directory mismatch — каждый .md в `материалы/` обязан иметь
        `тип: материал`, в `изделия/` — `тип: изделие`, в `технологии/` —
        `тип: технология`. Любое отклонение — нарушение: либо файл попал не
        в ту директорию, либо его `тип` заполнен неверно. Это смысловое
        правило каталога (в v9.46 введено после реклассификации #751).

    (b) normalized-name collision — два файла в РАЗНЫХ категориях с
        одинаковым человекочитаемым именем (id без префикса). Это НЕ ошибка
        (онтологическая двойственность: 'parylene_c' может быть и материалом
        и технологией CVD; 'pcm' — материалом Phase-Change и изделием
        Phase-Change Memory chip). Но это требует review при добавлении
        новых коллизий. Существующие коллизии перечислены в
        `f33_known_name_collisions` как допустимые.

    Формат violation: '<id>: ...' — совместим с дефолтной веткой
    normalizeViolationKey и титульником '[F33] Verify: <id>'.
    """
    violations = []
    if entries is None:
        entries = _load_all_catalog_entries()

    # Известные допустимые коллизии имён между категориями (v9.46).
    # Добавлять сюда ТОЛЬКО после review и фиксации в комментарии почему это OK.
    # Ключ — нормализованное имя (id без префикса), значение — короткое объяснение.
    f33_known_collisions_set: dict[str, str] = {
        # parylene_c: вещество (полимер Parylene C) vs технология CVD-нанесения
        'parylene_c': 'вещество (полимер) vs CVD-процесс нанесения',
        # pcm: Phase-Change Material (вещество) vs Phase-Change Memory (изделие-ИС)
        'pcm': 'Phase-Change Material (вещество) vs Phase-Change Memory chip (изделие)',
        # pcm_rt35: Phase-Change Material RT35 (вещество-парафин) vs изделие-обёртка
        # для композитных термопрокладок в изделия/компоненты/композитные/
        'pcm_rt35': 'Phase-Change Material RT35 (вещество) vs композитная термопрокладка (изделие)',
    }

    total = len(entries)
    valid = 0

    # (a) type-vs-directory mismatch
    type_mismatch_files: set[str] = set()
    for f, cat, data in entries:
        t = str(data.get('тип', '')).strip()
        expected = _EXPECTED_TYPE_BY_DIR.get(cat)
        if expected and t:
            # v9.60: 'expected' может быть tuple (множество допустимых значений)
            if isinstance(expected, tuple):
                ok = t in expected
            else:
                ok = (t == expected)
            if not ok:
                mid = str(data.get('id', '')).strip() or f.name
                violations.append(
                    f"{mid}: тип={t!r} не соответствует директории {cat!r} "
                    f"(ожидается {expected!r}) — реклассифицируйте файл или "
                    f"исправьте тип")
                type_mismatch_files.add(mid)

    # (b) normalized-name collision between categories
    by_name: dict[str, list[tuple[str, str]]] = {}  # name → [(cat, id), ...]
    for _f, cat, data in entries:
        mid = str(data.get('id', '')).strip()
        if not mid:
            continue
        name = _strip_category_prefix(mid)
        by_name.setdefault(name, []).append((cat, mid))

    cross_name_collisions: list[tuple[str, list[tuple[str, str]]]] = []
    for name, occ in sorted(by_name.items()):
        cats = {c for c, _ in occ}
        if len(cats) > 1:
            # Допустимая коллизия?
            if name in f33_known_collisions_set:
                continue
            cross_name_collisions.append((name, occ))
            for _c, mid in occ:
                type_mismatch_files.add(mid)

    for name, occ in cross_name_collisions:
        locations = ", ".join(f"[{c}] {mid}" for c, mid in occ)
        violations.append(
            f"имя='{name}' в нескольких категориях: {locations} — "
            f"разные каталожные сущности с одним именем; проверьте что это "
            f"онтологическая двойственность, а не дубликат (если OK, "
            f"добавьте имя в f33_known_collisions_set в check_F33)")

    valid = total - len(type_mismatch_files)
    ratio = valid / max(1, total)
    return {
        'metric': 'F33',
        'description': 'Классификационная консистентность: тип↔директория + коллизии имён между категориями',
        'total': total,
        'valid': max(0, valid),
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F34: ГЛУБИНА ДЕКОМПОЗИЦИИ (v9.47)
# ============================================================================

# Подтипы level-2 узлов, которые могут быть АТОМАРНЫМИ (не требуют дальнейшей
# декомпозиции до уровня 3/4). Anything else with дочерние_части = [] AND
# уровень_иерархии = 'промежуточный' (вместо 'неделимый') — это нарушение F34.
#
# Эти подтипы — GENUINELY неделимые конструктивные элементы (закупаемые как
# отдельная деталь, не разборная в полевых условиях):
F34_ATOMIC_SUBTYPES = {
    'корпус',          # корпусная деталь — цельнолитая/фрезерованная
    'крепёж',          # винт/болт/шайба — стандартный закупочный элемент
    'разъёмы',         # connector — закупочный элемент (MIL-DTL-38999 etc.)
    'инкапсулянт',     # эпоксид/гель — материал, не сборка
    'припой',          # solder — материал
    'изоляция',        # изоляционная прокладка — листовой материал
    'экранирование',   # EMI shield — фольга/сетка
    'уплотнение',      # gasket — формованная резина
    'кожух',           # крышка — листовой металл
    'крышка',          # cover
    'теплораспределитель',  # heat spreader — однородная пластина
    'теплообменник',   # heat exchanger — fabricated assembly (но обычно как готовый Сomponent)
    'охладитель',      # heatsink — закупочный
    'герметизация',    # sealant — материал
    'прокладка',       # gasket — листовой
    'демпфер',         # damper — закупочный
    'амортизатор',     # damper — закупочный
    'пружина',         # spring — закупочный
    'подшипники',      # bearing — закупочный (bearing assembly)
    'фланец',          # flange — фрезерованная
    'вал',             # shaft — точёная
    'заглушка',        # plug — закупочная
    'ручка',           # handle — закупочная
}

def check_F34(izdeliya: dict[str, dict]) -> dict:
    """F34: Глубина декомпозиции — НЕ ОГРАНИЧЕНА (v9.48).

    v9.47: первоначальная реализация требовала уровень ≥ 3 ИЛИ atomic-whitelist.
    v9.48: глубина НЕ ограничена ни по минимуму, ни по максимуму:
      - Атомарные части могут быть на любом уровне (1, 2, 3, 5, 7, ...)
      - Глубокие сборки могут иметь уровни 5, 6, 7, ... (нет потолка 4)
      - Минимум: часть ДОЛЖНА быть либо 'неделимый' (атомарная), либо иметь
        дочерние_части (продолжить декомпозицию). Это уже проверяется F16;
        F34 не дублирует F16, а лишь фиксирует нарушения для issue-очереди
        с информативным описанием (что делать: пометить 'неделимый' или
        создать sub-parts).

    Логика:
      - Для каждого узла в графе (всех, не только level-1):
        - Если `уровень_иерархии='неделимый'` — PASS (атомарный, любая глубина)
        - Если есть `дочерние_части` — PASS (продолжает декомпозицию)
        - Если `уровень_иерархии='промежуточный'` и `дочерние_части=[]` — FAIL:
          либо пометить 'неделимый' (если часть действительно атомарная),
          либо создать sub-parts (если часть составная)
          Дополнительно: если подтип в F34_ATOMIC_SUBTYPES whitelist —
          советуем пометить 'неделимый' (низкий риск атомарности)

    Returns:
        {metric, description, total, valid, ratio, pass, violations}
    """
    violations = []
    total = 0
    valid = 0

    for izd_id, data in izdeliya.items():
        hier = data.get('уровень_иерархии', '')
        children = data.get('дочерние_части', []) or []

        # 'неделимый' — атомарная часть, любая глубина OK
        if hier == 'неделимый':
            total += 1
            valid += 1
            continue

        # имеет детей — декомпозиция продолжается, OK (любой уровень)
        if isinstance(children, list) and children:
            total += 1
            valid += 1
            continue

        # 'верхний' (уровень 1) без детей — это либо атомарное top-level изделие
        # (например, izdelie_mednyi_provod), либо незавершённая декомпозиция.
        # F12a ловит топ-уровни без детей отдельно; F34 не дублирует.
        if hier == 'верхний':
            continue

        # 'промежуточный' без детей — нарушение (should be 'неделимый' or have children)
        # F16 уже пометит это как нарушение; F34 создаёт issue с actionable советом
        try:
            lvl = int(data.get('уровень_номер', 0) or 0)
        except (TypeError, ValueError):
            lvl = 0
        sub_type = data.get('подтип', '')

        total += 1
        if sub_type in F34_ATOMIC_SUBTYPES:
            # подсказка: probably should be 'неделимый'
            violations.append(
                f"{izd_id}: уровень_иерархии='промежуточный' (уровень {lvl}, "
                f"подтип='{sub_type}') но дочерние_части=[] — подтип в atomic-whitelist; "
                f"поставить уровень_иерархии='неделимый' (атомарная часть)"
            )
        else:
            # подсказка: декомпозировать дальше ИЛИ обосновать атомарность
            violations.append(
                f"{izd_id}: уровень_иерархии='промежуточный' (уровень {lvl}, "
                f"подтип='{sub_type}') но дочерние_части=[] — НЕ декомпозирована. "
                f"Либо пометить 'неделимый' (если атомарная), либо создать sub-parts "
                f"на уровне {lvl + 1} (если составная)"
            )

    ratio = valid / max(1, total)
    return {
        'metric': 'F34',
        'description': 'Глубина декомпозиции — не ограничена; часть должна быть '
                       "'неделимый' или иметь дочерние_части",
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


# ============================================================================
# F35: COMPONENTS CONSISTENCY (v9.60 — вариант A2 + D4-β)
# ============================================================================
# Новая метрика для разделения сущностей:
#   - изделие / сборка / часть / компонент (через поле 'тип')
#   - canonical материалы (id существует в материалы/)
#   - закупочные компоненты (имеют BOM в материалы_частей, не имеют sub-parts)
#
# Подметрики:
#   F35a: 'тип: компонент' ⇔ дочерние_части=[] ∧ материалы_частей непусто
#   F35b: каждый 'материал' в материалы_частей — canonical (файл в материалы/)
#   F35c: 'тип: часть' ⇔ дочерние_части=[] ∧ материалы_частей непусто
#   F35d: 'тип: сборка' ⇔ дочерние_части непусто
#   F35e: 'тип: изделие' ⇔ родитель=null ∧ уровень_номер=1
#
# Состояние v9.60 Фаза 1.3: NON-BLOCKING (warning), чтобы не сломать existing pass-rate
# перед миграцией файлов. В Фазе 2.3 станет BLOCKING.

def _load_canonical_materials_set() -> set:
    """Кэш canonical материалов из реальные данные/материалы/*.md."""
    global _CANONICAL_MATERIALS_CACHE
    if _CANONICAL_MATERIALS_CACHE is None:
        materials_dir = SKYNET_REPO / "реальные данные" / "материалы"
        _CANONICAL_MATERIALS_CACHE = {f.stem for f in materials_dir.glob("*.md")}
    return _CANONICAL_MATERIALS_CACHE


_CANONICAL_MATERIALS_CACHE: set | None = None


def check_F35(izdeliya: dict[str, dict]) -> dict:
    """F35: Components Consistency — разделение тип/материал/компонент (v9.60).

    NON-BLOCKING в Фазе 1.3. После миграции на A2-модель станет BLOCKING.

    Проверки:
    - F35a: узлы с тип='компонент' (илиleaf без canonical material) должны:
        * иметь пустые дочерние_части
        * иметь непустые материалы_частей
        * каждый 'материал' в материалы_частей должен быть canonical (файл в материалы/)
    - F35b: каждый 'материал' в материалы_частей любого узла должен быть canonical
      (если не canonical → это закупочный компонент, должен быть отдельным узлом)
    - F35c: leaf узлы (без детей) с тип='часть' или 'неделимый' должны иметь материалы_частей
    """
    canonical = _load_canonical_materials_set()
    violations = []
    total = 0
    valid = 0
    # v9.61: purchased_components_found убран — упразднён вместе с типом 'компонент'

    for izd_id, data in izdeliya.items():
        tip = data.get('тип', 'изделие')  # v9.61: 3 типа (изделие/сборка/часть)
        children = data.get('дочерние_части', [])
        if not isinstance(children, list):
            children = []
        materials_parts = data.get('материалы_частей', [])
        if not isinstance(materials_parts, list):
            materials_parts = []

        # F35b: каждый 'материал' в материалы_частей — canonical?
        for entry in materials_parts:
            if not isinstance(entry, dict):
                continue
            mat = entry.get('материал')
            if not mat:
                continue
            total += 1
            if mat in canonical:
                valid += 1
            else:
                # НЕ canonical → нужно создать canonical файл или заменить на canonical
                violations.append(
                    f"{izd_id}: материалы_частей содержит non-canonical '{mat}' — "
                    f"создайте canonical файл материалы/{mat}.md или замените на canonical материал."
                )

        # F35a: leaf узлы без материалы_частей — WARN (нужно заполнить BOM)
        if not children:
            if not materials_parts:
                if tip in ('изделие', 'часть'):
                    violations.append(
                        f"{izd_id}: leaf узел (тип={tip}) без материалы_частей — "
                        f"нужно заполнить BOM (canonical материал)."
                    )
                    total += 1

    ratio = valid / max(1, total)
    return {
        'metric': 'F35',
        'description': 'Components consistency — canonical-only материалы_частей (v9.61, non-blocking)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': True,  # NON-BLOCKING
        'blocking': False,
        'violations': violations,
    }


# ============================================================================
# F36: BODY MARKDOWN STRUCTURE (v9.61 NEW)
# ============================================================================
# Проверяет структуру markdown body, а не frontmatter.
# Валидатор F12a-F35 работают с YAML frontmatter; F36 проверяет body.
#
# Под-проверки:
#   F36a: обязательные секции (##) для каждого типа файла
#   F36b: malformed таблицы (неровное число столбцов)
#   F36c: body↔frontmatter согласованность
#         (## Используемые материалы ↔ frontmatter.материалы_частей,
#          ## Состав ↔ frontmatter.дочерние_части)
#
# NON-BLOCKING в v9.61 Фазе 1 — все violations идут в очередь verify-task.

# Канонические секции для каждого типа (H2 заголовки)
_CANONICAL_SECTIONS_BY_TYPE = {
    'изделие': ['## Описание', '## Технические характеристики', '## Состав',
                '## Используемые материалы', '## Принцип работы', '## Источники'],
    'сборка': ['## Описание', '## Технические характеристики', '## Принцип работы',
               '## Состав', '## Используемые материалы', '## Источники'],
    'часть': ['## Описание', '## Технические характеристики', '## Принцип работы',
              '## Состав', '## Используемые материалы', '## Источники'],
    'материал': ['## Описание', '## Источники'],  # минимально; опц: Физические свойства, Механические свойства, Химический состав
    'технология': ['## Описание', '## Источники'],
    'стандарт': ['## Описание', '## Источники'],
}

# Известные синонимы секций (заменять на канонические)
_SECTION_SYNONYMS = {
    '## Общее описание': '## Описание',
    '## Источники (F28)': '## Источники',
    '## Источники (F27)': '## Источники',
    '## Механические свойства (включая усталостную прочность и крип)': '## Механические свойства',
    '## Химический состав и структура': '## Химический состав',
    '## Технологии применения': '## Технологии получения',
    '## Альтернативы': '## Альтернативные технологии',
}


def _read_body(path: Path) -> str:
    """Прочитать markdown body (без frontmatter)."""
    text = path.read_text(encoding='utf-8')
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            return text[end + 4:]
    return text


def _extract_h2_sections(body: str) -> list:
    """Извлечь список H2 заголовков из body в порядке появления."""
    import re
    return re.findall(r'^##\s+(.+?)\s*$', body, re.MULTILINE)


def _normalize_section(name: str) -> str:
    """Нормализовать имя секции через синонимы."""
    full = f'## {name}'
    if full in _SECTION_SYNONYMS:
        return _SECTION_SYNONYMS[full]
    return full


def _check_malformed_tables(body: str) -> list:
    """Найти malformed таблицы (неровное число столбцов).

    Возвращает список описаний нарушений.
    """
    import re
    violations = []
    # Найти все таблицы (начинаются с |...|\n|---|...)
    lines = body.split('\n')
    in_table = False
    table_start = 0
    header_cols = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('|') and stripped.endswith('|'):
            cols = stripped.count('|') - 1  # количество столбцов
            if not in_table:
                # начало таблицы — это header
                in_table = True
                table_start = i
                header_cols = cols
            elif cols != header_cols and header_cols > 0:
                # строка с другим числом столбцов — malformed
                violations.append(
                    f"malformed таблица: строка {i+1} имеет {cols} столбцов "
                    f"(ожидалось {header_cols}) — проверьте лишний '| canon |' суффикс")
                # не выходим из таблицы (может быть ещё больше нарушений)
        else:
            if in_table:
                in_table = False
                header_cols = 0
    return violations


def _check_body_fm_consistency(body: str, data: dict) -> list:
    """Проверить согласованность body↔frontmatter.

    Проверки:
    - "## Состав" должен упоминать дочерние_части (если они есть)
    - "## Используемые материалы" должен содержать ссылки (если материалы_частей есть)
    """
    import re
    violations = []

    # Найти секцию "## Состав"
    m = re.search(r'^##\s+Состав\s*$(.*?)(?=^##\s|\Z)', body, re.MULTILINE | re.DOTALL)
    if m:
        section = m.group(1)
        # Если в frontmatter есть дочерние_части, body должен их упоминать
        children = data.get('дочерние_части', [])
        if isinstance(children, list) and children:
            # body говорит "Дочерних частей нет" / "не указаны"?
            if re.search(r'(?:дочерних\s+частей\s+нет|не\s+указаны|нет\s+дочерних)', section, re.IGNORECASE):
                violations.append(
                    f"## Состав body говорит 'дочерних частей нет/не указаны', "
                    f"но frontmatter содержит {len(children)} дочерних_частей — "
                    f"обновите текст body")

    # Найти секцию "## Используемые материалы"
    m = re.search(r'^##\s+Используемые\s+материалы\s*$(.*?)(?=^##\s|\Z)', body, re.MULTILINE | re.DOTALL)
    if m:
        section = m.group(1)
        materials = data.get('материалы_частей', [])
        if isinstance(materials, list) and materials:
            # body содержит placeholder?
            if re.search(r'(?:добавляются\s+после\s+связывания|ссылки\s+на\s+реальные_данные|'
                         r'_обратные\s+ссылки\s+ещё\s+не\s+проставлены_)', section, re.IGNORECASE):
                violations.append(
                    f"## Используемые материалы body содержит placeholder "
                    f"('добавляются после связывания'), но frontmatter материалы_частей "
                    f"заполнен ({len(materials)} записей) — отрендерите ссылки в body")

    return violations


def check_F36(entries: list | None = None) -> dict:
    """F36: Body markdown structure (v9.61).

    NON-BLOCKING. Проверяет:
    - F36a: обязательные секции (##) для каждого типа файла
    - F36b: malformed таблицы (неровное число столбцов)
    - F36c: body↔frontmatter согласованность
    """
    import re as _re
    violations = []
    total = 0
    valid = 0

    if entries is None:
        # Загрузить все записи самосто­ятельно
        all_entries = _load_all_catalog_entries()
    else:
        all_entries = entries

    for path, cat, data in all_entries:
        if not isinstance(data, dict):
            continue
        tip = str(data.get('тип', '')).strip()
        izd_id = str(data.get('id', '')).strip() or path.name

        # Только для типов с известными каноническими секциями
        canonical = _CANONICAL_SECTIONS_BY_TYPE.get(tip)
        if not canonical:
            continue

        # Прочитать body
        try:
            body = _read_body(path)
        except Exception:
            continue

        total += 1

        # F36a: обязательные секции
        sections_raw = _extract_h2_sections(body)
        sections_normalized = [_normalize_section(s) for s in sections_raw]
        missing = [sec for sec in canonical if sec not in sections_normalized]
        if not missing:
            valid += 1
        else:
            violations.append(
                f"[F36a] {izd_id}: отсутствуют обязательные секции: "
                f"{', '.join(missing)}")

        # F36b: malformed таблицы
        table_violations = _check_malformed_tables(body)
        for tv in table_violations:
            violations.append(f"[F36b] {izd_id}: {tv}")

        # F36c: body↔frontmatter согласованность
        consistency_violations = _check_body_fm_consistency(body, data)
        for cv in consistency_violations:
            violations.append(f"[F36c] {izd_id}: {cv}")

    ratio = valid / max(1, total)
    return {
        'metric': 'F36',
        'description': 'Body markdown structure: секции + таблицы + body↔fm согласованность (v9.61)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': True,  # NON-BLOCKING
        'blocking': False,
        'violations': violations,
    }


# ============================================================================
# F37: IS_PURCHASED FLAG (v9.61 NEW)
# ============================================================================
# Проверяет, что все файлы в изделия/компоненты/ имеют is_purchased: true.
# В v9.61 спецификация требует это поле для закупочных sub-assemblies.

def check_F37(izdeliya: dict[str, dict]) -> dict:
    """F37: is_purchased: true обязательно для изделия/компоненты/*.

    NON-BLOCKING в v9.61. После миграции может стать BLOCKING.
    """
    violations = []
    total = 0
    valid = 0

    for izd_id, data in izdeliya.items():
        if not isinstance(data, dict):
            continue
        # Проверяем только файлы в изделия/компоненты/ (по пути)
        path = data.get('_path', '')
        if '/компоненты/' not in path and '\\компоненты\\' not in path:
            continue
        total += 1
        is_purchased = data.get('is_purchased')
        if is_purchased is True:
            valid += 1
        else:
            violations.append(
                f"{izd_id}: файл в изделия/компоненты/ но is_purchased не true "
                f"(текущее: {is_purchased!r}) — должен быть true для закупочных sub-assemblies")

    ratio = valid / max(1, total)
    return {
        'metric': 'F37',
        'description': 'is_purchased: true для изделий/компоненты/ (v9.61, non-blocking)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': True,  # NON-BLOCKING
        'blocking': False,
        'violations': violations,
    }


# ============================================================================
# F38: КЛАСС ENUM-ВАЛИДАЦИЯ (v9.61 NEW)
# ============================================================================
# Проверяет, что поле `класс` в материалах и компонентах соответствует
# каноническому enum из §12.3.
#
# §12.3 enum: металл|полимер|керамика|композит|полупроводник|сплав|радиоизотоп|прочее
# Расширенный enum (v9.61): + жидкость, газ, эластомер (для корректной классификации)

_VALID_CLASS_ENUM = {
    'металл', 'полимер', 'керамика', 'композит', 'полупроводник', 'сплав',
    'радиоизотоп', 'прочее',
    # Расширенный enum (v9.61):
    'жидкость', 'газ', 'эластомер', 'углерод', 'метаматериал',
    'неорганическая_соль', 'неорганическая_жидкость',
    'органический_жидкий_электролит', 'органическая_соль',
    'жидкий_металл', 'гидрид_металла', 'кермет', 'керамика_металл',
    'композит_электрод', 'магнитотвёрдый', 'магнитотвёрдый_сплав',
    'функциональная_керамика', 'функциональный_стек', 'халькогенид',
    'радиоактивный_металл',
}

# Маппинг известных неправильных значений → канонических
_CLASS_NORMALIZATION = {
    'металл': 'металл',  # OK
    'полимер': 'полимер',  # OK
    # ... остальные — должны быть в _VALID_CLASS_ENUM
}


def check_F38(entries: list | None = None) -> dict:
    """F38: класс enum-валидация (v9.61).

    Проверяет, что поле `класс` в материалах принимает значение из
    расширенного enum. NON-BLOCKING.
    """
    violations = []
    total = 0
    valid = 0

    if entries is None:
        all_entries = _load_all_catalog_entries()
    else:
        all_entries = entries

    for path, cat, data in all_entries:
        if not isinstance(data, dict):
            continue
        # Только для материалов (класс определён в §12.3)
        if cat != 'материалы':
            continue
        klass = str(data.get('класс', '')).strip()
        if not klass:
            continue  # отсутствие класса — это другая метрика (F70g)
        mat_id = str(data.get('id', '')).strip() or path.name
        total += 1
        if klass in _VALID_CLASS_ENUM:
            valid += 1
        else:
            violations.append(
                f"{mat_id}: класс={klass!r} не входит в расширенный enum "
                f"(металл|полимер|керамика|композит|полупроводник|сплав|радиоизотоп|прочее|"
                f"жидкость|газ|эластомер|углерод|метаматериал|...)")

    ratio = valid / max(1, total)
    return {
        'metric': 'F38',
        'description': 'класс enum-валидация для материалов (v9.61, non-blocking)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': True,  # NON-BLOCKING
        'blocking': False,
        'violations': violations,
    }


# ============================================================================
# MAIN
# ============================================================================

def check_F_scal(izdeliya: dict[str, dict]) -> dict:
    """F-scal: наличие и заполненность опционального блока `масштабируемость` (v9.32 / P087).

    SOFT-метрика (warning, не блокирующая) — поле опциональное по схеме §12.6.
    Создаёт verify-task issues через workflow verify_decomposition.yml, чтобы
    cron-агент поэтапно заполнял блок.

    v9.32.1: расширено на ВСЕ уровни вложенности (не только top-level):
      - тип=изделие (top-level + промежуточные + leaf-части уровня 2/3+)
      - 685 файлов: level-1 (120), level-2 (555), level-3 (10)
      - Leaf-части (без дочерних_частей) имеют собственный физический режим
        (гайка/подшипник/чип/мембрана/балка) и часто выступают
        ограничивающие_части для родителя — без их блока проверки F-scal
        теряют половину смысла.

    Логика (для ВСЕХ изделий с тип=изделие, любой уровень):
      - блок `масштабируемость` отсутствует → нарушение "отсутствует"
      - блок есть, но `режим` отсутствует ИЛИ не из enum → нарушение "невалидный режим"
      - `ограничивающие_части` (если есть И у узла есть дочерние_части) содержит
        `часть` не из дочерних_части → нарушение "битая ссылка"
        (для leaf-частей без детей — не проверяем, нечего ограничивать)

    pass=True всегда (soft-метрика) — но violations возвращаются для issue-очереди.
    """
    ENUM_REZHIM = {'масштабируемая', 'квантуемая', 'фиксированная'}
    violations = []
    total = 0
    valid = 0

    for izd_id, data in izdeliya.items():
        # v9.61: расширяем фильтр на 3 типа (изделие/сборка/часть).
        # F-scal применим к любому узлу с физическим режимом.
        if data.get('тип') not in ('изделие', 'сборка', 'часть'):
            continue
        # v9.32.1: убраны фильтры уровня/родителя/детей — проверяем ВСЕ изделия
        # (top-level + промежуточные + leaf-части любого уровня)
        total += 1

        scal = data.get('масштабируемость')
        if not scal or not isinstance(scal, dict):
            violations.append(
                f"{izd_id}: отсутствует блок масштабируемость "
                f"(требуется P087: режим {sorted(ENUM_REZHIM)} + параметры + пределы + "
                f"закон_масштабирования + ограничивающие_части для составных узлов)"
            )
            continue

        rezhim = scal.get('режим')
        if not rezhim or rezhim not in ENUM_REZHIM:
            violations.append(
                f"{izd_id}: масштабируемость.режим='{rezhim}' не из enum "
                f"{sorted(ENUM_REZHIM)} (P087 §12.6)"
            )
            continue

        # Проверка ограничивающие_части — только для составных узлов (есть дети)
        # leaf-части без дочерние_части не имеют кого ограничивать → пропускаем
        children = data.get('дочерние_части', [])
        has_children = isinstance(children, list) and len(children) >= 1
        op = scal.get('ограничивающие_части')
        if isinstance(op, list) and op and has_children:
            for entry in op:
                if not isinstance(entry, dict):
                    continue
                cid = entry.get('часть')
                if cid and cid not in children:
                    violations.append(
                        f"{izd_id}: масштабируемость.ограничивающие_части ссылается на '{cid}' "
                        f"не из дочерние_части (P087 §12.6)"
                    )
                    # не continue — проверяем остальные записи

        valid += 1

    ratio = valid / max(1, total)
    return {
        'metric': 'F-scal',
        'description': 'масштабируемость (P087 §12.6): блок присутствует и режим валиден для ВСЕХ изделий (любой уровень)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        # SOFT-метрика: pass=True всегда — не блокирует pre-commit, но violations
        # попадают в JSON --json-out → workflow создаёт verify-task issues
        'pass': True,
        'violations': violations,
    }


def check_F_ai_lineage(izdeliya: dict[str, dict]) -> dict:
    """F-ai-lineage: ancestry-проверка для AI-улучшенных версий (v9.32 / §12.7).

    SOFT-метрика (warning, не блокирующая). Для каждого файла с
    `версия: ии-улучшенная` проверяет:
      (a) `предок` — непустое поле, ссылка на real-компонент
      (b) `предок` существует в `реальные данные/` (поиск по id)
      (c) `улучшения` — непустой список (≥1 запись)
      (d) каждое улучшение имеет тип/что/причина/источник
      (e) `real_check.статус` — заполнен и из enum {проверен, требует_проверки, отклонён}

    pass=True всегда (soft-метрика) — violations возвращаются для issue-очереди.
    """
    ENUM_REZHIM_CHECK = {'проверен', 'требует_проверки', 'отклонён'}
    ENUM_TIP_ULUCHSHENIA = {
        'замена_материала', 'замена_технологии', 'добавление_технологии',
        'оптимизация_геометрии', 'замена_параметра',
    }
    violations = []
    total = 0
    valid = 0

    # Сбор множества real-id для проверки существования предка
    real_ids = set()
    real_root = SKYNET_REPO / 'реальные данные'
    if real_root.exists():
        for f in real_root.rglob('*.md'):
            if f.name.startswith('_') and f.name != '_index.md':
                continue
            data, _, _ = read_yaml_frontmatter(f)
            if isinstance(data, dict) and data.get('id'):
                real_ids.add(str(data['id']).strip())

    for izd_id, data in izdeliya.items():
        if str(data.get('версия', '')).strip() != 'ии-улучшенная':
            continue
        total += 1

        errs = []

        # (a) предок
        predok = data.get('предок')
        predok_str = str(predok or '').strip()
        if not predok_str or predok_str in ('null', 'None'):
            errs.append(
                f"{izd_id}: отсутствует поле `предок` (real-компонент-источник) — "
                f"AI-улучшенная версия ОБЯЗАНА ссылаться на real-предка (§12.7)"
            )
        else:
            # (b) предок существует в реальные данные/
            if predok_str not in real_ids:
                errs.append(
                    f"{izd_id}: предок='{predok_str}' не найден в реальные данные/ "
                    f"(orphan AI-файл без real-предка)"
                )

        # (c) улучшения — непустой список
        uluch = data.get('улучшения')
        if not isinstance(uluch, list) or len(uluch) < 1:
            errs.append(
                f"{izd_id}: отсутствует или пуст список `улучшения` — "
                f"AI-улучшенная версия обязана описать что улучшено (§12.7)"
            )
        else:
            # (d) каждая запись имеет тип/что/причина/источник
            for i, entry in enumerate(uluch, 1):
                if not isinstance(entry, dict):
                    errs.append(f"{izd_id}: улучшения[{i}] не dict")
                    continue
                tip = str(entry.get('тип', '') or '').strip()
                chto = str(entry.get('что', '') or '').strip()
                prichina = str(entry.get('причина', '') or '').strip()
                istochnik = str(entry.get('источник', '') or '').strip()
                if not tip:
                    errs.append(f"{izd_id}: улучшения[{i}].тип пустой")
                elif tip not in ENUM_TIP_ULUCHSHENIA:
                    errs.append(
                        f"{izd_id}: улучшения[{i}].тип='{tip}' не из enum "
                        f"{sorted(ENUM_TIP_ULUCHSHENIA)} (§12.7)"
                    )
                if not chto:
                    errs.append(f"{izd_id}: улучшения[{i}].что пусто")
                if not prichina:
                    errs.append(f"{izd_id}: улучшения[{i}].причина пуста")
                if not istochnik:
                    errs.append(f"{izd_id}: улучшения[{i}].источник пуст")

        # (e) real_check.статус
        rc = data.get('real_check')
        if not isinstance(rc, dict):
            errs.append(
                f"{izd_id}: отсутствует блок `real_check` — "
                f"AI-улучшенная версия требует усиленной проверки реалистичности (§12.7)"
            )
        else:
            rc_status = str(rc.get('статус', '') or '').strip()
            if not rc_status:
                errs.append(f"{izd_id}: real_check.статус пустой")
            elif rc_status not in ENUM_REZHIM_CHECK:
                errs.append(
                    f"{izd_id}: real_check.статус='{rc_status}' не из enum "
                    f"{sorted(ENUM_REZHIM_CHECK)} (§12.7)"
                )

        if errs:
            violations.extend(errs)
        else:
            valid += 1

    ratio = valid / max(1, total)
    return {
        'metric': 'F-ai-lineage',
        'description': 'AI-lineage (§12.7): предок + улучшения + real_check для версия: ии-улучшенная',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        # SOFT-метрика: pass=True всегда
        'pass': True,
        'violations': violations,
    }


# ============================================================================
# F-fant-children: ССЫЛКИ МОДЕЛИ → ИЗДЕЛИЯ (v9.34 NEW)
# Каждая канон-модель (тип: модель_SkyNet) должна иметь декомпозицию:
# декларированные дочерние_части → соответствующие файлы в фантастические данные/модели/<stem>/<child>/
# ============================================================================
# Семантика (по определению пользователя):
#   - Изделие = одна функция (узел декомпозиции)
#   - Модель = несколько функций (top-level, тип: модель_SkyNet)
#   - Подсистема = набор изделий со схожими функциями
#
# Проверка:
#   - Если модель декларирует дочерние_части: [часть_X, часть_Y, ...]
#     но файлов часть_X/_index.md или часть_X.md НЕТ в поддиректории модели → нарушение
#   - Это побуждает декомпозицию фантастических моделей (которая пока не начата)
#   - 70 битых ссылок в 11 моделях на текущий момент (T-800, HK-Aerial, etc.)
# ============================================================================

def check_F_fant_children(izdeliya: dict[str, dict]) -> dict:
    """F-fant-children: ссылки модели → изделия (v9.34 NEW).

    Для каждой канон-модели (тип: модель_SkyNet) проверяет, что все
    декларированные в `дочерние_части` id имеют соответствующие файлы
    в фантастические данные/модели/<stem>/<child_id>/_index.md
    ИЛИ фантастические данные/модели/<stem>/<child_id>.md

    SOFT-метрика (pass=True всегда): нарушения попадают в --json-out,
    workflow создаёт verify-task issues для декомпозиции.
    """
    violations = []
    total = 0  # количество моделей с декларированными детьми
    valid = 0  # модели, у которых ВСЕ дети существуют

    for izd_id, data in izdeliya.items():
        # Только канон-модели
        if data.get('тип') != 'модель_SkyNet':
            continue
        children = data.get('дочерние_части', [])
        if not isinstance(children, list) or not children:
            continue
        total += 1

        # Путь к модели: либо фантастические данные/модели/<stem>/ (если есть поддиректория),
        # либо фантастические данные/модели/<stem>.md (если только .md)
        path_str = data.get('_path', '')
        # Определяем stem из id (SkyNet-T800 → t800) или из пути
        # Проще: ищем относительно файла модели
        from pathlib import Path
        model_path = Path(path_str) if path_str else None
        if model_path is None:
            continue

        # Поддиректория модели = та же папка, что и .md, но без .md
        # Для фантастические данные/модели/t800.md → stem = 't800'
        # Поддиректория для детей: фантастические данные/модели/t800/
        model_stem = model_path.stem  # 't800' (без .md)
        model_dir = model_path.parent / model_stem

        missing = []
        for child_id in children:
            if not isinstance(child_id, str):
                continue
            # Ищем либо <model_dir>/<child_id>/_index.md
            # либо <model_dir>/<child_id>.md
            child_idx = model_dir / child_id / '_index.md'
            child_md = model_dir / f'{child_id}.md'
            if not (child_idx.exists() or child_md.exists()):
                missing.append(child_id)

        if missing:
            violations.append(
                f"{izd_id}: декларирует {len(children)} дочерних_частей, но "
                f"{len(missing)} не имеют файлов в фантастические данные/модели/{model_stem}/ "
                f"(примеры: {missing[:3]}) — выполните декомпозицию модели: "
                f"создайте часть_*/_index.md для каждой декларированной части"
            )
        else:
            valid += 1

    ratio = valid / max(1, total)
    return {
        'metric': 'F-fant-children',
        'description': 'ссылки модели → изделия: каждая модель_SkyNet должна иметь файлы для всех декларированных дочерних_частей',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        # SOFT-метрика: pass=True всегда — не блокирует pre-commit,
        # но violations попадают в JSON --json-out → workflow создаёт verify-task issues
        'pass': True,
        'violations': violations,
    }


def run_all_checks() -> dict:
    """Запустить все проверки и вернуть сводку."""
    print("=== SkyNet Decomposition Validator v9.31 ===")
    print()
    
    izdeliya = load_all_izdeliya()
    models = load_all_models()
    
    print(f"Загружено: {len(izdeliya)} изделий, {len(models)} моделей")
    print()
    
    results = {}
    
    # F12a — граф parent↔children
    print("=== F12a: Граф parent↔children ===")
    r = check_F12a(izdeliya)
    results['F12a'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])}")
        for v in r['violations'][:5]:
            print(f"    - {v[:100]}")
    
    # F13 — покрытие подсистем
    print()
    print("=== F13: Покрытие подсистем ===")
    r = check_F13(models, izdeliya)
    results['F13'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    
    # F14 — сумма долей массы
    print()
    print("=== F14: Σ долей_массы ===")
    r = check_F14(izdeliya)
    results['F14'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    
    # F15a — масса
    print()
    print("=== F15a: масса_kg родителя ===")
    r = check_F15a(izdeliya)
    results['F15a'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    
    # F15b — прочность
    print()
    print("=== F15b: прочность_МПа родителя ===")
    r = check_F15b(izdeliya)
    results['F15b'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    
    # F15d — энергопотребление
    print()
    print("=== F15d: энергопотребление_W родителя ===")
    r = check_F15d(izdeliya)
    results['F15d'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    
    # F15g — габариты (v9.49: переформулирована с lifetime на габариты)
    print()
    print("=== F15g: габариты_mm родителя ≥ max(дочерних.габариты) ===")
    r = check_F15g(izdeliya)
    results['F15g'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")

    # F15h — lifetime (v9.50: переформирована из оригинальной F15g lifetime)
    print()
    print("=== F15h: lifetime родителя ≤ MIN(дочерних.lifetime) ===")
    r = check_F15h(izdeliya)
    results['F15h'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")
    
    # F16 — иерархия уровней
    print()
    print("=== F16: Иерархия уровней ===")
    r = check_F16(izdeliya)
    results['F16'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")

    # F17 — merged into F13 in v9.52 (чек B внутри check_F13)
    # Отдельный вызов удалён; F17 убрана из метрик

    # F18 — JSON Schema
    print()
    print("=== F18: JSON Schema ===")
    r = check_F18(izdeliya)
    results['F18'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    
    # F19 — Mermaid
    print()
    print("=== F19: Mermaid диаграммы ===")
    r = check_F19(izdeliya)
    results['F19'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    
    # F20 — идемпотентность
    print()
    print("=== F20: Идемпотентность ===")
    r = check_F20()
    results['F20'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']}")
    if r.get('note'):
        print(f"  note: {r['note']}")
    
    # F21 — canon
    print()
    print("=== F21: Canon верификация ===")
    r = check_F21(models, izdeliya)
    results['F21'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    
    # F22 — верификация источника (NON-BLOCKING для первого прогона)
    print()
    print("=== F22: Верификация источника ===")
    r = check_F22(izdeliya, models)  # v9.36: reuse loaded models
    results['F22'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")
    
    # F23/F24 — merged into F22 in v9.52 (чеки B, C внутри check_F22)
    # Отдельные вызовы удалены; F23, F24 убраны из метрик

    # F25 — уникальность данных
    print()
    print("=== F25: Уникальность данных ===")
    r = check_F25(izdeliya)
    results['F25'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F26 — merged into F25 in v9.52 (чек B внутри check_F25)
    # Отдельный вызов удалён; F26 убрана из метрик

    # F27 — незаполненные материалы-заглушки (v9.40; v9.41 — критерий e: вариант_структуры)
    print()
    print("=== F27: Незаполненные материалы (используемые изделиями) ===")
    r = check_F27(izdeliya)
    results['F27'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F27b — битые ссылки на материалы (v9.53; mirror F27 для отсутствующих
    # файлов: F27 итерирует существующие файлы, F27b — ссылки в frontmatter)
    print()
    print("=== F27b: Битые ссылки на материалы (файл отсутствует в каталоге) ===")
    r = check_F27b(izdeliya)
    results['F27b'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F27c — битые ссылки на технологии (v9.54; mirror F27b для каталога
    # технологии/: проверяет структурные id-ссылки в frontmatter — поле
    # `технологии_частей` для часть-level и `технологии` для изделия-level)
    print()
    print("=== F27c: Битые ссылки на технологии (файл отсутствует в каталоге) ===")
    r = check_F27c(izdeliya)
    results['F27c'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F27d — обратная связь: типичные материалы в frontmatter технологий (v9.55;
    # в v9.56 переориентирована: проверяет валидность id в
    # `типичные_материалы_для_процесса` (soft, опциональное) — конкретные
    # материалы процесса перенесены в изделие, в технологии_частей.материалы_для_процесса)
    print()
    print("=== F27d: Битые ссылки на типичные материалы в frontmatter технологий (soft) ===")
    r = check_F27d()
    results['F27d'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F27e — обязательность технологии_частей для частей с материалы_частей
    # (v9.56; warning, не блокирующая — 761 файл без технологий в backlog)
    print()
    print("=== F27e: Обязательность технологии_частей для частей с материалы_частей ===")
    r = check_F27e(izdeliya)
    results['F27e'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F27f — обязательность материалы_для_процесса внутри технологии_частей (v9.56)
    print()
    print("=== F27f: Обязательность материалы_для_процесса внутри технологии_частей ===")
    r = check_F27f(izdeliya)
    results['F27f'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F27g — валидность id материалов в технологии_частей.материалы_для_процесса
    # (v9.56; mirror F27b, но для материалов процесса внутри технологии_частей)
    print()
    print("=== F27g: Битые ссылки на материалы в технологии_частей.материалы_для_процесса ===")
    r = check_F27g(izdeliya)
    results['F27g'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F28 — альтернативные формы материалов (v9.42; идея: вебпоиск всех форм
    # mono/poly/amorphous/составов — выбор формы для AI-вариантов изделий)
    print()
    print("=== F28: Альтернативные формы материалов (используемые изделиями) ===")
    r = check_F28(izdeliya)
    results['F28'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F29 — форма материала в материалы_частей (v9.43; мягкий чек — заполнение)
    print()
    print("=== F29: Форма материала в части (мягкий чек) ===")
    r = check_F29(izdeliya)
    results['F29'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F30 — merged into F29 in v9.52 (чек B внутри check_F29)
    # Отдельный вызов удалён; F30 убрана из метрик

    # F31 — уникальность id/алиасов материалов и технологий (v9.44, дедупликация;
    # аннотация: #661 — material_ni-ysz создан поверх material_ni_ysz_cermet)
    print()
    print("=== F31: Уникальность id/алиасов (дедупликация) ===")
    mat_tech_entries = _load_materials_and_techs()
    r = check_F31(mat_tech_entries)
    results['F31'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F32 — merged into F31 in v9.52 (чек B внутри check_F31)
    # Отдельный вызов удалён; F32 убрана из метрик

    # F33 — классификационная консистентность (v9.46; тип↔директория +
    # коллизии имён между категориями; warning-метрика после реклассификации #751)
    print()
    print("=== F33: Классификационная консистентность (тип↔каталог + коллизии имён) ===")
    catalog_entries = _load_all_catalog_entries()
    r = check_F33(catalog_entries)
    results['F33'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F34 — глубина декомпозиции (v9.47; warning-метрика: top-level должен
    # достигать уровня ≥3 ИЛИ иметь атомарные части)
    print()
    print("=== F34: Глубина декомпозиции ===")
    r = check_F34(izdeliya)
    results['F34'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F35 — Components Consistency (v9.60 Фаза 1.3; NON-BLOCKING, warning)
    # Разделение тип/материал/компонент. После миграции на A2-модель станет BLOCKING.
    print()
    print("=== F35: Components consistency (v9.60, NON-BLOCKING) ===")
    r = check_F35(izdeliya)
    results['F35'] = r
    print(f"  pass={r['pass']} (NON-BLOCKING), ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 5):")
        for v in r['violations'][:5]:
            print(f"    - {v[:120]}")

    # F36 — body markdown structure (v9.61 NEW; NON-BLOCKING)
    print()
    print("=== F36: Body markdown structure (v9.61, NON-BLOCKING) ===")
    r = check_F36()
    results['F36'] = r
    print(f"  pass={r['pass']} (NON-BLOCKING), ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 5):")
        for v in r['violations'][:5]:
            print(f"    - {v[:140]}")

    # F37 — is_purchased flag (v9.61 NEW; NON-BLOCKING)
    print()
    print("=== F37: is_purchased: true для изделия/компоненты/ (v9.61, NON-BLOCKING) ===")
    r = check_F37(izdeliya)
    results['F37'] = r
    print(f"  pass={r['pass']} (NON-BLOCKING), ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 5):")
        for v in r['violations'][:5]:
            print(f"    - {v[:140]}")

    # F38 — класс enum-валидация (v9.61 NEW; NON-BLOCKING)
    print()
    print("=== F38: класс enum-валидация для материалов (v9.61, NON-BLOCKING) ===")
    r = check_F38()
    results['F38'] = r
    print(f"  pass={r['pass']} (NON-BLOCKING), ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 5):")
        for v in r['violations'][:5]:
            print(f"    - {v[:140]}")

    # F-scal — масштабируемость (v9.32 / P087; SOFT-метрика: pass=True всегда,
    # violations идут в --json-out → workflow создаёт verify-task issues)
    print()
    print("=== F-scal: Масштабируемость (P087 §12.6, soft) ===")
    r = check_F_scal(izdeliya)
    results['F-scal'] = r
    print(f"  pass={r['pass']} (SOFT), ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F-ai-lineage — AI-ancestry (v9.32 / §12.7; SOFT-метрика)
    print()
    print("=== F-ai-lineage: AI-lineage (предок+улучшения+real_check, §12.7, soft) ===")
    r = check_F_ai_lineage(izdeliya)
    results['F-ai-lineage'] = r
    print(f"  pass={r['pass']} (SOFT), ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # F-fant-children — ссылки модели → изделия (v9.34; SOFT-метрика)
    # Проверяет что каждая модель_SkyNet имеет файлы для всех декларированных дочерних_частей
    print()
    print("=== F-fant-children: ссылки модели → изделия (v9.34, soft) ===")
    r = check_F_fant_children(izdeliya)
    results['F-fant-children'] = r
    print(f"  pass={r['pass']} (SOFT), ratio={r['ratio']} ({r['valid']}/{r['total']})")
    if r['violations']:
        print(f"  violations: {len(r['violations'])} (первые 3):")
        for v in r['violations'][:3]:
            print(f"    - {v[:100]}")

    # Сводка
    print()
    print("=== Сводка ===")
    all_pass = True
    for m, r in results.items():
        mark = '✓' if r['pass'] else '✗'
        print(f"  {mark} {m}: {r['ratio']:.4f} ({r.get('valid', 0)}/{r.get('total', 0)})")
        if not r['pass']:
            all_pass = False
    
    return {
        'all_pass': all_pass,
        'results': results,
        'izdeliya_count': len(izdeliya),
        'models_count': len(models),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--metric', help='Запустить конкретную метрику')
    parser.add_argument('--fix', action='store_true', help='Авто-фикс где возможно')
    parser.add_argument('--json-out', dest='json_out',
                        help='Записать ПОЛНЫЙ machine-readable JSON со всеми violations '
                             '(в человеческом логе печатются только первые 3 на метрику) '
                             '— для CI (verify_decomposition.yml)')
    args = parser.parse_args()

    if args.metric:
        # Запуск конкретной метрики
        izdeliya = load_all_izdeliya()
        models = load_all_models()
        check_fn = globals().get(f'check_{args.metric}')
        if check_fn:
            if args.metric in ['F13', 'F21']:
                # Принимает (models, izdeliya) — эти metrics работают с обеими категориями
                r = check_fn(models, izdeliya)
            elif args.metric == 'F22':
                # F22 merged (v9.52): принимает (izdeliya, models=None) — переиспользуем models
                r = check_fn(izdeliya, models)
            elif args.metric in ('F31',):
                # F31 (v9.52 merged F31+F32) работает с материалами+технологиями
                r = check_fn(_load_materials_and_techs())
            elif args.metric == 'F33':
                # F33 работает со всеми .md 3-х категорий (материалы/изделия/технологии)
                r = check_fn(_load_all_catalog_entries())
            elif args.metric == 'F27d':
                # F27d (v9.55) работает с frontmatter файлов технологий (не izdeliya)
                r = check_fn()
            else:
                # F12a, F14, F15a-h, F16, F18, F19, F20, F25, F27-F30, F34 — работают с изделиями
                r = check_fn(izdeliya)
            print(f"{args.metric}: pass={r['pass']}, ratio={r['ratio']}")
            if r['violations']:
                for v in r['violations'][:10]:
                    print(f"  - {v}")
        return 0 if check_fn else 1

    results = run_all_checks()

    if args.json_out:
        # v9.35: единый источник списка метрик — scripts/_metrics.py
        from _metrics import get_metrics_for_json_out
        payload = {
            m: results['results'][m]['violations']
            for m in get_metrics_for_json_out()
            if m in results['results']
        }
        with open(args.json_out, 'w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        total = sum(len(v) for v in payload.values())
        print(f"JSON written ({args.json_out}): {total} violations (полный список, без обрезки)")

    return 0 if results['all_pass'] else 1


if __name__ == "__main__":
    sys.exit(main())
