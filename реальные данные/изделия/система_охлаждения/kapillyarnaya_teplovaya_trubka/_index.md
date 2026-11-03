---
id: izdelie_kapillyarnaya_teplovaya_trubka
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
  - часть_kapillyarnaya_teplovaya_trubka_core
  - часть_kapillyarnaya_teplovaya_trubka_housing
  - часть_kapillyarnaya_teplovaya_trubka_connectors
  - часть_kapillyarnaya_teplovaya_trubka_mounting
материалы_частей:
  - часть: часть_kapillyarnaya_teplovaya_trubka_core
    материал: generic_material
    доля_массы: 0.45
  - часть: часть_kapillyarnaya_teplovaya_trubka_housing
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
# Изделие: капиллярная тепловая трубка

## Описание

капиллярная тепловая трубка (heat pipe)

Полное наименование (как в CSV): `капиллярная тепловая трубка (heat pipe)`

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
    kapillyarnaya_teplov["izdelie_kapillyarnaya_teplovaya_trubka"]
    kapillyarnaya_teplovaya_t["часть_kapillyarnaya_teplovaya_trubka_core"]
    kapillyarnaya_teplov --> kapillyarnaya_teplovaya_t
    kapillyarnaya_teplovaya_t["часть_kapillyarnaya_teplovaya_trubka_housing"]
    kapillyarnaya_teplov --> kapillyarnaya_teplovaya_t
    kapillyarnaya_teplovaya_t["часть_kapillyarnaya_teplovaya_trubka_connectors"]
    kapillyarnaya_teplov --> kapillyarnaya_teplovaya_t
    kapillyarnaya_teplovaya_t["часть_kapillyarnaya_teplovaya_trubka_mounting"]
    kapillyarnaya_teplov --> kapillyarnaya_teplovaya_t
```
