# IA e impacto ambiental — nota temática

> Documento interno de trabalho da equipe OagronomIA · Fontes públicas · Data de corte: 01/10/2026 · Base para trechos do relatório do benchmark (Frentes 1, 2 e 3) · Não é entregável e não deve ser encaminhado ao cliente sem revisão.

**Como ler.** Todo número traz unidade, escopo, ano e fonte [n] (lista numerada no fim). Só entram números confirmados na verificação de fontes ou conferidos diretamente no PDF da fonte primária durante a redação (ver a nota de verificação, ao final). O que não pôde ser conferido aparece com a ressalva "não conferido" ou na seção 11. "Cálculo nosso" marca conta da equipe sobre dados publicados; "leitura nossa", interpretação da equipe. Siglas: **LB** (*location-based*, fator médio da rede onde a energia é consumida) e **MB** (*market-based*, fator dos contratos e certificados de energia comprados); Gt = bilhões de toneladas; Mt = milhões de toneladas; kt = mil toneladas; MTok = milhão de tokens; EJ = exajoule. PUE, WUE, as demais métricas e as conversões de unidade estão na seção 5. Ao levar um número para entregável, registrar a fonte em `06_fontes/`.

## 1. Resumo em uma página

**O contexto.** Na Semana do Clima de Nova York de 2026, durante a Assembleia Geral da ONU, a IA foi "o tema incontornável", relata a MIT Technology Review Brasil [1]. O secretário-geral da ONU, António Guterres, resumiu a ambiguidade: a IA "pode ajudar a resolver todos esses desafios ou pode agravá-los". O chefe de clima da ONU, Simon Stiell, foi mais duro: os líderes da IA "estão agora em terreno frágil no que diz respeito à licença para operar" e precisam mostrar "por que os benefícios da IA superam seus custos crescentes" [1]. A coluna registra a alta das emissões de Microsoft, Google e Meta, em grande parte pela IA, e a entrada de muito gás natural para atender os data centers, em usinas que duram décadas. Traz ainda um dado que interessa a quem produz combustível renovável: o capital de risco em tecnologias climáticas cresceu, puxado por produtos para data centers, enquanto o investimento de risco em gestão de carbono e em combustíveis de baixo carbono "despencou" em 2026 — soluções que "talvez não consigam se vender para um data center" [1]. (A coluna cita US$ 26 bilhões em capital de risco climático no 1º semestre de 2026, +55% no ano, com dados da Currence; não conferido na fonte primária.)

**A tensão entre pegada e benefício.**
- **Pegada:** os data centers consumiram cerca de 485 TWh em 2025 (+17% no ano; +50% nos focados em IA) e devem chegar a cerca de 950 TWh em 2030, perto de 3% da eletricidade mundial. As emissões associadas, pelo mix físico da rede (LB), devem dobrar até 2035, para cerca de 350 Mt CO₂ [33].
- **Benefício:** a adoção ampla de aplicações de IA que já existem reduziria cerca de 1,4 Gt CO₂ em 2035, cerca de quatro vezes os 350 Mt projetados para os data centers no mesmo ano (cálculo nosso; com a projeção anterior, de 300 Mt, a IEA falava em quase cinco vezes). A IEA ressalva, porém, que "não há momentum" para essa adoção e que a conta não inclui o efeito rebote [32][33].
- **Saldo:** não existe saldo líquido medido. Modelos sérios chegam a sinais opostos (seção 9).

**As ordens de grandeza.**
- Uma consulta de texto simples gasta de 0,2 a 0,4 Wh nas divulgações de 2025-2026 [7][8][10], cerca de dez vezes menos que os "3 Wh" ainda repetidos [5].
- O tipo de uso pesa mais que o número de consultas. Modelos com raciocínio gastam, em média, 30 vezes mais energia de GPU, e um agente com raciocínio chega a 50 Wh de GPU por tarefa [12][33].
- A água por consulta vai de 0,26 mL (Gemini, só o resfriamento no local) a 45 mL (Mistral, ciclo de vida, com a água da geração elétrica e da fabricação). A diferença vem sobretudo da fronteira da medição, não da eficiência [7][17].
- Treinar uma família de modelos emite de dezenas a milhares de toneladas de CO₂e. O Llama 3.1, por exemplo, emitiu 11.390 tCO₂e pelo método LB e zero pelo MB [23].
- As emissões operacionais dos quatro maiores hiperescaladores (escopos 1 e 2 LB) ficaram, em 2024, entre 192% e 239% do nível de 2020 [41]. A energia por prompt do Gemini caiu 33 vezes em um ano, mas a eletricidade do Google subiu 37% em 2025 [7][49].
- A mesma consulta emite de cerca de 5 a 7,6 vezes menos se for processada no Brasil em vez de nos EUA, conforme o fator de emissão usado (seção 5.5). A ressalva é o "se": boa parte das cargas brasileiras roda no exterior.

**O que as empresas fazem.** Medir ainda é minoria, mas a prática cresce. Em 2024, 12% das grandes empresas que já usavam IA generativa mediam a sua pegada; em 2026, 38% medem a energia e 34% o carbono da IA, em amostras diferentes [58][59]. Só 18% têm metas mensuráveis específicas para IA [60]. As práticas que se repetem são cinco: escolher o modelo do tamanho da tarefa, otimizar a inferência, escolher a região de nuvem, reportar pelos métodos LB e MB lado a lado e cobrar dados dos fornecedores. O gargalo é a transparência: em maio de 2025, 84% dos tokens dos 20 modelos mais usados numa grande plataforma de API foram para modelos sem nenhuma divulgação ambiental [2].

**Por que importa para uma empresa de combustíveis renováveis.**
- **Coerência:** ela vende redução de emissões medida e certificada, e a IA entra no seu inventário (escopos 2 e 3) e na sua narrativa.
- **Escala:** a ordem de grandeza do uso corporativo é pequena. Mil usuários frequentes somam de dezenas de quilos a cerca de dez toneladas de CO₂e por ano, conforme o tipo de uso e a rede (seção 5.5).
- **Risco:** usar números errados, alegar "IA verde" sem lastro ou não ter resposta quando um comprador, financiador ou auditor perguntar.
- **Vantagem:** o setor já domina a linguagem que a pegada da IA começa a exigir: ACV, intensidade de carbono por unidade funcional e verificação de terceira parte.
- **Oportunidade:** big techs já usam diesel renovável em data centers e compram certificados de SAF e de diesel renovável para o escopo 3 [49][52][53][54].

## 2. Por que o tema importa para o cliente

Leitura macro, feita com fontes públicas. Não é diagnóstico interno.

**Identidade e coerência da narrativa.** Uma empresa de combustíveis renováveis existe para reduzir as emissões de outros setores, como a aviação e o transporte pesado, e é remunerada por essa redução. Quando ela adota IA em escala no campo, na indústria e na gestão, a pergunta "e a pegada da sua IA?" tende a chegar, porque o tema está no centro do debate climático [1]. A resposta não precisa ser "zero". Precisa ser medida, com método declarado e números certos. Nem as big techs têm resposta confortável: o Google chama suas metas climáticas de "moonshots" [49], e a SAP diz que não está claro se a demanda de energia da IA e da nuvem poderá ser coberta integralmente com renováveis e que avalia se a sua meta de net zero em 2030 precisará de ajustes [68].

**Reporte de emissões (escopos 2 e 3).**
- **IA consumida como serviço** (nuvem, API, assistentes dentro de softwares contratados): entra no escopo 3, em geral na categoria 1, bens e serviços adquiridos [66]. Os grandes provedores de nuvem entregam relatórios mensais de emissões por cliente, mas a metodologia publicada ainda não separa os serviços de IA generativa [66].
- **IA em servidores próprios:** entra no escopo 2 (eletricidade) e, pela fabricação do hardware, no escopo 3 (categoria 2, bens de capital).
- **Regra brasileira:** o Programa Brasileiro GHG Protocol exige o escopo 2 pela abordagem de localização, com o fator médio do SIN, e aceita a de escolha de compra (MB) só como relato adicional [86].
- **Mercado de capitais:** a CVM tornou voluntário o relatório de sustentabilidade no padrão ISSB (normas CBPS) para exercícios a partir de 2026. A partir de 2027, a companhia aberta que não o arquivar deve justificar a escolha ("pratique ou explique") [85]. Para empresas fechadas, a pressão vem de compradores, financiadores e certificadoras.

**Certificações de carbono do setor.** Os programas que dão valor ao combustível renovável medem a intensidade de carbono por ACV:
- **RenovaBio:** a RenovaCalc calcula a intensidade em gCO₂e/MJ, do poço à roda, com certificação de terceira parte. A média certificada do etanol hidratado de cana é de 28,07 gCO₂e/MJ, contra 87,40 da gasolina (posição em 02/10/2025). A calculadora já cobre o SAF [109].
- **ISCC, CORSIA e programas dos EUA:** seguem a mesma lógica de ACV e verificação.

Leitura nossa: a pegada da IA corporativa tende a ficar fora da fronteira da intensidade certificada do combustível, que olha para o processo produtivo, mas entra no inventário da empresa. O ponto central é de linguagem. Unidade funcional, fronteira, fator de emissão e verificação independente formam o vocabulário que a pegada da IA começa a exigir (gCO₂e por consulta, kgCO₂e por milhão de tokens), e o setor já o pratica.

**Risco reputacional.** O risco não está na ordem de grandeza, mas no uso:
- repetir números errados, como "500 mL por pergunta" ou "10 vezes uma busca no Google", em material público (seção 11);
- alegar "IA 100% renovável" com base em certificados anuais, sem lastro horário e local (seção 5);
- abater do inventário as "emissões evitadas" por aplicações de IA, o que o guia do WBCSD não admite [87];
- associar a marca a data centers contestados. O CONAMA pediu diretrizes nacionais de licenciamento para data centers de IA, e o MPF e a DPU questionaram o licenciamento simplificado de um data center no Pecém (CE) [96][97].

**A vantagem da matriz elétrica brasileira, com três ressalvas.** As renováveis responderam por 86,8% da eletricidade do país em 2025 [90]. O fator médio do SIN foi de 46,1 gCO₂/kWh em 2025 [89], contra cerca de 350 gCO₂e/kWh na média dos EUA [44] e 435 gCO₂/kWh na média mundial [34], fatores calculados por métodos diferentes (seção 5.4). Mas:
1. a vantagem só vale se o processamento ocorrer no Brasil. O governo estima que cerca de 60% das cargas digitais nacionais são atendidas no exterior [93], e as consultas a modelos de fronteira tendem a rodar fora do país (leitura nossa);
2. a matriz hidrelétrica reduz o carbono, não necessariamente a água. Pelo método do WRI, que atribui à geração toda a evaporação dos reservatórios, a eletricidade brasileira tem o maior fator de consumo de água entre os países analisados: 4,91 galões/kWh, cerca de 18,6 L/kWh, com o mix de geração de 2016. O próprio WRI ressalva que o país tem baixo estresse hídrico no agregado nacional [46];
3. o fator oscila com a chuva (126,3 gCO₂/kWh em 2021, ano de crise hídrica) [89]. E, em rede limpa, o carbono incorporado na fabricação do hardware pesa mais (seção 3).

**Oportunidade de mercado.** A expansão dos data centers e as metas de emissão das big techs também criam demanda para o setor:
- a Microsoft usa diesel renovável (HVO) no lugar do diesel fóssil em cerca de 60% dos seus data centers na Europa e abate certificados de SAF no escopo 3 de viagens e de frete aéreo [52][53];
- o Google usou diesel renovável em máquinas e geradores de obras de data centers na América do Norte em 2025 e usa certificados de SAF para parte das emissões do transporte aéreo dos seus produtos [49];
- a Amazon comprou 3,6 milhões de galões de diesel renovável em 2025 para a frota de veículos ainda não eletrificada (não para data centers), 1,1 milhão a menos que em 2024 por falta de disponibilidade, e aplica certificados de SAF e de diesel renovável [54].

São sinais pequenos, mas mostram a IA e o combustível renovável no mesmo inventário.

## 3. O que a ciência mede

### 3.1 Energia e carbono por consulta: a evolução das estimativas

| Quando | Estimativa | O que mede | Status |
|---|---|---|---|
| 2009 | 0,3 Wh (0,0003 kWh) e cerca de 0,2 g CO₂ por busca no Google | busca sem IA generativa, incluindo a construção do índice; divulgação sem método | dado de 17 anos, nunca atualizado [4] |
| 2023 | 2,9 Wh por requisição ao ChatGPT ("10 vezes uma busca") | estimativa de terceiros para o GPT-3.5 em servidores A100 a plena potência | superado [5][6] |
| fev/2025 | cerca de 0,3 Wh por consulta típica ao GPT-4o; cerca de 2,5 Wh com 10 mil tokens de entrada; cerca de 40 Wh com 100 mil | estimativa *bottom-up* da Epoch AI | estimativa independente, não medição [9] |
| mai/2025 | 0,24 Wh, 0,03 gCO₂e e 0,26 mL por prompt de texto mediano do Gemini | medição em produção: acelerador, CPU e memória, máquinas ociosas e overhead do data center; carbono MB; água só no local | confirmado; não verificado de forma independente [7] |
| jun/2025 | 0,34 Wh e cerca de 0,32 mL por consulta média ao ChatGPT | declaração do CEO, sem método, modelo ou fronteira | citar como "declarado pela OpenAI" [8] |
| 2026 | 0,31 Wh por consulta típica (intervalo interquartil de 0,16 a 0,60); 3,91 Wh com raciocínio longo (consultas 15 vezes mais longas) | modelos com mais de 200 bilhões de parâmetros em GPUs H100, com PUE; estimativa revisada por pares, não medição | confirmado na versão publicada; a de 2025 dizia 0,34 e 4,32 Wh [10] |

O que essa evolução ensina:
- **A fronteira muda o número.** O mesmo prompt mediano do Gemini consome 0,10 Wh contando só o acelerador ativo e 0,24 Wh com CPU, memória, máquinas ociosas e overhead do data center [7].
- **O método do carbono também.** Os 0,03 gCO₂e do Gemini são cerca de 0,02 g de eletricidade MB (fator de 94 gCO₂e/kWh em 2024) mais 0,01 g dos escopos 1 e 3, que incluem a fabricação do hardware. Com o fator LB do próprio Google (345 gCO₂e/kWh) e os mesmos 0,01 g, o prompt teria cerca de 0,09 gCO₂e (cálculo nosso) [7].
- **A queda é rápida.** Entre maio de 2024 e maio de 2025, a energia do prompt mediano caiu de 7,92 para 0,24 Wh (33 vezes) e o carbono, de 1,32 para 0,03 gCO₂e (44 vezes). A queda de energia veio de software: 23 vezes de melhorias de modelo e 1,4 vez de melhor utilização das máquinas. A energia limpa só entra na queda do carbono [7][49].
- **O número cobre pouco.** As divulgações tratam de texto. Não cobrem imagem, vídeo, raciocínio longo nem agentes, e o Google informa que as estimativas por prompt não foram verificadas de forma independente [7].

### 3.2 Por tarefa: o tipo de uso domina

