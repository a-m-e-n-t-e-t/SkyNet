#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix_801.py — F22 [A-url] izdelie_SkyNet-TX

Wrapper 'работа и и/изделия/каркас/tx/_index.md': источник=web_search, но
источник_url пуст. Канон-модель t_x.md уже верифицирована ранее (URL
terminator.fandom.com/wiki/T-X, масса 150 кг подтверждена web_search
2026-11-07: 'battle chassis, weighing in excess of 150 kilos').
Прецедент: #794/#796 — wrapper получает тот же URL, что и канон.
"""
from pathlib import Path

P = Path("работа и и/изделия/каркас/tx/_index.md")

OLD = """дата_создания: 2026-11-03
дата_обновления: 2026-11-05
источник: web_search
источник_разбора: канон"""

NEW = """дата_создания: 2026-11-03
дата_обновления: 2026-11-07
источник: web_search
источник_url: https://terminator.fandom.com/wiki/T-X
источник_дата: 2026-11-07
источник_разбора: канон"""

t = P.read_text(encoding="utf-8")
n_old = t.count(OLD)
n_new = t.count(NEW)
if n_old == 1 and n_new == 0:
    P.write_text(t.replace(OLD, NEW), encoding="utf-8")
    print("PATCHED:", P)
elif n_new >= 1:
    print("SKIP (already patched)")
else:
    raise SystemExit(f"ABORT: n_old={n_old}, n_new={n_new}")
