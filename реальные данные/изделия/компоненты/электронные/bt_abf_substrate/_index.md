---
применяется_в_изделиях_счёт: 1
id: izdelie_bt_abf_substrate
псевдонимы: []
канонический_id: material_bt_resin
тип: изделие
уровень_иерархии: верхний
уровень_номер: 1
подсистема: компоненты
класс: композит
кристаллическая_структура: аморфный
вариант_структуры: layered_laminate_cu
оптимальная_структура:
  структура: аморфный
  обоснование_выбора: "Слоистый ламинат: жёсткое BT-ядро 0.4–0.8 мм держит плоскостность 55-мм панели и шаг BGA, тонкие ABF-слои 30–35 мкм дают мелкую топологию L/S 8–15 мкм под flip-chip площадки C4; медные полигоны питания/земли экранируют 256 ядер, низкий CTE ядра удерживает коробление при reflow"
  применение_по_умолчанию: подложка_FCBGA
  источник_обоснования: web_search
варианты_по_применению:
  ядро_BT:
    марка: 'BT-ламинат (MGC): 2–10 слоёв, L/S 30–40 мкм; Tg высокая, низкие Dk/DF'
    примечание: 'ядро 0.4–0.8 мм (INEMI large-body FCBGA substrate); по данным поставщиков Tg ядра 180–255 °C в зависимости от марки'
  build_up_ABF:
    марка: 'Ajinomoto ABF: GX-92 (стандарт), GX-T31 (низкая шероховатость/CTE), GZ-41 (низкая шероховатость, низкий CTE, высокая Tg), GL-102 (низкий Df)'
    примечание: '8–20+ build-up слоёв, L/S 8–15 мкм, трассы до 8/8 мкм; трёхслойная плёнка PET/ABF/защита; структура до 10-n-10, ленд вии от 85 мкм (Kyocera)'
исследовательская_группа: 'BT-смола: Mitsubishi Gas Chemical (MGC) — разработана и запатентована в 1978 г., коммерциализирована в 1980-е (MGC: «MGC invented a revolutionary thermal-hardened bismaleimide triazine (BT) resin»); ABF: Ajinomoto (R&D на базе аминокислотной химии с 1970-х, первая адопция крупным производителем полупроводников в 1999 г., автор — Shigeo Nakamura, с 2025 г. CEO Ajinomoto Group)'
стандарты:
  - IPC-4101 (ламинаты)
  - IPC-6012 (жёсткие платы)
  - JEDEC JESD22-A104 (термоциклирование пакета)
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
источник: web_search
источник_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10304058
источник_дата: 2026-11-06
источник_разбора: веб-верификация
ии_перепроектирован:
  статус: false
  верификация: []
canonical_inherits: material_bt_resin
наследуемые: {}
дополнительные:
  цена_usd_kg: 250
  температура_стеклования_C: {min: 150, max: 230, nominal: 200}
  температура_разложения_C: 350
  рабочая_температура_C: {min: -55, max: 150}
  толщина_ядра_мм: {min: 0.4, max: 0.8, nominal: 0.6}
  толщина_build_up_слоя_мкм: {min: 30, max: 35, nominal: 32}
  топология_L_S_мкм: {build_up: '8–15', ядро: '30–40'}
сравнение_структур: {}
дата_создания: 2026-11-06
дата_обновления: 2026-11-09
---
# Материал: пакетная подложка BT-ядро + ABF build-up (FCBGA)

## Описание

Стандартный материал высокоплотных пакетных подложек FCBGA: жёсткое ядро из BT-смолы (бисмалеимид-триазин, Mitsubishi Gas Chemical) обкладывается слоями Ajinomoto Build-up Film — эпоксидной плёнки с кремнезёмным наполнителем, специально созданной для полуб additive-процесса (SAP). FC-BGA подложки строятся «on BT resin or glass-epoxy cores using Ajinomoto Build-up Film (ABF) forming circuit traces down to 8/8 μm» (Exponential Industry, 2026); ABF работает межслойным диэлектриком над и под ядром (TheElec). BT-ядро держит 2–10 слоёв с L/S 30–40 мкм, ABF — 8–20+ слоёв с L/S 8–15 мкм (Kingsun PCB); Kyocera серийно даёт структуру до 10-n-10 слоёв с лендом вии от 85 мкм. Референс-модель FCBGA в Reliability Evaluation of Board-Level Flip-Chip Package (Shih et al., 2023) — 8-слойная build-up органическая подложка толщиной 1.2 мм; этот параметр принят для подложки чипа NorthPole с footprint 55×55 мм (референс-класс FCBGA-2743 пакета A100 PCIe). Свойства (плотность 2100 кг/м³, λ 0.5 Вт/(м·К), CTE in-plane 15 ppm/K, Tg 150–230 °C) — класс-типичные для BT/ABF-ламината с медными слоями; CTE соответствует диапазону органических пакетных подложек 14–17 ppm/K (EpoxySet). Термопластического плавления нет: термореактивный ламинат разлагается (~350 °C), поэтому температура_плавления_C = null (обоснованный null). История: BT-смола изобретена и запатентована Mitsubishi Gas Chemical в 1978 г.; ABF создана Ajinomoto (развитие аминокислотной химии с 1970-х, переход от жидких изоляторов к плёнке) и впервые принята крупным производителем полупроводников в 1999 г., после чего стала стандартом межслойного диэлектрика почти всех высокопроизводительных CPU.

## Источники

- https://pmc.ncbi.nlm.nih.gov/articles/PMC10304058 (Shih M.-K. et al., 2023: 8-слойная build-up органическая подложка толщиной 1.2 мм)
- https://exponentialindustry.com/blog/2026-08-12-fc-bga-substrates-abf-ai-packaging (BT-ядро/стекло-эпоксид + ABF, трассы до 8/8 мкм)
- https://www.thelec.net/news/articleView.html?idxno=14156 (ABF как межслойный диэлектрик над/под BT-ядром)
- https://www.kingsunpcb.com/bt-resin-package-substrate-vs-abf (BT: 2–10 слоёв, L/S 30–40 мкм; ABF: 8–20+ слоёв, L/S 8–15 мкм)
- https://www.aft-website.com/en/products/insulating_film-abf (марки ABF: GX-92, GX-T31, GZ-41, GL-102)
- https://global.kyocera.com/prdct/organic/prdct/package/fcbga/std (Kyocera FC-BGA: до 10-n-10 слоёв, ленд вии ≥85 мкм)
- https://thor.inemi.org/webdownload/newsroom/Presentations/Pkg_Substrates_Nov09/Large_body.pdf (ядро 0.4–0.8 мм, build-up слой 30–35 мкм)
- https://epoxysetinc.com/epoxy-adhesive/epoxy-underfill-for-electronics-assembly (CTE органических подложек 14–17 ppm/°C)
- https://www.mgc.co.jp/eng/rd/technology/bt.html (MGC: изобретение BT-смолы, лидерство рынка)
- https://www.ajinomoto.com/innovation/our_innovation/buildupfilm (Ajinomoto: история ABF, первая адопция 1999)
- https://www.convergenceanalysis.org/fellowships/economics/securing-the-substrate-behind-every-chip-a-us-strategy-for-ajinomoto-build-up-film-abf (Shigeo Nakamura — автор ABF)
