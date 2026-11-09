---
























id: material_ti-6al-4v
тип: материал
класс: металл
химический_состав: 'Ti-6Al-4V (Grade 5, UNS R56400): Al 5.5–6.75 %, V 3.5–4.5 %, Fe ≤0.30 %, O ≤0.20 %, C ≤0.08 %, N ≤0.05 %, H ≤0.015 %, Y ≤0.005 %, Ti — остальное (ASTM-спецификация, Wikipedia/ASM)'
кристаллическая_структура: 'двухфазная α+β: α-фаза ГПУ (стабилизатор Al), β-фаза ОЦК (стабилизатор V)'
вариант_структуры: двухфазный_альфа_бета_поликристалл
оптимальная_структура:
  структура: отожжённый двухфазный α+β поликристалл (отжиг 691–760 °C, охлаждение на воздухе или в печи — ATI)
  обоснование_выбора: "Отжиг ниже β-трансуса (999±14 °C по ATI) фиксирует равновесную двухфазную структуру (~90 % α + ~10 % β): максимум пластичности (δ ≥14 % по B265) и свариваемости при UTS 950 МПа; режим STA (закалка 913–954 °C + старение 524–552 °C) повышает прочность до ~1170 МПа ценой вязкости и трещиностойкости — состояние выбирается под требования изделия"
  применение_по_умолчанию: авиационно-космические_несущие_конструкции
  источник_обоснования: web_search
варианты_по_применению:
  авиационные_двигатели_компрессоры:
    описание: 'компрессорные лопатки, диски и кольца реактивных двигателей (ATI): усталостная прочность 500–600 МПа при 10⁷ циклах, рабочие температуры до 427 °C, плотность на ~40 % ниже стальных никелевых аналогов'
    свойства: {усталостная_прочность_МПа: '500–600 (10⁷ циклов)', плотность_kg_m3: '4430', рабочая_температура_C: 'до 427'}
    применение: 'компрессоры ТРДД, вентиляторы, валы двигателей'
  планер_и_космические_изделия:
    описание: 'силовые элементы планера, капсулы, сосуды давления, корпуса ракетных двигателей (ATI): наилучшее отношение прочность/масса среди промышленных конструкционных металлов; фюзеляж Boeing 787 — 15 % Ti по массе'
    свойства: {прочность_МПа: '950 (min B265)', удельная_прочность: '214 кН·м/кг'}
    применение: 'авиационные шпангоуты и лонжероны, сосуды давления, ракетные корпуса'
  медицинские_импланты:
    описание: 'вариация Grade 23 (Ti-6Al-4V ELI, O ≤0.13 %) — повышенная вязкость разрушения и криогенная пластичность; биосовместимость, модуль 110–114 ГПа ближе к костной ткани, чем у сталей (ASTM F136, ISO 5832-3)'
    свойства: {кислород_max: '0.13 %', стандарт: 'ASTM F136'}
    применение: 'эндопротезы, пластины, шурупы, зубные импланты'
  морские_и_химические_среды:
    описание: 'стойкая пассивная плёнка TiO2: практически полная стойкость к морской воде, хлоридам и окислителям; в отличие от нержавеющих сталей не подвержен хлоридному SCC и питтингу'
    свойства: {scc_хлориды: 'не подвержен', среда: 'морская вода, HNO3, хлориды'}
    применение: 'корпуса аппаратуры морского базирования, офшорное оборудование, теплообменники'
  крепёж_высоконагруженный:
    описание: 'болты, заклёпки, втулки несущих узлов, ступицы несущих винтов вертолётов (ATI); в состоянии STA прочность до 1170 МПа (Kyocera: UTS 1170/YS 1100 МПа, HRC 35–39)'
    свойства: {прочность_МПа: 'до 1170 (STA)', твердость: 'HRC 35–39 (STA)'}
    применение: 'авиационный крепёж, ступицы роторов, критические поковки'
  оружейные_корпуса_и_ресиверы:
    описание: 'легкосплавные ресиверы и корпуса скорострельного оружия (Dillon Aero M134D-H «Hybrid»): титан и skeletonized-детали снижают массу стального пулемёта M134D (~16 кг) на 4,5 кг при сохранении его ресурса свыше 1 500 000 выстрелов'
    свойства: {прочность_МПа: '950 (min B265)', плотность_kg_m3: '4430'}
    применение: 'ресиверы minigun M134D-H, корпуса оружейных установок, skeletonized детали оружия'
исследовательская_группа: null
стандарты:
  - ASTM B265 Grade 5 (лист и полоса: UTS ≥950 МПа, YS ≥880 МПа, δ ≥14 %)
  - ASTM B348 (пруток и профили Grade 5)
  - ASTM F136 / ISO 5832-3 (имплантабельный Ti-6Al-4V ELI)
  - AMS 4928 (пруток/поковки, отожжённый), AMS 4911 (лист), AMS 4965/4967 (STA/отжиг)
  - UNS R56400 (Grade 5); UNS R56401 (ELI, Grade 23)
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
источник: web_search
источник_url: https://www.atimaterials.com/Products/Documents/datasheets/titanium/alloyed/ati_6-4_tds_en_v1.pdf
источник_дата: 2026-11-06
источник_разбора: веб-верификация
ии_перепроектирован:
  статус: false
  верификация: []
основные:
  плотность_kg_m3: 4430
  прочность_МПа: {min: 895, max: 1170, nominal: 950}
  предел_текучести_МПа: {min: 828, max: 1100, nominal: 880}
  модуль_упругости_ГПа: 114
  коэффициент_Пуассона: 0.342
  ударная_вязкость_Дж_см2: null
  усталостная_прочность_МПа: {min: 500, max: 600, nominal: 550}
  температура_плавления_C: {min: 1604, max: 1660, nominal: 1632}
  теплопроводность_W_mK: {min: 6.7, max: 7.5, nominal: 6.7}
  теплоёмкость_J_kgK: 526
  коэффициент_термического_расширения_1_K: 8.6e-06
  электропроводность_S_m: 5.9e5
