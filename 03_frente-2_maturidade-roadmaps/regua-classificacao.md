# Régua de classificação

Critérios para dar nota a cada empresa do painel com base em **evidência pública**. Faz parte do [framework de maturidade](framework-maturidade.md) (BIA-ACL-FM-01) e é aplicada nas fichas de benchmark conforme o [protocolo de pesquisa](../01_mobilizacao/protocolo-pesquisa.md) (BIA-ACL-PP-01).

As tabelas abaixo alimentam a aba "Régua" da base Excel. Mantenha os marcadores `<!-- tabela:… -->` e as colunas como estão.

## Como pontuar

1. Leia as evidências da ficha, dimensão por dimensão.
2. A nota é o **maior nível cujos critérios estão atendidos** por evidência registrada no catálogo de fontes.
3. **Sem evidência, sem nota.** Falta de evidência pública deixa a nota vazia. Não é nota 1.
4. **Confiança** A, B ou C, pelo nível da evidência mais forte que sustenta a nota. Notas 4 e 5 exigem ao menos uma evidência A.
5. Os níveis são cumulativos: o nível 3 pressupõe o 2. Se a evidência pular um degrau, atribua o nível evidenciado e registre a lacuna na ficha.

## Estágios

<!-- tabela:estagios -->
| Estágio | Nome | Natureza do uso | Descrição |
|---|---|---|---|
| 1 | Exploração | Uso exploratório | Uso individual e informal de IA; dados fragmentados em planilhas e silos. |
| 2 | Pilotos | Apoio à decisão em teste | Provas de conceito com escopo e métrica; primeiros dados organizados. |
| 3 | Operacionalização | Apoio à decisão em produção | Primeiro caso em produção; plataforma de dados unificada; governança formal. |
| 4 | Escala | Automação inteligente | IA embutida nos processos-chave; dados como produto; centro de excelência. |
| 5 | Transformação | Sistemas autônomos | IA no modelo de negócio; agentes e máquinas autônomas com supervisão por exceção. |

## Critérios por dimensão

### Governança de IA

Quem decide, política, gestão de riscos e uso responsável.

<!-- tabela:regua-governanca -->
| Nível | Critério | Evidência pública típica |
|---|---|---|
| 1 | Nenhuma instância, política ou patrocínio de IA evidenciados. | IA ausente dos relatórios; iniciativas isoladas citadas na imprensa. |
| 2 | Patrocínio executivo explícito e ao menos uma regra formal de uso de IA. | Alta liderança cita IA como prioridade; política de uso de IA generativa ou diretriz para dados sensíveis. |
| 3 | Instância formal que decide sobre IA, com gestão de riscos associada. | Comitê ou área dona do tema, com mandato descrito; política corporativa de IA; riscos de IA tratados em privacidade e segurança. |
| 4 | Governança de IA integrada à gestão de riscos e ao compliance corporativos, cobrindo TI e TO. | Princípios de IA responsável publicados; inventário ou monitoramento de modelos; alinhamento declarado a referencial (ISO/IEC 42001, NIST AI RMF); IA no relatório de riscos. |
| 5 | Governança que habilita autonomia: limites de ação, supervisão e responsabilização para agentes e máquinas autônomas. | Regras de supervisão por exceção descritas; auditoria de decisões automatizadas; certificação ou participação na definição de padrões do setor. |

### Dados

Estratégia de dados, qualidade, integração, plataforma e infraestrutura, incluindo conectividade no campo.

