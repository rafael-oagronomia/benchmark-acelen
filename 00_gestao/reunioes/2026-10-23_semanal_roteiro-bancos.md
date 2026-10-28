# Semanal de 23/10/2026 — roteiro do bloco "Itaú, Bradesco e Nubank: governança e segurança" (Rafael)

> Documento interno da OagronomIA. Base: nota [bancos-itau-bradesco-nubank.md](../../03_frente-2_maturidade-roadmaps/bancos-itau-bradesco-nubank.md) (corte 20/10/2026), com o anexo de regulação, bancos globais e incidentes. Responde às pendências 17 e 18 da ata de 16/10. Os IDs entre colchetes são do catálogo; os M1075+ estão no lote provisório `rodada8.json`.

## Mensagem central (uma frase)

Os três bancos do pódio brasileiro em IA governam mais porque foram obrigados a governar modelos antes da IA generativa; o que a Acelen leva deles é o método, não o aparato.

## O que mostrar (3 slides)

**1. Os três bancos, lado a lado**
- Pódio: Nubank 1º, Itaú 2º, Bradesco 3º no índice latino-americano da Evident (20 bancos, só dados públicos) [M430, p. 9].
- **Itaú — plataforma única, muitos modelos, dado como produto.** 56 mil+ usuários da plataforma de IA generativa [M437, p. 16]; uma plataforma centralizada que orquestra 80+ modelos de terceiros escolhidos por acurácia e custo por tarefa, com FinOps; 1,5 mil curadores de dados, 95% dos dados com dono (imprensa) [M1043, p. 1-2]; 1,3 mil+ modelos em uso, R$ 11,7 bi em tecnologia em 2025 (imprensa) [M1192, web]; casos internos começam "em áreas limitadas" e só expandem "se aprovados" (imprensa) [M1125, web]. Governança publicada: só "robusta", em release [M1124, web].
- **Bradesco — a governança mais publicada.** Política de Riscos de IA aprovada pelo conselho, comissão de governança, análise de risco registrada no ciclo de vida, monitoramento com pausa ou desligamento, auditoria independente, termo de responsabilidade do usuário, usos proibidos [M456, web]; plataforma Bridge única e agnóstica de modelo, 200+ iniciativas (imprensa) [M1122, web]; adoção em sequência: gerentes → 60 mil funcionários (meta 2024) → 600 clientes em "teste controlado" (imprensa) [M1123, web].
- **Nubank — talento e modelo próprio, governança não publicada.** Modelo fundacional próprio no crédito, "every employee" com ferramentas de prototipagem, medição de uso e impacto por função [M447, web]; 5% do quadro em IA, três vezes a média [M430, p. 2, 4]; nenhum comitê, política ou regra de acesso em fonte pública. Como banco S1, tem o mesmo piso regulatório dos outros dois: não publicar não é não ter.
- Por que governam mais: 2017 (Res. CMN 4.557, avaliação independente de modelos) [M1078, p. 8]; 2021 (Res. CMN 4.893, política ciber aprovada pelo conselho) [M1077, p. 2-3]; 2011 nos EUA [M1075, web]. Para a Acelen vale só a LGPD [M1079, web].

**2. Os riscos além do shadow AI — e o que os três declaram**
- Dados em prompts: violações de política de dados em IA generativa dobraram, 223/mês, código-fonte 42% (Netskope, fornecedora) [M1049, p. 5]; Brasil: 64% com dados regulados, 9% senhas e chaves (via imprensa) [M1081, web].
- Credenciais: commits com IA vazam segredos em 3,2% vs 1,5% (GitGuardian, fornecedora) [M1082, web]; 24 mil segredos em configs de MCP [M1083, web]; o ataque ao pacote Nx usou as ferramentas de IA do dev para caçar chaves [M1084, web; M1085, web].
- Conectores e injeção de prompt: EchoLeak, zero clique no Microsoft 365 Copilot [M1088, web]; NCSC: "may never be totally mitigated" [M1086, web]; NIST: os 13 modelos de fronteira caíram ao menos uma vez [M1089, web]. O que se governa é o raio de ação.
- Skills e extensões: 341 maliciosas em 2.857 num marketplace de agentes [M1090, web]; 30 extensões de navegador, 260 mil usuários [M1092, web].
- Agentes com poder demais: banco de produção apagado [M1064, p. 1]; campanha de espionagem com 80–90% do trabalho feito pela IA [M1094, p. 6].
- O que os três declaram: Bradesco publica o "e se" (pausa, desligamento, incidentes, auditoria) [M456, web]; Itaú publica o "como" (plataforma única como ponto de controle) [M1043, p. 1-2]; Nubank, nada. A Febraban já nomeia "prompt injection" e "data exfiltration through prompts" como riscos do setor [M1104, p. 3-4]; nenhum dos três publica regra para agentes e conectores.
- Honestidade: mesmo no pódio a governança corre atrás. Febraban 2026 (25 bancos): 52% operam agentes, 16% em escala [M434, p. 21]; 36% com estrutura formal (14 respondentes) [M434, p. 25]; 17% sem governança de LLM [M434, p. 28].

