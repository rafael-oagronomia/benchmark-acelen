"""Slides de resultado acrescentados ao Report Final em 23/11/2026, a pedido do Guilherme:

- caso iFood (Frente 3, custo de uso da IA): um slide, com o gráfico redesenhado a partir dos números
  publicados pelo CEO (M1382); nota `04_frente-3_tendencias/custo-da-ia.md`, seção 5;
- colheita da macaúba e risco de trabalho, e robôs que sobem na palmeira (Frente 3, sistemas autônomos):
  dois pares, cada um com um slide visual e um descritivo; nota `04_frente-3_tendencias/ia-no-campo.md`,
  seção 7.4.

Todo número vem da nota, com a mesma citação. Ao mudar a nota, mudar aqui e na apresentação executiva.
Os gráficos são os da apresentação executiva (`workshop-executivo/src/graficos.py`). Recebe as peças do
gerador (novo, fontes, lista) para não importar o gerador de volta.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "workshop-executivo" / "src"))
import graficos as g  # noqa: E402


def slides(novo, fontes, lista) -> dict[str, list[dict]]:
    def painel(titulo, sub, corpo, classe="panel"):
        sub_html = f'<div class="sub">{sub}</div>' if sub else ""
        return f'<div class="{classe}"><h3>{titulo}</h3>{sub_html}{corpo}</div>'

    def leitura(texto):
        return f'<div class="read"><b>Leitura nossa.</b> {texto}</div>'

    def tiles(itens):
        return '<div class="tiles">' + "".join(f'<div class="tl"><div class="a">{a}</div><div class="n">{n}</div><p>{p}</p></div>' for a, n, p in itens) + "</div>"

    def faixa(itens):
        return '<div class="f4">' + "".join(f'<div class="i"><div class="n">{n}</div><div class="t">{t}</div></div>' for n, t in itens) + "</div>"

    # ---- Custo de uso da IA: caso iFood ----------------------------------------------------------
    # Só os dois rótulos finais são publicados; os pontos intermediários foram lidos no gráfico da publicação.
    tokens = [(0, 7), (1, 9), (2, 12), (3, 13), (3.6, 22), (4, 45), (4.5, 80), (5, 113), (6, 150), (7, 172), (8, 190), (8.85, 206)]
    custo = [(0, 11), (1, 13), (2, 17), (3, 20), (3.6, 45), (4, 85), (4.35, 105), (5, 100), (6, 101), (6.5, 85), (7, 62), (8, 54), (8.85, 49)]

    def etapa(n, rotulo, texto, classe=""):
        return f'<div class="r {classe}"><div class="bd">{n}</div><div><div class="rt">{rotulo}</div><p>{texto}</p></div></div>'

    ifood = novo(
        "Custo de uso da IA", "Custo de uso da IA · caso iFood · Frentes 1 e 3",
        "iFood: o uso de IA dobrou e a conta caiu pela metade, sem limitar o acesso",
        '<div class="g2" style="grid-template-columns:1.25fr 1fr;margin-top:12px">'
        + painel("A \"boca de jacaré\": os tokens sobem, o custo cai",
                 "Índices sem base informada; curvas redesenhadas a partir do gráfico da publicação, com valores intermediários aproximados",
                 g.duas_linhas(tokens, custo, ["fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out"],
                               [(3.6, "Bootcamp de IA", ""), (6, "Plataforma própria:", "modelos abertos como padrão")],
                               ("+106%", "tokens, desde junho"), ("−51%", "custo, desde junho"), altura=292)
                 + '<div class="lg"><span style="--c:#62A842">tokens consumidos</span><span style="--c:#B88A28">custo</span>'
                   '<span class="sd">De janeiro a abril: primeiros usuários.</span></div>')
        + '<div class="fv">'
        + etapa(1, "Problema", "<b>IA agêntica para todos</b> os colaboradores: no começo, o uso cresceu e a conta também.")
        + etapa(2, "Iniciativa", "<b>\"Nossa resposta não foi limitar o acesso\",</b> diz o CEO. Modelos abertos viraram o padrão numa plataforma própria; os premium ficaram para as tarefas que os justificam, com orçamento definido.")
        + etapa(3, "Resultado", "<b>Tokens 106% maiores e conta 51% menor</b> desde junho de 2026.", "res")
        + etapa(4, "Consequência", "<b>8 em cada 10 tokens</b> rodam em modelos abertos, e todos seguem com tokens ilimitados.")
        + etapa(5, "Lição", "<b>O modelo do tamanho da tarefa:</b> a conta cai quando o modelo mais caro deixa de ser o padrão (leitura nossa).")
        + "</div></div>"
        + faixa([("30×", "mais <b>uso de IA</b> desde janeiro de 2026"),
                 ("7×", "mais uso <b>por pessoa</b> desde janeiro"),
                 ("−86%", "no <b>custo por token</b> desde janeiro"),
                 ("", "<b>Como ler.</b> Números declarados pelo CEO numa rede social, sem valores em moeda e sem verificação de terceiros.")]),
        fontes(("M1382", "web")))

    # ---- Sistemas autônomos: colheita da macaúba e risco de trabalho -----------------------------
    colheita_visual = novo(
        "Sistemas autônomos · 5/8", "Sistemas autônomos · colheita da macaúba e segurança do trabalho",
        "Macaúba: a colheita depende de gente; o risco é descrito, mas não foi medido",
        '<div class="g2" style="grid-template-columns:1.25fr 1fr;margin-top:12px">'
        + painel("A altura do problema: até onde cada ferramenta alcança",
                 "Em metros, segundo quem desenvolveu ou testou cada uma · faixa verde: estipe da macaúba adulta",
                 g.alcance([("Colhedor|vibratório|(macaúba)", None, 4, "4 m", "verde"),
                            ("Cortador|motorizado|(palma)", 4.5, 6, "6 m", "cinza"),
                            ("Vara com|foice,|tradicional", 8, 10, "8 a 10 m", "cinza"),
                            ("Robôs de|coqueiro,|em teste", 13.42, 15.2, "15,2 m", "ambar"),
                            ("Vara de|alumínio|(INPA)", None, 19.2, "19,2 m", "cinza"),
                            ("Robô do|açaí,|à venda", None, None, "?", "ambar")],
                           (15, 20, "Macaúba adulta", "estipe de 15 a 20 m, com espinhos"), altura=222)
                 + '<p class="note" style="font-size:11px">No plantio, a planta é mais baixa: média de até 7 m aos 7 anos, da base à folha mais nova, em experimento da Embrapa. '
                   'Nenhuma fonte mede a altura do cacho; a do robô do açaí não é informada.</p>')
        + painel("O risco de trabalho tem número só nos análogos", "% dos trabalhadores, por autorrelato; açaí e coco são colhidos por escalada", tiles([
            ("Açaí · Ilha do Combu (PA)", "90%", "de 33 coletores já caíram do açaizeiro"),
            ("Coco · sul da Índia", "35,5%", "de 220 escaladores já caíram do coqueiro"),
            ("Palma · três estudos", "78–93%", "com distúrbio osteomuscular em 12 meses"),
            ("Macaúba", "sem dado", "nenhum número de acidente nem estudo ergonômico achado")]))
        + "</div>"
        + leitura("Confirma-se a dependência de gente; o risco é descrito, sem número. Queda é dado de culturas colhidas por escalada; a macaúba, com espinhos no estipe, se colhe do chão."),
        fontes(("M1265", "p. 9"), ("M1385", "p. 2"), ("M1422", "web"), ("M1418", "p. 12"), ("M1383", "web"), ("M1388", "web"), ("M1400", "web"),
               ("M1277", "p. 1"), ("M1256", "p. 6"), ("M1417", "p. 13-15"), ("M1410", "web"), ("M1407", "web"), ("M1411", "web")))

    colheita_descritivo = novo(
        "Sistemas autônomos · 6/8", "Sistemas autônomos · como se colhe e qual é o risco",
        "Colhe-se do chão ou com foice em vara; o risco de trabalho ainda não tem número",
        f"""<div class="col3">
  {painel("Como se colhe hoje", "", lista([
      "<b>Do chão:</b> no extrativismo, a maior parte dos frutos é apanhada no solo, depois da queda natural, o que traz problemas de qualidade (autores citados pela Embrapa Cerrados).",
      "<b>Com vara:</b> foice em vara corta o cacho, aparado em rede; artigos da UFV e da UFLA de 2017 a 2021 dizem que não há máquina no mercado.",
      "<b>Cacho inteiro:</b> em estudo preliminar da Embrapa Cerrados, colher o cacho inteiro, aos primeiros sinais de queda, não mudou o conteúdo de óleo.",
      "<b>Rendimento:</b> o único número, 37,5 kg por hora, é estimativa; não achamos custo da colheita nem descrição dos plantios comerciais."]))}
  {painel("O risco, na macaúba", "", lista([
      "<b>Descrito:</b> para o INPA, a coleta em palmeiras é trabalho sob risco constante de acidentes e exaustão; com espinhos, as varas improvisadas são difíceis, exaustivas e arriscadas.",
      "<b>Esforço:</b> no primeiro teste do colhedor da UFV, o cabeçote de 3,97 kg na ponta da haste comprometeu o trabalho por fadiga do operador.",
      "<b>Norma:</b> na NR-31, as medidas contra queda na colheita vão no programa de riscos da propriedade, com capacitação de no mínimo 2 horas; a leitura jurídica cabe a especialista.",
      "<b>Sem número:</b> não achamos acidente registrado nem estudo ergonômico da colheita da macaúba."]))}
  {painel("Nos análogos, o risco tem número", "", lista([
      "<b>Açaí (escalada):</b> 90% de 33 extrativistas já tinham caído do açaizeiro, na Ilha do Combu (PA).",
      "<b>Coco (escalada):</b> 35,5% dos escaladores (78 de 220) já tinham caído, no sul da Índia.",
      "<b>Palma (do chão, com vara longa):</b> de 78,0% a 93,0% com distúrbio osteomuscular em 12 meses, nos três estudos que mediram; cacho de 10 a 50 kg.",
      "<b>Leitura nossa:</b> são dados autorrelatados e não se transferem como taxa. O análogo mais próximo é a palma, colhida do chão."]))}
