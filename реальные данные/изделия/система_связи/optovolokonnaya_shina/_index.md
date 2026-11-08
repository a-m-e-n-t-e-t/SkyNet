---
id: izdelie_optovolokonnaya_shina
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: система_связи
подтип: прочее
стандарты: 
  - FCC Part 15
  - ETSI EN 301 489
исследовательская_группа: harris_thales
родитель: null
дочерние_части:
  - часть_optovolokonnaya_shina_core
  - часть_optovolokonnaya_shina_housing
  - часть_optovolokonnaya_shina_connectors
  - часть_optovolokonnaya_shina_mounting
материалы_частей:
  - часть: часть_optovolokonnaya_shina_core
    материал: al_6061-t6
    доля_массы: 0.45
  - часть: часть_optovolokonnaya_shina_housing
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
          min: 0.005
          max: 5
          nominal: 0.1
  габариты_mm:
          l: 50
          w: 30
          h: 5
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.01
          max: 5
          nominal: 1.2
наследуемые: {}
дополнительные:
  цена_usd: null
  обоснование_теплового_баланса: "номинал 1.2 W >= СУММ(дочерних) 1.10 W (core 1 W — активные трансиверы коммутационного блока; connectors 0.1 W; housing/mounting 0 W) + собственные пассивные потери волоконных трактов ~0.1 W (вставочные потери, микропоглощение). Оптические трансиверы рассеивают <=1 W (LINK-PP 10GBASE-T SFP power/heat guide; SFP+ Thermal and EMI Considerations 2013), максимум 5 W — верхняя граница многотерминальной конфигурации"
  источник_url_тепла: https://www.link-pp.com/resources/technical-specs/10gbase-t-sfp-power-heat-management-guide
  источник_url_2_тепла: https://core.ac.uk/download/pdf/42812227.pdf
дата_создания: 2026-11-03
дата_обновления: 2026-11-08
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: оптоволоконная шина

## Описание

оптоволоконная шина

Полное наименование (как в CSV): `оптоволоконная шина`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | система_связи | — | classify_subsystem |
| категория | прочее | — | — |
| выработка тепла (nominal) | 1.2 | W | СУММ(детей) 1.10 (core 1 + connectors 0.1) + пассивные потери ~0.1; трансиверы <=1 W — LINK-PP / SFP+ Thermal 2013 |

Тепловой баланс: номинал выработки тепла 1.2 W = СУММ(дочерних) 1.10 W (core 1 W — активные оптические трансиверы; connectors 0.1 W — терминаторы MPO/MTP) + собственные пассивные потери ~0.1 W; диапазон 0.01–5 W покрывает пассивные и многотерминальные конфигурации. См. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml.

## Состав

Изделие верхнего уровня (4 части): ядро (коммутационный блок 130×85×28), корпус (150×98×33), комплект разъёмов MPO/MTP, крепёж/жгуты (60×25×6). См. раздел Декомпозиция.

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Оптоволоконная шина — канал передачи данных по волоконно-оптическим линиям (авионика: MIL-STD-1773 — волоконная реализация протокола MIL-STD-1553B): терминалы BC/RT/BM обмениваются данными через пассивные волоконные ответвления; активная электроника терминалов (ядро, <=1 W на трансивер) генерирует тепло, пассивные волоконные тракты вносят только вставочные потери (~0.1 W), разъёмы MPO/MTP терминируют линии. Иммунитет к ЭМИ и гальваноразвязка — ключевые преимущества перед медной шиной.

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- MIL-STD-1773 Fiber Optic Data Bus, NASA GSFC (Small Explorer Data System, M. Flanegan) — https://core.ac.uk/download/pdf/42812227.pdf (обращение 2026-11-08)
- LINK-PP — 10GBASE-T SFP Power & Heat Management Guide: оптические трансиверы <1 W, медные модули ~3 W — https://www.link-pp.com/resources/technical-specs/10gbase-t-sfp-power-heat-management-guide (обращение 2026-11-08)

---


## Декомпозиция

```mermaid
graph TD
    optovolokonnaya_shin["izdelie_optovolokonnaya_shina"]
    optovolokonnaya_shina_cor["часть_optovolokonnaya_shina_core"]
    optovolokonnaya_shin --> optovolokonnaya_shina_cor
    optovolokonnaya_shina_hou["часть_optovolokonnaya_shina_housing"]
    optovolokonnaya_shin --> optovolokonnaya_shina_hou
    optovolokonnaya_shina_con["часть_optovolokonnaya_shina_connectors"]
    optovolokonnaya_shin --> optovolokonnaya_shina_con
    optovolokonnaya_shina_mou["часть_optovolokonnaya_shina_mounting"]
    optovolokonnaya_shin --> optovolokonnaya_shina_mou
```
