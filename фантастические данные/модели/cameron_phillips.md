---
id: SkyNet-Cameron
дочерние_части: 
  - часть_cameron_cpu
  - часть_cameron_эндоскелет
  - часть_cameron_топливная_ячейка_1
  - часть_cameron_топливная_ячейка_2
  - часть_cameron_рука_левая
  - часть_cameron_рука_правая
  - часть_cameron_нога_левая
  - часть_cameron_нога_правая
  - часть_cameron_сенсоры
  - часть_cameron_ткань_кожа
тип: модель_SkyNet
класс: гуманоидный
категория: стандартный
тип_модели: гуманоидный
источник_происхождения: сериал
функции: ["телохранитель", "инфильтрация (осознанная)"]
канон_источник: Terminator: The Sarah Connor Chronicles (2008-2009)
произведения: ["work_007"]
производитель: Скайнет → Resistance
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
  роль_модели: 'infiltrator (teenage girl, ~16 лет)'
  визуальная: 'живая ткань, женская форма'
  чувства: 'имитация эмоций (canon T:SCC)'
тактико_технические_характеристики: 
  мобильность:
          максимальная_скорость_км_ч: 40
          масса_кг: 65
  cpu: Neural Net CPU (Cameron variant)
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
# SkyNet-Cameron

## Описание

Cameron Phillips — перепрограммированный терминатор T:SCC; класс предположительно T-900; модель «Алисса»; защищает Джона Коннора; имитирует подростка.

## Источник канон

- **Произведение:** Terminator: The Sarah Connor Chronicles (2008-2009)
- **Тип:** сериал
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| рост_см | 165 |
| масса_кг | 120 |
| производитель | Скайнет → Resistance |
| класс | гуманоидный |
| категория | стандартный |
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

- ✅ `work_007` — «Terminator: The Sarah Connor Chronicles» (2008) → [`work_007.md`](../произведения/work_007.md)

## Источники

- Канон: Terminator: The Sarah Connor Chronicles (2008-2009)

## Декомпозиция

```mermaid
graph TD
    Cameron["SkyNet-Cameron"]
    subgraph вычислительная
    cameron_cpu["neural_net_cpu_cameron<br/>0.3 kg (0.5%)"]
    Cameron --> cameron_cpu
    end
    subgraph каркас
    cameron_эндоскелет["titanium_endoskeleton_small<br/>35.0 kg (53.8%)"]
    Cameron --> cameron_эндоскелет
    end
    subgraph энергетическая
    cameron_топливная_ячейка_["fuel_cell_small<br/>4.0 kg (6.2%)"]
    Cameron --> cameron_топливная_ячейка_
    cameron_топливная_ячейка_["fuel_cell_small<br/>4.0 kg (6.2%)"]
    Cameron --> cameron_топливная_ячейка_
    end
    subgraph приводная_система
    cameron_рука_левая["servo_arm_small<br/>5.0 kg (7.7%)"]
    Cameron --> cameron_рука_левая
    cameron_рука_правая["servo_arm_small<br/>5.0 kg (7.7%)"]
    Cameron --> cameron_рука_правая
    cameron_нога_левая["servo_leg_small<br/>4.5 kg (6.9%)"]
    Cameron --> cameron_нога_левая
    cameron_нога_правая["servo_leg_small<br/>4.5 kg (6.9%)"]
    Cameron --> cameron_нога_правая
    end
    subgraph сенсоры
    cameron_сенсоры["optical_audio_array<br/>0.5 kg (0.8%)"]
    Cameron --> cameron_сенсоры
    end
    subgraph прочее
    cameron_ткань_кожа["living_tissue_female<br/>2.0 kg (3.1%)"]
    Cameron --> cameron_ткань_кожа
    end
```