дополнительные:
  цена_usd_kg: null
  твердость_vickers_HV: null
  твердость_rockwell_HRC: 36
  твердость_по_моосу: null
  относительное_удлинение_процентов: {min: 10, max: 15, nominal: 14}
  магнитная_проницаемость: null
  коэффициент_демпфирования: null
  твердость_бринелль_HB: 334
  бета_трансус_C: 999
  электросопротивление_мкОм_м: 1.7
  сужение_процентов: '25–35 (отожжённый)'
  рабочая_температура_длительная_C: 350
  рабочая_температура_кратковременная_C: 427
  окислительная_стойкость_до_C: 538
сравнение_структур:
  отожжённое_состояние:
    описание: 'базовое промышленное состояние (отжиг 691–760 °C — ATI; 700–785 °C по ряду спецификаций): UTS ≥950 МПа, YS ≥880 МПа, δ ≥14 % (ASTM B265 Gr5); HRC 30–34 (ATI); максимум пластичности, свариваемости и усталостной однородности'
    свойства: {прочность_МПа: '950 (min B265) / 900–950 (тип.)', предел_текучести_МПа: '880 (min B265) / 880–920 (тип.)', относительное_удлинение: '≥14 %'}
    применение: 'универсальный конструкционный режим: планер, крепёж, морское оборудование'
  STA_закалка_старение:
    описание: 'решётка 913–954 °C (1 ч, вода) + старение 524–552 °C (4–8 ч) — ATI: UTS до ~1170 МПа, YS до ~1100 МПа (Kyocera 1170/1100), HRC 35–39; оптимально в тонких сечениях с быстрой закалкой, вязкость и пластичность снижены (δ 8–12 %)'
    свойства: {прочность_МПа: '1035–1240', предел_текучести_МПа: '965–1170', твердость: 'HRC 35–39'}
    применение: 'высоконагруженный крепёж, детали двигателей, поковки критического назначения'
  Grade_23_ELI_криогенная:
    описание: 'низкокислородная вариация (O ≤0.13 % против ≤0.20 %): выше вязкость разрушения и пластичность при криогенных температурах; стандарт имплантатов ASTM F136 / ISO 5832-3'
    свойства: {кислород_max: '0.13 %', позиционирование: 'импланты, криогеника'}
    применение: 'медицинские импланты, криогенные сосуды'
  Grade_2_чистый_титан_сравнение:
    описание: 'коммерчески чистый Ti без Al/V: прочность заметно ниже (UTS ≥345 МПа), но выше пластичность, теплопроводность (~16–17 Вт/(м·К)) и формуемость, дешевле; выбор когда прочность Grade 5 избыточна'
    свойства: {прочность_МПа: '≥345', теплопроводность_W_mK: '~16.4', легирование: 'без Al/V'}
    применение: 'химаппаратура, теплообменники, формуемые детали'
  Al_7075_T6_сравнение:
    описание: 'классический авиационный алюминий: легче (2810 кг/м³) и дешевле, но UTS 572 МПа и потеря прочности выше 150 °C; Ti-6Al-4V выигрывает в удельной прочности при повышенных температурах и усталости'
    свойства: {плотность_kg_m3: '2810', прочность_МПа: '572', класс: 'Al сплав'}
    применение: 'Ti-6Al-4V — там где алюминий не держит температуру/усталость; Al 7075 — где критична цена массы конструкции'
дата_создания: 2026-11-03
дата_обновления: 2026-11-06
---
## Описание

Ti-6Al-4V (Grade 5, UNS R56400) — двухфазный (α+β) титановый сплав, самый широко применяемый титановый сплав в мире (~50 % мирового потребления титана). Алюминий (5.5–6.75 %) стабилизирует α-фазу (ГПУ), ванадий (3.5–4.5 %) — β-фазу (ОЦК). Сочетает высокую прочность (до 1170 МПа в STA), низкую плотность (4430 кг/м³), превосходную коррозионную стойкость и работоспособность от криогенных температур до ~427 °C (ATI).

**Ключевые характеристики (ATI Ti-6Al-4V Grade 5 TDS, v1 2012; Kyocera; Wikipedia/ASM):**
- плотность 4430 кг/м³ (0.160 lb/in³ — ATI; 4.43 г/см³ — Kyocera/Wikipedia);
- диапазон плавления 1604–1660 °C (Kyocera: solidus 1604 / liquidus 1660; ATI указывает 1538–1649 °C — расхождение источников);
- β-трансус 999 °C ±14 (ATI);
- отожжённый (ASTM B265 Gr5): UTS ≥950 МПа, YS ≥880 МПа, δ ≥14 %;
- STA (Kyocera): UTS 1170 МПа, YS 1100 МПа;
- λ 6.7–7.5 Вт/(м·К) при комнатной температуре — очень низкая, причина плохой обрабатываемости резанием;
- рабочие температуры: длительно ~350 °C, кратковременно до 427 °C (ATI), окислительная стойкость до ~538 °C.

Полное наименование (как в CSV): `Ti-6Al-4V`

**Класс:** металл (двухфазный α+β титановый сплав)
**Кристаллическая структура:** двухфазный α+β поликристалл (α — ГПУ, β — ОЦК)

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| тип узла | материал | — | canon |


## Источники

- ATI Ti-6Al-4V, Grade 5 Technical Data Sheet (официальный datasheet ATI, v1 1/31/2012): https://www.atimaterials.com/Products/Documents/datasheets/titanium/alloyed/ati_6-4_tds_en_v1.pdf
- Kyocera SGS — Ti 6Al 4V (Grade 5) Titanium Alloy Data Sheet (E=114 ГПа, UTS 1170, HB 334, плавление 1604–1660 °C): https://kyocera-sgstool.co.uk/titanium-resources/titanium-information-everything-you-need-to-know/ti-6al-4v-grade-5-titanium-alloy-data-sheet
- Wikipedia — Ti-6Al-4V (состав ASTM, λ 6.7–7.5 Вт/(м·К), E 104–113 ГПа, UTS/YS 900–950/880–920): https://en.wikipedia.org/wiki/Ti-6Al-4V
- ChinaMetalSupply — Titanium Grade 5 Properties: Complete Engineering Guide (c_p 526, КТР 8.6–9.2·10⁻⁶, усталость 500–600 МПа @10⁷): https://chinametalsupply.com/titanium-grade-5-properties
- TIMETAL 6-4 datasheet (Timet — самый употребимый титановый сплав, 44 стр.): https://www.timet.com/documents/datasheets/alpha-and-beta-alloys/timetal-6-4.pdf
- CSV: `начальные данные_final.csv` (пользовательский ввод)

