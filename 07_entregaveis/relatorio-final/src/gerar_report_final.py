"""Gera o HTML-fonte do Report Final (BIA-ACL-RF-01): a apresentação final do benchmark.

O relatório final é entregue como apresentação dentro do sistema do estudo, com exportação em PDF
(o mesmo HTML, impresso pelo Chrome). O deck só tem slides de resultado (decisão de 11/11/2026):
nada de mapa com situação, lista de entregáveis, metodologia, "o que falta" ou "o que foi feito".
As três frentes do escopo e as sessões executivas abrem com um slide divisor que lista os temas da
parte e os slides onde estão.

Cada slide é de um de três tipos:
- reuso(n): slide n da entrega parcial (RP-02 v12), com o rótulo do bloco do Report Final;
- novo(...): slide escrito aqui;
- construir(...): slide planejado e ainda não escrito. Fica só aqui, como pauta: nunca entra no
  deck; o gerador lista os pendentes no terminal. Um tema só aparece no divisor quando tem slide.

Uso: python gerar_report_final.py   (grava report-final.html nesta pasta e lista os pendentes)
Depois, no repositório do sistema: npm run montar-apresentacao -- report-final 07_entregaveis/relatorio-final/src/report-final.html
"""
from __future__ import annotations

import json
import re
from datetime import date
from html import escape
from pathlib import Path
import sys

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import slides_ia_no_campo  # noqa: E402  (slides de resultado da nota IA no campo)
import slides_satelites  # noqa: E402  (slides de resultado da nota de satélites e modelos de fundação)
import slides_acrescimos  # noqa: E402  (acréscimos de 23/11/2026: caso iFood, colheita da macaúba e robôs que sobem na palmeira)
RAIZ = AQUI.parents[2]
PARCIAL = RAIZ / "07_entregaveis/relatorios-parciais/src/resultados-parciais-semanal-2026-10-23_v12.html"
SAIDA = AQUI / "report-final.html"

DOCUMENTO = "BIA-ACL-RF-01"
REVISAO = "Rev. 00"
VERSAO = "v0"
NOME = "Report Final do benchmark de uso de IA"
RODAPE = f"Acelen Energia Renovável · Report Final do benchmark · {DOCUMENTO} · {VERSAO}"
LOGO = "../../../docs/design-system/assets/logo-oagronomia-wordmark.png"

def bolinhas(n: int) -> str:
    """Cinco bolinhas, n cheias: o estágio geral na régua de 1 a 5."""
    return f'<span class="pg" title="estágio geral {n}">' + "".join(f'<i{" class=\"on\"" if k < n else ""}></i>' for k in range(5)) + "</span>"


def com_geral(nome: str, n: int) -> str:
    """Etiqueta da empresa com as bolinhas do estágio geral embaixo."""
    return f'<span class="eg"><span class="emp">{nome}</span>{bolinhas(n)}</span>'


# Trocas em slides reaproveitados da entrega parcial, conferidas uma a uma (cada trecho aparece uma
# vez no slide). 17, 18 e 25: páginas de fontes salvas de novo (a paginação do arquivo mudou).
# 16 (régua de governança): pedido de 25/11/2026. A régua usa os mesmos nomes da escada geral e o
# "2 · Pilotos" da Suzano parecia o estágio geral; a marca diz que é só a dimensão governança, e as
# bolinhas mostram o estágio geral de cada empresa (Bayer 4; Suzano e Deere 3; DJI 2; fichas, seção 11).
CORRECOES = {
    16: [
        ('<p style="font-size:13px;color:var(--fg-2);margin-top:4px">A métrica é a nota de 1 a 5 na dimensão Estratégia e governança, '
         'a mesma régua do slide anterior, dada só com o que a empresa publica</p>',
         '<div class="mk-g"><span class="tg">Só a dimensão governança</span>'
         '<span>no estágio geral, <b>Suzano e Deere estão no 3</b> · nota de 1 a 5 dada só com o que a empresa publica</span>'
         '<span class="lgd"><span class="pg"><i class="on"></i></span>bolinhas: estágio geral de cada empresa, de 1 a 5</span></div>'),
        ('<span class="emp">Bayer</span>', com_geral("Bayer", 4)),
        ('<span class="emp">Suzano</span><span class="emp">Deere</span><span class="emp">DJI</span>',
         com_geral("Suzano", 3) + com_geral("Deere", 3) + com_geral("DJI", 2)),
    ],
    17: [("Cloud and Threat Report: 2026, p. 2-3, 12 <a", "Cloud and Threat Report: 2026, p. 2-3, 22 <a")],
    18: [("Cloud and Threat Report: 2…, p. 6 <a", "Cloud and Threat Report: 2…, p. 10 <a")],
    25: [("Cloud and Threat Report: 2026, p. 5 <a", "Cloud and Threat Report: 2026, p. 7-8 <a")],
}

