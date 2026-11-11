---
id: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core
тип: сборка
категория: машиностроение
уровень_иерархии: промежуточный
уровень_номер: 2
подсистема: приводная_система
подтип: основной_элемент
стандарты:
- ISO 9001
исследовательская_группа: null
родитель: izdelie_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov
дочерние_части:
- часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_silovye_provoda
- часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_signalnye_provoda
- часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_ekran
- часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_zashchitnaya_obmotka
материалы_частей:
- часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_silovye_provoda
  материал: copper
  форма: шины_и_заземление
  доля_массы: 0.53
- часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_signalnye_provoda
  материал: copper
  форма: шины_и_заземление
  доля_массы: 0.2
- часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_ekran
  материал: copper
  форма: теплосъём_и_экранирование
  доля_массы: 0.16
- часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_zashchitnaya_obmotka
  материал: tedlar_pet
  форма: tpt_классическая_двусторонняя
  доля_массы: 0.11
технологии_частей:
- часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_silovye_provoda
  технология: izolirovannye_emalyu
  доля_использования: 0.53
  материалы_для_процесса:
  - материал: copper
    роль: токоведущая_основа
  - материал: ptfe
    роль: изоляционный_слой
- часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_signalnye_provoda
  технология: izolirovannye_emalyu
  доля_использования: 0.2
  материалы_для_процесса:
  - материал: copper
    роль: токоведущая_основа
  - материал: ptfe
    роль: изоляционный_слой
- часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_ekran
  технология: galvanika
  доля_использования: 0.16
  материалы_для_процесса:
  - материал: copper
    роль: обрабатываемая_основа_оплётки
  - материал: tin
    роль: гальваническое_покрытие_лужение
- часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_zashchitnaya_obmotka
  технология: spiralnaya_navivka
  доля_использования: 0.11
  материалы_для_процесса:
  - материал: pet
    роль: лента_обмотки
наследуемые_материалы:
- материал: copper
  форма: шины_и_заземление
  суммарная_доля_массы: 0.73
  источники_частей:
  - часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_silovye_provoda
  - часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_signalnye_provoda
- материал: copper
  форма: теплосъём_и_экранирование
  суммарная_доля_массы: 0.16
  источники_частей:
  - часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_ekran
- материал: pet
  форма: tpt_классическая_двусторонняя
  суммарная_доля_массы: 0.11
  источники_частей:
  - часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_zashchitnaya_obmotka
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
  масса_kg: 0.45
  доля_массы_родителя: 0.5
  габариты_mm:
    l: 250
    w: 180
    h: 45
  выработка_энергии_W: 0
  выработка_тепла_W: 1
наследуемые: {}
дополнительные: {}
дата_создания: 2026-11-03
дата_обновления: 2026-11-07
источник: web_search
источник_разбора: веб-верификация
источник_url: https://en.wikipedia.org/wiki/Cable_harness
источник_дата: 2026-11-05
масштабируемость:
  режим: фиксированная
  параметры:
  - имя: количество_единиц
    диапазон:
    - 1
    - 1
    единица: шт
  пределы:
    max_единиц_в_системе: 1
  закон_масштабирования: фиксированный — деталь не масштабируется (leaf node в составе
    родительского изделия)
  ограничивающие_части: []
---


# Часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core

## Описание

Жгут токопроводящих изолированных проводов — медные жилы с ПВХ/силиконовой изоляцией, экранированные ветки для силовых и сигнальных цепей. Референсное исполнение — жгут проводов (250×180×45, медь в изоляции). Габариты 250×180×45 мм, масса 0.45 кг — паспортные данные (жгут проводов). Материал — copper: медь Cu-ETP (C11000, проводниковая). Ядро жгута декомпозировано на 4 ветки: силовые провода (0.24 кг), сигнальные провода (0.09 кг), экранирующая оплётка (0.07 кг), защитная обмотка Tedlar/PET (0.05 кг) — реальная структура жгута (igus servo cables, Glenair braided shielding).

Родитель: `izdelie_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov` (подсистема: приводная_система).

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | приводная_система | — | canon |
| подтип | основной_элемент | — | canon |
| масса | 0.45 | kg | жгут проводов (250×180×45, медь в изоляции) |
| доля массы родителя | 0.5 | — | canon |
| габариты (Д×Ш×В) | 250×180×45 | mm | жгут проводов (250×180×45, медь в изоляции) |
| выработка энергии | 0 | W | canon |
| выработка тепла | 1 | W | canon |
| материал | copper / tedlar_pet | — | ветки ядра (медные жилы / ПЭТ-чулок) |

## Принцип работы

Распределение питания и сигналов по приводной системе: силовые ветки держат рабочий ток приводов (омический нагрев ~0.6 Вт), сигнальные витые пары передают обратную связь, экранирующая оплётка замыкает наводки на корпус, защитная обмотка стягивает и защищает пучок.

## Состав

Составная часть (уровень 2), декомпозирована на 4 ветки (уровень 3):

- `часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_silovye_provoda` — силовые провода (0.24 кг, 250×40×20)
- `часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_signalnye_provoda` — сигнальные провода (0.09 кг, 250×30×15)
- `часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_ekran` — экранирующая оплётка (0.07 кг, 250×35×8)
- `часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_zashchitnaya_obmotka` — защитная обмотка Tedlar/PET (0.05 кг, 250×75×10)

Σ масс = 0.45 кг = масса ядра; все ветки помещаются в габарит 250×180×45.

## Используемые материалы

- `copper` → [`copper.md`](../../../../материалы/copper.md) — медь (проводниковая)
- `tedlar_pet` → [`pet.md`](../../../../материалы/pet.md) — ПЭТ (защитный чулок)

## Источники

- жгут проводов (250×180×45, медь в изоляции) — https://en.wikipedia.org/wiki/Cable_harness (обращение 2026-11-05)
- Канон: декомпозиция `izdelie_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov` (web search 2026-11-03)
- Материалы: реальные данные/материалы/

## Декомпозиция

```mermaid
graph TD
    core["часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core"]
    silovye_provoda["часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_silovye_provoda"]
    signalnye_provoda["часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_signalnye_provoda"]
    ekran["часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_ekran"]
    zashchitnaya_obmotka["часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_zashchitnaya_obmotka"]
    core --> silovye_provoda
    core --> signalnye_provoda
    core --> ekran
    core --> zashchitnaya_obmotka
```

