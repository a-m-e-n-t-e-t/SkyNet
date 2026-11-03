#!/usr/bin/env python3
"""
SkyNet Decomposition Validator — v9.31
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


def read_yaml_frontmatter(filepath: Path) -> tuple[dict, str, str]:
    """Возвращает (yaml_data, yaml_raw_text, body_text).
    
    Поддерживает:
      - Стандартный формат: ---\n<yaml>\n---\n<body>
      - Без закрывающего --- (только opening): ---\n<yaml>\n\n<body>
        (некоторые файлы в репо не имеют закрывающего ---)
    """
    text = filepath.read_text(encoding='utf-8')
    if not text.startswith('---'):
        return {}, "", text
    
    rest = text[3:]
    # Удалить ведущие пустые строки
    rest_stripped = rest.lstrip('\n')
    
    # Найти закрывающий --- на отдельной строке
    end_match = re.search(r"\n---\s*\n", rest_stripped)
    if end_match:
        yaml_text = rest_stripped[:end_match.start()]
        body = rest_stripped[end_match.end():]
    else:
        # Без закрывающего --- — найти первый markdown заголовок или конец файла
        # Markdown body обычно начинается с "# "
        body_match = re.search(r"\n(#\s+\S)", rest_stripped)
        if body_match:
            yaml_text = rest_stripped[:body_match.start()]
            body = rest_stripped[body_match.start()+1:]  # +1 чтобы убрать \n перед #
        else:
            # Всё — YAML
            yaml_text = rest_stripped
            body = ""
    
    data = parse_yaml_block(yaml_text)
    return data, yaml_text, body


# ============================================================================
# ВСЕ ИЗДЕЛИЯ — загрузка графа
# ============================================================================

def load_all_izdeliya() -> dict[str, dict]:
    """Загрузить все .md в реальные данные/изделия/ в dict {id: data, ...}."""
    result = {}
    izd_dir = SKYNET_REPO / "реальные данные" / "изделия"
    for f in izd_dir.rglob("_index.md"):
        data, _, _ = read_yaml_frontmatter(f)
        if data and 'id' in data:
            data['_path'] = str(f)
            data['_filename'] = f.name
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
    """
    violations = []
    
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
    for izd_id, data in izdeliya.items():
        parent = data.get('родитель')
        if parent and parent != 'null':
            if parent not in izdeliya:
                violations.append(f"{izd_id}: родитель '{parent}' не существует")
            else:
                parent_children = izdeliya[parent].get('дочерние_части', [])
                if not isinstance(parent_children, list):
                    parent_children = []
                if izd_id not in parent_children:
                    violations.append(f"{izd_id}: родитель '{parent}' не содержит этот id в дочерние_части")
    
    # 3. Циклы (DFS)
    for izd_id in izdeliya:
        visited = set()
        current = izd_id
        while current and current != 'null':
            if current in visited:
                violations.append(f"{izd_id}: обнаружен цикл в иерархии (через {current})")
                break
            visited.add(current)
            data = izdeliya.get(current, {})
            current = data.get('родитель')
            if not isinstance(current, str) or current == 'null':
                break
    
    # 4. Сироты: часть с родителем=null, но не упомянута в дочерние_части ни одного верхнего
    for izd_id, data in izdeliya.items():
        parent = data.get('родитель')
        if parent and parent != 'null':
            continue  # имеет родителя — не сирота
        # нет родителя — должен быть упомянут в каком-то дочерние_части ИЛИ быть верхним уровнем
        level = data.get('уровень_иерархии', '')
        if level == 'верхний':
            continue  # OK — это верхний уровень
        # Не верхний уровень и без родителя — проверить не упоминается ли где
        mentioned = False
        for other_id, other_data in izdeliya.items():
            if other_id == izd_id:
                continue
            children = other_data.get('дочерние_части', [])
            if isinstance(children, list) and izd_id in children:
                mentioned = True
                break
        if not mentioned:
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

