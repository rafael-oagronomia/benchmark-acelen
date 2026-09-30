# Framework de maturidade em IA

**BIA-ACL-FM-01 · Rev. 00** (versão para discussão)

Referencial para posicionar empresas do agro, bioenergia e setores correlatos na adoção de IA e para enxergar o que precisa existir antes de cada salto de maturidade. O mesmo referencial permite, em leitura macro, posicionar a Acelen. Consolida os principais frameworks de mercado ([revisão](revisao-frameworks.md)) e os adapta a duas realidades que eles não cobrem: a operação de campo e a classificação por evidência pública.

Os números entre colchetes remetem ao [catálogo de fontes](../06_fontes/catalogo-fontes.csv).

## 1. Em uma página

- **5 estágios**, de Exploração a Transformação. São os mesmos da régua mostrada nas sessões executivas.
- **4 dimensões avaliadas com evidência pública:** governança de IA, dados, organização e aplicações.
- **2 lentes:** IA generativa (LLMs, copilotos e agentes) e campo e sistemas autônomos.
- **Regra do alicerce:** o estágio de uma empresa não passa da nota de Dados + 1.
- **Capacidades e dependências críticas** para cada salto, e **roadmaps observados** no mercado (sequência, ritmo e prioridades).

**O que o mercado mostra**

1. **Quase todas as empresas usam IA; poucas capturam valor em escala.** 89% das organizações usam IA em pelo menos uma função, mas só 22% escalaram IA em várias unidades de negócio. As que capturam valor relevante ficam entre 6% e 7,5% [F-0024; F-0012; F-0021].
2. **O divisor é sair do piloto e se sustentar em produção, e o gargalo é organizacional.** Pouco menos da metade dos projetos de IA chega à produção [F-0004]. As causas recorrentes são dados, valor mal definido, infraestrutura e governança, mais do que limites da tecnologia [F-0053; F-0005; F-0006].
3. **Dados primeiro.** Organizações bem-sucedidas com IA investem até quatro vezes mais em fundamentos de dados, governança e pessoas [F-0010]. 63% não têm, ou não sabem se têm, práticas de dados adequadas para IA [F-0006].
4. **No agro, a fundação inclui o campo.** Conectividade e centro de operações vêm antes da IA de campo. Levar a conectividade à escala levou de 3 a 5 anos nos casos observados [F-0104; F-0115; F-0103; F-0113; F-0112; F-0117].
5. **A IA generativa escala em meses sobre uma fundação pronta, e os agentes ainda estão no pico de expectativas.** Um assistente corporativo passou de um piloto com 500 pessoas para 110 mil trabalhadores com acesso em cerca de cinco meses [F-0119; F-0100]. Agentes totalmente autônomos ainda não estão prontos para a maioria dos usos corporativos [F-0009].

## 2. Como o framework foi construído

A [revisão de frameworks](revisao-frameworks.md) cobre os modelos do Gartner, MIT CISR, MIT Sloan Management Review com BCG, BCG, McKinsey, Microsoft, IBM, Google, Accenture, Deloitte e Cisco, além dos índices brasileiros e dos referenciais de governança e de campo. O framework consolidado segue cinco princípios.

1. **Compatível com a régua das sessões executivas.** Os estágios e as dimensões são os mesmos mostrados aos executivos (roteiro BIA-ACL-SE-01). Assim, o estágio declarado por eles pode ser comparado ao estágio evidenciado.
2. **Evidência pública, não autodeclaração.** Os frameworks de mercado classificam empresas por questionário respondido por elas mesmas. Aqui, cada nota exige uma fonte registrada. É isso que permite classificar empresas que não participam do estudo.
3. **Campo como lente própria.** Nenhum framework revisado tem recorte de agro nem trata a operação de campo (conectividade, telemetria, máquinas) como parte da maturidade.
4. **Dados como alicerce.** Os frameworks convergem neste ponto: sem dados prontos, a IA não sustenta o estágio seguinte. Daí o teto: estágio ≤ Dados + 1.
5. **IA generativa e agentes como lente transversal, não como estágio.** Eles aparecem em todos os estágios, com profundidade diferente em cada um.

