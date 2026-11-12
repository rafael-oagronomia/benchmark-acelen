# Linha de investigação — Satélites e modelos de fundação: imagem e clima

> Documento de trabalho da OagronomIA · Frente 3 — Tendências e perspectivas futuras · Aberto em 11/11/2026 · Protocolo do tema e estrutura da nota temática. Fica fora do assistente de IA (linha de investigação). Número novo só entra na nota depois de verificado e catalogado.

## 1. Por que o tema entra

- **Pedido do Guilherme (11/11/2026):** incluir nas tendências os satélites, em especial os modelos de fundação, tanto para imagem quanto para clima. A tese é que esse é um ponto que pode mostrar onde olhar a uma empresa de cultura perene.
- **Está no escopo** ([README da Frente 3](README.md)):
  - IA aplicada ao agro: sensoriamento remoto, modelos preditivos e apoio à decisão agronômica;
  - dados e soberania tecnológica: quem controla os modelos e os dados, e a dependência de fornecedores.
- **Completa a nota [IA no campo](ia-no-campo.md).** Ela mostrou que, nas perenes, a IA de imagem ainda está quase toda em pesquisa:
  - a detecção de palmeiras passa de 96%, mas o acerto nas plantas não sadias fica em 57%;
  - a previsão de produtividade do café por satélite vem de amostra pequena.

  A nota tratou o satélite como conexão (hipótese H4) e não olhou os modelos de imagem e de clima.
- **O que é um modelo de fundação**, para esta nota: um modelo grande, treinado com muitos dados sem rótulo (imagens de satélite ou dados de tempo e clima) e depois adaptado a várias tarefas com poucos dados rotulados. Nos modelos de tempo, entram também os modelos de IA que fazem a previsão no lugar ou ao lado da previsão numérica tradicional.
- **Escopo.** Macro e de mercado: o que existe, quem faz, o que está em operação, com que evidência e o que isso indica para culturas perenes. A nota não avalia nem recomenda modelo, plataforma ou fornecedor. Também não desenha o monitoramento da Acelen (regra do projeto). Modelos e empresas entram como caso público, rotulados.

## 2. O que o acervo já tem

| Bloco | IDs no catálogo (ponto de partida, a reler na página) |
|---|---|
| Satélite no agro, empresas brasileiras | M365 (Amaggi com Planet), M363 (Amaggi, data lake de imagens; bloqueado), M749 (Suzano, mapeamento de 500 milhões de ha com Google Earth Engine), M754 (Suzano e Marvin), M331 (SLC, prescrição por satélite), M321 (Amaggi) |
| Satélite em perenes | M348 (Fundecitrus, inventário por satélite), M1278 (inventário florestal de SC por imagem), M1263 (café com PlanetScope), M1279 (café, monitoramento hídrico), M1309 (palma, produtividade por aprendizado de máquina), M1236 e M1232 (palma, detecção e saúde por imagem) |
| Macaúba e clima | M1277 (zoneamento de risco climático da macaúba, 2024), M1256 (revisão sobre a macaúba) |
| IA de tempo e clima | M645 (previsões de IA do ECMWF entram em operação, 25/02/2025); M640, M585 e M638 (IA e clima, visão geral) |

## 3. Perguntas centrais

1. **O que são e quem faz.** Que modelos de fundação de observação da Terra (imagem) e de tempo e clima existem, quem os publicou, quais são abertos (código, pesos, licença) e quais estão em operação de 2023 a 2026?
2. **A evidência.** Qual o desempenho medido em artigo revisado por pares e em comparação com os métodos tradicionais? E nos trópicos e na América do Sul?
3. **No agro, com resultado.** Para que servem: mapeamento de culturas e de plantios, limites de talhão, fenologia, estimativa de produtividade, estresse hídrico, doenças, incêndio e carbono. O que existe em perenes (palma, café, citros, eucalipto, cacau, seringueira)?
4. **Tempo e clima por IA no agro.** Do prazo de horas ao sazonal: quais serviços meteorológicos já usam (ECMWF, NOAA, INMET, Inpe), como se leva a previsão à escala da fazenda (redução de escala) e onde entra no zoneamento de risco, no seguro e no planejamento de safra.
5. **Os dados.** Que satélites e resoluções servem às perenes (a copa de cada planta ou o talhão inteiro)? Que revisita? E as nuvens nos trópicos e o radar? Que satélites brasileiros existem (CBERS, Amazonia-1)? Quanto custa e o que é aberto ou comercial?
6. **Brasil.** Quem já usa: Embrapa, Inpe, MapBiomas, empresas e startups. O que existe sobre palmeiras nativas e plantadas, inclusive a macaúba, pela pesquisa pública?
7. **Limites e riscos.** Validação em campo, viés regional, licença de uso, custo de computação e dependência de grandes empresas de tecnologia (soberania).

## 4. Hipóteses de partida

A tese vem do Guilherme (11/11/2026): satélites e modelos de fundação, de imagem e de clima, são um ponto que pode mostrar a uma empresa de cultura perene onde olhar. As hipóteses abaixo desdobram a tese para testar, não para afirmar.

