---
id: izdelie_memristornye_matritsy
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: memristor_массив
стандарты: []
исследовательская_группа: hp_labs
родитель: null
дочерние_части:
- часть_memristornye_matritsy_crossbar
- часть_memristornye_matritsy_word_drivers
- часть_memristornye_matritsy_bit_sense
- часть_memristornye_matritsy_adc
- часть_memristornye_matritsy_controller
материалы_частей:
- часть: часть_memristornye_matritsy_crossbar
  материал: hfo2
  форма: high_k_затворная_диэлектрика
  доля_массы: 0.28
- часть: часть_memristornye_matritsy_word_drivers
  материал: si
  форма: подложки_ис_и_мэмс
  доля_массы: 0.18
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
    max: 0.05
    nominal: 0.01
  габариты_mm:
    l: 12
    w: 12
    h: 1
  выработка_энергии_W:
    min: 0
    max: 0
    nominal: 0
  выработка_тепла_W:
    min: 0.1
    max: 2.0
    nominal: 1.2
наследуемые: {}
дополнительные:
  технология: memristor crossbar
  источник: HP Labs research
  источник_url: https://www.nature.com/articles/s41467-024-45670-9
  источник_url_2: https://www.frontiersin.org/journals/nanotechnology/articles/10.3389/fnano.2021.734121/full
дата_создания: 2026-11-03
дата_обновления: '2026-11-11'
источник: web_search
источник_url: https://knowm.com/products/w-sdc-memristor-crossbars
источник_разбора: веб-верификация
источник_дата: '2026-11-11'
технологии_частей:
- часть: часть_memristornye_matritsy_crossbar
  технология: magnetron_sputtering_tio2
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: tio2_memristor
    роль: обрабатываемый
- часть: часть_memristornye_matritsy_word_drivers
  технология: cmos_7nm_intel4
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: si
    роль: обрабатываемый
наследуемые_материалы:
- материал: hfo2
  суммарная_доля_массы: 0.28
  источники_частей:
  - часть_memristornye_matritsy_crossbar
  форма: high_k_затворная_диэлектрика
- материал: si
  суммарная_доля_массы: 0.18
  источники_частей:
  - часть_memristornye_matritsy_word_drivers
  форма: подложки_ис_и_мэмс
масштабируемость:
  режим: масштабируемая
  параметры:
  - имя: количество_единиц
    диапазон:
    - 1
    - 1000
    единица: шт
  - имя: масса_единицы
    диапазон:
    - 0.005
    - 0.05
    единица: kg
  - имя: размер_матрицы
    диапазон:
    - 8
    - 256
    единица: cells
  пределы:
    max_единиц_в_системе: 1000
    min_массы: 0.005
    max_массы: 0.05
    min_матрицы: 8
    max_матрицы: 256
  закон_масштабирования: 'нелинейный — масса_системы = N × масса_единицы × 1.10 (10%
    overhead на PCB+connectors); типовая установка: Knowm W-SDC memristor crossbar
    (8x8 to 32x32, 5×5 μm lateral, 2 nm feature); Intel Optane M.2 (80×22×2 mm, 10g,
    16-32 GB)'
  ограничивающие_части:
  - часть_memristornye_matritsy_crossbar (TiO2 + W-SDC memristors — критическая точность
    производства, lab-grade)
  - часть_memristornye_matritsy_word_drivers (silicon CMOS drivers — критическая зависимость
    от CMOS foundry)
---


# Изделие: мемристорные матрицы

## Описание

мемристорные матрицы (RRAM)

Полное наименование (как в CSV): `мемристорные матрицы (RRAM)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | вычислительная | — | classify_subsystem |
| категория | прочее | — | — |
| рассеиваемая теплота (номинал) | 1.2 | W | Σ тепловыделения периферии crossbar (crossbar 0.5 + ADC 0.2 + bit_sense 0.15 + word_drivers 0.1 + controller 0.05 = 1.0 Вт) + запас 20 % на теплоотвод |
| рассеиваемая теплота (диапазон) | 0.1–2.0 | W | от спящего режима до пикового инференса; memristor crossbar PIM — джоулево тепло чтения/программирования (Aguirre et al. 2024, Nat. Commun. 15) |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

Тепловой баланс: все 5 дочерних частей оснащены реальными значениями тепловыделения (ранее — заглушки по 1 Вт, что давало Σ=5 Вт для чипа 12×12 мм — ~35 Вт/см², нереалистично). Оценка согласована с литературой по memristor-ускорителям: доминирующий вклад — джоулево тепло crossbar-массива при чтении/программировании (токи ~мкА–мА на ячейку, Aguirre et al. 2024), периферия (ADC/sense/drivers) — сотые-десятые доли ватта.

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
    memristornye_matrits["izdelie_memristornye_matritsy"]
    memristornye_matritsy_cro["часть_memristornye_matritsy_crossbar"]
    memristornye_matrits --> memristornye_matritsy_cro
    memristornye_matritsy_wor["часть_memristornye_matritsy_word_drivers"]
    memristornye_matrits --> memristornye_matritsy_wor
    memristornye_matritsy_bit["часть_memristornye_matritsy_bit_sense"]
    memristornye_matrits --> memristornye_matritsy_bit
    memristornye_matritsy_adc["часть_memristornye_matritsy_adc"]
    memristornye_matrits --> memristornye_matritsy_adc
    memristornye_matritsy_con["часть_memristornye_matritsy_controller"]
    memristornye_matrits --> memristornye_matritsy_con
```
