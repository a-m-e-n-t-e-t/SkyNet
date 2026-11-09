#!/usr/bin/env python3
"""SkyNet Recursive Decomposition Engine — v9.60.1 (production-ready)

Рекурсивный генератор декомпозиции на основе _decomp_registry.yaml.
Замещает decompose_all_izdeliya.py (который помечен как deprecated).

Главные отличия от decompose_all_izdeliya.py:
1. Рекурсивная декомпозиция — произвольная глубина (1..10 уровней)
2. Читает _decomp_registry.yaml (единственный источник правды)
3. Автоматическая остановка:
   - STOP_MATERIAL — подтип является canonical материалом (файл в материалы/)
   - STOP_ATOMIC — подтип в реестре с is_atomic=true
   - STOP_UNKNOWN — подтипа нет в реестре (F34 violation)
   - RECURSE — для каждого child рекурсивно
4. Поддержка A2-модели: новые типы сборка/часть/компонент
5. TransactionBatch для атомарной записи parent + all children
6. md_internal_link для динамических markdown-ссылок
7. v9.60.1: PRODUCTION — реальная запись файлов, BOM fill, обновление родителя
8. v9.60.1: --issue <N> флаг для интеграции с cron_run.sh

Использование:
    # Dry-run: показать дерево декомпозиции без записи файлов
    python3 scripts/recursive_decompose.py --dry-run --izdelie izdelie_apa

    # Применить декомпозицию к одному изделию (production)
    python3 scripts/recursive_decompose.py --izdelie izdelie_apa

    # Применить ко всем top-level изделиям (полная регенерация)
    python3 scripts/recursive_decompose.py --all

    # Интеграция с cron-агентом: F34-issue #146 для часть_X
    python3 scripts/recursive_decompose.py --izdelie izdelie_X --issue 146

Алгоритм:
1. Загрузить _decomp_registry.yaml + canonical материалы
2. Найти top-level изделие по --izdelie или все (--all)
3. decompose_node(subtype, parent_id, ...):
   - STOP_MATERIAL: skip (это canonical материал, не узел)
   - STOP_ATOMIC: записать leaf-файл с BOM из реестра
   - STOP_UNKNOWN: violation (F34 — нужна ручная декомпозиция)
   - RECURSE: для каждого child:
     a. Вычислить child_id, child_path
     b. Рекурсивно: decompose_node(child_subtype, child_id, ...)
     c. Собрать материалы от детей для обновления родителя
4. После рекурсии: обновить родительский файл (дочерние_части + материалы_частей)
5. TransactionBatch commit (атомарно все файлы)
"""
from __future__ import annotations

import os
import sys
import re
import argparse
import yaml
from pathlib import Path
from typing import Any
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from validate_decomposition import read_yaml_frontmatter, SKYNET_REPO
from _helpers import write_atomic, TransactionBatch, md_internal_link

REGISTRY_PATH = SKYNET_REPO / 'scripts' / '_decomp_registry.yaml'
MATERIALS_DIR = SKYNET_REPO / 'реальные данные' / 'материалы'
IZDELIYA_DIR = SKYNET_REPO / 'реальные данные' / 'изделия'

# Кэш
_REGISTRY_CACHE: dict | None = None
_CANONICAL_MATERIALS_CACHE: set | None = None
MAX_DEPTH = 10  # sanity check против бесконечной рекурсии

TODAY = date.today().isoformat()


def load_decomp_registry() -> dict:
    """Загрузить _decomp_registry.yaml (с кэшем)."""
    global _REGISTRY_CACHE
    if _REGISTRY_CACHE is None:
        data = yaml.safe_load(REGISTRY_PATH.read_text(encoding='utf-8'))
        _REGISTRY_CACHE = data['decomp_registry'] if data else {}
    return _REGISTRY_CACHE


def load_canonical_materials() -> set:
    """Кэш canonical материалов из реальные данные/материалы/*.md."""
    global _CANONICAL_MATERIALS_CACHE
    if _CANONICAL_MATERIALS_CACHE is None:
        _CANONICAL_MATERIALS_CACHE = {f.stem for f in MATERIALS_DIR.glob('*.md')}
    return _CANONICAL_MATERIALS_CACHE


def classify_subtype(subtype: str, registry: dict, canonical: set) -> tuple:
    """Вернуть (action, info) для подтипа.

    action ∈ {'STOP_MATERIAL', 'STOP_ATOMIC', 'STOP_UNKNOWN', 'RECURSE'}
    """
    if subtype in canonical:
        return 'STOP_MATERIAL', None
    if subtype not in registry:
        return 'STOP_UNKNOWN', None
    entry = registry[subtype]
    if entry.get('is_atomic'):
        return 'STOP_ATOMIC', entry
    return 'RECURSE', entry


