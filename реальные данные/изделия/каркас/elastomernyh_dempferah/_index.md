---
id: izdelie_elastomernyh_dempferah
тип: изделие
категория: прочее
уровень_иерархии: верхний
уровень_номер: 1
подсистема: каркас
подтип: прочее
стандарты: 
  - ISO 9001
исследовательская_группа: various
родитель: null
дочерние_части:
  - часть_elastomernyh_dempferah_core
  - часть_elastomernyh_dempferah_housing
  - часть_elastomernyh_dempferah_connectors
  - часть_elastomernyh_dempferah_mounting
материалы_частей:
  - часть: часть_elastomernyh_dempferah_core
    материал: silikon_40_50_shore_a
    доля_массы: 0.45
  - часть: часть_elastomernyh_dempferah_housing
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
          min: 0.1
          max: 100
          nominal: 5
  габариты_mm:
          l: 200
          w: 200
          h: 50
  выработка_энергии_W:
          min: 0
          max: 100
          nominal: 0
  выработка_тепла_W:
          min: 0
          max: 100
          nominal: 1
наследуемые: {}
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: эластомерных демпферах

## Описание

эластомерных демпферах

Полное наименование (как в CSV): `эластомерных демпферах`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | прочее | — | classify_subsystem |
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
    elastomernyh_dempfer["izdelie_elastomernyh_dempferah"]
    elastomernyh_dempferah_co["часть_elastomernyh_dempferah_core"]
    elastomernyh_dempfer --> elastomernyh_dempferah_co
    elastomernyh_dempferah_ho["часть_elastomernyh_dempferah_housing"]
    elastomernyh_dempfer --> elastomernyh_dempferah_ho
    elastomernyh_dempferah_co["часть_elastomernyh_dempferah_connectors"]
    elastomernyh_dempfer --> elastomernyh_dempferah_co
    elastomernyh_dempferah_mo["часть_elastomernyh_dempferah_mounting"]
    elastomernyh_dempfer --> elastomernyh_dempferah_mo
```
