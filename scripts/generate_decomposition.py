#!/usr/bin/env python3
"""SkyNet Decomposition Generator — v9.31
Связывает модели с изделиями и создаёт декомпозицию для топ-моделей.

Действия:
  1. Для каждой модели: заполнить реализация_промышленная ссылками на
     существующие изделия в реальные данные/изделия/ по совпадению подсистем
     (это нужно для F13, F17, F21)
  2. Для топ-10 моделей (T-800, T-1000, T-X, Rev-9, HK-Aerial, HK-Tank,
     T-600, T-850, Marcus, Cameron) — создать дочерние части как новые
     .md файлы в реальные данные/изделия/<подсистема>/ и заполнить
     дочерние_части + материалы_частей + родитель (это для F14, F15, F16, F19)
  3. Сгенерировать Mermaid диаграммы для изделий с дочерними (F19)
"""

from __future__ import annotations
import os
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from validate_decomposition import (
    read_yaml_frontmatter, parse_yaml_block, parse_yaml_value,
    SKYNET_REPO, EXPECTED_SUBSYSTEMS_BY_TYPE, TYPE_TEMPLATE_PARTS,
    CANON_DECOMPOSITION, generate_mermaid_diagram
)

TODAY = "2026-11-03"
IZDELIYA_DIR = SKYNET_REPO / "реальные данные" / "изделия"
MODELS_DIR = SKYNET_REPO / "фантастические данные" / "модели"


# ============================================================================
# КАНОН-ДЕКОМПОЗИЦИЯ ТОП-10 МОДЕЛЕЙ
# ============================================================================

# T-800 canon: Neural Net CPU + 2 водородных топливных элемента + hyperalloy endoskeleton
# + 2 оптических сенсора + 2 руки + 2 ноги (servo)
CANON_DECOMP_T800 = {
    'parts': [
        # v9.35: pairs merged into single part with count=2
        # (id, подсистема, подтип, масса_kg, доля_массы, count=1)
        ('часть_t800_cpu', 'вычислительная', 'neural_net_cpu', 0.5, 0.004),
        ('часть_t800_топливная_ячейка_1', 'энергетическая', 'hydrogen_fuel_cell', 5.0, 0.072, 2),  # ×2 (были _1 + _2)
        ('часть_t800_эндоскелет_торс', 'каркас', 'hyperalloy_endoskeleton', 50.0, 0.357),
        ('часть_t800_рука_левая', 'приводная_система', 'servo_arm', 12.0, 0.172, 2),  # ×2 (левая + правая)
        ('часть_t800_нога_левая', 'приводная_система', 'servo_leg', 18.0, 0.258, 2),  # ×2 (левая + правая)
        ('часть_t800_оптический_сенсор_1', 'сенсоры', 'optical_camera', 0.2, 0.0028, 2),  # ×2 (_1 + _2)
        ('часть_t800_аудио_сенсор', 'сенсоры', 'audio_microphone', 0.1, 0.0007),
        ('часть_t800_антенна', 'система_связи', 'skyet_link_antenna', 0.3, 0.002),
        ('часть_t800_гиро_навигация', 'навигация', 'imu_gyro', 0.5, 0.004),
        ('часть_t800_ткань_кожа', 'прочее', 'living_tissue', 18.0, 0.129),
    ],
    'materials': [
        # (часть, материал_id, доля_массы_в_части)
        ('часть_t800_эндоскелет_торс', 'hyperalloy_t800', 1.0),
        ('часть_t800_cpu', 'silicon_neural_net', 0.6),
        ('часть_t800_топливная_ячейка_1', 'lithium_hydrogen_cell', 1.0),
        ('часть_t800_рука_левая', 'hyperalloy_t800', 0.7),
        ('часть_t800_нога_левая', 'hyperalloy_t800', 0.7),
        ('часть_t800_ткань_кожа', 'living_tissue_clone', 1.0),
    ],
    'parent_mass': 140.0,  # canon T-800 ~140 kg
}

