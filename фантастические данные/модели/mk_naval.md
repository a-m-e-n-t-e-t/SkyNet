---
id: SkyNet-MKNaval
тип: модель_SkyNet
класс: водный_надводный
категория: водный_HK
тип_модели: водный_надводный
источник_происхождения: игра
функции: ["патруль", "штурм"]
канон_источник: Terminator: Resistance (2019)
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
  тип_брони: водный_надводный
  соответствует_типу_модели: true  # F74, max_mass_percent: 30, min_layers: 4
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
  - izdelie_reshetchatyi_karkas
  - izdelie_kompensatory
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
источник_разбора: канон
ии_перепроектирован:
  статус: false
  верификация: []
# v9.31: структурные поля §12.4.1-§12.4.X — добавлены как placeholder
# Реальные значения будут заполнены через web_search для каждой модели.
требования_выживаемости: 
  эми_защита: hardened
  термобарьер: морозостойкий (-2°C морская вода)
  коррозия: защита от морской соли
маскировка_инфильтратора: n/a
тактико_технические_характеристики: 
  мобильность:
          скорость_узлы: 30
  вооружение: плазма-пушки + торпеды
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
эмс_внутренняя: naval ECM
компоновка_изделий: катамаран/монокорпус
трассировка_соединителей: []
программное_обеспечение: 'Neural Net CPU + SkyNet OS (Hive mode по умолчанию, Rogue для автономных)'
единая_эми_стратегия: SkyNet sea supremacy
единая_герметичность: IP68 (постоянное погружение)
сертификация_модели_целого: 
  тест_skyet: phase_5 (F70 metrics PASS)
  канон_верификация: 'источник_разбора=канон'
журнал_экземпляра: SkyNet naval unit registry
утилизация_после_120_лет: 'T-800: 120 лет на 1 топливной ячейке (canon); после истощения — замена ячеек или разборка на запчасти'
экипаж_оператор: 0
промышленная_база: Skynet automated factory (Cyberdyne Systems / CRS)
alice_specs: ALICE sync protocol v9.31 (SkyNet hive-mind)
original_improved: canon
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
---
# SkyNet-MKNaval

## Описание

MK-Naval — надводный корабль-охотник; винт; плазменное вооружение; эскорт HK-Sub.

## Источник канон

- **Произведение:** Terminator: Resistance (2019)
- **Тип:** игра
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| водоизмещение_т | 150 |
| масса_кг | 150000 |
| производитель | Скайнет |
| класс | водный_надводный |
| категория | водный_HK |
| тип_модели | водный_надводный |

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

Минимум слоёв по типу: 4 (§11.6). Макс. доля массы брони: 30%.

1. Антикор. сталь (`anticorrosive_steel`)
2. RHA (`rha_steel`)
3. UHMWPE (`uhmwpe_dyneema`)
4. Резина (`rubber`)

## Произведения, где появляется

- 📚 `work_046` — «Terminator: Resistance» (2019) → [`work_046.md`](../произведения/work_046.md)

## Источники

- Канон: Terminator: Resistance (2019)