def build_part_id(parent_id: str, suffix: str) -> str:
    """Сгенерировать id дочерней части: 'часть_' + parent_short + '_' + suffix."""
    short = parent_id
    if short.startswith('izdelie_'):
        short = short[len('izdelie_'):]
    # Если parent уже часть_, не добавляем 'часть_' повторно
    if not short.startswith('часть_'):
        return f"часть_{short}_{suffix}"
    return f"{short}_{suffix}"


def serialize_materials_bom(part_id: str, materials_bom: list) -> str:
    """Сериализовать BOM материалы_частей в YAML-строку.

    materials_bom: list of (материал, форма, доля) tuples.
    """
    if not materials_bom:
        return ' []\n'
    lines = ['\n']
    for mat_id, forma, dolja in materials_bom:
        line = f'  - часть: {part_id}\n    материал: {mat_id}\n'
        if forma:
            line += f'    форма: {forma}\n'
        line += f'    доля_массы: {dolja}\n'
        lines.append(line)
    return ''.join(lines)


def serialize_children_yaml(children_ids: list) -> str:
    """Сериализовать дочерние_части в YAML-строку."""
    if not children_ids:
        return ' []\n'
    return '\n' + '\n'.join(f'  - {cid}' for cid in children_ids) + '\n'


def generate_part_content(*, part_id: str, parent_id: str, subsystem: str,
                          subtype: str, mass_kg: float, share: float,
                          file_path: Path, tip: str = 'часть',
                          materials_bom: list | None = None,
                          children_ids: list | None = None,
                          level_number: int = 2) -> str:
    """Сгенерировать содержимое часть_*.md файла (frontmatter + body).

    v9.61: упрощено — поле 'компоненты_частей' упразднено (вариант C).
    Закупочные sub-assemblies теперь тип: изделие с is_purchased: true.
    """
    materials_bom = materials_bom or []
    children_ids = children_ids or []

    children_yaml = serialize_children_yaml(children_ids)
    materials_yaml = serialize_materials_bom(part_id, materials_bom)

    # Markdown-ссылка на canonical материал (если BOM есть)
    material_link_lines = []
    for mat_id, forma, _ in materials_bom:
        try:
            link = md_internal_link(file_path, 'материалы', f'{mat_id}.md', mat_id)
            if forma:
                material_link_lines.append(f'- `{mat_id}` (форма: {forma}) → {link}')
            else:
                material_link_lines.append(f'- `{mat_id}` → {link}')
        except ValueError:
            material_link_lines.append(f'- `{mat_id}` → (canonical material link)')
    material_links_block = '\n'.join(material_link_lines) if material_link_lines else '(BOM не определён)'

    # уровень_иерархии по tip (3 типа: изделие/сборка/часть)
    hier = {'изделие': 'верхний', 'сборка': 'промежуточный', 'часть': 'неделимый'}.get(tip, 'неделимый')

    return f"""---
id: {part_id}
тип: {tip}
категория: машиностроение
уровень_иерархии: {hier}
уровень_номер: {level_number}
подсистема: {subsystem}
подтип: {subtype}
стандарты: []
исследовательская_группа: null
родитель: {parent_id}
дочерние_части:{children_yaml}материалы_частей:{materials_yaml}scaling_type: количественный
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
  габариты_mm:
    l: 100
    w: 100
    h: 50
  выработка_энергии_W: 0
  выработка_тепла_W: 0
наследуемые: {{}}
дополнительные: {{}}
дата_создания: {TODAY}
дата_обновления: {TODAY}
источник: web_search
источник_разбора: канон
---

# Часть: {part_id}

## Описание

Дочерняя часть `{parent_id}` (подсистема: {subsystem}, подтип: {subtype}).
Сгенерировано `recursive_decompose.py v9.61` на основе `_decomp_registry.yaml`.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | {subsystem} | — | canon |
| подтип | {subtype} | — | canon |
| масса | {mass_kg} | kg | canon |
| доля массы родителя | {share} | — | canon |
| тип узла | {tip} | — | canon |
| уровень_номер | {level_number} | — | canon |

## Принцип работы

Определяется типом и назначением родительского изделия.

## Состав

{'Промежуточная часть (сборка, уровень ' + str(level_number) + '). Структурная декомпозиция продолжается.' if tip == 'сборка' else 'Атомарная часть (leaf, уровень ' + str(level_number) + '). Дочерних частей нет.'}

## Используемые материалы

{material_links_block}

## Источники

- Канон: декомпозиция `{parent_id}` (recursive_decompose.py v9.61, {TODAY})
- Реестр: `scripts/_decomp_registry.yaml`
"""


