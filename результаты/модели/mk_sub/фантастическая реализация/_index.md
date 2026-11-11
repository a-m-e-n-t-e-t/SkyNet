---
id: SkyNet-MKSub
тип: модель_SkyNet
класс: водный_подводный
категория: водный_HK
тип_модели: водный_подводный
источник_происхождения: игра
функции: ["патруль", "разведка"]
канон_источник: 'Terminator: Resistance (2019)'
произведения: ["work_046"]
производитель: Скайнет
статус_реальности: canon
подтип_модели: стандартный
многослойная_броня:
  слои:
    - номер: 1
      материал: anticorrosive_steel  # Антикор. сталь
      толщина_мм: {min: 2, target: 10}
    - номер: 2
      материал: rha_steel  # RHA
      толщина_мм: {min: 2, target: 10}
    - номер: 3
      материал: uhmwpe_dyneema  # UHMWPE
      толщина_мм: {min: 2, target: 10}
    - номер: 4
      материал: rubber  # Резина
      толщина_мм: {min: 2, target: 10}
  тип_брони: водный_подводный
  соответствует_типу_модели: true  # F74, max_mass_percent: 35, min_layers: 4
доступность: фантастический
expected_subsystems: ["вычислительная", "энергетическая", "каркас", "броня", "маскировка", "сенсоры", "приводная_система", "система_связи", "навигация", "система_охлаждения", "система_питания", "система_передвижения"]
relations:
  successor_of: SkyNet-HKSubmarine
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
источник_url: 'https://terminator.fandom.com/wiki/Category:Submarines'
источник_дата: 2026-11-06
источник_разбора: канон
ии_перепроектирован:
  статус: false
  верификация: []
---
# v9.31: структурные поля §12.4.1-§12.4.X — добавлены как placeholder
# Реальные значения будут заполнены через web_search для каждой модели.
требования_выживаемости: 
  эми_защита: hardened
  термобарьер: морозостойкий
  давление: до 30 атм (300 м глубина)
маскировка_инфильтратора: n/a
тактико_технические_характеристики: 
  мобильность:
          скорость_узлы: 20
          глубина_m: 300
  вооружение: торпеды
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
эмс_внутренняя: sonar countermeasures
компоновка_изделий: цилиндрический корпус
трассировка_соединителей: []
программное_обеспечение: 'Neural Net CPU + SkyNet OS (Hive mode по умолчанию, Rogue для автономных)'
единая_эми_стратегия: SkyNet underwater supremacy
единая_герметичность: IP68 (300м глубина)
сертификация_модели_целого: 
  тест_skyet: phase_5 (F70 metrics PASS)
  канон_верификация: 'источник_разбора=канон'
журнал_экземпляра: SkyNet underwater unit registry
утилизация_после_120_лет: 'T-800: 120 лет на 1 топливной ячейке (canon); после истощения — замена ячеек или разборка на запчасти'
экипаж_оператор: 0
промышленная_база: Skynet automated factory (Cyberdyne Systems / CRS)
alice_specs: ALICE sync protocol v9.31 (SkyNet hive-mind)
original_improved: canon
дата_создания: 2026-11-03
дата_обновления: 2026-11-06
---
# SkyNet-MKSub

## Описание

MK-Sub — усовершенствованная подводная лодка Скайнет; меньше HK-Sub; специализирована на разведке.

По верифицированным данным веб-поиска (проверено 2026-11-06): обозначение «MK-Sub» НЕ найдено ни в одном канонном источнике франшизы. Категория «Submarines» Terminator Wiki (Fandom, получена через web-архив) содержит ровно 10 подводных машин франшизы — Aquatic Work Bot, ASW Bot, Gorshkov, HK-Hydrofoil, Hydrobot, USS Jimmy Carter, Korolev, Kraken, USS Roosevelt, USS Wilmington — ни одной с префиксом «MK». Атрибуция Resistance (2019) опровергнута полным списком врагов игры (StrategyWiki): базовая игра — Spider Scout, Silverfish, Scout Drone, Armored Drone, Armored Spider, Plasma Turret, T-47, T-800, HK-Aerial, HK-Tank; DLC Annihilation Line — HK-Centurion, T-600, T-650; подводных/морских юнитов в игре нет. Ближайшие канонные аналоги для ниши «малая подводная машина»: HK-Hydrofoil (Cyberdyne Systems C Series Autonomous Submersible Hydroplane, «Sea HK», Skynet 2.0 — гибрид канонерской лодки, подлодки и глиссера), Kraken (класс противолодочной войны Skynet, патрулирует океаны в 2027 г.), Hydrobot (малый подводный инфильтратор), ASW Bot. Файл, по-видимому, порождён процедурой разложения; РАСХОЖДЕНИЕ С ФАЙЛОМ: атрибуция work_046 и идентификатор «MK» источниками не подтверждаются; связь successor_of: SkyNet-HKSubmarine сохранена; таксономия (водный_подводный) оставлена до отдельной реклассификации/слияния с канонными HK-Hydrofoil/Kraken (F13/F33-таксономия), как для T-300 (#705)/T-950 (#708)/T-400 (#707)/T-20 (#709)/T-202 (#712)/T-204 (#710).

## Источник канон

- **Произведение:** Terminator: Resistance (2019)
- **Тип:** игра
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| рабочая_глубина_м | 150 |
| масса_кг | 8000 |
| производитель | Скайнет |
| класс | водный_подводный |
| категория | водный_HK |
| тип_модели | водный_подводный |

## Подсистемы (по типу)

- вычислительная
- энергетическая
- каркас
- броня
- маскировка
- сенсоры
- приводная_система
- система_связи
- навигация
- система_охлаждения
- система_питания
- система_передвижения

## Многослойная броня (§11.6)

Минимум слоёв по типу: 4 (§11.6). Макс. доля массы брони: 35%.

1. Антикор. сталь (`anticorrosive_steel`)
2. RHA (`rha_steel`)
3. UHMWPE (`uhmwpe_dyneema`)
4. Резина (`rubber`)

## Произведения, где появляется

- 📚 `work_046` — «Terminator: Resistance» (2019) → [`work_046.md`](../произведения/work_046.md)

## Источники

- Канон: Terminator: Resistance (2019) — атрибуция опровергнута: в игре нет подводных/морских юнитов (см. описание)
- [Category:Submarines | Terminator Wiki — Fandom](https://terminator.fandom.com/wiki/Category:Submarines) — полный список подводных машин франшизы (10 позиций, без «MK»); проверено 2026-11-06 через web-архив
- [Terminator: Resistance/Enemies — StrategyWiki](https://strategywiki.org/wiki/Terminator:_Resistance/Enemies) — полный список врагов игры (Spider Scout, Silverfish, Scout/Armored Drone, Armored Spider, Plasma Turret, T-47, T-800, HK-Aerial, HK-Tank; DLC: HK-Centurion, T-600, T-650) (проверено 2026-11-06)
- [HK-Hydrofoil | Terminator Wiki — Fandom](https://terminator.fandom.com/wiki/HK-Hydrofoil) — канонный подводный HK Skynet 2.0 (проверено 2026-11-06)
- [Kraken | Terminator Wiki — Fandom](https://terminator.fandom.com/wiki/Kraken) — класс противолодочных машин Skynet, 2027 г. (проверено 2026-11-06)
