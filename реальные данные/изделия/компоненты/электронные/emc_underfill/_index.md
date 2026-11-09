---
применяется_в_изделиях_счёт: 1
id: izdelie_emc_underfill
псевдонимы: []
канонический_id: material_epoxy
тип: изделие
уровень_иерархии: верхний
уровень_номер: 1
подсистема: компоненты
класс: полимер
химический_состав: 'Кварценаполненная эпоксидная система пакования flip-chip: двухкомпонентная эпоксидная смола с отвердителем + сферический кремнезём SiO₂ 65–75 мас.% (наполнитель CTE-снижения), безгалогенная; классы — капиллярный underfill (CUF) и формовочный компаунд (EMC)'
кристаллическая_структура: аморфный
вариант_структуры: filled_thermoset
оптимальная_структура:
  структура: аморфный
  обоснование_выбора: "Гомогенный наполненный термореактив: сферический SiO₂ снижает CTE ненаполненной эпоксидки (45–65 ppm/K) до <20–40 ppm/K и поднимает модуль до 5–10 ГПа, жёстко связывая кристалл Si 2.6 ppm/K с подложкой 14–17 ppm/K; низкая вязкость CUF обеспечивает капиллярное затекание в зазор 25–100 мкм под кристаллом без пустот"
  применение_по_умолчанию: underfill_FCBGA
  источник_обоснования: web_search
варианты_по_применению:
  капиллярный_underfill:
    марка: 'Henkel Loctite ECCOBOND UF 9000AG (advanced-node flip chip): высокая Tg, CTE <20 ppm/K'
    примечание: 'капиллярное затекание под перевёрнутый кристалл, армирование C4-микробамперов (Henkel, 2022; Namics CUF-серия)'
  формовочный_компаунд:
    марка: 'EMC (epoxy molding compound), наполнение SiO₂ до 80–90 мас.% для lidless-пакетов'
    примечание: 'прессовая формовка вокруг кристалла; та же эпоксид-SiO₂ химия, более высокая вязкость и наполнение'
исследовательская_группа: 'Yutaka Tsukada (IBM Japan, 1992) — капиллярный underfill для надёжного монтажа flip-chip на органическую подложку (процесс SBB); C.P. Wong и S.H. Shi (Georgia Institute of Technology) — первый патент на no-flow underfill, US 6,180,696 (2001); Sumitomo Bakelite (SUMIKON EME) — пионер класса эпоксидных формовочных компаундов (EMC) для корпусирования ИС'
стандарты:
  - JEDEC J-STD-020 (классификация MSL/reflow)
  - JEDEC JESD22-A104 (термоциклирование)
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
источник: web_search
источник_url: https://www.wnie.online/henkel-unveils-semiconductor-capillary-underfill-for-advanced-silicon-node-flip-chip-applications
источник_дата: 2026-11-06
источник_разбора: веб-верификация
ии_перепроектирован:
  статус: false
  верификация: []
основные:
  плотность_kg_m3: 1760
  прочность_МПа: {min: 40, max: 100, nominal: 70}
  предел_текучести_МПа: {min: null, max: null, nominal: null}
  модуль_упругости_ГПа: 7
  коэффициент_Пуассона: 0.35
  ударная_вязкость_Дж_см2: null
  усталостная_прочность_МПа: {min: null, max: null, nominal: null}
  температура_плавления_C: null
  теплопроводность_W_mK: 0.6
  теплоёмкость_J_kgK: 950
  коэффициент_термического_расширения_1_K: 2.5e-5
  электропроводность_S_m: 1.0e-11
наследуемые: {}
дополнительные:
  цена_usd_kg: 90
  температура_стеклования_C: {min: 100, max: 150, nominal: 130}
  температура_разложения_C: 320
  рабочая_температура_C: {min: -55, max: 150}
  наполнитель_SiO2_мас_процентов: {min: 65, max: 75, nominal: 70}
  CTE_присоединённый_ppm_K: {min: 20, max: 40, nominal: 25}
  вязкость_Pa_s: {min: 5, max: 60, nominal: 20}
сравнение_структур: {}
дата_создания: 2026-11-06
дата_обновления: 2026-11-09
---
# Материал: кварценаполненный эпоксидный underfill/формовочный компаунд (FCBGA)

## Описание

