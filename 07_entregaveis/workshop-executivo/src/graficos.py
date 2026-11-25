"""Peças gráficas em SVG da apresentação executiva.

Só usa as cores fixas do documento que têm variável no sistema (web/lib/apresentacoes/cores.json do
repositório do sistema): assim o gráfico acompanha o tema claro ou escuro do site. Texto em SVG só
em Manrope ou JetBrains Mono, as duas famílias que o site remapeia dentro dos gráficos.
"""
from __future__ import annotations

import math
from html import escape

VERDE = "#62A842"
VERDE_FRACO = "#3A7A2A"
VERDE_FUNDO = "#2C4A22"
LIMA = "#9BE05F"
AZUL = "#3A8FBF"
AZUL_CLARO = "#6FB8C9"
AMBAR = "#B88A28"
LARANJA = "#B85F33"
PERIGO = "#E5524A"
FG1 = "#F2F4EE"
FG2 = "#B8BFB1"
FG3 = "#7C8678"
LINHA = "#2A3328"
LINHA_FORTE = "#3A4537"
BG0 = "#050805"
BG1 = "#0B100B"
BG2 = "#131A13"
BG3 = "#1C241B"
FUNDO_VERDE = "#101A0E"
CORES = {"verde": VERDE, "fraco": VERDE_FRACO, "lima": LIMA, "ambar": AMBAR, "azul": AZUL, "azul-claro": AZUL_CLARO,
         "cinza": FG3, "laranja": LARANJA, "perigo": PERIGO}


def t(x: float, y: float, s: str, tam: float = 12.5, cor: str = FG2, fam: str = "texto", peso: int | None = None,
      anc: str | None = None) -> str:
    familia = "JetBrains Mono, monospace" if fam == "mono" else "Manrope, sans-serif"
    p = f' font-weight="{peso}"' if peso else ""
    a = f' text-anchor="{anc}"' if anc else ""
    return f'<text x="{x:.1f}" y="{y:.1f}" font-family="{familia}" font-size="{tam}"{p}{a} fill="{cor}">{escape(str(s))}</text>'


def barras_h(linhas: list[tuple], minimo: float = 0.0, maximo: float = 100.0, largura: int = 520, rotulo_w: int = 190,
             passo: int = 28, alt: float = 15.4, valor_w: int = 74, trilho: bool = True) -> str:
    """Barras horizontais. Cada linha: (rótulo, valor, texto do valor, cor[, destaque])."""
    util = largura - rotulo_w - valor_w
    svg = [f'<svg viewBox="0 0 {largura} {passo * len(linhas) + 4}">']
    for k, linha in enumerate(linhas):
        rotulo, valor, texto, cor = linha[:4]
        forte = len(linha) > 4 and linha[4]
        y = 4 + k * passo
        w = max(2.0, util * (valor - minimo) / (maximo - minimo))
        svg.append(t(rotulo_w - 10, y + alt * 0.8, rotulo, 12.5, FG1 if forte else FG2, peso=700 if forte else None, anc="end"))
        if trilho:
            svg.append(f'<rect x="{rotulo_w}" y="{y}" width="{util}" height="{alt}" rx="3" fill="{BG3}"/>')
        svg.append(f'<rect x="{rotulo_w}" y="{y}" width="{w:.1f}" height="{alt}" rx="3" fill="{CORES[cor]}"/>')
        svg.append(t(rotulo_w + util + 10, y + alt * 0.83, texto, 13.5, FG1, "mono", 500))
    svg.append("</svg>")
    return "\n".join(svg)


