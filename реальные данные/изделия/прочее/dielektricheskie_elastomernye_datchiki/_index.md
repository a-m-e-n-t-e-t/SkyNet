---
id: izdelie_dielektricheskie_elastomernye_datchiki
тип: изделие
категория: прочее
уровень_иерархии: верхний
уровень_номер: 1
подсистема: прочее
подтип: прочее
стандарты: 
  - ISO 9001
исследовательская_группа: various
родитель: null
дочерние_части:
  - часть_dielektricheskie_elastomernye_datchiki_core
  - часть_dielektricheskie_elastomernye_datchiki_housing
  - часть_dielektricheskie_elastomernye_datchiki_connectors
  - часть_dielektricheskie_elastomernye_datchiki_mounting
материалы_частей:
  - часть: часть_dielektricheskie_elastomernye_datchiki_core
    материал: generic_material
    доля_массы: 0.45
  - часть: часть_dielektricheskie_elastomernye_datchiki_housing
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
# Изделие: диэлектрические эластомерные датчики

## Описание

диэлектрические эластомерные датчики (DES)

Полное наименование (как в CSV): `диэлектрические эластомерные датчики (DES)`

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
    dielektricheskie_ela["izdelie_dielektricheskie_elastomernye_datchiki"]
    dielektricheskie_elastome["часть_dielektricheskie_elastomernye_datchiki_core"]
    dielektricheskie_ela --> dielektricheskie_elastome
    dielektricheskie_elastome["часть_dielektricheskie_elastomernye_datchiki_housing"]
    dielektricheskie_ela --> dielektricheskie_elastome
    dielektricheskie_elastome["часть_dielektricheskie_elastomernye_datchiki_connectors"]
    dielektricheskie_ela --> dielektricheskie_elastome
    dielektricheskie_elastome["часть_dielektricheskie_elastomernye_datchiki_mounting"]
    dielektricheskie_ela --> dielektricheskie_elastome
```