CSS_EXTRA = """
  /* Report Final: divisores das partes. */
  .rf-div .rf-n { font: 500 13px var(--font-mono); letter-spacing: 0.14em; color: var(--brand-green); margin-top: 6mm; }
  .rf-div h1 { font-size: 40px; margin-top: 4px; }
  .rf-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 14px; }
  .rf-grid.c3 { grid-template-columns: repeat(3, 1fr); }
  .rf-it { background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; padding: 11px 13px; display: flex; flex-direction: column; }
  .rf-it.ap { border-style: dashed; }
  .rf-it .k { font: 500 10.5px var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; color: var(--brand-green); }
  .rf-it.ap .k { color: var(--info); }
  .rf-it h3 { font-size: 14px; margin-top: 3px; }
  .rf-it p { font-size: 11.4px; color: var(--fg-2); margin-top: 5px; line-height: 1.4; flex: 1; }
  .rf-it .sl { margin-top: 8px; padding-top: 6px; border-top: 1px solid var(--line); font: 500 10.5px var(--font-mono); color: var(--brand-green-bright); }

  /* Peças da apresentação executiva usadas nos slides de 23/11/2026 (slides_acrescimos.py): legenda,
     etapas em coluna, faixa de números e matriz de estágio. Manter iguais às de gerar_apresentacao_executiva.py. */
  .lg { display: flex; gap: 16px; flex-wrap: wrap; font-size: 11px; color: var(--fg-3); margin-top: 6px; }
  .lg span::before { content: ""; display: inline-block; width: 10px; height: 10px; border-radius: 3px; margin-right: 6px; vertical-align: -1px; background: var(--c); }
  .f4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 10px; }
  .f4.c3 { grid-template-columns: repeat(3, 1fr); }
  .f4 .i { background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; padding: 9px 12px; display: flex; gap: 12px; align-items: center; }
  .f4 .i .n { font: 500 22px/1 var(--font-mono); color: var(--fg-1); flex: none; white-space: nowrap; }
  .f4 .i .t { font-size: 11.6px; color: var(--fg-2); line-height: 1.36; }
  .f4 .i .t b { color: var(--fg-1); }
  .f4 .i svg.lucide { width: 24px !important; height: 24px !important; }
  .fv { display: grid; gap: 6px; align-content: start; }
  .fv .r { display: grid; grid-template-columns: 22px 1fr; gap: 10px; background: var(--bg-2); border: 1px solid var(--line); border-radius: 9px; padding: 8px 12px 9px; align-items: start; }
  .fv .r.res { border-color: var(--brand-green); background: #101A0E; }
  .fv .r .bd { width: 22px; height: 22px; border-radius: 5px; background: var(--brand-green); color: #0B100B; font: 600 12px var(--font-mono); display: flex; align-items: center; justify-content: center; margin-top: 1px; }
  .fv .r .rt { font: 600 9.5px var(--font-display); letter-spacing: 0.14em; text-transform: uppercase; color: var(--fg-3); }
  .fv .r p { font-size: 12.4px; color: var(--fg-2); line-height: 1.4; margin-top: 2px; }
  .fv .r p b { color: var(--fg-1); }
  .mz { display: grid; grid-template-columns: 26px 1fr repeat(4, 62px); column-gap: 8px; margin-top: 2px; }
  .mz > div { padding: 5px 0; border-bottom: 1px solid var(--line); display: flex; align-items: center; }
  .mz > div.h { font: 600 8.8px/1.3 var(--font-display); letter-spacing: 0.08em; text-transform: uppercase; color: var(--fg-3); justify-content: center; text-align: center; padding: 2px 0 6px; }
  .mz svg.lucide { width: 22px !important; height: 22px !important; }
  .mz > div.nm { display: block; }
  .mz .nm b { font: 600 13.5px var(--font-display); color: var(--fg-1); display: block; }
  .mz .nm span { font-size: 11px; color: var(--fg-2); line-height: 1.3; display: block; }
  .mz > div.pt { justify-content: center; }
  .mz .pt span { width: 16px; height: 16px; border-radius: 50%; box-shadow: inset 0 0 0 1.5px var(--line-strong); display: block; }
  .mz .pt span.on { background: var(--brand-green); box-shadow: none; }
  .mz > div.fim { border-bottom: 0; }
  .lg span.sd::before { display: none; }

  /* Régua de governança (pedido de 25/11/2026): marca "só a dimensão governança" e bolinhas do estágio geral. */
  .mk-g { display: flex; align-items: center; gap: 10px; margin-top: 5px; font-size: 12.5px; color: var(--fg-2); }
  .mk-g .tg { font: 600 10px var(--font-display); letter-spacing: 0.1em; text-transform: uppercase; color: var(--warning); border: 1px solid var(--warning); border-radius: 999px; padding: 2px 9px; flex: none; }
  .mk-g b { color: var(--fg-1); }
  .mk-g .lgd { margin-left: auto; display: inline-flex; align-items: center; gap: 6px; font-size: 11px; color: var(--fg-3); flex: none; }
  .eg { display: inline-flex; flex-direction: column; align-items: center; margin: 0 3px 3px 0; vertical-align: top; }
  .eg .emp { margin: 0; }
  .pg { display: inline-flex; gap: 2px; }
  .eg .pg { margin-top: 3px; }
  .pg i { width: 7px; height: 7px; border-radius: 50%; box-shadow: inset 0 0 0 1px var(--line-strong); display: block; }
  .pg i.on { background: var(--brand-green-bright); box-shadow: none; }
"""


