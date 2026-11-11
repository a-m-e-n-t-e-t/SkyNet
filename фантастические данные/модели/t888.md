---
id: SkyNet-T888
web_verification: terminator.fandom.com/wiki/T-888 (T:SCC) (2026-11-03)
тактико_технические_характеристики:
  мобильность:
    максимальная_скорость_км_ч: 40
    масса_kg: 180
тип: модель_SkyNet
класс: гуманоидный
категория: стандартный
тип_модели: гуманоидный
источник_происхождения: сериал
функции:
- инфильтрация
- ' assassination'
- телохранитель
канон_источник: 'Terminator: The Sarah Connor Chronicles (2008-2009)'
произведения:
- work_007
производитель: Скайнет
статус_реальности: canon
подтип_модели: стандартный
многослойная_броня:
  слои:
  - номер: 1
    материал: b4c
    толщина_мм:
      min: 2
      target: 10
  - номер: 2
    материал: ti6al4v
    толщина_мм:
      min: 2
      target: 10
  - номер: 3
    материал: uhmwpe_dyneema
    толщина_мм:
      min: 2
      target: 10
  тип_брони: гуманоидный
  соответствует_типу_модели: true
доступность: фантастический
expected_subsystems:
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
relations:
  successor_of: SkyNet-T900
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
источник_url: https://terminator.fandom.com/wiki/T-888
источник_дата: '2026-11-11'
уровень_иерархии: верхний
уровень_номер: 1
дочерние_части:
- izdelie_tverdooksidnyi_topливnyi_element
- izdelie_SkyNet-HKAerial
- izdelie_SkyNet-Cameron
- izdelie_lidar_robosense_ac1
- izdelie_radiatsionno-stoikii_neiromorfnyi_tmr
- izdelie_bldc_enkoder
основные:
  масса_kg:
    min: 170.0
    max: 200.0
    nominal: 180.0
  рост_m: 1.85
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
    - 170.0
    - 200.0
    единица: kg
  - имя: рост_единицы
    диапазон:
    - 1.8
    - 1.9
    единица: m
  пределы:
    max_единиц_в_системе: 1000
    min_массы: 170.0
    max_массы: 200.0
  закон_масштабирования: 'линейный — масса_парка = N × масса_единицы; canon: T-888
    (TSCC 2008-2009), 180 kg, coltan+hyperalloy endoskeleton, 40 km/h, гибче T-800'
  ограничивающие_части:
  - izdelie_tverdooksidnyi_topливnyi_element (SOFC — критическая зависимость)
  - izdelie_radiatsionno-stoikii_neiromorfnyi_tmr (нейроморфный процессор)
  - izdelie_bldc_enkoder (BLDC приводы для конечностей)
наследуемые_материалы:
- материал: b4c
  суммарная_доля_массы: 0.1
  источники_частей:
  - многослойная_броня_слой_1
  форма: баллистическая_керамика
- материал: ti-6al-4v
  суммарная_доля_массы: 0.35
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

T-888 — серия T:SCC; Cromartie (Model 1001), Vick Chamberlain, Carter, Cameron Phillips (перепрограммирован Resistance); улучшенный эндоскелет coltan-tungsten.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| масса | 170.0–200.0 (номинал 180.0) | kg | canon |
| тип узла | модель_SkyNet | — | canon |
| уровень_номер | 1 | — | canon |


## Источники

- Канон: Terminator: The Sarah Connor Chronicles (2008-2009)

## Декомпозиция

```mermaid
graph TD
    SkyNet_T888["SkyNet-T888"]
    izdelie_tverdooksidnyi_top___nyi_element["izdelie_tverdooksidnyi_topливnyi_element"]
    SkyNet_T888 --> izdelie_tverdooksidnyi_top___nyi_element
    izdelie_SkyNet_HKAerial["izdelie_SkyNet-HKAerial"]
    SkyNet_T888 --> izdelie_SkyNet_HKAerial
    izdelie_SkyNet_Cameron["izdelie_SkyNet-Cameron"]
    SkyNet_T888 --> izdelie_SkyNet_Cameron
    izdelie_lidar_robosense_ac1["izdelie_lidar_robosense_ac1"]
    SkyNet_T888 --> izdelie_lidar_robosense_ac1
    izdelie_radiatsionno_stoikii_neiromorfnyi_tmr["izdelie_radiatsionno-stoikii_neiromorfnyi_tmr"]
    SkyNet_T888 --> izdelie_radiatsionno_stoikii_neiromorfnyi_tmr
    izdelie_bldc_enkoder["izdelie_bldc_enkoder"]
    SkyNet_T888 --> izdelie_bldc_enkoder
```


## Источник канон

- **Произведение:** Terminator: The Sarah Connor Chronicles (2008-2009)
- **Тип:** сериал
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| рост_см | 185 |
| масса_кг | 135 |
| производитель | Скайнет |
| класс | гуманоидный |
| категория | стандартный |
| тип_модели | гуманоидный |

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

Минимум слоёв по типу: 3 (§11.6). Макс. доля массы брони: 30%.

1. B₄C керамика (внешний жертвенный) (`b4c`)
2. Ti-6Al-4V (кин. слой) (`ti6al4v`)
3. UHMWPE Dyneema (арамидный подслой) (`uhmwpe_dyneema`)

## Произведения, где появляется

- ✅ `work_007` — «Terminator: The Sarah Connor Chronicles» (2008) → [`work_007.md`](../произведения/work_007.md)
