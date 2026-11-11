---
id: SkyNet-T70
web_verification: terminator.fandom.com/wiki/T-70 (T2 3D) (2026-11-03)
тактико_технические_характеристики:
  мобильность:
    максимальная_скорость_км_ч: 30
    масса_kg: 220
тип: модель_SkyNet
класс: гуманоидный
категория: ранняя_наземная
тип_модели: гуманоидный
источник_происхождения: игра
функции:
- охрана
- штурм
- прототип
канон_источник: 'T2 3D: Battle Across Time (1996)'
произведения:
- work_050
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
  successor_of: SkyNet-T600
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
источник_url: https://terminator.fandom.com/wiki/T-70
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
    min: 200.0
    max: 240.0
    nominal: 220.0
  рост_m: 2.4
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
    - 200.0
    - 240.0
    единица: kg
  - имя: рост_единицы
    диапазон:
    - 2.3
    - 2.5
    единица: m
  пределы:
    max_единиц_в_системе: 1000
    min_массы: 200.0
    max_массы: 240.0
  закон_масштабирования: 'линейный — масса_парка = N × масса_единицы; canon: T-70
    (T2 3D Battle Across Time 1996), 8 ft tall (2.4m), 220 kg, early hydraulic Terminator,
    базовый пехотинец Skynet'
  ограничивающие_части:
  - izdelie_tverdooksidnyi_topливnyi_element (SOFC — критическая зависимость)
  - izdelie_bldc_enkoder (BLDC/hydraulic приводы — early Terminator hydraulics)
наследуемые_материалы:
- материал: b4c
  суммарная_доля_массы: 0.12
  источники_частей:
  - многослойная_броня_слой_1
  форма: баллистическая_керамика
- материал: ti-6al-4v
  суммарная_доля_массы: 0.4
  источники_частей:
  - многослойная_броня_слой_2
  - endoskeleton
  форма: планер_и_космические_изделия
- материал: uhmwpe
  суммарная_доля_массы: 0.06
  источники_частей:
  - многослойная_броня_слой_3
  форма: высоконагруженные_тонкие_шнуры
дата_обновления: '2026-11-11'
---
## Описание

Прототип гуманоидного терминатора Скайнет; первая бипедальная модель; рост ~2.5м, цельнометаллический эндоскелет без живой ткани.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| масса | 200.0–240.0 (номинал 220.0) | kg | canon |
| тип узла | модель_SkyNet | — | canon |
| уровень_номер | 1 | — | canon |


## Источники

- Канон: T2 3D: Battle Across Time (1996)

## Декомпозиция

```mermaid
graph TD
    SkyNet_T70["SkyNet-T70"]
    izdelie_tverdooksidnyi_top___nyi_element["izdelie_tverdooksidnyi_topливnyi_element"]
    SkyNet_T70 --> izdelie_tverdooksidnyi_top___nyi_element
    izdelie_SkyNet_HKAerial["izdelie_SkyNet-HKAerial"]
    SkyNet_T70 --> izdelie_SkyNet_HKAerial
    izdelie_SkyNet_Cameron["izdelie_SkyNet-Cameron"]
    SkyNet_T70 --> izdelie_SkyNet_Cameron
    izdelie_lidar_robosense_ac1["izdelie_lidar_robosense_ac1"]
    SkyNet_T70 --> izdelie_lidar_robosense_ac1
    izdelie_radiatsionno_stoikii_neiromorfnyi_tmr["izdelie_radiatsionno-stoikii_neiromorfnyi_tmr"]
    SkyNet_T70 --> izdelie_radiatsionno_stoikii_neiromorfnyi_tmr
    izdelie_bldc_enkoder["izdelie_bldc_enkoder"]
    SkyNet_T70 --> izdelie_bldc_enkoder
```


## Источник канон

- **Произведение:** T2 3D: Battle Across Time (1996)
- **Тип:** игра
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| рост_см | 250 |
| масса_кг | 250 |
| производитель | Скайнет |
| класс | гуманоидный |
| категория | ранняя_наземная |
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

- 📚 `work_050` — «T2 3D: Battle Across Time» (1996) → [`work_050.md`](../произведения/work_050.md)
