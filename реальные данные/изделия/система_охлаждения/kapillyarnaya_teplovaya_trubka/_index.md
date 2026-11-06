---
id: izdelie_kapillyarnaya_teplovaya_trubka
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: система_охлаждения
подтип: прочее
стандарты: 
  - ASHRAE 15
исследовательская_группа: boyd_corp
родитель: null
дочерние_части:
  - часть_kapillyarnaya_teplovaya_trubka_core
  - часть_kapillyarnaya_teplovaya_trubka_housing
  - часть_kapillyarnaya_teplovaya_trubka_connectors
  - часть_kapillyarnaya_teplovaya_trubka_mounting
материалы_частей:
  - часть: часть_kapillyarnaya_teplovaya_trubka_core
    материал: generic_material
    доля_массы: 0.45
  - часть: часть_kapillyarnaya_teplovaya_trubka_housing
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
          l: 200
          w: 100
          h: 5
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0
          max: 0.2
          nominal: 0.1
наследуемые: {}
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: 2026-11-07
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: капиллярная тепловая трубка

## Описание

капиллярная тепловая трубка (heat pipe)

Полное наименование (как в CSV): `капиллярная тепловая трубка (heat pipe)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | система_охлаждения | — | classify_subsystem |
| категория | прочее | — | — |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Тепловой баланс (F15b)

Капиллярная тепловая трубка — пассивное устройство переноса тепла: испарение рабочего тела в зоне нагрева, конденсация в зоне охлаждения, возврат жидкости капиллярной силой фитиля. Собственного источника питания нет — «No power source (other than heat) is needed» (ACT, Heat Pipes 101): трубка ПЕРЕНОСИТ тепло (до 30 Вт для Ø6×200), а не вырабатывает его; внутренние потери — перепады ΔT на стенке/фитиле/паровом канале, а не теплогенерация. Единственный реальный источник тепла в сборке — контактные I²R-потери разъёма нагревателя (M12 Power K-code): ~0.1 Вт при переходном сопротивлении мОм-диапазона (Lectromec).

| Часть | Тепло, Вт | Механизм |
|---|---|---|
| core (медная трубка с водой) | 0 | пассивный перенос тепла, не генератор |
| housing (алюминиевый кожух) | 0 | пассивная оболочка |
| connectors (M12) | 0.1 | I²R контактов (мОм-диапазон) |
| mounting (прижим) | 0 | пассивный крепёж |

Σ детей = 0.1 Вт ≤ номинала родителя 0.1 Вт — F15b выполнено; max 0.2 Вт — запас ×2 на деградацию контактов (Lectromec: рост переходного сопротивления с циклами сочленения).

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

- ACT (Advanced Cooling Technologies), Heat Pipes 101 — пассивный двухфазный перенос тепла без движущихся частей («No power source (other than heat) is needed»); эффективная теплопроводность до 100 000 Вт/(м·К); потери внутри — ΔT на участках, не теплогенерация: https://www.1-act.com/thermal-solutions/passive/heat-pipes/heat-pipes-101/ (обращение 2026-11-07)
- Lectromec — Connector Contact Resistance (переходное сопротивление контактов мОм-диапазона; I²R-потери при протекании тока): https://lectromec.com/blog/connector-contact-resistance (обращение 2026-11-07)

## Декомпозиция

```mermaid
graph TD
    kapillyarnaya_teplov["izdelie_kapillyarnaya_teplovaya_trubka"]
    kapillyarnaya_teplovaya_t["часть_kapillyarnaya_teplovaya_trubka_core"]
    kapillyarnaya_teplov --> kapillyarnaya_teplovaya_t
    kapillyarnaya_teplovaya_t["часть_kapillyarnaya_teplovaya_trubka_housing"]
    kapillyarnaya_teplov --> kapillyarnaya_teplovaya_t
    kapillyarnaya_teplovaya_t["часть_kapillyarnaya_teplovaya_trubka_connectors"]
    kapillyarnaya_teplov --> kapillyarnaya_teplovaya_t
    kapillyarnaya_teplovaya_t["часть_kapillyarnaya_teplovaya_trubka_mounting"]
    kapillyarnaya_teplov --> kapillyarnaya_teplovaya_t
```