# ---------------------------------------------------------------------------------------------
# Peças
# ---------------------------------------------------------------------------------------------
def cabeca(rotulo: str) -> str:
    return f'<div class="head"><img src="{LOGO}" alt="OagronomIA"><span class="label">{rotulo}</span></div>'


def reuso(n: int, rotulo: str | None = None, revisar: str | None = None) -> dict:
    """Slide n da entrega parcial. `rotulo` troca o rótulo original; `revisar` vai para a lista de
    pendentes (nunca para o slide)."""
    return {"tipo": "reuso", "n": n, "rotulo": rotulo, "revisar": revisar}


def novo(rotulo: str, olho: str, titulo: str, corpo: str, fontes: str = "", classe: str = "slide v1") -> dict:
    return {"tipo": "novo", "rotulo": rotulo, "olho": olho, "titulo": titulo, "corpo": corpo, "fontes": fontes, "classe": classe}


def construir(rotulo: str, olho: str, titulo: str, entra: list[str], vem: list[str]) -> dict:
    """Slide planejado e ainda não escrito: o que entra e de onde vem. Não entra no deck."""
    return {"tipo": "construir", "rotulo": rotulo, "olho": olho, "titulo": titulo, "entra": entra, "vem": vem}


def item(k: str, titulo: str, texto: str, chave: str, aprofundamento: bool = False) -> dict:
    """Entregável de um bloco, no divisor: `chave` liga o item aos slides do grupo de mesmo nome."""
    return {"k": k, "titulo": titulo, "texto": texto, "chave": chave, "ap": aprofundamento}


def lista(itens: list[str]) -> str:
    return '<ul class="l">' + "".join(f"<li>{i}</li>" for i in itens) + "</ul>"


_CATALOGO: dict | None = None


def catalogo() -> dict:
    global _CATALOGO
    if _CATALOGO is None:
        itens = json.loads((RAIZ / "_triagem-pesquisa/_catalogo/catalogo.json").read_text(encoding="utf-8"))["itens"]
        _CATALOGO = {i["id"]: i for i in itens}
    return _CATALOGO


def fontes(*citacoes: tuple[str, str]) -> str:
    """Linha de fontes do slide, tirada do catálogo: [M123] Organização, título curto, p. N e link.
    Cada citação é (ID, "p. 4") ou (ID, "web"). No site, o [M123] abre o PDF na página."""
    partes = []
    for ident, pagina in citacoes:
        it = catalogo()[ident]
        org = re.split(r"\s*[;(]", it.get("organizacao") or "")[0].strip()
        titulo = it.get("titulo") or ""
        if len(titulo) > 52:
            titulo = titulo[:50].rsplit(" ", 1)[0] + "…"
        url = it.get("url") or ""
        dominio = re.sub(r"^https?://(www\.)?", "", url).split("/")[0]
        link = f' <a href="{escape(url)}">{escape(dominio)} ↗</a>' if url else ""
        pag = f", {pagina}" if pagina and pagina != "web" else ""
        partes.append(f'<span class="f">[{ident}] {escape(org)}, {escape(titulo)}{pag}{link}</span>')
    return '<div class="fontes"><b>Fontes</b>' + " ".join(partes) + "</div>"


