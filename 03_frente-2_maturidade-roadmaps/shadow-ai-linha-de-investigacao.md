# Linha de investigação — Shadow AI e o caminho das corporações

> Documento de trabalho da OagronomIA · Frente 2 — Maturidade e roadmaps (com Frentes 1 e 3) · Aberto em 15/10/2026 · Protocolo de pesquisa do tema. Os números novos só entram na nota temática depois de verificados e catalogados.

## 1. Por que o tema entra no estudo

- **Governança é a dimensão mais atrasada do painel.** Nas quatro fichas, estratégia e governança fica abaixo das demais dimensões.
- **O tema já apareceu nas sessões.** Na sessão 1, o entrevistado usa equipamento e assinaturas pessoais de IA para conseguir trabalhar, e o ambiente corporativo de IA generativa está com o acesso travado ([registro anonimizado](../05_sessoes-executivas/registros-anonimizados/Sessao-01.md)). Nas notas internas de 13/10, o uso por fora aparece como sentimento geral.
- **A Acelen precisa de uma resposta prática.** A pergunta "como sair do shadow AI" é de roadmap: quais capacidades, em que ordem, com que custo.
- **Escopo.** O tema fica em nível macro: caminhos e modelos de governança observados no mercado, sem avaliar nem recomendar ferramenta específica nem desenhar a solução interna da Acelen, que é tema da governança de TI da companhia.

## 2. Perguntas centrais

1. **Por que o shadow AI cresce** nas empresas, no Brasil e fora?
2. **O que as empresas estão fazendo para sair dele:** impor a ferramenta da casa (no Brasil, quase sempre o Copilot da Microsoft), liberar outras ferramentas com governança, proibir, ou combinar caminhos? O que dá resultado?
3. **Impor o Copilot é o caminho?** Ou há formas de usar outras ferramentas com governança, segurança e custo adequado?
4. **Ferramentas de prototipação com IA** (o chamado *vibe coding*: Lovable, Replit, Bolt, v0 e similares): como usá-las com segurança e governança? Há casos de sucesso?

## 3. Hipótese de partida

1. Cerca de 90% das empresas usam a Microsoft como base de gestão e governança da organização.
2. O Copilot perdeu a corrida inicial da IA, e a maioria das pessoas foi para outras ferramentas, principalmente ChatGPT e Claude.
3. Por isso o shadow AI ganhou tração dentro das companhias: a ferramenta oficial é a Microsoft, e a preferida está fora dela.

**O que o catálogo já mostra:**

- **A base é Microsoft.** Nas médias e grandes empresas brasileiras, o Microsoft Office está em 89% da base instalada, o Excel em 92% e o Word em 89% [M209, p. 11].
- **Mas o Copilot lidera a base de IA generativa no Brasil.** Na mesma pesquisa, o Copilot tem 40% da base instalada de IA generativa, contra 32% do ChatGPT e 20% do Gemini [M209, p. 15]. Lá fora, cerca de 70% das empresas da Fortune 500 usam o Microsoft 365 Copilot [M026, p. 8]. A hipótese precisa separar licença de uso.
- **O shadow AI é comum no Brasil.** Numa pesquisa pequena, com 200 profissionais, 47,4% usam IA sem aprovação oficial, e 59,1% das empresas não têm diretriz formal de uso [M525, web].

## 4. Hipóteses concorrentes (o que pode desmentir ou matizar)

