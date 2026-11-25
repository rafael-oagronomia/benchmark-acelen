# -*- coding: utf-8 -*-
"""Mede, em cada página do PDF da apresentação, a folga entre o corpo do slide e a linha de
fontes, e entre as fontes e o rodapé (em px do slide de 1280 x 720). Folga pequena ou negativa =
texto encavalado.

Serve para ajustar a ampliação de cada slide (ZOOM, em slides.py): com o corpo cheio, a folga
corpo→fontes fica perto de 30 px, e a das fontes para o rodapé, em 23 px. A capa não tem linha de
fontes e fica fora da medição.

Uso: python medir_folga.py <arquivo.pdf>
"""
import sys

import pymupdf

sys.stdout.reconfigure(encoding="utf-8")
PX = 1 / 0.75  # o PDF está em pontos; o slide, em px
for n, pagina in enumerate(pymupdf.open(sys.argv[1]), 1):
    if n == 1:
        continue
    linhas = []
    for bloco in pagina.get_text("dict")["blocks"]:
        for linha in bloco.get("lines", []):
            t = "".join(s["text"] for s in linha["spans"]).strip()
            if t:
                linhas.append((linha["bbox"][1], linha["bbox"][3], t))
    linhas.sort()
    rodape = [l for l in linhas if l[2].upper().startswith("ACELEN ENERGIA RENOV")]
    fontes = [l for l in linhas if l[2].upper().startswith("FONTES")]
    if not rodape or not fontes:
        print(f"{n:02d}  (sem fontes ou rodapé)")
        continue
    y_rodape, y_fontes = rodape[-1][0], fontes[-1][0]
    fim_corpo = max(l[1] for l in linhas if l[1] <= y_fontes + 1 and l[0] < y_fontes - 1)
    fim_fontes = max((l[1] for l in linhas if y_fontes - 1 <= l[0] < y_rodape - 1), default=y_rodape + 99)
    folga_corpo, folga_fontes = (y_fontes - fim_corpo) * PX, (y_rodape - fim_fontes) * PX
    alerta = "  <-- ENCAVALADO" if folga_corpo < 6 or folga_fontes < 4 else ""
    print(f"{n:02d}  corpo→fontes {folga_corpo:6.0f} px   fontes→rodapé {folga_fontes:5.0f} px{alerta}")