| Tarefa | Energia | Escopo | Fonte (ano) |
|---|---|---|---|
| Classificar texto / gerar texto / gerar imagem (médias) | 0,002 / 0,047 / 2,907 kWh por 1.000 inferências, ou seja, 0,002 / 0,047 / 2,9 Wh por inferência | modelos abertos em GPU A100, sem PUE; variação de mais de 1.450 vezes entre tarefas | [14] (2024) |
| Modelo de linguagem médio / mistura de especialistas grande / agente / modelo com raciocínio / agente com raciocínio | 0,05 / 0,31 / 1,14 / 7,6 / 50 Wh por tarefa | só energia de GPU, modelos abertos em condições padronizadas; valores indicativos | [33][12] (2026) |
| Com raciocínio × sem raciocínio | 30 vezes mais energia, em média; de 154 a 697 vezes ao ligar o raciocínio no mesmo modelo | energia de GPU por 1.000 consultas | [12] (2025) |
| Agentes de vários passos × consulta única | 62 a 136 vezes mais energia por consulta | energia de GPU medida (Llama 3.1 8B e 70B) | [15] (2025) |
| Vídeo gerado a partir de texto | de 0,14 Wh a mais de 415 Wh por vídeo | 7 modelos abertos em GPU H100 | [16] (2025) |
| Consultas a modelos comerciais via API | de 0,42 Wh (GPT-4o, consulta curta) a 29,1 Wh (DeepSeek-R1, consulta longa, servidores próprios); GPT-5 de 0,67 a 33,8 Wh | estimativa por latência e vazão, não medição | [13] (2025) |

Leitura: o que define a pegada de uma empresa usuária não é quantas consultas ela faz, mas que tipo de uso. Um fluxo agêntico com raciocínio pode custar centenas de vezes uma pergunta simples. Medições de laboratório e estimativas por API têm fronteiras diferentes das divulgações de produção: vale usar as razões entre tarefas, não os valores absolutos.

### 3.3 Treino × inferência

- **Treinos documentados:**
  - GPT-3: 1.287 MWh e 552 tCO₂e (estimativa de terceiros, 2021, só operação, LB com o fator médio dos EUA) [20];
  - BLOOM 176B: 24,7 tCO₂e contando só a energia dinâmica e 50,5 t com ociosidade e carbono incorporado (LB, rede francesa, 2023) [22];
  - família Llama 3.1: 39,3 milhões de horas de GPU H100, 11.390 tCO₂e LB e zero MB (2024) [23];
  - Llama 4 Scout e Maverick: 1.999 tCO₂e LB (2025) [23].
- **O que fica de fora:** experimentos e ajustes equivalem a cerca de metade do impacto do treino final e quase nunca são divulgados. A série OLMo somou pelo menos 493 tCO₂e (LB) e 2,769 milhões de L de água, com fabricação, desenvolvimento e treinos finais (2025) [24]. Os desenvolvedores de modelos fechados de fronteira não divulgam energia nem emissões de treino.
- **A divisão entre treino e inferência:** os únicos dados medidos são antigos. Cerca de 3/5 da energia de aprendizado de máquina do Google foi para inferência em 2019-2021 [21], e a Meta dividia a capacidade de potência da sua IA na proporção 10:20:70 entre experimentação, treino e inferência (dado publicado em 2022) [25]. A IEA afirma que o balanço "já migrou decisivamente do treino para a inferência", sem percentual público [33].
- **Implicação:** para uma empresa usuária, a inferência (o uso) é a parte que ela controla. O treino entra como fração amortizada, em linha separada (seção 5).

### 3.4 Água

Três distinções organizam o tema:
- **retirada × consumo:** retirada é a água captada, em grande parte devolvida; consumo é a que evapora ou não volta;
- **direta × indireta × incorporada:** direta é a do resfriamento no local; indireta, a da geração da eletricidade; incorporada, a da fabricação dos chips;
- **volume × estresse hídrico:** um litro numa bacia sob estresse vale mais que um litro numa bacia abundante.

Os números:
- **GPT-3 em data centers da Microsoft nos EUA:** 16,9 mL por resposta média, sendo 2,2 mL no local e 14,7 mL na geração da eletricidade (cerca de 87% indireta); 500 mL a cada 10 a 50 respostas médias; treino com 5,4 milhões de L, dos quais 0,7 milhão no local (versão revisada, 2025) [18].
- **Divulgações por consulta:** 0,26 mL no Gemini, só no local, com WUE de 1,15 L/kWh [7]; de 0 a 0,067 mL de água de resfriamento na Microsoft [11]; cerca de 0,32 mL no ChatGPT, declarados [8]; 45 mL por resposta de 400 tokens na Mistral, por ACV com geração e fabricação [17]. Os números não são comparáveis entre si.
- **Ilustração (cálculo nosso):** somando ao prompt do Gemini a água indireta média da eletricidade dos data centers dos EUA (4,52 L/kWh [35]), seria cerca de 1,1 mL a mais.
- **Agregado:** todos os data centers consumiram cerca de 560 bilhões de L em 2023, dois terços na geração de energia, e podem chegar a cerca de 1.200 bilhões em 2030 [32]. É um piso: a intensidade indireta implícita nessa conta (1,04 L/kWh) fica bem abaixo dos dados de empresas nos EUA (3,40 L/kWh) [40]. Só os sistemas de IA podem ter consumido de 312,5 a 764,6 bilhões de L em 2025 [40].
- **Risco local:** no ano fiscal de 2025, 48% do consumo de água da Microsoft (3.926 megalitros) ocorreu em áreas com estresse hídrico [52].

### 3.5 Carbono incorporado e lixo eletrônico

- **Fabricação:** 1.312 kgCO₂e por placa HGX H100 e 2.274 kgCO₂e por HGX B200, cada uma com 8 GPUs, do berço ao portão. Equivale a cerca de 164 e 284 kg por GPU (cálculo nosso). A memória HBM responde por 42% e 49% do total [26].
- **Peso no ciclo de vida:** nos TPUs do Google, a operação responde por cerca de 90% das emissões em 6 anos pelo método LB e por cerca de 70% pelo MB; o resto é fabricação [27]. Quanto mais limpa a energia, maior o peso da fabricação.
- **Consequência em rede limpa:** trocar uma GPU por outra "mais eficiente" pode levar mais de 7 anos para compensar a fabricação na França, contra 8 meses nos EUA, e algumas trocas não compensam [28]. Leitura nossa, por analogia com a rede francesa: no Brasil, a vida útil do hardware vira alavanca.
- **Lixo eletrônico:** os servidores de IA podem gerar de 131 a 224,8 mil toneladas por ano em 2030, volume comparável ao lixo eletrônico anual de Dinamarca, Noruega ou Áustria [29]. Para comparação, o mundo gerou 62 milhões de toneladas de lixo eletrônico em 2022, com 22,3% de coleta e reciclagem documentadas [31].

### 3.6 Efeito rebote

- **Ganho por unidade, consumo total em alta.** A energia por prompt mediano do Gemini caiu 33 vezes entre maio de 2024 e maio de 2025 [7]. Enquanto isso, os tokens processados pelo Google subiram de 9,7 trilhões por mês (2024) para mais de 3,2 quatrilhões (2026), cerca de 330 vezes (cálculo nosso) [51], e a eletricidade e a água da empresa cresceram 37% e 34% em 2025 [49]. É um padrão descritivo, sem prova de causalidade.
- **A IEA trata o paradoxo de Jevons como razão para o consumo total da IA subir no curto prazo**, mesmo com ganhos de 30% a 40% ao ano no desempenho por watt dos aceleradores [33].
- **Na economia como um todo,** um impulso de PIB pela IA elevaria a demanda global de energia em 0,9% a 2,6% (6 a 19 EJ) em 2035 [33].
- **No debate científico,** Luccioni, Strubell e Crawford argumentam que perguntar se a IA é "positiva ou negativa" para o clima é inadequado sem tratar o rebote [3].

## 4. A escala agregada

**Mundo.**
- **Consumo dos data centers:** cerca de 415 TWh em 2024 (cerca de 1,5% da eletricidade mundial) e 485 TWh em 2025, alta de 17%. Os data centers focados em IA cresceram 50% (dado preliminar de 2025) [32][33].
- **Projeção:** cerca de 950 TWh em 2030 no caso base da IEA, perto de 3% da demanda mundial, numa faixa de 833 a 1.008 TWh entre cenários. Os data centers focados em IA mais que triplicam, para cerca de 465 TWh. Os data centers respondem por pouco menos de 10% do crescimento da demanda elétrica mundial até 2030 [33].
- **Parcela da IA hoje:** só existe por aproximação. A IEA usa os servidores acelerados como proxy: 15% da demanda dos data centers em 2024 [32]. O EPRI, citando a IEA e a consultoria JLL, usa de 15% a 25% [37]. Uma revisão crítica de mais de 100 estudos situa a IA em 10 a 50 TWh em 2023 e considera plausíveis 200 a 400 TWh em 2030, de 35% a 50% do consumo dos data centers [38]. A mesma revisão traz, em outra página, outra faixa para 2023 (30 a 50 TWh).
- **Projeções divergentes:** o Gartner projeta mais de 1.200 TWh em 2030, depois de rever sua própria projeção de 980 TWh em sete meses, sem método público [39]. Deve ser tratado como cenário.

**EUA, centro da expansão.**
- **LBNL:** 192 TWh em 2024 (4,7% da eletricidade do país) e 649 TWh em 2030 (11,8%) no cenário de referência, numa faixa de 521 a 843 TWh (9,5% a 15,3%). Os servidores de IA chegam a 55% do consumo dos data centers em 2030 [36].
- **EPRI:** de 9% a 17% da eletricidade dos EUA em 2030 (380 a 790 TWh, incluindo criptomoedas), cerca de 60% acima da sua estimativa de 2024 [37].

**Emissões.**
- **Data centers:** cerca de 180 Mt CO₂ em 2024 (0,5% das emissões de combustão), dobrando para cerca de 350 Mt em 2035, cerca de 2% das emissões do setor elétrico. A conta usa o mix físico da rede (equivale ao LB) e exclui os geradores de reserva e o carbono incorporado [32][33].
- **Só os sistemas de IA:** de 32,6 a 79,7 Mt CO₂ em 2025, só operação, com a intensidade média da rede; estimativa por cenário com incerteza alta [40].
- **Empresas digitais:** as 163 empresas que reportaram eletricidade consumiram 494 TWh em 2024 (1,7% da eletricidade mundial). O conjunto monitorado emitiu 301 Mt CO₂e nos escopos 1 e 2 LB (0,8% das emissões ligadas à energia); pelo método MB, as emissões caem para cerca de um terço disso [41].

**Fontes de energia.**
- **Mix físico em 2024:** a eletricidade consumida pelos data centers veio cerca de 30% do carvão, 27% de renováveis, 26% do gás e 15% da nuclear [32].
- **Até 2030:** gás e carvão atendem mais de 40% da demanda adicional [32]. Em 2030, as renováveis chegam a cerca de 360 TWh, mais de um terço da geração para data centers; o gás mais que dobra, para cerca de 340 TWh; a nuclear sobe de cerca de 75 para quase 120 TWh [33].
- **Fontes novas chegam devagar:** os acordos de pequenos reatores modulares para data centers passaram de cerca de 25 GW (fim de 2024) para 45 GW (fim de 2025), mas os primeiros projetos só devem operar por volta de 2030. Entre 15 e 27 GW de gás gerado no próprio local podem abastecer data centers em 2030, sobretudo nos EUA. O setor de tecnologia respondeu por cerca de 40% dos PPAs corporativos de renováveis assinados em 2025 [33].
- **Contrato anual não é energia limpa na hora:** a energia solar contratada para cobrir 100% do consumo anual atende, em média, de 35% a 45% da demanda horária de um data center [32].

## 5. Métricas de pegada de carbono, energia e água

Esta é a seção prática da nota. Ela responde a três perguntas: o que se mede, como se calcula e qual valor de referência existe.

### 5.1 Tabela de métricas

**Por uso (consulta, tarefa ou token)**

| Métrica | Unidade | O que mede | Valor de referência publicado | Fonte |
|---|---|---|---|---|
| Energia por consulta | Wh/consulta | eletricidade de uma requisição de texto; declarar se inclui só o chip, o servidor, as máquinas ociosas e o PUE | 0,24 Wh (Gemini, mediana medida, com PUE, mai/2025); 0,31 Wh (modelos com mais de 200 bilhões de parâmetros, mediana estimada, com PUE, 2026); 0,34 Wh (ChatGPT, média declarada, sem método, 2025) | [7][10][8] |
| Energia por tarefa | Wh/tarefa ou kWh/1.000 inferências | custo por tipo de uso: texto, imagem, raciocínio, agente | de 0,05 Wh (texto, modelo médio) a 50 Wh (agente com raciocínio), só GPU (2026) | [33] |
| Energia por token | Wh/1.000 tokens, com entrada e saída separadas | base para inventário a partir dos registros de uso | 0,32 Wh (entrada) e 0,96 Wh (saída) por 1.000 tokens, antes do PUE; valores-padrão propostos, ainda em consulta, para hiperescaladores, derivados do prompt mediano do Gemini com 500 tokens supostos (2026) | [66] |
| Emissões por consulta | gCO₂e/consulta, LB e MB | carbono de uma requisição | 0,03 g MB, com escopos 1 e 3 (Gemini, 2025); cerca de 0,09 g LB, mesma fronteira (cálculo nosso); 1,14 g (Le Chat, resposta de 400 tokens, ACV LB com fabricação, 2025) | [7][17] |
| Emissões por milhão de tokens | kgCO₂e/MTok | unidade proposta para o escopo 3 de quem usa IA | treino amortizado de 0,1 kgCO₂e/MTok (supõe 10 mil tCO₂e LB por treino e 10¹⁴ tokens na vida do modelo) e fabricação amortizada de 0,017 kgCO₂e/MTok (GPU H100, 4 anos, 50% de uso); valores-padrão propostos, ainda em consulta, para hiperescaladores (2026) | [66] |
| Água por consulta | mL/consulta, com local e indireta separadas | água consumida para servir a requisição | 0,26 mL (Gemini, só local); de 0 a 0,067 mL (Microsoft, resfriamento); 45 mL (Le Chat, ACV com geração e fabricação) | [7][11][17] |
| Recursos minerais por consulta | mg Sb eq/consulta | esgotamento de recursos abióticos, sobretudo na fabricação | 0,16 mg Sb eq por resposta de 400 tokens (Le Chat, 2025) | [17] |

**Por modelo e hardware**

| Métrica | Unidade | O que mede | Valor de referência publicado | Fonte |
|---|---|---|---|---|
| Energia e emissões de treino | MWh; tCO₂e (LB e MB) | pegada do treino, reportada à parte da inferência | Llama 3.1: 39,3 milhões de horas de GPU H100, 11.390 t LB e zero MB (2024); GPT-3: 1.287 MWh e 552 t LB (estimativa de 2021) | [23][20] |
| Pontuação de eficiência do modelo (AI Energy Score) | Wh de GPU por 1.000 consultas; de 1 a 5 estrelas | compara modelos abertos em condições padronizadas | modelos com raciocínio consomem 30 vezes mais, em média (dez/2025) | [12] |
| Carbono incorporado | kgCO₂e por placa, servidor ou GPU | fabricação, materiais, montagem e transporte | 1.312 kgCO₂e (HGX H100) e 2.274 kgCO₂e (HGX B200) por placa de 8 GPUs (2025) | [26] |
| Intensidade de carbono da computação (CCI) | gCO₂e por exaFLOP utilizado | carbono do ciclo de vida por computação útil | melhora de 3 vezes da TPU v4i para a v6e (2025) | [27] |
| Reúso e reciclagem de hardware | % dos servidores e componentes | fim de vida | 92% na nuvem da Microsoft (ano fiscal de 2025) | [53] |

