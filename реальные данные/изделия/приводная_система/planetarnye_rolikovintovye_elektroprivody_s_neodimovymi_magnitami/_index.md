---
id: izdelie_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: приводная_система
подтип: планетарный_роликовинт
стандарты: 
  - DIN 69051
исследовательская_группа: gsk_rollvis
родитель: null
дочерние_части:
  - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_screw
  - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_rollers
  - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_nut
  - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_bearings
  - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_seals
  - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_housing
материалы_частей:
  - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_screw
    материал: bearing_steel_52100
    форма: направляющие_и_шпиндели
    доля_массы: 0.38
  - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_rollers
    материал: bearing_steel_52100
    форма: тела_качения_роликовинтовых_передач
    доля_массы: 0.19
  - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_nut
    материал: bearing_steel_52100
    форма: гайки_роликовинтовых_передач
    доля_массы: 0.38
  - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_bearings
    материал: stainless_steel_440c
    форма: шарики_и_тела_качения_подшипников
    доля_массы: 0.09
технологии_частей:
  - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_screw
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: 100cr6
        роль: обрабатываемый
  - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_rollers
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: 100cr6
        роль: обрабатываемый
  - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_nut
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: 100cr6
        роль: обрабатываемый
  - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_bearings
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: 100cr6
        роль: обрабатываемый
наследуемые_материалы:
  - материал: 100cr6
    суммарная_доля_массы: 0.85
    источники_частей:
      - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_screw
      - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_nut
      - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_bearings
  - материал: inconel_718
    суммарная_доля_массы: 0.19
    источники_частей:
      - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_rollers
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
          min: 0.5
          max: 50
          nominal: 5
  габариты_mm:
          l: 420
          w: 100
          h: 470
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 1
          max: 100
          nominal: 20
наследуемые: {}
масштабируемость:
  режим: масштабируемая
  параметры:
    - масса_kg
    - выработка_тепла_W
  пределы:
    min:
      масса_kg: 0.5
      выработка_тепла_W: 1
    max:
      масса_kg: 50
      выработка_тепла_W: 100
  шаг: {}
  закон_масштабирования:
    масса_kg: 'масштабирование по типоразмеру винта DIN 69051 (d 10–120 мм, L 100–2000 мм): масса ∝ d²·L — номинал 5 кг (винт 400×20×20 мм + гайка + корпус-гильза 90×90×450 мм); max 50 кг — крупный привод (винт 120 мм × 2000 мм)'
    выработка_тепла_W: 'P_тепло = P_мех·(1−η)/η при КПД роликовинтовой пары 85–95 % (DIN 69051): номинал 20 Вт при M_ном 100 Нм и V_линейная 1000 мм/с в режиме 20 % ПВ; min 1 Вт — микроприводы (d винта 10 мм, эпизодический режим); max 100 Вт — непрерывный режим крупного типоразмера'
  ограничивающие_части:
    - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_screw
      предел: 'винт 400×20×20 мм из закалённой стали 60–64 HRC: контактная усталость дорожек качения (Hertz >2 ГПа) лимитирует осевую силу и линейную скорость; типоразмеры DIN 69051 d 10–120 мм'
    - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_nut
      предел: 'гайка 60×60×40 мм с планетарной группой роликов: соосность и трение группы задают КПД 85–95 % и тепловой баланс привода; перегрев гайки >80 °C снижает ресурс смазки'
    - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_bearings
      предел: 'подшипниковый узел 25×52×15 мм: осевая preload и dn-лимит (диаметр×частота вращения) ограничивают скорость вращения винта и осевую жёсткость'
дополнительные: 
  M_ном_Нм: 100
  V_линейная_мм_с: 1000
  обоснование_габаритов: 'огибающая привода: корпус-гильза housing 90×90×450 мм (вертикальная компоновка по DIN 69051) — внутри винт screw 400×20×20 мм с профилем резьбы качения, гайка 60×60×40 мм, ролики 45×15×15 мм (планетарная группа), подшипниковый узел 25×52×15 мм, уплотнения 30×30×5 мм; по каждой оси огибающая = max(дети) + 20 мм монтажного зазора на крепёжные лапы, торцевые крышки и кабельный ввод датчика положения; V=420×100×470=19 740 000 мм³ ≥ ΣV детей×1.15=4 580 594 мм³ (ΣV=3 983 125 мм³ — housing 3 645 000 + screw 160 000 + nut 144 000 + bearings 19 500 + rollers 10 125 + seals 4 500), запас ×4.31; оси: l 420≥400 (screw), w 100≥90 (housing), h 470≥450 (housing)'
  источник: GSK / Rollvis planetary roller screw
дата_создания: 2026-11-03
дата_обновления: 2026-11-09
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: планетарные роликовинтовые электроприводы с неодимовыми магнитами

## Описание

планетарные роликовинтовые электроприводы с неодимовыми магнитами

Полное наименование (как в CSV): `планетарные роликовинтовые электроприводы с неодимовыми магнитами`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
| категория | прочее | — | — |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

Изделие верхнего уровня. Дочерние части не указаны (требуется декомпозиция).

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Требует описания на основе инженерного анализа.

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)

---


## Декомпозиция

```mermaid
graph TD
    planetarnye_rolikovi["izdelie_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami"]
    planetarnye_rolikovintovy["часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_screw"]
    planetarnye_rolikovi --> planetarnye_rolikovintovy
    planetarnye_rolikovintovy["часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_rollers"]
    planetarnye_rolikovi --> planetarnye_rolikovintovy
    planetarnye_rolikovintovy["часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_nut"]
    planetarnye_rolikovi --> planetarnye_rolikovintovy
    planetarnye_rolikovintovy["часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_bearings"]
    planetarnye_rolikovi --> planetarnye_rolikovintovy
    planetarnye_rolikovintovy["часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_seals"]
    planetarnye_rolikovi --> planetarnye_rolikovintovy
    planetarnye_rolikovintovy["часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_housing"]
    planetarnye_rolikovi --> planetarnye_rolikovintovy
```
