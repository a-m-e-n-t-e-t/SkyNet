---
id: izdelie_reshetchatyi_karkas
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: каркас
подтип: прочее
стандарты: 
  - ASTM A36
  - ISO 630
исследовательская_группа: boeing_lockheed
родитель: null
дочерние_части:
  - часть_reshetchatyi_karkas_core
  - часть_reshetchatyi_karkas_housing
  - часть_reshetchatyi_karkas_connectors
  - часть_reshetchatyi_karkas_mounting
материалы_частей:
  - часть: часть_reshetchatyi_karkas_core
    материал: generic_material
    доля_массы: 0.45
  - часть: часть_reshetchatyi_karkas_housing
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
          min: 1
          max: 1000
          nominal: 50
  габариты_mm:
          l: 500
          w: 500
          h: 500
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
источник_url: https://lectromec.com/blog/connector-contact-resistance
источник_дата: 2026-11-07
---
# Изделие: Решётчатый каркас

## Описание

Решётчатый каркас (SLM + HIP)

Полное наименование (как в CSV): `Решётчатый каркас (SLM + HIP)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | каркас | — | classify_subsystem |
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

## Тепловой баланс

Сборка — пассивная несущая рама (SLM + HIP): собственное тепловыделение конструкции равно нулю, тепло генерируют только электрически нагруженные контакты разъёмов (часть_reshetchatyi_karkas_connectors, 24-pin mixed signal + power).

Расчёт Σ детей (F15b):
- core — 0 Вт (пассивная сотовая Al 6061-T6, источников тепла нет; ранее — шаблонные 1 Вт, сняты 2026-11-07);
- housing — 0 Вт (пассивный кожух);
- connectors — 0.1 Вт: ohmic-нагрев контактов, P = I²R. Типовое контактное сопротивление силового контакта ~7.3 мОм (Lectromec: 55 мВ при 7.5 А → 0.41 Вт на контакт); сигнальные контакты (десятки мА) — пренебрежимо. Для набора из 24 контактов mixed signal+power с единичным силовым контактом, нагруженным частично: Σ ≈ 0.1 Вт;
- mounting — 0 Вт (кронштейны).

Σ(детей) = 0.1 Вт ≤ номинал родителя 0.1 Вт → F15b PASS (собственное тепловыделение рамы 0, максимум 0.2 Вт — резерв на деградацию контактов ×2).

Ранее родитель имел 0 Вт при Σ детей 1.10 Вт (шаблонная 1 Вт у core + 0.1 Вт разъёмы) — нарушение F15b (issue #767).

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- Контактное сопротивление разъёмов и ohmic-нагрев (7.3 мОм @ 7.5 А → 0.41 Вт/контакт) — https://lectromec.com/blog/connector-contact-resistance (обращение 2026-11-07)
- Пассивность несущих сотовых/изогрид-конструкций — https://www.beyondgravity.com/en/satellites/mechanical-solutions/satellite-structures (обращение 2026-11-07)

---


## Декомпозиция

```mermaid
graph TD
    reshetchatyi_karkas["izdelie_reshetchatyi_karkas"]
    reshetchatyi_karkas_core["часть_reshetchatyi_karkas_core"]
    reshetchatyi_karkas --> reshetchatyi_karkas_core
    reshetchatyi_karkas_housi["часть_reshetchatyi_karkas_housing"]
    reshetchatyi_karkas --> reshetchatyi_karkas_housi
    reshetchatyi_karkas_conne["часть_reshetchatyi_karkas_connectors"]
    reshetchatyi_karkas --> reshetchatyi_karkas_conne
    reshetchatyi_karkas_mount["часть_reshetchatyi_karkas_mounting"]
    reshetchatyi_karkas --> reshetchatyi_karkas_mount
```
