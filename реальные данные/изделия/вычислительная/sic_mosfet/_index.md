---
id: izdelie_sic_mosfet
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: силовой_транзистор
стандарты: 
  - JEDEC JESD47
  - AEC-Q101
исследовательская_группа: wolfspeed
родитель: null
дочерние_части:
  - часть_sic_mosfet_die
  - часть_sic_mosfet_lead_frame
  - часть_sic_mosfet_wire_bonds
  - часть_sic_mosfet_encapsulant
  - часть_sic_mosfet_solder
  - часть_sic_mosfet_gate_terminal
материалы_частей:
  - часть: часть_sic_mosfet_die
    материал: silicon_carbide
    форма: sic_mosfet_die
    доля_массы: 0.19
  - часть: часть_sic_mosfet_lead_frame
    материал: copper_alloy
    форма: выводные_рамки_силовой_электроники
    доля_массы: 0.475
  - часть: часть_sic_mosfet_wire_bonds
    материал: aluminum
    форма: электротехнические_проводники
    доля_массы: 0.0095
  - часть: часть_sic_mosfet_encapsulant
    материал: epoxy_molding
    форма: encapsulant_с_mc_силоых_ключей
    доля_массы: 0.19
  - часть: часть_sic_mosfet_solder
    материал: lead_free_solder
    форма: силовой_модуль_sic_die_substrate_attach
    доля_массы: 0.045
наследуемые_материалы:
  - материал: copper
    суммарная_доля_массы: 0.475
    источники_частей: [часть_sic_mosfet_lead_frame]
  - материал: monokristallicheskogo_sic
    суммарная_доля_массы: 0.19
    источники_частей: [часть_sic_mosfet_die]
  - материал: epotek_301-2
    суммарная_доля_массы: 0.19
    источники_частей: [часть_sic_mosfet_encapsulant]
  - материал: splav_sn-pb
    суммарная_доля_массы: 0.045
    источники_частей: [часть_sic_mosfet_solder]
  - материал: al_bondwire
    суммарная_доля_массы: 0.0095
    источники_частей: [часть_sic_mosfet_wire_bonds]

технологии_частей:
  - часть: часть_sic_mosfet_die
    технология: ion_implantation_si
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: monokristallicheskogo_sic
        роль: обрабатываемый
  - часть: часть_sic_mosfet_lead_frame
    технология: galvanika
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: copper_alloy
        роль: обрабатываемый
  - часть: часть_sic_mosfet_wire_bonds
    технология: diffuzionnaya_svarka
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: aluminum
        роль: обрабатываемый
  - часть: часть_sic_mosfet_encapsulant
    технология: anderfill
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: epoxy
        роль: обрабатываемый
  - часть: часть_sic_mosfet_solder
    технология: smd_montazh_oplavleniem
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: lead_free_solder
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
          min: 0.001
          max: 0.01
          nominal: 0.003
  габариты_mm:
          l: 15.94
          w: 20.95
          h: 5.02
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.5
          max: 50
          nominal: 5
наследуемые: {}
дополнительные: 
  V_max_V: 1700
  I_max_A: 100
  Rds_on_mOhm: 25
  источник: Wolfspeed datasheet
  габариты_метод: 'корпусная спецификация TO-247 — envelope корпуса прибора (Toshiba package dimensions TO-247, 15.94×20.95×5.02 мм)'
  обоснование_габаритов: 'дискретный SiC MOSFET в корпусе TO-247 — габариты приняты по реальной корпусной спецификации Toshiba 15.94×20.95×5.02 мм (та же корпоративная спецификация, что у выводной рамки части_sic_mosfet_lead_frame — рамка 15.5×20.5×0.6 мм целиком внутри envelope, толщина рамки 0.6 в диапазоне 0.55–0.68 мм JEDEC TO-247AD по Vishay case outline 92825); корроборация Vishay TO-247AD (D 20.80–21.10 × E 15.75–16.13 × высота 4.83–5.21 мм) подтверждает порядок величин; V(parent)=15.94×20.95×5.02=1676.4 мм³ ≥ ΣV(детей)×1.15=301.3 мм³ (запас ×5.6) — die 5.5×4.5×0.18, solder 5.5×5.5×0.08, encapsulant 8×8×1, lead_frame 15.5×20.5×0.6, wire_bonds 5×0.3×0.3, gate_terminal 1×0.6×0.05; по осям 15.94≥15.5 / 20.95≥20.5 / 5.02≥1.0 — F15g оба условия выполнены'
дата_создания: 2026-11-03
дата_обновления: 2026-11-10
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: SiC MOSFET