</div>""",
        fontes(("M1395", "p. 8, 10, 19"), ("M1390", "web"), ("M1387", "web"), ("M1265", "p. 3, 5, 11"), ("M1418", "p. 9, 11"), ("M1422", "web"),
               ("M1420", "p. 44-46"), ("M1410", "web"), ("M1407", "web"), ("M1411", "web"), ("M1408", "web")))

    # ---- Sistemas autônomos: robôs que sobem na palmeira ----------------------------------------
    def estagio(icone, nome, texto, pontos, fim=False):
        f = " fim" if fim else ""
        celulas = "".join(f'<div class="pt{f}"><span class="{"on" if p else ""}"></span></div>' for p in pontos)
        return (f'<div class="{f.strip()}"><i data-lucide="{icone}" class="ic"></i></div>'
                f'<div class="nm{f}"><b>{nome}</b><span>{texto}</span></div>{celulas}')

    robos_visual = novo(
        "Sistemas autônomos · 7/8", "Sistemas autônomos · robôs que sobem na palmeira e cortam o cacho",
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
        + painel("O caso público do açaí: AçaíBot", "Sobe, serra o cacho e o traz ao operador · caso público, não recomendação", tiles([
            ("Peso, segundo a empresa", "8,5 kg", "na página do produto; 8 kg em notícia da própria empresa"),
            ("Preço na loja da empresa", "R$ 22,9 mil", "em 23/11/2026, na página do produto"),
            ("Compra pública no Amapá", "44 robôs", "por R$ 1,01 milhão, em contratação direta (Diário Oficial, 08/05/2026)"),
            ("Ensaio independente", "0", "achados; os ganhos declarados vão de \"até 180%\" a \"10 vezes\"")]))
        + "</div>"
        + leitura("O robô escalador saiu do laboratório no açaí, por controle remoto e sem ganho medido por terceiro. Na macaúba, o que tem medição vem do chão."),
        fontes(("M1400", "web"), ("M1401", "web"), ("M1399", "p. 1"), ("M1391", "web"), ("M1392", "p. 2, 5"), ("M1383", "web"), ("M1388", "web"),
               ("M1389", "web"), ("M1404", "web"), ("M1385", "p. 3, 8"), ("M1256", "p. 6")))

    robos_descritivo = novo(
        "Sistemas autônomos · 8/8", "Sistemas autônomos · o que se sabe de cada robô",
        "O robô do açaí vende sem ensaio independente; no coco e na palma, o limite é a subida",
        f"""<div class="col3">
  {painel("Açaí: produto à venda", "", lista([
      "<b>AçaíBot:</b> por controle remoto, sobe na palmeira e traz o cacho ao operador; 8,5 kg e R$ 22.907,41 na página do produto, em 23/11/2026.",
      "<b>Compra pública:</b> o governo do Amapá contratou 44 unidades por R$ 1.010.000,00 e abriu edital para doá-las a entidades da cadeia do açaí.",
      "<b>Ganhos:</b> \"10 vezes\" para a empresa, \"até 180%\" na notícia do prêmio da CNI; não achamos ensaio independente. A IA aparece só nessa notícia.",
      "<b>Outro coletor:</b> protótipo criado com comunidades do Pará, em projeto do MDA com a Embrapa; os extrativistas veem os robôs autônomos como inviáveis no dia a dia, pelo preço."]))}
  {painel("Coco, tâmara e palma", "", lista([
      "<b>Coco, Índia:</b> o robô subiu até 15,2 m; no teste de campo, levou 21,9 minutos por coqueiro, e o colhedor, 11,8 (IEEE Spectrum).",
      "<b>Coco, China:</b> subiu até 13,42 m; em 10 coqueiros, 152,3 s para subir e 222,1 s para colher.",
      "<b>Tâmara:</b> um artigo de 2026 mede só a subida; um sistema com IA foi anunciado em 2025, sem resultado.",
      "<b>Palma:</b> a subida ainda não é confiável, e a revisão de 2024 lista cinco travas. Do chão, o cortador motorizado levou a colheita de 4,19 para 11,60 t de cachos por dia."]))}
  {painel("Macaúba", "", lista([
      "<b>Nenhum robô:</b> não achamos robô, escalador, plataforma ou drone de colheita, em artigo, patente ou notícia.",
      "<b>O que existe:</b> um colhedor vibratório portátil da UFV, com 434,09 kg por hora e 94,1% de eficiência, medidos pelos inventores; dano leve em 15,27% dos frutos e grave em 10,61%.",
      "<b>O obstáculo:</b> o estipe tem espinhos e restos de bainha; na palma, os escaladores só sobem troncos lisos. Não achamos teste (leitura nossa).",
      "<b>O que falta medir:</b> quanto se colhe por pessoa, a que altura fica o cacho no plantio e quantos acidentes há."]))}
</div>""",
        fontes(("M1400", "web"), ("M1399", "p. 1"), ("M1397", "web"), ("M1391", "web"), ("M1392", "p. 2-5"), ("M1383", "web"), ("M1403", "web"),
               ("M1388", "web"), ("M1389", "web"), ("M1404", "web"), ("M1385", "p. 2, 3, 16"), ("M1386", "web"), ("M1256", "p. 6")))

    return {"custo": [ifood], "colheita": [colheita_visual, colheita_descritivo, robos_visual, robos_descritivo]}