## 3. Os cinco estágios

| Estágio | Natureza do uso | Como reconhecer |
|---|---|---|
| **1 · Exploração** | Uso exploratório | Uso individual e informal de IA; iniciativas sem orçamento dedicado; dados em planilhas e silos |
| **2 · Pilotos** | Apoio à decisão em teste | Provas de conceito com escopo, métrica e patrocinador; primeiros dados organizados; regra de uso de IA generativa |
| **3 · Operacionalização** | Apoio à decisão em produção | Primeiro caso em produção com resultado medido; plataforma de dados unificada; governança formal; orçamento dedicado |
| **4 · Escala** | Automação inteligente | Portfólio em produção nos processos-chave; dados como produto; centro de excelência; valor recorrente |
| **5 · Transformação** | Sistemas autônomos | IA no modelo de negócio; agentes e máquinas autônomas operando com supervisão por exceção |

**A virada está entre os estágios 2 e 3.** Nos dados do MIT CISR, as empresas nos estágios 1 e 2 têm crescimento e lucro abaixo da média do seu setor; a partir do estágio 3, ficam acima [F-0013; F-0014]. No Gartner, o nível "operacional" é justamente o primeiro projeto em produção, com patrocinador executivo e orçamento dedicado [F-0002].

**Correspondência com os frameworks de mercado** (aproximada; leitura OagronomIA)

| OagronomIA | Gartner (atual) [F-0003] | MIT CISR [F-0013] | BCG [F-0020] |
|---|---|---|---|
| 1 · Exploração | Foundational | 1 · Experiment and Prepare | Stagnating |
| 2 · Pilotos | Emerging | 2 · Build Pilots and Capabilities | Emerging |
| 3 · Operacionalização | Operational | 3 · Develop AI Ways of Working | Scaling |
| 4 · Escala | Scaled | 3 · Develop AI Ways of Working | Scaling, Future-built |
| 5 · Transformação | Transformational | 4 · Become AI Future Ready | Future-built |

## 4. Dimensões e régua

| Dimensão | O que cobre | Capacidades do escopo |
|---|---|---|
| **Governança de IA** | Quem decide, política, gestão de riscos, uso responsável | Governança |
| **Dados** | Estratégia de dados, qualidade, integração, plataforma e infraestrutura, incluindo conectividade no campo | Dados, infraestrutura |
| **Organização** | Estruturas, papéis, competências, modelo operacional e patrocínio | Pessoas, processos |
| **Aplicações** | Do apoio à decisão à automação e às tecnologias de campo | Processos (IA embutida) |

A [régua de classificação](regua-classificacao.md) traz os critérios de cada nível por dimensão e por lente, com a evidência pública típica. Também define a regra do estágio consolidado:

- **Mediana** das quatro notas;
- **teto** da nota de Dados + 1;
- **mínimo** de três notas, entre elas a de Dados.

## 5. Capacidades necessárias em cada estágio

| Capacidade | 1 · Exploração | 2 · Pilotos | 3 · Operacionalização | 4 · Escala | 5 · Transformação |
|---|---|---|---|---|---|
| **Dados** | Planilhas e sistemas isolados; sem fonte única | Dados dos pilotos organizados, com responsável | Plataforma unificada nos domínios prioritários; qualidade monitorada | Dados como produto por domínio; dados de campo integrados quase em tempo real | Dados prontos para agentes (identidade, permissão, auditoria); troca de dados com a cadeia |
| **Infraestrutura** | Ferramentas de uso pessoal; conectividade de campo pontual | Ambiente de experimentação; sensores e drones em áreas-piloto | Ambiente de produção com operação de modelos; conectividade nas áreas prioritárias | Plataforma corporativa de IA com custo gerido; conectividade ampla; processamento na borda; segurança TI/TO | Operação contínua de agentes e máquinas: baixa latência no campo, redundância, supervisão remota |
| **Pessoas** | Entusiastas isolados | Patrocinador nomeado; núcleo técnico, interno ou com parceiro | Time dedicado com liderança nomeada; letramento em curso | Centro de excelência ou modelo federado; capacitação em escala | Novos papéis para trabalhar com agentes e operar máquinas à distância |
| **Processos** | Iniciativas avulsas | Portfólio de pilotos com métrica de valor e critério de parada | Caminho definido do piloto à produção; valor medido depois da implantação | Processos-chave redesenhados com IA; portfólio gerido por valor | Processos operados por agentes e máquinas, com supervisão por exceção |
| **Governança** | Sem regra; uso informal de IA generativa | Política de uso de IA e de dados sensíveis | Instância formal de decisão; inventário de modelos; gestão de riscos | Governança integrada a riscos e compliance, cobrindo TI e TO | Governança proporcional à autonomia: limites de ação, auditoria, responsabilização |

