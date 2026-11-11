---
id: izdelie_elektroflyuidnye_volokna_mit
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: приводная_система
подтип: прочее
стандарты:
- IEC 60034
- ISO 1940
исследовательская_группа: maxon_faulhaber
родитель: null
дочерние_части:
- часть_elektroflyuidnye_volokna_mit_core
- часть_elektroflyuidnye_volokna_mit_housing
- часть_elektroflyuidnye_volokna_mit_connectors
- часть_elektroflyuidnye_volokna_mit_mounting
материалы_частей:
- часть: часть_elektroflyuidnye_volokna_mit_core
  материал: ionnaya_zhidkost_emim_tfsi
  форма: электролит_батарей_и_суперконденсаторов
  доля_массы: 0.45
- часть: часть_elektroflyuidnye_volokna_mit_housing
  материал: al_6061-t6
  форма: крепёж_и_монтажные_плиты
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
    min: 0.05
    max: 50
    nominal: 1
  габариты_mm:
    l: 133
    w: 12
    h: 10
  выработка_энергии_W:
    min: 0
    max: 0
    nominal: 0
  выработка_тепла_W:
    min: 0.1
    max: 50
    nominal: 5
наследуемые: {}
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: '2026-11-11'
источник: web_search
источник_разбора: веб-верификация
источник_url: https://en.wikipedia.org/wiki/Ionic_liquid
источник_дата: '2026-11-11'
технологии_частей:
- часть: часть_elektroflyuidnye_volokna_mit_core
  технология: mikrovolokna_electrospinning
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: ionnaya_zhidkost_emim_tfsi
    роль: обрабатываемый
- часть: часть_elektroflyuidnye_volokna_mit_housing
  технология: anodirovanie
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: aluminum
    роль: обрабатываемый
наследуемые_материалы:
- материал: ionnaya_zhidkost_emim_tfsi
  суммарная_доля_массы: 0.45
  источники_частей:
  - часть_elektroflyuidnye_volokna_mit_core
  форма: электролит_батарей_и_суперконденсаторов
- материал: al_6061-t6
  суммарная_доля_массы: 0.27
  источники_частей:
  - часть_elektroflyuidnye_volokna_mit_housing
  форма: крепёж_и_монтажные_плиты
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
    - 0.001
    - 0.1
    единица: kg
  - имя: напряжение_управления
    диапазон:
    - 1
    - 10
    единица: V
  пределы:
    max_единиц_в_системе: 1000
    min_массы: 0.001
    max_массы: 0.1
    min_напряжения: 1
    max_напряжения: 10
  закон_масштабирования: 'линейный — масса_системы = N × масса_единицы (soft actuator,
    no overhead); типовая установка: MIT electrofluidic fibers (EMIM-TFSI ionic liquid
    + silicone microfibers, 1-10V, low-voltage actuation)'
  ограничивающие_части:
  - часть_elektroflyuidnye_volokna_mit_core (EMIM-TFSI ionic liquid + electrospun
    microfibers — критическая точность производства)
  - часть_elektroflyuidnye_volokna_mit_housing (aluminum + anodizing — стандартное
    производство)
---
## Описание

Электрофлюидные волокна MIT — модуль пучка электрофлюидных волоконных мышц (Electrofluidic Fiber Muscles, MIT / Science Robotics 2026, Afsar, Cacucciolo и др.): волокна миллиметрового масштаба (не толще зубочистки, несколько граммов каждое) с миниатюрными EHD-насосами твёрдотельного типа, закачивающими заряд в диэлектрическую жидкость в замкнутом контуре (без внешнего резервуара). Пучок конфигурации «strong» поднимает 4 кг; рычаг «fast» — выброс за 0.2 с; плетёная пара «бицепс-трицепс» сгибает роборукую. Габаритный конверт модуля 133×12×10 мм — осевая сборка: кожух пучка 115×8×8 (часть_elektroflyuidnye_volokna_mit_housing: волокно 100×5×5 с припуском ~15 %) + торцевой манифольд-блок 18×12×10 (часть_elektroflyuidnye_volokna_mit_mounting: 6× посадок Ø1.2 мм, флюидный порт ISO 6149 M3), продолжающий ось: 115+18=133 мм; ZIF-шлейф 18×5×2.6 (часть_elektroflyuidnye_volokna_mit_connectors) укладывается вдоль блока. Проверка упаковки: V(конверт)=133×12×10=15 960 мм³ ≥ Σ V(детей)=12 254 мм³ × 1.15 = 14 092 мм³ (коэффициент запаса 1.30); по осям 133≥115, 12≥12, 10≥10.

Полное наименование (как в CSV): `Электрофлюидные волокна MIT`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | приводная_система | — | canon |
| подтип | прочее | — | canon |
| масса | 0.05–50 (номинал 1) | kg | canon |
| габариты (Д×Ш×В) | 133×12×10 | mm | canon |
| выработка энергии | 0 | W | canon |
| выработка тепла | 0.1–50 | W | canon |
| тип узла | изделие | — | canon |
| уровень_номер | 1 | — | canon |


## Принцип работы

Требует описания на основе инженерного анализа.

## Состав

Изделие верхнего уровня (уровень 1, подсистема приводная_система). Дочерние части уровня 2: часть_elektroflyuidnye_volokna_mit_core (волокно с EHD-насосом, 100×5×5), часть_elektroflyuidnye_volokna_mit_housing (кожух пучка 115×8×8), часть_elektroflyuidnye_volokna_mit_connectors (ZIF FPC 24-конт., 18×5×2.6), часть_elektroflyuidnye_volokna_mit_mounting (торцевой манифольд 18×12×10).

## Используемые технологии

- `mikrovolokna_electrospinning` (доля: 1.0)
- `anodirovanie` (доля: 1.0)


## Используемые материалы

- `ionnaya_zhidkost_emim_tfsi` (форма: электролит_батарей_и_суперконденсаторов) → [`ionnaya_zhidkost_emim_tfsi`](../../../материалы/ionnaya_zhidkost_emim_tfsi.md)
- `al_6061-t6` (форма: крепёж_и_монтажные_плиты) → [`al_6061-t6`](../../../материалы/al_6061-t6.md)


## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)

---

## Декомпозиция

```mermaid
graph TD
    izdelie_elektroflyuidnye_volokna_mit["izdelie_elektroflyuidnye_volokna_mit"]
    ______elektroflyuidnye_volokna_mit_core["часть_elektroflyuidnye_volokna_mit_core"]
    izdelie_elektroflyuidnye_volokna_mit --> ______elektroflyuidnye_volokna_mit_core
    ______elektroflyuidnye_volokna_mit_housing["часть_elektroflyuidnye_volokna_mit_housing"]
    izdelie_elektroflyuidnye_volokna_mit --> ______elektroflyuidnye_volokna_mit_housing
    ______elektroflyuidnye_volokna_mit_connectors["часть_elektroflyuidnye_volokna_mit_connectors"]
    izdelie_elektroflyuidnye_volokna_mit --> ______elektroflyuidnye_volokna_mit_connectors
    ______elektroflyuidnye_volokna_mit_mounting["часть_elektroflyuidnye_volokna_mit_mounting"]
    izdelie_elektroflyuidnye_volokna_mit --> ______elektroflyuidnye_volokna_mit_mounting
```
