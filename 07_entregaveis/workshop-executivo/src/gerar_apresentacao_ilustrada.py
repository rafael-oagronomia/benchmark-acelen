"""Gera o HTML-fonte da versão ilustrada da apresentação executiva (BIA-ACL-AE-02).

Pedido do Guilherme de 23/11/2026: uma versão da apresentação executiva com mais imagens de referência
e menos texto, publicada como apresentação adicional no sistema. É um resumo visual da BIA-ACL-AE-01:
os mesmos números, com as mesmas citações. Na primeira versão, com fotos genéricas de licença aberta,
ele pediu que as ilustrações fossem a respeito do conteúdo de cada slide.

Regras deste deck, além das da apresentação executiva:
- cada imagem vem da própria fonte citada no slide (foto ou figura do relatório, do estudo, da página do
  produto ou da publicação), reproduzida como citação, para estudo e análise, com a origem escrita em cima
  da imagem: quem publicou, documento, página, ID do catálogo e link (`img/creditos.json`). Antes de usar
  o material fora do projeto, conferir o direito de uso de cada imagem;
- texto em cima de imagem usa cor em rgb()/rgba(), que não muda com o tema claro ou escuro do site.

Uso: python gerar_apresentacao_ilustrada.py   (grava apresentacao-executiva-ilustrada.html nesta pasta)
No sistema: npm run montar-apresentacao -- executiva-ilustrada 07_entregaveis/workshop-executivo/src/apresentacao-executiva-ilustrada.html
(o script copia `img/` para `web/public/apresentacoes/executiva-ilustrada/`).
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from html import escape
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import gerar_apresentacao_executiva as ex  # noqa: E402  (CSS, linha de fontes, cabeçalho e catálogo)
import graficos as g  # noqa: E402
import slides_ilustrada as conteudo  # noqa: E402

rf = ex.rf
SAIDA = AQUI / "apresentacao-executiva-ilustrada.html"
DOCUMENTO = "BIA-ACL-AE-02"
REVISAO = "Rev. 00"
VERSAO = "v0"
NOME = "Apresentação executiva ilustrada do benchmark de uso de IA"
RODAPE = f"Acelen Energia Renovável · Apresentação executiva ilustrada · {DOCUMENTO} · {VERSAO}"
CREDITOS = json.loads((AQUI / "img" / "creditos.json").read_text(encoding="utf-8"))

CSS_IL = """
  /* ---- Versão ilustrada: fotos e figuras de licença aberta, com o crédito em cima de cada uma ---- */
  .ph { position: relative; margin: 0; border-radius: 12px; overflow: hidden; border: 1px solid var(--line); background: var(--bg-2); min-height: 0; }
  .ph img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; }
  .ph.ct img { object-fit: contain; background: rgb(255, 255, 255); }
  .ph .cr { position: absolute; left: 0; right: 0; bottom: 0; padding: 18px 10px 5px; font: 400 8px/1.3 var(--font-mono); color: rgb(226, 232, 220); background: linear-gradient(rgba(5, 8, 5, 0), rgba(5, 8, 5, 0.82)); }
  .ph .cr a { color: inherit; text-decoration: none; }
  .ph .lb { position: absolute; left: 10px; top: 10px; padding: 4px 9px; border-radius: 6px; font: 600 10px var(--font-display); letter-spacing: 0.12em; text-transform: uppercase; color: rgb(242, 244, 238); background: rgba(5, 8, 5, 0.72); }
  .capa-ft { position: absolute; right: 15mm; top: 20mm; bottom: 20mm; width: 104mm; }
  .il { display: grid; grid-template-columns: 0.92fr 1.08fr; gap: 14px; margin: 12px 0 10px; flex: 1; min-height: 340px; }
  .il.inv { grid-template-columns: 1.08fr 0.92fr; }
  .il.gr { grid-template-columns: 1.3fr 0.7fr; }
  .il > .dir { display: flex; flex-direction: column; gap: 10px; min-height: 0; justify-content: center; }
  .il > .dir .panel svg { margin-top: 4px; }
  .ft2 { display: grid; grid-template-rows: 1fr 1fr; gap: 10px; min-height: 0; }
  .kp { display: grid; grid-template-columns: auto 1fr; column-gap: 16px; align-items: center; background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; padding: 11px 16px; }
  .kp .n { font: 500 36px/1 var(--font-mono); color: var(--fg-1); white-space: nowrap; }
  .kp.g { border-color: var(--brand-green); background: #101A0E; }
  .kp.w .n { color: #B85F33; }
  .kp .rt { font: 600 9.5px var(--font-display); letter-spacing: 0.14em; text-transform: uppercase; color: var(--fg-3); }
  .kp p { font-size: 13px; color: var(--fg-2); line-height: 1.38; margin-top: 2px; }
  .kp p b { color: var(--fg-1); }
  .kp.t { grid-template-columns: 1fr; }
  .kp.t p { font-size: 13.5px; margin-top: 3px; }
  .tr3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 12px 0 8px; flex: 1; min-height: 340px; }
  .tr3 .cd { display: grid; grid-template-rows: 1fr auto; gap: 8px; min-height: 0; }
  .tr3 .cd .tx { background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; padding: 10px 13px; }
  .tr3 .cd .tx .rt { font: 600 9.5px var(--font-display); letter-spacing: 0.14em; text-transform: uppercase; color: var(--brand-green-bright); }
  .tr3 .cd .tx .n { font: 500 26px/1.1 var(--font-mono); color: var(--fg-1); margin-top: 4px; white-space: nowrap; }
  .tr3 .cd .tx p { font-size: 12px; color: var(--fg-2); line-height: 1.38; margin-top: 4px; }
  .tr3 .cd .tx p b { color: var(--fg-1); }
  /* O caminho em seis fases, em lista */
  .fs6 { display: grid; gap: 6px; }
  .fs6 .f { display: grid; grid-template-columns: 26px 1fr auto; gap: 12px; align-items: center; background: var(--bg-2); border: 1px solid var(--line); border-radius: 9px; padding: 8px 13px; }
  .fs6 .f .no { width: 26px; height: 26px; border-radius: 6px; background: var(--brand-green); color: #0B100B; font: 600 13px var(--font-mono); display: flex; align-items: center; justify-content: center; }
  .fs6 .f.cau .no { background: #B88A28; }
  .fs6 .f h3 { font-size: 14px; }
  .fs6 .f p { font-size: 11.6px; color: var(--fg-2); margin-top: 1px; line-height: 1.34; }
  .fs6 .f .v { font: 500 20px/1 var(--font-mono); color: var(--fg-1); text-align: right; white-space: nowrap; }
  .fs6 .f .v small { display: block; font: 400 10px/1.3 var(--font-body); color: var(--fg-3); margin-top: 3px; }
  /* De onde vem o dado, quando a fonte é imprensa, diário oficial ou rede social (sem reproduzir a imagem dela) */
  .rc { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 8px; }
  .rc span { background: var(--bg-1); border: 1px solid var(--line); border-radius: 999px; padding: 4px 11px; font-size: 10.5px; color: var(--fg-2); }
  .rc span b { color: var(--fg-1); font-weight: 600; }
  /* Grades de fotos: 2 × 2 (painel de empresas), três em coluna (o caminho), duas lado a lado (perenes) e quatro cartões (robôs) */
  .q2 { display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 8px; flex: 1; min-height: 0; }
  .ft3 { display: grid; grid-template-rows: 1fr 1fr 1fr; gap: 8px; min-height: 0; }
  .ft1x2 { display: grid; grid-template-columns: 0.8fr 1.2fr; gap: 10px; min-height: 0; }
  .tr4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 12px 0 8px; flex: 1; min-height: 360px; }
  .tr4 .cd { display: grid; grid-template-rows: 1fr auto; gap: 8px; min-height: 0; }
  .tr4 .cd .tx { background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; padding: 10px 13px; }
  .tr4 .cd .tx .rt { font: 600 9.5px var(--font-display); letter-spacing: 0.14em; text-transform: uppercase; color: var(--brand-green-bright); }
  .tr4 .cd .tx .n { font: 500 24px/1.1 var(--font-mono); color: var(--fg-1); margin-top: 4px; white-space: nowrap; }
  .tr4 .cd .tx p { font-size: 12px; color: var(--fg-2); line-height: 1.38; margin-top: 4px; }
  .tr4 .cd .tx p b { color: var(--fg-1); }
"""


def foto(ident: str, rotulo: str = "", classe: str = "", estilo: str = "") -> str:
    """Imagem do deck (figura ou foto da própria fonte citada), com rótulo e, sobre ela, a origem:
    quem publicou, o documento, a página e o ID do catálogo, com o link da fonte."""
    c = CREDITOS[ident]
    pagina = f', {c["pagina"]}' if c["pagina"] != "web" else ""
    credito = f'Imagem: {escape(c["credito"])}{pagina} · [{c["id"]}] <a href="{escape(c["url"])}">fonte ↗</a>'
    lb = f'<span class="lb">{rotulo}</span>' if rotulo else ""
    est = f' style="{estilo}"' if estilo else ""
    return (f'<figure class="ph {classe}"{est}><img src="img/{c["arquivo"]}" alt="{escape(c["descricao"])}">{lb}'
            f'<figcaption class="cr">{credito}</figcaption></figure>')


def capa(fontes_no_acervo: int) -> str:
    milhar = f"{fontes_no_acervo:,}".replace(",", ".")
    metricas = [(milhar, "fontes públicas no catálogo"), ("4", "empresas com ficha de benchmark"),
                (str(ex.NOTAS_TEMATICAS), "notas temáticas"), ("4", "sessões executivas")]
    grade = "".join(f'<div class="metric"><div class="v">{v}</div><div class="lb" style="margin-top:5px">{r}</div></div>' for v, r in metricas)
    return f"""<section class="slide cover">
  <img class="logo" src="{ex.LOGO}" alt="OagronomIA">
  {foto("macauba-plantio", "Macaúba plantada · Embrapa Cerrados", "capa-ft")}
  <div class="eyebrow" style="margin-top:13mm">Benchmarking de uso de IA como diferencial estratégico · apresentação executiva ilustrada</div>
  <h1>O que o mercado<br>já fez com IA</h1>
  <p class="lead" style="max-width:168mm">Onde estão as empresas líderes do agro, da bioenergia e de setores vizinhos, como chegaram lá e para onde a IA aponta no campo, em imagens.</p>
  <div class="grid4" style="max-width:168mm;margin-top:18px">{grade}</div>
  <div class="legend" style="margin-bottom:6mm;max-width:168mm">
    <div class="label">Contratante</div><div>Acelen Energia Renovável</div>
    <div class="label">Documento</div><div>{NOME}</div>
    <div class="label">Nº / Versão</div><div style="font-family:var(--font-mono)">{DOCUMENTO} · {REVISAO} · versão de trabalho {VERSAO}</div>
    <div class="label">Data</div><div>{date.today():%d/%m/%Y}</div>
  </div>
</section>"""


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")  # o -I ignora PYTHONIOENCODING
    fonte = rf.PARCIAL.read_text(encoding="utf-8")
    css = re.search(r"<style>([\s\S]*?)</style>", fonte).group(1)
    slides = conteudo.slides(ex.fontes, g, foto)
    total = len(slides) + 1

    partes = [capa(len(rf.catalogo()))]
    zooms: set[int] = set()
    for n, s in enumerate(slides, 2):
        zoom = round(s.get("zoom", 1) * 100)
        classe = "slide v1" + (f" z{zoom}" if zoom != 100 else "")
        zooms.add(zoom)
        partes.append(f"""<section class="{classe}">
  {ex.cabeca(s["parte"])}
  <div class="eyebrow">{s["olho"]}</div>
  <h2>{s["titulo"]}</h2>
  {s["corpo"]}
  {s["fontes"]}
  <div class="foot"><span>{RODAPE}</span><span class="mono">{n:02d} / {total:02d}</span></div>
</section>""")

    cabecalho = fonte[: fonte.index("<style>")]
    cabecalho = re.sub(r"<title>[\s\S]*?</title>", "<title>Apresentação executiva ilustrada</title>", cabecalho)
    fixos = ":not(.head):not(.eyebrow):not(h2):not(.msg-top):not(.fontes):not(.foot)"
    css_zoom = "".join(f"  .slide.z{z} > {fixos} {{ zoom: {z / 100}; }}\n" for z in sorted(zooms - {100}))
    html = (cabecalho + "<style>" + css + ex.CSS_EXEC + ex.slides_metodologia.CSS + CSS_IL + css_zoom + "</style>\n</head>\n<body>\n\n" + "\n".join(partes)
            + '\n\n<script src="https://unpkg.com/lucide@0.469.0/dist/umd/lucide.min.js"></script>\n<script>if (window.lucide) lucide.createIcons();</script>\n</body>\n</html>\n')

    # Só cores com variável no sistema; em cima de imagem, a cor vai em rgb()/rgba() e fica fixa nos dois temas.
    mapeadas = {"#050805", "#0B100B", "#131A13", "#1C241B", "#2A3328", "#3A4537", "#F2F4EE", "#B8BFB1", "#7C8678", "#52C937", "#6FE34F",
                "#2F8B1F", "#E8B33B", "#4FB7C9", "#E5524A", "#62A842", "#3A7A2A", "#2C4A22", "#9BE05F", "#3A8FBF", "#6FB8C9", "#1FB8CD",
                "#B88A28", "#B85F33", "#D97757", "#1F2B1C", "#101A0E", "#16210F"}
    fora = sorted({c.upper() for c in re.findall(r"#[0-9a-fA-F]{6}\b", "\n".join(partes) + CSS_IL)} - mapeadas)
    if fora:
        raise SystemExit(f"Cores sem variável no sistema: {', '.join(fora)}")
    usadas = set(re.findall(r'src="img/([^"]+)"', html))
    faltam = sorted(a for a in usadas if not (AQUI / "img" / a).exists())
    if faltam:
        raise SystemExit(f"Imagens que faltam em img/: {', '.join(faltam)}")

    SAIDA.write_text(html, encoding="utf-8", newline="\n")
    print(f"{SAIDA.name}: {total} slides, {len(usadas)} imagens")
    for n, s in enumerate(slides, 2):
        print(f"  {n:02d}  {s['parte']:<34} {s['titulo']}")


if __name__ == "__main__":
    main()
