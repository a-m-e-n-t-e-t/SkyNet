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
    материал: stal_st3
    форма: строительные_конструкции_и_крепёж
    доля_массы: 0.45
  - часть: часть_belleville_shaiby_housing
    материал: al_6061-t6
    форма: силовые_элементы_конструкций
    доля_массы: 0.27
# F29 [B-BOM]: агрегация материалов частей (core 0.45×1.0, housing 0.27×1.0)
# F27e: технологии обработки — штамповка дисковых пружин DIN 2093 (Ck75/51CrV4,
# bellevillesprings.com), ЧПУ-фрезерование корпуса, литьё под давлением PA66-корпуса
# разъёма Deutsch DT06-4S, ЧПУ-точение стяжного узла (100Cr6)
наследуемые_материалы:
  - материал: stal_st3
    форма: строительные_конструкции_и_крепёж
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
      - материал: stal_st3
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
дата_обновления: 2026-11-10
источник: user_input
источник_разбора: пользовательский ввод
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
