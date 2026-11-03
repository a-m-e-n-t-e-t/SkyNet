---
id: izdelie_lt-sofc
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: твердооксидный_топливный_элемент
стандарты: 
  - IEC 62282
исследовательская_группа: ceres_power
родитель: null
дочерние_части:
  - часть_lt-sofc_anode
  - часть_lt-sofc_electrolyte
  - часть_lt-sofc_cathode
  - часть_lt-sofc_interconnect
  - часть_lt-sofc_seal
  - часть_lt-sofc_manifold
материалы_частей:
  - часть: часть_lt-sofc_anode
    материал: ni_ysz_cermet
    доля_массы: 0.18
  - часть: часть_lt-sofc_electrolyte
    материал: ysz_electrolyte
    доля_массы: 0.095
  - часть: часть_lt-sofc_cathode
    материал: lsm_cathode
    доля_массы: 0.18
  - часть: часть_lt-sofc_interconnect
    материал: crofer_22_apu
    доля_массы: 0.285
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
          min: 0.5
          max: 5
          nominal: 2
  габариты_mm:
          l: 150
          w: 150
          h: 100
  выработка_энергии_W:
          min: 50
          max: 500
          nominal: 200
  выработка_тепла_W:
          min: 50
          max: 500
          nominal: 200
наследуемые: {}
дополнительные: 
  T_рабочая_C: 500
  КПД_процентов: 60
  топливо: H2 + CO
  источник: Ceres Power steel-cell SOFC
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: LT-SOFC

## Описание

LT-SOFC (low-temperature SOFC, 300 °C)

Полное наименование (как в CSV): `LT-SOFC (low-temperature SOFC, 300 °C)`

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
    lt-sofc["izdelie_lt-sofc"]
    lt-sofc_anode["часть_lt-sofc_anode"]
    lt-sofc --> lt-sofc_anode
    lt-sofc_electrolyte["часть_lt-sofc_electrolyte"]
    lt-sofc --> lt-sofc_electrolyte
    lt-sofc_cathode["часть_lt-sofc_cathode"]
    lt-sofc --> lt-sofc_cathode
    lt-sofc_interconnect["часть_lt-sofc_interconnect"]
    lt-sofc --> lt-sofc_interconnect
    lt-sofc_seal["часть_lt-sofc_seal"]
    lt-sofc --> lt-sofc_seal
    lt-sofc_manifold["часть_lt-sofc_manifold"]
    lt-sofc --> lt-sofc_manifold
```
