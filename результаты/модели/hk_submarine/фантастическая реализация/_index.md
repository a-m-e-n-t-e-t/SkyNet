---
id: SkyNet-HKSubmarine
web_verification: The Terminator (1984) — mentioned by Kyle Reese
тактико_технические_характеристики:
  мобильность:
    скорость_узлы: 25
    глубина_m: 300
тип: модель_SkyNet
класс: водный_подводный
категория: водный_HK
тип_модели: водный_подводный
источник_происхождения: фильм
функции:
- патруль
- охрана водных путей
- штурм
канон_источник: The Terminator (1984) [mentioned]
произведения:
- work_001
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
источник_url: https://terminator.fandom.com/wiki/Hunter-Killer
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
    min: 50000.0
    max: 200000.0
    nominal: 100000.0
  длина_m: 30.0
масштабируемость:
  режим: квантуемая
  параметры:
  - имя: количество_единиц
    диапазон:
    - 1
    - 50
    единица: шт
  - имя: масса_единицы
    диапазон:
    - 50000.0
    - 200000.0
    единица: kg
  - имя: скорость
    диапазон:
    - 20
    - 30
    единица: knots
  - имя: глубина_погружения
    диапазон:
    - 200
    - 500
    единица: m
  пределы:
    max_единиц_в_системе: 50
    min_массы: 50000.0
    max_массы: 200000.0
    min_глубины: 200
    max_глубины: 500
  закон_масштабирования: 'линейный — масса_флота = N × масса_единицы; canon: HK-Submarine
    (The Terminator 1984, mentioned by Kyle Reese), 25 knots, 300m depth, patrol water
    routes'
  ограничивающие_части:
  - izdelie_tverdooksidnyi_topливnyi_element (SOFC for underwater power — критическая
    зависимость)
  - izdelie_bldc_enkoder (electric propulsion for stealth)
наследуемые_материалы:
- материал: ti-6al-4v
  суммарная_доля_массы: 0.5
  источники_частей:
  - многослойная_броня_слой_2
  - hull
  форма: планер_и_космические_изделия
- материал: uhmwpe
  суммарная_доля_массы: 0.04
  источники_частей:
  - многослойная_броня_слой_3
  форма: высоконагруженные_тонкие_шнуры
дата_обновления: '2026-11-11'
---
## Описание

Hunter-Killer Submarine — подводный охотник; SONAR; ракетное вооружение; упоминается в каноне T1.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| масса | 50000.0–200000.0 (номинал 100000.0) | kg | canon |
| тип узла | модель_SkyNet | — | canon |
| уровень_номер | 1 | — | canon |


## Источники

- Канон: The Terminator (1984) [mentioned]

## Декомпозиция

```mermaid
graph TD
    SkyNet_HKSubmarine["SkyNet-HKSubmarine"]
    izdelie_tverdooksidnyi_top___nyi_element["izdelie_tverdooksidnyi_topливnyi_element"]
    SkyNet_HKSubmarine --> izdelie_tverdooksidnyi_top___nyi_element
    izdelie_lidar_robosense_ac1["izdelie_lidar_robosense_ac1"]
    SkyNet_HKSubmarine --> izdelie_lidar_robosense_ac1
    izdelie_radiatsionno_stoikii_neiromorfnyi_tmr["izdelie_radiatsionno-stoikii_neiromorfnyi_tmr"]
    SkyNet_HKSubmarine --> izdelie_radiatsionno_stoikii_neiromorfnyi_tmr
    izdelie_bldc_enkoder["izdelie_bldc_enkoder"]
    SkyNet_HKSubmarine --> izdelie_bldc_enkoder
```


## Источник канон

- **Произведение:** The Terminator (1984) [mentioned]
- **Тип:** фильм
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| рабочая_глубина_м | 300 |
| масса_кг | 25000 |
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

- ✅ `work_001` — «The Terminator» (1984) → [`work_001.md`](../произведения/work_001.md)
