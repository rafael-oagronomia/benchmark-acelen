# Linha de investigação — Custo de uso da IA

> Documento de trabalho da OagronomIA · Frente 3 — Tendências e perspectivas futuras · Aberto em 14/10/2026 · Protocolo de pesquisa do tema. Os números novos só entram na nota temática depois de verificados e catalogados.

## 1. Por que o tema entra no estudo

- **O custo entra no retorno.** O retorno da IA é valor dividido por custo. A nota [Valor e retorno da IA](../02_frente-1_benchmark-estrategico/notas/valor-e-retorno-da-ia.md) cobre o numerador; falta o denominador.
- **O roteiro precisa de orçamento.** Um roadmap de IA (Frente 2) precisa prever quanto custa usar IA em escala e como controlar o gasto.
- **Está no escopo.** A Frente 3 cobre movimentos de mercado, IA generativa e modelos operacionais, dependência de fornecedores e riscos. O tema fica em nível macro: preços aparecem como dado de mercado, sem comparar nem recomendar ferramentas.
- **O mercado já se preocupa.**
  - 82% dos executivos se preocupam com o uso e o custo de tokens, e só 64% monitoram o consumo com limite de orçamento [M070, p. 1-2].
  - Cerca de 20% dizem que os custos de operação da IA, tokens inclusive, já restringiram o uso [M028, p. 3].
  - Para a Gartner, até 2028, 60% das 500 maiores empresas do mundo terão controles de gasto na inferência [M659, web].

## 2. Pergunta central

**O custo de usar IA vai deixar de ser preocupação para quem planeja a estratégia de IA de uma grande agroindústria?**

## 3. Hipótese de partida

A IA ficou cara e depois começou a baratear. A sequência:

1. O ChatGPT chega no fim de 2022 e surgem novas empresas de modelos.
2. Com o Claude e os modelos seguintes, o custo vira tema.
3. O DeepSeek derruba os preços, e surge o movimento chinês.
4. O Uber gasta em quatro meses o orçamento do ano.
5. O Jev derruba ainda mais o preço.

**Paralelo com os carros.** As montadoras chinesas entregam qualidade alta por preço muito menor e obrigam as outras a baixar o preço; a Hilux, por exemplo, teve desconto perto de R$ 60 mil. O mercado de IA se ajustaria do mesmo jeito.

**Conclusão da hipótese.** O preço da IA não deve ser tanta preocupação, porque o preço do token vem caindo ao longo do tempo.

**O que já sustenta a hipótese.** O custo para obter o desempenho do GPT-3.5 caiu de US$ 20 para US$ 0,07 por milhão de tokens entre nov/2022 e out/2024. É uma queda de mais de 280 vezes. Conforme a tarefa, os preços caíram de 9 a 900 vezes por ano [M230, p. 5, 65].

## 4. Hipóteses concorrentes (o que pode desmentir ou matizar)

