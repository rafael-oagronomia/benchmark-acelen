"""Slides de metodologia da apresentação executiva (pedido do Guilherme de 23/11/2026): as frentes
avaliadas, o que buscamos no mercado, o tamanho do acervo, as sessões executivas e como cada número
foi conferido.

O texto segue o descritivo da metodologia (01_mobilizacao/metodologia.md, BIA-ACL-MT-01 Rev. 01). Os
números do acervo vêm da contagem do sistema (web/lib/numeros.json do repositório rag-benchmark-acelen,
gerado pelo pipeline 00 a partir do catálogo): rodar o 00 antes de gerar o deck para a contagem ficar em dia.
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

NUMEROS = Path(__file__).resolve().parents[3].parent / "rag-benchmark-acelen/web/lib/numeros.json"
FONTE_MT = "Descritivo da metodologia (BIA-ACL-MT-01, Rev. 01), seções 1 a 9"

CSS = """
  /* ---- Metodologia ---- */
  .mf4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 12px; }
  .mf4 .c { background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; padding: 12px 14px; display: flex; flex-direction: column; gap: 6px; }
  .mf4 .c.s { border-color: var(--brand-green); background: #101A0E; }
  .mf4 .c .top { display: flex; align-items: center; gap: 10px; }
  .mf4 .c .top svg.lucide { width: 26px !important; height: 26px !important; }
  .mf4 .c .k { font: 600 10px var(--font-display); letter-spacing: 0.14em; text-transform: uppercase; color: var(--brand-green-bright); }
  .mf4 .c h3 { font-size: 15.5px; line-height: 1.2; }
  .mf4 .c p { font-size: 12px; color: var(--fg-2); line-height: 1.4; }
  .mf4 .c .n { font: 500 30px/1 var(--font-mono); color: var(--fg-1); margin-top: 2px; }
  .mf4 .c .n small { font: 400 11px var(--font-body); color: var(--fg-3); margin-left: 6px; }
  .mf4 .c ul { list-style: none; margin: 2px 0 0; padding: 0; display: grid; gap: 4px; }
  .mf4 .c li { font-size: 11.5px; color: var(--fg-2); line-height: 1.34; padding-left: 12px; position: relative; }
  .mf4 .c li::before { content: ""; position: absolute; left: 0; top: 6px; width: 5px; height: 5px; border-radius: 50%; background: var(--brand-green); }
  .mf4 .c li b { color: var(--fg-1); }
  .et5 { display: grid; grid-template-columns: repeat(5, 1fr); gap: 0; margin-top: 12px; }
  .et5 .e { position: relative; padding: 9px 14px 9px 30px; background: var(--bg-1); border: 1px solid var(--line); border-right: 0; }
  .et5 .e:first-child { border-radius: 10px 0 0 10px; }
  .et5 .e:last-child { border-radius: 0 10px 10px 0; border-right: 1px solid var(--line); }
  .et5 .e .no { position: absolute; left: 9px; top: 9px; font: 600 13px var(--font-mono); color: var(--brand-green); }
  .et5 .e h4 { font: 600 12.5px var(--font-display); color: var(--fg-1); }
  .et5 .e p { font-size: 10.8px; color: var(--fg-3); margin-top: 2px; line-height: 1.32; }
  .prc { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 10px; }
  .prc span { border: 1px solid var(--line); background: var(--bg-2); border-radius: 999px; padding: 5px 12px; font-size: 11px; color: var(--fg-2); }
  .prc span b { color: var(--fg-1); }
  .prc span.out { border-style: dashed; color: var(--fg-3); }
  .bq5 { display: grid; gap: 7px; margin-top: 6px; }
  .bq5 .b { display: grid; grid-template-columns: 28px 1fr; gap: 10px; align-items: start; }
  .bq5 .b svg.lucide { width: 22px !important; height: 22px !important; margin-top: 1px !important; }
  .bq5 .b .k { font: 600 13px var(--font-display); color: var(--fg-1); }
  .bq5 .b p { font-size: 11.6px; color: var(--fg-2); line-height: 1.36; margin-top: 1px; }
  .fl6 { display: grid; grid-template-columns: repeat(6, 1fr); gap: 8px; margin-top: 12px; }
  .fl6 .s { background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; padding: 10px 12px; display: flex; flex-direction: column; gap: 4px; position: relative; }
  .fl6 .s.on { border-color: var(--brand-green); background: #101A0E; }
  .fl6 .s .top { display: flex; align-items: center; justify-content: space-between; }
  .fl6 .s .top svg.lucide { width: 22px !important; height: 22px !important; }
  .fl6 .s .no { font: 600 11px var(--font-mono); color: var(--fg-3); }
  .fl6 .s .q { font: 600 9.5px var(--font-display); letter-spacing: 0.12em; text-transform: uppercase; color: var(--brand-green-bright); }
  .fl6 .s h3 { font-size: 14px; line-height: 1.2; }
  .fl6 .s p { font-size: 11px; color: var(--fg-2); line-height: 1.34; }
  .fl6 .s .n { font: 500 22px/1.05 var(--font-mono); color: var(--fg-1); margin-top: auto; padding-top: 4px; }
  .fl6 .s .n small { display: block; font: 400 10px/1.3 var(--font-body); color: var(--fg-3); margin-top: 2px; }
  .cl4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }
  .cl4 .cx { display: grid; grid-template-columns: 30px 1fr; gap: 10px; align-items: center; background: var(--bg-1); border: 1px solid var(--line); border-radius: 8px; padding: 7px 10px; }
  .cl4 .cx .l { width: 30px; height: 30px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font: 600 15px var(--font-mono); color: #0B100B; background: var(--brand-green); }
  .cl4 .cx.eb .l { background: #3A8FBF; }
  .cl4 .cx.ec .l { background: #B88A28; }
  .cl4 .cx.ed .l { background: #7C8678; }
  .cl4 .cx p { font-size: 11px; color: var(--fg-2); line-height: 1.32; }
  .cl4 .cx p b { color: var(--fg-1); }
"""


def milhar(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def numeros() -> dict:
    return json.loads(NUMEROS.read_text(encoding="utf-8"))


def slides(g, s, ic, painel, faixa) -> list[dict]:
    n = numeros()
    ac, cf, vf, es = n["acervo"], n["conferencia"], n["verificacao"], n["estudos"]
    contagem = date.fromisoformat(n["contagem_em"]).strftime("%d/%m/%Y")
    pct_recentes = round(100 * ac["recentes"] / ac["fontes"])
    pct_achadas = f"{100 * cf['metricas_achadas'] / cf['metricas_total']:.1f}".replace(".", ",")
    mil_paginas = f"{ac['paginas'] / 1000:.1f}".replace(".", ",")
    fontes_mt = (f'<div class="fontes"><b>Fontes</b><span class="f w">{FONTE_MT}. Números do acervo: catálogo do estudo, '
                 f'contagem de {contagem} (página Números do sistema).</span></div>')

    # ---------------- 1. As frentes, as sessões e as etapas ----------------
    def frente(classe, icone, rotulo, titulo, texto, itens):
        lista = "".join(f"<li>{i}</li>" for i in itens)
        return (f'<div class="c {classe}"><div class="top">{ic(icone)}<span class="k">{rotulo}</span></div>'
                f"<h3>{titulo}</h3><p>{texto}</p><ul>{lista}</ul></div>")

    def etapa(no, titulo, texto):
        return f'<div class="e"><span class="no">{no}</span><h4>{titulo}</h4><p>{texto}</p></div>'

    estudo = s(
        "O estudo", "Metodologia · escopo, frentes e etapas",
        "Três frentes e quatro sessões executivas, sobre evidência pública e verificável",
        '<div class="mf4">'
        + frente("", "building-2", "Frente 1", "Benchmark estratégico",
                 "Como as empresas líderes usam a IA como diferencial: o que funcionou, o que falhou e por quê.",
                 [f"<b>{es['fichas']} fichas</b> no mesmo padrão: Suzano e Bayer, indicadas pela Acelen; Deere e DJI, a corrida EUA × China",
                  "<b>Setores de referência:</b> bancos e energia, de maior maturidade digital",
                  "<b>Casos</b> de sucesso e insucesso, com a lição"])
        + frente("", "chart-no-axes-column-increasing", "Frente 2", "Maturidade e roadmaps",
                 "Um referencial para a Acelen se situar no mercado e enxergar os próximos passos.",
                 ["<b>Régua de 5 estágios × 4 dimensões,</b> a partir da revisão dos frameworks de mercado",
                  "<b>Checkpoints</b> e dependências de cada salto",
                  "<b>Roteiro</b> que o mercado seguiu, com o ritmo"])
        + frente("", "telescope", "Frente 3", "Tendências",
                 "O que deve moldar a IA no agro, separando tendência consolidada de sinal emergente.",
                 ["<b>Custo de uso da IA</b> e IA generativa",
                  "<b>Autonomia, perenes e colheita,</b> satélites e modelos de fundação",
                  "<b>EUA × China</b> e impacto ambiental da IA"])
        + frente("s", "message-circle", "Leitura primária", f"{es['sessoes']} sessões executivas",
                 "Conversas semiestruturadas com executivos e lideranças técnicas de grandes empresas do agro e da bioenergia.",
                 ["<b>De 13 a 21/10/2026,</b> de 30 a 70 minutos cada",
                  "<b>Roteiro de 10 temas</b> alinhados às frentes, validado pela Acelen em 09/10",
                  "<b>Sem nomes:</b> pessoas e empresas só no agregado"])
        + "</div>"
        + '<div class="et5">'
        + etapa(1, "Mobilização e desenho", "Painel, dimensões, protocolo de pesquisa e ficha padrão")
        + etapa(2, "Coleta e análise", "Fontes públicas em rodadas; fichas e notas por frente")
        + etapa(3, "Sessões executivas", "Registro anonimizado e síntese por frente")
        + etapa(4, "Síntese", "Régua, posicionamento, roteiro e tendências")
        + etapa(5, "Entrega e workshop", "Report Final, base de dados, assistente de IA e esta apresentação")
        + "</div>"
        + '<div class="prc"><span><b>Visão macro,</b> horizonte de cinco anos</span><span><b>IA em sentido amplo:</b> generativa, preditiva, visão, robótica e autonomia</span>'
          '<span><b>Brasil primeiro,</b> com EUA, China e setores mais maduros</span><span><b>Toda afirmação</b> com fonte e página</span>'
          '<span class="out">Fora do escopo: diagnóstico interno e recomendação de ferramenta</span></div>',
        fontes_mt)

    # ---------------- 2. O que buscamos e o tamanho do acervo ----------------
    def busca(icone, titulo, texto):
        return f'<div class="b">{ic(icone)}<div><div class="k">{titulo}</div><p>{texto}</p></div></div>'

    anos = [(a["rotulo"].replace("até ", "≤ "), a["valor"], milhar(a["valor"]), "verde" if a["rotulo"] in ("2024", "2025", "2026") else "cinza")
            for a in n["por_ano"]]
    temas = sorted(n["por_tema"], key=lambda t: -t["valor"])
    curto = {"Agro global, perenes e autonomia": "Agro global e perenes", "Agro Brasil: instituições e mídia": "Agro Brasil: instituições",
             "Empresas de agro, bioenergia e florestal": "Empresas do agro e florestal", "Big Four, Accenture e Capgemini": "Big Four e Accenture",
             "Consultorias de estratégia": "Consultorias de estratégia", "Outros setores maduros": "Outros setores maduros"}
    barras_temas = [(curto.get(t["rotulo"], t["rotulo"]), t["valor"], milhar(t["valor"]), "verde" if i < 3 else "cinza") for i, t in enumerate(temas)]

    acervo = s(
        "O estudo", "Metodologia · o que buscamos no mercado e quanto material foi lido",
        f"{milhar(ac['fontes'])} fontes públicas, {pct_recentes}% delas de 2024 a 2026",
        '<div class="g3" style="grid-template-columns:0.9fr 1fr 1.1fr;margin-top:12px">'
        + painel("O que procuramos em cada fonte", "O número com unidade, escopo, ano e página",
                 '<div class="bq5">'
                 + busca("users", "Adoção", "Quem usa IA, em quê e quanto: empresas, produtores, empregados.")
                 + busca("target", "Resultado medido", "Ganho, redução de custo ou de insumo e retorno, com a linha de base.")
                 + busca("chart-no-axes-column-increasing", "Maturidade", "O estágio de cada empresa em cada dimensão, pela evidência pública.")
                 + busca("timer", "Ritmo", "Quanto tempo cada etapa levou, do alicerce à escala.")
                 + busca("lightbulb", "Casos e lições", "Sucessos e insucessos, com a causa declarada.")
                 + "</div>")
        + painel("Fontes por ano de publicação", f"Catálogo do estudo, {contagem}",
                 g.colunas(anos, largura=400, altura=238, larg_col=34))
        + painel("Fontes por grupo", "Rodadas por tipo de fonte, por empresa e por tema",
                 g.barras_h(barras_temas, maximo=max(t[1] for t in barras_temas) * 1.08, largura=470, rotulo_w=196, passo=20, alt=12, valor_w=46))
        + "</div>"
        + faixa([("book-open", f"{mil_paginas} mil", f"<b>páginas lidas</b> em {milhar(ac['com_copia'])} documentos guardados, e {milhar(ac['web'])} páginas web"),
                 ("quote", milhar(ac["citadas"]), "<b>fontes citadas</b> nas fichas, nas notas e no Report Final"),
                 ("file-text", f"{es['fichas']} + {es['notas']}", "<b>fichas de empresa</b> e <b>notas temáticas</b>, todas com fonte e página"),
                 ("message-circle", str(es["sessoes"]), "<b>sessões executivas</b>, com registro anonimizado e síntese por frente")]),
        fontes_mt)

    # ---------------- 3. Como cada número chega ao estudo ----------------
    def passo(no, icone, quem, titulo, texto, numero="", legenda="", on=False):
        num = f'<div class="n">{numero}<small>{legenda}</small></div>' if numero else ""
        return (f'<div class="s{" on" if on else ""}"><div class="top">{ic(icone)}<span class="no">{no:02d}</span></div>'
                f'<div class="q">{quem}</div><h3>{titulo}</h3><p>{texto}</p>{num}</div>')

    emp = sorted(n["empresas"], key=lambda e: -e["afirmacoes"])
    conferencia = s(
        "O estudo", "Metodologia · conferência e controle de qualidade",
        "Nenhum número entra sem fonte conferida: quem pesquisa não confere",
        '<div class="fl6">'
        + passo(1, "search", "Agente pesquisador", "Busca", "Rodadas por tipo de fonte, por empresa e por tema; cada número anotado com a página.")
        + passo(2, "scan-eye", "Programa", "Conferência automática", "Procura cada número no texto da página citada.",
                milhar(cf["metricas_achadas"]), f"de {milhar(cf['metricas_total'])} métricas achadas ({pct_achadas}%)")
        + passo(3, "badge-check", "Outro agente", "Verificação", "Abre a fonte e confirma, corrige ou retira, afirmação por afirmação.",
                milhar(vf["conferidas"]), f"conferidas nas 7 pesquisas dirigidas; {vf['retiradas']} retiradas", True)
        + passo(4, "database", "Catálogo", "Identificador fixo", "Cada documento vira M001, M002…, com link, data e páginas.",
                milhar(ac["fontes"]), "fontes no catálogo")
        + passo(5, "file-text", "Redator e revisor", "Fichas e notas", "Toda afirmação cita o identificador e a página; um revisor tenta derrubar o texto.")
        + passo(6, "user-check", "Equipe OagronomIA", "Aprovação", "Escreveu as regras de cada etapa e aprova cada entrega: nada chega à Acelen sem ela.")
        + "</div>"
        + '<div class="g2" style="grid-template-columns:1.25fr 1fr;margin-top:10px">'
        + painel("Força da evidência: cada número leva a sua classe", "As regras valem para fichas, notas, gráficos e para o assistente de IA",
                 '<div class="cl4">'
                 '<div class="cx"><span class="l">A</span><p><b>Medido por terceiro</b> ou em artigo revisado por pares</p></div>'
                 '<div class="cx eb"><span class="l">B</span><p><b>Documento oficial</b> da empresa, do governo ou da instituição</p></div>'
                 '<div class="cx ec"><span class="l">C</span><p><b>Meta, previsão,</b> estimativa ou simulação</p></div>'
                 '<div class="cx ed"><span class="l">D</span><p><b>Quem vende</b> a tecnologia, ou só a imprensa</p></div></div>'
                 '<div class="prc" style="margin-top:9px"><span>Anúncio não é resultado</span><span>Piloto não é produção</span><span>Meta não é realizado</span>'
                 '<span>Global não é Brasil</span><span>Opinião não é medição</span></div>')
        + painel("As quatro fichas: afirmações com fonte e página", "Afirmações na ficha e páginas lidas dos documentos da própria empresa",
                 g.barras_h([(e["nome"], e["afirmacoes"], f"{e['afirmacoes']} · {milhar(e['paginas_lidas'])} p.", "verde" if i == 0 else "fraco")
                             for i, e in enumerate(emp)], maximo=emp[0]["afirmacoes"] * 1.05, largura=470, rotulo_w=86, passo=27, alt=15, valor_w=120))
        + "</div>",
        fontes_mt)

    return [estudo, acervo, conferencia]