def colunas(itens: list[tuple], largura: int = 340, altura: int = 190, maximo: float | None = None, larg_col: int = 46,
            minimo: float = 0.0) -> str:
    """Colunas verticais. Cada item: (rótulo, valor, texto do valor, cor). Rótulo pode ter duas linhas, com '|'."""
    base, topo = altura - 38, 26
    maximo = maximo or max(i[1] for i in itens)
    n = len(itens)
    passo = largura / n
    svg = [f'<svg viewBox="0 0 {largura} {altura}">',
           f'<line x1="6" y1="{base}" x2="{largura - 6}" y2="{base}" stroke="{LINHA_FORTE}" stroke-width="1"/>']
    for k, (rotulo, valor, texto, cor) in enumerate(itens):
        cx = passo * (k + 0.5)
        fracao = (valor - minimo) / (maximo - minimo)
        h = max(3.0, (base - topo) * fracao)
        svg.append(f'<rect x="{cx - larg_col / 2:.1f}" y="{base - h:.1f}" width="{larg_col}" height="{h:.1f}" rx="4" fill="{CORES[cor]}"/>')
        svg.append(t(cx, base - h - 7, texto, 15, FG1, "mono", 500, "middle"))
        for j, parte in enumerate(rotulo.split("|")):
            svg.append(t(cx, base + 15 + j * 13, parte, 11, FG2, anc="middle"))
    svg.append("</svg>")
    return "\n".join(svg)


def rosca(pct: float, texto: str, cor: str = "verde", tam: int = 118, esp: int = 15, sub: str = "") -> str:
    """Rosca de uma fatia: pct de 0 a 100, com o texto no centro."""
    r = (tam - esp) / 2
    c = 2 * math.pi * r
    meio = tam / 2
    partes = [f'<svg viewBox="0 0 {tam} {tam}" style="width:{tam}px;height:{tam}px;flex:none">',
              f'<circle cx="{meio}" cy="{meio}" r="{r}" fill="none" stroke="{BG3}" stroke-width="{esp}"/>',
              f'<circle cx="{meio}" cy="{meio}" r="{r}" fill="none" stroke="{CORES[cor]}" stroke-width="{esp}" '
              f'stroke-dasharray="{c * pct / 100:.1f} {c:.1f}" transform="rotate(-90 {meio} {meio})"/>',
              t(meio, meio + (2 if sub else (8 if tam >= 100 else 6)), texto, 23 if tam >= 100 else 16, FG1, "mono", 500, "middle")]
    if sub:
        partes.append(t(meio, meio + 18, sub, 9.5, FG3, anc="middle"))
    partes.append("</svg>")
    return "\n".join(partes)


