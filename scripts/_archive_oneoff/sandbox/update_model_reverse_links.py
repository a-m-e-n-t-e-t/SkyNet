#!/usr/bin/env python3
"""SkyNet — Обновление reverse-links в файлах моделей.

Для каждой модели из фантастические данные/модели/<file>.md:
  1. Извлекает обратный список work_id на основе YAML в work-файлах
     (поле модели_в_произведении в фантастические данные/произведения/work_XXX.md)
  2. Обновляет YAML-поле `произведения: [...]` в файле модели
  3. Обновляет markdown-секцию `## Произведения, где появляется`,
     добавляя markdown-ссылки на ../произведения/work_XXX.md
  4. Обновляет `дата_обновления` в YAML

Также обновляет фантастические данные/_индекс.md (тематический указатель моделей),
добавляя колонку «встречается в N произведениях».
"""

from __future__ import annotations
import os
import re
import json
import yaml
from pathlib import Path
from collections import defaultdict

# === Пути ===
REPO = Path("/home/z/my-project/skynet_clone/SkyNet")
MODELS_DIR = REPO / "фантастические данные" / "модели"
WORKS_DIR = REPO / "фантастические данные" / "произведения"
INDEX_PATH = REPO / "фантастические данные" / "_индекс.md"
LIST_PATH = REPO / "фантастические данные" / "_список_моделей.md"
TODAY = "2026-11-03"

# === 1. Простой YAML front-matter парсер (для чтения) ===
def read_yaml_frontmatter(filepath: Path) -> tuple[dict, str, str]:
    """Возвращает (yaml_data, yaml_text, body_text).
    
    yaml_data — словарь полей верхнего уровня
    yaml_text — исходный YAML-блок (без --- ограничителей)
    body_text — тело markdown после закрывающего ---
    """
    text = filepath.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, "", text
    # Найти закрывающий --- (с переносом строки)
    end_match = re.search(r"\n---\s*\n", text[3:])
    if not end_match:
        return {}, "", text
    yaml_text = text[3:3 + end_match.start()]
    body_text = text[3 + end_match.end():]
    
    # Простой парсинг верхнего уровня
    data = {}
    for line in yaml_text.split("\n"):
        if ":" in line and not line.startswith(" ") and not line.startswith("#"):
            key, val = line.split(":", 1)
            data[key.strip()] = val.strip()
    return data, yaml_text, body_text


# === 2. Построение обратного индекса model_id → [work_id, ...] ===
def build_reverse_index() -> dict[str, list[str]]:
    """Сканирует все work_*.md и возвращает {model_id: [work_id, ...]}."""
    # model_id → work_id list
    rev: dict[str, list[str]] = defaultdict(list)
    
    # Map: model_id → model_filename (для проверки существования модели)
    id_to_file: dict[str, str] = {}
    for f in MODELS_DIR.glob("*.md"):
        if f.name.startswith("_"):
            continue
        data, _, _ = read_yaml_frontmatter(f)
        mid = data.get("id")
        if mid:
            id_to_file[mid] = f.name
    
    # Парсим все work-файлы
    work_titles: dict[str, dict] = {}  # work_id → {title, year, type, canonicity}
    for wf in sorted(WORKS_DIR.glob("work_*.md")):
        data, _, _ = read_yaml_frontmatter(wf)
        wid = data.get("id", "")  # SkyNet-Work-XXX
        # Извлечь work_XXX
        m = re.match(r"SkyNet-Work-(\d+)", wid or "")
        if not m:
            continue
        work_id = f"work_{m.group(1)}"
        
        work_titles[work_id] = {
            "title": data.get("название", "").strip('"'),
            "year": data.get("год", ""),
            "type": data.get("категория", ""),
            "canonicity": data.get("каноничность", ""),
        }
        
        # Извлечь модели_в_произведении
        models_field = data.get("модели_в_произведении", "")
        # Формат: ["SkyNet-T800", "SkyNet-T600", ...]
        model_ids = re.findall(r'"(SkyNet-[A-Za-z0-9]+)"', models_field)
        for mid in model_ids:
            if mid in id_to_file:  # только если модель существует
                rev[mid].append(work_id)
    
    # Сортируем work_id в числовом порядке
    def work_sort_key(wid: str) -> int:
        m = re.match(r"work_(\d+)", wid)
        return int(m.group(1)) if m else 0
    
    for mid in rev:
        rev[mid] = sorted(set(rev[mid]), key=work_sort_key)
    
    # Сохранить work_titles для последующего использования
    build_reverse_index.work_titles = work_titles
    build_reverse_index.id_to_file = id_to_file
    return dict(rev)


