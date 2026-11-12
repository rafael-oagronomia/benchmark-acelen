"""Slides de resultado da nota "Satélites e modelos de fundação: imagem e clima" (Frente 3,
aprofundamento) para o Report Final.

Quatro pares, cada um com um slide visual e um descritivo. Todo número vem da nota
`04_frente-3_tendencias/satelites-e-modelos-de-fundacao.md`, com a mesma citação; a linha de fontes
sai do catálogo. Ao mudar a nota, mudar aqui também.

Recebe as peças do gerador (novo, fontes, barras, lista) para não importar o gerador de volta.
"""
from __future__ import annotations


def slides(novo, fontes, barras, lista) -> list[dict]:
    def tl4(itens):
        return '<div class="tl4">' + "".join(
            f'<div class="i"><div class="d">{d}</div><div><div class="k">{k}</div><p>{p}</p></div></div>' for d, k, p in itens) + "</div>"

    def tiles(itens, colunas=2):
        estilo = f' style="grid-template-columns:repeat({colunas},1fr)"' if colunas != 2 else ""
        return f'<div class="tiles"{estilo}>' + "".join(
            f'<div class="tl"><div class="a">{a}</div><div class="n">{n}</div><p>{p}</p></div>' for a, n, p in itens) + "</div>"

    def painel(titulo, sub, corpo, classe="panel"):
        sub_html = f'<div class="sub">{sub}</div>' if sub else ""
        return f'<div class="{classe}"><h3>{titulo}</h3>{sub_html}{corpo}</div>'

    def leitura(texto):
        return f'<div class="read"><b>Leitura nossa.</b> {texto}</div>'

    # ---- Par 1: o tempo, na média e nos recordes ---------------------------------------------------
    tempo_visual = novo(
        "Satélites e modelos de fundação · 1/8", "Satélites e modelos de fundação · previsão do tempo por IA",
        "Na média, a IA do tempo vence; nos recordes, os modelos avaliados perdem",
        f"""<div class="g2" style="grid-template-columns:1fr 1.1fr;margin-top:12px">
  {painel("Alvos em que o modelo de IA superou a previsão tradicional", "Segundo os autores; métricas globais; no GraphCast e no GenCast, a chuva ficou fora do placar",
          barras([("GraphCast · 1.380 alvos", 90, "90%", "verde"),
                  ("GenCast · 1.320 alvos", 97.2, "97,2%", "verde"),
                  ("Aurora · tempo global a 0,1°", 92, "92%", "verde")], rotulo_w=210)
          + '<div class="mini"><span class="n">Recordes</span><span>de calor, frio e vento: o modelo físico venceu em quase todos os prazos (GraphCast, Pangu-Weather e Fuxi; Science Advances, 2026)</span></div>')}
  {painel("Em operação, ao lado do modelo físico", "", tl4([
      ("fev/2025", "ECMWF", "o modelo de IA entra em operação ao lado do modelo físico, com grade de 28 km contra 9 km"),
      ("jul/2025", "ECMWF", "a versão por conjunto, com 51 previsões, entra em operação"),
      ("out/2025", "Organização Meteorológica Mundial", "aprova integrar a IA à previsão global: complementar, não substituir"),
      ("dez/2025", "NOAA (EUA)", "anuncia três modelos de IA em operação, partindo do GraphCast, do Google")]))}
</div>
{leitura("A IA do tempo já está em operação, mas ao lado do modelo físico, de cujas condições iniciais ela parte. Nos recordes, os modelos avaliados ainda perdem.")}""",
        fontes(("M1338", "p. 1, 4"), ("M1337", "p. 1, 4"), ("M1344", "p. 1"), ("M1343", "p. 1-3"), ("M645", "p. 2-3"), ("M1333", "p. 2"),
               ("M1350", "p. 1, 3"), ("M1346", "p. 1-2, 5-6")))

    tempo_descritivo = novo(
        "Satélites e modelos de fundação · 2/8", "Satélites e modelos de fundação · o que a média esconde",
        "O que a média esconde: chuva, recordes, grade e dependência da física",
        f"""<div class="col3">
  {painel("Fora do placar", "", lista([
      "<b>Chuva:</b> GraphCast e GenCast a excluíram da avaliação principal, por desconfiança nos dados de chuva da reanálise.",
      "<b>No AIFS:</b> a chuva foi pior que a do modelo físico nos prazos curtos dos extratrópicos e melhor nos longos, na verificação do ECMWF (pré-print)."]))}
  {painel("Recordes", "", lista([
      "<b>O que se mediu:</b> os modelos de IA avaliados subestimam a frequência e a intensidade dos recordes, com erro que cresce quanto maior a quebra.",
      "<b>O que não se mediu:</b> o AIFS e o GenCast ficaram fora; os autores supõem que os modelos por conjunto tenham o mesmo problema e pedem rodar os dois tipos em paralelo."]))}
  {painel("Grade e física", "", lista([
      "<b>Grade:</b> o modelo de IA do ECMWF roda com 28 km, contra 9 km do modelo físico.",
      "<b>Física:</b> parte das condições iniciais do modelo físico; para os autores do Aurora, o ajuste rápido só foi possível pelas décadas de dados dos modelos numéricos.",
      "<b>OMM:</b> a previsão local de alto impacto ainda precisa de teste antes do uso operacional."]))}
</div>""",
        fontes(("M1338", "p. 4"), ("M1337", "p. 4"), ("M1334", "p. 6-7"), ("M1343", "p. 1-3, 6"), ("M645", "p. 2-3"), ("M1333", "p. 2-3"),
               ("M1344", "p. 7"), ("M1350", "p. 3")))

    # ---- Par 2: o tempo no Brasil e no agro --------------------------------------------------------
    brasil_visual = novo(
        "Satélites e modelos de fundação · 3/8", "Satélites e modelos de fundação · previsão por IA no Brasil",
        "IA do tempo no Brasil: o resultado depende da estação e da variável",
        f"""<div class="g2" style="grid-template-columns:1.1fr 1fr;margin-top:12px">
  {painel("GraphCast contra o modelo do ECMWF, no geopotencial a 500 hPa", "Escore em que 100% é igual ao modelo europeu · PUCRS, pré-print de 2026, sem chuva",
          barras([("Sul · mar, out e jan", 135, "102% a 135%", "verde"),
                  ("Quatro sub-regiões · jul, 48 h", 88, "70% a 88%", "ambar"),
                  ("Sul · jul, 120 h", 47.91, "47,91%", "ambar")], maximo=200, rotulo_w=210)
          + '<div class="mini"><span class="n">p = 0,16</span><span>no teste pareado, a diferença do Sul em julho não foi significativa</span></div>')}
  {painel("No Brasil", "", tiles([
      ("MONAN (INPE)", "físico", "novo modelo operacional anunciado em 04/09/2026: global, 11 dias, cerca de 10 km"),
      ("INMET", "sem fonte", "oficial sobre uso ou teste de modelos de IA de previsão"),
      ("TUPANN (IMPA)", "10–180 min", "chuva prevista só com satélite; segundo os autores, apoia o Inea (RJ)"),
      ("Recordes", "poucos", "a avaliação principal tem poucos ou nenhum recorde na América do Sul")]))}
</div>
{leitura("O ganho da IA de tempo na América do Sul não está demonstrado nem negado: a única avaliação regional é um pré-print sem chuva.")}""",
        fontes(("M1352", "p. 13, 17, 19-22"), ("M1372", "p. 1-3"), ("M1366", "p. 1, 17"), ("M1343", "p. 3")))

    agro_descritivo = novo(
        "Satélites e modelos de fundação · 4/8", "Satélites e modelos de fundação · do tempo ao agro",
        "Previsão por IA no agro: escala na Índia, nenhum caso medido no Brasil",
        f"""<div class="col3">
  {painel("Índia: um caso com escala", "", lista([
      "<b>Monção:</b> previsão do início das chuvas por IA, enviada por SMS a mais de 3,88 crore de agricultores (38,8 milhões, cálculo nosso), em 13 estados, na safra de 2025.",
      "<b>O que mudou:</b> de 31% a 52% dos agricultores pesquisados em dois estados mudaram decisões de plantio; é mudança declarada, sem ganho de produtividade ou de renda medido."]))}
  {painel("Brasil: risco climático sem IA", "", lista([
      "<b>Zarc:</b> exigido para o Proagro e a subvenção ao seguro rural; a página da Embrapa não menciona IA.",
      "<b>Macaúba:</b> o zoneamento de 2024 usa balanço hídrico com 3.500 séries de chuva; o risco de frio é a chance de mínimas iguais ou menores que 3 °C, 1 °C ou 0 °C, conforme a espécie."]))}
  {painel("Do sazonal à fazenda", "", lista([
      "<b>Subsazonal:</b> o FuXi-S2S supera o sistema do ECMWF em chuva, segundo os autores; não achamos previsão sazonal por IA em operação.",
      "<b>Até a fazenda:</b> o CorrDiff leva a reanálise de 25 km a 2 km sobre Taiwan, com dados de treino sem uso comercial; não achamos redução de escala por IA avaliada no Brasil."]))}
</div>""",
        fontes(("M1378", "p. 1, 5-6"), ("M1371", "p. 1, 3-4"), ("M1277", "p. 1-2"), ("M1354", "p. 1, 4"), ("M1348", "p. 1, 22")))

    # ---- Par 3: modelos de fundação de imagem ------------------------------------------------------
    imagem_visual = novo(
        "Satélites e modelos de fundação · 5/8", "Satélites e modelos de fundação · imagem de satélite",
        "Modelo de fundação de imagem: ganha quando faltam rótulos, mas não sempre",
        f"""<div class="g2" style="grid-template-columns:1.1fr 1fr;margin-top:12px">
  {painel("Com 10% dos rótulos (mIoU)", "Comparação feita por terceiros (PANGAEA, pré-print) · verde: modelo de fundação; cinza: treinado do zero",
          '<div class="sub" style="margin-top:6px">Culturas do Sudão do Sul</div>'
          + barras([("S12-DINO", 38.44, "38,44", "verde"), ("CROMA", 36.77, "36,77", "verde"),
                    ("ViT do zero", 27.76, "27,76", "cinza"), ("U-Net do zero", 13.88, "13,88", "cinza")], maximo=50, rotulo_w=150)
          + '<div class="sub" style="margin-top:6px">Limites de talhão (Sudeste Asiático)</div>'
          + barras([("ViT do zero", 39.20, "39,20", "cinza"), ("CROMA", 38.48, "38,48", "verde"),
                    ("U-Net do zero", 34.84, "34,84", "cinza")], maximo=50, rotulo_w=150))}
  {painel("O que pesa contra", "", tiles([
      ("Todos os rótulos", "6 de 11", "bases em que a U-Net treinada do zero fica entre as duas melhores"),
      ("América do Sul", "4%", "das bases de observação da Terra cobrem a região"),
      ("Mapas de perenes", "16 mi", "de pontos de referência nos mapas do Google, contando os de pseudoausência"),
      ("Custo e prazo", "sem fonte", "nenhuma fonte mede quanto custa montar um monitoramento com modelo de fundação")]))}
</div>
{leitura("O ganho aparece onde faltam rótulos, como em culturas com pouco histórico, mas a prova vem de conjuntos de teste de outras regiões, não de monitoramento em operação.")}""",
        fontes(("M1335", "p. 8-9, 12-15"), ("M1327", "p. 1, 27")))

    imagem_descritivo = novo(
        "Satélites e modelos de fundação · 6/8", "Satélites e modelos de fundação · quem fez e o que é aberto",
        "Os modelos de fundação de imagem: quase todos em pré-print, com abertura que varia",
        f"""<div class="col3">
  {painel("Quem fez", "", lista([
      "<b>Prithvi-EO-2.0:</b> IBM, NASA e Jülich; pesos com licença Apache 2.0.",
      "<b>AlphaEarth:</b> Google; liberou só as camadas de vetores, com licença CC-BY 4.0.",
      "<b>OlmoEarth:</b> Ai2; pesos, dados e código grátis, com licença que proíbe mineração e desmatamento.",
      "<b>TerraMind:</b> IBM e ESA; modelos e código publicados."]))}
  {painel("Com que evidência", "", lista([
      "<b>Autores:</b> cada um declara o seu modelo à frente dos outros, em pré-print.",
      "<b>Terceiros:</b> com todos os rótulos, os modelos de fundação não superaram de forma consistente as redes treinadas para a tarefa.",
      "<b>Poucas amostras:</b> com 1 a 10 por classe, os métodos ficaram perto do acaso em muitos casos, segundo os autores do AlphaEarth."]))}
  {painel("O que limita", "", lista([
      "<b>Aplicar:</b> exige coletar, alinhar, preparar e rotular dados, ajustar o modelo e rodá-lo (Ai2).",
      "<b>Pré-treino:</b> cerca de 21.000 horas de GPU no Prithvi-EO-2.0 de 300 milhões de parâmetros; o ajuste de cada tarefa usou uma GPU.",
      "<b>Viés:</b> muitos modelos vão mal em regiões pouco representadas, como a África e o Sudeste Asiático."]))}
</div>""",
        fontes(("M1341", "p. 1, 5"), ("M1364", "p. 1"), ("M1324", "p. 12, 51"), ("M1331", "p. 1, 3, 11"), ("M1357", "p. 1-2"), ("M1363", "p. 1"),
               ("M1335", "p. 1, 9, 12-15")))

    # ---- Par 4: perenes no mapa --------------------------------------------------------------------
    perenes_visual = novo(
        "Satélites e modelos de fundação · 7/8", "Satélites e modelos de fundação · culturas perenes",
        "Perenes no mapa: mapear já funciona; o resultado validado vem de modelos treinados para a tarefa",
        f"""{tiles([
      ("Palma · mapa global (2021)", "88% · 77%", "acurácia do usuário nos plantios industriais e de pequenos produtores; perde os plantios jovens"),
      ("Cacau · Costa do Marfim e Gana (2023)", "91,7%", "F1 na validação de campo às cegas; detecta plantios jovens"),
      ("Seringueira · Sudeste Asiático (2023)", "0,95 → 0,57", "acurácia do produtor, quando calculada sobre a área estimada; com Random Forest"),
      ("Café · mapas do Google (2026)", "71%", "no conjunto de seleção; sem revisão por pares; o plantio sombreado é omitido em algumas regiões"),
      ("Macaúba · drone (Embrapa, 2026)", "93% · 89%", "no teste da mesma área e numa área de 4,0 ha fora dela"),
      ("Brasil · MapBiomas", "sem acurácia", "própria para café, citros e palma; só das classes agregadas")], colunas=3)}
{leitura("Mapear a área de perenes por satélite já é viável. Prever produtividade e saúde segue em pesquisa, e não achamos estudo de macaúba por satélite.")}""",
        fontes(("M1376", "p. 1, 8"), ("M1377", "p. 3-4, 8"), ("M1379", "p. 1-2, 9-10"), ("M1327", "p. 27, 35"), ("M1381", "web"), ("M1336", "p. 1, 3, 7"),
               ("M1373", "p. 24")))

    perenes_descritivo = novo(
        "Satélites e modelos de fundação · 8/8", "Satélites e modelos de fundação · o que isso indica para perenes",
        "Para perenes: o que já é viável, o que é tendência e o que é pesquisa",
        f"""<div class="col3">
  {painel("Já viável", "", lista([
      "<b>Mapear a área</b> com imagens abertas de 10 m e validação de campo (palma, cacau, seringueira; inventários de citros e de florestas no Brasil).",
      "<b>Previsões de tempo por IA abertas,</b> ao lado das físicas, com o catálogo do ECMWF aberto; na América do Sul, desempenho não demonstrado.",
      "<b>Risco climático por cultura:</b> já existe, pelo zoneamento agroclimático, sem IA."]))}
  {painel("Tendência", "", lista([
      "<b>Modelos de fundação e vetores prontos,</b> que pedem menos rótulos.",
      "<b>Previsão por conjunto e híbrida</b> nos centros de referência.",
      "<b>Chuva das próximas horas só com satélite,</b> onde falta radar.",
      "<b>Radar aberto de banda L</b> (NISAR), que penetra melhor a vegetação densa."]))}
  {painel("Ainda pesquisa", "", lista([
      "<b>Produtividade de perenes por satélite:</b> amostras pequenas.",
      "<b>Doença e estresse hídrico:</b> validados só com drone.",
      "<b>Macaúba por imagem:</b> só com drone.",
      "<b>Previsão sazonal por IA e redução de escala até a fazenda:</b> sem operação nem teste no Brasil."])
      + '<p class="note" style="margin-top:10px">Leitura nossa, macro; não é recomendação. Nos três grupos, a dependência comum é o dado de campo para rotular e validar.</p>')}
</div>""",
        fontes(("M1376", "p. 1"), ("M1377", "p. 1, 8"), ("M1379", "p. 2, 9"), ("M348", "p. 15"), ("M1278", "p. 43"), ("M645", "p. 2"), ("M1358", "p. 2-3"),
               ("M1352", "p. 22"), ("M1277", "p. 1-2"), ("M1335", "p. 1, 12-15"), ("M1333", "p. 2"), ("M1346", "p. 2, 4-5"), ("M1366", "p. 17"),
               ("M1370", "p. 1-4"), ("M1263", "p. 6, 9-10"), ("M1232", "p. 2"), ("M1279", "p. 2-3"), ("M1336", "p. 1, 3, 7"), ("M241", "web"),
               ("M1354", "p. 1"), ("M1348", "p. 1")))

    return [tempo_visual, tempo_descritivo, brasil_visual, agro_descritivo,
            imagem_visual, imagem_descritivo, perenes_visual, perenes_descritivo]