def escada(largura: int = 690, altura: int = 352) -> str:
    """A régua de cinco estágios em degraus, com as empresas do painel no estágio geral de cada uma."""
    nomes = ["Exploração", "Pilotos", "Operação", "Escala", "Transformação"]
    criterios = [("uso individual,", "sem caso com meta"), ("piloto medido, dono", "e regra de uso"),
                 ("caso em produção;", "política de IA publicada"), ("vários casos, área", "de IA e capacitação"),
                 ("receita com IA e", "retorno divulgado")]
    empresas = {1: ["DJI"], 2: ["Suzano", "Deere"], 3: ["Bayer"]}
    referencias = ["Aramco", "JPMorganChase"]
    base = altura - 66
    alturas = [36, 74, 112, 150, 186]
    passo, w = (largura - 14) / 5, (largura - 14) / 5 - 8
    svg = [f'<svg viewBox="0 0 {largura} {altura}">']
    for i in range(5):
        x = 8 + i * passo
        topo = base - alturas[i]
        cor_topo = VERDE if i < 4 else LINHA_FORTE
        svg.append(f'<rect x="{x:.1f}" y="{topo}" width="{w:.1f}" height="{alturas[i]}" rx="4" fill="{BG3}"/>')
        svg.append(f'<rect x="{x:.1f}" y="{topo}" width="{w:.1f}" height="4" rx="2" fill="{cor_topo}"/>')
        svg.append(t(x + 10, topo + 27, str(i + 1), 21, VERDE if i < 4 else FG3, "mono", 500))
        svg.append(t(x + 30, topo + 25, nomes[i], 13, FG1, peso=700))
        for j, linha in enumerate(criterios[i]):
            svg.append(t(x + 2, base + 17 + j * 13, linha, 10.4, FG3))
        for k, nome in enumerate(empresas.get(i, [])):
            py = topo - 30 - k * 28
            svg.append(f'<rect x="{x + 8:.1f}" y="{py}" width="{w - 16:.1f}" height="22" rx="11" fill="{VERDE}"/>')
            svg.append(t(x + w / 2, py + 15.5, nome, 12.5, BG1, peso=700, anc="middle"))
        if i == 4:
            for k, nome in enumerate(referencias):
                py = topo - 30 - k * 28
                svg.append(f'<rect x="{x + 6:.1f}" y="{py}" width="{w - 12:.1f}" height="22" rx="11" fill="none" stroke="{FG3}" stroke-width="1.2" stroke-dasharray="4 3"/>')
                svg.append(t(x + w / 2, py + 15.5, nome, 11.5, FG2, peso=600, anc="middle"))
            svg.append(t(x + 10, topo + 50, "ninguém no painel;", 10.4, FG3))
            svg.append(t(x + 10, topo + 63, "acima, referências", 10.4, FG3))
            svg.append(t(x + 10, topo + 76, "de valor divulgado,", 10.4, FG3))
            svg.append(t(x + 10, topo + 89, "sem nota no estudo", 10.4, FG3))
    # As quatro sessões executivas, no agregado: três no estágio 2, uma no 3.
    x1, x2 = 8 + passo, 8 + 2 * passo + w
    y = altura - 12
    svg.append(f'<line x1="{x1:.1f}" y1="{y - 9}" x2="{x2:.1f}" y2="{y - 9}" stroke="{AZUL_CLARO}" stroke-width="1.5"/>')
    for x in (x1, x2):
        svg.append(f'<line x1="{x:.1f}" y1="{y - 14}" x2="{x:.1f}" y2="{y - 4}" stroke="{AZUL_CLARO}" stroke-width="1.5"/>')
    svg.append(t((x1 + x2) / 2, y + 6, "sessões executivas: três no estágio 2, uma no 3", 10.8, AZUL_CLARO, peso=600, anc="middle"))
    svg.append("</svg>")
    return "\n".join(svg)


def gantt(linhas: list[tuple], ano0: int = 2015, ano1: int = 2026, largura: int = 1136, rotulo_w: int = 372, dur_w: int = 150,
          passo: int = 46) -> str:
    """Barras no tempo. Cada linha: (título, detalhe, início, fim, duração, cor), com início e fim em anos decimais."""
    x0, x1 = rotulo_w, largura - dur_w
    por_ano = (x1 - x0) / (ano1 - ano0)
    topo = 26
    altura = topo + passo * len(linhas) + 6
    svg = [f'<svg viewBox="0 0 {largura} {altura}">']
    for ano in range(ano0, ano1 + 1):
        x = x0 + (ano - ano0) * por_ano
        svg.append(f'<line x1="{x:.1f}" y1="{topo - 4}" x2="{x:.1f}" y2="{altura - 4}" stroke="{LINHA}" stroke-width="1"/>')
        svg.append(t(x, 13, str(ano), 10.5, FG3, "mono", anc="middle"))
    for k, (titulo, detalhe, inicio, fim, duracao, cor) in enumerate(linhas):
        y = topo + k * passo
        svg.append(t(0, y + 19, titulo, 13.5, FG1, peso=700))
        svg.append(t(0, y + 35, detalhe, 11, FG3))
        xa, xb = x0 + (inicio - ano0) * por_ano, x0 + (fim - ano0) * por_ano
        svg.append(f'<rect x="{xa:.1f}" y="{y + 12}" width="{max(8.0, xb - xa):.1f}" height="18" rx="9" fill="{CORES[cor]}"/>')
        svg.append(t(largura, y + 26, duracao, 14, FG1, "mono", 500, "end"))
    svg.append("</svg>")
    return "\n".join(svg)


