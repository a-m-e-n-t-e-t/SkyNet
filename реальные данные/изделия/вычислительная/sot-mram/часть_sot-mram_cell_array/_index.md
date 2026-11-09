---
id: часть_sot-mram_cell_array
тип: часть
категория: машиностроение
уровень_иерархии: промежуточный
уровень_номер: 2
подсистема: вычислительная
подтип: массив_ячеек
стандарты:
  - ISO 9001
исследовательская_группа: null
родитель: izdelie_sot-mram
дочерние_части: []
материалы_частей:
  - часть: часть_sot-mram_cell_array
    материал: coefeb_mgo
    доля_массы: 1.0

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
  масса_kg: 0.002
  доля_массы_родителя: 0.4
  габариты_mm:
    l: 6
    w: 6
    h: 0.2
  выработка_энергии_W: 0
  выработка_тепла_W: 0.012
наследуемые: {}
дополнительные: {}
дата_создания: 2026-11-03
дата_обновления: 2026-11-07
источник: web_search
источник_разбора: канон
источник_url: https://www.nature.com/articles/s44306-023-00003-2
источник_дата: 2026-11-07
---
# Часть: часть_sot-mram_cell_array

## Описание

Массив MTJ-ячеек CoFeB/MgO: субнанометровый барьер MgO (001) между свободным и опорным слоями Co20Fe60B20, TMR 200–600 %; STT-MRAM массив на кристалле 6×6 мм.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | вычислительная | — | canon |
| подтип | массив_ячеек | — | canon |
| масса | 0.002 | kg | canon |
| доля массы родителя | 0.4 | — | canon |
| габариты (Д×Ш×В) | 6×6×0.2 | mm | Igarashi et al., npj Spintronics 2024 — single-nanometer CoFeB/MgO MTJ |
| выработка энергии | 0 | W | canon |
| выработка тепла | 0.012 | W | расчёт: <100 fJ/бит (imec 2023) / 350 fJ@280 ps (VLSI 2018) при пиковой полосе записи ~120 Гбит/с + омический нагрев SOT-линий |
| материал | coefeb_mgo | — | coefeb_mgo.md |

## Принцип работы

Определяется типом и назначением родительского изделия.

## Состав

Промежуточная часть (уровень 2). Дочерних частей нет.

## Используемые материалы

- `coefeb_mgo` → [`coefeb_mgo.md`](../../../../материалы/coefeb_mgo.md)

## Источники

- Igarashi et al., npj Spintronics 2024 — single-nanometer CoFeB/MgO MTJ: https://www.nature.com/articles/s44306-023-00003-2 (проверено 2026-11-05)
- imec-int.com/en/press — Extremely scaled SOT-MRAM: record-low switching energy (Dec 2023): https://www.imec-int.com/en/press/imecs-extremely-scaled-sot-mram-devices-show-record-low-switching-energy-and-virtually (проверено 2026-11-07)
- Garello et al., VLSI 2018 — SOT-MRAM 300 mm integration (350 fJ @ 280 ps): https://ethz.ch/content/dam/ethz/special-interest/matl/intermag-dam/Publications/Papers/2018/VLSI_2018.pdf (проверено 2026-11-07)
- Материалы: реальные данные/материалы/
