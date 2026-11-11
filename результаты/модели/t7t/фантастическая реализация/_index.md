---
id: SkyNet-T7T
тип: модель_SkyNet
класс: наземный_гусеничный
категория: наземный_HK
тип_модели: наземный_гусеничный
источник_происхождения: игра
функции: ["штурм", "тяжёлая поддержка"]
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
источник_url: 'https://terminator.fandom.com/wiki/T-7T'
источник_дата: 2026-11-06
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
# SkyNet-T7T

## Описание

T-7T «Spider» — многоногий танк-паук; 6-8 ног; тяжёлое вооружение; аналог шагохода.

По верифицированным данным Fandom (проверено 2026-11-06): T-7T Tetrapod, прозвище «Spider» у Сопротивления — Skynet Terminator series и quadruped Hunter-Killer (четырёхногий), используемый для обороны ключевых точек (в т.ч. завод терминаторов и плазменные турели в Skynet City); для уничтожения в игре обычно требуется ракетное вооружение — в бою выступает боссом (HK Tank-стиль). Примечание: канон говорит о четырёх конечностях (Tetrapod), тогда как раннее описание в этом файле указывало 6–8 ног; таксономическое поле класс (наземный_гусеничный) сохранено для совместимости классификатора F13/F33 (отдельный шаг реклассификации).

## Источник канон

- **Произведение:** Terminator: Resistance (2019)
- **Тип:** игра
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| длина_гусеницы_м | 4 |
| масса_кг | 3000 |
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

- Канон: Terminator: Resistance (2019)
- [T-7T | Terminator Wiki — Fandom](https://terminator.fandom.com/wiki/T-7T) — Tetrapod («Spider»), quadruped Hunter-Killer, оборона ключевых точек, босс-бой в T: Resistance (проверено 2026-11-06)
