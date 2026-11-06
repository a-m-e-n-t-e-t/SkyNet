---
применяется_в_изделиях_счёт: 1
id: material_silica_aerogel_blanket
тип: материал
класс: композит
химический_состав: 'Аморфный SiO2 (>90%, нанопористый аэрогель) в армирующей стекловолоконной сетке; гидрофобизированная поверхность'
кристаллическая_структура: аморфный
вариант_структуры: single_phase
оптимальная_структура:
  структура: аморфный
  обоснование_выбора: "Нанопористость (поры ~20-100 нм < длины свободного пробега молекул воздуха) подавляет газовую теплопроводность (кнудсеновский эффект), ИК-опакеры гасят радиационный перенос при T>300°C"
  применение_по_умолчанию: высокотемпературная теплоизоляция
  источник_обоснования: web_search
варианты_по_применению:
  pyrogel_xte_промышленный_высокотемпературный:
    описание: Базовый промышленный гибкий бланкет Aspen Pyrogel XTE — аморфный SiO2-аэрогель со стеклосеткой, гидрофобизированный, с ИК-опакерами для высокотемпературного применения.
    свойства: плотность 200 кг/м3; теплопроводность (ASTM C177) 20 мВт/(м·К) при 0°C → 89 при 600°C; макс. температура 650°C (ASTM C447); прочность на сжатие 20.7 кПа при 10% (ASTM C165); толщины 5/10 мм; гидрофобен (CUI-защита); ASTM C1728 Type III Grade 1A, ASTM C795.
    применение: изоляция трубопроводов, резервуаров и оборудования нефтегаза до 650°C; до 75% тоньше конкурирующих изоляций при той же тепловой эффективности.
    источник_url: https://www.aerogel.com/product/pyrogel-xte
  cryogel_z_криогенный_с_паробарьером:
    описание: Aspen Cryogel Z — криогенный бланкет для суб-ambient применений, с интегральным паробарьером (нулевая паропроницаемость) и максимальной гибкостью при низких температурах.
    свойства: плотность 10.0 lb/ft3 (160 кг/м3); диапазон применения до −270°C…+125°C (257°F); толщины 5/10 мм; гидрофобен; нулевая паропроницаемость; измерения CEC-ICMC 2019 (CERN) — k 0.2 мВт/(м·К) при 10 К → 50 мВт/(м·К) при 273 К.
    применение: LNG-производство и хранение, криогенные трубопроводы, минимизация heat-gain и boil-off; до 50% меньше теплопритока против обычной изоляции.
    источник_url: https://www.pacorinc.com/aerogel-insulation-aspen-aerogels-products-cryogel-and-cryogel-z-aerogel-insulation
  spaceloft_строительный_тонкий:
    описание: Aspen Spaceloft — строительный гибкий бланкет для внутренней теплоизоляции ограждающих конструкций в стеснённых условиях.
    свойства: теплопроводность 15.0 мВт/(м·К); гибкий, режется ножом; серый цвет; толщины от 5 мм; еврокласс пожарных характеристик (European datasheet); гидрофобен.
    применение: внутренняя обшивка стен/полов/крыш зданий с дефицитом места — максимальное тепловое сопротивление на миллиметр толщины.
    источник_url: https://www.buyaerogel.com/wp-content/uploads/2017/09/Spaceloft-European-Datasheet-EN.pdf
  pyrogel_xtf_пассивная_огнезащита:
    описание: Aspen Pyrogel XTF — вариант бланкета для пассивной огнезащиты, сочетающий классическую теплоизоляцию аэрогелем с огнестойкими характеристиками.
    свойства: рабочий диапазон от ambient до 650°C (1200°F); exceptional passive fire protection; гибкий бланкет на основе SiO2-аэрогеля и стекловолокна.
    применение: пассивная огнезащита конструкций и оборудования (обвалование, переборки, технологические узлы) одновременно с теплоизоляцией.
    источник_url: https://www.agitec-aerogel.de/page/PDF-Dateien/Technische-Merkblaetter/Pyrogel-XTF-datasheet-Rev-4.2-EN.pdf
  гидрофобизированный_силилированный_состав:
    описание: Вариант состава аэрогеля по гидрофобности — нативный гидрофильный (силанольные Si-OH группы, сорбирует воду) против силилированного гидрофобного (ТМCS/МТМС, замена ~20-30% OH-групп делает гель водостойким).
    свойства: угол смачивания водой после силиляции TMCS/MTMS θ > 140° (до 155° при 100% MTMS); адсорбированная вода падает с 8.256% до 0.036% при росте доли MTMS 0→100%; мезопористая сеть сохраняется.
    применение: гидрофобная модификация обязательна для наружной изоляции и CUI-защиты; нативный гидрофильный аэрогель применяется как сорбент и в научных целях.
    источник_url: https://www.sciencedirect.com/science/article/abs/pii/S0304389420328491
