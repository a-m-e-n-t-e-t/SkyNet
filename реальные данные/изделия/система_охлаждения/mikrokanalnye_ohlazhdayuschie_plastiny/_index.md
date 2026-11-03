---
id: izdelie_mikrokanalnye_ohlazhdayuschie_plastiny
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
  - часть_mikrokanalnye_ohlazhdayuschie_plastiny_core
  - часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing
  - часть_mikrokanalnye_ohlazhdayuschie_plastiny_connectors
  - часть_mikrokanalnye_ohlazhdayuschie_plastiny_mounting
материалы_частей:
  - часть: часть_mikrokanalnye_ohlazhdayuschie_plastiny_core
    материал: generic_material
    доля_массы: 0.45
  - часть: часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing
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
# Изделие: Микроканальные охлаждающие пластины

## Описание

Микроканальные охлаждающие пластины

Полное наименование (как в CSV): `Микроканальные охлаждающие пластины`

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
    mikrokanalnye_ohlazh["izdelie_mikrokanalnye_ohlazhdayuschie_plastiny"]
    mikrokanalnye_ohlazhdayus["часть_mikrokanalnye_ohlazhdayuschie_plastiny_core"]
    mikrokanalnye_ohlazh --> mikrokanalnye_ohlazhdayus
    mikrokanalnye_ohlazhdayus["часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing"]
    mikrokanalnye_ohlazh --> mikrokanalnye_ohlazhdayus
    mikrokanalnye_ohlazhdayus["часть_mikrokanalnye_ohlazhdayuschie_plastiny_connectors"]
    mikrokanalnye_ohlazh --> mikrokanalnye_ohlazhdayus
    mikrokanalnye_ohlazhdayus["часть_mikrokanalnye_ohlazhdayuschie_plastiny_mounting"]
    mikrokanalnye_ohlazh --> mikrokanalnye_ohlazhdayus
```
