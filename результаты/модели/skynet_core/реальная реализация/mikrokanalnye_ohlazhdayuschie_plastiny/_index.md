---
id: izdelie_mikrokanalnye_ohlazhdayuschie_plastiny
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: система_охлаждения
подтип: прочее
стандарты: 
  - ASHRAE 15
исследовательская_группа: boyd_corp
родитель: null
дочерние_части:
  - часть_mikrokanalnye_ohlazhdayuschie_plastiny_core
  - часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing
  - часть_mikrokanalnye_ohlazhdayuschie_plastiny_connectors
  - часть_mikrokanalnye_ohlazhdayuschie_plastiny_mounting
материалы_частей:
  - часть: часть_mikrokanalnye_ohlazhdayuschie_plastiny_core
    материал: copper
    форма: теплосъём_и_экранирование
    доля_массы: 0.45
  - часть: часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing
    материал: al_6061-t6
    форма: корпуса_электроники
    доля_массы: 0.27

# F29 (B-BOM): агрегация материалов частей с долями родителя
# (формат validate_decomposition.check_F29: материал+форма+суммарная_доля_массы
# + источники_частей; core 0.45×1.0, housing 0.27×1.0).
наследуемые_материалы:
  - материал: copper
    форма: теплосъём_и_экранирование
    суммарная_доля_массы: 0.45
    источники_частей:
      - часть_mikrokanalnye_ohlazhdayuschie_plastiny_core
  - материал: al_6061-t6
    форма: корпуса_электроники
    суммарная_доля_массы: 0.27
    источники_частей:
      - часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing

# F27e: технологии обработки деталей — фрезерование ЧПУ обеих деталей:
# медная пластина с микроканалами (multi-blade milling) и корпус-рамка
# al_6061-T6 — CNC-фрезерование (rivcut.com: «Aluminum 6061-T6 is the
# default choice for 80% of cold plates… machines fast»; ptsmake.com:
# «CNC machining is the dominant process for making liquid cooling
# components»).
технологии_частей:
  - часть: часть_mikrokanalnye_ohlazhdayuschie_plastiny_core
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: copper
        роль: обрабатываемый
  - часть: часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: al_6061-t6
        роль: обрабатываемый

# F-scal (P087 §12.6): изделие квантуемое — N модульных пластин
# (core 0.1 кг + корпус 0.09 кг + разъём/крепёж); масштабирование —
# количественное (число пластин), пределы совпадают с основными.
масштабируемость:
  режим: квантуемая
  параметры: [масса_kg]
  пределы:
    min: {масса_kg: 0.05}
    max: {масса_kg: 5}
  закон_масштабирования:
    масса: 'линейный (N × модульная пластина: core 0.1 кг + корпус 0.09 кг + разъём/крепёж)'
  ограничивающие_части: []

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
          max: 5
          nominal: 0.5
  габариты_mm:
          l: 200
          w: 100
          h: 24
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0
          max: 0.15
          nominal: 0.1
наследуемые: {}
дополнительные:
  цена_usd: null
  габариты_метод: 'конверт сборки 200×100×24 мм: пластина 200×100×5 мм (ThermAvant micromachined cold plate) + разъём Anderson SB50 47.5×27.7×19 мм (datasheet APP) на верхней поверхности + крепёжные скобы 95×55×12 мм в пределах высоты разъёма; корпус-рамка 115×69×8 мм охватывает тепловую зону; V=480000 мм³ ≥ ΣV(детей) 181179×1.15=208356 (запас ×2.3), оси 200≥115 / 100≥69 / 24≥19'
  толщина_пластины_mm: 5
дата_создания: 2026-11-03
дата_обновления: 2026-11-08
источник: web_search
источник_разбора: веб-верификация
источник_url: https://www.thermavant.com/thermavant-products/cold-plates
источник_дата: 2026-11-07
---
## Описание

Микроканальная охлаждающая пластина (liquid cold plate) — пассивный теплообменник для отвода высоких тепловых потоков от силовой электроники/батарей: пластина 200×100×5 мм с внутренними микроканалами (0.3–0.5 мм), по которым прокачивается теплоноситель (деионизированная вода, EGW, PAO). Съём теплового потока до 50 Вт/см² (ThermAvant, micromachined/brazed cold plates). Корпус-рамка — алюминий al_6061-T6 — CNC-фрезерование (6061-T6 — базовый материал ~80 % cold plates: лёгкий, коррозионно-стойкий, анодируемый, k ≈ 167 Вт/(м·К), rivcut.com); тепловая зона (core) выполнена из меди Cu-ETP с микроканалами (ThermAvant micromachined). Масса пластины ~0.5 кг (оценка по плотности меди/алюминия и толщине стенок каналов).

