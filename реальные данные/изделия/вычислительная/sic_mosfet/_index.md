---
id: izdelie_sic_mosfet
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: силовой_транзистор
стандарты: 
  - JEDEC JESD47
  - AEC-Q101
исследовательская_группа: wolfspeed
родитель: null
дочерние_части:
  - часть_sic_mosfet_die
  - часть_sic_mosfet_lead_frame
  - часть_sic_mosfet_wire_bonds
  - часть_sic_mosfet_encapsulant
  - часть_sic_mosfet_solder
  - часть_sic_mosfet_gate_terminal
материалы_частей:
  - часть: часть_sic_mosfet_die
    материал: silicon_carbide
    доля_массы: 0.19
  - часть: часть_sic_mosfet_lead_frame
    материал: copper_alloy
    доля_массы: 0.475
  - часть: часть_sic_mosfet_wire_bonds
    материал: aluminum
    доля_массы: 0.0095
  - часть: часть_sic_mosfet_encapsulant
    материал: epoxy_molding
    доля_массы: 0.19
  - часть: часть_sic_mosfet_solder
    материал: lead_free_solder
    доля_массы: 0.045
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
          min: 0.001
          max: 0.01
          nominal: 0.003
  габариты_mm:
          l: 10
          w: 10
          h: 2
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.5
          max: 50
          nominal: 5
наследуемые: {}
дополнительные: 
  V_max_V: 1700
  I_max_A: 100
  Rds_on_mOhm: 25
  источник: Wolfspeed datasheet
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: SiC MOSFET

## Описание

SiC MOSFET (Wolfspeed CPM3-9000)

Полное наименование (как в CSV): `SiC MOSFET (Wolfspeed CPM3-9000)`

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
    sic_mosfet["izdelie_sic_mosfet"]
    sic_mosfet_die["часть_sic_mosfet_die"]
    sic_mosfet --> sic_mosfet_die
    sic_mosfet_lead_frame["часть_sic_mosfet_lead_frame"]
    sic_mosfet --> sic_mosfet_lead_frame
    sic_mosfet_wire_bonds["часть_sic_mosfet_wire_bonds"]
    sic_mosfet --> sic_mosfet_wire_bonds
    sic_mosfet_encapsulant["часть_sic_mosfet_encapsulant"]
    sic_mosfet --> sic_mosfet_encapsulant
    sic_mosfet_solder["часть_sic_mosfet_solder"]
    sic_mosfet --> sic_mosfet_solder
    sic_mosfet_gate_terminal["часть_sic_mosfet_gate_terminal"]
    sic_mosfet --> sic_mosfet_gate_terminal
```
