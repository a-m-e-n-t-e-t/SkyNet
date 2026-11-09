---
id: часть_sot-mram_io_interface
тип: часть
категория: машиностроение
уровень_иерархии: промежуточный
уровень_номер: 2
подсистема: вычислительная
подтип: I/O_интерфейс
стандарты:
  - ISO 9001
исследовательская_группа: null
родитель: izdelie_sot-mram
дочерние_части: []
материалы_частей:
  - часть: часть_sot-mram_io_interface
    материал: si
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
  масса_kg: 0.001
  доля_массы_родителя: 0.2
  габариты_mm:
    l: 1.2
    w: 1
    h: 0.35
  выработка_энергии_W: 0
  выработка_тепла_W: 0.008
наследуемые: {}
дополнительные: {}
дата_создания: 2026-11-03
дата_обновления: 2026-11-07
источник: web_search
источник_разбора: канон
источник_url: https://ieeexplore.ieee.org/iel8/6570653/10879154/11202876.pdf
источник_дата: 2026-11-07
---
# Часть: часть_sot-mram_io_interface

## Описание

Блок ввода-вывода SOT-MRAM чипа: CMOS-модуль ~1.2×1.0 мм, содержащий приёмопередатчики шин, регистры команд и цепи согласования уровней между ядром записи (VDDH = 0.8–1.3 В для SOT-линии) и логикой управления. Сквозное проектирование устройства и системы для SOT-MRAM (IEEE 2025) выделяет в периферии write drivers, sense circuits и level shifters как обязательные блоки сопряжения массива с внешним интерфейсом.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | вычислительная | — | canon |
| подтип | I/O_интерфейс | — | canon |
| масса | 0.001 | kg | SOT-MRAM device-to-system co-design: write drivers, sensing circuits, level shifters (IEEE 2025) |
| доля массы родителя | 0.2 | — | canon |
| габариты (Д×Ш×В) | 1.2×1×0.35 | mm | SOT-MRAM device-to-system co-design: write drivers, sensing circuits, level shifters (IEEE 2025) |
| выработка энергии | 0 | W | canon |
| выработка тепла | 0.008 | W | расчёт: DDR-выходные каскады, ~10 мА суммарно при 0.8 В swinging |
| материал | si | — | si.md |

## Принцип работы

I/O-блок принимает адреса/команды по внешней шине, мультиплексирует bank/column выборку и передаёт данные от sense-усилителей; развязывающие level shifters переводят сигналы низковольтной логики к повышенному напряжению записи SOT-линии.

## Состав

Промежуточная часть (уровень 2). Дочерних частей нет.

## Используемые материалы

- `si` → [`si.md`](../../../../материалы/si.md)

## Источники

- SOT-MRAM device-to-system co-design: write drivers, sensing circuits, level shifters (IEEE 2025): https://ieeexplore.ieee.org/iel8/6570653/10879154/11202876.pdf (проверено 2026-11-05)
- imec-int.com/en/press — Extremely scaled SOT-MRAM: record-low switching energy (Dec 2023): https://www.imec-int.com/en/press/imecs-extremely-scaled-sot-mram-devices-show-record-low-switching-energy-and-virtually (проверено 2026-11-07)
- Garello et al., VLSI 2018 — SOT-MRAM 300 mm integration (350 fJ @ 280 ps): https://ethz.ch/content/dam/ethz/special-interest/matl/intermag-dam/Publications/Papers/2018/VLSI_2018.pdf (проверено 2026-11-07)
- Материалы: реальные данные/материалы/
