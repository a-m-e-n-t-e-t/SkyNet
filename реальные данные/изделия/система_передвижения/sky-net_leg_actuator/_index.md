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
  - часть: часть_SkyNet-LegActuator_knee
    материал: ti-6al-4v
    доля_массы: 0.30
  - часть: часть_SkyNet-LegActuator_ankle
    материал: al_6061-t6
    доля_массы: 0.25
  - часть: часть_SkyNet-LegActuator_mounting
    материал: ss_aisi_304
    доля_массы: 0.10
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
дата_обновления: 2026-11-05
источник: web_search
источник_разбора: канон
источник_url: https://bostondynamics.com/products/atlas
источник_дата: 2026-11-05
---
# Изделие: izdelie_SkyNet-LegActuator

## Описание

Гуманоидный нога-привод (leg actuator assembly): модуль из 3 сочленений (тазобедренное hip, коленное knee, голеностопное ankle) с BLDC-моторами + harmonic-drive редукторами, формирующий одну ногу гуманоидной платформы класса Atlas/Optimus. Аналог энергоблока SkyNet-гуманоидов (T700/T900/T950/TRIP): 6 степеней свободы на ногу, пиковый момент 220 Нм на hip, работа до 4 часов от батарейного рюкзака. Envelope модуля 380×180×120 мм, масса 3.5 кг (пара ног — 7 кг из ~75 кг корпуса робота).

Родитель: верхний уровень иерархии (подсистема: `система_передвижения`).

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | система_передвижения | — | canon |
| подтип | привод_конечности | — | canon |
| масса (nominal) | 3.5 | kg | web_search (Boston Dynamics Atlas spec) |
| габариты (Д×Ш×В) | 380×180×120 | mm | оценка по hip+knee+ankle envelope |
| пиковый момент | 220 | Нм | web_search (Atlas-class hip joint) |
| степеней свободы | 6 | — | canon (3 на ногу × 2) |
| тип привода | BLDC + harmonic drive | — | canon |
| теплоотдача (пик) | 800 | W | web_search (Atlas actuator efficiency) |

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

## Используемые материалы

- `al_6061-t6` → hip/ankle корпуса (лёгкость, усталостная прочность)
- `ti-6al-4v` → knee (высокий момент, усталость при динамических пиках)
- `ss_aisi_304` → крепёж (M8/M10 болты фланцевых стыков)

## Источники

- Канон: декомпозиция SkyNet-гуманоидных моделей (web_search 2026-11-05)
- Boston Dynamics Atlas (electric): https://bostondynamics.com/products/atlas
- Humanoid actuator commonality: https://humanoid.guide/humanoid-actuator-commonality
- Материалы: реальные данные/материалы/