**De onde vem a matriz**

- **Estágios do MIT CISR:**
  - estágio 1: educação, políticas de uso, dados acessíveis;
  - estágio 2: métricas, simplificação de processos, silos de dados consolidados;
  - estágio 3: plataforma reutilizável e cultura de testar e aprender;
  - estágio 4: IA em todas as decisões, combinando IA generativa, agêntica e robótica [F-0013].
- **Capacidades das organizações maduras em IA** segundo o Gartner: modelo operacional escalável, engenharia de IA, capacitação e gestão da mudança, e gestão de confiança, risco e segurança [F-0004].
- **Organizações de alta maturidade** (Gartner): 91% têm um líder de IA dedicado e 63% fazem análise de ROI e de risco [F-0008].
- **As seis capacidades do Rewired** [F-0025].
- **Referenciais de governança:** NIST AI RMF e ISO/IEC 42001 [F-0059; F-0061].

## 6. Dependências críticas

O que precisa estar estabelecido antes de cada salto. A evidência é consistente: projetos de IA travam menos por limite da tecnologia e mais por dados, valor mal definido, infraestrutura, governança e adoção.

- Só 48% dos projetos de IA chegam à produção, e a passagem do protótipo à produção leva em média 8 meses [F-0004].
- A regra 10-20-70 dos líderes em IA reserva 10% dos recursos para algoritmos, 20% para tecnologia e dados e 70% para pessoas e processos [F-0019].
- Na alta maturidade, 45% das iniciativas de IA ficam três anos ou mais em produção. Na baixa, 20% [F-0008].
- No agro brasileiro, um painelista resumiu assim: "a cada 100 testes, cinco viraram projetos que trazem retorno" [F-0001].

### 1 → 2 · De Exploração a Pilotos

**Precisa existir**

- Patrocínio executivo e IA na agenda estratégica.
- Problemas escolhidos pelo negócio, com métrica de valor e dono, e não pela tecnologia.
- Acesso aos dados dos casos escolhidos.
- Uma regra de uso de IA generativa que traga para dentro o uso informal.

**Quando falta:** a RAND aponta como causas-raiz de fracasso o problema mal entendido ou mal comunicado e o foco na tecnologia mais recente em vez do problema real [F-0053].

### 2 → 3 · De Pilotos a Operacionalização

É a travessia mais difícil e a que mais separa desempenho.

**Precisa existir**

- Dados prontos para IA nos domínios dos casos: plataforma unificada, qualidade e responsáveis.
- Engenharia para colocar e manter modelos em produção, integrados aos sistemas e ao fluxo de trabalho.
- Governança formal: quem decide, inventário de modelos e gestão de riscos.
- Método para medir o valor antes e depois da implantação.
- Nos casos de campo, conectividade e integração entre TI e TO nas áreas dos casos.

**Quando falta**

- Ao menos 30% dos projetos de IA generativa seriam abandonados depois da prova de conceito por dados ruins, controles de risco inadequados, custos crescentes ou valor incerto [F-0005].
- 60% dos projetos sem dados prontos para IA devem ser abandonados até 2026 [F-0006].
- A principal barreira declarada é estimar e demonstrar valor (49%) [F-0004].
- O MIT CISR nomeia quatro desafios desta passagem: estratégia, sistemas, sincronização de pessoas e papéis, e stewardship. E adverte: sem um time dedicado, a empresa fica presa no piloto [F-0014].

