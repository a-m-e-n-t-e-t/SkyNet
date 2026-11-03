---
id: izdelie_induktivnyi_nakopitel
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: индуктивный_накопитель
стандарты: 
  - IEEE C57.16
исследовательская_группа: general_electric
родитель: null
дочерние_части:
  - часть_induktivnyi_nakopitel_coil
  - часть_induktivnyi_nakopitel_core
  - часть_induktivnyi_nakopitel_housing
  - часть_induktivnyi_nakopitel_switch
  - часть_induktivnyi_nakopitel_cooling
материалы_частей:
  - часть: часть_induktivnyi_nakopitel_coil
    материал: copper_wire
    доля_массы: 0.475
  - часть: часть_induktivnyi_nakopitel_core
    материал: electrical_steel
    доля_массы: 0.285
  - часть: часть_induktivnyi_nakopitel_housing
    материал: aluminum
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
          min: 10
          max: 1000
          nominal: 100
  габариты_mm:
          l: 500
          w: 500
          h: 800
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 10
          max: 500
          nominal: 100
наследуемые: {}
дополнительные: 
  L_мкГн: 100
  I_max_kA: 50
  источник: GE pulsed power
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Индуктивный накопитель

## Описание

Индуктивный накопитель

Полное наименование (как в CSV): `Индуктивный накопитель`

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
    induktivnyi_nakopite["izdelie_induktivnyi_nakopitel"]
    induktivnyi_nakopitel_coi["часть_induktivnyi_nakopitel_coil"]
    induktivnyi_nakopite --> induktivnyi_nakopitel_coi
    induktivnyi_nakopitel_cor["часть_induktivnyi_nakopitel_core"]
    induktivnyi_nakopite --> induktivnyi_nakopitel_cor
    induktivnyi_nakopitel_hou["часть_induktivnyi_nakopitel_housing"]
    induktivnyi_nakopite --> induktivnyi_nakopitel_hou
    induktivnyi_nakopitel_swi["часть_induktivnyi_nakopitel_switch"]
    induktivnyi_nakopite --> induktivnyi_nakopitel_swi
    induktivnyi_nakopitel_coo["часть_induktivnyi_nakopitel_cooling"]
    induktivnyi_nakopite --> induktivnyi_nakopitel_coo
```