def update_parent_file(parent_path: Path, children_ids: list,
                       materials_per_child: dict, batch: TransactionBatch,
                       dry_run: bool = False) -> bool:
    """Обновить родительский файл: заполнить дочерние_части и материалы_частей.

    materials_per_child: dict {child_id: [(материал, форма, доля), ...]}

    Возвращает True если файл обновлён, False если не нужен апдейт.
    """
    text = parent_path.read_text(encoding='utf-8')
    data, _, _ = read_yaml_frontmatter(parent_path)
    if not data:
        return False

    # Сериализовать дочерние_части
    children_yaml = serialize_children_yaml(children_ids)

    # Сериализовать материалы_частей (агрегация от всех детей)
    # Каждая запись: часть: <child_id>, материал: <id>, форма: <forma>, доля_массы: <dolja>
    if materials_per_child:
        mat_lines = ['\n']
        for child_id, bom in materials_per_child.items():
            for mat_id, forma, dolja in bom:
                line = f'  - часть: {child_id}\n    материал: {mat_id}\n'
                if forma:
                    line += f'    форма: {forma}\n'
                line += f'    доля_массы: {dolja}\n'
                mat_lines.append(line)
        materials_yaml = ''.join(mat_lines)
    else:
        materials_yaml = ' []\n'

    # Заменить дочерние_части: ... (после родитель: ... строки до следующего top-level поля)
    # Используем regex: ^дочерние_части:\s*(\[\]|.*?)(?=^[A-Za-zА-Яа-яЁё_])
    new_text = re.sub(
        r'(^дочерние_части:).*?(?=^[A-Za-zА-Яа-яЁё_][\wА-Яа-яЁё+-]*:)',
        lambda m: f'дочерние_части:{children_yaml}',
        text,
        count=1,
        flags=re.MULTILINE | re.DOTALL,
    )

    # Заменить материалы_частей: ...
    new_text = re.sub(
        r'(^материалы_частей:).*?(?=^scaling_type:)',
        lambda m: f'материалы_частей:{materials_yaml}',
        new_text,
        count=1,
        flags=re.MULTILINE | re.DOTALL,
    )

    # Обновить дата_обновления
    new_text = re.sub(
        r'(^дата_обновления:)\s*\S+',
        lambda m: f'дата_обновления: {TODAY}',
        new_text,
        count=1,
        flags=re.MULTILINE,
    )

    if new_text != text:
        if not dry_run:
            batch.write(parent_path, new_text)
        return True
    return False


