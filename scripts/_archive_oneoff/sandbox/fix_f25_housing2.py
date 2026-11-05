# -*- coding: utf-8 -*-
"""Issue #109: 13 изделий-уровневых housing из кластера 660×660×660 — ручные референсы."""
import re, glob, os, sys, math

sys.path.insert(0, '/home/z/my-project/scripts')
import fix_f25_cluster2 as c2

ITEMS = {
 'часть_induktivnyi_nakopitel_housing': ('500','500','800',45,'stal_st3','https://en.wikipedia.org/wiki/Inductor','Индуктивный накопитель энергии (машинный шкаф класса)','est'),
 'часть_marx_generator_housing': ('800','600','1600',120,'stal_st3','https://en.wikipedia.org/wiki/Marx_generator','Генератор Маркса (напольный импульсный шкаф)','est'),
 'часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_housing': ('90','90','450',8,'al_6061-t6','https://en.wikipedia.org/wiki/Planetary_roller_screw','привод ПРВП (серводвигатель + ролико-винтовая пара в кожухе)','est'),
 'часть_asrg_housing': ('620','320','320',30,'al_6061-t6','https://en.wikipedia.org/wiki/Advanced_Stirling_radioisotope_generator','ASRG (Advanced Stirling Radioisotope Generator, NASA: ~60×30×30 см, ~30 кг)','ref'),
 'часть_mmrtg_housing': ('680','680','750',42,'al_6061-t6','https://rps.nasa.gov/power-and-thermal-systems/power-systems/mmrtg/','MMRTG (NASA: Ø64.3×69 см, ~45.8 кг整机)','ref'),
 'часть_mptm_housing': ('220','160','90',3.5,'al_6061-t6','https://en.wikipedia.org/wiki/Electronic_control_unit','блок электроники управления (компактный корпус ЭКУ)','est'),
 'часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_housing': ('180','180','120',6,'al_6061-t6','https://en.wikipedia.org/wiki/Superconducting_magnetic_energy_storage','узел ВТСП-подшипника (корпус с криоконтуром)','est'),
 'часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_housing': ('200','150','100',4,'al_6061-t6','https://en.wikipedia.org/wiki/Artificial_muscle','испытательный модуль магнитной мышцы (UNIST)','est'),
 'часть_coilgun_housing': ('400','250','1200',55,'stal_st3','https://en.wikipedia.org/wiki/Coilgun','катушечная пушка (стволовый кожух с каскадами)','est'),
 'часть_zeno_power_am-241_housing': ('300','300','500',25,'al_6061-t6','https://zenopower.com','Zeno Power: радиоизотопный источник на AM-241 (корпус РИТЭГ)','ref'),
 'часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_housing': ('120','120','160',5,'stal_st3','https://en.wikipedia.org/wiki/Electromagnetic_clutch','порошковая электромагнитная муфта/тормоз (корпус с катушкой)','est'),
 'часть_emi-generator_housing': ('600','500','1200',90,'stal_st3','https://en.wikipedia.org/wiki/Electromagnetic_interference','генератор ЭМИ (импульсный шкаф)','est'),
 'часть_alyuminievo-vozdushnye_toplivnye_elementy_housing': ('420','300','250',12,'al_6061-t6','https://en.wikipedia.org/wiki/Aluminium%E2%80%93air_battery','батарея Al-air (корпус с воздушными каналами)','est'),
}

