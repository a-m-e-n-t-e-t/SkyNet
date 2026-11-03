---
id: izdelie_tverdotelnye_akkumulyatory
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: литий-ионный_аккумулятор
стандарты: 
  - IEC 61960
  - UN 38.3
исследовательская_группа: panasonic_lg
родитель: null
дочерние_части:
  - часть_tverdotelnye_akkumulyatory_anode
  - часть_tverdotelnye_akkumulyatory_cathode
  - часть_tverdotelnye_akkumulyatory_electrolyte
  - часть_tverdotelnye_akkumulyatory_separator
  - часть_tverdotelnye_akkumulyatory_current_collector_cu
  - часть_tverdotelnye_akkumulyatory_current_collector_al
  - часть_tverdotelnye_akkumulyatory_case
материалы_частей:
  - часть: часть_tverdotelnye_akkumulyatory_anode
    материал: graphite
    доля_массы: 0.18
  - часть: часть_tverdotelnye_akkumulyatory_cathode
    материал: lini_mn_co_o2
    доля_массы: 0.34
  - часть: часть_tverdotelnye_akkumulyatory_electrolyte
    материал: lipf6_ec_dmc
    доля_массы: 0.19
  - часть: часть_tverdotelnye_akkumulyatory_separator
    материал: pe_pp
    доля_массы: 0.038
  - часть: часть_tverdotelnye_akkumulyatory_current_collector_cu
    материал: copper
    доля_массы: 0.0792
  - часть: часть_tverdotelnye_akkumulyatory_current_collector_al
    материал: aluminum
    доля_массы: 0.0792
  - часть: часть_tverdotelnye_akkumulyatory_case
    материал: aluminum
    доля_массы: 0.19
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
          l: 100
          w: 50
          h: 10
  выработка_энергии_W:
          min: 1
          max: 100
          nominal: 20
  выработка_тепла_W:
          min: 0.1
          max: 5
          nominal: 1
наследуемые: {}
дополнительные: 
  ёмкость_Ач: 5
  V: 3.7
  T_жизни_циклы: 1000
  источник: Panasonic NCR18650 / LG HG2
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Твердотельные аккумуляторы

## Описание

Твердотельные аккумуляторы

Полное наименование (как в CSV): `Твердотельные аккумуляторы`

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
    tverdotelnye_akkumul["izdelie_tverdotelnye_akkumulyatory"]
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_anode"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_cathode"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_electrolyte"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_separator"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_current_collector_cu"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_current_collector_al"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_case"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
```
