---
id: часть_svintsovo-kislotnye_akb_cathode
тип: изделие
категория: машиностроение
уровень_иерархии: промежуточный
уровень_номер: 2
подсистема: энергетическая
подтип: Pb_катод
стандарты:
  - IEC 60095
исследовательская_группа: null
родитель: izdelie_svintsovo-kislotnye_akb
дочерние_части: []
материалы_частей:
  - часть: часть_svintsovo-kislotnye_akb_cathode
    материал: spongy_lead
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
  масса_kg: 0.15
  доля_массы_родителя: 0.01
  габариты_mm:
    l: 160
    w: 146
    h: 1.6
  выработка_энергии_W: 250
  выработка_тепла_W: 2.0
наследуемые: {}
дополнительные: {}
дата_создания: 2026-11-03
дата_обновления: 2026-11-07
источник: web_search
источник_разбора: канон
источник_url: https://patents.google.com/patent/CN112103513A/en
источник_дата: 2026-11-05
---
# Часть: часть_svintsovo-kislotnye_akb_cathode

## Описание

Отрицательная пластина свинцово-кислотной АКБ: решётка из Pb-Sb/Pb-Ca с рамкой 1.2–1.4 мм и 12–15 поперечными рёбрами (тоньше положительной — нет коррозионного роста), заполнена губчатым свинцом (пористость ~40–50 %). Пластина 160×146×1.6 мм для DIN-корпуса 350×175×190 мм; масса ~0.15 кг (объём 37.4 см³ × ~4.0 г/см³ с учётом пористости губчатой массы).

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | canon |
| подтип | Pb_катод | — | canon |
| масса | 0.15 | kg | Chaowei Power patent CN112103513A (2020): positive grid frame 1.8–2.0 mm / 15–16 ribs, negative grid frame 1.2–1.4 mm / 12–15 ribs; plate L×W derived from canon DIN-format case 350×175×190 (6 cells, cell pitch 58.3 mm → plate 160×146 mm); Suzuki Battery engineering blog (PbO2 positive / sponge lead negative) |
| доля массы родителя | 0.01 | — | оценка |
| габариты (Д×Ш×В) | 160×146×1.6 | mm | Chaowei Power patent CN112103513A (2020): positive grid frame 1.8–2.0 mm / 15–16 ribs, negative grid frame 1.2–1.4 mm / 12–15 ribs; plate L×W derived from canon DIN-format case 350×175×190 (6 cells, cell pitch 58.3 mm → plate 160×146 mm); Suzuki Battery engineering blog (PbO2 positive / sponge lead negative) |
| выработка энергии | 250 | W | вклад пары PbO2↔Pb (канон-модель; web_search 2026-11-07) |
| выработка тепла | 2.0 | W | I²R пасты + перенапряжение (BU-802a; web_search 2026-11-07) |
| материал | spongy_lead | — | spongy_lead.md |

## Принцип работы

При разряде губчатый свинец окисляется до сульфата: Pb + SO4²⁻ → PbSO4 + 2e⁻ (E° ≈ −0.36 В); электроны через решётку уходят во внешнюю цепь. При заряде PbSO4 восстанавливается обратно в пористый Pb; добавки (барий, лигносульфонаты) препятствуют срастанию кристаллов и сульфатации.

## Энергетический баланс (F15d/F15b)

Отрицательная пластина — второй электрод пары: Pb + H2SO4 → PbSO4 + 2H⁺ + 2e⁻ (E° ≈ −0.36 В); электроны через решётку уходят во внешнюю цепь. Учётная мощность пары «PbO2 ↔ Pb»: 250 Вт + 250 Вт = 500 Вт номинала родителя (I ≈ 41.7 А общий ток пластин; E°cell = 2.05 В — Wikipedia). По отдельности пластина мощность не отдаёт — значение отражает вклад пары.

Тепло 2.0 Вт при I = 41.7 А — омические потери пасты + активационное перенапряжение окисления Pb (I²R-аппроксимация — BU-802a). Ранее 1 Вт — канон-заглушка.

## Состав

Промежуточная часть (уровень 2). Дочерних частей нет.

## Используемые материалы

- `spongy_lead` → [`spongy_lead.md`](../../../../материалы/spongy_lead.md)

## Источники

- Chaowei Power patent CN112103513A (2020): positive grid frame 1.8–2.0 mm / 15–16 ribs, negative grid frame 1.2–1.4 mm / 12–15 ribs; plate L×W derived from canon DIN-format case 350×175×190 (6 cells, cell pitch 58.3 mm → plate 160×146 mm); Suzuki Battery engineering blog (PbO2 positive / sponge lead negative): https://patents.google.com/patent/CN112103513A/en (проверено 2026-11-05)
- Материалы: реальные данные/материалы/

- Wikipedia — Lead–acid battery (E°cell = 2.05 В; КПД заряда/разряда 50–95 %; реакции пластин Pb/PbO2): https://en.wikipedia.org/wiki/Lead%E2%80%93acid_battery (обращение 2026-11-07)
- Battery University BU-802a — How does Rising Internal Resistance Affect Performance (I²R — принятая производителями оценка тепловыделения при разряде): https://batteryuniversity.com/article/bu-802a-how-does-rising-internal-resistance-affect-performance (обращение 2026-11-07)