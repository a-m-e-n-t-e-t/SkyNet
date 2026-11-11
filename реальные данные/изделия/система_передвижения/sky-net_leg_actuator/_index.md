---
id: izdelie_SkyNet-LegActuator
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: система_передвижения
подтип: привод_конечности
стандарты:
- ISO 9283 (промышленные роботы — точность позы)
- IEC 60034-1 (вращающиеся машины)
исследовательская_группа: boston_dynamics
родитель: null
дочерние_части:
- часть_SkyNet-LegActuator_hip
- часть_SkyNet-LegActuator_knee
- часть_SkyNet-LegActuator_ankle
- часть_SkyNet-LegActuator_mounting
материалы_частей:
- часть: часть_SkyNet-LegActuator_hip
  материал: al_6061-t6
  доля_массы: 0.35
  форма: силовые_элементы_конструкций
- часть: часть_SkyNet-LegActuator_knee
  материал: ti-6al-4v
  доля_массы: 0.3
  форма: планер_и_космические_изделия
- часть: часть_SkyNet-LegActuator_ankle
  материал: al_6061-t6
  форма: корпуса_электроники
  доля_массы: 0.25
- часть: часть_SkyNet-LegActuator_mounting
  материал: ss_aisi_304
  доля_массы: 0.1
  форма: крепёж_пружины_холоднодеформ
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
    min: 1.5
    max: 6.0
    nominal: 3.5
  габариты_mm:
    l: 380
    w: 180
    h: 120
  выработка_энергии_W:
    min: 0
    max: 0
  выработка_тепла_W:
    min: 50
    max: 800
наследуемые: {}
дополнительные:
  число_степеней_свободы: 6
  пиковый_момент_Нм: 220
  тип_привода: BLDC + harmonic drive
дата_создания: 2026-11-05
дата_обновления: '2026-11-11'
источник: web_search
источник_разбора: веб-верификация
источник_url: https://en.wikipedia.org/wiki/Humanoid_robot
источник_дата: '2026-11-11'
технологии_частей:
- часть: часть_SkyNet-LegActuator_hip
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: al_6061-t6
    роль: обрабатываемый
- часть: часть_SkyNet-LegActuator_knee
  технология: ebw
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: ti-6al-4v
    роль: обрабатываемый
- часть: часть_SkyNet-LegActuator_ankle
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: al_6061-t6
    роль: обрабатываемый
- часть: часть_SkyNet-LegActuator_mounting
  технология: shtampovka_listovaya
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: ss_aisi_304
    роль: обрабатываемый
наследуемые_материалы:
- материал: al_6061-t6
  суммарная_доля_массы: 1.5
  источники_частей:
  - часть_SkyNet-LegActuator_hip
  - часть_SkyNet-LegActuator_knee
  - часть_SkyNet-LegActuator_ankle
  форма: корпуса_электроники
- материал: copper
  суммарная_доля_массы: 0.9
  источники_частей:
  - часть_SkyNet-LegActuator_hip
  - часть_SkyNet-LegActuator_knee
  - часть_SkyNet-LegActuator_ankle
  форма: обмотки_электрических_машин
- материал: 100cr6
  суммарная_доля_массы: 0.9
  источники_частей:
  - часть_SkyNet-LegActuator_hip
  - часть_SkyNet-LegActuator_knee
  - часть_SkyNet-LegActuator_ankle
  форма: подшипники_качения
- материал: spring_steel
  суммарная_доля_массы: 0.65
  источники_частей:
  - часть_SkyNet-LegActuator_hip
  - часть_SkyNet-LegActuator_knee
  форма: a229_маслоотпущенная
- материал: ti-6al-4v
  суммарная_доля_массы: 0.3
  источники_частей:
  - часть_SkyNet-LegActuator_knee
  форма: планер_и_космические_изделия
- материал: spring_steel
  суммарная_доля_массы: 0.25
  источники_частей:
  - часть_SkyNet-LegActuator_ankle
  форма: a228_музыкальная_проволока
- материал: ss_aisi_304
  суммарная_доля_массы: 0.1
  источники_частей:
  - часть_SkyNet-LegActuator_mounting
  форма: крепёж_пружины_холоднодеформ
масштабируемость:
  режим: квантуемая
  параметры:
  - имя: количество_единиц
    диапазон:
    - 1
    - 4
    единица: шт
  - имя: масса_единицы
    диапазон:
    - 2.0
    - 10.0
    единица: kg
  пределы:
    max_единиц_в_системе: 4
    min_массы: 2.0
    max_массы: 10.0
  закон_масштабирования: 'линейный — масса_системы = N × масса_единицы; типовая установка:
    LegActuator для гуманоидного робота (hip+knee+ankle, Al/Ti/SS joints)'
  ограничивающие_части:
  - часть_SkyNet-LegActuator_hip (al_6061-t6 hip joint — критическая механика)
  - часть_SkyNet-LegActuator_knee (ti-6al-4v knee joint — high-strength)
