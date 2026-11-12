# -*- coding: utf-8 -*-
"""
Junta os dossiês verificados de uma pesquisa dirigida num dossiê do tema (_dossies/<tema>.json),
com o ID do catálogo em cada evidência. Rodar depois de consolidar o catálogo com a rodada nova.

Uso (a partir de _triagem-pesquisa/):
    python -I _ferramentas/juntar_dossie.py ia-no-campo _dossies/_verificado_campo_A.json ...

Cada evidência ganha "id" pelo arquivo citado (ou pela URL, se for só web). Evidência sem ID no
catálogo é listada no fim (fonte que não entrou na rodada ou caminho errado). O resultado leva
também as lacunas e o resumo de cada verificação.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def norm_url(u: str) -> str:
    u = re.sub(r"^https?://(www\.)?", "", (u or "").strip().lower())
    return u.split("#")[0].rstrip("/")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    tema, entradas = sys.argv[1], sys.argv[2:]
    itens = json.loads((RAIZ / "_catalogo/catalogo.json").read_text(encoding="utf-8"))["itens"]
    por_arquivo = {i["arquivo"].replace("\\", "/").lower(): i["id"] for i in itens if i.get("arquivo")}
    por_url = {norm_url(i["url"]): i["id"] for i in itens if i.get("url")}
    evidencias, lacunas, verificacoes, sem_id = [], [], {}, []
    for arq in entradas:
        caminho = Path(arq) if Path(arq).is_absolute() else RAIZ / arq
        dossie = json.loads(caminho.read_text(encoding="utf-8"))
        verificacoes[dossie.get("tema", caminho.stem)] = dossie.get("verificacao", {})
        lacunas += dossie.get("lacunas", [])
        for e in dossie.get("evidencias", []):
            fonte = (e.get("fonte") or "").replace("\\", "/")
            ident = e.get("id") or por_arquivo.get(fonte.lower()) or por_url.get(norm_url(fonte))
            e = dict(e, id=ident, bloco=dossie.get("tema", caminho.stem))
            if not ident:
                sem_id.append(e)
            evidencias.append(e)
    saida = RAIZ / "_dossies" / f"{tema}.json"
    saida.write_text(json.dumps({"tema": tema, "evidencias": evidencias, "lacunas": lacunas, "verificacao": verificacoes},
                                ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{saida.name}: {len(evidencias)} evidências de {len({e['id'] for e in evidencias if e['id']})} fontes; sem ID: {len(sem_id)}")
    for e in sem_id[:30]:
        print(f"  sem ID: {e.get('fonte')} | {e.get('afirmacao', '')[:90]}")


if __name__ == "__main__":
    main()
