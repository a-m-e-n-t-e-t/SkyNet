---
id: izdelie_termomoduli_pelte
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: модуль_Пельтье
стандарты: 
  - JEDEC JESD47
исследовательская_группа: marlow_industries
родитель: null
дочерние_части:
  - часть_termomoduli_pelte_peltier_couples
  - часть_termomoduli_pelte_ceramic_top
  - часть_termomoduli_pelte_electrodes
  - часть_termomoduli_pelte_solder
  - часть_termomoduli_pelte_wires
  - часть_termomoduli_pelte_ceramic_bottom
материалы_частей:
  - часть: часть_termomoduli_pelte_peltier_couples
  - часть: часть_termomoduli_pelte_ceramic_bottom
    материал: alumina
    доля_массы: 0.2000
    материал: bi2te3
    доля_массы: 0.38
  - часть: часть_termomoduli_pelte_ceramic_top
    материал: alumina
    доля_массы: 0.19
    материал: alumina
    доля_массы: 0.19
  - часть: часть_termomoduli_pelte_electrodes
    материал: copper
    доля_массы: 0.095
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
          max: 0.5
          nominal: 0.05
  габариты_mm:
          l: 40
          w: 40
          h: 4
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 1
          max: 100
          nominal: 10
наследуемые: {}
дополнительные: 
  Qmax_W: 50
  dT_max_C: 70
  источник: Marlow Industries TEC
дата_создания: 2026-11-03
дата_обновления: 2026-11-05
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: термомодули Пельтье

## Описание

термомодули Пельтье

Полное наименование (как в CSV): `термомодули Пельтье`

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
    termomoduli_pelte["izdelie_termomoduli_pelte"]
    termomoduli_pelte_peltier["часть_termomoduli_pelte_peltier_couples"]
    termomoduli_pelte --> termomoduli_pelte_peltier
    termomoduli_pelte_ceramic["часть_termomoduli_pelte_ceramic_top"]
    termomoduli_pelte --> termomoduli_pelte_ceramic
    termomoduli_pelte --> termomoduli_pelte_ceramic
    termomoduli_pelte_electro["часть_termomoduli_pelte_electrodes"]
    termomoduli_pelte --> termomoduli_pelte_electro
    termomoduli_pelte_solder["часть_termomoduli_pelte_solder"]
    termomoduli_pelte --> termomoduli_pelte_solder
    termomoduli_pelte_wires["часть_termomoduli_pelte_wires"]
    termomoduli_pelte --> termomoduli_pelte_wires
```