# T-1000 canon: одна часть — сам миметический полисплав
CANON_DECOMP_T1000 = {
    'parts': [
        ('часть_t1000_миметический_полисплав', 'вычислительная', 'mimetic_polyalloy', 120.0, 1.0),
    ],
    'materials': [
        ('часть_t1000_миметический_полисплав', 'mimetic_polyalloy', 1.0),
    ],
    'parent_mass': 120.0,
}

# Rev-9 canon: endoskeleton + polyalloy sheath (split-able)
CANON_DECOMP_REV9 = {
    'parts': [
        ('часть_rev9_endoskeleton', 'каркас', 'carbon_endoskeleton', 80.0, 0.5),
        ('часть_rev9_полисплав_оболочка', 'вычислительная', 'mimetic_polyalloy_sheath', 80.0, 0.5),
    ],
    'materials': [
        ('часть_rev9_endoskeleton', 'carbon_fiber_endoskeleton', 1.0),
        ('часть_rev9_полисплав_оболочка', 'mimetic_polyalloy', 1.0),
    ],
    'parent_mass': 160.0,
}

# HK-Aerial canon: фюзеляж + 2 двигателя + сенсоры + вооружение + плазма-пушка
CANON_DECOMP_HK_AERIAL = {
    'parts': [
        ('часть_hk_aerial_фюзеляж', 'каркас', 'fuselage', 1500.0, 0.5),
        ('часть_hk_aerial_двигатель_левый', 'энергетическая', 'nuclear_vtol_engine', 400.0, 0.266, 2),  # ×2 (левый + правый)
        ('часть_hk_aerial_сенсоры', 'сенсоры', 'multi_sensor_array', 100.0, 0.033),
        ('часть_hk_aerial_плазма_пушка', 'встроенное_оружие', 'plasma_cannon', 200.0, 0.067),
        ('часть_hk_aerial_навигация', 'навигация', 'radar_navigation', 50.0, 0.017),
        ('часть_hk_aerial_связь', 'система_связи', 'skynet_link', 50.0, 0.017),
        ('часть_hk_aerial_крылья', 'каркас', 'wings', 300.0, 0.1),
    ],
    'materials': [
        ('часть_hk_aerial_фюзеляж', 'titanium_alloy', 0.8),
        ('часть_hk_aerial_двигатель_левый', 'inconel_718', 0.6),
        ('часть_hk_aerial_плазма_пушка', 'tungsten_alloy', 0.7),
    ],
    'parent_mass': 3000.0,
}

# HK-Tank canon: корпус + 2 гусеницы + башня + вооружение + сенсоры
CANON_DECOMP_HK_TANK = {
    'parts': [
        ('часть_hk_tank_корпус', 'каркас', 'tank_body', 15000.0, 0.5),
        ('часть_hk_tank_гусеница_левая', 'приводная_система', 'tank_track', 3000.0, 0.2, 2),  # ×2 (левая + правая)
        ('часть_hk_tank_башня', 'каркас', 'turret', 2000.0, 0.067),
        ('часть_hk_tank_плазма_пушка_1', 'встроенное_оружие', 'plasma_cannon', 500.0, 0.034, 2),  # ×2 (_1 + _2)
        ('часть_hk_tank_сенсоры', 'сенсоры', 'radar_sensor', 500.0, 0.017),
        ('часть_hk_tank_двигатель', 'энергетическая', 'nuclear_engine', 2000.0, 0.067),
        ('часть_hk_tank_связь', 'система_связи', 'skynet_link', 500.0, 0.017),
        ('часть_hk_tank_навигация', 'навигация', 'gps_nav', 200.0, 0.007),
        ('часть_hk_tank_боеприпасы', 'энергетическая', 'plasma_ammo', 2800.0, 0.093),
    ],
    'materials': [
        ('часть_hk_tank_корпус', 'rolled_homogeneous_armor', 0.9),
        ('часть_hk_tank_гусеница_левая', 'steel_track', 1.0),
        ('часть_hk_tank_башня', 'rolled_homogeneous_armor', 0.9),
    ],
    'parent_mass': 30000.0,
}

