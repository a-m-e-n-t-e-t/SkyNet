#!/usr/bin/env python3
# scripts/organize_models.py v9.59
#
# Создаёт структуру результаты/модели/{model_name}/{3 подпапки} для всех 41 canon-моделей SkyNet.
# Копирует (не перемещает) файлы из 3 источников:
#   - фантастические данные/модели/{name}.md → "фантастическая реализация/_index.md"
#   - работа и и/изделия/.../_index.md (id=izdelie_SkyNet-*) → "доработанная ии реализация/_index.md"
#   - реальные данные/изделия/.../_index.md (id=izdelie_SkyNet-*) → "реальная реализация/_index.md"
#
# Использование: python3 scripts/organize_models.py
# Параметр --move для перемещения вместо копирования (по умолчанию копирует)

import os
import sys
import shutil
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANON_DIR = os.path.join(REPO_ROOT, 'фантастические данные', 'модели')
REAL_DIR = os.path.join(REPO_ROOT, 'реальные данные', 'изделия')
WORK_II_DIR = os.path.join(REPO_ROOT, 'работа и и', 'изделия')
OUTPUT_DIR = os.path.join(REPO_ROOT, 'результаты', 'модели')

SUBDIRS = [
    'фантастическая реализация',
    'реальная реализация',
    'доработанная ии реализация',
]

MOVE = '--move' in sys.argv

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

def find_wrappers(base_dir):
    """Находит все top-level _index.md с id=izdelie_SkyNet-* (не часть_*)."""
    result = {}
    for root, dirs, files in os.walk(base_dir):
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
    print(f'=== organize_models.py v9.59 (move={MOVE}) ===')
    print()

    # 1. Найти canon-модели
    canon_models = find_canon_models()
    print(f'Найдено canon-моделей: {len(canon_models)}')

    # 2. Найти обёртки izdelie_SkyNet-* (для ИИ-улучшенных)
    real_wrappers = find_wrappers(REAL_DIR)
    print(f'Найдено реальных обёрток izdelie_SkyNet-*: {len(real_wrappers)}')
    work_ii_wrappers = find_wrappers(WORK_II_DIR)
    print(f'Найдено ИИ-улучшенных обёрток izdelie_SkyNet-*: {len(work_ii_wrappers)}')

    # 3. Построить map: izdelie_id → [пути] для всех _index.md в реальные данные/
    real_id_map = {}
    for root, dirs, files in os.walk(REAL_DIR):
        for f in files:
            if f != '_index.md':
                continue
            fpath = os.path.join(root, f)
            iid = read_yaml_id(fpath)
            if iid:
                real_id_map.setdefault(iid, []).append(fpath)
    print(f'Уникальных id в реальные данные/: {len(real_id_map)}')
    print()

    # 4. Создать структуру и скопировать файлы
    created = 0
    canon_copied = 0
    real_copied = 0
    work_ii_copied = 0

    for name, canon_id, canon_path in canon_models:
        # Имя папки: canon-имя файла без .md (t800, cameron_phillips, t_x)
        model_dir = os.path.join(OUTPUT_DIR, name)

        # Создать 3 подпапки
        for subdir in SUBDIRS:
            os.makedirs(os.path.join(model_dir, subdir), exist_ok=True)
        created += 1

        # Файл фантастической реализации (canon .md → _index.md)
        canon_dest = os.path.join(model_dir, 'фантастическая реализация', '_index.md')
        if os.path.exists(canon_dest):
            os.remove(canon_dest)
        if MOVE:
            shutil.move(canon_path, canon_dest)
        else:
            shutil.copy2(canon_path, canon_dest)
        canon_copied += 1

        # Файлы реальной реализации — ВСЕ из реализация_промышленная
        # Читаем canon frontmatter чтобы получить реализация_промышленная
        try:
            with open(canon_dest, encoding='utf-8') as fp:
                canon_text = fp.read()
            canon_fm = canon_text.split('---')[1] if '---' in canon_text else ''
            canon_data = yaml.safe_load(canon_fm) or {}
        except Exception:
            canon_data = {}
        rp_list = canon_data.get('реализация_промышленная', []) or []

        # Создать подпапку для каждой реализации
        real_dir_path = os.path.join(model_dir, 'реальная реализация')
        for rid in rp_list:
            if rid in real_id_map:
                for src in real_id_map[rid]:
                    # Подпапка по имени реализации (id без префикса izdelie_)
                    sub_name = rid.replace('izdelie_', '', 1) if rid.startswith('izdelie_') else rid
                    sub_dir = os.path.join(real_dir_path, sub_name)
                    os.makedirs(sub_dir, exist_ok=True)
                    dest = os.path.join(sub_dir, '_index.md')
                    if os.path.exists(dest):
                        os.remove(dest)
                    if MOVE:
                        shutil.move(src, dest)
                    else:
                        shutil.copy2(src, dest)
                    real_copied += 1

        # Файл доработанной ИИ-реализации (если есть обёртка с matching canon-id)
        work_ii_dest = os.path.join(model_dir, 'доработанная ии реализация', '_index.md')
        if canon_id in work_ii_wrappers:
            src = work_ii_wrappers[canon_id]
            if os.path.exists(work_ii_dest):
                os.remove(work_ii_dest)
            if MOVE:
                shutil.move(src, work_ii_dest)
            else:
                shutil.copy2(src, work_ii_dest)
            work_ii_copied += 1

    print(f'=== Результаты ===')
    print(f'Создано папок моделей: {created}')
    print(f'Скопировано canon-файлов: {canon_copied}')
    print(f'Скопировано реальных изделий (из реализация_промышленная): {real_copied}')
    print(f'Скопировано ИИ-улучшенных обёрток: {work_ii_copied}')
    print()

    # 5. Отчёт о пустых папках
    missing_work_ii = []
    missing_real = []
    for name, canon_id, _ in canon_models:
        real_dir_path = os.path.join(OUTPUT_DIR, name, 'реальная реализация')
        work_ii_dest = os.path.join(OUTPUT_DIR, name, 'доработанная ии реализация', '_index.md')
        # Если в реальная реализация нет ни одной подпапки с _index.md
        has_real = False
        if os.path.exists(real_dir_path):
            for sub in os.listdir(real_dir_path):
                if os.path.exists(os.path.join(real_dir_path, sub, '_index.md')):
                    has_real = True
                    break
        if not has_real:
            missing_real.append(name)
        if not os.path.exists(work_ii_dest):
            missing_work_ii.append(name)
    print(f'Моделей без "реальная реализация": {len(missing_real)}')
    print(f'Моделей без "доработанная ии реализация": {len(missing_work_ii)}')
    print(f'Моделей с "доработанная ии реализация": {created - len(missing_work_ii)}')

if __name__ == '__main__':
    main()
