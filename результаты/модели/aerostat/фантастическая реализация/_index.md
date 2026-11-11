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
основные:
  масса_kg:
    min: 1.0
    max: 10.0
    nominal: 5.0
  размер_m: 0.5
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
    izdelie_tverdooksidnyi_toplivnyi_element["izdelie_tverdooksidnyi_toplivnyi_element"]
    SkyNet_Aerostat --> izdelie_tverdooksidnyi_toplivnyi_element
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
