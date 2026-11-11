---
id: izdelie_superkondensatory
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: система_питания
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
    материал: activated_carbon
    форма: электрод_EDLC
    доля_массы: 0.2
  - часть: часть_superkondensatory_separator
    материал: cellulose
    форма: сепаратор_суперконденсаторов
    доля_массы: 0.0475
  - часть: часть_superkondensatory_electrolyte
    материал: acetonitrile_teabf4
    форма: электролит_суперконденсаторов
    доля_массы: 0.1425
  - часть: часть_superkondensatory_current_collector
    материал: aluminum
    форма: гибкая_фольга_и_упаковка
    доля_массы: 0.1425
  - часть: часть_superkondensatory_case
    материал: al_6061-t6
    форма: корпуса_электроники
    доля_массы: 0.1425
  - часть: часть_superkondensatory_terminal
    материал: al_6061-t6
    форма: крепёж_и_монтажные_плиты
    доля_массы: 0.05
наследуемые_материалы:
  - материал: activated_carbon
    форма: электрод_EDLC
    суммарная_доля_массы: 0.2
    источники_частей:
      - часть_superkondensatory_electrode_pos
  - материал: cellulose
    форма: сепаратор_суперконденсаторов
    суммарная_доля_массы: 0.0475
    источники_частей:
      - часть_superkondensatory_separator
  - материал: acetonitrile_teabf4
    форма: электролит_суперконденсаторов
    суммарная_доля_массы: 0.1425
    источники_частей:
      - часть_superkondensatory_electrolyte
  - материал: aluminum
    форма: гибкая_фольга_и_упаковка
    суммарная_доля_массы: 0.1425
    источники_частей:
      - часть_superkondensatory_current_collector
  - материал: al_6061-t6
    форма: крепёж_и_монтажные_плиты
    суммарная_доля_массы: 0.05
    источники_частей:
      - часть_superkondensatory_terminal
  - материал: al_6061-t6
    форма: корпуса_электроники
    суммарная_доля_массы: 0.1425
    источники_частей:
      - часть_superkondensatory_case

масштабируемость:
  режим: квантуемая
  параметры: [масса_kg, ёмкость_F, выработка_тепла_W]
  пределы:
    min: {масса_kg: 0.1, ёмкость_F: 650, выработка_тепла_W: 0.05}
    max: {масса_kg: 5, ёмкость_F: 3000, выработка_тепла_W: 12.8}
  закон_масштабирования:
    масса: '∝ ёмкости (Ф); семейство Maxwell K2 650–3000 Ф (BCAP0650 ≈ 0.16 кг → BCAP3000 0.51 кг); энергия E = ½CV² ≈ 3 Вт·ч при 3000 Ф / 2.7 В'
    тепло: 'P = I²·ESR (ESR_DC 0.29 мОм): 13 A → 0.05 Вт, 130 A_RMS → 4.9 Вт (ΔT=15 °C), 210 A_RMS → 12.8 Вт (ΔT=40 °C)'
    энергия: 'ёмкость квантуется номиналами ячеек K2-серии; модуль масштабируется числом последовательных/параллельных ячеек'
  ограничивающие_части:
    - часть: часть_superkondensatory_electrolyte
      предел: 'ионная проводимость 1M TEABF4/ACN — доминирующий вклад ESR (2.0 Вт из 4.9); температурный диапазон −40…+65 °C'
    - часть: часть_superkondensatory_electrode_pos
      предел: 'поровое сопротивление активированного угля (1.5 Вт); площадь поверхности задаёт ёмкость'
    - часть: часть_superkondensatory_case
      предел: 'теплоотвод корпуса: ΔT=15/40 °C при 130/210 A_RMS; цилиндрический can Ø60.4×138 мм'
