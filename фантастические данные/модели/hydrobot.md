---
id: SkyNet-Hydrobot
web_verification: Terminator Salvation (2009)
тактико_технические_характеристики:
  мобильность:
    тип: водный змей
    скорость_узлы: 15
тип: модель_SkyNet
класс: водный_подводный
категория: водный_HK
тип_модели: водный_подводный
источник_происхождения: фильм
функции:
- патруль
- охрана водных путей
- штурм
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
    материал: anticorrosive_steel
    толщина_мм:
      min: 2
      target: 10
  - номер: 2
    материал: rha_steel
    толщина_мм:
      min: 2
      target: 10
  - номер: 3
    материал: uhmwpe_dyneema
    толщина_мм:
      min: 2
      target: 10
  - номер: 4
    материал: rubber
    толщина_мм:
      min: 2
      target: 10
  тип_брони: водный_подводный
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
источник_url: https://terminator.fandom.com/wiki/Hydrobot
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
    min: 30.0
    max: 100.0
    nominal: 60.0
  длина_m: 2.0
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
    - 30.0
    - 100.0
    единица: kg
  - имя: скорость
    диапазон:
    - 10
    - 30
    единица: km/h
  пределы:
    max_единиц_в_системе: 500
    min_массы: 30.0
    max_массы: 100.0
    min_скорости: 10
    max_скорости: 30
  закон_масштабирования: 'линейный — масса_парка = N × масса_единицы; canon: Hydrobot
    (Terminator Salvation 2009), serpent-like water unit, 15 knots (28 km/h), claw
    head, patrols water'
  ограничивающие_части:
  - izdelie_tverdooksidnyi_topливnyi_element (SOFC — критическая зависимость)
  - izdelie_bldc_enkoder (BLDC motors for aquatic propulsion)
наследуемые_материалы:
- материал: ti-6al-4v
  суммарная_доля_массы: 0.4
  источники_частей:
  - многослойная_броня_слой_2
  - endoskeleton
  форма: планер_и_космические_изделия
- материал: uhmwpe
  суммарная_доля_массы: 0.05
  источники_частей:
  - многослойная_броня_слой_3
  форма: высоконагруженные_тонкие_шнуры
дата_обновления: '2026-11-11'
---
## Описание

Hydrobot — змееобразный водный терминатор; плавающий; хватательные манипуляторы-«зубы»; патрулирует реки и каналы.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| масса | 30.0–100.0 (номинал 60.0) | kg | canon |
| тип узла | модель_SkyNet | — | canon |
| уровень_номер | 1 | — | canon |


## Источники

- Канон: Terminator: Salvation (2009)

## Декомпозиция

```mermaid
graph TD
    SkyNet_Hydrobot["SkyNet-Hydrobot"]
    izdelie_tverdooksidnyi_top___nyi_element["izdelie_tverdooksidnyi_topливnyi_element"]
    SkyNet_Hydrobot --> izdelie_tverdooksidnyi_top___nyi_element
    izdelie_lidar_robosense_ac1["izdelie_lidar_robosense_ac1"]
    SkyNet_Hydrobot --> izdelie_lidar_robosense_ac1
    izdelie_radiatsionno_stoikii_neiromorfnyi_tmr["izdelie_radiatsionno-stoikii_neiromorfnyi_tmr"]
    SkyNet_Hydrobot --> izdelie_radiatsionno_stoikii_neiromorfnyi_tmr
    izdelie_bldc_enkoder["izdelie_bldc_enkoder"]
    SkyNet_Hydrobot --> izdelie_bldc_enkoder
```


## Источник канон

- **Произведение:** Terminator: Salvation (2009)
- **Тип:** фильм
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| рабочая_глубина_м | 50 |
| масса_кг | 600 |
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

- ✅ `work_004` — «Terminator Salvation» (2009) → [`work_004.md`](../произведения/work_004.md)
- 📚 `work_045` — «Terminator: Salvation (game)» (2009) → [`work_045.md`](../произведения/work_045.md)
