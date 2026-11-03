---
id: izdelie_optovolokonnaya_shina
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: система_связи
подтип: прочее
стандарты: 
  - FCC Part 15
  - ETSI EN 301 489
исследовательская_группа: harris_thales
родитель: null
дочерние_части:
  - часть_optovolokonnaya_shina_core
  - часть_optovolokonnaya_shina_housing
  - часть_optovolokonnaya_shina_connectors
  - часть_optovolokonnaya_shina_mounting
материалы_частей:
  - часть: часть_optovolokonnaya_shina_core
    материал: generic_material
    доля_массы: 0.45
  - часть: часть_optovolokonnaya_shina_housing
    материал: aluminum
    доля_массы: 0.27
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
          max: 5
          nominal: 0.1
  габариты_mm:
          l: 50
          w: 30
          h: 5
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.01
          max: 5
          nominal: 0.5
наследуемые: {}
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: оптоволоконная шина

## Описание

оптоволоконная шина

Полное наименование (как в CSV): `оптоволоконная шина`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | система_связи | — | classify_subsystem |
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
    optovolokonnaya_shin["izdelie_optovolokonnaya_shina"]
    optovolokonnaya_shina_cor["часть_optovolokonnaya_shina_core"]
    optovolokonnaya_shin --> optovolokonnaya_shina_cor
    optovolokonnaya_shina_hou["часть_optovolokonnaya_shina_housing"]
    optovolokonnaya_shin --> optovolokonnaya_shina_hou
    optovolokonnaya_shina_con["часть_optovolokonnaya_shina_connectors"]
    optovolokonnaya_shin --> optovolokonnaya_shina_con
    optovolokonnaya_shina_mou["часть_optovolokonnaya_shina_mounting"]
    optovolokonnaya_shin --> optovolokonnaya_shina_mou
```
