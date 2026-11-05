# -*- coding: utf-8 -*-
"""Общий модуль для батч-фиксов F25-кластеров (части с шаблонными данными).

История: fix_f25_cluster2.py (#107), fix_f25_housing1/2.py (#109),
fix_f25_connectors.py (#108) повторяли одну и ту же regex-логику ~100 строк each.
Теперь: словарь ITEMS + один вызов apply_batch().

Использование в новом батч-скрипте:
    from fix_f25 import apply_batch, check_unique_dims, MAT_NOTES

    ITEMS = {'<id>:': (l, w, h, massa, mat, url, ref, basis, funkc), ...}
    # или расширенный кортеж с pin: (l, w, h, massa, mat, pin, url, ref, basis, funkc)
    check_unique_dims(ITEMS)
    apply_batch(ITEMS, old_dims=('50','50','30'), date='2026-11-05')

basis: 'ref' = паспортные данные стандарта/каталога, 'est' = оценка по типовым изделиям.
Идемпотентно: обрабатывает только файлы с исходными old_dims.
"""
import re, glob, os, sys

REPO = '/home/z/my-project/SkyNet'

MAT_NOTES = {
 'becu': 'бериллиевая бронза (контакты, CuBe; золотое покрытие по Ni)',
 'latun_c36000': 'латунь C36000 (корпуса/контакты, покрытие Au/Ni)',
 'al_6061-t6': 'алюминиевый сплав 6061-T6 (корпуса)',
 'stal_st3': 'конструкционная сталь Ст3 (корпуса с цинковым покрытием)',
 'poliimid': 'полиимид (термопластичные корпуса/шлейфы)',
 'neilon_6_66': 'нейлон 6/6 (PA66, корпус разъёма)',
 'si': 'монокристаллический кремний',
 'ti-6al-4v': 'титановый сплав Ti-6Al-4V',
 'peek': 'PEEK (полиэфирэфиркетон)',
 'mednyi_provod': 'медь (проводниковая)',
 'inconel_718': 'жаропрочный сплав Inconel 718',
 'cfrp_t1100g': 'углепластик на волокне T1100',
 'aln': 'нитрид алюминия (AlN, пьезоэлектрик)',
}


def fmt(x):
    s = ('%.6f' % x).rstrip('0').rstrip('.')
    return s if s else '0'


def check_unique_dims(items):
    """Проверить уникальность (l, w, h) по всем items до записи. Прерывает по дубликату."""
    seen = {}
    for k, v in items.items():
        key = (str(v[0]), str(v[1]), str(v[2]))
        if key in seen:
            raise ValueError('DUP DIMS: %s и %s: %s' % (k, seen[key], key))
        seen[key] = k
    return len(items)


def _norm_key(items):
    """Нормализовать ключи: допускаются id с префиксом 'часть_' и без."""
    out = {}
    for k, v in items.items():
        out[k] = v
        base = k.replace('часть_', '', 1)
        out.setdefault(base, v)
    return out