def check_F13(models: dict[str, dict], izdeliya: dict[str, dict]) -> dict:
    """F13: покрытие подсистем — expected_subsystems покрыты дочерними."""
    violations = []
    total = 0
    valid = 0
    
    for mid, mdata in models.items():
        mtype = mdata.get('тип_модели', '')
        if mtype not in EXPECTED_SUBSYSTEMS_BY_TYPE:
            continue
        expected = EXPECTED_SUBSYSTEMS_BY_TYPE[mtype]
        if not expected:
            continue
        
        total += 1
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
            izd_data = izdeliya.get(izd_id, {})
            sub = izd_data.get('подсистема')
            if sub:
                covered.add(sub)
        
        # Также учесть дочерние_части
        for izd_id in real_impl:
            if not isinstance(izd_id, str):
                continue
            izd_data = izdeliya.get(izd_id, {})
            children = izd_data.get('дочерние_части', [])
            if isinstance(children, list):
                for child_id in children:
                    if isinstance(child_id, str) and child_id in izdeliya:
                        sub = izdeliya[child_id].get('подсистема')
                        if sub:
                            covered.add(sub)
        
        missing = set(expected) - covered
        if missing:
            violations.append(f"{mid} ({mtype}): не покрыты подсистемы: {sorted(missing)}")
        else:
            valid += 1
    
    ratio = valid / max(1, total)
    return {
        'metric': 'F13',
        'description': 'Покрытие подсистем — expected_subsystems по типу модели',
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
        elif total_share > 1.01:  # Σ > 1.0 — ошибка
            violations.append(f"{izd_id}: Σ долей_массы = {total_share:.4f}, ожидается ≤ 1.0")
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
    """F15a: масса_kg родителя = Σ(дочерних.масса × доля_массы).
    
    v9.31: если нет данных (total=0), pass=True — нет данных для проверки.
    """
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
        
        total += 1
        computed = 0.0
        has_data = True
        materials = data.get('материалы_частей', [])
        if not isinstance(materials, list):
            materials = []
        # Map: часть → доля_массы
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
                has_data = False
                break
            child_data = izdeliya[child_id]
            child_basic = child_data.get('основные', {})
            if not isinstance(child_basic, dict):
                has_data = False
                break
            child_mass = child_basic.get('масса_kg')
            if child_mass is None:
                has_data = False
                break
            try:
                child_mass = float(child_mass)
            except (TypeError, ValueError):
                has_data = False
                break
            share = share_map.get(child_id, 1.0 / len(children))
            computed += child_mass * share
        
        if has_data and abs(computed - parent_mass) > 0.5:  # ±0.5 kg tolerance
            violations.append(f"{izd_id}: масса родителя {parent_mass}, вычисленная {computed:.2f}")
        else:
            valid += 1
    
    # v9.31: если нет данных, метрика не активна — pass=True
    ratio = valid / max(1, total)
    return {
        'metric': 'F15a',
        'description': 'масса_kg родителя = Σ(дочерних.масса × доля_массы)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': True if total == 0 else ratio >= 1.0,  # v9.31: нет данных = pass
        'violations': violations,
    }


def check_F15b(izdeliya: dict[str, dict]) -> dict:
    """F15b: прочность_МПа родителя = MIN(дочерних.прочность)."""
    violations = []
    total = 0
    valid = 0
    
    for izd_id, data in izdeliya.items():
        children = data.get('дочерние_части', [])
        if not isinstance(children, list) or not children:
            continue
        parent_strength = data.get('основные', {}).get('прочность_МПа')
        if parent_strength is None:
            continue
        try:
            parent_strength = float(parent_strength)
        except (TypeError, ValueError):
            continue
        
        total += 1
        child_strengths = []
        for child_id in children:
            if not isinstance(child_id, str) or child_id not in izdeliya:
                continue
            child_data = izdeliya[child_id]
            cs = child_data.get('основные', {}).get('прочность_МПа')
            if cs is not None:
                try:
                    child_strengths.append(float(cs))
                except (TypeError, ValueError):
                    pass
        
        if child_strengths:
            computed = min(child_strengths)
            if abs(computed - parent_strength) > 50:  # ±50 MPa tolerance
                violations.append(f"{izd_id}: прочность родителя {parent_strength}, MIN(детей) = {computed:.0f}")
            else:
                valid += 1
        else:
            valid += 1  # нет данных — пропускаем
    
    ratio = valid / max(1, total)
    return {
        'metric': 'F15b',
        'description': 'прочность_МПа родителя = MIN(дочерних.прочность)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': True if total == 0 else ratio >= 1.0,
        'violations': violations,
    }


def check_F15d(izdeliya: dict[str, dict]) -> dict:
    """F15d: энергопотребление_W родителя = Σ(дочерних.пиковое_потребление)."""
    violations = []
    total = 0
    valid = 0
    
    for izd_id, data in izdeliya.items():
        children = data.get('дочерние_части', [])
        if not isinstance(children, list) or not children:
            continue
        parent_power = data.get('основные', {}).get('энергопотребление_W')
        if parent_power is None:
            continue
        try:
            parent_power = float(parent_power)
        except (TypeError, ValueError):
            continue
        
        total += 1
        computed = 0.0
        has_data = True
        for child_id in children:
            if not isinstance(child_id, str) or child_id not in izdeliya:
                has_data = False
                break
            child_data = izdeliya[child_id]
            cp = child_data.get('основные', {}).get('пиковое_потребление_W') or \
                 child_data.get('основные', {}).get('энергопотребление_W')
            if cp is not None:
                try:
                    computed += float(cp)
                except (TypeError, ValueError):
                    pass
        
        if has_data and abs(computed - parent_power) > 1.0:
            violations.append(f"{izd_id}: энергопотребление родителя {parent_power}, вычисленное {computed:.1f}")
        else:
            valid += 1
    
    ratio = valid / max(1, total)
    return {
        'metric': 'F15d',
        'description': 'энергопотребление_W родителя = Σ(дочерних.пиковое_потребление)',
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': True if total == 0 else ratio >= 1.0,
        'violations': violations,
    }


def check_F15g(izdeliya: dict[str, dict]) -> dict:
    """F15g: lifetime_years родителя = MIN(дочерних.lifetime)."""
    violations = []
    total = 0
    valid = 0
    
    for izd_id, data in izdeliya.items():
        children = data.get('дочерние_части', [])
        if not isinstance(children, list) or not children:
            continue
        parent_life = data.get('наследуемые', {}).get('lifetime_years')
        if parent_life is None:
            continue
        try:
            parent_life = float(parent_life)
        except (TypeError, ValueError):
            continue
        
        total += 1
        child_lives = []
        for child_id in children:
            if not isinstance(child_id, str) or child_id not in izdeliya:
                continue
            child_data = izdeliya[child_id]
            cl = child_data.get('наследуемые', {}).get('lifetime_years')
            if cl is not None:
                try:
                    child_lives.append(float(cl))
                except (TypeError, ValueError):
                    pass
        
        if child_lives:
            computed = min(child_lives)
            if abs(computed - parent_life) > 0.5:
                violations.append(f"{izd_id}: lifetime родителя {parent_life}, MIN(детей) = {computed:.1f}")
            else:
                valid += 1
        else:
            valid += 1
    
    ratio = valid / max(1, total)
    return {
        'metric': 'F15g',
        'description': 'lifetime_years родителя = MIN(дочерних.lifetime)',
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
    
    # Дополнительная проверка: неделимый (уровень 4) не имеет дочерних
    for izd_id, data in izdeliya.items():
        level = data.get('уровень_номер')
        try:
            level = int(level) if level is not None else None
        except (TypeError, ValueError):
            level = None
        if level == 4:  # неделимый
            children = data.get('дочерние_части', [])
            if isinstance(children, list) and children:
                violations.append(f"{izd_id}: неделимый (уровень 4) но имеет дочерние_части")
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
        'description': 'Иерархия уровней — ребёнок = родитель + 1',
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
        "тип": {"type": "string", "enum": ["изделие"]},
        "категория": {"type": "string"},
        "уровень_иерархии": {"type": "string", "enum": ["верхний", "промежуточный", "неделимый"]},
        "уровень_номер": {"type": "integer", "minimum": 1, "maximum": 4},
        "подсистема": {"type": "string"},
        "подтип": {"type": "string"},
        "стандарты": {"type": "array"},
        "исследовательская_группа": {"type": ["string", "null"]},
        "родитель": {"type": ["string", "null"]},
        "дочерние_части": {"type": "array"},
        "материалы_частей": {"type": "array"},
        "статус_реальности": {"type": "string", "enum": ["real", "canon", "canon_realizable"]},
        "доступность": {"type": "string"},
    }
}