def inclinacao(series: list[tuple], esquerda: str, direita: str, largura: int = 520, altura: int = 232) -> str:
    """Duas datas, uma linha por série. Cada série: (rótulo, valor antes, valor depois, cor), em %."""
    xa, xb = 206, largura - 110
    topo, base = 34, altura - 14

    def y(v: float) -> float:
        return base - (base - topo) * v / 100

    svg = [f'<svg viewBox="0 0 {largura} {altura}">',
           t(xa, 14, esquerda, 11, FG3, "mono", anc="middle"), t(xb, 14, direita, 11, FG3, "mono", anc="middle"),
           f'<line x1="{xa}" y1="{topo - 8}" x2="{xa}" y2="{base}" stroke="{LINHA_FORTE}" stroke-width="1"/>',
           f'<line x1="{xb}" y1="{topo - 8}" x2="{xb}" y2="{base}" stroke="{LINHA_FORTE}" stroke-width="1"/>']
    desloca = {}
    if len(series) == 2 and abs(y(series[0][2]) - y(series[1][2])) < 28:
        cima = 0 if series[0][2] > series[1][2] else 1
        falta = (28 - abs(y(series[0][2]) - y(series[1][2]))) / 2
        desloca = {cima: -falta, 1 - cima: falta}
    for k, (rotulo, antes, depois, cor) in enumerate(series):
        c = CORES[cor]
        svg.append(f'<line x1="{xa}" y1="{y(antes):.1f}" x2="{xb}" y2="{y(depois):.1f}" stroke="{c}" stroke-width="3.2" stroke-linecap="round"/>')
        for x, v in ((xa, antes), (xb, depois)):
            svg.append(f'<circle cx="{x}" cy="{y(v):.1f}" r="6.5" fill="{c}"/>')
        svg.append(t(xa - 16, y(antes) + 6, f"{antes:.0f}%", 19, FG1, "mono", 500, "end"))
        svg.append(t(xa - 70, y(antes) + 5, rotulo, 11.5, FG2, anc="end"))
        svg.append(t(xb + 16, y(depois) + 7 + desloca.get(k, 0), f"{depois:.0f}%", 24, FG1, "mono", 500))
    svg.append("</svg>")
    return "\n".join(svg)


def faixas_tempo(itens: list[tuple], maximo: float = 4.0, largura: int = 340, altura: int = 150) -> str:
    """Faixas de duração num eixo em anos. Cada item: (rótulo, de, até, texto, cor)."""
    x0, x1 = 12, largura - 12
    por = (x1 - x0) / maximo
    base = altura - 24
    svg = [f'<svg viewBox="0 0 {largura} {altura}">',
           f'<line x1="{x0}" y1="{base}" x2="{x1}" y2="{base}" stroke="{LINHA_FORTE}" stroke-width="1"/>']
    for a in range(0, int(maximo) + 1):
        x = x0 + a * por
        svg.append(f'<line x1="{x:.1f}" y1="{base}" x2="{x:.1f}" y2="{base + 4}" stroke="{LINHA_FORTE}" stroke-width="1"/>')
        svg.append(t(x, base + 17, f"{a} ano" + ("s" if a != 1 else "") if a else "0", 10, FG3, "mono", anc="middle" if 0 < a < maximo else ("start" if a == 0 else "end")))
    for k, (rotulo, de, ate, texto, cor) in enumerate(itens):
        y = 8 + k * 50
        svg.append(t(x0, y + 11, rotulo, 11.5, FG2))
        svg.append(f'<rect x="{x0 + de * por:.1f}" y="{y + 18}" width="{(ate - de) * por:.1f}" height="16" rx="8" fill="{CORES[cor]}"/>')
        tx = x0 + ate * por + 8
        ancora = "start"
        if tx > largura - 96:
            tx, ancora = x0 + de * por - 8, "end"
        svg.append(t(tx, y + 31, texto, 14, FG1, "mono", 500, ancora))
    svg.append("</svg>")
    return "\n".join(svg)