def decompose_node(subtype: str, parent_id: str, subsystem: str,
                   parent_path: Path, depth: int,
                   registry: dict, canonical: set,
                   batch: TransactionBatch, dry_run: bool = False,
                   _max_depth: int = MAX_DEPTH,
                   mass_kg: float = 0.1, share: float = 0.1) -> dict:
    """Рекурсивно декомпозировать узел и записать файлы.

    Возвращает dict:
      {action, parts_created, depth_reached, child_ids, materials_bom,
       file_path, tip, violation?}

    v9.60.1: production-ready — реальная запись через TransactionBatch.
    """
    if depth > _max_depth:
        return {'action': 'STOP_DEPTH_LIMIT', 'parts_created': 0, 'depth_reached': depth}

    action, info = classify_subtype(subtype, registry, canonical)

    if action == 'STOP_MATERIAL':
        # Подтип сам является canonical материалом — дальше не идём
        return {'action': 'STOP_MATERIAL', 'parts_created': 0, 'depth_reached': depth}

    if action == 'STOP_UNKNOWN':
        # Подтипа нет в реестре — F34 violation
        # Для depth=1 (top-level изделие): НЕ перезаписываем существующий _index.md
        # (это уже полноценное изделие, а не stub). Только сообщаем о violation.
        # Для depth>=2: создаём stub-файл часть_X.md (его не существует).
        tip = 'часть'
        materials_bom = []
        if not dry_run and parent_path:
            if depth == 1:
                # Top-level изделие без подтипа в реестре — не трогаем.
                # Cron-агент должен решить: пометить 'неделимый' или добавить подтип в реестр.
                pass
            else:
                # Создать stub-файл часть_X.md (новый файл, не перезапись)
                content = generate_part_content(
                    part_id=parent_id, parent_id=parent_id, subsystem=subsystem,
                    subtype=subtype, mass_kg=mass_kg, share=share,
                    file_path=parent_path, tip=tip,
                    materials_bom=materials_bom, level_number=depth)
                batch.write(parent_path, content)
        return {'action': 'STOP_UNKNOWN', 'tip': tip, 'materials_bom': materials_bom,
                'parts_created': 0 if depth == 1 else 1, 'depth_reached': depth,
                'file_path': str(parent_path) if parent_path else None,
                'violation': f'подтип {subtype!r} отсутствует в _decomp_registry.yaml — '
                             f'{"top-level не тронут (нужно решение: неделимый или добавить в реестр)" if depth == 1 else "создан stub"}'}

    if action == 'STOP_ATOMIC':
        # v9.61: закупочные sub-assemblies теперь тип: изделие (с is_purchased: true)
        # Либо тип: часть (если is_purchased: false). В обоих случаях нужен BOM.
        tip = 'изделие' if info.get('is_purchased') else 'часть'
        materials_bom = []
        for m in info.get('materials', []):
            materials_bom.append((m.get('материал'), m.get('форма'), m.get('доля', 1.0)))

        # Для depth=1 (top-level изделие): НЕ перезаписываем существующий _index.md.
        # Только возвращаем BOM для агрегации в родительский файл (через update_parent_file).
        if not dry_run and parent_path and depth > 1:
            content = generate_part_content(
                part_id=parent_id, parent_id=parent_id, subsystem=subsystem,
                subtype=subtype, mass_kg=mass_kg, share=share,
                file_path=parent_path, tip=tip,
                materials_bom=materials_bom, level_number=depth)
            batch.write(parent_path, content)
        return {'action': 'STOP_ATOMIC', 'tip': tip, 'materials_bom': materials_bom,
                'parts_created': 1, 'depth_reached': depth,
                'file_path': str(parent_path) if parent_path else None}

    # RECURSE — для каждого child рекурсивно
    children = info.get('children', [])
    if not children:
        return {'action': 'STOP_NO_CHILDREN', 'parts_created': 0, 'depth_reached': depth,
                'violation': f'подтип {subtype!r} в реестре is_atomic=false, но children=[] — противоречие'}

    # Вычислить пути детей
    # Для top-level (depth=1): дети живут в <изделие>/<часть_X>/_index.md
    # Для depth>=2: дети живут в <родитель_dir>/<часть_X>/_index.md
    if depth == 1:
        children_base_dir = parent_path.parent
    else:
        children_base_dir = parent_path.parent

    child_ids = []
    materials_per_child = {}  # child_id → BOM
    total_created = 0
    max_depth_reached = depth

    for child in children:
        suffix = child.get('suffix', 'unknown')
        child_subtype = child.get('подтип_части', '')
        child_mass = child.get('масса_kg', 0.1)
        child_share = child.get('доля_массы', 0.1)
        child_id = build_part_id(parent_id, suffix)
        child_dir = children_base_dir / child_id
        child_path = child_dir / '_index.md'

        # Создать директорию
        if not dry_run:
            child_dir.mkdir(parents=True, exist_ok=True)

        # Рекурсивно декомпозировать ребёнка
        sub_result = decompose_node(child_subtype, child_id, subsystem,
                                     child_path, depth + 1, registry, canonical,
                                     batch, dry_run, _max_depth=_max_depth,
                                     mass_kg=child_mass, share=child_share)

        child_ids.append(child_id)
        if sub_result.get('materials_bom'):
            materials_per_child[child_id] = sub_result['materials_bom']
        total_created += sub_result.get('parts_created', 0)
        max_depth_reached = max(max_depth_reached, sub_result.get('depth_reached', depth))

    # Обновить родительский файл: заполнить дочерние_части + материалы_частей
    if not dry_run and depth == 1:
        # Только для top-level: обновляем _index.md родителя
        update_parent_file(parent_path, child_ids, materials_per_child, batch, dry_run)
    elif not dry_run and depth > 1:
        # Для промежуточных сборок: записываем их файл с детьми
        # (этот файл мог быть создан ранее, но мы его обновим с детьми)
        # В MVP: создаём заново с корректными children_ids
        tip = 'сборка'
        # Aggregate BOM от детей для наследуемых_материалы (упрощённо — для родителя)
        parent_bom = []
        for cid, bom in materials_per_child.items():
            for mat_id, forma, dolja in bom:
                parent_bom.append((mat_id, forma, dolja))
        if parent_path and parent_path.exists():
            content = generate_part_content(
                part_id=parent_id, parent_id=parent_id, subsystem=subsystem,
                subtype=subtype, mass_kg=mass_kg, share=share,
                file_path=parent_path, tip=tip,
                materials_bom=[],  # сборка не имеет собственного BOM (наследует)
                children_ids=child_ids, level_number=depth)
            batch.write(parent_path, content)

    return {
        'action': 'RECURSE',
        'children': len(child_ids),
        'child_ids': child_ids,
        'materials_per_child': materials_per_child,
        'parts_created': total_created,
        'depth_reached': max_depth_reached,
    }