## Химический состав

Grade 5 (ASTM-спецификация, wt %): Al 5.5–6.75; V 3.5–4.5; Fe ≤0.30; O ≤0.20; C ≤0.08; N ≤0.05; H ≤0.015; Y ≤0.005; Ti — остальное. Вариация Grade 23 (ELI) отличается O ≤0.13 % — повышенная вязкость разрушения для имплантов и криогеники (ASTM F136). Кислород — ключевой упрочнитель α-фазы: его предел определяет класс прочности.

## Физические свойства

| Свойство | Значение | Источник |
|---|---|---|
| Плотность | 4430 кг/м³ (0.160 lb/in³; 4.43 г/см³) | ATI (lb), Kyocera, Wikipedia |
| Диапазон плавления | 1604–1660 °C (solidus/liquidus) | Kyocera; ATI: 1538–1649 °C |
| β-трансус | 999 °C ±14 (1830 °F ±25) | ATI |
| Теплопроводность | 6.7–7.5 Вт/(м·К) при ~20 °C | Wikipedia [13][14], Kyocera |
| Удельная теплоёмкость | 526 Дж/(кг·К) при 20 °C (0.5263 Дж/(г·°C)) | datasheet 6Al-4V, ChinaMetalSupply |
| КТР | 8.6·10⁻⁶ 1/К (20–100 °C); до 9.2·10⁻⁶ при нагреве | datasheet 6Al-4V, ChinaMetalSupply |
| Электросопротивление | ~1.7 мкОм·м (20 °C) | ASM/MatWeb-данные |

## Механические свойства

- **Модуль упругости**: 113.8–114 ГПа (Kyocera 114; Wikipedia 104–113; ChinaMetalSupply 110–114);
- **Пуассона коэффициент**: 0.342 (ASM/MatWeb);
- **Отожжённый** (ASTM B265 Grade 5 минимумы): UTS ≥950 МПа, YS ≥880 МПа, δ ≥14 %; типичные 900–950 / 880–920 МПа (Wikipedia); сужение 25–35 %;
- **STA** (закалка 913–954 °C + старение 524–552 °C): UTS до ~1170 МПа, YS до ~1100 МПа, δ 8–12 % (Kyocera 1170/1100/10 %);
- **Твёрдость**: HRC 30–34 отожжённый, HRC 35–39 STA (ATI); типично HRC 36 (Wikipedia); HB 334 (Kyocera);
- **Усталостная прочность**: гладкие ненадрезанные образцы на воздухе — амплитуды 500–600 МПа при базе >10⁷ циклов (ChinaMetalSupply);
- **Теплообработка** (ATI): отжиг 691–760 °C ½–2 ч; снятие напряжений 538–649 °C 1–8 ч; полная закалка 913–954 °C + старение 524–552 °C 4–8 ч.

## Тепловые свойства

Диапазон плавления 1604–1660 °C (Kyocera solidus/liquidus; ATI приводит 1538–1649 °C — источники расходятся, для расчётов рекомендуется консервативный нижний предел 1538 °C). Теплопроводность 6.7–7.5 Вт/(м·К) при ~20 °C — одна из самых низких среди конструкционных металлов (у стали ~50, у алюминия ~200): обуславливает плохую обрабатываемость (тепло концентрируется на кромке инструмента) и градиенты температур в толстых сечениях при сварке. КТР 8.6·10⁻⁶ 1/К (20–100 °C) — промежуточное между алюминием (23) и сталями (12–17). Удельная теплоёмкость 526 Дж/(кг·К). Рекомендуемые длительные рабочие температуры до ~350 °C (до ~400 °C кратковременно сохраняются прочностные свойства); ATI допускает применение до 800 °F (427 °C); приемлемая окислительная стойкость до ~538 °C (1000 °F) — выше начинается заметное окисление и охрупчивание α-каркаса кислородом.

## Электрические свойства

Удельное электросопротивление ~1.7 мкОм·м при 20 °C → электропроводность σ ≈ 5.9·10⁵ См/м (~1 % IACS — проводит плохо, типично для титана с его d-электронной структурой). Парамагнетик; практически не влияет на электромагнитные поля (немагнитный крепёж радаров и МРТ-совместимого оборудования).

## Эксплуатационные характеристики

- Коррозионная стойкость: прочная пассивная плёнка TiO2 — полная стойкость к морской воде, хлоридам (нет SCC и питтинга, в отличие от нержавеющих сталей), окислителям; в восстанавливающих кислотах (HCl, H2SO4) слабее;
- водородное охрупчивание: H ≤0.015 % по спецификации; наводороживание при неправильном травлении/сварке без защиты — ATI Special Precautions;
- гальваническая пара: в контакте с алюминием/сталью титан — катод: парный металл корродирует (использовать изоляцию);
- обрабатываемость резанием: плохая (низкая λ) — медленные скорости, тяжёлые подачи, обильная нехлоридная СОЖ (ATI);
- свариваемость: легко сваривается в отожжённом состоянии; обязательна защита от O/N/H (инертные камеры, trailing shield) — ATI;
- старение при 524–552 °C после сварки завершается в процессе послесваречной термообработки.

## Технологии получения

Первичная плавка вакуумно-дуговая (VAR), электронно-лучевая (EB) или плазменно-дуговая гарниссажная (PAM), переплав одним-двумя вакуумно-дуговыми шагами (ATI). Далее — ковка/прокатка (окончательная ковка от 954 °C с финишной температурой 788 °C, обжатия ≥35 % для оптимальных свойств), отжиг или STA. Формовка при комнатной температуре затруднена — гибка/вытяжка отожжённого материала с подогревом до 649 °C; creep-forming 538–649 °C. Спецификации: AMS 4928 (пруток/поковки), AMS 4911 (лист), AMS 4965/4967 (STA), ASTM B265/B348, F136 (ELI).