### 3 → 4 · De Operacionalização a Escala

**Precisa existir**

- Dados tratados como produto e plataforma reaproveitada entre casos.
- Modelo operacional que escala: centro de excelência ou modelo federado, com liderança de IA dedicada.
- Capacitação e gestão da mudança em escala.
- Portfólio gerido por valor (ROI e risco) e custo de IA sob controle.
- Segurança integrada entre TI e TO.

**Quando falta**

- Organizações bem-sucedidas investem até quatro vezes mais em fundamentos [F-0010].
- O redesenho de fluxos de trabalho é o fator com maior efeito no EBIT, e quase três quartos dos high performers o fazem, contra um quarto das demais [F-0022; F-0024].
- Quem acompanha o ROI e gere a IA como portfólio tem retorno positivo em 81% das iniciativas [F-0012].

### 4 → 5 · De Escala a Transformação

**Precisa existir**

- Dados prontos para agentes: identidade, permissões e trilha de auditoria.
- Governança proporcional à autonomia: controles que crescem com o poder de ação do agente ou da máquina.
- Processos redesenhados para humanos e agentes trabalharem juntos.
- Para máquinas autônomas no campo: requisitos de segurança funcional, conectividade de baixa latência e operação remota.

**Quando falta**

- Mais de 40% dos projetos de IA agêntica devem ser cancelados até o fim de 2027 por custo, valor incerto ou controles de risco inadequados [F-0007].
- 40% das empresas devem rebaixar ou desativar agentes autônomos por lacunas de governança descobertas só depois de incidentes [F-0011].
- Só 5% das empresas têm hoje os controles completos para dar autonomia a agentes [F-0021].

## 7. IA generativa e agentes em cada estágio

A IA generativa chegou a 70% de adoção em três anos [F-0018]. Os agentes vêm em seguida, mas as medições divergem conforme a definição usada:

- 23% das organizações escalam agentes e 39% experimentam [F-0023];
- 40% das grandes empresas escalam agentes em 2026 [F-0024];
- numa pesquisa com CIOs, só 17% implantaram agentes [F-0009].

A divergência é sinal de que o termo ainda é elástico. O Gartner chama de "agent washing" a prática de rebatizar assistentes, automações e chatbots como agentes [F-0007]. A confiança em agentes totalmente autônomos caiu de 43% para 27% [F-0057].

| Estágio | Como a IA generativa aparece | Papel humano [F-0056] | Autonomia do agente [F-0011] |
|---|---|---|---|
| 1 · Exploração | Uso individual de assistentes públicos | Operador | — |
| 2 · Pilotos | Assistentes corporativos com grupos-piloto | Operador, colaborador | Observar, aconselhar |
| 3 · Operacionalização | Assistente corporativo em produção sobre documentos da empresa | Colaborador | Aconselhar |
| 4 · Escala | Copilotos nos fluxos-chave; agentes executam com aprovação humana | Consultor, aprovador | Agir com aprovação |
| 5 · Transformação | Agentes operam processos com supervisão por exceção | Observador | Agir de forma autônoma |

Correspondência entre as escalas: leitura OagronomIA.

A supervisão humana acompanha o nível de autonomia. Passa de "no circuito", com intervenção em cada decisão, para "sobre o circuito", com monitoramento da operação [F-0058]. É também o critério do AI Act europeu: supervisão proporcional ao risco e ao nível de autonomia [F-0062].

**Como os líderes incorporam**

- **Assistente para todos primeiro, casos específicos depois.**
  - Petrobras: de um piloto com 500 pessoas para 110 mil trabalhadores com acesso em cerca de cinco meses [F-0119; F-0100].
  - Suzano: copiloto para quase 50 mil pessoas cerca de um ano depois do primeiro assistente industrial [F-0107].
  - Moderna: mais de 750 assistentes especializados em poucos meses [F-0102].