---
## Описание

Гуманоидный нога-привод (leg actuator assembly): модуль из 3 сочленений (тазобедренное hip, коленное knee, голеностопное ankle) с BLDC-моторами + harmonic-drive редукторами, формирующий одну ногу гуманоидной платформы класса Atlas/Optimus. Аналог энергоблока SkyNet-гуманоидов (T700/T900/T950/TRIP): 6 степеней свободы на ногу, пиковый момент 220 Нм на hip, работа до 4 часов от батарейного рюкзака. Envelope модуля 380×180×120 мм, масса 3.5 кг (пара ног — 7 кг из ~75 кг корпуса робота).

Родитель: верхний уровень иерархии (подсистема: `система_передвижения`).

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | система_передвижения | — | canon |
| подтип | привод_конечности | — | canon |
| масса | 1.5–6.0 (номинал 3.5) | kg | canon |
| габариты (Д×Ш×В) | 380×180×120 | mm | canon |
| выработка энергии | 0–0 | W | canon |
| выработка тепла | 50–800 | W | canon |
| тип узла | изделие | — | canon |
| уровень_номер | 1 | — | canon |


## Принцип работы

Каждое сочленение — модульная сборка «BLDC + strain-wave (harmonic) редуктор + torque sensor + absolute encoder»: мотор разгоняется до 9000 об/мин, harmonic drive (ratio 100–160:1) снижает до 60–90 об/мин на выходе с моментом 100–220 Нм. Контроллер FOC (field-oriented control) на 400 Гц с датчиком тока и момента закрывает петлю обратной связи; trajectory-planner верхнего уровня выдаёт целевые углы суставов с частотой 1 кГц. Гуманоидная походка поддерживается баланс-контроллером (MPC + ZMP). Источник: Boston Dynamics Atlas spec sheet + humanoid.guide (актyator commonality).

## Состав

Изделие уровня 1, состоит из 4 дочерних частей (hip, knee, ankle, mounting). Каждое сочленение — отдельныйservo-узел; mounting-часть включает интерфейс к тазовому/стопному фланцам.

```mermaid
graph TD
    izdelie_SkyNet-LegActuator["izdelie_SkyNet-LegActuator"]
    hip["часть_SkyNet-LegActuator_hip"]
    izdelie_SkyNet-LegActuator --> hip
    knee["часть_SkyNet-LegActuator_knee"]
    izdelie_SkyNet-LegActuator --> knee
    ankle["часть_SkyNet-LegActuator_ankle"]
    izdelie_SkyNet-LegActuator --> ankle
    la_mounting["часть_SkyNet-LegActuator_mounting"]
    izdelie_SkyNet-LegActuator --> la_mounting
```

## Используемые технологии

- `frezervanie_chpu` (доля: 1.0)
- `ebw` (доля: 1.0)
- `frezervanie_chpu` (доля: 1.0)
- `shtampovka_listovaya` (доля: 1.0)


## Используемые материалы

- `al_6061-t6` (форма: силовые_элементы_конструкций) → [`al_6061-t6`](../../../материалы/al_6061-t6.md)
- `ti-6al-4v` (форма: планер_и_космические_изделия) → [`ti-6al-4v`](../../../материалы/ti-6al-4v.md)
- `al_6061-t6` (форма: корпуса_электроники) → [`al_6061-t6`](../../../материалы/al_6061-t6.md)
- `ss_aisi_304` (форма: крепёж_пружины_холоднодеформ) → [`ss_aisi_304`](../../../материалы/ss_aisi_304.md)


## Источники

- Канон: декомпозиция SkyNet-гуманоидных моделей (web_search 2026-11-05)
- Boston Dynamics Atlas (electric): https://bostondynamics.com/products/atlas
- Humanoid actuator commonality: https://humanoid.guide/humanoid-actuator-commonality
- Материалы: реальные данные/материалы/

## Декомпозиция

```mermaid
graph TD
    izdelie_SkyNet_LegActuator["izdelie_SkyNet-LegActuator"]
    ______SkyNet_LegActuator_hip["часть_SkyNet-LegActuator_hip"]
    izdelie_SkyNet_LegActuator --> ______SkyNet_LegActuator_hip
    ______SkyNet_LegActuator_knee["часть_SkyNet-LegActuator_knee"]
    izdelie_SkyNet_LegActuator --> ______SkyNet_LegActuator_knee
    ______SkyNet_LegActuator_ankle["часть_SkyNet-LegActuator_ankle"]
    izdelie_SkyNet_LegActuator --> ______SkyNet_LegActuator_ankle
    ______SkyNet_LegActuator_mounting["часть_SkyNet-LegActuator_mounting"]
    izdelie_SkyNet_LegActuator --> ______SkyNet_LegActuator_mounting
```