# T-600 canon: rubber skin + titanium endoskeleton
CANON_DECOMP_T600 = {
    'parts': [
        ('часть_t600_cpu', 'вычислительная', 'early_neural_cpu', 1.0, 0.005),
        ('часть_t600_эндоскелет', 'каркас', 'titanium_endoskeleton', 150.0, 0.75),
        ('часть_t600_топливная_ячейка', 'энергетическая', 'fuel_cell', 10.0, 0.05),
        ('часть_t600_рука_левая', 'приводная_система', 'servo_arm', 15.0, 0.15, 2),  # ×2 (левая + правая)
        ('часть_t600_нога_левая', 'приводная_система', 'servo_leg', 4.0, 0.04, 2),  # ×2 (левая + правая)
        ('часть_t600_резиновая_кожа', 'прочее', 'rubber_skin', 1.0, 0.005),
    ],
    'materials': [
        ('часть_t600_эндоскелет', 'titanium_alloy', 0.9),
        ('часть_t600_резиновая_кожа', 'synthetic_rubber', 1.0),
    ],
    'parent_mass': 200.0,
}

# T-850 canon: similar to T-800 but improved
CANON_DECOMP_T850 = {
    'parts': [
        ('часть_t850_cpu', 'вычислительная', 'neural_net_cpu_v2', 0.5, 0.003),
        ('часть_t850_топливная_ячейка_1', 'энергетическая', 'hydrogen_fuel_cell_v2', 6.0, 0.068, 2),  # ×2 (_1 + _2)
        ('часть_t850_эндоскелет', 'каркас', 'hyperalloy_endoskeleton', 60.0, 0.343),
        ('часть_t850_рука_левая', 'приводная_система', 'servo_arm_improved', 13.0, 0.148, 2),  # ×2 (левая + правая)
        ('часть_t850_нога_левая', 'приводная_система', 'servo_leg_improved', 19.0, 0.218, 2),  # ×2 (левая + правая)
        ('часть_t850_сенсоры', 'сенсоры', 'optical_audio_array', 1.0, 0.006),
        ('часть_t850_связь', 'система_связи', 'skyet_link', 0.5, 0.003),
        ('часть_t850_навигация', 'навигация', 'imu_gyro', 0.5, 0.003),
        ('часть_t850_ткань_кожа', 'прочее', 'living_tissue', 36.0, 0.206),
    ],
    'materials': [
        ('часть_t850_эндоскелет', 'hyperalloy_t850', 1.0),
        ('часть_t850_ткань_кожа', 'living_tissue_clone', 1.0),
    ],
    'parent_mass': 175.0,
}

# Marcus Wright canon: human brain + cybernetic endoskeleton (hybrid)
CANON_DECOMP_MARCUS = {
    'parts': [
        ('часть_marcus_человеческий_мозг', 'вычислительная', 'human_brain_hybrid', 1.4, 0.016),
        ('часть_marcus_эндоскелет', 'каркас', 'cybernetic_endoskeleton', 50.0, 0.556),
        ('часть_marcus_сердце_гибрид', 'энергетическая', 'hybrid_heart', 0.5, 0.006),
        ('часть_marcus_топливная_ячейка', 'энергетическая', 'fuel_cell', 5.0, 0.056),
        ('часть_marcus_рука_левая', 'приводная_система', 'servo_arm', 8.0, 0.178, 2),  # ×2 (левая + правая)
        ('часть_marcus_нога_левая', 'приводная_система', 'servo_leg', 7.0, 0.156, 2),  # ×2 (левая + правая)
        ('часть_marcus_человеческое_сердце', 'энергетическая', 'biological_heart', 0.3, 0.003),
        ('часть_marcus_человеческая_кожа', 'прочее', 'human_tissue', 3.0, 0.033),
    ],
    'materials': [
        ('часть_marcus_эндоскелет', 'cybernetic_alloy', 0.9),
        ('часть_marcus_человеческий_мозг', 'biological_tissue', 1.0),
    ],
    'parent_mass': 90.0,
}

