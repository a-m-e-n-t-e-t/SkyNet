---
id: izdelie_intel_loihi_2
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: нейроморфный_процессор
стандарты: 
  - Intel 4 process
исследовательская_группа: intel_labs
родитель: null
дочерние_части:
  - часть_intel_loihi_2_die
  - часть_intel_loihi_2_substrate
  - часть_intel_loihi_2_pins_balls
  - часть_intel_loihi_2_thermal_spreader
  - часть_intel_loihi_2_encapsulant
  - часть_intel_loihi_2_capacitors
  - часть_intel_loihi_2_pcb
материалы_частей:
  - часть: часть_intel_loihi_2_die
    материал: silicon_wafer
    доля_массы: 0.1
  - часть: часть_intel_loihi_2_substrate
    материал: bt_resin
    доля_массы: 0.14
  - часть: часть_intel_loihi_2_pins_balls
    материал: copper_alloy
    доля_массы: 0.1
  - часть: часть_intel_loihi_2_thermal_spreader
    материал: copper
    доля_массы: 0.18
  - часть: часть_intel_loihi_2_encapsulant
    материал: epoxy_molding
    доля_массы: 0.1
  - часть: часть_intel_loihi_2_capacitors
    материал: ceramic_mlcc
    доля_массы: 0.1
  - часть: часть_intel_loihi_2_pcb
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
  выработка_тепла_W:
          min: 0.5
          max: 1.5
          nominal: 1.0
наследуемые: {}
дополнительные: 
  нейроны: 1000000
  синапсы: 120000000
  ядро_нейронов: 128
  процесс: Intel 4 (7nm EUV)
  источник: open-neuromorphic.org/hardware/loihi-2-intel
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Intel Loihi 2

## Описание

Intel Loihi 2

Полное наименование (как в CSV): `Intel Loihi 2`

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
    intel_loihi_2["izdelie_intel_loihi_2"]
    intel_loihi_2_die["часть_intel_loihi_2_die"]
    intel_loihi_2 --> intel_loihi_2_die
    intel_loihi_2_substrate["часть_intel_loihi_2_substrate"]
    intel_loihi_2 --> intel_loihi_2_substrate
    intel_loihi_2_pins_balls["часть_intel_loihi_2_pins_balls"]
    intel_loihi_2 --> intel_loihi_2_pins_balls
    intel_loihi_2_thermal_spr["часть_intel_loihi_2_thermal_spreader"]
    intel_loihi_2 --> intel_loihi_2_thermal_spr
    intel_loihi_2_encapsulant["часть_intel_loihi_2_encapsulant"]
    intel_loihi_2 --> intel_loihi_2_encapsulant
    intel_loihi_2_capacitors["часть_intel_loihi_2_capacitors"]
    intel_loihi_2 --> intel_loihi_2_capacitors
    intel_loihi_2_pcb["часть_intel_loihi_2_pcb"]
    intel_loihi_2 --> intel_loihi_2_pcb
```
