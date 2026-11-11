# -*- coding: utf-8 -*-
"""F27e #1004: добавление технологии_частей для izdelie_bldc (родитель + 4 части).
Прецедент: bldc_enkoder (connectors→tokarnaya, housing/mounting→frezervanie).
core → shtampovka_listovaya (статорный пакет листов — по описанию части:
«Статорный пакет: листы электротехнической стали соединены неразъёмно»).
Материалы_для_процесса = материал из материалы_частей части.
"""
import pathlib
import sys

BASE = pathlib.Path('реальные данные/изделия/приводная_система/bldc')

TECH_BLOCKS = {
    '_index.md': (
        "# F27e: технологии обработки частей BLDC Ø45 (класс Maxon EC45) — штамповка\n"
        "# листов статорного пакета, ЧПУ-точение цилиндрического корпуса и разъёмов\n"
        "# MIL-DTL-38999, ЧПУ-фрезеровка кожуха и L-кронштейна\n"
        "технологии_частей:\n"
        "  - часть: часть_bldc_core\n"
        "    технология: shtampovka_listovaya\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: al_6061-t6\n"
        "        роль: обрабатываемый\n"
        "  - часть: часть_bldc_housing\n"
        "    технология: frezervanie_chpu\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: al_6061-t6\n"
        "        роль: обрабатываемый\n"
        "  - часть: часть_bldc_connectors\n"
        "    технология: tokarnaya_obrabotka_chpu\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: al_6061-t6\n"
        "        роль: обрабатываемый\n"
        "  - часть: часть_bldc_mounting\n"
        "    технология: frezervanie_chpu\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: al_6061-t6\n"
        "        роль: обрабатываемый\n"
    ),
    'часть_bldc_core/_index.md': (
        "# F27e: электромагнитное ядро BLDC — штамповка листов статорного пакета\n"
        "# (по описанию части: листы соединены неразъёмно — самосклейка/сварка/клёпка)\n"
        "технологии_частей:\n"
        "  - часть: часть_bldc_core\n"
        "    технология: shtampovka_listovaya\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: al_6061-t6\n"
        "        роль: обрабатываемый\n"
    ),
    'часть_bldc_housing/_index.md': (
        "# F27e: цилиндрический кожух BLDC Ø52×104 с монтажными лапами и крышкой —\n"
        "# ЧПУ-фрезерование (прецедент bldc_enkoder_housing)\n"
        "технологии_частей:\n"
        "  - часть: часть_bldc_housing\n"
        "    технология: frezervanie_chpu\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: al_6061-t6\n"
        "        роль: обрабатываемый\n"
    ),
    'часть_bldc_connectors/_index.md': (
        "# F27e: силовой разъём MIL-DTL-38999 Series III (размер 13, Ø19.8) —\n"
        "# ЧПУ-точение алюминиевого корпуса (прецедент bldc_enkoder_connectors)\n"
        "технологии_частей:\n"
        "  - часть: часть_bldc_connectors\n"
        "    технология: tokarnaya_obrabotka_chpu\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: al_6061-t6\n"
        "        роль: обрабатываемый\n"
    ),
    'часть_bldc_mounting/_index.md': (
        "# F27e: L-образный кронштейн-хомут 120×60×5 — ЧПУ-фрезерование с вырезами\n"
        "# облегчения (прецедент bldc_enkoder_mounting)\n"
        "технологии_частей:\n"
        "  - часть: часть_bldc_mounting\n"
        "    технология: frezervanie_chpu\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: al_6061-t6\n"
        "        роль: обрабатываемый\n"
    ),
}

DATE_OLD = {'_index.md': 'дата_обновления: 2026-11-08',
            'часть_bldc_core/_index.md': 'дата_обновления: 2026-11-08',
            'часть_bldc_housing/_index.md': 'дата_обновления: 2026-11-05',
            'часть_bldc_connectors/_index.md': 'дата_обновления: 2026-11-05',
            'часть_bldc_mounting/_index.md': 'дата_обновления: 2026-11-05'}


def rep(path: pathlib.Path, old: str, new: str, label: str) -> None:
    txt = path.read_text()
    if 'технологии_частей' in txt:
        print(f'  SKIP {label} (уже есть технологии_частей)')
        return
    if old not in txt:
        print(f'  FAIL {label}: якорь не найден!')
        sys.exit(1)
    path.write_text(txt.replace(old, new, 1))
    print(f'  OK   {label}')


def main() -> None:
    # 1. Родитель: вставка сразу после доля_массы: 0.27 (без пустой строки)
    parent = BASE / '_index.md'
    old_parent = "    материал: aluminum\n    доля_массы: 0.27\nscaling_type:"
    new_parent = (
        "    материал: aluminum\n    доля_массы: 0.27\n"
        + TECH_BLOCKS['_index.md']
        + "\nscaling_type:"
    )
    rep(parent, old_parent, new_parent, 'родитель')

    # 2. Части: вставка перед scaling_type (после пустой строки)
    for rel, block in TECH_BLOCKS.items():
        if rel == '_index.md':
            continue
        part = BASE / rel
        old = "\n\nscaling_type:"
        new = "\n" + block + "\nscaling_type:"
        rep(part, old, new, rel)

    # 3. дата_обновления у всех 5 файлов
    for rel, old_date in DATE_OLD.items():
        p = BASE / rel
        txt = p.read_text()
        if old_date in txt:
            p.write_text(txt.replace(old_date, 'дата_обновления: 2026-11-10'))
            print(f'  DATE {rel}: {old_date[-10:]} → 2026-11-10')
    print('DONE')


if __name__ == '__main__':
    main()
