---
id: izdelie_superkondensatory
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: суперконденсатор
стандарты: 
  - IEC 62391
исследовательская_группа: maxwell_technologies
родитель: null
дочерние_части:
  - часть_superkondensatory_electrode_pos
  - часть_superkondensatory_separator
  - часть_superkondensatory_electrolyte
  - часть_superkondensatory_current_collector
  - часть_superkondensatory_terminal
  - часть_superkondensatory_case
материалы_частей:
  - часть: часть_superkondensatory_electrode_pos
  - часть: часть_superkondensatory_separator
    материал: cellulose
    доля_массы: 0.0475
  - часть: часть_superkondensatory_electrolyte
    материал: tebabf4_acn
    доля_массы: 0.1425
  - часть: часть_superkondensatory_current_collector
    материал: aluminum
    доля_массы: 0.1425
  - часть: часть_superkondensatory_case
    материал: aluminum
    доля_массы: 0.1425
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
          min: 0.1
          max: 5
          nominal: 0.5
  габариты_mm:
          l: 150
          w: 50
          h: 50
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.05
          max: 12.8
          nominal: 4.9
наследуемые: {}
дополнительные: 
  ёмкость_F: 3000
  V_max_V: 2.7
  источник: Maxwell BCAP3000
  тепловыделение_обоснование: омический нагрев P=I²·ESR по datasheet Maxwell BCAP3000 P270 (ESR_DC=0.29 мОм, IMAX(ΔT=15°C)=130 A_RMS → 4.9 Вт номинал; IMAX(ΔT=40°C)=210 A_RMS → 12.8 Вт max; min — 10% тока 13 A → 0.05 Вт); распределение по детям пропорционально вкладу в ESR — электролит 2.0 (ионная проводимость — доминирующий вклад), электрод 1.5 (поровое сопротивление активированного угля), вывод 0.7 (контактное сопротивление), токосъёмник 0.6 (фольга+приварка лепестков), сепаратор 0.1 (тонкий спейсер), корпус 0 (пассивная оболочка); Σ детей = 4.9 = номинал родителя
дата_создания: 2026-11-03
дата_обновления: 2026-11-08
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Суперконденсаторы

## Описание

Суперконденсаторы

Полное наименование (как в CSV): `Суперконденсаторы`

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
- Maxwell Technologies datasheet «2.7V 3000F Ultracapacitor Cell BCAP3000 P270» — ESR_DC=0.29 мОм, формула IMAX (максимальный непрерывный ток): https://maxwell.com/wp-content/uploads/2024/07/3003279-EN.3_DS_2.7V-3000F-Cell-BCAP3000-P270_20240704.pdf (проверено 2026-11-08)
- Maxwell K2 Series 650–3000F datasheet — Maximum Continuous Current: 130 A_RMS (ΔT=15°C), 210 A_RMS (ΔT=40°C): https://media.pneda.com/datasheetfiles/130135.pdf (проверено 2026-11-08)

---


## Декомпозиция

```mermaid
graph TD
    superkondensatory["izdelie_superkondensatory"]
    superkondensatory_electro["часть_superkondensatory_electrode_pos"]
    superkondensatory --> superkondensatory_electro
    superkondensatory --> superkondensatory_electro
    superkondensatory_separat["часть_superkondensatory_separator"]
    superkondensatory --> superkondensatory_separat
    superkondensatory_electro["часть_superkondensatory_electrolyte"]
    superkondensatory --> superkondensatory_electro
    superkondensatory_current["часть_superkondensatory_current_collector"]
    superkondensatory --> superkondensatory_current
    superkondensatory_termina["часть_superkondensatory_terminal"]
    superkondensatory --> superkondensatory_termina
    superkondensatory_case["часть_superkondensatory_case"]
    superkondensatory --> superkondensatory_case
```