**Por data center e energia**

| Métrica | Unidade | O que mede | Valor de referência publicado | Fonte |
|---|---|---|---|---|
| PUE | energia total ÷ energia de TI (1,0 é o ideal) | eficiência da infraestrutura de resfriamento e energia | 1,09 (Google, 2025); 1,14 (Amazon, 2025); 1,17 (Microsoft, ano fiscal de 2025); 1,36 (média da UE, 2024); 1,45 (média dos EUA, 2024); 1,54 (média ponderada dos respondentes da pesquisa global do Uptime, 2025) | [49][54][53][84][36][43] |
| WUE | L por kWh de TI | água usada no local por energia de TI; cada fonte usa uma fronteira (retirada, consumo, só resfriamento), então os valores não se ranqueiam | 0,12 (Amazon, retirada, 2025); 0,27 (Microsoft, água de resfriamento e umidificação, ano fiscal de 2025); 1,15 (Google, consumo de água doce, 2024); 0,58 (média da UE, água total de entrada, 2024); teto do Redata no Brasil: 0,05 (fronteira a definir em regulamento) | [54][53][7][84][92] |
| Água indireta da eletricidade | L/kWh | água consumida na geração da energia | 4,52 L/kWh (eletricidade dos data centers dos EUA, 2023); cerca de 18,6 L/kWh (Brasil, método conservador do WRI, mix de geração de 2016) | [35][46] |
| CUE | kgCO₂e por kWh de TI (= PUE × fator da rede) | carbono da operação por energia de TI | cerca de 0,51 nos EUA e 0,07 no Brasil, com PUE de 1,45 e os fatores LB do eGRID (2023) e do SIN (2025) (cálculo nosso, ilustrativo) | [36][44][89] |
| Energia livre de carbono horária (CFE) | % das horas de consumo cobertas | quanto do consumo, hora a hora, é atendido por fonte livre de carbono na mesma rede | cerca de 65% (Google, 2025); 87% na região São Paulo do Google Cloud e 57% na Virgínia do Norte (2025) | [49][45] |
| Fração renovável (REF) | de 0 a 1 | renovável contratada no ano (base MB) | 0,86 (média da UE, 2024) | [84] |
| Reúso de energia (ERF) | % do calor reaproveitado | calor residual usado fora do data center | cerca de 1,8% na UE (2024) | [84] |

**Corporativo**

| Métrica | Unidade | O que mede | Valor de referência publicado | Fonte |
|---|---|---|---|---|
| Escopo 2 LB e MB | tCO₂e | eletricidade comprada, pelos dois métodos | Google, 2025: 15,15 Mt LB contra 2,82 Mt MB | [49] |
| Escopo 3, categoria 1 (IA comprada como serviço) | tCO₂e | IA consumida via nuvem, API ou software | para US$ 100 mil/ano de API: 13,4 t pelo gasto; 3,7 t (MB) a 5,4 t (LB) pela atividade, mais 1,8 t de treino em linha separada; 3,2 t (MB) a 4,5 t (LB) com dado do provedor (exemplo ilustrativo, 2026) | [66] |
| Intensidade por resultado | tCO₂e ou MWh por token, transação ou receita | eficiência da IA ao longo do tempo | SAP: −60% nas emissões médias por token entre 2024 e o 1º trimestre de 2025 (análise interna, sem método publicado) | [68] |
| Água em áreas de estresse hídrico | % do consumo ou da retirada | risco hídrico local | Microsoft, ano fiscal de 2025: 48% do consumo e 50% da retirada | [52] |

### 5.2 Como se calcula

```text
Energia total (kWh)            = energia de TI do uso (kWh) × PUE
Emissões operacionais (kgCO₂e) = energia total (kWh) × fator de emissão da rede (kgCO₂e/kWh)
Emissões incorporadas (kgCO₂e) = carbono de fabricação (kgCO₂e) × (tempo de uso ÷ vida útil) × (fração do equipamento usada)
Treino amortizado (kgCO₂e)     = (emissões do treino ÷ tokens servidos na vida do modelo) × tokens usados   → linha separada
Água (L)                       = energia de TI (kWh) × WUE (L/kWh, local) + energia total (kWh) × fator de água da rede (L/kWh, indireta)
```

**Unidades.** 1 kWh = 1.000 Wh; 1 MWh = 1.000 kWh; 1 TWh = 1 bilhão de kWh. Energia em kWh × fator em gCO₂e/kWh = gramas; ÷ 1.000 = kg; ÷ 1.000.000 = t. gCO₂e/kWh e kgCO₂e/MWh têm o mesmo valor numérico (67,4 kg/MWh = 67,4 g/kWh). 1 L = 1.000 mL; 1 m³ = 1.000 L. Exemplo (cálculo nosso): uma consulta de 0,24 Wh gasta 0,00024 kWh; com o fator do SIN (46,1 gCO₂/kWh), emite cerca de 0,011 gCO₂; com a média dos EUA (349,7 gCO₂e/kWh), cerca de 0,084 gCO₂e.

**Energia.** Pode ser medida, por telemetria, ou estimada (tokens × Wh por token, ou consultas × Wh por consulta). Atenção à dupla contagem: se o valor por consulta já inclui o PUE, como os 0,24 Wh do Google e os 0,31 Wh da Microsoft, não se multiplica de novo.

**Fator de emissão: LB × MB.**
- **LB:** fator médio da rede onde o consumo ocorre. No caso da IA, vale a região do data center que processa a inferência, não a do escritório do usuário.
- **MB:** fator dos instrumentos contratuais, como PPAs e certificados de energia. Sem instrumento, o GHG Protocol manda usar o mix residual. O Programa Brasileiro aceita certificados de energia renovável e contratos do mercado livre com autodeclaração, e a energia sem rastreio entra com o fator médio do SIN [86].
- **Regra:** o GHG Protocol pede os dois métodos. No Brasil, o Programa Brasileiro GHG Protocol exige o LB e aceita o MB como adicional [86].
- **A diferença na prática:**
  - Llama 3.1: 11.390 t LB contra zero MB [23];
  - Google, escopo 2: 15,15 Mt LB contra 2,82 Mt MB, razão de 5,4 vezes (cálculo nosso) [49];
  - Meta, escopo 2 em 2024: 5,97 Mt LB contra 1.358 t MB [55];
  - nas empresas digitais monitoradas pela UIT, o MB é cerca de um terço do LB [41].
- **Casamento anual × horário:** o "100% renovável" das big techs é anual e MB. A Microsoft casou 34,5 de 37,0 TWh no ano fiscal de 2025 (cerca de 93%) e chega a 100% contando a parcela renovável da rede. Os 43,6 TWh "100% renováveis" do Google incluem 10,6 TWh de renovável da rede [52][49]. A revisão do escopo 2 do GHG Protocol discute exigir casamento horário; na consulta pública, só 22% de 909 respondentes apoiaram a exigência [79].

**Carbono incorporado.** Entra pelo escopo 3: na categoria 2 (bens de capital), para hardware próprio; para IA comprada como serviço, junto com o serviço, como linha de fabricação amortizada [66]. Pesa mais em redes limpas [27][28].

**Treino.** É amortizado por token ou por consulta e reportado à parte. A ITU-T L.1801 exige o relato separado do treino [77].

**Três níveis de medição para quem usa IA** [66]:
1. **Gasto:** valor pago × fator de insumo-produto (0,134 kgCO₂e por dólar de 2023, setor de processamento de dados e hospedagem). O fator já embute a cadeia, inclusive a fabricação do hardware.
2. **Atividade:** (tokens de entrada × intensidade de entrada + tokens de saída × intensidade de saída) × PUE × fator da rede, mais a fabricação amortizada. O treino amortizado vai em linha separada.
3. **Dado do provedor:** kgCO₂e por milhão de tokens informado pelo fornecedor.

No exemplo do estudo, uma empresa fictícia com US$ 100 mil por ano em API:
- **gasto:** 13,4 tCO₂e;
- **atividade:** 9,1 t na versão simplificada (fator único e média nacional); na detalhada, 5,4 t (LB) e 3,7 t (MB), mais 1,8 t de treino amortizado em linha separada;
- **dado do provedor** (números do Gemini como aproximação): 4,5 t (LB) e 3,2 t (MB), com fabricação e sem treino.

Segundo o estudo, o treino, o termo mais incerto, responderia por 32% a 56% do total. A lição principal é a diferença de até cerca de quatro vezes entre o nível do gasto e os demais. O documento é um preprint em formato de white paper, com valores-padrão ainda em consulta, não uma norma.

### 5.3 Padrões e índices

| Padrão ou índice | Quem | O que define | Situação |
|---|---|---|---|
| ISO/IEC 21031:2024 (SCI) | ISO/IEC, a partir da Green Software Foundation | SCI = ((E × I) + M) por R: energia × intensidade da rede, mais carbono incorporado, por unidade funcional. Usa só o fator de localização; compensações, certificados e PPAs não reduzem o escore | publicada em 2024 [75] |
| SCI for AI | Green Software Foundation | extensão do SCI para IA, com escore do provedor (desenvolvimento, treino, implantação) e do consumidor (operação); unidades por token, inferência ou FLOP | ratificada em 17/12/2025 [76] |
| ITU-T L.1801 (equivalente à ETSI ES 204 135) | UIT | ACV de sistemas de IA. Treino reportado à parte; unidade funcional em tokens de entrada, gerados e de "raciocínio"; água direta e indireta; prioriza dado MB quando conhecido | aprovada em 06/02/2026 [77] |
| ISO/IEC TR 20226:2025 e CEN/CLC/TR 18145:2025 | ISO/IEC; CEN-CENELEC | relatórios técnicos sobre aspectos de sustentabilidade de sistemas de IA | publicados em 2025 [78] |
| IEEE P7100, CEN/CLC prEN 18287 e ISO/IEC TS 42112 | IEEE; CEN-CENELEC; ISO/IEC | medição de impactos ambientais da IA; diretrizes e métricas; eficiência do treino | em desenvolvimento, com publicação incerta a partir de 2026 [78] |
| ISO/IEC 30134 (partes 1 a 9) | ISO/IEC | indicadores de data center, como PUE, CUE e WUE | publicadas [78] |
| AI Energy Score | Hugging Face e Salesforce | Wh de GPU por 1.000 consultas em condições padronizadas; de 1 a 5 estrelas | v2 em dez/2025; só modelos abertos e só GPU [12] |
| Metodologia do Google por prompt | Google | "abordagem abrangente" (acelerador, CPU e memória, ociosidade e PUE); mediana; carbono MB; água no local | ago/2025 [7] |
| Metodologia da Mistral | Mistral, Carbone 4 e ADEME | ACV multicritério (carbono LB, água com geração e fabricação, recursos minerais), com base no referencial francês de IA frugal (AFNOR) e no GHG Protocol Product Standard | jul/2025 [17] |
| PUE, WUE e CUE | The Green Grid; ISO/IEC 30134 | eficiência do data center | consolidados; PUE e WUE são de reporte obrigatório na UE para data centers de 500 kW ou mais [84][32] |
| CFE horário | Google (metodologia 24/7) | % das horas de consumo cobertas por energia livre de carbono na mesma rede | Google e Microsoft têm meta de casamento horário de 100% em 2030 [32][49] |
| GHG Protocol, escopo 2 (em revisão) | WRI e WBCSD, com a ISO | métodos LB e MB; a revisão discute casamento horário e entregabilidade | consulta em 2025-2026 com quase 1.100 respostas de 56 países; norma consolidada com a ISO prevista para o 4º trimestre de 2028 [79][80] |

### 5.4 Fatores de emissão da rede

| Rede | Fator | Método | Ano | Fonte |
|---|---|---|---|---|
| Brasil (SIN) | 46,1 gCO₂/kWh (0,0461 tCO₂/MWh) | fator médio para inventários; só CO₂; LB | 2025 | [89] |
| Brasil (SIN), meses de 2026 | de 31,2 a 51,7 gCO₂/kWh (jan-ago) | idem | 2026 | [89] |
| Brasil (SIN), ano seco | 126,3 gCO₂/kWh | idem | 2021 | [89] |
| Brasil (SIN), média de 10 anos | cerca de 77 gCO₂/kWh | média dos fatores do MCTI | 2015-2024 | [99] |
| Brasil (geração) | mais de 70 gCO₂/kWh; 50 em 2030 | CO₂ total ÷ geração total (IEA) | 2025 | [34] |
| Brasil (setor elétrico) | 67,4 gCO₂e/kWh (67,4 kgCO₂e/MWh) | todo o setor elétrico, em CO₂e (EPE) | 2025 | [90] |
| Região São Paulo do Google Cloud | 73 gCO₂e/kWh; 87% de CFE horário | intensidade operacional média da rede local (LB), com dados da Electricity Maps | 2025 | [45] |
| EUA, média nacional | 349,7 gCO₂e/kWh (770,9 lb CO₂e/MWh; só CO₂: 348,0 g/kWh) | eGRID, sobre a geração total, sem perdas de rede; LB | 2023 (revisão de 2025) | [44] |
| Eletricidade dos data centers dos EUA | 340 gCO₂e/kWh (0,34 kgCO₂e/kWh) e 4,52 L/kWh de água indireta | LB ponderado pela localização dos data centers, sem PPAs | 2023 | [35] |
| Virgínia do Norte (Google Cloud) | 343 gCO₂e/kWh; 57% de CFE horário | intensidade operacional média da rede local (LB), com dados da Electricity Maps | 2025 | [45] |
| União Europeia | 170 gCO₂/kWh; 90 em 2030 | CO₂ total ÷ geração total (IEA) | 2025 | [34] |
| Mundo | 435 gCO₂/kWh; 360 em 2030 | CO₂ total ÷ geração total (IEA) | 2025 | [34] |
| Frota do Google | 345 gCO₂e/kWh LB contra 94 MB | corporativo | 2024 | [7] |

**Qual fator usar.** Para a IA, vale o fator da região do data center que processa a carga. A fonte e o método devem ser declarados:
- o fator do MCTI mede só CO₂ pelo método de inventário, e sua base foi ampliada em janeiro de 2025 (inclusão de conjuntos de usinas eólicas e solares e de térmicas a biomassa), o que, segundo o próprio MCTI, pode reduzir o fator e prejudica a comparação com anos anteriores [89];
- a IEA divide o CO₂ total pela geração total [34];
- a EPE cobre todo o setor elétrico em CO₂e [90].

Comparar países com fatores de métodos diferentes distorce a razão. Pelo fator do MCTI, o SIN fica perto de um nono da média mundial da IEA; pelo fator da própria IEA, perto de um sexto (cálculo nosso).

### 5.5 Exemplo ilustrativo: o mesmo uso processado no Brasil, nos EUA e na média mundial

