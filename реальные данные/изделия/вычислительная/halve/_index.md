---
id: izdelie_halve
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: нейроморфный_процессор
стандарты: []
исследовательская_группа: advanced_research
родитель: null
дочерние_части:
  - часть_halve_die
  - часть_halve_substrate
  - часть_halve_pins_balls
  - часть_halve_thermal_spreader
  - часть_halve_encapsulant
  - часть_halve_capacitors
  - часть_halve_pcb
материалы_частей:
  - часть: часть_halve_die
    материал: silicon_wafer
    доля_массы: 0.1
  - часть: часть_halve_substrate
    материал: bt_resin
    доля_массы: 0.14
  - часть: часть_halve_pins_balls
    материал: copper_alloy
    доля_массы: 0.1
  - часть: часть_halve_thermal_spreader
    материал: copper
    доля_массы: 0.18
  - часть: часть_halve_encapsulant
    материал: epoxy_molding
    доля_массы: 0.1
  - часть: часть_halve_capacitors
    материал: ceramic_mlcc
    доля_массы: 0.1
  - часть: часть_halve_pcb
    материал: fr4
    доля_массы: 0.16
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
          min: 0.1
          max: 1
          nominal: 0.5
наследуемые: {}
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: HALVE

## Описание

HALVE

Полное наименование (как в CSV): `HALVE`

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
    halve["izdelie_halve"]
    halve_die["часть_halve_die"]
    halve --> halve_die
    halve_substrate["часть_halve_substrate"]
    halve --> halve_substrate
    halve_pins_balls["часть_halve_pins_balls"]
    halve --> halve_pins_balls
    halve_thermal_spreader["часть_halve_thermal_spreader"]
    halve --> halve_thermal_spreader
    halve_encapsulant["часть_halve_encapsulant"]
    halve --> halve_encapsulant
    halve_capacitors["часть_halve_capacitors"]
    halve --> halve_capacitors
    halve_pcb["часть_halve_pcb"]
    halve --> halve_pcb
```
