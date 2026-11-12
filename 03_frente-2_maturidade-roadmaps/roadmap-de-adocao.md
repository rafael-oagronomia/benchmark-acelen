# Roadmap de adoção de IA — trajetória, checkpoints, papéis e política de uso — nota temática

> Documento de trabalho da OagronomIA · Frente 2 — Maturidade e roadmaps · Fontes públicas do catálogo e registros anonimizados das sessões executivas · Data de corte: 04/11/2026 · Base: framework de maturidade de 30/09/2026 (BIA-ACL-FM-01, rev. 00, para discussão), conciliado com a régua do estudo · Entrega parcial em revisão — não encaminhar ao cliente sem revisão.

**Como ler.** [M###, p. N] remete ao item do catálogo de fontes e à página do PDF catalogado (numeração do arquivo, que pode diferir da impressa); [M###, web], à página web do catálogo, usada só com o que ali está registrado. [S-01] a [S-04] remetem aos registros anonimizados das sessões executivas, usados só no agregado. "Leitura nossa" marca interpretação da equipe. É referência de mercado: a nota não avalia nem recomenda ferramenta e não desenha a solução interna de nenhuma empresa.

## 1. Resumo em uma página

- **Não existe caminho publicado; existe uma sequência que se repete** (leitura nossa, a partir de dez jornadas de empresas e das pesquisas de maturidade):
  1. alicerce de dados e de campo;
  2. estrutura dedicada;
  3. IA preditiva em dores medidas;
  4. IA generativa para todos;
  5. governança com democratização;
  6. agentes com cautela.

  Detalhes na seção 3.
- **Sair do piloto é o salto que mais pesa.**
  - No MIT CISR, empresas nos estágios 1 e 2 crescem e lucram abaixo da média do setor; nos estágios 3 e 4, acima [M189, p. 4; M190, p. 9].
  - No Gartner, só 48% dos projetos de IA chegam à produção, em média, e o caminho leva 8 meses (644 respondentes, 4º tri/2023) [M122, web].
- **O ritmo depende da base.**
  - Na IA generativa, levar o assistente à empresa toda levou meses: na Petrobras, foram 500 funcionários em jul/2023 e 110 mil trabalhadores com acesso em dez/2023 [M1245, p. 2; M1240, p. 1].
  - A base de campo levou anos: a São Martinho começou a conectividade em 2015 e previa R$ 40 milhões até 2020 para ter 4G em todas as usinas [M1222, p. 27-28].
- **Os checkpoints (seção 4)** traduzem cada estágio em itens verificáveis por dimensão.
  - O estágio geral de uma empresa é o mais alto com evidência em pelo menos três das quatro dimensões.
  - Do estágio 3 em diante, só conta evidência de uso em produção ou em escala.
- **Política clara de uso é a virada da governança, mas sozinha não basta.** Proibir é contornado [M1044, p. 11]. Nem regras rígidas com ferramentas homologadas zeram o uso por fora percebido por executivos brasileiros [M1009, p. 2]. Para o Gartner, a política precisa virar regra aplicada por tecnologia [M1016, p. 2, 4]. Detalhes na seção 7.
- **Quem faz (seção 5):** patrocínio executivo, um comitê que prioriza e define a regra, um dono técnico na TI e pessoas de referência nas áreas.
- **Nas quatro sessões executivas com empresas do agro**, o que distingue quem está mais à frente é o canal oficial para todos com regras claras, o registro de quem usa e os facilitadores nas áreas. Nenhuma delas mede ainda o retorno de forma consolidada [S-01; S-02; S-03; S-04] (seção 9).
- **Agro e outros setores.** Bancos e mineração montaram a base de dados e a estrutura de IA anos antes da onda da IA generativa [M1238, p. 2; M1252, p. 2; M1251, p. 1]. O agro brasileiro saiu da última posição e chegou à média em maturidade digital, mas segue abaixo dela em IA [M1201, p. 11; M081, p. 12-13] (seção 10).

## 2. Como ler este roadmap

- **Referência de mercado, não receita.**
  - As fontes mostram o que as empresas fizeram e em que ordem.
  - O ritmo varia por setor e por área: corporativo, indústria e campo.
  - Nenhum estudo do catálogo compara caminhos com método; a sequência da seção 3 é leitura nossa a partir de casos e pesquisas.
- **A régua é a do estudo:**
  - cinco estágios: exploração, pilotos, operacionalização, escala e transformação;
  - quatro dimensões: estratégia e governança; dados e infraestrutura; organização e pessoas; aplicações e valor;
  - critérios cumulativos, isto é, só se sobe com o anterior cumprido [M194, p. 6; M189, p. 3].
- **Evidência, não autodeclaração.** Quem se avalia tende a se pôr mais acima. Numa pesquisa da Microsoft com a Ipsos (2023):
  - 34% puseram a própria organização nos dois estágios mais altos;
  - depois de responder ao questionário, foram 28%;
  - pelo modelo da pesquisa, 25% [M1203, p. 7].
- **O campo tem trilha própria**, tratada na Frente 3: conectividade, dados agronômicos, autonomia de máquinas e ciclos longos.

## 3. A trajetória observada: olhar para trás

### 3.1 A sequência que se repete

Fases recorrentes nas jornadas públicas (leitura nossa). As datas mostram quando cada empresa passou pela fase; não são obrigatórias nem simultâneas.

| Fase | O que as empresas fizeram | Casos com data |
|---|---|---|
| 1. Alicerce de dados e de campo | Fora do agro, dados e nuvem; no agro, conectividade no campo e um centro de operações que concentra os dados | **Fora do agro:**<br>• Itaú: migração para a nuvem desde 2017, com 65% dos aplicativos na nuvem em dez/2024 [M1238, p. 2]<br>• Vale: programa de transformação digital desde 2016 [M1252, p. 2]<br>**No agro:**<br>• São Martinho: conectividade no campo desde 2015 [M1222, p. 27]<br>• SLC: 4G em cinco unidades, cerca de 70 mil ha, em 2019 [M1220, p. 3]<br>• Klabin: torre de controle florestal desde 2021 [M1216, p. 2]<br>• BP Bunge: 98 torres 4G para 3 milhões de ha nas 11 unidades (2024) [M1223, p. 2]<br>• Atvos: rede 4G própria em oito usinas, com 375 mil ha cobertos (2025) [M1224, p. 1-2] |
| 2. Estrutura dedicada | Centro, área ou grupo responsável pela IA | • Vale: centro de IA aberto em 2019 [M1251, p. 1]<br>• Klabin: IA Office, grupo que avalia e direciona o uso de soluções de IA [M326, p. 63]<br>• Itaú: cerca de 500 cientistas de dados [M1239, p. 2] |
| 3. IA preditiva em dores medidas | Incêndio, insumos, manutenção e logística | • Vale: os projetos de IA já davam US$ 20 milhões de economia quando o centro foi criado [M1251, p. 1]<br>• SLC: R$ 82 milhões economizados com aplicação localizada de defensivos na safra 2022/23 [M332, p. 69]<br>• bp bioenergy: 50% menos incêndios e 77% menos área queimada entre 2019 e 2025 [M1217, p. 1]<br>• Atvos: R$ 5,8 milhões de economia na primeira fase do centro de inteligência agrícola [M1219, p. 2]<br>• Suzano: 85% dos incêndios controlados no início nos últimos três anos [M753, p. 3] |
| 4. IA generativa: da proibição ao assistente para todos (2023–2024) | Restrição depois dos primeiros vazamentos; depois, assistente corporativo para todos | **Proibição:**<br>• a Samsung proibiu o uso depois de um vazamento de código-fonte, e o JPMorgan Chase restringiu a ferramenta (2023) [M1013, p. 1-2]<br>• 27% das organizações chegaram a proibir a IA generativa ao menos por um tempo (Cisco, 2.600 profissionais de privacidade e segurança) [M1008, p. 22]<br>**Assistente para todos:**<br>• Petrobras: de 500 funcionários (jul/2023) a 110 mil trabalhadores com acesso (dez/2023) [M1245, p. 2; M1240, p. 1]<br>• Suzano: assistente corporativo para quase 50 mil colaboradores no 1º semestre de 2024 [M334, p. 6]<br>• Moderna: assistente próprio com mais de 80% de adoção interna e, em poucos meses, mais de 750 assistentes especializados [M1248, p. 1-2] |
| 5. Governança e democratização (2024–2026) | Política de uso com treinamento, triagem de demandas, várias ferramentas sob a mesma regra e criação pelos próprios usuários | • São Martinho: 99% do público elegível treinado na política de uso de IA [M357, p. 46]<br>• Klabin: em 2025, mais de 300 demandas de IA avaliadas e 18 selecionadas [M326, p. 65], com critérios para o colaborador criar agentes [M326, p. 63-65, 74]<br>• Vale: plataforma de dados e IA aberta a 19 áreas de negócio [M1247, p. 2]; transição, em 2025, de iniciativas pontuais para uma abordagem estruturada e escalável, com mais de 45 produtos de IA [M496, p. 32]<br>• Itaú: 150 soluções de IA generativa em produção e mais de 750 em desenvolvimento [M1239, p. 1]<br>• JPMorganChase: adesão voluntária, liberação em fases e treinamento [M025, p. 3-4] |
| 6. Agentes com cautela (2025 em diante) | Plataformas de agentes com limites de autonomia | • A Petrobras abriu uma plataforma de agentes apontando a falta de maturidade desses sistemas para ambientes de missão crítica [M1246, p. 2]<br>• O Gartner prevê que, até 2027, 40% das empresas vão rebaixar ou desativar agentes autônomos por falhas de governança [M1202, p. 1]<br>• Para o BCG, só 5% das empresas têm hoje os controles completos para dar autonomia a agentes [M1199, p. 10] |

### 3.2 O ritmo

| Etapa | Tempo observado | Casos |
|---|---|---|
| Conectividade de campo em escala | Anos | • São Martinho: início em 2015 e plano de 4G em todas as usinas até 2020 [M1222, p. 27-28]<br>• Atvos: 375 mil ha cobertos em 2025, com meta de 500 mil [M1224, p. 1-2] |
| Da estrutura de IA ao portfólio | Cerca de seis anos | Vale: centro de IA em 2019 [M1251, p. 1]; abordagem estruturada e escalável em 2025 [M496, p. 32] |
| Do piloto de IA generativa à empresa toda | Meses | • Petrobras: cerca de cinco meses [M1245, p. 2; M1240, p. 1]<br>• Suzano: do assistente do cozimento da celulose (jun/2023) ao assistente para todos (1º semestre de 2024) [M334, p. 4, 6] |
| Autonomia pesada | Cerca de três anos até uma mina 100% autônoma, mais dois para replicar | Vale:<br>• caminhões autônomos em teste em Brucutu desde 2016; os 13 caminhões da mina com a tecnologia em 2019 [M1242, p. 4]<br>• replicação em Carajás em 2021 [M1250, p. 1] |
| Nuvem num grande banco | Mais de uma década | Itaú: início em 2017, 65% dos aplicativos em dez/2024 e conclusão prevista para 2028 [M1238, p. 2] |

### 3.3 Atalhos e armadilhas

**Atalhos** (leitura nossa a partir dos casos):
- IA generativa sobre uma base de dados pronta;
- assistente para todos antes dos casos específicos;
- democratizar com regras claras;
- uma torre de controle como porta de entrada dos dados de campo.

**Armadilhas relatadas publicamente:**
- **O mais caro é obter os dados**, não aplicar a técnica de IA [M1241, p. 4].
- **A TI vira gargalo.** Na Vale, antes da plataforma aberta às áreas, todo pedido de informação dependia da TI e podia levar até três semanas [M1247, p. 3].
- **Rede de campo própria exige operação contínua.** A São Martinho vai trocar a rede privativa, implantada há oito anos, pela rede pública de uma operadora até a safra 2027/2028 [M1218, p. 1-2].
- **A demanda supera a capacidade:** na Klabin, mais de 300 demandas e 18 selecionadas [M326, p. 65].
- **Licença não é uso:** num ministério britânico, cerca de 30% dos licenciados usaram o assistente por dia útil [M1011, p. 16].
- **Agentes ainda imaturos para ambientes críticos** [M1246, p. 2].

### 3.4 O que a trajetória sugere

Leitura nossa, como referência de mercado:
- **O alicerce é a etapa mais longa e vem antes do valor.**
- **O valor aparece na passagem do piloto à produção.**
- **IA generativa para todos dá velocidade de adoção; o valor vem dos casos específicos e do redesenho do trabalho.** Na McKinsey, redesenhar fluxos de trabalho foi o atributo com maior efeito no EBIT da IA generativa (1.491 respondentes, jul/2024) [M029, p. 3].
- **Autonomia pesada é aposta de longo prazo.**

## 4. Os checkpoints: a régua com pré-requisitos

### 4.1 A regra

- **Estágios cumulativos:** cada estágio supõe os anteriores.
- **Do estágio 3 em diante, só evidência de uso em produção ou em escala**; anúncio, piloto e meta não bastam.
- **Estágio geral:** o mais alto com evidência em ao menos três das quatro dimensões.
- **O resultado principal é o perfil por dimensão e por área** (corporativo, indústria, campo). O nível máximo em tudo pode não ser pertinente [M194, p. 6].
- **Como usar:** cada linha das tabelas abaixo é um conjunto de checkpoints verificáveis. Na leitura de uma empresa de fora, vale a evidência pública típica. Numa autoavaliação, vale a resposta objetiva a cada item: sim, com evidência, ou não.

### 4.2 Checkpoints por dimensão

Critérios a partir da régua de classificação de 30/09, da seção 6.2 dos frameworks de maturidade e dos indicadores de uso fora dos canais oficiais (nota de shadow AI, seção 12) e de gestão do custo (nota de custo da IA). Leitura nossa, como proposta de trabalho.

**Estratégia e governança**

| Estágio | Precisa estar de pé | Evidência pública típica |
|---|---|---|
| 1. Exploração | Ponto de partida: sem patrocínio, regra ou instância de IA; uso individual e informal | IA ausente dos relatórios; iniciativas isoladas na imprensa |
| 2. Pilotos | • Patrocinador executivo nomeado<br>• Diretriz escrita que diz o que pode e que dado não entra nas ferramentas de IA<br>• Pilotos escolhidos pelo negócio, com dono e métrica | Alta liderança cita IA como prioridade; diretriz de uso de IA generativa ou de dados sensíveis |
| 3. Operacionalização | • Comitê ou área com mandato para decidir sobre IA<br>• Política corporativa de uso, com percentual de pessoas treinadas<br>• Canal oficial de IA para todos, com conta da empresa, proteção de dados no contrato e registro de uso<br>• Orçamento dedicado<br>• Riscos de IA tratados em privacidade e segurança | Comitê nomeado; política com percentual treinado; dado de uso com unidade e período |
| 4. Escala | • Governança de IA integrada à gestão de riscos e ao compliance, cobrindo TI e TO<br>• Catálogo de ferramentas aprovadas ou plataforma com vários modelos, sob a mesma governança<br>• Uso real (não licença), uso por fora e custo por área medidos<br>• Casos geridos como portfólio, com valor e risco | IA no relatório de riscos; alinhamento declarado a um referencial (NIST AI RMF, ISO/IEC 42001); usuários ativos com critério; total de casos divulgado |
| 5. Transformação | • Regras aplicadas por tecnologia e verificadas sempre<br>• Limites de ação proporcionais à autonomia dos agentes, com supervisão por exceção e auditoria das decisões automatizadas<br>• Ferramenta ou modelo novo entra por avaliação rápida, com prazo | Regras de supervisão por exceção descritas; rotina de auditoria e de avaliação divulgadas |

**Dados e infraestrutura**

| Estágio | Precisa estar de pé | Evidência pública típica |
|---|---|---|
| 1. Exploração | Ponto de partida: dados em planilhas e sistemas isolados | Nenhuma menção a plataforma de dados |
| 2. Pilotos | • Dados dos pilotos organizados, com responsável<br>• Painéis corporativos ou repositório inicial<br>• Ambiente de experimentação separado da produção | Painéis corporativos; sistema de gestão agrícola; primeiros sensores ou telemetria |
| 3. Operacionalização | • Plataforma de dados unificada nos domínios prioritários, com qualidade monitorada<br>• Papéis de governança de dados<br>• Ambiente de produção com operação de modelos<br>• Conectividade nas áreas prioritárias do campo | Data lake ou lakehouse com várias áreas; cobertura de conectividade divulgada |
| 4. Escala | • Dados tratados como produto, por domínio, com dono<br>• Dados de campo integrados quase em tempo real<br>• Plataforma corporativa de IA com custo gerido<br>• Conectividade ampla e processamento na borda; segurança entre TI e TO | Arquitetura por domínios; telemetria, imagens e sensores integrados; conectividade na maior parte da área |
| 5. Transformação | • Dados prontos para agentes: identidade, permissões e trilha de auditoria<br>• Troca de dados com a cadeia, sob contrato<br>• Operação contínua com baixa latência e redundância | Controle de identidade e auditoria para agentes; dados na base de novos serviços |

**Organização e pessoas**

| Estágio | Precisa estar de pé | Evidência pública típica |
|---|---|---|
| 1. Exploração | Ponto de partida: iniciativas dependem de entusiastas | Nenhuma área, cargo ou programa de dados e IA |
| 2. Pilotos | • Núcleo técnico, interno ou com parceiro, conduzindo os pilotos<br>• Letramento básico para quem usa<br>• Grupo de primeiros usuários que testa antes de liberar | Laboratório de inovação; parceria para pilotos |
| 3. Operacionalização | • Área de dados e IA com liderança nomeada<br>• Papéis definidos com o negócio (dono do caso e dono técnico)<br>• Programa de letramento com percentual atingido<br>• Facilitadores (champions) nomeados nas áreas | Diretoria ou gerência de dados e IA; programa de capacitação com número |
| 4. Escala | • Centro de excelência ou modelo federado, com times nas áreas<br>• Capacitação em escala, com trilhas por perfil e letramento como condição de acesso às ferramentas avançadas<br>• Metas de adoção pelo uso ativo, não pela licença<br>• Líder de IA dedicado | Centro de excelência; capacitação de parcela relevante da força de trabalho; metas de adoção |
| 5. Transformação | • Organização redesenhada em torno da IA<br>• Novos papéis: supervisão de agentes e operação remota de máquinas<br>• IA nas decisões de estrutura e de força de trabalho | Papéis de supervisão de agentes ou de operação remota |

**Aplicações e valor**

| Estágio | Precisa estar de pé | Evidência pública típica |
|---|---|---|
| 1. Exploração | Ponto de partida: usos pontuais, sem caso em produção | Menções genéricas a IA; desafios de inovação |
| 2. Pilotos | • Pilotos com escopo, métrica, dono e critério de parada<br>• Portfólio de pilotos registrado | Provas de conceito anunciadas com objetivo |
| 3. Operacionalização | • Ao menos um caso em produção, com resultado medido (unidade e período)<br>• Caminho definido do piloto à produção<br>• Valor medido depois da implantação | Caso em operação com ganho quantificado |
| 4. Escala | • Portfólio em produção em vários processos-chave e em mais de uma área<br>• Total de casos e resultados divulgados de forma recorrente<br>• Processos-chave redesenhados com IA<br>• Custo gerido por caso | Casos em operação agrícola, industrial, logística e corporativa; ganhos recorrentes |
| 5. Transformação | • Produtos ou serviços com IA<br>• Retorno consolidado divulgado<br>• Agentes ou máquinas operando com supervisão por exceção | Oferta baseada em IA; retorno consolidado |

**Bases dos critérios:**
- **Passagem do estágio 1:** sair da exploração pede um mínimo institucional (liderança, governança, roteiro e políticas, ainda que rudimentares) [M194, p. 35].
- **No estágio 1 do MIT CISR,** as empresas educam pessoas, definem políticas de uso e tornam os dados acessíveis [M189, p. 4].
- **Estágios 3 e 4:** sistemas em produção e mantidos [M159, p. 10]; governança e processos aprovados para toda a empresa [M194, p. 10].
- **Alta maturidade:** 91% das organizações de alta maturidade nomearam líderes dedicados de IA, e 63% fazem análise financeira de riscos e de retorno [M121, web].
- **Divulgação pelos bancos:** o total de casos é divulgado por 55% dos bancos latino-americanos, e nenhum dos 20 grandes bancos da região divulga retorno consolidado [M430, p. 23].

### 4.3 O que precisa existir antes de cada salto

**1 → 2 · De exploração a pilotos**
- **Precisa existir:**
  - patrocínio executivo;
  - problemas escolhidos pelo negócio, com métrica e dono;
  - acesso aos dados dos casos;
  - uma regra de uso que traga para dentro o uso informal.
- **Quando falta:** entre as causas-raiz de fracasso, a RAND aponta o problema mal entendido ou mal comunicado e o foco na tecnologia mais recente em vez do problema real [M195, p. 2].

**2 → 3 · De pilotos a operacionalização** (a travessia que mais separa desempenho)
- **Precisa existir:**
  - dados prontos para IA nos domínios dos casos;
  - engenharia para pôr e manter modelos em produção;
  - governança formal;
  - método para medir o valor antes e depois.
- **Quando falta:**
  - ao menos 30% dos projetos de IA generativa seriam abandonados depois da prova de conceito até o fim de 2025, segundo previsão do Gartner [M119, web];
  - 63% das organizações não têm, ou não sabem se têm, práticas de dados adequadas para IA (1.203 líderes de dados, jul/2024) [M124, web];
  - 49% apontam a dificuldade de estimar e demonstrar valor como principal barreira [M122, web];
  - o MIT CISR nomeia quatro desafios desta passagem: estratégia, sistemas, sincronização de pessoas e papéis, e uso responsável [M190, p. 3-4].

**3 → 4 · De operacionalização a escala**
- **Precisa existir:**
  - dados como produto e plataforma reaproveitada entre casos;
  - modelo operacional que escala, com liderança de IA dedicada;
  - capacitação em escala;
  - portfólio gerido por valor e custo sob controle.
- **O que as pesquisas mostram:**
  - entre as organizações que rastreiam o retorno e tratam a IA como portfólio, 81% das iniciativas têm retorno positivo [M123, web];
  - as líderes do BCG põem 70% dos recursos em pessoas e processos [M035, p. 6].

**4 → 5 · De escala a transformação**
- **Precisa existir:**
  - dados prontos para agentes: identidade, permissões e trilha de auditoria;
  - governança proporcional à autonomia;
  - processos redesenhados para pessoas e agentes trabalharem juntos.
- **Quando falta,** segundo previsões do Gartner:
  - mais de 40% dos projetos de IA agêntica serão cancelados até o fim de 2027 [M120, web];
  - até 2027, 40% das empresas vão rebaixar ou desativar agentes autônomos por falhas de governança [M1202, p. 1].

### 4.4 IA generativa e agentes em cada estágio

- **A IA generativa chegou a 70% de adoção em três anos** (MIT Sloan Management Review e BCG, 2.102 respondentes, primavera de 2025) [M192, p. 5, 7].
- **As medições de agentes divergem conforme a definição.**
  - Na McKinsey, 23% escalam um sistema agêntico em alguma área, e outros 39% experimentam [M027, p. 6].
  - Na Capgemini, a confiança em agentes totalmente autônomos caiu de 43% para 27% em 12 meses [M062, p. 4].

| Estágio | Como a IA generativa aparece | Papel de quem usa | Autonomia do agente |
|---|---|---|---|
| 1. Exploração | Uso individual de assistentes públicos | Operador | — |
| 2. Pilotos | Assistentes corporativos com grupos-piloto | Operador, colaborador | Observar, aconselhar |
| 3. Operacionalização | Assistente corporativo em produção sobre documentos da empresa | Colaborador | Aconselhar |
| 4. Escala | Copilotos nos fluxos-chave; agentes executam com aprovação | Consultor, aprovador | Agir com aprovação |
| 5. Transformação | Agentes operam processos com supervisão por exceção | Observador | Agir de forma autônoma |

**De onde vêm as escalas:**
- **Papéis de quem usa:** operador, colaborador, consultor, aprovador e observador [M1209, p. 1].
- **Níveis de autonomia dos agentes:** observar, aconselhar, agir com aprovação e agir de forma autônoma, este último com pessoas revendo exceções e trilhas de auditoria [M1202, p. 1-2].
- **A correspondência com os estágios** é leitura nossa.
- **Supervisão humana:**
  - acompanha a autonomia: de "no circuito", com intervenção em cada ciclo de decisão, a "sobre o circuito", com monitoramento [M1208, p. 18];
  - no AI Act europeu, as medidas de supervisão são proporcionais aos riscos, ao nível de autonomia e ao contexto de uso [M1212, p. 2];
  - o regulamento se aplica de forma geral a partir de 02/08/2026 [M1211, p. 1].

## 5. Quem faz o quê: papéis e responsabilidades

As empresas citam comitês, áreas e redes de usuários, mas quase nunca dizem quem compõe esses grupos, com que frequência se reúnem ou o que podem decidir (seção 13).

| Papel | O que faz | Exemplos e referências |
|---|---|---|
| Patrocínio executivo e conselho | Define a ambição, os limites de risco e o orçamento; cobra resultado | • Na McKinsey, a supervisão da governança de IA pelo CEO está entre os atributos mais ligados ao EBIT da IA generativa (1.491 respondentes, jul/2024) [M029, p. 3]<br>• No Commonwealth Bank, o conselho tem a responsabilidade final e fixa o apetite de risco de IA todo ano [M423, p. 13]<br>• O Bradesco tem política de riscos de IA aprovada pelo conselho [M456, p. 1]<br>• Na KPMG, 53% põem a responsabilidade por decisões apoiadas em IA na alta direção (2.131 líderes, 3º tri/2026) [M072, p. 13] |
| Líder de IA dedicado | Conduz estratégia, implementação e orçamento | • Na pesquisa da IBM, 26% das organizações contatadas tinham um Chief AI Officer, contra 11% em 2023 [M135, p. 8]<br>• Entre eles, 57% se reportam ao CEO ou ao conselho [M135, p. 14] e 61% controlam o orçamento de IA [M135, p. 10]<br>• No Gartner, 91% das organizações de alta maturidade nomearam líderes de IA dedicados [M121, web] |
| Comitê de IA | Avalia e direciona o uso, prioriza demandas, dá contraponto nos casos de maior risco e propõe mudanças na política | • Klabin: IA Office, equipe multidisciplinar, com a área de privacidade, que avalia riscos, segurança e ganhos das ferramentas de IA [M326, p. 63-64]<br>• Commonwealth Bank: comitê de risco de IA para os casos de maior risco e para mudanças na política [M423, p. 13]<br>• A Roland Berger recomenda um órgão de governança independente, com poder real de revisão [M031, p. 13] |
| Centro de excelência ou área central | Cuida de plataforma, padrões, reúso, segurança e apoio metodológico; o resultado fica com a área de negócio | • Deloitte: o centro de excelência como núcleo estratégico, capacidade técnica compartilhada e motor de captura de valor [M093, p. 1-2]<br>• Banco Neon: a área central cuida de infraestrutura, ferramentas e segurança, e o resultado de cada aplicação fica com a unidade de negócio [M018, p. 26] |
| TI e dono técnico | Arquiteta e guarda o ambiente: plataforma, acesso a dados, identidade, segurança, monitoramento e custo. Não é dona de toda solução | • ADL [M033, p. 4-5]<br>• Na Vale, depois de abrir a plataforma às áreas, a TI passou a responder pela segurança e pelos custos [M1247, p. 3] |
| RH e educação | Aprendizagem e letramento por perfil, redesenho de cargos e gestão da mudança | • Na IBM, 32% dos CAIOs veem o diretor de RH como um dos maiores opositores da IA [M135, p. 14]; a recomendação é RH e CAIO juntos nos programas [M135, p. 24]<br>• 93,2% dos líderes de dados e IA apontam cultura e gestão da mudança como o maior impedimento à adoção (cerca de 110 grandes empresas) [M116, p. 13] |
| Jurídico, privacidade, segurança e risco | Política, contratos, proteção de dados, segurança desde o desenho e incidentes | • NIST: funções de supervisão em todo o ciclo de vida [M223, p. 23]<br>• ANBIMA: estrutura formal de papéis e responsabilidades, com supervisão humana definida [M1000, p. 14]<br>• MAS (Singapura): modelo de três linhas e uma função de controle que identifica o uso de IA na instituição [M1114, p. 11, 13] |
| Champions e usuários avançados nas áreas | Tiram dúvidas, registram casos, levam demandas ao comitê e criam soluções nas áreas | • Uma empresa brasileira mantém uma comunidade de cerca de 500 "AI Champions", com formação própria [M018, p. 12]<br>• São Martinho: rede de Embaixadores da Inovação [M357, p. 43]<br>• No Tesouro australiano, 42 participantes foram campeões voluntários, mas o engajamento foi baixo e só o chat da comunidade ficou ativo [M1012, p. 13, 23] |
| Usuário | Usa conforme a política, revisa o que a IA produz e responde pelo resultado | Tesouro australiano: a pessoa deve conseguir explicar e assumir qualquer resultado feito com IA [M1012, p. 48] |

**Centralizar ou distribuir:**
- **McKinsey:** risco e conformidade (57% totalmente centralizado) e governança de dados para IA (46%) tendem a ficar num centro; talento técnico e adoção, em arranjos híbridos ou distribuídos (1.229 respondentes) [M029, p. 5].
- **IBM:** os modelos centralizados ou hub-and-spoke levam o dobro de pilotos à produção, com retorno 36% maior que o dos descentralizados (autodeclarado) [M135, p. 16]. A IBM desaconselha criar um "departamento de TI paralelo" só de IA [M135, p. 19].
- **Roland Berger:** 58% das pioneiras distribuem a capacidade de IA por todas as unidades, contra 14% das atrasadas (472 executivos) [M031, p. 14].
- **Leitura nossa:** o padrão é um centro pequeno, com plataforma, regra e segurança, e capacidade distribuída nas áreas, que respondem pelo resultado.

**O papel da TI** (leitura nossa a partir das fontes):
- **De barreira a habilitadora:** a TI provê plataforma, identidade, dados, segurança e controle de custo, e as áreas desenvolvem [M033, p. 4-5].
- **Nova cobrança:** o CIO passa a ser avaliado também por dar acesso fácil e seguro às ferramentas [M033, p. 5].
- **A ambição vem do negócio,** patrocinada pelo CEO [M033, p. 6].
- **Orçamento:** um orçamento dedicado, com responsabilidade pelo retorno, faz parte do mandato que a IBM recomenda dar ao líder de IA [M135, p. 20].

## 6. O fluxo de implementação

### 6.1 De uma ideia ao caso em produção

| Etapa | O que acontece | Referências |
|---|---|---|
| 1. Entrada | Demandas registradas de forma estruturada: de cima para baixo, em poucos domínios de maior valor, e de baixo para cima | • Deloitte: gestão da demanda e entrada priorizada de casos [M093, p. 2]<br>• JPMorgan: uma frente em poucos domínios de maior valor e outra de inovação federada, com ferramentas de autoatendimento [M025, p. 4] |
| 2. Triagem | Valor, dados, risco, custo e se a IA é mesmo necessária | • Klabin: em 2025, mais de 300 demandas avaliadas pelo potencial de valor e 18 selecionadas [M326, p. 65]<br>• Commonwealth Bank: pré-triagem na ideação para separar os casos que pedem supervisão reforçada [M423, p. 16]<br>• MAS: materialidade de risco por caso, com o risco residual dentro do apetite antes de implantar [M1114, p. 15]<br>• NIST: considerar alternativas que não usem IA [M222, p. 37]<br>• ADL: a IA cria uma nova base de custos, que precisa ser justificada pelos benefícios [M033, p. 6] |
| 3. Piloto | Escopo, métrica e prazo; grupo escolhido | • CNP Seguros: todo projeto de IA precisa de um business case com VPL de três anos [M018, p. 37]<br>• C&A Pay: cada prova de conceito precisa demonstrar retorno antes de escalar [M018, p. 35]<br>• DBT britânico: 70% das licenças para voluntários e 30% para uma amostra aleatória por diretoria e nível, para reduzir a autosseleção [M1011, p. 7] |
| 4. Decisão | Escalar, ajustar ou desligar | • NIST: decisão explícita sobre prosseguir [M222, p. 37] e critérios de desativação revistos regularmente [M223, p. 46]<br>• AWS (fornecedor): considerar o risco de custo afundado desde o início [M149, p. 31] |
| 5. Produção | Teste, revisão independente, aprovação e dono | Commonwealth Bank: teste, revisão por quem não desenvolveu e aprovação por pessoa autorizada [M423, p. 16] |
| 6. Acompanhamento | Monitoramento, revisão de adequação e inventário | • Commonwealth Bank: monitoramento periódico e nova revisão a cada mudança relevante [M423, p. 16]<br>• MAS: inventário de casos com finalidade, dados, estágio e materialidade [M1114, p. 14]<br>• Banco do Brasil: mais de 2,3 mil soluções de IA catalogadas, com avaliação de risco e rastreabilidade (1º semestre de 2026) [M417, p. 2] |

Nenhuma fonte pública traz pesos de priorização, duração ou meta de piloto, nem um critério de desligamento aplicado; as normas dizem só que é preciso defini-los.

### 6.2 De um pedido de ferramenta nova à liberação

| Etapa | O que acontece | Referências |
|---|---|---|
| 1. Pedido | Com o caso de uso, por um processo conhecido | MAS: a política básica traz a lista de ferramentas aprovadas e o processo para pedir novas [M1114, p. 9] |
| 2. Avaliação | Segurança, dados, contrato e termos de uso | • ANBIMA: avaliar o fornecedor e revisar o contrato ou os termos de uso, com as responsabilidades e os padrões de privacidade e proteção de dados [M1000, p. 16]<br>• NIST: diligência de compra que cubra propriedade intelectual, privacidade e segurança [M223, p. 25]<br>• Allianz Partners: questionário, análise de vulnerabilidade e testes; o que não passa é bloqueado [M018, p. 27]<br>• No governo britânico, o assistente herda as permissões de quem usa, e permissões erradas viram exposição [M1021, p. 4] |
| 3. Decisão e perfil de acesso | Por caso de uso claro e em fases | • Tesouro australiano: licenças a partir de casos de uso claros, em fases [M1012, p. 10]<br>• Allianz Partners: começar pelas aplicações de menor risco [M018, p. 28]<br>• Zurich: os modelos mais complexos ficam para quem passou pelo letramento, para controlar custo e risco [M018, p. 12] |
| 4. Letramento como condição | Treinamento antes da licença | Tesouro australiano: sessão de integração, auditoria de permissões e módulo obrigatório com prova, com nota mínima de 80% [M1012, p. 13] |
| 5. Liberação | Conta da empresa, registro de uso e adesão em fases | JPMorgan: avaliou riscos e controles antes; depois liberou a quem pedisse, em fases e com treinamento [M025, p. 4] |
| 6. Revisão de uso e custo | Painéis de uso e de custo; desligar o que não pegou | • KPMG: 61% revisam o custo de IA na aprovação e 59% em operação, mas só 12% avaliam de forma consistente o valor contra o custo [M072, p. 3]<br>• Microsoft (prática interna, fornecedor): avisar o dono e pôr em quarentena o que não é usado há tempo [M1034, p. 39] |

**Liberação em fases, um exemplo:** o Tesouro australiano liberou primeiro a TI (10 pessoas), depois o time do projeto (22) e o grupo de trabalho de IA (8), e só então os 218 participantes do teste [M1012, p. 13].

### 6.3 Criação fora da TI: agentes, automações e protótipos

- **Klabin:** critérios de valor, risco e complexidade definem quando a TI apoia e quando o colaborador pode criar agentes nos sistemas que já usa [M326, p. 65].
- **Suzano:** um programa coordena aprendizado e governança das tecnologias "democratizadas", com mentoria da área digital [M751, p. 3].
- **Microsoft** (prática interna, fornecedor): a criação por usuários de negócio é separada em três faixas de risco [M1034, p. 40], com ambiente de desenvolvimento separado e promoção à produção [M1034, p. 18].
- **NCSC britânico:** supervisão conforme o risco, com mais autonomia em protótipos sem dados sensíveis e revisão onde há autenticação e dados pessoais [M1047, p. 2].
- **OWASP:**
  - soluções criadas fora da TI ficam órfãs, sem dono, monitoramento ou nível de serviço; o OWASP recomenda dono e ciclo de vida obrigatórios [M1051, p. 31-32];
  - credenciais pessoais embutidas fazem qualquer usuário agir com a identidade de quem criou [M1051, p. 9].

## 7. Política de uso clara

### 7.1 O que ela contém

Nenhuma empresa publica o texto integral da sua política. Os itens abaixo reúnem o que pedem os referenciais e o que as empresas descrevem.

| Item | O que diz | Referências |
|---|---|---|
| 1. Alcance e responsável | Quem, que ferramentas e que dados; um responsável na alta gestão | MAS: a política básica tem um responsável na alta gestão [M1114, p. 9] |
| 2. Ferramentas aprovadas | A lista e como pedir outra | • MAS [M1114, p. 9]<br>• NIST: lista de tecnologias e fornecedores aprovados [M223, p. 25] |
| 3. Classes de dados | O que nunca entra em ferramenta pública | MAS: informação confidencial, proprietária ou de clientes [M1114, p. 9] |
| 4. Uso por fora | Se ferramentas paralelas são admitidas e como | • ANBIMA: dizer se é permitido usar sistemas de IA paralelos e, se for, como [M1000, p. 16]<br>• NIST: estender a política a tecnologias abertas e de terceiros [M223, p. 25] |
| 5. Revisão humana e responsabilidade | Toda saída é revisada; quem usa responde | • DBT: alucinações ocorrem, e cada saída deve passar por revisão [M1011, p. 39]<br>• Tesouro australiano [M1012, p. 48]<br>• MAS: revisão humana obrigatória quando cabível [M1114, p. 9] |
| 6. Transparência | Quando e como declarar o uso de IA | • Tesouro australiano: faltou orientação sobre quando e como declarar o uso [M1012, p. 28]<br>• DBT: a exigência de aviso existia, mas quase ninguém a aplicou [M1011, p. 34]<br>• Bradesco: identificação clara de conteúdos gerados por IA [M456, p. 3] |
| 7. Usos proibidos | Listados | • Bradesco: usos de risco inaceitável, como manipulação, pontuação social e vigilância biométrica não autorizada [M456, p. 4]<br>• NIST: tratar usos ilegais [M223, p. 19] |
| 8. Agentes, conectores e automações | O que cada agente pode fazer, a que dados tem acesso e quando exige aprovação | • McKinsey [M039, p. 9]<br>• MAS: inventário de agentes com identificador, acessos e limites [M1114, p. 15]<br>• Banco do Brasil: diretrizes com níveis de autonomia e governança de agentes [M417, p. 1] |
| 9. Criação fora da TI | Ambiente isolado, revisão antes de publicar e dono | Seção 6.3 |
| 10. Letramento obrigatório | Treinamento na política, com percentual | • São Martinho: 99% do público elegível treinado na política de uso de IA [M357, p. 46]<br>• ANBIMA: treinar e manter um canal de dúvidas [M1000, p. 16] |
| 11. Registro e incidentes | Registro de uso, incidentes com responsável e causa, canal de relato | • Commonwealth Bank: registro de entradas e saídas na IA generativa; incidentes com responsável e análise de causa [M423, p. 12, 16]<br>• Bradesco [M456, p. 4]<br>• NIST: campos mínimos do registro de incidentes [M223, p. 23]<br>• MAS: quem usa é treinado para relatar comportamento inesperado [M1114, p. 28] |
| 12. Revisão periódica | Documento vivo, com dono e frequência | • ANBIMA [M1000, p. 17]<br>• NIST: frequência de revisão definida [M223, p. 20] |

Consequências e sanções não aparecem em nenhuma fonte pública do catálogo (seção 13).

### 7.2 O que faz a política funcionar, e o que não basta

- **Conhecer a política.** No DBT, o conhecimento das políticas era desigual e havia confusão entre as duas ferramentas disponíveis; quem tinha dúvida ficava cauteloso [M1011, p. 34].
- **Proibir aumenta o risco.** No estudo KPMG e Universidade de Melbourne (48.340 pessoas em 47 países):
  - cerca de 48% dos empregados que usam IA já puseram informação sensível da empresa em ferramentas públicas, mais onde a IA generativa foi proibida;
  - 56% usaram IA no trabalho sem saber se era permitido [M110, p. 77].
- **Equilíbrio.** Controles rígidos demais criam gargalos e estimulam usos informais, e regras só declaratórias não chegam ao cotidiano [M018, p. 29].
- **Regra aplicada por tecnologia.**
  - Para o Gartner (analista que vende o próprio método), política e treinamento declaram a intenção, mas não garantem o comportamento; é preciso inventário, monitoramento e regras aplicadas por tecnologia [M1016, p. 2, 4].
  - A ANBIMA também pede ferramentas que impeçam o uso de sistemas não autorizados [M1000, p. 16].
  - Na KPMG, 55% já operam uma camada formal de controle de IA, contra 86% entre as que relatam retorno [M072, p. 12].
- **Canal oficial bom.**
  - A Alelo desenvolveu plataforma própria para reduzir o shadow AI [M018, p. 35].
  - A Allianz Partners bloqueia as ferramentas não homologadas e monitora as autorizadas [M018, p. 27].
  - Para os demais caminhos e controles, ver a nota de shadow AI, seções 7 e 8.

## 8. Rituais e métricas de adoção

### 8.1 Rituais

- **Comunidade e apoio técnico.** No Tesouro australiano:
  - o chat da comunidade foi o único mecanismo de apoio ativo de forma consistente [M1012, p. 23];
  - a avaliação concluiu que fóruns e campeões voluntários não deram o suporte técnico necessário, e recomendou treinamento estruturado, duplas de apoio e comunidades de prática [M1012, p. 48].
- **Formação contínua.**
  - Lojas Marisa: encontros semanais de uma hora e meia e trilhas para os profissionais dos processos atendidos [M018, p. 29-30].
  - Commonwealth Bank: série de aprendizagem com atividades quinzenais [M423, p. 18].
  - JPMorgan: as equipes criaram bibliotecas de prompts [M025, p. 7].
- **Vitrine e exemplo.**
  - São Martinho: Semana de Tecnologia Agroindustrial, na 19ª edição em 2025, com capacitação e vitrine [M357, p. 43].
  - Microsoft (fornecedor): recomenda que os líderes mostrem como usam IA e compartilhem acertos e erros [M166, p. 11].
- **Comunicar o valor.** Na Oliver Wyman, funcionários de empresas líderes em IA têm 10 vezes mais chance de dizer que a empresa deu uma visão clara da estratégia de IA (41% contra 4%) [M030, p. 18].
- **Gerência intermediária:** é ela que transforma prioridade em rotina e define quem age diante de um erro [M018, p. 26].
- **Custo na rotina.** Entre as organizações com retorno estabelecido, na KPMG:
  - 77% têm painéis de custo de IA;
  - 73% revisam o custo na aprovação;
  - 46% usam orçamentos de uso ou de tokens [M072, p. 22].

### 8.2 Métricas

| Métrica | Como se mede | Referências |
|---|---|---|
| Uso ativo, não licença | "Ativo" é quem interagiu ao menos uma vez nos 30 dias anteriores; a taxa é ativos ÷ licenças | • Governo britânico: 83% no pico e cerca de 80% até o fim, com 20 mil servidores de 12 órgãos [M1021, p. 7]; por aplicativo, 71% no Teams e 23% no Excel [M1021, p. 8]<br>• DBT: 21% de usuários ativos diários (30% sem fins de semana) e 64% semanais [M1011, p. 16] |
| Tempo poupado | Autodeclarado, com ajustes | • Governo britânico: média de 26 minutos por dia, autodeclarada [M1021, p. 11]<br>• O DBT descontou saídas não usadas e tarefas novas criadas pela ferramenta [M1011, p. 10] e não achou evidência de ganho de produtividade [M1011, p. 5]<br>• O JPMorgan não tenta quantificar as horas do uso cotidiano e busca o valor em poucos domínios estratégicos [M025, p. 4] |
| Ponto de equilíbrio da licença | Minutos por semana que pagam a licença | Tesouro australiano: cerca de 13 minutos por semana para um servidor de nível médio [M1012, p. 33] |
| Custo contra valor | Custo na aprovação, em operação e contra o valor gerado | KPMG: só 12% avaliam de forma consistente o valor contra o custo [M072, p. 3] |
| Letramento | Percentual treinado; inscrição não é conclusão | • São Martinho: 99% [M357, p. 46]<br>• Banco do Brasil: mais de 36 mil inscritos nas trilhas de IA em 2026 [M417, p. 3] |
| Casos e valor | Indicadores do próprio negócio, comparados com a linha de base | • Porto Bank: NPS, tempo de resolução e produtividade por hora, contra a linha de base anterior à automação [M018, p. 18]<br>• McKinsey: acompanhar indicadores bem definidos é a prática mais ligada ao resultado, mas menos de uma em cada cinco empresas o faz [M029, p. 9-10]<br>• Roland Berger: 15% têm indicadores claros de adoção [M031, p. 18] |
| Uso por fora | Só aparece em pesquisa, nunca medido dentro de uma empresa | KPMG e Universidade de Melbourne: 70% dos empregados acessam IA no trabalho por ferramentas públicas gratuitas [M110, p. 73] |

### 8.3 A conta de um caso

Método simples, com exemplo nosso e sem metas.
1. Tempo que a tarefa leva hoje, menos o tempo com IA.
2. Vezes que a tarefa se repete × pessoas que a fazem.
3. Conta do ano, comparada com a capacidade do time.
4. O que não entra na conta: erro, retrabalho e dependência de uma pessoa.
5. Do outro lado, licença e consumo.

**Exemplo (cálculo nosso):** um relatório que leva 6 horas e passa a levar 2 poupa 4 horas. Feito toda semana por duas pessoas, são 8 horas por semana, cerca de 400 horas por ano. O ponto de equilíbrio do Tesouro australiano faz a mesma conta pelo lado do custo [M1012, p. 33].

## 9. O que as quatro sessões executivas mostram

Leitura agregada das quatro sessões com lideranças de empresas do agro e da bioenergia, sem identificar entrevistado nem empresa e sem misturar o relato com documentos públicos de quem participou.

- **A IA generativa chegou antes da regra.** Em uma sessão, a ferramenta interna teve pouco uso até a empresa liberar para todos um assistente integrado ao pacote de escritório, com menos fricção [S-02]. Em outra, o canal oficial segue travado, e iniciativas são feitas por fora e só depois trazidas para dentro [S-01].
- **Canal oficial com regras claras.**
  - Duas usam vias homologadas, com licença especial por perfil ou por solicitação aprovada [S-02; S-03].
  - Uma abre exceção para quem demonstra valor [S-03].
  - Uma registra todo acesso a IA no ambiente interno [S-04].
- **Pessoas.**
  - Há facilitadores por área previstos ou recentes [S-03; S-04] e encontros abertos de usuários avançados [S-02].
  - O letramento vem antes da ferramenta: primeiro o básico para todos, depois as trilhas por área [S-03]. Em outra sessão, a prioridade é o letramento, e não o treinamento técnico [S-01].
- **Comitê e TI.**
  - Uma tem comitê multidisciplinar, com tecnologia, letramento e cibersegurança [S-04].
  - Em outra, o comitê horizontal é recente e ainda não funciona como deveria, e a TI ligada à agricultura vê pouco do potencial da IA [S-01].
- **Valor.** Nenhuma mede o retorno de forma consolidada; os ganhos citados são de tempo e de qualidade, medidos por caso [S-01; S-02; S-03]. Uma aponta o próximo ano como o de medir o retorno, ampliar o acesso e educar [S-04].
- **Na régua (leitura nossa, a partir dos relatos):** as quatro estão entre os estágios 2 e 3, na passagem entre as fases 4 e 5 da trajetória. O checkpoint que separa as mais adiantadas é o canal oficial para todos, com política, registro de uso e facilitadores. O seguinte é medir o valor.

**Falas dos entrevistados:**
> "A IA já está dentro da empresa. Não tem como segurar." [S-01]

> "Tem recurso em abundância, e por isso tem gente que nem sabe que tem." [S-02]

> "Tudo tem um jeitinho: se mostrar valor, é possível." [S-03]

> "Toda pessoa que acessa uma IA dentro da companhia tem um registro: sabe-se exatamente quem fez." [S-04]

## 10. O agro e os outros setores

**Onde o agro está nas medições:**
- **ITDBr:**
  - em 2024, o agronegócio tinha o menor índice de maturidade digital entre as indústrias avaliadas (3,1, contra 3,7 da média), e pessoas e cultura teve a avaliação mais baixa de todo o estudo (2,7) [M1201, p. 11];
  - em 2025, o agro chegou a 3,6, igual à média, mas a dimensão de IA ficou em 3,4, contra 3,7 [M081, p. 12-13];
  - em IA, serviços financeiros marcam 4,8 e energia, 4,2 [M082, p. 20].
- **Cetic.br:** 17% das empresas brasileiras com 10 ou mais pessoas usam IA; entre as grandes, 50% (4.174 empresas, 2025) [M1205, p. 1].
- **IBGE:** na indústria com 100 ou mais pessoas, o uso de IA foi de 16,9% em 2022 para 41,9% em 2024 [M186, p. 32].
- **Gatua:** numa pesquisa com 84 respondentes do agro (mar–mai/2026), 78% têm IA na agenda de 2026, mas, nos painéis do mesmo evento, o setor foi descrito como "ainda numa fase de validação" [M748, p. 32, 53].

**Distância no tempo** (leitura nossa):
- **Base de dados:** os setores de referência montaram dados e estrutura de IA anos antes da IA generativa. O Itaú está na nuvem desde 2017 [M1238, p. 2], e a Vale tem programa digital desde 2016 e centro de IA desde 2019 [M1252, p. 2; M1251, p. 1].
- **Agro no mesmo período:** os líderes do agro começaram pela conectividade e pelos centros de operação [M1222, p. 27; M1220, p. 3; M1216, p. 2].
- **IA generativa:** a onda chegou a todos ao mesmo tempo, em 2023–2024 [M1245, p. 2; M334, p. 6].
- **Onde está a distância:** é menor no assistente para todos e maior na base de dados integrada, na governança publicada e na medição do valor.
- **Por que os bancos governam mais:** regulação e risco de modelo; ver a nota sobre Itaú, Bradesco e Nubank.

## 11. O campo fica na Frente 3

A trilha do campo tem ritmo próprio e vai para a Frente 3: conectividade, dados agronômicos, processamento na borda, níveis de autonomia de máquinas, normas de segurança e culturas perenes de baixa mecanização. A base já está no catálogo (rodada 10, grupo de campo e sistemas autônomos) e na seção 7 dos frameworks de maturidade.

## 12. Números que não devem ser usados (ou só com ressalva)

- **"A cada 100 testes, cinco viraram projetos que trazem retorno":** fala de painelista em evento, não é medição [M748, p. 53]. O ebook tem distribuição restrita: citar com atribuição, sem reproduzir.
- **"95% das iniciativas sem retorno" (MIT NANDA, 2025):**
  - os achados são preliminares e a amostra é pequena;
  - a taxa real "poderia ser três vezes maior ou três vezes menor";
  - 80% das empresas pesquisadas nunca tinham pilotado ferramenta sob medida [M1204, p. 2, 4].
- **Autodeclaração de estágio e de agenda** (por exemplo, "78% com IA na agenda"): usar só com a ressalva de que é autodeclaração [M748, p. 32; M1203, p. 7].
- **Previsões de analistas** (abandono de projetos, cancelamento de projetos agênticos, rebaixamento de agentes): são previsões, não medições [M119, web; M120, web; M1202, p. 1].
- **Fontes da rodada 10 sem cópia guardada** (relatórios anuais de 2023 e 2024 do Itaú, 20-F de 2020 da Petrobras, nota de cinco anos do centro de inteligência agrícola da SLC, comunicados do Gartner de 2019 e de abr/2026): os números delas não entram até serem salvos e conferidos [M1243; M1244; M1249; M1221; M1207; M1206].

## 13. Lacunas

- **Comparação de caminhos:** nenhum estudo do catálogo compara caminhos de adoção com método; a sequência é leitura nossa.
- **Agro:** não há distribuição de maturidade em IA por estágio para agro, bioenergia ou florestal com dados públicos.
- **Políticas de uso:** as políticas completas das empresas raramente são públicas; o que aparece são princípios, percentuais de treinamento e descrições de comitê.
- **Fontes da rodada 10 sem cópia:** os relatórios do Itaú (linha do tempo de dados e IA), o 20-F da Petrobras (diretoria digital de 2019 e centro de excelência de 2020) e a nota da SLC precisam ser salvos à mão no navegador.

## Fontes
<!-- fontes:inicio -->
- **M018** — MIT Technology Review Brasil, TEC.Institute e Peers Consulting + Technology (2026). Gerando valor com GenAI — Do piloto ao resultado: a rentabilidade da IA (2ª edição). [link](https://mittechreview.com.br/) · citado em p. 12, 18, 26, 27, 28, 29, 29-30, 35, 37
- **M025** — McKinsey & Company (Financial Services Practice) (2025). JPMorgan Chase's Derek Waldron on building an AI-first bank culture (entrevista, 29/10/2025). [link](https://www.mckinsey.com/industries/financial-services/our-insights/jpmorgan-chases-derek-waldron-on-building-an-ai-first-bank-culture) · citado em p. 3-4, 4, 7
- **M027** — McKinsey & Company (QuantumBlack) (2025). The state of AI in 2025: Agents, innovation, and transformation. [link](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/november%202025/the-state-of-ai-2025-agents-innovation_cmyk-v1.pdf) · citado em p. 6
- **M029** — McKinsey & Company (QuantumBlack) (2025). The state of AI: How organizations are rewiring to capture value. [link](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value) · citado em p. 3, 5, 9-10
- **M030** — Oliver Wyman Forum (2025). How AI Leaders Are Taking Flight: A field guide to their practices, strategies, and cultures. [link](https://www.oliverwymanforum.com/artificial-intelligence/four-secrets-to-how-ai-leaders-are-gaining-an-edge.html) · citado em p. 18
- **M031** — Roland Berger (2026). The AI-First Organization: Turning AI power into enterprise performance (estudo completo). [link](https://www.rolandberger.com/en/Insights/Publications/The-AI-First-Organization.html) · citado em p. 13, 14, 18
- **M033** — Arthur D. Little (2026). The AI First Organization: How IT can help reshape the operating model for AI. [link](https://www.adlittle.com/en/insights/viewpoints/ai-first-organization) · citado em p. 4-5, 5, 6
- **M035** — Boston Consulting Group (BCG) (2024). Where's the Value in AI?. [link](https://www.bcg.com/publications/2024/wheres-value-in-ai) · citado em p. 6
- **M039** — McKinsey & Company (2026). Building the foundations for agentic AI at scale. [link](https://www.mckinsey.com/~/media/mckinsey/business%20functions/technology/our%20insights/building%20the%20foundations%20for%20agentic%20ai%20at%20scale/building-the-foundations-for-agentic-ai-at-scale_vf.pdf) · citado em p. 9
- **M062** — Capgemini Research Institute (2025). Rise of agentic AI: How trust is the key to human-AI collaboration. [link](https://www.capgemini.com/insights/research-library/ai-agents/) · citado em p. 4
- **M072** — KPMG International (2026). Global AI Pulse Q3 2026 — AI at scale: Accountability, resilience and economics. [link](https://kpmg.com/xx/en/our-insights/ai-and-technology/ai-pulse.html) · citado em p. 3, 12, 13, 22
- **M081** — PwC Brasil e Fundação Dom Cabral (FDC) (2026). Índice de Transformação Digital Brasil (ITDBr) 2025 — Destaques do Agronegócio. [link](https://www.pwc.com.br/pt/estudos/servicos/consultoria-negocios/indice-transformacao-digital-brasil-2025/destaques-do-agronegocio.html) · citado em p. 12-13
- **M082** — PwC Brasil e Fundação Dom Cabral (FDC) (2025). Índice de Transformação Digital Brasil (ITDBr) 2025 — estudo completo. [link](https://www.pwc.com.br/pt/estudos/servicos/consultoria-negocios/indice-transformacao-digital-brasil-2025.html) · citado em p. 20
- **M093** — Deloitte África (2025). The rise of the AI operating model: Why every business needs an AI Centre of Excellence today. [link](https://www.deloitte.com/content/dam/assets-zone1/za/en/docs/services/consulting/2025/za-the-rise-of-the-ai-operating-model-full-report.pdf) · citado em p. 1-2, 2
- **M110** — University of Melbourne e KPMG International (2025). Trust, attitudes and use of artificial intelligence: A global study 2025. [link](https://kpmg.com/xx/en/our-insights/ai-and-technology/trust-attitudes-and-use-of-ai.html) · citado em p. 73, 77
- **M116** — Data & AI Leadership Exchange (Randy Bean; prefácio de Thomas H. Davenport) (2026). 2026 AI & Data Leadership Executive Benchmark Survey — Executive Summary of Findings. [link](https://static1.squarespace.com/static/62adf3ca029a6808a6c5be30/t/6942c3cb535da44088c2dbff/1765983179572/2026+AI+&+Data+Leadership+Executive+Benchmark+Survey+Final.pdf) · citado em p. 13
- **M119** — Gartner (2024). Gartner Predicts 30% of Generative AI Projects Will Be Abandoned After Proof of Concept By End of 2025. [link](https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025) · citado em web
- **M120** — Gartner (2025). Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027. [link](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) · citado em web
- **M121** — Gartner (2025). Gartner Survey Finds 45% of Organizations With High AI Maturity Keep AI Projects Operational for at Least Three Years. [link](https://www.gartner.com/en/newsroom/press-releases/2025-06-30-gartner-survey-finds-forty-five-percent-of-organizations-with-high-artificial-intelligence-maturity-keep-artificial-intelligence-projects-operational-for-at-least-three-years) · citado em web
- **M122** — Gartner (2024). Gartner Survey Finds Generative AI Is Now the Most Frequently Deployed AI Solution in Organizations. [link](https://www.gartner.com/en/newsroom/press-releases/2024-05-07-gartner-survey-finds-generative-ai-is-now-the-most-frequently-deployed-ai-solution-in-organizations) · citado em web
- **M123** — Gartner (2026). Gartner Survey Finds Only 22% of Organizations Have Successfully Scaled AI Across Multiple Business Units. [link](https://www.gartner.com/en/newsroom/press-releases/gartner-survey-finds-only-22-percent-of-organizations-have-successfully-scaled-ai-across-multiple-business-units) · citado em web
- **M124** — Gartner (2025). Lack of AI-Ready Data Puts AI Projects at Risk. [link](https://www.gartner.com/en/newsroom/press-releases/2025-02-26-lack-of-ai-ready-data-puts-ai-projects-at-risk) · citado em web
- **M135** — IBM Institute for Business Value / Oxford Economics / Dubai Future Foundation (2025). Solving the AI ROI puzzle: How Chief AI Officers cut through complexity to create new paths to value. [link](https://www.ibm.com/downloads/documents/us-en/1379d32d7fdaec18) · citado em p. 8, 10, 14, 16, 19, 20, 24
- **M149** — AWS (2024). AWS Cloud Adoption Framework for Artificial Intelligence, Machine Learning, and Generative AI (CAF-AI). [link](https://docs.aws.amazon.com/pdfs/whitepapers/latest/aws-caf-for-ai/aws-caf-for-ai.pdf) · citado em p. 31
- **M159** — Google Cloud (2020). Google Cloud's AI Adoption Framework. [link](https://services.google.com/fh/files/misc/ai_adoption_framework_whitepaper.pdf) · citado em p. 10
- **M166** — Microsoft (2026). Becoming a Frontier Firm: A How-To Guide for Transforming with AI and Agents. [link](https://adoption.microsoft.com/files/copilot/FrontierFirmPlaybook.pdf) · citado em p. 11
- **M186** — IBGE (com ABDI e UFRJ) (2025). Pesquisa de Inovação Semestral 2024 - Indicadores temáticos: Tecnologias digitais avançadas, teletrabalho e cibersegurança. [link](https://agenciadenoticias.ibge.gov.br/media/com_mediaibge/arquivos/58ab6f34051f3fa2b73b75cc6e926067.pdf) · citado em p. 32
- **M189** — MIT CISR (Weill, Woerner, Sebastian) (2024). Building Enterprise AI Maturity (Research Briefing XXIV-12). [link](https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian) · citado em p. 3, 4
- **M190** — MIT CISR (Woerner, Sebastian, Weill, Káganer) (2025). Grow Enterprise AI Maturity for Bottom-Line Impact (Research Briefing XXV-8). [link](https://cisr.mit.edu/publication/2025_0801_EnterpriseAIMaturityUpdate_WoernerSebastianWeillKaganer) · citado em p. 3-4, 9
- **M192** — MIT Sloan Management Review + BCG (2025). The Emerging Agentic Enterprise: How Leaders Must Navigate a New Age of AI. [link](https://web-assets.bcg.com/dc/c5/1bcbfdc0405c85fb14972a57c20a/the-emerging-agentic-enterprise-how-leaders-must-navigate-a-new-age-of-ai.pdf) · citado em p. 5, 7
- **M194** — MITRE Corporation (2023). The MITRE AI Maturity Model and Organizational Assessment Tool Guide: A Path to Successful AI Adoption. [link](https://www.mitre.org/sites/default/files/2023-11/PR-22-1879-MITRE-AI-Maturity-Model-and-Organizational-Assessment-Tool-Guide.pdf) · citado em p. 6, 10, 35
- **M195** — RAND Corporation (2024). The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed: Avoiding the Anti-Patterns of AI. [link](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2600/RRA2680-1/RAND_RRA2680-1.pdf) · citado em p. 2
- **M222** — NIST (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0) - NIST AI 100-1. [link](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) · citado em p. 37
- **M223** — NIST (National Institute of Standards and Technology, EUA) (2024). Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1). [link](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) · citado em p. 19, 20, 23, 25, 46
- **M326** — Klabin (2026 (ref. 2025)). Relatório de Sustentabilidade 2025. [link](https://rs2025.klabin.com.br/documents/2996966/4590388/RS+2025+A4+-+Klabin+-+v2_compressed.pdf/980d0243-ee3c-1e4d-7394-f29527a186e9?t=1788271818905) · citado em p. 63, 63-64, 63-65, 65, 74
- **M332** — SLC Agrícola (2024 (ref. 2023)). Relatório Integrado 2023. [link](https://blobslcagricola.blob.core.windows.net/media/document/23.pdf) · citado em p. 69
- **M334** — Suzano (2025). Microsoft e Suzano desenvolvem solução para impulsionar eficiência industrial com IA generativa (notícia, 23/04/2025). [link](https://www.suzano.com.br/noticia/microsoft-e-suzano-desenvolvem-ia-generativa) · citado em p. 4, 6
- **M357** — São Martinho (2026 (safra 2025/26)). Relato Integrado 2025/2026. [link](https://www.saomartinho.com.br/Download.aspx?Arquivo=8rGueYhS+9fDqXheg2ZTaQ==&IdCanal=E/5CI5hbGiTfjZ7mhu2y5w==) · citado em p. 43, 46
- **M417** — Banco do Brasil (2026). BB é pioneiro global em diretrizes para IA generativa e agêntica (release, 24/08/2026). [link](https://imprensa.bb.com.br/bb-e-pioneiro-global-em-diretrizes-para-ia-generativa-e-agentica/) · citado em p. 1, 2, 3
- **M423** — Commonwealth Bank of Australia (CommBank) (2025). Our Approach to Adopting AI (December 2025). [link](https://www.commbank.com.au/content/dam/commbank-assets/about-us/docs/our-approach-to-adopting-ai-december-2025.pdf) · citado em p. 12, 13, 16, 18
- **M430** — Evident Insights (2026). Evident AI Index | Banks – LATAM: Key Findings Report (July 2026). [link](https://evidentinsights.com/insights/banking-ai-index-latam-2026-report) · citado em p. 23
- **M456** — Banco Bradesco (2026). Trusted AI – Compromisso do Bradesco com a IA confiável (versão de 2026). [link](https://assets.bradesco/content/dam/portal-bradesco/assets/classic/pdf/sustentabilidade/trusted-ai.pdf) · citado em p. 1, 3, 4
- **M496** — Vale (2026). Relatório de Pesquisa, Desenvolvimento & Inovação 2025. [link](https://vale.com/documents/d/guest/relatorio_pdi_2025) · citado em p. 32
- **M748** — Gatua (2026). TI do Futuro — Do Centro de Custo ao Pilar Estratégico (ebook do Gatua Meeting E01, com a pesquisa pré-evento de 84 respondentes). · citado em p. 32, 53
- **M751** — Suzano (2025). Programa de empoderamento tecnológico da Suzano, criado em parceria com a Koru, resulta em inovação e otimização de recursos. [link](https://www.suzano.com.br/noticia/curso-habilidades-digitais-suzano-koru) · citado em p. 3
- **M753** — Suzano (2026). Suzano investe em inovação tecnológica para prevenir e combater incêndios florestais. [link](https://www.suzano.com.br/noticia/inovacao-tecnologica-para-prevenir-incendios-florestais) · citado em p. 3
- **M1000** — ANBIMA (Associação Brasileira das Entidades dos Mercados Financeiro e de Capitais) – Rede ANBIMA de Inovação (2024 (atualização de jul/2024)). Guia orientativo – Boas práticas para o uso de sistemas de inteligência artificial nos mercados financeiro e de capitais (atualização de jul/2024). [link](https://www.anbima.com.br/data/files/63/74/15/39/F12C091039E04909EA2BA2A8/Guia_orientativo_boas_praticas_para_o_uso_de_sistemas_de_inteligencia_artificial.pdf) · citado em p. 14, 16, 17
- **M1008** — Cisco (2024 (25/01/2024)). Cisco 2024 Data Privacy Benchmark Study. [link](https://www.cisco.com/c/dam/en_us/about/doing_business/trust-center/docs/cisco-privacy-benchmark-study-2024.pdf) · citado em p. 22
- **M1009** — Convergência Digital (cobrindo estudo da Peers Consulting + Technology e do TEC.Institute publicado pela MIT Technology Review Brasil) (2026 (24/09/2026)). Executivos brasileiros admitem uso não autorizado de IA generativa na rotina do trabalho. [link](https://convergenciadigital.com.br/carreira/executivos-brasileiros-admitem-uso-nao-autorizado-de-ia-generativa-na-rotina-do-trabalho/) · citado em p. 2
- **M1011** — Department for Business and Trade (DBT), Governo do Reino Unido (2025 (ago/2025)). The Evaluation of the M365 Copilot Pilot in the Department for Business and Trade (relatório de avaliação, ago/2025). [link](https://assets.publishing.service.gov.uk/media/68adbe409e1cebdd2c96a19d/dbt-microsoft-365-copilot-evaluation.pdf) · citado em p. 5, 7, 10, 16, 34, 39
- **M1012** — Department of the Treasury (Austrália) – Australian Centre for Evaluation (ACE) (2025 (fev/2025)). Evaluation of a trial of generative artificial intelligence (Copilot) in The Department of the Treasury (relatório de avaliação, fev/2025). [link](https://evaluation.treasury.gov.au/sites/evaluation.treasury.gov.au/files/2025-02/evaluation-generative-artificial-intelligence.pdf) · citado em p. 10, 13, 23, 28, 33, 48
- **M1013** — Forbes (edição australiana), com base em reportagem da Bloomberg (2023 (02/05/2023)). Samsung bans ChatGPT among employees after sensitive code leak. [link](https://www.forbes.com.au/news/innovation/samsung-bans-chatgpt-among-employees-after-sensitive-code-leak/) · citado em p. 1-2
- **M1016** — Gartner (2026 (10/06/2026)). AI Governance Requires More Than Policies (artigo, 10/06/2026; na aba do navegador, 'AI Governance Needs More Than Policies'). [link](https://www.gartner.com/en/articles/ai-governance-trism) · citado em p. 2, 4
- **M1021** — Government Digital Service (GDS), Governo do Reino Unido (2025 (jun/2025)). Microsoft 365 Copilot Experiment: Cross-Government Findings Report (jun/2025). [link](https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf) · citado em p. 4, 7, 8, 11
- **M1034** — Microsoft (2026 (consulta em 15/10/2026)). Develop a tenant environment strategy to adopt Power Platform at scale; Key concepts — Copilot Studio security and governance (documentação oficial). [link](https://learn.microsoft.com/en-us/power-platform/guidance/adoption/environment-strategy) · citado em p. 18, 39, 40
- **M1044** — Monash University (Departamento de Economia e SoDa Labs) (2023 (abr/2023)). The Unintended Consequences of Censoring Digital Technology – Evidence from Italy's ChatGPT Ban (artigo de trabalho, arXiv 2304.09339, abr/2023). [link](https://arxiv.org/abs/2304.09339) · citado em p. 11
- **M1047** — National Cyber Security Centre (NCSC), Reino Unido (2026 (18/06/2026)). The 'vibe coding spectrum' approach to AI-assisted software development. [link](https://www.ncsc.gov.uk/blogs/the-vibe-coding-spectrum-approach-to-ai-assisted-software-development) · citado em p. 2
- **M1051** — OWASP Foundation (projeto OWASP Citizen Development Top 10) (2025 (documento sem data; referências até set/2025)). OWASP Top 10 Risks for Citizen Development (riscos do desenvolvimento cidadão: low-code/no-code, programação assistida por IA e agentes). [link](https://owasp.org/www-project-citizen-development-top-10/) · citado em p. 9, 31-32
- **M1114** — Monetary Authority of Singapore (MAS) (2026 (07/10/2026; vigência a partir de 07/10/2027)). Guidelines on Artificial Intelligence Risk Management for Financial Institutions. [link](https://www.mas.gov.sg/-/media/mas-media-library/regulation/guidelines/bd/guidelines-on-artificial-intelligence-risk-management-for-financial-institutions/guidelines-on-artificial-intelligence-risk-management.pdf) · citado em p. 9, 11, 13, 14, 15, 28
- **M1199** — Boston Consulting Group (2026 (30/09/2026)). The Formula for Agentic AI Value — The Applied AI Index 2026. [link](https://www.bcg.com/publications/2026/the-formula-for-agentic-ai-value) · citado em p. 10
- **M1201** — PwC Brasil; Fundação Dom Cabral (2024 (03/12/2024)). ITDBr 2024 – Destaques do setor do Agronegócio. [link](https://www.pwc.com.br/pt/estudos/servicos/consultoria-negocios/indice-transformacao-digital-brasil/2024/PwC-ITDBr-Agro-24.pdf) · citado em p. 11
- **M1202** — Gartner (2026 (26/05/2026)). Gartner Says Applying Uniform Governance Across AI Agents Will Lead to Enterprise AI Agent Failure. [link](https://www.gartner.com/en/newsroom/press-releases/2026-05-26-gartner-says-applying-uniform-governance-across-ai-agents-will-lead-to-enterprise-ai-agent-failure) · citado em p. 1, 1-2
- **M1203** — Microsoft; pesquisa IPSOS (2024 (abr/2024)). Navigating the Stages of AI Value Creation (The AI Strategy Roadmap). [link](https://marketingassets.microsoft.com/gdc/gdc65yR29/original) · citado em p. 7
- **M1204** — 80,000 Hours (Robert Wiblin) (2026 (28/04/2026)). The story behind the bad AI stat that moved markets and misled millions. [link](https://80000hours.org/podcast/episodes/ai-workplace-mit-study/) · citado em p. 2, 4
- **M1205** — Cetic.br / NIC.br (2026 (15/06/2026)). Uso de inteligência artificial por empresas brasileiras avança e atinge 17% (TIC Empresas 2025). [link](https://cetic.br/pt/noticia/uso-de-inteligencia-artificial-por-empresas-brasileiras-avanca-e-atinge-17-aponta-pesquisa-do-cetic-br/) · citado em p. 1
- **M1206** — Gartner (2026 (16/04/2026)). Gartner Says Organizations with Successful AI Initiatives Invest Up to Four Times More in Data and Analytics Foundations. [link](https://www.gartner.com/en/newsroom/press-releases/2026-04-16-gartner-says-organizations-with-successful-ai-initiatives-invest-up-to-four-times-more-in-data-and-analytics-foundations)
- **M1207** — Gartner (Smarter With Gartner; K. Panetta) (2019 (05/02/2019)). The CIO's Guide to Artificial Intelligence (infográfico AI Maturity Model). [link](https://www.gartner.com/smarterwithgartner/the-cios-guide-to-artificial-intelligence/)
- **M1208** — High-Level Expert Group on AI (Comissão Europeia) (2019 (08/04/2019)). Ethics Guidelines for Trustworthy AI. [link](https://ec.europa.eu/newsroom/dae/document.cfm?doc_id=60419) · citado em p. 18
- **M1209** — K. J. Kevin Feng, David W. McDonald, Amy X. Zhang — University of Washington; Knight First Amendment Institute (2025 (28/07/2025)). Levels of Autonomy for AI Agents (arXiv 2506.12469). [link](https://arxiv.org/abs/2506.12469) · citado em p. 1
- **M1211** — Parlamento Europeu e Conselho da União Europeia (2024 (13/06/2024)). Regulation (EU) 2024/1689 — Artificial Intelligence Act. [link](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113) · citado em p. 1
- **M1212** — Parlamento Europeu e Conselho da União Europeia (2024 (13/06/2024)). Regulation (EU) 2024/1689 — Artificial Intelligence Act, Article 14: Human oversight. [link](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14) · citado em p. 2
- **M1216** — IT Forum (2023 (22/12/2023)). Torre controla transporte de madeira da Klabin. [link](https://itforum.com.br/noticias/torre-controla-transporte-de-madeira-da-klabin/) · citado em p. 2
- **M1217** — Jornal Cana (2026 (10/07/2026)). bp bioenergy reduz incêndios em 50% e consolida modelo de prevenção baseado em IA. [link](https://jornalcana.com.br/agricultura/tecnologia-agricola/bp-bioenergy-reduz-incendios-em-50-e-consolida-modelo-de-prevencao-baseado-em-ia) · citado em p. 1
- **M1218** — Mobile Time (2026 (11/06/2026)). São Martinho troca rede privativa por rede pública no campo. [link](https://www.mobiletime.com.br/noticias/11/06/2026/sao-martinho-rcp/) · citado em p. 1-2
- **M1219** — RPA News (2020 (17/11/2020)). Atvos tem economia de R$ 5,8 milhões com CIA. [link](https://revistarpanews.com.br/atvos-tem-economia-de-r-58-milhoes-com-cia/) · citado em p. 2
- **M1220** — Revista Cultivar (2020 (08/06/2020)). Conectividade no campo aumenta desempenho das fazendas da SLC Agrícola. [link](https://revistacultivar.com.br/noticias/conectividade-no-campo-aumenta-desempenho-das-fazendas-da-slc-agricola) · citado em p. 3
- **M1221** — SLC Agrícola (release publicado em Notícias Agrícolas) (2024 (27/09/2024)). Centro de Inteligência Agrícola da SLC completa cinco anos. [link](https://www.noticiasagricolas.com.br/noticias/agronegocio/385655-centro-de-inteligencia-agricola-da-slc-completa-cinco-anos-proporcionando-uma-agricultura-mais-eficiente-e-sustentavel.html)
- **M1222** — São Martinho (2018). Relatório Anual de Sustentabilidade 2017/18. [link](https://www.saomartinho.com.br/Download.aspx?Arquivo=0KPphi%2FhjYHruGs9g80smw%3D%3D&IdCanal=E%2F5CI5hbGiTfjZ7mhu2y5w%3D%3D) · citado em p. 27, 27-28
- **M1223** — Telesíntese (2024 (29/04/2024)). BP Bunge investe mais de R$ 100 milhões em transformação digital no campo. [link](https://telesintese.com.br/bp-bunge-investe-mais-de-r-100-milhoes-em-transformacao-digital-no-campo/) · citado em p. 2
- **M1224** — UDOP (nota da empresa) (2025 (30/04/2025)). Atvos investe R$ 16 milhões em rede própria de 4G. [link](https://www.udop.com.br/noticia/2025/04/30/atvos-investe-r-16-milhoes-em-rede-propria-de-4g.html) · citado em p. 1-2
- **M1238** — About Amazon (AWS) (2024 (09/12/2024)). Itaú Unibanco vai migrar o coração do banco para a nuvem. [link](https://www.aboutamazon.com.br/noticias/aws/itau-unibanco-vai-migrar-o-coracao-do-banco-para-a-nuvem) · citado em p. 2
- **M1239** — TI Inside (2026 (12/01/2026)). Itaú coloca 150 soluções de GenAI em produção e amplia uso de IA em 141%. [link](https://tiinside.com.br/12/01/2026/itau-coloca-150-solucoes-de-genai-em-producao-e-amplia-uso-de-ia-em-141/) · citado em p. 1, 2
- **M1240** — Agência Petrobras (2023 (05/12/2023)). Petrobras cria ferramenta com inteligência artificial generativa para apoiar mais de 100 mil trabalhadores. [link](https://agencia.petrobras.com.br/w/petrobras-cria-ferramenta-com-inteligencia-artificial-generativa-para-apoiar-mais-de-100-mil-trabalhadores) · citado em p. 1
- **M1241** — HSM Management (texto do head de IA da Vale) (2023 (24/08/2023)). Vale nos trilhos da inteligência artificial. [link](https://hsmmanagement.com.br/vale-nos-trilhos-da-inteligencia-artificial/) · citado em p. 4
- **M1242** — International Mining (2021 (02/07/2021)). Vale expects 21 autonomous drills running end-2021, passes 100 Mt hauled mark with AHS fleet at Brucutu. [link](https://im-mining.com/2021/07/02/vale-expects-21-autonomous-drills-running-end-2021-passes-100-mt-hauled-mark-ahs-fleet-brucutu/) · citado em p. 4
- **M1243** — Itaú Unibanco (2025). Integrated Annual Report 2024. [link](https://www.itau.com.br/download-file/v2/d/42787847-4cf6-4461-94a5-40ed237dca33/c54c2832-35d3-876f-acfc-930865b159d0?origin=2)
- **M1244** — Itaú Unibanco (2024). Relatório Anual Integrado 2023. [link](https://www.itau.com.br/download-file/v2/d/42787847-4cf6-4461-94a5-40ed237dca33/15ce52e3-fdd5-1bd2-4929-0674f0f3ce57?origin=2)
- **M1245** — Mobile Time (2024 (09/02/2024)). ChatGPT da Petrobras está disponível para toda companhia. [link](https://www.mobiletime.com.br/noticias/09/02/2024/chatgpt-da-petrobras-esta-disponivel-para-toda-companhia/) · citado em p. 2
- **M1246** — Mobile Time (2025 (14/05/2025)). Petrobras e agentes de IA. [link](https://www.mobiletime.com.br/noticias/14/05/2025/petrobras-agentes-ia/) · citado em p. 2
- **M1247** — Mobile Time (2026 (16/09/2026)). Vale abre plataforma de dados e IA a 19 áreas de negócio. [link](https://www.mobiletime.com.br/noticias/16/09/2026/vale-ia-bens-impostos/) · citado em p. 2, 3
- **M1248** — Moderna (2024 (24/04/2024)). Moderna and OpenAI Collaborate To Advance mRNA Medicine. [link](https://s29.q4cdn.com/435878511/files/doc_news/Moderna-and-OpenAI-Collaborate-To-Advance-mRNA-Medicine-2024.pdf) · citado em p. 1-2
- **M1249** — Petrobras (SEC) (2021). Form 20-F 2020. [link](https://www.sec.gov/Archives/edgar/data/1119639/000129281421001152/pbraform20f_2020.htm)
- **M1250** — Vale (2021 (02/09/2021)). Focused on safety and people, Vale starts operating autonomous trucks in its largest iron ore complex in Brazil. [link](https://vale.com/w/focused-on-safety-and-people-vale-starts-operating-autonomous-trucks-in-its-largest-iron-ore-complex-in-brazil) · citado em p. 1
- **M1251** — Vale (2019 (10/01/2019)). Vale creates Artificial Intelligence Center. [link](https://vale.com/w/vale-creates-artificial-intelligence-center) · citado em p. 1
- **M1252** — Vale (Newsroom) (2018 (09/11/2018)). Vale will have the first mine operating only with autonomous trucks in Brazil. [link](https://vale.com/documents/44618/2699492/Newsroom_-_Innovation_-_Vale_will_have_the_first_mine_operating_only_with_autonomous_trucks_in_Brazil_ID=1086.pdf/2fc567ec-9770-07cc-5ec9-c670830cfe74?version=1.0&t=1672692649808&download=true) · citado em p. 2
<!-- fontes:fim -->