**Premissas.**
- **Uso:** 1.000 usuários × 20 consultas por dia útil × 230 dias úteis = 4,6 milhões de consultas por ano (premissa nossa).
- **Energia por consulta:** 0,24 Wh (0,00024 kWh), o prompt de texto mediano do Gemini, já com PUE (mai/2025) [7]. Cenário pesado: 3,91 Wh, a mediana estimada para consultas longas com raciocínio (cerca de 500 tokens de entrada e 5.000 de saída), também com PUE [10]. Em cada linha, o modelo e a eficiência do data center são os mesmos; entre as colunas, só muda a rede.
- **Fatores (LB):** SIN em 2025, 46,1 gCO₂/kWh (MCTI, só CO₂) [89]; média dos EUA, 349,7 gCO₂e/kWh (eGRID2023) [44]; média mundial, 435 gCO₂/kWh (IEA, 2025) [34]. Na rede dos EUA, CO₂ e CO₂e diferem em menos de 1% (348,0 contra 349,7 g/kWh), então a comparação entre as colunas vale.
- **Onde roda:** a coluna "Brasil" supõe que a inferência ocorre num data center no país, o que hoje não é a regra para modelos de fronteira (seção 2).
- **Conta:** consultas × kWh por consulta × fator (g/kWh) = gramas; ÷ 1.000 = kg; ÷ 1.000.000 = t. Só a eletricidade da inferência; treino e fabricação estão na leitura 4.

**Resultados (cálculo nosso).**

| Cenário | Energia por ano | Processado no Brasil | Processado nos EUA | Média mundial |
|---|---|---|---|---|
| Texto simples (0,24 Wh por consulta) | 1,1 MWh (1.104 kWh) | 51 kg CO₂ | 386 kg CO₂e | 480 kg CO₂ |
| Raciocínio longo (3,91 Wh por consulta) | 18,0 MWh (17.986 kWh) | 0,83 t CO₂ | 6,3 t CO₂e | 7,8 t CO₂ |

**Leituras.**
1. **Rede.** Pelos fatores usados nos inventários de cada país (MCTI e eGRID), a mesma carga emite cerca de 7,6 vezes menos no Brasil que nos EUA. Com a intensidade da IEA para o Brasil (mais de 70 g/kWh) contra o eGRID, a razão cai para cerca de 5, mas mistura métodos. Numa fonte única, as regiões de São Paulo (73 g) e da Virgínia do Norte (343 g) de um grande provedor de nuvem dão cerca de 4,7 vezes [45].
2. **Tipo de uso.** O raciocínio longo multiplica energia e emissões por cerca de 16 (3,91 ÷ 0,24, combinando fontes diferentes). Dentro do mesmo estudo da Microsoft, a alta é de 13 vezes (de 0,31 para 3,91 Wh) [10].
3. **Contrato.** Pelo número do Google (0,03 gCO₂e por prompt, MB, já com os escopos 1 e 3, que incluem a fabricação do hardware), o caso simples daria 138 kg (4,6 milhões × 0,03 g). Fica abaixo do LB dos EUA e acima do LB do Brasil, mas a comparação é só indicativa: mudam o método (MB × LB) e a fronteira (com e sem fabricação).
4. **Treino e fabricação.** Com os valores-padrão propostos por Bistline et al. (treino amortizado de 0,1 kgCO₂e/MTok, LB, e fabricação de 0,017 kgCO₂e/MTok) e cerca de 500 tokens por consulta, a mesma premissa do estudo [66], o caso simples soma 2.300 MTok por ano: cerca de 230 kg de treino e 39 kg de fabricação, reportados em linhas separadas. No cenário pesado, com cerca de 5.500 tokens por consulta, seriam cerca de 2,5 t e 0,4 t. Os dois superam a operação no Brasil: em rede limpa, a parte "invisível" pode dominar. Ressalva: o treino é o termo mais incerto. O valor-padrão supõe 10 mil tCO₂e por treino, tirados do model card do Llama 3.3, que é inconsistente (seção 11), e 10¹⁴ tokens na vida do modelo. Na faixa testada pelo estudo (10¹³ a 10¹⁵ tokens), o treino do caso simples iria de cerca de 23 kg a 2,3 t.
5. **Água.** No local, cerca de 1,2 m³ por ano (0,26 mL × 4,6 milhões = 1.196 L). A água indireta da eletricidade acrescentaria cerca de 5,0 m³ com o fator dos data centers dos EUA (1.104 kWh × 4,52 L/kWh) [35] e cerca de 20,5 m³ com o fator do WRI para o Brasil (1.104 kWh × cerca de 18,6 L/kWh) [46]. O fator brasileiro é conservador: atribui à geração toda a evaporação dos reservatórios e usa o mix de geração de 2016. Ainda assim, mostra que vantagem de carbono não é vantagem de água.
6. **Escala.** Somadas a operação e as linhas de treino e fabricação, o cenário pesado fica entre cerca de 3,8 t (Brasil) e 11 t (média mundial) de CO₂e por ano; o caso simples, abaixo de 1 t. Para um usuário corporativo, o tema é de coerência e governança, não de volume (leitura nossa).

## 6. O que dizem e fazem as big techs

| Empresa (ano dos dados) | Emissões e variação | Método e ressalvas | Metas | Água | Energia por consulta | Acordos de energia |
|---|---|---|---|---|---|---|
| Google (2025) | 14,5 MtCO₂e no perímetro da meta: +18% no ano e +81% sobre 2019; 18,85 Mt no perímetro integral do GHG Protocol | MB, com exclusões no escopo 3; escopo 2 de 15,15 Mt LB contra 2,82 Mt MB; eletricidade de 43,6 TWh (+37%); não separa a IA | net zero em 2030; −50% sobre 2019; energia livre de carbono 24/7 em 2030 (chamadas de "moonshots") | 41 bilhões de L consumidos (+34%); repôs 78% da água doce consumida, rumo a 120% | 0,24 Wh, 0,03 gCO₂e (MB) e 0,26 mL (só local) por prompt mediano do Gemini (mai/2025) | mais de 12 GW de novos contratos de energia limpa em 2025, incluindo nuclear (Duane Arnold, 600 MW) e geotermia |
| Microsoft (ano fiscal de 2025) | 20,29 MtCO₂e (MB, critério da gestão): +25% no ano e +57,5% sobre o ano fiscal de 2020; 21,12 Mt pelo GHG Protocol sem ajustes (+62% sobre o ano fiscal de 2020) | escopo 2 de 12,03 Mt LB contra 2,71 Mt MB (0,26 Mt no ano anterior), após o fim da compra de certificados avulsos em fev/2025; eletricidade de 37,0 TWh, 3,4 vezes a de 2020 | carbono negativo e saldo hídrico positivo em 2030 | 8.170 megalitros (cerca de 8,2 bilhões de L) consumidos (+22%); 48% em áreas com estresse hídrico; WUE de 0,27 L/kWh | 0,31 Wh de mediana (intervalo interquartil de 0,16 a 0,60 Wh) por consulta típica a modelos de fronteira, com PUE (estimativa de estudo próprio, não medição de produto) | contrato para reativar a usina nuclear Crane (ex-Three Mile Island); HVO em cerca de 60% dos data centers na Europa |
| Amazon (2025) | 80,85 MtCO₂e: +16% no ano e +58% sobre 2019 | MB com certificados, inclusive de SAF e diesel renovável; o relatório não traz o escopo 2 LB (busca no texto) | net zero nas operações em 2040 | WUE de 0,12 L/kWh (retirada por kWh de TI) | não divulgada | portfólio de 42 GW livres de carbono; 1.900 MW nucleares da Talen até 2042; 5 GW de nova energia nuclear com a X-energy |
| Meta (2024, último dado publicado) | 15,63 MtCO₂e LB; 8,20 Mt com instrumentos contratuais | escopo 2 de 5,97 Mt LB contra 1.358 t MB; sem relatório com dados de 2025 até 01/10/2026 | net zero na cadeia de valor e devolver mais água do que usa, em 2030 | — | não divulgada; o treino é divulgado nos model cards (Llama 3.1: 11.390 t LB, zero MB) | — |
| NVIDIA (ano fiscal de 2026) | escopo 3 de 10,70 MtCO₂e (3,64 Mt dois anos antes) | parte da alta vem de troca de método na categoria 1; publica pegada de produto das placas de GPU | — | — | — | — |
| OpenAI | sem inventário público localizado | — | — | cerca de 0,32 mL por consulta média (declarado) | 0,34 Wh por consulta média (declarado, sem método) | — |
| Mistral | 20,4 ktCO₂e, 281.000 m³ de água e 660 kg Sb eq (Mistral Large 2: treino e 18 meses de uso, até jan/2025) | ACV com Carbone 4 e ADEME; LB, com fabricação | — | 45 mL por resposta de 400 tokens (com geração e fabricação) | 1,14 gCO₂e por resposta (não informa Wh) | — |
| Anthropic | sem números públicos localizados | declara compensar anualmente as emissões operacionais com créditos verificados (2024) | — | — | não divulgada | compromisso de pagar 100% das melhorias de rede para conectar seus data centers (2026) |

Fontes da tabela: Google [49][7]; Microsoft [52][53][10][11]; Amazon [54]; Meta [55][23]; NVIDIA [56][26]; OpenAI [8]; Mistral [17]; Anthropic [57].

**A tendência de transparência.**
- **Por consulta, só o Google publica medição de produção com metodologia.** É o único provedor de modelo de fronteira com números por prompt nessa granularidade, e ainda assim como mediana da frota, que não se liga ao tráfego de um cliente [66][7]. A OpenAI deu um número sem método; a Microsoft, um estudo de estimativa; a Mistral, uma ACV.
- **A divulgação recuou.** A publicação direta de dados ambientais de modelos notáveis teve pico em 2022, com 10% dos modelos, e caiu com a onda de modelos comerciais. Em maio de 2025, entre os 20 modelos mais usados na plataforma de API OpenRouter, 84% dos tokens foram para modelos sem nenhuma divulgação, 14% para modelos com divulgação indireta e 2% para modelos com divulgação direta [2].
- **Ninguém separa a IA no inventário.** O Google declarou em 2024 que a distinção entre a IA e as demais cargas "não será significativa" [50], e nenhuma das empresas analisadas por de Vries-Gao reporta métricas específicas de IA [40].
- **Os métodos endurecem.** A Microsoft parou de comprar certificados avulsos em fevereiro de 2025, o que multiplicou por cerca de 10 o seu escopo 2 MB [52]. O Google mudou em 2026 o método da métrica de emissões por GWh, que não deve ser comparada com relatórios anteriores [49]. As séries são recalculadas todo ano: citar sempre o relatório mais recente.
- **Metas mantidas, tom mudado.** Nenhuma meta foi formalmente abandonada, mas as emissões sobem (escopos 1 e 2 LB entre 192% e 239% do nível de 2020 nos quatro hiperescaladores em 2024 [41]), e o Google trata as suas como "moonshots" [49]. A Microsoft e a Anthropic passaram a se comprometer a não encarecer a conta de luz das comunidades onde instalam data centers [53][57].
- **Benefício declarado não é saldo.** O Google atribui 41 MtCO₂e de reduções "habilitadas" a nove soluções em 2025, cerca de três vezes a sua pegada. Mas 27,8 Mt vêm do Google Earth, contando a geração inteira de usinas de parceiros, e a empresa informa que os dados não foram verificados de forma independente [49].

## 7. Consultorias e empresas usuárias

**Quantas medem a pegada da IA.**

| Pesquisa | Amostra | Resultado | Fonte |
|---|---|---|---|
| Capgemini (jan/2025; campo em ago-set/2024) | 2.000 executivos de empresas com receita acima de US$ 1 bilhão e iniciativas de IA generativa, em 15 países, inclusive o Brasil | 12% medem a pegada da IA generativa; dessas, 28% divulgam e 24% têm meta; 74% das que não medem citam a falta de transparência dos provedores | [58] |
| Capgemini (2026; campo em jun-jul/2026) | 2.100 executivos de 701 organizações, em 13 países, sem o Brasil | 38% medem a energia da IA e 34% o carbono; 33% divulgam energia ou carbono dos modelos e 25% a água; 45% dizem que a IA elevou significativamente suas emissões (percepção, não medição); 71% acham que os benefícios da IA generativa superam os impactos (57% em 2025); 60% citam a falta de transparência dos provedores | [59] |
| KPMG (2026; campo em set/2025) | 350 executivos de mais de 15 países | 18% têm metas mensuráveis específicas para IA; 43% não conseguem rastrear energia, água e emissões da IA; só 4% se dizem "otimizados"; quase 9 em cada 10 citam a sustentabilidade como critério-chave na escolha de parceiros de IA | [60] |
| Deloitte (2026; campo em mai-jun/2026) | 2.156 executivos de alta direção em 29 países | 28% tratam a sustentabilidade como critério formal nas decisões de IA | [63] |
| Kyndryl e Microsoft (2025) | 1.286 líderes de 20 países, inclusive o Brasil | 43% consideram energia e carbono ao implantar IA (35% em 2024) | [64] |
| Logicalis (2026) | mais de 1.000 CIOs | 39% estão extremamente confiantes de que a empresa gerencia ativamente o impacto ambiental da IA | [65] |
| PwC (2026) | análise de milhares de divulgações corporativas | 60% das empresas usam IA para descarbonizar; menos de 1% relatam resultado mensurável | [61] |

As séries não são comparáveis entre si: perguntas e amostras mudam. Indicam tendência, não evolução medida.

**Práticas de "IA sustentável" observadas no mercado.** A lista descreve o que empresas fazem; não é recomendação.
1. **Modelo do tamanho da tarefa.**
   - Modelos generalistas emitiram cerca de 10 g de CO₂e por 1.000 inferências de perguntas e respostas, contra 0,3 g de modelos específicos para a tarefa [14].
   - A Salesforce usa modelos de 44 a 135 milhões de parâmetros em tarefas como detecção de toxicidade e mascaramento de dados pessoais, que diz serem cerca de 99% mais eficientes que os grandes modelos de fronteira (alegação da empresa) [67].
   - A SAP roteia as consultas simples para modelos mais eficientes e diz embutir a IA nos produtos "só onde ela entrega valor" [68].
   - O raciocínio fica reservado aos casos em que agrega valor, dado o seu custo de energia (seção 3.2).
2. **Eficiência da inferência.** Otimizações bem aplicadas (lotes, decodificação, software de serviço, hardware) reduzem a energia de inferência em até 73% frente a configurações não otimizadas [70]. No Google, as melhorias de modelo responderam por 23 vezes de queda na energia por prompt [7].
3. **Região, horário e data center.**
   - Num estudo de 2022, a região de nuvem mudou as emissões do mesmo treino de um modelo BERT pequeno (8 GPUs por 36 horas, cerca de 37 kWh) de cerca de 7 kg para cerca de 26 kg de CO₂, entre 16 regiões [71].
   - Nos dados publicados por um grande provedor de nuvem, a região de São Paulo tem 87% de energia livre de carbono horária, contra 57% na Virgínia do Norte (2025) [45].
   - A Salesforce usa PUE e WUE como critérios de escolha de data centers [67].
4. **Medição e reporte.**
   - A SAP monitora as emissões das cargas de IA em painéis, inclui no inventário as emissões do treino de modelos de terceiros e cobra dos hiperescaladores a alocação das emissões de pré-treino aos clientes, prática que ainda considera limitada [68].
   - A política de IA do Crédit Agricole afirma que "todo sistema de IA tem um impacto ambiental que deve ser medido ou estimado para depois ser reduzido" e se apoia no referencial francês de IA frugal [69].
