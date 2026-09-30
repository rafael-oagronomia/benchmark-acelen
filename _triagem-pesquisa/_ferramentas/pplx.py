# -*- coding: utf-8 -*-
"""
Consulta a API da Perplexity (chave lida de C:/dev/acelen/benchmark/.env).

Uso:
    python pplx.py "pergunta"                         # sonar-pro (rápido, centavos)
    python pplx.py "pergunta" --model sonar-deep-research --out ../_perplexity/dr01.md
    python pplx.py --arquivo prompt.md --model sonar-deep-research --out saida.md

Imprime a resposta e a lista numerada de fontes (URLs). Cada chamada é registrada
em _perplexity/log.jsonl (modelo, tokens, custo informado pela API), sem a chave.

IMPORTANTE: nunca inclua nas perguntas o nome do cliente, do projeto ou qualquer
informação interna — só temas genéricos de mercado.
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests

ENV = Path(r"C:/dev/acelen/benchmark/.env")
API_URL = "https://api.perplexity.ai/chat/completions"
LOG = Path(__file__).resolve().parent.parent / "_perplexity" / "log.jsonl"

SYSTEM = (
    "Você é um analista sênior de pesquisa de mercado. Seu objetivo é localizar DOCUMENTOS "
    "publicados (relatórios, estudos, pesquisas, whitepapers, relatórios anuais) e dados "
    "quantitativos verificáveis. Para cada documento, informe título exato, organização, ano, "
    "URL da página oficial e, quando existir, URL direta do PDF. Priorize 2024-2026 e fontes "
    "oficiais (site da organização). Nunca invente URLs nem números: se não houver evidência, "
    "diga explicitamente. Responda em português do Brasil."
)


def load_key() -> str:
    for line in ENV.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("PERPLEXITY_API_KEY") and "=" in line:
            key = line.split("=", 1)[1].strip().strip('"').strip("'")
            if key and not key.startswith("<"):
                return key
    sys.exit("ERRO: PERPLEXITY_API_KEY não encontrada em " + str(ENV))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pergunta", nargs="?")
    ap.add_argument("--arquivo", help="lê a pergunta de um arquivo")
    ap.add_argument("--model", default="sonar-pro",
                    help="sonar-pro (padrão) | sonar-reasoning-pro | sonar-deep-research")
    ap.add_argument("--effort", default="high", choices=["low", "medium", "high"])
    ap.add_argument("--out", help="salva resposta + fontes em markdown (e .raw.json ao lado)")
    ap.add_argument("--recencia", choices=["month", "year"], help="search_recency_filter")
    a = ap.parse_args()

    pergunta = Path(a.arquivo).read_text(encoding="utf-8") if a.arquivo else a.pergunta
    if not pergunta:
        sys.exit("Informe a pergunta ou --arquivo")

    payload = {
        "model": a.model,
        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": pergunta}],
    }
    if a.model == "sonar-deep-research":
        payload["reasoning_effort"] = a.effort
    if a.recencia:
        payload["search_recency_filter"] = a.recencia
    headers = {"Authorization": f"Bearer {load_key()}", "Content-Type": "application/json"}

    t0 = time.time()
    data, err = None, None
    for tentativa in range(1, 7):
        try:
            r = requests.post(API_URL, json=payload, headers=headers, timeout=3600)
            if r.status_code == 200:
                data = r.json()
                break
            err = f"HTTP {r.status_code}: {r.text[:400]}"
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(45 * tentativa)
                continue
            break
        except requests.exceptions.RequestException as e:
            err = str(e)
            time.sleep(20 * tentativa)
    if data is None:
        sys.exit("FALHA Perplexity: " + str(err))

    content = data["choices"][0]["message"]["content"]
    content = re.sub(r"<think>.*?</think>\s*", "", content, flags=re.DOTALL)
    results = data.get("search_results") or []
    cits = data.get("citations") or []
    fontes = [f"{i}. {r.get('title', '')} — {r.get('url', '')} ({r.get('date') or 's/d'})"
              for i, r in enumerate(results, 1)] or [f"{i}. {c}" for i, c in enumerate(cits, 1)]
    usage = data.get("usage", {})
    elapsed = time.time() - t0

    texto = content + "\n\n---\nFONTES\n" + "\n".join(fontes)
    if a.out:
        out = Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        cab = f"# Perplexity — {a.model}\n\n> Pergunta:\n\n{pergunta.strip()}\n\n> Tempo: {elapsed/60:.1f} min\n\n"
        out.write_text(cab + texto, encoding="utf-8")
        out.with_suffix(".raw.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"model": a.model, "segundos": round(elapsed), "usage": usage,
                            "pergunta": pergunta[:300], "out": a.out}, ensure_ascii=False) + "\n")
    sys.stdout.reconfigure(encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
