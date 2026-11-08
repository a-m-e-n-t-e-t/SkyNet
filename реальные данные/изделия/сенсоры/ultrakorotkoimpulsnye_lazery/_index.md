---
id: izdelie_ultrakorotkoimpulsnye_lazery
тип: изделие
категория: оптика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: сенсоры
подтип: прочее
стандарты: 
  - MIL-STD-810
  - IEC 60068
исследовательская_группа: flir_l3
родитель: null
дочерние_части:
  - часть_ultrakorotkoimpulsnye_lazery_core
  - часть_ultrakorotkoimpulsnye_lazery_housing
  - часть_ultrakorotkoimpulsnye_lazery_connectors
  - часть_ultrakorotkoimpulsnye_lazery_mounting
материалы_частей:
  - часть: часть_ultrakorotkoimpulsnye_lazery_core
    материал: al_6061-t6
    доля_массы: 0.45
  - часть: часть_ultrakorotkoimpulsnye_lazery_housing
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
          l: 100
          w: 100
          h: 50
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.1
          max: 10
          nominal: 2
наследуемые: {}
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Ультракороткоимпульсные лазеры

## Описание

Ультракороткоимпульсные лазеры (USPL)

Полное наименование (как в CSV): `Ультракороткоимпульсные лазеры (USPL)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | сенсоры | — | classify_subsystem |
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
    ultrakorotkoimpulsny["izdelie_ultrakorotkoimpulsnye_lazery"]
    ultrakorotkoimpulsnye_laz["часть_ultrakorotkoimpulsnye_lazery_core"]
    ultrakorotkoimpulsny --> ultrakorotkoimpulsnye_laz
    ultrakorotkoimpulsnye_laz["часть_ultrakorotkoimpulsnye_lazery_housing"]
    ultrakorotkoimpulsny --> ultrakorotkoimpulsnye_laz
    ultrakorotkoimpulsnye_laz["часть_ultrakorotkoimpulsnye_lazery_connectors"]
    ultrakorotkoimpulsny --> ultrakorotkoimpulsnye_laz
    ultrakorotkoimpulsnye_laz["часть_ultrakorotkoimpulsnye_lazery_mounting"]
    ultrakorotkoimpulsny --> ultrakorotkoimpulsnye_laz
```