5. **Governança e fornecedores.**
   - A KPMG observa que as empresas mais avançadas definem o que conta como IA (treino, inferência, funções embutidas), fixam as fronteiras de escopos 2 e 3, usam unidades por interação ou decisão e buscam asseguração externa [60].
   - A falta de dados dos provedores é a barreira mais citada [58][59].

**Empresas de energia e do agro.** A pesquisa desta rodada não localizou empresa de energia, de combustíveis ou do agronegócio que publique kWh, tCO₂e ou m³ atribuídos ao próprio uso de IA. Os exemplos vêm de software, serviços financeiros e tecnologia. Na pauta de TI do agro brasileiro registrada pela Gatua em 2026 (painéis e pesquisa com 84 respondentes), a pegada ambiental da IA não aparece (busca no texto) [74].

## 8. Regulação e padrões

**União Europeia.**
- **AI Act:** os provedores de modelos de IA de propósito geral devem documentar o consumo de energia "conhecido ou estimado" do modelo (Anexo XI), em obrigação vigente desde 02/08/2025 [83][82].
  - O Código de Prática de jul/2025 prevê entregar essa documentação ao AI Office e às autoridades nacionais mediante pedido; não há obrigação de divulgação pública [81].
  - A metodologia de medição ainda está em estudo. A Comissão consultou o mercado entre abril e maio de 2026 para um estudo que pode levar a um rótulo de energia e emissões para a IA [82].
  - O art. 40 pede normas técnicas sobre o reporte do consumo de energia e de recursos. O art. 112 obriga a Comissão a avaliar, até 02/08/2028, o avanço das normas de eficiência energética desses modelos e a necessidade de medidas, inclusive vinculantes [83].
- **Diretiva de Eficiência Energética:** data centers com 500 kW ou mais de TI reportam indicadores todo ano, inclusive PUE e WUE (Regulamento Delegado 2024/1364) [32].
  - O primeiro relatório da Comissão mostra 68 TWh consumidos em 2024 (114 TWh, 3,2% da demanda, em 2030), PUE médio de 1,36, WUE de 0,58 L/kWh, fração renovável de 0,86 e só cerca de 1,8% do calor reaproveitado [84].
  - Mais de 70% dos data centers casam 100% do consumo com renováveis em base anual, em grande parte por PPAs e garantias de origem não necessariamente locais ou adicionais. Reportaram 770 data centers, cerca de 36% do universo, e a Comissão propõe padrões mínimos de desempenho [84].
- **Mandatos nacionais:**
  - PUE máximo de 1,2 para data centers novos até 2026 e de 1,3 para os existentes até 2030 na Alemanha; 1,5 na China até 2025; 1,4 na Austrália até 2025 [32].
  - Na Irlanda, a política de conexão publicada pelo regulador em dezembro de 2025 exige que os novos data centers tragam geração ou armazenamento despachável equivalente à sua capacidade máxima de importação e supram ao menos 80% da demanda anual com renováveis geradas no país [34].

**Padrões técnicos.** Ver a seção 5.3: SCI e SCI for AI, ITU-T L.1801, ISO/IEC TR 20226 e ISO/IEC 30134, além das normas em preparação (IEEE P7100, prEN 18287).

**GHG Protocol.**
- A revisão do escopo 2 discute exigir casamento horário e entregabilidade física para o método MB. Na consulta pública, com quase 1.100 respostas de 56 países, só 22% de 909 respondentes apoiaram exigir casamento horário e 70% deram apoio baixo ou nenhum [79].
- A norma corporativa consolidada, copublicada com a ISO, está prevista para o 4º trimestre de 2028 [80].
- Não há guia oficial específico para a IA no escopo 3.
- Se o casamento horário vier, as emissões MB atribuídas à IA na nuvem tendem a subir (leitura nossa).

**Emissões evitadas.**
- O WBCSD manda reportar emissões evitadas à parte do inventário e proíbe usá-las para alegar neutralidade [87].
- A ITU-T L.1480 mede o efeito líquido contra um cenário de referência, descontando a pegada da própria solução e tratando o rebote [88].

**ISSB e CVM.** A Resolução CVM 244, de 29/05/2026, revogou a obrigatoriedade do relatório de sustentabilidade no padrão ISSB (normas CBPS) prevista na Resolução CVM 193 [85]:
- o relatório passou a ser voluntário para exercícios a partir de 2026;
- quem aderir publica por pelo menos três exercícios seguidos;
- a partir de 2027, a companhia aberta que não o arquivar deve justificar a opção ("pratique ou explique").

**Brasil: data centers.**
- **Lei 15.504/2026 (Redata):** para obter o benefício tributário, o data center precisa ter WUE de até 0,05 L/kWh, com aferição anual. Precisa também atender 100% da demanda elétrica com fontes renováveis ou de baixa emissão "na forma de regulamento" e publicar relatório de sustentabilidade com o WUE e as fontes de energia [92]. A lei não exige PUE nem métrica de carbono, e a definição de "baixa emissão" fica para o regulamento.
- **Antes da lei:** em 2025, a IEA não registrava no Brasil nenhum requisito de reporte (emissões, eletricidade) nem mandato de desempenho (PUE, WUE) para data centers [32].
- **CONAMA, Moção 147 (22/06/2026):** pede diretrizes nacionais de licenciamento que classifiquem os data centers de IA como atividade efetiva ou potencialmente poluidora [96]. As diretrizes devem prever:
  - critérios de eficiência energética e hídrica comparáveis e monitorados;
  - avaliação cumulativa por território;
  - critérios de exclusão em áreas de estresse hídrico crítico.
  A moção recomenda não usar ritos simplificados ou autodeclaratórios enquanto as diretrizes não existirem e pede que incentivos fiscais dependam de critérios rigorosos de sustentabilidade.
- **MPF e DPU (19/05/2026):** recomendação sobre o Data Center Pecém, em Caucaia (CE), com até 300 MW, geradores a diesel e localização em região de escassez hídrica. Os órgãos consideram insuficiente o relatório ambiental simplificado e apontam divergência entre os volumes de água informados [97].
- **Plano Brasileiro de IA (2025):** trata a "IA sustentável com matriz energética limpa" como janela de oportunidade e prevê um Centro de Monitoramento e Promoção da IA Sustentável e a ação Pró-Infra IA Sustentável, com meta de apoiar 42 projetos em cinco anos [98].

## 9. IA a favor do clima e o saldo líquido

**As estimativas de benefício e de saldo.**

| Estudo | Estimativa | Método e limites | Fonte |
|---|---|---|---|
| IEA (2025) | cerca de 1,4 Gt CO₂ evitadas em 2035, de 4% a 5% das emissões do setor energético | caso exploratório de adoção ampla de aplicações já existentes na indústria, nos transportes e nos edifícios; sem rebote; "não há momentum" | [32] |
| IEA (2026) | cerca de 13,5 EJ de economia potencial em 2035 (cerca de 3% do consumo final), contra 6 a 19 EJ de demanda a mais pelo crescimento econômico puxado pela IA | exploratório; somar as duas contas é "complexo", porque as medições variam em escopo e incerteza (paráfrase) | [33] |
| Stern et al. (2025) | de 3,2 a 5,4 GtCO₂e por ano em 2035 em três setores (energia elétrica, carne e laticínios, veículos leves), contra 0,4 a 1,6 Gt da pegada de data centers e IA | artigo de perspectiva; sem rebote; dados não abertos | [101] |
| PwC (2025) | de −0,1% a −1,1% das emissões acumuladas de 2024 a 2035 | modelo próprio, dependente de premissa de eficiência; em energia, de −0,9% a +0,1%, ou seja, pode ser aumento | [62] |
| Alpine et al. (2026) | aumento líquido de 0,47 a 1,8 Gt CO₂ por ano | equilíbrio geral; a IA também aumenta a produtividade do petróleo e do gás; o empate exige ganhos 4 a 5 vezes maiores nas renováveis; há uma correção dos autores, de set/2026, não consultada | [102] |
| BCG (2021) e BCG com Google (2023) | de 5% a 10% das emissões globais até 2030 | extrapolação da "experiência com clientes"; não usar como estimativa (seção 11) | [73] |

**As críticas.**
- **Evidência fraca.** Um levantamento de ONGs analisou 154 alegações de benefício climático da IA: só 26% citam pesquisa acadêmica publicada, 36% não citam evidência alguma e 97% tratam de IA "tradicional", não da IA generativa que puxa a demanda dos data centers [103].
- **A IA também serve à indústria fóssil.** Para ilustrar o rebote, a IEA calcula que uma queda hipotética de US$ 10 por barril no petróleo elevaria as emissões globais de CO₂ no equivalente às de 20 milhões de carros [32]. A conta de Alpine et al. vai na mesma direção [102].
- **Origem obscura.** Luccioni et al. registram que o raciocínio por trás dos "5% a 10%" não é claro [2].

**Como contar o benefício.** O benefício só se sustenta se for medido como efeito líquido contra um cenário de referência, descontando a pegada da própria solução e tratando o rebote [88]. Deve ser reportado à parte do inventário, sem abater emissões nem embasar alegação de neutralidade [87]. O caso do Google ilustra o problema: são 41 MtCO₂e "habilitadas", não verificadas de forma independente, que não são saldo líquido [49].

**Aplicações em agro, energia e biocombustíveis (evidência pontual).**

| Aplicação | Resultado | Escala e ressalvas | Fonte |
|---|---|---|---|
| Pulverização localizada por visão computacional em cana (Austrália) | −35% de herbicida em média (até −65% com pouca infestação), com 97% da eficácia da aplicação em área total; −39% na concentração e −54% na carga de herbicidas na água de escoamento | ensaios de campo; a economia é proporcional à infestação | [104] |
| Manejo de nutrientes por sítio com ferramentas digitais (milho, arroz e trigo em 11 países da África e da Ásia) | −10% de nitrogênio, +12% de produtividade e +15% de lucratividade | meta-análise; dados de GEE "mínimos"; onde falta adubo, a recomendação pode elevar emissões | [105] |
| Adubação em taxa variável no arroz (algoritmo e sensoriamento remoto) | até −40% de fertilizante, mantendo ou elevando o potencial produtivo em 15% a 20% | dado citado pela FAO, sem o estudo primário | [106] |
| Biorrefinaria de algas com IA embarcada (Índia, escala piloto) | +18% a 27% no rendimento de lipídios para biocombustível; −10% a 15% de energia | dados da própria empresa ao observatório da IEA | [107] |
| Siderurgia no Brasil (IA no alto-forno) | −1,5 kg de combustível e −4,4 kg de CO₂ por tonelada de gusa | dados da empresa ao observatório da IEA | [107] |
| Desenho de SAF por IA | candidatos com previsão de mais de 17% de redução na tendência de formar fuligem | triagem virtual, sem validação experimental; fuligem não é GEE | [108] |
| Previsão de trilhas de condensação (aviação) | −54% de trilhas em 70 voos de teste, com 2% a mais de combustível nos voos desviados; em 2025, o modelo emitiu cerca de 380 tCO₂e de computação e evitou cerca de 3.000 tCO₂e | teste com uma companhia aérea; dados da empresa; a conversão do efeito das trilhas em CO₂e é incerta | [110][49] |
| Metano em óleo e gás | detecção contínua de vazamentos com IA evitaria quase 2 Mt de metano (cerca de 60 Mt CO₂e) | estimativa da IEA | [32] |

**O que falta.** A pesquisa não localizou:
- redução de intensidade de carbono de biocombustível em escala industrial atribuída à IA;
- estudo oficial brasileiro (Embrapa, MAPA, EPE, ANP) que quantifique redução de insumos ou de emissões por IA em cana, soja, milho, eucalipto ou pastagem.

Leituras nossas:
- parte do que se divulga como "IA no agro" é agricultura de precisão sem IA (piloto automático, taxa variável), o que dificulta atribuir ganhos à IA;
- para um produtor de biocombustível, o lugar natural em que um ganho real de IA aparece de forma verificável é a intensidade de carbono certificada (gCO₂e/MJ na RenovaCalc), com verificação de terceira parte [109];
- o próprio Google apresenta a IA para trilhas de condensação como ganho de curto prazo "enquanto soluções de longo prazo, como o combustível sustentável de aviação, continuam a ganhar escala" (tradução nossa) [49]. É uma narrativa que convive com a do SAF e, em parte, compete com ela.

## 10. Brasil

**Matriz e fator de emissão.**
- **Matriz:** as renováveis foram 86,8% da eletricidade em 2025 (88,2% em 2024) [90]. As hidrelétricas caem de 52% da geração em 2025 para 46% em 2030, com a solar e a eólica em alta [34].
- **Cortes de geração:** os cortes de eólica e solar passaram de 20% em 2025, cerca de 37 TWh de energia renovável não aproveitada [34]. Leitura nossa: com rede e flexibilidade, essa energia poderia atender cargas novas; sem elas, os data centers disputam a mesma rede congestionada.
- **Fator do SIN:** 46,1 gCO₂/kWh em 2025, 54,5 em 2024 e 38,5 em 2023, mas 126,3 em 2021, ano de crise hídrica [89]. O fator acompanha a chuva, e a comparação entre 2024 e 2025 é afetada pela ampliação da base do ONS. A IEA, por outro método, registra alta de cerca de 8% em 2025, para mais de 70 gCO₂/kWh [34]. Os demais fatores e a escolha do fator estão na seção 5.4.

**Data centers: tamanho e expansão.**
- **Tamanho:** não há medição oficial do consumo.
  - Capacidade de TI: cerca de 800 a 843 MW em 2024 [95][94].
  - Consumo: a Brasscom estima 11,3 TWh em 2024 (1,7% do consumo nacional), mas a conta supõe operação a plena carga (843,1 MW × 8.760 h × PUE de 1,53) e é um teto [94]. A IEA atribui 1,4 TWh (2024) e 1,5 TWh (2025) a toda a América Central e do Sul, números que não servem para o Brasil [33].
  - Faixa a usar: de cerca de 2 a 11 TWh, sem dado oficial. O piso vem da revisão crítica da IEA 4E, que cita cerca de 700 MW de TI somando Brasil, Chile e México, com 2 a 3 TWh por ano [38]. Como as fontes brasileiras atribuem de 800 a 843 MW só ao Brasil, o piso tende a subestimar o país (leitura nossa).
- **Expansão:**
  - Pedidos de conexão: subiram de 19,8 GW para 26,2 GW entre setembro e novembro de 2025 (+32%). Se todos saíssem do papel, somariam mais de um quarto da demanda elétrica do país; só cerca de 6 GW estavam em análise ou em fase avançada [34].
  - Planejamento oficial: o PLAN 2026-2030 acrescenta 321 MW médios em 2026 e 2.157 MW médios em 2030 só de novos data centers ligados à rede básica. São cerca de 2,8 e 18,9 TWh por ano e, em 2030, cerca de 2,2% da carga projetada do SIN (cálculos nossos). O cenário não considera o Redata [91].
