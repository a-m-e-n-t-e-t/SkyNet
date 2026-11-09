#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v9.61 Фаза 3a: Создать 12 canonical файлов веществ.

Эти 12 файлов — canonical-основа для мигрирующих закупочных изделий.
Все 12 — это чистые вещества (полимеры, химические соединения, элементы),
не закупочные sub-assemblies.

Список:
1. uhmwpe — Ultra-High Molecular Weight Polyethylene
2. aramid — aromatic polyamide (класс для Kevlar, Twaron, Nomex)
3. pet — Polyethylene terephthalate
4. pvf — Polyvinyl fluoride (класс для Tedlar)
5. paraffin — смесь алканов C20-C40
6. cacl2_6h2o — хлорид кальция гексагидрат
7. dcpd — dicyclopentadiene (C10H12)
8. cnt — carbon nanotubes (аллотроп углерода, класс для SWCNT/MWCNT)
9. sio2_amorphous — аморфный диоксид кремния
10. silane — силаны (класс для silane coupling agents)
11. uo2 — диоксид урана
12. silver — серебро (Ag)
"""
import sys
from pathlib import Path
from datetime import date

sys.path.insert(0, '/home/z/my-project/SkyNet/scripts')
from _helpers import write_atomic

REPO = Path('/home/z/my-project/SkyNet')
MAT_DIR = REPO / 'реальные данные' / 'материалы'
TODAY = date.today().isoformat()


def make_material(filename: str, mat_id: str, klass: str, composition: str,
                    crystal: str, description: str, source_url: str,
                    density: float = None, mp: float = None) -> str:
    """Создать минимальный canonical материал."""
    density_line = f'  плотность_kg_m3: {density}\n' if density else '  плотность_kg_m3: null\n'
    mp_line = f'  температура_плавления_C: {mp}\n' if mp else '  температура_плавления_C: null\n'
    return f"""---
применяется_в_изделиях_счёт: 0
id: material_{mat_id}
псевдонимы: []
канонический_id: material_{mat_id}
тип: материал
класс: {klass}
химический_состав: '{composition}'
кристаллическая_структура: '{crystal}'
вариант_структуры: ''
оптимальная_структура:
  структура: ''
  обоснование_выбора: '{description}'
  применение_по_умолчанию: ''
  источник_обоснования: web_search
варианты_по_применению: {{}}
сравнение_структур: {{}}
исследовательская_группа: null
стандарты: []
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
источник: web_search
источник_url: {source_url}
источник_дата: {TODAY}
источник_разбора: v9.61 canonical
ии_перепроектирован:
  статус: false
  верификация: []
основные:
{density_line}{mp_line}  прочность_МПа: null
  предел_текучести_МПа: null
  модуль_упругости_ГПа: null
  коэффициент_Пуассона: null
  ударная_вязкость_Дж_см2: null
  усталостная_прочность_МПа: null
  теплопроводность_W_mK: null
  теплоёмкость_J_kgK: null
  коэффициент_термического_расширения_1_K: null
  электропроводность_S_m: null
наследуемые: {{}}
дополнительные: {{}}
дата_создания: {TODAY}
дата_обновления: {TODAY}
---
# Материал: {mat_id}

## Описание

{description}

## Химический состав

{composition}

## Кристаллическая структура

{crystal}

## Источники

