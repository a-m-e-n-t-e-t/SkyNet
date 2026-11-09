---
id: izdelie_emi-generator
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: встроенное_оружие
подтип: ЭМИ_генератор
стандарты: 
  - MIL-STD-461
исследовательская_группа: lockheed_martin
родитель: null
дочерние_части:
  - часть_emi-generator_capacitor_bank
  - часть_emi-generator_antenna
  - часть_emi-generator_switch
  - часть_emi-generator_source
  - часть_emi-generator_waveguide
  - часть_emi-generator_housing
материалы_частей:
  - часть: часть_emi-generator_capacitor_bank
    материал: ceramic_capacitors
    доля_массы: 0.38
  - часть: часть_emi-generator_antenna
    материал: aluminum
    доля_массы: 0.19
  - часть: часть_emi-generator_waveguide
    материал: aluminum
    доля_массы: 0.285
  - часть: часть_emi-generator_housing
    материал: aluminum
    доля_массы: 0.38
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
          min: 50
          max: 1000
          nominal: 200
  габариты_mm:
          l: 1200
          w: 800
          h: 1200
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 100
          max: 2000
          nominal: 500
наследуемые: {}
дополнительные: 
  E_field_V_m: 50000
  источник: HPM weapon systems
  обоснование_габаритов: 'Промышленный напольный шкаф 19'' 800 мм (ширина) × 1200 мм (глубина) × 27U ≈ 1200 мм (высота; 1U=44.45 мм по EIA-310/IEC 60297): вмещает рупорную антенну ETS-Lindgren 3162-01 1062.7×647.7×746.8 мм (по глубине 1200 мм), корпус Ti-6Al-4V 600×500×1200 мм (полная высота шкафа), банк конденсаторов CDE WL 279×337×572 мм, коммутатор 350×160×160 мм, источник 70×70×300 мм и волновод WR-284; V(шкафа)=1.152 м³ ≥ Σ V(детей)×1.15=1.079 м³'
  источник_url: https://www.upcom.com.tr/products/server-rack-cabinet-19/
  источник_дата: 2026-11-08
дата_создания: 2026-11-03
дата_обновления: 2026-11-08
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: ЭМИ-генератор

## Описание

ЭМИ-генератор (EMP — электромагнитный импульс) — оружие поражения электроники

Полное наименование (как в CSV): `ЭМИ-генератор (EMP — электромагнитный импульс) — оружие поражения электроники`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
| категория | энергетика | — | classify_subsystem |
| габариты_mm (l×w×h) | 1200×800×1200 | мм | шкаф 19'' 800W×1200D×27U (EIA-310), upcom.com.tr |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

Изделие верхнего уровня, 6 дочерних частей: capacitor_bank, antenna, switch, source, waveguide, housing — размещены в напольном шкафу 19'' 800×1200×1200 мм; V(шкафа)=1.152 м³ ≥ Σ V(детей)×1.15=1.079 м³ (упаковочный коэффициент 1.15 с зазорами на крепёж и кабельные каналы).

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
    emi-generator["izdelie_emi-generator"]
    emi-generator_capacitor_b["часть_emi-generator_capacitor_bank"]
    emi-generator --> emi-generator_capacitor_b
    emi-generator_antenna["часть_emi-generator_antenna"]
    emi-generator --> emi-generator_antenna
    emi-generator_switch["часть_emi-generator_switch"]
    emi-generator --> emi-generator_switch
    emi-generator_source["часть_emi-generator_source"]
    emi-generator --> emi-generator_source
    emi-generator_waveguide["часть_emi-generator_waveguide"]
    emi-generator --> emi-generator_waveguide
    emi-generator_housing["часть_emi-generator_housing"]
    emi-generator --> emi-generator_housing
```
