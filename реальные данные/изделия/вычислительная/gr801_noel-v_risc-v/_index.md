---
id: izdelie_gr801_noel-v_risc-v
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: RISC-V_процессор
стандарты: 
  - RV64GC ISA
исследовательская_группа: cobham_gaisler
родитель: null
дочерние_части:
  - часть_gr801_noel-v_risc-v_die
  - часть_gr801_noel-v_risc-v_package
  - часть_gr801_noel-v_risc-v_crystal_osc
  - часть_gr801_noel-v_risc-v_flash
  - часть_gr801_noel-v_risc-v_sram
  - часть_gr801_noel-v_risc-v_substrate
  - часть_gr801_noel-v_risc-v_thermal_pad
  - часть_gr801_noel-v_risc-v_pins
  - часть_gr801_noel-v_risc-v_capacitors
  - часть_gr801_noel-v_risc-v_pcb
материалы_частей:
  - часть: часть_gr801_noel-v_risc-v_die
    материал: silicon_wafer
    форма: подложки_нейроморфных_процессоров
    доля_массы: 0.1
  - часть: часть_gr801_noel-v_risc-v_package
    материал: plastic_qfp
    форма: корпус_qfp_tqfp_lqfp
    доля_массы: 0.16
  - часть: часть_gr801_noel-v_risc-v_crystal_osc
    материал: quartz
    форма: пьезоэлектрический_резонатор
    доля_массы: 0.02
  - часть: часть_gr801_noel-v_risc-v_flash
    материал: silicon_wafer
    форма: подложки_нейроморфных_процессоров
    доля_массы: 0.04
  - часть: часть_gr801_noel-v_risc-v_sram
    материал: silicon_wafer
    форма: подложки_нейроморфных_процессоров
    доля_массы: 0.04

технологии_частей:
  - часть: часть_gr801_noel-v_risc-v_die
    технология: ion_implantation_si
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: si
        роль: обрабатываемый
  - часть: часть_gr801_noel-v_risc-v_package
    технология: anderfill
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: epoxy
        роль: обрабатываемый
  - часть: часть_gr801_noel-v_risc-v_crystal_osc
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: quartz
        роль: обрабатываемый
  - часть: часть_gr801_noel-v_risc-v_flash
    технология: ion_implantation_si
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: si
        роль: обрабатываемый
  - часть: часть_gr801_noel-v_risc-v_sram
    технология: ion_implantation_si
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: si
        роль: обрабатываемый
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
          min: 0.005
          max: 0.05
          nominal: 0.01
  габариты_mm:
          l: 40
          w: 40
          h: 3.5
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 1
          max: 5
          nominal: 3
