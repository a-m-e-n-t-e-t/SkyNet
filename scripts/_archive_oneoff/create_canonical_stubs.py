#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ФАЗА 2.5b: Создать canonical-файлы для 35 non-canonical материалов из DECOMP_TEMPLATES.

Каждый файл — минимальный canonical-материал с:
- id, канонический_id (если alias), тип: материал
- класс, химический_состав (где возможно)
- основные: плотность (если известна)
- источник_url (где возможно)
- дата_создания/обновления

Цель: устранить 35 F27b нарушений (битые ссылки) одним батчем.
Файлы создаются как STUB (статус: заглушка) для последующего наполнения
через cron-агента (verify_decomposition.yml).

Прецедент: в коммите 8555c09 я уже создавал canonical-файлы
(aluminum_6063.md, stainless_steel_mesh.md — последний потом удалён в f2e7512).
"""
import sys
import os
import re
from pathlib import Path

sys.path.insert(0, '/home/z/my-project/SkyNet/scripts')
from _helpers import write_atomic

REPO = Path('/home/z/my-project/SkyNet')
MATERIALS_DIR = REPO / 'реальные данные' / 'материалы'

# ============================================================================
# 35 материалов — структурированный реестр
# ============================================================================
# Для каждого: (filename, id, класс, химический_состав, описание, источник_url)
# Если известен canonical alias — указывается канонический_id.

MATERIALS = [
    # === Топливные элементы ===
    ('ni_ysz_cermet.md', 'ni_ysz_cermet', 'керамика_металл',
     'Ni (40 vol%) + YSZ (60 vol%) cermet — анод SOFC',
     'Никель-иттрий-стабилизированный диоксид циркония кермет — стандартный анод твердооксидного топливного элемента (SOFC).',
     'https://en.wikipedia.org/wiki/Solid_oxide_fuel_cell'),
    ('ysz_electrolyte.md', 'ysz_electrolyte', 'керамика',
     'ZrO₂ + 8 mol% Y₂O₃ (8YSZ) — твёрдый электролит SOFC',
     'Иттрий-стабилизированный диоксид циркония — кислород-ионный проводник при 800°C, стандартный электролит SOFC.',
     'https://en.wikipedia.org/wiki/Yttria-stabilized_zirconia'),
    ('nafion_117.md', 'nafion_117', 'полимер',
     'Перфторсульфоновая иономерная мембрана (Nafion 117, DuPont)',
     'Nafion 117 — стандартная протон-обменная мембрана для PEM-топливных элементов, толщина 183 мкм.',
     'https://www.chemours.com/nafion'),
    ('pt_carbon.md', 'pt_carbon', 'композит',
     'Pt (20-40 мас.%) на углеродной подложке (Vulcan XC-72)',
     'Платина на углероде — стандартный катализатор для PEM-топливных элементов.',
     'https://en.wikipedia.org/wiki/Platinum_on_carbon'),
    ('carbon_paper.md', 'carbon_paper', 'углерод',
     'Toray/Carbon Paper TGP-H-060 — газодиффузионный слой',
     'Углеродная бумага для газодиффузионного слоя (GDL) топливных элементов.',
     'https://www.fuelcellstore.com/toray-carbon-paper'),

    # === Радиоизотопные генераторы ===
    ('pu238_oxide.md', 'pu238_oxide', 'керамика',
     '²³⁸PuO₂ (плутоний-238 диоксид) — радиоизотопный источник тепла',
     'Диоксид плутония-238 — стандартный теплоисточник для РИТЭГ (RTG), T½=87.7 лет, удельная мощность 0.56 Вт/г.',
     'https://en.wikipedia.org/wiki/Plutonium-238'),
    ('titanium_alloy.md', 'titanium_alloy', 'металл',
     'Ti-6Al-4V (Grade 5) — корпус РИТЭГ',
     'Титановый сплав Ti-6Al-4V — стандартный материал корпуса космических РИТЭГ.',
     'https://en.wikipedia.org/wiki/Ti-6Al-4V'),
    ('aerogel.md', 'aerogel', 'композит',
     'SiO₂ аэрогель — термоизоляция',
     'Кремнезёмный аэрогель — лучшая в мире твёрдая термоизоляция, λ=0.013 Вт/м·К.',
     'https://en.wikipedia.org/wiki/Aerogel'),
    ('copper_wire.md', 'copper_wire', 'металл',
     'Cu провод (AWG 24-30) с эмалевой изоляцией',
     'Медный эмальпровод — обмотки альтернаторов, электромагнитов.',
     'https://en.wikipedia.org/wiki/Magnet_wire'),

    # === Суперконденсаторы ===
    ('activated_carbon.md', 'activated_carbon', 'углерод',
     'Активированный уголь (BET 1500-2000 m²/g) — электрод суперконденсатора',
     'Активированный уголь — стандартный электродный материал для EDLC суперконденсаторов.',
     'https://en.wikipedia.org/wiki/Activated_carbon'),

    # === Литий-ионные ===
    ('lipf6_ec_dmc.md', 'lipf6_ec_dmc', 'жидкость',
     'LiPF₆ 1M в EC:DMC (1:1) — стандартный электролит Li-ion',
     'Стандартный органический электролит для литий-ионных аккумуляторов.',
     'https://en.wikipedia.org/wiki/Lithium_hexafluorophosphate'),
    ('pe_pp.md', 'pe_pp', 'полимер',
     'PE/PP многослойный сепаратор (Celgard)',
     'Полиэтилен/полипропиленовый микропористый сепаратор для Li-ion батарей.',
     'https://www.celgard.com'),
    ('pe_separator.md', 'pe_separator', 'полимер',
     'PE микропористый сепаратор свинцово-кислотных батарей',
     'Полиэтиленовый сепаратор для свинцово-кислотных аккумуляторов (AGM альтернатива).',
     'https://en.wikipedia.org/wiki/VRLA_battery'),

    # === Бетавольтаики ===
    ('ni63_metal.md', 'ni63_metal', 'металл',
     '⁶³Ni металлическая фольга — бета-источник',
     'Никель-63 — бета-излучатель для бетавольтаических генераторов, T½=100.2 года, Eβ_max=66.9 кэВ.',
     'https://en.wikipedia.org/wiki/Nickel-63'),
    ('epoxy.md', 'epoxy', 'полимер',
     'Эпоксидная смола (DGEBA) — инкапсулянт',
     'Эпоксидная смола — стандартный инкапсулянт для электроники, бета-источников.',
     'https://en.wikipedia.org/wiki/Epoxy'),
    ('tritium_gas.md', 'tritium_gas', 'газ',
     'T₂ (тритий) газ под давлением — бета-источник',
     'Тритий — радиоактивный изотоп водорода, T½=12.3 года, бета-излучатель для бетавольтаиков.',
     'https://en.wikipedia.org/wiki/Tritium'),

    # === Am-241 ===
    ('am241_oxide.md', 'am241_oxide', 'керамика',
     '²⁴¹AmO₂ — америций-241 диоксид',
     'Диоксид америция-241 — теплоисточник для космических РИТЭГ, T½=432.2 года.',
     'https://en.wikipedia.org/wiki/Americium-241'),
    ('tungsten_alloy.md', 'tungsten_alloy', 'металл',
     'W-Ni-Fe (W 90-97%) — тяжёлый сплав для радиационной защиты',
     'Вольфрамовый тяжёлый сплав — радиационная защита для америциевых РИТЭГ.',
     'https://en.wikipedia.org/wiki/Tungsten_heavy_alloy'),

    # === Фотомодули ===
    ('monocrystalline_si.md', 'monocrystalline_si', 'полупроводник',
     'Si монокристалл (Czochralski) — фотоэлектрический преобразователь',
     'Монокристаллический кремний — стандартный материал солнечных ячеек (η=22-26%).',
     'https://en.wikipedia.org/wiki/Monocrystalline_silicon'),
    ('eva.md', 'eva', 'полимер',
     'Этилен-винилацетат (EVA) — инкапсулянт PV-модулей',
     'EVA — стандартный инкапсулянт для фотоэлектрических модулей.',
     'https://en.wikipedia.org/wiki/Ethylene-vinyl_acetate'),

    # === Микрореактор ===
    ('uo2_pellets.md', 'uo2_pellets', 'керамика',
     'UO₂ таблетки — ядерное топливо микро-реакторов',
     'Диоксид урана — стандартное ядерное топливо для микро-реакторов.',
     'https://en.wikipedia.org/wiki/Uranium_dioxide'),

    # === Генератор Маркса ===
    ('ceramic_capacitors.md', 'ceramic_capacitors', 'керамика',
     'Керамические конденсаторы (MLCC) для генератора Маркса',
     'MLCC-конденсаторы — стандартные для высоковольтных импульсных генераторов.',
     'https://en.wikipedia.org/wiki/Ceramic_capacitor'),
    ('tungsten_electrodes.md', 'tungsten_electrodes', 'металл',
     'W электроды — искровые промежутки',
     'Вольфрамовые электроды для искровых разрядников генератора Маркса.',
     'https://en.wikipedia.org/wiki/Tungsten'),

    # === Пельтье ===
    ('alumina.md', 'alumina', 'керамика',
     'Al₂O₃ (96%) — керамические пластины модуля Пельтье',
     'Оксид алюминия — стандартные керамические пластины для модулей Пельтье.',
     'https://en.wikipedia.org/wiki/Aluminium_oxide'),

    # === TPV ===
    ('gaSb.md', 'gaSb', 'полупроводник',
     'GaSb (галлий-антимонид) — фотоэлемент для TPV',
     'Галлий-антимонид — фотоэлектрический материал для термофотоэлектрических генераторов.',
     'https://en.wikipedia.org/wiki/Gallium_antimonide'),
    ('gold_coating.md', 'gold_coating', 'металл',
     'Au покрытие — отражатель TPV',
     'Золотое покрытие — высокоотражающий слой для TPV-генераторов.',
     'https://en.wikipedia.org/wiki/Gold'),

    # === Электромагнитный ускоритель ===
    ('aluminum_electrolytic.md', 'aluminum_electrolytic', 'электролит',
     'Al электролитический конденсатор — банк конденсаторов coilgun',
     'Алюминиевые электролитические конденсаторы — стандарт для банка конденсаторов электромагнитных ускорителей.',
     'https://en.wikipedia.org/wiki/Electrolytic_capacitor'),
    ('composite_material.md', 'composite_material', 'композит',
     'Композитный материал (углерод-волокно/эпоксид) — ствол coilgun',
     'Композитный материал — диэлектрический ствол для электромагнитных ускорителей.',
     'https://en.wikipedia.org/wiki/Composite_material'),

    # === Электромагнитная муфта ===
    ('steel_1045.md', 'steel_1045', 'металл',
     'Сталь 1045 (AISI) — ротор электромагнитной муфты',
     'Углеродистая сталь AISI 1045 — конструкционный материал ротора муфты.',
     'https://en.wikipedia.org/wiki/AISI_1045'),
    ('iron_powder.md', 'iron_powder', 'металл',
     'Fe порошок — рабочая среда электромагнитной муфты',
     'Железный порошок — магнитный наполнитель электромагнитных муфт.',
     'https://en.wikipedia.org/wiki/Iron_powder'),

    # === HTS подшипник ===
    ('ybco_bulk.md', 'ybco_bulk', 'керамика',
     'YBa₂Cu₃O₇₋ₓ (YBCO) — высокотемпературный сверхпроводник',
     'YBCO — сверхпроводник для HTS-подшипников, Tc=92 K, левитация при 77 K (LN₂).',
     'https://en.wikipedia.org/wiki/Yttrium_barium_copper_oxide'),

    # === Алюминиево-воздушный ТЭ ===
    ('aluminum_1100.md', 'aluminum_1100', 'металл',
     'Al 1100 (Al ≥99%) — анод алюминиево-воздушного ТЭ',
     'Алюминий 1100 — технически чистый алюминий для анода воздушно-алюминиевых ТЭ.',
     'https://en.wikipedia.org/wiki/1100_aluminium_alloy'),
    ('koh_aqueous.md', 'koh_aqueous', 'жидкость',
     'KOH водный раствор (4-6 M) — электролит Al-air ТЭ',
     'Гидроксид калия — щелочной электролит для алюминиево-воздушных ТЭ.',
     'https://en.wikipedia.org/wiki/Potassium_hydroxide'),

    # === Микро-ТЭЦ ===
    ('cast_iron.md', 'cast_iron', 'металл',
     'Серый чугун (EN-GJL-250) — блок цилиндров микро-ТЭЦ',
     'Серый чугун — стандартный материал блоков цилиндров двигателей внутреннего сгорания.',
     'https://en.wikipedia.org/wiki/Cast_iron'),

    # === Прочее (placeholder) ===
    ('generic_material.md', 'generic_material', 'неопределённый',
     'Шаблонный материал (placeholder)',
     'Шаблонный материал — должен быть заменён на canonical при декомпозиции.',
     None),
]


def make_material_file(filename: str, mat_id: str, klass: str,
                        composition: str, description: str, source_url) -> str:
    """Создать минимальный canonical-файл материала (stub для последующего наполнения)."""
    src_url_line = f'источник_url: {source_url}\n' if source_url else 'источник_url: null\n'
    return f"""---