исследовательская_группа: null
стандарты:
  - ASTM C1728 Type III Grade 1A
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
источник: web_search
источник_разбора: веб-верификация
ии_перепроектирован:
  статус: false
  верификация: []
основные:
  плотность_kg_m3: 200
  прочность_МПа: {min: null, max: null, nominal: null}
  предел_текучести_МПа: {min: null, max: null, nominal: null}
  модуль_упругости_ГПа: null
  коэффициент_Пуассона: null
  ударная_вязкость_Дж_см2: null
  усталостная_прочность_МПа: {min: null, max: null, nominal: null}
  температура_плавления_C: null
  теплопроводность_W_mK: 0.020
  теплоёмкость_J_kgK: 1000
  коэффициент_термического_расширения_1_K: null
  электропроводность_S_m: null
наследуемые: {}
дополнительные:
  цена_usd_kg: null
  твердость_vickers_HV: null
  твердость_rockwell_HRC: null
  твердость_по_моосу: null
  относительное_удлинение_процентов: null
  прочность_на_сжатие_kPa: 20.7
  толщины_выпуска_мм: [5, 10]
  гидрофобность: да
  макс_рабочая_температура_C: 650
сравнение_структур:
  бланкет_волокноармированный_гибкий:
    описание: Текущая форма — нанопористый аморфный SiO2-аэрогель в армирующей стекловолоконной сетке; аэрогельное тело связано волокнами, что даёт механическую прочность и гибкость.
    свойства: плотность 150-200 кг/м3; k 15-20 мВт/(м·К) при 0-25°C; гибкий, сворачивается в рулоны, устойчив к вибрации; пылевыделение сведено к минимуму связующим волокнами.
    применение: промышленная и строительная изоляция, огнезащита — там где нужны гибкость, монтаж обмоткой и стойкость к механике.
    источник_url: https://www.aerogel.com/about-aerogel
  монолит_аморфный_siO2:
    описание: Чистый монолитный аэрогель без армирования — сплошная аморфная нанопористая сеть SiO2 (поры 20-100 нм), почти прозрачная (n ≈ 1.05).
    свойства: плотность от 3 кг/м3 (ультралёгкие) до ~200 кг/м3; k до 9 мВт/(м·К) при ambient-условиях (монолит ambient-pressure drying, MIT); хрупок, низкая прочность на изгиб, дорог в крупных формах.
    применение: окна и оптические элементы, детекторы (Черенков), научные стенды — где прозрачность/минимальная k важнее механики.
    источник_url: https://dspace.mit.edu/bitstreams/3dff2c13-55d3-4de0-8c50-bba2074a40dd/download
  гранулированный_засыпной:
    описание: Засыпные гранулы/частицы аэрогеля — полусферические фракции для полостного заполнения; теплопроводность слоя выше монолита из-за межзеренных контактов и газовых зазоров.
    свойства: насыпная теплопроводность выше монолитной (Neugebauer 2014, Energy and Buildings); светопрозрачные гранулы для светопрозрачных ограждений; засыпается в полости любой геометрии.
    применение: засыпная изоляция полостей стен, стеклопакеты и светопрозрачные конструкции, заполнение сложных полостей где бланкет не укладывается.
    источник_url: https://www.sciencedirect.com/science/article/abs/pii/S0378778814003351