- **Só anda rápido sobre base pronta.** O Itaú construiu data lake e nuvem entre 2014 e 2023. Depois passou de cerca de 10 para 150 soluções de IA generativa em produção em cerca de dois anos [F-0089; F-0090; F-0092].
- **Governança e letramento antes da escala.**
  - São Martinho: 99% do público elegível treinado na política de uso de IA [F-0105].
  - Klabin: 18 selecionadas entre mais de 300 demandas, com critérios para quando colaboradores podem criar agentes [F-0109].
- **Agentes com cautela.** A Petrobras abriu uma plataforma de agentes reconhecendo que os padrões ainda não estão maduros [F-0101].
- **O valor vem do redesenho do trabalho, não da ferramenta** [F-0024; F-0015].

## 8. Campo e sistemas autônomos em cada estágio

No agro, boa parte do valor e da mão de obra está no campo, e os frameworks corporativos não cobrem essa operação. Por isso a lente de campo é própria.

**Não existe escala oficial de níveis para máquinas agrícolas.** A norma ISO 18497-1:2024 recusou de propósito a escala de seis níveis dos veículos autônomos. Ela descreve combinações de funções — parcialmente automatizada, semiautônoma e autônoma — e avisa que isso "não é nível nem categoria de máquina" [F-0068]. A lente, portanto, classifica **operações de campo**. Vale o nível mais alto alcançado em operação regular, e não em piloto.

A trilha tem três bases:

- a FAO, que decompõe toda operação agrícola em diagnóstico, decisão e execução [F-0072];
- a tipologia de gêmeos digitais: monitorar, prever, prescrever e operar com autonomia [F-0073];
- a sequência proposta pela Embrapa: anomalias, variabilidade para intervenção e atuação autônoma [F-0075].

| Nível | Operação | Quem diagnostica, decide e executa | Maturidade da tecnologia |
|---|---|---|---|
| **1 · Enxergar** | Monitoramento digital: imagens de satélite ou drone, telemetria, sensores, contagem de plantas | O humano diagnostica e decide com dado digital | Em escala ou madura |
| **2 · Antecipar** | Diagnóstico e previsão: produtividade, pragas, falhas, incêndio; mapas de variabilidade | O modelo diagnostica e prevê; o humano decide | Em escala no mapeamento; perto do mercado na análise por IA |
| **3 · Executar com precisão** | Guiagem e direção automáticas, controle de seções, taxa variável, drone em rota programada | A máquina executa a prescrição; a decisão é humana | Madura |
| **4 · Delegar tarefas** | A máquina completa ciclos sem interação, em zona e condições definidas, com operador próximo | A máquina executa a tarefa; o operador retoma quando preciso | Perto do mercado ou início da escala |
| **5 · Supervisionar a autonomia** | Autonomia em todo o ciclo; o humano programa, monitora várias unidades e trata exceções | A máquina diagnostica, decide e executa; o humano supervisiona | Protótipo ou perto do mercado; normas em construção |

Maturidade pela régua da FAO: protótipo, perto do mercado, em escala, maduro [F-0072].

No nível 5, a máquina assume três responsabilidades do operador: conduzir monitorando o ambiente, monitorar a própria saúde e garantir a qualidade do trabalho [F-0069].

A lente é independente do estágio: uma empresa pode estar no estágio 4 na organização e no nível 3 no campo. A "agricultura 5.0", com robótica e alguma forma de IA, é a fronteira que a indústria aponta [F-0074].

### Onde o campo está

- **Brasil, produtores.**
  - 84% usam ao menos uma tecnologia digital, mas só 6% usam sistemas automatizados ou robotizados. A pesquisa é online e de 2020, com peso de pequenos produtores [F-0052].
  - Só 33,9% da área agrícola tem sinal 4G ou 5G [F-0079]. Nos outros dois terços, a falta de sinal limita telemetria, correção de sinal e supervisão remota.