применяется_в_изделиях_счёт: 0
id: material_{mat_id}
псевдонимы: []
канонический_id: material_{mat_id}
тип: материал
класс: {klass}
химический_состав: '{composition}'
кристаллическая_структура: ''
вариант_структуры: ''
оптимальная_структура:
  структура: ''
  обоснование_выбора: 'STUB — создано в v9.60 Фазе 2.5b для устранения битых ссылок DECOMP_TEMPLATES. Требует детального наполнения (cron-агент verify_decomposition.yml).'
  применение_по_умолчанию: ''
  источник_обоснования: web_search
варианты_по_применению: {{}}
сравнение_структур: {{}}
исследовательская_группа: null
стандарты: []
версия: реальная
статус_реальности: real
доступность: промышленный
статус: заглушка
источник: web_search
{src_url_line}источник_дата: 2026-11-09
источник_разбора: v9.60 stub
ии_перепроектирован:
  статус: false
  верификация: []
основные:
  плотность_kg_m3: null
  прочность_МПа: null
  предел_текучести_МПа: null
  модуль_упругости_ГПа: null
  коэффициент_Пуассона: null
  ударная_вязкость_Дж_см2: null
  усталостная_прочность_МПа: null
  температура_плавления_C: null
  теплопроводность_W_mK: null
  теплоёмкость_J_kgK: null
  коэффициент_термического_расширения_1_K: null
  электропроводность_S_m: null