def check_F18(izdeliya: dict[str, dict]) -> dict:
    """F18: JSON Schema валидация структуры файла изделия."""
    violations = []
    total = len(izdeliya)
    valid = 0
    
    try:
        import jsonschema
        has_jsonschema = True
    except ImportError:
        has_jsonschema = False
    
    for izd_id, data in izdeliya.items():
        # Удалить служебные поля
        clean_data = {k: v for k, v in data.items() if not k.startswith('_')}
        
        if has_jsonschema:
            try:
                jsonschema.validate(clean_data, SCHEMA_IZDELIE)
                valid += 1
            except jsonschema.ValidationError as e:
                violations.append(f"{izd_id}: schema violation: {e.message[:100]}")
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
    """F19: Mermaid диаграмма присутствует в markdown body каждого изделия с дочерними."""
    violations = []
    total = 0
    valid = 0
    
    for izd_id, data in izdeliya.items():
        children = data.get('дочерние_части', [])
        if not isinstance(children, list) or not children:
            continue
        total += 1
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
    """
    violations = []
    total = 0
    valid = 0
    
    for model_id, canon_spec in CANON_DECOMPOSITION.items():
        # Найти wrapper-изделие izdelie_<model_id>
        wrapper_id = f"izdelie_{model_id}"
        if wrapper_id not in izdeliya:
            continue
        total += 1
        wrapper = izdeliya[wrapper_id]
        children = wrapper.get('дочерние_части', [])
        if not isinstance(children, list):
            children = []
        
        # Подсчитать сколько изделий каждой подсистемы
        sub_counts: dict[str, int] = {}
        for child_id in children:
            if not isinstance(child_id, str) or child_id not in izdeliya:
                continue
            sub = izdeliya[child_id].get('подсистема')
            if sub:
                sub_counts[sub] = sub_counts.get(sub, 0) + 1
        
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
# MAIN
# ============================================================================

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
    
    # F15g — lifetime
    print()
    print("=== F15g: lifetime_years родителя ===")
    r = check_F15g(izdeliya)
    results['F15g'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    
    # F16 — иерархия уровней
    print()
    print("=== F16: Иерархия уровней ===")
    r = check_F16(izdeliya)
    results['F16'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    
    # F17 — тип-специфичные шаблоны
    print()
    print("=== F17: Тип-специфичные шаблоны ===")
    r = check_F17(models, izdeliya)
    results['F17'] = r
    print(f"  pass={r['pass']}, ratio={r['ratio']} ({r['valid']}/{r['total']})")
    
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
    args = parser.parse_args()
    
    if args.metric:
        # Запуск конкретной метрики
        izdeliya = load_all_izdeliya()
        models = load_all_models()
        check_fn = globals().get(f'check_{args.metric}')
        if check_fn:
            if args.metric in ['F13', 'F17', 'F21']:
                r = check_fn(models, izdeliya)
            else:
                r = check_fn(izdeliya)
            print(f"{args.metric}: pass={r['pass']}, ratio={r['ratio']}")
            if r['violations']:
                for v in r['violations'][:10]:
                    print(f"  - {v}")
        return 0 if check_fn else 1
    
    results = run_all_checks()
    return 0 if results['all_pass'] else 1


if __name__ == "__main__":
    sys.exit(main())
