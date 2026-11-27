---
id: izdelie_termomoduli_pelte
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: система_охлаждения
подтип: модуль_Пельтье
стандарты: 
  - JEDEC JESD47
исследовательская_группа: marlow_industries
родитель: null
дочерние_части:
  - часть_termomoduli_pelte_peltier_couples
  - часть_termomoduli_pelte_ceramic_top
  - часть_termomoduli_pelte_electrodes
  - часть_termomoduli_pelte_solder
  - часть_termomoduli_pelte_wires
материалы_частей:
  - часть: часть_termomoduli_pelte_peltier_couples
    материал: bi2te3
    форма: модуль_пельтье
    доля_массы: 0.2
  - часть: часть_termomoduli_pelte_ceramic_top
    материал: oksid_alyuminiya
    форма: electronic_substrate
    доля_массы: 0.116
  - часть: часть_termomoduli_pelte_electrodes
    материал: copper
    форма: шины_и_заземление
    доля_массы: 0.04
  - часть: часть_termomoduli_pelte_solder
    материал: splav_sn-pb
    форма: smt_tht_пайка_pcb
    доля_массы: 0.04
  - часть: часть_termomoduli_pelte_wires
    материал: copper
    форма: шины_и_заземление
    доля_массы: 0.02
# F29 B-BOM: агрегация (материал, форма) по частям; доли = масса_части/0.05 кг
# (0.01→0.2; 0.0058→0.116; 0.002→0.04; 0.002→0.04; 0.001→0.02); copper = electrodes+wires
наследуемые_материалы:
  - материал: bi2te3
    форма: модуль_пельтье
    суммарная_доля_массы: 0.2
    источники_частей:
      - часть_termomoduli_pelte_peltier_couples
  - материал: oksid_alyuminiya
    форма: electronic_substrate
    суммарная_доля_массы: 0.116
    источники_частей:
      - часть_termomoduli_pelte_ceramic_top
  - материал: copper
    форма: шины_и_заземление
    суммарная_доля_массы: 0.06
    источники_частей:
      - часть_termomoduli_pelte_electrodes
      - часть_termomoduli_pelte_wires
  - материал: splav_sn-pb
    форма: smt_tht_пайка_pcb
    суммарная_доля_массы: 0.04
    источники_частей:
      - часть_termomoduli_pelte_solder
# F27e: технология обработки каждой части (файлы технологии/ существуют — F27c)
технологии_частей:
  - часть: часть_termomoduli_pelte_peltier_couples
    технология: vakuumnoe_spekanie
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: bi2te3
        роль: обрабатываемый
  - часть: часть_termomoduli_pelte_ceramic_top
    технология: tape_casting
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: oksid_alyuminiya
        роль: обрабатываемый
  - часть: часть_termomoduli_pelte_electrodes
    технология: shtampovka_listovaya
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: copper
        роль: обрабатываемый
  - часть: часть_termomoduli_pelte_solder
    технология: payka_silovyh_kontaktov
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: splav_sn-pb
        роль: обрабатываемый
  - часть: часть_termomoduli_pelte_wires
    технология: volochenie
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: copper
        роль: обрабатываемый
# F-scal (P087 §12.6): масштабирование TEC по площади пластины / числу пар
масштабируемость:
  режим: масштабируемая
  параметры: [масса_kg, выработка_тепла_W]
  пределы:
    min: {масса_kg: 0.005, выработка_тепла_W: 1}
    max: {масса_kg: 0.5, выработка_тепла_W: 100}
  закон_масштабирования:
    масса: '≈ линейный от площади керамических пластин (40×40 мм типовой размер ряда 10×10…62×62 мм)'
    холодопроизводительность: 'Qc ∝ числу термопар (127 пар при 40×40 мм); Qmax 50 Вт при ΔT 0 (Marlow TEC)'
  ограничивающие_части:
    - часть: часть_termomoduli_pelte_peltier_couples
      причина: 'ZT≈1 Bi2Te3 задаёт ΔT_max 70 °C и Qc модуля'
    - часть: часть_termomoduli_pelte_ceramic_top
      причина: 'теплопроводность и термостойкость Al2O3-подложки ограничивают плотность потока'
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
          min: 0.005
          max: 0.5
          nominal: 0.05
  габариты_mm:
          l: 55
          w: 42
          h: 4
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 1
          max: 100
          nominal: 10
наследуемые: {}
дополнительные: 
  Qmax_W: 50
  dT_max_C: 70
  источник: Marlow Industries TEC
дата_создания: 2026-11-03
дата_обновления: 2026-11-05
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: термомодули Пельтье

## Описание

термомодули Пельтье

Полное наименование (как в CSV): `термомодули Пельтье`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
| категория | прочее | — | — |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

Изделие верхнего уровня — однокаскадный термомодуль Пельтье 40×40 мм (127 пар Bi2Te3, керамика Al2O3 96 %, медные электроды, пайка Sn-Pb, медные токоподводы). Пять составных частей:

- `часть_termomoduli_pelte_peltier_couples` — p/n-термоэлементы (127 пар Bi2Te3);
- `часть_termomoduli_pelte_ceramic_top` — керамические пластины Al2O3 (верх/низ, ×2);
- `часть_termomoduli_pelte_electrodes` — медные коммутационные электроды;
- `часть_termomoduli_pelte_solder` — паяные соединения Sn-Pb;
- `часть_termomoduli_pelte_wires` — медные токоподводящие провода.

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
    termomoduli_pelte["izdelie_termomoduli_pelte"]
    termomoduli_pelte_peltier["часть_termomoduli_pelte_peltier_couples"]
    termomoduli_pelte --> termomoduli_pelte_peltier
    termomoduli_pelte_ceramic["часть_termomoduli_pelte_ceramic_top"]
    termomoduli_pelte --> termomoduli_pelte_ceramic
    termomoduli_pelte --> termomoduli_pelte_ceramic
    termomoduli_pelte_electro["часть_termomoduli_pelte_electrodes"]
    termomoduli_pelte --> termomoduli_pelte_electro
    termomoduli_pelte_solder["часть_termomoduli_pelte_solder"]
    termomoduli_pelte --> termomoduli_pelte_solder
    termomoduli_pelte_wires["часть_termomoduli_pelte_wires"]
    termomoduli_pelte --> termomoduli_pelte_wires
```
