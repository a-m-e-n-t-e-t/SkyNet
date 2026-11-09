---
id: material_pbte_teg
тип: материал
класс: полупроводник
химический_состав: 'Термоэлектрическая пара PbTe/TAGS-85: n-нога — легированный PbTe-сплав TE1010; p-нога — двухсегментная: PbSnTe-сплав TE2003 у горячего спая + TAGS-85 ((GeTe)0.85(AgSbTe2)0.15 — теллурид-антимонид-германий-серебро) у холодного спая'
кристаллическая_структура: поликристаллический
вариант_структуры: thermoelectric_legs
оптимальная_структура:
  структура: поликристаллический
  обоснование_выбора: "Среднетемпературный термоэлектрик оптимален для градиента RTG 525→~200 °C: PbTe даёт ZT~0.8–1.0 в диапазоне 400–600 °C, двухсегментная p-нога (TE2003+TAGS-85) выдерживает горячий спай ~525 °C и снижает термические напряжения; альтернатива Bi2Te3 не работает выше ~250 °C, скаттерудиты требуют 600 °C горячей стороны"
  применение_по_умолчанию: термопары_RTG
  источник_обоснования: web_search
варианты_по_применению:
  mmrtg_couple:
    марка: 'TE1010 (n, PbTe-сплав) + TE2003/TAGS-85 (p) — штатная пара MMRTG (Curiosity/Perseverance)'
    примечание: '768 пар MMRTG: 16 модулей × 48 пар (LPI/USRA 2016); p-нога сегментирована PbSnTe+TAGS-85'
  emmrtg_skutterudite:
    марка: 'eMMRTG: замена PbTe/TAGS на скаттерудиты — +25 % мощности на BOL при 600 °C горячей стороны'
    примечание: 'Woerner 2016 (J. Electron. Mater. 45:1278); требуется модифицированный GPHS-режим'
исследовательская_группа: 'E.A. Skrabek и D.S. Trimmer (Teledyne Energy Systems) — изобретатели TAGS-85 ((GeTe)0.85(AgSbTe2)0.15; CRC Handbook of Thermoelectrics, гл. 22), впервые применён в РИТЭГ SNAP-19 (Viking/Pioneer); программа SNAP (США) — первый космический РИТЭГ SNAP-3 (1961) на парах PbTe; Teledyne Energy Systems — изготовитель PbTe/TAGS-пар MMRTG (Curiosity/Perseverance) по контракту с Aerojet Rocketdyne'
стандарты: []
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
источник: web_search
источник_url: https://beyondnerva.wordpress.com/radioisotope-power-sources/mmrtg
источник_дата: 2026-11-06
источник_разбора: веб-верификация
ии_перепроектирован:
  статус: false
  верификация: []
основные:
  плотность_kg_m3: 8000
  прочность_МПа: {min: 25, max: 60, nominal: 40}
  предел_текучести_МПа: {min: null, max: null, nominal: null}
  модуль_упругости_ГПа: 55
  коэффициент_Пуассона: 0.25
  ударная_вязкость_Дж_см2: null
  усталостная_прочность_МПа: {min: null, max: null, nominal: null}
  температура_плавления_C: 924
  теплопроводность_W_mK: 2.2
  теплоёмкость_J_kgK: 160
  коэффициент_термического_расширения_1_K: 2.0e-5
  электропроводность_S_m: 1.0e5
дополнительные:
  цена_usd_kg: 500
  ZT_безразмерный: {min: 0.6, max: 1.0, nominal: 0.85}
  T_горячего_спая_max_C: 525
  рабочая_температура_C: {min: -60, max: 550}
  термоэдс_мкВ_K: {min: 150, max: 250, nominal: 200}
сравнение_структур: {}
дата_создания: 2026-11-06
дата_обновления: 2026-11-06
---
## Описание

