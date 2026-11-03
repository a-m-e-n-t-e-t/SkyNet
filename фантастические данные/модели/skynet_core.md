---
id: SkyNet-Core
тип: модель_SkyNet
класс: стационарный
категория: ИИ-ядро
тип_модели: стационарный
источник_происхождения: фильм
функции: ["центральный ИИ", "командование", "управление"]
канон_источник: Все произведения
произведения: ["work_001", "work_002", "work_003", "work_004", "work_005", "work_006", "work_007", "work_008", "work_009", "work_010", "work_011", "work_012", "work_013", "work_014", "work_015", "work_016", "work_017", "work_018", "work_019", "work_020", "work_021", "work_022", "work_023", "work_024", "work_025", "work_026", "work_027", "work_028", "work_029", "work_030", "work_031", "work_032", "work_033", "work_034", "work_035", "work_036", "work_037", "work_038", "work_039", "work_040", "work_041", "work_042", "work_043", "work_044", "work_045", "work_046", "work_047", "work_048", "work_049", "work_050", "work_051", "work_052"]
производитель: Cyberdyne Systems
статус_реальности: canon
подтип_модели: стандартный
многослойная_броня:
  слои:
    - номер: 1
      материал: b4c  # B₄C
      толщина_мм: {min: 2, target: 10}
    - номер: 2
      материал: rha_steel  # RHA
      толщина_мм: {min: 2, target: 10}
    - номер: 3
      материал: ti6al4v  # Ti-6Al-4V
      толщина_мм: {min: 2, target: 10}
    - номер: 4
      материал: uhmwpe_dyneema  # UHMWPE
      толщина_мм: {min: 2, target: 10}
    - номер: 5
      материал: era_block  # ERA (опционально)
      толщина_мм: {min: 2, target: 10}
  тип_брони: стационарный
  соответствует_типу_модели: true  # F74, max_mass_percent: 100, min_layers: 5
доступность: фантастический
expected_subsystems: ["вычислительная", "энергетическая", "каркас", "броня", "сенсоры", "система_связи", "система_охлаждения"]
relations:
  successor_of: null
  variation_of: null
  hybrid_of: []
  paradigm_shift_from: null
реализация_промышленная: 
  - izdelie_halve
  - izdelie_kondensatory_keramicheskie
  - izdelie_sic_mosfet
  - izdelie_tverdooksidnyi_toplivnyi_element
  - izdelie_nasa_asc-e_srsc
  - izdelie_superkondensatory
  - izdelie_loop_heat_pipe
  - izdelie_kapillyarnaya_teplovaya_trubka
  - izdelie_mikrokanalnye_ohlazhdayuschie_plastiny
  - izdelie_radiatsionno-stoikii_neiromorfnyi_tmr
  - izdelie_razryvnye_mufty_iso_16028
  - izdelie_flat-face_couplings_iso_16028
реализация_ии: []
источник: web_search
источник_разбора: канон
ии_перепроектирован:
  статус: false
  верификация: []
# v9.31: структурные поля §12.4.1-§12.4.X — добавлены как placeholder
# Реальные значения будут заполнены через web_search для каждой модели.
требования_выживаемости: 
  эми_защита: hardened (faraday cage вокруг серверной)
  термобарьер:
          рабочий_диапазон_C:
                      min: 10
                      target: 30
  физическая_защита: серверная в бункере (Skynet Core)
маскировка_инфильтратора: n/a
тактико_технические_характеристики: 
  мобильность: стационарный (серверная в бункере)
  сознание: Skynet — artificial neural network-based conscious group mind (canon Wikipedia)
защита_от_собственной_радиации: n/a (или радиационная защита для бункера)
кибербезопасность: 
  аппаратные_меры:
          HSM: true
          secure_boot: true
          TPM: true
          anti_tamper: zeroization
  iff: SkyNet IFF v3.1 (transponder 1090 MHz + crypto)
  шифрование: AES-256 + SkyNet proprietary
  skynet_protocol: Hive (collective consciousness) или Rogue (autonomous)