## Описание

SiC MOSFET (Wolfspeed CPM3-9000)

Полное наименование (как в CSV): `SiC MOSFET (Wolfspeed CPM3-9000)`

Дискретный силовой SiC MOSFET в корпусе TO-247: монокристаллический 4H-SiC кристалл (часть_sic_mosfet_die, 5.5×4.5×0.18 мм) напаивается на die pad выводной медной рамки (часть_sic_mosfet_lead_frame, 15.5×20.5×0.6 мм, C11000 с Ni-барьером и Ag-пайкой), соединяется алюминиевыми проводниками (часть_sic_mosfet_wire_bonds) и затворным выводом (часть_sic_mosfet_gate_terminal), фиксируется на подложке слоем пайки (часть_sic_mosfet_solder, bondline 80 мкм) и защищается эпоксидным glob-top компаундом (часть_sic_mosfet_encapsulant, 8×8×1 мм). Габариты изделия — envelope корпуса TO-247 15.94×20.95×5.02 мм (Toshiba package dimensions; корроборация Vishay case outline TO-247AD).

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | вычислительная | — | classify_subsystem |
| категория | прочее | — | — |
| габариты (Д×Ш×В) | 15.94×20.95×5.02 | mm | Toshiba, TO-247 package dimensions; корроборация Vishay case outline TO-247AD 92825 |

## Состав

Изделие верхнего уровня (уровень 1), 6 дочерних частей уровня 2:

| Часть | Роль | Габариты, мм |
|---|---|---|
| часть_sic_mosfet_die | SiC кристалл (4H-SiC, монокристалл) | 5.5×4.5×0.18 |
| часть_sic_mosfet_solder | пайка кристалла к рамке (bondline 80 мкм) | 5.5×5.5×0.08 |
| часть_sic_mosfet_lead_frame | выводная рамка TO-247 (die pad + 3 вывода) | 15.5×20.5×0.6 |
| часть_sic_mosfet_wire_bonds | алюминиевые проводники затвора/истока | 5×0.3×0.3 |
| часть_sic_mosfet_gate_terminal | затворный вывод | 1×0.6×0.05 |
| часть_sic_mosfet_encapsulant | эпоксидный glob-top компаунд | 8×8×1 |

Габаритный баланс (F15g): V(parent)=1676.4 мм³ ≥ ΣV(детей)×1.15=301.3 мм³; по осям 15.94≥15.5, 20.95≥20.5, 5.02≥1.0 — все части помещаются внутри envelope корпуса.

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Вертикальный траншейный SiC MOSFET: при положительном смещении затвора под затворным диэлектриком формируется инверсионный канал в 4H-SiC, ток течёт от истока через канал и дрейфовый эпитаксиальный слой к тыльному стоку (die pad рамки). Широкозонный SiC (критическое поле ~2.8 МВ/см, теплопроводность ~490 Вт/(м·К)) позволяет держать 1700 В блокировки при RDS(on) 25 мОм на кристалле 5.5×4.5 мм; тепло от кристалла отводится через пайку в медную рамку и фланец-Tab корпуса TO-247 на радиатор.

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- Toshiba, TO-247 package dimensions (15.94×20.95×5.02 мм): https://toshiba.semicon-storage.com/us/semiconductor/design-development/package/detail.TO-247.html (проверено 2026-11-06)
- Vishay, Case Outline for TO-247AD 3L (JEDEC TO-247AD — D 20.80–21.10, E 15.75–16.13, A 4.83–5.21 мм): https://www.vishay.com/docs/92825/packinfo_case_outline_to-247ad_3l.pdf (проверено 2026-11-08)

---


## Декомпозиция

```mermaid
graph TD
    sic_mosfet["izdelie_sic_mosfet"]
    sic_mosfet_die["часть_sic_mosfet_die"]
    sic_mosfet --> sic_mosfet_die
    sic_mosfet_lead_frame["часть_sic_mosfet_lead_frame"]
    sic_mosfet --> sic_mosfet_lead_frame
    sic_mosfet_wire_bonds["часть_sic_mosfet_wire_bonds"]
    sic_mosfet --> sic_mosfet_wire_bonds
    sic_mosfet_encapsulant["часть_sic_mosfet_encapsulant"]
    sic_mosfet --> sic_mosfet_encapsulant
    sic_mosfet_solder["часть_sic_mosfet_solder"]
    sic_mosfet --> sic_mosfet_solder
    sic_mosfet_gate_terminal["часть_sic_mosfet_gate_terminal"]
    sic_mosfet --> sic_mosfet_gate_terminal
```
