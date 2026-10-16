# -*- coding: utf-8 -*-
"""
Registra em 06_fontes/ as fontes citadas nas notas, fichas e entregáveis do benchmark.

As notas citam as fontes pelo ID estável do catálogo, no formato [M123, p. 4] ou [M123; M045, p. 2-3].
O script:
  1. procura essas citações nos .md das pastas das frentes e de entregáveis;
  2. em cada arquivo, reescreve a lista de fontes entre as marcas
         <!-- fontes:inicio -->  e  <!-- fontes:fim -->
     com organização, ano, título, link e páginas citadas (vindos do catálogo, nunca digitados à mão);
  3. gera 06_fontes/fontes-citadas.md (registro geral) e 06_fontes/fontes-citadas.json (base do assistente de IA);
  4. aponta IDs citados que não existem no catálogo.

Uso (precisa do catálogo consolidado, que fica na máquina do Guilherme):
    python 06_fontes/registrar_fontes.py            # atualiza tudo
    python 06_fontes/registrar_fontes.py --checar   # só confere, sem escrever
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CATALOGO = RAIZ / "_triagem-pesquisa" / "_catalogo" / "catalogo.json"
PASTAS = ["02_frente-1_benchmark-estrategico", "03_frente-2_maturidade-roadmaps", "04_frente-3_tendencias", "07_entregaveis"]
CITACAO = re.compile(r"\[(M\d{3,4}[^\]]*)\]")
ID = re.compile(r"M\d{3,4}")
INICIO, FIM = "<!-- fontes:inicio -->", "<!-- fontes:fim -->"


def paginas_por_id(trecho):
    """'M123, p. 4; M045, p. 2-3' -> {'M123': {'p. 4'}, 'M045': {'p. 2-3'}}"""
    saida = defaultdict(set)
    for parte in re.split(r";", trecho):
        ids = ID.findall(parte)
        pag = re.search(r"\bp\.\s*[\d\-–, e]+|\bweb\b|página oficial", parte)
        for i in ids:
            saida[i].add(pag.group(0).strip().rstrip(",") if pag else "")
    return saida


def resumir_paginas(pags):
    """{'p. 2, 4', 'p. 4', 'p. 2-3', 'web'} -> 'p. 2, 2-3, 4; web'"""
    nums, outros = set(), set()
    for p in pags:
        if not p:
            continue
        achados = re.findall(r"\d+(?:\s*[-–]\s*\d+)?", p)
        if achados:
            nums |= {re.sub(r"\s*[-–]\s*", "-", a) for a in achados}
        else:
            outros.add(p)
    partes = []
    if nums:
        partes.append("p. " + ", ".join(sorted(nums, key=lambda x: [int(n) for n in x.split("-")])))
    partes += sorted(outros)
    return "; ".join(partes)


def linha_fonte(it, pags):
    ano = it.get("ano") or "s/d"
    link = it.get("url") or ""
    pags = resumir_paginas(pags)
    onde = f" · citado em {pags}" if pags else ""
    link_md = f" [link]({link})" if link else ""
    titulo = (it.get("titulo") or "").rstrip(". ")
    return f"- **{it['id']}** — {it.get('organizacao', '')} ({ano}). {titulo}.{link_md}{onde}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--checar", action="store_true")
    a = ap.parse_args()
    if not CATALOGO.exists():
        sys.exit(f"Catálogo não encontrado: {CATALOGO} (rode o consolidar.py na máquina com os PDFs)")
    itens = {it["id"]: it for it in json.loads(CATALOGO.read_text(encoding="utf-8"))["itens"]}

    registro = defaultdict(lambda: {"arquivos": set(), "paginas": set()})
    problemas = []
    for pasta in PASTAS:
        for md in sorted((RAIZ / pasta).rglob("*.md")):
            texto = md.read_text(encoding="utf-8")
            corpo = texto.split(INICIO)[0] if INICIO in texto else texto
            citados = defaultdict(set)
            for m in CITACAO.finditer(corpo):
                for i, pags in paginas_por_id(m.group(1)).items():
                    citados[i] |= pags
            if not citados:
                continue
            rel = str(md.relative_to(RAIZ)).replace("\\", "/")
            desconhecidos = sorted(i for i in citados if i not in itens)
            if desconhecidos:
                problemas.append(f"{rel}: IDs fora do catálogo: {', '.join(desconhecidos)}")
            for i, pags in citados.items():
                registro[i]["arquivos"].add(rel)
                registro[i]["paginas"] |= {p for p in pags if p}
            if INICIO in texto and FIM in texto and not a.checar:
                linhas = [linha_fonte(itens[i], citados[i]) for i in sorted(citados, key=lambda x: int(x[1:])) if i in itens]
                novo = texto.split(INICIO)[0] + INICIO + "\n" + "\n".join(linhas) + "\n" + FIM + texto.split(FIM, 1)[1]
                if novo != texto:
                    md.write_text(novo, encoding="utf-8")
            elif INICIO not in texto:
                problemas.append(f"{rel}: sem as marcas {INICIO} / {FIM} (lista de fontes não gerada)")

    ids = sorted((i for i in registro if i in itens), key=lambda x: int(x[1:]))
    if not a.checar:
        cab = ["# Fontes citadas no benchmark", "",
               "Gerado por `06_fontes/registrar_fontes.py` a partir das citações [M###, p. N] das notas, fichas e entregáveis. "
               "Não editar à mão: corrigir a citação no documento ou o item no catálogo (`_triagem-pesquisa/`) e rodar o script de novo.", "",
               f"**{len(ids)} fontes citadas** em {len({f for r in registro.values() for f in r['arquivos']})} documentos.", "",
               "| ID | Organização | Ano | Título | Tipo | Frentes | Citado em |", "|---|---|---|---|---|---|---|"]
        for i in ids:
            it = itens[i]
            tit = it.get("titulo", "").replace("|", "/")
            tit = f"[{tit}]({it['url']})" if it.get("url") else tit
            onde = "<br>".join(f"[{Path(f).stem}](../{f})" for f in sorted(registro[i]["arquivos"]))
            cab.append(f"| {i} | {it.get('organizacao', '').replace('|', '/')} | {it.get('ano', '')} | {tit} | "
                       f"{it.get('tipo_fonte', '')} | {', '.join(it.get('frentes') or [])} | {onde} |")
        (RAIZ / "06_fontes" / "fontes-citadas.md").write_text("\n".join(cab) + "\n", encoding="utf-8")
        base = [{"id": i, "titulo": itens[i].get("titulo"), "organizacao": itens[i].get("organizacao"),
                 "ano": itens[i].get("ano"), "tipo_fonte": itens[i].get("tipo_fonte"), "url": itens[i].get("url"),
                 "frentes": itens[i].get("frentes"), "metricas": itens[i].get("metricas"), "resumo": itens[i].get("resumo"),
                 "citado_em": sorted(registro[i]["arquivos"]), "paginas_citadas": sorted(registro[i]["paginas"])} for i in ids]
        (RAIZ / "06_fontes" / "fontes-citadas.json").write_text(json.dumps(base, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({"fontes_citadas": len(ids), "problemas": problemas}, ensure_ascii=False, indent=1))
    return 1 if any("fora do catálogo" in p for p in problemas) else 0


if __name__ == "__main__":
    sys.exit(main())
