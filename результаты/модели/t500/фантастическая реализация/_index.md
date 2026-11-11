---
id: SkyNet-T500
тип: модель_SkyNet
класс: наземный_гусеничный
категория: наземный_HK
тип_модели: наземный_гусеничный
источник_происхождения: игра
функции: ["штурм", "поддержка"]
канон_источник: 'Terminator: Resistance (2019)'
произведения: ["work_046"]
производитель: Скайнет
статус_реальности: canon
подтип_модели: стандартный
многослойная_броня:
  слои:
    - номер: 1
      материал: b4c  # B₄C (внешний)
      толщина_мм: {min: 2, target: 10}
    - номер: 2
      материал: rha_steel  # RHA steel (кин.)
      толщина_мм: {min: 2, target: 10}
    - номер: 3
      материал: uhmwpe_dyneema  # UHMWPE (арамидный)
      толщина_мм: {min: 2, target: 10}
    - номер: 4
      материал: rubber  # Резина (подложка)
      толщина_мм: {min: 2, target: 10}
  тип_брони: наземный_гусеничный
  соответствует_типу_модели: true  # F74, max_mass_percent: 50, min_layers: 4
доступность: фантастический
expected_subsystems: ["вычислительная", "энергетическая", "каркас", "броня", "сенсоры", "приводная_система", "система_связи", "навигация", "система_питания", "система_передвижения"]
relations:
  successor_of: null
  variation_of: null
  hybrid_of: []
  paradigm_shift_from: null
реализация_промышленная: 
  - izdelie_tverdooksidnyi_toplivnyi_element
  - izdelie_nasa_asc-e_srsc
  - izdelie_superkondensatory
  - izdelie_SkyNet-HKAerial
  - izdelie_SkyNet-Rev9
  - izdelie_SkyNet-Cameron
  - izdelie_metalinza
  - izdelie_mwir_nbn_640
  - izdelie_lidar_robosense_ac1
  - izdelie_hasel
  - izdelie_povorotnoe_uplotnenie
  - izdelie_elektroflyuidnye_volokna_mit
  - izdelie_radiatsionno-stoikii_neiromorfnyi_tmr
  - izdelie_razryvnye_mufty_iso_16028
  - izdelie_flat-face_couplings_iso_16028
реализация_ии: []
источник: web_search
источник_url: 'https://villains.fandom.com/wiki/T-500'
источник_разбора: канон
ии_перепроектирован:
  статус: false
  верификация: []
---
# v9.31: структурные поля §12.4.1-§12.4.X — добавлены как placeholder
# Реальные значения будут заполнены через web_search для каждой модели.
требования_выживаемости: 
  эми_защита: hardened (боевая машина)
  термобарьер:
          рабочий_диапазон_C:
                      min: -40
                      target: 60
  броня: тяжёлая (танк-охотник)
маскировка_инфильтратора: n/a
тактико_технические_характеристики: 
  мобильность:
          скорость_км_ч:
                      min: 20
                      target: 60
          преодоление_препятствий: гусеничный ход
  вооружение: двойные плазма-пушки + мини-ган
защита_от_собственной_радиации: n/a
кибербезопасность: 
  аппаратные_меры:
          HSM: true
          secure_boot: true
          TPM: true
          anti_tamper: zeroization
  iff: SkyNet IFF v3.1 (transponder 1090 MHz + crypto)
  шифрование: AES-256 + SkyNet proprietary
  skynet_protocol: Hive (collective consciousness) или Rogue (autonomous)
эмс_внутренняя: ECM + IFF
компоновка_изделий: танк с двойной гусеницей; 2 башни
трассировка_соединителей: []
программное_обеспечение: 'Neural Net CPU + SkyNet OS (Hive mode по умолчанию, Rogue для автономных)'
единая_эми_стратегия: SkyNet ground supremacy
единая_герметичность: IP65 (защита от пыли и дождя)
сертификация_модели_целого: 
  тест_skyet: phase_5 (F70 metrics PASS)
  канон_верификация: 'источник_разбора=канон'
журнал_экземпляра: SkyNet ground unit registry
утилизация_после_120_лет: 'T-800: 120 лет на 1 топливной ячейке (canon); после истощения — замена ячеек или разборка на запчасти'
экипаж_оператор: 0
промышленная_база: Skynet automated factory (Cyberdyne Systems / CRS)
alice_specs: ALICE sync protocol v9.31 (SkyNet hive-mind)
original_improved: canon
дата_создания: 2026-11-03
дата_обновления: 2026-11-06
---
# SkyNet-T500

## Описание

T-500 — средний гусеничный дрон с плазменным вооружением; эволюция серии T-1.