| # | Hipótese | Sinais já no catálogo | O que confirmaria |
|---|---|---|---|
| H2 | **O preço cai, mas a conta sobe** (paradoxo de Jevons): a tarefa passa a consumir mais tokens (modelos de raciocínio, agentes) e o uso cresce mais rápido do que o preço cai | Tokens processados por mês pelo Google: de cerca de 480 trilhões em 2025 para mais de 3,2 quatrilhões em mai/2026, 7 vezes em um ano [M666, web]. Na Microsoft, o custo por token caiu mais da metade e o volume de tokens subiu 5 vezes [M701, web]. O consumo de tokens de raciocínio por empresa subiu 320 vezes em 12 meses [M170, p. 3, 6]. A energia por tarefa vai de 0,05 Wh num modelo médio a 50 Wh num agente com raciocínio [M514, p. 29] | Gasto total das empresas com IA subindo mais rápido que o volume de valor; casos de estouro de orçamento (Uber) |
| H3 | **A queda é desigual:** a capacidade de ontem barateia muito, a de ponta barateia menos, e modelos da faixa barata às vezes sobem de preço quando melhoram | A queda varia de 9 a 900 vezes por ano conforme a tarefa [M230, p. 65] | Séries de preço por faixa (ponta, intermediária, econômica); reajustes para cima |
| H4 | **O preço está abaixo do custo:** guerra de preços financiada por capital, com piso de energia, chips e data centers. Pode haver reajuste ou fim de planos de uso ilimitado | Laboratório se comprometendo a cobrir o aumento da conta de luz causado por seus data centers [M630, p. 2] | Resultado financeiro dos laboratórios; limites de uso e mudança de cobrança em 2025–2026 |
| H5 | **O token é a menor parte da conta:** integração, dados, pessoas e governança pesam mais | Para cada US$ 1 gasto em tecnologia, US$ 4 vão para pessoas e processos [M003, p. 53] | Composição do custo total de projetos de IA |
| H6 | **O Brasil tem custo próprio:** câmbio, tributos sobre serviço importado, preço de nuvem no país e incentivos a data centers | Lei do Redata [M196, p. 1; M603] | Carga tributária sobre software e nuvem importados; preço de nuvem em região brasileira |
| H7 | **O mais barato pode não ser utilizável:** restrições de segurança e soberania para modelos de certas origens; modelo aberto rodando em casa troca o preço do token pelo custo de infraestrutura | Avaliações do governo americano sobre os modelos DeepSeek [M853; M852] | Políticas de empresas e governos sobre modelos de origem chinesa |

**Leitura preliminar (a confirmar).** Os sinais do catálogo apontam para duas curvas ao mesmo tempo: o preço por token cai rápido, e o consumo cresce mais rápido ainda. Se isso se confirmar, a mensagem para o planejamento não é "o custo não importa". É "o preço unitário não deve travar a IA; o que precisa de gestão é o consumo e o que ele entrega".

## 5. Linha do tempo a reconstruir

Cada marco precisa de fonte primária com data: página oficial de preços, anúncio de lançamento, artigo técnico ou documento regulatório. A imprensa serve para localizar o marco ou como fonte secundária marcada. As pistas abaixo ainda não foram verificadas.

| Período | Marco | O que conferir |
|---|---|---|
| nov/2022 | ChatGPT; preço da API da época | Preço por mil tokens dos modelos então disponíveis |
| mar/2023 | Nova API de conversa, cerca de 10 vezes mais barata que a anterior; GPT-4 caro; lançamento do Claude | Preços de lançamento |
| 2023–2024 | Novos entrantes (Anthropic, Google, Mistral, Meta com pesos abertos) e cortes sucessivos dos modelos de ponta e das versões econômicas | Série de preços por faixa |
| mai/2024 | DeepSeek-V2 e guerra de preços na China, com cortes de grandes empresas chinesas. O "movimento chinês" começa antes do R1 | Preço do V2; cortes anunciados na China |
| set/2024 | Primeiros modelos de raciocínio: mais tokens por tarefa | Preço e cobrança dos tokens de raciocínio |
| dez/2024–jan/2025 | DeepSeek-V3 e R1; preço do R1 contra o do modelo de raciocínio americano equivalente; queda de valor de mercado de fabricantes de chips | Preços oficiais; custo de treino declarado (só a rodada final, número que não deve ser usado sem ressalva) |
| 2025 | Onda de modelos abertos chineses [M832]; cortes de preço de laboratórios americanos; fim do uso ilimitado em ferramentas de programação | Datas e percentuais oficiais; anúncios de limites de uso |
| 2026 | DeepSeek V4 [M852]; novos cortes em julho (pista); Uber (abr–mai, pista); Jev (set, pista) | Ver abaixo |

**Pistas já levantadas em 14/10/2026 (a verificar):**