Штатный термоэлектрический материал генераторов MMRTG (Curiosity, Perseverance): пара из n-ноги PbTe-сплава TE1010 и сегментированной p-ноги TE2003 (PbSnTe) + TAGS-85 — (GeTe)0.85(AgSbTe2)0.15 (Beyond NERVA; LPI/USRA: 16 модулей × 48 пар = 768 пар на генератор). Рабочее окно PbTe/TAGS ограничено горячей стороной ~525 °C — подъём до 600 °C возможен только на скаттерудитах (eMMRTG: +25 % мощности на BOL, Woerner et al., J. Electron. Mater. 45:1278). Bi₂Te₃ для этой задачи непригоден: его эффективность падает выше ~250 °C. Свойства: плотность 8000 кг/м³ (PbTe 8160, TAGS-85 ~7600 — составленная пара), λ 2.2 Вт/(м·К), плавление по PbTe 924 °C, ZT 0.6–1.0 в рабочем диапазоне (класс-типичные значения PbTe-термоэлектриков). Хрупкость (25–60 МПа) компенсируется пружинным прижатием модулей и сегментированием p-ноги, гасящим термические напряжения при циклике Марс/вакуум.

Историческая атрибуция: PbTe-пары — родоначальник космических РИТЭГ: первый РИТЭГ в космосе SNAP-3 (1961, 2.5 Вт эл.) использовал простые PbTe-сплавы обеих полярностей (обзор LaLonde/Pei/Snyder, Energy Environ. Sci. 2011; NASA SNAP-3). Материал TAGS-85 изобретён E.A. Скрабеком и D.S. Триммером на Teledyne Energy Systems (каноническая ссылка — CRC Handbook of Thermoelectrics, гл. 22) и впервые полетел в РИТЭГ SNAP-19 для Viking Lander и Pioneer (NTRS 19700067079, «SNAP 19 TAGS 85/2N»). Та же Teledyne Energy Systems по субподряду изготавливает PbTe-TAGS пары MMRTG — прямое продолжение технологии SNAP-19 (монография «The Technology of Discovery», Wiley 2023).

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| тип узла | материал | — | canon |


## Источники

- https://beyondnerva.wordpress.com/radioisotope-power-sources/mmrtg (композиция пар: n-TE1010 PbTe, p-TE2003 PbSnTe + TAGS-85; 8 рёбер Al6063; Haynes 25 лайнер)
- https://www.lpi.usra.edu/opag/meetings/feb2016/posters/1-MMRTG.PDF (16 ТЭ-модулей последовательно, 48 пар в модуле)
- https://ui.adsabs.harvard.edu/abs/2016JEMat..45.1278W/abstract (Woerner D. et al., 2016: eMMRTG — замена PbTe/TAGS, +25 % BOL)
- https://www.academia.edu/26535138/Increasing_the_Efficiency_of_the_Multi_mission_Radioisotope_Thermoelectric_Generator (горячая сторона PbTe/TAGS 525 °C → 600 °C на скаттерудитах)
- https://www.energy.gov/ne/articles/powering-curiosity-multi-mission-radioisotope-thermoelectric-generators (MMRTG: 8 GPHS, 4.8 кг PuO2, 110 Вт эл.)
- https://beyondnerva.wordpress.com/blog/page/2 (Skrabek & Trimmer, Teledyne Energy Systems — изобретатели TAGS-85; история TAGS/SNAP-19)
- https://ntrs.nasa.gov/citations/19700067079 (NASA NTRS, Linkous 1970: «SNAP 19 TAGS 85/2N» — первый полёт TAGS-85 в РИТЭГ для Viking Lander/Pioneer)
- https://en.wikipedia.org/wiki/Systems_for_Nuclear_Auxiliary_Power (SNAP-3 — первый РИТЭГ в космосе, 1961, 2.5 Вт, PbTe-пары)
- https://dokumen.pub/the-technology-of-discovery-radioisotope-thermoelectric-generators-and-thermoelectric-technologies-for-space-exploration-2022051673-2022051674-9781119811367-9781119811374-9781119811381.html («The Technology of Discovery», Wiley 2023: Teledyne Energy Systems — субподрядчик PbTe-TAGS пар SNAP-19 → MMRTG)
