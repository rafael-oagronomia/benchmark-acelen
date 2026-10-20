# -*- coding: utf-8 -*-
"""
Baixa um documento público e valida que é um PDF de verdade. Usa curl_cffi com perfis
de navegador reais (passa pela proteção anti-robô de McKinsey, BCG, PwC, Gartner etc.).
Rode SEMPRE com o Python do venv:  _ferramentas/.venv/Scripts/python.exe

Modos:
    baixar.py URL --pasta 01_consultorias-estrategia --nome McKinsey_2025_state-of-ai
        -> baixa o PDF; se a URL for uma página HTML, devolve os links .pdf encontrados nela
    baixar.py URL --texto [--max 12000]
        -> lê uma página web (quando WebFetch falhar) e imprime título, texto limpo e links .pdf
    baixar.py URL --pasta ... --nome ... --imprimir
        -> imprime a página web em PDF pelo Chrome headless (só para artigos sem PDF)

Saída do modo download (JSON em uma linha):
    {"ok": true, "arquivo": "...", "paginas": 32, "bytes": ..., "sha256": "...", "titulo_pdf": "...",
     "primeira_pagina": "...", "duplicado_de": null}
    {"ok": false, "motivo": "HTML, não PDF ...", "links_pdf": [...]}

Regras: só fontes oficiais; não contorna login, paywall nem formulário; arquivo inválido é apagado.
"""
import argparse
import hashlib
import html as htmllib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urljoin

import pymupdf
from curl_cffi import requests as cr

RAIZ = Path(__file__).resolve().parent.parent
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
PERFIS = ["chrome131", "firefox133", "safari17_0", "chrome"]
HEADERS = {"Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"}
LIMITE = 150 * 1024 * 1024


def slug(s):
    s = re.sub(r"[^\w\-.]+", "-", s, flags=re.ASCII).strip("-")
    return re.sub(r"-{2,}", "-", s)[:120]


def sha(p):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def duplicado(novo, h):
    for p in RAIZ.rglob("*.pdf"):
        if "_ferramentas" in p.parts or p == novo:
            continue
        if p.stat().st_size == novo.stat().st_size and sha(p) == h:
            return str(p.relative_to(RAIZ)).replace("\\", "/")
    return None


def saida(d):
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(d, ensure_ascii=False))
    sys.exit(0)


def buscar(url):
    """Tenta os perfis de navegador em sequência; devolve a primeira resposta 200."""
    ultimo = None
    for perfil in PERFIS:
        try:
            r = cr.get(url, impersonate=perfil, timeout=90, headers=HEADERS, allow_redirects=True)
        except Exception as e:
            ultimo = f"erro de rede ({perfil}): {e}"[:300]
            continue
        if r.status_code == 200:
            return r, None
        ultimo = f"HTTP {r.status_code} ({perfil})"
        if r.status_code not in (401, 403, 406, 429, 503):
            break
    return None, ultimo


def links_pdf(base, html):
    achados = re.findall(r'(?:href|data-href|src)=["\']([^"\']+?\.pdf(?:\?[^"\']*)?)["\']', html, re.I)
    achados += re.findall(r'https?://[^\s"\'<>]+?\.pdf', html, re.I)
    return sorted({urljoin(base, htmllib.unescape(a)) for a in achados})[:40]


def texto_html(html):
    t = re.sub(r"(?is)<(script|style|noscript|svg|header|footer|nav)[^>]*>.*?</\1>", " ", html)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</h\d>|</li>|</div>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = htmllib.unescape(t)
    t = re.sub(r"[ \t\r\f\v]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--pasta")
    ap.add_argument("--nome")
    ap.add_argument("--imprimir", action="store_true")
    ap.add_argument("--texto", action="store_true")
    ap.add_argument("--max", type=int, default=12000)
    a = ap.parse_args()

    if a.texto:
        r, erro = buscar(a.url)
        if not r:
            saida({"ok": False, "motivo": erro})
        if r.content[:5] == b"%PDF-":
            saida({"ok": False, "motivo": "a URL é um PDF — use o modo download"})
        html = r.text
        titulo = re.search(r"(?is)<title[^>]*>(.*?)</title>", html)
        sys.stdout.reconfigure(encoding="utf-8")
        print("TÍTULO:", htmllib.unescape(titulo.group(1).strip()) if titulo else "")
        print("URL FINAL:", r.url)
        print("LINKS PDF:", json.dumps(links_pdf(r.url, html), ensure_ascii=False))
        print("TEXTO:\n" + texto_html(html)[: a.max])
        return

    if not (a.pasta and a.nome):
        sys.exit("Informe --pasta e --nome")
    pasta = RAIZ / a.pasta
    pasta.mkdir(parents=True, exist_ok=True)
    destino = pasta / (slug(a.nome) + ".pdf")
    if destino.exists():
        saida({"ok": False, "motivo": "já existe arquivo com esse nome", "arquivo": str(destino.relative_to(RAIZ))})

    if a.imprimir:
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                            "--virtual-time-budget=20000", f"--print-to-pdf={destino}", a.url],
                           capture_output=True, text=True, timeout=180)
        if not destino.exists() or destino.stat().st_size < 20_000:
            destino.unlink(missing_ok=True)
            saida({"ok": False, "motivo": "impressão falhou ou página vazia/bloqueada"})
    else:
        r, erro = buscar(a.url)
        if not r:
            saida({"ok": False, "motivo": erro})
        corpo = r.content
        if corpo[:5] != b"%PDF-":
            saida({"ok": False, "motivo": "HTML, não PDF (landing page, formulário, login ou bloqueio)",
                   "url_final": r.url, "content_type": r.headers.get("content-type", ""),
                   "links_pdf": links_pdf(r.url, r.text)})
        if len(corpo) > LIMITE:
            saida({"ok": False, "motivo": "arquivo acima de 150 MB — registre só o link"})
        destino.write_bytes(corpo)

    try:
        doc = pymupdf.open(destino)
        info = {"paginas": len(doc), "titulo_pdf": (doc.metadata or {}).get("title") or "",
                "primeira_pagina": re.sub(r"\s+", " ", doc[0].get_text() if len(doc) else "").strip()[:300]}
        doc.close()
    except Exception as e:
        destino.unlink(missing_ok=True)
        saida({"ok": False, "motivo": f"PDF inválido: {e}"[:200]})

    h = sha(destino)
    dup = duplicado(destino, h)
    if dup:
        destino.unlink()
        saida({"ok": True, "duplicado_de": dup, "sha256": h, "arquivo": dup})
    saida({"ok": True, "arquivo": str(destino.relative_to(RAIZ)).replace("\\", "/"),
           "bytes": destino.stat().st_size, "sha256": h, "duplicado_de": None, **info})


if __name__ == "__main__":
    main()