- **Contexto da política:** a exposição de motivos da medida provisória que deu origem ao Redata registra que o país tem cerca de 2% do mercado mundial de data centers (dados do Data Center Map), que cerca de 60% das cargas digitais nacionais são atendidas no exterior e que operar aqui custa em média 30% mais, sobretudo pelos tributos sobre equipamentos [93].

**Água.**
- **O teto do Redata:** 0,05 L/kWh [92], contra a média europeia de 0,58 L/kWh [84] e os 0,27 e 0,12 L/kWh de Microsoft e Amazon [53][54]. Na prática, o teto exige resfriamento quase sem água.
- **O que o WUE não vê:** a água da geração elétrica, que no Brasil inclui a evaporação dos reservatórios [46].
- **Estimativa para São Paulo:** um estudo estima que o polo de data centers de IA da Grande São Paulo, com cerca de 550 MW de TI, tem pegada hídrica de 16,1 milhões de m³ por ano, mais de 46% dela evaporada nos reservatórios hidrelétricos. As premissas são fortes: PUE de 1,5, WUE de 1,8 L/kWh e operação a plena carga [100].
- **O agregado nacional:** a Brasscom estima que os data centers usaram 0,003% do consumo de água do país em 2022, mas a conta inclui só a água direta, em agregado nacional, sem estresse hídrico local [94].

**Posicionamentos.**
- **Governo:** incentivo com contrapartidas hídricas e energéticas (Redata) e a "IA sustentável" como bandeira do Plano Brasileiro de IA [92][98].
- **Conselho ambiental e Ministério Público:** cautela com licenciamento simplificado, água e territórios [96][97].
- **Setor de TI:** estudo setorial que estima uso de água muito baixo, contando só a água direta [94].
- **Agro:** ausência do tema na pauta de TI do setor [74].

## 11. Números que não devem ser usados (ou só com ressalva)

| Afirmação popular | Problema | O que usar no lugar | Fonte |
|---|---|---|---|
| "Uma consulta ao ChatGPT gasta 10 vezes uma busca no Google (3 Wh × 0,3 Wh)" — ou "25 vezes", no relatório do Banco Mundial de 2025 | compara uma estimativa de 2023 (GPT-3.5, chips A100, muitos tokens) com um dado de busca de 2009; a fala original tratava de custo; o EPRI chama a regra de "cada vez mais desatualizada"; os "25 vezes" vêm de um jornal, sem método | de 0,2 a 0,4 Wh por consulta de texto (2025-2026), com fronteira declarada; 3,9 Wh ou mais com raciocínio longo | [2][4][5][6][7][10][37][48] |
| "O ChatGPT 'bebe' 500 mL a cada 20 a 50 perguntas" (ou 500 mL por pergunta) | número do GPT-3 (2020), da versão de 2023 do estudo; cerca de 87% é água da geração elétrica; a versão revisada fala em 10 a 50 respostas médias; nunca foi 500 mL por pergunta. Circula com variações: "20 a 50 consultas" (Capgemini, 2025), "29 a 50 perguntas" (Banco Mundial, 2025) e como água de resfriamento (Plano Brasileiro de IA) | por escopo: 0,26 mL (só local, Gemini); 16,9 mL (GPT-3, local + geração, média dos EUA); 45 mL (ACV, Mistral) | [18][7][17][58][48][98] |
| "A IA vai demandar de 4,2 a 6,6 bilhões de m³ de água em 2027, mais da metade do Reino Unido" | é retirada, não consumo, quase toda para resfriar termelétricas | consumo: de 0,38 a 0,60 bilhão de m³ em 2027; de 312,5 a 764,6 bilhões de L (0,31 a 0,76 bilhão de m³) só para sistemas de IA em 2025 | [18][40] |
| "Treinar um modelo emite o mesmo que cinco carros na vida útil (cerca de 284 t)" | caso extremo de busca de arquitetura (NAS), estimado em 2019; segundo o Google, a estimativa de energia ficou 18,7 vezes alta para uma organização média e, no data center real, a emissão foi de 3,2 t, 88 vezes menos | dados por modelo: GPT-3, 552 t LB; BLOOM, de 24,7 a 50,5 t LB; Llama 3.1, 11.390 t LB | [19][20][22][23] |
| "As emissões das big techs subiram 150% por causa da IA" | o comunicado da UIT de 2025 transformou "150% do nível de 2020" (alta de 50%) em "alta de 150%"; o relatório não atribui a alta só à IA | em 2024, de 192% a 239% do nível de 2020 | [42][41] |
| "Os data centers passam de 1.000 TWh em 2026, o consumo do Japão" ou "podem chegar a 3.000 TWh em 2030" | o primeiro era o topo de uma faixa de 620 a 1.050 TWh que incluía criptomoedas (IEA, 2024); o segundo, de uma diretriz do PNUMA, não tem fonte e fica acima de todos os cenários da IEA | 485 TWh em 2025; cerca de 950 TWh em 2030, numa faixa de 833 a 1.008 TWh entre cenários | [6][47][33] |
| "Os data centers de IA vão consumir 90 TWh em 2026, dez vezes 2022" | provável leitura errada de um crescimento anual como consumo absoluto | IA: de 10 a 50 TWh em 2023; de 200 a 400 TWh plausíveis em 2030 | [38] |
| "Os data centers de IA vão emitir 718 Mt em 2030, 3,4% das emissões globais" | incoerente: 718 Mt ÷ 612 TWh = 1,17 tCO₂/MWh, acima de uma térmica a carvão; o total global implícito seria de cerca de 21 Gt | todos os data centers: cerca de 180 Mt (2024) e 350 Mt (2035) | [72][32][33] |
| "A IA pode reduzir de 5% a 10% das emissões globais até 2030" | extrapolação da experiência com clientes, sem modelo, cenário contrafactual ou rebote | IEA: 1,4 Gt em 2035, condicionado à adoção; PwC: de −0,1% a −1,1%; Alpine et al.: aumento líquido possível | [73][32][62][102] |
| Versões superadas: "as emissões dos data centers chegam a 300 Mt em 2035 (500 Mt no cenário de alta)" e "a Microsoft estima 0,34 Wh por consulta" (número repetido pela IEA em 2026) | a primeira é a projeção de 2025, revisada pela própria IEA; a segunda vem da versão preliminar do estudo | cerca de 350 Mt em 2035; 0,31 Wh (intervalo interquartil de 0,16 a 0,60) na versão publicada | [32][33][10] |
| "Um prompt do Gemini gasta cinco gotas de água: a pegada da IA é desprezível" | mediana de texto; só água no local; carbono MB; exclui treino, imagem, vídeo, raciocínio e o volume total; não verificado de forma independente | citar como "prompt de texto mediano, mai/2025, carbono MB, água no local"; o consumo total do Google subiu 37% (eletricidade) e 34% (água) em 2025 | [7][49] |
| "IA 100% renovável" ou "treino com emissão zero" | contabilidade MB com casamento anual; o mesmo treino do Llama 3.1 emitiu 11.390 t LB; o CFE horário do Google é de cerca de 65% | reportar LB e MB e, se possível, o CFE horário | [23][49] |
| "As soluções de IA do Google evitaram três vezes as emissões da empresa" | 41 Mt "habilitadas" em terceiros, não verificadas; 27,8 Mt do Google Earth contam a geração inteira de usinas de parceiros | tratar à parte do inventário, como emissões evitadas | [49][87] |
| "Só 12% das empresas medem a pegada da IA" | dado de 2024; o mesmo relatório repete números superados de água e energia | em 2026, 38% medem a energia e 34% o carbono (amostra diferente, sem o Brasil) | [58][59] |
| "Llama 3.3 70B emitiu 11.390 t no treino" | é o total da família Llama 3.1; o model card do 3.3 é inconsistente, e o erro aparece num white paper de 2026 | Llama 3.1 70B: 7,0 milhões de horas de GPU e 2.040 t LB | [23][66] |
| "A IA generativa vai gerar 16 milhões de toneladas de lixo eletrônico até 2030" | cenário otimista de um preprint de 2024 (de 8 a 16 Mt acumuladas em 2020-2030, conforme o cenário); a versão publicada do mesmo estudo reduziu a faixa para 1,2 a 5,0 Mt acumuladas | de 131 a 224,8 mil t por ano em 2030 | [30][29] |
| "Gerar uma imagem gasta o mesmo que carregar um celular" | vale só para o pior modelo testado, e a versão preliminar usava uma carga de celular de 0,012 kWh; na versão publicada, com 0,022 kWh por carga, o pior caso dá cerca de meia carga por imagem | média de cerca de 2,9 Wh por imagem (2,907 kWh por 1.000 imagens) | [14] |
| "WUE baixo significa pegada hídrica baixa" | o WUE mede só a água no local; a da geração costuma ser maior (dois terços do total na IEA; cerca de 87% no caso do GPT-3) | reportar água local e indireta, retirada e consumo, e estresse hídrico | [32][18][46] |
| "O SIN emite um nono da média mundial" | compara o fator do MCTI (46,1 g, só CO₂, método de inventário) com a intensidade da IEA (435 g) | pela IEA (mais de 70 g/kWh) ou pela EPE (67,4 gCO₂e/kWh), cerca de um sexto; declarar o fator | [89][34][90] |
| "O Brasil consome 1,5 TWh em data centers" ou "11,3 TWh" | o primeiro é a IEA para toda a região, com capacidade subestimada; o segundo supõe plena carga | faixa de cerca de 2 a 11 TWh, sem dado oficial | [33][94][38] |
| "O relatório ISSB é obrigatório para companhias abertas desde 2026" | a obrigatoriedade foi revogada antes de valer | voluntário a partir de 2026; "pratique ou explique" a partir de 2027 | [85] |

## 12. Implicações para o benchmark

**F1 — Benchmark estratégico (fichas do painel).** A sustentabilidade da IA entra como subdimensão da governança de IA. Em fontes públicas, observar:
- se a empresa menciona a pegada da IA (energia, carbono, água) no relatório de sustentabilidade, no relatório integrado ou na política de IA;
- se mede, e como: LB e MB, unidade (por consulta, por token, por carga) e fronteira (treino, inferência, hardware);
- se tem meta ou critério formal, como sustentabilidade na escolha de modelo, de fornecedor ou de região de nuvem;
- se exige dados dos fornecedores (cláusulas, níveis de serviço de sustentabilidade);
- se separa o benefício (emissões evitadas por aplicações de IA) do inventário e com qual método;
- se usa IA para medir o próprio carbono: MRV, rastreabilidade, intensidade de carbono certificada.

Expectativa: pouca evidência pública no agro e na bioenergia (seção 7). A ausência é um achado do benchmark, não uma falha da ficha.

**F2 — Framework de maturidade.** Incluir "IA sustentável: medir, reportar, otimizar" como capacidade transversal, dentro de governança, com marcos na régua de cinco estágios usada nas sessões executivas. É uma leitura do mercado, não uma prescrição.

| Estágio | Medir | Reportar | Otimizar |
|---|---|---|---|
| 1. Exploração | nenhuma medição; circulam números genéricos (risco dos mitos da seção 11) | — | — |
| 2. Pilotos | inventário dos serviços de IA usados e de onde rodam; estimativa pelo gasto (escopo 3, categoria 1) | menção qualitativa no relatório de sustentabilidade | escolha de modelo e de região considerada nos pilotos |
| 3. Operacionalização | estimativa pela atividade (tokens ou consultas × intensidade × PUE × fator da rede), LB e MB | linha própria no inventário, com método declarado | critérios ambientais nas compras: dado do fornecedor, região, PUE e WUE |
| 4. Escala | dado do provedor (kgCO₂e/MTok); água local e indireta; carbono incorporado do hardware próprio | metas específicas para IA; divulgação de energia, carbono e água; asseguração externa | modelo do tamanho da tarefa; raciocínio só quando agrega; inferência otimizada; vida útil do hardware |
| 5. Transformação | intensidade por resultado (por decisão, por tonelada produzida); CFE horário | benefício líquido medido contra cenário de referência, separado do inventário | IA como alavanca verificável de descarbonização, por exemplo na intensidade de carbono certificada |

Calibragem: só 18% das empresas têm metas mensuráveis específicas para IA e 4% se dizem "otimizadas" [60]; 38% medem a energia e 34% o carbono da IA [59]. A maioria do mercado está entre os estágios 1 e 3 nessa capacidade (leitura nossa).

**F3 — Tendências, riscos e oportunidades.**
- **Licença para operar.** Cresce a resistência pública e institucional aos data centers, da ONU [1] ao CONAMA e ao MPF [96][97]. Para quem usa IA, o risco é de associação e de alegações frágeis.
- **Custo e disponibilidade de energia.**
  - Os data centers podem levar a demanda elétrica dos EUA a 9% a 17% do total em 2030 [37], e os pedidos de conexão no Brasil chegaram a 26,2 GW [34].
  - O gás supre parte relevante da expansão [32][33]. Microsoft e Anthropic já se comprometem a não encarecer a conta de luz local [53][57].
  - A IA fica mais cara e mais disputada em energia; o raciocínio e os agentes multiplicam o consumo por tarefa (seção 3.2).
- **Regulação.**
  - Na UE: documentação de energia dos modelos, possível rótulo e padrões mínimos para data centers [82][84].
  - No Brasil: WUE do Redata e diretrizes de licenciamento pedidas pelo CONAMA [92][96].
  - No GHG Protocol: possível casamento horário, que tenderia a elevar as emissões MB atribuídas à IA (leitura nossa) [79].
  - No ISSB e na CVM: reporte voluntário, com "pratique ou explique" para companhias abertas [85].
- **Oportunidades.**
  - A matriz brasileira, se o processamento for local [89][93].
  - A demanda de data centers e big techs por combustíveis renováveis e certificados (HVO para geradores, SAF no escopo 3) [53][54][49].
  - A IA a serviço de MRV e certificação, com ganho verificável em gCO₂e/MJ [109].
- **Alerta de capital.** Segundo a coluna da MIT Technology Review, o capital de risco climático cresce puxado por soluções para data centers, enquanto o destinado a combustíveis de baixo carbono despencou em 2026 [1]. É um ponto a acompanhar no financiamento do setor.

**Sessões executivas: duas perguntas opcionais para o roteiro.** Sugestão: incluir como perguntas 11 e 12, antes do encerramento, se houver tempo; ou encaixar a 11 logo depois da pergunta 5 (governança e riscos). O nível continua macro.
- **11. Pegada da IA (Frentes 1 e 3).** "A pegada ambiental da IA, em energia, carbono e água, já entrou na pauta da empresa? Vocês medem, reportam ou usam isso como critério na escolha de modelos, fornecedores ou de onde processar os dados?"
  - Quem pergunta sobre isso hoje: conselho, clientes, financiadores, auditores?
  - Há meta, ou só acompanhamento?
- **12. Coerência com a sustentabilidade (Frentes 2 e 3).** "Para uma empresa de bioenergia, que vende redução de emissões, como você equilibraria a expansão da IA com a coerência da narrativa de sustentabilidade? A IA já ajuda a medir ou a reduzir a intensidade de carbono do produto?"

Como nas demais perguntas, pedir evidência ("qual iniciativa mostra isso?") e trazer a conversa de volta à lógica da decisão se entrar em ferramentas.

## 13. O que o mercado mede

