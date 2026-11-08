---
id: часть_minigun_m134_core_barrels
тип: изделие
категория: машиностроение
уровень_иерархии: неделимый
уровень_номер: 3
подсистема: встроенное_оружие
подтип: стволы
стандарты:
  - ISO 9001
  - MIL-STD-810
исследовательская_группа: null
родитель: часть_minigun_m134_core
дочерние_части: []
материалы_частей:
  - часть: часть_minigun_m134_core_barrels
    материал: stal_st3
    форма: строительные_конструкции_и_крепёж
    доля_массы: 1.0

технологии_частей:
  - часть: часть_minigun_m134_core_barrels
    технология: honing_plateau_finish
    доля_использования: 1.0
    # v9.56: канал ствола — глубокое сверление (gun drilling) + хонингование
    # перед нанесением хромового покрытия (Gül, «Specialized Processes in the
    # Manufacturing of Military Firearm Barrels»: deep hole drilling, honing,
    # straightening, broaching, chrome plating, heat treatment).
    материалы_для_процесса:
      - материал: stal_st3
        роль: обрабатываемый
  - часть: часть_minigun_m134_core_barrels
    технология: galvanika
    доля_использования: 1.0
    # v9.56: хромирование канала ствола (hard chrome lining) — стандарт военного
    # производства: электролитическое покрытие канала твёрдым хромом против
    # эрозии/коррозии (SERDP-ESTCP «Chromium Elimination in Medium Caliber Gun
    # Barrels»: hexavalent chrome plating — действующий процесс; практичум
    # barrel making 101: равномерная толщина hard chrome по нарезам).
    материалы_для_процесса:
      - материал: stal_st3
        роль: хромируемый_канал

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
  масса_kg: 4.2
  доля_массы_родителя: 0.35
  габариты_mm:
    l: 558.8
    w: 150
    h: 150
  выработка_энергии_W: 0
  выработка_тепла_W: 0.6
наследуемые: {}
дополнительные: {}
дата_создания: 2026-11-07
дата_обновления: 2026-11-08
источник: web_search
источник_разбора: веб-верификация
источник_url: https://en.wikipedia.org/wiki/M134_Minigun
источник_дата: 2026-11-07
---

# Часть: часть_minigun_m134_core_barrels

## Описание

Пакет 6 стволов 7.62×51мм NATO (M134: 559–686 мм, хромированный канал, скорострельность до 6000 выстр/мин на пакет). Каждый ствол с собственным затворным блоком, циклируется вращением вокруг центральной оси. Референс — General Dynamics M134 spec (barrel cluster).

Родитель: `часть_minigun_m134_core` (подсистема: встроенное_оружие).

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | встроенное_оружие | — | canon |
| подтип | стволы | — | canon |
| масса_kg | 4.2 | кг | General Dynamics M134 spec / Wikipedia |
| габариты_mm | 559×150×150 | мм | пакет 6 стволов по 558.8 мм (22 in), ширина/высота пакета ~150 мм |
| материал | stal_st3 | — | реальный материал |

## Используемые технологии

- [`honing_plateau_finish`](../../../../технологии/honing_plateau_finish.md) — хонингование канала ствола: глубокое сверление заготовки (gun drilling) и доводка канала перед хромированием (Gül: «deep hole drilling, honing, straightening, broaching, chrome plating, heat treatment» — стандарт военного производства стволов)
- [`galvanika`](../../../../технологии/galvanika.md) — гальваническое хромирование канала (hard chrome lining): электролитическое нанесение твёрдого хрома на канал ствола против эрозии и коррозии; описание стволов M134 прямо указывает «хромированный канал» (Wikipedia M134); SERDP-ESTCP подтверждает гальваническое hexavalent chrome plating как действующий процесс для стволов среднего калибра

## Источники

- SERDP-ESTCP WP-1502, «Chromium Elimination in Medium Caliber Gun Barrels» (hexavalent chrome plating стволов): <https://serdp-estcp.mil/projects/details/fad914b6-1e49-4e9b-9de2-f9a86d256aea>
- Gül, «Specialized Processes in the Manufacturing of Military Firearm Barrels» (deep hole drilling → honing → broaching → chrome plating → heat treatment): <https://www.linkedin.com/pulse/specialized-processes-manufacturing-military-firearm-barrels-g%C3%BCl-xpuhf>
- Practical Machinist, «Barrel Making 101» (равномерный слой hard chrome по нарезам): <https://www.practicalmachinist.com/forum/threads/barrel-making-101.224668>
- Wikipedia: M134 Minigun (6 стволов 7.62×51, хромированный канал, 2000–6000 выстр/мин): <https://en.wikipedia.org/wiki/M134_Minigun>

## Иерархия

```mermaid
graph TD
    core["часть_minigun_m134_core"]
    barrels["часть_minigun_m134_core_barrels"]
    core --> barrels
```
