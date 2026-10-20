# Custo de uso da IA — nota temática

> Documento de trabalho da OagronomIA · Frente 3 — Tendências e perspectivas futuras · Fontes públicas do catálogo · Data de corte: 14/10/2026 · Entrega parcial em revisão — não encaminhar ao cliente sem revisão.

**Como ler.** [M###, p. N] é o item M### do catálogo e a página N do PDF; [M###, web], item só na web. Preços em US$ por milhão de tokens, na forma entrada/saída (US$ 2/US$ 10), pela tabela pública na data indicada, sem desconto negociado, cache ou lote. Cada número diz de quem é: dado oficial, pesquisa independente, projeção de analista, número declarado pela empresa ou imprensa. "Cálculo nosso" marca conta da equipe; "leitura nossa", interpretação. Modelos e preços são dado de mercado: a nota não recomenda fornecedor nem avalia ferramenta. Desde o Claude 4.7, o tokenizador da Anthropic gera cerca de 30% mais tokens para o mesmo texto [M903, p. 1]; o asterisco (\*) marca esses modelos nas comparações. A cruz (†) marca preço da OpenAI tirado da tabela de out/2026, sem cópia da época.

**Termos.** *Token* é um pedaço de palavra, um número ou um sinal; mil tokens são cerca de 750 palavras em inglês [M969, p. 2; M924, p. 1]. *Entrada* é o que se envia ao modelo; *saída*, o que ele gera, em geral mais cara. *Inferência* é usar um modelo já treinado para responder [M230, p. 65]. *Modelo de raciocínio* gera um "pensamento" interno antes de responder, cobrado como saída [M972, p. 6]. *Agente* é um sistema que encadeia muitas chamadas ao modelo para cumprir uma tarefa sozinho [M912, p. 10]. *Modelo aberto* tem os pesos publicados, que terceiros podem usar e adaptar [M832, p. 3].

## 1. Resumo em uma página

- **Resposta curta: não, pelas evidências reunidas; o custo muda de lugar.** A hipótese de partida acerta no preço: a mesma capacidade ficou muito mais barata. Não se confirma a conclusão: a conta total tende a subir, porque o consumo cresce, a ponta encareceu e há reajustes. A preocupação passa do preço do token para o consumo e o que ele entrega (leitura nossa; seção 10).
- **O preço para a mesma capacidade despencou.** O custo de um modelo com o desempenho do GPT-3.5 passou de US$ 20 para US$ 0,07 por milhão de tokens entre nov/2022 e out/2024, mais de 280 vezes menos (AI Index, pesquisa independente) [M230, p. 65]. Com outra base, a Epoch AI mede quedas de 9 a 900 vezes por ano, conforme a tarefa [M933, p. 1].
- **Mas a queda é desigual, e a ponta voltou a subir.** Em out/2026, o GPT-6 Astra, modelo mais capaz da OpenAI, custa US$ 10/US$ 50, oito vezes a entrada e cinco vezes a saída do GPT-5, de ago/2025 (cálculo nosso); o topo da Anthropic, o Fable 5\*, custa o mesmo [M968, p. 1; M958, p. 1; M903, p. 1]. Há sucessores mais caros e aumentos já marcados [M953, p. 4-5; M952, p. 3].
- **O consumo cresce depressa.** Modelos de raciocínio geram cerca de 8 vezes mais tokens por resposta (Epoch AI) [M934, p. 1]; agentes, cerca de 4 vezes mais que o chat, e sistemas com vários agentes, 15 vezes (dados da Anthropic) [M911, p. 3]. O Google declara mais de 3,2 quatrilhões de tokens por mês, 7 vezes um ano antes [M666, web]. Para o Gartner, o consumo sobe mais rápido do que cai o custo do token, e o custo total de inferência deve aumentar (projeção) [M948, p. 2].
- **A conta já preocupa.** Nos EUA, 82% dos executivos de empresas que investem em IA dizem que a organização se preocupa com o custo de tokens, e só 64% monitoram o consumo com limites de orçamento (EY, jul/2026) [M070, p. 1-2]. Na pesquisa global da McKinsey, 1 em cada 5 respondentes diz que o custo de operação já limitou o uso; para a consultoria, ainda não é uma restrição generalizada [M028, p. 15].
- **O caso Uber mostra o problema e a saída.** Segundo a imprensa de referência, a Uber esgotou em cerca de quatro meses o orçamento anual de IA [M986, p. 2]. Depois, segundo a empresa, multiplicou o uso por 7 com gasto "relativamente estável", cortando consumo sem valor [M995, p. 2, 16].
- **A cobrança migra para o uso.** O GitHub passou o Copilot para cobrança por uso em jun/2026, dizendo que o modelo anterior "não é mais sustentável" [M951, p. 1-2].
- **O movimento chinês pesa, mas não explica tudo.** A guerra de preços na China começou em mai/2024, antes do DeepSeek-R1 [M999, p. 2-3]. Nas fontes catalogadas, nenhum laboratório americano atribuiu cortes à concorrência chinesa; a DeepSeek subiu preços em 2026 [M924, p. 2; M925, p. 2]; e há movimentos de baixa também do lado americano: o Jev, modelo de decisão de uma empresa americana, entrou em set/2026 com o menor preço da sua categoria, e a OpenAI lançou um concorrente 21 dias depois, segundo a imprensa inspirado nele [M990, p. 1-2, 4; M955, p. 2; M967, p. 1].
- **O paralelo com os carros vale em parte.** As marcas chinesas passaram de cerca de 2,8% para ao menos 17,4% dos emplacamentos no Brasil entre 2023 e jan–set/2026 (cálculo nosso) [M935, p. 9; M938, p. 9]. Mas o desconto da Hilux foi promoção [M913, p. 1-4], e a analogia quebra no essencial: carro mais barato não multiplica o consumo; no token, há sinais de que sim (leitura nossa) [M974, p. 32].
- **O Brasil acrescenta camadas.** Na AWS, as instâncias comparadas custam em São Paulo de 59% a 70% a mais por hora que na Virgínia do Norte (cálculo nosso) [M897, p. 18, 63; M898, p. 32, 81], embora o token na implantação global da Azure custe o mesmo [M958, p. 1]; e o serviço importado paga tributos em transição [M977, web; M976, web].

## 2. A pergunta e a hipótese de partida

**Pergunta central.** O custo de usar IA vai deixar de ser preocupação para quem planeja a estratégia de IA de uma grande agroindústria? O retorno da IA é valor dividido por custo: a nota [Valor e retorno da IA](../02_frente-1_benchmark-estrategico/notas/valor-e-retorno-da-ia.md) trata do valor; esta, do custo de usar modelos.

**Hipótese de partida (H1).** A IA ficou cara e depois começou a baratear:
1. O ChatGPT chega no fim de 2022 e surgem novas empresas de modelos.
2. Com o Claude e os modelos seguintes, o custo vira tema.
3. O DeepSeek derruba os preços, e surge o movimento chinês.
4. O Uber gasta em quatro meses o orçamento do ano.
5. O Jev derruba ainda mais o preço.

Paralelo: as montadoras chinesas entregam qualidade por preço menor e obrigam as outras a baixar o preço, como no desconto de perto de R$ 60 mil da Hilux. Conclusão: o preço da IA não deve ser tanta preocupação, porque o token vem barateando.

**Hipóteses concorrentes.** H2: o preço cai, mas a conta sobe (paradoxo de Jevons: o recurso que barateia passa a ser tão usado que o gasto total aumenta). H3: a queda é desigual entre faixas. H4: o preço está abaixo do custo e pode subir. H5: o token é a menor parte da conta. H6: o Brasil tem custo próprio. H7: o mais barato pode não ser utilizável.

**Método.** São 376 evidências de três frentes de busca (preços; consumo, gasto e Brasil; carros), todas conferidas na fonte.

## 3. Linha do tempo do preço, 2022–2026

Preço de tabela em US$ por milhão de tokens (entrada/saída); "único" quando não havia separação. Em 2022–2023, a OpenAI cobrava por mil tokens: os valores foram convertidos (cálculo nosso).

| Data | Marco | Preço oficial | Fonte |
|---|---|---|---|
| dez/2022 | Ano do ChatGPT; o Davinci era o modelo mais capaz da API da OpenAI | US$ 20 (único) | [M969, p. 2; M992, p. 9] |
| 01/03/2023 | API do gpt-3.5-turbo, "10 vezes mais barata"; a OpenAI diz ter cortado 90% do custo do ChatGPT desde dez/2022 (declarado) | US$ 2 (único) | [M965, p. 3, 8] |
| mar/2023 | GPT-4, com contexto de 8 mil tokens | US$ 30/US$ 60 | [M970, p. 4] |
| jul/2023 | Claude 2 | US$ 11,02/US$ 32,68 | [M908, p. 1] |
| 04/03/2024 | Claude 3: Opus, Sonnet e Haiku | US$ 15/US$ 75; US$ 3/US$ 15; US$ 0,25/US$ 1,25 | [M907, p. 1, 7-9] |
| mai/2024 | Guerra de preços na China (imprensa); GPT-4o; DeepSeek-V2 | GPT-4o: US$ 5/US$ 15†; V2: US$ 0,14/US$ 0,28 | [M999, p. 2-3; M967, p. 18; M968, p. 1; M927, p. 1] |
| 12/09/2024 | Primeiros modelos de raciocínio da OpenAI, o1-preview e o1-mini | o1: US$ 15/US$ 60† | [M967, p. 15-16; M968, p. 1; M901, p. 6] |
| dez/2024–jan/2025 | DeepSeek-V3 e R1; a Nvidia perde quase US$ 600 bilhões de valor num dia, o que a CNBC atribui à DeepSeek (imprensa) | V3: US$ 0,27/US$ 1,10; R1: US$ 0,55/US$ 2,19 (mar/2025, horário padrão) | [M926, p. 1-2; M918, p. 1] |
| abr–jun/2025 | O o3 é lançado e tem o preço reduzido em 10/06/2025 | US$ 10/US$ 40 em 21/04/2025; US$ 2/US$ 8 na tabela de out/2026 (−80%, cálculo nosso) | [M966, p. 2; M967, p. 13-14; M968, p. 1] |
| 07/08/2025 | GPT-5 | US$ 1,25/US$ 10† (igual na Azure desde 01/08/2025) | [M967, p. 13; M968, p. 1; M958, p. 1] |
| 29/09/2025 | DeepSeek-V3.2-Exp, com corte de mais de 50% | De US$ 0,56/US$ 1,68 para US$ 0,28/US$ 0,42 | [M929, p. 1-3] |
| 24/11/2025 | Claude Opus 4.5 | US$ 5/US$ 25 (Opus 4.1: US$ 15/US$ 75) | [M905, p. 1-2; M903, p. 1] |
| dez/2025–abr/2026 | GPT-5.2, GPT-5.4 e GPT-5.5 | US$ 1,75/US$ 14; US$ 2,50/US$ 15; US$ 5/US$ 30† | [M967, p. 8, 11; M968, p. 1] |
| jul–ago/2026 | GPT-5.6: em 30/07, Luna −80% e Terra −20%, atribuídos pela empresa a ganhos de eficiência; em 21/08, o Sol entra em promoção, válida ao menos até 21/11/2026 | Luna: US$ 0,20/US$ 1,20; Sol: US$ 4/US$ 20 (promocional) | [M967, p. 4-5; M964, p. 1-3] |
| set/2026 | GPT-6 Astra, o mais capaz da OpenAI; GPT-6 Sol e GPT-6 Luna | US$ 10/US$ 50†; US$ 2/US$ 10; US$ 0,10/US$ 0,50 | [M967, p. 2-3; M968, p. 1] |
| 15/09–06/10/2026 | Jev, "modelo de decisão" da TypeSafe AI (EUA), em acesso antecipado (data da imprensa); 21 dias depois, a OpenAI lança a sua Decisions API | Jev: US$ 0,042 na entrada, saída grátis (outra categoria) | [M955, p. 4; M990, p. 4; M967, p. 1] |

## 4. O que caiu e o que não caiu

**Preço para desempenho constante.** Quatro medidas acompanham o preço de uma capacidade fixa, com bases diferentes: os números não se somam nem se comparam sem dizer a base.

| Medida | Base | Resultado | Fonte |
|---|---|---|---|
| AI Index 2025 (Stanford) | Modelo mais barato com a nota do GPT-3.5 no teste MMLU; média 3:1 entre entrada e saída | Mais de 280 vezes (nov/2022–out/2024) | [M230, p. 65] |
| Epoch AI (mar/2025) | Modelo mais barato que atinge cada marco, em seis testes | De 9 a 900 vezes por ano; as quedas mais rápidas são recentes, e não é claro que durem | [M933, p. 1] |
| a16z (nov/2024) | Nota fixa no MMLU, só OpenAI, Anthropic e Llama; média simples | 10 vezes por ano | [M901, p. 2] |
| Artificial Analysis (3º tri/2025) | Classes do índice da própria empresa; média 3:1 | Nível GPT-4 100 vezes mais barato; mudanças menores no topo | [M912, p. 10, 14] |

A a16z investe no setor: liderou a rodada da TypeSafe AI e assina o estudo da OpenRouter [M991, p. 1-2; M974, p. 1]. Sobre as causas, a Epoch cita modelos menores e hardware mais eficiente e não achou evidência clara de margens menores [M933, p. 2-3].

**Preço de tabela por faixa** (US$ por milhão de tokens, entrada/saída):

| Faixa | Antes | Out/2026 | Leitura nossa | Fonte |
|---|---|---|---|---|
| Topo | GPT-4: 30/60 (mar/2023); Claude 3 Opus: 15/75 (mar/2024); em 2025, GPT-5† e Gemini 2.5 Pro: 1,25/10, e Claude Opus 4.5: 5/25 | GPT-6 Astra e Claude Fable 5\*: 10/50; Gemini 4 Argon: 2/10, o dobro a partir de dez/2026 | Caiu até 2025 e voltou a subir | [M970, p. 4; M907, p. 7; M968, p. 1; M953, p. 4; M905, p. 2; M903, p. 1; M952, p. 3] |
| Intermediária | Claude 3 Sonnet: 3/15 (mar/2024); Gemini 2.0 Flash: 0,10/0,40 (jul/2025) | Sonnet 5\* e GPT-6 Sol: 2/10; Gemini 3.8 Flash: 0,75/3,75, o dobro a partir de jan/2027 | Queda pequena ou alta | [M907, p. 8; M953, p. 5; M903, p. 1; M968, p. 1; M952, p. 4] |
| Econômica | Claude 3 Haiku: 0,25/1,25 (mar/2024); GPT-4o mini: 0,15/0,60 (jul/2024)†; Gemini 2.5 Flash-Lite: 0,10/0,40 (jul/2025) | Haiku 5.5\* (até 100 mil tokens) e GPT-6 Luna: 0,10/0,50; Gemini 3.5 Flash-Lite: 0,30/2,50 | Caiu, com idas e vindas; subiu no Google | [M907, p. 9; M967, p. 17; M968, p. 1; M953, p. 4; M903, p. 1; M952, p. 8-9] |

**A ponta subindo em 2025–2026.** Na OpenAI, o modelo principal foi do GPT-5 (US$ 1,25/US$ 10†) ao GPT-5.5 (US$ 5/US$ 30†) e ao GPT-6 Astra, cuja saída, a US$ 50†, se aproxima dos US$ 60 do GPT-4 de 2023 [M968, p. 1; M970, p. 4]. Modelos mais novos fazem mais [M230, p. 65], mas a ponta ficou mais cara (leitura nossa), e as empresas migram em massa para o melhor modelo, sem capturar a economia dos antigos, segundo a Menlo Ventures, investidora da Anthropic [M956, p. 6-7].

**O sucessor mais caro e o preço que vai e volta** (cálculos nossos):
- Claude 3 Haiku → Claude 3.5 Haiku, revisado para US$ 0,80/US$ 4 em dez/2024: 3,2 vezes [M907, p. 9; M906, p. 1].
- Gemini 2.0 Flash → 2.5 Flash (US$ 0,30/US$ 2,50): 3 vezes na entrada e 6,25 vezes na saída, em jul/2025 [M953, p. 4-5].
- Claude Opus 4.6 → 4.7\*: mesmo preço por token, mas cerca de 30% mais tokens por texto [M903, p. 1].
- Gemini 4 Argon e 3.8 Flash dobram de preço em 01/12/2026 e 01/01/2027 [M952, p. 3-4]; já o preço introdutório do Sonnet 5\* virou padrão [M903, p. 1].

**A própria DeepSeek reajustou.** O V3.1 (US$ 0,56/US$ 1,68, set/2025) custava mais que o V3 (US$ 0,27/US$ 1,10, mar/2025, horário padrão) até o corte de 29/09/2025 [M853, p. 66; M926, p. 2]. Quem manteve o nome do V4-Flash, que custava US$ 0,14/US$ 0,28 em jul/2026, paga hoje o preço do V4.1-Flash: US$ 0,30/US$ 1,20 no pico, 2,1 vezes a entrada e 4,3 vezes a saída (cálculo nosso), e a metade fora do pico [M924, p. 2; M925, p. 2].

## 5. O consumo e a conta

**Tokens por tarefa.** O raciocínio é cobrado como saída, a tarifa mais cara, mesmo quando não aparece na resposta, e vai de centenas a dezenas de milhares de tokens por resposta [M972, p. 6; M910, p. 6]. Para responder "quanto é 2 mais 3", modelos do tipo o1 gastaram em média 1.953% mais tokens que os convencionais (estudo da Tencent e da Universidade Jiao Tong) [M987, p. 2]. Num modelo agêntico, o Gartner estima de 5 a 30 vezes mais tokens por tarefa que num chatbot [M948, p. 2].

**Mais tokens não garantem mais resultado.** Em 21.730 execuções de agentes (Princeton e coautores), mais raciocínio deu acurácia igual ou menor em 21 de 36 combinações, e o modelo mais caro ficou entre as melhores opções de custo e acurácia em só 1 de 9 testes [M978, p. 1, 6-7]. O CAISI, órgão de avaliação de IA do governo americano, mede o gasto por tarefa porque o número de tokens varia entre modelos: quem cobra metade por token e usa quatro vezes mais tokens sai o dobro [M853, p. 14].

**Volume total** (números declarados). A Microsoft processou no 1º tri/2025 cinco vezes os tokens de um ano antes, e o seu custo de servir cada token caiu mais da metade, sem período informado [M701, web]. Na OpenAI, os tokens de raciocínio por organização cresceram 320 vezes em 12 meses [M170, p. 6]. Na OpenRouter, plataforma que distribui chamadas entre modelos, os de raciocínio passaram de quase nada a mais da metade dos tokens em 2025 [M974, p. 13].

**Gasto das empresas.** O gasto com APIs de modelos foi de US$ 3,5 bilhões (nov/2024) para US$ 8,4 bilhões (meados de 2025), segundo estimativa da Menlo [M956, p. 1]. Na base de clientes da Ramp, nos EUA, a empresa mediana gastou com IA US$ 11,95 por funcionário em jul/2026, e o 1% que mais gasta, US$ 7.400, ambos no mês [M979, p. 5]. O retorno não acompanha: quase 40% das empresas que mediram a economia com IA ficaram entre 0% e 10%, mas 90% voltam a aumentar o orçamento, agora para agentes (Bain) [M004, p. 2].

**O caso Uber.**

| O que se sabe | Quem diz | Fonte |
|---|---|---|
| Em abr/2026, o CTO revelou que o orçamento anual de IA acabara em cerca de quatro meses, o que parece ter ocorrido depois de incentivo ao uso e de rankings internos | Imprensa de referência: TechCrunch, citando The Information; a Fortune fala em "relatos" | [M986, p. 2; M941, p. 3] |
| A ligação entre o uso do Claude Code e funcionalidades úteis ao consumidor "ainda não existe" | COO da Uber, via Fortune | [M941, p. 3] |
| Teto de US$ 1.500 por mês por funcionário e por ferramenta de programação agêntica, com exceções (jun/2026) | Bloomberg, via TechCrunch | [M986, p. 2] |
| Custos de IA 6 vezes maiores desde 2024 | Engenheiros da Uber, via The Pragmatic Engineer (declarado) | [M989, p. 3] |
| De fev a ago/2026, uso 7 vezes maior, gasto "relativamente estável" desde abril; faixa de gasto única, alertas e aprovação do gestor, "para evitar tetos rígidos" | Blog de engenharia (declarado); desenho diferente do teto de junho | [M995, p. 2, 15] |

A Uber mapeia 16 padrões de desperdício, como rodar sessões simples no modelo mais caro [M995, p. 15]. O valor do orçamento não tem fonte (seção 13).

**A cobrança migra para o uso.** O GitHub cobra o Copilot por uso desde 01/06/2026, porque uma pergunta rápida e uma sessão agêntica de horas custavam o mesmo [M951, p. 1-2]. O Cursor trocou 500 requisições por US$ 20 de uso a preço de API em jun/2025 [M923, p. 1-2]. A Anthropic pôs limites semanais nos planos Pro e Max em ago/2025 [M984, p. 2] e cobra o Enterprise por assento mais todo o uso a preço de API [M909, p. 11; M904, p. 2]. Leitura nossa: quem paga por uso carrega o risco do consumo.

## 6. Quem paga a conta

**Sinais de preço abaixo do custo.** O CEO da OpenAI disse, em jan/2025, que a empresa perdia dinheiro com o ChatGPT Pro, de US$ 200 por mês, porque os assinantes usavam mais que o previsto (via TechCrunch) [M985, p. 2]. O GitHub diz ter absorvido grande parte do custo crescente de inferência [M951, p. 2]. A TypeSafe AI diz não poder provar que o preço do Jev não é subsidiado [M990, p. 7]. Um estudo da equipe da USCC, comissão do Congresso americano, diz que o governo chinês subsidia o acesso a modelos por API [M992, p. 8].

**O que os números oficiais mostram.** Os US$ 4,1 bilhões de perdas da Microsoft com a OpenAI no trimestre jul–set/2025 são a parcela da Microsoft no resultado da OpenAI, por equivalência patrimonial, não o prejuízo total da OpenAI [M961, p. 9, 11]. O ganho de US$ 6,5 bilhões do ano fiscal 2026 vem da diluição na recapitalização e não indica lucro [M960, p. 41, 60]. A margem bruta da nuvem da Microsoft caiu para 66% nesse ano, por causa da infraestrutura de IA, segundo a empresa [M960, p. 37]. OpenAI e Anthropic divulgam só receita; a OpenAI diz que "às vezes, a capacidade vem antes do uso" e, em outras, o uso vem antes [M973, p. 4].

**Projeções do Gartner.**
- Até 2030, a inferência num modelo de 1 trilhão de parâmetros custará aos fornecedores mais de 90% menos que em 2025, sem repasse integral às empresas [M948, p. 1].
- A virada dos fornecedores do "crescimento subsidiado" para a lucratividade está entre as causas da alta prevista do custo da IA no atendimento ao cliente [M947, p. 1].
- Se o ritmo atual continuar, mais de US$ 3,5 trilhões investidos em infraestrutura de IA podem ficar expostos a baixa contábil até 2030, e mais de 80% das "neoclouds", nuvens especializadas em GPU, devem deixar de operar sozinhas [M949, p. 1-2].

**GPU e energia.** A AWS cortou até 45% o preço de instâncias com GPU em jun/2025, embora dissesse que a demanda superava a oferta [M899, p. 1]; em 13/10/2026, a hora de uma GPU H100 custava US$ 2,85 no índice da Silicon Data [M982, p. 1]. A Anthropic se comprometeu a cobrir a alta da conta de luz causada por seus data centers [M630, p. 1-2] (energia: ver [IA e impacto ambiental](ia-e-impacto-ambiental.md)).

Leitura nossa: o custo de servir cai, mas o capital comprometido é enorme, e parte da conta ainda não chegou ao usuário.

## 7. O movimento chinês

**A guerra de preços começou antes do R1.** Em mai/2024, segundo a Yicai (imprensa), a gestora High-Flyer anunciou preço de cerca de 1/100 do GPT-4; a Zhipu cortou 80%; a ByteDance lançou o Doubao cerca de 99% abaixo da média do setor; a Alibaba cortou até 97%; e a Baidu zerou dois modelos. Para um analista da Canalys, a meta era atrair clientes de nuvem [M999, p. 2-3].

**DeepSeek.** O custo de treino declarado do V3, US$ 5,576 milhões, cobre só o treino final [M928, p. 5]. Em mar/2025, o R1 custava cerca de 1/27 do o1 (cálculo nosso, com o preço do o1 na tabela de out/2026) [M926, p. 2; M968, p. 1]; depois dele, as grandes de tecnologia americanas perderam temporariamente mais de US$ 1 trilhão em valor de mercado [M198, p. 74]. Para Stanford e DigiChina, atraiu por ser livre para adaptar, barato de implantar e bom o bastante [M832, p. 3].

**Participação.** Na OpenRouter, os modelos abertos chineses foram de 1,2% do volume semanal de tokens no fim de 2024 a perto de 30% em algumas semanas de 2025, com média de cerca de 13% [M974, p. 5]. Em jan/2026, o Kimi K2.5 custava US$ 1,20 por milhão de tokens, contra US$ 4,81 do GPT-5.2, em preço combinado 3:1 de entrada e saída e com a mesma nota num índice de inteligência (estudo da equipe da USCC) [M992, p. 8]. Para o AI Index, com a distância entre os países quase fechada, a disputa vai para custo, confiabilidade e utilidade [M198, p. 69].

**O mais barato depende da data e da tarefa.** O CAISI achou o GPT-5-mini, em média, 35% mais barato que o DeepSeek V3.1 para desempenho semelhante em set/2025, com um preço que a DeepSeek cortou em mais da metade duas semanas depois [M853, p. 2, 66; M929, p. 1-3]. Em abr/2026, com o preço declarado pela desenvolvedora, o V4 Pro saiu mais barato que o GPT-5.4 mini em 5 de 7 testes, de 53% mais barato a 41% mais caro por tarefa [M852, p. 2, 7].

**Restrições de origem.** No CAISI, agentes baseados no modelo mais seguro da DeepSeek seguiram instruções maliciosas, em média, 12 vezes mais que os americanos de fronteira; para o órgão, o uso desses modelos pode trazer risco a desenvolvedores, consumidores e à segurança nacional americana [M853, p. 2]. Para Stanford e DigiChina, modelo aberto servido por nuvem estrangeira ainda traz risco de dependência [M832, p. 14]. E restringir o processamento a uma região custa mais: 10% na OpenAI e 1,1 vez a tarifa na Anthropic (inferência só nos EUA) [M968, p. 3; M903, p. 2].

**A pressão não é só chinesa.** Nas fontes do catálogo, nenhum laboratório americano declarou ter cortado preço por causa da concorrência chinesa; as justificativas oficiais falam em eficiência e acesso [M965, p. 3; M964, p. 1; M905, p. 2; M954, p. 1]. Ao cortar em jul/2026, a OpenAI se comparou a um concorrente americano, a Anthropic [M964, p. 2]. A relação com os cortes chineses é só temporal, e coincidência no tempo não prova causa. Atribuir cortes à concorrência é leitura de analistas: para a a16z, modelos abertos de Meta, Mistral e outros reduziram margens e preços [M901, p. 6]. O Jev, da americana TypeSafe AI, cobra US$ 0,042 por milhão de tokens de entrada, mas devolve decisões, não texto, e a comparação com modelos de conversa é da própria empresa [M990, p. 1-2, 4]; na sua categoria, a OpenAI cobra US$ 0,10 (imprensa) [M955, p. 6]. **Mas, nessa categoria, a reação veio rápido.** A OpenAI lançou a sua Decisions API em 06/10/2026, 21 dias depois do Jev [M967, p. 1], e um integrante da empresa disse, num podcast citado pela Fortune, que o Jev "inspirou" o produto (imprensa) [M955, p. 2]. Em out/2026, as ofertas hospedadas da categoria, de três empresas (TypeSafe AI, OpenAI e Cloudflare), cobravam de US$ 0,042 a US$ 0,24 por milhão de tokens de entrada, e nenhuma cobrava a saída [M955, p. 6]. É o único caso do catálogo em que a imprensa registra um incumbente reagindo a um entrante de preço baixo, e ele vem de uma empresa americana, não chinesa (leitura nossa).

## 8. O paralelo com os carros: onde vale e onde quebra

**As chinesas no Brasil** (participação nos emplacamentos de automóveis e comerciais leves, Fenabrave):

| Marca | 2023 | 2024 | 2025 | Jan–set/2026 | Fonte |
|---|---|---|---|---|---|
| BYD | 0,82% | 3,09% | 4,43% | 7,84% | [M935, p. 9; M936, p. 9; M937, p. 9; M938, p. 9] |
| Chinesas entre as 21 primeiras (cálculo nosso, piso) | 2,8% | 6,7% | 9,2% | 17,4% | [M935, p. 9; M936, p. 9; M937, p. 9; M938, p. 9] |
| Toyota | 8,82% | 8,20% | 6,69% | 5,69% | [M935, p. 9; M936, p. 9; M937, p. 9; M938, p. 9] |

A soma inclui a Caoa Chery, feita no Brasil por grupo brasileiro com marca chinesa (classificação nossa). O Brasil foi o 2º destino das exportações chinesas de veículos de jan a ago/2026 (CPCA) [M919, p. 4-5], e a BYD já produz em Camaçari (BA) [M916, p. 5], enquanto o imposto de importação dos elétricos montados, fora da cota, subiu de 10% em jan/2024 para 35% em jul/2026 [M920, p. 1-3; M921, p. 22].

**O caso Hilux.** Os descontos foram promoções temporárias, não corte de tabela, segundo a imprensa:
- set/2026: Hilux SRV de R$ 314.690 por R$ 269.990, até 30/09, à vista, numa cor só e no varejo (14,2%, cálculo nosso) [M913, p. 1-4];
- jan/2026: até 22% na venda direta para CNPJ e produtor rural, até 31/01 [M945, web];
- Agrishow 2026: 23% na Hilux SR, só no estande [M997, p. 2-3].

Os "cerca de R$ 60 mil" só aparecem na venda direta (até R$ 64,4 mil, conforme a versão) e na Agrishow (R$ 71,3 mil), não no varejo (cálculo nosso). A ligação com as chinesas é leitura da imprensa; a Toyota não deu motivo [M913, p. 2]. Nas picapes grandes, de jan a set/2026, a Toro teve 21,39% do segmento, a Hilux 16,69%, a Ranger 13,43% e a S10 11,46%, contra 2,59% da Poer, única chinesa entre as 11 primeiras [M938, p. 18]: a Hilux disputa sobretudo com as três (leitura nossa). A troca de geração, prevista pela imprensa para o início de 2027, também pode explicar a liquidação de estoque (leitura nossa) [M913, p. 3].

**A guerra de preços na China e a reação do governo.** Em mai/2025, a BYD deu descontos de até 34% em 22 modelos (imprensa) [M942, p. 2]. Um responsável do Ministério da Indústria disse que a "guerra de preços" "não tem vencedores, muito menos futuro" [M962, p. 1], e, em fev/2026, o regulador de mercado passou a ver "risco jurídico grave" em vender abaixo do custo para excluir concorrentes [M895, p. 1, 3]. A margem de lucro do setor caiu para 3,6% em jan–ago/2026 (CPCA) [M919, p. 4], e só 3 de 30 montadoras chinesas de elétricos e híbridos plug-in lucraram em 2025; a AlixPartners prevê consolidação [M896, p. 2]. A mesma "involução" aparece na IA chinesa, e a campanha de 2025 contra ela vai dos elétricos à IA (War on the Rocks, análise) [M998, web].

**Onde vale e onde quebra.**

| Ponto | Carros | IA | Leitura nossa |
|---|---|---|---|
| Entrante chinês mais barato | Avanço nos emplacamentos (tabela acima) | Cerca de 13% do volume numa plataforma [M974, p. 5] | Vale |
| Papel do Estado | Pequim ajudou a criar as condições da sobrecapacidade (análise) [M998, web] e agora combate a "involução" [M917, p. 11] | Subsídio à energia e ao uso [M992, p. 8-9] | Vale; nos carros, subsídio não medido |
| Reação dos incumbentes | Promoções sem causa declarada [M913, p. 2] | Cortes atribuídos a eficiência [M964, p. 1]; na categoria do Jev, produto concorrente em 21 dias, que a imprensa liga ao entrante [M955, p. 2] | Vale em parte: na IA há um caso de reação registrado pela imprensa; nos carros, só coincidência no tempo |
| Quantidade | Ninguém compra sete picapes porque ficaram baratas | Uso multiplicado com preço em queda; sinais do paradoxo de Jevons [M974, p. 32] | Quebra |
| Troca de fornecedor | Decisão de compra | Só 11% trocaram de fornecedor em um ano [M956, p. 5] | Quebra em parte |
| Restrições de origem | Software de veículo conectado ligado à China vetado nos EUA [M931, p. 1-2] | Riscos apontados pelo governo americano [M853, p. 2] | Vale |
| Fim da guerra de preço | Consolidação prevista [M896, p. 2] | Consolidação prevista nas "neoclouds" [M949, p. 1-2] | Vale como risco de fornecedor |
| Preço comparável | Tabela e promoção | Token, tokenizador, cache, lote, pico e limites | Quebra: vale o custo por tarefa |

## 9. Brasil

**Tributos sobre software e nuvem importados.** Quadro descritivo, sem soma e sem orientação tributária: bases, créditos e enquadramento dependem de cada contrato.

| Tributo | Norma | O que diz | Situação em out/2026 | Fonte |
|---|---|---|---|---|
| IRRF | Solução de Consulta Cosit 191, de 23/03/2017 | 15% sobre remessa por software como serviço | Depende do enquadramento | [M980, p. 2] |
| CIDE-Tecnologia | Mesma consulta; STF, Tema 914, 13/08/2025 | 10% sobre essas remessas | Ampliação validada pelo STF | [M980, p. 2; M983, p. 1] |
| PIS/Pasep e Cofins-Importação | Lei 10.865, de 30/04/2004 | 1,65% e 7,6% | Revogados a partir de 01/01/2027 | [M977, web] |
| ISS | LC 116, de 31/07/2003 | De 2% a 5% | Reduções de 2029 a 2032; revogação em 2033 | [M975, web] |
| IOF-câmbio | Decretos 12.466 (mai/2025) e 12.499 (jun/2025) | De 0,38% para 3,5% em remessas | Cautelar do STF de 16/07/2025; aplicação ao serviço importado depende do enquadramento | [M894, p. 1; M930, p. 2, 4] |
| IBS e CBS | LC 214, de 16/01/2025, alterada pela LC 227/2026 | Incidem sobre serviço importado consumido no País; em 2026, CBS de 0,9% e IBS de 0,1%, compensáveis | No regime regular, gera crédito | [M976, web; M981, p. 4-5] |

**Nuvem em região brasileira** (preço de lista sob demanda, Linux, out/2026; AWS: São Paulo e Virgínia do Norte; Azure: Brazil South e East US 2):

| Item | Brasil | EUA | Diferença (cálculo nosso) | Fonte |
|---|---|---|---|---|
| AWS m6i.xlarge, por hora | US$ 0,306 | US$ 0,192 | +59% | [M897, p. 63; M898, p. 81] |
| AWS g6.xlarge (GPU), por hora | US$ 1,368 | US$ 0,8048 | +70% | [M897, p. 18; M898, p. 32] |
| AWS p5.48xlarge (GPU H100), por hora | US$ 92,4672 | US$ 55,04 | +68% | [M897, p. 39; M898, p. 85] |
| GPT-5 na Azure, implantação global | US$ 1,25/US$ 10 | US$ 1,25/US$ 10 | Igual | [M958, p. 1] |

Na Azure, manter os dados nos EUA custa 10% a mais, e não apareceu opção equivalente para o Brasil [M958, p. 1].

**Câmbio e horário.** Os preços são em dólar [M968, p. 1; M958, p. 1], e nenhuma fonte catalogada mede o efeito do câmbio no custo de IA. O pico da DeepSeek vai das 01h às 04h e das 06h às 10h UTC [M924, p. 2]: o horário comercial de Brasília cai fora do pico, a meio preço (cálculo nosso).

**Redata.** A Lei 15.504, de 15/09/2026, suspende tributos federais na compra de equipamentos para data centers, com contrapartidas como 10% da capacidade para o mercado interno e energia renovável ou de baixa emissão [M603, p. 1-2, 4]; a suspensão dura cinco anos, e a renúncia estimada é de cerca de R$ 5,2 bilhões em 2026 (Agência Senado) [M196, p. 1]. Leitura nossa: barateia a construção de data centers no País, mas o efeito no preço da inferência ainda não é mensurável.

**Pesquisas brasileiras.** Custo é o 4º desafio para implementar IA, citado por 35% das empresas, atrás da falta de pessoal especializado (50%) (IDC/ABES, abr/2026) [M141, p. 26]. Na PINTEC do IBGE, altos custos foram a dificuldade mais citada (78,6%) pelas indústrias com 100 ou mais pessoas que usam tecnologias digitais avançadas, conjunto que inclui a IA [M186, p. 55-56].

## 10. Veredito sobre as hipóteses

Régua única: *confirmada*, evidência direta e consistente de mais de uma fonte; *em parte*, só parte da afirmação se sustenta ou há evidência contrária relevante; *não se confirma*, a evidência aponta no sentido oposto; *sem evidência suficiente*, faltam dados.

| Hipótese | Veredito | Evidência principal |
|---|---|---|
| H1. O preço do token vem caindo | Confirmada em parte | Mais de 280 vezes entre nov/2022 e out/2024 para desempenho constante [M230, p. 65]; não cai igual na ponta nem nos sucessores [M968, p. 1; M953, p. 4-5] |
| H1. Por isso, o custo não deve preocupar | Não se confirma | 82% dos executivos se preocupam com tokens [M070, p. 1-2]; o Gartner projeta alta do custo total [M948, p. 2]; estouro na Uber [M986, p. 2] |
| Sequência: o custo vira tema com o Claude e os seguintes | Confirmada em parte | Vira tema nas empresas em 2025–2026, com agentes como o Claude Code [M984, p. 2; M941, p. 3; M070, p. 1-2]; mas a ponta já era cara em 2023 [M970, p. 4] |
| Sequência: o DeepSeek derruba os preços | Confirmada em parte | Preço baixo e choque de mercado [M926, p. 2; M198, p. 74]; mas a guerra chinesa é de mai/2024 [M999, p. 2-3], a ligação com cortes americanos é só temporal [M964, p. 1], e a DeepSeek subiu preços [M924, p. 2] |
| Sequência: o Uber gasta o orçamento em quatro meses | Confirmada (imprensa de referência) | [M986, p. 2; M941, p. 3]; sem documento da empresa; o caso sustenta a H2, não a H1 |
| Sequência: o Jev derruba ainda mais o preço | Confirmada em parte, na sua categoria | É o mais barato entre os modelos de decisão, e a OpenAI lançou concorrente em 21 dias, segundo a imprensa inspirado nele [M990, p. 4; M955, p. 2, 6; M967, p. 1]; outra categoria, sem efeito medido nos preços dos modelos de conversa |
| Paralelo com os carros | Confirmada em parte | Entrada chinesa e guerra de preços reais [M938, p. 9; M962, p. 1]; Hilux em promoção [M913, p. 2]; quebra na quantidade |
| H2. O preço cai, mas a conta sobe | Confirmada | Volumes 5 a 7 vezes maiores em um ano (declarados) [M666, web; M701, web]; gasto com APIs mais que dobrado entre nov/2024 e meados de 2025 (estimativa) [M956, p. 1]; projeção do Gartner [M948, p. 2]; com gestão, a conta pode estabilizar (Uber, declarado) [M995, p. 2] |
| H3. A queda é desigual | Confirmada | De 9 a 900 vezes por ano conforme a tarefa [M933, p. 1]; topo a US$ 10/US$ 50 [M968, p. 1]; altas marcadas [M952, p. 3] |
| H4. Preço abaixo do custo, com risco de reajuste | Confirmada em parte | Prejuízo declarado num plano, custo absorvido pelo GitHub, limites semanais [M985, p. 2; M951, p. 2; M984, p. 2]; sem resultado oficial dos laboratórios |
| H5. O token é a menor parte da conta | Confirmada em parte | US$ 4 em pessoas e processos para cada US$ 1 em tecnologia [M003, p. 53]; as empresas mais satisfeitas gastam mais em dados, governança e talentos [M125, p. 3]; mas no uso agêntico intenso o token pesa [M989, p. 3], e ninguém mede a parcela |
| H6. O Brasil tem custo próprio | Confirmada em parte | Nuvem local mais cara (cálculo nosso) [M897, p. 63; M898, p. 81]; tributos em transição [M976, web]; o token global custa o mesmo [M958, p. 1]; câmbio sem medida |
| H7. O mais barato pode não ser utilizável | Confirmada em parte | Riscos apontados pelo governo americano [M853, p. 2]; residência de dados mais cara [M968, p. 3]; rodar modelo aberto exige GPU, com custo próprio (leitura nossa) [M982, p. 1]; sem política de empresa brasileira no catálogo |

## 11. Implicações para a estratégia de IA

Leitura nossa, macro.

- **O preço unitário não deve travar a IA; o consumo precisa de gestão.** A pergunta passa a ser quanto custa e quanto vale cada tarefa, o que completa a nota [Valor e retorno da IA](../02_frente-1_benchmark-estrategico/notas/valor-e-retorno-da-ia.md).
- **Orçar por consumo.** O orçamento tende a ter uma parte fixa, por usuário, e uma variável, por uso [M951, p. 1; M909, p. 11], com cenários de volume, de mix (raciocínio e agentes pesam mais) e de reajuste.
- **Medir custo e valor por tarefa.** Para o CAISI, o gasto por tarefa é a medida mais relevante [M853, p. 14]; a Uber acompanha o custo por sessão [M995, p. 2].
- **Gestão do gasto como capacidade do roadmap (Frente 2).** Proposta para o framework, dentro de governança:

| Estágio | Gestão do custo da IA |
|---|---|
| 1. Exploração | Gasto disperso em assinaturas; ninguém conhece o total |
| 2. Pilotos | Gasto por projeto; custo por usuário, não por tarefa |
| 3. Operacionalização | Painel de consumo por área, limites e alertas; modelo do tamanho da tarefa |
| 4. Escala | Custo e valor por tarefa medidos; orçamento por consumo; contratos com regras de reajuste e portabilidade |
| 5. Transformação | Gasto gerido como portfólio ligado a resultado; tarefas distribuídas entre modelos por custo e qualidade |

  Calibragem: o Gartner prevê que, até 2028, 60% das 500 maiores empresas do mundo terão controles de gasto na inferência [M659, web].
- **Risco de reajuste e de fornecedor.** O preço de tabela anda nos dois sentidos, promoções acabam, regras de plano mudam, e guerra de preço pode terminar em consolidação [M896, p. 2; M949, p. 1-2]. Usar vários modelos já é comum: 37% dos CIOs ouvidos pela a16z usam cinco ou mais, sobretudo porque cada um rende mais em certos usos; evitar a dependência de um fornecedor é outro motivo [M900, p. 4].
- **O efeito do Brasil.** O orçamento em reais herda o câmbio; processar dados em região brasileira custa mais; os tributos sobre serviço importado mudam a partir de 2027.
- **Para o cliente.** Uma agroindústria que estrutura a IA tende a começar com conta pequena, como a empresa americana mediana na base da Ramp (seção 5). O risco é o salto quando raciocínio e agentes ganham escala sem medida de valor; vale prever orçamento por consumo, custo por tarefa e limites desde os pilotos.

## 12. Números que não devem ser usados (ou só com ressalva)

| Afirmação | Problema | O que usar no lugar | Fonte |
|---|---|---|---|
| "O DeepSeek-V3 custou US$ 5,6 milhões para treinar" | Só o treino final, com aluguel suposto de US$ 2 por hora de GPU | Citar com a ressalva da empresa | [M928, p. 5] |
| "O preço da IA cai 10 (ou 280, ou 900) vezes por ano" | Capacidade fixa, bases diferentes; não vale para a ponta nem para a conta | Dizer a base (seção 4) | [M230, p. 65; M933, p. 1; M901, p. 2] |
| "O Jev derrubou o preço da IA" | Modelo de decisão; comparação da empresa entre categorias; preço sem data | Comparar na categoria | [M990, p. 4; M955, p. 6] |
| "Corte de 10% no preço dá só 0,5% mais uso" | Comparação entre modelos, não efeito de um corte ao longo do tempo | Retrato da segmentação | [M974, p. 30] |
| "O paradoxo de Jevons está comprovado" (Menlo) | Previsão de uma investidora da Anthropic, não medição | Volumes e gastos medidos | [M957, p. 17; M956, p. 7] |
| "As empresas gastaram US$ 37 bilhões com IA generativa" | Exclui inferência em nuvem, chips e IA embutida | Citar com o escopo | [M957, p. 2, 18] |
| "A OpenAI perdeu US$ 4,1 bilhões no trimestre" ou "deu lucro em 2026" | É a parcela da Microsoft; o ganho de 2026 vem de diluição | Não há resultado oficial da OpenAI | [M961, p. 9, 11; M960, p. 60] |
| "A Uber tem 5.000 engenheiros que gastam de US$ 500 a 2.000 por mês", "média de US$ 150 a 250", "sessão de US$ 1.200 do CTO", "Claude Code de 32% em fevereiro para 84% em março" | Sem fonte verificada; o último é leitura errada: 84% são usuários de programação agêntica | Quase 3.000 pessoas na tecnologia; Claude Code de 32% (dez/2025) para 63% (fev/2026) | [M989, p. 1-2] |
| "A Uber limita o gasto a US$ 1.500 por funcionário" | Teto noticiado em jun/2026; em ago/2026 a empresa descreve outro desenho | Dois desenhos em datas diferentes | [M986, p. 2; M995, p. 15] |
| "A Anthropic trocou a assinatura fixa por cobrança por uso" (Fortune) | Vale para o Enterprise; Pro e Max seguem fixos, com limites | Dizer o plano | [M941, p. 6; M909, p. 11] |
| "A Toyota cortou R$ 60 mil da Hilux por causa das chinesas" | Promoções por canal e prazo; sem declaração da Toyota; chinesas marginais no segmento | Canal, prazo e versão: de 14,2% a 23% | [M913, p. 1-4; M945, web; M997, p. 2; M938, p. 18] |

## 13. Lacunas

- **Causa dos cortes.** Nenhum laboratório americano atribuiu oficialmente um corte à concorrência.
- **Resultado dos laboratórios.** Não há margem nem prejuízo oficiais da OpenAI e da Anthropic.
- **Preço da GPU.** Não há série pública longa e gratuita.
- **Composição do custo (H5).** Nenhuma fonte mede a parcela dos tokens no custo total de projetos de IA.
- **Brasil.** Faltam o efeito do câmbio, a carga efetiva sobre APIs importadas, o enquadramento do IOF e dados da CNI e da FGV.
- **Uber.** O valor do orçamento não foi achado; a reportagem original é paga.
- **A catalogar.** Preços de lançamento do GPT-5.6, do Claude 3.5 Haiku e do DeepSeek V4 Pro (com desconto temporário na data da avaliação americana) e notas da DeepSeek de ago e set/2026, que conflitam com a tabela sobre o V4-Pro.
- **Séries recentes.** Não há atualização pública de 2026 da série de preço a desempenho constante.
- **Carros.** Não há cópia datada do preço de tabela oficial da Hilux, nem estudo institucional que compare as duas guerras de preço.
- **Agro.** Nenhuma fonte pública traz o custo de uso de IA em agroindústrias.

## Fontes

<!-- fontes:inicio -->
- **M003** — Bain & Company (2026). Technology Report 2026: AI, the Most Consequential Technology of Our Lifetimes. [link](https://www.bain.com/insights/topics/technology-report/) · citado em p. 53
- **M004** — Bain & Company (2026). Your AI Budget Is Growing. Your Returns Aren't. Here's Why. [link](https://www.bain.com/insights/your-ai-budget-is-growing-your-returns-arent-heres-why/) · citado em p. 2
- **M028** — McKinsey & Company (QuantumBlack) (2026). The state of AI in 2026: On the road to ROI. [link](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) · citado em p. 15
- **M070** — EY US (2026). EY Survey: C-Suites Pivot from AI Adoption to Unlocking Value as Escalating Token Costs Trigger Fiscal Scrutiny — US AI Pulse Survey, 5ª onda. [link](https://www.ey.com/en_us/newsroom/2026/07/ey-survey-c-suites-pivot-from-ai-adoption-to-unlocking-value-as-escalating-token-costs-trigger-fiscal-scrutiny) · citado em p. 1-2
- **M125** — Gartner (2026). The New AI Challenge Isn't Adoption. It's AI Spend. (The Real Threat to AI ROI Is Unchecked AI Spend). [link](https://www.gartner.com/en/articles/rein-in-ai-spend) · citado em p. 3
- **M141** — IDC / ABES (2026). Estratégias Digitais em Alta Performance: os vetores tecnológicos impulsionados pela IA (IDC para ABES). [link](https://abes.org.br/ia-impulsiona-nova-corrida-tecnologica-nas-empresas-brasileiras-aponta-estudo-inedito-da-abes/) · citado em p. 26
- **M170** — OpenAI (2025). The state of enterprise AI — 2025 Report. [link](https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf) · citado em p. 6
- **M186** — IBGE (com ABDI e UFRJ) (2025). Pesquisa de Inovação Semestral 2024 - Indicadores temáticos: Tecnologias digitais avançadas, teletrabalho e cibersegurança. [link](https://agenciadenoticias.ibge.gov.br/media/com_mediaibge/arquivos/58ab6f34051f3fa2b73b75cc6e926067.pdf) · citado em p. 55-56
- **M196** — Senado Federal (Agência Senado) (2026). Sancionada lei de incentivo à instalação de data centers (Lei 15.504/2026 — Redata). [link](https://www12.senado.leg.br/noticias/materias/2026/09/16/sancionada-lei-de-incentivo-para-a-instalacao-de-data-centers) · citado em p. 1
- **M198** — Stanford HAI (2026). Artificial Intelligence Index Report 2026. [link](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) · citado em p. 69, 74
- **M230** — Stanford HAI (2025). Artificial Intelligence Index Report 2025. [link](https://hai-production.s3.amazonaws.com/files/hai_ai_index_report_2025.pdf) · citado em p. 65
- **M603** — Presidência da República (Planalto) (2026). Lei nº 15.504, de 15 de setembro de 2026 (Redata — Regime Especial de Tributação para Serviços de Datacenter). [link](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15504.htm) · citado em p. 1-2, 4
- **M630** — Anthropic (2026). Covering electricity price increases from our data centers. [link](https://www.anthropic.com/news/covering-electricity-price-increases) · citado em p. 1-2
- **M659** — Gartner (2026 (15/09/2026)). Gartner Unveils Top Strategic Predictions for 2027 and Beyond (press release). [link](https://www.gartner.com/en/newsroom/press-releases/2026-09-15-gartner-unveils-top-strategic-predictions-for-2027-and-beyond) · citado em web
- **M666** — Google (Sundar Pichai) (2026 (19/05/2026)). Google I/O 2026: Sundar Pichai's opening keynote. [link](https://blog.google/intl/en-in/company-news/technology/sundar-pichai-io-2026/) · citado em web
- **M701** — Microsoft (Satya Nadella) (2025 (30/04/2025)). Microsoft Fiscal Year 2025 Third Quarter Earnings Conference Call. [link](https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q3) · citado em web
- **M832** — Stanford HAI e DigiChina (2025). Beyond DeepSeek: China's Diverse Open-Weight AI Ecosystem and Its Policy Implications. [link](https://hai.stanford.edu/assets/files/hai-digichina-issue-brief-beyond-deepseek-chinas-diverse-open-weight-ai-ecosystem-policy-implications.pdf) · citado em p. 3, 14
- **M852** — NIST – CAISI (EUA) (2026). CAISI Evaluation of DeepSeek V4 Pro. [link](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro) · citado em p. 2, 7
- **M853** — NIST – CAISI (EUA) (2025). Evaluation of DeepSeek AI Models. [link](https://www.nist.gov/document/caisi-evaluation-deepseek-ai-models-report) · citado em p. 2, 14, 66
- **M894** — ABES - Associação Brasileira das Empresas de Software (2025 (30/05/2025)). ABES critica aumento do IOF e alerta para impactos na inovação, competitividade e internacionalização do setor de software. [link](https://abes.org.br/abes-critica-aumento-do-iof-e-alerta-para-impactos-na-inovacao-competitividade-e-internacionalizacao-do-setor-de-software/) · citado em p. 1
- **M895** — Administração Estatal de Regulação do Mercado da China (SAMR) (2026). 市场监管总局关于发布《汽车行业价格行为合规指南》的公告 (2026年第10号) — Guia de conformidade de preços do setor automotivo. [link](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/jjjzs/art/2026/art_10120651065444b5b3b070dcae41e98a.html) · citado em p. 1, 3
- **M896** — AlixPartners (2026). The 23rd annual AlixPartners Global Automotive Outlook – China (comunicado de 30/06/2026). [link](https://www.alixpartners.com/newsroom/press-release-the-23rd-annual-alixpartners-global-automotive-outlook-china/) · citado em p. 2
- **M897** — Amazon Web Services (2026 (publicação de 12/10/2026)). AWS Price List — EC2 sob demanda, Linux, South America (São Paulo) (cópia datada). [link](https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/South%20America%20(Sao%20Paulo)/Linux/index.json) · citado em p. 18, 39, 63
- **M898** — Amazon Web Services (2026 (publicação de 12/10/2026)). AWS Price List — EC2 sob demanda, Linux, US East (N. Virginia) (cópia datada). [link](https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/US%20East%20(N.%20Virginia)/Linux/index.json) · citado em p. 32, 81, 85
- **M899** — Amazon Web Services (AWS News Blog) (2025 (05/06/2025)). Announcing up to 45% price reduction for Amazon EC2 NVIDIA GPU-accelerated instances. [link](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/) · citado em p. 1
- **M900** — Andreessen Horowitz (a16z) (2025 (10/06/2025)). How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025. [link](https://a16z.com/ai-enterprise-2025/) · citado em p. 4
- **M901** — Andreessen Horowitz (a16z) (2024). Welcome to LLMflation – LLM inference cost is going down fast. [link](https://a16z.com/llmflation-llm-inference-cost/) · citado em p. 2, 6
- **M903** — Anthropic (2026). Claude API — Pricing (versão Markdown oficial, consulta em 14/10/2026). [link](https://platform.claude.com/docs/en/about-claude/pricing) · citado em p. 1, 2
- **M904** — Anthropic (2026 (consulta em 14/10/2026)). How am I billed for my Enterprise plan? (Central de Ajuda do Claude). [link](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan) · citado em p. 2
- **M905** — Anthropic (2025). Introducing Claude Opus 4.5. [link](https://www.anthropic.com/news/claude-opus-4-5) · citado em p. 1-2, 2
- **M906** — Anthropic (2024). Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku. [link](https://www.anthropic.com/news/3-5-models-and-computer-use) · citado em p. 1
- **M907** — Anthropic (2024). Introducing the next generation of Claude. [link](https://www.anthropic.com/news/claude-3-family) · citado em p. 1, 7, 7-9, 8, 9
- **M908** — Anthropic (2023). Model Pricing — tabela de preços da Anthropic (jul/2023, cópia arquivada). [link](https://web.archive.org/web/20230802213320id_/https://www-files.anthropic.com/production/images/model_pricing_july2023.pdf) · citado em p. 1
- **M909** — Anthropic (2026 (consulta em 14/10/2026)). Plans & pricing (Claude). [link](https://claude.com/pricing) · citado em p. 11
- **M910** — Anthropic (2026 (consulta em 14/10/2026)). Steering thinking (custos e preços do raciocínio do Claude). [link](https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost) · citado em p. 6
- **M911** — Anthropic (Engineering) (2025 (13/06/2025)). How we built our multi-agent research system. [link](https://www.anthropic.com/engineering/multi-agent-research-system) · citado em p. 3
- **M912** — Artificial Analysis (2025). Artificial Analysis State of AI Q3 2025 – Highlights Edition. [link](https://artificialanalysiscdn.com/public-reports/state-of-ai-2025-q3-highlights-artificial-analysis.pdf) · citado em p. 10, 14
- **M913** — Auto+ TV (AutoMais) (2026). Toyota reduz preços de Hilux e SW4 em mais de R$ 54.000. [link](https://www.automaistv.com.br/novidades/toyota-reduz-precos-de-hilux-e-sw4-em-mais-de-r-54-000/) · citado em p. 1-4, 2, 3
- **M916** — BYD Brasil (2025). BYD inaugura em Camaçari a maior fábrica de veículos elétricos da América Latina e apresenta o primeiro carro super-híbrido plug-in flex fuel do mundo. [link](https://www.byd.com/br/noticias-byd-brasil/byd-inaugura-em-camacari-a-maior-fabrica-de-veiculos-eletricos-d) · citado em p. 5
- **M917** — Bruegel (2026). Growth without profits: how will 'involution' in China end? (Working Paper 01/2026). [link](https://www.bruegel.org/working-paper/growth-without-profits-how-will-involution-china-end) · citado em p. 11
- **M918** — CNBC (2025). Nvidia sheds almost $600 billion in market cap, biggest one-day loss in U.S. history. [link](https://www.cnbc.com/2025/01/27/nvidia-sheds-almost-600-billion-in-market-cap-biggest-drop-ever.html) · citado em p. 1
- **M919** — CPCA — Associação de Informação do Mercado de Carros de Passeio (ligada à Associação Chinesa de Revendedores de Automóveis) (2026). 【月度分析】2026年9月份全国乘用车市场分析 (Análise mensal do mercado de carros de passeio — setembro de 2026). [link](https://www.cpcaauto.com/newslist.php?types=csjd&id=4350) · citado em p. 4, 4-5
- **M920** — Comitê-Executivo de Gestão (Gecex) da Câmara de Comércio Exterior (Camex) — MDIC (2023). Ata da 209ª Reunião Ordinária do Gecex/Camex (10/11/2023) — versão pública. [link](https://www.gov.br/mdic/pt-br/assuntos/camex/atas/gecex/2023/ata-da-209a-reuniao-ordinaria-do-gecex.pdf) · citado em p. 1-3
- **M921** — Comitê-Executivo de Gestão (Gecex) da Câmara de Comércio Exterior (Camex) — MDIC (2026). Deliberações da 238ª Reunião Ordinária do Gecex (publicadas em 23/06/2026). [link](https://www.gov.br/mdic/pt-br/assuntos/camex/outros-documentos/deliberacoes/deliberacoes-da-238a-reuniao-ordinaria-do-comite-executivo-de-gestao-gecex) · citado em p. 22
- **M923** — Cursor (Anysphere) (2025 (04/07/2025)). Clarifying our pricing (Esclarecendo nossos preços). [link](https://cursor.com/blog/june-2025-pricing) · citado em p. 1-2
- **M924** — DeepSeek (2026). DeepSeek API — Models & Pricing (consulta em 14/10/2026). [link](https://api-docs.deepseek.com/quick_start/pricing) · citado em p. 1, 2
- **M925** — DeepSeek (2026). DeepSeek API — Models & Pricing (cópia arquivada de 02/07/2026). [link](https://web.archive.org/web/20260702051533/https://api-docs.deepseek.com/quick_start/pricing) · citado em p. 2
- **M926** — DeepSeek (2025). DeepSeek API — Models & Pricing (cópia arquivada de 15/03/2025, texto da página). [link](https://web.archive.org/web/20250315174458/https://api-docs.deepseek.com/quick_start/pricing) · citado em p. 1-2, 2
- **M927** — DeepSeek (2024). DeepSeek API — Pricing (cópia arquivada de 28/05/2024). [link](https://web.archive.org/web/20240528120559/https://platform.deepseek.com/api-docs/pricing/) · citado em p. 1
- **M928** — DeepSeek (2024). DeepSeek-V3 Technical Report (arXiv 2412.19437). [link](https://arxiv.org/abs/2412.19437) · citado em p. 5
- **M929** — DeepSeek (2025). Introducing DeepSeek-V3.2-Exp. [link](https://api-docs.deepseek.com/news/news250929) · citado em p. 1-3
- **M930** — Demarest Advogados (2025 (jul/2025)). Majoração do IOF — STF publica decisão cautelar restabelecendo a eficácia do Decreto nº 12.499/2025. [link](https://demarest.com.br/wp-content/uploads/2025/07/DEMAREST_Majoracao_IOF-Decisao_Cautelar_16_07_25_v2.pdf) · citado em p. 2, 4
- **M931** — Departamento de Comércio dos EUA — Bureau of Industry and Security (BIS), Federal Register (2025). Securing the Information and Communications Technology and Services Supply Chain: Connected Vehicles (Final rule, 90 FR 5360). [link](https://www.federalregister.gov/documents/2025/01/16/2025-00592/securing-the-information-and-communications-technology-and-services-supply-chain-connected-vehicles) · citado em p. 1-2
- **M933** — Epoch AI (2025). LLM inference prices have fallen rapidly but unequally across tasks (Data Insight). [link](https://epoch.ai/data-insights/llm-inference-price-trends) · citado em p. 1, 2-3
- **M934** — Epoch AI (2025 (17/04/2025)). LLM responses to benchmark questions are getting longer over time (Data Insight). [link](https://epoch.ai/data-insights/output-length) · citado em p. 1
- **M935** — Fenabrave (Federação Nacional da Distribuição de Veículos Automotores) (2024 (dados de 2023)). Informativo Emplacamentos — Resumo mensal de dezembro de 2023 (Ed. 252). [link](https://www.fenabrave.org.br/portal/files/2023_12_2.pdf) · citado em p. 9
- **M936** — Fenabrave (Federação Nacional da Distribuição de Veículos Automotores) (2025 (dados de 2024)). Informativo Emplacamentos — Resumo mensal de dezembro de 2024 (Ed. 264). [link](https://www.fenabrave.org.br/portal/files/2024_12_02.pdf) · citado em p. 9
- **M937** — Fenabrave (Federação Nacional da Distribuição de Veículos Automotores) (2026 (dados de 2025)). Informativo Emplacamentos — Resumo mensal de dezembro de 2025 (Ed. 276). [link](https://www.fenabrave.org.br/portal/files/2025_12_02.pdf) · citado em p. 9
- **M938** — Fenabrave (Federação Nacional da Distribuição de Veículos Automotores) (2026). Informativo Emplacamentos — Resumo mensal de setembro de 2026 (Ed. 285). [link](https://www.fenabrave.org.br/portal/files/2026_09_02.pdf) · citado em p. 9, 18
- **M941** — Fortune (2026 (26/05/2026)). Uber burned through its entire 2026 AI budget in four months. Now its COO is questioning whether it's worth it. [link](https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/) · citado em p. 3, 6
- **M942** — Fortune (com Bloomberg) (2025). Chinese EV stocks tumble after BYD slashes prices as much as 34%. [link](https://fortune.com/asia/2025/05/26/chinese-ev-stocks-tumble-after-byd-slashes-prices-as-much-as-34/) · citado em p. 2
- **M945** — Garagem360 (2026). Toyota Hilux 2026: Descontos para CNPJ superam R$ 64 mil e preço fica abaixo do Corolla Cross. [link](https://garagem360.com.br/toyota-hilux-2026-descontos-para-cnpj-superam-r-64-mil-e-preco-fica-abaixo-do-corolla-cross/) · citado em web
- **M947** — Gartner (2026 (26/01/2026)). Gartner Predicts GenAI Cost Per Resolution for Customer Service Will Exceed Offshore Human Agent Costs by 2030. [link](https://www.gartner.com/en/newsroom/press-releases/2026-01-26-gartner-predicts-genai-cost-per-resolution-for-customer-service-will-exceed-offshore-human-agent-costs-by-2030) · citado em p. 1
- **M948** — Gartner (2026 (25/03/2026)). Gartner Predicts That by 2030, Performing Inference on an LLM With 1 Trillion Parameters Will Cost GenAI Providers Over 90% Less Than in 2025. [link](https://www.gartner.com/en/newsroom/press-releases/2026-03-25-gartner-predicts-that-by-2030-performing-inference-on-an-llm-with-1-trillion-parameters-will-cost-genai-providers-over-90-percent-less-than-in-2025) · citado em p. 1, 2
- **M949** — Gartner (2026 (14/10/2026)). Gartner Says Over $3.5 Trillion of AI Infrastructure Spending Could Be Exposed to Impairment by the End of 2030. [link](https://www.gartner.com/en/newsroom/press-releases/2026-10-14-gartner-says-over-us-dollars-three-and-a-half-trillion-of-artificial-intelligence-infrastructure-spending-could-be-exposed-to-impairment-by-the-end-of-2030) · citado em p. 1-2
- **M951** — GitHub (Microsoft) (2026 (27/04/2026)). GitHub Copilot is moving to usage-based billing. [link](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) · citado em p. 1, 1-2, 2
- **M952** — Google (Google AI for Developers) (2026). Gemini Developer API pricing (consulta em 14/10/2026). [link](https://ai.google.dev/gemini-api/docs/pricing?hl=en) · citado em p. 3, 3-4, 4, 8-9
- **M953** — Google (Google AI for Developers) (2025). Gemini Developer API pricing (cópia arquivada de 20/07/2025, texto da página). [link](https://web.archive.org/web/20250720200308/https://ai.google.dev/gemini-api/docs/pricing) · citado em p. 4, 4-5, 5
- **M954** — Google (Google Developers Blog) (2024). Gemini 1.5 Flash price drop with tuning rollout complete, and more. [link](https://developers.googleblog.com/en/gemini-15-flash-updates-google-ai-studio-gemini-api/) · citado em p. 1
- **M955** — Let's Data Science (2026). OpenAI Shipped a Jev Rival in Three Weeks. TypeSafe Just Raised $870 Million. [link](https://letsdatascience.com/blog/openai-jev-rival-three-weeks-typesafe-raised-870-million) · citado em p. 2, 4, 6
- **M956** — Menlo Ventures (2025 (31/07/2025)). 2025 Mid-Year LLM Market Update: Foundation Model Landscape + Economics. [link](https://menlovc.com/perspective/2025-mid-year-llm-market-update/) · citado em p. 1, 5, 6-7, 7
- **M957** — Menlo Ventures (2025 (09/12/2025)). 2025: The State of Generative AI in the Enterprise. [link](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) · citado em p. 2, 17, 18
- **M958** — Microsoft (Azure) (2026 (consulta em 14/10/2026)). Azure Retail Prices API — Azure OpenAI GPT-5 em Brazil South e East US 2 (cópia datada). [link](https://prices.azure.com/api/retail/prices?$filter=%28armRegionName%20eq%20%27brazilsouth%27%20or%20armRegionName%20eq%20%27eastus2%27%29%20and%20contains%28productName%2C%20%27OpenAI%27%29%20and%20%28contains%28skuName%2C%20%27GPT%205%20Inpt%27%29%20or%20contains%28skuName%2C%20%27GPT%205%20outpt%27%29%29) · citado em p. 1
- **M960** — Microsoft (SEC) (2026 (29/07/2026)). Form 10-K — ano fiscal encerrado em 30/06/2026. [link](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323660/msft-20260630.htm) · citado em p. 37, 41, 60
- **M961** — Microsoft (SEC) (2025 (29/10/2025)). Form 10-Q — trimestre encerrado em 30/09/2025 (1º tri do ano fiscal 2026). [link](https://www.sec.gov/Archives/edgar/data/789019/000119312525256321/msft-20250930.htm) · citado em p. 9, 11
- **M962** — Ministério da Indústria e Tecnologia da Informação da China (MIIT), texto da agência Xinhua (2025). 关于汽车行业“价格战”等“内卷式”竞争，工业和信息化部作出回应 (MIIT responde sobre a 'guerra de preços' e a concorrência 'involutiva' no setor automotivo). [link](https://www.miit.gov.cn/xwfb/mtbd/wzbd/art/2025/art_68aafd9c515c47fbb64bcb5736890033.html) · citado em p. 1
- **M964** — OpenAI (2026). Advancing the price-performance frontier with GPT-5.6. [link](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/) · citado em p. 1, 1-3, 2
- **M965** — OpenAI (2023). Introducing ChatGPT and Whisper APIs (cópia arquivada de 01/03/2023). [link](https://web.archive.org/web/20230301180254/https://openai.com/blog/introducing-chatgpt-and-whisper-apis) · citado em p. 3, 8
- **M966** — OpenAI (2025). OpenAI API Pricing (cópia arquivada de 21/04/2025, texto da página). [link](https://web.archive.org/web/20250421013405/https://openai.com/api/pricing/) · citado em p. 2
- **M967** — OpenAI (2026). OpenAI API — Changelog (versão Markdown oficial, consulta em 14/10/2026). [link](https://developers.openai.com/api/docs/changelog) · citado em p. 1, 2-3, 4-5, 8, 11, 13, 13-14, 15-16, 17, 18
- **M968** — OpenAI (2026). OpenAI API — Pricing (versão Markdown oficial, consulta em 14/10/2026). [link](https://developers.openai.com/api/docs/pricing) · citado em p. 1, 3
- **M969** — OpenAI (2022). OpenAI API — página de preços (cópia arquivada de 01/12/2022). [link](https://web.archive.org/web/20221201044427/https://openai.com/api/pricing/) · citado em p. 2
- **M970** — OpenAI (2023). OpenAI — página de preços (cópia arquivada de 20/03/2023). [link](https://web.archive.org/web/20230320202742/https://openai.com/pricing) · citado em p. 4
- **M972** — OpenAI (2026 (consulta em 14/10/2026)). Reasoning models (guia da API). [link](https://developers.openai.com/api/docs/guides/reasoning) · citado em p. 6
- **M973** — OpenAI (2026 (18/01/2026)). Um negócio que escala com o valor da inteligência (A business that scales with the value of intelligence). [link](https://openai.com/pt-BR/index/a-business-that-scales-with-the-value-of-intelligence/) · citado em p. 4
- **M974** — OpenRouter Inc. e Andreessen Horowitz (a16z) (2025). State of AI: An Empirical 100 Trillion Token Study with OpenRouter (arXiv 2601.10088). [link](https://arxiv.org/abs/2601.10088) · citado em p. 1, 5, 13, 30, 32
- **M975** — Presidência da República (Planalto) (2003 (texto compilado consultado em 14/10/2026)). Lei Complementar nº 116, de 31 de julho de 2003 (ISS). [link](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp116.htm) · citado em web
- **M976** — Presidência da República (Planalto) (2025 (texto compilado consultado em 14/10/2026)). Lei Complementar nº 214, de 16 de janeiro de 2025 (IBS, CBS e Imposto Seletivo). [link](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm) · citado em web
- **M977** — Presidência da República (Planalto) (2004 (texto compilado consultado em 14/10/2026)). Lei nº 10.865, de 30 de abril de 2004 (PIS/Pasep-Importação e Cofins-Importação). [link](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l10.865.htm) · citado em web
- **M978** — Princeton University e coautores (HAL) (2025 (13/10/2025, arXiv 2510.11977)). Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation. [link](https://arxiv.org/abs/2510.11977) · citado em p. 1, 6-7
- **M979** — Ramp (Ramp Economics Lab) (2026 (12/08/2026)). August 2026 Ramp AI Index: Cracks in the AI thesis. [link](https://ramp.com/data/ai-index-august-2026) · citado em p. 5
- **M980** — Receita Federal do Brasil (Cosit) (2017 (DOU de 29/03/2017)). Solução de Consulta Cosit nº 191, de 23 de março de 2017 (IRRF e CIDE sobre Software as a Service). [link](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=81598&visao=anotado) · citado em p. 2
- **M981** — Rolim Goulart Cardoso Advogados (2025 (abr/2025)). E-book Reforma Tributária: aspectos práticos e oportunidades — Capítulo 4: IBS e CBS sobre importações e exportações. [link](https://painel-website.rolim.com/wp-content/uploads/2025/04/Capitulo-4-IBS-e-CBS-sobre-Importacoes-e-Exportacoes-1.pdf) · citado em p. 4-5
- **M982** — Silicon Data (2026 (consulta em 14/10/2026; leitura de 13/10/2026)). H100 Rental Price Index — SDH100RT. [link](https://www.silicondata.com/products/silicon-index/h100) · citado em p. 1
- **M983** — Supremo Tribunal Federal (STF) (2025 (13/08/2025)). RE 928.943 (Tema 914) — CIDE-Tecnologia: informação à sociedade. [link](https://www.stf.jus.br/arquivo/cms/noticiaNoticiaStf/anexo/InfoSociedadeRE928943.pdf) · citado em p. 1
- **M984** — TechCrunch (2025 (28/07/2025)). Anthropic unveils new rate limits to curb Claude Code power users. [link](https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/) · citado em p. 2
- **M985** — TechCrunch (2025 (05/01/2025)). OpenAI is losing money on its pricey ChatGPT Pro plan, CEO Sam Altman says. [link](https://techcrunch.com/2025/01/05/openai-is-losing-money-on-its-pricey-chatgpt-pro-plan-ceo-sam-altman-says/) · citado em p. 2
- **M986** — TechCrunch (2026 (02/06/2026)). Uber caps employee AI spending after blowing through budget in 4 months. [link](https://techcrunch.com/2026/06/02/uber-caps-employee-ai-spending-after-blowing-through-budget-in-four-months/) · citado em p. 2
- **M987** — Tencent AI Lab e Shanghai Jiao Tong University (2024 (dez/2024)). Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs. [link](https://arxiv.org/abs/2412.21187) · citado em p. 2
- **M989** — The Pragmatic Engineer (newsletter), sobre palestra de engenheiros da Uber no Pragmatic Summit (2026 (10/03/2026, atualizado em 11/03/2026)). How Uber uses AI for development: inside look. [link](https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development) · citado em p. 1-2, 3
- **M990** — TypeSafe AI (2026). Introducing System One Models & Jev. [link](https://typesafe.ai/blog/introducing-system-one-models-and-jev) · citado em p. 1-2, 4, 7
- **M991** — TypeSafe AI (2026). TypeSafe A raises Series AI. [link](https://typesafe.ai/blog/series-ai) · citado em p. 1-2
- **M992** — U.S.-China Economic and Security Review Commission (USCC) (2026). Two Loops: How China's Open AI Strategy Reinforces Its Industrial Dominance (Research Working Group Paper). [link](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf) · citado em p. 8, 8-9, 9
- **M995** — Uber Technologies (Uber Engineering) (2026 (27/08/2026)). Running a Software Factory Efficiently at Uber Scale (blog de engenharia). [link](https://www.uber.com/us/en/blog/efficient-software-factory/) · citado em p. 2, 15, 16
- **M997** — Vrum (Diários Associados / Estado de Minas) (2026). Toyota oferece 23% de desconto na Hilux durante a Agrishow 2026. [link](https://www.vrum.com.br/bom-negocio/2026/04/7408726-toyota-oferece-23-de-desconto-na-hilux-durante-a-agrishow-2026.html) · citado em p. 2, 2-3
- **M998** — War on the Rocks (2026). Forged in a Knife Fight: China's Brutal Domestic AI Competition. [link](https://warontherocks.com/cogs-of-war/forged-in-a-knife-fight-chinas-brutal-domestic-ai-competition/) · citado em web
- **M999** — Yicai Global (Yicai Media Group) (2024). Baidu Follows Alibaba's Steep LLM Price Cut With Two Free Ernie Bot Models. [link](https://www.yicaiglobal.com/news/baidu-offers-two-ernie-models-for-free-as-chinese-llm-market-ushers-in-price-war) · citado em p. 2-3
<!-- fontes:fim -->
