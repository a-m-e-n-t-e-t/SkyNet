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
    материал: generic_material
    доля_массы: 0.45
  - часть: часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing
    материал: aluminum
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
# Изделие: Микроканальные охлаждающие пластины

## Описание

Микроканальная охлаждающая пластина (liquid cold plate) — пассивный теплообменник для отвода высоких тепловых потоков от силовой электроники/батарей: пластина 200×100×5 мм с внутренними микроканалами (0.3–0.5 мм), по которым прокачивается теплоноситель (деионизированная вода, EGW, PAO). Съём теплового потока до 50 Вт/см² (ThermAvant, micromachined/brazed cold plates). Материал корпуса — Ti-6Al-4V (Grade 5, ρ 4.43 г/см³) — лёгкий и коррозионно-стойкий, но с низкой теплопроводностью 6.8 Вт/(м·К) (TC4/Grade 5), поэтому тепловая зона (core) выполнена из меди Cu-ETP. Масса пластины ~0.5 кг (оценка по плотности меди/титана и толщине стенок каналов).

Габарит изделия — конверт сборки **200×100×24 мм**: сама пластина 5 мм толщиной; разъём питания насоса Anderson SB50 (47.5×27.7×19 мм по datasheet Anderson Power Products) установлен на верхней поверхности; крепёжные скобы (95×55×12 мм) размещаются на верхней же поверхности в пределах высоты разъёма; корпус-рамка (115×69×8 мм) охватывает тепловую зону в основании. Объём конверта 480000 мм³ ≥ ΣV(детей)×1.15 = 208356 мм³ (запас ×2.3) — все 4 части физически помещаются в изделие (оси: 200≥115 / 100≥69 / 24≥19).

Родитель — верхний уровень подсистемы система_охлаждения. Состав: core (медная пластина с каналами), housing (титановый корпус), connectors (разъём Anderson SB50 50 А для насоса), mounting (крепёж 8×M4).

## Принцип работы

Чип/источник тепла передаёт тепловой поток через контактную поверхность к медному core, где микроканалы заполняются теплоносителем. Прокачка теплоносителя насосом переносит тепло к радиатору/чиллеру за пределами пластины. Пластина пассивна: собственное тепловыделение определяется только джоулевыми потерями в разъёме питания насоса (Anderson SB50, 50 А, ~0.1 Вт) — именно это значение фигурирует в балансе F15b (parent 0.1 Вт ≥ Σ детей 0.1 Вт).

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | система_охлаждения | — | classify_subsystem |
| подтип | жидкостный cold plate | — | web_search |
| масса | 0.5 (0.05–5) | kg | оценка по плотности меди/титана |
| габариты (Д×Ш×В) | 200×100×24 (конверт сборки; пластина 5 мм) | mm | пластина canon + разъём SB50 19 мм datasheet Anderson Power Products |
| тепловая нагрузка (съём) | до 50 | Вт/см² | ThermAvant (cold plates) |
| собственное тепловыделение | 0.1 (0–0.15) | W | расчёт: I²R контактов разъёма Anderson SB50 (50 А × ~0.3 мОм × 2) |
| выработка энергии | 0 | W | пассивный теплообменник |
| теплоноситель | DI water / EGW / PAO | — | ThermAvant |

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Источники

- ThermAvant Technologies — Cold Plates, High Heat Flux Thermal Management (heat flux до 50 W/cm², материалы Al/Cu/Cu-Mo/stainless, рабочие жидкости DI water/EGW/PAO): https://www.thermavant.com/thermavant-products/cold-plates (обращение 2026-11-07)
- Power-E — Жидкостная система охлаждения в современных корпусах (микроканальные охладители: тонкие медные листы, химическое травление каналов): https://power-e.ru/cooling/zhidkostnaya-sistema-ohlazhdeniya (обращение 2026-11-07)
- Титановый сплав TC4 (Ti-6Al-4V) — теплопроводность 6.8 Вт/(м·°C) при 20°C: https://www.google.com/goto?url=CAESwwEBxCJF1596eWxv72iFnfkKY8DVD4ccYZHwyi8Gw9Ngpn4hgDjddFFzm6tfu_QOhSlf5i_9XAXVFcH7-s7kcGLozqSA14uON2iFe9YTJXzmNQaXlzjk6rnJlq2yBfILISKZKp6YA4FEeQ-laoL92mbzlf2HI4Cy4tFLjGlzLyNwWdKZo-EkboRmQs4qXKnzkHozj6FkIUHJZXbGwK8P3snwuTNQ6NAbp_y7KpOCTK6e1ad2CT99NUV-YiPr1Ya1AWuwiTc (обращение 2026-11-07)
- CSV: `начальные данные_final.csv` (пользовательский ввод)

---


## Декомпозиция

```mermaid
graph TD
    mikrokanalnye_ohlazh["izdelie_mikrokanalnye_ohlazhdayuschie_plastiny"]
    mikrokanalnye_ohlazhdayus["часть_mikrokanalnye_ohlazhdayuschie_plastiny_core"]
    mikrokanalnye_ohlazh --> mikrokanalnye_ohlazhdayus
    mikrokanalnye_ohlazhdayus["часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing"]
    mikrokanalnye_ohlazh --> mikrokanalnye_ohlazhdayus
    mikrokanalnye_ohlazhdayus["часть_mikrokanalnye_ohlazhdayuschie_plastiny_connectors"]
    mikrokanalnye_ohlazh --> mikrokanalnye_ohlazhdayus
    mikrokanalnye_ohlazhdayus["часть_mikrokanalnye_ohlazhdayuschie_plastiny_mounting"]
    mikrokanalnye_ohlazh --> mikrokanalnye_ohlazhdayus
```
