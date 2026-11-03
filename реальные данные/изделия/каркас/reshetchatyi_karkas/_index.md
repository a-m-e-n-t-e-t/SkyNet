---
id: izdelie_reshetchatyi_karkas
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: каркас
подтип: прочее
стандарты: 
  - ASTM A36
  - ISO 630
исследовательская_группа: boeing_lockheed
родитель: null
дочерние_части:
  - часть_reshetchatyi_karkas_core
  - часть_reshetchatyi_karkas_housing
  - часть_reshetchatyi_karkas_connectors
  - часть_reshetchatyi_karkas_mounting
материалы_частей:
  - часть: часть_reshetchatyi_karkas_core
    материал: generic_material
    доля_массы: 0.45
  - часть: часть_reshetchatyi_karkas_housing
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
          min: 1
          max: 1000
          nominal: 50
  габариты_mm:
          l: 500
          w: 500
          h: 500
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
# Изделие: Решётчатый каркас

## Описание

Решётчатый каркас (SLM + HIP)

Полное наименование (как в CSV): `Решётчатый каркас (SLM + HIP)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | каркас | — | classify_subsystem |
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
    reshetchatyi_karkas["izdelie_reshetchatyi_karkas"]
    reshetchatyi_karkas_core["часть_reshetchatyi_karkas_core"]
    reshetchatyi_karkas --> reshetchatyi_karkas_core
    reshetchatyi_karkas_housi["часть_reshetchatyi_karkas_housing"]
    reshetchatyi_karkas --> reshetchatyi_karkas_housi
    reshetchatyi_karkas_conne["часть_reshetchatyi_karkas_connectors"]
    reshetchatyi_karkas --> reshetchatyi_karkas_conne
    reshetchatyi_karkas_mount["часть_reshetchatyi_karkas_mounting"]
    reshetchatyi_karkas --> reshetchatyi_karkas_mount
```
