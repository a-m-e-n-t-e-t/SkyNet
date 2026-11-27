#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Валидация системы шаблонов SkyNet (папка шаблоны/: 21 шаблон + README; карточки v10/v11).

Использование:
  python3 scripts/validate_templates.py [ПАПКА_ШАБЛОНОВ]

ПАПКА по умолчанию — ../шаблоны относительно скрипта.
Проверяет:
 1. состав: 21 шаблон + README (8 карточек + фантастический материал + обёртка §12.7
    + 10 списков + сводный реестр);
 2. строка 1 = «---»; ровно 2 «---»; внутри Markdown-тела «---» нет;
 3. YAML front matter парсится (PyYAML);
 4. v6: конструкция {min, max, nominal} запрещена (рекурсивно + по тексту);
 5. карточные шаблоны: блок-цитата («Единый источник данных»; фантастический
    материал — «Материал из канона»); чек-лист (кроме фантастического материала);
    единый блок «метаданные» с обязательными ключами (v10/v11);
 6. структурные правила v10.1/v11: материал — структурные_варианты (id/вариант/
    основной/существует, enum 14 с не_определён); изделие — оптимальная_
    структура.вариант_id; модель — поля «класс» нет, enum тип_модели (7) и
    категория (11); технология — кпд_pct, прототип; стандарт — обозначение/
    название/статус_действия; группа — специализация (список); произведение —
    категории (6, порядок v11.0); обёртка §12.7 — предок/улучшения/real_check/
    версия ии-улучшенная;
 7. списковые шаблоны: блок «метаданные» (тип_файла/генератор/охват/обновлено/
    счётчики; реестр — без домена), тело начинается с «# », чек-лист, полнота
    секций enum;
 8. README: состав 21, разделы «Правила обёрток ии-улучшения» и «Инструменты»,
    история «Списки v2 (текущая)», маркеры версий 2–6.