def barras(linhas: list[tuple[str, float, str, str]], maximo: float = 100, largura: int = 470, rotulo_w: int = 190) -> str:
    """Barras horizontais em SVG, nas cores do documento (o site troca as cores pelo tema).
    Cada linha: (rótulo, valor, texto do valor, cor: "verde" | "ambar" | "azul" | "cinza")."""
    cores = {"verde": "#62A842", "ambar": "#B88A28", "azul": "#3A8FBF", "cinza": "#7C8678"}
    passo, altura_barra = 28, 15.4
    util = largura - rotulo_w - 70
    svg = [f'<svg viewBox="0 0 {largura} {passo * len(linhas) + 4}">']
    for k, (rotulo, valor, texto, cor) in enumerate(linhas):
        y = 6 + k * passo
        w = max(2.0, util * valor / maximo)
        svg.append(f'<text x="{rotulo_w - 10}" y="{y + 12.2:.1f}" text-anchor="end" font-family="Manrope, sans-serif" font-size="12.5" fill="#B8BFB1">{escape(rotulo)}</text>')
        svg.append(f'<rect x="{rotulo_w}" y="{y}" width="{w:.1f}" height="{altura_barra}" rx="3" fill="{cores[cor]}"/>')
        svg.append(f'<text x="{rotulo_w + w + 8:.1f}" y="{y + 12.7:.1f}" font-family="JetBrains Mono, monospace" font-size="13.5" font-weight="500" fill="#F2F4EE">{escape(texto)}</text>')
    svg.append("</svg>")
    return "\n".join(svg)


