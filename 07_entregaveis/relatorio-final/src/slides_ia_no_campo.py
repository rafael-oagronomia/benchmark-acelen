"""Slides de resultado da nota "IA no campo" (Frente 3, itens 3.3 e 3.4) para o Report Final.

Quatro pares, cada um com um slide visual e um descritivo (pouco texto no visual, explicação no
seguinte). Os pares 5/8 a 8/8 dos sistemas autônomos (colheita da macaúba e robôs que sobem na
palmeira) estão em `slides_acrescimos.py`. Todo número vem da nota `04_frente-3_tendencias/ia-no-campo.md`, com a mesma citação;
a linha de fontes sai do catálogo. Ao mudar a nota, mudar aqui também.

Recebe as peças do gerador (novo, fontes, barras, lista) para não importar o gerador de volta.
"""
from __future__ import annotations


def slides(novo, fontes, barras, lista) -> dict[str, list[dict]]:
    def tl4(itens):
        return '<div class="tl4">' + "".join(
            f'<div class="i"><div class="d">{d}</div><div><div class="k">{k}</div><p>{p}</p></div></div>' for d, k, p in itens) + "</div>"

    def tiles(itens):
        return '<div class="tiles">' + "".join(f'<div class="tl"><div class="a">{a}</div><div class="n">{n}</div><p>{p}</p></div>' for a, n, p in itens) + "</div>"

    def painel(titulo, sub, corpo, classe="panel"):
        sub_html = f'<div class="sub">{sub}</div>' if sub else ""
        return f'<div class="{classe}"><h3>{titulo}</h3>{sub_html}{corpo}</div>'

    def leitura(texto):
        return f'<div class="read"><b>Leitura nossa.</b> {texto}</div>'

    # ---- 3.4 IA aplicada ao agro: aplicação seletiva e adoção ------------------------------------
    aplicacao_visual = novo(
        "IA aplicada ao agro · 1/4", "IA aplicada ao agro · onde a IA já entrega",
        "A IA do campo entrega na aplicação seletiva; a adoção medida ainda é baixa",
        f"""<div class="g2" style="grid-template-columns:1.1fr 1fr;margin-top:12px">
  {painel("Menos herbicida com pulverização seletiva", "Universidades dos EUA, medido por terceiro · empresas no Brasil, segundo a empresa*",
          barras([("Iowa State · 5 lavouras, média", 76, "76%", "verde"),
                  ("Arkansas · ensaio de 3 anos", 59, "43% a 59%", "verde"),
                  ("Amaggi · 7 máquinas*", 85, "85%", "ambar"),
                  ("SLC · sensores; IA não informada*", 67, "67%", "cinza")], rotulo_w=232)
          + '<div class="mini"><span class="n">+280%</span><span>ao ano de caruru no ensaio do Arkansas, quando a sensibilidade das câmeras era baixa</span></div>')}
  {painel("A adoção medida ainda é baixa", "Produtores que usam, McKinsey, abr–jul/2026",
          barras([("IA generativa · América Latina", 26, "26%", "verde"),
                  ("IA generativa · 10 países", 17, "17%", "verde"),
                  ("Automação e robótica · 7 países", 5, "5%", "ambar")], rotulo_w=232)
          + '<div class="mini"><span class="n">Brasil</span><span>nenhuma pesquisa publica o uso de IA só pelo produtor brasileiro</span></div>')}
</div>
{leitura("A IA que entrega resultado está embarcada na máquina e decide planta a planta, dentro de uma regra definida por pessoas. A IA generativa de uso geral ainda é pouco usada pelo produtor.")}""",
        fontes(("M1286", "p. 1-2"), ("M1296", "p. 2-3"), ("M321", "p. 88, 102"), ("M331", "p. 81"), ("M021", "p. 8, 24, 26")))

    aplicacao_descritivo = novo(
        "IA aplicada ao agro · 2/4", "IA aplicada ao agro · quem decide no campo",
        "O diagnóstico ficou mais rápido; a decisão segue humana, com exceções estreitas",
        f"""<div class="col3">
  {painel("Enxergar e antecipar: o diagnóstico chega antes", "", lista([
      "<b>Inventário florestal (Embrapa):</b> 1.150 ha num sobrevoo de pouco mais de 2 horas, contra 73 dias de cinco pessoas; acurácia não informada.",
      "<b>Incêndio (Raízen):</b> IA e satélite posicionam a frota de combate; 27,6% menos tempo de chegada, segundo a empresa.",
      "<b>Incêndio (Suzano):</b> câmeras com IA reconhecem a fumaça, e um operador confirma cada alerta antes de mandar a brigada."]))}
  {painel("A exceção: a máquina decide por alvo", "", lista([
      "<b>Pulverização seletiva:</b> a máquina decide planta a planta, em tempo real, dentro de uma regra definida por pessoas.",
      "<b>Colheitadeira:</b> ajusta as regulagens com sensores e IA; €70 a mais por hectare e 7,4% mais toneladas por hora, segundo a CNH.",
      "<b>O risco:</b> com sensibilidade baixa, o caruru cresceu 280% ao ano no ensaio do Arkansas."]))}
  {painel("O que ainda não existe", "", lista([
      "<b>Tempo até a decisão:</b> nenhum antes e depois publicado, nem para o mapa de falhas de plantio.",
      "<b>A cadeia inteira:</b> da imagem à máquina, só na \"catação\" da cana com drones, sem a fonte dizer se há validação humana nem se usa IA.",
      "<b>Manejo:</b> nenhuma máquina decide o manejo em operação regular (leitura nossa)."]))}
</div>
<p class="note" style="margin-top:10px">Os números das empresas são declarados por elas; os das universidades foram medidos por terceiro.</p>""",
        fontes(("M1271", "p. 1-3"), ("M329", "p. 20"), ("M769", "p. 3"), ("M321", "p. 88, 102"), ("M1296", "p. 2-3"), ("M391", "p. 2"), ("M880", "p. 56")))

    # ---- 3.4 IA aplicada ao agro: melhoramento e edição genética --------------------------------
    melhoramento_visual = novo(
        "IA aplicada ao agro · 3/4", "IA aplicada ao agro · melhoramento e edição genética",
        "No melhoramento, a IA encurta ciclos; em cultura perene, o produto editado ainda é raro",
        f"""<div class="g2" style="grid-template-columns:1fr 1.1fr;margin-top:12px">
  {painel("Quanto dura um ciclo", "", tiles([
      ("Palma", "20 anos", "por geração; simulada, a seleção genômica faz 4 ciclos em 50 anos, não 76"),
      ("Eucalipto (Suzano)", "21 → 7 anos", "clones com Speed Breeding, segundo a empresa, sem ligar a técnica à IA"),
      ("Milho (Bayer)", "4 meses", "o ciclo de geração, antes de cerca de 5 anos, segundo a empresa; ao mercado, 1 a 2 anos menos"),
      ("Macaúba", "≈ 4.000 ha", "plantados, sem cultivar comercial")]))}
  {painel("Edição genética: onde está", "", tl4([
      ("2018", "Brasil", "a CTNBio decide caso a caso; o editado sem DNA de fora pode não ser transgênico"),
      ("2025", "IA no desenho", "editores gerados por modelos de linguagem, validados em células humanas (Nature)"),
      ("fev/2026", "Eucalipto editado", "classificado como convencional pela CTNBio, segundo a Suzano; vai a testes de campo"),
      ("jun/2026", "União Europeia", "adota regras para novas técnicas genômicas, aplicáveis dois anos após a publicação")]))}
</div>
{leitura("Em perene, pesa mais o ciclo longo que a regra: no Brasil, a regulação da edição é caso a caso e mais simples que a dos transgênicos. Na macaúba, antes da edição vem a cultivar.")}""",
        fontes(("M1295", "p. 3, 6, 12"), ("M755", "p. 84"), ("M789", "p. 13-14"), ("M1256", "p. 8"), ("M1273", "p. 11-12"),
               ("M1257", "p. 1, 4"), ("M778", "p. 1-3"), ("M1255", "p. 1, 3")))

    melhoramento_descritivo = novo(
        "IA aplicada ao agro · 4/4", "IA aplicada ao agro · o que a IA faz no melhoramento",
        "A IA prevê e simula; a edição desenhada por IA ainda não chegou às perenes",
        f"""<div class="col3">
  {painel("Prever e simular", "", lista([
      "<b>Predição pelo DNA:</b> um método de aprendizado de máquina da Unicamp, com Esalq/USP, IAC e Embrapa, superou em mais de 50% a acurácia dos métodos tradicionais em gramíneas poliploides, entre elas a cana (validação cruzada, não ganho realizado).",
      "<b>Gêmeo digital (Bayer):</b> de 3 locais de teste para mais de 85 mil simulados; o ganho genético dobrado é modelado.",
      "<b>Onde está a vantagem:</b> para o chefe de P&amp;D da Bayer, nos dados que dizem o que editar e no germoplasma de elite."]))}
  {painel("Editar", "", lista([
      "<b>Editores desenhados por IA:</b> validados em células humanas (Nature, 2025) e, por um instituto público indiano, em arroz.",
      "<b>Em perene:</b> não achamos edição desenhada por IA; na palma, o relato é de edição em protoplastos, células isoladas.",
      "<b>Brasil:</b> 109 produtos reconhecidos como editados desde 2018, pela contagem obtida pelo AgFeed; a revisão acadêmica conta cerca de 63 pedidos até nov/2024, e os números não fecham."]))}
  {painel("Macaúba (pesquisa pública)", "", lista([
      "<b>Domesticação:</b> o baixo grau de domesticação é o principal gargalo para ampliar os plantios; o melhoramento está no início, com período juvenil longo.",
      "<b>Genoma:</b> um preprint de 2026, sem revisão por pares, traz o que os autores dizem ser o primeiro genoma da espécie em nível de cromossomo, com 28.215 genes previstos; não testa seleção genômica nem marcadores.",
      "<b>Colheita:</b> feita em grande parte à mão; a falta de equipamento específico é uma das principais lacunas tecnológicas da cadeia."]))}
</div>""",
        fontes(("M1258", "p. 1"), ("M789", "p. 13-14"), ("M790", "p. 28"), ("M1257", "p. 1, 4"), ("M1285", "p. 1"), ("M377", "p. 11"),
               ("M1266", "p. 1-4"), ("M1273", "p. 16"), ("M1256", "p. 7-8"), ("M1264", "p. 1-2"), ("M239", "p. 24")))

    # ---- 3.3 Sistemas autônomos: autonomia e quebras --------------------------------------------
    autonomia_visual = novo(
        "Sistemas autônomos · 1/8", "Sistemas autônomos · máquinas, robôs e drones",
        "A autonomia já é produto em nichos, com supervisão a distância, e teve quebras no caminho",
        f"""<div class="g2" style="grid-template-columns:1fr 1.1fr;margin-top:12px">
  {painel("Frotas declaradas pelos fabricantes", "Todos os números são das próprias empresas", tiles([
      ("Pomares e vinhedos (GUSS)", "250+", "pulverizadores autônomos; um operador supervisiona até oito"),
      ("Citros (Arbus, Jacto)", "16 mil h", "em cerca de 60 mil ha antes de virar produto, em abr/2026"),
      ("Lavoura (Solix)", "≈ 150 + 100", "robôs nos EUA e no Brasil, segundo a Forbes"),
      ("Preparo de solo (Deere)", "200 mil acres", "de preparo autônomo desde o início da oferta")]))}
  {painel("Quebras e recuos", "", tl4([
      ("fev/2024", "Small Robot Company", "Reino Unido: liquidação voluntária de credores; faltou capital antes da escala"),
      ("mar/2025", "FarmWise", "EUA: reestruturação e encerramento gradual, por macroeconomia e queda do capital de risco, segundo o CEO"),
      ("out/2025", "Naïo", "França: plano de cessão e, no dia seguinte, conversão do processo em liquidação judicial"),
      ("nov/2025", "Monarch", "EUA: avisos oficiais de demissão; ação de concessionária que alega autonomia aquém da vendida, sem decisão")]))}
</div>
{leitura("Nas quebras com causa declarada, o capital acabou antes da escala. Não achamos autonomia plena, sem supervisão, em operação regular.")}""",
        fontes(("M1284", "p. 1"), ("M325", "p. 2-3"), ("M253", "p. 7"), ("M868", "p. 14"), ("M1319", "p. 1"), ("M1320", "p. 2"),
               ("M1298", "p. 2"), ("M1301", "p. 1-2"), ("M1300", "p. 1"), ("M1303", "p. 10"), ("M1318", "p. 2-4")))

    autonomia_descritivo = novo(
        "Sistemas autônomos · 2/8", "Sistemas autônomos · o que trava",
        "O que trava a autonomia é o entorno e também a própria tecnologia",
        f"""<div class="col3">
  {painel("A tecnologia", "", lista([
      "<b>Percepção:</b> poeira, palha, lama e neblina dificultam padronizar os testes de detecção, segundo autores ligados a um fabricante europeu.",
      "<b>Colheita de frutas:</b> colhedoras robóticas de maçã não estão disponíveis comercialmente; eficiência, custo e confiabilidade precisam melhorar.",
      "<b>Velocidade:</b> um braço robótico de cerca de US$ 5.500 colhe uma maçã em cerca de 25 segundos (Washington State University)."]))}
  {painel("As regras", "", lista([
      "<b>Normas:</b> as que apoiariam a avaliação de risco ainda estão em desenvolvimento, segundo a associação europeia de fabricantes (nov/2025).",
      "<b>Supervisão:</b> na UE, a partir de 14/01/2027, o regulamento de máquinas cria a supervisão remota e exige avaliação por terceiro do software que aprende.",
      "<b>Reino Unido:</b> a supervisão no local o tempo todo eliminava o ganho para pequenos e médios produtores (análise citada pela FAO)."]))}
  {painel("O sinal", "", lista([
      "<b>Rede:</b> só 33,9% da área agrícola brasileira tinha 4G ou 5G em abr/2025 (Teletime).",
      "<b>Satélite no celular:</b> a oferta direta, em degustação desde 26/10/2026, é só para smartphone e veda drones e veículos autônomos sem autorização.",
      "<b>Nas máquinas:</b> o satélite chega por antena, segundo os fabricantes."]))}
</div>""",
        fontes(("M1230", "p. 3-5"), ("M376", "p. 4, 7"), ("M407", "web"), ("M1228", "p. 2"), ("M1260", "p. 49, 51, 81"), ("M183", "p. 117"),
               ("M1214", "p. 1-2"), ("M1272", "p. 2-6"), ("M863", "p. 23"), ("M391", "p. 3")))

    # ---- 3.3 Sistemas autônomos: perenes e mão de obra ------------------------------------------
    perenes_visual = novo(
        "Sistemas autônomos · 3/8", "Sistemas autônomos · culturas perenes e mão de obra",
        "Nas perenes, a falta de gente puxa a máquina; na palma, falta a solução integrada de colheita",
        f"""<div class="g2" style="margin-top:12px">
  {painel("Hectares por trabalhador na colheita da palma", "Estudo citado pelo MPOB (Malásia)",
          barras([("À mão", 21, "21 ha", "cinza"),
                  ("Cortador motorizado", 35, "35 ha", "ambar"),
                  ("Colhedora de médio porte", 86, "86 ha", "verde")], rotulo_w=200)
          + '<div class="mini"><span class="n">60% · 50%</span><span>da força de trabalho e do custo de produção da palma estão na colheita</span></div>')}
  {painel("Brasil: a principal resposta à falta de mão de obra", "CNA/Cepea, 2026, no agro em geral; amostra não informada",
          barras([("Mecanização", 26, "26%", "verde"),
                  ("Automação ou tecnologias digitais", 8.7, "8,7%", "ambar")], rotulo_w=232)
          + '<div class="mini"><span class="n">94,8%</span><span>dos produtores relatam dificuldade para contratar</span></div>')}
</div>
{leitura("A falta de gente é o motor declarado, mas a resposta é mais mecanização que IA. Na macaúba, antes da máquina vem a cultivar.")}""",
        fontes(("M377", "p. 11-12"), ("M1234", "p. 1"), ("M1268", "p. 14"), ("M245", "p. 2")))

    perenes_descritivo = novo(
        "Sistemas autônomos · 4/8", "Sistemas autônomos · perene por perene",
        "Perene por perene: o que já existe e o que falta",
        f"""<div class="col3">
  {painel("Palma", "", lista([
      "<b>Colheita:</b> em 2023, a Sime Darby Plantation escreveu que nenhuma plantação tinha conseguido mecanizar a colheita; em 2026, o MPOB chama a solução integrada de \"lacuna-chave\".",
      "<b>Fora da colheita:</b> drones substituíram mais de 100 trabalhadores na pulverização de viveiros (Sime Darby Plantation, 2022, segundo a empresa).",
      "<b>Imagem:</b> mais de 96% das palmeiras detectadas por satélite; nas não sadias, o acerto cai para 57%."]))}
  {painel("Café, citros e florestal", "", lista([
      "<b>Café:</b> acima de 101 ha, todos usam colhedora; a mão de obra passa de 40% do custo onde a colheita é manual e fica abaixo de 10% onde é mecanizada.",
      "<b>Citros:</b> quem mecanizar a colheita \"terá de mudar o pomar\" (Fundecitrus); na Flórida, a pesquisa de colheita mecânica parou por volta de 2013.",
      "<b>Florestal:</b> a Klabin estima mais da metade do manejo da silvicultura mecanizado no fim de 2026, pela falta de mão de obra rural."]))}
  {painel("Macaúba (pesquisa pública)", "", lista([
      "<b>Domesticação:</b> cerca de 4.000 ha plantados de sementes de populações naturais, sem cultivar comercial.",
      "<b>Colheita:</b> em grande parte à mão; faltam equipamentos específicos.",
      "<b>O que já se testou:</b> um colhedor por vibração com 97,4% de eficiência para cachos até cerca de 4 m (2018); identificação de plantas por drone e IA com 98% de acerto médio (pesquisa)."]))}
</div>""",
        fontes(("M383", "p. 7"), ("M1288", "p. 5-6"), ("M384", "p. 3-4"), ("M1236", "p. 4-5"), ("M1232", "p. 2, 5"), ("M1267", "p. 3, 5-7"),
               ("M1269", "p. 2-3"), ("M1282", "p. 2, 20"), ("M1297", "p. 2"), ("M326", "p. 15"), ("M1256", "p. 8"), ("M239", "p. 24"),
               ("M1265", "p. 2, 6, 9, 11-12"), ("M241", "web")))

    return {
        "autonomos": [autonomia_visual, autonomia_descritivo, perenes_visual, perenes_descritivo],
        "agro": [aplicacao_visual, aplicacao_descritivo, melhoramento_visual, melhoramento_descritivo],
    }
