#!/usr/bin/env python3
"""CI: valida cada bloque ```mermaid``` renderizándolo con mermaid-cli (mmdc).

Requiere `mmdc` en el PATH y un puppeteer config en /tmp/pp.json con --no-sandbox.
"""
import re
import glob
import subprocess
import sys

blocks = []
for f in glob.glob("**/*.md", recursive=True):
    if "/.git/" in f or f.startswith(".git"):
        continue
    text = open(f, encoding="utf-8").read()
    for i, m in enumerate(re.finditer(r"```mermaid\n(.*?)```", text, re.S)):
        blocks.append((f, i, m.group(1)))

bad = 0
for n, (f, i, code) in enumerate(blocks):
    src = f"/tmp/diag_{n}.mmd"
    with open(src, "w", encoding="utf-8") as fh:
        fh.write(code)
    r = subprocess.run(
        ["mmdc", "-i", src, "-o", f"/tmp/diag_{n}.svg", "-p", "/tmp/pp.json"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        print(f"MERMAID INVÁLIDO: {f} (bloque {i})")
        err = (r.stderr or "") + "\n" + (r.stdout or "")
        # quédate con la primera línea de error de mermaid (Parse error / Expecting …)
        for ln in err.splitlines():
            if any(k in ln for k in ("Error", "Expecting", "Parse", "Lexical", "got '")):
                print("  >>", ln.strip())
        print(err[:1500])
        bad += 1

print(f"bloques mermaid: {len(blocks)} | inválidos: {bad}")
sys.exit(1 if bad else 0)
