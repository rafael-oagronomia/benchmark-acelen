# -*- coding: utf-8 -*-
"""
Extrai texto de um PDF baixado para ler o conteúdo e achar métricas.

Uso:
    python texto_pdf.py ARQUIVO.pdf                      # 3 primeiras páginas
    python texto_pdf.py ARQUIVO.pdf --paginas 1-10
    python texto_pdf.py ARQUIVO.pdf --buscar ROI retorno "%" payback  # trechos com os termos (±250 caracteres)
"""
import argparse
import re
import sys
from pathlib import Path

import pymupdf as fitz

RAIZ = Path(__file__).resolve().parent.parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arquivo")
    ap.add_argument("--paginas", default="1-3")
    ap.add_argument("--buscar", nargs="*")
    ap.add_argument("--max", type=int, default=40, help="máximo de trechos na busca")
    a = ap.parse_args()
    p = Path(a.arquivo)
    if not p.is_absolute() and not p.exists():
        p = RAIZ / a.arquivo
    doc = fitz.open(p)
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"# {p.name} — {len(doc)} páginas")
    if a.buscar:
        n = 0
        for i, pg in enumerate(doc, 1):
            t = re.sub(r"\s+", " ", pg.get_text())
            for termo in a.buscar:
                for m in re.finditer(re.escape(termo), t, re.I):
                    print(f"\n[p.{i}] …{t[max(0, m.start()-250):m.end()+250]}…")
                    n += 1
                    if n >= a.max:
                        return
        return
    ini, _, fim = a.paginas.partition("-")
    ini, fim = int(ini), int(fim or ini)
    for i in range(ini - 1, min(fim, len(doc))):
        print(f"\n--- página {i+1} ---\n" + doc[i].get_text())


if __name__ == "__main__":
    main()
