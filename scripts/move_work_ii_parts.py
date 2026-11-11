#!/usr/bin/env python3
# scripts/move_work_ii_parts.py v9.59
#
# Перемещает ВСЕ дочерние части (часть_*) из работа и и/изделия/{подсистема}/{wrapper}/
# в результаты/модели/{canon_name}/доработанная ии реализация/
#
# Используется ПОСЛЕ move_models_to_results.py (который перемещает _index.md обёрток).

import os
import sys
import shutil
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK_II_DIR = os.path.join(REPO_ROOT, 'работа и и', 'изделия')
RESULTS_DIR = os.path.join(REPO_ROOT, 'результаты', 'модели')

DRY_RUN = '--dry-run' in sys.argv

# Mapping: canon_id → canon_name (для поиска canon-name по canon-id)
# Строится из результаты/модели/*/фантастическая реализация/_index.md
def build_canon_id_to_name():
    mapping = {}
    if not os.path.isdir(RESULTS_DIR):
        return mapping
    for name in os.listdir(RESULTS_DIR):
        model_dir = os.path.join(RESULTS_DIR, name)
        if not os.path.isdir(model_dir):
            continue
        canon_path = os.path.join(model_dir, 'фантастическая реализация', '_index.md')
        if not os.path.exists(canon_path):
            continue
        try:
            with open(canon_path, encoding='utf-8') as f:
                text = f.read()
            fm = text.split('---')[1] if '---' in text else ''
            data = yaml.safe_load(fm) or {}
            canon_id = data.get('id', '')
            if canon_id:
                mapping[canon_id] = name
        except Exception:
            pass
    return mapping

def main():
    print(f'=== move_work_ii_parts.py v9.59 (dry_run={DRY_RUN}) ===\n')

    canon_id_to_name = build_canon_id_to_name()
    print(f'Canon-id → name: {len(canon_id_to_name)} моделей')

    # Найти все поддиректории в работа и и/изделия/{подсистема}/{wrapper}/, которые
    # содержат часть_* (это значит обёртка была перемещена, но части остались)
    moved_count = 0
    removed_dirs = 0

    for sub in os.listdir(WORK_II_DIR):
        sub_dir = os.path.join(WORK_II_DIR, sub)
        if not os.path.isdir(sub_dir):
            continue
        for wrapper in os.listdir(sub_dir):
            wrapper_dir = os.path.join(sub_dir, wrapper)
            if not os.path.isdir(wrapper_dir):
                continue
            # Проверить что в wrapper_dir НЕТ _index.md (обёртка перемещена)
            wrapper_index = os.path.join(wrapper_dir, '_index.md')
            if os.path.exists(wrapper_index):
                continue  # обёртка на месте, не трогаем
            # Содержимое wrapper_dir — это дочерние части (часть_*)
            # Найти canon-id по имени директории
            # Имя директории может быть: cameron, hkaerial, marcuswright, rev9, t600, t800, t850, tx, hktank, t1000, t1001
            # Соответствует canon-id: SkyNet-Cameron, SkyNet-HKAerial и т.д.
            # Сопоставление через reverse lookup
            canon_name = None
            # Normalize wrapper name (remove underscores, lowercase) for matching
            for cid, cname in canon_id_to_name.items():
                # cid like 'SkyNet-Cameron', 'SkyNet-HKAerial'
                # cname like 'cameron_phillips', 'hk_aerial'
                # wrapper like 'cameron', 'hkaerial'
                # Normalize: remove '-' and '_' and lowercase
                cid_norm = cid.replace('SkyNet-', '').replace('-', '').replace('_', '').lower()
                cname_norm = cname.replace('-', '').replace('_', '').lower()
                wrapper_norm = wrapper.replace('-', '').replace('_', '').lower()
                # Match if wrapper_norm is a prefix of cname_norm OR they start the same
                if wrapper_norm and (cname_norm.startswith(wrapper_norm) or cid_norm.startswith(wrapper_norm)):
                    canon_name = cname
                    break
            if not canon_name:
                print(f'  ⚠️  Не найден canon-name для wrapper dir: {wrapper} ({sub})')
                continue

            # Целевая директория: результаты/модели/{canon_name}/доработанная ии реализация/
            target_dir = os.path.join(RESULTS_DIR, canon_name, 'доработанная ии реализация')
            if not os.path.exists(target_dir):
                os.makedirs(target_dir, exist_ok=True)

            # Переместить все дочерние директории (часть_*)
            for item in os.listdir(wrapper_dir):
                src = os.path.join(wrapper_dir, item)
                dst = os.path.join(target_dir, item)
                if not os.path.isdir(src):
                    continue
                if os.path.exists(dst):
                    # Если уже есть — пропустить (защита от перезаписи)
                    print(f'  ⚠️  Already exists: {dst} — skip')
                    continue
                if DRY_RUN:
                    print(f'  [DRY-RUN] MOVE: {src}')
                    print(f'         → {dst}')
                else:
                    shutil.move(src, dst)
                    moved_count += 1

            # Удалить пустую wrapper_dir
            if not os.listdir(wrapper_dir):
                if DRY_RUN:
                    print(f'  [DRY-RUN] RMDIR: {wrapper_dir}')
                else:
                    os.rmdir(wrapper_dir)
                    removed_dirs += 1

    print(f'\n=== Итог ===')
    print(f'Перемещено поддиректорий часть_*: {moved_count}')
    print(f'Удалено пустых wrapper дир: {removed_dirs}')

if __name__ == '__main__':
    main()
