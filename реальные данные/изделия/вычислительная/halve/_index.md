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
          l: 80
          w: 22
          h: 2.8
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
  форм_фактор: 'M.2-модуль 2280: плата-носитель FR-4 80×22×0.8 мм с BGA-пакетом процессора 12×12 мм на верхней стороне'
  обоснование_габаритов: 'PCB 0.8±0.08 мм (M.2: компоненты ≤1.5 мм/сторону — Wikipedia M.2) + BGA-пакет ≈2.0 мм (IC-подложка 0.6 + полость кристалла/glob-top ≈0.9 + IHS 0.5) = 2.8 мм; реальный форм-фактор нейроморфных процессоров: BrainChip AKD1000 выпускается в виде M.2-карт (B+M Key / E Key), Intel Loihi 2 — на add-in-картах (Oheo Gulch — одночиповая с Arria 10 FPGA, Kapoho Point — 8-чиповая ~4×4″); V = 80×22×2.8 = 4928 мм³ ≥ ΣV(детей)×1.15 = 1916 мм³ (F15g A), все части помещаются по осям (F15g B)'
дата_создания: 2026-11-03
дата_обновления: 2026-11-08
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: HALVE

## Описание

HALVE — нейроморфный процессор в форм-факторе M.2-модуля: плата-носитель FR-4 (M.2 2280, 80×22×0.8 мм) с BGA-пакетом 12×12 мм — кристалл 4×4 мм (Intel 4, 7 нм), медный теплораспределитель (IHS), эпоксидный glob-top, шары BGA Sn63/Pb37 и блок керамических MLCC-конденсаторов развязки питания. Форм-фактор подтверждён практикой отрасли: BrainChip AKD1000 выпускается в виде M.2-карт (B+M Key / E Key), Loihi 2 Intel — на add-in-картах (Oheo Gulch — одночиповая карта с Arria 10 FPGA, Kapoho Point — 8-чиповая система ~4×4″).

Полное наименование (как в CSV): `HALVE`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | вычислительная | — | classify_subsystem |
| категория | прочее | — | — |
| габариты (Д×Ш×В) | 80×22×2.8 | mm | M.2 2280 (PCB 0.8±0.08 мм, Wikipedia M.2) + BGA-пакет ≈2.0 мм (substrate 0.6 + cavity + IHS 0.5) |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

M.2-модуль нейроморфного процессора (уровень 1), 7 дочерних частей:

- `часть_halve_die` — кремниевый кристалл 4×4×0.5 мм (Intel 4, 7 нм)
- `часть_halve_substrate` — корпусная IC-подложка BGA 12×12×0.6 мм
- `часть_halve_pins_balls` — шары BGA Sn63/Pb37 Ø0.4 мм
- `часть_halve_thermal_spreader` — медный теплораспределитель (IHS) 12×12×0.5 мм
- `часть_halve_encapsulant` — эпоксидный glob-top 10×10×0.5 мм
- `часть_halve_capacitors` — MLCC развязки питания 0805 (2×1.25×0.8 мм)
- `часть_halve_pcb` — плата-носитель FR-4, M.2 2280 (80×22×0.8 мм)

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Требует описания на основе инженерного анализа.

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- https://en.wikipedia.org/wiki/M.2 — M.2 2280: 22 мм ширина × 80 мм длина, PCB 0.8 мм ±10%, компоненты ≤1.5 мм/сторону (обращение 2026-11-08)
- https://brainchip.com/upgrade-the-raspberry-pi-for-ai-with-a-neuromorphic-processor — BrainChip AKD1000: нейроморфный процессор в виде M.2-карт (B+M Key / E Key)
- https://www.intel.com/content/dam/www/central-libraries/us/en/documents/neuromorphic-computing-loihi-2-brief.pdf — Intel Loihi 2 brief: Oheo Gulch (одночиповая карта, Arria 10 FPGA), Kapoho Point (8 чипов, ~4×4″)

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
