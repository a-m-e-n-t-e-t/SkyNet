---
id: izdelie_alyuminievo-vozdushnye_toplivnye_elementy
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: алюминиево-воздушный_ТЭ
стандарты: 
  - IEC 62282
исследовательская_группа: phiotech
родитель: null
дочерние_части:
  - часть_alyuminievo-vozdushnye_toplivnye_elementy_anode
  - часть_alyuminievo-vozdushnye_toplivnye_elementy_cathode
  - часть_alyuminievo-vozdushnye_toplivnye_elementy_electrolyte
  - часть_alyuminievo-vozdushnye_toplivnye_elementy_separator
  - часть_alyuminievo-vozdushnye_toplivnye_elementy_air_electrode
  - часть_alyuminievo-vozdushnye_toplivnye_elementy_housing
материалы_частей:
  - часть: часть_alyuminievo-vozdushnye_toplivnye_elementy_anode
    материал: aluminum_1100
    форма: расходуемые_аноды_металл-воздушных_батарей
    доля_массы: 0.38
  - часть: часть_alyuminievo-vozdushnye_toplivnye_elementy_cathode
    материал: carbon_ptfe
    форма: воздушные_катоды_металл-воздушных_батарей
    доля_массы: 0.18
  - часть: часть_alyuminievo-vozdushnye_toplivnye_elementy_electrolyte
    материал: koh_aqueous
    форма: электролиты_металл-воздушных_батарей
    доля_массы: 0.19
  - часть: часть_alyuminievo-vozdushnye_toplivnye_elementy_air_electrode
    материал: carbon_ptfe
    форма: воздушные_катоды_металл-воздушных_батарей
    доля_массы: 0.002
технологии_частей:
  - часть: часть_alyuminievo-vozdushnye_toplivnye_elementy_anode
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: aluminum
        роль: обрабатываемый
  - часть: часть_alyuminievo-vozdushnye_toplivnye_elementy_cathode
    технология: gidrofobnoe_pokrytie
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: carbon_ptfe
        роль: обрабатываемый
  - часть: часть_alyuminievo-vozdushnye_toplivnye_elementy_air_electrode
    технология: gidrofobnoe_pokrytie
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: carbon_ptfe
        роль: обрабатываемый
наследуемые_материалы:
  - материал: aluminum_1100
    суммарная_доля_массы: 0.38
    источники_частей:
      - часть_alyuminievo-vozdushnye_toplivnye_elementy_anode
  - материал: karbon
    суммарная_доля_массы: 0.18
    источники_частей:
      - часть_alyuminievo-vozdushnye_toplivnye_elementy_cathode
  - материал: ptfe
    суммарная_доля_массы: 0.19
    источники_частей:
      - часть_alyuminievo-vozdushnye_toplivnye_elementy_electrolyte
  - материал: carbon_ptfe
    суммарная_доля_массы: 0.002
    источники_частей:
      - часть_alyuminievo-vozdushnye_toplivnye_elementy_air_electrode
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
          min: 0.5
          max: 50
          nominal: 5
  габариты_mm:
          l: 420
          w: 310
          h: 300
  выработка_энергии_W:
          min: 10
          max: 1000
          nominal: 100
  выработка_тепла_W:
          min: 10
          max: 1000
          nominal: 100
наследуемые: {}
дополнительные: 
  T_рабочая_C: 60
  КПД_процентов: 40
  обоснование_габаритов: 'модуль = корпус ячейки 420×300×250 (часть_housing) + воздушный коллектор с крышкой и заливочной горловиной сверху (+50 мм по h, +10 мм по w на подвод электролита) — компоновка типовых Al-air модулей: пакет пластин + верхняя крышка + система электролита (патент CN112542637B); V(bbox)=420×310×300=39 060 000 мм³ ≥ ΣV(детей)×1.15=37 538 520 мм³ (Σ V детей=32 642 191, запас ×1.04); оси: l 420 ≥ max_child 420 (housing), w 310 ≥ 300 (housing), h 300 ≥ 250 (housing)'
  источник: Al-air fuel cell research
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Алюминиево-воздушные топливные элементы

## Описание

Алюминиево-воздушные топливные элементы

Полное наименование (как в CSV): `Алюминиево-воздушные топливные элементы`

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
    alyuminievo-vozdushn["izdelie_alyuminievo-vozdushnye_toplivnye_elementy"]
    alyuminievo-vozdushnye_to["часть_alyuminievo-vozdushnye_toplivnye_elementy_anode"]
    alyuminievo-vozdushn --> alyuminievo-vozdushnye_to
    alyuminievo-vozdushnye_to["часть_alyuminievo-vozdushnye_toplivnye_elementy_cathode"]
    alyuminievo-vozdushn --> alyuminievo-vozdushnye_to
    alyuminievo-vozdushnye_to["часть_alyuminievo-vozdushnye_toplivnye_elementy_electrolyte"]
    alyuminievo-vozdushn --> alyuminievo-vozdushnye_to
    alyuminievo-vozdushnye_to["часть_alyuminievo-vozdushnye_toplivnye_elementy_separator"]
    alyuminievo-vozdushn --> alyuminievo-vozdushnye_to
    alyuminievo-vozdushnye_to["часть_alyuminievo-vozdushnye_toplivnye_elementy_air_electrode"]
    alyuminievo-vozdushn --> alyuminievo-vozdushnye_to
    alyuminievo-vozdushnye_to["часть_alyuminievo-vozdushnye_toplivnye_elementy_housing"]
    alyuminievo-vozdushn --> alyuminievo-vozdushnye_to
```
