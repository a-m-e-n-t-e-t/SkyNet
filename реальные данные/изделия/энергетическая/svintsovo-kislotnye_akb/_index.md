---
id: izdelie_svintsovo-kislotnye_akb
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: свинцово-кислотная_батарея
стандарты: 
  - IEC 60095
  - JIS D5301
исследовательская_группа: exide
родитель: null
дочерние_части:
  - часть_svintsovo-kislotnye_akb_anode
  - часть_svintsovo-kislotnye_akb_cathode
  - часть_svintsovo-kislotnye_akb_electrolyte
  - часть_svintsovo-kislotnye_akb_separator
  - часть_svintsovo-kislotnye_akb_grid_pos
  - часть_svintsovo-kislotnye_akb_case
  - часть_svintsovo-kislotnye_akb_terminal
материалы_частей:
  - часть: часть_svintsovo-kislotnye_akb_anode
    материал: pbo2
    доля_массы: 0.19
  - часть: часть_svintsovo-kislotnye_akb_cathode
    материал: spongy_lead
    доля_массы: 0.19
  - часть: часть_svintsovo-kislotnye_akb_electrolyte
    материал: h2so4_aqueous
    доля_массы: 0.285
  - часть: часть_svintsovo-kislotnye_akb_separator
    материал: pe_separator
    доля_массы: 0.019
  - часть: часть_svintsovo-kislotnye_akb_grid_pos
    материал: pb_sb_alloy
    доля_массы: 0.095
  - часть: часть_svintsovo-kislotnye_akb_case
    материал: polypropylene
    доля_массы: 0.095
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
          min: 5
          max: 50
          nominal: 15
  габариты_mm:
          l: 350
          w: 175
          h: 190
  выработка_энергии_W:
          min: 50
          max: 1000
          nominal: 500
  выработка_тепла_W:
          min: 1
          max: 50
          nominal: 10
наследуемые: {}
дополнительные: 
  ёмкость_Ач: 100
  V: 12
  T_жизни_циклы: 500
  источник: Exide lead-acid battery
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: свинцово-кислотные АКБ

## Описание

свинцово-кислотные АКБ

Полное наименование (как в CSV): `свинцово-кислотные АКБ`

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
    svintsovo-kislotnye_["izdelie_svintsovo-kislotnye_akb"]
    svintsovo-kislotnye_akb_a["часть_svintsovo-kislotnye_akb_anode"]
    svintsovo-kislotnye_ --> svintsovo-kislotnye_akb_a
    svintsovo-kislotnye_akb_c["часть_svintsovo-kislotnye_akb_cathode"]
    svintsovo-kislotnye_ --> svintsovo-kislotnye_akb_c
    svintsovo-kislotnye_akb_e["часть_svintsovo-kislotnye_akb_electrolyte"]
    svintsovo-kislotnye_ --> svintsovo-kislotnye_akb_e
    svintsovo-kislotnye_akb_s["часть_svintsovo-kislotnye_akb_separator"]
    svintsovo-kislotnye_ --> svintsovo-kislotnye_akb_s
    svintsovo-kislotnye_akb_g["часть_svintsovo-kislotnye_akb_grid_pos"]
    svintsovo-kislotnye_ --> svintsovo-kislotnye_akb_g
    svintsovo-kislotnye_ --> svintsovo-kislotnye_akb_g
    svintsovo-kislotnye_akb_c["часть_svintsovo-kislotnye_akb_case"]
    svintsovo-kislotnye_ --> svintsovo-kislotnye_akb_c
    svintsovo-kislotnye_akb_t["часть_svintsovo-kislotnye_akb_terminal"]
    svintsovo-kislotnye_ --> svintsovo-kislotnye_akb_t
```
