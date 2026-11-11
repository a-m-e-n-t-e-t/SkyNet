---
id: izdelie_lidar_robosense_ac1
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
- часть_lidar_robosense_ac1_core
- часть_lidar_robosense_ac1_housing
- часть_lidar_robosense_ac1_connectors
- часть_lidar_robosense_ac1_mounting
материалы_частей:
- часть: часть_lidar_robosense_ac1_core
  материал: al_6061-t6
  форма: силовые_элементы_конструкций
  доля_массы: 0.45
- часть: часть_lidar_robosense_ac1_housing
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
    l: 80
    w: 75
    h: 65
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
- часть: часть_lidar_robosense_ac1_core
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: al_6061-t6
    роль: обрабатываемый
- часть: часть_lidar_robosense_ac1_housing
  технология: anodirovanie
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: aluminum
    роль: обрабатываемый
наследуемые_материалы:
- материал: al_6061-t6
  суммарная_доля_массы: 0.45
  источники_частей:
  - часть_lidar_robosense_ac1_core
  форма: силовые_элементы_конструкций
- материал: aluminum
  суммарная_доля_массы: 0.27
  источники_частей:
  - часть_lidar_robosense_ac1_housing
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
    - 2.0
    единица: kg
  - имя: длина_единицы
    диапазон:
    - 80
    - 120.0
    единица: mm
  пределы:
    max_единиц_в_системе: 100
    min_массы: 0.5
    max_массы: 2.0
  закон_масштабирования: нелинейный — масса_системы = N × масса_единицы × 1.10 (10%
    overhead на mounting+control unit)
  ограничивающие_части:
  - часть_lidar_robosense_ac1_core (sensor core — критическая зависимость от supplier)
  - часть_lidar_robosense_ac1_housing (aluminum + anodizing MIL-A-8625 — стандартное
    производство)
источник_url: https://www.robosense.ai/products/lidar/RS-LiDAR-AC1
источник_дата: '2026-11-11'
---

# Изделие: LIDAR RoboSense AC1

## Описание

LIDAR RoboSense AC1

Полное наименование (как в CSV): `LIDAR RoboSense AC1`

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
    lidar_robosense_ac1["izdelie_lidar_robosense_ac1"]
    lidar_robosense_ac1_core["часть_lidar_robosense_ac1_core"]
    lidar_robosense_ac1 --> lidar_robosense_ac1_core
    lidar_robosense_ac1_housi["часть_lidar_robosense_ac1_housing"]
    lidar_robosense_ac1 --> lidar_robosense_ac1_housi
    lidar_robosense_ac1_conne["часть_lidar_robosense_ac1_connectors"]
    lidar_robosense_ac1 --> lidar_robosense_ac1_conne
    lidar_robosense_ac1_mount["часть_lidar_robosense_ac1_mounting"]
    lidar_robosense_ac1 --> lidar_robosense_ac1_mount
```