def main():
    parser = argparse.ArgumentParser(description='SkyNet Recursive Decomposition Engine v9.60.1 (production)')
    parser.add_argument('--izdelie', help='id изделия для декомпозиции')
    parser.add_argument('--all', action='store_true', help='декомпозировать все top-level изделия')
    parser.add_argument('--dry-run', action='store_true', help='не записывать файлы, только отчёт')
    parser.add_argument('--max-depth', type=int, default=None, help=f'максимальная глубина (default {MAX_DEPTH})')
    parser.add_argument('--issue', type=int, help='GitHub issue # для интеграции с cron_run.sh (записывает в лог для коммита)')
    args = parser.parse_args()

    if not args.izdelie and not args.all:
        parser.error('укажите --izdelie <id> или --all')

    max_depth = args.max_depth if args.max_depth is not None else MAX_DEPTH

    print("=== SkyNet Recursive Decomposition Engine v9.60.1 (production) ===")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'APPLY'}")
    print(f"Max depth: {max_depth}")
    if args.issue:
        print(f"GitHub issue: #{args.issue}")
    print()

    registry = load_decomp_registry()
    canonical = load_canonical_materials()
    print(f"Реестр: {len(registry)} подтипов")
    print(f"Canonical материалов: {len(canonical)}")
    print()

    # Найти top-level изделия для обработки
    if args.all:
        top_files = list(IZDELIYA_DIR.rglob('_index.md'))
        top_izdeliya = []
        for f in top_files:
            data, _, _ = read_yaml_frontmatter(f)
            if data and data.get('уровень_номер') == 1:
                top_izdeliya.append((data.get('id'), f))
        print(f"Найдено top-level изделий: {len(top_izdeliya)}")
    else:
        top_izdeliya = []
        for f in IZDELIYA_DIR.rglob('_index.md'):
            data, _, _ = read_yaml_frontmatter(f)
            if data and data.get('id') == args.izdelie:
                top_izdeliya = [(args.izdelie, f)]
                break
        if not top_izdeliya:
            print(f"ERROR: изделие {args.izdelie!r} не найдено")
            sys.exit(1)

    print(f"К обработке: {len(top_izdeliya)} top-level изделий")
    print()

    # Декомпозировать каждое
    total_parts = 0
    total_depth = 0
    all_files_written = []  # для интеграции с cron_run.sh
    violations = []

    for izd_id, izd_path in top_izdeliya:
        data, _, _ = read_yaml_frontmatter(izd_path)
        subtype = data.get('подтип', 'прочее')
        subsystem = data.get('подсистема', 'прочее')

        print(f"--- {izd_id} (подтип: {subtype}) ---")

        if not args.dry_run:
            with TransactionBatch() as batch:
                result = decompose_node(subtype, izd_id, subsystem,
                                         izd_path, 1, registry, canonical, batch,
                                         _max_depth=max_depth)
        else:
            result = decompose_node(subtype, izd_id, subsystem,
                                     izd_path, 1, registry, canonical, None,
                                     dry_run=True, _max_depth=max_depth)
        print(f"  action: {result['action']}")
        print(f"  parts_created: {result.get('parts_created', 0)}")
        print(f"  depth_reached: {result.get('depth_reached', 0)}")
        if 'violation' in result:
            print(f"  VIOLATION: {result['violation']}")
            violations.append((izd_id, result['violation']))
        if result.get('child_ids'):
            print(f"  children: {result['child_ids']}")
            all_files_written.extend(result.get('child_ids', []))
        total_parts += result.get('parts_created', 0)
        total_depth = max(total_depth, result.get('depth_reached', 0))

    print()
    print(f"=== ИТОГО ===")
    print(f"Создано частей: {total_parts}")
    print(f"Максимальная глубина: {total_depth}")
    if violations:
        print(f"Violations: {len(violations)} (нужно ручное наполнение)")
    if args.issue and all_files_written:
        print(f"\n=== Для cron_run.sh ===")
        print(f"Files to commit:")
        for cid in all_files_written:
            print(f"  реальные данные/изделия/.../{cid}/_index.md")
        print(f"\nbash scripts/cron_run.sh {args.issue} \\")
        for i, cid in enumerate(all_files_written):
            sep = ' \\' if i < len(all_files_written) - 1 else ''
            print(f"  'реальные данные/изделия/.../{cid}/_index.md'{sep}")


if __name__ == '__main__':
    main()
