---
id: izdelie_akusticheskaya_linza
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
- часть_akusticheskaya_linza_core
- часть_akusticheskaya_linza_housing
- часть_akusticheskaya_linza_connectors
- часть_akusticheskaya_linza_mounting
материалы_частей:
- часть: часть_akusticheskaya_linza_core
  материал: silikon_80_shore_a_steklyannye_mikrosfery
  форма: силовые_элементы_конструкций
  доля_массы: 0.45
- часть: часть_akusticheskaya_linza_housing
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
    h: 150
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
- часть: часть_akusticheskaya_linza_core
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: silikon_80_shore_a_steklyannye_mikrosfery
    роль: обрабатываемый
- часть: часть_akusticheskaya_linza_housing
  технология: anodirovanie
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: aluminum
    роль: обрабатываемый
наследуемые_материалы:
- материал: silikon_80_shore_a_steklyannye_mikrosfery
  суммарная_доля_массы: 0.45
  источники_частей:
  - часть_akusticheskaya_linza_core
  форма: силовые_элементы_конструкций
- материал: aluminum
  суммарная_доля_массы: 0.27
  источники_частей:
  - часть_akusticheskaya_linza_housing
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
    - 0.5
    - 5.0
    единица: kg
  - имя: длина_единицы
    диапазон:
    - 200
    - 300.0
    единица: mm
  пределы:
    max_единиц_в_системе: 100
    min_массы: 0.5
    max_массы: 5.0
  закон_масштабирования: нелинейный — масса_системы = N × масса_единицы × 1.10 (10%
    overhead на mounting+control unit)
  ограничивающие_части:
  - часть_akusticheskaya_linza_core (sensor core — критическая зависимость от supplier)
  - часть_akusticheskaya_linza_housing (aluminum + anodizing MIL-A-8625 — стандартное
    производство)
источник_url: https://en.wikipedia.org/wiki/Acoustic_lens
источник_дата: '2026-11-11'
---

# Изделие: Акустическая линза

## Описание

Акустическая линза

Полное наименование (как в CSV): `Акустическая линза`

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
    akusticheskaya_linza["izdelie_akusticheskaya_linza"]
    akusticheskaya_linza_core["часть_akusticheskaya_linza_core"]
    akusticheskaya_linza --> akusticheskaya_linza_core
    akusticheskaya_linza_hous["часть_akusticheskaya_linza_housing"]
    akusticheskaya_linza --> akusticheskaya_linza_hous
    akusticheskaya_linza_conn["часть_akusticheskaya_linza_connectors"]
    akusticheskaya_linza --> akusticheskaya_linza_conn
    akusticheskaya_linza_moun["часть_akusticheskaya_linza_mounting"]
    akusticheskaya_linza --> akusticheskaya_linza_moun
```
