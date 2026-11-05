---
id: SkyNet-TX
# web_verification: terminator.fandom.com/wiki/T-X (2026-11-03) — "weighing in excess of 150 kilos"
тактико_технические_характеристики: 
  мобильность:
          максимальная_скорость_км_ч: 80
          масса_kg: 150
дочерние_части: 
  - часть_t_x_cpu
  - часть_t_x_эндоскелет
  - часть_t_x_топливная_ячейка_1
  - часть_t_x_плазма_пушка
  - часть_t_x_нанотех_инъектор
  - часть_t_x_рука_левая
  - часть_t_x_нога_левая
  - часть_t_x_сенсоры
  - часть_t_x_ткань_кожа
тип: модель_SkyNet
класс: гуманоидный
категория: жидкий_металл
тип_модели: гуманоидный
источник_происхождения: фильм
функции: ["инфильтрация", " assassination", "анти-терминатор"]
канон_источник: Terminator 3: Rise of the Machines (2003)
произведения: ["work_003", "work_043", "work_044"]
производитель: Скайнет
статус_реальности: canon
подтип_модели: стандартный
многослойная_броня:
  слои:
    - номер: 1
      материал: b4c  # B₄C керамика (внешний жертвенный)
      толщина_мм: {min: 2, target: 10}
    - номер: 2
      материал: ti6al4v  # Ti-6Al-4V (кин. слой)
      толщина_мм: {min: 2, target: 10}
    - номер: 3
      материал: uhmwpe_dyneema  # UHMWPE Dyneema (арамидный подслой)
      толщина_мм: {min: 2, target: 10}
  тип_брони: гуманоидный
  соответствует_типу_модели: true  # F74, max_mass_percent: 30, min_layers: 3
доступность: фантастический
expected_subsystems: ["вычислительная", "энергетическая", "каркас", "броня", "сенсоры", "приводная_система", "система_связи", "навигация", "система_питания", "система_передвижения"]
relations:
  successor_of: null
  variation_of: null
  hybrid_of: []
  paradigm_shift_from: null
реализация_промышленная: 
  - izdelie_halve
  - izdelie_kondensatory_keramicheskie
  - izdelie_sic_mosfet
  - izdelie_tverdooksidnyi_toplivnyi_element
  - izdelie_nasa_asc-e_srsc
  - izdelie_superkondensatory
  - izdelie_SkyNet-HKAerial
  - izdelie_SkyNet-Rev9
  - izdelie_SkyNet-Cameron
  - izdelie_metalinza
  - izdelie_mwir_nbn_640
  - izdelie_lidar_robosense_ac1
  - izdelie_hasel
  - izdelie_povorotnoe_uplotnenie
  - izdelie_elektroflyuidnye_volokna_mit
  - izdelie_radiatsionno-stoikii_neiromorfnyi_tmr
  - izdelie_razryvnye_mufty_iso_16028
  - izdelie_flat-face_couplings_iso_16028
реализация_ии: []
источник: web_search
источник_разбора: канон
ии_перепроектирован:
  статус: false
  верификация: []
---
# v9.31: структурные поля §12.4.1-§12.4.X — добавлены как placeholder
# Реальные значения будут заполнены через web_search для каждой модели.
требования_выживаемости: 
  эми_защита:
          уровень: hardened
          порог_импульса_В_м:
                      min: 50000
                      target: 100000
          экранирование: faraday_cage (endoskeleton как клетка Фарадея)
          фильтры_питания: true
          оптическая_развязка: true
  термобарьер:
          рабочий_диапазон_C:
                      min: -50
                      target: 60
          предел_C:
                      min: -196
                      target: 1500
  удар:
          ускорение_g:
                      min: 50
                      target: 200
          drop_высота_m: 5
  вибрация: mil-std-810h
  пулестойкость: 'малый калибр (9mm, 5.56mm) — стоп; .50 BMG — пробивает корпус'
маскировка_инфильтратора: 
  роль_модели: infiltrator (Terminatrix)
  тип: 'static_camouflage (живая ткань + эндоскелет, как T-850)'
  shapeshift: ограниченный (миметический полисплав только для конечностей)
  nanotech: true
  сканирование_ДНК: true
тактико_технические_характеристики: 
  мобильность:
          максимальная_скорость_км_ч: 80
          масса_кг: 150
  cpu: 'Neural Net CPU (как T-850, но улучшенный)'
  питание: 2 plasma-ячейки
  вооружение: встроенная плазма-пушка + нанотехнологический инъектор (canon T3)
защита_от_собственной_радиации: неприменимо (без RTG); T-800 использует 2 водородных топливных элементов
кибербезопасность: 
  аппаратные_меры:
          HSM: true
          secure_boot: true
          TPM: true
          anti_tamper: zeroization
  iff: SkyNet IFF v3.1 (transponder 1090 MHz + crypto)
  шифрование: AES-256 + SkyNet proprietary
  skynet_protocol: Hive (collective consciousness) или Rogue (autonomous)
эмс_внутренняя: 
  экранирование_блока_cpu: inertial shock dampers вокруг Neural Net CPU
  фильтры_питания: кабель-силовой с фильтрами EMI
  размещение_антенн: внутри черепа (слуховые сенсоры)
