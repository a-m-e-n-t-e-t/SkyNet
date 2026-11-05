---
id: часть_svintsovo-kislotnye_akb_anode
тип: изделие
категория: машиностроение
уровень_иерархии: промежуточный
уровень_номер: 2
подсистема: энергетическая
подтип: PbO2_анод
стандарты:
  - IEC 60095
исследовательская_группа: null
родитель: izdelie_svintsovo-kislotnye_akb
дочерние_части: []
материалы_частей:
  - часть: часть_svintsovo-kislotnye_akb_anode
    материал: pbo2
    доля_массы: 1.0

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
  масса_kg: 0.247
  доля_массы_родителя: 0.0164
  габариты_mm:
    l: 160
    w: 146
    h: 2.2
  выработка_энергии_W: 0
  выработка_тепла_W: 1
наследуемые: {}
дополнительные: {}
дата_создания: 2026-11-03
дата_обновления: 2026-11-05
источник: web_search
источник_разбора: канон
источник_url: https://patents.google.com/patent/CN112103513A/en
источник_дата: 2026-11-05
---
# Часть: часть_svintsovo-kislotnye_akb_anode

## Описание

Положительная пластина свинцово-кислотной АКБ: решётка (токоотвод) из сплава Pb-Sb/Pb-Ca с рамкой 1.8–2.0 мм и 15–16 поперечными рёбрами, заполнена пастой активной массы PbO2 (β-фаза, пористость ~50 %). Пластина 160×146×2.2 мм — типовой формат DIN-батареи с корпусом 350×175×190 мм (6 ячеек вдоль длины, шаг 58.3 мм; высота пластин ~146 мм). Масса пластины ~0.25 кг (объём 51.4 см³ × ~4.8 г/см³ кажущейся плотности пасты).

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | canon |
| подтип | PbO2_анод | — | canon |
| масса | 0.247 | kg | Chaowei Power patent CN112103513A (2020): positive grid frame 1.8–2.0 mm / 15–16 ribs, negative grid frame 1.2–1.4 mm / 12–15 ribs; plate L×W derived from canon DIN-format case 350×175×190 (6 cells, cell pitch 58.3 mm → plate 160×146 mm); Suzuki Battery engineering blog (PbO2 positive / sponge lead negative) |
| доля массы родителя | 0.0164 | — | оценка |
| габариты (Д×Ш×В) | 160×146×2.2 | mm | Chaowei Power patent CN112103513A (2020): positive grid frame 1.8–2.0 mm / 15–16 ribs, negative grid frame 1.2–1.4 mm / 12–15 ribs; plate L×W derived from canon DIN-format case 350×175×190 (6 cells, cell pitch 58.3 mm → plate 160×146 mm); Suzuki Battery engineering blog (PbO2 positive / sponge lead negative) |
| выработка энергии | 0 | W | canon |
| выработка тепла | 1 | W | canon |
| материал | pbo2 | — | pbo2.md |

## Принцип работы

При разряде PbO2 восстанавливается до PbSO4 с поглощением электронов: PbO2 + SO4²⁻ + 4H⁺ + 2e⁻ → PbSO4 + 2H2O (E° ≈ +1.69 В). При заряде реакция идёт в обратную сторону с выделением PbO2; решётка служит токоотводом и каркасом, пористая паста — местом электрохимической реакции.

## Состав

Промежуточная часть (уровень 2). Дочерних частей нет.

## Используемые материалы

- `pbo2` → [`pbo2.md`](../../../../материалы/pbo2.md)

## Источники

- Chaowei Power patent CN112103513A (2020): positive grid frame 1.8–2.0 mm / 15–16 ribs, negative grid frame 1.2–1.4 mm / 12–15 ribs; plate L×W derived from canon DIN-format case 350×175×190 (6 cells, cell pitch 58.3 mm → plate 160×146 mm); Suzuki Battery engineering blog (PbO2 positive / sponge lead negative): https://patents.google.com/patent/CN112103513A/en (проверено 2026-11-05)
- Материалы: реальные данные/материалы/
