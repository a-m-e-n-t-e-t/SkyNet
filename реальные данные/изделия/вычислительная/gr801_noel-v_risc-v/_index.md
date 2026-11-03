---
id: izdelie_gr801_noel-v_risc-v
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: RISC-V_процессор
стандарты: 
  - RV64GC ISA
исследовательская_группа: cobham_gaisler
родитель: null
дочерние_части:
  - часть_gr801_noel-v_risc-v_die
  - часть_gr801_noel-v_risc-v_package
  - часть_gr801_noel-v_risc-v_crystal_osc
  - часть_gr801_noel-v_risc-v_flash
  - часть_gr801_noel-v_risc-v_sram
  - часть_gr801_noel-v_risc-v_substrate
  - часть_gr801_noel-v_risc-v_thermal_pad
  - часть_gr801_noel-v_risc-v_pins
  - часть_gr801_noel-v_risc-v_capacitors
  - часть_gr801_noel-v_risc-v_pcb
материалы_частей:
  - часть: часть_gr801_noel-v_risc-v_die
    материал: silicon_wafer
    доля_массы: 0.1
  - часть: часть_gr801_noel-v_risc-v_package
    материал: plastic_qfp
    доля_массы: 0.16
  - часть: часть_gr801_noel-v_risc-v_crystal_osc
    материал: quartz
    доля_массы: 0.02
  - часть: часть_gr801_noel-v_risc-v_flash
    материал: silicon_wafer
    доля_массы: 0.04
  - часть: часть_gr801_noel-v_risc-v_sram
    материал: silicon_wafer
    доля_массы: 0.04
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
          l: 15
          w: 15
          h: 1
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 1
          max: 5
          nominal: 3
наследуемые: {}
дополнительные: 
  архитектура: RV64GC RISC-V 64-bit
  ядра: 8
  тактовая_МГц: 1000
  источник: Cobham Gaisler datasheet
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: GR801 NOEL-V RISC-V

## Описание

GR801 NOEL-V RISC-V (rad-hard)

Полное наименование (как в CSV): `GR801 NOEL-V RISC-V (rad-hard)`

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
    gr801_noel-v_risc-v["izdelie_gr801_noel-v_risc-v"]
    gr801_noel-v_risc-v_die["часть_gr801_noel-v_risc-v_die"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_die
    gr801_noel-v_risc-v_packa["часть_gr801_noel-v_risc-v_package"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_packa
    gr801_noel-v_risc-v_cryst["часть_gr801_noel-v_risc-v_crystal_osc"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_cryst
    gr801_noel-v_risc-v_flash["часть_gr801_noel-v_risc-v_flash"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_flash
    gr801_noel-v_risc-v_sram["часть_gr801_noel-v_risc-v_sram"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_sram
    gr801_noel-v_risc-v_subst["часть_gr801_noel-v_risc-v_substrate"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_subst
    gr801_noel-v_risc-v_therm["часть_gr801_noel-v_risc-v_thermal_pad"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_therm
    gr801_noel-v_risc-v_pins["часть_gr801_noel-v_risc-v_pins"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_pins
    gr801_noel-v_risc-v_capac["часть_gr801_noel-v_risc-v_capacitors"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_capac
    gr801_noel-v_risc-v_pcb["часть_gr801_noel-v_risc-v_pcb"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_pcb
```
