---
id: izdelie_tverdooksidnyi_toplivnyi_element
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: твердооксидный_топливный_элемент
стандарты: 
  - IEC 62282
исследовательская_группа: bloom_energy
родитель: null
дочерние_части:
  - часть_tverdooksidnyi_toplivnyi_element_anode
  - часть_tverdooksidnyi_toplivnyi_element_electrolyte
  - часть_tverdooksidnyi_toplivnyi_element_cathode
  - часть_tverdooksidnyi_toplivnyi_element_interconnect
  - часть_tverdooksidnyi_toplivnyi_element_seal
  - часть_tverdooksidnyi_toplivnyi_element_manifold
материалы_частей:
  - часть: часть_tverdooksidnyi_toplivnyi_element_anode
    материал: ni-ysz
    доля_массы: 0.18
  - часть: часть_tverdooksidnyi_toplivnyi_element_electrolyte
    материал: ysz_electrolyte
    доля_массы: 0.095
  - часть: часть_tverdooksidnyi_toplivnyi_element_cathode
    материал: lsm_cathode
    доля_массы: 0.18
  - часть: часть_tverdooksidnyi_toplivnyi_element_interconnect
    материал: crofer_22_apu
    доля_массы: 0.285
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
          min: 1
          max: 10
          nominal: 5
  габариты_mm:
          l: 200
          w: 200
          h: 150
  выработка_энергии_W:
          min: 100
          max: 1000
          nominal: 500
  выработка_тепла_W:
          min: 100
          max: 1000
          nominal: 500
наследуемые: {}
дополнительные: 
  T_рабочая_C: 800
  КПД_процентов: 55
  источник: Bloom Energy Energy Server
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Твёрдооксидный топливный элемент

## Описание

Твёрдооксидный топливный элемент (SOFC)

Полное наименование (как в CSV): `Твёрдооксидный топливный элемент (SOFC)`

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
    tverdooksidnyi_topli["izdelie_tverdooksidnyi_toplivnyi_element"]
    tverdooksidnyi_toplivnyi_["часть_tverdooksidnyi_toplivnyi_element_anode"]
    tverdooksidnyi_topli --> tverdooksidnyi_toplivnyi_
    tverdooksidnyi_toplivnyi_["часть_tverdooksidnyi_toplivnyi_element_electrolyte"]
    tverdooksidnyi_topli --> tverdooksidnyi_toplivnyi_
    tverdooksidnyi_toplivnyi_["часть_tverdooksidnyi_toplivnyi_element_cathode"]
    tverdooksidnyi_topli --> tverdooksidnyi_toplivnyi_
    tverdooksidnyi_toplivnyi_["часть_tverdooksidnyi_toplivnyi_element_interconnect"]
    tverdooksidnyi_topli --> tverdooksidnyi_toplivnyi_
    tverdooksidnyi_toplivnyi_["часть_tverdooksidnyi_toplivnyi_element_seal"]
    tverdooksidnyi_topli --> tverdooksidnyi_toplivnyi_
    tverdooksidnyi_toplivnyi_["часть_tverdooksidnyi_toplivnyi_element_manifold"]
    tverdooksidnyi_topli --> tverdooksidnyi_toplivnyi_
```
