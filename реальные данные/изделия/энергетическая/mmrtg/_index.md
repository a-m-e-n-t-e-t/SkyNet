---
id: izdelie_mmrtg
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: радиоизотопный_генератор
стандарты: 
  - NASA-STD-8729.1
  - DOE 10 CFR 71
исследовательская_группа: nasa_glenn
родитель: null
дочерние_части:
  - часть_mmrtg_isotope
  - часть_mmrtg_thermocouples
  - часть_mmrtg_cold_side
  - часть_mmrtg_hot_side
  - часть_mmrtg_housing
  - часть_mmrtg_thermal_insulation
  - часть_mmrtg_connector
материалы_частей:
  - часть: часть_mmrtg_isotope
    материал: dioksid_plutoniya-238
    форма: ртэг_генераторы
    доля_массы: 0.38
  - часть: часть_mmrtg_thermocouples
    материал: pbte_teg
    форма: mmrtg_couple
    доля_массы: 0.27
  - часть: часть_mmrtg_cold_side
    материал: aluminum
    форма: теплоотводящие_узлы
    доля_массы: 0.1425
  - часть: часть_mmrtg_housing
    материал: titanium_alloy
    форма: forged_bar_ams_4928
    доля_массы: 0.285
  - часть: часть_mmrtg_thermal_insulation
    материал: sio2_amorphous
    форма: pyrogel_xte_промышленный_высокотемпературный
    доля_массы: 0.09

технологии_частей:
  - часть: часть_mmrtg_isotope
    технология: vakuumnoe_spekanie
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: dioksid_plutoniya-238
        роль: обрабатываемый
  - часть: часть_mmrtg_thermocouples
    технология: payka_silovyh_kontaktov
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: pbte_teg
        роль: обрабатываемый
  - часть: часть_mmrtg_cold_side
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: al_6063-t5
        роль: обрабатываемый
  - часть: часть_mmrtg_housing
    технология: ebw
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: al_6061-t6
        роль: обрабатываемый
  - часть: часть_mmrtg_thermal_insulation
    технология: sborka_v_termoizolyatsionnoi_opravke
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: sio2_amorphous
        роль: обрабатываемый

наследуемые_материалы:
  - материал: dioksid_plutoniya-238
    форма: ртэг_генераторы
    суммарная_доля_массы: 0.38
    источники_частей:
      - часть_mmrtg_isotope
  - материал: pbte_teg
    форма: mmrtg_couple
    суммарная_доля_массы: 0.27
    источники_частей:
      - часть_mmrtg_thermocouples
  - материал: al_6063-t5
    форма: T5_стенка_до_13мм
    суммарная_доля_массы: 0.1425
    источники_частей:
      - часть_mmrtg_cold_side
  - материал: al_6061-t6
    форма: корпуса_электроники
    суммарная_доля_массы: 0.285
    источники_частей:
      - часть_mmrtg_housing
  - материал: sio2_amorphous
    форма: pyrogel_xte_промышленный_высокотемпературный
    суммарная_доля_массы: 0.09
    источники_частей:
      - часть_mmrtg_thermal_insulation

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
          min: 40
          max: 50
          nominal: 45
  выработка_энергии_W:
          min: 100
          max: 130
          nominal: 110
  выработка_тепла_W:
          min: 1500
          max: 2000
          nominal: 2000
наследуемые: {}
дополнительные: 
  изотоп: Pu-238
  T_жизни_лет: 17
  источник: NASA Multi-Mission RTG (MMRTG) — Mars 2020 Perseverance
дата_создания: 2026-11-03
дата_обновления: 2026-11-09
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: MMRTG

## Описание

MMRTG

Полное наименование (как в CSV): `MMRTG`

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
    mmrtg["izdelie_mmrtg"]
    mmrtg_isotope["часть_mmrtg_isotope"]
    mmrtg --> mmrtg_isotope
    mmrtg_thermocouples["часть_mmrtg_thermocouples"]
    mmrtg --> mmrtg_thermocouples
    mmrtg_cold_side["часть_mmrtg_cold_side"]
    mmrtg --> mmrtg_cold_side
    mmrtg_hot_side["часть_mmrtg_hot_side"]
    mmrtg --> mmrtg_hot_side
    mmrtg_housing["часть_mmrtg_housing"]
    mmrtg --> mmrtg_housing
    mmrtg_thermal_insulation["часть_mmrtg_thermal_insulation"]
    mmrtg --> mmrtg_thermal_insulation
    mmrtg_connector["часть_mmrtg_connector"]
    mmrtg --> mmrtg_connector
```