Кремнезём-наполненный эпоксидный компаунд — обязательный элемент корпуса FCBGA: капиллярный underfill заполняет зазор между перевёрнутым кристаллом и органической подложкой, формовочный компаунд (EMC) укрывает бампы и проводники в lidless-исполнении. Ненаполненная отверждённая эпоксидка имеет CTE 45–65 ppm/°C (Polymer Innovation Blog); загрузка сферическим SiO₂ 65–75 мас.% снижает CTE до <20–40 ppm/K и поднимает модуль (силы: силика-частицы «reduce the CTE and increase the elastic modulus», Wong et al., GaTech). Передовой класс — Henkel Loctite ECCOBOND UF 9000AG (2022): «high glass transition temperature (Tg) and ultra-low (<20 ppm) coefficient of thermal expansion» (WNIE). Функция — перераспределение термических напряжений от рассогласования CTE кремния ~2.6 ppm/°C и органической подложки 14–17 ppm/°C (EpoxySet), защита припойных C4-микробамперов при термоциклировании JESD22-A104. Плотность 1760 кг/м³ — расчёт для 70 мас.% SiO₂ (ряд CUF 1.6–1.9 г/см³); теплопроводность 0.6 Вт/(м·К) — класс-типичная для наполненных CUF (Namics выпускает специальные высокотеплопроводные серии выше). Термореактив: плавления нет, разложение ~320 °C, температура_плавления_C = null (обоснованный null).

Историческая атрибуция технологии: flip-chip появился в IBM в начале 1960-х (Solid Logic Technology), но на дешёвые органические платы его перевёл именно underfill — в 1992 году Yutaka Tsukada (IBM Japan) опубликовал данные, что «FC chips could be reliably attached directly to PWB laminate if the chips were similarly underfilled» (обзор origins of flip chip, imapsource.org; процесс SBB — solder bump bonding + underfill). Второе поколение — no-flow underfill, совмещённый с пайкой: первый патент на материал — C.P. Wong и S.H. Shi (Georgia Institute of Technology), «No-flow underfill of epoxy resin, anhydride, fluxing agent and surfactant», US 6,180,696 (30.01.2001, Georgia Tech Research Corp.). Класс формовочных компаундов (EMC) для корпусирования ИС создан и де-факто стандартизован Sumitomo Bakelite (линейка SUMIKON EME — эталонные эпоксидные формовочные компаунды для полупроводниковых пакетов).

## Источники

- https://www.wnie.online/henkel-unveils-semiconductor-capillary-underfill-for-advanced-silicon-node-flip-chip-applications (Henkel Loctite ECCOBOND UF 9000AG: высокая Tg, CTE <20 ppm)
- https://www.henkel.com/press-and-media/press-releases-and-kits/2022-09-19-henkel-unveils-semiconductor-capillary-underfill-for-advanced-silicon-node-flip-chip-applications-1752358 (пресс-релиз Henkel, 2022)
- https://polymerinnovationblog.com/fillers-action-reducing-coefficient-thermal-expansion-thermosets (CTE ненаполненной эпоксидки 45–65 ppm/°C)
- https://repository.gatech.edu/bitstreams/f9b4b0e4-ed2b-4a4f-b2ad-73bf850d62e6/download (Wong C.P. et al.: силика снижает CTE и повышает модуль underfill)
- https://epoxysetinc.com/epoxy-adhesive/epoxy-underfill-for-electronics-assembly (Si 2.6 ppm/°C vs органическая подложка 14–17 ppm/°C)
- https://namics-corp.com/capillary-underfills (Namics: класс капиллярных underfills для flip chip)
- https://patents.google.com/patent/US20110122590A1/en (эпоксидные формулы CUF: высоконаполненный низковязкий состав)
- https://imapsource.org/article/56583-on-the-origins-status-and-future-of-flip-chip-wafer-level-packaging.pdf (обзор origins of flip chip: Tsukada IBM Japan 1992 — подfill для прямого монтажа на PWB)
- https://patents.google.com/patent/US6180696B1/en (Wong C.P., Shi S.H., Georgia Tech — первый патент на no-flow underfill, US 6,180,696, 30.01.2001)
- https://repository.gatech.edu/bitstreams/fd36e6d9-82c2-4494-9223-74215a6ae41b/download (C.P. Wong, IEEE 2004: «The first patent on the no-flow underfill material was by Wong and Shi at the Georgia Institute of Technology»)
- https://www.sumibe.co.jp/english/product/it-materials/epoxy/sumikon-eme (Sumitomo Bakelite SUMIKON EME — класс эпоксидных формовочных компаундов для корпусирования ИС)
