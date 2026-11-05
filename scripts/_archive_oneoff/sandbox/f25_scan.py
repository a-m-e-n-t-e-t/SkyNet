"""Полный скан F25-групп: зеркалит логику validate_decomposition.py через его же загрузчик."""
import sys
from collections import defaultdict

sys.path.insert(0, '/home/z/my-project/SkyNet/scripts')
from validate_decomposition import load_all_izdeliya  # noqa: E402

izdeliya = load_all_izdeliya()
sigs = defaultdict(list)
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
    l, w, h = dims.get('l'), dims.get('w'), dims.get('h')
    material = ''
    mats = data.get('материалы_частей', [])
    if isinstance(mats, list):
        for m in mats:
            if isinstance(m, dict):
                material = str(m.get('материал', ''))
                break
    sigs[(l, w, h, mass, material)].append(izd_id)

groups = sorted(((s, ids) for s, ids in sigs.items() if len(ids) > 2),
                key=lambda x: -len(x[1]))
print(f'Всего сигнатур: {len(sigs)}, файлы часть_*: {sum(len(v) for v in sigs.values())}')
print(f'Групп с >2 файлов: {len(groups)}\n')
for sig, ids in groups:
    ids_sorted = sorted(ids)
    print(f'{len(ids):3d} шт  {sig[0]}×{sig[1]}×{sig[2]}  {sig[3]}кг  {sig[4]}: {ids_sorted[0]}')

# Отдельные проверки по issue
print('\n--- Проверки по issue ---')
for l, w, h, m, mat, label in [
        (660.0, 660.0, 660.0, 0.3, 'ti-6al-4v', '#75 (660)'),
        (100.0, 100.0, 50.0, 0.5, 'ti-6al-4v', '#74/#82 (100x100x50)')]:
    hits = sorted(sigs.get((l, w, h, m, mat), []))
    print(f'{label}: {len(hits)} файлов' + (f', первый: {hits[0]}' if hits else ''))