# === 3. Обновление одного файла модели ===
def update_model_file(filepath: Path, model_id: str, work_ids: list[str],
                      work_titles: dict[str, dict]) -> bool:
    """Обновляет YAML и markdown в файле модели.
    
    Возвращает True, если файл был изменён.
    """
    text = filepath.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    
    # Найти конец YAML
    end_match = re.search(r"\n---\s*\n", text[3:])
    if not end_match:
        return False
    yaml_end_pos = 3 + end_match.start()
    body_start_pos = 3 + end_match.end()
    yaml_text = text[3:yaml_end_pos]
    body = text[body_start_pos:]
    
    new_yaml = yaml_text
    changed = False
    
    # 3a. Обновить `произведения: [...]` в YAML
    yaml_works_str = "[" + ", ".join(f'"{w}"' for w in work_ids) + "]" if work_ids else "[]"
    new_yaml, n_sub = re.subn(
        r'^произведения:\s*\[.*?\]\s*$',
        f'произведения: {yaml_works_str}',
        new_yaml,
        count=1,
        flags=re.MULTILINE,
    )
    if n_sub == 0:
        # Поля нет — добавим после id
        new_yaml = re.sub(
            r'^(id:\s*SkyNet-[^\n]+\n)',
            rf'\1произведения: {yaml_works_str}\n',
            new_yaml,
            count=1,
            flags=re.MULTILINE,
        )
    if new_yaml != yaml_text:
        changed = True
    
    # 3b. Обновить `дата_обновления`
    new_yaml2, n_sub = re.subn(
        r'^дата_обновления:\s*\d{4}-\d{2}-\d{2}\s*$',
        f'дата_обновления: {TODAY}',
        new_yaml,
        count=1,
        flags=re.MULTILINE,
    )
    if n_sub > 0:
        new_yaml = new_yaml2
        changed = True
    
    # 3c. Обновить markdown-секцию «Произведения, где появляется»
    # Новая секция:
    if work_ids:
        lines = ["", "## Произведения, где появляется", ""]
        for wid in work_ids:
            wt = work_titles.get(wid, {})
            title = wt.get("title", "")
            year = wt.get("year", "")
            canon = wt.get("canonicity", "")
            canon_marker = "✅" if canon == "canon" else "📚"
            num = wid.split("_")[1]
            fname = f"work_{num}.md"
            link = f"../произведения/{fname}"
            lines.append(
                f"- {canon_marker} `{wid}` — «{title}» ({year}) → [`{fname}`]({link})"
            )
        lines.append("")
    else:
        lines = ["", "## Произведения, где появляется", "",
                 "_Модель не связана ни с одним произведением в реестре._", ""]
    
    new_section = "\n".join(lines)
    
    # Заменить существующую секцию или добавить новую (перед "## Источники" если её нет)
    # Паттерн: ## Произведения, где появляется ... (до следующего ## или конца)
    sec_pattern = re.compile(
        r'## Произведения, где появляется[^\n]*\n(.*?)(?=\n## |\Z)',
        re.DOTALL,
    )
    
    new_body = body
    if sec_pattern.search(body):
        # Заменить существующую секцию, сохранив заголовок и контент
        new_body = sec_pattern.sub(
            lambda m: "## Произведения, где появляется\n" + new_section.split("## Произведения, где появляется\n", 1)[1],
            body,
            count=1,
        )
        # Убираем лишний пробельный хвост
        new_body = re.sub(r'\n{3,}$', '\n\n', new_body)
    else:
        # Секции нет — добавить перед "## Источники" (если есть) или в конец
        if re.search(r'^## Источники', new_body, re.MULTILINE):
            new_body = re.sub(
                r'^(## Источники)',
                new_section.rstrip() + "\n\n" + r"\1",
                new_body,
                count=1,
                flags=re.MULTILINE,
            )
        else:
            new_body = new_body.rstrip() + "\n\n" + new_section
    
    if new_body != body:
        changed = True
    
    if not changed:
        return False
    
    # Собрать новый файл
    new_text = "---\n" + new_yaml + "\n---\n" + new_body
    filepath.write_text(new_text, encoding="utf-8")
    return True