наследуемые: {}
дополнительные: 
  архитектура: RV64GC RISC-V 64-bit (NOEL-V)
  ядра: 1
  нейроморфный_движок: Brainchip Akida 1.0 — 8 узлов, 1024 MAC/такт
  тактовая_МГц: 1000
  техпроцесс: 28 нм FDSOI (STMicroelectronics)
  корпус: FCTEBGA 23×23 мм, 441 ball, шаг 1 мм
  питание: core 1.0 В, I/O 1.8 В и 3.3 В
  память: 8 МБ on-chip RAM (3.2 МБ для Akida), QSPI x2
  интерфейсы: PCIe Gen3 x4, GbE (GMII), CPI 8-bit, SpaceWire 4×200 Мбит/с, 2×CAN FD, SPI, 2×I2C, 3×UART, 16×GPIO
  стойкость: TID 50 krad(Si) гарантировано / 100 krad(Si) скрининг; SEL ≥60 МэВ·см²/мг
  источник: Frontgrade Gaisler (https://www.gaisler.com/products/gr801)
  форм_фактор: 'SoC-модуль: пакет FCTEBGA 23×23×1.5 мм (441 шар, шаг 1 мм) на несущей PCB 40×40×1.6 мм с обвязкой (кварц 3225, QSPI-flash, SRAM, MLCC-блокировка)'
  обоснование_габаритов: 'стек модуля = несущая PCB 40×40×1.6 мм (fanout FCTEBGA-441, 8 слоёв) + BGA-шары 0.4 мм + пакет 1.5 мм (FCTEBGA 23×23, 441 ball, шаг 1 мм — gaisler.com/products/gr801) = 3.5 мм; V = 40×40×3.5 = 5600 мм³ ≥ ΣV(детей)×1.15 = 4877 мм³ (F15g A), по осям 40≥40/40≥40/3.5≥1.6 (F15g B); земляной план кварца/flash/SRAM/конденсаторов на PCB ≤ 40×40 ✓'
дата_создания: 2026-11-03
дата_обновления: 2026-11-10
источник: user_input
источник_разбора: веб-верификация
источник_url: https://www.gaisler.com/products/gr801
источник_дата: 2026-11-07
---
# Изделие: GR801 NOEL-V RISC-V

## Описание

GR801 — радиационно-стойкий SoC Frontgrade Gaisler: одножерный RISC-V NOEL-V (RV64GC) для системного управления + нейроморфный AI-движок Brainchip Akida™ 1.0 (8 узлов, 1024 MAC/такт, 1–4-битное квантование) на 28 нм FDSOI, корпус FCTEBGA 23×23 мм, 441 ball

Полное наименование (как в CSV): `GR801 NOEL-V RISC-V (rad-hard)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | вычислительная | — | classify_subsystem |
| габариты (Д×Ш×В) | 40×40×3.5 | mm | SoC-модуль: PCB 40×40×1.6 + шары 0.4 + пакет FCTEBGA 23×23×1.5 (gaisler.com) |
| выработка тепла | 3 | W | тепловой бюджет SoC-модуля: NOEL-V (core 1.0 В) + Akida, 28 нм FDSOI; min 1 / max 5 Вт |
| техпроцесс | 28 нм FDSOI | — | STMicroelectronics (gaisler.com/products/gr801) |
| стойкость | TID 50–100 krad(Si), SEL ≥60 МэВ·см²/мг | — | gaisler.com/products/gr801 |
| категория | электроника | — | canon |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

SoC-модуль GR801 (уровень 1), 10 частей (уровень 2): die (кристалл NOEL-V+Akida 8×8×0.5, 3 Вт — весь тепловой бюджет), package (FCTEBGA 23×23×1.5, 441 ball), substrate (23×23×1.0), pins (BGA-шары 21×21, шаг 1 мм), thermal_pad, pcb — несущая плата 40×40×1.6 (fanout BGA, 8 слоёв), flash (QSPI 8×6), sram (4×3), crystal_osc (3225: 3.2×2.5), capacitors (MLCC 0402). Тепловой баланс: 3 Вт выделяется в кристалле и отводится через термопрокладку/подложку/плату.

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

NOEL-V (RV64GC) исполняет ОС и конвейер данных; AI-нагрузка (камера CPI, SpaceWire-потоки) уходит в Akida: SNN исполняются событийно — вычисление активируется только спайками, квантование 1–4 бита; FDSOI даёт подложечное смещение (энергоэффективность) и встроенную стойкость к одиночным событиям. Всё тепловыделение (номинал 3 Вт, min 1 / max 5) депонируется в кристалле и отводится пассивно: die → thermal_pad/подложка → плата. Вывод — PCIe Gen3 x4 или GbE в бортовой контур.

## Источники

- Frontgrade Gaisler, «GR801» — RV64GC (NOEL-V) + Akida 1.0, 28 нм FDSOI, FCTEBGA 23×23 мм, TID/SEL: https://www.gaisler.com/products/gr801 (проверено 2026-11-07)
- CSV: `начальные данные_final.csv` (пользовательский ввод)

---


## Декомпозиция

```mermaid
graph TD
    gr801_noel-v_risc-v["izdelie_gr801_noel-v_risc-v"]
    gr801_noel-v_risc-v_die["часть_gr801_noel-v_risc-v_die"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_die
    gr801_noel-v_risc-v_packa["часть_gr801_noel-v_risc-v_package"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_packa
    gr801_noel-v_risc-v_cryst["часть_gr801_noel-v_risc-v_crystal_osc"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_cryst
    gr801_noel-v_risc-v_flash["часть_gr801_noel-v_risc-v_flash"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_flash
    gr801_noel-v_risc-v_sram["часть_gr801_noel-v_risc-v_sram"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_sram
    gr801_noel-v_risc-v_subst["часть_gr801_noel-v_risc-v_substrate"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_subst
    gr801_noel-v_risc-v_therm["часть_gr801_noel-v_risc-v_thermal_pad"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_therm
    gr801_noel-v_risc-v_pins["часть_gr801_noel-v_risc-v_pins"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_pins
    gr801_noel-v_risc-v_capac["часть_gr801_noel-v_risc-v_capacitors"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_capac
    gr801_noel-v_risc-v_pcb["часть_gr801_noel-v_risc-v_pcb"]
    gr801_noel-v_risc-v --> gr801_noel-v_risc-v_pcb
```
