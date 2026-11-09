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
    форма: PEM_мембрана_топливных_элементов
    доля_массы: 0.095
  - часть: часть_vodorodnye_toplivnye_elementy_catalyst_anode
    материал: pt_carbon
    форма: катализаторы_и_катализаторные_покрытия
    доля_массы: 0.01
  - часть: часть_vodorodnye_toplivnye_elementy_catalyst_cathode
    материал: pt_carbon
    форма: катализаторы_и_катализаторные_покрытия
    доля_массы: 0.01
  - часть: часть_vodorodnye_toplivnye_elementy_gdl_anode
    материал: carbon_paper
    форма: газодиффузионные_слои_топливных_элементов
    доля_массы: 0.095
  - часть: часть_vodorodnye_toplivnye_elementy_bipolar_plate
    материал: stainless_steel_316
    форма: пластина_PEM_стека
    доля_массы: 0.38
  - часть: часть_vodorodnye_toplivnye_elementy_end_plate
    материал: aluminum
    форма: поликристаллический_прокат
    доля_массы: 0.285
технологии_частей:
  - часть: часть_vodorodnye_toplivnye_elementy_membrane
    технология: plazmennaya_aktivatsiya
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: nafion
        роль: обрабатываемый
  - часть: часть_vodorodnye_toplivnye_elementy_catalyst_anode
    технология: dc_magnetron_sputtering
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: pt
        роль: обрабатываемый
  - часть: часть_vodorodnye_toplivnye_elementy_catalyst_cathode
    технология: dc_magnetron_sputtering
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: pt
        роль: обрабатываемый
  - часть: часть_vodorodnye_toplivnye_elementy_gdl_anode
    технология: gidrofobnoe_pokrytie
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: ptfe
        роль: обрабатываемый
  - часть: часть_vodorodnye_toplivnye_elementy_bipolar_plate
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: grafit_kompozit_bpp
        роль: обрабатываемый
  - часть: часть_vodorodnye_toplivnye_elementy_end_plate
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: aluminum
        роль: обрабатываемый
наследуемые_материалы:
  - материал: nafion
    форма: PEM_мембрана_топливных_элементов
    суммарная_доля_массы: 0.095
    источники_частей:
      - часть_vodorodnye_toplivnye_elementy_membrane
  - материал: pt
    форма: катализаторы_и_катализаторные_покрытия
    суммарная_доля_массы: 0.02
    источники_частей:
      - часть_vodorodnye_toplivnye_elementy_catalyst_anode
      - часть_vodorodnye_toplivnye_elementy_catalyst_cathode
  - материал: ptfe
    форма: безкаталитический_углеродный_GDL
    суммарная_доля_массы: 0.095
    источники_частей:
      - часть_vodorodnye_toplivnye_elementy_gdl_anode
  - материал: grafit_kompozit_bpp
    форма: пластина_PEM_стека
    суммарная_доля_массы: 0.38
    источники_частей:
      - часть_vodorodnye_toplivnye_elementy_bipolar_plate
  - материал: ti-6al-4v
    форма: морские_и_химические_среды
    суммарная_доля_массы: 0.285
    источники_частей:
      - часть_vodorodnye_toplivnye_elementy_end_plate
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
          w: 250
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
  обоснование_габаритов: 'огибающая стека PEM ТЭ: активная площадь ячейки 250×250 мм (membrane 250×250×0.183 мм Nafion 117, bipolar_plate 250×250×2 мм, gasket 250×250×0.5 мм, end_plate 250×250×10 мм) — по оси w огибающая = max(дети) = 250 мм (verify #2140); l 300 мм — запас на торцевые коллекторы реагентов и крепёж стека; h 200 мм — стек из ~40 ячеек (шаг ячейки ~5 мм: BPP 2 мм + GDL 2×0.3 мм + мембрана 0.183 мм + уплотнения) + торцевые пластины; V=300×250×200=15 000 000 мм³ ≥ ΣV детей×1.15=947 859 мм³ (ΣV=824 225 мм³: membrane 11 437.5 + catalyst_anode 25 000 + catalyst_cathode 37.5 + gdl_anode 2 800 + gdl_cathode 3 700 + bipolar_plate 125 000 + gasket 31 250 + end_plate 625 000), запас ×15.8'
  обоснование_технологий: 'MEA-цепочка производства PEM ТЭ (web_search, verify #2140): plasma treatment/etching Nafion-мембраны — established стратегия улучшения межфазной адгезии и подавления поляризационных потерь (Ultra-low Mass Sputtered Catalyst, 2017; ANU Fuel Cell Research); магнетронное напыление Pt — ultra-low loading 0.1 мг/см² электроды (Villamayor et al. 2024; Cavarroc et al. 2009 — magnetron co-sputtering C+Pt, cited 154); гидрофобизация PTFE углеродной бумаги GDL (DOE Parts of a Fuel Cell; fuelcellstore GDL); фрезерование каналов ПЧ на графитовых биполярных пластинах — «graphite bipolar plates with machined grooves» (PEMFC schematics, academia.edu Next Generation Bipolar Plates); ЧПУ-фрезерование алюминиевых торцевых пластин с портами коллекторов'
  источник: Ballard PEM fuel cell
дата_создания: 2026-11-03
дата_обновления: 2026-11-09
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
