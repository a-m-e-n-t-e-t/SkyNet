---
id: izdelie_brainchip_akida_2
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: нейроморфный_процессор
стандарты: 
  - ISO 9001
  - JEDEC JESD47
исследовательская_группа: brainchip_team
родитель: null
дочерние_части:
  - часть_brainchip_akida_2_die
  - часть_brainchip_akida_2_substrate
  - часть_brainchip_akida_2_pins_balls
  - часть_brainchip_akida_2_thermal_spreader
  - часть_brainchip_akida_2_encapsulant
  - часть_brainchip_akida_2_capacitors
  - часть_brainchip_akida_2_pcb
материалы_частей:
  - часть: часть_brainchip_akida_2_die
    материал: silicon_wafer
    форма: подложки_нейроморфных_процессоров
    доля_массы: 0.1
  - часть: часть_brainchip_akida_2_substrate
    материал: bt_resin
    форма: подложки_bga_csp_нейроморфов
    доля_массы: 0.14
  - часть: часть_brainchip_akida_2_pins_balls
    материал: copper_alloy
    форма: штырьки_и_шарики_разъёмов
    доля_массы: 0.1
  - часть: часть_brainchip_akida_2_thermal_spreader
    материал: copper
    форма: теплосъём_и_экранирование
    доля_массы: 0.18
  - часть: часть_brainchip_akida_2_encapsulant
    материал: epoxy_molding
    форма: encapsulant_нейроморфов_bga
    доля_массы: 0.1
  - часть: часть_brainchip_akida_2_capacitors
    материал: ceramic_mlcc
    форма: развязка_и_фильтрация_нейроморфов
    доля_массы: 0.1
  - часть: часть_brainchip_akida_2_pcb
    материал: fr4
    форма: несущая_плата_PCB
    доля_массы: 0.16
наследуемые_материалы:
  - материал: si
    суммарная_доля_массы: 0.1
    источники_частей: [часть_brainchip_akida_2_die]
  - материал: ptfe
    суммарная_доля_массы: 0.14
    источники_частей: [часть_brainchip_akida_2_substrate]
  - материал: splav_sn-pb
    суммарная_доля_массы: 0.1
    источники_частей: [часть_brainchip_akida_2_pins_balls]
  - материал: copper
    суммарная_доля_массы: 0.18
    источники_частей: [часть_brainchip_akida_2_thermal_spreader]
  - материал: epoksid_epon_828_teta
    суммарная_доля_массы: 0.1
    источники_частей: [часть_brainchip_akida_2_encapsulant]
  - материал: batio3
    суммарная_доля_массы: 0.1
    источники_частей: [часть_brainchip_akida_2_capacitors]
  - материал: fr4
    суммарная_доля_массы: 0.16
    источники_частей: [часть_brainchip_akida_2_pcb]
технологии_частей:
  - часть: часть_brainchip_akida_2_die
    технология: ion_implantation_si
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: si
        роль: обрабатываемый
  - часть: часть_brainchip_akida_2_substrate
    технология: galvanika
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: ptfe
        роль: обрабатываемый
  - часть: часть_brainchip_akida_2_pins_balls
    технология: smd_montazh_oplavleniem
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: splav_sn-pb
        роль: обрабатываемый
  - часть: часть_brainchip_akida_2_thermal_spreader
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: copper
        роль: обрабатываемый
  - часть: часть_brainchip_akida_2_encapsulant
    технология: anderfill
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: epoksid_epon_828_teta
        роль: обрабатываемый
  - часть: часть_brainchip_akida_2_capacitors
    технология: tape_casting
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: batio3
        роль: обрабатываемый
  - часть: часть_brainchip_akida_2_pcb
    технология: smd_montazh_oplavleniem
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: fr4
        роль: обрабатываемый
масштабируемость:
  режим: фиксированная
  параметры: [масса_kg, выработка_тепла_W]
  пределы:
    min: {масса_kg: 0.005, выработка_тепла_W: 0.02}
    max: {масса_kg: 0.05, выработка_тепла_W: 0.05}
  закон_масштабирования:
    масса: фиксированный
    тепловыделение: фиксированный
  ограничивающие_части: [часть_brainchip_akida_2_die, часть_brainchip_akida_2_capacitors]
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
          min: 0.02
          max: 0.05
          nominal: 0.03
наследуемые: {}
дополнительные: 
  цена_usd: 250
  TOPS: 1.2
  weight_bits:
    - 1
    - 2
    - 4
    - 8
  SRAM_MB: 8
  источник: open-neuromorphic.org/hardware/akida-brainchip
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: BrainChip Akida 2

## Описание

BrainChip Akida 2

Полное наименование (как в CSV): `BrainChip Akida 2`

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
    brainchip_akida_2["izdelie_brainchip_akida_2"]
    brainchip_akida_2_die["часть_brainchip_akida_2_die"]
    brainchip_akida_2 --> brainchip_akida_2_die
    brainchip_akida_2_substra["часть_brainchip_akida_2_substrate"]
    brainchip_akida_2 --> brainchip_akida_2_substra
    brainchip_akida_2_pins_ba["часть_brainchip_akida_2_pins_balls"]
    brainchip_akida_2 --> brainchip_akida_2_pins_ba
    brainchip_akida_2_thermal["часть_brainchip_akida_2_thermal_spreader"]
    brainchip_akida_2 --> brainchip_akida_2_thermal
    brainchip_akida_2_encapsu["часть_brainchip_akida_2_encapsulant"]
    brainchip_akida_2 --> brainchip_akida_2_encapsu
    brainchip_akida_2_capacit["часть_brainchip_akida_2_capacitors"]
    brainchip_akida_2 --> brainchip_akida_2_capacit
    brainchip_akida_2_pcb["часть_brainchip_akida_2_pcb"]
    brainchip_akida_2 --> brainchip_akida_2_pcb
```