# === 4. Обновление _индекс.md ===
def update_models_index(rev_index: dict[str, list[str]],
                         work_titles: dict[str, dict],
                         id_to_file: dict[str, str]) -> bool:
    """Обновляет _индекс.md, добавляя число произведений к каждой записи.
    
    Формат строки:
    - **SkyNet-T70** — игра: T2 3D: Battle Across Time (1996) → `t70.md`
    
    Новый формат:
    - **SkyNet-T70** — игра: T2 3D: Battle Across Time (1996) → `t70.md` · **в 3 произведениях**
    """
    if not INDEX_PATH.exists():
        print(f"  ⚠️ {INDEX_PATH} не найден")
        return False
    
    text = INDEX_PATH.read_text(encoding="utf-8")
    new_text = text
    
    # Найти все строки вида:
    # - **SkyNet-XXX** — ... → `file.md`
    pattern = re.compile(
        r'^(- \*\*SkyNet-[A-Za-z0-9]+\*\* — [^\n]+? → `[^`]+\.md`)(.*)$',
        re.MULTILINE,
    )
    
    def replace_match(m: re.Match) -> str:
        prefix = m.group(1)
        rest = m.group(2)
        # Извлечь SkyNet-ID из строки
        id_match = re.search(r'\*\*(SkyNet-[A-Za-z0-9]+)\*\*', prefix)
        if not id_match:
            return m.group(0)
        mid = id_match.group(1)
        n = len(rev_index.get(mid, []))
        # Удалить старый хвост «· в N произведениях» если есть
        rest_clean = re.sub(r'\s*·\s*\*\*в \d+ произведени\w*\*\*', '', rest)
        if n == 0:
            return prefix + rest_clean
        word = "произведении" if n == 1 else "произведениях"
        return prefix + rest_clean + f" · **в {n} {word}**"
    
    new_text = pattern.sub(replace_match, new_text)
    
    # Обновить header — обновить дату
    new_text = re.sub(
        r'^# Обновлено: \d{4}-\d{2}-\d{2}',
        f'# Обновлено: {TODAY}',
        new_text,
        count=1,
        flags=re.MULTILINE,
    )
    
    if new_text != text:
        INDEX_PATH.write_text(new_text, encoding="utf-8")
        return True
    return False


# === 5. Обновление _список_моделей.md ===
def update_models_list(rev_index: dict[str, list[str]],
                        id_to_file: dict[str, str]) -> bool:
    """Обновляет _список_моделей.md, добавляя колонку N_произведений."""
    if not LIST_PATH.exists():
        return False
    
    text = LIST_PATH.read_text(encoding="utf-8")
    new_text = text
    
    # Обновить header
    new_text = re.sub(
        r'^# Обновлено: \d{4}-\d{2}-\d{2}',
        f'# Обновлено: {TODAY}',
        new_text,
        count=1,
        flags=re.MULTILINE,
    )
    
    # Найти строки таблицы
    # | SkyNet-T70 | `t70.md` | гуманоидный | гуманоидный | T2 3D: Battle Across Time (1996) | canon |
    # Добавить колонку N_произведений перед статусом_реальности
    row_pattern = re.compile(
        r'^(?P<prefix>\|\s*SkyNet-[A-Za-z0-9]+\s*\|\s*`[^`]+\.md`\s*\|\s*[^|]+\|\s*[^|]+\|\s*[^|]+\|\s*)(?P<status>[^|]+)\|$',
        re.MULTILINE,
    )
    
    def replace_row(m: re.Match) -> str:
        prefix = m.group("prefix")
        status = m.group("status").strip()
        id_match = re.search(r'(SkyNet-[A-Za-z0-9]+)', prefix)
        if not id_match:
            return m.group(0)
        mid = id_match.group(1)
        n = len(rev_index.get(mid, []))
        return f"{prefix}{n} | {status} |"
    
    # Если колонка уже добавлена — не дублировать
    if "| N_произведений |" not in new_text and "N_произведений" not in new_text:
        # Добавить колонку в header
        header_pattern = re.compile(
            r'^(\| id \| имя_файла \| класс \| тип_модели \| канон_источник \|)( статус_реальности \|)$',
            re.MULTILINE,
        )
        new_text = header_pattern.sub(
            r'\1 N_произведений |\2', new_text
        )
        # Добавить разделитель
        sep_pattern = re.compile(r'^(\|---\|---\|---\|---\|---\|)(---\|)$', re.MULTILINE)
        new_text = sep_pattern.sub(r'\1---\|\2', new_text)
        # Обновить строки
        new_text = row_pattern.sub(replace_row, new_text)
    else:
        # Уже есть колонка — просто обновить значения
        # TODO: для простоты предполагаем что добавили впервые
        pass
    
    if new_text != text:
        LIST_PATH.write_text(new_text, encoding="utf-8")
        return True
    return False


