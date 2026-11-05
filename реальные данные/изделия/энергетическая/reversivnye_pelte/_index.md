---
id: izdelie_reversivnye_pelte
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: реверсивный_модуль_Пельтье
стандарты: 
  - JEDEC JESD47
исследовательская_группа: ferrotec
родитель: null
дочерние_части:
  - часть_reversivnye_pelte_peltier_couples
  - часть_reversivnye_pelte_ceramic_top
  - часть_reversivnye_pelte_electrodes
  - часть_reversivnye_pelte_solder
материалы_частей:
  - часть: часть_reversivnye_pelte_peltier_couples
    материал: bi₂te₃
    доля_массы: 0.137
  - часть: часть_reversivnye_pelte_ceramic_top
    материал: oksid_alyuminiya
    доля_массы: 0.149
  - часть: часть_reversivnye_pelte_electrodes
    материал: copper
    доля_массы: 0.06
  - часть: часть_reversivnye_pelte_solder
    материал: splav_sn-pb
    доля_массы: 0.054
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
  Qmax_W: 100
  источник: Ferrotec 9500 series
дата_создания: 2026-11-03
дата_обновления: 2026-11-05
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Реверсивные Пельтье

## Описание

Реверсивные Пельтье

Полное наименование (как в CSV): `Реверсивные Пельтье`

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
    reversivnye_pelte["izdelie_reversivnye_pelte"]
    reversivnye_pelte_peltier["часть_reversivnye_pelte_peltier_couples"]
    reversivnye_pelte --> reversivnye_pelte_peltier
    reversivnye_pelte_ceramic["часть_reversivnye_pelte_ceramic_top"]
    reversivnye_pelte --> reversivnye_pelte_ceramic
    reversivnye_pelte --> reversivnye_pelte_ceramic
    reversivnye_pelte_electro["часть_reversivnye_pelte_electrodes"]
    reversivnye_pelte --> reversivnye_pelte_electro
    reversivnye_pelte_solder["часть_reversivnye_pelte_solder"]
    reversivnye_pelte --> reversivnye_pelte_solder
```
