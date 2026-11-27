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
основные:
  масса_kg:
    min: 100.0
    max: 200.0
    nominal: 136.0
  размах_крыльев_m: 1.8
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
    izdelie_tverdooksidnyi_toplivnyi_element["izdelie_tverdooksidnyi_toplivnyi_element"]
    SkyNet_HKDrone --> izdelie_tverdooksidnyi_toplivnyi_element
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
