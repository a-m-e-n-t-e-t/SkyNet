---
id: izdelie_SkyNet-PowerBackpack
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: система_питания
подтип: батарейный_блок
стандарты:
  - UN 38.3 (транспорт литий-ионных батарей)
  - IEC 62133-2 (безопасность Li-ion)
  - IEEE 1625 (многоэлементные сборки)
исследовательская_группа: boston_dynamics
родитель: null
дочерние_части:
  - часть_SkyNet-PowerBackpack_cells
  - часть_SkyNet-PowerBackpack_bms
  - часть_SkyNet-PowerBackpack_housing
  - часть_SkyNet-PowerBackpack_mounting
материалы_частей:
  - часть: часть_SkyNet-PowerBackpack_cells
    материал: nmc_graphite
    доля_массы: 0.65
  - часть: часть_SkyNet-PowerBackpack_bms
    материал: al_6061-t6
    доля_массы: 0.12
  - часть: часть_SkyNet-PowerBackpack_housing
    материал: al_6061-t6
    доля_массы: 0.15
  - часть: часть_SkyNet-PowerBackpack_mounting
    материал: ss_aisi_304
    форма: крепёж_пружины_холоднодеформ
    доля_массы: 0.08
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
    min: 4.0
    max: 12.0
    nominal: 7.5
  габариты_mm:
    l: 360
    w: 280
    h: 200
  выработка_энергии_W:
    min: 0
    max: 1500
  выработка_тепла_W:
    min: 10
    max: 250
наследуемые: {}
дополнительные:
  тип_химии: NMC (LiNiMnCoO₂) / graphite
  ёмкость_Wh: 1500
  напряжение_номинал_V: 48
  время_разряда_ч: 4
  циклов_до_80_pct: 1000
дата_создания: 2026-11-05
дата_обновления: 2026-11-07
источник: web_search
источник_разбора: канон
источник_url: https://bostondynamics.com/products/atlas
источник_дата: 2026-11-05
---
# Изделие: izdelie_SkyNet-PowerBackpack

## Описание

Батарейный рюкзак гуманоидной платформы: модульный Li-ion (NMC/graphite) блок 48 В × ~31 А·ч (~1500 Вт·ч), размещённый в спинном отсеке гуманоида класса Atlas/Optimus. Аналог системы питания SkyNet-гуманоидов (T700/T900/T950/TRIP): 4 часа непрерывной ходьбы с нагрузкой 30 кг (sustained) или 50 кг (instant). Батарейный отсек 320×220×140 мм; рюкзак в сборе с несущей рамой, быстросъёмным посадочным лотком и вентиляционным каналом — 360×280×200 мм, масса 7.5 кг (≈10% массы робота). Активный BMS (battery management system) с поканальным мониторингом температуры, тока и напряжения; система терморегуляции (heat-pipe + forced air) отводит 250 Вт пикового тепла.

Родитель: верхний уровень иерархии (подсистема: `система_питания`).

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | система_питания | — | canon |
| подтип | батарейный_блок | — | canon |
| масса (nominal) | 7.5 | kg | web_search (Atlas-class battery backpack) |
| габариты в сборе (Д×Ш×В) | 360×280×200 | mm | рюкзак в сборе (отсек 320×220×140 + несущая рама с посадочным лотком); масштабирование от Spot battery 324×168×93 мм / payload mounting area 850×240×270 мм (batterydesign.net, bostondynamics.com) |
| химия | NMC / graphite | — | web_search (Boston Dynamics Atlas) |
| ёмкость | 1500 | Wh | web_search (Atlas spec: 4h runtime) |
| напряжение номинал | 48 | V | canon (промышленный standard) |
| циклов до 80% | 1000 | — | IEC 62133-2 (NMC typical) |
| теплоотдача (пик) | 250 | W | оценка при 1.5 кВт разряде, η≈0.85 |

## Принцип работы

Li-ion сборка 14s×10p (14 последовательно × 10 параллельно) NMC-ячеек 21700 формата (~5 А·ч каждая), суммарно ~1500 Вт·ч при 48 В. BMS на каждой ячейке: мониторинг напряжения ±10 мВ, тока ±0.1 А, температуры ±1°C; балансировка при 4.20 В ±50 мВ. Разрядная способность до 30 А непрерывно (1500 Вт), 50 А пик (2500 Вт <10 сек). Корпус с принудительным обдувом (вентилятор 40×40 мм, 12 CFM) отводит 250 Вт тепла при пиковой разрядке. Совместимость с UN 38.3 и IEC 62133-2. Источник: Boston Dynamics Atlas spec sheet (4 часа battery life, 50 кг weight capacity).

## Состав

Изделие уровня 1, состоит из 4 дочерних частей: ячейки (cells), система управления (BMS), корпус с терморегуляцией (housing), крепёж (mounting).

```mermaid
graph TD
    izdelie_SkyNet-PowerBackpack["izdelie_SkyNet-PowerBackpack"]
    cells["часть_SkyNet-PowerBackpack_cells"]
    izdelie_SkyNet-PowerBackpack --> cells
    bms["часть_SkyNet-PowerBackpack_bms"]
    izdelie_SkyNet-PowerBackpack --> bms
    housing["часть_SkyNet-PowerBackpack_housing"]
    izdelie_SkyNet-PowerBackpack --> housing
    pb_mounting["часть_SkyNet-PowerBackpack_mounting"]
    izdelie_SkyNet-PowerBackpack --> pb_mounting
```

## Используемые материалы

- `nmc_graphite` → ячейки (NMC катод / графит анод)
- `al_6061-t6` → корпус и радиатор BMS
- `ss_aisi_304` → крепёж + бандажные ленты

## Источники

- Канон: декомпозиция SkyNet-гуманоидных моделей (web_search 2026-11-05)
- Boston Dynamics Atlas (4h battery, 50 kg capacity): https://bostondynamics.com/products/atlas
- Boston Dynamics Spot battery pack (референс компоновки: 324×168×93 мм, 605 Wh, 14s4p, hot-swap): https://www.batterydesign.net/boston-dynamics-spot-battery/
- Boston Dynamics Spot payload mounting area 850×240×270 мм, интерфейс M5 T-slot rails: https://bostondynamics.com/products/spot
- IEC 62133-2 + UN 38.3 safety standards
- Материалы: реальные данные/материалы/
