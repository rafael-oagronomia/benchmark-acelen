"""Slides da apresentação executiva (BIA-ACL-AE-01).

Todo número vem de uma nota, ficha ou slide já conferido do estudo, com a mesma citação:
- painel e régua: fichas de benchmark e slides 4, 12 e 13 do Report Final;
- casos: ficha da Suzano, nota IA no campo (seção de aplicação seletiva) e nota de custo da IA (Uber e iFood);
- roteiro (caminho, checkpoints principais e índices do mercado): nota roadmap-de-adocao.md, seções 3, 4, 8 e 10
  (as mesmas frases da página Roteiro do sistema);
- shadow AI, retorno e custo: notas shadow-ai-e-governanca.md, custo-da-ia.md e slides 6, 14, 15 e 22 do Report Final;
- campo, perenes e satélites: notas ia-no-campo.md e satelites-e-modelos-de-fundacao.md;
- colheita da macaúba e robôs que sobem na palmeira: nota ia-no-campo.md, seção 7.4 (fontes lidas na web, sem cópia guardada);
- sessões executivas: síntese agregada (slides 45 a 47 do Report Final), sem perfil de empresa;
- metodologia (três primeiros slides): descritivo BIA-ACL-MT-01 e contagem do catálogo (slides_metodologia.py).
Ao mudar uma nota, mudar aqui também.
"""
from __future__ import annotations

import slides_metodologia

F1 = "Frente 1 · Onde o mercado está"
F2 = "Frente 2 · Como o mercado chegou lá"
F3 = "Frente 3 · Para onde vai"
ZOOM = [1.07, 1.06, 1.11,
        1, 1, 1.10, 1.10, 1.09, 1.09, 1, 1,
        0.95, 1.10, 1.03, 1.05, 1.20, 1.09,
        1.30, 1.12, 1.15, 1.0, 1.0, 1.14, 1.16,
        1.10, 1.06]