Indicadores que empresas líderes acompanham para a pegada da IA, em nível macro:
1. **Eletricidade:** total e dos data centers (TWh), com a variação anual [49][52].
2. **Emissões:** escopo 2 pelos dois métodos (LB e MB) e escopo 3 com a cadeia de hardware e a construção [49][52][55].
3. **Qualidade do suprimento:** energia livre de carbono horária, além da fração renovável anual [49][84].
4. **Eficiência do data center:** PUE e WUE, com a fronteira declarada [49][53][54].
5. **Água:** retirada, consumo, reposição e parcela em áreas de estresse hídrico [49][52].
6. **Uso:** Wh, gCO₂e e mL por prompt (Google), por consulta (estudo da Microsoft) e ACV por resposta (Mistral) [7][10][17].
7. **Modelo:** energia e emissões de treino, LB e MB (model cards) [23].
8. **Hardware:** carbono incorporado por produto, intensidade de carbono por computação e taxa de reúso e reciclagem de servidores [26][27][53].
9. **Intensidade por resultado:** emissões por token e por unidade de energia [68][49].
10. **Usuários corporativos:** escopo 3 da IA comprada (kgCO₂e por milhão de tokens), metas específicas para IA e critérios ambientais na escolha de fornecedores [66][60].
11. **Benefício:** emissões evitadas ou "habilitadas", reportadas à parte do inventário e, idealmente, com método de efeito líquido [49][87][88].

O que ainda falta medir:
- a parcela da IA nos inventários;
- as emissões de IA por cliente, informadas pelos provedores de nuvem;
- a água indireta;
- uma unidade funcional comum entre provedores (consulta média, prompt mediano ou resposta de 400 tokens).

## Fontes

**Contexto e transparência**
1. Crownhart, C. IA domina as conversas na Climate Week. MIT Technology Review Brasil, 2026 (PDF salvo em 01/10/2026). https://mittechreview.com.br/ (URL da matéria não registrada; cópia em `_triagem-pesquisa/10_ia-sustentabilidade/MITTRBrasil_2026_ia-domina-conversas-climate-week.pdf`)
2. Luccioni, S.; Gamazaychikov, B.; Alves da Costa, T.; Strubell, E. Misinformation by Omission: The Need for More Environmental Transparency in AI. arXiv 2506.15572, 2025. https://arxiv.org/abs/2506.15572
3. Luccioni, S.; Strubell, E.; Crawford, K. From Efficiency Gains to Rebound Effects: The Problem of Jevons' Paradox in AI's Polarized Environmental Debate. ACM FAccT, 2025. https://doi.org/10.1145/3715275.3732007

**Energia, carbono e água por uso**

4. Google (Hölzle, U.). Powering a Google search. Official Google Blog, 11/01/2009. https://googleblog.blogspot.com/2009/01/powering-google-search.html
5. de Vries, A. The growing energy footprint of artificial intelligence. Joule 7(10):2191-2194, 2023. https://doi.org/10.1016/j.joule.2023.09.004
6. IEA. Electricity 2024 – Analysis and forecast to 2026. 2024. https://iea.blob.core.windows.net/assets/6b2fd954-2017-408e-bf08-952fdd62118a/Electricity2024-Analysisandforecastto2026.pdf
7. Elsworth, C. et al. (Google). Measuring the environmental impact of delivering AI at Google Scale. arXiv 2508.15734, 2025. https://arxiv.org/abs/2508.15734
8. Altman, S. (OpenAI). The Gentle Singularity. Blog, jun/2025. https://blog.samaltman.com/the-gentle-singularity
9. You, J. (Epoch AI). How much energy does ChatGPT use? 2025. https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
10. Oviedo, F. et al. (Microsoft). Energy use of AI inference, efficiency pathways, and test-time scaling. Joule 10, 102430, 2026 (arXiv 2509.20241 v2). https://doi.org/10.1016/j.joule.2026.102430
11. Microsoft. Scaling AI with 8 to 20x energy efficiency. Microsoft Cloud Blog, 15/06/2026. https://www.microsoft.com/en-us/microsoft-cloud/blog/2026/06/15/scaling-ai-with-8-to-20x-energy-efficiency/
12. Luccioni, S.; Gamazaychikov, B. (Hugging Face e Salesforce). AI Energy Score v2: Refreshed Leaderboard, now with Reasoning. Dez/2025. https://huggingface.co/blog/sasha/ai-energy-score-v2
13. Jegham, N. et al. How Hungry is AI? Benchmarking Energy, Water, and Carbon Footprint of LLM Inference. arXiv 2505.09598, 2025. https://arxiv.org/abs/2505.09598
14. Luccioni, S.; Jernite, Y.; Strubell, E. Power Hungry Processing: Watts Driving the Cost of AI Deployment? ACM FAccT, 2024. https://arxiv.org/abs/2311.16863
15. Kim, J.; Shin, B.; Chung, J.; Rhu, M. (KAIST). The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling from an AI Infrastructure Perspective. arXiv 2506.04301, 2025. https://arxiv.org/abs/2506.04301
16. Delavande, J.; Pierrard, R.; Luccioni, S. Video Killed the Energy Budget: Characterizing the Latency and Power Regimes of Open Text-to-Video Models. arXiv 2509.19222, 2025. https://arxiv.org/abs/2509.19222
17. Mistral AI (com Carbone 4 e ADEME). Our contribution to a global environmental standard for AI. 22/07/2025. https://mistral.ai/news/our-contribution-to-a-global-environmental-standard-for-ai
18. Li, P.; Yang, J.; Islam, M. A.; Ren, S. Making AI Less "Thirsty": Uncovering and Addressing the Secret Water Footprint of AI Models. arXiv 2304.03271 v5, 2025; Communications of the ACM 68(7), 2025. https://arxiv.org/abs/2304.03271

**Treino, hardware e resíduos**