По верифицированным данным веб-поиска (проверено 2026-11-06, страница Villains Wiki «T-500» через web.archive.org, Terminator Wiki «T-500» (Fandom, через web.archive.org) и фанатская техдокументация goingfaster.com/term2029): **T-500 = Cyberdyne Systems Series 500 Armored Battle Chassis** (эндоскелет Series 500 Model 100) — серия боевых терминаторов Skynet из игры **The Terminator: Dawn of Fate (2002)**, созданная в 2027 как «preferred soldiers» Skynet; преемники T-400 и **последние специализированные гуманоидные Hunter-Killer'ы перед переходом Skynet на эндоскелеты как основную пехоту**; позже устарели, производство остановлено, действующие юниты отключены и заменены T-600 (Resistance Fighters Chronicles: «served as Skynet's preferred soldier prior to the development of the Series 600, the Series 700, and the Series 800»). Классификация по фанатской техдокументации T:2029 — «Infiltrator / Terminator» unit. Дизайн: ходячее бронированное боевое шасси («walking armored battle chassis»), похож на T-70 и T-800 основной линии; грудные пластины T-800 в таймлайнах Genisys и Dark Fate похожи на пластины T-500; некоторые юниты полностью покрыты человеческой кожей. Вооружение: лазерное (Dawn of Fate), синхронизировано с ИИ-программой («enhanced weapons are synched to their A.I. programs for a highly dangerous threat»); по фанатской ТТХ для вселенной Terminator: 2029 (DOS, 1992) — плазменная винтовка Westinghouse M25A1 + совместимость с любым стрелковым оружием мира ~1997 г. Фанатская ТТХ (goingfaster.com, НЕ канон): первый эндоскелетный HK — микропроцессорное управление, боевое шасси из гиперсплава на серво-гидравлических приводах, «блестящий металлический скелет»; рост 2 м, масса ~400 кг, броня — оболочка из гиперсплава 0,5 см; бег 60 км/ч (рывки до 75 км/ч с перегрузкой сервоприводов); жим 5× собственного веса, пробивает бетон и металл; сенсоры легче, но не слабее Series 1200 Scout; три режима управления (direct — Skynet как марионетка / automatic — предпрограммированные реакции / autonomous — месяцы независимых search-and-destroy); память read-only → предсказуемая тактика; потери Сопротивления 80:1; никогда не устаёт, не ест, не дышит. **РАСХОЖДЕНИЕ С ФАЙЛОМ:** ① T-500 — НЕ «средний гусеничный дрон»: это гуманоидный эндоскелет-шасси/инфильтратор (как T-200 в #713 — 人形而非履带式), гусениц в дизайне нет; класс «наземный_гусеничный» и категория «наземный_HK» по канону ошибочны; ② канон_источник по данным веба — The Terminator: Dawn of Fate (2002, игра), а не Terminator: Resistance (2019); ③ «эволюция серии T-1» неверна: преемник T-400, предшественник T-600; ④ ТТХ таблицы (длина_гусеницы 2,5 м; масса 1100 кг; «двойные плазма-пушки + мини-ган») источниками не подтверждаются (фанатская ТТХ: 2 м / ~400 кг / плазменная винтовка); ⑤ остальное оставлено до реклассификации (F13/F33-таксономия), как для T-200 (#713)/Turret (#716)/MK-Naval (#717)/SkyNet-Core (#719).

## Источник канон

- **Произведение:** Terminator: Resistance (2019)
- **Тип:** игра
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| длина_гусеницы_м | 2.5 |
| масса_кг | 1100 |
| производитель | Скайнет |
| класс | наземный_гусеничный |
| категория | наземный_HK |
| тип_модели | наземный_гусеничный |

## Подсистемы (по типу)

- вычислительная
- энергетическая
- каркас
- броня
- сенсоры
- приводная_система
- система_связи
- навигация
- система_питания
- система_передвижения

## Многослойная броня (§11.6)

Минимум слоёв по типу: 4 (§11.6). Макс. доля массы брони: 50%.

1. B₄C (внешний) (`b4c`)
2. RHA steel (кин.) (`rha_steel`)
3. UHMWPE (арамидный) (`uhmwpe_dyneema`)
4. Резина (подложка) (`rubber`)

## Произведения, где появляется

- 📚 `work_046` — «Terminator: Resistance» (2019) → [`work_046.md`](../произведения/work_046.md)

## Источники

- Канон: Terminator: Resistance (2019) — уточняется по веб-данным: происхождение T-500 — The Terminator: Dawn of Fate (2002); в T: Resistance (2019) серия не фигурирует
- [T-500 | Villains Wiki — Fandom](https://villains.fandom.com/wiki/T-500) — Cyberdyne Systems Series 500 Armored Battle Chassis; происхождение The Terminator: Dawn of Fate; «preferred soldiers» Skynet 2027, преемники T-400; последние спец. гуманоидные HK перед эндоскелетами; заменены T-600; ходячее шасси, лазеры, синхронизация с ИИ; кожа на части юнитов; сходство с T-70/T-800 (проверено 2026-11-06 через web.archive.org)
- [T-500 | Terminator Wiki — Fandom](https://terminator.fandom.com/wiki/T-500) — «T-500 Endo, or Cyberdyne Systems Series 500 Armored Battle Chassis» (проверено 2026-11-06 через web.archive.org)
- [T500 Technical Data — goingfaster.com (фанатская ТТХ Terminator: 2029)](https://www.goingfaster.com/term2029/t500techdata.html) — Endoskeleton Series 500 Model 100 (Infiltrator/Terminator); первый эндоскелетный HK; гиперсплав 0,5 см; 2 м / ~400 кг; 60–75 км/ч; Westinghouse M25A1 plasma rifle; режимы direct/automatic/autonomous; память read-only; потери Сопротивления 80:1 (проверено 2026-11-06; НЕОФИЦИАЛЬНАЯ фанатская документация)
