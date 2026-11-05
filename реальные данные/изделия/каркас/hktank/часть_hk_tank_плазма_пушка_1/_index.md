---
id: часть_hk_tank_плазма_пушка_1
тип: изделие
категория: машиностроение
уровень_иерархии: промежуточный
уровень_номер: 2
подсистема: встроенное_оружие
подтип: plasma_cannon
стандарты:
  - MIL-STD-810
  - MIL-STD-1913
исследовательская_группа: null
родитель: izdelie_SkyNet-HKTank
количество: 2
дочерние_части: []
материалы_частей:
  - часть: часть_hk_tank_плазма_пушка_1
    материал: w-ni-fe
    доля_массы: 1.0
scaling_type: количественный
соединители:
  - шина_данных
  - кабель_силовой
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
ии_перепроектирован:
  статус: false
  верификация: []
основные:
  масса_kg: 500.0
  доля_массы_родителя: 0.017
  габариты_mm:
    l: 1500
    w: 500
    h: 500
  выработка_энергии_W: 0
  выработка_тепла_W: 500
наследуемые: {}
дополнительные:
  тип: 'dual-barrel phased plasma cannon (twin-barreled directional plasma cannon)'
  мощность_выстрела_MJ: 5
  скорострельность_выстр_мин: 200
  power_source: 'fusion reactor (источник питания HK-Tank)'
  rotation: '360 degrees (turret-mounted on steel arm)'
  target_type: 'aerial and ground based targets'
  ammo_type: 'plasma bolt (no conventional ammunition — energy weapon)'
дата_создания: 2026-11-03
дата_обновления: 2026-11-05
источник: web_search
источник_разбора: канон
источник_url: https://terminator.fandom.com/wiki/HK-Tank + https://terminator.fandom.com/wiki/Plasma_cannon + https://kaiju.wikidot.com/wiki:hunter-killer
источник_дата: 2026-11-04
---
# Часть: часть_hk_tank_плазма_пушка_1 (×2)
## Описание

Двухствольная фазированная плазменная пушка HK-Tank (twin-barreled directional plasma cannon), установленная на стальном «руке» в составе конусной башни (conning tower). Основное вооружение HK-Tank — совместно со второй плазменной пушкой и спаренными пулемётами.

Из terminator.fandom.com/wiki/HK-Tank: «...two steel "arms" equipped with twin-barreled directional plasma cannons». Пушка способна вести огонь по наземным и воздушным целям. Конструкция обеспечивает 360-градусное вращение.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | встроенное_оружие | — | canon |
| подтип | plasma_cannon | — | canon |
| масса | 500.0 | kg | canon |
| доля массы родителя | 0.017 | — | canon |
| габариты (Д×Ш×В) | 1500×500×500 | mm | canon |
| выработка энергии | 0 | W | canon |
| выработка тепла | 500 | W | canon |
| материал | w-ni-fe (W-Ni-Fe heavy alloy) | — | canon |
| тип оружия | dual-barrel phased plasma cannon | — | Fandom |
| мощность выстрела | 5 | MJ | canon |
| скорострельность | 200 | выстр/мин | canon |
| вращение | 360 | degrees | kaiju.wikidot.com |
| цель | наземные и воздушные | — | Fandom |

## Принцип работы

Capacitor bank разряжается через plasma cell → Lorentz force ускоряет плазму. Питание от fusion reactor HK-Tank.

Плазменная пушка использует электромагнитный принцип ускорения высокотемпературной плазмы. Заряд конденсаторной батареи подаётся на импульсные катушки, создавая магнитное поле, которое ускоряет плазменный тороид по стволу с использованием силы Лоренца. Энергия выстрела — 5 МДж, скорострельность — 200 выстрелов в минуту.

## Состав

Промежуточная часть (уровень 2). Дочерних частей нет.

## Используемые материалы

- `w-ni-fe` → [`w-ni-fe.md`](../../../../материалы/w-ni-fe.md) — вольфрам-никель-железный тяжёлый сплав для ствола и теплоотвода

## Источники

- https://terminator.fandom.com/wiki/HK-Tank — HK-Tank armament (dual plasma cannons + dual machine guns)
- https://terminator.fandom.com/wiki/Plasma_cannon — known plasma cannons (Mark-108, 40-watt Phased)
- https://kaiju.wikidot.com/wiki:hunter-killer — 360-degree plasma cannon rotation
- Декомпозиция: `izdelie_SkyNet-HKTank` (web search 2026-11-03)
- Материалы: реальные данные/материалы/


## Примечание о количестве

Эта часть представляет собой **2 идентичных экземпляра** (поле `количество: 2`).
для устранения дублирования данных (принцип P085 — канонизация).
Масса и габариты указаны за **один** экземпляр; `доля_массы_родителя` — суммарная.
