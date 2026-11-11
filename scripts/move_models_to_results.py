#!/usr/bin/env python3
# scripts/move_models_to_results.py v9.59
#
# Перемещает canon-модели и ИИ-обёртки из исходных мест в результаты/модели/:
#   - фантастические данные/модели/{name}.md → результаты/модели/{name}/фантастическая реализация/_index.md
#   - работа и и/изделия/.../_index.md (id=izdelie_SkyNet-*) → результаты/модели/{name}/доработанная ии реализация/_index.md
#
# Реальные данные в реальные данные/изделия/ НЕ ТРОГАЕТ (они нужны на месте для валидаторов).
#
# Использование: python3 scripts/move_models_to_results.py
# Параметр --dry-run — показать что будет сделано без выполнения.

import os
import sys
import shutil
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANON_DIR = os.path.join(REPO_ROOT, 'фантастические данные', 'модели')
WORK_II_DIR = os.path.join(REPO_ROOT, 'работа и и', 'изделия')
OUTPUT_DIR = os.path.join(REPO_ROOT, 'результаты', 'модели')

DRY_RUN = '--dry-run' in sys.argv

def read_yaml_id(path):
    try:
        with open(path, encoding='utf-8') as f:
            text = f.read()
        fm = text.split('---')[1] if '---' in text else ''
        data = yaml.safe_load(fm) or {}
        return data.get('id', '')
    except Exception:
        return ''

def find_canon_models():
    """Возвращает [(name, canon_id, canon_path), ...] для всех .md файлов моделей."""
    models = []
    for f in sorted(os.listdir(CANON_DIR)):
        if not f.endswith('.md'):
            continue
        if f.startswith('_'):
            continue
        path = os.path.join(CANON_DIR, f)
        canon_id = read_yaml_id(path)
        if not canon_id.startswith('SkyNet-'):
            continue
        name = os.path.splitext(f)[0]
        models.append((name, canon_id, path))
    return models

def find_work_ii_wrappers():
    """Находит все top-level _index.md с id=izdelie_SkyNet-* (не часть_*)."""
    result = {}  # canon_id → path
    for root, dirs, files in os.walk(WORK_II_DIR):
        for f in files:
            if f != '_index.md':
                continue
            fpath = os.path.join(root, f)
            if 'часть_' in fpath:
                continue
            iid = read_yaml_id(fpath)
            if iid.startswith('izdelie_SkyNet-'):
                canon = iid.replace('izdelie_', '', 1)
                result[canon] = fpath
    return result

def main():
    print(f'=== move_models_to_results.py v9.59 (dry_run={DRY_RUN}) ===')
    print()

    canon_models = find_canon_models()
    print(f'Найдено canon-моделей для перемещения: {len(canon_models)}')

    work_ii_wrappers = find_work_ii_wrappers()
    print(f'Найдено ИИ-обёрток для перемещения: {len(work_ii_wrappers)}')
    print()

    moved_canon = 0
    moved_work_ii = 0
    removed_empty_dirs = 0

    # 1. Переместить canon .md → результаты/модели/{name}/фантастическая реализация/_index.md
    for name, canon_id, canon_path in canon_models:
        model_dir = os.path.join(OUTPUT_DIR, name)
        canon_dest_dir = os.path.join(model_dir, 'фантастическая реализация')
        canon_dest = os.path.join(canon_dest_dir, '_index.md')
        os.makedirs(canon_dest_dir, exist_ok=True)

        # Проверить что в canon_dest уже лежит файл (скопированный ранее) — заменить его
        if os.path.exists(canon_dest):
            os.remove(canon_dest)

        if DRY_RUN:
            print(f'  [DRY-RUN] MOVE: {canon_path}')
            print(f'         → {canon_dest}')
        else:
            shutil.move(canon_path, canon_dest)
            print(f'  ✓ MOVED canon: {name} → фантастическая реализация/_index.md')
        moved_canon += 1

    # 2. Удалить пустые поддиректории в фантастические данные/модели/
    for d in sorted(os.listdir(CANON_DIR)):
        dpath = os.path.join(CANON_DIR, d)
        if not os.path.isdir(dpath):
            continue
        # Проверить что директория пустая
        if not os.listdir(dpath):
            if DRY_RUN:
                print(f'  [DRY-RUN] RMDIR: {dpath} (empty)')
            else:
                os.rmdir(dpath)
                print(f'  ✓ RMDIR empty: {d}')
            removed_empty_dirs += 1

    # 3. Переместить ИИ-обёртки из работа и и/ → результаты/модели/{name}/доработанная ии реализация/_index.md
    for canon_id, src_path in work_ii_wrappers.items():
        # Найти canon-name по canon-id
        matching = [(name, cid, cpath) for name, cid, cpath in canon_models if cid == canon_id]
        if not matching:
            print(f'  ⚠️  {canon_id} not found in canon_models — skip')
            continue
        name, _, _ = matching[0]
        model_dir = os.path.join(OUTPUT_DIR, name)
        work_ii_dest_dir = os.path.join(model_dir, 'доработанная ии реализация')
        work_ii_dest = os.path.join(work_ii_dest_dir, '_index.md')
        os.makedirs(work_ii_dest_dir, exist_ok=True)

        if os.path.exists(work_ii_dest):
            os.remove(work_ii_dest)

        if DRY_RUN:
            print(f'  [DRY-RUN] MOVE: {src_path}')
            print(f'         → {work_ii_dest}')
        else:
            shutil.move(src_path, work_ii_dest)
            print(f'  ✓ MOVED wrapper: {canon_id} → доработанная ии реализация/_index.md')
        moved_work_ii += 1

        # Удалить родительскую директорию обёртки в работа и и/, если она стала пустой
        parent_dir = os.path.dirname(src_path)
        if os.path.exists(parent_dir):
            # Не удалять сразу, проверить что в parent_dir нет других _index.md (часть_*)
            # Если есть часть_*, оставить директорию
            has_parts = any('часть_' in f for f in os.listdir(parent_dir))
            if not has_parts and not os.listdir(parent_dir):
                if DRY_RUN:
                    print(f'  [DRY-RUN] RMDIR: {parent_dir} (empty after move)')
                else:
                    os.rmdir(parent_dir)
                    print(f'  ✓ RMDIR empty: {parent_dir}')

    print()
    print(f'=== Итог ===')
    print(f'Перемещено canon-моделей: {moved_canon}')
    print(f'Удалено пустых дир: {removed_empty_dirs}')
    print(f'Перемещено ИИ-обёрток: {moved_work_ii}')

if __name__ == '__main__':
    main()
