---
id: izdelie_poristyi_gazovyi_podshipnik_iz_sic
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
  - часть_poristyi_gazovyi_podshipnik_iz_sic_core
  - часть_poristyi_gazovyi_podshipnik_iz_sic_housing
  - часть_poristyi_gazovyi_podshipnik_iz_sic_connectors
  - часть_poristyi_gazovyi_podshipnik_iz_sic_mounting
материалы_частей:
  - часть: часть_poristyi_gazovyi_podshipnik_iz_sic_core
    материал: generic_material
    доля_массы: 0.45
  - часть: часть_poristyi_gazovyi_podshipnik_iz_sic_housing
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
# Изделие: пористый газовый подшипник из SiC

## Описание

пористый газовый подшипник из SiC (NewWay Air Bearings)

Полное наименование (как в CSV): `пористый газовый подшипник из SiC (NewWay Air Bearings)`

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
    poristyi_gazovyi_pod["izdelie_poristyi_gazovyi_podshipnik_iz_sic"]
    poristyi_gazovyi_podshipn["часть_poristyi_gazovyi_podshipnik_iz_sic_core"]
    poristyi_gazovyi_pod --> poristyi_gazovyi_podshipn
    poristyi_gazovyi_podshipn["часть_poristyi_gazovyi_podshipnik_iz_sic_housing"]
    poristyi_gazovyi_pod --> poristyi_gazovyi_podshipn
    poristyi_gazovyi_podshipn["часть_poristyi_gazovyi_podshipnik_iz_sic_connectors"]
    poristyi_gazovyi_pod --> poristyi_gazovyi_podshipn
    poristyi_gazovyi_podshipn["часть_poristyi_gazovyi_podshipnik_iz_sic_mounting"]
    poristyi_gazovyi_pod --> poristyi_gazovyi_podshipn
```