## Применение в изделиях

**Используется в частях/изделиях:**
- `часть_3d_sic-mikropillarnyi_tritii-betavoltaik_case` — корпус
- `часть_3d_sic-mikropillarnyi_tritii-betavoltaik_micropillars` — 3D_SiC_микропилляры
- `часть_3d_sic-mikropillarnyi_tritii-betavoltaik_substrate` — SiC_подложка
- `часть_4h-sic_betavoltaik_case` — корпус
- `часть_4h-sic_betavoltaik_isotope` — Ni-63_источник
- `часть_4h-sic_betavoltaik_sic_diode` — SiC_pn_диод
- `часть_4h-sic_betavoltaik_substrate` — SiC_подложка
- `часть_ads-b_priemnik_core` — основной_элемент
- `часть_aesa_radar_core` — основной_элемент
- `часть_akusticheskaya_linza_core` — основной_элемент
- `часть_akusticheskaya_linza_housing` — корпус
- `часть_akusticheskaya_linza_mounting` — крепёж
- `часть_alyuminievo-vozdushnye_toplivnye_elementy_cathode` — воздушный_катод
- `часть_alyuminievo-vozdushnye_toplivnye_elementy_electrolyte` — щелочной_электролит
- `часть_alyuminievo-vozdushnye_toplivnye_elementy_housing` — корпус
- `часть_alyuminievo-vozdushnye_toplivnye_elementy_separator` — сепаратор
- `часть_apa_core` — основной_элемент
- `часть_apa_housing` — корпус
- `часть_apa_mounting` — крепёж
- `часть_asrg_alternator` — генератор_тока
- `часть_asrg_cooler` — охладитель
- `часть_asrg_heater_head` — нагреватель_голова
- `часть_asrg_housing` — корпус
- `часть_asrg_piston` — поршень
- `часть_asrg_regenerator` — регенератор
- `часть_belleville_shaiby_core` — основной_элемент
- `часть_belleville_shaiby_housing` — корпус
- `часть_belleville_shaiby_mounting` — крепёж
- `часть_betavoltaiki_case` — корпус_титан
- `часть_betavoltaiki_isotope` — Ni-63_источник
- `часть_betavoltaiki_semiconductor` — SiC_преобразователь
- `часть_betavoltaiki_terminal` — вывод
- `часть_bldc_enkoder_core` — основной_элемент
- `часть_bldc_enkoder_housing` — корпус
- `часть_bldc_enkoder_mounting` — крепёж
- `часть_bldc_core` — основной_элемент
- `часть_bldc_housing` — корпус
- `часть_bldc_mounting` — крепёж
- `часть_cameron_cpu` — neural_net_cpu_cameron
- `часть_cameron_нога_левая` — servo_leg_small
- `часть_cameron_рука_левая` — servo_arm_small
- `часть_cameron_сенсоры` — optical_audio_array
- `часть_cameron_ткань_кожа` — living_tissue_female
- `часть_cameron_топливная_ячейка_1` — fuel_cell_small
- `часть_cameron_топливная_ячейка_2` — fuel_cell_small
- `часть_cameron_эндоскелет` — titanium_endoskeleton_small
- `часть_coilgun_barrel` — ствол
- `часть_coilgun_capacitor_bank` — батарея_конденсаторов
- `часть_coilgun_coil` — катушка
- `часть_coilgun_housing` — корпус
- `часть_coilgun_projectile` — снаряд
- `часть_coilgun_switch` — коммутатор
- `часть_copv_core` — основной_элемент
- `часть_copv_housing` — корпус
- `часть_copv_mounting` — крепёж
- `часть_cw-lazer_core` — основной_элемент
- `часть_cw-lazer_housing` — корпус
- `часть_cw-lazer_mounting` — крепёж
- `часть_dea_core` — основной_элемент
- `часть_dea_housing` — корпус
- `часть_dea_mounting` — крепёж
- `часть_dielektricheskie_elastomernye_datchiki_core` — основной_элемент
- `часть_dielektricheskie_elastomernye_datchiki_housing` — корпус
- `часть_dielektricheskie_elastomernye_datchiki_mounting` — крепёж
- `часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_coil` — катушка
- `часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_housing` — корпус
- `часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_spring` — пружина
- `часть_dvs_core` — основной_элемент
- `часть_dvs_housing` — корпус
- `часть_dvs_mounting` — крепёж
- `часть_elastomernyh_dempferah_core` — основной_элемент
- `часть_elastomernyh_dempferah_housing` — корпус
- `часть_elastomernyh_dempferah_mounting` — крепёж
- `часть_elektroflyuidnye_volokna_mit_core` — основной_элемент
- `часть_elektroflyuidnye_volokna_mit_housing` — корпус
- `часть_elektroflyuidnye_volokna_mit_mounting` — крепёж
- `часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_bearings` — подшипники
- `часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_coil` — электромагнит
- `часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_housing` — корпус
- `часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_powder` — магнитный_порошок
- `часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_rotor` — ротор
- `часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_stator` — статор
- `часть_emi-generator_antenna` — антенна_рупор
- `часть_emi-generator_capacitor_bank` — батарея_конденсаторов
- `часть_emi-generator_housing` — корпус
- `часть_emi-generator_source` — взрывной_источник
- `часть_emi-generator_switch` — коммутатор
- `часть_emi-generator_waveguide` — волновод
- `часть_eo_ir_kamera_core` — основной_элемент
- `часть_eo_ir_kamera_housing` — корпус
- `часть_eo_ir_kamera_mounting` — крепёж
- `часть_event_cameras_core` — основной_элемент
- `часть_event_cameras_housing` — корпус
- `часть_event_cameras_mounting` — крепёж
- `часть_ferritovye_klinya_na_kabelyah_sensorov_core` — основной_элемент
- `часть_ferritovye_klinya_na_kabelyah_sensorov_housing` — корпус
- `часть_ferritovye_klinya_na_kabelyah_sensorov_mounting` — крепёж
- `часть_flat-face_couplings_iso_16028_core` — основной_элемент
- `часть_flat-face_couplings_iso_16028_housing` — корпус
- `часть_flat-face_couplings_iso_16028_mounting` — крепёж
- `часть_fleksury_8_diskov_po_0_15_mm_core` — основной_элемент
- `часть_fleksury_8_diskov_po_0_15_mm_housing` — корпус
- `часть_fleksury_8_diskov_po_0_15_mm_mounting` — крепёж
- `часть_flir_boson_640_core` — основной_элемент
- `часть_flir_boson_640_housing` — корпус
- `часть_flir_boson_640_mounting` — крепёж
- `часть_flir_core` — основной_элемент
- `часть_flir_housing` — корпус
- `часть_flir_lwir_2_core` — основной_элемент
- `часть_flir_lwir_2_housing` — корпус
- `часть_flir_lwir_2_mounting` — крепёж
- `часть_flir_mounting` — крепёж
- `часть_gibkii_pcb_core` — основной_элемент
- `часть_gibkii_pcb_housing` — корпус
- `часть_gibkii_pcb_mounting` — крепёж
- `часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_core` — основной_элемент
- `часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing` — корпус
- `часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting` — крепёж
- `часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_core` — основной_элемент
- `часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_housing` — корпус
- `часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_mounting` — крепёж
- `часть_gr801_noel-v_risc-v_capacitors` — конденсаторы
- `часть_gr801_noel-v_risc-v_crystal_osc` — кварцевый_резонатор
- `часть_gr801_noel-v_risc-v_flash` — флеш_память
- `часть_gr801_noel-v_risc-v_pcb` — плата
- `часть_gr801_noel-v_risc-v_pins` — пины
- `часть_gr801_noel-v_risc-v_sram` — SRAM_кэш
- `часть_gr801_noel-v_risc-v_substrate` — подложка
- `часть_gr801_noel-v_risc-v_thermal_pad` — термопрокладка
- `часть_hasel_core` — основной_элемент
- `часть_hasel_housing` — корпус
- `часть_hasel_mounting` — крепёж
- `часть_hk_aerial_крылья` — wings
- `часть_hk_aerial_навигация` — radar_navigation
- `часть_hk_aerial_связь` — skynet_link
- `часть_hk_aerial_фюзеляж` — fuselage
- `часть_hk_tank_башня` — turret
- `часть_hk_tank_боеприпасы` — plasma_ammo
- `часть_hk_tank_гусеница_левая` — tank_track
- `часть_hk_tank_двигатель` — nuclear_engine
- `часть_hk_tank_корпус` — tank_body
- `часть_hk_tank_навигация` — gps_nav
- `часть_hk_tank_связь` — skynet_link
- `часть_hk_tank_сенсоры` — radar_sensor
- `часть_ibm_northpole_capacitors` — MLCC_блок
- `часть_ibm_northpole_hbm` — память_HBM
- `часть_ibm_northpole_package` — корпус_FCBGA
- `часть_ibm_northpole_substrate` — органическая_подложка
- `часть_induktivnyi_nakopitel_coil` — индуктивность
- `часть_induktivnyi_nakopitel_cooling` — охлаждение
- `часть_induktivnyi_nakopitel_core` — магнитопровод
- `часть_induktivnyi_nakopitel_housing` — корпус
- `часть_induktivnyi_nakopitel_switch` — коммутатор
- `часть_ipg_yls-eco_core` — основной_элемент
- `часть_ipg_yls-eco_housing` — корпус
- `часть_ipg_yls-eco_mounting` — крепёж
- `часть_ipmc_core` — основной_элемент
- `часть_ipmc_housing` — корпус
- `часть_ipmc_mounting` — крепёж
- `часть_iridium_sbd_core` — основной_элемент
- `часть_iridium_sbd_housing` — корпус
- `часть_iridium_sbd_mounting` — крепёж
- `часть_kapillyarnaya_teplovaya_trubka_core` — основной_элемент
- `часть_kapillyarnaya_teplovaya_trubka_housing` — корпус
- `часть_kapillyarnaya_teplovaya_trubka_mounting` — крепёж
- `часть_kaskadnyi_stirling-kriokuler_core` — основной_элемент
- `часть_kaskadnyi_stirling-kriokuler_housing` — корпус
- `часть_kaskadnyi_stirling-kriokuler_mounting` — крепёж
- `часть_kompensatory_core` — основной_элемент
- `часть_kompensatory_housing` — корпус
- `часть_kompensatory_mounting` — крепёж
- `часть_kondensatory_keramicheskie_inner_electrodes` — внутренние_электроды
- `часть_kondensatory_keramicheskie_outer_electrodes` — внешние_электроды
- `часть_kondensatory_keramicheskie_plating` — гальваническое_покрытие
- `часть_kondensatory_keramicheskie_termination` — терминалы
- `часть_lidar_core` — основной_элемент
- `часть_lidar_housing` — корпус
- `часть_lidar_mounting` — крепёж
- `часть_lidar_robosense_ac1_core` — основной_элемент
- `часть_lidar_robosense_ac1_housing` — корпус
- `часть_lidar_robosense_ac1_mounting` — крепёж
- `часть_litii-tionilhloridnye_batarei_anode` — литий_анод
- `часть_litii-tionilhloridnye_batarei_case` — корпус_нерж
- `часть_litii-tionilhloridnye_batarei_cathode` — угольный_катод
- `часть_litii-tionilhloridnye_batarei_electrolyte` — thionyl_chloride
- `часть_litii-tionilhloridnye_batarei_separator` — сепаратор
- `часть_litii-tionilhloridnye_batarei_terminal` — вывод
- `часть_loop_heat_pipe_core` — основной_элемент
- `часть_loop_heat_pipe_housing` — корпус
- `часть_loop_heat_pipe_mounting` — крепёж
- `часть_lt-sofc_interconnect` — интерконнект
- `часть_lt-sofc_manifold` — коллектор_газа
- `часть_lt-sofc_seal` — герметизация
- `часть_lwir_boson_1024_core` — основной_элемент
- `часть_lwir_boson_1024_housing` — корпус
- `часть_lwir_boson_1024_mounting` — крепёж
- `часть_marcus_нога_левая` — servo_leg
- `часть_marcus_рука_левая` — servo_arm
- `часть_marcus_сердце_гибрид` — hybrid_heart
- `часть_marcus_топливная_ячейка` — fuel_cell
- `часть_marcus_человеческая_кожа` — human_tissue
- `часть_marcus_человеческий_мозг` — human_brain_hybrid
- `часть_marcus_человеческое_сердце` — biological_heart
- `часть_marcus_эндоскелет` — cybernetic_endoskeleton
- `часть_marx_generator_capacitors` — конденсаторы
- `часть_marx_generator_housing` — корпус
- `часть_marx_generator_insulator` — изоляторы_SF6
- `часть_marx_generator_output_terminal` — выходной_вывод
- `часть_marx_generator_resistors` — зарядные_резисторы
- `часть_marx_generator_spark_gaps` — искровые_промежутки
- `часть_memristornye_matritsy_adc` — АЦП
- `часть_memristornye_matritsy_bit_sense` — sense_amplifiers
- `часть_memristornye_matritsy_controller` — контроллер
- `часть_memristornye_matritsy_crossbar` — кроссбар_матрица
- `часть_memristornye_matritsy_word_drivers` — драйверы_строк
- `часть_mems-imu_core` — основной_элемент
- `часть_mems-imu_housing` — корпус
- `часть_mems-imu_mounting` — крепёж
- `часть_mems-mikrofonov_core` — основной_элемент
- `часть_mems-mikrofonov_housing` — корпус
- `часть_mems-mikrofonov_mounting` — крепёж
- `часть_metalinza_core` — основной_элемент
- `часть_metalinza_housing` — корпус
- `часть_metalinza_mounting` — крепёж
- `часть_mikrokanalnye_ohlazhdayuschie_plastiny_core` — основной_элемент
- `часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing` — корпус
- `часть_mikrokanalnye_ohlazhdayuschie_plastiny_mounting` — крепёж
- `часть_mikroreaktor_deleniya_coolant` — охладитель
- `часть_mikroreaktor_deleniya_fuel` — U-235_топливо
- `часть_mikroreaktor_deleniya_heat_exchanger` — теплообменник
- `часть_mikroreaktor_deleniya_moderator` — замедлитель
- `часть_mikroreaktor_deleniya_shielding` — экранирование
- `часть_mikroreaktor_deleniya_vessel` — корпус_реактора
- `часть_minigun_m134_core` — основной_элемент
- `часть_minigun_m134_housing` — корпус
- `часть_mmrtg_connector` — разъём
- `часть_mmrtg_hot_side` — горячий_узел
- `часть_mmrtg_housing` — корпус
- `часть_mptm_controls` — электроника_управления
- `часть_mptm_engine` — двигатель
- `часть_mptm_generator` — генератор
- `часть_mptm_heat_exchanger` — теплообменник
- `часть_mptm_housing` — корпус
- `часть_multispektralnye_cmos-matritsy_s_ik-diapazonom_core` — основной_элемент
- `часть_multispektralnye_cmos-matritsy_s_ik-diapazonom_housing` — корпус
- `часть_multispektralnye_cmos-matritsy_s_ik-diapazonom_mounting` — крепёж
- `часть_mwir_2_core` — основной_элемент
- `часть_mwir_2_housing` — корпус
- `часть_mwir_2_mounting` — крепёж
- `часть_mwir_nbn_640_core` — основной_элемент
- `часть_mwir_nbn_640_housing` — корпус
- `часть_mwir_nbn_640_mounting` — крепёж
- `часть_nasa_asc-e_srsc_alternator` — линейный_генератор
- `часть_nasa_asc-e_srsc_displacer_piston` — поршень_вытеснитель
- `часть_nasa_asc-e_srsc_heater_head` — нагреватель
- `часть_nasa_asc-e_srsc_power_piston` — рабочий_поршень
- `часть_nasa_asc-e_srsc_regenerator` — регенератор
- `часть_ni-63_betavoltaik_4h-sic_case` — корпус
- `часть_ni-63_betavoltaik_4h-sic_isotope` — Ni-63_источник
- `часть_ni-63_betavoltaik_4h-sic_sic_diode` — SiC_pn_диод
- `часть_ni-63_betavoltaik_4h-sic_substrate` — SiC_подложка
- `часть_nvidia_jetson_orin_nano_enclosure` — корпус
- `часть_nvidia_jetson_orin_nano_heat_sink` — радиатор
- `часть_nvidia_jetson_orin_nano_memory` — LPDDR_память
- `часть_nvidia_jetson_orin_nano_pcb` — плата
- `часть_nvidia_jetson_orin_nano_pmic` — PMIC_питание
- `часть_nvidia_jetson_orin_nano_soc` — SoC_модуль
- `часть_nvidia_jetson_orin_nano_storage` — eMMC_флеш
- `часть_nvidia_jetson_orin_nano_wifi_bt` — WiFi_BT_модуль
- `часть_obd-ii_core` — основной_элемент
- `часть_obd-ii_housing` — корпус
- `часть_obd-ii_mounting` — крепёж
- `часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core` — основной_элемент
- `часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing` — корпус
- `часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_mounting` — крепёж
- `часть_optovolokonnaya_shina_core` — основной_элемент
- `часть_optovolokonnaya_shina_housing` — корпус
- `часть_optovolokonnaya_shina_mounting` — крепёж
- `часть_pcm_cell_array` — массив_PCM_ячеек
- `часть_pcm_controller` — контроллер
- `часть_pcm_io_interface` — I/O
- `часть_pcm_periphery` — периферия
- `часть_pcm_selector` — селектор_устройство
- `часть_perovskite_tandem_backsheet` — подложка
- `часть_perovskite_tandem_cells` — Si_ячейки
- `часть_perovskite_tandem_encapsulant` — инкапсулянт_EVA
- `часть_perovskite_tandem_frame` — рама_алюминий
- `часть_perovskite_tandem_front_glass` — переднее_стекло
- `часть_perovskite_tandem_junction_box` — распредкоробка
- `часть_pezo-mems_core` — основной_элемент
- `часть_pezo-mems_housing` — корпус
- `часть_pezo-mems_mounting` — крепёж
- `часть_pezo-sensor_core` — основной_элемент
- `часть_pezo-sensor_housing` — корпус
- `часть_pezo-sensor_mounting` — крепёж
- `часть_pezoelektricheskie_mems_core` — основной_элемент
- `часть_pezoelektricheskie_mems_housing` — корпус
- `часть_pezoelektricheskie_mems_mounting` — крепёж
- `часть_pezoelektricheskii_gromkogovoritel_core` — основной_элемент
- `часть_pezoelektricheskii_gromkogovoritel_housing` — корпус
- `часть_pezoelektricheskii_gromkogovoritel_mounting` — крепёж
- `часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_bearings` — подшипники
- `часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_housing` — корпус
- `часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_nut` — гайка
- `часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_rollers` — ролики
- `часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_screw` — винт
- `часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_seals` — уплотнения
- `часть_pmut_core` — основной_элемент
- `часть_pmut_housing` — корпус
- `часть_pmut_mounting` — крепёж
- `часть_polyimide_fpc_core` — основной_элемент
- `часть_polyimide_fpc_housing` — корпус
- `часть_polyimide_fpc_mounting` — крепёж
- `часть_poristyi_gazovyi_podshipnik_iz_sic_core` — основной_элемент
- `часть_poristyi_gazovyi_podshipnik_iz_sic_housing` — корпус
- `часть_poristyi_gazovyi_podshipnik_iz_sic_mounting` — крепёж
- `часть_povorotnoe_uplotnenie_core` — основной_элемент
- `часть_povorotnoe_uplotnenie_housing` — корпус
- `часть_povorotnoe_uplotnenie_mounting` — крепёж
- `часть_provodnikovaya_nanoreshetka_core` — основной_элемент
- `часть_provodnikovaya_nanoreshetka_housing` — корпус
- `часть_provodnikovaya_nanoreshetka_mounting` — крепёж
- `часть_quantum_cascade_laser_core` — основной_элемент
- `часть_quantum_cascade_laser_housing` — корпус
- `часть_quantum_cascade_laser_mounting` — крепёж
- `часть_radiatsionno-stoikii_neiromorfnyi_tmr_core` — основной_элемент
- `часть_radiatsionno-stoikii_neiromorfnyi_tmr_housing` — корпус
- `часть_radiatsionno-stoikii_neiromorfnyi_tmr_mounting` — крепёж
- `часть_razryvnye_mufty_iso_16028_core` — основной_элемент
- `часть_razryvnye_mufty_iso_16028_housing` — корпус
- `часть_razryvnye_mufty_iso_16028_mounting` — крепёж
- `часть_reshetchatyi_karkas_core` — основной_элемент
- `часть_reshetchatyi_karkas_housing` — корпус
- `часть_reshetchatyi_karkas_mounting` — крепёж
- `часть_reversivnye_pelte_ceramic_top` — керамика_верх
- `часть_reversivnye_pelte_electrodes` — электроды
- `часть_reversivnye_pelte_peltier_couples` — термоэлементы
- `часть_reversivnye_pelte_solder` — припой
- `часть_sensora_volnovogo_fronta_core` — основной_элемент
- `часть_sensora_volnovogo_fronta_housing` — корпус
- `часть_sensora_volnovogo_fronta_mounting` — крепёж
- `часть_sic_mosfet_die` — sic_кристалл
- `часть_sic_mosfet_encapsulant` — эпоксидный_корпус
- `часть_sic_mosfet_gate_terminal` — затвор
- `часть_sic_mosfet_lead_frame` — силовые_выводы
- `часть_sic_mosfet_solder` — пайка_кристалла
- `часть_sic_mosfet_wire_bonds` — проволочные_соединения
- `часть_slm_eos_m290_core` — основной_элемент
- `часть_slm_eos_m290_housing` — корпус
- `часть_slm_eos_m290_mounting` — крепёж
- `часть_sot-mram_cell_array` — массив_ячеек
- `часть_sot-mram_io_interface` — I/O_интерфейс
- `часть_sot-mram_periphery` — периферия
- `часть_sot-mram_row_decoders` — дешифраторы_строк
- `часть_sot-mram_sense_amplifiers` — sense_amplifiers
- `часть_starlink_mini_core` — основной_элемент
- `часть_starlink_mini_housing` — корпус
- `часть_starlink_mini_mounting` — крепёж
- `часть_stm32_core` — основной_элемент
- `часть_stm32_housing` — корпус
- `часть_stm32_mounting` — крепёж
- `часть_stm32h743_core` — основной_элемент
- `часть_stm32h743_housing` — корпус
- `часть_stm32h743_mounting` — крепёж
- `часть_superkondensatory_case` — корпус
- `часть_superkondensatory_current_collector` — токосъёмник
- `часть_superkondensatory_electrode_pos` — положительный_электрод
- `часть_superkondensatory_electrolyte` — электролит
- `часть_superkondensatory_separator` — сепаратор
- `часть_superkondensatory_terminal` — выводы
- `часть_svintsovo-kislotnye_akb_anode` — PbO2_анод
- `часть_svintsovo-kislotnye_akb_case` — корпус_PP
- `часть_svintsovo-kislotnye_akb_cathode` — Pb_катод
- `часть_svintsovo-kislotnye_akb_electrolyte` — H2SO4_электролит
- `часть_svintsovo-kislotnye_akb_grid_pos` — решётка_PbSb
- `часть_svintsovo-kislotnye_akb_separator` — сепаратор
- `часть_svintsovo-kislotnye_akb_terminal` — вывод
- `часть_svobodnoporshnevoi_stirling_alternator` — генератор
- `часть_svobodnoporshnevoi_stirling_cooler` — охладитель
- `часть_svobodnoporshnevoi_stirling_gas_spring` — газовая_пружина
- `часть_svobodnoporshnevoi_stirling_piston` — поршень
- `часть_svobodnoporshnevoi_stirling_regenerator` — регенератор
- `часть_t1001_миметический_полисплав` — mimetic_polyalloy_t1001
- `часть_t600_нога_левая` — servo_leg
- `часть_t600_рука_левая` — servo_arm
- `часть_t600_топливная_ячейка` — fuel_cell
- `часть_t600_эндоскелет` — titanium_endoskeleton
- `часть_t800_антенна` — skyet_link_antenna
- `часть_t800_аудио_сенсор` — audio_microphone
- `часть_t800_гиро_навигация` — imu_gyro
- `часть_t800_нога_левая` — servo_leg
- `часть_t800_рука_левая` — servo_arm
- `часть_t800_эндоскелет_торс` — hyperalloy_endoskeleton
- `часть_t850_cpu` — neural_net_cpu_v2
- `часть_t850_навигация` — imu_gyro
- `часть_t850_нога_левая` — servo_leg_improved
- `часть_t850_рука_левая` — servo_arm_improved
- `часть_t850_связь` — skyet_link
- `часть_t850_сенсоры` — optical_audio_array
- `часть_t850_топливная_ячейка_1` — hydrogen_fuel_cell_v2
- `часть_t850_эндоскелет` — hyperalloy_endoskeleton
- `часть_t_x_cpu` — neural_net_cpu_tx
- `часть_t_x_нога_левая` — servo_leg
- `часть_t_x_плазма_пушка` — built_in_plasma_cannon
- `часть_t_x_рука_левая` — servo_arm
- `часть_t_x_сенсоры` — optical_audio_array
- `часть_t_x_ткань_кожа` — living_tissue_female
- `часть_t_x_топливная_ячейка_1` — plasma_cell
- `часть_t_x_эндоскелет` — hyperalloy_endoskeleton_tx
- `часть_tcp_core` — основной_элемент
- `часть_tcp_housing` — корпус
- `часть_tcp_mounting` — крепёж
- `часть_termoelektricheskii_postoyannyi_magnit_clamping` — прижимные_болты
- `часть_termoelektricheskii_postoyannyi_magnit_heat_sink_cold` — холодный_радиатор
- `часть_termoelektricheskii_postoyannyi_magnit_heat_sink_hot` — горячий_радиатор
- `часть_termoelektricheskii_postoyannyi_magnit_teg_modules` — ТЕГ_модули
- `часть_termomoduli_pelte_ceramic_top` — керамика_верх
- `часть_termomoduli_pelte_electrodes` — электроды
- `часть_termomoduli_pelte_peltier_couples` — термоэлементы
- `часть_termomoduli_pelte_solder` — припой
- `часть_termomoduli_pelte_wires` — провода
- `часть_tpv-lenty_cooling` — охлаждение
- `часть_tpv-lenty_emitter_ribbon` — излучающая_лента
- `часть_tpv-lenty_pv_cells` — PV_ячейки
- `часть_tpv-lenty_reflector` — рефлектор
- `часть_tpv_cooling` — охлаждение
- `часть_tpv_emitter` — излучатель
- `часть_tpv_filter` — оптический_фильтр
- `часть_tpv_heat_source` — источник_тепла
- `часть_tpv_housing` — корпус
- `часть_tpv_pv_cell` — PV_ячейка
- `часть_tsa_core` — основной_элемент
- `часть_tsa_housing` — корпус
- `часть_tsa_mounting` — крепёж
- `часть_tverdooksidnyi_toplivnyi_element_interconnect` — интерконнект
- `часть_tverdooksidnyi_toplivnyi_element_manifold` — коллектор_газа
- `часть_tverdooksidnyi_toplivnyi_element_seal` — герметизация
- `часть_tverdotelnye_akkumulyatory_case` — корпус
- `часть_tverdotelnye_akkumulyatory_current_collector_al` — алюминиевый_токосъёмник
- `часть_tverdotelnye_akkumulyatory_current_collector_cu` — медный_токосъёмник
- `часть_tverdotelnye_akkumulyatory_electrolyte` — LiPF6_электролит
- `часть_tverdotelnye_akkumulyatory_separator` — сепаратор
- `часть_tverdotelnyi_mmwave_radar_core` — основной_элемент
- `часть_tverdotelnyi_mmwave_radar_housing` — корпус
- `часть_tverdotelnyi_mmwave_radar_mounting` — крепёж
- `часть_ultrakorotkoimpulsnye_lazery_core` — основной_элемент
- `часть_ultrakorotkoimpulsnye_lazery_housing` — корпус
- `часть_ultrakorotkoimpulsnye_lazery_mounting` — крепёж
- `часть_usb-c_core` — основной_элемент
- `часть_usb-c_housing` — корпус
- `часть_usb-c_mounting` — крепёж
- `часть_vodorodnye_toplivnye_elementy_bipolar_plate` — биполярная_пластина
- `часть_vodorodnye_toplivnye_elementy_catalyst_cathode` — Pt_катод
- `часть_vodorodnye_toplivnye_elementy_end_plate` — торцевая_пластина
- `часть_vodorodnye_toplivnye_elementy_gasket` — уплотнение
- `часть_vodorodnye_toplivnye_elementy_gdl_anode` — GDL_анод
- `часть_vodorodnye_toplivnye_elementy_gdl_cathode` — GDL_катод
- `часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_cryostat` — криостат
- `часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_housing` — корпус
- `часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_hts_element` — YBCO_элемент
- `часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_shaft` — вал
- `часть_zeno_power_am-241_housing` — корпус
- `часть_zeno_power_am-241_shielding` — экранирование
- `часть_zubchataya_mufta_core` — основной_элемент
- `часть_zubchataya_mufta_housing` — корпус
- `часть_zubchataya_mufta_mounting` — крепёж

## Аналоги и заменители

- **Ti-6Al-4V ELI (Grade 23, UNS R56401)** — низкокислородная вариация для имплантов и криогеники (ASTM F136);
- **Ti-6Al-4V Grade 5 STA** — термически упрочнённое состояние того же сплава (до 1170 МПа);
- **Ti-6Al-2Sn-4Zr-2Mo (Ti-6242)** — жаропрочный α-сплав для компрессоров до ~540 °C;
- **Ti-5Al-5Mo-5V-3Cr (Ti-5553)** — β-сплав повышенной прочности для шасси;
- **Grade 2 (чистый Ti)** — дешевле, пластичнее, но UTS всего ≥345 МПа;
- **Al 7075-T6 / сталь 4340** — альтернативы по цене/массе в авиационных конструкциях.