технологии_частей:
  - часть: часть_superkondensatory_electrode_pos
    технология: spiralnaya_navivka
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: cnt
        роль: обрабатываемый
  - часть: часть_superkondensatory_separator
    технология: spiralnaya_navivka
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: cellulose
        роль: обрабатываемый
      - материал: acetonitrile_teabf4
        роль: пропитка
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
          l: 138
          w: 60.4
          h: 60.4
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
  обоснование_габаритов: 'bbox цилиндра Ø60.4×138 мм — BCAP3000 P270 K04/K05: 2.390" Dia × 5.433" L (datasheet Maxwell 3003279-EN.3; дистрибьюторские листинги Mouser/eBay сходятся); V(bbox)=138×60.4×60.4=503 446 мм³ ≥ ΣV(детей)×1.15=72 847 мм³ (запас ×6.9); оси: l 138 ≥ max_child 138 (case/electrode/separator — объёмно-эквивалентные слои в footprint ячейки, материальная модель в файлах частей), w 60.4 ≥ 60.4, h 60.4 ≥ 12 (терминал M12×1.75)'
  ёмкость_F: 3000
  V_max_V: 2.7
  источник: Maxwell BCAP3000
  тепловыделение_обоснование: омический нагрев P=I²·ESR по datasheet Maxwell BCAP3000 P270 (ESR_DC=0.29 мОм, IMAX(ΔT=15°C)=130 A_RMS → 4.9 Вт номинал; IMAX(ΔT=40°C)=210 A_RMS → 12.8 Вт max; min — 10% тока 13 A → 0.05 Вт); распределение по детям пропорционально вкладу в ESR — электролит 2.0 (ионная проводимость — доминирующий вклад), электрод 1.5 (поровое сопротивление активированного угля), вывод 0.7 (контактное сопротивление), токосъёмник 0.6 (фольга+приварка лепестков), сепаратор 0.1 (тонкий спейсер), корпус 0 (пассивная оболочка); Σ детей = 4.9 = номинал родителя
дата_создания: 2026-11-03
дата_обновления: 2026-11-09
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Суперконденсаторы

## Описание

Суперконденсаторы — одиночная цилиндрическая ячейка EDLC Maxwell BCAP3000 P270 (K2 Series): 3000 Ф, 2.7 В, Ø60.4 × 138 мм, масса 0.51 кг, ESR_DC = 0.29 мОм.

Полное наименование (как в CSV): `Суперконденсаторы`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
| категория | прочее | — | — |
| масса (реал) | 0.51 | kg | datasheet Maxwell BCAP3000 (1.124 lbs) |
| габариты (Д×Ш×В) | 138×60.4×60.4 | mm | bbox цилиндра Ø60.4×138 мм (datasheet Maxwell BCAP3000 P270 K04/K05) |
| ёмкость | 3000 | F | datasheet Maxwell BCAP3000 P270 |

(Энергетические параметры — номинал 0.5 кг канон; реал 0.51 кг по datasheet)

## Состав

Изделие верхнего уровня (одиночная ячейка BCAP3000). Шесть дочерних частей:

- `часть_superkondensatory_electrode_pos` — позитивный электрод: активированный уголь на углеволоконной подложке, 2 шт (симметричный EDLC)
- `часть_superkondensatory_separator` — целлюлозный сепаратор, 2 ленты
- `часть_superkondensatory_electrolyte` — электролит 1M TEABF4 в ацетонитриле
- `часть_superkondensatory_current_collector` — травленая алюминиевая фольга токосъёмника
- `часть_superkondensatory_terminal` — резьбовые силовые выводы M12×1.75 (пара)
- `часть_superkondensatory_case` — тянутый алюминиевый корпус ячейки (Al can)

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

EDLC: спиральная намотка «электрод | сепаратор | электрод | сепаратор» (технология spiralnaya_navivka) — активированный уголь на углеволоконной подложке; заряд накапливается электростатически на границе уголь/электролит (двойной электрический слой, ионы TEA+/BF4⁻ в ацетонитриле) без фарадеевских реакций — отсюда >1 000 000 duty cycles и низкое ESR_DC 0.29 мОм. Токосъёмники — травленая алюминиевая фольга, соединённая с резьбовыми терминалами M12×1.75, выведенными через крышку тянутого алюминиевого корпуса (Al can).

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- Maxwell Technologies datasheet «2.7V 3000F Ultracapacitor Cell BCAP3000 P270» — ESR_DC=0.29 мОм, формула IMAX (максимальный непрерывный ток): https://maxwell.com/wp-content/uploads/2024/07/3003279-EN.3_DS_2.7V-3000F-Cell-BCAP3000-P270_20240704.pdf (проверено 2026-11-08)
- Maxwell K2 Series 650–3000F datasheet — Maximum Continuous Current: 130 A_RMS (ΔT=15°C), 210 A_RMS (ΔT=40°C): https://media.pneda.com/datasheetfiles/130135.pdf (проверено 2026-11-08)
- Maxwell BCAP3000 P270 K04/K05 — габариты ячейки Ø60.4 мм × 138 мм (2.390″ Dia × 5.433″ L), масса 0.51 кг (1.124 lbs): datasheet 3003279-EN.3 + дистрибьюторские листинги Mouser/DigiKey (проверено 2026-11-09)

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
