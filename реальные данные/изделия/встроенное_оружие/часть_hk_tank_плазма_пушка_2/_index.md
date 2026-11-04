---
id: часть_hk_tank_плазма_пушка_2
тип: изделие
категория: машиностроение
уровень_иерархии: промежуточный
уровень_номер: 2
подсистема: встроенное_оружие
подтип: plasma_cannon
стандарты:
  - MIL-STD-810
исследовательская_группа: null
родитель: izdelie_SkyNet-HKTank
дочерние_части: []
материалы_частей:
  - часть: часть_hk_tank_плазма_пушка_2
    материал: w-ni-fe
    доля_массы: 1.0

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
  тип: 'phased plasma cannon (второй экземпляр спарки — на другой стальной «руке» конусной башни)'
  мощность_выстрела_MJ: 5
  скорострельность_выстр_мин: 200
  mount_side: 'вторая стальная «рука» башни HK-Tank (парная к пушке_1)'
  ammo_type: 'plasma bolt (directed-energy weapon, без боеприпасов)'

дата_создания: 2026-11-03
дата_обновления: 2026-11-04
источник: web_search
источник_url: https://terminator.fandom.com/wiki/HK-Tank + https://kaiju.wikidot.com/wiki:hunter-killer + https://terminator.fandom.com/wiki/Plasma_weaponry
источник_дата: 2026-11-04
источник_разбора: канон
---

# Часть: часть_hk_tank_плазма_пушка_2

## Описание

Вторая фазированная плазменная пушка HK-Tank (phased plasma cannon), смонтированная на второй стальной «руке» конусной башни (conning tower); парная к `часть_hk_tank_плазма_пушка_1`.

По terminator.fandom.com/wiki/HK-Tank: «...two steel "arms" equipped with twin-barreled directional plasma cannons». Каталог kaiju.wikidot.com для HK Tank '84/'91 фиксирует вооружение «Two plasma cannons, sensors» при высоте машины 32 ft (≈10 м) и массе ≈60 т. Технология относится к плазменному оружию Future War (terminator.fandom.com/wiki/Plasma_weaponry): directed-energy weapon, стреляющий болтом/потоком плазмы, без традиционных боеприпасов.

Родитель: `izdelie_SkyNet-HKTank` (подсистема: встроенное_оружие).

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
| материал | w-ni-fe | — | canon |
| тип вооружения | two plasma cannons (на стальных «руках») | — | terminator.fandom.com/wiki/HK-Tank |
| машина-носитель | HK Tank '84/'91: h≈10 м, ≈60 т | — | kaiju.wikidot.com/wiki:hunter-killer |

## Принцип работы

Capacitor bank разряжается через plasma cell → сила Лоренца ускоряет плазму (directed-energy выстрел болтом плазмы). Реальный аналог физики ускорения плазмы — проект MARAUDER (Magnetically Accelerated Ring to Achieve Ultrahigh Directed Energy and Radiation) Лаборатории ВВС США: коаксиальный плазменный рельсотрон (plasma railgun), разгоняющий плазменное кольцо двумя параллельными электродами (en.wikipedia.org/wiki/Plasma_cannon → Plasma railgun).

## Состав

Промежуточная часть (уровень 2). Дочерних частей нет.

## Используемые материалы

- `w-ni-fe` → [`w-ni-fe.md`](../../материалы/w-ni-fe.md)

## Источники

- https://terminator.fandom.com/wiki/HK-Tank — «two steel "arms" equipped with twin-barreled directional plasma cannons»
- https://kaiju.wikidot.com/wiki:hunter-killer — HK Tank '84/'91: «Two plasma cannons, sensors», h 32 ft, ≈60 т
- https://terminator.fandom.com/wiki/Plasma_weaponry — плазменное оружие Future War (directed-energy)
- https://en.wikipedia.org/wiki/Plasma_cannon — реальная физика: MARAUDER (коаксиальный плазменный рельсотрон, USAF Research Laboratory)
- Декомпозиция: `izdelie_SkyNet-HKTank` (web search 2026-11-03)
- Материалы: реальные данные/материалы/
