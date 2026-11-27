---
id: izdelie_belleville_shaiby
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
- часть_belleville_shaiby_core
- часть_belleville_shaiby_housing
- часть_belleville_shaiby_connectors
- часть_belleville_shaiby_mounting
материалы_частей:
- часть: часть_belleville_shaiby_core
  материал: spring_steel
  форма: a231_a232_хром_ванадиевая
  доля_массы: 0.45
- часть: часть_belleville_shaiby_housing
  материал: al_6061-t6
  форма: силовые_элементы_конструкций
  доля_массы: 0.27
наследуемые_материалы:
- материал: spring_steel
  форма: a231_a232_хром_ванадиевая
  суммарная_доля_массы: 0.45
  источники_частей:
  - часть_belleville_shaiby_core
- материал: al_6061-t6
  форма: силовые_элементы_конструкций
  суммарная_доля_массы: 0.27
  источники_частей:
  - часть_belleville_shaiby_housing
технологии_частей:
- часть: часть_belleville_shaiby_core
  технология: shtampovka_listovaya
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: spring_steel
    роль: обрабатываемый
- часть: часть_belleville_shaiby_housing
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: al_6061-t6
    роль: обрабатываемый
- часть: часть_belleville_shaiby_connectors
  технология: lite_pod_davleniem
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: neilon_6_66
    роль: обрабатываемый
- часть: часть_belleville_shaiby_mounting
  технология: tokarnaya_obrabotka_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: 100cr6
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
    w: 50
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
масштабируемость:
  режим: масштабируемая
  параметры:
  - имя: количество_единиц
    диапазон:
    - 1
    - 1000
    единица: шт
  - имя: масса_единицы
    диапазон:
    - 0.005
    - 0.5
    единица: kg
  - имя: прогиб_mm
    диапазон:
    - 0.1
    - 5.0
    единица: mm
  пределы:
    max_единиц_в_системе: 1000
    min_массы: 0.005
    max_массы: 0.5
    min_прогиба: 0.1
    max_прогиба: 5.0
  закон_масштабирования: 'линейный — масса_стопки = N × масса_диска (без overhead,
    discrete components); типовая установка: DIN 2093 Belleville disc springs (51CrV4
    / Ck75 spring steel, bellevillesprings.com)'
  ограничивающие_части:
  - часть_belleville_shaiby_core (51CrV4 spring steel — критическая точность производства)
  - часть_belleville_shaiby_housing (al_6061-t6 + anodizing — стандартное производство)
источник_url: https://en.wikipedia.org/wiki/Belleville_washer
источник_дата: '2026-11-11'
---

## Описание

Belleville шайбы

Полное наименование (как в CSV): `Belleville шайбы`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | приводная_система | — | canon |
| подтип | прочее | — | canon |
| масса | 0.05–50 (номинал 1) | kg | canon |
| габариты (Д×Ш×В) | 100×50×50 | mm | canon |
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
- `lite_pod_davleniem` (доля: 1.0)
- `tokarnaya_obrabotka_chpu` (доля: 1.0)


## Используемые материалы

- `stal_st3` (форма: строительные_конструкции_и_крепёж) → [`stal_st3`](../../../материалы/stal_st3.md)
- `al_6061-t6` (форма: силовые_элементы_конструкций) → [`al_6061-t6`](../../../материалы/al_6061-t6.md)


## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)

---

## Декомпозиция

```mermaid
graph TD
    izdelie_belleville_shaiby["izdelie_belleville_shaiby"]
    ______belleville_shaiby_core["часть_belleville_shaiby_core"]
    izdelie_belleville_shaiby --> ______belleville_shaiby_core
    ______belleville_shaiby_housing["часть_belleville_shaiby_housing"]
    izdelie_belleville_shaiby --> ______belleville_shaiby_housing
    ______belleville_shaiby_connectors["часть_belleville_shaiby_connectors"]
    izdelie_belleville_shaiby --> ______belleville_shaiby_connectors
    ______belleville_shaiby_mounting["часть_belleville_shaiby_mounting"]
    izdelie_belleville_shaiby --> ______belleville_shaiby_mounting
```