- **América Latina, grandes produtores.**
  - Controle de seções em pulverizadores em 75% e monitoramento de produtividade em 49% [F-0076].
  - Em 2026, 26% usavam IA generativa, a maioria em ferramentas gratuitas; a robótica tinha penetração mínima [F-0077].
- **Agtechs brasileiras.** 83% das 170 que responderam ao Radar Agtech usam IA. É oferta de tecnologia, não adoção no campo, e o dado não vale para as 2.075 mapeadas [F-0078].
- **China.**
  - Mecanização de 75,64% em preparo, plantio e colheita em 2024 [F-0080] e 76,7% em 2025.
  - Mais de 300 mil drones agrícolas em 2025. Drones e robôs entraram pela primeira vez no Documento Central nº 1, de 2026 [F-0081].
  - Meta de informatização da produção agrícola: 30% até 2026 e 40% até 2035 [F-0082].
- **Mundo.** Robôs autônomos de lavoura só entraram em uso comercial recentemente [F-0072]. Não há dado público verificado de unidades ou hectares de máquinas autônomas em operação.
- **Líderes do agro brasileiro observados.** Estão nos níveis 2 e 3 em operação regular:
  - detecção de incêndio por IA [F-0108; F-0114];
  - aplicação localizada [F-0113];
  - drones de aplicação [F-0109].

  Nenhum mostra frota autônoma em operação regular.

### Palmeiras de baixa mecanização

A palma de óleo é o análogo mais próximo da macaúba: palmeira perene, colheita manual e escassez de mão de obra.

- **A colheita é o gargalo.**
  - Na palma, a colheita concentra cerca de 60% da força de trabalho e 50% do custo de produção [F-0084].
  - A Malásia tem déficit de 40 mil trabalhadores. Nas palavras do ministro do setor, drones já servem para fertilização e pesticidas, mas ainda não há máquina para colher [F-0083].
  - A colheita mecânica é problema aberto desde 2004, e a robótica de colheita segue em fase experimental [F-0085; F-0084].
- **Contar plantas por imagem é maduro; diagnosticar saúde, ainda não.**
  - A detecção de palmeiras passa de 96% de acerto [F-0086].
  - O diagnóstico de plantas doentes confrontado com o campo fica em 57% [F-0087].
- **Na macaúba, a própria mecanização da produção de frutos ainda é agenda de pesquisa** [F-0088].

**Leitura:** a trilha de campo não avança por igual em todas as culturas. Em palmeiras de baixa mecanização:

- os níveis 1 e 2 são viáveis hoje: censo de plantas, mapeamento de copas e previsão;
- o nível 3 já existe na aplicação de insumos por drone;
- a colheita nos níveis 4 e 5 está em pesquisa há mais de 20 anos.

### Dependências da autonomia no campo

- **Normas técnicas insuficientes.** As normas para a entrada segura de máquinas autônomas no mercado ainda estão em construção [F-0070; F-0071].
- **Custo.** O custo inicial alto limita a adoção de robôs, sobretudo em fazendas pequenas e médias [F-0071].
- **Supervisão a distância.** Só funciona quando a operação autônoma é relativamente livre de falhas, e alguns países exigem supervisão humana no local [F-0072].
- **Conectividade e sinal de posicionamento.** Na palma, a copa e o relevo limitam o GPS [F-0084]. No Brasil, dois terços da área agrícola estão sem 4G ou 5G [F-0079].

## 9. Roadmaps observados no mercado

Foram verificadas em fontes públicas dez jornadas: quatro de setores de referência (financeiro, mineração, óleo e gás, farmacêutico) e seis do agro, da bioenergia e do setor florestal.

### Sequência típica

1. **Fundação.**
   - Fora do agro, dados e nuvem. O Itaú teve data lake em 2014/15 e iniciou a nuvem em 2017 [F-0089; F-0091].
   - No agro, conectividade de campo e um centro de operações que concentra os dados em tempo real:
     - São Martinho, desde 2015 [F-0104];
     - SLC, 2019 [F-0103; F-0113];
     - Klabin, 2021 [F-0118];
     - Raízen [F-0110];
     - BP Bunge [F-0111];
     - Atvos [F-0112].
