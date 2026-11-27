---
id: izdelie_kondensatory_keramicheskie
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: керамический_конденсатор
стандарты: 
  - EIA RS-198
  - AEC-Q200
исследовательская_группа: Murata_TDK
родитель: null
дочерние_части:
  - часть_kondensatory_keramicheskie_ceramic_layers
  - часть_kondensatory_keramicheskie_inner_electrodes
  - часть_kondensatory_keramicheskie_outer_electrodes
  - часть_kondensatory_keramicheskie_termination
  - часть_kondensatory_keramicheskie_plating
материалы_частей:
  - часть: часть_kondensatory_keramicheskie_ceramic_layers
    материал: batio3
    форма: X7R_MLCC_класс_II_EIA
    доля_массы: 0.475
  - часть: часть_kondensatory_keramicheskie_inner_electrodes
    материал: nickel
    форма: внутренние_электроды_MLCC_BME
    доля_массы: 0.19
  - часть: часть_kondensatory_keramicheskie_outer_electrodes
    материал: copper
    форма: внешние_электроды_и_терминация_MLCC
    доля_массы: 0.08
  - часть: часть_kondensatory_keramicheskie_termination
    материал: copper
    форма: внешние_электроды_и_терминация_MLCC
    доля_массы: 0.09
  - часть: часть_kondensatory_keramicheskie_plating
    материал: tin
    форма: matte_sn_покрытие_MLCC
    доля_массы: 0.09

технологии_частей:
  - часть: часть_kondensatory_keramicheskie_ceramic_layers
    технология: vakuumnoe_spekanie
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: batio3
        роль: обрабатываемый
  - часть: часть_kondensatory_keramicheskie_inner_electrodes
    технология: pogruzhenie_v_mo-shliker
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: nickel
        роль: обрабатываемый
  - часть: часть_kondensatory_keramicheskie_outer_electrodes
    технология: pogruzhenie_v_mo-shliker
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: copper
        роль: обрабатываемый
  - часть: часть_kondensatory_keramicheskie_termination
    технология: galvanika
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: copper
        роль: обрабатываемый
  - часть: часть_kondensatory_keramicheskie_plating
    технология: galvanika
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: tin
        роль: обрабатываемый

наследуемые_материалы:
  - материал: batio3
    форма: X7R_MLCC_класс_II_EIA
    суммарная_доля_массы: 0.475
    источники_частей:
      - часть_kondensatory_keramicheskie_ceramic_layers
  - материал: nickel
    форма: внутренние_электроды_MLCC_BME
    суммарная_доля_массы: 0.19
    источники_частей:
      - часть_kondensatory_keramicheskie_inner_electrodes
  - материал: copper
    форма: внешние_электроды_и_терминация_MLCC
    суммарная_доля_массы: 0.17
    источники_частей:
      - часть_kondensatory_keramicheskie_outer_electrodes
      - часть_kondensatory_keramicheskie_termination
  - материал: tin
    форма: matte_sn_покрытие_MLCC
    суммарная_доля_массы: 0.09
    источники_частей:
      - часть_kondensatory_keramicheskie_plating

масштабируемость:
  режим: квантуемая
  параметры: [масса_kg, ёмкость_мкФ, выработка_тепла_W]
  пределы:
    min: {масса_kg: 0.0001, ёмкость_мкФ: 0.1, выработка_тепла_W: 0.001}
    max: {масса_kg: 0.005, ёмкость_мкФ: 47, выработка_тепла_W: 0.05}
  закон_масштабирования:
    масса: '∝ числа слоёв и площади обкладок (EIA-кейсы 0201–2220); запасённая энергия E = ½CV² = 1.25 мДж при 1 мкФ / 50 В'
    тепло: 'P = ESR·I²_RMS (X7R, 50 В): 0.01 Вт номинал при типовых пульсациях для кейса 0805'
    энергия: 'ёмкость квантуется кейсом EIA (0201/0402/0603/0805/1206) и рядом номиналов X7R 100 пФ – 47 мкФ'
  ограничивающие_части:
    - часть: часть_kondensatory_keramicheskie_ceramic_layers
      предел: 'BaTiO3 X7R слои 47.5% массы: толщина диэлектрика ~1–5 мкм/слой задаёт рабочее напряжение (DC-bias деградация ёмкости)'
    - часть: часть_kondensatory_keramicheskie_inner_electrodes
      предел: 'Ni BME электроды 19% массы: ко-спекание 1100–1300 °C; вклад в ESR при росте числа слоёв'
    - часть: часть_kondensatory_keramicheskie_plating
      предел: 'matte Sn 9% массы: теплостойкость пайки (reflow ≤260 °C), risk dewetting при повторных циклах'

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
          min: 0.0001
          max: 0.005
          nominal: 0.001
  габариты_mm:
          l: 2.3
          w: 1.45
          h: 1.45
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.001
          max: 0.05
          nominal: 0.01
наследуемые: {}
дополнительные: 
  ёмкость_мкФ: 1
  V_max_V: 50
  источник: Murata GCJ21BR71H105MA01K datasheet
  габариты_метод: предельные размеры корпуса по datasheet (2.0±0.3 × 1.25±0.2 × 1.25±0.2 → максимум 2.3×1.45×1.45)
  обоснование_габаритов: огибающая при максимальном материале по Murata GCJ21BR71H105MA01K (0805, 2012M — длина 2.0±0.3, ширина 1.25±0.2, толщина 1.25±0.2 мм, внешний терминал 0.2–0.7 мм); проверка F15g — Σ V детей 2.944 мм³ ≤ 4.833/1.15 = 4.202 (запас 30 %), оси 2.3≥1.5 / 1.45≥1.25 / 1.45≥1.25