- **Uber.** Segundo a revista Fortune (26/05/2026), "relatos" dizem que a empresa esgotou em quatro meses o orçamento de 2026 para ferramentas de programação com IA, depois de estimular o uso com um ranking interno entre equipes. O COO disse num podcast que ainda não há ligação clara entre o uso e o que chega ao cliente. Outros sites citam um teto de US$ 1.500 por mês por funcionário e por ferramenta, mas a Fortune não traz esse número. Falta achar a fonte original.
- **Jev.** É um "modelo de decisão" da TypeSafe AI, de São Francisco (EUA), em acesso antecipado desde meados de set/2026. Ele devolve decisões estruturadas, não texto de conversa. Sites secundários falam em cerca de US$ 0,04 por milhão de tokens de entrada, com a saída gratuita, e numa rodada de US$ 870 milhões noticiada pela Bloomberg. Dois cuidados:
  - É uma empresa americana: a pressão sobre o preço não vem só da China.
  - É outra categoria de modelo: comparar o preço por token dele com o de modelos de conversa exige ressalva.

## 6. O paralelo com a indústria automotiva

**O que o paralelo sugere.** Entrantes chineses com qualidade alta e preço menor forçam os incumbentes a cortar preço. Por trás disso estão escala, eficiência e apoio do Estado. O mercado se reorganiza num patamar de preço mais baixo.

**O caso da Hilux (pista de 14/10/2026, a verificar).**
- Os cortes noticiados em set/2026 eram promoções temporárias, não redução do preço de tabela. A matéria da AutoMais (09/09/2026) fala em validade até 30/09, pagamento à vista e uma cor só, com estes valores:
  - Hilux SRV: R$ 44,7 mil a menos;
  - SW4: R$ 54,6 mil a menos.
- Outras matérias citam descontos para CNPJ (cerca de 22%) e na Agrishow (23%).
- A imprensa associa os descontos à concorrência da S10 e da GWM Poer P30, que custa de R$ 205 mil a R$ 247 mil. A Toyota não deu motivo.
- A nova geração da Hilux chega no início de 2027, o que também explica liquidar estoque.
- O caso ilustra a concorrência, mas não prova a causa sozinho.

**Onde o paralelo pode valer (a testar):**
- Modelos chineses abertos com desempenho perto da ponta e preço muito menor.
- Cortes de preço dos laboratórios americanos depois disso. Coincidência no tempo não prova causa: é preciso achar quem disse que cortou por causa da concorrência.
- Apoio do Estado chinês nos dois setores.

**Onde o paralelo pode quebrar (a testar):**
1. **Quantidade.** Quem compra uma picape não compra sete porque ficou mais barata. Com token barato, o uso se multiplica (H2). Nos carros, o preço menor reduz o gasto por necessidade atendida; na IA, pode aumentar o gasto total.
2. **Troca de fornecedor.** Trocar de marca de carro é decisão de compra. Trocar de modelo de IA pode exigir integração, testes e conformidade. Por outro lado, muitas interfaces de programação são compatíveis entre si, e isso facilita a troca.
3. **Restrições de origem.** Nos dois setores há restrições a fornecedores chineses por causa de dados (software de veículo conectado; modelos de IA). O peso disso numa empresa regulada precisa ser medido.
4. **Guerra de preço termina em consolidação.** Na China, o governo reagiu à guerra de preços dos carros. Se o mesmo ocorrer na IA, o risco de fornecedor quebrar entra na conta de quem compra.
5. **Preço difícil de comparar.** Carro tem preço de tabela. IA tem preço por token, por usuário, com desconto por cache ou por lote, e com limites de uso. Por isso o custo por tarefa vale mais que o preço por token.

## 7. Indicadores a coletar

