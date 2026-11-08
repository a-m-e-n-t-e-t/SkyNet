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
    форма: monocrystalline_wafer
    доля_массы: 0.38
  - часть: часть_perovskite_tandem_front_glass
    материал: low_iron_glass
    форма: ар_покрытие_высокоэффективное
    доля_массы: 0.285
  - часть: часть_perovskite_tandem_backsheet
    материал: tedlar_pet
    форма: tpt_классическая_двусторонняя
    доля_массы: 0.095
  - часть: часть_perovskite_tandem_frame
    материал: al_6063-t5
    форма: T5_стенка_до_13мм
    доля_массы: 0.19
  - часть: часть_perovskite_tandem_encapsulant
    материал: eva
    доля_массы: 0.095
технологии_частей:
  - часть: часть_perovskite_tandem_front_glass
    технология: dc_magnetron_sputtering
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: low_iron_glass
        роль: подложка
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
          h: 53
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
дата_обновления: 2026-11-08
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
| КПД модуля | 33 | % | canon (дополнительные; лабораторные рекорды тандемных ячеек LONGi/Oxford PV 28.6–34%) |
| выработка энергии | 300 (100–500) | W | canon; атрибуция — тандемный стек ячеек (F15d) |
| выработка тепла | 100 (50–200) | W | canon (диссипация поглощённой части спектра) |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

Изделие верхнего уровня (уровень 1). Дочерние части:

- `часть_perovskite_tandem_cells` — тандемный стек ячеек (перовскит + Si HJT), **генератор энергии 300 Вт**;
- `часть_perovskite_tandem_front_glass` — фронтальное низкожелезистое стекло;
- `часть_perovskite_tandem_backsheet` — тыльная подложка (Tedlar/PET);
- `часть_perovskite_tandem_frame` — алюминиевая рама (Al 6063-T5 экструдированный профиль);
- `часть_perovskite_tandem_junction_box` — соединительная коробка;
- `часть_perovskite_tandem_encapsulant` — инкапсулянт (EVA).

Энергобаланс (F15d): Σ(выработка_энергии детей) = 300 Вт (только стек ячеек) ≥ выработка_энергии родителя 300 Вт ✓; остальные части — пассивные (0 Вт).

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Перовскитно-кремниевый тандемный фотоэлектрический модуль (референс Oxford PV, IEC 61215/61730): монолитный 2-контактный стек — верхний перовскитный подэлемент (широкая запрещённая зона ~1.68 эВ) поглощает синюю/зелёную часть солнечного спектра, нижний кремниевый HJT-подэлемент (~1.12 эВ) — красную/ИК; последовательно включённые переходы суммируют напряжения и поднимают КПД выше предела одиночного кремния (рекорды: 28.6% ячейка NREL-certified 2023; 25% / 421 Вт полномасштабный модуль 1.68 м² Fraunhofer ISE 2024; 26.9% 60-ячеечный модуль 2024). Остальные части пакета (стекло/инкапсулянт/подложка/рама/коробка) обеспечивают оптический ввод, изоляцию и механическую защиту; поглощённое вне генерации тепло диссипируется (~100 Вт canon).

## Источники

- Oxford PV / Fraunhofer ISE, «Full-sized tandem PV module» (2024-01-31): 25% КПД, 421 Вт на 1.68 м² — https://www.oxfordpv.com/press-releases/oxford-pv-solar-sustainability-initiative (обращение 2026-11-08)
- PV-Tech, «Oxford PV unveils record 26.9% perovskite tandem module» (2024-06-19): https://www.pv-tech.org/oxford-pv-unveils-record-26-9-perovskite-tandem-module (обращение 2026-11-08)
- CSV: `начальные данные_final.csv` (пользовательский ввод) — canon: КПД 33%, 300 Вт, Oxford PV perovskite-on-silicon tandem

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
