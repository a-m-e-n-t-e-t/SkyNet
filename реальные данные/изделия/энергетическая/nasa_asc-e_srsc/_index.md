---
id: izdelie_nasa_asc-e_srsc
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: Стирлинг_конвертер
стандарты: 
  - NASA-STD-8729.1
исследовательская_группа: nasa_glenn
родитель: null
дочерние_части:
  - часть_nasa_asc-e_srsc_heater_head
  - часть_nasa_asc-e_srsc_regenerator
  - часть_nasa_asc-e_srsc_cooler
  - часть_nasa_asc-e_srsc_displacer_piston
  - часть_nasa_asc-e_srsc_power_piston
  - часть_nasa_asc-e_srsc_alternator
материалы_частей:
  - часть: часть_nasa_asc-e_srsc_heater_head
    материал: inconel_625
    доля_массы: 0.19
  - часть: часть_nasa_asc-e_srsc_regenerator
    материал: stainless_steel_mesh
    доля_массы: 0.095
  - часть: часть_nasa_asc-e_srsc_displacer_piston
    материал: inconel_718
    доля_массы: 0.18
  - часть: часть_nasa_asc-e_srsc_power_piston
    материал: inconel_718
    доля_массы: 0.18
  - часть: часть_nasa_asc-e_srsc_alternator
    материал: copper
    доля_массы: 0.18
  - часть: часть_nasa_asc-e_srsc_cooler
    материал: al_6061-t6
    доля_массы: 0.067
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
          min: 1
          max: 5
          nominal: 3
  габариты_mm:
          l: 200
          w: 100
          h: 100
  выработка_энергии_W:
          min: 50
          max: 100
          nominal: 80
  выработка_тепла_W:
          min: 200
          max: 400
          nominal: 250
наследуемые: {}
дополнительные: 
  T_нагрев_C: 850
  КПД_процентов: 38
  источник: NASA ASC (Advanced Stirling Convertor)
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: NASA ASC-e / SRSC

## Описание

NASA ASC-e / SRSC — компактный FPSE

Полное наименование (как в CSV): `NASA ASC-e / SRSC — компактный FPSE`

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
    nasa_asc-e_srsc["izdelie_nasa_asc-e_srsc"]
    nasa_asc-e_srsc_heater_he["часть_nasa_asc-e_srsc_heater_head"]
    nasa_asc-e_srsc --> nasa_asc-e_srsc_heater_he
    nasa_asc-e_srsc_regenerat["часть_nasa_asc-e_srsc_regenerator"]
    nasa_asc-e_srsc --> nasa_asc-e_srsc_regenerat
    nasa_asc-e_srsc_cooler["часть_nasa_asc-e_srsc_cooler"]
    nasa_asc-e_srsc --> nasa_asc-e_srsc_cooler
    nasa_asc-e_srsc_displacer["часть_nasa_asc-e_srsc_displacer_piston"]
    nasa_asc-e_srsc --> nasa_asc-e_srsc_displacer
    nasa_asc-e_srsc_power_pis["часть_nasa_asc-e_srsc_power_piston"]
    nasa_asc-e_srsc --> nasa_asc-e_srsc_power_pis
    nasa_asc-e_srsc_alternato["часть_nasa_asc-e_srsc_alternator"]
    nasa_asc-e_srsc --> nasa_asc-e_srsc_alternato
```
