---
id: izdelie_mikroreaktor_deleniya
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: микро_реактор_деления
стандарты: 
  - IAEA SSR-4
  - 10 CFR 50
исследовательская_группа: westinghouse_oklo
родитель: null
дочерние_части:
  - часть_mikroreaktor_deleniya_fuel
  - часть_mikroreaktor_deleniya_moderator
  - часть_mikroreaktor_deleniya_heat_exchanger
  - часть_mikroreaktor_deleniya_control_rods
  - часть_mikroreaktor_deleniya_shielding
  - часть_mikroreaktor_deleniya_vessel
  - часть_mikroreaktor_deleniya_coolant
материалы_частей:
  - часть: часть_mikroreaktor_deleniya_fuel
    материал: uo2_pellets
    форма: топливные_пебблы_triso
    доля_массы: 0.095
  - часть: часть_mikroreaktor_deleniya_moderator
    материал: graphite
    форма: монолитный_замедлитель_микрореактора
    доля_массы: 0.38
  - часть: часть_mikroreaktor_deleniya_heat_exchanger
    материал: inconel_625
    форма: химическая_промышленность
    доля_массы: 0.15
  - часть: часть_mikroreaktor_deleniya_shielding
    материал: concrete_barite
    форма: боковая_защита_микрореактора
    доля_массы: 0.38
  - часть: часть_mikroreaktor_deleniya_vessel
    материал: stainless_steel_316
    форма: поликристаллический_прокат
    доля_массы: 0.19
  - часть: часть_mikroreaktor_deleniya_coolant
    материал: sodium
    форма: натриевые_heat_pipes_микрореактора
    доля_массы: 0.0475
технологии_частей:
  - часть: часть_mikroreaktor_deleniya_fuel
    технология: vakuumnoe_spekanie
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: uo2
        роль: обрабатываемый
  - часть: часть_mikroreaktor_deleniya_moderator
    технология: otzhig
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: graphite
        роль: обрабатываемый
  - часть: часть_mikroreaktor_deleniya_heat_exchanger
    технология: diffuzionnaya_svarka
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: inconel_625
        роль: обрабатываемый
  - часть: часть_mikroreaktor_deleniya_shielding
    технология: betonirovanie_baritovyh_moduley
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: concrete_barite
        роль: обрабатываемый
  - часть: часть_mikroreaktor_deleniya_vessel
    технология: ebw
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: ss_316l
        роль: обрабатываемый
  - часть: часть_mikroreaktor_deleniya_coolant
    технология: izgotovlenie_natrievyh_heat_trub
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: sodium
        роль: обрабатываемый

наследуемые_материалы:
  - материал: uo2
    форма: топливные_пебблы_triso
    суммарная_доля_массы: 0.095
    источники_частей:
      - часть_mikroreaktor_deleniya_fuel
  - материал: graphite
    форма: монолитный_замедлитель_микрореактора
    суммарная_доля_массы: 0.38
    источники_частей:
      - часть_mikroreaktor_deleniya_moderator
  - материал: inconel_625
    форма: химическая_промышленность
    суммарная_доля_массы: 0.15
    источники_частей:
      - часть_mikroreaktor_deleniya_heat_exchanger
  - материал: concrete_barite
    форма: боковая_защита_микрореактора
    суммарная_доля_массы: 0.38
    источники_частей:
      - часть_mikroreaktor_deleniya_shielding
  - материал: ss_316l
    форма: поликристаллический_прокат
    суммарная_доля_массы: 0.19
    источники_частей:
      - часть_mikroreaktor_deleniya_vessel
  - материал: sodium
    форма: натриевые_heat_pipes_микрореактора
    суммарная_доля_массы: 0.0475
    источники_частей:
      - часть_mikroreaktor_deleniya_coolant
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
          min: 1000
          max: 50000
          nominal: 10000
  габариты_mm:
          l: 5000
          w: 2000
          h: 2500
  выработка_энергии_W:
          min: 1000000
          max: 50000000
          nominal: 5000000
  выработка_тепла_W:
          min: 2000000
          max: 100000000
          nominal: 15000000
