#!/usr/bin/env python3
"""CI: comprueba que todos los enlaces markdown relativos resuelven a un fichero existente."""
import os
import re
import glob
import sys

md = [f for f in glob.glob("**/*.md", recursive=True)
      if "/.git/" not in f and not f.startswith(".git")]
link_re = re.compile(r'\]\(([^)]+)\)')

broken = []
for f in md:
    d = os.path.dirname(f) or "."
    text = open(f, encoding="utf-8").read()
    for m in link_re.finditer(text):
        dest = m.group(1).strip()
        if dest.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path = dest.split("#")[0]
        if not path:
            continue
        if not os.path.exists(os.path.normpath(os.path.join(d, path))):
            broken.append(f"{f} -> {dest}")

print(f".md escaneados: {len(md)} | enlaces relativos rotos: {len(broken)}")
for b in broken:
    print("  ROTO:", b)
sys.exit(1 if broken else 0)