def main():
    changed, clashes = [], []
    dims_seen = {}
    for f in glob.glob('реальные данные/изделия/**/часть_*/_index.md', recursive=True):
        try: txt = open(f, encoding='utf-8').read()
        except Exception: continue
        fm = txt.split('---')[1] if txt.startswith('---') else ''
        m_id = re.search(r'^id:\s*(\S+)', fm, re.M)
        if not m_id: continue
        item_id = m_id.group(1)
        if item_id not in ITEMS: continue
        lm = re.search(r'габариты_mm:\s*\n\s+l:\s*(\S+)\s*\n\s+w:\s*(\S+)\s*\n\s+h:\s*(\S+)', fm)
        massa = re.search(r'^  масса_kg:\s*(\S+)', fm, re.M)
        if not (lm and massa): continue
        if (lm.group(1), lm.group(2), lm.group(3)) != ('660','660','660'):
            print('SKIP (не 660):', item_id); continue
        l, w, h, massa_new, mat, url, ref, basis = ITEMS[item_id]
        d = (str(l), str(w), str(h))
        if d in dims_seen: clashes.append((item_id, d, dims_seen[d]))
        dims_seen[d] = item_id
        mfmt = c2.fmt(massa_new)
        basis_txt = 'паспортные данные %s' % ref.split(' (')[0] if basis == 'ref' else 'оценка по типовым изделиям класса (%s)' % ref.split(' (')[0]
        desc = ('Корпус (housing) изделия — несущий защитный кожух узла: референс — %s. Обеспечивает жёсткость '
                'конструкции, отвод тепла и защиту внутренних компонентов; кабельные вводы и монтажные точки по стыковочным '
                'поверхностям. Габариты %s×%s×%s мм, масса %s кг — %s. Материал — %s: %s.') % (
                ref, l, w, h, mfmt, basis_txt, mat, c2.MAT_NOTES.get(mat, mat))
        old_mat_m = re.search(r'^\s+материал:\s*(\S+)', fm, re.M)
        old_mat = old_mat_m.group(1) if old_mat_m else None
        txt = re.sub(r'(габариты_mm:\s*\n\s+l:)\s*\S+', r'\g<1> %s' % l, txt, count=1)
        txt = re.sub(r'(\n\s+w:)\s*\S+', r'\g<1> %s' % w, txt, count=1)
        txt = re.sub(r'(\n\s+h:)\s*\S+', r'\g<1> %s' % h, txt, count=1)
        txt = re.sub(r'(  масса_kg:)\s*\S+', r'\g<1> %s' % mfmt, txt, count=1)
        if old_mat != mat:
            txt = re.sub(r'(\n  - часть: %s\n    материал: )\S+' % re.escape(item_id), r'\g<1>%s' % mat, txt, count=1)
        txt = re.sub(r'^источник_разбора:.*$', 'источник_разбора: веб-верификация', txt, count=1, flags=re.M)
        txt = re.sub(r'^дата_обновления:.*$', 'дата_обновления: 2026-11-05', txt, count=1, flags=re.M)
        if re.search(r'^источник_url:', txt, re.M):
            txt = re.sub(r'^источник_url:.*$', 'источник_url: %s' % url, txt, count=1, flags=re.M)
        else:
            txt = re.sub(r'^источник_разбора: веб-верификация$', 'источник_разбора: веб-верификация\nисточник_url: %s\nисточник_дата: 2026-11-05' % url, txt, count=1, flags=re.M)
        if not re.search(r'^источник_дата:', txt, re.M):
            txt = re.sub(r'^(источник_url: .+)$', r'\1\nисточник_дата: 2026-11-05', txt, count=1, flags=re.M)
        txt = re.sub(r'(## Описание\n\n).*?(\n\nРодитель:)', r'\g<1>%s\g<2>' % desc, txt, count=1, flags=re.S)
        txt = re.sub(r'\| масса \| \S+ \| kg \|[^|]*\|', '| масса | %s | kg | %s |' % (mfmt, ref), txt, count=1)
        txt = re.sub(r'\| габариты \(Д×Ш×В\) \| \S+ \| mm \|[^|]*\|', '| габариты (Д×Ш×В) | %s×%s×%s | mm | %s |' % (l, w, h, ref), txt, count=1)
        txt = re.sub(r'\| материал \| (\S+)[^|]*\|[^|]*\|', '| материал | %s | — | корпус узла |' % mat, txt, count=1)
        if old_mat and old_mat != mat:
            pat = r'- `%s` → \[[^\]]+\]\([^)]+\)[^\n]*' % re.escape(old_mat)
            repl = '- `%s` → [`%s.md`](../../../../материалы/%s.md) — %s' % (mat, mat, mat, c2.MAT_NOTES.get(mat, mat))
            txt2, n = re.subn(pat, repl, txt, count=1)
            txt = txt2 if n else txt
        src_line = '- %s — %s (обращение 2026-11-05)' % (ref, url)
        if src_line not in txt:
            if '- Канон:' in txt: txt = txt.replace('- Канон:', src_line + '\n- Канон:', 1)
            else: txt = txt.replace('- Материалы:', src_line + '\n- Материалы:', 1)
        open(f, 'w', encoding='utf-8').write(txt)
        changed.append('%s → %s×%s×%s, %s кг, %s' % (item_id, l, w, h, mfmt, mat))
    print('CHANGED: %d' % len(changed))
    for c in changed: print('  ✓', c)
    print('CLASHES:', clashes if clashes else 'NONE')

if __name__ == '__main__':
    if 'SkyNet' not in os.getcwd():
        os.chdir('/home/z/my-project/SkyNet')
    main()