<!-- tabela:regua-dados -->
| Nível | Critério | Evidência pública típica |
|---|---|---|
| 1 | Dados dispersos em planilhas e sistemas isolados; sem estratégia de dados evidenciada. | Digitalização incipiente; nenhuma menção a plataforma de dados. |
| 2 | Organização inicial dos dados: BI ou data warehouse corporativo e digitalização de processos de campo em curso. | Painéis corporativos; sistema de gestão agrícola implantado; primeiros sensores ou telemetria. |
| 3 | Plataforma de dados unificada em operação, com governança de dados e conectividade nas áreas prioritárias do campo. | Data lake ou lakehouse com dados de várias áreas; papéis de governança de dados; cobertura de conectividade divulgada. |
| 4 | Dados tratados como produto: domínios responsáveis e dados de campo integrados em escala, quase em tempo real. | Arquitetura por domínios ou APIs de dados; telemetria de frota, imagens e sensores integrados; conectividade na maior parte da área. |
| 5 | Dados prontos para agentes e para o ecossistema: acesso governado por agentes e troca de dados com a cadeia. | Controle de identidade e auditoria para agentes; compartilhamento de dados com parceiros sob contrato; dados na base de novos serviços. |

### Organização

Estruturas, papéis, competências, modelo operacional e patrocínio.

<!-- tabela:regua-organizacao -->
| Nível | Critério | Evidência pública típica |
|---|---|---|
| 1 | Sem estrutura dedicada; iniciativas dependem de entusiastas. | Nenhuma área, cargo ou programa de dados e IA mencionado. |
| 2 | Núcleo técnico, interno ou com parceiro, conduz os pilotos, com patrocinador nomeado. | Laboratório de inovação; equipe de transformação digital; parceria com startup ou universidade para pilotos. |
| 3 | Área dedicada de dados e IA com liderança nomeada, papéis definidos com o negócio e programa de letramento. | Diretoria ou gerência de dados e IA; cargo de CDO ou equivalente; programa de capacitação em dados. |
| 4 | Centro de excelência ou modelo federado, com times de produto no negócio e capacitação em escala. | Centro de excelência em IA; times multidisciplinares nas áreas; capacitação de parcela relevante da força de trabalho; metas de adoção. |
| 5 | Organização redesenhada em torno da IA, com novos papéis para trabalhar com agentes e máquinas autônomas. | Papéis de supervisão de agentes ou de operação remota de máquinas; IA nas decisões de estrutura e força de trabalho. |

### Aplicações

Do apoio à decisão à automação e às tecnologias de campo, em nível macro.

<!-- tabela:regua-aplicacoes -->
| Nível | Critério | Evidência pública típica |
|---|---|---|
| 1 | Usos pontuais ou experimentais, sem caso em produção evidenciado. | Menções genéricas a IA; eventos e desafios de inovação. |
| 2 | Pilotos com escopo e objetivo divulgados, sobretudo de apoio à decisão. | Provas de conceito anunciadas, como previsão de safra ou detecção de pragas por imagem em área-piloto. |
| 3 | Ao menos um caso em produção com resultado mensurável divulgado. | Caso em operação com ganho quantificado em custo, produtividade ou perdas. |
| 4 | Portfólio em produção em vários processos-chave, com resultados recorrentes: automação inteligente em escala. | Casos em operação agrícola, industrial, logística e corporativa; ganhos divulgados de forma recorrente. |
| 5 | IA no modelo de negócio e operações autônomas em escala comercial. | Produtos ou serviços baseados em IA; agentes ou máquinas autônomas operando com supervisão por exceção. |

## Lentes

As lentes detalham duas frentes que o escopo pede para acompanhar em cada estágio. Recebem nível de 0 (sem evidência) a 5 e não entram no cálculo do estágio consolidado: são leituras dentro da dimensão Aplicações.

### IA generativa

LLMs, assistentes, copilotos e agentes.

<!-- tabela:regua-ia-generativa -->
| Nível | Critério | Evidência pública típica |
|---|---|---|
| 0 | Sem evidência. | — |
| 1 | Uso individual e informal, ou política inicial de uso. | Orientação interna sobre assistentes públicos; restrição de uso por segurança. |
| 2 | Pilotos de assistentes ou copilotos corporativos em ambiente controlado. | Assistente liberado a grupo-piloto; provas de conceito em atendimento, jurídico ou código. |
| 3 | Assistente corporativo em produção sobre dados e documentos da empresa, com governança de uso. | Assistente interno aberto a parcela relevante dos funcionários; consulta a documentos internos. |
| 4 | IA generativa integrada a processos-chave; agentes executam tarefas com aprovação humana. | Copilotos em fluxos de trabalho; agentes que preparam e submetem tarefas para aprovação; valor medido. |
| 5 | Agentes operam processos de ponta a ponta com supervisão por exceção; IA generativa em produtos e serviços. | Processos operados por agentes com humano monitorando exceções; oferta ao cliente baseada em IA generativa. |