дата_создания: 2026-11-03
дата_обновления: 2026-11-09
источник: web_search
источник_разбора: веб-верификация
источник_url: https://www.tme.eu/rs/en/details/gcg21br71h105ma01k/mlcc-smd-capacitors/murata
источник_дата: 2026-11-08
---
# Изделие: Конденсаторы: керамические

## Описание

Многослойный керамический конденсатор (MLCC) 0805-класса: 1 мкФ ±20 %, 50 В, X7R (−55…+125 °C, ΔC/C ±15 %, EIA RS-198 класс II) — референс Murata GCJ21BR71H105MA01K (2.0×1.25×1.25 мм, допуски ±0.3/±0.2/±0.2). BME-конструкция: никелевые внутренние электроды, ко-спечённые с X7R-диэлектриком на легированном BaTiO3 (core-shell, εr ~3000), Cu-терминация с Ni-барьером и matte-Sn финишем (AEC-Q200).

Полное наименование (как в CSV): `Конденсаторы: керамические (X7R)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | вычислительная | — | classify_subsystem |
| категория | электроника | — | синхронизировано с YAML |
| типоразмер | 0805 (2012 metric) | — | Murata GCJ21BR71H105MA01K |
| габариты корпуса | 2.0±0.3 × 1.25±0.2 × 1.25±0.2 (огибающая 2.3×1.45×1.45) | mm | Murata datasheet |
| ёмкость | 1 ±20 % | мкФ | Murata GCJ21BR71H105MA01K |
| номинальное напряжение | 50 | В | Murata GCJ21BR71H105MA01K |
| температурный класс | X7R (−55…+125 °C, ΔC/C ±15 %) | — | EIA RS-198, класс II |
| выработка тепла | 0.01 (0.001–0.05) | W | канон |
| выработка энергии | 0 | W | канон |

## Состав

Изделие верхнего уровня — MLCC 0805 (BME-конструкция), 5 дочерних частей:

- `часть_kondensatory_keramicheskie_ceramic_layers` — X7R-диэлектрик на BaTiO3 (керамический чип 1.5×1.25×1.25 мм между зонами терминации)
- `часть_kondensatory_keramicheskie_inner_electrodes` — Ni-стек внутренних электродов (~150 слоёв, footprint 1.3×1.0×0.15 мм)
- `часть_kondensatory_keramicheskie_outer_electrodes` — Cu-торцевой электрод (0.25×1.25×1.25 мм на торце)
- `часть_kondensatory_keramicheskie_termination` — Cu-плёнка терминации (~20 мкм, глубина 0.4 мм)
- `часть_kondensatory_keramicheskie_plating` — Ni-барьер + matte Sn финиш (~8 мкм)

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Ёмкость набирается сотнями чередующихся слоёв: C = ε0·εr·N·A/d — X7R-диэлектрик (легированный BaTiO3, εr ~3000) между Ni-внутренними электродами; каждый слой выводится на противоположные торцы к Cu-терминации. Сегнетоэлектрическая поляризация тетрагонального BaTiO3 обеспечивает высокую εr; core-shell легирование (Dy/Ho/Y, Mn, Mg) стабилизирует класс X7R и делает BME-диэлектрик совместимым с Ni в восстановительном ко-спекании при 1150–1350 °C (NASA NTRS 20150004115). Cu-терминация с Ni-барьером и matte-Sn финишем образует паяемое покрытие, стойкое к перепайке (AEC-Q200).

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- Murata GCJ21BR71H105MA01K — MLCC 0805, 1 мкФ ±20 %, 50 В, X7R, размеры 2.0±0.3×1.25±0.2×1.25±0.2 мм, внешний терминал 0.2–0.7 мм: https://www.tme.eu/rs/en/details/gcg21br71h105ma01k/mlcc-smd-capacitors/murata (проверено 2026-11-08)
- Murata GCM21BR71H105MA03K (0805, 2.00×1.25 мм, толщина макс 1.45 мм — подтверждение предельной огибающей): https://www.digikey.com.br/en/products/detail/murata-electronics/GCM21BR71H105MA03K/10695904 (проверено 2026-11-08)

---


## Декомпозиция

```mermaid
graph TD
    kondensatory_keramic["izdelie_kondensatory_keramicheskie"]
    kondensatory_keramicheski["часть_kondensatory_keramicheskie_ceramic_layers"]
    kondensatory_keramic --> kondensatory_keramicheski
    kondensatory_keramicheski["часть_kondensatory_keramicheskie_inner_electrodes"]
    kondensatory_keramic --> kondensatory_keramicheski
    kondensatory_keramicheski["часть_kondensatory_keramicheskie_outer_electrodes"]
    kondensatory_keramic --> kondensatory_keramicheski
    kondensatory_keramicheski["часть_kondensatory_keramicheskie_termination"]
    kondensatory_keramic --> kondensatory_keramicheski
    kondensatory_keramicheski["часть_kondensatory_keramicheskie_plating"]
    kondensatory_keramic --> kondensatory_keramicheski
```
