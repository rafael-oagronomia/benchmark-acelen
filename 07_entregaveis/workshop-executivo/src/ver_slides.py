# -*- coding: utf-8 -*-
"""Gera o HTML da apresentação executiva, imprime o PDF pelo Chrome e salva as páginas em PNG,
para conferir o desenho slide a slide antes de publicar.

Uso: python ver_slides.py <pasta de saída> [páginas...]
     python ver_slides.py C:/tmp/exec 8 19     (só as páginas 8 e 19; sem páginas, todas)

Grava <pasta>/exec.pdf e <pasta>/sNN.png. Depois, medir_folga.py <pasta>/exec.pdf mostra onde o
texto encosta na linha de fontes ou no rodapé.
"""
import subprocess
import sys
from pathlib import Path

import pymupdf

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).resolve().parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

pasta = Path(sys.argv[1])
paginas = [int(x) for x in sys.argv[2:]]
pasta.mkdir(parents=True, exist_ok=True)
subprocess.run([sys.executable, "-I", str(AQUI / "gerar_apresentacao_executiva.py")], check=True, stdout=subprocess.DEVNULL)
pdf = pasta / "exec.pdf"
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=15000",
                f"--print-to-pdf={pdf}", (AQUI / "apresentacao-executiva.html").as_uri()],
               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
doc = pymupdf.open(pdf)
for n in (paginas or range(1, doc.page_count + 1)):
    doc[n - 1].get_pixmap(dpi=88).save(pasta / f"s{n:02d}.png")
print(f"{doc.page_count} páginas em {pdf}")
