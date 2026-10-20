# -*- coding: utf-8 -*-
"""
Extrai os resultados dos agentes de uma rodada de varredura (journal.jsonl do Workflow)
para o formato que o consolidar.py lê.

Uso:
    python extrair_journal.py CAMINHO/journal.jsonl _catalogo/rodada1.json
"""
import json
import sys
from pathlib import Path

PASTAS = {
    "Consultorias de estratégia": "01_consultorias-estrategia",
    "Big Four, Accenture e Capgemini": "02_big4-accenture-capgemini",
    "Analistas e big techs": "03_analistas-big-techs",
    "Academia e instituições": "04_academia-instituicoes",
    "Agro Brasil: instituições e mídia": "05_agro-brasil-instituicoes-midia",
    "Empresas brasileiras de agro, bioenergia e florestal": "06_empresas-agro-bioenergia-florestal-br",
    "Agro global, culturas perenes e autonomia": "07_agro-global-perenes-autonomia",
    "Setor financeiro": "08_setor-financeiro",
    "Outros setores maduros": "09_outros-setores",
}


def main(journal, saida):
    texto = Path(journal).read_text(encoding="utf-8")
    if texto.lstrip().startswith("{") and '"result"' in texto[:2000]:
        # arquivo .output do Workflow: {"result": {"resultados": [{grupo, pasta, itens, ...}]}}
        resultados = json.loads(texto)["result"]["resultados"]
        Path(saida).parent.mkdir(parents=True, exist_ok=True)
        Path(saida).write_text(json.dumps({"resultados": resultados}, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{len(resultados)} grupos, {sum(len(r.get('itens', [])) for r in resultados)} itens -> {saida}")
        return
    rotulos, resultados = {}, []
    for linha in texto.splitlines():
        d = json.loads(linha)
        if d.get("type") == "started":
            rotulos[d["agentId"]] = d.get("label", "")
        elif d.get("type") == "result" and isinstance(d.get("result"), dict):
            r = d["result"]
            if "itens" not in r:
                continue
            grupo = rotulos.get(d["agentId"], "")
            pasta = r.get("pasta") or PASTAS.get(grupo) or next(
                (i["arquivo"].split("/")[0] for i in r["itens"] if i.get("arquivo")), "")
            resultados.append({"grupo": r.get("grupo_nome") or grupo, "pasta": pasta, **{k: v for k, v in r.items() if k != "pasta"}})
    Path(saida).parent.mkdir(parents=True, exist_ok=True)
    Path(saida).write_text(json.dumps({"resultados": resultados}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(resultados)} grupos, {sum(len(r['itens']) for r in resultados)} itens -> {saida}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