| # | Indicador | Para quê | Onde buscar |
|---|---|---|---|
| 1 | Preço de lista por milhão de tokens (entrada e saída), por faixa e por origem, no lançamento e depois dos cortes, 2022–2026 | Curva de preço; H1 e H3 | Páginas oficiais de preço e cópias arquivadas com data |
| 2 | Preço para desempenho constante | H1 | AI Index 2025 [M230] e 2026; Epoch AI; a16z |
| 3 | Tokens por tarefa e volume total de tokens | H2 | [M666], [M701], [M170]; estudos de agentes e raciocínio |
| 4 | Gasto das empresas com IA e estouros de orçamento | H2 e H5 | Gartner [M125; M153; M659], EY [M070], McKinsey [M028], Bain [M003; M004]; Uber; pesquisas de mercado |
| 5 | Formas de cobrança: por token, por usuário, limites de uso, descontos | H4 | Anúncios e documentação oficial |
| 6 | Custo de produção e sustentabilidade do preço: energia, chips, data centers, resultado dos laboratórios | H4 | [M514], [M630]; demonstrações financeiras públicas |
| 7 | Participação dos modelos chineses no uso | Paralelo; H7 | Estudos de uso de tokens; [M832] |
| 8 | Brasil: câmbio, tributos sobre software e nuvem importados, preço de nuvem no país, Redata | H6 | Receita Federal e legislação; páginas de preço; [M196; M603] |
| 9 | Carros: participação das chinesas no Brasil, preço de tabela contra promoção, tarifa de importação de elétricos, guerra de preços na China | Paralelo | Fenabrave; montadoras; Gecex/MDIC; fontes oficiais chinesas |

## 8. Como vamos pesquisar

- **Três frentes de busca, no fluxo das fichas:**
  - A: preços e linha do tempo;
  - B: consumo, gasto e economia da oferta, com o Brasil;
  - C: paralelo automotivo.
- **Depois da busca:** verificação adversarial; entrada no catálogo (rodada 6, pasta `11_custo-da-ia`); dossiê; nota temática; revisão.
- **Regras próprias do tema:**
  - Todo preço com data, moeda e unidade (US$ por milhão de tokens, entrada e saída).
  - Página de preço muda: guardar cópia datada.
  - Preço de tabela e promoção não se misturam.
  - Número declarado pela empresa (adoção, volume, economia) é marcado como tal.
  - Não comparar preço por token entre categorias de modelo sem ressalva.
  - Custo por tarefa vale mais que preço por token.
  - Coincidência no tempo não prova causa.
- **Sessões executivas (sugestão, a validar com a equipe):** acrescentar uma pergunta de aprofundamento sobre como a empresa orça e controla o gasto com IA. Os insights entram só de forma agregada.
- **Buscas externas:** nunca mencionam o cliente nem o projeto. Formulário de acesso fica para envio manual.

## 9. Produtos

- **Nota temática** [custo-da-ia.md](custo-da-ia.md), escrita e revisada em 14/10/2026 a partir de 106 fontes novas (IDs M894 a M999, pasta `11_custo-da-ia`). Traz:
  - linha do tempo com preços;
  - a curva de preço contra a curva de consumo;
  - o paralelo automotivo, com onde vale e onde quebra;
  - o Brasil;
  - implicações em nível macro;
  - números que não devem ser usados;
  - lacunas.
- **Insumos para as outras frentes:**
  - Frente 1: o custo no cálculo do retorno.
  - Frente 2: gestão do gasto como capacidade no roadmap.
  - Relatório e workshop: um gráfico de preço contra consumo.
- **Assistente de IA do estudo:** fontes catalogadas com ID, consultáveis.

## Fontes

