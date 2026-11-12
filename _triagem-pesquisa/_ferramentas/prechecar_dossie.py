# -*- coding: utf-8 -*-
"""
Pré-checagem de um dossiê de pesquisa: procura cada número das evidências e das métricas na
página citada do PDF guardado. Não aprova nada: só mostra ao verificador onde olhar primeiro.

Uso (a partir de _triagem-pesquisa/):
    python -I _ferramentas/prechecar_dossie.py _dossies/_bruto_campo_A.json

Grava _dossies/_prechecagem_<tema>.json (o nome do bruto com "_bruto_" trocado por
"_prechecagem_"), com a contagem por situação e a lista "revisar":
- "ok": todos os números da frase estão na página citada;
- "número só na página vizinha": achado a até duas páginas da citada (página provavelmente errada);
- "número não achado na página": falta algum número (datas por extenso, números por extenso,
  tabelas em imagem e erros de página caem aqui);
- "sem número": frase sem número (o verificador lê a página);
- "web": fonte sem PDF guardado (o verificador abre a página);
- "arquivo ou página inexistente".
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

import pymupdf

pymupdf.TOOLS.mupdf_display_errors(False)
RAIZ = Path(__file__).resolve().parent.parent
_paginas: dict[str, list[str] | None] = {}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).replace("­", "").replace(" ", " ").replace(" ", " ")
    s = re.sub(r"(?<=\d)[  ](?=\d{3}\b)", "", s)  # 1 234 -> 1234
    return re.sub(r"\s+", " ", s).lower()


def texto_paginas(arquivo: str) -> list[str] | None:
    if arquivo not in _paginas:
        caminho = RAIZ / arquivo
        try:
            doc = pymupdf.open(caminho)
            _paginas[arquivo] = [norm(p.get_text()) for p in doc]
        except Exception:
            _paginas[arquivo] = None
    return _paginas[arquivo]


def paginas_citadas(pagina: str) -> list[int]:
    nums: list[int] = []
    for a, b in re.findall(r"(\d+)\s*(?:[-–]\s*(\d+))?", str(pagina)):
        a = int(a)
        b = int(b) if b else a
        if b < a or b - a > 30:
            b = a
        nums.extend(range(a, b + 1))
    return sorted(set(nums))


NUMERO = re.compile(r"(?<![A-Za-zÀ-ÿ\d])\d+(?:[.,]\d+)*(?![A-Za-zÀ-ÿ\d])")  # fora de nomes como a16z, T50, 4G


def variantes(tok: str) -> set[str]:
    """Grafias do mesmo número em português e em inglês.
    '1.234' -> 1234, 1,234; '3,5' -> 3.5; '1.234,5' -> 1234.5, 1,234.5; '0,0200' -> 0.0200."""
    v = {tok}
    grupos = re.split(r"[.,]", tok)
    seps = re.findall(r"[.,]", tok)
    if len(grupos) == 1:
        return v
    milhar = (not grupos[0].startswith("0") and len(grupos[0]) <= 3
              and all(len(g) == 3 for g in grupos[1:-1]))
    if milhar and len(grupos[-1]) == 3 and len(set(seps)) == 1:     # 1.234 ou 1,234 (milhar)
        inteiro = "".join(grupos)
        v |= {inteiro, ",".join(grupos), ".".join(grupos)}
    if len(set(seps)) == 2 and milhar:                               # 1.234,5 ou 1,234.5
        inteiro, dec = "".join(grupos[:-1]), grupos[-1]
        v |= {f"{inteiro}.{dec}", f"{inteiro},{dec}", f"{','.join(grupos[:-1])}.{dec}", f"{'.'.join(grupos[:-1])},{dec}"}
    if len(grupos) == 2:                                             # decimal: 3,5 <-> 3.5
        v |= {f"{grupos[0]}.{grupos[1]}", f"{grupos[0]},{grupos[1]}"}
    return v


DATAS = [
    r"\b\d{1,2}/\d{1,2}/\d{2,4}\b",                          # 01/12/2022
    r"\b\d{4}/\d{2,4}\b",                                     # safra 2025/26
    r"\b\d{1,2}/\d{4}\b",                                     # 12/2024
    r"\b(?:jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)\w*/\d{2,4}\b",
    r"\b(?:19|20)\d{2}\b",                                    # anos: o verificador confere a data
]


def numeros(frase: str) -> list[str]:
    frase = re.sub(r"\[M\d+[^\]]*\]", " ", frase)            # citações não contam
    frase = re.sub(r"\bp\.\s*\d+(?:\s*[-–]\s*\d+)?", " ", frase)
    for padrao in DATAS:
        frase = re.sub(padrao, " ", frase, flags=re.I)
    vistos: list[str] = []
    for tok in NUMERO.findall(frase):
        tok = tok.rstrip(".,")
        if tok and tok not in vistos:
            vistos.append(tok)
    return vistos


def presente(tok: str, texto: str) -> bool:
    for v in variantes(tok):
        zeros = "0*" if re.search(r"[.,]\d+$", v) else ""   # 950.516,6 também acha 950.516,60
        if re.search(rf"(?<![\d]){re.escape(v)}{zeros}(?![\d])", texto):
            return True
    return False


def checar(frase: str, arquivo: str | None, pagina: str) -> dict:
    if not arquivo or str(arquivo).startswith("http") or str(pagina).strip().lower() in ("web", ""):
        return {"situacao": "web"}
    pags = texto_paginas(arquivo)
    citadas = paginas_citadas(pagina)
    if pags is None or not citadas or max(citadas) > len(pags):
        return {"situacao": "arquivo ou página inexistente", "paginas": citadas}
    toks = numeros(frase)
    if not toks:
        return {"situacao": "sem número", "paginas": citadas}
    texto = " ".join(pags[p - 1] for p in citadas)
    faltam = [t for t in toks if not presente(t, texto)]
    if not faltam:
        return {"situacao": "ok", "paginas": citadas}
    vizinhas = {}
    for t in faltam:
        perto = [p for p in range(max(1, min(citadas) - 2), min(len(pags), max(citadas) + 2) + 1)
                 if p not in citadas and presente(t, pags[p - 1])]
        if perto:
            vizinhas[t] = perto
    situacao = "número só na página vizinha" if len(vizinhas) == len(faltam) else "número não achado na página"
    return {"situacao": situacao, "faltam": faltam, "paginas": citadas, "vizinhas": vizinhas}


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    entrada = Path(sys.argv[1])
    if not entrada.is_absolute():
        entrada = RAIZ / entrada
    dossie = json.loads(entrada.read_text(encoding="utf-8"))
    catalogo = {i["id"]: i for i in json.loads((RAIZ / "_catalogo/catalogo.json").read_text(encoding="utf-8"))["itens"]}
    contagem: dict[str, int] = {}
    revisar = []

    def registrar(tipo: str, indice: int, frase: str, arquivo, pagina, extra: dict | None = None):
        r = checar(frase, arquivo, pagina)
        chave = r["situacao"] if tipo == "evidencia" else f"métrica: {r['situacao']}"
        contagem[chave] = contagem.get(chave, 0) + 1
        if r["situacao"] != "ok":
            revisar.append({"tipo": tipo, "indice": indice, "fonte": arquivo, "pagina": pagina, "afirmacao": frase, **r, **(extra or {})})

    for i, e in enumerate(dossie.get("evidencias", [])):
        arquivo = e.get("fonte")
        if e.get("id") and e["id"] in catalogo and (not arquivo or str(arquivo).startswith("http")):
            arquivo = catalogo[e["id"]].get("arquivo") or arquivo
        registrar("evidencia", i, e.get("afirmacao", ""), arquivo, e.get("pagina", ""))
    for i, it in enumerate(dossie.get("itens", [])):
        for m in it.get("metricas", []):
            pag = re.search(r"\((?:p\.|pp\.)\s*([\d\s,–-]+)\)\s*$", m)
            registrar("metrica", i, m, it.get("arquivo"), pag.group(1) if pag else "", {"item": it.get("titulo", "")[:90]})

    if "_bruto_" in entrada.name:
        saida = entrada.with_name(entrada.name.replace("_bruto_", "_prechecagem_"))
    else:  # nunca sobrescrever a entrada (ex.: rodada sobre um _verificado_)
        saida = entrada.with_name("_prechecagem_" + entrada.name.lstrip("_"))
    if saida.resolve() == entrada.resolve():
        raise SystemExit("A saída teria o mesmo nome da entrada: renomeie a entrada")
    saida.write_text(json.dumps({"contagem": contagem, "revisar": revisar}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(contagem, ensure_ascii=False, indent=1))
    print(f"Revisar: {len(revisar)} → {saida}")


if __name__ == "__main__":
    main()
