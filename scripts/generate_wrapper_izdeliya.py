#!/usr/bin/env python3
"""SkyNet — Создаёт wrapper-изделия для моделей с декомпозицией.

Для каждой модели в фантастические данные/модели/<model>.md, у которой есть
дочерние_части (декомпозиция), создать wrapper-изделие в
реальные данные/изделия/<подсистема>/<model_id>/_index.md.

Это нужно, чтобы:
  • Части (часть_t800_cpu) ссылались на родитель = id wrapper-изделия
    (izdelie_SkyNet-T800), а не на id модели (SkyNet-T800)
  • F12a работала (родитель существует в графе изделий)
  • F14, F15a-h, F16, F19 тоже работали (т.к. они проверяют изделия)
"""

from __future__ import annotations
import os
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from validate_decomposition import read_yaml_frontmatter, SKYNET_REPO
from _helpers import write_atomic  # v9.37: atomic writes (T1)

TODAY = "2026-11-03"
IZDELIYA_DIR = SKYNET_REPO / "реальные данные" / "изделия"
MODELS_DIR = SKYNET_REPO / "фантастические данные" / "модели"


# Подсистема по умолчанию для wrapper-изделия модели
MODEL_DEFAULT_SUBSYSTEM = "прочее"


def get_model_subsystem(model_id: str) -> str:
    """Определить подсистему для wrapper-изделия на основе типа модели."""
    # По типу модели — выбираем основную подсистему
    subsystem_map = {
        'гуманоидный': 'каркас',  # основной элемент — endoskeleton
        'жидкий_металл': 'вычислительная',
        'воздушный': 'каркас',
        'наземный_гусеничный': 'каркас',
        'наземный_колёсный': 'каркас',
        'водный_надводный': 'каркас',
        'водный_подводный': 'каркас',
        'стационарный': 'вычислительная',
    }
    return subsystem_map.get(model_id, MODEL_DEFAULT_SUBSYSTEM)


def generate_wrapper_izdelie(model_id: str, model_data: dict, children_ids: list,
                              materials: list = None, parts: list = None) -> tuple[str, str, str]:
    """Сгенерировать .md файл для wrapper-изделия модели.
    
    Добавляет:
      • дочерние_части (children_ids)
      • материалы_частей с долями (для F14 — Σ=1.0)
      • Mermaid диаграмму в body (для F19)
    """
    mtype = model_data.get('тип_модели', '')
    subsystem = get_model_subsystem(mtype)
    canon = model_data.get('канон_источник', '')
    mass_kg = model_data.get('основные', {}).get('масса_kg') if isinstance(model_data.get('основные'), dict) else None
    
    folder_name = model_id.replace('SkyNet-', '').lower()
    
    # Сериализовать материалы_частей
    # v9.31: доля_массы — это доля массы МАТЕРИАЛА в РОДИТЕЛЕ (всей модели).
    # Формула: доля_массы_материала = доля_массы_части × доля_материала_в_части
    # Если parts доступны, можно посчитать правильно.
    # Иначе доля_массы из materials трактуется как доля_массы_части (упрощение).
    parts_map = {}
    if parts:
        for p in parts:
            if isinstance(p, (tuple, list)) and len(p) >= 5:
                parts_map[p[0]] = p[4]  # часть → share
    
    if materials:
        materials_yaml = "\n"
        for m in materials:
            # m — tuple (часть, материал, доля_материала_в_части)
            if isinstance(m, (tuple, list)):
                part_id, material_id, share_in_part = m[0], m[1], m[2]
            elif isinstance(m, dict):
                part_id = m.get('часть')
                material_id = m.get('материал')
                share_in_part = m.get('доля_массы')
            else:
                continue
            # Посчитать долю_массы_материала_в_родителе
            share_in_parent = parts_map.get(part_id, share_in_part) * share_in_part
            materials_yaml += f"  - часть: {part_id}\n    материал: {material_id}\n    доля_массы: {round(share_in_parent, 4)}\n"
    else:
        materials_yaml = "[]"
    
    # Сериализовать дочерние_части
    if children_ids:
        children_yaml = "\n" + "\n".join(f"  - {cid}" for cid in children_ids)
    else:
        children_yaml = "[]"
    
    content = f"""---
id: izdelie_{model_id}
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: {subsystem}
подтип: модель_обёртка
стандарты: []
исследовательская_группа: skynet
родитель: null
дочерние_части:{children_yaml}
материалы_частей:{materials_yaml}
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
  масса_kg: {mass_kg if mass_kg else 'null'}
наследуемые: {{}}
дополнительные:
  соответствующая_модель: {model_id}
  канон_источник: '{canon}'
дата_создания: {TODAY}
дата_обновления: {TODAY}
источник: web_search
источник_разбора: канон
---

# Изделие-обёртка: {model_id}

## Описание

Wrapper-изделие для модели `{model_id}` (тип: {mtype}, подсистема: {subsystem}).

Создано для поддержки декомпозиции: дочерние части (часть_*) ссылаются на
этот id как на родителя. Сама модель остаётся в фантастические данные/модели/.

## Декомпозиция

```mermaid
graph TD
    {model_id.replace('SkyNet-', '')}["{model_id}"]
"""
    # Добавить дочерние в Mermaid
    for cid in children_ids:
        short = cid.replace('часть_', '')[:25]
        content += f'    {short}["{cid}"]\n'
        content += f'    {model_id.replace("SkyNet-", "")} --> {short}\n'
    
    content += """```

## Состав

Дочерние части:
"""
    for cid in children_ids:
        content += f"- `{cid}`\n"
    
    content += f"""
## Связанная модель

- [`{model_id}`](../../../фантастические%20данные/модели/) — модель SkyNet

## Источники

- Wrapper-изделие создано автоматически ({TODAY}) для поддержки декомпозиции
"""
    return content, folder_name, subsystem


def main():
    print("=== SkyNet Wrapper-Izdelie Generator ===")
    print()
    
    # Импортировать CANON_DECOMP_ALL из generate_decomposition
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        from generate_decomposition import CANON_DECOMP_ALL
    except ImportError:
        CANON_DECOMP_ALL = {}
    
    created = 0
    updated = 0
    
    for mf in sorted(MODELS_DIR.glob("*.md")):
        if mf.name.startswith('_'):
            continue
        data, _, _ = read_yaml_frontmatter(mf)
        if not data or 'id' not in data:
            continue
        model_id = data['id']
        children = data.get('дочерние_части', [])
        if not isinstance(children, list) or not children:
            continue
        
        # Найти материалы и parts из CANON_DECOMP_ALL
        materials = None
        parts = None
        if model_id in CANON_DECOMP_ALL:
            materials = CANON_DECOMP_ALL[model_id].get('materials')
            parts = CANON_DECOMP_ALL[model_id].get('parts')
        
        # Создать wrapper-изделие
        content, folder_name, subsystem = generate_wrapper_izdelie(model_id, data, children, materials, parts)
        fpath = IZDELIYA_DIR / subsystem / folder_name / "_index.md"
        
        if fpath.exists():
            # Обновить
            write_atomic(fpath, content)  # v9.37: atomic write
            updated += 1
        else:
            fpath.parent.mkdir(parents=True, exist_ok=True)
            write_atomic(fpath, content)  # v9.37: atomic write
            created += 1
        
        print(f"  ✓ {model_id} → реальные данные/изделия/{subsystem}/{folder_name}/_index.md")
    
    print()
    print(f"=== Сводка ===")
    print(f"  Создано wrapper-изделий: {created}")
    print(f"  Обновлено wrapper-изделий: {updated}")


if __name__ == "__main__":
    main()
