---
id: izdelie_loop_heat_pipe
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: система_охлаждения
подтип: прочее
стандарты: 
  - ASHRAE 15
исследовательская_группа: boyd_corp
родитель: null
дочерние_части:
  - часть_loop_heat_pipe_core
  - часть_loop_heat_pipe_housing
  - часть_loop_heat_pipe_connectors
  - часть_loop_heat_pipe_mounting
материалы_частей:
  - часть: часть_loop_heat_pipe_core
    материал: generic_material
    доля_массы: 0.45
  - часть: часть_loop_heat_pipe_housing
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
          min: 0.05
          max: 5
          nominal: 0.5
  габариты_mm:
          l: 200
          w: 100
          h: 5
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0
          max: 0
          nominal: 0
наследуемые: {}
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Loop Heat Pipe

## Описание

Loop Heat Pipe (LHP)

Полное наименование (как в CSV): `Loop Heat Pipe (LHP)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | система_охлаждения | — | classify_subsystem |
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
    loop_heat_pipe["izdelie_loop_heat_pipe"]
    loop_heat_pipe_core["часть_loop_heat_pipe_core"]
    loop_heat_pipe --> loop_heat_pipe_core
    loop_heat_pipe_housing["часть_loop_heat_pipe_housing"]
    loop_heat_pipe --> loop_heat_pipe_housing
    loop_heat_pipe_connectors["часть_loop_heat_pipe_connectors"]
    loop_heat_pipe --> loop_heat_pipe_connectors
    loop_heat_pipe_mounting["часть_loop_heat_pipe_mounting"]
    loop_heat_pipe --> loop_heat_pipe_mounting
```
