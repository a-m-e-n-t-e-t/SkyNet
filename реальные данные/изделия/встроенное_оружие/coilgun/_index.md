---
id: izdelie_coilgun
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: встроенное_оружие
подтип: электромагнитный_ускоритель
стандарты: []
исследовательская_группа: sandia_labs
родитель: null
дочерние_части:
  - часть_coilgun_coil
  - часть_coilgun_capacitor_bank
  - часть_coilgun_barrel
  - часть_coilgun_switch
  - часть_coilgun_projectile
  - часть_coilgun_housing
материалы_частей:
  - часть: часть_coilgun_coil
    материал: copper
    доля_массы: 0.38
  - часть: часть_coilgun_capacitor_bank
    материал: aluminum_electrolytic
    доля_массы: 0.36
  - часть: часть_coilgun_barrel
    материал: composite_material
    доля_массы: 0.09
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
          min: 100
          max: 10000
          nominal: 1000
  габариты_mm:
          l: 5000
          w: 1000
          h: 1500
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 100
          max: 10000
          nominal: 1000
наследуемые: {}
дополнительные: 
  V_снаряд_км_с: 3
  источник: Sandia coilgun research
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Coilgun

## Описание

Coilgun (электромагнитная катапульта) — рельсовое оружие

Полное наименование (как в CSV): `Coilgun (электромагнитная катапульта) — рельсовое оружие`

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
    coilgun["izdelie_coilgun"]
    coilgun_coil["часть_coilgun_coil"]
    coilgun --> coilgun_coil
    coilgun_capacitor_bank["часть_coilgun_capacitor_bank"]
    coilgun --> coilgun_capacitor_bank
    coilgun_barrel["часть_coilgun_barrel"]
    coilgun --> coilgun_barrel
    coilgun_switch["часть_coilgun_switch"]
    coilgun --> coilgun_switch
    coilgun_projectile["часть_coilgun_projectile"]
    coilgun --> coilgun_projectile
    coilgun_housing["часть_coilgun_housing"]
    coilgun --> coilgun_housing
```
