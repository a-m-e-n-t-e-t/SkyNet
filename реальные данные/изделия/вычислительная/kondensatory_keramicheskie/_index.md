---
id: izdelie_kondensatory_keramicheskie
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: керамический_конденсатор
стандарты: 
  - EIA RS-198
  - AEC-Q200
исследовательская_группа: Murata_TDK
родитель: null
дочерние_части:
  - часть_kondensatory_keramicheskie_ceramic_layers
  - часть_kondensatory_keramicheskie_inner_electrodes
  - часть_kondensatory_keramicheskie_outer_electrodes
  - часть_kondensatory_keramicheskie_termination
  - часть_kondensatory_keramicheskie_plating
материалы_частей:
  - часть: часть_kondensatory_keramicheskie_ceramic_layers
    материал: barium_titanate
    доля_массы: 0.475
  - часть: часть_kondensatory_keramicheskie_inner_electrodes
    материал: nickel
    доля_массы: 0.19
  - часть: часть_kondensatory_keramicheskie_outer_electrodes
    материал: copper
    доля_массы: 0.08
  - часть: часть_kondensatory_keramicheskie_termination
    материал: copper
    доля_массы: 0.09
  - часть: часть_kondensatory_keramicheskie_plating
    материал: tin
    доля_массы: 0.09
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
          min: 0.0001
          max: 0.005
          nominal: 0.001
  габариты_mm:
          l: 1
          w: 0.5
          h: 0.5
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.001
          max: 0.05
          nominal: 0.01
наследуемые: {}
дополнительные: 
  ёмкость_мкФ: 100
  V_max_V: 50
  источник: Murata MLCC datasheet
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Конденсаторы: керамические

## Описание

Конденсаторы: керамические (X7R)

Полное наименование (как в CSV): `Конденсаторы: керамические (X7R)`

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
    kondensatory_keramic["izdelie_kondensatory_keramicheskie"]
    kondensatory_keramicheski["часть_kondensatory_keramicheskie_ceramic_layers"]
    kondensatory_keramic --> kondensatory_keramicheski
    kondensatory_keramicheski["часть_kondensatory_keramicheskie_inner_electrodes"]
    kondensatory_keramic --> kondensatory_keramicheski
    kondensatory_keramicheski["часть_kondensatory_keramicheskie_outer_electrodes"]
    kondensatory_keramic --> kondensatory_keramicheski
    kondensatory_keramicheski["часть_kondensatory_keramicheskie_termination"]
    kondensatory_keramic --> kondensatory_keramicheski
    kondensatory_keramicheski["часть_kondensatory_keramicheskie_plating"]
    kondensatory_keramic --> kondensatory_keramicheski
```