2. **Estrutura dedicada**, de 0 a 3 anos depois.
   - Vale: programa digital em 2016 e centro de IA em 2019 [F-0093; F-0094].
   - Petrobras: diretoria digital em 2019 e centro de excelência em 2020 [F-0099].
   - Klabin: IA Office em 2024 [F-0109].
3. **IA preditiva e de otimização** em dores mensuráveis: incêndio, insumos, manutenção e logística.
   - SLC: economia de R$ 2 milhões para R$ 82 milhões em quatro anos [F-0103].
   - Raízen: tempo de chegada aos incêndios 27,6% menor [F-0110].
   - BP Bunge: incêndios 50% menores [F-0114].
4. **IA generativa para toda a empresa**, na onda de 2023–24 [F-0100; F-0107; F-0109].
5. **Governança e democratização:** política de uso, letramento, triagem de demandas e criação pelos próprios usuários [F-0105; F-0109; F-0097].
6. **Agentes e autonomia avançada**, a partir de 2025 e com cautela.
   - Petrobras: plataforma de agentes [F-0101].
   - Vale: primeira mina já nascida 100% autônoma [F-0096].

### Ritmo

| Etapa | Tempo observado | Casos |
|---|---|---|
| Conectividade de campo em escala | 3 a 5 anos | São Martinho, SLC, Atvos [F-0104; F-0115; F-0103; F-0113; F-0112; F-0117] |
| Do centro de inteligência ao retorno relevante | Cerca de 4 anos | SLC [F-0103] |
| Da estrutura de IA a um portfólio escalável | Cerca de 6 anos | Vale [F-0094; F-0096] |
| Da fundação de dados à IA generativa | 8 a 9 anos | Itaú [F-0089] |
| Do piloto de IA generativa à empresa toda | 5 a 12 meses | Petrobras, Suzano, Moderna [F-0100; F-0107; F-0102] |
| Autonomia pesada | Cerca de 3 anos até 100% de uma mina, mais 2 para replicar | Vale [F-0093; F-0116; F-0095] |

### Prioridades

- **Começar por dores mensuráveis com dono no negócio.** No agro: incêndio, insumos, manutenção e logística.
- **Concentrar em poucos domínios.** Os líderes perseguem cerca de metade das oportunidades dos demais e geram 62% do valor nos processos centrais do negócio [F-0019].
- **Medir valor como disciplina, não como exceção** [F-0012].

### Atalhos e armadilhas

**Atalhos que funcionaram**

- IA generativa sobre base de dados pronta.
- Assistente para todos antes dos casos específicos.
- Democratização com regras claras.
- Torre de controle como porta de entrada dos dados de campo em tempo real.

**Armadilhas relatadas publicamente**

- O mais caro é obter os dados. Levá-los da rede de automação à TI pode ser caro e demorado [F-0098].
- A TI vira gargalo: pedidos de dados levavam até três semanas antes de a plataforma ser aberta às áreas de negócio [F-0097].
- Rede de campo própria exige operação contínua. Uma usina está trocando a rede privativa pela de uma operadora [F-0106].
- A demanda supera a capacidade: mais de 300 pedidos de IA e 18 selecionados [F-0109].
- Agentes ainda imaturos para ambientes críticos [F-0101].

### O que isso sugere para o médio e o longo prazo

Leitura OagronomIA, como referência de mercado. Não é desenho de solução interna.

- **A fundação de campo é a etapa mais longa e vem antes da IA de campo.** Conectividade em escala levou de 3 a 5 anos nos casos observados.
- **O valor aparece na passagem do piloto à produção.** Ela depende de dados prontos, estrutura dedicada e medição.
- **IA generativa para todos dá velocidade de adoção.** O valor, porém, vem dos casos específicos e do redesenho do trabalho.
- **Autonomia pesada é aposta de longo prazo.** Na referência mais madura do Brasil, foram cerca de três anos de piloto controlado até uma mina 100% autônoma, e mais dois para replicar.

