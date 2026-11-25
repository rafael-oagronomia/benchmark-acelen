# -*- coding: utf-8 -*-
"""Confere a apresentação executiva contra o material já conferido do estudo.

1. Citações: todo [M###, p. N] do deck (nos cartões e na linha de fontes) precisa existir no
   catálogo, e cada página citada precisa já estar citada para esse ID nas notas, nas fichas, na
   página Roteiro do sistema ou no Report Final.
2. Números: cada número do corpo de um slide precisa aparecer, no material conferido, numa linha
   (ou slide) que cite ao menos uma das fontes do slide. O que não bater sai numa lista para
   conferência manual (por exemplo, número lido direto na página da fonte, ou a numeração das
   perguntas do último slide).

Uso: python conferir_deck.py [deck.html]   (depois de rodar o gerador; sem argumento, confere a apresentação executiva;
     com apresentacao-executiva-ilustrada.html, a versão ilustrada)
"""
import html
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
DECK = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else AQUI / "apresentacao-executiva.html"
# A página Roteiro fica no repositório do sistema (rag-benchmark-acelen), ao lado deste.
ROTEIRO = RAIZ.parent / "rag-benchmark-acelen/web/lib/i18n/conteudo/roteiro.ts"
RF = RAIZ / "07_entregaveis/relatorio-final/src/report-final.html"

catalogo = {i["id"] for i in json.loads((RAIZ / "_triagem-pesquisa/_catalogo/catalogo.json").read_text(encoding="utf-8"))["itens"]}


def paginas(spec: str) -> set[int]:
    saida = set()
    for parte in re.findall(r"\d+(?:\s*-\s*\d+)?", spec):
        if "-" in parte:
            a, b = [int(x) for x in re.split(r"\s*-\s*", parte)]
            saida |= set(range(a, b + 1))
        else:
            saida.add(int(parte))
    return saida


def texto(h: str) -> str:
    h = re.sub(r"<(br|/p|/li|/h\d|/div|/tr|/td|/th|/text|/span)[^>]*>", " ", h)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h)))


# ---------------- material conferido ----------------
unidades: list[tuple[str, set[str], str]] = []   # (texto, IDs, origem)
pag_corpus: dict[str, set[int]] = {}
web_corpus: set[str] = set()

CIT = re.compile(r"\[((?:M\d+[^\]\[]*?))\]")


def registrar_citacoes(trecho: str) -> set[str]:
    ids = set()
    for bloco in CIT.findall(trecho):
        for parte in bloco.split(";"):
            m = re.match(r"\s*(M\d+)\s*(?:,\s*(.*))?$", parte.strip())
            if not m:
                continue
            ident, resto = m.group(1), (m.group(2) or "")
            ids.add(ident)
            if "web" in resto:
                web_corpus.add(ident)
            if "p." in resto:
                pag_corpus.setdefault(ident, set()).update(paginas(resto.split("p.", 1)[1]))
    return ids


pastas = ["02_frente-1_benchmark-estrategico/fichas-benchmark", "03_frente-2_maturidade-roadmaps", "04_frente-3_tendencias"]
for pasta in pastas:
    for arq in sorted((RAIZ / pasta).glob("*.md")):
        if "linha-de-investigacao" in arq.name or arq.name == "README.md":
            continue
        for linha in arq.read_text(encoding="utf-8").splitlines():
            ids = registrar_citacoes(linha)
            if ids:
                unidades.append((linha, ids, arq.name))

roteiro = ROTEIRO.read_text(encoding="utf-8") if ROTEIRO.exists() else ""
if not roteiro:
    print(f"Aviso: não achei a página Roteiro em {ROTEIRO}; a conferência segue só com as notas e o Report Final.")
for linha in roteiro.splitlines():
    cits = re.findall(r'\["(M\d+)",\s*(null|\d+)(?:,\s*"p\. ([^"]+)")?\]', linha)
    if not cits:
        continue
    ids = set()
    for ident, pag, faixa in cits:
        ids.add(ident)
        if pag == "null":
            web_corpus.add(ident)
        else:
            pag_corpus.setdefault(ident, set()).update(paginas(faixa) if faixa else {int(pag)})
    unidades.append((linha, ids, "roteiro.ts"))