**3. Régua e o que é transferível**
- Leitura nossa, sem ficha: Bradesco 4 em governança; Itaú 3→4; Nubank 2→3 por evidência pública (o Evident mede talento e inovação, não governança). Painel do estudo: Bayer 3; Suzano, Deere e DJI 2. Agro: um a dois estágios atrás (ITDBr: 4,8 × 3,4 em IA; 3,9 × 3,3 em governança) [M082, p. 20].
- Por quê: orçamento (R$ 50,4 bi em tecnologia em 2026 [M434, p. 7]; TI por usuário 2,7× a média [M1186, web]), regulação direta, dado nativo de crédito e fraude, ciber no conselho (58%) [M434, p. 33], 25 anos de governança de modelos.
- Transferível (método): plataforma governada em vez de proibição; catálogo de usos com risco; regra de dado em uma frase; dado antes do modelo; acesso faseado com letramento; dono e reporte ao conselho; conector e agente como identidade com privilégio mínimo; ambientes separados. Não copiar: aparato regulatório, três linhas completas, validação independente de tudo.
- Próximos passos: indicador "governança de agentes e conectores" na régua; perguntas para as sessões executivas; seção no relatório de 06/11; reler os PDFs do Itaú e do Bradesco já catalogados.

## O que falar (fio, 10–12 minutos)

1. **Abrir pelo pedido do Bruno.** "Vocês pediram para começar pelos bancos e citaram o Itaú. Pegamos os três do pódio brasileiro em IA — Nubank, Itaú e Bradesco — e fomos aos documentos públicos deles, do Banco Central e dos índices. O que trago é a visão de mercado da OagronomIA sobre governança e segurança, a parte em que vivi o setor por dentro."
2. **Os três, em uma frase cada.** Itaú: canal único que escolhe o modelo por tarefa, e dado tratado como produto. Bradesco: o que publica de governança é o mais completo do país, com política aprovada pelo conselho e botão de desligar. Nubank: o mais maduro em talento e modelo próprio, e o que menos publica sobre governança — o que mostra que liderar em adoção não é publicar governança.
3. **Por que eles governam mais.** As três datas. Frase-chave: "o banco não governa IA por vocação; governa porque o regulador cobra validação de modelo desde 2017 e política de ciber aprovada pelo conselho desde 2021. A Acelen não tem esse empurrão; tem a LGPD. A decisão de governar é dela."
4. **Ligar ao ponto do Bruno sobre acesso por cargo.** Nenhum dos três publica a regra, mas o padrão existe: Itaú começa por "áreas limitadas" e expande se aprovado; Bradesco foi de gerentes para 60 mil e depois para 600 clientes em teste controlado. É acesso faseado com letramento, não "plano top para alguns".
5. **Riscos além do shadow AI.** Um mecanismo por frase. Frase-chave: "o risco mudou de 'alguém colou um dado no chat' para 'um agente com a credencial da empresa leu uma instrução escondida num e-mail e mandou dado para fora sem ninguém clicar'. Isso não tem correção definitiva; o que se governa é o quanto o agente pode fazer. Nenhum dos três publica esse controle ainda."
6. **Honestidade sobre os bancos.** "Mesmo no pódio, um em cada seis grandes bancos não governa modelos de linguagem e só 16% têm agentes em escala. Estar à frente é em estrutura — dono, política, conselho — não em controle fino." Evita a leitura de que o agro está "errado".
7. **O que vale para a Acelen.** Os princípios como perguntas: "a empresa sabe quantos usos e agentes de IA tem e quem é o dono de cada um? Um funcionário sabe, sem perguntar, o que pode colar e onde? Algum agente acessa produção, e com que credencial?" Fechar: "método, não aparato."
8. **Fechar com os próximos passos** e perguntar se o comparativo bancos × painel entra no relatório como seção própria ou como norte dentro da Frente 2.

## Cuidados

- Nada de dado interno de banco: a experiência pessoal entra como leitura de mercado, sempre apoiada em documento público (cada afirmação da nota tem fonte).
- Dizer de quem é cada número de fornecedor (Netskope, GitGuardian, Koi, Snyk) e de consultoria (Deloitte, PwC). Não usar "Itaú cortou 65% do custo" (só imprensa), "60 mil usam a BIA" (era meta), "90% sem intervenção humana" (case da consultoria) nem "Nubank é o mais maduro em IA" sem dizer o que o índice mede: estão na seção 8 da nota.
- Se perguntarem "qual ferramenta?", responder com o padrão (plataforma governada com vários modelos), não com marca: o estudo não avalia nem recomenda ferramenta.
- Executivos e empresas das sessões executivas nunca aparecem; as declarações citadas são de executivos de bancos na imprensa.
- As fontes M1075 em diante estão em lote provisório (rodada 8), sem PDF baixado; a leitura de estágio dos três é nossa, sem ficha. Dizer "provisório" se for mostrado.
