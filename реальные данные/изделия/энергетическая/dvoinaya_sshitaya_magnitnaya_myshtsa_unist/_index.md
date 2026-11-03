---
id: izdelie_dvoinaya_sshitaya_magnitnaya_myshtsa_unist
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: магнитная_мышца
стандарты: []
исследовательская_группа: brigham_young_university
родитель: null
дочерние_части:
  - часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_magnets
  - часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_coil
  - часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_spring
  - часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_housing
материалы_частей:
  - часть: часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_magnets
    материал: ndfeb
    доля_массы: 0.475
  - часть: часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_coil
    материал: copper_wire
    доля_массы: 0.18
  - часть: часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_spring
    материал: spring_steel
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
          min: 0.01
          max: 1
          nominal: 0.1
  габариты_mm:
          l: 100
          w: 20
          h: 20
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.01
          max: 1
          nominal: 0.1
наследуемые: {}
дополнительные: 
  сила_Н: 100
  ход_мм: 30
  источник: BYU UNIST magnetic muscle research
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: двойная сшитая магнитная мышца UNIST

## Описание

двойная сшитая магнитная мышца UNIST

Полное наименование (как в CSV): `двойная сшитая магнитная мышца UNIST`

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
    dvoinaya_sshitaya_ma["izdelie_dvoinaya_sshitaya_magnitnaya_myshtsa_unist"]
    dvoinaya_sshitaya_magnitn["часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_magnets"]
    dvoinaya_sshitaya_ma --> dvoinaya_sshitaya_magnitn
    dvoinaya_sshitaya_magnitn["часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_coil"]
    dvoinaya_sshitaya_ma --> dvoinaya_sshitaya_magnitn
    dvoinaya_sshitaya_magnitn["часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_spring"]
    dvoinaya_sshitaya_ma --> dvoinaya_sshitaya_magnitn
    dvoinaya_sshitaya_magnitn["часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_housing"]
    dvoinaya_sshitaya_ma --> dvoinaya_sshitaya_magnitn
```
