---
id: izdelie_litii-tionilhloridnye_batarei
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: литий-тионилхлоридная_батарея
стандарты: 
  - IEC 60086
  - UN 3090
исследовательская_группа: saft_tadiran
родитель: null
дочерние_части:
  - часть_litii-tionilhloridnye_batarei_anode
  - часть_litii-tionilhloridnye_batarei_cathode
  - часть_litii-tionilhloridnye_batarei_electrolyte
  - часть_litii-tionilhloridnye_batarei_separator
  - часть_litii-tionilhloridnye_batarei_case
  - часть_litii-tionilhloridnye_batarei_terminal
материалы_частей:
  - часть: часть_litii-tionilhloridnye_batarei_anode
    материал: lithium_metal
    доля_массы: 0.19
  - часть: часть_litii-tionilhloridnye_batarei_cathode
    материал: carbon_black
    доля_массы: 0.18
  - часть: часть_litii-tionilhloridnye_batarei_electrolyte
    материал: socl2
    доля_массы: 0.38
  - часть: часть_litii-tionilhloridnye_batarei_separator
    материал: pp_membrane
    доля_массы: 0.019
  - часть: часть_litii-tionilhloridnye_batarei_case
    материал: stainless_steel_304
    доля_массы: 0.19
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
          max: 1.0
          nominal: 0.3
  габариты_mm:
          l: 50
          w: 25
          h: 25
  выработка_энергии_W:
          min: 0.001
          max: 1
          nominal: 0.1
  выработка_тепла_W:
          min: 0.001
          max: 0.1
          nominal: 0.01
наследуемые: {}
дополнительные: 
  ёмкость_Ач: 19
  V: 3.6
  T_хранения_лет: 20
  источник: Saft LSH20 datasheet
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Литий-тионилхлоридные батареи

## Описание

Литий-тионилхлоридные батареи (Li-SOCl₂)

Полное наименование (как в CSV): `Литий-тионилхлоридные батареи (Li-SOCl₂)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | вычислительная | — | classify_subsystem |
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
    litii-tionilhloridny["izdelie_litii-tionilhloridnye_batarei"]
    litii-tionilhloridnye_bat["часть_litii-tionilhloridnye_batarei_anode"]
    litii-tionilhloridny --> litii-tionilhloridnye_bat
    litii-tionilhloridnye_bat["часть_litii-tionilhloridnye_batarei_cathode"]
    litii-tionilhloridny --> litii-tionilhloridnye_bat
    litii-tionilhloridnye_bat["часть_litii-tionilhloridnye_batarei_electrolyte"]
    litii-tionilhloridny --> litii-tionilhloridnye_bat
    litii-tionilhloridnye_bat["часть_litii-tionilhloridnye_batarei_separator"]
    litii-tionilhloridny --> litii-tionilhloridnye_bat
    litii-tionilhloridnye_bat["часть_litii-tionilhloridnye_batarei_case"]
    litii-tionilhloridny --> litii-tionilhloridnye_bat
    litii-tionilhloridnye_bat["часть_litii-tionilhloridnye_batarei_terminal"]
    litii-tionilhloridny --> litii-tionilhloridnye_bat
```
