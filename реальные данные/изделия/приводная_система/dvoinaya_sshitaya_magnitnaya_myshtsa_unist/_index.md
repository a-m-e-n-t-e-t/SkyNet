---
id: izdelie_dvoinaya_sshitaya_magnitnaya_myshtsa_unist
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: приводная_система
подтип: магнитная_мышца
стандарты: []
исследовательская_группа: brigham_young_university
родитель: null
дочерние_части:
  - часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_magnets
  - часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_coil
  - часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_spring
  - часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_housing
материалы_частей:
  - часть: часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_magnets
    материал: ndfeb
    форма: магнитные_актуаторы_и_мышцы
    доля_массы: 0.475
  - часть: часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_coil
    материал: copper
    форма: обмотки_электрических_машин
    доля_массы: 0.18
  - часть: часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_spring
    материал: spring_steel
    форма: a228_музыкальная_проволока
    доля_массы: 0.19
технологии_частей:
  - часть: часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_magnets
    технология: vakuumnoe_spekanie
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: ndfeb
        роль: спекаемый_порошок
      - материал: argon
        роль: защитная_атмосфера
  - часть: часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_coil
    технология: izolirovannye_emalyu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: copper
        роль: изолируемый_проводник
  - часть: часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_spring
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: spring_steel
        роль: обрабатываемая_заготовка
наследуемые_материалы:
  - материал: ndfeb
    суммарная_доля_массы: 0.475
    источники_частей:
      - часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_magnets
  - материал: copper
    суммарная_доля_массы: 0.18
    источники_частей:
      - часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_coil
  - материал: spring_steel
    суммарная_доля_массы: 0.19
    источники_частей:
      - часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_spring
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
          min: 0.01
          max: 1
          nominal: 0.1
  габариты_mm:
          l: 210
          w: 160
          h: 110
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.01
          max: 1
          nominal: 1.0
  обоснование_габаритов: 'сборочная огибающая: корпус (housing) 200×150×100 мм задаёт все три оси — внутри магнитный слой 100×20×5 мм, катушка 100×20×8 мм, пружина 48×12×12 мм; итог 210×160×110 мм = корпус + припуск 10 мм на сторону (монтажные лапы, кабельные вводы катушки, тепловые зазоры привода); V=210×160×110=3 696 000 мм³ ≥ ΣV детей×1.15=3 487 849 мм³ (ΣV детей=3 032 912 мм³ — housing 3 000 000 + coil 16 000 + magnets 10 000 + spring 6 912), запас +6.0 %; оси: l 210≥200, w 160≥150, h 110≥100'
наследуемые: {}
масштабируемость:
  режим: масштабируемая
  параметры: [масса_kg, выработка_тепла_W]
  пределы:
    min:
      масса_kg: 0.01
      выработка_тепла_W: 0.01
    max:
      масса_kg: 1
      выработка_тепла_W: 1
  шаг: {}
  закон_масштабирования:
    масса_kg: "линейный по объёму активной зоны (NdFeB-композит с двойной сшивкой + катушка + пружина): m ∝ V_активной_зоны; номинал 0.1 кг — модуль UNIST-класса в корпусе 200×150×100 мм (референс Kim 2026: мышца 1.25 г, нагрузка 5 кг)"
    выработка_тепла_W: "Джоулев нагрев катушки P = I²R (эмалированная медь, класс изоляции до 220 °C); номинал 1.0 Вт — режим переключения мягкий↔жёсткий (AFM 2025, DOI 10.1002/adfm.202516218)"
  ограничивающие_части:
    - часть: часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_magnets
      предел: магнитная тяга и деформация ∝ объёму NdFeB-композита (сокращение до 86.4 % в двойной сшитой матрице, Kim 2026 ADFM); рост хода/силы → рост объёма магнитного слоя
    - часть: часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_coil
      предел: I²R нагрев ограничивает ток удержания (изоляция эмаль-провода Class 220); теплосъём корпуса задаёт непрерывный режим
    - часть: часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_spring
      предел: жёсткость возвратной пружины (A228 музыкальная проволока) задаёт противодействие и линейность хода 30 мм
    - часть: часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_housing
      предел: огибающая 200×150×100 мм и жёсткость корпуса при нагрузке 100 Н; укрупнение модуля требует пересчёта теплового баланса
дополнительные: 
  сила_Н: 100
  ход_мм: 30
  источник: BYU UNIST magnetic muscle research
дата_создания: 2026-11-03
дата_обновления: 2026-11-09
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: двойная сшитая магнитная мышца UNIST

## Описание

двойная сшитая магнитная мышца UNIST

