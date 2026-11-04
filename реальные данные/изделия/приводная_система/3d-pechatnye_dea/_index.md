---
id: izdelie_3d-pechatnye_dea
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: приводная_система
подтип: прочее
стандарты: 
  - IEC 60034
  - ISO 1940
исследовательская_группа: maxon_faulhaber
родитель: null
дочерние_части:
  - часть_3d-pechatnye_dea_core
  - часть_3d-pechatnye_dea_housing
  - часть_3d-pechatnye_dea_connectors
  - часть_3d-pechatnye_dea_mounting
материалы_частей:
  - часть: часть_3d-pechatnye_dea_core
    материал: generic_material
    доля_массы: 0.45
  - часть: часть_3d-pechatnye_dea_housing
    материал: aluminum
    доля_массы: 0.27
  - часть: часть_3d-pechatnye_dea_connectors
    материал: becu
    доля_массы: 0.05
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
          max: 50
          nominal: 1
  габариты_mm:
          l: 100
          w: 50
          h: 50
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.1
          max: 50
          nominal: 5
наследуемые: {}
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: 3D-печатные DEA

## Описание

3D-печатные DEA

Полное наименование (как в CSV): `3D-печатные DEA`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | приводная_система | — | classify_subsystem |
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
    3d-pechatnye_dea["izdelie_3d-pechatnye_dea"]
    3d-pechatnye_dea_core["часть_3d-pechatnye_dea_core"]
    3d-pechatnye_dea --> 3d-pechatnye_dea_core
    3d-pechatnye_dea_housing["часть_3d-pechatnye_dea_housing"]
    3d-pechatnye_dea --> 3d-pechatnye_dea_housing
    3d-pechatnye_dea_connecto["часть_3d-pechatnye_dea_connectors"]
    3d-pechatnye_dea --> 3d-pechatnye_dea_connecto
    3d-pechatnye_dea_mounting["часть_3d-pechatnye_dea_mounting"]
    3d-pechatnye_dea --> 3d-pechatnye_dea_mounting
```
