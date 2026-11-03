---
id: izdelie_mikroreaktor_deleniya
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: микро_реактор_деления
стандарты: 
  - IAEA SSR-4
  - 10 CFR 50
исследовательская_группа: westinghouse_oklo
родитель: null
дочерние_части:
  - часть_mikroreaktor_deleniya_fuel
  - часть_mikroreaktor_deleniya_moderator
  - часть_mikroreaktor_deleniya_heat_exchanger
  - часть_mikroreaktor_deleniya_control_rods
  - часть_mikroreaktor_deleniya_shielding
  - часть_mikroreaktor_deleniya_vessel
  - часть_mikroreaktor_deleniya_coolant
материалы_частей:
  - часть: часть_mikroreaktor_deleniya_fuel
    материал: uo2_pellets
    доля_массы: 0.095
  - часть: часть_mikroreaktor_deleniya_moderator
    материал: graphite
    доля_массы: 0.38
  - часть: часть_mikroreaktor_deleniya_heat_exchanger
    материал: inconel_625
    доля_массы: 0.15
  - часть: часть_mikroreaktor_deleniya_shielding
    материал: concrete_barite
    доля_массы: 0.38
  - часть: часть_mikroreaktor_deleniya_vessel
    материал: stainless_steel_316
    доля_массы: 0.19
  - часть: часть_mikroreaktor_deleniya_coolant
    материал: sodium
    доля_массы: 0.0475
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
          min: 1000
          max: 50000
          nominal: 10000
  габариты_mm:
          l: 5000
          w: 2000
          h: 2500
  выработка_энергии_W:
          min: 1000000
          max: 50000000
          nominal: 5000000
  выработка_тепла_W:
          min: 2000000
          max: 100000000
          nominal: 15000000
наследуемые: {}
дополнительные: 
  T_жизни_лет: 20
  мощность_MWe: 5
  источник: Westinghouse eVinci / Oklo Aurora
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Микрореактор деления

## Описание

Микрореактор деления (Kilopower / KRUSTY)

Полное наименование (как в CSV): `Микрореактор деления (Kilopower / KRUSTY)`

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
    mikroreaktor_deleniy["izdelie_mikroreaktor_deleniya"]
    mikroreaktor_deleniya_fue["часть_mikroreaktor_deleniya_fuel"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_fue
    mikroreaktor_deleniya_mod["часть_mikroreaktor_deleniya_moderator"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_mod
    mikroreaktor_deleniya_hea["часть_mikroreaktor_deleniya_heat_exchanger"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_hea
    mikroreaktor_deleniya_con["часть_mikroreaktor_deleniya_control_rods"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_con
    mikroreaktor_deleniya_shi["часть_mikroreaktor_deleniya_shielding"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_shi
    mikroreaktor_deleniya_ves["часть_mikroreaktor_deleniya_vessel"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_ves
    mikroreaktor_deleniya_coo["часть_mikroreaktor_deleniya_coolant"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_coo
```