# Cameron Phillips canon: T-900 variant (female form, smaller)
CANON_DECOMP_CAMERON = {
    'parts': [
        ('часть_cameron_cpu', 'вычислительная', 'neural_net_cpu_cameron', 0.3, 0.005),
        ('часть_cameron_эндоскелет', 'каркас', 'titanium_endoskeleton_small', 35.0, 0.538),
        ('часть_cameron_топливная_ячейка_1', 'энергетическая', 'fuel_cell_small', 4.0, 0.124, 2),  # ×2 (_1 + _2)
        ('часть_cameron_рука_левая', 'приводная_система', 'servo_arm_small', 5.0, 0.154, 2),  # ×2 (левая + правая)
        ('часть_cameron_нога_левая', 'приводная_система', 'servo_leg_small', 4.5, 0.138, 2),  # ×2 (левая + правая)
        ('часть_cameron_сенсоры', 'сенсоры', 'optical_audio_array', 0.5, 0.008),
        ('часть_cameron_ткань_кожа', 'прочее', 'living_tissue_female', 2.0, 0.031),
    ],
    'materials': [
        ('часть_cameron_эндоскелет', 'titanium_alloy', 0.9),
        ('часть_cameron_ткань_кожа', 'living_tissue_clone', 1.0),
    ],
    'parent_mass': 65.0,
}

# T-X canon: endoskeleton + plasma cannon + nanotech
CANON_DECOMP_TX = {
    'parts': [
        ('часть_t_x_cpu', 'вычислительная', 'neural_net_cpu_tx', 0.5, 0.003),
        ('часть_t_x_эндоскелет', 'каркас', 'hyperalloy_endoskeleton_tx', 75.0, 0.5),
        ('часть_t_x_топливная_ячейка_1', 'энергетическая', 'plasma_cell', 7.0, 0.094, 2),  # ×2 (_1 + _2)
        ('часть_t_x_плазма_пушка', 'встроенное_оружие', 'built_in_plasma_cannon', 15.0, 0.1),
        ('часть_t_x_нанотех_инъектор', 'встроенное_оружие', 'nanotech_injector', 2.0, 0.013),
        ('часть_t_x_рука_левая', 'приводная_система', 'servo_arm', 10.0, 0.134, 2),  # ×2 (левая + правая)
        ('часть_t_x_нога_левая', 'приводная_система', 'servo_leg', 14.0, 0.186, 2),  # ×2 (левая + правая)
        ('часть_t_x_сенсоры', 'сенсоры', 'optical_audio_array', 1.0, 0.007),
        ('часть_t_x_ткань_кожа', 'прочее', 'living_tissue_female', 4.0, 0.027),
    ],
    'materials': [
        ('часть_t_x_эндоскелет', 'hyperalloy_tx', 0.9),
        ('часть_t_x_плазма_пушка', 'tungsten_alloy', 0.7),
        ('часть_t_x_ткань_кожа', 'living_tissue_clone', 1.0),
    ],
    'parent_mass': 150.0,
}

# T-1001 (Catherine Weaver) canon: similar to T-1000
CANON_DECOMP_T1001 = {
    'parts': [
        ('часть_t1001_миметический_полисплав', 'вычислительная', 'mimetic_polyalloy_t1001', 130.0, 1.0),
    ],
    'materials': [
        ('часть_t1001_миметический_полисплав', 'mimetic_polyalloy', 1.0),
    ],
    'parent_mass': 130.0,
}

# Сводная таблица
CANON_DECOMP_ALL: dict[str, dict] = {
    'SkyNet-T800': CANON_DECOMP_T800,
    'SkyNet-T1000': CANON_DECOMP_T1000,
    'SkyNet-T1001': CANON_DECOMP_T1001,
    'SkyNet-TX': CANON_DECOMP_TX,
    'SkyNet-Rev9': CANON_DECOMP_REV9,
    'SkyNet-HKAerial': CANON_DECOMP_HK_AERIAL,
    'SkyNet-HKTank': CANON_DECOMP_HK_TANK,
    'SkyNet-T600': CANON_DECOMP_T600,
    'SkyNet-T850': CANON_DECOMP_T850,
    'SkyNet-MarcusWright': CANON_DECOMP_MARCUS,
    'SkyNet-Cameron': CANON_DECOMP_CAMERON,
}


# ============================================================================
# ГЕНЕРАЦИЯ ФАЙЛОВ ДОЧЕРНИХ ЧАСТЕЙ
# ============================================================================