# === 6. Main ===
def main():
    print("=== SkyNet reverse-link updater ===")
    print()
    
    # 1. Построить обратный индекс
    rev_index = build_reverse_index()
    work_titles = build_reverse_index.work_titles
    id_to_file = build_reverse_index.id_to_file
    
    print(f"Обратный индекс построен:")
    print(f"  Моделей в индексе: {len(rev_index)}")
    print(f"  Всего моделей (с id): {len(id_to_file)}")
    print(f"  Work-файлов: {len(work_titles)}")
    
    # 2. Проверить, какие модели без reverse-link
    no_links = [mid for mid in id_to_file if mid not in rev_index]
    if no_links:
        print(f"  ⚠️ Модели без reverse-links: {no_links}")
    
    # 3. Обновить каждый файл модели
    print()
    print(f"Обновление файлов моделей:")
    updated_count = 0
    for mid, fname in sorted(id_to_file.items()):
        fpath = MODELS_DIR / fname
        work_ids = rev_index.get(mid, [])
        old_data, _, _ = read_yaml_frontmatter(fpath)
        old_yaml_works = old_data.get("произведения", "")
        old_works_list = re.findall(r'"(work_\d+)"', old_yaml_works)
        changed = update_model_file(fpath, mid, work_ids, work_titles)
        delta = len(work_ids) - len(old_works_list)
        status = "✓ updated" if changed else "  (no change)"
        delta_str = f" (+{delta})" if delta > 0 else (f" ({delta})" if delta < 0 else "")
        print(f"  {status} {fname:25s} → {len(work_ids)} works{delta_str}")
        if changed:
            updated_count += 1
    print(f"\nОбновлено файлов моделей: {updated_count}/{len(id_to_file)}")
    
    # 4. Обновить _индекс.md (тематический указатель моделей)
    print()
    print("Обновление _индекс.md (модели)...")
    if update_models_index(rev_index, work_titles, id_to_file):
        print("  ✓ _индекс.md обновлён")
    else:
        print("  (нет изменений)")
    
    # 5. Обновить _список_моделей.md
    print()
    print("Обновление _список_моделей.md...")
    if update_models_list(rev_index, id_to_file):
        print("  ✓ _список_моделей.md обновлён")
    else:
        print("  (нет изменений)")
    
    # 6. Сводка
    print()
    print("=== Сводка ===")
    total_links = sum(len(v) for v in rev_index.values())
    print(f"  Всего моделей: {len(id_to_file)}")
    print(f"  Моделей с reverse-links: {len(rev_index)}")
    print(f"  Всего reverse-links (model→work): {total_links}")
    avg = total_links / max(1, len(rev_index))
    print(f"  Среднее число произведений на модель: {avg:.1f}")
    
    # Топ-5 моделей по числу произведений
    print()
    print("Топ-5 моделей по числу произведений:")
    top = sorted(rev_index.items(), key=lambda kv: -len(kv[1]))[:5]
    for mid, works in top:
        print(f"  {mid} ({id_to_file[mid]:25s}) → {len(works)} произведений")

if __name__ == "__main__":
    main()
