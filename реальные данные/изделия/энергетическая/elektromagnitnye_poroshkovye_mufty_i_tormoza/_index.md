---
id: izdelie_elektromagnitnye_poroshkovye_mufty_i_tormoza
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: электромагнитная_муфта
стандарты: 
  - DIN VDE 0580
исследовательская_группа: kendrion_mayr
родитель: null
дочерние_части:
  - часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_coil
  - часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_rotor
  - часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_stator
  - часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_powder
  - часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_bearings
  - часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_housing
материалы_частей:
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_coil
    материал: copper
    доля_массы: 0.18
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_rotor
    материал: steel_1045
    доля_массы: 0.285
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_stator
    материал: steel_1045
    доля_массы: 0.285
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_powder
    материал: iron_powder
    доля_массы: 0.057
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_bearings
    материал: stainless_steel_440c
    доля_массы: 0.054
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
          w: 100
          h: 100
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 1
          max: 100
          nominal: 10
наследуемые: {}
дополнительные: 
  M_ном_Нм: 50
  источник: Kendrion / Mayr electromagnetic clutches
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: электромагнитные порошковые муфты и тормоза

## Описание

электромагнитные порошковые муфты и тормоза (magnetic particle brake/clutch)

Полное наименование (как в CSV): `электромагнитные порошковые муфты и тормоза (magnetic particle brake/clutch)`

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
    elektromagnitnye_por["izdelie_elektromagnitnye_poroshkovye_mufty_i_tormoza"]
    elektromagnitnye_poroshko["часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_coil"]
    elektromagnitnye_por --> elektromagnitnye_poroshko
    elektromagnitnye_poroshko["часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_rotor"]
    elektromagnitnye_por --> elektromagnitnye_poroshko
    elektromagnitnye_poroshko["часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_stator"]
    elektromagnitnye_por --> elektromagnitnye_poroshko
    elektromagnitnye_poroshko["часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_powder"]
    elektromagnitnye_por --> elektromagnitnye_poroshko
    elektromagnitnye_poroshko["часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_bearings"]
    elektromagnitnye_por --> elektromagnitnye_poroshko
    elektromagnitnye_poroshko["часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_housing"]
    elektromagnitnye_por --> elektromagnitnye_poroshko
```
