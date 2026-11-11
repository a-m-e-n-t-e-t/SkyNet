---
id: SkyNet-Aerostat
web_verification: Terminator Salvation (2009)
тактико_технические_характеристики:
  мобильность:
    тип: aerostat (легче воздуха)
    скорость_км_ч: 80
тип: модель_SkyNet
класс: воздушный
категория: воздушный_HK
тип_модели: воздушный
источник_происхождения: фильм
функции:
- разведка
- патруль
- наблюдение
канон_источник: 'Terminator: Salvation (2009)'
произведения:
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
источник_url: https://terminator.fandom.com/wiki/Aerostat
источник_дата: '2026-11-11'
уровень_иерархии: верхний
уровень_номер: 1
дочерние_части:
- izdelie_tverdooksidnyi_topливnyi_element
- izdelie_lidar_robosense_ac1
- izdelie_radiatsionno-stoikii_neiromorfnyi_tmr
- izdelie_bldc_enkoder
основные:
  масса_kg:
    min: 1.0
    max: 10.0
    nominal: 5.0
  размер_m: 0.5
масштабируемость:
  режим: квантуемая
  параметры:
  - имя: количество_единиц
    диапазон:
    - 1
    - 1000
    единица: шт
  - имя: масса_единицы
    диапазон:
    - 1.0
    - 10.0
    единица: kg
  - имя: скорость
    диапазон:
    - 40
    - 100
    единица: km/h
  пределы:
    max_единиц_в_системе: 1000
    min_массы: 1.0
    max_массы: 10.0
    min_скорости: 40
    max_скорости: 100
  закон_масштабирования: 'линейный — масса_парка = N × масса_единицы; canon: Aerostat
    (Terminator Salvation 2009), car wheel size ~0.5m, turbofan, lighter-than-air,
    scout unit signals Harvesters'
  ограничивающие_части:
  - izdelie_bldc_enkoder (BLDC motor for turbofan — критическая зависимость)
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

Aerostat — малый сферический дрон; плавающий/парящий в воздухе; глаза-сенсоры; мгновенное обнаружение людей.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| масса | 1.0–10.0 (номинал 5.0) | kg | canon |
| тип узла | модель_SkyNet | — | canon |
| уровень_номер | 1 | — | canon |


## Источники

- Канон: Terminator: Salvation (2009)

## Декомпозиция

```mermaid
graph TD
    SkyNet_Aerostat["SkyNet-Aerostat"]
    izdelie_tverdooksidnyi_top___nyi_element["izdelie_tverdooksidnyi_topливnyi_element"]
    SkyNet_Aerostat --> izdelie_tverdooksidnyi_top___nyi_element
    izdelie_lidar_robosense_ac1["izdelie_lidar_robosense_ac1"]
    SkyNet_Aerostat --> izdelie_lidar_robosense_ac1
    izdelie_radiatsionno_stoikii_neiromorfnyi_tmr["izdelie_radiatsionno-stoikii_neiromorfnyi_tmr"]
    SkyNet_Aerostat --> izdelie_radiatsionno_stoikii_neiromorfnyi_tmr
    izdelie_bldc_enkoder["izdelie_bldc_enkoder"]
    SkyNet_Aerostat --> izdelie_bldc_enkoder
```


## Источник канон

- **Произведение:** Terminator: Salvation (2009)
- **Тип:** фильм
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| размах_крыльев_м | 1.2 |
| масса_кг | 25 |
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

- ✅ `work_004` — «Terminator Salvation» (2009) → [`work_004.md`](../произведения/work_004.md)
- 📚 `work_045` — «Terminator: Salvation (game)» (2009) → [`work_045.md`](../произведения/work_045.md)