| # | Hipótese | Sinais já no catálogo ou nas buscas (pistas a verificar) | O que confirmaria |
|---|---|---|---|
| H2 | **O motor do shadow AI é a falta de ferramenta oficial boa, não a marca.** Quando a empresa oferece uma ferramenta aprovada, o uso por fora cai | Pista: na Netskope, o uso de IA generativa por contas pessoais caiu de 78% para 47% em um ano, e o de contas da empresa subiu de 25% para 62% (jan/2026). Pista: no MIT NANDA, 40% das empresas compraram assinatura oficial e mais de 90% têm funcionários usando ferramentas pessoais (ago/2025) | Queda do uso pessoal onde há ferramenta oficial; falta de acesso como motivo declarado |
| H3 | **O Copilot ganhou a licença, não o uso.** As empresas compram Copilot, e os funcionários continuam no ChatGPT | Catálogo: Copilot lidera a base instalada no Brasil [M209, p. 15]. Pistas: a Bloomberg relata que, mesmo com plano de 20 mil licenças de Copilot, funcionários da Amgen seguiam no ChatGPT; numa pesquisa com 150 mil pessoas nos EUA, o Copilot como ferramenta principal caiu de 18,8% para 11,5% entre jul/2025 e jan/2026 (Recon Analytics, via imprensa); numa pesquisa com 40 decisores, 82% adotaram o Copilot e 71% o ChatGPT (Jefferies, via imprensa) | Dados de uso ativo por ferramenta dentro de empresas que licenciaram o Copilot |
| H4 | **Proibir funciona pouco.** Regras mais duras não reduzem o uso por fora; o que reduz é liberar com controle | Pista: no Brasil, 66% dos executivos consideram provável o uso de IA pública sem aval, e regras internas mais rígidas reduzem pouco esse comportamento (Peers Consulting e TEC.Institute, via MIT Technology Review Brasil, set/2026). Pista: 88% dos funcionários com ferramenta da empresa também usam uma pessoal (Gartner, 1º tri/2026, via terceiros) | Comparação de empresas que proíbem e que liberam com controle |
| H5 | **Há caminhos além do Copilot, com governança e custo adequado.** Várias ferramentas aprovadas, plataforma interna com vários modelos ou a própria Microsoft abrindo o Copilot a outros modelos | Catálogo: um banco espanhol estende o ChatGPT Enterprise a mais de 120 mil funcionários, habilitou o Gemini para mais de 87 mil e tem 15 mil licenças de GitHub Copilot [M413, p. 6]; no maior banco dos EUA, mais de 65 mil pessoas do banco comercial e de investimento usam ativamente a plataforma interna de IA generativa [M441, p. 64]; uma empresa brasileira de celulose liberou um copiloto corporativo para quase 50 mil pessoas [M334, p. 6]; um grupo de cana pôs um assistente no Teams para 20 mil funcionários [M362, web] | Casos com governança descrita (identidade única, proteção de dados, registro de uso, treinamento) e custo por usuário |
| H6 | **O vibe coding abre uma nova frente de "aplicativos-sombra".** A facilidade de prototipar gera aplicativos fora da TI, com riscos de segurança próprios | Pista: no Brasil, 74% dos executivos já encontraram aplicativos ou agentes de IA criados por outras áreas sem aval da TI (Nutanix, 2026, via imprensa) | Incidentes documentados, controles empresariais das ferramentas e casos de uso seguro (protótipo em ambiente isolado, sem dado de produção, com caminho de promoção pela TI) |
| H7 | **O risco é real e tem custo.** Vazamento de dados, propriedade intelectual e conformidade (no Brasil, LGPD) | Pista: 88% dos profissionais compartilharam dados de trabalho com ferramenta pública de IA (PagerDuty, 2026). A sessão 1 relata cuidado próprio com o que é sensível | Custo de incidentes ligados ao shadow AI; casos de vazamento |

**Leitura preliminar (a confirmar).** O shadow AI parece nascer menos da marca e mais da distância entre o que o funcionário precisa e o que a empresa oferece, com governança lenta. Se isso se confirmar, a resposta não é "Copilot à força" nem "liberar tudo", e sim oferecer rápido ferramentas aprovadas (uma ou várias), com identidade única, proteção de dados, registro de uso, treinamento e um caminho para levar protótipos à produção.

## 5. O que investigar

**Frente A — Tamanho e causas do shadow AI, e a disputa Copilot × ChatGPT/Claude**
- Prevalência global e no Brasil, com método e amostra: Netskope, Verizon (DBIR 2026), PagerDuty, Gartner, MIT NANDA, Microsoft (Work Trend Index, "traga sua própria IA"), KPMG e Universidade de Melbourne [M110], Thomson Reuters, WatchGuard, Nutanix, Peers e TEC.Institute.
- Custo e incidentes: relatório de custo de vazamentos da IBM (2025 e 2026) com o recorte de shadow AI; casos públicos de vazamento por IA pública.
- Copilot × outras ferramentas: dados oficiais da Microsoft (licenças e uso), Bloomberg, Recon Analytics, Jefferies, Menlo Ventures, Ramp; movimentos da Microsoft (Copilot Chat sem custo adicional para quem tem Microsoft 365, outros modelos dentro do Copilot, preços).

**Frente B — Caminhos das corporações**
- Modelos de resposta: proibir, ferramenta única da casa, catálogo de ferramentas aprovadas, plataforma interna com vários modelos, combinação.
- Casos com governança descrita, globais e brasileiros (bancos, agro, indústria): ferramenta escolhida, alcance, regras, resultado. Inclui casos de Copilot imposto e seus resultados (ex.: testes de governos com o Copilot) e casos de várias ferramentas.
- Controles: política de uso, identidade única, prevenção de vazamento de dados, descoberta de aplicativos de IA na rede, registro e auditoria, treinamento, comitê; referências (NIST AI RMF, ISO/IEC 42001).
- Custo por usuário das opções corporativas, pelas páginas oficiais de preço, com data.

