---
id: izdelie_marx_generator
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: импульсный_генератор_Маркса
стандарты: 
  - IEEE C57.12.00
исследовательская_группа: general_electric
родитель: null
дочерние_части:
  - часть_marx_generator_capacitors
  - часть_marx_generator_spark_gaps
  - часть_marx_generator_resistors
  - часть_marx_generator_housing
  - часть_marx_generator_output_terminal
  - часть_marx_generator_insulator
материалы_частей:
  - часть: часть_marx_generator_capacitors
    материал: ceramic_capacitors
    доля_массы: 0.475
  - часть: часть_marx_generator_spark_gaps
    материал: tungsten_electrodes
    доля_массы: 0.1
  - часть: часть_marx_generator_housing
    материал: aluminum
    доля_массы: 0.285
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
          min: 50
          max: 5000
          nominal: 500
  габариты_mm:
          l: 1000
          w: 800
          h: 1500
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 10
          max: 1000
          nominal: 100
наследуемые: {}
дополнительные: 
  V_импульс_kV: 1000
  I_импульс_kA: 100
  источник: Marx generator heritage
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Marx generator

## Описание

Marx generator

Полное наименование (как в CSV): `Marx generator`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
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
    marx_generator["izdelie_marx_generator"]
    marx_generator_capacitors["часть_marx_generator_capacitors"]
    marx_generator --> marx_generator_capacitors
    marx_generator_spark_gaps["часть_marx_generator_spark_gaps"]
    marx_generator --> marx_generator_spark_gaps
    marx_generator_resistors["часть_marx_generator_resistors"]
    marx_generator --> marx_generator_resistors
    marx_generator_housing["часть_marx_generator_housing"]
    marx_generator --> marx_generator_housing
    marx_generator_output_ter["часть_marx_generator_output_terminal"]
    marx_generator --> marx_generator_output_ter
    marx_generator_insulator["часть_marx_generator_insulator"]
    marx_generator --> marx_generator_insulator
```