Габарит изделия — конверт сборки **200×100×24 мм**: сама пластина 5 мм толщиной; разъём питания насоса Anderson SB50 (47.5×27.7×19 мм по datasheet Anderson Power Products) установлен на верхней поверхности; крепёжные скобы (95×55×12 мм) размещаются на верхней же поверхности в пределах высоты разъёма; корпус-рамка (115×69×8 мм) охватывает тепловую зону в основании. Объём конверта 480000 мм³ ≥ ΣV(детей)×1.15 = 208356 мм³ (запас ×2.3) — все 4 части физически помещаются в изделие (оси: 200≥115 / 100≥69 / 24≥19).

Родитель — верхний уровень подсистемы система_охлаждения. Состав: core (медная пластина с каналами), housing (фрезерованный корпус-рамка al_6061-T6), connectors (разъём Anderson SB50 50 А для насоса), mounting (крепёж 8×M4).

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | система_охлаждения | — | canon |
| подтип | прочее | — | canon |
| масса | 0.05–5 (номинал 0.5) | kg | canon |
| габариты (Д×Ш×В) | 200×100×24 | mm | canon |
| выработка энергии | 0 | W | canon |
| выработка тепла | 0–0.15 | W | canon |
| тип узла | изделие | — | canon |
| уровень_номер | 1 | — | canon |


## Принцип работы

Чип/источник тепла передаёт тепловой поток через контактную поверхность к медному core, где микроканалы заполняются теплоносителем. Прокачка теплоносителя насосом переносит тепло к радиатору/чиллеру за пределами пластины. Пластина пассивна: собственное тепловыделение определяется только джоулевыми потерями в разъёме питания насоса (Anderson SB50, 50 А, ~0.1 Вт) — именно это значение фигурирует в балансе F15b (parent 0.1 Вт ≥ Σ детей 0.1 Вт).

## Используемые технологии

- `frezervanie_chpu` (доля: 1.0)
- `frezervanie_chpu` (доля: 1.0)


## Используемые материалы

- `copper` (форма: теплосъём_и_экранирование) → [`copper`](../../../материалы/copper.md)
- `al_6061-t6` (форма: корпуса_электроники) → [`al_6061-t6`](../../../материалы/al_6061-t6.md)


## Источники

- ThermAvant Technologies — Cold Plates, High Heat Flux Thermal Management (heat flux до 50 W/cm², материалы Al/Cu/Cu-Mo/stainless, рабочие жидкости DI water/EGW/PAO): https://www.thermavant.com/thermavant-products/cold-plates (обращение 2026-11-07)
- Power-E — Жидкостная система охлаждения в современных корпусах (микроканальные охладители: тонкие медные листы, химическое травление каналов): https://power-e.ru/cooling/zhidkostnaya-sistema-ohlazhdeniya (обращение 2026-11-07)
- RivCut — Cold Plate Machining (Aluminum 6061-T6 — базовый материал ~80 % cold plates, CNC-фрезерование пластин и корпусов): https://www.rivcut.com/blog/cold-plate-machining (обращение 2026-11-10)
- PTSMAKE — CNC Machining for Liquid Cooling Components (CNC-обработка — доминирующий процесс изготовления cold plates, коллекторов и коннекторов): https://www.ptsmake.com/cnc-machining-for-liquid-cooling-components (обращение 2026-11-10)
- ToneCooling — Liquid Cold Plate Design Process (процессы: CNC machining, vacuum brazing, diffusion bonding, FSW): https://tonecooling.com/about-us/liquid-cold-plate-design-process (обращение 2026-11-10)
- CSV: `начальные данные_final.csv` (пользовательский ввод)

---

## Декомпозиция

```mermaid
graph TD
    izdelie_mikrokanalnye_ohlazhdayuschie_plastiny["izdelie_mikrokanalnye_ohlazhdayuschie_plastiny"]
    ______mikrokanalnye_ohlazhdayuschie_plastiny_core["часть_mikrokanalnye_ohlazhdayuschie_plastiny_core"]
    izdelie_mikrokanalnye_ohlazhdayuschie_plastiny --> ______mikrokanalnye_ohlazhdayuschie_plastiny_core
    ______mikrokanalnye_ohlazhdayuschie_plastiny_housing["часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing"]
    izdelie_mikrokanalnye_ohlazhdayuschie_plastiny --> ______mikrokanalnye_ohlazhdayuschie_plastiny_housing
    ______mikrokanalnye_ohlazhdayuschie_plastiny_connectors["часть_mikrokanalnye_ohlazhdayuschie_plastiny_connectors"]
    izdelie_mikrokanalnye_ohlazhdayuschie_plastiny --> ______mikrokanalnye_ohlazhdayuschie_plastiny_connectors
    ______mikrokanalnye_ohlazhdayuschie_plastiny_mounting["часть_mikrokanalnye_ohlazhdayuschie_plastiny_mounting"]
    izdelie_mikrokanalnye_ohlazhdayuschie_plastiny --> ______mikrokanalnye_ohlazhdayuschie_plastiny_mounting
```