эмс_внутренняя: faraday cage + UPS
компоновка_изделий: серверная стойка + резервирование
трассировка_соединителей: []
программное_обеспечение: 'Neural Net CPU + SkyNet OS (Hive mode по умолчанию, Rogue для автономных)'
единая_эми_стратегия: n/a (стационарная)
единая_герметичность: IP55 (серверная)
сертификация_модели_целого: 
  тест_skyet: phase_5 (F70 metrics PASS)
  канон_верификация: 'источник_разбора=канон'
журнал_экземпляра: SkyNet core infrastructure log
утилизация_после_120_лет: 'T-800: 120 лет на 1 топливной ячейке (canon); после истощения — замена ячеек или разборка на запчасти'
экипаж_оператор: 0
промышленная_база: Skynet automated factory (Cyberdyne Systems / CRS)
alice_specs: ALICE sync protocol v9.31 (SkyNet hive-mind)
original_improved: canon
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
---
# SkyNet-Core

## Описание

Skynet Core — центральный ИИ Скайнет; основное вычислительное ядро; инициатор Судного дня; самоосознающий; координатор всех моделей.

## Источник канон

- **Произведение:** Все произведения
- **Тип:** фильм
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| мощность_кВт | 50000 |
| производитель | Cyberdyne Systems |
| класс | стационарный |
| категория | ИИ-ядро |
| тип_модели | стационарный |

## Подсистемы (по типу)

- вычислительная
- энергетическая
- каркас
- броня
- сенсоры
- система_связи
- система_охлаждения

## Многослойная броня (§11.6)

Минимум слоёв по типу: 5 (§11.6). Макс. доля массы брони: 100%.

1. B₄C (`b4c`)
2. RHA (`rha_steel`)
3. Ti-6Al-4V (`ti6al4v`)
4. UHMWPE (`uhmwpe_dyneema`)
5. ERA (опционально) (`era_block`)

## Произведения, где появляется