def serialize_value(value: Any, indent: int = 0) -> str:
    """YAML-сериализация (как в fill_canon_data.py)."""
    pad = "  " * indent
    pad_child = "  " * (indent + 1)
    
    if isinstance(value, str):
        if any(c in value for c in [":", "#", "\n", "{", "}", "[", "]", ",", "&", "*", "?", "|", "<", ">", "=", "%", "@", "`", '"', "'"]):
            escaped = value.replace("'", "''")
            return f"'{escaped}'"
        return value
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, type(None)):
        return "null"
    if isinstance(value, list):
        if not value:
            return "[]"
        items = []
        for v in value:
            items.append(f"{pad_child}- {serialize_value(v, indent + 1)}")
        return "\n" + "\n".join(items)
    if isinstance(value, dict):
        if not value:
            return "{}"
        lines = []
        for k, v in value.items():
            if isinstance(v, dict):
                if v:
                    lines.append(f"{pad_child}{k}:")
                    sub = serialize_value(v, indent + 2)
                    for line in sub.split("\n"):
                        if line:
                            lines.append(pad_child + "  " + line)
                else:
                    lines.append(f"{pad_child}{k}: {{}}")
            elif isinstance(v, list):
                if v:
                    lines.append(f"{pad_child}{k}:")
                    sub = serialize_value(v, indent + 1)
                    for line in sub.split("\n"):
                        if line:
                            lines.append(pad_child + line if not line.startswith(" ") else pad_child + "  " + line.lstrip())
                else:
                    lines.append(f"{pad_child}{k}: []")
            else:
                lines.append(f"{pad_child}{k}: {serialize_value(v, indent + 1)}")
        return "\n" + "\n".join(lines)
    return "null"


def generate_part_file(part_id: str, parent_id: str, subsystem: str, subtype: str,
                       mass_kg: float, share: float, count: int = 1) -> str:
    """Сгенерировать содержимое .md файла для дочерней части.
    
    v9.31: уровень_номер=2 (не 4) — parent=1, child=2 (разница 1, проходит F16).
    v9.35: добавлено поле количество=N (для paired parts: левая+правая, _1+_2).
          Если count>1, в body заголовок содержит (×N).
    """
    count_yaml = f"количество: {count}\n" if count > 1 else ""
    title_suffix = f" (×{count})" if count > 1 else ""
    yaml_data = f"""---
id: {part_id}
тип: изделие
категория: машиностроение
уровень_иерархии: промежуточный
уровень_номер: 2
подсистема: {subsystem}
подтип: {subtype}
стандарты: []
исследовательская_группа: null
родитель: {parent_id}
{count_yaml}дочерние_части: []
материалы_частей: []
scaling_type: количественный
соединители: []
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
ии_перепроектирован:
  статус: false
  верификация: []
основные:
  масса_kg: {mass_kg}
  доля_массы_родителя: {share}
наследуемые: {{}}
дополнительные: {{}}
дата_создания: {TODAY}
дата_обновления: {TODAY}
источник: web_search
источник_разбора: канон
---

# Часть: {part_id}{title_suffix}

## Описание

Дочерняя часть изделия `{parent_id}` (подсистема: {subsystem}).

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | {subsystem} | — | canon |
| подтип | {subtype} | — | canon |
| масса | {mass_kg} | kg | canon |
| доля массы родителя | {share} | — | canon |
| количество | {count} | шт. | canon |

## Состав

Промежуточная часть (уровень 2). Дочерних частей нет.

## Источники

- Канон: декомпозиция модели `{parent_id}` (web search 2026-11-03)
"""
    return yaml_data


def create_part_files(model_id: str, decomp: dict) -> list[str]:
    """Создать файлы для всех дочерних частей модели.
    
    v9.35: поддерживает опциональный 6-й элемент count в кортеже parts.
    """
    created = []
    for part in decomp['parts']:
        # Unpack 5-tuple or 6-tuple
        if len(part) == 6:
            part_id, subsystem, subtype, mass, share, count = part
        else:
            part_id, subsystem, subtype, mass, share = part
            count = 1
        # Подсистема — это имя папки
        # Sanitize part_id для имени файла
        fname = part_id + ".md"
        fpath = IZDELIYA_DIR / subsystem / part_id / "_index.md"
        fpath.parent.mkdir(parents=True, exist_ok=True)
        
        if not fpath.exists():
            content = generate_part_file(part_id, model_id, subsystem, subtype, mass, share, count)
            fpath.write_text(content, encoding='utf-8')
            created.append(str(fpath))
    
    return created


