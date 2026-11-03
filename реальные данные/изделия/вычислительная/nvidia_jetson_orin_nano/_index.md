---
id: izdelie_nvidia_jetson_orin_nano
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: edge_AI_модуль
стандарты: 
  - JEDEC JESD47
  - PCIe 3.0
исследовательская_группа: nvidia
родитель: null
дочерние_части:
  - часть_nvidia_jetson_orin_nano_soc
  - часть_nvidia_jetson_orin_nano_memory
  - часть_nvidia_jetson_orin_nano_storage
  - часть_nvidia_jetson_orin_nano_pmic
  - часть_nvidia_jetson_orin_nano_wifi_bt
  - часть_nvidia_jetson_orin_nano_connectors
  - часть_nvidia_jetson_orin_nano_heat_sink
  - часть_nvidia_jetson_orin_nano_pcb
  - часть_nvidia_jetson_orin_nano_enclosure
материалы_частей:
  - часть: часть_nvidia_jetson_orin_nano_soc
    материал: silicon_wafer
    доля_массы: 0.09
  - часть: часть_nvidia_jetson_orin_nano_memory
    материал: silicon_wafer
    доля_массы: 0.045
  - часть: часть_nvidia_jetson_orin_nano_storage
    материал: silicon_wafer
    доля_массы: 0.045
  - часть: часть_nvidia_jetson_orin_nano_heat_sink
    материал: aluminum
    доля_массы: 0.285
  - часть: часть_nvidia_jetson_orin_nano_pcb
    материал: fr4
    доля_массы: 0.32
  - часть: часть_nvidia_jetson_orin_nano_enclosure
    материал: aluminum
    доля_массы: 0.45
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
          min: 0.08
          max: 0.15
          nominal: 0.13
  выработка_тепла_W:
          min: 7
          max: 25
          nominal: 15
наследуемые: {}
дополнительные: 
  TOPS: 67
  GPU: Ampere 1024 CUDA cores
  process_nm: 8
  цена_usd: 249
  источник: nvidia.com Jetson Orin Nano Super
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: NVIDIA Jetson Orin Nano

## Описание

NVIDIA Jetson Orin Nano

Полное наименование (как в CSV): `NVIDIA Jetson Orin Nano`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | вычислительная | — | classify_subsystem |
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
    nvidia_jetson_orin_n["izdelie_nvidia_jetson_orin_nano"]
    nvidia_jetson_orin_nano_s["часть_nvidia_jetson_orin_nano_soc"]
    nvidia_jetson_orin_n --> nvidia_jetson_orin_nano_s
    nvidia_jetson_orin_nano_m["часть_nvidia_jetson_orin_nano_memory"]
    nvidia_jetson_orin_n --> nvidia_jetson_orin_nano_m
    nvidia_jetson_orin_nano_s["часть_nvidia_jetson_orin_nano_storage"]
    nvidia_jetson_orin_n --> nvidia_jetson_orin_nano_s
    nvidia_jetson_orin_nano_p["часть_nvidia_jetson_orin_nano_pmic"]
    nvidia_jetson_orin_n --> nvidia_jetson_orin_nano_p
    nvidia_jetson_orin_nano_w["часть_nvidia_jetson_orin_nano_wifi_bt"]
    nvidia_jetson_orin_n --> nvidia_jetson_orin_nano_w
    nvidia_jetson_orin_nano_c["часть_nvidia_jetson_orin_nano_connectors"]
    nvidia_jetson_orin_n --> nvidia_jetson_orin_nano_c
    nvidia_jetson_orin_nano_h["часть_nvidia_jetson_orin_nano_heat_sink"]
    nvidia_jetson_orin_n --> nvidia_jetson_orin_nano_h
    nvidia_jetson_orin_nano_p["часть_nvidia_jetson_orin_nano_pcb"]
    nvidia_jetson_orin_n --> nvidia_jetson_orin_nano_p
    nvidia_jetson_orin_nano_e["часть_nvidia_jetson_orin_nano_enclosure"]
    nvidia_jetson_orin_n --> nvidia_jetson_orin_nano_e
```
