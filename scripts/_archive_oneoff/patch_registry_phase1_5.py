#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ФАЗА 1.5: Ручная правка 8 закупочных компонентов в _decomp_registry.yaml.

Кандидаты из auto-классификации (PART_DATA.материал не в canonical):

  YSZ_электролит         → alias: 8ysz (canonical файл существует)
  rubber_skin             → создать canonical: полиуретан (T-600 skin material)
  анод_Ni_Cermet          → создать canonical: ni_cermet (Ni-YSZ cermet для SOFC)
  катод_LSM               → создать canonical: lsm_cathode (Lanthanum Strontium Manganite)
  керамические_слои       → alias: batio3 (canonical файл существует)
  пины_BGA                → alias: copper (canonical файл существует)
  разъёмы                 → alias: copper (canonical файл существует)
  теплораспределитель     → alias: copper (canonical файл существует)

Все 8 — на самом деле АТОМАРНЫЕ ЧАСТИ с canonical материалом (не закупочные компоненты).
Только `rubber_skin`, `анод_Ni_Cermet`, `катод_LSM` требуют создания canonical файлов.

Этот скрипт:
1. Загружает _decomp_registry.yaml
2. Для 5 атомарных частей с alias-материалом — переписывает is_purchased=false,
   materials=[{материал: <canonical_alias>, ...}], убирает candidate_material/note
3. Для 3 атомарных частей, требующих canonical — помечает как 'needs_canonical_file',
   сохраняя is_purchased=true до создания файла
4. Сохраняет обновлённый реестр
"""
import sys
import yaml
from pathlib import Path

REPO = Path('/home/z/my-project/SkyNet')
REGISTRY_PATH = REPO / 'scripts' / '_decomp_registry.yaml'

# Соответствие: подтип → canonical материал (alias)
ALIAS_MAP = {
    'YSZ_электролит':         '8ysz',     # canonical файл 8ysz.md существует
    'керамические_слои':      'batio3',   # canonical файл batio3.md существует
    'пины_BGA':               'copper',   # canonical файл copper.md существует
    'разъёмы':                'copper',
    'теплораспределитель':    'copper',
}

# Подтипы, требующие СОЗДАНИЯ canonical файла
NEEDS_CANONICAL_FILE = {
    'rubber_skin':    'полиуретан',       # polyurethane для T-600 skin
    'анод_Ni_Cermet': 'ni_cermet',        # Ni-YSZ cermet для SOFC anode
    'катод_LSM':      'lsm_cathode',      # Lanthanum Strontium Manganite для SOFC cathode
}


def main():
    print("=== Фаза 1.5: Ручная правка 8 закупочных компонентов ===\n")
    data = yaml.safe_load(REGISTRY_PATH.read_text(encoding='utf-8'))
    reg = data['decomp_registry']

    # Применить alias-замены
    for subtype, canonical_alias in ALIAS_MAP.items():
        if subtype not in reg:
            print(f"  WARN: {subtype} не найден в реестре")
            continue
        entry = reg[subtype]
        entry['is_atomic'] = True
        entry['is_purchased'] = False  # это атомарная часть, не закупочный компонент
        entry['materials'] = [{
            'материал': canonical_alias,
            'форма': None,  # нужно заполнить в canonical файле
            'доля': 1.0,
        }]
        entry.pop('candidate_material', None)
        entry.pop('note', None)
        entry.pop('materials_source', None)
        print(f"  OK alias: {subtype} → {canonical_alias}")

    # Пометить как needs_canonical_file
    for subtype, canonical_id in NEEDS_CANONICAL_FILE.items():
        if subtype not in reg:
            print(f"  WARN: {subtype} не найден в реестре")
            continue
        entry = reg[subtype]
        entry['is_atomic'] = True
        entry['is_purchased'] = True  # остаётся purchased, пока нет canonical файла
        entry['needs_canonical_file'] = canonical_id
        entry['materials'] = []  # BOM не определён, пока canonical файл не создан
        # Обновить note
        entry['note'] = (f'Требуется создать canonical файл материалы/{canonical_id}.md '
                         f'(is_purchased=true до создания). После создания — '
                         f'переписать is_purchased=false и заполнить materials.')
        entry.pop('candidate_material', None)
        entry.pop('materials_source', None)
        print(f"  OK needs_canonical: {subtype} → {canonical_id}.md (создать)")

    # Сохранить
    output = yaml.safe_dump(data, allow_unicode=True, default_flow_style=False,
                            sort_keys=True, width=120)
    # Сохранить с заголовком
    header = """# SkyNet Decomposition Registry — v9.60
# ============================================================================
# Рекурсивный реестр декомпозиции. Источник правды для:
# - scripts/recursive_decompose.py (canonical генератор, Фаза 3)
# - validate_decomposition.py:check_F35 (новая метрика)
#
# Структура (по варианту A2 + D4-β):
#   <subtype>:
#     is_atomic: bool        # true = лист структурной декомпозиции (часть/компонент)
#     is_purchased: bool     # true = закупочный узел (компонент), имеет BOM материалов
#                            # false = атомарная часть (canonical material)
#     children:              # опц., для is_atomic=false
#       - suffix: <str>     # добавляется к <parent_id>_ для формирования id ребёнка
#         подтип_части: <str>  # должен быть ключом в этом реестре ИЛИ canonical материалом
#         масса_kg: <float>
#         доля_массы: <float>
#     materials:             # опц., для is_atomic=true (BOM компонента или материала части)
#       - материал: <canonical_id>
#         форма: <form_key>   # ключ из материал.варианты_по_применению
#         доля: <float>       # 0..1, Σ ≤ 1.0
#     needs_canonical_file: <id>  # опц., для is_purchased=true: canonical материал нужно создать
#
# Критерий остановки декомпозиции:
#   1. STOP_MATERIAL — подтип является canonical материалом (файл в материалы/)
#   2. STOP_ATOMIC — подтип в реестре с is_atomic=true → записать BOM, закончить
#   3. STOP_UNKNOWN — подтипа нет в реестре → F34 нарушение
#   4. RECURSE — подтип в реестре с is_atomic=false → рекурсивно для каждого child
#
# Фаза 1.5 (этот коммит): 8 закупочных компонентов классифицированы вручную:
#   - 5 атомарных частей с alias-материалом (YSZ→8ysz, batio3, copper×3)
#   - 3 требуют создания canonical файла (полиуретан, ni_cermet, lsm_cathode)
#
# Сгенерировано: scripts/build_decomp_registry.py + scripts/_archive_oneoff/patch_registry_phase1_5.py
"""
    REGISTRY_PATH.write_text(header + output, encoding='utf-8')
    print(f"\nРеестр обновлён: {REGISTRY_PATH.relative_to(REPO)}")

    # Финальная статистика
    stats = {'structural': 0, 'atomic_part': 0, 'purchased_component': 0, 'needs_canonical': 0}
    for k, v in reg.items():
        if v.get('is_atomic') is None:
            continue  # unknown
        if not v.get('is_atomic'):
            stats['structural'] += 1
        elif v.get('is_purchased'):
            if v.get('needs_canonical_file'):
                stats['needs_canonical'] += 1
            else:
                stats['purchased_component'] += 1
        else:
            stats['atomic_part'] += 1
    print(f"\nФинальная статистика:")
    for k, v in stats.items():
        print(f"  {k}: {v}")


if __name__ == '__main__':
    main()
