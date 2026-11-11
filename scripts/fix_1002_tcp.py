# -*- coding: utf-8 -*-
"""F27e #1002: добавление технологии_частей для izdelie_tcp (родитель + 4 части).
Паттерн #976/#979: блок вставляется перед якорем scaling_type:.
Технологии обоснованы web_search (Haines 2014, Mirvakili 2014 — MIT):
скручивание нейлоновой мононити DC-мотором до самонавивки коила + отжиг
термофиксации (нейлон 120-150 °C; UHMWPE 130 °C — Man 2023).
"""
import pathlib
import sys

BASE = pathlib.Path('реальные данные/изделия/приводная_система/tcp')

TECH_BLOCKS = {
    '_index.md': (
        "# F27e: технологии обработки частей TCP-актуатора — спиральная навивка коила\n"
        "# (Haines 2014 / Mirvakili 2014 MIT: скручивание нейлоновой мононити DC-мотором\n"
        "# до порога самонавивки + отжиг термофиксации 120-150 °C), ЧПУ-точение алюминиевого\n"
        "# рукава, литьё под давлением TPI-выводов, ЧПУ-фрезеровка кронштейнов\n"
        "технологии_частей:\n"
        "  - часть: часть_tcp_core\n"
        "    технология: spiralnaya_navivka\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: neilon_6_66\n"
        "        роль: обрабатываемый\n"
        "  - часть: часть_tcp_housing\n"
        "    технология: tokarnaya_obrabotka_chpu\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: al_6061-t6\n"
        "        роль: обрабатываемый\n"
        "  - часть: часть_tcp_connectors\n"
        "    технология: lite_pod_davleniem\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: poliimid\n"
        "        роль: обрабатываемый\n"
        "  - часть: часть_tcp_mounting\n"
        "    технология: frezervanie_chpu\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: al_6061-t6\n"
        "        роль: обрабатываемый\n"
    ),
    'часть_tcp_core/_index.md': (
        "# F27e: TCP-коил — скручивание нейлоновой мононити DC-мотором до порога\n"
        "# самонавивки с последующей термофиксацией формы при 120-150 °C\n"
        "# (Haines 2014, Science 347; Mirvakili 2014 — silver painted nylon 6,6)\n"
        "технологии_частей:\n"
        "  - часть: часть_tcp_core\n"
        "    технология: spiralnaya_navivka\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: neilon_6_66\n"
        "        роль: обрабатываемый\n"
    ),
    'часть_tcp_housing/_index.md': (
        "# F27e: защитный рукав TCP-актуатора — ЧПУ-точение алюминиевой трубки\n"
        "# 173x6x6 мм из прутка 6061-T6\n"
        "технологии_частей:\n"
        "  - часть: часть_tcp_housing\n"
        "    технология: tokarnaya_obrabotka_chpu\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: al_6061-t6\n"
        "        роль: обрабатываемый\n"
    ),
    'часть_tcp_connectors/_index.md': (
        "# F27e: электрические выводы джоулева нагрева — литьё под давлением\n"
        "# термопластичного полиимида (TPI, AURUM-класс)\n"
        "технологии_частей:\n"
        "  - часть: часть_tcp_connectors\n"
        "    технология: lite_pod_davleniem\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: poliimid\n"
        "        роль: обрабатываемый\n"
    ),
    'часть_tcp_mounting/_index.md': (
        "# F27e: торцевые кронштейны крепления TCP-актуатора — ЧПУ-фрезерование\n"
        "# из плиты 6061-T6\n"
        "технологии_частей:\n"
        "  - часть: часть_tcp_mounting\n"
        "    технология: frezervanie_chpu\n"
        "    доля_использования: 1.0\n"
        "    материалы_для_процесса:\n"
        "      - материал: al_6061-t6\n"
        "        роль: обрабатываемый\n"
    ),
}


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
    # 1. Родитель: вставка перед scaling_type (сразу после доля_массы: 0.27)
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
    for rel in TECH_BLOCKS:
        p = BASE / rel
        txt = p.read_text()
        if 'дата_обновления: 2026-11-08' in txt:
            p.write_text(txt.replace('дата_обновления: 2026-11-08', 'дата_обновления: 2026-11-10'))
            print(f'  DATE {rel}')
    print('DONE')


if __name__ == '__main__':
    main()