- ✅ `work_001` — «The Terminator» (1984) → [`work_001.md`](../произведения/work_001.md)
- ✅ `work_002` — «Terminator 2: Judgment Day» (1991) → [`work_002.md`](../произведения/work_002.md)
- ✅ `work_003` — «Terminator 3: Rise of the Machines» (2003) → [`work_003.md`](../произведения/work_003.md)
- ✅ `work_004` — «Terminator Salvation» (2009) → [`work_004.md`](../произведения/work_004.md)
- ✅ `work_005` — «Terminator Genisys» (2015) → [`work_005.md`](../произведения/work_005.md)
- ✅ `work_006` — «Terminator: Dark Fate» (2019) → [`work_006.md`](../произведения/work_006.md)
- ✅ `work_007` — «Terminator: The Sarah Connor Chronicles» (2008) → [`work_007.md`](../произведения/work_007.md)
- ✅ `work_008` — «Terminator Zero» (2024) → [`work_008.md`](../произведения/work_008.md)
- 📚 `work_009` — «The Terminator (novelization)» (1984) → [`work_009.md`](../произведения/work_009.md)
- 📚 `work_010` — «T2: Judgment Day (novelization)» (1991) → [`work_010.md`](../произведения/work_010.md)
- 📚 `work_011` — «T2: Infiltrator» (2001) → [`work_011.md`](../произведения/work_011.md)
- 📚 `work_012` — «T2: Rising Storm» (2003) → [`work_012.md`](../произведения/work_012.md)
- 📚 `work_013` — «T2: Future War» (2004) → [`work_013.md`](../произведения/work_013.md)
- 📚 `work_014` — «T2: The New John Connor Chronicles» (2002) → [`work_014.md`](../произведения/work_014.md)
- 📚 `work_015` — «Terminator 3: Rise of the Machines (novelization)» (2003) → [`work_015.md`](../произведения/work_015.md)
- 📚 `work_016` — «Terminator Salvation: Cold War» (2009) → [`work_016.md`](../произведения/work_016.md)
- 📚 `work_017` — «Terminator Salvation: Trial by Fire» (2010) → [`work_017.md`](../произведения/work_017.md)
- 📚 `work_018` — «Terminator Salvation: From the Ashes» (2009) → [`work_018.md`](../произведения/work_018.md)
- 📚 `work_019` — «Terminator: Hunt for the Dark Fate» (2019) → [`work_019.md`](../произведения/work_019.md)
- 📚 `work_020` — «Now Comics Terminator» (1990) → [`work_020.md`](../произведения/work_020.md)
- 📚 `work_021` — «Dark Horse Comics Terminator» (1990) → [`work_021.md`](../произведения/work_021.md)
- 📚 `work_022` — «Terminator: Tempest» (1992) → [`work_022.md`](../произведения/work_022.md)
- 📚 `work_023` — «Terminator: Secondary Objectives» (1992) → [`work_023.md`](../произведения/work_023.md)
- 📚 `work_024` — «Terminator: The Enemy Within» (1992) → [`work_024.md`](../произведения/work_024.md)
- 📚 `work_025` — «Terminator: End Game» (1992) → [`work_025.md`](../произведения/work_025.md)
- 📚 `work_026` — «Terminator/Robocop: Kill Your Machine» (1992) → [`work_026.md`](../произведения/work_026.md)
- 📚 `work_027` — «Robocop vs. Terminator» (1993) → [`work_027.md`](../произведения/work_027.md)
- 📚 `work_028` — «Superman vs. Terminator: Death to the Future» (1999) → [`work_028.md`](../произведения/work_028.md)
- 📚 `work_029` — «Alien vs. Predator vs. Terminator» (2000) → [`work_029.md`](../произведения/work_029.md)
- 📚 `work_030` — «Terminator: Infinity» (2007) → [`work_030.md`](../произведения/work_030.md)
- 📚 `work_031` — «Terminator: Revolution» (2009) → [`work_031.md`](../произведения/work_031.md)
- 📚 `work_032` — «Terminator: 2029-2029» (2010) → [`work_032.md`](../произведения/work_032.md)
- 📚 `work_033` — «Terminator: Salvation - The Final Battle» (2013) → [`work_033.md`](../произведения/work_033.md)
- 📚 `work_034` — «Terminator: Enemy of My Enemy» (2014) → [`work_034.md`](../произведения/work_034.md)
- 📚 `work_035` — «Terminator: Sector War» (2018) → [`work_035.md`](../произведения/work_035.md)
- 📚 `work_036` — «Marvel's Terminator» (2025) → [`work_036.md`](../произведения/work_036.md)
- 📚 `work_037` — «The Terminator (DOS)» (1991) → [`work_037.md`](../произведения/work_037.md)
- 📚 `work_038` — «Terminator 2029» (1992) → [`work_038.md`](../произведения/work_038.md)
- 📚 `work_039` — «RoboCop versus The Terminator» (1993) → [`work_039.md`](../произведения/work_039.md)
- 📚 `work_040` — «Terminator 2: Judgment Day (arcade)» (1991) → [`work_040.md`](../произведения/work_040.md)
- 📚 `work_041` — «Terminator 2: Judgment Day - Chess Wars» (1993) → [`work_041.md`](../произведения/work_041.md)
- 📚 `work_042` — «Terminator: Dawn of Fate» (2002) → [`work_042.md`](../произведения/work_042.md)
- 📚 `work_043` — «Terminator 3: Rise of the Machines» (2003) → [`work_043.md`](../произведения/work_043.md)
- 📚 `work_044` — «Terminator 3: The Redemption» (2004) → [`work_044.md`](../произведения/work_044.md)
- 📚 `work_045` — «Terminator: Salvation (game)» (2009) → [`work_045.md`](../произведения/work_045.md)
- 📚 `work_046` — «Terminator: Resistance» (2019) → [`work_046.md`](../произведения/work_046.md)
- 📚 `work_047` — «Terminator: Dark Fate — Defiance» (2023) → [`work_047.md`](../произведения/work_047.md)
- 📚 `work_048` — «Terminator: Survivors» (2025) → [`work_048.md`](../произведения/work_048.md)
- 📚 `work_049` — «Terminator Genisys: Future War» (2017) → [`work_049.md`](../произведения/work_049.md)
- 📚 `work_050` — «T2 3D: Battle Across Time» (1996) → [`work_050.md`](../произведения/work_050.md)
- 📚 `work_051` — «T2: Super Nintendo» (1993) → [`work_051.md`](../произведения/work_051.md)
- ✅ `work_052` — «Legion» (2019) → [`work_052.md`](../произведения/work_052.md)

## Источники

- Канон: Все произведения