**Frente C — Vibe coding com governança**
- Ferramentas (Lovable, Replit, Bolt, v0 e afins): controles para empresas (login único, espaços de trabalho, varredura de segurança, residência de dados).
- Incidentes e estudos de segurança de código gerado por IA.
- Modelos de governança: ambiente isolado, sem dado de produção, revisão de segurança, caminho de promoção para a TI, centro de excelência de "desenvolvedores cidadãos" (o mesmo modelo usado em low-code).
- Casos de uso seguro e de sucesso, globais e brasileiros.

## 6. Como o tema entra no benchmark (proposta)

- **Frente 2, régua de maturidade:** acrescentar em estratégia e governança um indicador de "uso de IA fora dos canais oficiais", descrito estágio a estágio. Ele seria o par do indicador de gestão do custo já proposto na nota de custo.
- **Sessões executivas:** pergunta de aprofundamento sobre como a empresa lida com o uso por fora: ferramenta única ou várias, regras, e o que faz com ferramentas de prototipação. A validar com a equipe; o questionário validado com a Acelen não muda.
- **Nota temática:** [shadow-ai-e-governanca.md](shadow-ai-e-governanca.md), escrita e revisada em 15/10/2026 a partir de 75 fontes novas (IDs M1000 a M1074, pasta `12_shadow-ai-governanca`), com os caminhos observados, casos e o que funciona.
- **Apresentação e relatório:** um par de slides (visual e descritivo) no formato já usado.

## 7. Regras próprias do tema

- **Pesquisa de percepção não é medição.** Dados de tráfego de rede (Netskope, Verizon) e pesquisas de opinião (PagerDuty, Gartner) medem coisas diferentes; não se somam nem se comparam sem dizer a base.
- **Material de fornecedor marcado.** Quem vende ferramenta de segurança ou de IA tem interesse no tema; o dado entra marcado como tal.
- **Licença não é uso.** Separar empresas que compraram uma ferramenta de pessoas que de fato a usam.
- **Sem recomendação de ferramenta.** Nomes de produtos aparecem como dado de mercado.
- **Buscas** nunca mencionam o cliente nem o projeto. Formulários ficam para envio manual.

## Fontes

<!-- fontes:inicio -->
- **M026** — McKinsey & Company (QuantumBlack) (2025). Seizing the agentic AI advantage. [link](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage) · citado em p. 8
- **M110** — University of Melbourne e KPMG International (2025). Trust, attitudes and use of artificial intelligence: A global study 2025. [link](https://kpmg.com/xx/en/our-insights/ai-and-technology/trust-attitudes-and-use-of-ai.html)
- **M209** — FGV EAESP - FGVcia (Fernando Meirelles) (2025). Pesquisa do Uso de TI - 36ª Edição Anual, FGVcia, 2025. [link](https://eaesp.fgv.br/sites/default/files/files-eaesp/u68/pesti_fgvcia_2025.pdf) · citado em p. 11, 15
- **M334** — Suzano (2025). Microsoft e Suzano desenvolvem solução para impulsionar eficiência industrial com IA generativa (notícia, 23/04/2025). [link](https://www.suzano.com.br/noticia/microsoft-e-suzano-desenvolvem-ia-generativa) · citado em p. 6
- **M362** — Think Work Lab / iFood Benefícios (Acrescenta) (2025). Com IA generativa, Raízen transforma o atendimento interno (case da assistente BIA). [link](https://beneficios.ifood.com.br/acrescenta/artigos/ia-generativa-raizen) · citado em web
- **M413** — BBVA (2025). BBVA deploys 'The Eight', its strategy to transform the financial experience with AI (12/12/2025). [link](https://www.bbva.com/en/innovation/bbva-deploys-the-eight-its-strategy-to-transform-the-financial-experience-with-ai/) · citado em p. 6
- **M441** — JPMorganChase (2026). Annual Report 2025 (carta do CEO Jamie Dimon, carta do COO e cartas dos negócios). [link](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/annualreport-2025.pdf) · citado em p. 64
- **M525** — Exame, cobrindo pesquisa Abiacom/Brazil Panels/Lideres.ai (2026). 72% das empresas brasileiras estão no início da adoção de IA, aponta pesquisa. [link](https://exame.com/inteligencia-artificial/72-das-empresas-brasileiras-estao-no-inicio-da-adocao-de-ia-aponta-pesquisa/) · citado em web
<!-- fontes:fim -->
