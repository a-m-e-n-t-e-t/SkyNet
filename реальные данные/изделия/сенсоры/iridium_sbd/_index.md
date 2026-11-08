---
id: izdelie_iridium_sbd
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
  - часть_iridium_sbd_core
  - часть_iridium_sbd_housing
  - часть_iridium_sbd_connectors
  - часть_iridium_sbd_mounting
материалы_частей:
  - часть: часть_iridium_sbd_core
    материал: al_6061-t6
    доля_массы: 0.45
  - часть: часть_iridium_sbd_housing
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
# Изделие: Iridium SBD

## Описание

Iridium SBD (Short Burst Data)

Полное наименование (как в CSV): `Iridium SBD (Short Burst Data)`

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
    iridium_sbd["izdelie_iridium_sbd"]
    iridium_sbd_core["часть_iridium_sbd_core"]
    iridium_sbd --> iridium_sbd_core
    iridium_sbd_housing["часть_iridium_sbd_housing"]
    iridium_sbd --> iridium_sbd_housing
    iridium_sbd_connectors["часть_iridium_sbd_connectors"]
    iridium_sbd --> iridium_sbd_connectors
    iridium_sbd_mounting["часть_iridium_sbd_mounting"]
    iridium_sbd --> iridium_sbd_mounting
```