## 10. Onde o mercado está

### No mundo

- **Uso generalizado.** 88% das organizações usavam IA em pelo menos uma função em 2025, contra 55% em 2023 [F-0044].
- **Escala é minoria.**
  - Só 22% escalaram IA em várias unidades de negócio [F-0012].
  - Na visão dos CEOs, só 16% das iniciativas escalaram para a empresa toda [F-0031].
- **Distribuição por estágio.** Entre 36% e 52% das empresas ainda estão nos dois primeiros estágios, e entre 7,5% e 18% chegaram ao topo:
  - MIT CISR: 13%, 23%, 46% e 18% nos quatro estágios [F-0014];
  - BCG: 4,5% stagnating, 47% emerging, 41% scaling e 7,5% future-built [F-0021].

  As amostras e os critérios diferem.

### No Brasil

- **Uso.**
  - 17% das empresas com 10 ou mais pessoas usam IA; entre as grandes, 50% [F-0049].
  - Na indústria com 100 ou mais pessoas, 41,9%, contra 16,9% em 2022 [F-0048].
- **Escala e governança são o gargalo.** Só 23% das empresas escalaram 40% ou mais dos pilotos, e só 27% têm governança madura para IA agêntica [F-0050].
- **Nem os bancos chegaram ao topo.** 40% têm maturidade média ou alta em IA [F-0051].

### No agro

- **Maturidade digital.** O agro saiu do último lugar em maturidade digital (3,1 contra 3,7 em 2024) e chegou à média (3,6 em 2025). Infraestrutura e estratégia puxaram essa melhora; a dimensão IA seguiu abaixo da média [F-0046; F-0047].
- **O ganho é de eficiência, não de modelo de negócio.** 90% citam eficiência operacional como resultado da digitalização, e só 21% citam novos modelos de negócio [F-0047].
- **Na agroindústria,** o uso de IA em alimentos (39,0%) e em celulose e papel (33,1%) fica perto ou abaixo da média industrial [F-0048].
- **Declarado × evidenciado.**
  - 78% das empresas do agro dizem ter IA na agenda de 2026: 42% em piloto e 36% em produção, por autodeclaração.
  - Os especialistas do mesmo evento descrevem o setor "ainda numa fase de validação" [F-0001].
  - A pesquisa da Microsoft mede esse viés em geral: 34% se declaram nos dois estágios mais altos, contra 25% pelo modelo [F-0026].
- **Líderes observados.**
  - Têm conectividade e centros de operação, IA preditiva com resultado em incêndio, insumos e manutenção, e IA generativa para todos os funcionários.
  - Nenhuma tem frota autônoma pesada verificada.
  - Ver os roadmaps da seção 9.

**Hipótese de trabalho, a confirmar com as fichas da Frente 1:**

- o agro típico está entre os estágios 1 e 2;
- as líderes com evidência pública estão entre o 3 e o 4;
- nenhuma empresa do agro chegou ao 5.

## 11. Como usar o framework

- **Frente 1 — fichas de benchmark.** Cada empresa do painel recebe notas pela régua, com fonte, e o estágio consolidado é calculado na base Excel (BIA-ACL-BD-01).
- **Sessões executivas.** O estágio declarado pelos executivos é comparado, de forma agregada, com o evidenciado.
- **Workshop Executivo.** Posicionamento do painel e leitura macro da Acelen na mesma régua, pela dinâmica descrita em BIA-ACL-WS-01.
- **Roadmap de médio e longo prazo.** Dependências críticas e ritmos observados servem de referência de sequência e prazo.

## 12. Limites

- **Evidência pública mostra mais sucessos que fracassos.** As sessões executivas ajudam a equilibrar.
- **As pesquisas globais são autodeclaradas e não têm recorte de agro.** Servem para calibrar, não para comparar empresa a empresa.
- **A correspondência entre frameworks é aproximada.** Cada um mede coisas diferentes.
- **Estudos preliminares ou com método frágil** entram só de forma qualitativa. É o caso do MIT NANDA 2025 [F-0054; F-0055].