дата_создания: 2026-11-05
дата_обновления: 2026-11-06
источник_url: https://www.aerogel.com/product/pyrogel-xte
источник_дата: 2026-11-05
---

# Материал: Гибкий аэрогель-бланкет на основе диоксида кремния (Pyrogel XTE)

## Описание

Промышленный гибкий изоляционный бланкет Aspen Aerogels Pyrogel XTE: нанопористый аморфный SiO2-аэрогель, армированный стекловолоконной сеткой. Плотность 12.5 lb/ft3 (0.20 г/см3 = 200 кг/м3). Теплопроводность (ASTM C177): 20 мВт/(м·К) при 0°C, 23 при 100°C, 28 при 200°C, 35 при 300°C, 46 при 400°C, 64 при 500°C, 89 при 600°C. Максимальная температура применения 1200°F (650°C) по ASTM C447. Толщины выпуска 5 и 10 мм. Прочность на сжатие ≥3 psi (20.7 кПа) при 10% деформации (ASTM C165). Гидрофобен (защита от коррозии под изоляцией, CUI). До 75% тоньше конкурирующих изоляций при той же тепловой эффективности; соответствует ASTM C1728 Type III Grade 1A.

## Источники

- Aspen Aerogels — Pyrogel XTE product page (max use temp 1200°F/650°C, density 12.5 lb/ft3, k=20-89 мВт/м·К при 0-600°C, толщины 5/10 мм, прочность на сжатие 20.7 кПа): https://www.aerogel.com/product/pyrogel-xte
- Insulcon — Aerogel insulation -200°C up to 650°C (ASTM C1728 Type III Grade 1A): https://www.insulcon.com/products/aerogel-calcium-silicate-microporous/aerogel-aerogel-insulation-200c-up-to-650c
- Pacor — Cryogel Z industrial insulation (max use 257°F/125°C, thicknesses 5/10 mm, integral vapor barrier, zero water vapor permeability): https://www.pacorinc.com/aerogel-insulation-aspen-aerogels-products-cryogel-and-cryogel-z-aerogel-insulation
- General Insulation — Cryogel Z blanket (density 10.0 lb/ft3 = 160 kg/m3, hydrophobic): https://www.generalinsulation.com/products/mechanical-insulation-products/insulation-types/aerogel-commercial-insulation/cryogel
- CERN CEC-ICMC 2019 (Ilardi) — Cryogel Z k measured 0.2 mW/mK @10 K to 50 mW/mK @273 K: https://indico.cern.ch/event/760666/contributions/3390739/attachments/1884474/3105853/20190722-Ilardi-Oral_CEC-ICMC2019-Cryogel-v2htk.pdf
- Aspen Aerogels — Spaceloft European datasheet (k = 15.0 mW/m-K, flexible nanoporous blanket): https://www.buyaerogel.com/wp-content/uploads/2017/09/Spaceloft-European-Datasheet-EN.pdf
- Agitec — Pyrogel XTF datasheet Rev 4.2 (passive fire protection, ambient to 650°C/1200°F): https://www.agitec-aerogel.de/page/PDF-Dateien/Technische-Merkblaetter/Pyrogel-XTF-datasheet-Rev-4.2-EN.pdf
- Çok et al. 2021, J. Hazard. Mater. — TMCS/MTMS silylated silica aerogels hydrophobicity θ > 140°: https://www.sciencedirect.com/science/article/abs/pii/S0304389420328491
- Neugebauer et al. 2014, Energy and Buildings — granular aerogel bed k higher than monolithic: https://www.sciencedirect.com/science/article/abs/pii/S0378778814003351
- MIT thesis (Neugebauer 2013) — ambient-pressure-dried monolithic silica aerogel k down to 9 mW/m-K: https://dspace.mit.edu/bitstreams/3dff2c13-55d3-4de0-8c50-bba2074a40dd/download
- Aspen Aerogels — About Aerogel (refractive index ~1.05, nearly transparent, k lower than still air): https://www.aerogel.com/about-aerogel