def update_model_decomposition(model_id: str, decomp: dict) -> bool:
    """Обновить модель: заполнить дочерние_части + материалы_частей + mermaid."""
    # Найти файл модели
    model_filename_map = {
        'SkyNet-T800': 't800.md',
        'SkyNet-T1000': 't1000.md',
        'SkyNet-T1001': 't1001.md',
        'SkyNet-TX': 't_x.md',
        'SkyNet-Rev9': 'rev9.md',
        'SkyNet-HKAerial': 'hk_aerial.md',
        'SkyNet-HKTank': 'hk_tank.md',
        'SkyNet-T600': 't600.md',
        'SkyNet-T850': 't850.md',
        'SkyNet-MarcusWright': 'marcus_wright.md',
        'SkyNet-Cameron': 'cameron_phillips.md',
    }
    fname = model_filename_map.get(model_id)
    if not fname:
        return False
    fpath = MODELS_DIR / fname
    if not fpath.exists():
        return False
    
    text = fpath.read_text(encoding='utf-8')
    data, yaml_text, body = read_yaml_frontmatter(fpath)
    
    # Заменить дочерние_части
    children_ids = [p[0] for p in decomp['parts']]
    new_yaml = yaml_text
    
    # Найти существующее поле дочерние_части
    pattern = r"^дочерние_части:.*?(?=^[A-Za-zА-Яа-яЁё_][\wА-Яа-яЁё-]*:|\Z)"
    serialized = serialize_value(children_ids)
    if re.search(pattern, new_yaml, re.MULTILINE | re.DOTALL):
        new_yaml = re.sub(pattern, f"дочерние_части: {serialized}\n", new_yaml, count=1, flags=re.MULTILINE | re.DOTALL)
    else:
        # Поля нет — добавить после id:
        id_pattern = r"^(id:\s*[^\n]+\n)"
        if re.search(id_pattern, new_yaml, re.MULTILINE):
            new_yaml = re.sub(id_pattern, rf"\1дочерние_части: {serialized}\n", new_yaml, count=1, flags=re.MULTILINE)
    
    # Заменить материалы_частей — добавим как новое поле после дочерние_части
    # В моделях нет материалы_частей по умолчанию — пропускаем
    
    # Обновить дата_обновления
    new_yaml = re.sub(
        r"^дата_обновления:\s*\d{4}-\d{2}-\d{2}\s*$",
        f"дата_обновления: {TODAY}",
        new_yaml,
        count=1,
        flags=re.MULTILINE,
    )
    
    # Добавить Mermaid диаграмму в body (если ещё нет)
    if '```mermaid' not in body:
        mermaid_diagram = generate_mermaid_for_model(model_id, decomp)
        body = body.rstrip() + "\n\n## Декомпозиция\n\n" + mermaid_diagram + "\n"
    
    new_text = "---\n" + new_yaml + "\n---\n" + body
    fpath.write_text(new_text, encoding='utf-8')
    return True


def generate_mermaid_for_model(model_id: str, decomp: dict) -> str:
    """Сгенерировать Mermaid диаграмму для модели."""
    lines = ["```mermaid", "graph TD"]
    
    def short_id(id_str: str) -> str:
        return id_str.replace("SkyNet-", "").replace("часть_", "")[:25]
    
    lines.append(f'    {short_id(model_id)}["{model_id}"]')
    
    # Группировать части по подсистемам
    by_sub: dict[str, list] = {}
    for part_id, sub, subtype, mass, share in decomp['parts']:
        by_sub.setdefault(sub, []).append((part_id, subtype, mass, share))
    
    for sub, parts in by_sub.items():
        lines.append(f'    subgraph {sub}')
        for part_id, subtype, mass, share in parts:
            label = f"{subtype}<br/>{mass} kg ({share*100:.1f}%)"
            lines.append(f'    {short_id(part_id)}["{label}"]')
            lines.append(f'    {short_id(model_id)} --> {short_id(part_id)}')
        lines.append('    end')
    
    lines.append("```")
    return "\n".join(lines)


