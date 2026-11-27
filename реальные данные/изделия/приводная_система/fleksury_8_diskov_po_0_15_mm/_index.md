---
id: izdelie_fleksury_8_diskov_po_0_15_mm
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
- часть_fleksury_8_diskov_po_0_15_mm_core
- часть_fleksury_8_diskov_po_0_15_mm_housing
- часть_fleksury_8_diskov_po_0_15_mm_connectors
- часть_fleksury_8_diskov_po_0_15_mm_mounting
материалы_частей:
- часть: часть_fleksury_8_diskov_po_0_15_mm_core
  материал: becu
  форма: разъёмы_и_контакты
  доля_массы: 0.45
- часть: часть_fleksury_8_diskov_po_0_15_mm_housing
  материал: al_6061-t6
  форма: корпуса_электроники
  доля_массы: 0.27
технологии_частей:
- часть: часть_fleksury_8_diskov_po_0_15_mm_core
  технология: shtampovka_listovaya
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: becu
    роль: обрабатываемый
- часть: часть_fleksury_8_diskov_po_0_15_mm_housing
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: al_6061-t6
    роль: обрабатываемый
- часть: часть_fleksury_8_diskov_po_0_15_mm_connectors
  технология: tokarnaya_obrabotka_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: latun_c36000
    роль: обрабатываемый
- часть: часть_fleksury_8_diskov_po_0_15_mm_mounting
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: ss_aisi_304
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
    min: 0.05
    max: 50
    nominal: 1
  габариты_mm:
    l: 100
    w: 60
    h: 50
  выработка_энергии_W:
    min: 0
    max: 0
    nominal: 0
  выработка_тепла_W:
    min: 0.1
    max: 50
    nominal: 5
наследуемые: {}
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: '2026-11-11'
источник: web_search
источник_разбора: веб-верификация
наследуемые_материалы:
- материал: becu
  суммарная_доля_массы: 0.45
  источники_частей:
  - часть_fleksury_8_diskov_po_0_15_mm_core
  форма: разъёмы_и_контакты
- материал: al_6061-t6
  суммарная_доля_массы: 0.27
  источники_частей:
  - часть_fleksury_8_diskov_po_0_15_mm_housing
  форма: корпуса_электроники
масштабируемость:
  режим: масштабируемая
  параметры:
  - имя: количество_единиц
    диапазон:
    - 1
    - 100
    единица: шт
  - имя: масса_единицы
    диапазон:
    - 0.01
    - 0.5
    единица: kg
  - имя: количество_дисков
    диапазон:
    - 3
    - 12
    единица: шт
  - имя: толщина_диска_mm
    диапазон:
    - 0.1
    - 0.3
    единица: mm
  пределы:
    max_единиц_в_системе: 100
    min_массы: 0.01
    max_массы: 0.5
    min_дисков: 3
    max_дисков: 12
  закон_масштабирования: 'линейный — масса_сборки = N × масса_диска (без overhead);
    типовая установка: Oxford-like flexure bearing (8 дисков × 0.15 мм BeCu, 5mm stroke
    linear compressor/cryocooler, ResearchGate 2026)'
  ограничивающие_части:
  - часть_fleksury_8_diskov_po_0_15_mm_core (BeCu flexure discs 0.15mm — критическая
    точность штамповки)
  - часть_fleksury_8_diskov_po_0_15_mm_housing (aluminum + anodizing — стандартное
    производство)
источник_url: https://www.researchgate.net/publication/303168628_Design_OF_Flexure_Bearing_For_Linear_Compressor
источник_дата: '2026-11-11'
---
## Описание

флексуры 8 дисков по 0,15 мм (вместо 4×0,5), спираль 720°, отверстия разгрузки

Полное наименование (как в CSV): `флексуры 8 дисков по 0,15 мм (вместо 4×0,5), спираль 720°, отверстия разгрузки`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | приводная_система | — | canon |
| подтип | прочее | — | canon |
| масса | 0.05–50 (номинал 1) | kg | canon |
| габариты (Д×Ш×В) | 100×60×50 | mm | canon |
| выработка энергии | 0 | W | canon |
| выработка тепла | 0.1–50 | W | canon |
| тип узла | изделие | — | canon |
| уровень_номер | 1 | — | canon |


## Принцип работы

Требует описания на основе инженерного анализа.

## Состав

Изделие верхнего уровня. Дочерние части не указаны (требуется декомпозиция).

## Используемые технологии

- `shtampovka_listovaya` (доля: 1.0)
- `frezervanie_chpu` (доля: 1.0)
- `tokarnaya_obrabotka_chpu` (доля: 1.0)
- `frezervanie_chpu` (доля: 1.0)


## Используемые материалы

- `becu` (форма: разъёмы_и_контакты) → [`becu`](../../../материалы/becu.md)
- `al_6061-t6` (форма: корпуса_электроники) → [`al_6061-t6`](../../../материалы/al_6061-t6.md)


## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- Free-Flex® Pivot engineering data (flexpivots.com): AISI 410/420, серия 5000/6000, L/D ≈ 1.6 — продольная ось узла флексуры несёт длину корпуса/концевиков: https://flexpivots.com/products (проверено 2026-11-07)

---

## Декомпозиция

```mermaid
graph TD
    izdelie_fleksury_8_diskov_po_0_15_mm["izdelie_fleksury_8_diskov_po_0_15_mm"]
    ______fleksury_8_diskov_po_0_15_mm_core["часть_fleksury_8_diskov_po_0_15_mm_core"]
    izdelie_fleksury_8_diskov_po_0_15_mm --> ______fleksury_8_diskov_po_0_15_mm_core
    ______fleksury_8_diskov_po_0_15_mm_housing["часть_fleksury_8_diskov_po_0_15_mm_housing"]
    izdelie_fleksury_8_diskov_po_0_15_mm --> ______fleksury_8_diskov_po_0_15_mm_housing
    ______fleksury_8_diskov_po_0_15_mm_connectors["часть_fleksury_8_diskov_po_0_15_mm_connectors"]
    izdelie_fleksury_8_diskov_po_0_15_mm --> ______fleksury_8_diskov_po_0_15_mm_connectors
    ______fleksury_8_diskov_po_0_15_mm_mounting["часть_fleksury_8_diskov_po_0_15_mm_mounting"]
    izdelie_fleksury_8_diskov_po_0_15_mm --> ______fleksury_8_diskov_po_0_15_mm_mounting
```
