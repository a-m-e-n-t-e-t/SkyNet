---
id: izdelie_vodorodnye_toplivnye_elementy
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: водородный_топливный_элемент
стандарты: 
  - IEC 62282
  - ISO 14687
исследовательская_группа: ballard_power
родитель: null
дочерние_части:
  - часть_vodorodnye_toplivnye_elementy_membrane
  - часть_vodorodnye_toplivnye_elementy_catalyst_anode
  - часть_vodorodnye_toplivnye_elementy_catalyst_cathode
  - часть_vodorodnye_toplivnye_elementy_gdl_anode
  - часть_vodorodnye_toplivnye_elementy_gdl_cathode
  - часть_vodorodnye_toplivnye_elementy_bipolar_plate
  - часть_vodorodnye_toplivnye_elementy_gasket
  - часть_vodorodnye_toplivnye_elementy_end_plate
материалы_частей:
  - часть: часть_vodorodnye_toplivnye_elementy_membrane
    материал: nafion_117
    доля_массы: 0.095
  - часть: часть_vodorodnye_toplivnye_elementy_catalyst_anode
    материал: pt_carbon
    доля_массы: 0.01
  - часть: часть_vodorodnye_toplivnye_elementy_catalyst_cathode
    материал: pt_carbon
    доля_массы: 0.01
  - часть: часть_vodorodnye_toplivnye_elementy_gdl_anode
    материал: carbon_paper
    доля_массы: 0.095
  - часть: часть_vodorodnye_toplivnye_elementy_bipolar_plate
    материал: stainless_steel_316
    доля_массы: 0.38
  - часть: часть_vodorodnye_toplivnye_elementy_end_plate
    материал: aluminum
    доля_массы: 0.285
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
          max: 100
          nominal: 25
  габариты_mm:
          l: 300
          w: 200
          h: 200
  выработка_энергии_W:
          min: 100
          max: 5000
          nominal: 1000
  выработка_тепла_W:
          min: 100
          max: 5000
          nominal: 1000
наследуемые: {}
дополнительные: 
  T_рабочая_C: 80
  КПД_процентов: 50
  источник: Ballard PEM fuel cell
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Водородные топливные элементы

## Описание

Водородные топливные элементы (PEM)

Полное наименование (как в CSV): `Водородные топливные элементы (PEM)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
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
    vodorodnye_toplivnye["izdelie_vodorodnye_toplivnye_elementy"]
    vodorodnye_toplivnye_elem["часть_vodorodnye_toplivnye_elementy_membrane"]
    vodorodnye_toplivnye --> vodorodnye_toplivnye_elem
    vodorodnye_toplivnye_elem["часть_vodorodnye_toplivnye_elementy_catalyst_anode"]
    vodorodnye_toplivnye --> vodorodnye_toplivnye_elem
    vodorodnye_toplivnye_elem["часть_vodorodnye_toplivnye_elementy_catalyst_cathode"]
    vodorodnye_toplivnye --> vodorodnye_toplivnye_elem
    vodorodnye_toplivnye_elem["часть_vodorodnye_toplivnye_elementy_gdl_anode"]
    vodorodnye_toplivnye --> vodorodnye_toplivnye_elem
    vodorodnye_toplivnye_elem["часть_vodorodnye_toplivnye_elementy_gdl_cathode"]
    vodorodnye_toplivnye --> vodorodnye_toplivnye_elem
    vodorodnye_toplivnye_elem["часть_vodorodnye_toplivnye_elementy_bipolar_plate"]
    vodorodnye_toplivnye --> vodorodnye_toplivnye_elem
    vodorodnye_toplivnye_elem["часть_vodorodnye_toplivnye_elementy_gasket"]
    vodorodnye_toplivnye --> vodorodnye_toplivnye_elem
    vodorodnye_toplivnye_elem["часть_vodorodnye_toplivnye_elementy_end_plate"]
    vodorodnye_toplivnye --> vodorodnye_toplivnye_elem
```