Полное наименование (как в CSV): `двойная сшитая магнитная мышца UNIST`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
| категория | прочее | — | — |
| сила | 100 | Н | canon (дополнительные) |
| ход | 30 | мм | canon (дополнительные) |
| выработка тепла (режим переключения) | 1.0 | W | Joule-нагрев катушки «до ~1 Вт», AFM 2025 (DOI 10.1002/adfm.202516218); min 0.01 — простой без тока, max 1.0 — пиковое переключение |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

Изделие верхнего уровня (уровень 1). Дочерние части:

- `часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_magnets` — магнитоактивный композитный слой (NdFeB/полимер с двойной сшивкой), 100×20×5 мм, доля массы 0.475;
- `часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_coil` — катушка Joule-подогрева (эмалированная медь), 100×20×8 мм, доля массы 0.18;
- `часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_spring` — возвратная пружина (spring_steel), 48×12×12 мм, доля массы 0.19;
- `часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_housing` — корпус (неделимый), 200×150×100 мм.

Тепловой баланс: Σ(выработка_тепла детей) = 1.0 Вт (только катушка — единственный источник тепла; магнитный слой, пружина и корпус пассивны) ≤ выработка_тепла родителя 1.0 Вт.

## Используемые технологии

- `vakuumnoe_spekanie` — спекание NdFeB-порошка магнитного слоя (в аргоновой атмосфере, 1050–1080 °C); связь зафиксирована в технологии_частей.
- `izolirovannye_emalyu` — эмалирование (изоляция) медного обмоточного провода катушки Joule-подогрева (magnet wire, изоляция до Class 220).
- `frezervanie_chpu` — ЧПУ-фрезерование заготовки возвратной пружины (spring_steel, полоса A228).

## Используемые материалы

- `ndfeb` (форма: магнитные_актуаторы_и_мышцы) — NdFeB-композит магнитоактивного слоя (ключ из ndfeb.md варианты_по_применению)
- `copper` (форма: обмотки_электрических_машин) — обмоточный провод катушки (ключ из copper.md)
- `spring_steel` (форма: a228_музыкальная_проволока) — возвратная пружина (ASTM A228, ключ из spring_steel.md)
- `al_6061-t6` — корпус (дочерний файл)

## Принцип работы

Мышца — магнитоактивный композитный привод (NdFeB микрочастицы в матрице полимера с памятью формы с двойной сшивкой, UNIST, DOI 10.1002/adfm.202516218). Внешнее магнитное поле создаёт тягу в магнитном слое — сокращение до 86.4% длины, плотность работы 1150 кДж/м³. Переключение мягкий↔жёсткий — термическое: катушка рассеивает Joule-тепло (~1 Вт, I²R), нагревая композит до температуры разрыва обратимых физических связей двойной сети — мышца переходит в мягкое состояние (растяжение до 12×); при отключении тока связи восстанавливаются — мышца жёстко держит нагрузку до 5 кг. Пружина возвращает ход, корпус защищает композит.

## Источники

- S. Kim et al., «Soft Magnetic Artificial Muscles with High Work Density and Actuation Strain via Dual Cross-Linking Design», Advanced Functional Materials (Wiley), DOI: https://doi.org/10.1002/adfm.202516218 (онлайн 2025-09-07) — сокращение 86.4%, плотность работы 1150 кДж/м³, NdFeB в матрице SMP, переключение тепловым стимулом (разрыв/восстановление физических связей), дата обращения 2026-11-08
- Chosun Biz, «UNIST develops artificial muscle 30 times stronger than human muscle» (2025-09-17): https://biz.chosun.com/en/en-science/2025/09/17/S4PZHTK7JZFHRBJR2T2GKNJFN4 — масса мышцы 1.25 г, нагрузка 5 кг, растяжение до 12×, проф. Hoon Eui Jeong (UNIST Dept. of Mechanical Engineering), дата обращения 2026-11-08
- TechXplore, «Artificial muscle can switch from soft to rigid to support over 4,000 times its own weight» (2025-10-13): https://techxplore.com/news/2025-10-artificial-muscle-soft-rigid-weight.html — механик переключения мягкий/жёсткий, дата обращения 2026-11-08
- CSV: `начальные данные_final.csv` (пользовательский ввод)

---


## Декомпозиция

```mermaid
graph TD
    dvoinaya_sshitaya_ma["izdelie_dvoinaya_sshitaya_magnitnaya_myshtsa_unist"]
    dvoinaya_sshitaya_magnitn["часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_magnets"]
    dvoinaya_sshitaya_ma --> dvoinaya_sshitaya_magnitn
    dvoinaya_sshitaya_magnitn["часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_coil"]
    dvoinaya_sshitaya_ma --> dvoinaya_sshitaya_magnitn
    dvoinaya_sshitaya_magnitn["часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_spring"]
    dvoinaya_sshitaya_ma --> dvoinaya_sshitaya_magnitn
    dvoinaya_sshitaya_magnitn["часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_housing"]
    dvoinaya_sshitaya_ma --> dvoinaya_sshitaya_magnitn
```
