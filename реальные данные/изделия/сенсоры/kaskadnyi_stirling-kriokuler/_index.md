---
id: izdelie_kaskadnyi_stirling-kriokuler
тип: изделие
категория: оптика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: сенсоры
подтип: прочее
стандарты:
- MIL-STD-810
- IEC 60068
исследовательская_группа: flir_l3
родитель: null
дочерние_части:
- часть_kaskadnyi_stirling-kriokuler_core
- часть_kaskadnyi_stirling-kriokuler_housing
- часть_kaskadnyi_stirling-kriokuler_connectors
- часть_kaskadnyi_stirling-kriokuler_mounting
материалы_частей:
- часть: часть_kaskadnyi_stirling-kriokuler_core
  материал: al_6061-t6
  форма: силовые_элементы_конструкций
  доля_массы: 0.45
- часть: часть_kaskadnyi_stirling-kriokuler_housing
  материал: aluminum
  форма: корпуса_электроники
  доля_массы: 0.27
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
    max: 5
    nominal: 0.5
  габариты_mm:
    l: 200
    w: 200
    h: 100
  выработка_энергии_W:
    min: 0
    max: 0
    nominal: 0
  выработка_тепла_W:
    min: 0.1
    max: 10
    nominal: 2
наследуемые: {}
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: '2026-11-11'
источник: web_search
источник_разбора: веб-верификация
технологии_частей:
- часть: часть_kaskadnyi_stirling-kriokuler_core
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: al_6061-t6
    роль: обрабатываемый
- часть: часть_kaskadnyi_stirling-kriokuler_housing
  технология: anodirovanie
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: aluminum
    роль: обрабатываемый
наследуемые_материалы:
- материал: al_6061-t6
  суммарная_доля_массы: 0.45
  источники_частей:
  - часть_kaskadnyi_stirling-kriokuler_core
  форма: силовые_элементы_конструкций
- материал: aluminum
  суммарная_доля_массы: 0.27
  источники_частей:
  - часть_kaskadnyi_stirling-kriokuler_housing
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
    - 1.0
    - 10.0
    единица: kg
  - имя: длина_единицы
    диапазон:
    - 200
    - 300.0
    единица: mm
  пределы:
    max_единиц_в_системе: 100
    min_массы: 1.0
    max_массы: 10.0
  закон_масштабирования: нелинейный — масса_системы = N × масса_единицы × 1.10 (10%
    overhead на mounting+control unit)
  ограничивающие_части:
  - часть_kaskadnyi_stirling-kriokuler_core (sensor core — критическая зависимость
    от supplier)
  - часть_kaskadnyi_stirling-kriokuler_housing (aluminum + anodizing MIL-A-8625 —
    стандартное производство)
источник_url: https://en.wikipedia.org/wiki/Stirling_cryocooler
источник_дата: '2026-11-11'
---

# Изделие: каскадный Стирлинг-криокулер

## Описание

каскадный Стирлинг-криокулер (Stirling cooler)

Полное наименование (как в CSV): `каскадный Стирлинг-криокулер (Stirling cooler)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | сенсоры | — | classify_subsystem |
| категория | прочее | — | — |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

Изделие верхнего уровня. Дочерние части не указаны (требуется декомпозиция).

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Требует описания на основе инженерного анализа.

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)

---


## Декомпозиция

```mermaid
graph TD
    kaskadnyi_stirling-k["izdelie_kaskadnyi_stirling-kriokuler"]
    kaskadnyi_stirling-krioku["часть_kaskadnyi_stirling-kriokuler_core"]
    kaskadnyi_stirling-k --> kaskadnyi_stirling-krioku
    kaskadnyi_stirling-krioku["часть_kaskadnyi_stirling-kriokuler_housing"]
    kaskadnyi_stirling-k --> kaskadnyi_stirling-krioku
    kaskadnyi_stirling-krioku["часть_kaskadnyi_stirling-kriokuler_connectors"]
    kaskadnyi_stirling-k --> kaskadnyi_stirling-krioku
    kaskadnyi_stirling-krioku["часть_kaskadnyi_stirling-kriokuler_mounting"]
    kaskadnyi_stirling-k --> kaskadnyi_stirling-krioku
```
