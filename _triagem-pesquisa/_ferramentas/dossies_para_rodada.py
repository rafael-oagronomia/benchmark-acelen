# -*- coding: utf-8 -*-
"""
Passa as fontes novas de dossiês verificados para um arquivo de rodada do catálogo
(_catalogo/rodadaN.json), no formato que o consolidar.py lê:
{"resultados": [{"grupo", "pasta", "itens", "formularios", "lacunas"}]}.

Uso (a partir de _triagem-pesquisa/):
    python -I _ferramentas/dossies_para_rodada.py _catalogo/rodada11.json "IA no campo" \
        _dossies/_verificado_campo_A.json _dossies/_verificado_campo_B.json ...

- Um resultado por pasta de destino; o rótulo vira "<rótulo> (<tema do dossiê>)".
- Só entram os campos do catálogo; os de trabalho (pasta, verificação) ficam no dossiê.
- Formulários vão para o primeiro resultado de cada dossiê.
- Lacunas que mencionam o cliente saem (o catálogo é neutro; a regra fica no protocolo).
- Grava JSON com indent 2, UTF-8, LF e quebra de linha no fim. Não sobrescreve uma rodada que já exista.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CAMPOS = ["titulo", "organizacao", "ano", "tipo_fonte", "setor", "pais_regiao", "url", "arquivo", "status",
          "frentes", "metricas", "resumo", "relevancia"]
CLIENTE = re.compile(r"acelen|mubadala|empresa cliente", re.I)


def limpa_item(it: dict) -> dict:
    novo = {c: it.get(c) for c in CAMPOS}
    novo["arquivo"] = novo["arquivo"] or ""
    novo["frentes"] = novo["frentes"] or ["F3"]
    novo["metricas"] = novo["metricas"] or []
    return novo


def sem_cliente(lacunas: list[str]) -> list[str]:
    saida = []
    for lacuna in lacunas:
        if not CLIENTE.search(lacuna):
            saida.append(lacuna)
            continue
        frases = [f for f in re.split(r"(?<=[.;])\s+", lacuna) if not CLIENTE.search(f)]
        if frases:
            saida.append(" ".join(frases))
    return saida


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    destino, rotulo, entradas = Path(sys.argv[1]), sys.argv[2], sys.argv[3:]
    if not destino.is_absolute():
        destino = RAIZ / destino
    if destino.exists():
        raise SystemExit(f"{destino} já existe: apague ou escolha outro número de rodada")
    resultados: list[dict] = []
    for arq in entradas:
        caminho = Path(arq) if Path(arq).is_absolute() else RAIZ / arq
        dossie = json.loads(caminho.read_text(encoding="utf-8"))
        tema = dossie.get("tema", caminho.stem)
        por_pasta: dict[str, list[dict]] = {}
        for it in dossie.get("itens", []):
            pasta = it.get("pasta") or (it.get("arquivo") or "").split("/")[0] or "07_agro-global-perenes-autonomia"
            por_pasta.setdefault(pasta, []).append(limpa_item(it))
        primeiro = True
        for pasta, itens in por_pasta.items():
            resultados.append({
                "grupo": f"{rotulo} ({tema})",
                "pasta": pasta,
                "itens": itens,
                "formularios": dossie.get("formularios", []) if primeiro else [],
                "lacunas": sem_cliente(dossie.get("lacunas", [])) if primeiro else [],
            })
            primeiro = False
    destino.write_text(json.dumps({"resultados": resultados}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"{destino.name}: {sum(len(r['itens']) for r in resultados)} itens em {len(resultados)} resultados")
    for r in resultados:
        print(f"  {r['pasta']}: {len(r['itens'])} itens, {len(r['formularios'])} formulários, {len(r['lacunas'])} lacunas ({r['grupo']})")


if __name__ == "__main__":
    main()