"""
import pathlib
import re
import sys

import yaml

BASE = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else \
    pathlib.Path(__file__).resolve().parent.parent / "шаблоны"

CARD_TEMPLATES = {
    "шаблон_материала.md", "шаблон_изделия.md", "шаблон_технологии.md",
    "шаблон_модели.md", "шаблон_реализации_модели.md", "шаблон_стандарта.md",
    "шаблон_исследовательской_группы.md", "шаблон_произведения.md",
    "шаблон_фантастического_материала.md", "шаблон_ии_улучшения.md",
}
LIST_ENUM_SECTIONS = {
    "шаблон_списка_материалов.md":
        ["металл", "сплав", "керамика", "полупроводник", "полимер",
         "композит", "радиоизотоп", "прочее"],
    "шаблон_списка_изделий.md":
        ["вычислительная", "энергетическая", "каркас", "броня", "маскировка",
         "встроенное_оружие", "сенсоры", "приводная_система", "система_связи",
         "навигация", "система_охлаждения", "система_питания",
         "система_передвижения", "прочее"],
    "шаблон_списка_технологий.md":
        ["обработка", "сборка", "испытание", "модификация", "прочее"],
    "шаблон_списка_моделей.md":
        ["стационарный", "гуманоидный", "воздушный", "наземный_гусеничный",
         "наземный_колёсный", "водный_надводный", "водный_подводный"],
    "шаблон_списка_стандартов.md": ["промышленный_стандарт", "прочее"],
    "шаблон_списка_произведений.md":
        ["фильм", "сериал", "игра", "книга", "комикс", "HTML-концепция"],
}
LIST_PLAIN = {
    "шаблон_списка_исследовательских_групп.md": ["## группы ("],
    "шаблон_списка_фантастических_материалов.md":
        ["## фантастические материалы ("],
    "шаблон_списка_частей.md": ["### izdelie_", "(уровень "],
    "шаблон_списка_реализаций.md":
        ["### реальная реализация (", "### фантастическая реализация (",
         "### доработанная ии реализация ("],
}
REGISTRY = "шаблон_сводного_реестра.md"

errors: list[str] = []
report: list[str] = []


def find_minmaxnominal(node, prefix=""):
    """Рекурсивно ищет {min, max, nominal} (v6: запрещены — одно свойство — одно значение).

    НЕ флагует легитимные конструкции: {min, target} (требования модели),
    {l, w, h} (габариты), {computed_from} (вычислимые агрегаты),
    пределы {min: {…}, max: {…}} (масштабируемость).
    """
    found: list[str] = []
    if isinstance(node, dict):
        if set(node.keys()) == {"min", "max", "nominal"}:
            found.append(prefix or "<корень>")
        for k, v in node.items():
            if isinstance(v, (dict, list)):
                found += find_minmaxnominal(v, f"{prefix}.{k}" if prefix else str(k))
    elif isinstance(node, list):
        for i, item in enumerate(node):
            if isinstance(item, (dict, list)):
                found += find_minmaxnominal(item, f"{prefix}[{i}]")
    return found


# 1. состав
expected = (CARD_TEMPLATES | set(LIST_ENUM_SECTIONS) | set(LIST_PLAIN)
            | {REGISTRY, "README.md"})
present = {p.name for p in BASE.glob("*.md")} if BASE.is_dir() else set()
for name in sorted(expected - present):
    errors.append(f"состав: отсутствует файл {name}")
for name in sorted(present - expected):
    errors.append(f"состав: лишний файл {name} (не входит в систему 21 шаблона)")
report.append(f"состав: {len(present)} файлов (ожидается {len(expected)})")

for name in sorted((expected - {"README.md"}) & present):
    path = BASE / name
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # 2. структура «---»
    if not lines or lines[0].strip() != "---":
        errors.append(f"{name}: строка 1 не '---'")
        continue
    sep_idx = [i for i, ln in enumerate(lines) if ln.strip() == "---"]
    if len(sep_idx) != 2:
        errors.append(f"{name}: ожидается ровно 2 '---', найдено {len(sep_idx)}")
        continue
    open_i, close_i = sep_idx
    body = lines[close_i + 1:]
    body_text = "\n".join(body)

    # 3. YAML front matter
    try:
        data = yaml.safe_load("\n".join(lines[1:close_i]))
    except yaml.YAMLError as exc:
        errors.append(f"{name}: YAML front matter не парсится: {exc}")
        continue
    if not isinstance(data, dict):
        errors.append(f"{name}: front matter — не словарь")
        continue

    # 4. v6: {min, max, nominal} запрещены
    for bad in find_minmaxnominal(data):
        errors.append(f"{name}: поле «{bad}» — конструкция {{min, max, nominal}} "
                      "(v6: одно свойство — одно значение)")
    if "min: null, max: null, nominal: null" in text:
        errors.append(f"{name}: в тексте осталась конструкция "
                      "{{min: null, max: null, nominal: null}} (v6)")

    if name in CARD_TEMPLATES:
        # 5. карточные шаблоны (пропускаем пустые строки после '---')
        first_body = next((ln for ln in body if ln.strip()), "")
        if not (first_body.strip().startswith("<!--") or first_body.strip().startswith("# ")):
            errors.append(f"{name}: после закрывающего '---' нет заголовка/HTML-комментария")
        if name == "шаблон_фантастического_материала.md":
            if "Материал из канона" not in body_text:
                errors.append(f"{name}: нет блок-цитаты «Материал из канона» (§12.3a)")
        elif "Единый источник данных" not in body_text:
            errors.append(f"{name}: нет блок-цитаты «Единый источник данных»")
        if name not in ("шаблон_фантастического_материала.md", "шаблон_материала.md") \
                and "Чек-лист" not in body_text:
            errors.append(f"{name}: нет чек-листа")
        meta = data.get("метаданные")
        if not isinstance(meta, dict):
            errors.append(f"{name}: нет единого блока «метаданные» (v10/v11)")
        else:
            for field in ("версия_схемы", "источник", "создано", "обновлено"):
                if field not in meta:
                    errors.append(f"{name}: в блоке метаданные нет поля «{field}» (v10/v11)")

    if name == "шаблон_материала.md":
        sv = data.get("структурные_варианты")
        if not (isinstance(sv, list) and sv and all(isinstance(v, dict) for v in sv)):
            errors.append("шаблон_материала.md: структурные_варианты — не список вариантов (v10.1)")
            sv = []
        if sv:
            for key in ("id", "вариант", "основной", "существует"):
                if key not in sv[0]:
                    errors.append(f"шаблон_материала.md: в варианте нет поля «{key}» (v10.1)")
            variant_line = next((ln for ln in lines if "вариант:" in ln and "монокристаллический" in ln), "")
            for struct in ("микрокристаллический", "полукристаллический", "нанокристаллический",
                           "молекулярный_кристалл", "не_определён"):
                if struct not in variant_line:
                    errors.append(f"шаблон_материала.md: в enum вариант нет «{struct}» (v10.1)")
        if "кристаллическая_структура" in data:
            errors.append("шаблон_материала.md: поле «кристаллическая_структура» переименовано "
                           "в структурные_варианты (v10.1)")
        if "оптимальная_структура" in data:
            errors.append("шаблон_материала.md: оптимальная_структура — в шаблоне изделия (материалы_частей)")

    if name == "шаблон_фантастического_материала.md":
        if str(data.get("класс")) != "фантастический_материал":
            errors.append("шаблон_фантастического_материала.md: класс = фантастический_материал (§12.3a)")
        if not data.get("канон_факты"):
            errors.append("шаблон_фантастического_материала.md: нет блока канон_фактов (§12.3a)")
        if str(data.get("химический_состав")) != "не_определён":
            errors.append("шаблон_фантастического_материала.md: реальный состав запрещён (состав = не_определён)")
        meta = data.get("метаданные") or {}
        if str(meta.get("реальность")) != "канон":
            errors.append("шаблон_фантастического_материала.md: метаданные.реальность = канон")

    if name == "шаблон_изделия.md":
        parts = data.get("материалы_частей")
        ok = (isinstance(parts, list) and parts and isinstance(parts[0], dict)
              and isinstance(parts[0].get("оптимальная_структура"), dict))
        if not ok:
            errors.append("шаблон_изделия.md: оптимальная_структура не вложена в материалы_частей (F62)")
        elif "вариант_id" not in parts[0]["оптимальная_структура"]:
            errors.append("шаблон_изделия.md: в оптимальная_структура нет машиночитаемой связи "
                          "вариант_id → структурные_варианты.id (v10.1)")

    if name == "шаблон_технологии.md":
        osn = data.get("основные")
        if not isinstance(osn, dict):
            errors.append("шаблон_технологии.md: нет блока основных параметров режима")
        else:
            for field in ("температура_режима_C", "давление_Pa", "время_цикла_s",
                          "кпд_pct", "производительность_шт_ч",
                          "потребление_энергии_kWh", "потребление_воды_L"):
                if field not in osn:
                    errors.append(f"шаблон_технологии.md: в основных нет поля «{field}» (v11)")
        if "прототип" not in data:
            errors.append("шаблон_технологии.md: нет поля «прототип» (v11 — для наследуемых)")

    if name == "шаблон_модели.md":
        if "класс" in data:
            errors.append("шаблон_модели.md: поле «класс» должно быть удалено (дубль тип_модели, v3)")
        tm_line = next((ln for ln in lines if ln.strip().startswith("тип_модели:")), "")
        for canon in ("стационарный", "гуманоидный", "воздушный", "наземный_гусеничный",
                      "наземный_колёсный", "водный_надводный", "водный_подводный"):
            if canon not in tm_line:
                errors.append(f"шаблон_модели.md: в enum тип_модели нет «{canon}» (§11.0)")
        kat_line = next((ln for ln in lines if ln.strip().startswith("категория:")), "")
        for fam in ("стандартный", "жидкий_металл", "ранняя_наземная", "воздушный_HK",
                    "наземный_HK", "водный_HK", "ИИ-ядро", "гибрид",
                    "альтернативный_производитель", "GRACE", "прочее"):
            if fam not in kat_line:
                errors.append(f"шаблон_модели.md: в enum категории нет «{fam}» (v3)")

    if name == "шаблон_реализации_модели.md":
        meta = data.get("метаданные") or {}
        if str(meta.get("вариант")) not in ("промышленный", "ии-улучшенный"):
            errors.append("шаблон_реализации_модели.md: метаданные.вариант = промышленный | ии-улучшенный")
        osn = data.get("основные")
        if not isinstance(osn, dict):
            errors.append("шаблон_реализации_модели.md: нет блока основных")
        else:
            for field in ("масса_kg", "выработка_энергии_W", "выработка_тепла_W"):
                if field not in osn:
                    errors.append(f"шаблон_реализации_модели.md: в основных нет поля «{field}»")

    if name == "шаблон_стандарта.md":
        for field in ("обозначение", "название", "статус_действия"):
            if field not in data:
                errors.append(f"шаблон_стандарта.md: нет поля «{field}» (v11)")

    if name == "шаблон_исследовательской_группы.md":
        if not isinstance(data.get("специализация"), list):
            errors.append("шаблон_исследовательской_группы.md: специализация — список направлений (v11)")
        if "изделий_в_группе_счёт" in data:
            errors.append("шаблон_исследовательской_группы.md: счётчик изделий_в_группе_счёт удалён (v11 — "
                          "вычисляемые значения — в списках/CI)")

    if name == "шаблон_произведения.md":
        kat_line = next((ln for ln in lines if ln.strip().startswith("категория:")), "")
        for value in ("фильм", "сериал", "игра", "книга", "комикс", "HTML-концепция"):
            if value not in kat_line:
                errors.append(f"шаблон_произведения.md: в enum категории нет «{value}» (v11)")

    if name == "шаблон_ии_улучшения.md":
        if not (data.get("предок") and str(data.get("id")).endswith("__ii")):
            errors.append("шаблон_ии_улучшения.md: id = id предка + «__ii»; поле «предок» обязательно (§12.7)")
        meta = data.get("метаданные") or {}
        if str(meta.get("версия")) != "ии-улучшенная":
            errors.append("шаблон_ии_улучшения.md: метаданные.версия = ии-улучшенная")
        if str(meta.get("статус_реальности")) != "ии-улучшенная":
            errors.append("шаблон_ии_улучшения.md: метаданные.статус_реальности = ии-улучшенная (работа и и/)")
        if str(meta.get("ии_перепроектирован")) != "да":
            errors.append("шаблон_ии_улучшения.md: метаданные.ии_перепроектирован = да")
        uluch = data.get("улучшения")
        if not (isinstance(uluch, list) and uluch and isinstance(uluch[0], dict)):
            errors.append("шаблон_ии_улучшения.md: улучшения — список ≥1 записи (§12.7)")
        elif any(k not in uluch[0] for k in ("тип", "что", "причина", "источник")):
            errors.append("шаблон_ии_улучшения.md: в записи улучшений нет тип/что/причина/источник")
        rc = data.get("real_check")
        if not (isinstance(rc, dict) and "статус" in rc and "метод" in rc):
            errors.append("шаблон_ии_улучшения.md: real_check (статус/метод) обязателен (§12.7)")

    # 7. списковые шаблоны
    if name in LIST_ENUM_SECTIONS or name in LIST_PLAIN or name == REGISTRY:
        if body and body[0].strip().startswith("<!--"):
            errors.append(f"{name}: у списков правила ведения — в комментариях front matter, "
                          "не в теле")
        meta = data.get("метаданные")
        if not isinstance(meta, dict):
            errors.append(f"{name}: нет блока «метаданные» (машиночитаемо для CI)")
        else:
            fields = ["тип_файла", "генератор", "охват", "обновлено", "счётчики"]
            if name != REGISTRY:
                fields.append("домен")   # у реестра охват — весь репозиторий, без домена
            for field in fields:
                if field not in meta:
                    errors.append(f"{name}: в метаданных нет поля «{field}»")
            if str(meta.get("генератор") or "").startswith("scripts/") and \
                    "generate_lists" not in str(meta.get("генератор")):
                errors.append(f"{name}: генератор — scripts/generate_lists.py либо вручную")
            if not isinstance(meta.get("счётчики"), dict) or not meta.get("счётчики"):
                errors.append(f"{name}: счётчики — непустой словарь (сверка — CI)")
        for value in LIST_ENUM_SECTIONS.get(name, []):
            if f"## {value} (" not in body_text:
                errors.append(f"{name}: нет секции «## {value} (N)» — полнота enum (вкл. пустые)")
        for marker in LIST_PLAIN.get(name, []):
            if marker not in body_text:
                errors.append(f"{name}: нет маркера {marker!r}")
        if "Чек-лист" not in body_text:
            errors.append(f"{name}: нет чек-листа")
        if name == REGISTRY:
            for marker in ("## Домены и типы", "## Покрытие списками"):
                if marker not in body_text:
                    errors.append(f"{name}: нет раздела {marker!r}")
            for row in ("реализация_модели", "фантастическ"):
                if row not in body_text:
                    errors.append(f"{name}: нет строки «{row}…» (v1.1)")
            if str((data.get("метаданные") or {}).get("версия_схемы")) != "1.1":
                errors.append(f"{name}: версия_схемы = 1.1 (v1.1)")

    # общие для всех шаблонов
    if any(ln.strip() == "---" for ln in body):
        errors.append(f"{name}: в Markdown-теле найден разделитель '---'")

# 8. README
readme_path = BASE / "README.md"
if readme_path.is_file():
    readme = readme_path.read_text(encoding="utf-8")
    for marker in ("Состав системы шаблонов (21)",
                   "Правила структуры файла (рендер на GitHub)",
                   "Правила сводных списков",
                   "Правила обёрток ии-улучшения",
                   "Инструменты (scripts/)",
                   "generate_lists.py",
                   "validate_templates.py",
                   "Одно значение — одно место",
                   "Одно свойство — одно значение",
                   "История исправлений",
                   "Списки v2 (2026-11-27, текущая)",
                   "Версия 6", "Версия 5", "Версия 4", "Версия 3", "Версия 2",
                   "структурные_варианты", "вариант_id",
                   "шаблон_ии_улучшения.md", "шаблон_списка_стандартов.md",
                   "шаблон_списка_исследовательских_групп.md",
                   "шаблон_списка_произведений.md",
                   "шаблон_списка_фантастических_материалов.md",
                   "шаблон_списка_реализаций.md"):
        if marker not in readme:
            errors.append(f"README.md: отсутствует маркер {marker!r}")
    for stale in ("v6 (текущая)",):
        if stale in readme:
            errors.append(f"README.md: «(текущая)» — у «Списки v2», не у v6")
    report.append(f"README.md: {len(readme)} символов")

print("=== ОТЧЁТ ===")
for line in report:
    print(" ", line)
print("=== ОШИБКИ ===" if errors else "=== ОШИБКИ: 0 (система валидна) ===")
for err in errors:
    print(" !", err)
sys.exit(1 if errors else 0)