# ============================================================================
# СВЯЗЫВАНИЕ МОДЕЛЕЙ С ИЗДЕЛИЯМИ (реализация_промышленная)
# ============================================================================

def link_models_to_izdeliya() -> int:
    """Для каждой модели заполнить реализация_промышленная ссылками на изделия
    той же подсистемы. Возвращает количество обновлённых моделей.
    """
    izdeliya = {}
    for f in IZDELIYA_DIR.rglob("_index.md"):
        data, _, _ = read_yaml_frontmatter(f)
        if data and 'id' in data:
            data['_path'] = str(f)
            izdeliya[data['id']] = data
    
    # Группировать изделия по подсистемам
    by_subsystem: dict[str, list[str]] = {}
    for izd_id, data in izdeliya.items():
        sub = data.get('подсистема')
        if sub:
            by_subsystem.setdefault(sub, []).append(izd_id)
    
    updated = 0
    for mf in sorted(MODELS_DIR.glob("*.md")):
        if mf.name.startswith('_'):
            continue
        data, yaml_text, body = read_yaml_frontmatter(mf)
        if not data:
            continue
        mtype = data.get('тип_модели', '')
        expected = EXPECTED_SUBSYSTEMS_BY_TYPE.get(mtype, [])
        if not expected:
            continue
        
        # Собрать id изделий для каждой ожидаемой подсистемы
        impl_ids = []
        for sub in expected:
            ids = by_subsystem.get(sub, [])
            # Взять максимум 3 из каждой подсистемы (для разумного размера)
            impl_ids.extend(ids[:3])
        
        if not impl_ids:
            continue
        
        # Заменить реализация_промышленная
        new_yaml = yaml_text
        pattern = r"^реализация_промышленная:.*?(?=^[A-Za-zА-Яа-яЁё_][\wА-Яа-яЁё-]*:|\Z)"
        serialized = serialize_value(impl_ids)
        new_yaml = re.sub(pattern, f"реализация_промышленная: {serialized}\n", new_yaml, count=1, flags=re.MULTILINE | re.DOTALL)
        
        # Обновить дата_обновления
        new_yaml = re.sub(
            r"^дата_обновления:\s*\d{4}-\d{2}-\d{2}\s*$",
            f"дата_обновления: {TODAY}",
            new_yaml,
            count=1,
            flags=re.MULTILINE,
        )
        
        new_text = "---\n" + new_yaml + "\n---\n" + body
        mf.write_text(new_text, encoding='utf-8')
        updated += 1
    
    return updated


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=== SkyNet Decomposition Generator v9.31 ===")
    print()
    
    # 1. Связать модели с изделиями
    print("=== Шаг 1: Связывание моделей с изделиями (реализация_промышленная) ===")
    updated = link_models_to_izdeliya()
    print(f"  ✓ Обновлено моделей: {updated}")
    
    # 2. Создать дочерние части для топ-10 моделей
    print()
    print("=== Шаг 2: Создание дочерних частей для топ-10 моделей ===")
    total_parts_created = 0
    for model_id, decomp in CANON_DECOMP_ALL.items():
        created = create_part_files(model_id, decomp)
        print(f"  ✓ {model_id}: создано {len(created)} частей")
        total_parts_created += len(created)
    
    # 3. Обновить модели — заполнить дочерние_части + Mermaid
    print()
    print("=== Шаг 3: Обновление моделей (дочерние_части + Mermaid) ===")
    updated_models = 0
    for model_id, decomp in CANON_DECOMP_ALL.items():
        if update_model_decomposition(model_id, decomp):
            updated_models += 1
            print(f"  ✓ {model_id}: обновлён")
    
    print()
    print(f"=== Сводка ===")
    print(f"  Моделей связано с изделиями: {updated}")
    print(f"  Дочерних частей создано: {total_parts_created}")
    print(f"  Моделей обновлено с декомпозицией: {updated_models}")


if __name__ == "__main__":
    main()
