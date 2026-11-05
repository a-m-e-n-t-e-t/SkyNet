#!/usr/bin/env python3
"""Find files matching F25 signature: 660x660x660mm, 0.3kg, ti-6al-4v (issue #52)."""
import os, re, glob

ROOT = '/home/z/my-project/SkyNet/реальные данные/изделия'
hits = []
for f in glob.glob(os.path.join(ROOT, '**', '_index.md'), recursive=True):
    try:
        t = open(f, encoding='utf-8').read()
    except Exception:
        continue
    fm = t.split('---')[1] if t.startswith('---') else ''
    m_l = re.search(r'l:\s*([\d.]+)', fm)
    m_w = re.search(r'w:\s*([\d.]+)', fm)
    m_h = re.search(r'h:\s*([\d.]+)', fm)
    m_mass = re.search(r'масса_kg:\s*([\d.]+)', fm)
    mats = re.findall(r'материал:\s*(\S+)', fm)
    if not (m_l and m_w and m_h and m_mass):
        continue
    dims = (float(m_l.group(1)), float(m_w.group(1)), float(m_h.group(1)))
    mass = float(m_mass.group(1))
    if dims == (660.0, 660.0, 660.0) and mass == 0.3 and 'ti-6al-4v' in mats:
        pid = re.search(r'id:\s*(\S+)', fm).group(1)
        hits.append((pid, f.replace(ROOT + '/', '')))

for pid, rel in sorted(hits):
    print(f'{pid:60s} | {rel}')
print('TOTAL:', len(hits))
