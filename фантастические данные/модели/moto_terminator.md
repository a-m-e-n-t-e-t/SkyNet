---
id: SkyNet-MotoTerminator
web_verification: terminator.fandom.com/wiki/Moto-Terminator (2026-11-03)
тактико_технические_характеристики:
  мобильность:
    скорость_км_ч: 322
    тип: мотоциклетный
  вооружение: plasma_emitters
тип: модель_SkyNet
класс: наземный_колёсный
категория: наземный_HK
тип_модели: наземный_колёсный
источник_происхождения: фильм
функции:
- преследование
- патруль
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
  тип_брони: наземный_колёсный
  соответствует_типу_модели: true
доступность: фантастический
expected_subsystems:
- вычислительная
- энергетическая
- каркас
- сенсоры
- приводная_система
- система_связи
- навигация
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
источник_url: https://terminator.fandom.com/wiki/Moto-Terminator
источник_дата: '2026-11-11'
уровень_иерархии: верхний
уровень_номер: 1
дочерние_части:
- izdelie_tverdooksidnyi_toplivnyi_element
- izdelie_SkyNet-HKAerial
- izdelie_lidar_robosense_ac1
- izdelie_radiatsionno-stoikii_neiromorfnyi_tmr
- izdelie_bldc_enkoder
основные:
  масса_kg:
    min: 180.0
    max: 250.0
    nominal: 220.0
  габариты_mm:
    l: 2100
    w: 800
    h: 1100
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
    - 180.0
    - 250.0
    единица: kg
  - имя: скорость
    диапазон:
    - 200
    - 322
    единица: km/h
  пределы:
    max_единиц_в_системе: 1000
    min_массы: 180.0
    max_массы: 250.0
    min_скорости: 200
    max_скорости: 322
  закон_масштабирования: 'линейный — масса_парка = N × масса_единицы; каждая единица
    независима (autonomous pursuit); canon: Skynet Moto-Terminator (Terminator Salvation
    2009), Ducati Monster 1100 S base, 200 mph (322 km/h), dual plasma emitters'
  ограничивающие_части:
  - izdelie_tverdooksidnyi_toplivnyi_element (SOFC — критическая зависимость от топливных
    элементов)
  - izdelie_lidar_robosense_ac1 (LiDAR — критическая зависимость от поставок RoboSense)
  - izdelie_bldc_enkoder (BLDC motor — критическая зависимость от Maxon/Faulhaber)
дата_обновления: '2026-11-11'
наследуемые_материалы:
- материал: b4c
  суммарная_доля_массы: 0.15
  источники_частей:
  - многослойная_броня_слой_1_B4C
  форма: баллистическая_керамика
- материал: ti-6al-4v
  суммарная_доля_массы: 0.4
  источники_частей:
  - многослойная_броня_слой_2_Ti6Al4V
  форма: планер_и_космические_изделия
- материал: uhmwpe
  суммарная_доля_массы: 0.1
  источники_частей:
  - многослойная_броня_слой_3_UHMWPE
  форма: высоконагруженные_тонкие_шнуры
---
## Описание

Moto-Terminator — автономный мотоцикл; 2 колеса; высокая скорость; плазменные орудия спереди; используется в погоне за людьми.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| масса | 180.0–250.0 (номинал 220.0) | kg | canon |
| габариты (Д×Ш×В) | 2100×800×1100 | mm | canon |
| тип узла | модель_SkyNet | — | canon |
| уровень_номер | 1 | — | canon |


## Источники

- Канон: Terminator: Salvation (2009)

## Декомпозиция

```mermaid
graph TD
    SkyNet_MotoTerminator["SkyNet-MotoTerminator"]
    izdelie_tverdooksidnyi_toplivnyi_element["izdelie_tverdooksidnyi_toplivnyi_element"]
    SkyNet_MotoTerminator --> izdelie_tverdooksidnyi_toplivnyi_element
    izdelie_SkyNet_HKAerial["izdelie_SkyNet-HKAerial"]
    SkyNet_MotoTerminator --> izdelie_SkyNet_HKAerial
    izdelie_lidar_robosense_ac1["izdelie_lidar_robosense_ac1"]
    SkyNet_MotoTerminator --> izdelie_lidar_robosense_ac1
    izdelie_radiatsionno_stoikii_neiromorfnyi_tmr["izdelie_radiatsionno-stoikii_neiromorfnyi_tmr"]
    SkyNet_MotoTerminator --> izdelie_radiatsionno_stoikii_neiromorfnyi_tmr
    izdelie_bldc_enkoder["izdelie_bldc_enkoder"]
    SkyNet_MotoTerminator --> izdelie_bldc_enkoder
```


## Источник канон

- **Произведение:** Terminator: Salvation (2009)
- **Тип:** фильм
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| число_осей | 1 |
| масса_кг | 350 |
| производитель | Скайнет |
| класс | наземный_колёсный |
| категория | наземный_HK |
| тип_модели | наземный_колёсный |

## Подсистемы (по типу)

- вычислительная
- энергетическая
- каркас
- сенсоры
- приводная_система
- система_связи
- навигация
- система_питания
- система_передвижения

## Многослойная броня (§11.6)

Минимум слоёв по типу: 3 (§11.6). Макс. доля массы брони: 40%.

1. B₄C (`b4c`)
2. Ti-6Al-4V (`ti6al4v`)
3. UHMWPE (`uhmwpe_dyneema`)

## Произведения, где появляется

- ✅ `work_004` — «Terminator Salvation» (2009) → [`work_004.md`](../произведения/work_004.md)
- 📚 `work_045` — «Terminator: Salvation (game)» (2009) → [`work_045.md`](../произведения/work_045.md)