# ---------------------------------------------------------------------------------------------
# Estrutura do relatório: blocos → grupos (entregáveis) → slides
# ---------------------------------------------------------------------------------------------
def estrutura() -> list[dict]:
    campo = slides_ia_no_campo.slides(novo, fontes, barras, lista)
    satelites = slides_satelites.slides(novo, fontes, barras, lista)
    acrescimos = slides_acrescimos.slides(novo, fontes, lista)
    return [
        {
            "id": "resumo", "nome": "Resumo executivo", "divisor": None,
            "grupos": [
                ("resumo", [construir(
                    "Resumo executivo", "Resumo executivo", "As mensagens do estudo em uma página",
                    ["As conclusões de cada frente, com o número que as sustenta e a fonte.",
                     "Onde o mercado está na régua de maturidade e o que separa um estágio do seguinte.",
                     "O que isso sugere para a estratégia de IA da Acelen, em leitura macro."],
                    ["Fecha por último, depois das três frentes.", "Síntese das sessões executivas, só no agregado."])]),
            ],
        },
        {
            "id": "f1", "nome": "Frente 1 · Benchmark estratégico de IA", "curto": "Frente 1", "icone": "building-2",
            "divisor": "Como as empresas líderes usam IA: o que funcionou, o que falhou e por quê. Um painel de empresas do agro e de setores vizinhos, lido nas mesmas dimensões, com uma ficha padronizada por empresa.",
            "itens": [
                item("1.1", "Painel de empresas", "Quatro empresas com ficha completa e os setores que saem na frente como referência.", "painel"),
                item("1.2", "Fichas de benchmark", "Síntese padronizada por empresa, comparável entre casos: Suzano, Bayer, Deere e DJI.", "fichas"),
                item("1.3", "Dimensões de análise", "Governança, dados, organização e aplicações, do apoio à decisão às tecnologias de campo.", "dimensoes"),
                item("1.4", "Casos de sucesso e insucesso", "O que funcionou, o que falhou e as lições, inclusive falhas de infraestrutura, governança e dados.", "casos"),
                item("Aprofundamento", "Valor e retorno da IA", "Quem paga o consumo, como se mede o retorno e a diferença entre IA generativa e preditiva.", "retorno", True),
                item("Aprofundamento", "Setores de referência", "O que um setor de maior maturidade digital já faz: os bancos.", "setores", True),
            ],
            "grupos": [
                ("painel", [
                    construir("Painel de empresas", "Frente 1 · Painel de empresas", "O painel: quatro empresas com ficha e os setores de referência",
                              ["Quem está no painel e por que entrou: semelhança com o modelo da Acelen, jornada de IA estruturada e material público suficiente.",
                               "Suzano e Bayer, indicadas pela Acelen; Deere e DJI, para retratar a corrida entre EUA e China.",
                               "Setores de maior maturidade digital como referência comparativa."],
                              ["Descritivo da metodologia (BIA-ACL-MT-01), seção 5.", "Fichas de benchmark das quatro empresas."]),
                    reuso(8),
                ]),
                ("fichas", [
                    construir(f"Ficha · {e}", "Frente 1 · Fichas de benchmark", f"{e}: {t}",
                              ["Estratégia e patrocínio, governança, dados e infraestrutura, organização e pessoas.",
                               "Aplicações no campo, na indústria e no corporativo; IA generativa e agentes.",
                               "Resultados divulgados, com fonte e página; insucessos e lições.",
                               "Estágio de maturidade por dimensão, com a evidência que o sustenta."],
                              [f"Ficha de benchmark da {e} (estudo no acervo do sistema).", "Par de slides: um visual, um descritivo."])
                    for e, t in [("Suzano", "a ficha em um slide"), ("Bayer", "a ficha em um slide"), ("Deere", "a ficha em um slide"), ("DJI", "a ficha em um slide")]
                ]),
                ("dimensoes", [
                    reuso(15),
                    construir("Dimensões de análise", "Frente 1 · Dimensões de análise", "Leitura transversal: dados, organização e aplicações nas quatro empresas",
                              ["O que as quatro empresas têm em comum em cada dimensão e onde divergem.",
                               "Aplicações por área: campo, indústria e logística, corporativo.",
                               "O que é evidência de uso em produção e o que ainda é anúncio ou piloto."],
                              ["Fichas de benchmark (seções 2 a 7).", "Nota de valor e retorno da IA."]),
                ]),
                ("casos", [
                    reuso(12),
                    construir("Casos de sucesso e insucesso", "Frente 1 · Casos de sucesso e insucesso", "O que funcionou, o que falhou e por quê",
                              ["Casos de sucesso com resultado medido, por empresa.",
                               "Insucessos com registro público: fragilidade de infraestrutura, de governança e de qualidade de dados.",
                               "As lições que se repetem."],
                              ["Fichas de benchmark (seções 8 e 10).", "Notas de valor e retorno, shadow AI e custo."]),
                ]),
                ("retorno", [reuso(13), reuso(14), reuso(33)]),
                ("setores", [
                    reuso(22), reuso(23),
                    construir("Setores de referência", "Frente 1 · Setores de referência", "Química e farmacêutica, e a parcela do faturamento em P&D",
                              ["Como química e farmacêutica usam IA em P&D e o que isso antecipa para o agro.",
                               "Parcela do faturamento investida em P&D e o cruzamento com o retorno divulgado."],
                              ["Fontes do catálogo sobre química, farmacêutica e P&D.", "Ficha da Bayer."]),
                ]),
            ],
        },
        {
            "id": "f2", "nome": "Frente 2 · Modelos de maturidade e roadmaps", "curto": "Frente 2", "icone": "chart-no-axes-column-increasing",
            "divisor": "Uma régua de cinco estágios e quatro dimensões para a Acelen se situar no mercado: o que cada estágio exige, o que condiciona cada salto e a sequência que as empresas líderes seguiram.",
            "itens": [
                item("2.1", "Frameworks de maturidade", "Revisão dos frameworks de mercado e o framework consolidado, aplicável ao agro.", "frameworks"),
                item("2.2", "Estágios de evolução", "Do uso exploratório aos sistemas autônomos, com o posicionamento do painel.", "estagios"),
                item("2.3", "Capacidades por etapa", "Dados, infraestrutura, pessoas, processos e governança em cada estágio.", "capacidades"),
                item("2.4", "Dependências críticas", "Os pré-requisitos que condicionam cada salto de maturidade.", "dependencias"),
                item("2.5", "IA generativa nos modelos", "Como LLMs, agentes e copilotos entram em cada estágio.", "generativa"),
                item("2.6", "Roadmaps observados", "Sequência, ritmo e prioridades típicos: o roteiro de adoção.", "roadmaps"),
                item("Aprofundamento", "Governança e shadow AI", "Uso de IA por fora dos canais oficiais e a governança dos bancos como referência.", "governanca", True),
            ],
            "grupos": [
                ("frameworks", [
                    construir("Frameworks de maturidade", "Frente 2 · Frameworks de maturidade", "Os frameworks de mercado e o que eles têm em comum",
                              ["Os principais modelos de institutos de pesquisa, analistas, consultorias e big techs.",
                               "O que se repete entre eles: estágios, dimensões e critérios de passagem."],
                              ["Nota de frameworks de maturidade (estudo no acervo)."]),
                    construir("Frameworks de maturidade", "Frente 2 · Framework consolidado", "A régua do estudo: cinco estágios e quatro dimensões",
                              ["Os cinco estágios: exploração, pilotos, operacionalização, escala e transformação.",
                               "As quatro dimensões: estratégia e governança, dados e infraestrutura, organização e pessoas, aplicações e valor.",
                               "Como se posiciona: evidência pública de uso em produção, critérios cumulativos."],
                              ["Descritivo da metodologia (BIA-ACL-MT-01), seção 6.", "Nota de frameworks de maturidade."]),
                ]),
                ("estagios", [reuso(21), reuso(16)]),
                ("capacidades", [
                    construir("Capacidades por etapa", "Frente 2 · Capacidades por etapa", "O que cada estágio exige em dados, infraestrutura, pessoas, processos e governança",
                              ["Uma linha por estágio, uma coluna por capacidade.", "Os checkpoints de cada nível da régua."],
                              ["Nota do roteiro de adoção de IA.", "Página Roteiro do sistema."]),
                ]),
                ("dependencias", [
                    construir("Dependências críticas", "Frente 2 · Dependências críticas", "O que condiciona cada salto de maturidade",
                              ["Os pré-requisitos sem os quais o estágio seguinte não se sustenta.", "Onde as empresas travam e por quê."],
                              ["Nota do roteiro de adoção de IA.", "Síntese das sessões executivas, no agregado."]),
                ]),
                ("generativa", [
                    construir("IA generativa nos modelos", "Frente 2 · IA generativa nos modelos e roadmaps", "Onde LLMs, agentes e copilotos entram em cada estágio",
                              ["Do uso individual ao uso integrado a processos e aos agentes com supervisão.", "Como os líderes incorporam a IA generativa ao que já tinham de IA preditiva."],
                              ["Notas de frameworks de maturidade e do roteiro de adoção.", "Fichas de benchmark (seção 7)."]),
                ]),
                ("roadmaps", [
                    construir("Roadmaps observados", "Frente 2 · Roadmaps observados no mercado", "O roteiro de adoção: sequência, ritmo e prioridades",
                              ["A sequência de marcos que o mercado seguiu e as lições aprendidas.",
                               "Quem faz o quê, o fluxo de implementação e a política de uso.",
                               "O paralelo com outros setores e com florestal, energia e agro."],
                              ["Nota do roteiro de adoção de IA.", "Página Roteiro do sistema, com a autoavaliação."]),
                ]),
                ("governanca", [reuso(17), reuso(18), reuso(19), reuso(24), reuso(25)]),
            ],
        },
        {
            "id": "f3", "nome": "Frente 3 · Tendências e perspectivas futuras", "curto": "Frente 3", "icone": "telescope",
            "divisor": "O que deve mudar a IA no agro e nos setores vizinhos nos próximos anos, separando a tendência consolidada, com adoção e resultado medido, do sinal emergente.",
            "itens": [
                item("3.1", "Movimentos de mercado", "Investimentos, parcerias, aquisições e sinais de direção.", "mercado"),
                item("3.2", "IA generativa", "LLMs, agentes e copilotos, e o custo de uso: preço, consumo e valor por tarefa.", "generativa3"),
                item("3.3", "Sistemas autônomos", "Máquinas autônomas, drones e robótica de campo, com atenção a culturas perenes e à colheita da macaúba.", "autonomos"),
                item("3.4", "IA aplicada ao agro", "Agricultura de precisão, sensoriamento, modelos preditivos e melhoramento.", "agro"),
                item("Aprofundamento", "Satélites e modelos de fundação", "Imagem e clima: o que já está em operação, o que a validação mostra e o que falta no Brasil.", "satelites", True),
                item("3.5", "Dados e soberania", "Controle dos dados, dependência de fornecedores e a corrida entre EUA e China.", "soberania"),
                item("3.6", "Mudanças organizacionais", "Estruturas, papéis e competências que mudam com a IA.", "organizacao"),
                item("3.7", "Oportunidades e riscos", "Tecnológicos, organizacionais e competitivos, relevantes para a Acelen.", "riscos"),
                item("Aprofundamento", "IA e impacto ambiental", "Energia, água e emissões: cada consulta gasta menos, o total sobe.", "ambiental", True),
            ],
            "grupos": [
                ("mercado", [
                    construir("Movimentos de mercado", "Frente 3 · Movimentos de mercado", "Investimentos, parcerias e aquisições: para onde o mercado aponta",
                              ["Os movimentos recentes das empresas do painel e dos setores vizinhos.", "O que é tendência consolidada e o que é sinal emergente."],
                              ["Fichas de benchmark (seção 9).", "Fontes do catálogo sobre investimentos e aquisições."]),
                ]),
                ("generativa3", [
                    construir("IA generativa", "Frente 3 · Tendências em IA generativa", "LLMs, agentes e copilotos: o que muda na decisão, na produtividade e na operação",
                              ["Do assistente ao agente: o que já está em uso e o que ainda é promessa.", "Implicações para a decisão estratégica e para o modelo operacional."],
                              ["Notas de custo da IA e de valor e retorno.", "Síntese das sessões executivas, no agregado."]),
                    reuso(9), reuso(10), reuso(11), *acrescimos["custo"],
                ]),
                ("autonomos", campo["autonomos"] + acrescimos["colheita"]),
                ("agro", campo["agro"]),
                ("satelites", satelites),
                ("soberania", [
                    construir("Dados e soberania", "Frente 3 · Dados e soberania tecnológica", "EUA × China: duas rotas para a IA no agro e o que elas dizem sobre dependência",
                              ["Propriedade e controle dos dados, dependência de fornecedores e autonomia tecnológica.", "A corrida entre EUA e China na mecanização, nos drones e nas máquinas autônomas."],
                              ["Nota EUA × China: IA no agro (estudo no acervo)."]),
                ]),
                ("organizacao", [
                    construir("Mudanças organizacionais", "Frente 3 · Mudanças organizacionais esperadas", "Estruturas, papéis e competências: o que muda nas empresas",
                              ["Novos papéis, capacitação e redesenho do trabalho.", "O papel da TI e das áreas de negócio na transição."],
                              ["Fichas de benchmark (seção 5).", "Notas de shadow AI e do roteiro de adoção.", "Síntese das sessões executivas."]),
                ]),
                ("riscos", [
                    construir("Oportunidades e riscos", "Frente 3 · Oportunidades e riscos estratégicos", "Oportunidades e riscos para a Acelen, em leitura macro",
                              ["Riscos tecnológicos, organizacionais e competitivos.", "As oportunidades que o estudo destaca para uma cultura perene em domesticação."],
                              ["Fecha depois dos demais temas da Frente 3."]),
                ]),
                ("ambiental", [reuso(20)]),
            ],
        },
        {
            "id": "sessoes", "nome": "Sessões executivas", "curto": "Sessões", "icone": "message-circle",
            "divisor": "Quatro conversas com executivos e lideranças técnicas, de 30 a 70 minutos, com roteiro alinhado às três frentes. Entram sem nome de pessoa nem de empresa, só no agregado.",
            "itens": [
                item("S.1", "As quatro sessões", "O retrato de cada conversa, com perfil genérico e sem números do entrevistado.", "sessoes4"),
                item("S.2", "Síntese", "O que se repete nas quatro e como elas se situam na régua.", "sintese"),
            ],
            "grupos": [
                ("sessoes4", [reuso(26), reuso(27), reuso(28), reuso(29)]),
                ("sintese", [reuso(30), reuso(31), reuso(32)]),
            ],
        },
        {
            "id": "fim", "nome": "Encerramento", "divisor": None,
            "grupos": [
                ("fim", [construir("Encerramento", "Encerramento", "Mensagens finais e próximos passos",
                                   ["As mensagens que ficam de cada frente.", "O que o estudo sugere como próximos passos, em leitura macro.", "O workshop com as lideranças."],
                                   ["Fecha junto com o resumo executivo."])]),
            ],
        },
    ]