- {source_url}
"""


MATERIALS = [
    # 1. UHMWPE
    ('uhmwpe.md', 'uhmwpe', 'полимер',
     '(—CH₂—CH₂—)ₙ, Mw >3.5×10⁶ г/моль (Ultra-High Molecular Weight Polyethylene)',
     'полукристаллический (орторомбическая элементарная ячейка)',
     'UHMWPE — полиэтилен сверхвысокой молекулярной массы (Mw >3.5 млн г/моль). Полимер с фиксированной химической структурой (—CH₂—CH₂—)ₙ, но экстремально высокой молекулярной массой. Бренды Dyneema® (DSM) и Spectra® (Honeywell) — это формы UHMWPE, производимые гель-прядением. Сам UHMWPE как вещество описывается этим canonical-файлом.',
     'https://en.wikipedia.org/wiki/Ultra-high-molecular-weight_polyethylene',
     930, 135),

    # 2. Aramid
    ('aramid.md', 'aramid', 'полимер',
     '(—NH—C₆H₄—NH—CO—C₆H₄—CO—)ₙ — ароматический полиамид (aramid)',
     'полукристаллический (водородные связи между цепями)',
     'Арамид (aromatic polyamide) — класс полимеров с ароматическими кольцами в основной цепи и амидными связями. Включает para-aramid (Kevlar®, Twaron®) и meta-aramid (Nomex®). Бренды — закупочные изделия; canonical-класс aramid описывает химию.',
     'https://en.wikipedia.org/wiki/Aramid',
     1440, None),

    # 3. PET
    ('pet.md', 'pet', 'полимер',
     '(—C₂H₄—O—CO—C₆H₄—CO—O—)ₙ — polyethylene terephthalate',
     'полукристаллический (триклинная ячейка)',
     'PET — полиэтилентерефталат, термопластичный полиэфир. Mylar® (BoPET film), Dacron® (волокно), PET-бутылки — формы/бренды PET. Canonical pet описывает химию вещества.',
     'https://en.wikipedia.org/wiki/Polyethylene_terephthalate',
     1380, 250),

    # 4. PVF
    ('pvf.md', 'pvf', 'полимер',
     '(—CH₂—CHF—)ₙ — polyvinyl fluoride',
     'полукристаллический',
     'PVF — поливинилфторид, фторполимер с одним атомом F на мономерное звено. Tedlar® (DuPont) — плёнка PVF, используемая в PV-модулях как backsheet. Canonical pvf описывает химию.',
     'https://en.wikipedia.org/wiki/Polyvinyl_fluoride',
     1380, 190),

    # 5. Paraffin
    ('paraffin.md', 'paraffin', 'полимер',
     'Смесь нормальных алканов C₂₀H₄₂–C₄₀H₈₂ (твёрдый парафин)',
     'поликристаллический (орторомбическая)',
     'Парафин — смесь нормальных алканов C20-C40, твёрдое при комнатной температуре. Используется как Phase Change Material (PCM) с температурой плавления 20-60°C. Rubitherm RT35 — бренд-specific состав парафина с Tпл=35°C.',
     'https://en.wikipedia.org/wiki/Paraffin_wax',
     900, 50),

    # 6. CaCl2·6H2O
    ('cacl2_6h2o.md', 'cacl2_6h2o', 'неорганическая_соль',
     'CaCl₂·6H₂O — гексагидрат хлорида кальция',
     'гексагональная',
     'CaCl₂·6H₂O — неорганическое соединение, Phase Change Material с Tпл=29°C (latent heat 190 Дж/г). Используется в PCM-композитах с нуклеатором SrCl₂·6H₂O.',
     'https://en.wikipedia.org/wiki/Calcium_chloride',
     1710, 29),

    # 7. DCPD
    ('dcpd.md', 'dcpd', 'полимер',
     'C₁₀H₁₂ — dicyclopentadiene (DCPD)',
     'молекулярный кристалл',
     'DCPD — дициклопентадиен, органическое соединение C10H12. Используется для самовосстанавливающихся микрокапсул (rupture → полимеризация через катализатор Граббса).',
     'https://en.wikipedia.org/wiki/Dicyclopentadiene',
     980, 32),

    # 8. CNT
    ('cnt.md', 'cnt', 'углерод',
     'C (sp²/sp³) — carbon nanotubes (аллотроп углерода)',
     'свернутый графеновый лист (цилиндр)',
     'CNT — углеродные нанотрубки, аллотропная модификация углерода (как графит, алмаз, графен). Бывают SWCNT (single-wall), MWCNT (multi-wall), super-aligned forest (SACNT). Бренды/формы (CoMoCAT, SuperPureTubes, SACNT-SF) — закупочные изделия. Canonical cnt описывает вещество/класс.',
     'https://en.wikipedia.org/wiki/Carbon_nanotube',
     1330, None),

    # 9. SiO2 amorphous
    ('sio2_amorphous.md', 'sio2_amorphous', 'керамика',
     'SiO₂ (аморфный, некристаллический)',
     'аморфный (стекловидный)',
     'Аморфный SiO₂ — диоксид кремния без кристаллической решётки. Основа для аэрогелей (Aspen Pyrogel, Spaceloft), стекловолокна (E-glass), кварцевого стекла. Canonical sio2_amorphous описывает вещество; бренды аэрогелей и стёкол — закупочные sub-assemblies.',
     'https://en.wikipedia.org/wiki/Silicon_dioxide',
     2200, None),

    # 10. Silane
    ('silane.md', 'silane', 'полимер',
     'SiH₄ (моносилан) и производные RₙSiX₄₋ₙ (silane coupling agents)',
     'газ (SiH₄) / жидкость (organic silanes)',
     'Silane — класс кремний-органических соединений с формулой RₙSiX₄₋ₙ. SiH₄ — моносилан (газ). Silane coupling agents (KH-550, vinyl-silane, Dow Corning Z-6040) — производные для адгезии полимер-металл. Брендовые силан-праймеры — закупочные изделия.',
     'https://en.wikipedia.org/wiki/Silane',
     None, -185),

    # 11. UO2
    ('uo2.md', 'uo2', 'керамика',
     'UO₂ — диоксид урана (uranium dioxide)',
     'кубическая (флюорит CaF₂-тип)',
     'UO₂ — диоксид урана, керамическое ядерное топливо. Pellets (топливные таблетки) — форма поставки, но само вещество UO₂ описывается этим canonical-файлом.',
     'https://en.wikipedia.org/wiki/Uranium_dioxide',
     10970, 2865),

    # 12. Silver
    ('silver.md', 'silver', 'металл',
     'Ag ≥99.9% (серебро)',
     'ГЦК (FCC)',
     'Ag — серебро, химический элемент. Чистое вещество. Ag-пена (metallic foam), Ag-покрытие — формы вещества; canonical silver описывает элемент.',
     'https://en.wikipedia.org/wiki/Silver',
     10490, 962),
]


def main():
    print("=== v9.61 Фаза 3a: Создание 12 canonical файлов веществ ===\n")
    created = 0
    for entry in MATERIALS:
        filename = entry[0]
        fpath = MAT_DIR / filename
        if fpath.exists():
            print(f"  SKIP: {filename} уже существует")
            continue
        content = make_material(*entry)
        write_atomic(fpath, content)
        created += 1
        print(f"  OK: {filename} (класс: {entry[2]})")
    print(f"\nСоздано: {created}")


if __name__ == '__main__':
    main()