def concentracao(largura: int = 340, altura: int = 150) -> str:
    """20% das empresas ficam com 74% do retorno: dez empresas, duas em destaque, e a barra do retorno."""
    svg = [f'<svg viewBox="0 0 {largura} {altura}">', t(12, 15, "Empresas", 11.5, FG2)]
    lado, vao = 24, 7.5
    for k in range(10):
        x = 12 + k * (lado + vao)
        svg.append(f'<rect x="{x:.1f}" y="24" width="{lado}" height="{lado}" rx="5" fill="{VERDE if k < 2 else BG3}"/>')
    svg.append(t(12, 66, "20%", 17, FG1, "mono", 500))
    svg.append(t(58, 65, "das empresas", 11, FG3))
    svg.append(t(12, 93, "Retorno da IA", 11.5, FG2))
    total = largura - 24
    svg.append(f'<rect x="12" y="101" width="{total}" height="20" rx="5" fill="{BG3}"/>')
    svg.append(f'<rect x="12" y="101" width="{total * 0.74:.1f}" height="20" rx="5" fill="{VERDE}"/>')
    svg.append(t(12, 143, "74%", 17, FG1, "mono", 500))
    svg.append(t(58, 142, "do retorno fica com elas", 11, FG3))
    svg.append("</svg>")
    return "\n".join(svg)