# ---------------------------------------------------------------------------------------------
# Montagem
# ---------------------------------------------------------------------------------------------
def faixa(ns: list[int]) -> str:
    if not ns:
        return "—"
    return f"{ns[0]:02d}" if len(ns) == 1 else f"{ns[0]:02d}–{ns[-1]:02d}"


def main() -> None:
    fonte = PARCIAL.read_text(encoding="utf-8")
    css = re.search(r"<style>([\s\S]*?)</style>", fonte).group(1)
    parciais = re.findall(r'<section class="([^"]*)">([\s\S]*?)</section>', fonte)
    blocos = estrutura()

    # 1ª passada: só os slides escritos entram, numerados; o planejado vai para a lista de pendentes.
    ordem: list[dict] = [{"tipo": "capa"}]
    pendentes: list[str] = []
    partes_usadas = []
    for b in blocos:
        b["por_grupo"] = {}
        escritos = []
        for chave, slides in b["grupos"]:
            feitos = []
            for s in slides:
                s = dict(s, bloco=b)
                if s["tipo"] == "construir":
                    pendentes.append(f"{b['nome']} · {s['titulo']}")
                    continue
                if s.get("revisar"):
                    pendentes.append(f"{b['nome']} · slide {s['n']} da RP-02: {s['revisar']}")
                feitos.append(s)
            b["por_grupo"][chave] = feitos
            escritos += feitos
        if not escritos:
            continue  # parte sem slide escrito ainda: fica fora do deck
        b["slides"] = []
        if b["divisor"]:
            d = {"tipo": "divisor", "bloco": b}
            ordem.append(d)
            b["slides"].append(d)
        ordem += escritos
        b["slides"] += escritos
        partes_usadas.append(b)
    for i, s in enumerate(ordem, 1):
        s["num"] = i
    total = len(ordem)

    def pe(s: dict) -> str:
        return f'<div class="foot"><span>{RODAPE}</span><span class="mono">{s["num"]:02d} / {total:02d}</span></div>'

    def rotulo_do_bloco(b: dict, rotulo: str) -> str:
        curto = b.get("curto")
        return f"{curto} · {rotulo}" if curto and not rotulo.startswith(curto) else rotulo

    # 2ª passada: o HTML de cada slide.
    def capa() -> str:
        return f"""<section class="slide cover">
  <img class="logo" src="{LOGO}" alt="OagronomIA">
  <div class="eyebrow" style="margin-top:16mm">Benchmarking de uso de IA como diferencial estratégico · relatório final</div>
  <h1>Report Final</h1>
  <p class="lead" style="max-width:230mm">O uso de IA em empresas líderes do agro, da bioenergia, do setor florestal e de setores vizinhos: benchmark estratégico, maturidade e roadmaps, tendências.</p>
  <div style="display:flex;gap:22px;margin-top:20px;align-items:center"><i data-lucide="building-2" class="ic big"></i><i data-lucide="chart-no-axes-column-increasing" class="ic big"></i><i data-lucide="telescope" class="ic big"></i><i data-lucide="message-circle" class="ic big"></i></div>
  <div class="legend" style="margin-bottom:6mm">
    <div class="label">Contratante</div><div>Acelen Energia Renovável</div>
    <div class="label">Documento</div><div>{NOME}</div>
    <div class="label">Nº / Versão</div><div style="font-family:var(--font-mono)">{DOCUMENTO} · {REVISAO} · versão de trabalho {VERSAO}</div>
    <div class="label">Data</div><div>{date.today():%d/%m/%Y}</div>
  </div>
</section>"""

    def divisor(s: dict) -> str:
        b = s["bloco"]
        itens = [it for it in b["itens"] if b["por_grupo"][it["chave"]]]
        cartoes = "".join(
            f'<div class="rf-it{" ap" if it["ap"] else ""}"><div class="k">{it["k"]}</div><h3>{it["titulo"]}</h3><p>{it["texto"]}</p>'
            f'<div class="sl">slides {faixa([x["num"] for x in b["por_grupo"][it["chave"]]])}</div></div>'
            for it in itens)
        colunas = " c3" if len(itens) <= 3 else ""
        return f"""<section class="slide v1 rf-div">
  {cabeca(b["nome"])}
  <div class="rf-n">{b["curto"].upper()} · SLIDES {faixa([x["num"] for x in b["slides"]])}</div>
  <h1>{b["nome"].split(" · ")[-1]}</h1>
  <p class="lead" style="max-width:250mm">{b["divisor"]}</p>
  <div class="colt" style="margin-top:14px">O que esta parte traz e onde está</div>
  <div class="rf-grid{colunas}" style="margin-top:4px">{cartoes}</div>
  <div class="fontes"><b>Fontes</b><span class="f w">Escopo do estudo, seção 3. Tracejado: tema de aprofundamento</span></div>
  {pe(s)}
</section>"""

    def reaproveitado(s: dict) -> str:
        classe, corpo = parciais[s["n"] - 1]
        for de, para in CORRECOES.get(s["n"], []):
            assert corpo.count(de) == 1, (s["n"], de)
            corpo = corpo.replace(de, para)
        original = re.search(r'<span class="label">([\s\S]*?)</span>', corpo).group(1)
        rotulo = s["rotulo"] or rotulo_do_bloco(s["bloco"], original)
        corpo = corpo.replace(f'<span class="label">{original}</span>', f'<span class="label">{rotulo}</span>', 1)
        corpo, trocas = re.subn(r'<div class="foot">[\s\S]*?</div>\s*$', pe(s) + "\n", corpo)
        assert trocas == 1, s["n"]
        return f'<section class="{classe}">{corpo}</section>'

    partes = []
    for s in ordem:
        if s["tipo"] == "capa":
            partes.append(capa())
        elif s["tipo"] == "divisor":
            partes.append(divisor(s))
        elif s["tipo"] == "reuso":
            partes.append(reaproveitado(s))
        elif s["tipo"] == "novo":
            partes.append(f"""<section class="{s['classe']}">
  {cabeca(rotulo_do_bloco(s['bloco'], s['rotulo']))}
  <div class="eyebrow">{s['olho']}</div>
  <h2>{s['titulo']}</h2>
  {s['corpo']}
  {s['fontes']}
  {pe(s)}
</section>""")
        else:
            raise SystemExit(f"Tipo de slide sem montagem: {s['tipo']}")

    cabecalho = fonte[: fonte.index("<style>")]
    cabecalho = re.sub(r"<title>[\s\S]*?</title>", "<title>Report Final</title>", cabecalho)
    html = (cabecalho + "<style>" + css + CSS_EXTRA + "</style>\n</head>\n<body>\n\n" + "\n".join(partes)
            + '\n\n<script src="https://unpkg.com/lucide@0.469.0/dist/umd/lucide.min.js"></script>\n<script>if (window.lucide) lucide.createIcons();</script>\n</body>\n</html>\n')
    SAIDA.write_text(html, encoding="utf-8", newline="\n")

    print(f"{SAIDA.name}: {total} slides, só de resultado")
    for b in partes_usadas:
        print(f"  {faixa([x['num'] for x in b['slides']]):>7}  {b['nome']}")
    print(f"Pendentes, fora do deck ({len(pendentes)}):")
    for linha in pendentes:
        print(f"  - {linha}")


if __name__ == "__main__":
    main()
