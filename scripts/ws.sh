#!/usr/bin/env python3
"""Обёртка над z-ai web_search: чистый JSON в stdout."""
import json
import subprocess
import sys

query = sys.argv[1]
num = sys.argv[2] if len(sys.argv) > 2 else "8"
r = subprocess.run(
    ["z-ai", "function", "-n", "web_search", "-a", json.dumps({"query": query, "num": int(num)})],
    capture_output=True, text=True, timeout=120,
)
out = r.stdout
start = out.find("[")
end = out.rfind("]")
if start == -1 or end == -1:
    print(json.dumps([]))
    sys.exit(0)
try:
    data = json.loads(out[start:end + 1])
except Exception:
    print(json.dumps([]))
    sys.exit(0)
for item in data[: int(num)]:
    print(f"- {item.get('name','')[:90]}\n  {item.get('url','')}\n  {(item.get('snippet') or '')[:260]}")
