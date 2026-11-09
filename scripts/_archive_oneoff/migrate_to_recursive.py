#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ФАЗА 1.2: Классификация всех 719 _index.md под изделия/ для миграции в A2-модель.

Рекурсивно обходит реальные данные/изделия/ и работа и и/изделия/, для каждого узла определяет
целевой тип в новой модели A2:

  - 'изделие'   : top-level (уровень_номер: 1, нет родителя)
  - 'сборка'    : промежуточный (имеет дочерние_части, не top-level)
  - 'часть'     : атомарная деталь, материал canonical (неделимый, has материалы_частей)
  - 'компонент' : закупочный узел, материал НЕ canonical (например, stainless_steel_mesh)

Алгоритм классификации:
  1. Если уровень_номер == 1 (или нет 'родитель') → 'изделие'
  2. Если есть дочерние_части (непустой) → 'сборка'
  3. Если в материалы_частей указан canonical материал → 'часть'
  4. Если в материалы_частей указан НЕ canonical материал → 'компонент'
     (это кандидат в закупочные узлы; см. decomp_registry.yaml)
  5. Если нет ни детей, ни материалы_частей → 'часть' с WARNING (нужно заполнить BOM)

Запуск:
  python3 scripts/_archive_oneoff/migrate_to_recursive.py            # dry-run, отчёт
  python3 scripts/_archive_oneoff/migrate_to_recursive.py --apply    # применить (после dry-run)

Файл отчёта: результаты/migration_log_<дата>.md
"""
import sys
import os
import re
import yaml
import argparse
from pathlib import Path
from datetime import date

sys.path.insert(0, '/home/z/my-project/SkyNet/scripts')

REPO = Path('/home/z/my-project/SkyNet')
IZDELIYA_REAL = REPO / 'реальные данные' / 'изделия'
IZDELIYA_II = REPO / 'работа и и' / 'изделия'
MATERIALS_DIR = REPO / 'реальные данные' / 'материалы'

# Кэш canonical материалов (заполняется один раз)
_canonical_materials_cache = None


def load_canonical_materials() -> set:
    global _canonical_materials_cache
    if _canonical_materials_cache is None:
        _canonical_materials_cache = {f.stem for f in MATERIALS_DIR.glob('*.md')}
    return _canonical_materials_cache


def read_yaml_frontmatter(path: Path) -> tuple:
    """Прочитать YAML frontmatter (между --- ... ---). Вернуть (data, yaml_text, body)."""
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---'):
        return {}, '', text
    end = text.find('\n---', 3)
    if end == -1:
        return {}, '', text
    yaml_text = text[3:end]
    body = text[end + 4:]
    try:
        data = yaml.safe_load(yaml_text)
    except yaml.YAMLError:
        return {}, yaml_text, body
    return data or {}, yaml_text, body


def classify_node(data: dict, canonical_materials: set) -> tuple:
    """Вернуть (тип, reason). Тип ∈ {'изделие','сборка','часть','компонент','unknown'}."""
    parent = data.get('родитель')
    level_num = data.get('уровень_номер')
    children = data.get('дочерние_части', [])
    if not isinstance(children, list):
        children = []
    materials_parts = data.get('материалы_частей', [])
    if not isinstance(materials_parts, list):
        materials_parts = []

    # 1. top-level
    if level_num == 1 or not parent or parent == 'null':
        return 'изделие', f'level={level_num}, parent={parent!r}'

    # 2. has children → сборка
    if children:
        return 'сборка', f'has {len(children)} children'

    # 3-4. leaf → 'часть' или 'компонент' по материалу
    if not materials_parts:
        return 'часть', 'leaf without материалы_частей (WARN: нужно заполнить BOM)'

    # Найти первый материал в материалы_частей
    first_material_id = None
    for entry in materials_parts:
        if isinstance(entry, dict):
            mat = entry.get('материал')
            if mat:
                first_material_id = mat
                break

    if first_material_id is None:
        return 'часть', 'leaf with пустой материалы_частей'

    if first_material_id in canonical_materials:
        return 'часть', f'canonical material: {first_material_id}'
    else:
        return 'компонент', f'non-canonical material: {first_material_id}'


def walk_izdeliya(root_dir: Path) -> list:
    """Найти все _index.md под root_dir, вернуть список Path."""
    result = []
    for path in root_dir.rglob('_index.md'):
        result.append(path)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true',
                        help='Применить миграцию (по умолчанию dry-run)')
    args = parser.parse_args()

    print("=== Фаза 1.2: Классификация узлов для A2-модели ===\n")

    canonical = load_canonical_materials()
    print(f"Canonical материалов: {len(canonical)}")

    # Собрать все _index.md
    all_files = []
    if IZDELIYA_REAL.exists():
        all_files += walk_izdeliya(IZDELIYA_REAL)
    if IZDELIYA_II.exists():
        all_files += walk_izdeliya(IZDELIYA_II)
    print(f"Всего _index.md в изделиях: {len(all_files)}")

    # Классифицировать
    classifications = []
    stats = {'изделие': 0, 'сборка': 0, 'часть': 0, 'компонент': 0, 'unknown': 0}
    for path in all_files:
        data, _, _ = read_yaml_frontmatter(path)
        if not data:
            classifications.append((path, 'unknown', 'no frontmatter'))
            stats['unknown'] += 1
            continue
        tip, reason = classify_node(data, canonical)
        classifications.append((path, tip, reason))
        stats[tip] += 1

    print(f"\nКлассификация:")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print(f"  TOTAL: {sum(stats.values())}")

    # Список компонентов (для ручной верификации)
    components = [(p, r) for p, t, r in classifications if t == 'компонент']
    print(f"\nЗакупочные компоненты (нужно проверить вручную): {len(components)}")
    for path, reason in components[:20]:
        rel = path.relative_to(REPO)
        print(f"  {rel}  ({reason})")
    if len(components) > 20:
        print(f"  ... и ещё {len(components) - 20}")

    if not args.apply:
        print("\n[DRY-RUN] Изменения не применены. Используйте --apply для миграции.")
        return

    # Применить миграцию: для каждого файла обновить поле 'тип' на новое значение
    print("\n=== Применение миграции ===")
    migrated = 0
    for path, tip, _ in classifications:
        if tip == 'unknown':
            continue
        text = path.read_text(encoding='utf-8')
        old_type_match = re.search(r'^тип:\s*(\S+)', text, re.MULTILINE)
        if not old_type_match:
            print(f"  SKIP {path.relative_to(REPO)}: поле 'тип' не найдено")
            continue
        old_type = old_type_match.group(1)
        if old_type == tip:
            continue  # уже корректно
        new_text = re.sub(r'^тип:\s*\S+', f'тип: {tip}', text, count=1, flags=re.MULTILINE)
        path.write_text(new_text, encoding='utf-8')
        migrated += 1
    print(f"Мигрировано файлов: {migrated}")


if __name__ == '__main__':
    main()
