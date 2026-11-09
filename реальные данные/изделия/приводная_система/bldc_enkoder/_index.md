---
id: izdelie_bldc_enkoder
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: приводная_система
подтип: прочее
стандарты: 
  - IEC 60034
  - ISO 1940
исследовательская_группа: maxon_faulhaber
родитель: null
дочерние_части:
  - часть_bldc_enkoder_core
  - часть_bldc_enkoder_housing
  - часть_bldc_enkoder_connectors
  - часть_bldc_enkoder_mounting
материалы_частей:
  - часть: часть_bldc_enkoder_core
    материал: al_6061-t6
    форма: силовые_элементы_конструкций
    доля_массы: 0.45
  - часть: часть_bldc_enkoder_housing
    материал: al_6061-t6
    форма: силовые_элементы_конструкций
    доля_массы: 0.27
# F29 [B-BOM]: агрегация материалов частей — core 0.45×1.0 + housing 0.27×1.0
# F27e: технологии — ЧПУ-фрезерование/точение корпусов и кронштейнов al_6061-T6
# (xinqidamachining.com: turn-milling 6061-T6 motor housing, davantech.com:
# 6061-T6 CNC ±0.01 мм)
наследуемые_материалы:
  - материал: al_6061-t6
    форма: силовые_элементы_конструкций
    суммарная_доля_массы: 0.72
    источники_частей:
      - часть_bldc_enkoder_core
      - часть_bldc_enkoder_housing
технологии_частей:
  - часть: часть_bldc_enkoder_core
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: al_6061-t6
        роль: обрабатываемый
  - часть: часть_bldc_enkoder_housing
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: al_6061-t6
        роль: обрабатываемый
  - часть: часть_bldc_enkoder_connectors
    технология: tokarnaya_obrabotka_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: al_6061-t6
        роль: обрабатываемый
  - часть: часть_bldc_enkoder_mounting
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: stal_st3
        роль: обрабатываемый
scaling_type: количественный
соединители: []
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
ии_перепроектирован:
  статус: false
  верификация: []
основные: 
  масса_kg:
          min: 0.6
          max: 2.0
          nominal: 1
  габариты_mm:
          l: 70
          w: 70
          h: 160
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.2
          max: 30
          nominal: 5
наследуемые: {}
дополнительные:
  цена_usd: null
  источник_url: https://www.maxongroup.com/maxon/view/product/488607
  источник_url_2: https://us.aspina-group.com/en/learning-zone/columns/what-is/034
дата_создания: 2026-11-03
дата_обновления: 2026-11-10
источник: web_search
источник_разбора: веб-верификация
источник_дата: 2026-11-10
---
## Описание

BLDC + энкодер — безщёточный двигатель постоянного тока с интегральным энкодером (servo-модуль): статорный пакет в стальном корпусе Ø45–52 мм с инкрементальным/абсолютным энкодером на заднем фланце и милитари-разъёмом M38999. Envelope 70×70×160 мм (фланцевое основание + корпус двигателя 127 мм + разъёмная группа), масса ~1 кг.

Полное наименование (как в CSV): `BLDC + энкодер`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | приводная_система | — | canon |
| подтип | прочее | — | canon |
| масса | 0.6–2.0 (номинал 1) | kg | canon |
| габариты (Д×Ш×В) | 70×70×160 | mm | canon |
| выработка энергии | 0 | W | canon |
| выработка тепла | 0.2–30 | W | canon |
| тип узла | изделие | — | canon |
| уровень_номер | 1 | — | canon |


## Принцип работы

Требует описания на основе инженерного анализа.

## Состав

Изделие верхнего уровня, 4 дочерние части: [`часть_bldc_enkoder_core`](часть_bldc_enkoder_core/_index.md) — статорный пакет с ротором, [`часть_bldc_enkoder_housing`](часть_bldc_enkoder_housing/_index.md) — корпус 52×52×127, [`часть_bldc_enkoder_mounting`](часть_bldc_enkoder_mounting/_index.md) — фланец/кронштейн, [`часть_bldc_enkoder_connectors`](часть_bldc_enkoder_connectors/_index.md) — разъёмы M38999.

## Используемые технологии

- `frezervanie_chpu` (доля: 1.0)
- `frezervanie_chpu` (доля: 1.0)
- `tokarnaya_obrabotka_chpu` (доля: 1.0)
- `frezervanie_chpu` (доля: 1.0)


## Используемые материалы

- `al_6061-t6` (форма: силовые_элементы_конструкций) → [`al_6061-t6`](../../../материалы/al_6061-t6.md)
- `al_6061-t6` (форма: силовые_элементы_конструкций) → [`al_6061-t6`](../../../материалы/al_6061-t6.md)


## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)

---

## Декомпозиция

```mermaid
graph TD
    izdelie_bldc_enkoder["izdelie_bldc_enkoder"]
    ______bldc_enkoder_core["часть_bldc_enkoder_core"]
    izdelie_bldc_enkoder --> ______bldc_enkoder_core
    ______bldc_enkoder_housing["часть_bldc_enkoder_housing"]
    izdelie_bldc_enkoder --> ______bldc_enkoder_housing
    ______bldc_enkoder_connectors["часть_bldc_enkoder_connectors"]
    izdelie_bldc_enkoder --> ______bldc_enkoder_connectors
    ______bldc_enkoder_mounting["часть_bldc_enkoder_mounting"]
    izdelie_bldc_enkoder --> ______bldc_enkoder_mounting
```