19. Strubell, E.; Ganesh, A.; McCallum, A. Energy and Policy Considerations for Deep Learning in NLP. ACL, 2019. https://aclanthology.org/P19-1355.pdf
20. Patterson, D. et al. (Google e UC Berkeley). Carbon Emissions and Large Neural Network Training. arXiv 2104.10350, 2021. https://arxiv.org/abs/2104.10350
21. Patterson, D. et al. The Carbon Footprint of Machine Learning Training Will Plateau, Then Shrink. IEEE Computer, 2022. https://arxiv.org/abs/2204.05149
22. Luccioni, S.; Viguier, S.; Ligozat, A.-L. Estimating the Carbon Footprint of BLOOM, a 176B Parameter Language Model. Journal of Machine Learning Research 24, 2023. https://jmlr.org/papers/volume24/23-0069/23-0069.pdf
23. Meta. Llama 3.1 Model Card e Llama 4 Model Card (repositório meta-llama/llama-models). 2024-2025. https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md e https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md
24. Morrison, J. et al. (Allen Institute for AI). Holistically Evaluating the Environmental Impact of Creating Language Models. ICLR, 2025. https://arxiv.org/abs/2503.05804
25. Wu, C.-J. et al. (Meta). Sustainable AI: Environmental Implications, Challenges and Opportunities. MLSys, 2022. https://arxiv.org/abs/2111.00364
26. NVIDIA. Product Carbon Footprint (PCF) Summary – NVIDIA HGX H100 e HGX B200. 2025. https://images.nvidia.com/aem-dam/Solutions/documents/HGX-H100-PCF-Summary.pdf e https://images.nvidia.com/aem-dam/Solutions/documents/HGX-B200-PCF-Summary.pdf
27. Schneider, I. et al. (Google). Life-Cycle Emissions of AI Hardware: A Cradle-To-Grave Approach and Generational Trends. arXiv 2502.01671, 2025. https://arxiv.org/abs/2502.01671
28. Baeuerle, T. et al. (Hasso Plattner Institute). Green or Greedy? An Ecological Analysis of Data Center GPU Replacements. ICDE, 2026. https://hpi.de/oldsite/fileadmin/user_upload/fachgebiete/rabl/publications/2026/green-or-greedy-icde2026.pdf
29. de Vries-Gao, A. Recalibrating global artificial intelligence e-waste estimates. Resources, Conservation and Recycling 229, 108872, 2026 (resumo da VU Amsterdam, 27/02/2026: https://vu.nl/en/news/2026/new-estimate-of-ai-e-waste). https://doi.org/10.1016/j.resconrec.2026.108872
30. Wang, P.; Zhang, L.-Y.; Tzachor, A.; Masanet, E.; Chen, W.-Q. E-waste Challenges of Generative Artificial Intelligence (preprint v1). Research Square, 2024. https://www.researchsquare.com/article/rs-3978528/v1 ; versão publicada: Wang, P.; Zhang, L.-Y.; Tzachor, A.; Chen, W.-Q. E-waste challenges of generative artificial intelligence. Nature Computational Science 4:818-823, 28/10/2024 (resumo conferido via Europe PMC). https://doi.org/10.1038/s43588-024-00712-6
31. UIT e UNITAR. The Global E-waste Monitor 2024. https://ewastemonitor.info/the-global-e-waste-monitor-2024/

**Agregados, projeções e fatores**

32. IEA. Energy and AI (World Energy Outlook Special Report). 2025. https://iea.blob.core.windows.net/assets/de9dea13-b07d-42c5-a398-d1b3ae17d866/EnergyandAI.pdf
33. IEA. Key Questions on Energy and AI (World Energy Outlook Special Report). 2026. https://iea.blob.core.windows.net/assets/3179f7f8-01f6-4dd6-bffa-c9f7b73f1dc9/KeyQuestionsonEnergyandAI.pdf
34. IEA. Electricity 2026 – Analysis and forecast to 2030. 2026. https://iea.blob.core.windows.net/assets/b73798cb-e452-42b9-9d8a-07542de7a041/Electricity_2026.pdf
35. Shehabi, A. et al. (Lawrence Berkeley National Laboratory). 2024 United States Data Center Energy Usage Report. 2024. https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report.pdf
36. Lawrence Berkeley National Laboratory. United States Data Center Energy Usage Report: 2025 Update. 2026. https://escholarship.org/content/qt33m6w3x0/qt33m6w3x0.pdf
37. EPRI. Powering Intelligence 2026: Updated Scenarios of U.S. Data Center Electricity Use and Power Strategies. 2026. https://restservice.epri.com/publicdownload/000000003002034696/0/Product
38. Kamiya, G.; Coroamă, V. (IEA 4E TCP / EDNA). Data Centre Energy Use: Critical Review of Models and Results. 2025. https://www.iea-4e.org/wp-content/uploads/2025/05/Data-Centre-Energy-Use-Critical-Review-of-Models-and-Results.pdf
39. Gartner. Gartner Says Data Center Electricity Consumption to Grow 26% in 2026 (press release). 10/06/2026. https://www.gartner.com/en/newsroom/press-releases/2026-06-10-gartner-says-data-center-electricity-demand-to-grow-26-percent-in-2026 (a previsão anterior, de 980 TWh em 2030, é do comunicado de 17/11/2025; URL não registrada)
40. de Vries-Gao, A. The carbon and water footprints of data centers and what this could mean for artificial intelligence. Patterns 7, 101430, 2026. https://doi.org/10.1016/j.patter.2025.101430
41. UIT e World Benchmarking Alliance. Greening Digital Companies 2026. https://www.itu.int/en/ITU-D/Environment/Documents/Publications/2026/Greening%20Digital%20Companies%202026_vf.pdf
42. UIT e World Benchmarking Alliance. Greening Digital Companies 2025 (https://www.itu.int/en/ITU-D/Environment/Documents/Publications/2025/Greening%20Digital%20Companies%202025%20Final.pdf) e comunicado de imprensa de 05/06/2025. https://www.itu.int/en/mediacentre/Pages/PR-2025-06-05-greening-digital-companies-report.aspx
43. Uptime Institute. Global Data Center Survey 2025. https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2025.Annual.Survey.Report.pdf
44. U.S. EPA. eGRID2023 Summary Tables (revisão 2). Jun/2025. https://www.epa.gov/system/files/documents/2025-06/summary_tables_rev2.pdf
45. Google Cloud. Carbon free energy for Google Cloud regions (dados de 2025). 2026. https://cloud.google.com/sustainability/region-carbon
46. Reig, P. et al. (World Resources Institute, com WSP). Guidance for Calculating Water Use Embedded in Purchased Electricity. 2020. https://files.wri.org/d8/s3fs-public/guidance-calculating-water-use-embedded-purchased-electricity_0.pdf
47. PNUMA (United for Efficiency). Sustainable Procurement Guidelines for Data Centres and Servers. 2025. https://united4efficiency.org/wp-content/uploads/2025/02/2025-U4E-Sustainable-Procurement-for-Data-Centers-and-Servers_Final.pdf
48. Banco Mundial. Digital Progress and Trends Report 2025: Strengthening AI Foundations. 2025. https://documents1.worldbank.org/curated/en/099112525160536089/pdf/P505350-59c98ca8-0803-4f23-b470-17f3dab010ab.pdf

**Big techs e desenvolvedoras de modelos**

49. Google. 2026 Environmental Report (dados de 2025). https://sustainability.google/reports/google-2026-environmental-report/
50. Google. 2024 Environmental Report (dados de 2023). https://www.gstatic.com/gumdrop/sustainability/google-2024-environmental-report.pdf
51. Pichai, S. (Google). Google I/O 2026: keynote de abertura. 19/05/2026. https://blog.google/intl/en-in/company-news/technology/sundar-pichai-io-2026/
52. Microsoft. 2026 Environmental Data Fact Sheet (ano fiscal de 2025). https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Data-Fact-Sheet-PDF.pdf
53. Microsoft. 2026 Environmental Sustainability Report (ano fiscal de 2025). https://aka.ms/SustainabilityReport2026
54. Amazon. 2025 Amazon Sustainability Report. 2026. https://sustainability.aboutamazon.com/2025-amazon-sustainability-report.pdf
55. Meta. 2025 Environmental Data Index (dados de 2024). https://sustainability.atmeta.com/wp-content/uploads/2025/10/Meta_2025-Environmental-Data-Index.pdf
56. NVIDIA. Sustainability Report Fiscal Year 2026. https://images.nvidia.com/aem-dam/Solutions/documents/NVIDIA-Sustainability-Report-Fiscal-Year-2026.pdf
57. Anthropic. The Claude 3 Model Family – Model Card, seção 4.3 (2024), https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf; e Covering electricity price increases from our data centers (2026), https://www.anthropic.com/news/covering-electricity-price-increases

**Consultorias, analistas e empresas usuárias**

58. Capgemini Research Institute. Developing sustainable Gen AI. Jan/2025. https://www.capgemini.com/wp-content/uploads/2025/01/Final-Web-Version-Report-Sustainable-Gen-AI-2.pdf
59. Capgemini Research Institute. A world in balance 2026: The resilience reset. 2026. https://www.capgemini.com/wp-content/uploads/2026/09/Final-Web-Version-Report-Sustainability-Trends.pdf
60. KPMG LLP. Sustainable AI is the new performance frontier. 2026. https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/sustainable-ai.pdf
61. PwC. State of Decarbonization 2026. https://www.pwc.com/us/en/services/esg/library/decarbonization-strategic-plan.html
62. PwC. Could net-zero AI become a reality? (Value in Motion). 2025. https://www.pwc.com/gx/en/issues/value-in-motion/ai-energy-consumption-net-zero.html
63. Deloitte Global. 2026 C-suite Sustainability Report. 2026. https://www.deloitte.com/content/dam/assets-shared/docs/about/2026/2026-deloitte-global-c-suite-sustainability-report-secured.pdf
64. Kyndryl e Microsoft (pesquisa Ecosystm). From Planning to Progress: AI-Driven Sustainability in Practice – Global Sustainability Barometer 2025. https://www.kyndryl.com/content/dam/kyndrylprogram/doc/en/2025/sustainability-barometer.pdf
65. Logicalis. 2026 CIO Report (press release). 03/03/2026. https://www.logicalis.com/insights/cio-report-2026-ai-investment-governance
66. Bistline, J. et al. (Watershed). Estimating GHG Emissions from AI Use: Framework for Corporate-Level Measurement. arXiv 2608.06733, 2026. https://arxiv.org/abs/2608.06733
67. Salesforce. AI Sustainability Outlook: The Challenges, Potential, and Path Forward. Ago/2025. https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/company/sustainability/salesforce-ai-sustainability-outlook.pdf
68. SAP. AI and Sustainability at SAP (2025), https://www.sap.com/sea/docs/download/2025/11/56a1a0fa-2e7f-0010-bca6-c68f7e60039b.pdf; e Integrated Report 2025 (2026), https://www.sap.com/docs/download/investors/2025/sap-2025-integrated-report.pdf
69. Crédit Agricole Group. Artificial Intelligence Policy. 2026. https://www.credit-agricole.com/en/pdfPreview/210816
70. Fernandez, J. et al. Energy Considerations of Large Language Model Inference and Efficiency Optimizations. ACL, 2025. https://aclanthology.org/2025.acl-long.1563.pdf
71. Dodge, J. et al. Measuring the Carbon Intensity of AI in Cloud Instances. ACM FAccT, 2022. https://doi.org/10.1145/3531146.3533234
72. Accenture. Powering sustainable AI. 2025. https://www.accenture.com/content/dam/accenture/final/corporate/corporate-initiatives/sustainability/document/Powering-Sustainable-AI.pdf
73. BCG. Reduce Carbon and Costs with the Power of AI (2021), https://www.bcg.com/publications/2021/ai-to-reduce-carbon-emissions; e BCG e Google, Accelerating Climate Action with AI (2023), https://web-assets.bcg.com/72/cf/b609ac3d4ac6829bae6fa88b8329/bcg-accelerating-climate-action-with-ai-nov-2023-rev.pdf
74. Gatua. TI do Futuro — Do Centro de Custo ao Pilar Estratégico (ebook do Gatua Meeting E01, 21/05/2026). Material de evento, sem URL pública; cópia em `docs/referencias/`; citar com atribuição, sem reproduzir.

**Padrões e regulação**

75. Green Software Foundation. Software Carbon Intensity (SCI) Specification v1.1 (base da ISO/IEC 21031:2024). https://sci.greensoftware.foundation/ ; ISO: https://www.iso.org/standard/86612.html
76. Green Software Foundation. SCI for AI Specification Ratified. 17/12/2025. https://greensoftware.foundation/articles/sci-ai-specification-ratified-standard-for-measuring-ai-emissions-across-the/
77. UIT (ITU-T, Comissão de Estudos 5). Recommendation ITU-T L.1801 – Guidelines for assessing the environmental impact of artificial intelligence systems. Fev/2026. https://www.itu.int/rec/T-REC-L.1801-202602-I/en
78. Coalizão para IA Sustentável (com ISO, UIT, IEEE, OCDE e UNESCO). Standardization for AI Environmental Sustainability — Towards a coordinated global approach (atualização de 2026). https://www.itu.int/en/ITU-T/studygroups/2025-2028/05/Documents/AI%20Impact%20Summit%20Logo_Global_Approach_AI_Summit_2026%20Update_FINAL.pdf
79. GHG Protocol. Scope 2 Public Consultation – Summary of Feedback. 29/07/2026. https://ghgprotocol.org/sites/default/files/2026-07/S2-PublicConsultationSummaryofFeedback-2026.07.29.pdf
80. GHG Protocol. Corporate Standard – Consolidated Standard Development Plan. 29/07/2026. https://ghgprotocol.org/sites/default/files/2026-07/Consolidated-StandardDevelopmentPlan(SDP)-2026.07.29.pdf
81. Comissão Europeia (AI Office). Code of Practice for General-Purpose AI Models – Transparency Chapter. Jul/2025. https://ec.europa.eu/newsroom/dae/redirection/document/118120
82. Comissão Europeia. Targeted consultation on measuring energy consumption and emissions of AI models and systems. 2026. https://digital-strategy.ec.europa.eu/en/consultations/targeted-consultation-measuring-energy-consumption-and-emissions-ai-models-and-systems
83. União Europeia. Regulamento (UE) 2024/1689 (AI Act), arts. 40, 53, 112 e 113 e Anexo XI. https://eur-lex.europa.eu/eli/reg/2024/1689/oj
84. Comissão Europeia. Report on the energy efficiency of data centres in the EU – COM(2026) 500. 21/09/2026. https://energy.ec.europa.eu/document/download/8a87a5fe-0260-462a-b165-09f1496d1aa0_en?filename=COM_2026_500_1_EN_ACT_part1_v4.pdf
85. CVM. Resolução CVM nº 244, de 29 de maio de 2026 (altera a Resolução CVM nº 193/2023). https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/resolucoes/anexos/200/resol244.pdf
86. FGVces / FGV EAESP. Perguntas Frequentes – Programa Brasileiro GHG Protocol (v1.3). 2026. https://eaesp.fgv.br/sites/default/files/uploads/FGVces/PROJETOS/Programa%20Brasileiro%20GHG%20Protocol/faq_ghg.pdf
87. WBCSD. Guidance on Avoided Emissions: Helping business drive innovations and scale solutions toward Net Zero. 2023. https://www.wbcsd.org/wp-content/uploads/2023/09/Climate-Avoided-Emissions-guidance_WBCSD.pdf
88. UIT (ITU-T). Recommendation ITU-T L.1480 – Enabling the Net Zero transition: Assessing how the use of ICT solutions impacts greenhouse gas emissions of other sectors. Jul/2025. https://www.itu.int/rec/T-REC-L.1480-202507-I/en

**Brasil**

89. MCTI. Fator médio de emissão do SIN – Inventários corporativos (planilha Inventario_2026_janago.xlsx, atualizada em 16/09/2026; https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/sirene/dados-e-ferramentas/fatores-de-emissao/arquivo/Inventario_2026_janago.xlsx) e nota de jun/2025 sobre a ampliação da base do ONS (https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/cgcl/paginas/NT_FE_jun25.pdf).
90. EPE. Balanço Energético Nacional 2026 – Relatório Síntese, ano base 2025. https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-975/topico-847/BEN_S%C3%ADntese_2026_PT.pdf
91. EPE, ONS e CCEE. Nota Técnica EPE-DEA-SEE-013/2026 – Previsão de carga para o Planejamento Anual da Operação Energética 2026-2030. 2026. https://www.ons.org.br/AcervoDigitalDocumentosEPublicacoes/Nota%20T%C3%A9cnica%20-%20Previs%C3%A3o%20de%20Carga%20para%20o%20Planejamento%20Anual%20da%20Opera%C3%A7%C3%A3o%20Energ%C3%A9tica%20-%202026-2030.pdf
92. Brasil. Lei nº 15.504, de 15 de setembro de 2026 (Redata). https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15504.htm
93. Brasil (MDIC, MF e MME). Exposição de Motivos EMI nº 10/2025 – Medida Provisória nº 1.318/2025. https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/exm/exm-1318-25.pdf
94. Brasscom (com ABDC). Estudo sobre o Consumo de Energia e Água em Data Centers no Brasil. 2025. https://brasscom.org.br/wp-content/uploads/2025/08/Estudo-sobre-o-Consumo-de-Energia-e-Agua-em-Data-Centers-no-Brasil-v7.pdf
95. CGI.br / NIC.br (Cetic.br). Data centers no Brasil — Panorama Setorial da Internet, ano 17, n. 4. 2025. https://www.cgi.br/media/docs/publicacoes/6/pt-br/20251209175312/psi-a17-n4-data_centers_no_brasil.pdf
96. CONAMA (MMA). Moção nº 147, de 22 de junho de 2026. https://conama.mma.gov.br/?id=858&option=com_sisconama&task=arquivo.download
97. MPF (Procuradoria da República no Ceará) e DPU. MPF e DPU pedem adequações em licenciamento ambiental de data center antes do início da operação no Ceará. 20/05/2026. https://www.mpf.mp.br/o-mpf/unidades/pr-ce/noticias/mpf-e-dpu-pedem-adequacoes-em-licenciamento-ambiental-de-data-center-no-ceara-antes-do-inicio-da-operacao
98. MCTI e CGEE. IA para o bem de todos — Plano Brasileiro de Inteligência Artificial 2024-2028 (versão final). 2025. https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/transformacaodigital/plano-brasileiro-de-inteligencia-artificial-pbia-_vf.pdf
99. Ministério da Fazenda. Taxonomia Sustentável Brasileira – Caderno Eletricidade e Gás (CNAE D). 2025. https://www.gov.br/fazenda/pt-br/orgaos/spe/taxonomia-sustentavel-brasileira/cadernos/02-4_tsb_cnae-d.pdf
100. Liang, G. The cloud's thirst: Quantifying AI's water footprint and its impact on the water-energy nexus in São Paulo, Brazil. Cambridge Prisms: Water 4, e11, 2026. https://doi.org/10.1017/wat.2026.10020

**IA a favor do clima, agro e biocombustíveis**

101. Stern, N. et al. (LSE Grantham Research Institute e Systemiq). Green and intelligent: the role of AI in the climate transition. npj Climate Action 4:56, 2025. https://doi.org/10.1038/s44168-025-00252-3
102. Alpine, M.; Geldner, N.; Alpine, R.; Chepeliev, M. AI-driven productivity gains enable more CO₂ emissions than they avoid in a global energy–economy model. npj Climate Action 5:71, 2026. https://doi.org/10.1038/s44168-026-00411-0
103. Joshi, K. (Beyond Fossil Fuels e ONGs parceiras). The AI Climate Hoax: Behind the Curtain of How Big Tech Greenwashes Impacts. 2026. https://beyondfossilfuels.org/2026/02/17/the-ai-climate-hoax-behind-the-curtain-of-how-big-tech-greenwashes-impacts/
104. Rahimi Azghadi, M. et al. (James Cook University). Precision Robotic Spot-Spraying: Reducing Herbicide Use and Enhancing Environmental Outcomes in Sugarcane. Computers and Electronics in Agriculture, 2024 (arXiv 2401.13931). https://arxiv.org/abs/2401.13931
105. CGIAR. 2024 Breakthrough Agenda Report — Reducing emissions from fertilizer application via site-specific nutrient management (ficha 4). 2024. https://agriculture-breakthrough2024.cgiar.org/wp-content/uploads/Factsheet-4-Reducing-emissions-from-fertilizer-application-via-site-specific-nutrient-management.pdf
106. FAO. FAO Global Conference on Smart Farming (notícia, 12/05/2026). https://www.fao.org/plant-production-protection/news-and-events/news/news-detail/fao-global-conference-on-smart-farming/en
107. IEA e IndiaAI Mission. Casebook on AI in Energy. 2026. http://d19ob9sqegt2wc.cloudfront.net/stage/uploads/Casebook_on_AI_A5_202447a94e.pdf
108. Freitas, R. et al. An AI-driven de novo design and optimisation of sustainable aviation fuels. Energy and AI 25, 100791, 2026. https://doi.org/10.1016/j.egyai.2026.100791
109. Pereira, L. G. et al. (Embrapa, CNPEM e outros; publicado pela ANP). RenovaCalc: Calculation of Carbon Intensities Under Brazil's National Biofuel Policy. Sustainability 17:10442, 2025. https://www.gov.br/anp/pt-br/assuntos/renovabio/arq/arquivos-estudos-relatorio-e-seminarios/renovacalc-pereira-et-al-2025.pdf
110. Google Research. How AI is helping airlines mitigate the climate impact of contrails. 2023. https://blog.google/technology/ai/ai-airlines-contrails-climate-change/

## Nota de verificação

- **Base:** os números vêm das duas verificações de fontes desta rodada (ciência, agências e métricas; empresas, consultorias, regulação e Brasil), usando só os itens com status "confirmado" e as correções indicadas.
- **Conferidos na redação:** outros números foram conferidos diretamente no PDF da fonte primária: BEN 2026 (86,8%), exposição de motivos do Redata (60% das cargas no exterior), Resolução CVM 244, ITU-T L.1801, SCI e SCI for AI, GHG Protocol (consulta e cronograma), AI Act (documentação de energia, a partir da consulta da Comissão), Moção 147 do CONAMA, recomendação do MPF e da DPU, Programa Brasileiro GHG Protocol, PLAN 2026-2030 (carga do SIN e Redata), Liang, Plano Brasileiro de IA, IEA (mix físico de 2024, casamento horário, mandatos de PUE, quadro de políticas, Irlanda, cortes de geração no Brasil, UE com 170 g/kWh, pequenos reatores, PPAs, metano e rebote do petróleo), BLOOM, OLMo, tarefas, agentes, vídeo, otimização de inferência, região de nuvem, troca de GPU, lixo eletrônico, práticas de SAP, Salesforce e Crédit Agricole, pesquisas de Deloitte, Kyndryl e Logicalis, compras de HVO e de certificados de SAF por big techs, aplicações em agro e biocombustíveis, levantamento das ONGs e afirmações do Banco Mundial.
- **Revisão crítica (01/10/2026):** mais de 60 números foram reconferidos nos PDFs locais (`_triagem-pesquisa/10_ia-sustentabilidade/`), entre eles os valores-padrão e o exemplo de Bistline et al., o eGRID, a nota do MCTI, o WRI, o Uptime, a IEA (Electricity 2026, Energy and AI e Key Questions), Microsoft, Amazon, Google, SAP, Meta, NVIDIA, Dodge, Luccioni, KAIST, Delavande, OLMo, BLOOM, Patterson (2021), HPI, de Vries-Gao, Liang, RenovaCalc, BEN 2026, PLAN 2026-2030, Brasscom, CGI.br, IEA 4E, EPRI, Comissão Europeia, GHG Protocol, Programa Brasileiro GHG Protocol, CVM, CONAMA, MPF e as pesquisas de Deloitte, Kyndryl, Logicalis e KPMG. As contas do exemplo da seção 5.5 foram refeitas.
- **Fora do texto:** números da pesquisa que não puderam ser conferidos ficaram de fora ou aparecem com a ressalva "não conferido".
- **Pendências antes de entregável:**
  - abrir a correção dos autores de Alpine et al. (set/2026); o site da revista exige login e o Crossref só registra a data (08/09/2026);
  - reconferir as afirmações do Banco Mundial ("25 vezes" e "29 a 50 perguntas"), cujo PDF não está salvo localmente, e registrar a URL do comunicado do Gartner de 17/11/2025;
  - conferir o formulário de documentação do Código de Prática da UE (campos de energia);
  - conferir no texto do AI Act, no EUR-Lex, a redação dos arts. 40 e 112 e as datas de aplicação, citadas sem cópia local;
  - registrar as fontes em `06_fontes/`.
