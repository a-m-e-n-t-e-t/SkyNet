---
id: izdelie_optovolokonnaya_shina
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: система_связи
подтип: прочее
стандарты:
- FCC Part 15
- ETSI EN 301 489
исследовательская_группа: harris_thales
родитель: null
дочерние_части:
- часть_optovolokonnaya_shina_core
- часть_optovolokonnaya_shina_housing
- часть_optovolokonnaya_shina_connectors
- часть_optovolokonnaya_shina_mounting
материалы_частей:
- часть: часть_optovolokonnaya_shina_core
  материал: al_6061-t6
  форма: силовые_элементы_конструкций
  доля_массы: 0.45
- часть: часть_optovolokonnaya_shina_housing
  материал: al_6061-t6
  форма: корпуса_электроники
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
    min: 0.1
    max: 5.0
    nominal: 0.5
  габариты_mm:
    l: 200
    w: 117
    h: 46
  выработка_энергии_W:
    min: 0
    max: 0
    nominal: 0
  выработка_тепла_W:
    min: 0.01
    max: 5
    nominal: 1.2
наследуемые: {}
дополнительные:
  цена_usd: null
  обоснование_теплового_баланса: номинал 1.2 W >= СУММ(дочерних) 1.10 W (core 1 W
    — активные трансиверы коммутационного блока; connectors 0.1 W; housing/mounting
    0 W) + собственные пассивные потери волоконных трактов ~0.1 W (вставочные потери,
    микропоглощение). Оптические трансиверы рассеивают <=1 W (LINK-PP 10GBASE-T SFP
    power/heat guide; SFP+ Thermal and EMI Considerations 2013), максимум 5 W — верхняя
    граница многотерминальной конфигурации
  источник_url_тепла: https://www.link-pp.com/resources/technical-specs/10gbase-t-sfp-power-heat-management-guide
  источник_url_2_тепла: https://core.ac.uk/download/pdf/42812227.pdf
дата_создания: 2026-11-03
дата_обновления: '2026-11-11'
источник: web_search
источник_разбора: веб-верификация
технологии_частей:
- часть: часть_optovolokonnaya_shina_core
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: al_6061-t6
    роль: обрабатываемый
- часть: часть_optovolokonnaya_shina_housing
  технология: anodirovanie
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: aluminum
    роль: обрабатываемый
наследуемые_материалы:
- материал: al_6061-t6
  суммарная_доля_массы: 0.45
  источники_частей:
  - часть_optovolokonnaya_shina_core
  форма: силовые_элементы_конструкций
- материал: al_6061-t6
  суммарная_доля_массы: 0.27
  источники_частей:
  - часть_optovolokonnaya_shina_housing
  форма: корпуса_электроники
масштабируемость:
  режим: масштабируемая
  параметры:
  - имя: количество_единиц
    диапазон:
    - 1
    - 100
    единица: шт
  - имя: масса_единицы
    диапазон:
    - 0.1
    - 5.0
    единица: kg
  - имя: скорость_передачи
    диапазон:
    - 1
    - 1000
    единица: Mbps
  - имя: дальность
    диапазон:
    - 30
    - 2000
    единица: m
  пределы:
    max_единиц_в_системе: 100
    min_массы: 0.1
    max_массы: 5.0
    min_дальности: 30
    max_дальности: 2000
  закон_масштабирования: 'нелинейный — масса_системы = N × масса_единицы × 1.10 (10%
    overhead на terminators+couplers); типовая установка: MIL-STD-1553 FOE (fiber
    optic extender, 200×100×30 mm, 0.5 kg, 1 Mbps, 1+ km range); FO-1553 1.0625 Gbps
    (Avionics Interface Technologies, 1+ mile range)'
  ограничивающие_части:
  - часть_optovolokonnaya_shina_core (fiber optic transceiver + 1553 protocol chip
    — критическая зависимость от avionics suppliers)
  - часть_optovolokonnaya_shina_housing (aluminum + anodizing MIL-A-8625 — стандартное
    производство)
источник_url: https://en.wikipedia.org/wiki/MIL-STD-1553
источник_дата: '2026-11-11'
---
## Описание

оптоволоконная шина

Полное наименование (как в CSV): `оптоволоконная шина`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | система_связи | — | canon |
| подтип | прочее | — | canon |
| масса | 0.1–5.0 (номинал 0.5) | kg | canon |
| габариты (Д×Ш×В) | 200×117×46 | mm | canon |
| выработка энергии | 0 | W | canon |
| выработка тепла | 0.01–5 | W | canon |
| тип узла | изделие | — | canon |
| уровень_номер | 1 | — | canon |


## Принцип работы

Оптоволоконная шина — канал передачи данных по волоконно-оптическим линиям (авионика: MIL-STD-1773 — волоконная реализация протокола MIL-STD-1553B): терминалы BC/RT/BM обмениваются данными через пассивные волоконные ответвления; активная электроника терминалов (ядро, <=1 W на трансивер) генерирует тепло, пассивные волоконные тракты вносят только вставочные потери (~0.1 W), разъёмы MPO/MTP терминируют линии. Иммунитет к ЭМИ и гальваноразвязка — ключевые преимущества перед медной шиной.

## Состав

Изделие верхнего уровня (4 части): ядро (коммутационный блок 130×85×28), корпус (150×98×33), комплект разъёмов MPO/MTP, крепёж/жгуты (60×25×6). См. раздел Декомпозиция.

## Используемые технологии

- `frezervanie_chpu` (доля: 1.0)
- `anodirovanie` (доля: 1.0)


## Используемые материалы

- `al_6061-t6` (форма: силовые_элементы_конструкций) → [`al_6061-t6`](../../../материалы/al_6061-t6.md)
- `al_6061-t6` (форма: корпуса_электроники) → [`al_6061-t6`](../../../материалы/al_6061-t6.md)


## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- MIL-STD-1773 Fiber Optic Data Bus, NASA GSFC (Small Explorer Data System, M. Flanegan) — https://core.ac.uk/download/pdf/42812227.pdf (обращение 2026-11-08)
- LINK-PP — 10GBASE-T SFP Power & Heat Management Guide: оптические трансиверы <1 W, медные модули ~3 W — https://www.link-pp.com/resources/technical-specs/10gbase-t-sfp-power-heat-management-guide (обращение 2026-11-08)

---

## Декомпозиция

```mermaid
graph TD
    izdelie_optovolokonnaya_shina["izdelie_optovolokonnaya_shina"]
    ______optovolokonnaya_shina_core["часть_optovolokonnaya_shina_core"]
    izdelie_optovolokonnaya_shina --> ______optovolokonnaya_shina_core
    ______optovolokonnaya_shina_housing["часть_optovolokonnaya_shina_housing"]
    izdelie_optovolokonnaya_shina --> ______optovolokonnaya_shina_housing
    ______optovolokonnaya_shina_connectors["часть_optovolokonnaya_shina_connectors"]
    izdelie_optovolokonnaya_shina --> ______optovolokonnaya_shina_connectors
    ______optovolokonnaya_shina_mounting["часть_optovolokonnaya_shina_mounting"]
    izdelie_optovolokonnaya_shina --> ______optovolokonnaya_shina_mounting
```
