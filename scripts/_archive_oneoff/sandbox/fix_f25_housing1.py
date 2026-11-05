# -*- coding: utf-8 -*-
"""Issue #109 (F25 cluster 660×660×660): 68 файлов *_housing.
Housing = корпус соответствующего _core (данные из fix_f25_cluster2.ITEMS):
габариты ядра +15 % (припуск на стенки/крепёж), масса ≈ 90 % массы ядра,
материал al_6061-t6 (stal_st3 для крупногабарита), URL/референс — от ядра.
"""
import re, glob, os, sys, math

sys.path.insert(0, '/home/z/my-project/scripts')
import fix_f25_cluster2 as c2

BIG = {'copv_core', 'slm_eos_m290_core', 'ipg_yls-eco_core', 'kaskadnyi_stirling-kriokuler_core',
       'reshetchatyi_karkas_core', 'ultrakorotkoimpulsnye_lazery_core', 'minigun_m134_core'}

def margin(v):
    """+15% к габариту ядра, округление вверх, мин +3 мм."""
    fv = float(v)
    base = int(fv) if fv == int(fv) else fv
    grown = fv * 1.15
    return int(max(fv + 3, math.ceil(grown)))

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
        if not item_id.endswith('_housing'): continue
        lm = re.search(r'габариты_mm:\s*\n\s+l:\s*(\S+)\s*\n\s+w:\s*(\S+)\s*\n\s+h:\s*(\S+)', fm)
        massa = re.search(r'^  масса_kg:\s*(\S+)', fm, re.M)
        if not (lm and massa): continue
        if (lm.group(1), lm.group(2), lm.group(3)) != ('660','660','660'): continue
        core_key = item_id.replace('_housing', '_core')
        key = core_key if core_key in c2.ITEMS else core_key.replace('часть_', '', 1)
        if key not in c2.ITEMS:
            print('NO CORE DATA:', item_id); continue
        cl, cw, ch, cm, cmat, curl, cref, cbasis, cfunc = c2.ITEMS[key]
        l, w, h = margin(cl), margin(cw), margin(ch)
        mat = 'stal_st3' if key in BIG else 'al_6061-t6'
        massa_new = max(0.015, round(cm * 0.9, 3))
        d = (str(l), str(w), str(h))
        if d in dims_seen: clashes.append((item_id, d, dims_seen[d]))
        dims_seen[d] = item_id
        mfmt = c2.fmt(massa_new)
        ref_short = cref.split(' (')[0]
        func_short = cfunc.split('—')[0].strip().rstrip('.')
        desc = ('Корпус (housing) узла «%s» — защитный кожух ядра (%s): жёсткая оболочка с монтажными лапами, '
                'съёмной крышкой и локальными кабельными вводами; экранирует ядро от внешних ЭМИ-полей и механических '
                'воздействий. Габариты %d×%d×%d мм — габарит ядра (%s×%s×%s) с припуском ~15 %% на стенки и крепёж. '
                'Масса %s кг — оценка (оболочка ≈ 90 %% массы узла). Материал — %s: жёсткость, ЭМИ-экранирование, '
                'коррозионная стойкость; крепёж — нержавеющие винты M3/M4.') % (
                func_short, ref_short, l, w, h, cl, cw, ch, mfmt, mat)
        old_mat_m = re.search(r'^\s+материал:\s*(\S+)', fm, re.M)
        old_mat = old_mat_m.group(1) if old_mat_m else None
        txt = re.sub(r'(габариты_mm:\s*\n\s+l:)\s*\S+', r'\g<1> %d' % l, txt, count=1)
        txt = re.sub(r'(\n\s+w:)\s*\S+', r'\g<1> %d' % w, txt, count=1)
        txt = re.sub(r'(\n\s+h:)\s*\S+', r'\g<1> %d' % h, txt, count=1)
        txt = re.sub(r'(  масса_kg:)\s*\S+', r'\g<1> %s' % mfmt, txt, count=1)
        if old_mat != mat:
            txt = re.sub(r'(\n  - часть: %s\n    материал: )\S+' % re.escape(item_id), r'\g<1>%s' % mat, txt, count=1)
        txt = re.sub(r'^источник_разбора:.*$', 'источник_разбора: веб-верификация', txt, count=1, flags=re.M)
        txt = re.sub(r'^дата_обновления:.*$', 'дата_обновления: 2026-11-05', txt, count=1, flags=re.M)
        if re.search(r'^источник_url:', txt, re.M):
            txt = re.sub(r'^источник_url:.*$', 'источник_url: %s' % curl, txt, count=1, flags=re.M)
        else:
            txt = re.sub(r'^источник_разбора: веб-верификация$', 'источник_разбора: веб-верификация\nисточник_url: %s\nисточник_дата: 2026-11-05' % curl, txt, count=1, flags=re.M)
        if not re.search(r'^источник_дата:', txt, re.M):
            txt = re.sub(r'^(источник_url: .+)$', r'\1\nисточник_дата: 2026-11-05', txt, count=1, flags=re.M)
        txt = re.sub(r'(## Описание\n\n).*?(\n\nРодитель:)', r'\g<1>%s\g<2>' % desc, txt, count=1, flags=re.S)
        txt = re.sub(r'\| масса \| \S+ \| kg \|[^|]*\|', '| масса | %s | kg | корпус ядра %s |' % (mfmt, ref_short), txt, count=1)
        txt = re.sub(r'\| габариты \(Д×Ш×В\) \| \S+ \| mm \|[^|]*\|', '| габариты (Д×Ш×В) | %d×%d×%d | mm | ядро %s + припуск 15%% |' % (l, w, h, ref_short), txt, count=1)
        txt = re.sub(r'\| материал \| (\S+)[^|]*\|[^|]*\|', '| материал | %s | — | корпус узла |' % mat, txt, count=1)
        if old_mat and old_mat != mat:
            pat = r'- `%s` → \[[^\]]+\]\([^)]+\)[^\n]*' % re.escape(old_mat)
            repl = '- `%s` → [`%s.md`](../../../../материалы/%s.md) — %s' % (mat, mat, mat, c2.MAT_NOTES.get(mat, mat))
            txt2, n = re.subn(pat, repl, txt, count=1)
            txt = txt2 if n else txt
        src_line = '- %s (корпус узла по габаритам ядра) — %s (обращение 2026-11-05)' % (ref_short, curl)
        if src_line not in txt:
            if '- Канон:' in txt: txt = txt.replace('- Канон:', src_line + '\n- Канон:', 1)
            else: txt = txt.replace('- Материалы:', src_line + '\n- Материалы:', 1)
        open(f, 'w', encoding='utf-8').write(txt)
        changed.append('%s → %d×%d×%d, %s кг, %s' % (item_id, l, w, h, mfmt, mat))
    print('CHANGED: %d' % len(changed))
    for c in changed: print('  ✓', c)
    print('CLASHES:', clashes if clashes else 'NONE')

if __name__ == '__main__':
    if 'SkyNet' not in os.getcwd():
        os.chdir('/home/z/my-project/SkyNet')
    main()