компоновка_изделий: 
  cpu_расположение: 'череп (endoskull, в инерционных амортизаторах)'
  энергетика: 2 водородных топливных элемента в грудной клетке (позиция сердца)
  серводвигатели: axial drive motors + clavicular trailing links
  сенсоры: 'оптические (40,000 bit display, 15x zoom, IR), слуховые, внутренний хронометр'
трассировка_соединителей: frictionless bearings + hydraulic servo-actuated control
программное_обеспечение: 'Neural Net CPU + SkyNet OS (Hive mode по умолчанию, Rogue для автономных)'
единая_эми_стратегия: 'Standalone (T-800): прямой SkyNet link; Rogue mode: автономные единицы возвращаются для sync'
единая_герметичность: IP67 (живая ткань требует герметичности для предотвращения некроза); cryogenic storage в hybermatrix перед развёртыванием
сертификация_модели_целого: 
  тест_skyet: phase_5 (F70 metrics PASS)
  канон_верификация: 'источник_разбора=канон'
журнал_экземпляра: 
  serial_number: SkyNet-XXX-NNNN
  production_date: post-2026 (Skynet autonomous manufacturing)
  deployments: []
  kill_count: 0
  last_mission: null
утилизация_после_120_лет: 'T-800: 120 лет на 1 топливной ячейке (canon); после истощения — замена ячеек или разборка на запчасти'
экипаж_оператор: 0
промышленная_база: Skynet automated factory (Cyberdyne Systems / CRS)
alice_specs: ALICE sync protocol v9.31 (SkyNet hive-mind)
original_improved: canon
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
---
# SkyNet-TX

## Описание

T-X (T-Xa) — гибрид: эндоскелет T-900 покрыт миметическим полисплавом (как у T-1000); встроено плазменное оружие в руку; женская внешность; миссия: убить лейтенантов Коннора.

## Источник канон

- **Произведение:** Terminator 3: Rise of the Machines (2003)
- **Тип:** фильм
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| рост_см | 175 |
| масса_кг | 150 |
| производитель | Скайнет |
| класс | гуманоидный |
| категория | жидкий_металл |
| тип_модели | гуманоидный |

## Подсистемы (по типу)

- вычислительная
- энергетическая
- каркас
- броня
- сенсоры
- приводная_система
- система_связи
- навигация
- система_питания
- система_передвижения

## Многослойная броня (§11.6)

Минимум слоёв по типу: 3 (§11.6). Макс. доля массы брони: 30%.

1. B₄C керамика (внешний жертвенный) (`b4c`)
2. Ti-6Al-4V (кин. слой) (`ti6al4v`)
3. UHMWPE Dyneema (арамидный подслой) (`uhmwpe_dyneema`)

## Произведения, где появляется

- ✅ `work_003` — «Terminator 3: Rise of the Machines» (2003) → [`work_003.md`](../произведения/work_003.md)
- 📚 `work_043` — «Terminator 3: Rise of the Machines» (2003) → [`work_043.md`](../произведения/work_043.md)
- 📚 `work_044` — «Terminator 3: The Redemption» (2004) → [`work_044.md`](../произведения/work_044.md)

## Источники

- Канон: Terminator 3: Rise of the Machines (2003)

## Декомпозиция

```mermaid
graph TD
    TX["SkyNet-TX"]
    subgraph вычислительная
    t_x_cpu["neural_net_cpu_tx<br/>0.5 kg (0.3%)"]
    TX --> t_x_cpu
    end
    subgraph каркас
    t_x_эндоскелет["hyperalloy_endoskeleton_tx<br/>75.0 kg (50.0%)"]
    TX --> t_x_эндоскелет
    end
    subgraph энергетическая
    t_x_топливная_ячейка_1["plasma_cell<br/>7.0 kg (4.7%)"]
    TX --> t_x_топливная_ячейка_1
    t_x_топливная_ячейка_2["plasma_cell<br/>7.0 kg (4.7%)"]
    TX --> t_x_топливная_ячейка_2
    end
    subgraph встроенное_оружие
    t_x_плазма_пушка["built_in_plasma_cannon<br/>15.0 kg (10.0%)"]
    TX --> t_x_плазма_пушка
    t_x_нанотех_инъектор["nanotech_injector<br/>2.0 kg (1.3%)"]
    TX --> t_x_нанотех_инъектор
    end
    subgraph приводная_система
    t_x_рука_левая["servo_arm<br/>10.0 kg (6.7%)"]
    TX --> t_x_рука_левая
    t_x_рука_правая["servo_arm<br/>10.0 kg (6.7%)"]
    TX --> t_x_рука_правая
    t_x_нога_левая["servo_leg<br/>14.0 kg (9.3%)"]
    TX --> t_x_нога_левая
    t_x_нога_правая["servo_leg<br/>14.0 kg (9.3%)"]
    TX --> t_x_нога_правая
    end
    subgraph сенсоры
    t_x_сенсоры["optical_audio_array<br/>1.0 kg (0.7%)"]
    TX --> t_x_сенсоры
    end
    subgraph прочее
    t_x_ткань_кожа["living_tissue_female<br/>4.0 kg (2.7%)"]
    TX --> t_x_ткань_кожа
    end
```