### Campo e sistemas autônomos

Sensoriamento, visão computacional, drones, robótica e máquinas autônomas, sem marcas nem modelos.

A lente classifica **operações de campo, não máquinas**. É o mesmo princípio da norma ISO 18497-1:2024, que recusou uma escala de níveis por máquina.

- **Vale o nível mais alto em operação regular** em ao menos uma operação de campo relevante. Registre qual operação é.
- **Pilotos não dão nota.** Entram na ficha como evidência de direção.
- **Cada nível responde a três perguntas:** quem diagnostica, quem decide e quem executa.

<!-- tabela:regua-campo -->
| Nível | Critério | Evidência pública típica |
|---|---|---|
| 0 | Sem evidência. | — |
| 1 | Enxergar: monitoramento digital em operação regular; o humano diagnostica e decide com dado digital. | Imagens de satélite ou drone; telemetria; sensores; contagem de plantas por imagem. |
| 2 | Antecipar: modelos de diagnóstico e previsão em uso regular; o humano decide. | Previsão de produtividade, pragas ou falhas; mapas de variabilidade; detecção de incêndio por IA. |
| 3 | Executar com precisão, com o operador no comando: a máquina executa a prescrição em operação regular. | Guiagem e direção automáticas; controle de seções; aplicação localizada ou em taxa variável; drone de aplicação em rota programada. |
| 4 | Delegar tarefas delimitadas: a máquina completa ciclos sem interação, em zona e condições definidas, com operador próximo. | Pulverização autônoma, robô de capina ou de monitoramento, trator com kit autônomo, em operação regular. |
| 5 | Supervisionar a operação autônoma: autonomia em todo o ciclo; o humano programa, monitora várias unidades e trata exceções. | Frota autônoma em operação comercial, supervisionada no campo ou a distância. |

## Estágio consolidado

Calculado a partir das quatro notas de dimensão:

1. **Mediana das quatro notas.** Com quatro notas, a mediana é a média das duas do meio. Quando ela cai entre dois estágios, o estágio é registrado como transição (ex.: 3→4) e vale 3,5 na base Excel.
2. **Teto do alicerce:** o estágio não passa da nota de Dados + 1. Todos os frameworks revisados convergem neste ponto: sem alicerce de dados, a IA não sustenta o estágio seguinte.
3. **Mínimo de três notas, entre elas a de Dados.** Sem isso, o estágio fica como "evidência insuficiente". Com três notas, vale a do meio.

| Governança | Dados | Organização | Aplicações | Mediana | Teto (Dados + 1) | Estágio |
|---|---|---|---|---|---|---|
| 3 | 3 | 4 | 4 | 3,5 | 4 | 3→4 |
| 3 | 4 | 4 | 4 | 4 | 5 | 4 |
| 4 | 2 | 4 | 4 | 4 | 3 | 3 |
| 3 | — | 4 | 4 | 4 | — | Evidência insuficiente (sem nota de Dados) |
| 2 | 3 | — | — | 2,5 | 4 | Evidência insuficiente (só duas notas) |

## Declarado × evidenciado

Nas sessões executivas, o entrevistado posiciona a própria empresa na mesma régua de cinco estágios (pergunta 1 do roteiro BIA-ACL-SE-01). O estágio declarado não entra na nota de nenhuma empresa do painel. Ele é comparado, de forma agregada, com os estágios evidenciados, para medir o quanto o setor se vê mais maduro do que as evidências mostram.