def apply_batch(items, old_dims=('50', '50', '30'), date='2026-11-05', desc_prefix='Комплект разъёмов и жгутов изделия'):
    """Применить батч к репозиторию. Возвращает (changed, skipped).

    items: {key: (l, w, h, massa, mat, [pin,] url, ref, basis, funkc)}
    Распознаёт 9- и 10-польные кортежи (pin опционален).
    old_dims: исходная шаблонная комбинация габаритов (условие обработки).
    """
    os.chdir(REPO) if not os.getcwd().endswith('SkyNet') else None
    items = _norm_key(items)
    changed, skipped = [], []
    for f in sorted(glob.glob('реальные данные/изделия/**/часть_*/_index.md', recursive=True)):
        try:
            txt = open(f, encoding='utf-8').read()
        except Exception:
            continue
        fm = txt.split('---')[1] if txt.startswith('---') else ''
        m_id = re.search(r'^id:\s*(\S+)', fm, re.M)
        if not m_id:
            continue
        item_id = m_id.group(1)
        key = item_id if item_id in items else item_id.replace('часть_', '', 1)
        if key not in items:
            continue
        lm = re.search(r'габариты_mm:\s*\n\s+l:\s*(\S+)\s*\n\s+w:\s*(\S+)\s*\n\s+h:\s*(\S+)', fm)
        massa = re.search(r'^  масса_kg:\s*(\S+)', fm, re.M)
        if not (lm and massa):
            continue
        if (lm.group(1), lm.group(2), lm.group(3)) != tuple(old_dims):
            skipped.append(item_id)
            continue
        v = items[key]
        if len(v) == 10:
            l, w, h, massa_new, mat, pin, url, ref, basis, funkc = v
        else:
            l, w, h, massa_new, mat, url, ref, basis, funkc = v
            pin = None
        old_share = re.search(r'^  доля_массы_родителя:\s*(\S+)', fm, re.M)
        new_share = fmt(round(massa_new * float(old_share.group(1)) / 0.05, 6)) if old_share else None
        old_mat_m = re.search(r'^\s+материал:\s*(\S+)', fm, re.M)
        old_mat = old_mat_m.group(1) if old_mat_m else None
        basis_txt = 'паспортные данные стандарта/каталога' if basis == 'ref' else 'оценка по типовым изделиям класса'
        desc = ('%s: %s. Референсное исполнение — %s. Габариты %s×%s×%s мм, масса %s кг — %s. '
                'Материал — %s: %s.') % (desc_prefix, funkc, ref, l, w, h, fmt(massa_new), basis_txt, mat, MAT_NOTES.get(mat, mat))
        principle = ('Стыковка/функционирование по референсу (%s): параметры соответствуют типовому '
                     'исполнению семейства; тепловыделение и ресурс — по паспорту/оценке класса.' % ref)
        t = txt
        t = re.sub(r'(габариты_mm:\s*\n\s+l:)\s*\S+', r'\g<1> %s' % l, t, count=1)
        t = re.sub(r'(\n\s+w:)\s*\S+', r'\g<1> %s' % w, t, count=1)
        t = re.sub(r'(\n\s+h:)\s*\S+', r'\g<1> %s' % h, t, count=1)
        t = re.sub(r'(  масса_kg:)\s*\S+', r'\g<1> %s' % fmt(massa_new), t, count=1)
        if new_share:
            t = re.sub(r'(  доля_массы_родителя:)\s*\S+', r'\g<1> %s' % new_share, t, count=1)
        if pin is not None:
            t = re.sub(r'^(\s+pin_count:)\s*\S+', r'\g<1> %s' % pin, t, count=1, flags=re.M)
        if old_mat != mat:
            t = re.sub(r'(\n  - часть: %s\n    материал: )\S+' % re.escape(item_id), r'\g<1>%s' % mat, t, count=1)
        t = re.sub(r'^источник_разбора:.*$', 'источник_разбора: веб-верификация', t, count=1, flags=re.M)
        t = re.sub(r'^дата_обновления:.*$', 'дата_обновления: %s' % date, t, count=1, flags=re.M)
        if re.search(r'^источник_url:', t, re.M):
            t = re.sub(r'^источник_url:.*$', 'источник_url: %s' % url, t, count=1, flags=re.M)
        else:
            t = re.sub(r'^источник_разбора: веб-верификация$', 'источник_разбора: веб-верификация\nисточник_url: %s\nисточник_дата: %s' % (url, date), t, count=1, flags=re.M)
        if not re.search(r'^источник_дата:', t, re.M):
            t = re.sub(r'^(источник_url: .+)$', r'\1\nисточник_дата: %s' % date, t, count=1, flags=re.M)
        t = re.sub(r'(## Описание\n\n).*?(\n\nРодитель:)', r'\g<1>%s\g<2>' % desc, t, count=1, flags=re.S)
        t = re.sub(r'\| масса \| \S+ \| kg \|[^|]*\|', '| масса | %s | kg | %s |' % (fmt(massa_new), ref), t, count=1)
        if new_share:
            t = re.sub(r'\| доля массы родителя \| \S+ \| — \| canon \|', '| доля массы родителя | %s | — | расчёт (масса / номинал родителя) |' % new_share, t, count=1)
        t = re.sub(r'\| габариты \(Д×Ш×В\) \| \S+ \| mm \|[^|]*\|', '| габариты (Д×Ш×В) | %s×%s×%s | mm | %s |' % (l, w, h, ref), t, count=1)
        t = re.sub(r'\| материал \| [^\n]*', '| материал | %s | — | %s |' % (mat, ref), t, count=1)
        t = re.sub(r'(## Принцип работы\n\n)[^\n]*', r'\g<1>%s' % principle, t, count=1)
        if old_mat and old_mat != mat:
            pat = r'- `%s` → \[[^\]]+\]\([^)]+\)[^\n]*' % re.escape(old_mat)
            repl = '- `%s` → [`%s.md`](../../../../материалы/%s.md) — %s' % (mat, mat, mat, MAT_NOTES.get(mat, mat))
            t2, n = re.subn(pat, repl, t, count=1)
            t = t2 if n else t
        src_line = '- %s — %s (обращение %s)' % (ref, url, date)
        if src_line not in t:
            if '- Канон:' in t:
                t = t.replace('- Канон:', src_line + '\n- Канон:', 1)
            else:
                t = t.replace('- Материалы:', src_line + '\n- Материалы:', 1)
        open(f, 'w', encoding='utf-8').write(t)
        changed.append('%s → %s×%s×%s, %s кг, %s' % (item_id, l, w, h, fmt(massa_new), mat))
    return changed, skipped


def report(changed, skipped):
    print('CHANGED: %d' % len(changed))
    for c in changed:
        print('  ✓', c)
    print('SKIPPED: %d' % len(skipped))
    for s in skipped:
        print('  -', s)


if __name__ == '__main__':
    print('Модуль fix_f25 — импортируйте apply_batch/check_unique_dims в батч-скрипте.')