наследуемые: {{}}
дополнительные: {{}}
дата_создания: 2026-11-09
дата_обновления: 2026-11-09
---
# Материал: {mat_id}

## Описание

{description}

**STUB:** Этот файл создан автоматически в v9.60 Фазе 2.5b для устранения 35 битых ссылок в `decompose_all_izdeliya.py:DECOMP_TEMPLATES`. Содержимое — минимальная заготовка. Требуется детальное наполнение (физические свойства, варианты_по_применению, стандарты) через cron-агента `verify_decomposition.yml`.

## Химический состав

{composition}

## Источники

"""
    + (f"- {source_url}\n" if source_url else "- Требуется web_search для подтверждения источника.\n")


def main():
    print("=== Фаза 2.5b: Создание 35 canonical stub-файлов материалов ===\n")
    created = 0
    skipped = 0
    for entry in MATERIALS:
        filename, mat_id, klass, composition, description, source_url = entry
        fpath = MATERIALS_DIR / filename
        if fpath.exists():
            skipped += 1
            continue
        content = make_material_file(filename, mat_id, klass, composition, description, source_url)
        write_atomic(fpath, content)
        created += 1
    print(f"Создано canonical stub-файлов: {created}")
    print(f"Пропущено (уже существуют): {skipped}")
    print(f"Всего в реестре: {len(MATERIALS)}")

    # Проверить: остались ли non-canonical в DECOMP_TEMPLATES?
    print("\nПроверка: non-canonical материалы в DECOMP_TEMPLATES после создания файлов:")
    import sys
    sys.path.insert(0, '/home/z/my-project/SkyNet/scripts')
    from decompose_all_izdeliya import DECOMP_TEMPLATES
    canonical = {f.stem for f in MATERIALS_DIR.glob('*.md')}
    remaining = set()
    for subtype, tmpl in DECOMP_TEMPLATES.items():
        for part_suffix, material_id, _ in tmpl.get('materials', []):
            if material_id not in canonical:
                remaining.add(material_id)
    if remaining:
        print(f"  Осталось non-canonical: {len(remaining)}")
        for m in sorted(remaining):
            print(f"    - {m}")
    else:
        print("  ✓ Все материалы в DECOMP_TEMPLATES теперь canonical!")


if __name__ == '__main__':
    main()
