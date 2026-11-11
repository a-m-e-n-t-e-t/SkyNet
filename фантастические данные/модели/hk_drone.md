---
id: SkyNet-HKDrone
web_verification: terminator.fandom.com/wiki/HK-Drone (2026-11-03)
тактико_технические_характеристики:
  мобильность:
    скорость_км_ч: 400
    тип: VTOL
тип: модель_SkyNet
класс: воздушный
категория: воздушный_HK
тип_модели: воздушный
источник_происхождения: фильм
функции:
- разведка
- патруль
канон_источник: 'T2: Judgment Day (1991), T: Salvation (2009)'
произведения:
- work_002
- work_004
- work_045
производитель: Скайнет
статус_реальности: canon
подтип_модели: стандартный
многослойная_броня:
  слои:
  - номер: 1
    материал: al_6061_t6
    толщина_мм:
      min: 2
      target: 10
  - номер: 2
    материал: uhmwpe_dyneema
    толщина_мм:
      min: 2
      target: 10
  тип_брони: воздушный
  соответствует_типу_модели: true
доступность: фантастический
expected_subsystems:
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
источник_разбора: канон
ии_перепроектирован:
  статус: false
  верификация: []
источник_url: https://terminator.fandom.com/wiki/HK-Drone
источник_дата: '2026-11-11'
уровень_иерархии: верхний
уровень_номер: 1
дочерние_части:
- izdelie_tverdooksidnyi_topливnyi_element
- izdelie_SkyNet-HKAerial
- izdelie_lidar_robosense_ac1
- izdelie_radiatsionno-stoikii_neiromorfnyi_tmr
- izdelie_bldc_enkoder
основные:
  масса_kg:
    min: 100.0
    max: 200.0
    nominal: 136.0
  размах_крыльев_m: 1.8
масштабируемость:
  режим: квантуемая
  параметры:
  - имя: количество_единиц
    диапазон:
    - 1
    - 500
    единица: шт
  - имя: масса_единицы
    диапазон:
    - 100.0
    - 200.0
    единица: kg
  - имя: скорость
    диапазон:
    - 300
    - 500
    единица: km/h
  пределы:
    max_единиц_в_системе: 500
    min_массы: 100.0
    max_массы: 200.0
    min_скорости: 300
    max_скорости: 500
  закон_масштабирования: 'линейный — масса_парка = N × масса_единицы; canon: HK-Drone
    (T3 2003), 1.8m wingspan, 136 kg, VTOL, 2 machine guns + 2 missile pods; prototype
    for HK-Aerial'
  ограничивающие_части:
  - izdelie_tverdooksidnyi_topливnyi_element (SOFC — критическая зависимость)
  - izdelie_bldc_enkoder (BLDC motors for VTOL)
наследуемые_материалы:
- материал: al_6061-t6
  суммарная_доля_массы: 0.55
  источники_частей:
  - многослойная_броня_слой_1
  - endoskeleton
  форма: силовые_элементы_конструкций
- материал: uhmwpe
  суммарная_доля_массы: 0.05
  источники_частей:
  - многослойная_броня_слой_2
  форма: высоконагруженные_тонкие_шнуры
дата_обновления: '2026-11-11'
---
## Описание

HK-Drone — малый беспилотник; винтокрылый; автономный патруль; не имеет оружия или лёгкое.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| масса | 100.0–200.0 (номинал 136.0) | kg | canon |
| тип узла | модель_SkyNet | — | canon |
| уровень_номер | 1 | — | canon |


## Источники

- Канон: T2: Judgment Day (1991), T: Salvation (2009)

## Декомпозиция

```mermaid
graph TD
    SkyNet_HKDrone["SkyNet-HKDrone"]
    izdelie_tverdooksidnyi_top___nyi_element["izdelie_tverdooksidnyi_topливnyi_element"]
    SkyNet_HKDrone --> izdelie_tverdooksidnyi_top___nyi_element
    izdelie_SkyNet_HKAerial["izdelie_SkyNet-HKAerial"]
    SkyNet_HKDrone --> izdelie_SkyNet_HKAerial
    izdelie_lidar_robosense_ac1["izdelie_lidar_robosense_ac1"]
    SkyNet_HKDrone --> izdelie_lidar_robosense_ac1
    izdelie_radiatsionno_stoikii_neiromorfnyi_tmr["izdelie_radiatsionno-stoikii_neiromorfnyi_tmr"]
    SkyNet_HKDrone --> izdelie_radiatsionno_stoikii_neiromorfnyi_tmr
    izdelie_bldc_enkoder["izdelie_bldc_enkoder"]
    SkyNet_HKDrone --> izdelie_bldc_enkoder
```


## Источник канон

- **Произведение:** T2: Judgment Day (1991), T: Salvation (2009)
- **Тип:** фильм
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| размах_крыльев_м | 3 |
| масса_кг | 80 |
| производитель | Скайнет |
| класс | воздушный |
| категория | воздушный_HK |
| тип_модели | воздушный |

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

Минимум слоёв по типу: 2 (§11.6). Макс. доля массы брони: 15%.

1. Al 6061-T6 (лёгкий кин.) (`al_6061_t6`)
2. UHMWPE (энергопоглощение) (`uhmwpe_dyneema`)

## Произведения, где появляется

- ✅ `work_002` — «Terminator 2: Judgment Day» (1991) → [`work_002.md`](../произведения/work_002.md)
- ✅ `work_004` — «Terminator Salvation» (2009) → [`work_004.md`](../произведения/work_004.md)
- 📚 `work_045` — «Terminator: Salvation (game)» (2009) → [`work_045.md`](../произведения/work_045.md)
