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
    доля_массы: 0.38
  - часть: часть_alyuminievo-vozdushnye_toplivnye_elementy_cathode
    материал: carbon_ptfe
    доля_массы: 0.18
  - часть: часть_alyuminievo-vozdushnye_toplivnye_elementy_electrolyte
    материал: koh_aqueous
    доля_массы: 0.19
  - часть: часть_alyuminievo-vozdushnye_toplivnye_elementy_air_electrode
    материал: carbon_ptfe
    доля_массы: 0.002
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
          l: 200
          w: 150
          h: 100
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
