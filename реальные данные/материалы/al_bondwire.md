---
применяется_в_изделиях_счёт: 0
id: material_al_bondwire
тип: материал
класс: металл
химический_состав: 'Al ≥99.99% (heavy bonding wire, класс Al-H11/Al-CR)'
кристаллическая_структура: поликристаллический
вариант_структуры: single_phase
оптимальная_структура:
  структура: поликристаллический
  обоснование_выбора: "Стандартный материал heavy wire bonds силовых полупроводников (MOSFET/IGBT): диаметры 125–500 мкм; испытанные классы Al-H11, Al-CR, AlX (Sc-легированный) в power-cycling исследованиях MOSFET-модулей (веб-верификация bond-iq/Inseto)"
  применение_по_умолчанию: проволочные_соединения_силовых_кристаллов
  источник_обоснования: web_search
варианты_по_применению: {}
исследовательская_группа: требует_верификации
стандарты: []
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
источник: web_search
источник_url: https://www.bond-iq.de/blog-publications/publication-007
источник_дата: 2026-11-05
источник_разбора: веб-верификация
ии_перепроектирован:
  статус: false
  верификация: []
основные:
  плотность_kg_m3: 2700
  прочность_МПа: {min: 30, max: 100, nominal: 60}
  предел_текучести_МПа: {min: 25, max: 80, nominal: 45}
  модуль_упругости_ГПа: 70
  коэффициент_Пуассона: 0.33
  ударная_вязкость_Дж_см2: null
  усталостная_прочность_МПа: {min: null, max: null, nominal: 25}
  температура_плавления_C: 660
  теплопроводность_W_mK: 237
  теплоёмкость_J_kgK: 900
  коэффициент_термического_расширения_1_K: 2.35e-5
  электропроводность_S_m: 3.7e7
наследуемые: {}
дополнительные:
  цена_usd_kg: 6
  твердость_vickers_HV: 25
  твердость_rockwell_HRC: null
  твердость_по_моосу: 2.75
  относительное_удлинение_процентов: 12
  магнитная_проницаемость: null
  коэффициент_демпфирования: null
сравнение_структур: {}
дата_создания: 2026-11-05
дата_обновления: 2026-11-05

# Материал: Алюминиевая бондинг-проволока (heavy Al wire)

## Описание

Алюминиевая heavy bonding wire (Al ≥99.99%, классы Al-H11/Al-CR/AlX с добавками Si, Mg или Sc): основной материал проволочных соединений силовых полупроводников — IGBT и MOSFET, включая дискретные SiC MOSFET в корпусах TO-247. Типовые диаметры large-diameter Al wire — 125–500 мкм (стандартные ряды 125, 300, 400 мкм); в power-cycling исследованиях MOSFET-модулей (DCB-подложка Al₂O₃, topside металлизация AlSiCu0.5) проволока Ø125 мкм показала в 10–15 раз больший ресурс, чем Ø300 мкм, а Sc-легированный AlX за счёт выделений-упрочнителей при 200–300 °C сохраняет ресурс >500 тыс. циклов при ΔT=95 K. Соединение выполняется ультразвуковой клин-бондингом на алюминиевую топ-метализацию кристалла.

## Источники

- [bond-iq Publication 007: Impact of Aluminum Wire Material and Diameter on Power Cycling — Al-H11/Al-CR/AlX, 125/300/400 µm](https://www.bond-iq.de/blog-publications/publication-007)
- [Inseto: Large Diameter Aluminium Bonding Wire — 125–500 µm for power electronics](https://www.inseto.com/consumables/bonding-wire-ribbon-precision-metal-stampings-solder-preforms-by-coining/bonding-wire-and-ribbons-by-coining/large-diameter-aluminium-bonding-wire)
- [Tanaka: Aluminum Bonding Wire for Power Devices — IGBT/MOSFET track record](https://tanaka-preciousmetals.com/en/products/bonding_wires/power_devices)