<!-- fontes:inicio -->
- **M003** — Bain & Company (2026). Technology Report 2026: AI, the Most Consequential Technology of Our Lifetimes. [link](https://www.bain.com/insights/topics/technology-report/) · citado em p. 53
- **M004** — Bain & Company (2026). Your AI Budget Is Growing. Your Returns Aren't. Here's Why. [link](https://www.bain.com/insights/your-ai-budget-is-growing-your-returns-arent-heres-why/)
- **M028** — McKinsey & Company (QuantumBlack) (2026). The state of AI in 2026: On the road to ROI. [link](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) · citado em p. 3
- **M070** — EY US (2026). EY Survey: C-Suites Pivot from AI Adoption to Unlocking Value as Escalating Token Costs Trigger Fiscal Scrutiny — US AI Pulse Survey, 5ª onda. [link](https://www.ey.com/en_us/newsroom/2026/07/ey-survey-c-suites-pivot-from-ai-adoption-to-unlocking-value-as-escalating-token-costs-trigger-fiscal-scrutiny) · citado em p. 1-2
- **M125** — Gartner (2026). The New AI Challenge Isn't Adoption. It's AI Spend. (The Real Threat to AI ROI Is Unchecked AI Spend). [link](https://www.gartner.com/en/articles/rein-in-ai-spend)
- **M153** — Gartner (2026). Gartner Forecasts Worldwide AI Spending to Grow 49.5% in 2026. [link](https://www.gartner.com/en/newsroom/press-releases/2026-09-16-gartner-forecasts-worldwide-ai-spending-to-grow-49-point-5-percent-in-2026)
- **M170** — OpenAI (2025). The state of enterprise AI — 2025 Report. [link](https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf) · citado em p. 3, 6
- **M196** — Senado Federal (Agência Senado) (2026). Sancionada lei de incentivo à instalação de data centers (Lei 15.504/2026 — Redata). [link](https://www12.senado.leg.br/noticias/materias/2026/09/16/sancionada-lei-de-incentivo-para-a-instalacao-de-data-centers) · citado em p. 1
- **M230** — Stanford HAI (2025). Artificial Intelligence Index Report 2025. [link](https://hai-production.s3.amazonaws.com/files/hai_ai_index_report_2025.pdf) · citado em p. 5, 65
- **M514** — IEA - Agência Internacional de Energia (2026). Key Questions on Energy and AI (World Energy Outlook Special Report). [link](https://iea.blob.core.windows.net/assets/3179f7f8-01f6-4dd6-bffa-c9f7b73f1dc9/KeyQuestionsonEnergyandAI.pdf) · citado em p. 29
- **M603** — Presidência da República (Planalto) (2026). Lei nº 15.504, de 15 de setembro de 2026 (Redata — Regime Especial de Tributação para Serviços de Datacenter). [link](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15504.htm)
- **M630** — Anthropic (2026). Covering electricity price increases from our data centers. [link](https://www.anthropic.com/news/covering-electricity-price-increases) · citado em p. 2
- **M659** — Gartner (2026 (15/09/2026)). Gartner Unveils Top Strategic Predictions for 2027 and Beyond (press release). [link](https://www.gartner.com/en/newsroom/press-releases/2026-09-15-gartner-unveils-top-strategic-predictions-for-2027-and-beyond) · citado em web
- **M666** — Google (Sundar Pichai) (2026 (19/05/2026)). Google I/O 2026: Sundar Pichai's opening keynote. [link](https://blog.google/intl/en-in/company-news/technology/sundar-pichai-io-2026/) · citado em web
- **M701** — Microsoft (Satya Nadella) (2025 (30/04/2025)). Microsoft Fiscal Year 2025 Third Quarter Earnings Conference Call. [link](https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q3) · citado em web
- **M832** — Stanford HAI e DigiChina (2025). Beyond DeepSeek: China's Diverse Open-Weight AI Ecosystem and Its Policy Implications. [link](https://hai.stanford.edu/assets/files/hai-digichina-issue-brief-beyond-deepseek-chinas-diverse-open-weight-ai-ecosystem-policy-implications.pdf)
- **M852** — NIST – CAISI (EUA) (2026). CAISI Evaluation of DeepSeek V4 Pro. [link](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro)
- **M853** — NIST – CAISI (EUA) (2025). Evaluation of DeepSeek AI Models. [link](https://www.nist.gov/document/caisi-evaluation-deepseek-ai-models-report)
<!-- fontes:fim -->