| # | Hipótese | O que confirmaria ou derrubaria |
|---|---|---|
| H1 | **Os modelos de fundação de imagem baratearam montar um monitoramento:** uma base serve a várias tarefas com poucos rótulos de campo. Isso interessa a culturas com pouco histórico, como uma perene em domesticação | Resultados com poucos rótulos frente a modelos treinados do zero; casos de uso no agro com custo ou tempo de desenvolvimento |
| H2 | **Os modelos de tempo por IA já igualam ou superam a previsão numérica tradicional** em métricas globais e estão em operação em centros de referência | Artigos revisados com comparação; datas de entrada em operação; limitações declaradas (extremos, consistência física) |
| H3 | **Nas perenes, satélite com IA já serve para mapear, acompanhar o ciclo e o risco climático; prever produtividade e saúde planta a planta ainda é fraco** | Casos com acurácia e escala em palma, café, citros, eucalipto e cacau; separação entre mapeamento, monitoramento e previsão |
| H4 | **O ganho nos trópicos e no Brasil ainda não está demonstrado**, por falta de dado de campo e de validação regional | Avaliações em regiões tropicais e na América do Sul; uso por instituições brasileiras |
| H5 | **Modelos e dados abertos diminuem a dependência de fornecedores**, mas o processamento e os melhores dados comerciais seguem concentrados | Licenças dos modelos; dados abertos (Sentinel, Landsat, CBERS) contra comerciais; quem roda os modelos |

## 5. Estrutura proposta da nota temática

Arquivo: `04_frente-3_tendencias/satelites-e-modelos-de-fundacao.md`. Entra no assistente: incluir `E-satelites-e-modelos-de-fundacao` em `liberados` no `config/acervo.json` do RAG. Mesmo formato das demais notas: citação [M###, p. N], "leitura nossa", números que não devem ser usados e lacunas.

1. **Resumo em uma página.**
2. **Como ler.** O que é um modelo de fundação; aberto e fechado; classes de evidência; anúncio não é resultado.
3. **Modelos de fundação de imagem.** Quem fez, o que é aberto, para que serve, com que evidência.
4. **IA no tempo e no clima.** Os modelos, o que entrou em operação, o desempenho, os limites e os trópicos.
5. **Do modelo ao campo.** Aplicações no agro com resultado, por cultura, com destaque para as perenes. Tabela com resultado, escopo, classe e fonte.
6. **Os dados.** Satélites e resoluções para perenes; nuvens e radar; satélites brasileiros; aberto e comercial.
7. **Brasil.** Quem usa e o que existe, inclusive sobre palmeiras e macaúba.
8. **O que isso indica para culturas perenes** (leitura nossa, macro): o que é viável hoje, o que é tendência e o que ainda é pesquisa, sem desenhar solução.
9. **O que as hipóteses de partida mostraram.**
10. **Leitura para o estudo.**
11. **Números que não devem ser usados (ou só com ressalva); Lacunas; Fontes.**

**Regras desta nota:**
- referência de mercado e de pesquisa, nunca desenho do monitoramento da Acelen;
- não avalia nem recomenda modelo, plataforma ou fornecedor: entram só como caso público, rotulados;
- desempenho declarado por quem fez o modelo é marcado como tal;
- nada das sessões executivas nem das reuniões;
- a macaúba entra pela pesquisa pública sobre a cultura.

## 6. Fontes a levantar (rodada 12 do catálogo)

**A. Imagem: modelos de fundação de observação da Terra e aplicações**
- Os modelos e os artigos que os descrevem, com a licença de uso: de agências espaciais com empresas de tecnologia, de grandes empresas de tecnologia e de iniciativas abertas (2023 a 2026).
- Avaliações comparativas publicadas (conjuntos de teste para observação da Terra).
- Aplicações no agro com resultado: tipo de cultura, limites de talhão, altura de copa, produtividade, estresse hídrico, doença, incêndio; mapeamentos globais de plantios perenes (palma, cacau, café, seringueira, eucalipto).
- Brasil: MapBiomas (classes de culturas perenes e método), Inpe, Embrapa, empresas; satélites brasileiros (CBERS, Amazonia-1) e acesso aos dados; mosaicos e imagens comerciais abertos aos trópicos.

**B. Tempo e clima: modelos de IA**
- Os modelos de previsão por IA e os artigos (2022 a 2026), com o desempenho frente à previsão numérica tradicional e os limites declarados (extremos, consistência física, dependência de reanálise).
- Entrada em operação em centros meteorológicos e o que a Organização Meteorológica Mundial diz sobre isso.
- Desempenho nos trópicos e na América do Sul; previsão sazonal; redução de escala para a fazenda.
- Brasil: INMET, Inpe/CPTEC, Embrapa (zoneamento de risco), seguro rural; aplicações no agro com resultado.

**Regras das buscas** (as do método, seção 9 do descritivo):
- nunca citar a Acelen nem o projeto;
- só fontes oficiais ou primárias (artigo científico, agência, empresa sobre o próprio modelo, marcado como tal); imprensa serve para localizar ou entra marcada;
- cada documento com link, organização e data, e cada número com a página de onde saiu;
- documento que pede cadastro: registrar o formulário para a equipe decidir, sem preencher;
- sem contornar login nem paywall.

## 7. Como será feito

Mesmo caminho da nota IA no campo:
1. **Pesquisadores** (dois agentes, A e B, um por bloco da seção 6) gravam `_triagem-pesquisa/_dossies/_bruto_satelite_X.json`.
2. **Pré-checagem** por programa (`_ferramentas/prechecar_dossie.py`).
3. **Verificadores**, outros agentes, gravam `_verificado_satelite_X.json`.
4. **Catálogo:** as fontes novas entram na `rodada12.json` (`_ferramentas/dossies_para_rodada.py`), e a consolidação dá os IDs; o dossiê do tema sai com `_ferramentas/juntar_dossie.py`.
5. **Redator,** outro agente, escreve a nota só com o que passou pela verificação.
6. **Revisor,** outro agente, lê a nota tentando derrubá-la; o redator aplica.
7. **Conferência linha a linha** por programa (`_ferramentas/conferir_nota.py`), registro das fontes citadas e pipelines do sistema.
8. **Report Final:** slides de resultado, em pares de slide visual e descritivo, quando a nota estiver aprovada.

## Fontes
<!-- fontes:inicio -->
<!-- fontes:fim -->