rf = RF.read_text(encoding="utf-8")
secoes_rf = re.findall(r'<section class="([^"]*)">([\s\S]*?)</section>', rf)
for n, (_, corpo) in enumerate(secoes_rf, 1):
    ids = set()
    for ident, resto in re.findall(r'<span class="f">\[(M\d+)\]([\s\S]*?)</span>', corpo):
        ids.add(ident)
        m = re.search(r",\s*p\.\s*([\d,\s-]+)", html.unescape(re.sub(r"<[^>]+>", "", resto)))
        if m:
            pag_corpus.setdefault(ident, set()).update(paginas(m.group(1)))
        else:
            web_corpus.add(ident)
    unidades.append((texto(re.sub(r'<div class="fontes">[\s\S]*?</div>', "", corpo)), ids, f"report-final slide {n}"))

# ---------------- o deck ----------------
deck = DECK.read_text(encoding="utf-8")
secoes = re.findall(r'<section class="([^"]*)">([\s\S]*?)</section>', deck)
erros = 0
NUM = re.compile(r"(?<![\w])\d[\d.]*(?:,\d+)?")

print(f"material conferido: {len(unidades)} linhas ou slides com citação; {len(pag_corpus)} IDs com página")
for n, (classe, corpo) in enumerate(secoes, 1):
    if "cover" in classe:
        continue
    fontes_html = re.search(r'<div class="fontes">([\s\S]*?)</div>', corpo)
    cits = []
    for ident, resto in re.findall(r'<span class="f">\[(M\d+)\]([\s\S]*?)</span>', fontes_html.group(1) if fontes_html else ""):
        m = re.search(r",\s*p\.\s*([\d,\s-]+)", html.unescape(re.sub(r"<[^>]+>", "", resto)))
        cits.append((ident, m.group(1).strip() if m else "web", "fontes"))
    for bloco in re.findall(r'<(?:div|span) class="ct">([\s\S]*?)</(?:div|span)>', corpo):
        for ident, resto in re.findall(r"\[(M\d+)(?:,\s*([^\]]*))?\]", bloco):
            cits.append((ident, (resto or "web").replace("p.", "").strip(), "cartão"))
    ids_slide = {c[0] for c in cits}
    problemas = []
    for ident, spec, onde in cits:
        if ident not in catalogo:
            problemas.append(f"{ident} fora do catálogo ({onde})")
            continue
        if spec == "web":
            if ident not in web_corpus and ident not in pag_corpus:
                problemas.append(f"{ident} (web) não aparece no material conferido")
            continue
        faltam = paginas(spec) - pag_corpus.get(ident, set())
        if faltam:
            problemas.append(f"{ident}: página(s) {sorted(faltam)} sem citação anterior ({onde}); já citadas: {sorted(pag_corpus.get(ident, set()))[:14]}")
    ids_fontes = {c[0] for c in cits if c[2] == "fontes"}
    for ident in sorted({c[0] for c in cits if c[2] == "cartão"} - ids_fontes):
        problemas.append(f"{ident} citado no cartão e ausente da linha de fontes")

    # números do corpo (sem a linha de fontes, o rodapé, as citações dos cartões e a numeração das etapas)
    corpo_sem = re.sub(r'<div class="fontes">[\s\S]*?</div>', "", corpo)
    corpo_sem = re.sub(r'<div class="foot">[\s\S]*?</div>', "", corpo_sem)
    corpo_sem = re.sub(r'<(?:div|span) class="ct">[\s\S]*?</(?:div|span)>', "", corpo_sem)
    corpo_sem = re.sub(r'<div class="rt"><b>\d</b>', '<div class="rt">', corpo_sem)
    numeros = sorted({x.strip(".") for x in NUM.findall(texto(corpo_sem))}, key=lambda x: (len(x), x))
    if ids_slide:
        candidatas = [u for u in unidades if u[1] & ids_slide]
    else:  # sessões executivas e fecho: contra os slides das sessões no Report Final e o Roteiro
        candidatas = [(texto(c), set(), f"report-final slide {k}") for k, (_, c) in enumerate(secoes_rf, 1) if 40 <= k <= 47]
        candidatas.append((roteiro, set(), "roteiro.ts"))
    sem_par = []
    for num in numeros:
        if len(num) == 1:
            continue
        padrao = re.compile(r"(?<![\d.,])" + re.escape(num) + r"(?![\d]|[.,]\d)")
        if not any(padrao.search(u[0]) for u in candidatas):
            sem_par.append(num)
    titulo = texto(re.search(r"<h2[^>]*>([\s\S]*?)</h2>", corpo).group(1)).strip()
    estado = "ok" if not problemas and not sem_par else "VER"
    print(f"\n{n:02d} [{estado}] {titulo[:70]}  ({len(ids_slide)} fontes, {len(numeros)} números)")
    for p in problemas:
        erros += 1
        print("     citação:", p)
    if sem_par:
        print("     números sem par no material conferido:", ", ".join(sem_par))
print(f"\nproblemas de citação: {erros}")
