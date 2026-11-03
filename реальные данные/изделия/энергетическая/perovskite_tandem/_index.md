---
id: izdelie_perovskite_tandem
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: фотоэлектрический_модуль
стандарты: 
  - IEC 61215
  - IEC 61730
исследовательская_группа: oxford_pv
родитель: null
дочерние_части:
  - часть_perovskite_tandem_cells
  - часть_perovskite_tandem_front_glass
  - часть_perovskite_tandem_backsheet
  - часть_perovskite_tandem_frame
  - часть_perovskite_tandem_junction_box
  - часть_perovskite_tandem_encapsulant
материалы_частей:
  - часть: часть_perovskite_tandem_cells
    материал: monocrystalline_si
    доля_массы: 0.38
  - часть: часть_perovskite_tandem_front_glass
    материал: low_iron_glass
    доля_массы: 0.285
  - часть: часть_perovskite_tandem_backsheet
    материал: tedlar_pet
    доля_массы: 0.095
  - часть: часть_perovskite_tandem_frame
    материал: aluminum_6063
    доля_массы: 0.19
  - часть: часть_perovskite_tandem_encapsulant
    материал: eva
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
          min: 1
          max: 30
          nominal: 10
  габариты_mm:
          l: 1500
          w: 1000
          h: 5
  выработка_энергии_W:
          min: 100
          max: 500
          nominal: 300
  выработка_тепла_W:
          min: 50
          max: 200
          nominal: 100
наследуемые: {}
дополнительные: 
  КПД_процентов: 33
  источник: Oxford PV perovskite-on-silicon tandem
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Perovskite tandem

## Описание

Perovskite tandem (солнечная ячейка)

Полное наименование (как в CSV): `Perovskite tandem (солнечная ячейка)`

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
    perovskite_tandem["izdelie_perovskite_tandem"]
    perovskite_tandem_cells["часть_perovskite_tandem_cells"]
    perovskite_tandem --> perovskite_tandem_cells
    perovskite_tandem_front_g["часть_perovskite_tandem_front_glass"]
    perovskite_tandem --> perovskite_tandem_front_g
    perovskite_tandem_backshe["часть_perovskite_tandem_backsheet"]
    perovskite_tandem --> perovskite_tandem_backshe
    perovskite_tandem_frame["часть_perovskite_tandem_frame"]
    perovskite_tandem --> perovskite_tandem_frame
    perovskite_tandem_junctio["часть_perovskite_tandem_junction_box"]
    perovskite_tandem --> perovskite_tandem_junctio
    perovskite_tandem_encapsu["часть_perovskite_tandem_encapsulant"]
    perovskite_tandem --> perovskite_tandem_encapsu
```