def eixo_marcos(marcos: list[tuple], inicio: float, fim: float, rotulos: list[tuple], largura: int = 1136, altura: int = 54) -> str:
    """Eixo horizontal com marcos. marcos: (posição, cor); rotulos: (posição, texto) do eixo."""
    x0, x1 = 20, largura - 20
    por = (x1 - x0) / (fim - inicio)
    y = 22
    svg = [f'<svg viewBox="0 0 {largura} {altura}">',
           f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{LINHA_FORTE}" stroke-width="2"/>']
    for pos, texto in rotulos:
        x = x0 + (pos - inicio) * por
        ancora = "start" if pos == inicio else ("end" if pos == fim else "middle")
        svg.append(f'<line x1="{x:.1f}" y1="{y - 5}" x2="{x:.1f}" y2="{y + 5}" stroke="{LINHA_FORTE}" stroke-width="1.5"/>')
        svg.append(t(x, y + 22, texto, 10.5, FG3, "mono", anc=ancora))
    for pos, cor in marcos:
        x = x0 + (pos - inicio) * por
        svg.append(f'<circle cx="{x:.1f}" cy="{y}" r="8" fill="{CORES[cor]}" stroke="{BG2}" stroke-width="3"/>')
    svg.append("</svg>")
    return "\n".join(svg)


def capa_ilustracao() -> str:
    """Ilustração da capa: a régua em degraus e a trajetória em seis marcos."""
    largura, altura = 470, 330
    svg = [f'<svg class="capa-il" viewBox="0 0 {largura} {altura}">']
    base = altura - 20
    alturas = [50, 100, 150, 200, 250]
    w = 78
    for i, h in enumerate(alturas):
        x = 14 + i * 90
        svg.append(f'<rect x="{x}" y="{base - h}" width="{w}" height="{h}" rx="5" fill="{BG2}" stroke="{LINHA}" stroke-width="1"/>')
        svg.append(f'<rect x="{x}" y="{base - h}" width="{w}" height="5" rx="2.5" fill="{VERDE if i < 4 else LINHA_FORTE}"/>')
        svg.append(t(x + w / 2, base - h + 36, str(i + 1), 26, FG3 if i == 4 else VERDE, "mono", 500, "middle"))
    pontos = [(30, base - 78), (106, base - 122), (188, base - 176), (262, base - 214), (346, base - 268), (432, base - 296)]
    caminho = " ".join(f"{'M' if k == 0 else 'L'}{x},{y}" for k, (x, y) in enumerate(pontos))
    svg.append(f'<path d="{caminho}" fill="none" stroke="{LIMA}" stroke-width="2" stroke-dasharray="6 6"/>')
    for k, (x, y) in enumerate(pontos):
        svg.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{BG0}" stroke="{LIMA}" stroke-width="2.4"/>')
    svg.append("</svg>")
    return "\n".join(svg)


def duas_linhas(serie_a: list[tuple], serie_b: list[tuple], meses: list[str], marcos: list[tuple], rotulo_a: tuple, rotulo_b: tuple,
                largura: int = 640, altura: int = 318, maximo: float = 250) -> str:
    """Duas séries em índice no tempo, com a área entre elas a partir de um ponto ("a boca se abre").
    Séries: listas de (posição no eixo, valor), com a posição em meses a partir do primeiro rótulo.
    marcos: (posição, linha 1, linha 2) das linhas tracejadas; rotulo_*: (texto grande, texto pequeno) no fim de cada série."""
    x0, x1 = 34, largura - 150
    topo, base = 16, altura - 26
    fim = max(serie_a[-1][0], serie_b[-1][0])

    def px(m: float) -> float:
        return x0 + (x1 - x0) * m / fim

    def py(v: float) -> float:
        return base - (base - topo) * v / maximo

    svg = [f'<svg viewBox="0 0 {largura} {altura}">']
    for v in range(0, int(maximo) + 1, 50):
        svg.append(f'<line x1="{x0}" y1="{py(v):.1f}" x2="{x1}" y2="{py(v):.1f}" stroke="{LINHA}" stroke-width="1"/>')
        svg.append(t(x0 - 8, py(v) + 4, str(v), 10, FG3, "mono", anc="end"))
    for k, mes in enumerate(meses):
        svg.append(t(px(k), base + 16, mes, 10.5, FG3, anc="middle"))
    # a boca: área entre as duas séries depois do último marco
    abre = marcos[-1][0]
    cima = [(m, v) for m, v in serie_a if m >= abre]
    baixo = [(m, v) for m, v in serie_b if m >= abre]
    pontos = " ".join(f"{px(m):.1f},{py(v):.1f}" for m, v in cima) + " " + " ".join(f"{px(m):.1f},{py(v):.1f}" for m, v in reversed(baixo))
    svg.append(f'<polygon points="{pontos}" fill="{VERDE_FUNDO}" fill-opacity="0.55"/>')
    for pos, linha1, linha2 in marcos:
        svg.append(f'<line x1="{px(pos):.1f}" y1="{topo}" x2="{px(pos):.1f}" y2="{base}" stroke="{FG3}" stroke-width="1" stroke-dasharray="4 4"/>')
        svg.append(t(px(pos) + 6, topo + 9, linha1, 10.5, FG2, peso=600))
        if linha2:
            svg.append(t(px(pos) + 6, topo + 22, linha2, 10.5, FG2))
    for serie, cor in ((serie_b, AMBAR), (serie_a, VERDE)):
        caminho = " ".join(f"{'M' if k == 0 else 'L'}{px(m):.1f},{py(v):.1f}" for k, (m, v) in enumerate(serie))
        svg.append(f'<path d="{caminho}" fill="none" stroke="{cor}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
        m, v = serie[-1]
        svg.append(f'<circle cx="{px(m):.1f}" cy="{py(v):.1f}" r="5" fill="{cor}"/>')
    for serie, (grande, pequeno) in ((serie_a, rotulo_a), (serie_b, rotulo_b)):
        m, v = serie[-1]
        svg.append(t(px(m) + 12, py(v) + 2, grande, 24, FG1, "mono", 500))
        svg.append(t(px(m) + 12, py(v) + 18, pequeno, 10.5, FG3))
    svg.append("</svg>")
    return "\n".join(svg)


def alcance(colunas_: list[tuple], faixa: tuple, maximo: float = 24.0, largura: int = 640, altura: int = 318) -> str:
    """Até onde cada ferramenta alcança, em metros, ao lado de uma palmeira com espinhos no estipe.
    colunas_: (rótulo com '|' entre as linhas, altura mínima ou None, altura máxima ou None, texto, cor);
    altura máxima None desenha a coluna tracejada ("não informada"). faixa: (de, até, linha 1, linha 2)."""
    x0, x1 = 40, largura - 8
    linhas_rotulo = max(len(c[0].split("|")) for c in colunas_)
    topo, base = 22, altura - (10 + 13 * linhas_rotulo)

    def py(m: float) -> float:
        return base - (base - topo) * m / maximo

    svg = [f'<svg viewBox="0 0 {largura} {altura}">']
    de, ate, linha1, linha2 = faixa
    svg.append(f'<rect x="{x0}" y="{py(ate):.1f}" width="{x1 - x0}" height="{py(de) - py(ate):.1f}" fill="{VERDE_FUNDO}" fill-opacity="0.5"/>')
    for m in range(0, int(maximo) + 1, 5):
        svg.append(f'<line x1="{x0}" y1="{py(m):.1f}" x2="{x1}" y2="{py(m):.1f}" stroke="{LINHA}" stroke-width="1"/>')
        svg.append(t(x0 - 7, py(m) + 4, f"{m} m" if m else "0", 10, FG3, "mono", anc="end"))
    # a palmeira: estipe com espinhos, copa e cacho
    px_, copa = x0 + 54, py((de + ate) / 2)
    svg.append(f'<path d="M{px_ - 5},{base} L{px_ - 3.2},{copa:.1f} L{px_ + 3.2},{copa:.1f} L{px_ + 5},{base} Z" fill="{LINHA_FORTE}"/>')
    passo = (base - copa) / 13
    for k in range(1, 13):
        y = base - k * passo
        lado = -1 if k % 2 else 1
        svg.append(f'<line x1="{px_ + lado * 4:.1f}" y1="{y:.1f}" x2="{px_ + lado * 10:.1f}" y2="{y - 3:.1f}" stroke="{FG3}" stroke-width="1.2" stroke-linecap="round"/>')
    for dx, dy in ((-44, -4), (-36, -24), (-17, -37), (17, -37), (36, -24), (44, -4)):
        svg.append(f'<path d="M{px_},{copa:.1f} Q{px_ + dx * 0.55:.1f},{copa + dy * 1.25:.1f} {px_ + dx},{copa + dy + 15:.1f}" '
                   f'fill="none" stroke="{VERDE}" stroke-width="3.2" stroke-linecap="round"/>')
    for dx, dy in ((7, 9), (12, 15), (6, 19), (11, 24)):
        svg.append(f'<circle cx="{px_ + dx}" cy="{copa + dy:.1f}" r="3.6" fill="{AMBAR}"/>')
    svg.append(t(px_ + 58, py(ate) + 15, linha1, 11, FG1, peso=700))
    svg.append(t(px_ + 58, py(ate) + 29, linha2, 10.5, FG2))
    # as colunas
    ini = x0 + 128
    vao = (x1 - ini) / len(colunas_)
    larg = min(46.0, vao * 0.5)
    for k, (rotulo, minimo, maximo_c, texto, cor) in enumerate(colunas_):
        cx = ini + vao * (k + 0.5)
        if maximo_c is None:
            alto = py(maximo * 0.42)
            svg.append(f'<rect x="{cx - larg / 2:.1f}" y="{alto:.1f}" width="{larg:.1f}" height="{base - alto:.1f}" rx="4" fill="none" '
                       f'stroke="{CORES[cor]}" stroke-width="1.6" stroke-dasharray="5 4"/>')
            svg.append(t(cx, alto - 8, texto, 15, FG1, "mono", 500, "middle"))
        else:
            alto = py(maximo_c)
            svg.append(f'<rect x="{cx - larg / 2:.1f}" y="{alto:.1f}" width="{larg:.1f}" height="{base - alto:.1f}" rx="4" fill="{CORES[cor]}"/>')
            if minimo:
                svg.append(f'<rect x="{cx - larg / 2:.1f}" y="{alto:.1f}" width="{larg:.1f}" height="{py(minimo) - alto:.1f}" rx="4" fill="{BG1}" fill-opacity="0.45"/>')
            svg.append(t(cx, alto - 8, texto, 13.5, FG1, "mono", 500, "middle"))
        for n, parte in enumerate(rotulo.split("|")):
            svg.append(t(cx, base + 16 + n * 13, parte, 10.5, FG1 if cor == "verde" else FG2, peso=700 if cor == "verde" else None, anc="middle"))
    svg.append(f'<line x1="{x0}" y1="{base}" x2="{x1}" y2="{base}" stroke="{LINHA_FORTE}" stroke-width="1.2"/>')
    svg.append("</svg>")
    return "\n".join(svg)
