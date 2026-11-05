#!/usr/bin/env python3
"""#256 фикс ссылок после переноса: пересчёт ../-ссылок от СТАРОГО каталога файла
+ починка исторически битой кросс-зонной ссылки на модели/ в обёртках."""
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MODELS_ROOT = REPO / "фантастические данные" / "модели"

# стем модели → имя каталога обёртки внутри реализация/
IMPL = {
    "t600": "t600", "t800": "t800", "t850": "t850", "t_x": "tx",
    "cameron_phillips": "cameron", "rev9": "rev9", "marcus_wright": "marcuswright",
    "hk_tank": "hktank", "hk_aerial": "hkaerial", "t1000": "t1000", "t1001": "t1001",
}

LINK_RE = re.compile(r"\((\.\./[^)\s]*(?:%20[^)\s]*)*)\)")


def rewrite(new_file: Path, old_dir: Path) -> int:
    text = new_file.read_text(encoding="utf-8")
    n = 0

    def _sub(m: re.Match) -> str:
        nonlocal n
        old_rel = m.group(1)
        target = (old_dir / old_rel.replace("%20", " ")).resolve()
        if not target.exists():
            return m.group(0)
        new_rel = os.path.relpath(target, new_file.parent.resolve()).replace(" ", "%20")
        if new_rel != old_rel:
            n += 1
        return f"({new_rel})"

    out = LINK_RE.sub(_sub, text)
    if n:
        new_file.write_text(out, encoding="utf-8")
    return n


def main() -> int:
    total = 0
    fixed_model_links = 0
    for stem, impl in IMPL.items():
        impl_dir = MODELS_ROOT / stem / "реализация" / impl
        if not impl_dir.is_dir():
            print(f"ERROR: нет {impl_dir}")
            return 1
        for f in impl_dir.rglob("*.md"):
            # старый каталог файла = положение до git mv
            rel_under_impl = f.parent.relative_to(impl_dir)
            old_dir = REPO / "реальные данные" / "изделия" / (
                "каркас" if stem not in ("t1000", "t1001") else "вычислительная"
            ) / impl / rel_under_impl
            total += rewrite(f, old_dir)
        # починка битой ссылки на каталог моделей в обёртке
        wrapper = impl_dir / "_index.md"
        text = wrapper.read_text(encoding="utf-8")
        # старая: ../../../фантастические%20данные/модели/ (из реальные данные/изделия/<подс>/<impl>/)
        # новая от .../модели/<stem>/реализация/<impl>/: каталог моделей = ../../
        if "(../../../фантастические%20данные/модели/)" in text:
            text = text.replace("(../../../фантастические%20данные/модели/)", "(../../)")
            wrapper.write_text(text, encoding="utf-8")
            fixed_model_links += 1
    print(f"ссылок пересчитано: {total}; обёрток с починенной ссылкой на модели/: {fixed_model_links}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
