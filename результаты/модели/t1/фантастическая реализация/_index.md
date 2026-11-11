---
id: SkyNet-T1
web_verification: terminator.fandom.com/wiki/T-1 (T3) (2026-11-03)
тактико_технические_характеристики:
  мобильность:
    скорость_км_ч: 25
    масса_kg: 2000
  вооружение: dual_plasma_cannons
тип: модель_SkyNet
класс: наземный_гусеничный
категория: наземный_HK
тип_модели: наземный_гусеничный
источник_происхождения: фильм
функции:
- прототип
- охрана
- штурм
канон_источник: 'Terminator 3: Rise of the Machines (2003)'
произведения:
- work_003
- work_043
- work_044
производитель: Cyberdyne Systems
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
  тип_брони: наземный_гусеничный
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
источник_url: https://terminator.fandom.com/wiki/T-1
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
    min: 1500.0
    max: 2200.0
    nominal: 2000.0
  высота_m: 2.4
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
    - 1500.0
    - 2200.0
    единица: kg
  - имя: скорость
    диапазон:
    - 20
    - 30
    единица: km/h
  пределы:
    max_единиц_в_системе: 500
    min_массы: 1500.0
    max_массы: 2200.0
    min_скорости: 20
    max_скорости: 30
  закон_масштабирования: 'линейный — масса_парка = N × масса_единицы; canon: T-1 Battlefield
    Robot (T3 2003), 8 ft tall (2.4m), 2000 kg, 25 km/h, dual plasma cannons, tracked
    platform; prototype for HK-Tank'
  ограничивающие_части:
  - izdelie_tverdooksidnyi_topливnyi_element (SOFC — критическая зависимость)
  - izdelie_bldc_enkoder (BLDC/hydraulic motors for tracks)
наследуемые_материалы:
- материал: b4c
  суммарная_доля_массы: 0.15
  источники_частей:
  - многослойная_броня_слой_1
  форма: баллистическая_керамика
- материал: ti-6al-4v
  суммарная_доля_массы: 0.5
  источники_частей:
  - многослойная_броня_слой_2
  форма: планер_и_космические_изделия
- материал: uhmwpe
  суммарная_доля_массы: 0.05
  источники_частей:
  - многослойная_броня_слой_3
  форма: высоконагруженные_тонкие_шнуры
дата_обновления: '2026-11-11'
---
## Описание

T-1 — прототип наземного боевого дрона; гусеницы; автономный; запущен Cyberdyne до Судного дня; вооружён 2 Minigun M134.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| масса | 1500.0–2200.0 (номинал 2000.0) | kg | canon |
| тип узла | модель_SkyNet | — | canon |
| уровень_номер | 1 | — | canon |


## Источники

- Канон: Terminator 3: Rise of the Machines (2003)

## Декомпозиция

```mermaid
graph TD
    SkyNet_T1["SkyNet-T1"]
    izdelie_tverdooksidnyi_top___nyi_element["izdelie_tverdooksidnyi_topливnyi_element"]
    SkyNet_T1 --> izdelie_tverdooksidnyi_top___nyi_element
    izdelie_SkyNet_HKAerial["izdelie_SkyNet-HKAerial"]
    SkyNet_T1 --> izdelie_SkyNet_HKAerial
    izdelie_lidar_robosense_ac1["izdelie_lidar_robosense_ac1"]
    SkyNet_T1 --> izdelie_lidar_robosense_ac1
    izdelie_radiatsionno_stoikii_neiromorfnyi_tmr["izdelie_radiatsionno-stoikii_neiromorfnyi_tmr"]
    SkyNet_T1 --> izdelie_radiatsionno_stoikii_neiromorfnyi_tmr
    izdelie_bldc_enkoder["izdelie_bldc_enkoder"]
    SkyNet_T1 --> izdelie_bldc_enkoder
```


## Источник канон

- **Произведение:** Terminator 3: Rise of the Machines (2003)
- **Тип:** фильм
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| длина_гусеницы_м | 2.2 |
| масса_кг | 800 |
| производитель | Cyberdyne Systems |
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

- ✅ `work_003` — «Terminator 3: Rise of the Machines» (2003) → [`work_003.md`](../произведения/work_003.md)
- 📚 `work_043` — «Terminator 3: Rise of the Machines» (2003) → [`work_043.md`](../произведения/work_043.md)
- 📚 `work_044` — «Terminator 3: The Redemption» (2004) → [`work_044.md`](../произведения/work_044.md)
