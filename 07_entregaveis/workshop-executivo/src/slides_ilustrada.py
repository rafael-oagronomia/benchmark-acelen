"""Slides da versão ilustrada da apresentação executiva (BIA-ACL-AE-02).

Cada slide mostra imagens do próprio conteúdo: a foto ou a figura da fonte citada (relatório da empresa,
estudo, página do produto, publicação do executivo) e poucos números grandes. Todo número é o mesmo da
apresentação executiva (BIA-ACL-AE-01, `slides.py`), com a mesma citação: ao mudar um número lá, mudar
aqui também. Metodologia, resumo em seis números e sessões executivas são os slides da executiva.
"""
from __future__ import annotations

import slides as executiva

F1, F2, F3 = executiva.F1, executiva.F2, executiva.F3


def slides(fontes, g, foto) -> list[dict]:
    base = executiva.slides(fontes, g)
    estudo, acervo = base[0], base[1]  # metodologia (slides_metodologia.py)
    resumo = next(b for b in base if b["titulo"] == "O benchmark em seis números")
    sessoes = next(b for b in base if b["parte"] == "Sessões executivas")

    def ic(nome: str, classe: str = "ic") -> str:
        return f'<i data-lucide="{nome}" class="{classe}"></i>'

    def painel(titulo: str, sub: str, corpo: str, estilo: str = "") -> str:
        sub_html = f'<div class="sub">{sub}</div>' if sub else ""
        est = f' style="{estilo}"' if estilo else ""
        return f'<div class="panel"{est}><h3>{titulo}</h3>{sub_html}{corpo}</div>'

    def leitura(texto: str) -> str:
        return f'<div class="read" style="margin-top:0"><b>Leitura nossa.</b> {texto}</div>'

    def kp(n: str, rotulo: str, texto: str, classe: str = "") -> str:
        num = f'<div class="n">{n}</div>' if n else ""
        return f'<div class="kp {classe}{"" if n else " t"}">{num}<div><div class="rt">{rotulo}</div><p>{texto}</p></div></div>'

    def comoler(texto: str) -> str:
        return f'<div class="rc"><span><b>Como ler</b> · {texto}</span></div>'

    def s(parte: str, olho: str, titulo: str, corpo: str, fts: str = "", zoom: float = 1.0) -> dict:
        return {"parte": parte, "olho": olho, "titulo": titulo, "corpo": corpo, "fontes": fts, "zoom": zoom}

    # ---------------- Frente 1 ----------------
    regua = s(
        F1, "Painel de empresas na régua de maturidade", "No painel, ninguém chega ao estágio 5; a governança de IA é o degrau mais baixo",
        '<div class="il gr" style="grid-template-columns:1.22fr 0.78fr">'
        + painel("A régua de cinco estágios e o estágio geral de cada empresa",
                 "Só com evidência pública; o geral é o maior estágio atingido em ao menos três das quatro dimensões", g.escada(665, 318))
        + '<div class="dir" style="justify-content:stretch">'
        + '<div class="q2">' + foto("suzano-plantio", "Suzano · estágio 3") + foto("bayer-melhoramento", "Bayer · estágio 4")
        + foto("deere-pulverizador", "Deere · estágio 3") + foto("dji-drone", "DJI · estágio 2") + "</div>"
        + kp("3 de 4", "Governança", "empresas no <b>estágio 2 em governança;</b> dados e aplicações chegam ao 3 e ao 4.")
        + "</div></div>",
        fontes(("M789", "p. 11, 30"), ("M335", "p. 69, 101"), ("M867", "p. 10"), ("M845", "p. 1"), ("M784", "p. 1-3"), ("M336", "p. 22, 39"),
               ("M397", "p. 25, 27"), ("M876", "p. 5")))

    caso_suzano = s(
        F1, "Caso 1 · IA preditiva no campo", "Suzano: torres com IA contra incêndio, com uma pessoa confirmando cada alerta",
        '<div class="il">'
        + foto("suzano-brigada", "Suzano · combate a incêndio no relatório de 2024")
        + '<div class="dir">'
        + kp("133", "Iniciativa", "<b>torres com câmeras e IA</b> que reconhecem a fumaça, acompanhadas 24 horas (dez/2024).")
        + kp("−61%", "Resultado", "<b>de incêndios em áreas de plantio</b> em 2024, contra 2023; a empresa credita o número a esforços integrados, não só à IA.", "g")
        + kp("85%", "Consequência", "<b>dos focos controlados</b> antes de virar ocorrência de maior impacto, nos três anos até ago/2026.")
        + leitura("Um operador confirma cada alerta antes de mandar a brigada: a tecnologia encurta o tempo, a decisão segue humana.")
        + "</div></div>",
        fontes(("M335", "p. 69"), ("M769", "p. 2-3"), ("M753", "p. 2-4")))

    caso_seletiva = s(
        F1, "Caso 2 · IA embarcada na máquina", "Pulverização seletiva: a máquina decide planta a planta; a regra continua humana",
        '<div class="il inv">'
        + '<div class="dir">'
        + kp("", "Iniciativa", "<b>Câmeras e IA na barra:</b> a máquina aplica só onde há planta daninha, dentro de uma sensibilidade definida por pessoas.")
        + kp("−76%", "Resultado", "<b>de herbicida,</b> em média, em 5 lavouras de soja (Iowa State, 2024), medido por terceiro.", "g")
        + kp("+280%", "O risco", "<b>ao ano de caruru</b> no ensaio de 3 anos do Arkansas, na sensibilidade mais baixa.", "w")
        + leitura("Economizar demais hoje pode custar o controle amanhã: a máquina decide, a pessoa calibra.")
        + "</div>"
        + '<div class="ft2">' + foto("seletiva-aplicacao", "Ensaio do Arkansas · o jato em azul") + foto("seletiva-mapa", "Iowa State · em amarelo, onde a barra aplicou") + "</div>"
        + "</div>",
        fontes(("M1286", "p. 1-2"), ("M1296", "p. 2-3")))

    caso_uber = s(
        F1, "Caso 3 · IA generativa e custo", "Uber: o orçamento de IA acabou em quatro meses; o controle veio pelo consumo",
        '<div class="il" style="grid-template-columns:1.25fr 0.75fr">'
        + '<div class="ft2">' + foto("uber-adocao", "Uber · uso e custo, fev a ago/2026", "ct") + foto("uber-custo", "Uber · custo por sessão com o mesmo modelo", "ct") + "</div>"
        + '<div class="dir">'
        + kp("≈ 4 meses", "Problema", "durou o <b>orçamento de IA de 2026;</b> os custos tinham crescido 6 vezes desde 2024.", "w")
        + kp("US$ 1.500", "Iniciativa", "de <b>teto por mês,</b> por funcionário e por ferramenta; depois, faixa única de gasto, com alertas.")
        + kp("−52%", "Resultado", "<b>no custo por sessão,</b> contra o pico de jun/2026, com o mesmo modelo.", "g")
        + comoler("números declarados pela empresa; o estouro do orçamento vem da imprensa")
        + "</div></div>",
        fontes(("M989", "p. 3"), ("M986", "p. 2"), ("M941", "p. 3"), ("M995", "p. 2, 15")))

    caso_ifood = s(
        F1, "Caso 4 · IA generativa e custo · publicação do CEO do iFood", "iFood: o uso de IA dobrou e a conta caiu pela metade, sem limitar o acesso",
        '<div class="il" style="grid-template-columns:0.62fr 1.38fr">'
        + foto("ifood-post", "", "ct")
        + '<div class="dir">'
        + kp("+106% · −51%", "Resultado", "<b>tokens e custo</b> desde junho de 2026, segundo o CEO: \"a boca de jacaré\".", "g")
        + kp("8 em 10", "Iniciativa", "tokens rodam em <b>modelos abertos,</b> o padrão de uma plataforma própria; os premium ficam para as tarefas que os justificam, com orçamento.")
        + kp("30×", "Uso", "mais <b>uso de IA</b> desde janeiro de 2026, 7 vezes mais por pessoa, e todos seguem com tokens ilimitados.")
        + leitura("O modelo do tamanho da tarefa: a conta cai quando o modelo mais caro deixa de ser o padrão, sem limitar o acesso.")
        + comoler("números declarados pelo CEO numa rede social, sem valores em moeda e sem verificação de terceiros")
        + "</div></div>",
        fontes(("M1382", "web")))

    # ---------------- Frente 2 ----------------
    def fase(n, titulo, texto, valor, legenda, classe=""):
        return (f'<div class="f {classe}"><div class="no">{n}</div><div><h3>{titulo}</h3><p>{texto}</p></div>'
                f'<div class="v">{valor}<small>{legenda}</small></div></div>')

    caminho = s(
        F2, "Roteiro de adoção · o caminho", "O caminho que se repete: seis fases, em ordem parecida",
        '<div class="il inv" style="grid-template-columns:1.18fr 0.82fr">'
        + '<div class="dir"><div class="fs6">'
        + fase(1, "Alicerce de dados e de campo", "Dados e nuvem; no agro, conectividade no campo e centro de operações.", "2015", "São Martinho: início da rede no campo")
        + fase(2, "Estrutura dedicada", "Um centro, área ou grupo responsável pela IA.", "2019", "Vale: centro de IA aberto")
        + fase(3, "IA preditiva em dores medidas", "Incêndio, insumos, manutenção e logística, com resultado medido.", "−50%", "bp bioenergy: incêndios, 2019–2025")
        + fase(4, "IA generativa: da proibição ao assistente", "Restrição depois dos primeiros vazamentos; depois, assistente para todos.", "110 mil", "Petrobras: com acesso em dez/2023")
        + fase(5, "Governança e democratização", "Política com treinamento e triagem de demandas.", "99%", "São Martinho: treinados na política de IA")
        + fase(6, "Agentes com cautela", "Plataformas de agentes com limites de autonomia.", "5%", "têm os controles completos (BCG)", "cau")
        + "</div></div>"
        + '<div class="ft3">' + foto("saomartinho-centro", "Fase 1 · São Martinho: centro de operações") + foto("vale", "Fase 2 · Vale")
        + foto("bp-centro", "Fase 3 · bp bioenergy: monitoramento de incêndios") + "</div>"
        + "</div>",
        fontes(("M1222", "p. 27"), ("M1251", "p. 1"), ("M1217", "p. 1"), ("M1245", "p. 2"), ("M1240", "p. 1"), ("M357", "p. 46"), ("M1199", "p. 10")))

    shadow = s(
        F2, "IA generativa · do uso por fora ao canal oficial", "Proibir funciona pouco; quando a empresa oferece o canal, a conta oficial cresce",
        '<div class="il inv">'
        + painel("Usuários de IA generativa, por tipo de conta", "Netskope, medição de tráfego na clientela, em um ano",
                 g.inclinacao([("contas pessoais", 78, 47, "laranja"), ("contas da empresa", 25, 62, "verde")], "out/2024", "out/2025", 560, 320)
                 + '<div class="cap">As duas mudanças aconteceram juntas; a fonte não prova que uma causou a outra.</div>')
        + '<div class="dir">'
        + kp("67%", "Onde a IA é proibida", "enviam <b>dado sensível a IA pública;</b> onde não há política, 33% (KPMG e Univ. de Melbourne, 2025).", "w")
        + kp("90%", "Hoje", "das organizações <b>bloqueiam algum aplicativo de IA,</b> em média 10 (clientela da Netskope).")
        + kp("", "O caminho", "<b>Canal oficial:</b> conta da empresa, dado protegido no contrato, registro de uso e regra de dado clara e treinada (leitura nossa).", "g")
        + "</div></div>",
        fontes(("M110", "p. 73, 77"), ("M1049", "p. 2-3, 10")))

    # ---------------- Frente 3 ----------------
    autonomia = s(
        F3, "Sistemas autônomos · máquinas, robôs e drones", "A autonomia já é produto em nichos, com supervisão; quatro quebras no caminho",
        '<div class="il">'
        + '<div class="ft2">' + foto("arbus", "Citros · pulverizador autônomo Arbus (Jacto)") + foto("solix", "Lavoura · robô Solix (Solinftec)") + "</div>"
        + '<div class="dir">'
        + kp("16 mil h", "Citros", "do pulverizador autônomo em cerca de <b>60 mil ha</b> antes de virar produto, em abr/2026, segundo a empresa.")
        + kp("≈ 150 + 100", "Lavoura", "<b>robôs nos EUA e no Brasil,</b> segundo a Forbes.")
        + kp("1 : 8", "Supervisão", "um operador para até <b>oito pulverizadores</b> autônomos em pomares: a supervisão segue humana, a distância.", "g")
        + kp("4", "Quebras e recuos", "empresas de robótica de campo em 2024 e 2025; nas com causa declarada, <b>o capital acabou antes da escala.</b>", "w")
        + "</div></div>",
        fontes(("M325", "p. 2-3"), ("M253", "p. 7"), ("M1284", "p. 1"), ("M1319", "p. 1"), ("M1298", "p. 2"), ("M1301", "p. 1-2"), ("M1303", "p. 10")))

    perenes = s(
        F3, "Culturas perenes e mão de obra", "Nas perenes, a falta de gente puxa a máquina; a colheita é o gargalo",
        '<div class="il inv">'
        + '<div class="dir">'
        + kp("60% · 50%", "Palma de óleo", "da <b>força de trabalho</b> e do <b>custo de produção</b> estão na colheita.")
        + kp("21 → 86 ha", "Por trabalhador", "na colheita da palma: <b>à mão</b> e com <b>colhedora de médio porte</b> (estudo citado pelo MPOB).", "g")
        + kp("26% × 8,7%", "Brasil", "<b>mecanização</b> contra <b>automação ou digital</b> como principal resposta à falta de mão de obra (CNA/Cepea, 2026).")
        + leitura("A falta de gente é o motor declarado, mas a resposta é mais mecanização que IA. Na macaúba, antes da máquina vem a cultivar.")
        + "</div>"
        + '<div class="ft1x2">' + foto("palma-cortador", "Palma · cortador motorizado em vara") + foto("palma-maquina", "Palma · máquina para palmas altas") + "</div>"
        + "</div>",
        fontes(("M1234", "p. 1"), ("M377", "p. 11-12"), ("M1268", "p. 14"), ("M1385", "p. 2-3")))

    colheita = s(
        F3, "Colheita da macaúba · mão de obra e segurança do trabalho", "Macaúba: a colheita depende de gente; o risco é descrito, mas não foi medido",
        '<div class="il" style="grid-template-columns:0.72fr 1.28fr">'
        + '<div class="ft2">' + foto("inpa-vara", "Palmeiras · vara de coleta no cacho (INPA)") + foto("macauba-telas", "Macaúba · cachos em tela (Embrapa Cerrados)") + "</div>"
        + '<div class="dir">'
        + painel("A altura do problema: até onde cada ferramenta alcança", "Em metros, segundo quem desenvolveu ou testou cada uma · faixa verde: estipe da macaúba adulta",
                 g.alcance([("Colhedor|vibratório|(macaúba)", None, 4, "4 m", "verde"),
                            ("Cortador|motorizado|(palma)", 4.5, 6, "6 m", "cinza"),
                            ("Vara com|foice,|tradicional", 8, 10, "8 a 10 m", "cinza"),
                            ("Robôs de|coqueiro,|em teste", 13.42, 15.2, "15,2 m", "ambar"),
                            ("Vara de|alumínio|(INPA)", None, 19.2, "19,2 m", "cinza"),
                            ("Robô do|açaí,|à venda", None, None, "?", "ambar")],
                           (15, 20, "Macaúba adulta", "estipe de 15 a 20 m, com espinhos"), largura=700, altura=214))
        + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">'
        + kp("", "Como se colhe", "<b>Do chão ou com foice em vara;</b> não há máquina no mercado (Embrapa Cerrados, UFV e UFLA).")
        + kp("", "Risco", "<b>Nenhum número de acidente</b> na macaúba; no açaí, 90% de 33 coletores já caíram.", "w")
        + "</div></div></div>",
        fontes(("M1395", "p. 8"), ("M1390", "web"), ("M1265", "p. 9"), ("M1418", "p. 9, 11-12"), ("M1422", "web"), ("M1277", "p. 1"),
               ("M1256", "p. 6"), ("M1385", "p. 2"), ("M1383", "web"), ("M1388", "web"), ("M1400", "web"), ("M1410", "web")))

    def cartao(imagem, rotulo_foto, rotulo, numero, texto, classe=""):
        return (f'<div class="cd">{foto(imagem, rotulo_foto, classe)}<div class="tx"><div class="rt">{rotulo}</div>'
                f'<div class="n">{numero}</div><p>{texto}</p></div></div>')

    robos = s(
        F3, "Robótica de colheita em palmeiras · robôs que sobem no estipe e cortam o cacho", "Robô escalador: à venda no açaí, em teste no coco, nada para a macaúba",
        '<div class="tr4">'
        + cartao("acaibot", "Açaí · AçaíBot (Kaatech)", "Açaí · à venda", "R$ 22,9 mil",
                 "<b>por controle remoto,</b> na loja do fabricante; o Amapá comprou 44. Sem ensaio independente.")
        + cartao("amaran", "Coco · Amaran (Índia)", "Coco · teste dos autores", "21,9 × 11,8 min",
                 "<b>por coqueiro:</b> o robô foi mais lento que o colhedor (IEEE Spectrum).")
        + cartao("robo-palma", "Palma · protótipo escalador", "Palma · protótipo", "5 travas",
                 "<b>a subida ainda não é confiável;</b> os protótipos pedem montagem à mão.")
        + cartao("colhedor-macauba", "Macaúba · colhedor vibratório (UFV)", "Macaúba · nenhum robô", "434 kg/h",
                 "<b>do chão:</b> colhedor portátil, medido pelos inventores.", "ct")
        + "</div>",
        fontes(("M1400", "web"), ("M1399", "p. 1"), ("M1383", "web"), ("M1403", "web"), ("M1385", "p. 3, 8, 16"), ("M1386", "web"), ("M1265", "p. 9")))

    satelites = s(
        F3, "Satélites e modelos de fundação · imagem e clima", "Satélite: mapear perenes já funciona; a IA do tempo opera ao lado da física",
        '<div class="il" style="grid-template-columns:1.2fr 0.8fr">'
        + '<div class="ft2">' + foto("palma-mapa", "Palma · imagem, classificação e probabilidade (mapa global)", "ct") + foto("cacau-mapa", "Cacau · mapa da Costa do Marfim", "ct") + "</div>"
        + '<div class="dir">'
        + kp("88% · 77%", "Palma · mapa global", "de acerto nos <b>plantios industriais</b> e nos <b>de pequenos produtores;</b> perde os plantios jovens.")
        + kp("91,7%", "Cacau · África Ocidental", "de acerto na <b>validação de campo às cegas;</b> detecta plantios jovens.", "g")
        + kp("90% · 97,2%", "IA do tempo", "dos alvos em que <b>dois modelos de IA</b> superaram o modelo físico, segundo os autores; a chuva ficou fora do placar.")
        + kp("", "Recordes", "<b>De calor, frio e vento:</b> o modelo físico venceu em quase todos os prazos (Science Advances, 2026).", "w")
        + "</div></div>",
        fontes(("M1376", "p. 1, 8"), ("M1377", "p. 3-4, 8"), ("M1338", "p. 1, 4"), ("M1337", "p. 1, 4"), ("M1343", "p. 1-3")))

    # ---------------- Fecho ----------------
    def pergunta(icone, n, titulo, texto, ver):
        return (f'<div class="p"><div class="top">{ic(icone)}<span class="no">{n}</span></div><h3>{titulo}</h3><p>{texto}</p>'
                f'<div class="vr">{ver}</div></div>')

    fecho = s(
        "Fecho", "Para a conversa", "Seis perguntas que o mercado respondeu antes de escalar a IA",
        '<div class="pg6">'
        + pergunta("target", "01", "Qual dor medida vem primeiro?", "Os casos com resultado partem de um problema do negócio, com métrica e dono.", "casos 1 e 2")
        + pergunta("database", "02", "A base de dados e de campo está de pé?", "Conectividade, dados e estrutura levaram anos e vieram antes da IA generativa.", "o caminho")
        + pergunta("crown", "03", "Quem patrocina e quem decide?", "Patrocínio executivo, comitê e champions aparecem nas jornadas públicas e nas sessões.", "sessões executivas")
        + pergunta("badge-check", "04", "Qual é o canal oficial e a regra de dado?", "Proibir funciona pouco; a conta oficial cresce quando a empresa oferece o canal.", "do uso por fora ao canal oficial")
        + pergunta("gauge", "05", "Como o valor é medido, caso a caso?", "A conta da IA se controla pelo consumo e pelo modelo do tamanho da tarefa.", "casos 3 e 4")
        + pergunta("eye", "06", "Onde a pessoa decide e onde a máquina decide?", "No campo, a decisão segue humana, com exceções estreitas, dentro de uma regra definida por pessoas.", "casos 1 e 2 · autonomia")
        + "</div>"
        + '<div class="box g" style="margin-top:12px"><b>Leitura nossa, macro.</b> Não é diagnóstico da Acelen nem recomendação de ferramenta. '
          'As imagens vêm das fontes citadas em cada slide, com a origem indicada, para fins de estudo; o detalhe e todas as fontes estão na apresentação executiva (BIA-ACL-AE-01) e no Report Final (BIA-ACL-RF-01).</div>',
        '<div class="fontes"><b>Fontes</b><span class="f w">As dos slides indicados em cada pergunta.</span></div>', zoom=1.06)

    return [estudo, acervo, resumo, regua, caso_suzano, caso_seletiva, caso_uber, caso_ifood, caminho, shadow,
            autonomia, perenes, colheita, robos, satelites, sessoes, fecho]
