# -*- coding: utf-8 -*-
"""
Confere uma nota temática ou ficha linha a linha: cada citação [M123, p. 4] tem ID no catálogo e
página existente no PDF guardado, e os números da linha aparecem nas páginas citadas na linha (ou
no registro do catálogo, para fonte web). Não aprova nada sozinho: aponta o que conferir à mão.

Uso (a partir da raiz do repositório):
    python -I _triagem-pesquisa/_ferramentas/conferir_nota.py 04_frente-3_tendencias/ia-no-campo.md

Saída: um resumo e a lista de linhas a conferir (ID inexistente, página inexistente, número não
achado nas páginas citadas). O bloco "## Fontes" do fim da nota não é conferido.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from prechecar_dossie import NUMERO, DATAS, norm, presente, texto_paginas, paginas_citadas  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
CITACAO = re.compile(r"\[([^\[\]]*?\bM\d{3,4}\b[^\[\]]*?)\]")
PARTE = re.compile(r"(M\d{3,4})(?:,\s*([^;]+))?")


def numeros_da_linha(linha: str) -> list[str]:
    texto = CITACAO.sub(" ", linha)
    texto = re.sub(r"\(https?://[^)]+\)", " ", texto)
    for padrao in DATAS:
        texto = re.sub(padrao, " ", texto, flags=re.I)
    vistos: list[str] = []
    for tok in NUMERO.findall(texto):
        tok = tok.rstrip(".,")
        if tok and tok not in vistos and not re.fullmatch(r"[0-9]", tok):  # um dígito só: ruído demais
            vistos.append(tok)
    return vistos


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    nota = Path(sys.argv[1])
    texto = nota.read_text(encoding="utf-8").split("\n## Fontes")[0]
    catalogo = {i["id"]: i for i in json.loads((RAIZ / "_catalogo/catalogo.json").read_text(encoding="utf-8"))["itens"]}
    problemas, citacoes, linhas_com_citacao = [], 0, 0
    for n, linha in enumerate(texto.split("\n"), 1):
        grupos = CITACAO.findall(linha)
        if not grupos:
            continue
        linhas_com_citacao += 1
        paginas_da_linha: list[str] = []   # textos das páginas citadas na linha
        registros: list[str] = []          # registros do catálogo (fontes web)
        for grupo in grupos:
            for parte in grupo.split(";"):
                m = PARTE.search(parte.strip())
                if not m:
                    continue
                citacoes += 1
                ident, resto = m.group(1), (m.group(2) or "").strip()
                item = catalogo.get(ident)
                if not item:
                    problemas.append((n, f"{ident} não existe no catálogo"))
                    continue
                registros.append(norm(" ".join([item.get("titulo") or "", item.get("resumo") or "", " ".join(item.get("metricas") or [])])))
                pag = re.search(r"pp?\.\s*([\d\s,–-]+)", resto)
                if not pag:
                    continue
                arquivo = item.get("arquivo")
                textos = texto_paginas(arquivo) if arquivo else None
                if textos is None:
                    problemas.append((n, f"{ident}: página citada, mas o catálogo não tem cópia guardada"))
                    continue
                for p in paginas_citadas(pag.group(1)):
                    if p > len(textos):
                        problemas.append((n, f"{ident}, p. {p}: o arquivo tem {len(textos)} páginas"))
                    else:
                        paginas_da_linha.append(textos[p - 1])
        if not paginas_da_linha and not registros:
            continue
        alvo = " ".join(paginas_da_linha + registros)
        faltam = [t for t in numeros_da_linha(linha) if not presente(t, alvo)]
        if faltam:
            problemas.append((n, f"número(s) não achado(s) nas páginas citadas: {', '.join(faltam)}"))
    print(f"{nota.name}: {linhas_com_citacao} linhas com citação, {citacoes} citações, {len(problemas)} pontos a conferir")
    for n, p in problemas:
        print(f"  L{n}: {p}")


if __name__ == "__main__":
    main()