def slides(fontes, g) -> list[dict]:
    def ic(nome: str, classe: str = "ic") -> str:
        return f'<i data-lucide="{nome}" class="{classe}"></i>'

    def painel(titulo: str, sub: str, corpo: str, estilo: str = "") -> str:
        sub_html = f'<div class="sub">{sub}</div>' if sub else ""
        est = f' style="{estilo}"' if estilo else ""
        return f'<div class="panel"{est}><h3>{titulo}</h3>{sub_html}{corpo}</div>'

    def leitura(texto: str) -> str:
        return f'<div class="read"><b>Leitura nossa.</b> {texto}</div>'

    def ct(*citacoes: str) -> str:
        return '<div class="ct">' + " ".join(f"[{c}]" for c in citacoes) + "</div>"

    def lista(itens: list[str]) -> str:
        return '<ul class="l">' + "".join(f"<li>{i}</li>" for i in itens) + "</ul>"

    def fato(numero: str, texto: str, rotulo: bool = False) -> str:
        return f'<div class="fato{" k" if rotulo else ""}"><span class="n">{numero}</span><span>{texto}</span></div>'

    def faixa(itens: list[tuple], colunas: int = 4) -> str:
        classe = "f4 c3" if colunas == 3 else "f4"
        celulas = "".join(
            f'<div class="i">{ic(icone) if icone else ""}' + (f'<div class="n">{n}</div>' if n else "") + f'<div class="t">{texto}</div></div>'
            for icone, n, texto in itens)
        return f'<div class="{classe}">{celulas}</div>'

    def caso(icone: str, nome: str, oque: str, selo: str, etapas: list[tuple], atencao: bool = False) -> str:
        """Etapas: (rótulo, ícone, número ou frase, é frase?, texto, citações, classe)."""
        rotulos = "".join(
            ("" if k == 0 else '<div class="sx">→</div>')
            + f'<div class="et {classe}"><div class="rt"><b>{k + 1}</b>{rotulo}</div>{ic(icone_e)}'
            + f'<div class="n{" s" if frase else ""}">{numero}</div><p>{texto}</p>{ct(*cits)}</div>'
            for k, (rotulo, icone_e, numero, frase, texto, cits, classe) in enumerate(etapas))
        return (f'<div class="cz">{ic(icone, "ic big")}<div><div class="nm">{nome}</div><div class="oq">{oque}</div></div>'
                f'<span class="tg{" at" if atencao else ""}">{selo}</span></div><div class="fluxo">{rotulos}</div>')

    def s(parte: str, olho: str, titulo: str, corpo: str, fts: str = "", msg: str = "", zoom: float = 1.0) -> dict:
        return {"parte": parte, "olho": olho, "titulo": titulo, "corpo": corpo, "fontes": fts, "msg": msg, "zoom": zoom}

    # ------------------------------------------------------------------------------------------
    # Resumo
    # ------------------------------------------------------------------------------------------
    def numero(icone, k, n, titulo, texto, *cits):
        return (f'<div class="c"><div class="top">{ic(icone)}<span class="k">{k}</span></div><div class="n">{n}</div>'
                f'<h3>{titulo}</h3><p>{texto}</p>{ct(*cits)}</div>')

    resumo = s(
        "Resumo", "O estudo em uma página", "O benchmark em seis números",
        '<div class="x6">'
        + numero("database", "A base vem antes", "<span>2015</span>", "O alicerce veio anos antes da IA generativa",
                 "A São Martinho trabalha a conectividade no campo desde 2015; o Itaú está na nuvem desde 2017.", "M1222, p. 27", "M1238, p. 2")
        + numero("shield-check", "Governança", "3 de 4", "A governança de IA é a dimensão mais atrasada",
                 "Três das quatro empresas do painel estão no estágio 2 em governança; dados e aplicações chegam ao 3 e ao 4.",
                 "M784, p. 1-3", "M336, p. 22, 39", "M397, p. 25, 27", "M876, p. 5")
        + numero("ban", "IA generativa", "67% × 33%", "Proibir funciona pouco",
                 "O envio de dado sensível a IA pública é mais comum onde a IA é proibida (67%) do que onde não há política (33%).", "M110, p. 73, 77")
        + numero("flame", "IA preditiva", "−61%", "O valor medido está na dor medida",
                 "Incêndios em áreas de plantio da Suzano, 2024 contra 2023, com torres com IA e esforços integrados.", "M335, p. 69")
        + numero("hourglass", "Retorno", "2 a 4 anos", "O retorno demora e se concentra",
                 "É o prazo de um caso típico de IA até dar retorno; 20% das empresas ficam com 74% do retorno.", "M064, p. 1-3", "M080, p. 3")
        + numero("tractor", "Campo", "1 : 8", "Autonomia em nichos, com supervisão",
                 "Um operador supervisiona até oito pulverizadores autônomos em pomares; não achamos autonomia plena em operação regular.",
                 "M1284, p. 1")
        + "</div>",
        fontes(("M1222", "p. 27"), ("M1238", "p. 2"), ("M784", "p. 1-3"), ("M336", "p. 22, 39"), ("M397", "p. 25, 27"), ("M876", "p. 5"),
               ("M110", "p. 73, 77"), ("M335", "p. 69"), ("M064", "p. 1-3"), ("M080", "p. 3"), ("M1284", "p. 1")))

    # ------------------------------------------------------------------------------------------
    # Frente 1 · Onde o mercado está
    # ------------------------------------------------------------------------------------------
    def calor() -> str:
        cab = ["", "Governança", "Dados", "Pessoas", "Aplicações", "Geral"]
        linhas = [("Bayer", "Crop Science", [3, 4, 4, 4], 4), ("Suzano", "", [2, 3, 3, 3], 3),
                  ("Deere", "", [2, 4, 3, 4], 3), ("DJI", "Agriculture", [2, 3, None, 3], 2)]
        h = '<div class="hm">' + "".join(f'<div class="h">{c}</div>' for c in cab)
        for nome, sub, notas, geral in linhas:
            h += f'<div class="e">{nome}' + (f"<small>{sub}</small>" if sub else "") + "</div>"
            for n in notas:
                h += f'<div class="c n{n}">{n}</div>' if n else '<div class="c n0">sem evidência</div>'
            h += f'<div class="c n{geral} g">{geral}</div>'
        return h + "</div>"

    regua = s(
        F1, "Painel de empresas na régua de maturidade", "No painel, ninguém chega ao estágio 5; a governança de IA é o degrau mais baixo",
        '<div class="g2" style="grid-template-columns:1.52fr 1fr;margin-top:12px">'
        + painel("A régua de cinco estágios e o estágio geral de cada empresa",
                 "Só com evidência pública; o geral é o maior estágio atingido em ao menos três das quatro dimensões", g.escada(665, 318))
        + painel("O estágio por dimensão", "De 1 a 5; quanto mais claro o verde, mais alto",
                 calor()
                 + fato("≈95%", "dos empregados da Bayer fizeram o treinamento obrigatório de IA responsável; é a única do painel com princípios próprios de IA publicados.")
                 + fato("≈ US$ 2,6 bi", "de valor de soluções de IA em 2025, pela métrica da própria Saudi Aramco: a referência do estágio 5 é quem divulga o retorno."))
        + "</div>"
        + leitura("Dados e aplicações estão à frente; a governança de IA, atrás. O que separa o 2 do 3 em governança é uma regra própria de IA, publicada."),
        fontes(("M789", "p. 11, 30"), ("M335", "p. 69, 101"), ("M867", "p. 10"), ("M845", "p. 1"), ("M784", "p. 1-3"), ("M783", "p. 110"),
               ("M494", "p. 67"), ("M441", "p. 59")))

    setores = s(
        F1, "O agro e os outros setores", "Bancos e energia lideram em IA; o agro chegou à média digital, não em IA",
        '<div class="g2" style="grid-template-columns:1.25fr 1fr;margin-top:12px">'
        + painel("Inteligência artificial, por setor", "ITDBr 2025 (PwC e Fundação Dom Cabral), dimensão de IA, escala de 1 a 6",
                 g.barras_h([("Serviços financeiros", 4.8, "4,8", "azul"), ("Energia", 4.2, "4,2", "azul"),
                             ("Consultoria e serviços", 4.1, "4,1", "cinza"), ("Tecnologia da informação", 3.8, "3,8", "cinza"),
                             ("Média das indústrias", 3.7, "3,7", "ambar", True), ("Saúde", 3.6, "3,6", "cinza"),
                             ("Varejo e consumo", 3.5, "3,5", "cinza"), ("Agronegócio", 3.4, "3,4", "verde", True),
                             ("Produção industrial", 3.2, "3,2", "cinza")], minimo=1, maximo=6, largura=600, rotulo_w=178, passo=24, alt=14, valor_w=52))
        + painel("O agro contra a média", "ITDBr: índice geral em 2024 e 2025 e dimensão de IA em 2025 (escala de 1 a 6)",
                 g.colunas([("agro|2024", 3.1, "3,1", "verde"), ("média|2024", 3.7, "3,7", "cinza"), ("agro|2025", 3.6, "3,6", "verde"),
                            ("média|2025", 3.6, "3,6", "cinza"), ("agro|IA 2025", 3.4, "3,4", "verde"), ("média|IA 2025", 3.7, "3,7", "cinza")],
                           largura=470, altura=158, minimo=1, maximo=6, larg_col=40)
                 + '<div class="lado" style="margin-top:4px">' + g.rosca(17, "17%", "cinza", 76, 11) + g.rosca(50, "50%", "verde", 76, 11)
                 + '<div class="cap"><b>17%</b> das empresas brasileiras com 10 ou mais pessoas usam IA; entre as grandes, <b>50%</b> (Cetic.br, 2025).</div></div>')
        + "</div>"
        + faixa([("message-circle", "≈90%", "de resolução da IA generativa na assistente do <b>Bradesco</b>, em 2025"),
                 ("banknote", "R$ 1 bi+", "de lucro líquido a mais com IA no crédito, diz o <b>Bradesco</b>"),
                 ("cpu", "40%", "do código escrito no <b>Santander</b> em jun/2026 veio de IA"),
                 ("users", "15 mi+", "de usuários por mês no assistente com IA do <b>Nubank</b>, em teste")]),
        fontes(("M082", "p. 8, 20"), ("M081", "p. 12-13"), ("M1201", "p. 11"), ("M1205", "p. 1"), ("M429", "p. 2"),
               ("M430", "p. 7, 9, 11, 23-24"), ("M414", "p. 43"), ("M416", "p. 2-3"), ("M447", "p. 3")))

    caso_suzano = s(
        F1, "Caso 1 · IA preditiva no campo · problema, iniciativa, resultado, consequência e lição",
        "Suzano: torres com IA contra incêndio, com uma pessoa confirmando cada alerta",
        caso("flame", "Suzano", "Florestal · proteção do plantio contra incêndios · 2024 a 2026", "resultado positivo", [
            ("Problema", "flame", "Incêndio em área de plantio", True,
             "Risco direto ao ativo de uma cultura perene: dor clara, operação 24 horas e métrica de resposta.", ("M335, p. 69",), ""),
            ("Iniciativa", "cctv", "133 torres", False,
             "com câmeras e IA que reconhecem a fumaça, acompanhadas 24 horas (dez/2024); satélites e drones complementam.",
             ("M335, p. 69", "M769, p. 2-3"), ""),
            ("Resultado", "trending-down", "−61%", False,
             "de incêndios em áreas de plantio em 2024, contra 2023. A empresa credita o número a esforços integrados, não só à IA.",
             ("M335, p. 69",), "res"),
            ("Consequência", "shield-check", "85%", False,
             "dos focos controlados antes de virar ocorrência de maior impacto, nos três anos até ago/2026 (toda a estrutura de prevenção e combate).",
             ("M753, p. 3",), ""),
            ("Lição", "lightbulb", "Começar pelo risco ao ativo", True,
             "Um operador confirma cada alerta antes de mandar a brigada: a tecnologia encurta o tempo, a decisão segue humana.",
             ("M769, p. 3", "M753, p. 4"), "")])
        + faixa([("siren", "27,6%", "menos tempo de chegada da frota de combate na <b>Raízen</b>, com IA e satélite, segundo a empresa"),
                 ("clipboard-check", "", "<b>Como ler.</b> Os números são das próprias empresas. Na Suzano, o resultado é do sistema inteiro: torres, drones, brigadas, frota e centrais de despacho."),
                 ("sprout", "", "<b>Por que importa.</b> É o caso mais maduro da ficha: protege o ativo de uma cultura perene, com métrica de resposta.")], 3),
        fontes(("M335", "p. 69"), ("M769", "p. 2-3"), ("M753", "p. 2-4"), ("M329", "p. 20")))

    caso_seletiva = s(
        F1, "Caso 2 · IA embarcada na máquina · problema, iniciativa, resultado, consequência e lição",
        "Pulverização seletiva: a máquina decide planta a planta; a regra continua humana",
        caso("spray-can", "Pulverização seletiva", "Grãos · ensaios de universidades dos EUA, medidos por terceiro · divulgados em 2024 e 2025", "resultado positivo, com risco", [
            ("Problema", "sprout", "Herbicida em área total", True,
             "A barra aplica na lavoura inteira, haja ou não planta daninha no alvo.", ("M1286, p. 1-2",), ""),
            ("Iniciativa", "scan-eye", "Câmeras e IA na barra", True,
             "A máquina decide planta a planta, em tempo real, dentro de uma regra definida por pessoas: a sensibilidade.",
             ("M1286, p. 1-2", "M1296, p. 2-3"), ""),
            ("Resultado", "trending-down", "−76%", False,
             "de herbicida, em média, em 5 lavouras de soja (de 43,9% a 90,6%), cerca de US$ 15,7 por acre (Iowa State, 2024).",
             ("M1286, p. 1-2",), "res"),
            ("Consequência", "triangle-alert", "+280%", False,
             "ao ano de caruru no ensaio de 3 anos do Arkansas, na sensibilidade mais baixa; lá, a economia foi de 43% a 59%.",
             ("M1296, p. 2-3",), "neg"),
            ("Lição", "lightbulb", "A máquina decide, a pessoa calibra", True,
             "A economia depende da pressão de daninhas e da regra. Economizar demais hoje pode custar o controle amanhã.",
             ("M1286, p. 1-2", "M1296, p. 2-3"), "")], atencao=True)
        + faixa([("sparkles", "26%", "dos produtores da <b>América Latina</b> usam IA generativa (McKinsey, abr–jul/2026)"),
                 ("globe", "17%", "é a parcela em <b>10 países</b>; no Brasil, nenhuma pesquisa publica o uso de IA só pelo produtor"),
                 ("bot", "5%", "usam <b>automação e robótica</b>, em 7 países: a adoção medida ainda é baixa")], 3),
        fontes(("M1286", "p. 1-2"), ("M1296", "p. 2-3"), ("M021", "p. 8, 24, 26")))

    caso_uber = s(
        F1, "Caso 3 · IA generativa e custo · problema, iniciativa, resultado, consequência e lição",
        "Uber: o orçamento de IA acabou em quatro meses; o controle veio pelo consumo",
        caso("coins", "Uber", "Tecnologia · programação com agentes de IA · 2024 a 2026", "insucesso corrigido", [
            ("Problema", "trending-up", "≈ 4 meses", False,
             "foi quanto durou o orçamento de IA de 2026 (abr/2026). Os custos tinham crescido 6 vezes desde 2024.",
             ("M986, p. 2", "M941, p. 3", "M989, p. 3"), "neg"),
            ("Iniciativa", "gauge", "US$ 1.500", False,
             "de teto por mês, por funcionário e por ferramenta (jun/2026); depois, faixa única de gasto, com alertas (ago/2026).",
             ("M986, p. 2", "M995, p. 15"), ""),
            ("Resultado", "trending-down", "−52%", False,
             "no custo por sessão, contra o pico de jun/2026, com o mesmo modelo.", ("M995, p. 2, 15",), "res"),
            ("Consequência", "users", "7×", False,
             "mais usuários semanais de agentes entre fev e ago/2026, e 9,4 vezes mais requisições.", ("M995, p. 2",), ""),
            ("Lição", "lightbulb", "Medir resultado, não volume", True,
             "O ranking interno premiava o uso. A empresa mapeou 16 tipos de desperdício, como usar o modelo mais caro em tarefa simples.",
             ("M995, p. 15", "M941, p. 3"), "")], atencao=True)
        + '<div class="box g" style="margin-top:10px"><b>O mesmo roteiro em outra empresa.</b> Na Accenture, com o uso de IA monitorado (fev/2026), funcionários inflaram o consumo; '
          'em out/2026, a empresa passou a custear até US$ 29 por pessoa por mês, e o excedente vai para o projeto. A Accenture contesta a leitura de limite firme. '
          '<span class="ct">Números da Uber declarados por ela; o estouro do orçamento vem da imprensa.</span></div>',
        fontes(("M989", "p. 3"), ("M986", "p. 2"), ("M941", "p. 3"), ("M995", "p. 2, 15"), ("M1195", "p. 1-2"), ("M1196", "p. 2-3"),
               ("M1194", "p. 1"), ("M1197", "p. 1-2"), ("M1198", "p. 2-3")))

    # Caso iFood: números declarados pelo CEO no LinkedIn (M1382). O gráfico é redesenhado: só os dois
    # rótulos finais são publicados; os pontos intermediários foram lidos no gráfico da publicação.
    tokens_ifood = [(0, 7), (1, 9), (2, 12), (3, 13), (3.6, 22), (4, 45), (4.5, 80), (5, 113), (6, 150), (7, 172), (8, 190), (8.85, 206)]
    custo_ifood = [(0, 11), (1, 13), (2, 17), (3, 20), (3.6, 45), (4, 85), (4.35, 105), (5, 100), (6, 101), (6.5, 85), (7, 62), (8, 54), (8.85, 49)]

    def etapa(n, rotulo, texto, classe=""):
        return f'<div class="r {classe}"><div class="bd">{n}</div><div><div class="rt">{rotulo}</div><p>{texto}</p></div></div>'

    caso_ifood = s(
        F1, "Caso 4 · IA generativa e custo · problema, iniciativa, resultado, consequência e lição",
        "iFood: o uso de IA dobrou e a conta caiu pela metade, sem limitar o acesso",
        '<div class="g2" style="grid-template-columns:1.25fr 1fr;margin-top:12px">'
        + painel("A \"boca de jacaré\": os tokens sobem, o custo cai", "Índices sem base informada; curvas redesenhadas a partir do gráfico da publicação, com valores intermediários aproximados",
                 g.duas_linhas(tokens_ifood, custo_ifood, ["fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out"],
                               [(3.6, "Bootcamp de IA", ""), (6, "Plataforma própria:", "modelos abertos como padrão")],
                               ("+106%", "tokens, desde junho"), ("−51%", "custo, desde junho"))
                 + '<div class="lg"><span style="--c:#62A842">tokens consumidos</span><span style="--c:#B88A28">custo</span>'
                   '<span class="sd">De janeiro a abril: primeiros usuários.</span></div>')
        + '<div class="fv">'
        + etapa(1, "Problema", "<b>IA agêntica para todos</b> os colaboradores: no começo, o uso cresceu e a conta também.")
        + etapa(2, "Iniciativa", "<b>\"Nossa resposta não foi limitar o acesso\",</b> diz o CEO. Modelos abertos viraram o padrão numa plataforma própria; os premium ficaram para as tarefas que os justificam, com orçamento definido.")
        + etapa(3, "Resultado", "<b>Tokens 106% maiores e conta 51% menor</b> desde junho de 2026.", "res")
        + etapa(4, "Consequência", "<b>8 em cada 10 tokens</b> rodam em modelos abertos, e todos seguem com tokens ilimitados.")
        + etapa(5, "Lição", "<b>O modelo do tamanho da tarefa:</b> a conta cai quando o modelo mais caro deixa de ser o padrão (leitura nossa).")
        + "</div></div>"
        + faixa([("trending-up", "30×", "mais <b>uso de IA</b> desde janeiro de 2026"),
                 ("users", "7×", "mais uso <b>por pessoa</b> desde janeiro"),
                 ("coins", "−86%", "no <b>custo por token</b> desde janeiro"),
                 ("clipboard-check", "", "<b>Como ler.</b> Números declarados pelo CEO numa rede social, sem valores em moeda e sem verificação de terceiros.")]),
        fontes(("M1382", "web")))

    valor = s(
        F1, "Valor e retorno da IA", "O valor medido vem da IA preditiva; o retorno demora e se concentra",
        '<div class="g3" style="margin-top:12px">'
        + painel("O retorno ainda é baixo", "Função financeira, mais de 280 executivos, mar/2025 (BCG)",
                 '<div class="lado">' + g.colunas([("ROI mediano|informado", 10, "10%", "ambar"), ("meta de muitos|executivos", 20, "20%", "cinza")],
                                                  largura=210, altura=150, maximo=24, larg_col=48)
                 + g.rosca(45, "45%", "verde", 104, 14, "medem") + "</div>"
                 + '<div class="cap"><b>45%</b> conseguem medir o retorno da IA; os demais não conseguem quantificá-lo.</div>')
        + painel("Demora", "1.854 executivos na Europa e no Oriente Médio (Deloitte)",
                 g.faixas_tempo([("Investimento típico em tecnologia", 7 / 12, 1.0, "7 a 12 meses", "cinza"),
                                 ("Caso típico de IA até dar retorno", 2, 4, "2 a 4 anos", "ambar")], largura=350, altura=150)
                 + '<div class="cap"><b>85%</b> aumentaram o investimento em IA mesmo assim.</div>')
        + painel("Se concentra", "1.217 empresas (PwC)", g.concentracao(350, 150)
                 + '<div class="cap">Uma em cada cinco empresas fica com quase três quartos do retorno.</div>')
        + "</div>"
        + '<div class="pipe" style="margin-top:10px">'
          f'<div class="p">{ic("users")}<div class="k">Pessoas</div><p>que conhecem o processo</p></div><div class="ar">→</div>'
          f'<div class="p">{ic("sparkles")}<div class="k">IA generativa</div><p>código, preparo de dados, documentação e testes</p></div><div class="ar">→</div>'
          f'<div class="p">{ic("chart-line")}<div class="k">Modelos preditivos</div><p>e de otimização: safra, falha, processo</p></div><div class="ar">→</div>'
          f'<div class="p">{ic("target")}<div class="k">Valor medido</div><p>contra a linha de base</p></div></div>'
        + leitura("A IA preditiva gera o valor medido; a generativa acelera quem a constrói e se mede primeiro em tempo."),
        fontes(("M1193", "p. 2-3"), ("M064", "p. 1-3"), ("M080", "p. 3"), ("M494", "p. 67"), ("M441", "p. 59, 64")))

    # ------------------------------------------------------------------------------------------
    # Frente 2 · Como o mercado chegou lá
    # ------------------------------------------------------------------------------------------
    fases = [
        (1, "Alicerce de dados e de campo", "anos antes", "", "Dados e nuvem; no agro, conectividade no campo e centro de operações.", [
            ("São Martinho", "2015", "início da conectividade no campo"),
            ("Itaú", "2017", "na nuvem desde então; 65% dos aplicativos em dez/2024"),
            ("Atvos", "375 mil ha", "com 4G próprio, em oito usinas (2025)")]),
        (2, "Estrutura dedicada", "antes da escala", "", "Um centro, área ou grupo responsável pela IA.", [
            ("Vale", "2019", "centro de IA aberto"),
            ("Itaú", "≈ 500", "cientistas de dados"),
            ("Klabin", "IA Office", "grupo que avalia e direciona o uso de IA")]),
        (3, "IA preditiva em dores medidas", "primeiro valor", "", "Incêndio, insumos, manutenção e logística, com resultado medido.", [
            ("Vale", "US$ 20 mi", "de economia já quando o centro foi criado"),
            ("Atvos", "R$ 5,8 mi", "na 1ª fase do centro de inteligência agrícola"),
            ("bp bioenergy", "−50%", "de incêndios e −77% de área queimada (2019–2025)")]),
        (4, "IA generativa: da proibição ao assistente", "2023–2024", "", "Restrição depois dos primeiros vazamentos; depois, assistente para todos.", [
            ("Samsung", "2023", "proíbe depois de um vazamento de código"),
            ("Petrobras", "110 mil", "com acesso em dez/2023; eram 500 em jul/2023"),
            ("Suzano", "≈ 50 mil", "colaboradores com assistente (1º sem. de 2024)")]),
        (5, "Governança e democratização", "2024–2026", "", "Política com treinamento, triagem de demandas e várias ferramentas sob a mesma regra.", [
            ("São Martinho", "99%", "do público elegível treinado na política de uso de IA"),
            ("Klabin", "300+ → 18", "demandas de IA avaliadas e selecionadas (2025)"),
            ("Vale", "19 áreas", "com acesso à plataforma de dados e IA")]),
        (6, "Agentes com cautela", "2025 em diante", "cau", "Plataformas de agentes com limites de autonomia.", [
            ("BCG", "5%", "têm os controles completos para dar autonomia a agentes"),
            ("Gartner, previsão", "40%", "vão rebaixar ou desativar agentes autônomos até 2027"),
            ("Petrobras", "", "plataforma de agentes, com a ressalva de que falta maturidade para missão crítica")]),
    ]

    def chip(emp, v, txt):
        valor = f'<span class="v">{v}</span>' if v else ""
        return f'<div class="cs"><b>{emp}</b>{valor}<span>{txt}</span></div>'

    trajetoria = s(
        F2, "Roteiro de adoção · o caminho", "O caminho que se repete: seis fases, em ordem parecida",
        '<div class="f6">' + "".join(
            f'<div class="fz {classe}"><div class="no">{n}</div><div class="qd">{quando}</div><h3>{titulo}</h3><div class="oq">{oque}</div>'
            + "".join(chip(*c) for c in casos) + "</div>"
            for n, titulo, quando, classe, oque, casos in fases) + "</div>"
        + leitura("O alicerce é a etapa mais longa e vem antes do valor; o valor aparece na passagem do piloto à produção. As datas não são obrigatórias nem simultâneas."),
        fontes(("M1222", "p. 27"), ("M1238", "p. 2"), ("M1224", "p. 1-2"), ("M1251", "p. 1"), ("M1239", "p. 2"), ("M326", "p. 63, 65"),
               ("M1219", "p. 2"), ("M1217", "p. 1"), ("M1013", "p. 1-2"), ("M1245", "p. 2"), ("M1240", "p. 1"), ("M334", "p. 6"),
               ("M357", "p. 46"), ("M1247", "p. 2"), ("M1199", "p. 10"), ("M1202", "p. 1"), ("M1246", "p. 2")))

    ritmo = s(
        F2, "Roteiro de adoção · o ritmo", "A base leva anos; a IA generativa foi do piloto à empresa toda em meses",
        painel("Quanto tempo cada etapa levou", "Datas das fontes; durações: cálculo nosso",
               g.gantt([
                   ("São Martinho · rede no campo", "início em 2015; plano de 4G em todas as usinas até 2020", 2015, 2020, "≈ 5 anos", "verde"),
                   ("Vale · caminhões autônomos", "testes desde 2016; os 13 caminhões de Brucutu em 2019", 2016, 2019, "≈ 3 anos", "verde"),
                   ("Itaú · migração para a nuvem", "desde 2017; 65% dos aplicativos em dez/2024; conclusão prevista para 2028", 2017, 2024.95, "7 anos, 65%", "azul"),
                   ("Vale · do centro de IA ao portfólio", "centro em 2019; abordagem estruturada e escalável em 2025", 2019, 2025, "≈ 6 anos", "azul"),
                   ("Petrobras · IA generativa para todos", "de 500 pessoas (jul/2023) a 110 mil com acesso (dez/2023)", 2023.5, 2023.95, "≈ 5 meses", "ambar")],
                   largura=1136, rotulo_w=372, dur_w=136, passo=40)
               + '<div class="lg"><span style="--c:#62A842">campo e operação</span><span style="--c:#3A8FBF">dados e estrutura</span><span style="--c:#B88A28">IA generativa</span></div>',
               "margin-top:12px")
        + '<div class="colt" style="margin-top:10px;margin-bottom:0;color:var(--warning)">Armadilhas relatadas</div>'
        + '<div class="ar4" style="margin-top:4px">'
          '<div class="a"><b>O dado custa mais que a técnica</b>O mais caro é obter os dados, não aplicar a IA (head de IA da Vale).</div>'
          '<div class="a"><b>A TI vira gargalo</b>Na Vale, pedidos de dados podiam levar até três semanas antes da plataforma aberta às áreas.</div>'
          '<div class="a"><b>Rede própria pede operação contínua</b>A São Martinho vai migrar para a rede de uma operadora.</div>'
          '<div class="a"><b>Licença não é uso</b>Num ministério britânico, cerca de 30% dos licenciados usaram por dia útil.</div></div>',
        fontes(("M1222", "p. 27-28"), ("M1242", "p. 4"), ("M1238", "p. 2"), ("M1251", "p. 1"), ("M496", "p. 32"), ("M1245", "p. 2"),
               ("M1240", "p. 1"), ("M1241", "p. 4"), ("M1247", "p. 3"), ("M1218", "p. 1-2"), ("M1011", "p. 16")))

    # Checkpoints principais: dois por célula, tirados das tabelas da seção 4.2 da nota do roteiro
    # (e da 4.4, na linha de IA generativa e agentes). O estágio 1 é o ponto de partida.
    dimensoes = [
        ("shield-check", "Estratégia e governança", "sem patrocínio, regra ou instância de IA", "", [
            ["<b>Patrocinador executivo</b> nomeado", "Diretriz escrita de uso e de dados"],
            ["<b>Comitê ou área</b> com mandato", "<b>Política de uso,</b> com % de treinados", "Canal oficial de IA para todos"],
            ["Governança integrada a riscos e compliance", "Casos geridos <b>como portfólio</b>"],
            ["Regras aplicadas por tecnologia", "Agentes com limites de ação e auditoria"]]),
        ("database", "Dados e infraestrutura", "dados em planilhas e sistemas isolados", "", [
            ["Dados dos pilotos, com responsável", "Ambiente de experimentação separado"],
            ["<b>Plataforma de dados unificada</b>", "<b>Conectividade</b> nas áreas prioritárias do campo"],
            ["<b>Dados como produto,</b> com dono", "Dados de campo quase em tempo real"],
            ["Dados prontos para agentes, com trilha de auditoria", "Operação contínua, com redundância"]]),
        ("users", "Organização e pessoas", "iniciativas dependem de entusiastas", "", [
            ["Núcleo técnico conduz os pilotos", "<b>Letramento básico</b> para quem usa"],
            ["Área de dados e IA com <b>liderança nomeada</b>", "<b>Champions</b> nomeados nas áreas"],
            ["Centro de excelência ou modelo federado", "Letramento como <b>condição de acesso</b>"],
            ["Organização redesenhada em torno da IA", "Supervisão de agentes e operação remota"]]),
        ("target", "Aplicações e valor", "usos pontuais, sem caso em produção", "", [
            ["Pilotos com <b>métrica, dono</b> e critério de parada", "Portfólio de pilotos registrado"],
            ["<b>Um caso em produção,</b> com resultado medido", "Caminho do piloto à produção"],
            ["<b>Portfólio em produção</b> em vários processos", "Custo gerido por caso"],
            ["Produtos ou serviços com IA", "<b>Retorno consolidado</b> divulgado"]]),
        ("sparkles", "IA generativa e agentes", "uso individual de assistentes públicos", "ia", [
            ["Assistentes corporativos com grupos-piloto"],
            ["Assistente em produção, sobre documentos da empresa"],
            ["Copilotos nos fluxos-chave; agentes agem com aprovação"],
            ["Agentes operam, com supervisão por exceção"]]),
    ]
    cabecalho_ck = ('<div class="hd e1"><b>1</b>Exploração · ponto de partida</div><div class="hd e2"><b>2</b>Pilotos</div>'
                    '<div class="hd e3"><b>3</b>Operação</div><div class="hd e4"><b>4</b>Escala</div><div class="hd e5"><b>5</b>Transformação</div>')
    linhas_ck = "".join(
        f'<div class="dm {classe}">{ic(icone)}<div><div class="k">{nome}</div><p>{partida}</p></div></div>'
        + "".join('<div class="c">' + "".join(f"<p>{c}</p>" for c in celula) + "</div>" for celula in celulas)
        for icone, nome, partida, classe, celulas in dimensoes)
    checkpoints = s(
        F2, "Roteiro de adoção · a régua com pré-requisitos · leitura nossa, a partir dos frameworks de maturidade", "Os checkpoints principais: o que precisa estar de pé em cada estágio",
        f'<div class="ck">{cabecalho_ck}{linhas_ck}</div>'
        + '<div class="rg"><span><b>Cumulativos:</b> cada estágio supõe os anteriores</span>'
          '<span><b>Do 3 em diante,</b> só conta uso em produção ou em escala</span>'
          '<span><b>Estágio geral:</b> o mais alto em três das quatro dimensões</span>'
          '<span><b>Autoavaliação:</b> página Roteiro</span></div>',
        fontes(("M194", "p. 6, 10, 35"), ("M189", "p. 4"), ("M159", "p. 10"), ("M1209", "p. 1"), ("M1202", "p. 1-2"), compacta=True))

    def indice(pct, cor, texto):
        rotulo = f"{pct:g}%".replace(".", ",")
        return f'<div class="ix">{g.rosca(pct, rotulo, cor, 54, 8)}<p>{texto}</p></div>'

    def degrau(st, nomes, itens):
        return (f'<div class="sa"><div class="st">{st}</div><div class="nm">{nomes}</div>'
                f'<div class="ixs">{"".join(indice(*i) for i in itens)}</div></div>')

    indices = s(
        F2, "Roteiro de adoção · índices do mercado", "Índices do mercado: onde as empresas estão em cada degrau da régua",
        '<div class="saltos">'
        + degrau("1 → 2", "Exploração → Pilotos", [
            (17, "verde", "<b>das empresas brasileiras</b> com 10 ou mais pessoas usam IA; entre as grandes, 50% (Cetic.br, 2025)"),
            (78, "verde", "<b>têm IA na agenda de 2026,</b> entre 84 respondentes do agro; autodeclarado (Gatua)"),
            (56, "ambar", "<b>dos empregados já usaram IA no trabalho</b> sem saber se era permitido (KPMG)")])
        + degrau("2 → 3", "Pilotos → Operação", [
            (48, "verde", "<b>dos projetos de IA chegam à produção,</b> em média em 8 meses (Gartner)"),
            (63, "ambar", "<b>não têm, ou não sabem se têm,</b> práticas de dados adequadas para IA (Gartner)"),
            (49, "ambar", "<b>apontam a dificuldade de demonstrar valor</b> como a principal barreira (Gartner)")])
        + degrau("3 → 4", "Operação → Escala", [
            (81, "verde", "<b>das iniciativas têm retorno positivo</b> entre quem rastreia o retorno e trata a IA como portfólio (Gartner)"),
            (91, "verde", "<b>das organizações de alta maturidade</b> nomearam líderes dedicados de IA (Gartner)"),
            (12, "verde", "<b>avaliam de forma consistente</b> o valor contra o custo (KPMG)")])
        + degrau("4 → 5", "Escala → Transformação", [
            (5, "verde", "<b>têm os controles completos</b> para dar autonomia a agentes (BCG)"),
            (23, "verde", "<b>escalam um sistema agêntico</b> em alguma área; outros 39% experimentam (McKinsey)"),
            (40, "ambar", "<b>vão rebaixar ou desativar agentes autônomos</b> até 2027, por falhas de governança (previsão do Gartner)")])
        + "</div>"
        + '<div class="lg"><span style="--c:#62A842">parcela que já faz</span><span style="--c:#B88A28">barreira, risco ou previsão</span>'
          '<span class="sd">Bases diferentes: os índices não se comparam entre si; a distribuição pelos degraus é leitura nossa.</span></div>'
        + faixa([("activity", "83%", "de <b>uso ativo</b> no pico, entre 20 mil servidores britânicos; ativo é quem usou nos 30 dias anteriores"),
                 ("timer", "26 min", "poupados <b>por dia,</b> em média, segundo os próprios usuários (governo britânico)"),
                 ("coins", "13 min", "por semana <b>pagam a licença</b> de um servidor de nível médio (Tesouro australiano)")], 3),
        fontes(("M1205", "p. 1"), ("M748", "p. 32"), ("M110", "p. 77"), ("M122", "web"), ("M124", "web"), ("M123", "web"), ("M121", "web"),
               ("M072", "p. 3"), ("M1199", "p. 10"), ("M027", "p. 6"), ("M1202", "p. 1"), ("M1021", "p. 7, 11"), ("M1012", "p. 33")))

    shadow = s(
        F2, "IA generativa · do uso por fora ao canal oficial", "Proibir funciona pouco; quando a empresa oferece o canal, a conta oficial cresce",
        '<div class="g2" style="margin-top:12px">'
        + painel("Envio de dado sensível a IA pública, pela política da empresa", "Comparação entre grupos (Univ. de Melbourne e KPMG, 2025); o da proibição reúne 6% dos empregados",
                 g.barras_h([("IA proibida", 67, "67%", "laranja", True), ("Com política de uso", 56, "56%", "ambar"),
                             ("Sem política", 33, "33%", "cinza")], largura=540, rotulo_w=168, passo=38, alt=22, valor_w=58)
                 + '<div class="cap" style="margin-top:10px">Por que acontece: <b>53%</b> usam a própria ferramenta por preferir escolher; <b>33%</b>, porque a TI não oferece o que precisam (Software AG, fornecedora).</div>')
        + painel("Usuários de IA generativa, por tipo de conta", "Netskope, medição de tráfego na clientela, em um ano",
                 g.inclinacao([("contas pessoais", 78, 47, "laranja"), ("contas da empresa", 25, 62, "verde")], "out/2024", "out/2025", 540, 186)
                 + '<div class="cap">As duas mudanças aconteceram juntas; a fonte não prova que uma causou a outra.</div>')
        + "</div>"
        + '<div class="cam3">'
          f'<div class="p">{ic("ban")}<div><div class="k">2023 · Proibir</div><p>A Samsung proibiu depois de um vazamento de código; 27% das organizações proibiram ao menos por um tempo (Cisco).</p></div></div><div class="sx">→</div>'
          f'<div class="p">{ic("shield")}<div><div class="k">Hoje · Bloquear o que é de risco</div><p>90% das organizações bloqueiam algum aplicativo de IA, em média 10 (clientela da Netskope).</p></div></div><div class="sx">→</div>'
          f'<div class="p on">{ic("badge-check")}<div><div class="k">Canal oficial</div><p>Conta da empresa, dado protegido no contrato, registro de uso e regra de dado clara e treinada (leitura nossa).</p></div></div></div>',
        fontes(("M110", "p. 73, 77"), ("M1062", "p. 2"), ("M1049", "p. 2-3, 10"), ("M1013", "p. 1-2"), ("M1008", "p. 22")))

    def no(icone, titulo, texto, classe=""):
        return f'<div class="nd {classe}">{ic(icone)}<div><h3>{titulo}</h3><p>{texto}</p></div></div>'

    papeis = s(
        F2, "Roteiro de adoção · quem faz o quê", "Quem faz o quê: patrocínio no topo, champions nas áreas",
        '<div class="g2" style="grid-template-columns:2.35fr 1fr;margin-top:12px">'
        + '<div class="pir">'
          f'<div class="cam c1">{no("crown", "Patrocínio executivo e conselho", "Define ambição, limites de risco e orçamento; cobra resultado.", "top")}</div>'
          '<div class="sep">↓</div>'
          '<div class="cam c3a">'
          + no("user-cog", "Líder de IA dedicado", "Estratégia, implementação e orçamento.")
          + no("users", "Comitê de IA", "Prioriza demandas e cuida da política.")
          + no("blocks", "Centro de excelência", "Plataforma, padrões e reúso.") + "</div>"
          '<div class="sep">↓</div>'
          '<div class="cam c3b">'
          + no("server", "TI e dono técnico", "Plataforma, identidade, dados, segurança e custo.")
          + no("graduation-cap", "RH e educação", "Letramento por perfil e gestão da mudança.")
          + no("scale", "Jurídico, privacidade, segurança e risco", "Política, contratos e incidentes.") + "</div>"
          '<div class="sep">↓</div>'
          '<div class="cam c2">'
          + no("flag", "Champions nas áreas", "Tiram dúvidas, registram casos, levam demandas e criam soluções.")
          + no("user-check", "Usuário", "Usa conforme a política, revisa o que a IA produz e responde pelo resultado.") + "</div></div>"
        + '<div class="ev3">'
          '<div class="e"><div class="n">93,2%</div><p>dos líderes de dados e IA apontam cultura e gestão da mudança como o maior impedimento.</p></div>'
          '<div class="e"><div class="n">2×</div><p>mais pilotos levados à produção em modelos centralizados ou hub-and-spoke (IBM, autodeclarado).</p></div>'
          '<div class="e"><div class="n">26%</div><p>das organizações tinham um Chief AI Officer, contra 11% em 2023 (IBM).</p></div></div>'
        + "</div>"
        + leitura("A supervisão da governança de IA pelo CEO está entre os atributos mais ligados ao resultado da IA generativa (McKinsey). A TI passa de barreira a habilitadora: provê plataforma, identidade, dados e segurança, e as áreas desenvolvem."),
        fontes(("M029", "p. 3"), ("M135", "p. 8, 16"), ("M116", "p. 13"), ("M033", "p. 4-5")))

    # ------------------------------------------------------------------------------------------
    # Frente 3 · Para onde vai
    # ------------------------------------------------------------------------------------------
    custo = s(
        F3, "Custo de uso da IA", "O preço do token despenca, mas cada tarefa consome mais, e a conta sobe",
        '<div class="g3" style="margin-top:12px">'
        + painel("O preço da mesma capacidade", "Modelo mais barato com o desempenho do GPT-3.5 (AI Index)",
                 '<div class="gn">280×<small>mais barato</small></div>'
                 '<div class="seta2"><div>US$ 20<small>nov/2022</small></div><div class="ar">→</div><div>US$ 0,07<small>out/2024 · por milhão de tokens</small></div></div>'
                 '<div class="cap" style="margin-top:12px">Nos modelos de ponta, que as empresas querem usar, o preço não cai igual.</div>')
        + painel("Tokens por tarefa, contra um chat", "Agentes: Anthropic, jun/2025 · *tokens por resposta, contra modelos sem raciocínio (Epoch AI, abr/2025)",
                 g.colunas([("Chat", 1, "1×", "cinza"), ("Agente", 4, "4×", "verde"), ("Com|raciocínio*", 8, "≈ 8×", "ambar"),
                            ("Vários|agentes", 15, "15×", "verde")], largura=350, altura=172, maximo=17, larg_col=50))
        + painel("O consumo dispara", "Tokens processados por mês, segundo o próprio Google",
                 '<div class="gn">7×<small>em um ano</small></div>'
                 '<div class="cap" style="margin-top:10px">Mais de <b>3,2 quatrilhões</b> de tokens por mês em mai/2026.</div>'
                 + fato("82%", "dos executivos dizem que a empresa se preocupa com o custo de tokens; só <b>64%</b> monitoram o consumo com limite de orçamento (EY, EUA, jul/2026)."))
        + "</div>"
        + leitura("Para o mesmo desempenho, o preço despencou; a conta sobe porque cada tarefa consome mais e há mais tarefas. Orçar em duas partes: fixa por pessoa e variável por uso, com custo e valor medidos por tarefa."),
        fontes(("M230", "p. 65"), ("M968", "p. 1"), ("M953", "p. 4-5"), ("M911", "p. 3"), ("M934", "p. 1"), ("M666", "web"), ("M070", "p. 1-2")))

    def tile(icone, a, n, p):
        return f'<div class="tl">{ic(icone)}<div class="a">{a}</div><div class="n">{n}</div><p>{p}</p></div>'

    autonomia = s(
        F3, "Sistemas autônomos · máquinas, robôs e drones", "A autonomia já é produto em nichos, com supervisão; quatro quebras no caminho",
        '<div class="g2" style="grid-template-columns:1fr 1.18fr;margin-top:12px">'
        + painel("Frotas declaradas pelos fabricantes", "Todos os números são das próprias empresas",
                 '<div class="tiles ic2" style="margin-top:8px">'
                 + tile("cherry", "Pomares e vinhedos (GUSS)", "250+", "pulverizadores autônomos; um operador supervisiona até oito")
                 + tile("citrus", "Citros (Arbus, Jacto)", "16 mil h", "em cerca de 60 mil ha antes de virar produto, em abr/2026")
                 + tile("bot", "Lavoura (Solix)", "≈ 150 + 100", "robôs nos EUA e no Brasil, segundo a Forbes")
                 + tile("tractor", "Preparo de solo (Deere)", "200 mil acres", "de preparo autônomo desde o início da oferta") + "</div>")
        + painel("Quebras e recuos, 2024 e 2025", "Empresas de robótica de campo",
                 g.eixo_marcos([(1.2, "laranja"), (14.5, "laranja"), (21.4, "laranja"), (22.7, "laranja")], 0, 24,
                               [(0, "jan/2024"), (12, "jan/2025"), (24, "dez/2025")], largura=600, altura=50)
                 + '<div class="q4">'
                   '<div class="q"><div class="d">fev/2024 · Reino Unido</div><div class="k">Small Robot Company</div><p>Liquidação; faltou capital antes da escala.</p></div>'
                   '<div class="q"><div class="d">mar/2025 · EUA</div><div class="k">FarmWise</div><p>Reestruturação e encerramento gradual, com a queda do capital de risco.</p></div>'
                   '<div class="q"><div class="d">out/2025 · França</div><div class="k">Naïo</div><p>Plano de cessão e, no dia seguinte, liquidação judicial.</p></div>'
                   '<div class="q"><div class="d">nov/2025 · EUA</div><div class="k">Monarch</div><p>Demissões e ação que alega autonomia aquém da vendida, sem decisão.</p></div></div>'
                 + '<div class="cap" style="margin-top:8px"><b>Nas quebras com causa declarada, o capital acabou antes da escala.</b></div>')
        + "</div>"
        + faixa([("eye", "1 : 8", "um operador para até <b>oito pulverizadores</b> autônomos: a supervisão segue humana, a distância"),
                 ("radio-tower", "33,9%", "da área agrícola brasileira tinha <b>4G ou 5G</b> em abr/2025"),
                 ("search", "0", "casos de <b>autonomia plena</b>, sem supervisão, em operação regular: não achamos nenhum (leitura nossa)")], 3),
        fontes(("M1284", "p. 1"), ("M325", "p. 2-3"), ("M253", "p. 7"), ("M868", "p. 14"), ("M1319", "p. 1"), ("M1320", "p. 2"), ("M1298", "p. 2"),
               ("M1301", "p. 1-2"), ("M1300", "p. 1"), ("M1303", "p. 10"), ("M1318", "p. 2-4"), ("M1214", "p. 1-2")))

    def perene(icone, nome, texto, classe=""):
        return f'<div class="r {classe}">{ic(icone)}<div class="k">{nome}</div><p>{texto}</p></div>'

    perenes = s(
        F3, "Culturas perenes e mão de obra", "Nas perenes, a falta de gente puxa a máquina; a colheita é o gargalo",
        '<div class="g2" style="grid-template-columns:1fr 1.12fr;margin-top:12px">'
        + '<div style="display:grid;gap:10px">'
        + painel("Hectares por trabalhador na colheita da palma", "Estudo citado pelo MPOB (Malásia)",
                 g.barras_h([("À mão", 21, "21 ha", "cinza"), ("Cortador motorizado", 35, "35 ha", "ambar"),
                             ("Colhedora de médio porte", 86, "86 ha", "verde", True)], largura=520, rotulo_w=186, passo=27, alt=15, valor_w=62)
                 + fato("60% · 50%", "da força de trabalho e do custo de produção da palma estão na colheita."))
        + painel("Brasil: a principal resposta à falta de mão de obra", "CNA/Cepea, 2026, agro em geral; amostra não informada",
                 g.barras_h([("Mecanização", 26, "26%", "verde", True), ("Automação ou tecnologias digitais", 8.7, "8,7%", "ambar")],
                            maximo=40, largura=520, rotulo_w=218, passo=27, alt=15, valor_w=58)
                 + fato("94,8%", "dos produtores relatam dificuldade para contratar."))
        + "</div>"
        + painel("Perene por perene", "O que já existe e o que falta",
                 '<div class="pr5">'
                 + perene("tree-palm", "Palma", "<b>Colheita sem solução integrada:</b> em 2026, o MPOB ainda a chama de \"lacuna-chave\".")
                 + perene("coffee", "Café", "<b>Acima de 101 ha, todos usam colhedora;</b> onde a colheita é manual, a mão de obra passa de 40% do custo.")
                 + perene("citrus", "Citros", "<b>Quem mecanizar a colheita \"terá de mudar o pomar\",</b> diz o Fundecitrus.")
                 + perene("trees", "Florestal", "<b>Mais da metade do manejo da silvicultura mecanizado</b> no fim de 2026, estima a Klabin, pela falta de mão de obra rural.")
                 + perene("sprout", "Macaúba", "<b>Cerca de 4.000 ha plantados, sem cultivar comercial;</b> colheita em grande parte à mão (pesquisa pública).", "on")
                 + "</div>")
        + "</div>"
        + leitura("A falta de gente é o motor declarado, mas a resposta é mais mecanização que IA. Na macaúba, antes da máquina vem a cultivar."),
        fontes(("M377", "p. 11-12"), ("M1234", "p. 1"), ("M1268", "p. 14"), ("M245", "p. 2"), ("M1288", "p. 5-6"), ("M1267", "p. 3, 5-7"),
               ("M1269", "p. 2-3"), ("M1282", "p. 2, 20"), ("M326", "p. 15"), ("M1256", "p. 8"), ("M239", "p. 24")))

    # Colheita da macaúba: mão de obra e risco de trabalho (dossiê robotica-colheita-A, verificado em 23/11/2026;
    # nota IA no campo, seção 7.4). Os números de risco são de açaí, coco e palma, não da macaúba.
    colheita = s(
        F3, "Colheita da macaúba · mão de obra e segurança do trabalho · hipótese checada",
        "Macaúba: a colheita depende de gente; o risco é descrito, mas não foi medido",
        '<div class="g2" style="grid-template-columns:1.22fr 1fr;margin-top:12px">'
        + painel("A altura do problema: até onde cada ferramenta alcança", "Em metros, segundo quem desenvolveu ou testou cada uma · faixa verde: estipe da macaúba adulta",
                 g.alcance([("Colhedor|vibratório|(macaúba)", None, 4, "4 m", "verde"),
                            ("Cortador|motorizado|(palma)", 4.5, 6, "6 m", "cinza"),
                            ("Vara com|foice,|tradicional", 8, 10, "8 a 10 m", "cinza"),
                            ("Robôs de|coqueiro,|em teste", 13.42, 15.2, "15,2 m", "ambar"),
                            ("Vara de|alumínio|(INPA)", None, 19.2, "19,2 m", "cinza"),
                            ("Robô do|açaí,|à venda", None, None, "?", "ambar")],
                           (15, 20, "Macaúba adulta", "estipe de 15 a 20 m, com espinhos"), altura=242)
                 + '<div class="cap"><b>No plantio, a planta é mais baixa:</b> média de até 7 m aos 7 anos, da base à folha mais nova, em experimento da Embrapa. '
                   'Nenhuma fonte mede a altura do cacho; a do robô do açaí não é informada.</div>')
        + '<div style="display:grid;gap:10px;align-content:start">'
        + painel("Como se colhe hoje", "Pesquisa pública; não achamos descrição dos plantios comerciais",
                 fato("Do chão", "a maior parte é apanhada no solo, após a queda natural.", True)
                 + fato("Com vara", "foice em vara corta o cacho, aparado em rede; <b>não há máquina no mercado</b> (UFV e UFLA).", True)
                 + fato("37,5 kg/h", "única estimativa do rendimento manual; sem medição nem custo."))
        + painel("O risco de trabalho na macaúba", "",
                 fato("Descrito", "risco constante de acidentes e exaustão, com espinhos, varas longas e animais peçonhentos (INPA, palmeiras em geral).", True)
                 + fato("Sem número", "nenhum acidente registrado nem estudo ergonômico achado.", True))
        + "</div></div>"
        + faixa([("", "90%", "<b>Açaí:</b> de 33 coletores, já caíram do açaizeiro (Pará)"),
                 ("", "35,5%", "<b>Coco:</b> de 220 escaladores, já caíram do coqueiro (Índia)"),
                 ("", "78–93%", "<b>Palma:</b> com distúrbio osteomuscular em 12 meses (três estudos)"),
                 ("search", "0", "<b>Macaúba:</b> nenhum número de acidente achado")])
        + leitura("Confirma-se a dependência de gente; o risco é descrito, sem número. Queda é dado de culturas colhidas por escalada; a macaúba se colhe do chão."),
        fontes(("M1395", "p. 8"), ("M1390", "web"), ("M1265", "p. 3, 5, 9"), ("M1418", "p. 9, 11-12"), ("M1422", "web"), ("M1417", "p. 13-15"), ("M1277", "p. 1"), ("M1256", "p. 6"), ("M1385", "p. 2"), ("M1383", "web"), ("M1388", "web"), ("M1400", "web"), ("M1410", "web"), ("M1407", "web"), ("M1411", "web")))

    # Robôs que sobem na palmeira: dossiê robotica-colheita-B, verificado em 23/11/2026 (nota IA no campo, seção 7.4).
    def estagio(icone, nome, texto, pontos, fim=False):
        f = " fim" if fim else ""
        celulas = "".join(f'<div class="pt{f}"><span class="{"on" if p else ""}"></span></div>' for p in pontos)
        return f'<div class="{f.strip()}">{ic(icone)}</div><div class="nm{f}"><b>{nome}</b><span>{texto}</span></div>{celulas}'

    robos = s(
        F3, "Robótica de colheita em palmeiras · robôs que sobem no estipe e cortam o cacho",
        "Robô escalador: à venda no açaí, em teste no coco, nada para a macaúba",
        '<div class="g2" style="grid-template-columns:1.2fr 1fr;margin-top:12px">'
        + painel("Em que estágio está, por palmeira", "O que achamos em fonte pública; ponto cheio = existe",
                 '<div class="mz"><div class="h"></div><div class="h"></div><div class="h">Protótipo</div><div class="h">Teste de campo em artigo</div>'
                 '<div class="h">À venda</div><div class="h">Ganho medido por terceiro</div>'
                 + estagio("grape", "Açaí", "Robô à venda, por controle remoto; outro em protótipo.", (1, 0, 1, 0))
                 + estagio("tree-palm", "Coco", "Subiram 15,2 m e 13,42 m em testes dos autores.", (1, 1, 0, 0))
                 + estagio("tree-palm", "Tâmara", "Artigo mede só a subida; outro sistema, só anúncio.", (1, 0, 0, 0))
                 + estagio("tree-palm", "Palma de óleo", "Subida ainda não confiável; montagem à mão.", (1, 0, 0, 0))
                 + estagio("sprout", "Macaúba", "Nenhum robô achado; estipe com espinhos.", (0, 0, 0, 0), True)
                 + "</div>")
        + painel("O caso público do açaí: AçaíBot", "Sobe, serra o cacho e o traz ao operador · caso público, não recomendação",
                 '<div class="tiles ic2" style="margin-top:8px">'
                 + tile("weight", "Peso, segundo a empresa", "8,5 kg", "na página do produto; 8 kg em notícia da própria empresa")
                 + tile("tag", "Preço na loja da empresa", "R$ 22,9 mil", "em 23/11/2026, na página do produto")
                 + tile("landmark", "Compra pública no Amapá", "44 robôs", "por R$ 1,01 milhão, em contratação direta (Diário Oficial, 08/05/2026)")
                 + tile("search", "Ensaio independente", "0", "achados; os ganhos declarados vão de \"até 180%\" a \"10 vezes\"") + "</div>"
                 + '<div class="cap" style="margin-top:8px"><b>E a IA?</b> A página do produto só fala em controle remoto. A notícia do prêmio de inovação da CNI '
                   'cita visão computacional e aprendizado de máquina; não achamos documento técnico.</div>')
        + "</div>"
        + faixa([("timer", "21,9 min", "<b>por coqueiro para o robô e 11,8 para o colhedor,</b> num teste dos autores (IEEE Spectrum)"),
                 ("triangle-alert", "5 travas", "<b>na palma:</b> andar no talhão, localizar-se, subir, cortar o cacho e ler a maturação"),
                 ("sprout", "434 kg/h", "<b>na macaúba, só um colhedor vibratório portátil,</b> medido pelos inventores")], 3)
        + leitura("O robô escalador saiu do laboratório no açaí, por controle remoto e sem ganho medido por terceiro. Na macaúba, o que tem medição vem do chão."),
        fontes(("M1400", "web"), ("M1401", "web"), ("M1399", "p. 1"), ("M1391", "web"), ("M1392", "p. 2, 5"), ("M1383", "web"), ("M1388", "web"), ("M1403", "web"), ("M1389", "web"), ("M1404", "web"), ("M1385", "p. 3, 8, 16"), ("M1386", "web"), ("M1256", "p. 6")))

    def mapa(a, n, p):
        return f'<div class="tl"><div class="a">{a}</div><div class="n">{n}</div><p>{p}</p></div>'

    satelites = s(
        F3, "Satélites e modelos de fundação · imagem e clima", "Satélite: mapear perenes já funciona; a IA do tempo opera ao lado da física",
        '<div class="g2" style="grid-template-columns:1.3fr 1fr;margin-top:12px">'
        + painel("Imagem: acerto dos mapas de culturas perenes", "Métricas diferentes em cada estudo; não se comparam entre si",
                 '<div class="tiles t3" style="margin-top:8px">'
                 + mapa("Palma · mapa global (2021)", "88% · 77%", "plantios industriais e de pequenos produtores; perde os plantios jovens")
                 + mapa("Cacau · Costa do Marfim e Gana (2023)", "91,7%", "na validação de campo às cegas; detecta plantios jovens")
                 + mapa("Seringueira · Sudeste Asiático (2023)", "0,95 → 0,57", "cai quando calculada sobre a área estimada")
                 + mapa("Café · mapas do Google (2026)", "71%", "sem revisão por pares; omite plantio sombreado em algumas regiões")
                 + mapa("Macaúba · drone (Embrapa, 2026)", "93% · 89%", "no teste da mesma área e numa área de 4,0 ha fora dela")
                 + mapa("Brasil · MapBiomas", "sem acurácia", "própria para café, citros e palma; só das classes agregadas")
                 + "</div>")
        + painel("Tempo: alvos em que a IA superou o modelo físico", "Segundo os autores; métricas globais; no GraphCast e no GenCast, a chuva ficou fora do placar",
                 g.barras_h([("GraphCast · 1.380 alvos", 90, "90%", "verde"), ("GenCast · 1.320 alvos", 97.2, "97,2%", "verde"),
                             ("Aurora · tempo global a 0,1°", 92, "92%", "verde")], largura=440, rotulo_w=192, passo=27, alt=15, valor_w=62)
                 + fato("Recordes", "De calor, frio e vento: o modelo físico venceu em quase todos os prazos (Science Advances, 2026).", True)
                 + fato("Operação", "No centro europeu desde 25/02/2025, ao lado do modelo físico; a NOAA anunciou três modelos em 17/12/2025.", True)
                 + fato("Brasil", "A única avaliação regional é um pré-print, sem chuva; o resultado depende da estação.", True))
        + "</div>"
        + leitura("Mapear a área de perenes por satélite já é viável; prever produtividade e saúde segue em pesquisa. Na previsão do tempo, a IA vence na média e perde nos recordes."),
        fontes(("M1376", "p. 1, 8"), ("M1377", "p. 3-4, 8"), ("M1379", "p. 1-2, 9-10"), ("M1327", "p. 27, 35"), ("M1381", "web"), ("M1336", "p. 1, 3, 7"),
               ("M1373", "p. 24"), ("M1338", "p. 1, 4"), ("M1337", "p. 1, 4"), ("M1344", "p. 1"), ("M1343", "p. 1-3"), ("M645", "p. 2-3"),
               ("M1350", "p. 1, 3"), ("M1352", "p. 13, 17, 19-22")))

    def item(icone, titulo, texto):
        return f'<div class="it">{ic(icone)}<div><div class="k">{titulo}</div><p>{texto}</p></div></div>'

    horizonte = s(
        F3, "O que isso indica para culturas perenes", "Para perenes: o que já é viável, o que é tendência e o que ainda é pesquisa",
        '<div class="hz">'
        + f'<div class="col v"><div class="cb">{ic("circle-check")}<h3>Já viável</h3><span class="sb">em operação</span></div>'
        + item("map", "Mapear a área plantada", "Imagem aberta de 10 m e validação de campo: palma, cacau e seringueira.")
        + item("cctv", "Vigiar incêndio com câmeras e IA", "Com um operador confirmando cada alerta.")
        + item("cloud-sun", "Usar previsão do tempo por IA", "Aberta e ao lado da física; na América do Sul, desempenho não demonstrado.")
        + item("eye", "Pulverizar pomar com máquina autônoma", "Já é produto em nichos, com um operador para até oito máquinas.")
        + item("thermometer-sun", "Conhecer o risco climático da cultura", "Pelo zoneamento agroclimático, que não usa IA.")
        + "</div>"
        + f'<div class="col t"><div class="cb">{ic("trending-up")}<h3>Tendência</h3><span class="sb">chegando</span></div>'
        + item("layers", "Modelos de fundação de imagem", "Vetores prontos, que pedem menos rótulos de campo.")
        + item("wind", "Previsão por conjunto e híbrida", "IA com física, nos centros de referência.")
        + item("radar", "Radar aberto de banda L", "Penetra melhor a vegetação densa (NISAR).")
        + item("cloud-rain", "Chuva das próximas horas só com satélite", "Onde falta radar meteorológico.")
        + item("bot", "Robô que sobe na palmeira e corta o cacho", "À venda para o açaí, por controle remoto; sem ensaio independente.")
        + "</div>"
        + f'<div class="col p"><div class="cb">{ic("flask-conical")}<h3>Ainda pesquisa</h3><span class="sb">sem validação</span></div>'
        + item("chart-line", "Prever produtividade por satélite", "Amostras pequenas no café; na palma, modelo sem satélite.")
        + item("leaf", "Detectar doença e estresse hídrico", "Os casos validados são de drone, não de satélite.")
        + item("tree-palm", "Colher palma com solução integrada", "A robótica de colheita segue experimental.")
        + item("sprout", "Identificar macaúba por imagem", "Só com drone; não achamos estudo por satélite.")
        + item("hand", "Colher macaúba com máquina", "Só um colhedor vibratório portátil, medido pelos inventores; nenhum robô.")
        + "</div></div>"
        + '<p class="note" style="margin-top:9px;font-size:11px">Leitura nossa, macro; não é recomendação. Nos três grupos, a dependência comum é o dado de campo para rotular e validar.</p>',
        fontes(("M1376", "p. 1"), ("M1377", "p. 1, 8"), ("M1379", "p. 2, 9"), ("M769", "p. 3"), ("M645", "p. 2"), ("M1352", "p. 22"), ("M1277", "p. 1-2"),
               ("M1335", "p. 1, 12-15"), ("M1333", "p. 2"), ("M1346", "p. 2, 4-5"), ("M1366", "p. 17"), ("M1370", "p. 1-4"), ("M1284", "p. 1"), ("M1263", "p. 6, 9-10"),
               ("M1309", "p. 12"), ("M1232", "p. 2"), ("M1279", "p. 2-3"), ("M1288", "p. 5-6"), ("M1234", "p. 1-2"), ("M1336", "p. 1, 3, 7"),
               ("M1400", "web"), ("M1386", "web")))

    # ------------------------------------------------------------------------------------------
    # Fecho
    # ------------------------------------------------------------------------------------------
    def sinal(frente, texto, n):
        pontos = "".join(f'<span class="{"on" if k < n else ""}"></span>' for k in range(4))
        return f'<div class="fr">{frente}</div><div class="lb">{texto}</div><div class="ds">{pontos}</div><div class="n">{n}/4</div>'

    sessoes = s(
        "Sessões executivas", "Quatro conversas com executivos do agro e da bioenergia · agregado e anonimizado",
        "Sessões: letramento e governança nas quatro; retorno medido em nenhuma",
        '<div class="g2" style="grid-template-columns:1.45fr 1fr;margin-top:12px">'
        + painel("O que se repete", "Cada ponto é uma das quatro empresas ouvidas",
                 '<div class="sg">'
                 + sinal("F1", "Nenhuma mede o retorno financeiro da IA generativa; o ganho é tempo, horas ou uso", 4)
                 + sinal("F1", "Resultado comprovado na IA preditiva ou na embarcada no campo", 2)
                 + sinal("F2", "Política, comitê ou homologação central de IA", 4)
                 + sinal("F2", "Letramento como desafio central", 4)
                 + sinal("F2", "Dados centralizados antes da IA", 3)
                 + sinal("F2", "Acesso avançado por perfil, por valor provado ou por formação", 3)
                 + sinal("F2", "Champions por área como papel formal", 2)
                 + sinal("F3", "Autonomia vista como inevitável; em duas, pela falta de mão de obra", 3)
                 + sinal("F3", "Consumo controlado por cota ou orçamento, sem cobrança por resultado", 3)
                 + sinal("F3", "Falta de padrão entre fabricantes trava a autonomia", 2)
                 + "</div>")
        + '<div>'
        + painel("Na régua de maturidade", "Leitura nossa",
                 fato("3 + 1", "três empresas no estágio 2 e uma no 3: dados e governança chegam ao 3; pessoas e aplicações ficam para trás.")
                 + fato("Para o 4", "falta às quatro medir o retorno e acompanhar os casos como portfólio; uma delas tem isso como meta de 2027."))
        + '<div class="fala">"A IA já está dentro da empresa. Não tem como segurar."<small>Fala de um dos entrevistados</small></div>'
        + '<div class="fala">"Vai se trabalhando mais por uso, não por retorno."<small>Fala de um dos entrevistados</small></div>'
        + '<div class="fala">"Tudo tem um jeitinho. Se mostrar valor, é possível."<small>Fala de um dos entrevistados</small></div>'
        + "</div></div>",
        '<div class="fontes"><b>Fontes</b><span class="f w">Sessões executivas do estudo, de 13 a 21/10/2026. Entram só no agregado, sem nome de pessoa nem de empresa.</span></div>')

    def pergunta(icone, n, titulo, texto, ver):
        return (f'<div class="p"><div class="top">{ic(icone)}<span class="no">{n}</span></div><h3>{titulo}</h3><p>{texto}</p>'
                f'<div class="vr">{ver}</div></div>')

    fecho = s(
        "Fecho", "Para a conversa", "Seis perguntas que o mercado respondeu antes de escalar a IA",
        '<div class="pg6">'
        + pergunta("target", "01", "Qual dor medida vem primeiro?", "Os casos com resultado partem de um problema do negócio, com métrica e dono.", "casos 1 a 3 · checkpoints")
        + pergunta("database", "02", "A base de dados e de campo está de pé?", "Conectividade, dados e estrutura levaram anos e vieram antes da IA generativa.", "o caminho e o ritmo")
        + pergunta("crown", "03", "Quem patrocina e quem decide?", "Patrocínio executivo, comitê e champions aparecem nas jornadas públicas e nas sessões.", "quem faz o quê")
        + pergunta("badge-check", "04", "Qual é o canal oficial e a regra de dado?", "Proibir funciona pouco; a conta oficial cresce quando a empresa oferece o canal.", "do uso por fora ao canal oficial")
        + pergunta("gauge", "05", "Como o valor é medido, caso a caso?", "Quem rastreia o retorno e trata a IA como portfólio tem mais iniciativas com retorno positivo.", "valor, custo e índices do degrau 3 → 4")
        + pergunta("eye", "06", "Onde a pessoa decide e onde a máquina decide?", "No campo, a decisão segue humana, com exceções estreitas, dentro de uma regra definida por pessoas.", "casos 1 e 2 · autonomia")
        + "</div>"
        + '<div class="box g" style="margin-top:12px"><b>Leitura nossa, macro.</b> Não é diagnóstico da Acelen nem recomendação de ferramenta. '
          'Cada número desta apresentação tem fonte e página no sistema do estudo; o detalhe de cada tema está no Report Final (BIA-ACL-RF-01).</div>',
        '<div class="fontes"><b>Fontes</b><span class="f w">As dos slides indicados em cada pergunta.</span></div>')

    metodo = slides_metodologia.slides(g, s, ic, painel, faixa)
    deck = [*metodo, resumo, regua, setores, caso_suzano, caso_seletiva, caso_uber, caso_ifood, valor,
            trajetoria, ritmo, checkpoints, indices, shadow, papeis,
            custo, autonomia, perenes, colheita, robos, satelites, horizonte,
            sessoes, fecho]
    # Ampliação do corpo de cada slide (1 = tamanho de desenho), ajustada pela folga medida no PDF.
    for slide, zoom in zip(deck, ZOOM):
        slide["zoom"] = zoom
    return deck
