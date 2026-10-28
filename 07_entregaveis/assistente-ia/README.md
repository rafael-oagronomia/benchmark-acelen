# Assistente de IA do estudo — especificação de trabalho

> Documento interno da equipe OagronomIA. A versão para a Acelen está no [descritivo da metodologia](../../01_mobilizacao/metodologia.md), seção 10.

## Objetivo

Responder, em linguagem natural, a dúvidas sobre os estudos e as fontes de dados públicas levantadas no benchmark, **sempre com a fonte** (documento, organização, ano e página). É um dos entregáveis finais e um objetivo do estudo (decisão da OagronomIA em 09/10/2026, a apresentar à Acelen na semanal de 16/10).

O assistente é um meio de consultar o acervo do estudo. Não é uma solução para a operação da Acelen: o escopo continua excluindo a aplicação dos resultados na rotina da empresa e o desenho de soluções internas.

## Base de conhecimento

| Entra | Onde está | Observação |
|---|---|---|
| Catálogo de fontes públicas: metadados, métricas verificadas com página, resumos | `_triagem-pesquisa/_catalogo/catalogo.json` | IDs estáveis (M001…), registrados em `_catalogo/ids.json` |
| Fontes citadas nos entregáveis | `06_fontes/` | Lista gerada a partir das citações [M###, p. N] das notas e fichas |
| Fichas por empresa e notas temáticas | `02_frente-1_…/`, `03_frente-2_…/`, `04_frente-3_…/` | Só versões revisadas |
| Relatório final e base em Excel | `07_entregaveis/` | Versão final |
| Texto integral dos documentos públicos baixados | `_triagem-pesquisa/` (fora do Git) | Texto por página para a busca; o PDF fica no Storage privado e abre no sistema, na página citada, só para usuário logado; responder com trechos curtos e remeter ao original |
| Registros anonimizados das sessões executivas | `05_sessoes-executivas/registros-anonimizados/` | Decisão de 27/10: entram sem data e com os números relatados pelos entrevistados mascarados; a sessão 1 fica restrita até o consentimento |

**Não entra:** dados internos da Acelen; o repertório da Acelen (documento interno de preparação); nada tratado nas reuniões com a Acelen (atas, transcrições, pautas, pendências e pedidos do cliente); número que não seja de estudo público; transcrições brutas e nomes das sessões executivas; relatórios parciais; qualquer condição comercial do projeto.

## Como responde

- Cita no formato **Organização (ano), título curto, p. N — [M###]**. Sem fonte recuperada, não responde com número.
- Separa número verificado, "não conferido", "cálculo nosso" e "leitura nossa", como nos entregáveis.
- Aplica as regras de leitura: anúncio não é resultado; piloto não é produção; meta não é realizado; dado global não é dado do Brasil; dado do grupo não é dado da divisão.
- Quando o acervo não tem a resposta, diz isso e sugere o que procurar.
- Segue o escopo macro: não avalia nem recomenda ferramentas ou fornecedores.
- Trava de escopo (28/10): pergunta sem relação com o benchmark ou o acervo (saúde, receitas, esportes etc.) recebe o aviso de fora do escopo, sem busca nem resposta ao conteúdo.
- Responde em português.

## Perguntas de teste

Montar um conjunto de 20 a 30 perguntas com a resposta esperada e as fontes, à medida que as fichas e notas ficarem prontas. Medir: resposta correta, fonte correta (ID e página) e recusa correta quando não há base. Exemplos:

1. Que parcela das empresas brasileiras usa IA, segundo os estudos de 2026? (mais de uma fonte, com amostras diferentes)
2. O que a Suzano divulga sobre IA nas operações florestais?
3. O que é o E.L.Y. da Bayer e para quem ele foi feito?
4. Quais estudos medem o retorno da IA e o que eles encontram?
5. Como o MIT CISR descreve os estágios de maturidade em IA?
6. O que a China definiu no plano nacional de agricultura inteligente?
7. Pergunta sem base no acervo, para testar a recusa (ex.: um número interno de uma empresa que ela nunca divulgou).

## Disponibilização (a definir com a Estratégia e a TI da Acelen)

| Opção | Como funciona | Prós | Pontos de atenção |
|---|---|---|---|
| A. Base portátil | Entregamos a base de conhecimento (arquivos com o texto, as citações e as instruções do assistente) para carregar na ferramenta interna de IA da Acelen | Respeita a governança de TI e a soberania dos dados; a Acelen controla acesso e hospedagem | Depende da ferramenta interna aceitar a base; testes no ambiente da Acelen |
| B. Hospedado pela OagronomIA | Assistente com acesso restrito à Estratégia durante o projeto | Permite demonstrar e testar cedo | Precisa de aval da TI; a cópia da OagronomIA é excluída 90 dias após o fim, como os demais dados |
| C. Plataforma corporativa escolhida pela Acelen | Montagem na plataforma indicada pela TI | Integração com o ambiente da empresa | Prazo e acessos dependem da Acelen |

Preferência inicial, a validar: **A**, com uma demonstração (B) durante o projeto se a TI concordar.

**Decisão da OagronomIA (27/10):** construir a opção B, hospedada em Supabase Pro e Vercel Pro (região São Paulo). O acesso é por usuário cadastrado pelo admin, com senha temporária e troca obrigatória no primeiro acesso. Há conexão MCP para a pessoa consultar o acervo pela IA que ela usa, com o mesmo login. Perguntas e respostas ficam guardadas por 90 dias, com aviso ao usuário, e o prazo pode ser prorrogado. A base continua exportável (opção A) na entrega. Falta validar com a TI da Acelen, inclusive quais clientes de IA podem se conectar pelo MCP.

**Código e pipelines:** repositório separado `rag-benchmark-acelen` (pasta `C:\dev\rag-benchmark-acelen`), com a arquitetura em `docs/arquitetura.md`. Este repositório continua sendo o acervo: os pipelines leem o catálogo, os PDFs, as fichas, as notas e os registros das sessões daqui.

## Construção

| Semana | Passo |
|---|---|
| S3 (13–16/10) | IDs estáveis no catálogo; registro das fontes citadas em `06_fontes/`; primeiras fichas e notas no formato de citação |
| S4 (19–23/10) | Primeiro protótipo com o catálogo, as fichas e as notas; conjunto de perguntas de teste |
| S5 (26–30/10) | Testes de qualidade; ajustes; definição da disponibilização com a TI |
| S6 (03–06/11) | Entrega com o relatório final; acervo congelado na data de corte do relatório |

## Cuidados

- **Direitos autorais:** documentos de terceiros são públicos, mas não são nossos. Responder com síntese e trechos curtos, sempre remetendo ao original.
- **Alucinação:** responder só com base no que foi recuperado do acervo, com citação obrigatória, e medir isso nos testes.
- **Confidencialidade:** das sessões executivas, só os registros anonimizados (sem nomes nem data, números mascarados, sessão 1 restrita até o consentimento; metodologia Rev. 01) e a síntese; nada de dados internos da Acelen.
- **Atualização:** o acervo é congelado na data de corte do relatório; atualizações depois disso são outro trabalho.