наследуемые: {}
дополнительные: 
  T_жизни_лет: 20
  мощность_MWe: 5
  источник: Westinghouse eVinci / Oklo Aurora
дата_создания: 2026-11-03
дата_обновления: 2026-11-07
источник: user_input
источник_разбора: веб-верификация
источник_url: https://www.nrc.gov/docs/ML2305/ML23053A351.pdf
источник_дата: 2026-11-07
---
# Изделие: Микрореактор деления

## Описание

Микрореактор деления eVinci-класса (5 МВт э / 15 МВт т, HALEU TRISO + натриевые тепловые трубы)

Полное наименование (как в CSV): `Микрореактор деления (Kilopower / KRUSTY)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
| выработка энергии | 5000000 | W | eVinci — 5 MWe microreactor (NRC ML23053A351; IAEA ARIS eVinci, 2024) |
| выработка тепла | 15000000 | W | eVinci — 15 MWt core, 19.75 % HALEU TRISO (IAEA ARIS; NRC ML23053A351) |
| категория | энергетика | — | canon |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

Изделие верхнего уровня, 7 частей (уровень 2): fuel (TRISO HALEU, 15 МВт(т) — вся мощность деления), moderator (ядерный графит IG-110), heat_exchanger (PCHE 316L), control_rods (B₄C), shielding (баритобетон), vessel (SS 316L), coolant (натриевые тепловые трубы). Энергобаланс: 15 МВт(т) в топливе → 5 МВт(э) в замкнутом цикле Брайтона (КПД ~33 %).

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Гетерогенная активная зона: TRISO-пебблы HALEU (19.75 % U-235) в монолитной графитовой кладке IG-110, тепло отводится натриевыми тепловыми трубами к печатному теплообменнику (PCHE) и преобразуется в электричество замкнутым циклом Брайтона (sCO₂/гелий). Вся тепловая мощность деления 15 МВт(т) депонируется в топливе; 5 МВт(э) — после преобразования с КПД ~33 % (NRC ML23053A351, IAEA ARIS). Управление реактивностью — B₄C стержни с падающей гравитацией SCRAM; защита — баритобетонные модули; корпус SS 316L герметизирует инертную атмосферу (без насосов, полностью пассивный теплоотвод — 8+ лет кампании без перегрузки).

## Источники

- NRC ML23053A351, «eVinci Microreactor Overview» (Westinghouse, 2023): 5 MWe/15 MWt, тепловые трубы, TRISO: https://www.nrc.gov/docs/ML2305/ML23053A351.pdf (проверено 2026-11-07)
- IAEA ARIS, «eVinci» (2024): 5 MWe/15 MWth, HALEU 19.75 %, closed Brayton cycle: https://aris.iaea.org (проверено 2026-11-07)
- Westinghouse eVinci Microreactor (официальная страница): https://westinghousenuclear.com/innovation/evinci-microreactor (проверено 2026-11-07)
- CSV: `начальные данные_final.csv` (пользовательский ввод)

---


## Декомпозиция

```mermaid
graph TD
    mikroreaktor_deleniy["izdelie_mikroreaktor_deleniya"]
    mikroreaktor_deleniya_fue["часть_mikroreaktor_deleniya_fuel"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_fue
    mikroreaktor_deleniya_mod["часть_mikroreaktor_deleniya_moderator"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_mod
    mikroreaktor_deleniya_hea["часть_mikroreaktor_deleniya_heat_exchanger"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_hea
    mikroreaktor_deleniya_con["часть_mikroreaktor_deleniya_control_rods"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_con
    mikroreaktor_deleniya_shi["часть_mikroreaktor_deleniya_shielding"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_shi
    mikroreaktor_deleniya_ves["часть_mikroreaktor_deleniya_vessel"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_ves
    mikroreaktor_deleniya_coo["часть_mikroreaktor_deleniya_coolant"]
    mikroreaktor_deleniy --> mikroreaktor_deleniya_coo
```
