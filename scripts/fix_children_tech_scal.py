#!/usr/bin/env python3
# fix_children_tech_scal.py
# Добавляет технологии_частей и масштабируемость (фиксированная) к детям,
# у которых есть материалы_частей но нет технологии_частей / масштабируемость
#
# Использование: python3 scripts/fix_children_tech_scal.py <parent_id>

import sys, os, yaml, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util

spec = importlib.util.spec_from_file_location('vd', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'validate_decomposition.py'))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
izdeliya = mod.load_all_izdeliya()

parent_id = sys.argv[1]
parent_data = izdeliya.get(parent_id)
if not parent_data:
    print(f"✗ {parent_id} not found")
    sys.exit(1)

# Технологии по умолчанию для материала
TECH_BY_MATERIAL = {
    'al_6061-t6': 'frezervanie_chpu',
    'aluminum': 'anodirovanie',
    'ti-6al-4v': 'ebw',
    'silicone-textile_composite': 'parylene_c',
    'tungsten_alloy': 'frezervanie_chpu',
    'carbon_fiber_composite': 'autoclave_composite_curing',
    'latun_c36000': 'stampovka',
    'si': 'cmos_7nm_intel4',
    'inconel_718': 'investement_casting_superalloy',
}

count_fixed = 0
for pid in parent_data.get('дочерние_части', []):
    part = izdeliya.get(pid)
    if not part:
        continue
    path = part.get('_path')
    if not path or not os.path.exists(path):
        continue
    with open(path) as f:
        text = f.read()
    fm = text.split('---')[1] if '---' in text else ''
    data = yaml.safe_load(fm) or {}
    if not data:
        continue

    changed = False
    mp = data.get('материалы_частей', [])
    if mp and not data.get('технологии_частей'):
        # Add технологии_частей
        new_tech = []
        for m in mp:
            mat = m.get('материал', '')
            tech = TECH_BY_MATERIAL.get(mat, 'frezervanie_chpu')
            new_tech.append({
                'часть': pid,
                'технология': tech,
                'доля_использования': 1.0,
                'материалы_для_процесса': [{'материал': mat, 'роль': 'обрабатываемый'}],
            })
        data['технологии_частей'] = new_tech
        changed = True

    if not data.get('масштабируемость'):
        data['масштабируемость'] = {
            'режим': 'фиксированная',
            'параметры': [
                {'имя': 'количество_единиц', 'диапазон': [1, 1], 'единица': 'шт'},
            ],
            'пределы': {'max_единиц_в_системе': 1},
            'закон_масштабирования': 'фиксированный — деталь не масштабируется (leaf node в составе родительского изделия)',
            'ограничивающие_части': [],
        }
        changed = True

    if changed:
        out = io.StringIO()
        out.write('---\n')
        yaml.safe_dump(data, out, allow_unicode=True, sort_keys=False, default_flow_style=False)
        out.write('---\n')
        new_text = out.getvalue() + text.split('---', 2)[2]
        with open(path, 'w') as f:
            f.write(new_text)
        print(f'  ✓ {pid}: added технологии_частей + масштабируемость')
        count_fixed += 1

print(f'\nИтого: {count_fixed} детей исправлено')
