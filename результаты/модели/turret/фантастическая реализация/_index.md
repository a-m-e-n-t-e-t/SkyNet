---
id: SkyNet-Turret
тип: модель_SkyNet
класс: стационарный
категория: ИИ-ядро
тип_модели: стационарный
источник_происхождения: фильм
функции: ["оборона", "штурм"]
канон_источник: 'T: Salvation (2009)'
произведения: ["work_004"]
производитель: Скайнет
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
источник_url: 'https://terminator.fandom.com/wiki/Turret'
источник_разбора: канон
ии_перепроектирован:
  статус: false
  верификация: []
---
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
  мобильность: стационарная
  вооружение: плазма-пушка
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
дата_обновления: 2026-11-06
---
# SkyNet-Turret

## Описание

Turret — стационарная плазменная пушка; устанавливается на стенах Skynet-объектов; автономная; локальный ИИ.

По верифицированным данным веб-поиска (проверено 2026-11-06, страница Fandom «Turret» выкачана целиком через web.archive.org): Skynet обычно устанавливает турели на крупных объектах как оборонительную сетку (defense grid). Для Salvation-таймлайна (канон файла) описан Gun Turret — стационарная многоствольная турель в двух вариациях: установленная в Skynet VLA с 4 «руками»-стволами и в Skynet Central с 2 «руками». В финале фильма турель Skynet Central просканировала Маркуса Райта и опознала его перед пропуском внутрь; Маркус отключил North Gun Turret, чтобы отряд Tech-Com Джона Коннора смог войти в периметр и атаковать Skynet Central. Семейство турелей канона шире: F/K Turret (таймлайн Rise of the Machines) — неподвижная орудийная батарея для охраны зоны или создания коридоров поражения (kill-zones); F/K Sentry Gun — уменьшенная версия для охраны внутренних помещений объектов Skynet; Plasma Turret (Resistance-таймлайн) — два типа: с красной плазменной ячейкой (2022 г.) и с фиолетовой (2028 г.); Defense Turret установлена снаружи комплекса Skynet у Шайенн-Маунтин. Часть турелей вооружена плазменным оружием; некоторые турели могут быть перехвачены Сопротивлением (захват центра управления). Появления: The Terminator: Future Shock (1995), The Terminator: SkyNET (1996), T2 3-D: Battle Across Time, The Terminator: Dawn of Fate, T3 (игра, 2003), Terminator Salvation (фильм и игра, 2009), Terminator Genisys, Terminator: Resistance, The Terminator RPG. РАСХОЖДЕНИЕ С ФАЙЛОМ: по канону турель — стационарное пушечное/плазменное вооружение оборонительного периметра, а категория «ИИ-ядро» и ТТХ второго YAML-блока (серверная стойка, faraday cage, серверная в бункере) — шаблон SkyNet Core, оставлены до отдельной реклассификации (F13/F33-таксономия), как для T-300 (#705)/T-950 (#708)/T-400 (#707)/T-20 (#709)/T-204 (#710)/T-202 (#712)/T-200 (#713).

## Источник канон

- **Произведение:** T: Salvation (2009)
- **Тип:** фильм
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| мощность_кВт | 15 |
| производитель | Скайнет |
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

- ✅ `work_004` — «Terminator Salvation» (2009) → [`work_004.md`](../произведения/work_004.md)

## Источники

- Канон: T: Salvation (2009) — подтверждается (Gun Turret в Skynet Central/VLA, сцены с Маркусом Райтом)
- [Turret | Terminator Wiki — Fandom](https://terminator.fandom.com/wiki/Turret) — F/K Turret и F/K Sentry Gun (T3), Gun Turret (Salvation: 4 «руки» в VLA, 2 — в Central, сканирование Маркуса, North Gun Turret), Plasma Turret (Resistance: красная 2022/фиолетовая 2028), Defense Turret у Шайенн-Маунтин; список появлений 1995–2019 (проверено 2026-11-06 через web.archive.org)
- [10 Coolest Weapons in the Terminator Movie Franchise — The Flagship Eclipse](https://www.theflagshipeclipse.com/2025/06/17/10-coolest-weapons-in-the-terminator-movie-franchise) — Skynet Gun Turrets (Terminator: Salvation): полностью автоматические турели на заводах, бункерах и оборонительных аванпостах Skynet как эталон обороны периметра (проверено 2026-11-06)
