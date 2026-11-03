---
id: izdelie_ibm_northpole
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: AI_инференс_чип
стандарты: 
  - IBM 2nm
исследовательская_группа: ibm_research
родитель: null
дочерние_части:
  - часть_ibm_northpole_die
  - часть_ibm_northpole_package
  - часть_ibm_northpole_hbm
  - часть_ibm_northpole_substrate
  - часть_ibm_northpole_thermal_spreader
  - часть_ibm_northpole_capacitors
материалы_частей:
  - часть: часть_ibm_northpole_die
    материал: silicon_wafer
    доля_массы: 0.15
  - часть: часть_ibm_northpole_package
    материал: bt_resin
    доля_массы: 0.18
  - часть: часть_ibm_northpole_hbm
    материал: silicon_wafer
    доля_массы: 0.15
  - часть: часть_ibm_northpole_substrate
    материал: bt_resin
    доля_массы: 0.154
  - часть: часть_ibm_northpole_thermal_spreader
    материал: copper
    доля_массы: 0.135
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
          min: 0.005
          max: 0.05
          nominal: 0.01
  габариты_mm:
          l: 12
          w: 12
          h: 1
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 50
          max: 100
          nominal: 75
наследуемые: {}
дополнительные: 
  параметры_млрд: 22
  производительность_TOPS: 4640
  источник: IBM Research
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: IBM NorthPole

## Описание

IBM NorthPole

Полное наименование (как в CSV): `IBM NorthPole`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | вычислительная | — | classify_subsystem |
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
    ibm_northpole["izdelie_ibm_northpole"]
    ibm_northpole_die["часть_ibm_northpole_die"]
    ibm_northpole --> ibm_northpole_die
    ibm_northpole_package["часть_ibm_northpole_package"]
    ibm_northpole --> ibm_northpole_package
    ibm_northpole_hbm["часть_ibm_northpole_hbm"]
    ibm_northpole --> ibm_northpole_hbm
    ibm_northpole_substrate["часть_ibm_northpole_substrate"]
    ibm_northpole --> ibm_northpole_substrate
    ibm_northpole_thermal_spr["часть_ibm_northpole_thermal_spreader"]
    ibm_northpole --> ibm_northpole_thermal_spr
    ibm_northpole_capacitors["часть_ibm_northpole_capacitors"]
    ibm_northpole --> ibm_northpole_capacitors
```
