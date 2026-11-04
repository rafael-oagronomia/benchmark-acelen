# Linha de investigação — Roadmap de adoção: trajetória, checkpoints, papéis e políticas de uso

> Documento de trabalho da OagronomIA · Frente 2 — Maturidade e roadmaps · Aberto em 03/11/2026 · Protocolo do tema e estrutura da nota temática e da página do site do assistente. Fica fora do assistente de IA (linha de investigação). Número novo só entra na nota depois de verificado e catalogado.

## 1. Por que o tema entra

- **É o que falta na Frente 2.** Três itens do escopo seguem abertos no [README da frente](README.md): capacidades necessárias em cada etapa, dependências críticas de cada salto e roadmaps observados no mercado. O relatório final também promete um "roadmap de mercado para adoção de IA".
- **Foi o pedido central da semanal de 30/10** ([transcrição anonimizada](../00_gestao/reunioes/2026-10-30_semanal_transcricao.md), 44:37 a 51:31):
  - enxergar um roadmap de adoção: a sequência de marcos que as empresas seguiram, olhando para trás (lições aprendidas), para o cenário de hoje e para a frente;
  - os pré-requisitos de cada nível da régua, "para dar o check": a distância da média do mercado e o que falta estruturar;
  - o paralelo com outros setores (financeiro e outros) e com florestal, energia e agro, porque a percepção é de que o agro está atrás;
  - a passagem que o cliente deu de exemplo: proibição, uso por fora no celular e na conta pessoal, e depois política, governança e ferramentas específicas por área. "Não é a fórmula mágica, mas é o que o mercado fez."
- **Outros pontos da mesma reunião ligados ao tema:**
  - política clara de uso, com consequências (15:31 a 27:08);
  - como se proteger ao liberar ferramentas além da oficial (23:24);
  - o papel da TI, de quem trava a quem lidera a transição (1:05:08 a 1:10:56);
  - como a IA chega à operação de campo, inclusive em culturas perenes (53:29 a 1:04:16).
- **Material de evento** (fotos recebidas em 03/11/2026). São seis slides de um parceiro da Microsoft sobre adoção do Copilot:
  - os papéis da adoção (patrocinador, champions por área, early adopters, comitê de IA, dono técnico na TI, usuário final);
  - o que o champion faz e o que não é;
  - os rituais com cadência;
  - uma matriz de métricas;
  - a conta do retorno de um caso.

  As fotos estão em `_triagem-pesquisa/_eventos/2026-11_evento-parceiro-microsoft_adocao-copilot/`, fora do Git. **Uso: só como inspiração de estrutura.** É material comercial de fornecedor, sem fonte pública, e as metas dos slides são sugestões do parceiro, sem base divulgada. Cada elemento só entra no estudo com fonte pública do catálogo. O estudo não recomenda ferramenta, nem o Copilot nem outra.
- **Escopo.** Macro e de mercado: o que as empresas fizeram, em que ordem e com que papéis e regras. Não é diagnóstico da Acelen nem desenho da governança interna, que é tema da TI da companhia (regra do projeto).

## 2. O que o acervo já tem

| Bloco | O que já existe | Onde |
|---|---|---|
| Estágios e passagem | Régua de 5 estágios e 4 dimensões; passagem por evidência pública, cumulativa | [frameworks-de-maturidade.md](frameworks-de-maturidade.md), seções 3 e 6 |
| Capacidades, dependências e jornadas | Capacidades por estágio; o que precisa existir antes de cada salto (1→2 a 4→5); IA generativa e campo em cada estágio; dez jornadas verificadas, com sequência, ritmo, prioridades, atalhos e armadilhas; régua com critério e evidência típica por dimensão | Ramo do Rafael de 30/09 (`origin/rafael/estruturacao-analitica-frente-2`): `framework-maturidade.md` (BIA-ACL-FM-01, rev. 00, para discussão) e `regua-classificacao.md`, nunca levados ao main |
| Uso fora dos canais oficiais | Caminhos das corporações (proibir, ferramenta única, várias ferramentas, plataforma interna); controles; indicador de 5 estágios | [shadow-ai-e-governanca.md](shadow-ai-e-governanca.md), seções 7, 8 e 12 |
| Custo | Indicador de gestão do custo; consumo por usuário e por ferramenta | [custo-da-ia.md](../04_frente-3_tendencias/custo-da-ia.md) |
| Valor | Como as empresas medem (e não medem) o retorno | [valor-e-retorno-da-ia.md](../02_frente-1_benchmark-estrategico/notas/valor-e-retorno-da-ia.md) |
| Setor financeiro | Por que governa mais; riscos além do shadow AI; o que é transferível (método, não aparato) | [bancos-itau-bradesco-nubank.md](bancos-itau-bradesco-nubank.md), seções 3, 5 e 7 |
| Sessões executivas (só o agregado) | Assistente corporativo para todos como salto de uso (S-02); vias homologadas e licença por perfil ou por solicitação aprovada (S-02, S-03); facilitadores por área previstos ou recentes (S-03, S-04); encontro semanal aberto de usuários avançados (S-02); comitê multidisciplinar e registro de quem usa (S-04); governança que trava e TI com pouca visão do potencial (S-01); medir o retorno, ampliar o acesso e educar em 2027 (S-04) | [registros anonimizados](../05_sessoes-executivas/registros-anonimizados/) e síntese RP-07 |

**O framework do Rafael é a base mais pronta, mas cita outro catálogo.** Ele usa os IDs F-#### do catálogo próprio de 30/09. Dos 94 IDs F citados no framework e na régua:
- 35 já têm par no catálogo M: 23 pela URL e 12 pelo título, a conferir;
- 59 não têm par. Entre eles estão as jornadas de Itaú, Vale, Petrobras, Moderna, SLC, São Martinho, Atvos, BP Bunge e Klabin, comunicados do Gartner de 2026 e o roteiro de valor de IA da Microsoft com a Ipsos.

O mapa automático está em `_triagem-pesquisa/_catalogo/mapa_F_rafael_para_M.json`, fora do Git.

## 3. Perguntas centrais

1. **Trajetória.** Que sequência de marcos as empresas seguiram na adoção de IA (preditiva e generativa), em especial de 2023 a 2026, e quanto tempo levou cada etapa?
2. **Checkpoints.** O que precisa estar de pé em cada estágio da régua, por dimensão, e como se verifica (em fonte pública e, para quem se autoavalia, por pergunta objetiva)?
3. **Papéis.** Quem faz o quê nas empresas que avançaram: patrocinador, comitê, área de IA ou centro de excelência, TI, segurança, jurídico e privacidade, RH e educação, champions ou builders, usuário?
4. **Fluxo.** Como um caso vai da ideia à produção e à medição? E como uma ferramenta ou um modelo novo vai do pedido à liberação?
5. **Política de uso.** O que uma política clara contém, e o que a faz funcionar (canal oficial bom, treinamento, aplicação por tecnologia)?
6. **Rotina.** Que rituais e métricas sustentam a adoção depois do lançamento?
7. **TI.** Como a TI passa de barreira a habilitadora, e de onde sai o orçamento?
8. **Comparação.** Onde agro, bioenergia e florestal estão nessa trajetória, comparados a financeiro, mineração, óleo e gás e farmacêutico?

## 4. Hipóteses de partida

Falas da equipe na reunião de 30/10 e leituras anteriores. Servem para testar, não para afirmar.

1. **Não existe caminho único publicado;** o que existe são evidências convergentes. A nota precisa dizer isso logo no início.
2. **A trajetória recorrente** (hipótese de trabalho, leitura nossa, a datar com casos):

   | Fase | O que acontece | Evidência que já está no catálogo |
   |---|---|---|
   | 0. Alicerce (antes de 2023) | Dados, plataforma e IA preditiva em dores mensuráveis | Jornadas do Rafael; S-03, S-04 |
   | 1. Uso livre e choque de risco | Proibição ou restrição | M1013, M1008, M1044 |
   | 2. Canal oficial único | Assistente para todos; licença não é uso | M517, M334, M326, M1011 |
   | 3. Política com várias ferramentas por perfil | Letramento e liberação em fases | M025, M413, M357, M1012; S-02, S-03 |
   | 4. Champions nas áreas, comitê que prioriza | Registro de uso e custo gerido | M018, M326; S-03, S-04; nota de custo |
   | 5. Valor medido em portfólio | Agentes com limites; regras aplicadas por tecnologia | M072, M1016; bancos §5; S-04 |
3. **Uma ferramenta só não atende a todos:** uma base para todos e ferramentas específicas por perfil. A divisão "70% numa ferramenta e 30% em outras" é fala da equipe, sem fonte: não entra sem estudo que a sustente.
4. **Letramento como condição de acesso** às ferramentas avançadas.
5. **Champions ou builders nas áreas** substituem a área central de IA como motor da adoção, num modelo federado.
6. **A TI trava por falta de orçamento e de patrocínio,** não por vocação. Quando a alta gestão abre uma linha de orçamento, a TI passa a adequar as ferramentas por área.
7. **Medir o retorno depende de governança e de registro de uso,** porque sem registro não há base para a conta.

## 5. Estrutura proposta da nota temática

Arquivo: `03_frente-2_maturidade-roadmaps/roadmap-de-adocao.md`. Entra no assistente: incluir `E-roadmap-de-adocao` em `liberados` no `config/acervo.json` do RAG. Mesmo formato das demais notas: citação [M###, p. N], "leitura nossa", números que não devem ser usados e lacunas.

1. **Resumo em uma página.**
2. **Como ler:** não há caminho único; há uma sequência recorrente, com ritmos diferentes por área (corporativo, indústria, campo).
3. **A trajetória observada (olhar para trás).** Fases com datas, casos de cada fase, o que deu errado e a lição. Ritmo: tempos observados de cada etapa. Base: seção 9 do framework do Rafael e seção 7 da nota de shadow AI.
4. **Os checkpoints por estágio (a régua com pré-requisitos).** Matriz de 5 estágios × 4 dimensões, cada célula com 2 a 4 itens verificáveis (sim ou não) e a evidência pública típica, mais o que precisa existir antes de cada salto. Base: régua do Rafael, seção 6.2 dos frameworks, indicadores de shadow AI e de custo. Exemplo de formato, em estratégia e governança:

   | Salto | Precisa estar de pé (amostra) | Como verificar |
   |---|---|---|
   | 1 → 2 | Patrocinador nomeado; diretriz que diz o que pode e que dado não entra | Diretriz divulgada; responsável nomeado |
   | 2 → 3 | Comitê com mandato; política com percentual treinado; canal oficial para todos com login único e proteção de dados no contrato; orçamento dedicado | Comitê nomeado; política e treinamento com número; dado de uso com unidade e período |
   | 3 → 4 | Governança ligada a riscos e compliance; catálogo de ferramentas aprovadas ou plataforma com vários modelos; uso por fora e custo por área medidos; portfólio gerido por valor | Usuários ativos com critério; total de casos divulgado |
   | 4 → 5 | Regras aplicadas por tecnologia; limites proporcionais à autonomia dos agentes; auditoria de decisões automatizadas; avaliação rápida de ferramenta nova | Rotina de avaliação e auditoria divulgadas |
5. **Quem faz o quê.**
   - Os papéis: patrocinador, comitê, centro de excelência ou área de IA, dono técnico na TI, segurança, jurídico e privacidade, RH e educação, champions, early adopters, dono do caso no negócio e usuário.
   - Os modelos de organização: centralizado, federado, centro de excelência.
   - O papel da TI, com uma matriz de responsabilidade por etapa do fluxo.
6. **O fluxo de implementação.**
   - (a) Caso: ideia registrada → triagem (valor, dados, risco, custo) → piloto com escopo, métrica e critério de parada → decisão de escalar, ajustar ou desligar → produção com dono → medição recorrente.
   - (b) Ferramenta ou modelo novo: pedido com caso de uso → avaliação de segurança, dados e contrato → decisão e perfil de acesso → letramento como condição → liberação com login único e registro → revisão de uso e custo.
7. **Política de uso clara.** O que ela contém, o que a faz funcionar e o que não basta (política sem canal bom nem aplicação por tecnologia). Itens mínimos, cada um com referência pública:
   1. alcance;
   2. ferramentas aprovadas e como pedir outra, com prazo;
   3. classes de dados e o que nunca entra;
   4. só conta da empresa e login único;
   5. revisão humana e responsabilidade por quem assina;
   6. quando dizer que algo foi feito com IA;
   7. propriedade intelectual e confidencialidade;
   8. agentes, conectores e automações: permissões e limites de ação;
   9. criação fora da TI: ambiente isolado, sem dado de produção, revisão antes de publicar;
   10. letramento obrigatório e trilhas por perfil;
   11. registro, monitoramento, incidentes e canal de dúvidas;
   12. consequências, dono e revisão periódica da política.
8. **Rituais e métricas de adoção.**
   - Cadência: comunidade aberta, plantão de dúvidas, vitrine de casos, comitê, painel de uso.
   - Métricas: uso ativo (não licença), uso por fora, custo por área, percentual treinado, casos em produção e retorno.
   - A conta de um caso como método, com exemplo nosso e sem metas inventadas: horas poupadas por execução × frequência × pessoas = horas por ano, mais o que não entra na conta (erro, retrabalho, dependência de uma pessoa).
9. **O campo, uma trilha própria.** Conectividade, dados agronômicos, processamento na borda, autonomia de máquinas e ciclos longos. Base: seção 8 do framework do Rafael, seção 7 dos frameworks e Frente 3. Responde à parte de campo da reunião de 30/10.
10. **O paralelo com outros setores.** Onde financeiro, mineração, óleo e gás e farmacêutico estavam em cada fase, e o agro (jornadas do Rafael, nota dos bancos, ITDBr).
11. **Números que não devem ser usados (ou só com ressalva); Lacunas; Fontes.**

**Regras desta nota:**
- referência de mercado, nunca desenho interno da Acelen;
- não avalia nem recomenda ferramenta: fornecedor só como caso ou fonte rotulada;
- sessões só no agregado;
- caso público de empresa que também deu entrevista entra só como caso público, sem nenhuma ligação com o relato da sessão;
- nada das reuniões com a Acelen.

## 6. A feature no site do assistente

Página **Roteiro de adoção** (`/roteiro`; em inglês, *Adoption roadmap*), na navegação principal ao lado de Metodologia. Segue o padrão da página de metodologia:
- página do servidor com textos em `web/lib/i18n/conteudo/roteiro.ts` (português e inglês);
- componentes com animação (`Revelar`, linha do tempo, trilha de passos);
- citações em link para `/fonte` na página certa.

O conteúdo vem da nota da seção 5, que é a fonte única: a página e o chat dizem a mesma coisa.

```
┌──────────────────────────────────────────────────────────────────────┐
│ ROTEIRO DE ADOÇÃO DE IA                                              │
│ "Não há fórmula mágica; há o que o mercado fez."  [3 números-chave]  │
├──────────────────────────────────────────────────────────────────────┤
│ 1 · A TRAJETÓRIA (olhar para trás)                                   │
│   2023 ──●── 2024 ──●── 2025 ──●── 2026 ──●──▶                        │
│   cada fase: o que as empresas fizeram · o que deu errado · a lição  │
│   · casos com link para a fonte · ritmo observado                    │
├──────────────────────────────────────────────────────────────────────┤
│ 2 · OS CHECKPOINTS (a régua com pré-requisitos)                      │
│        Estratégia  Dados  Pessoas  Aplicações                        │
│   5    [ ]         [ ]    [ ]      [ ]   ← clicar abre a lista do    │
│   4    [ ]         [ ]    [ ]      [ ]     que precisa estar de pé,  │
│   3    [ ]         [ ]    [ ]      [ ]     com a evidência e a fonte │
│   2    [ ]         [ ]    [ ]      [ ]                               │
│   1    [ ]         [ ]    [ ]      [ ]                               │
│   [Onde vocês estão?] autoavaliação só no navegador: nada gravado    │
│   nem enviado ao assistente → estágio por dimensão e os próximos     │
│   checkpoints                                                        │
├──────────────────────────────────────────────────────────────────────┤
│ 3 · QUEM FAZ O QUÊ   cartões dos papéis + matriz por etapa do fluxo  │
├──────────────────────────────────────────────────────────────────────┤
│ 4 · O FLUXO   caso: ideia → triagem → piloto → decisão → produção →  │
│               medição   |   ferramenta nova: pedido → avaliação →    │
│               letramento → liberação por perfil → revisão            │
├──────────────────────────────────────────────────────────────────────┤
│ 5 · POLÍTICA DE USO CLARA   12 blocos clicáveis: por quê, exemplo    │
│               público e fonte · "o que não basta"                    │
├──────────────────────────────────────────────────────────────────────┤
│ 6 · RITUAIS E MÉTRICAS   cadência · matriz "o que medir e de onde    │
│               sai o dado" · conta do caso (calculadora, sem metas)   │
├──────────────────────────────────────────────────────────────────────┤
│ 7 · O CAMPO   trilha própria: conectividade → dados → borda →        │
│               autonomia                                              │
├──────────────────────────────────────────────────────────────────────┤
│ Em cada seção: [Perguntar ao assistente] com perguntas prontas       │
└──────────────────────────────────────────────────────────────────────┘
```

**Regras da página:**
- nada das reuniões (nem "a Acelen pediu");
- a autoavaliação não grava nem envia nada, porque dado interno da Acelen não entra no sistema;
- sem metas numéricas de fornecedor;
- texto novo de interface nos dois idiomas;
- depois de publicar a nota, rodar os pipelines e o `00_numeros.py`, se os números do acervo mudarem.

## 7. Fontes

**Já no catálogo, por bloco** (ponto de partida, a reler na página citada):

| Bloco | IDs |
|---|---|
| Trajetória | M1013, M1008, M1044, M1049, M025, M441, M413, M1001, M437, M1043, M417, M517, M334, M326, M357, M751, M1011, M1012, M1021, M018, M166, M168, M143, M144 |
| Checkpoints | M189, M190, M194, M159, M149, M121, M122, M152, M430, M072, M076, M029, M035, M062, M368 |
| Papéis e TI | M093, M031, M033, M135, M121, M126, M116, M039, M030, M018 |
| Política de uso | M222, M223, M1025, M1000, M197, M456, M423, M1114, M1016, M1023, M110, M1009, M525, M1034, M1051, M1047 |
| Rituais e métricas | M029, M072, M1011, M1012, M1021, M064, M080, M1193, M125 |
| Campo | M368, M270, M179, M290, M279, M215, M081, M082 |

**A levantar (rodada 10 do catálogo):**
1. **As 59 fontes do framework do Rafael sem par no catálogo M:** baixar, conferir e dar ID M (jornadas, comunicados do Gartner de 2026, MIT CISR de 2026, BCG Applied AI Index 2026, Rewired, roteiro de valor de IA da Microsoft, ITDBr do agro, TIC Empresas 2026, AI Act, normas e iniciativas de autonomia agrícola).
2. **Adoção e papéis em material público dos fornecedores,** rotulado como fornecedor:
   - guias de adoção e de programa de champions da Microsoft;
   - o capítulo de governança e de centro de excelência do Cloud Adoption Framework para IA;
   - os equivalentes de Google e AWS (M159 e M149 já estão no catálogo).
3. **Políticas de uso publicadas por governos e reguladores** (Reino Unido, Austrália e Brasil, como guias de IA generativa no setor público e normas do Judiciário), modelos de política de associações profissionais e pesquisas sobre a parcela de empresas com política formal.
4. **Trajetórias datadas de empresas:**
   - da proibição de 2023 à ferramenta interna;
   - da ferramenta única a várias ferramentas;
   - programas de champions com número;
   - comitês com mandato publicado.

   Prioridade para agro, bioenergia e florestal.
5. **Papel da TI e orçamento da IA:** quem paga, linha própria de orçamento, TI como habilitadora.

## 8. Plano

| Quando | O quê | Quem |
|---|---|---|
| 04/11 | Conciliar o framework e a régua do Rafael com o main (F → M); rodada 10 do catálogo (itens 1 a 5 acima) | Rafael (conciliação e jornadas) e agentes de pesquisa |
| 04–05/11 | Nota `roadmap-de-adocao.md`, com verificação | Equipe e agentes |
| 05/11 | Página `/roteiro` no site (versão 1) e par de slides por bloco para a apresentação | Equipe |
| 06/11 | Semanal: mostrar a trajetória, os checkpoints e a página | Guilherme e Rafael |
| 06/11 à tarde ou 09–10/11 | Reunião intermediária pedida pela Acelen, antes do workshop final | Acelen e OagronomIA |

Limite de uso: não rodar mais de três agentes pesados no mesmo bloco de 5 horas; progresso salvo em arquivo para retomar.

## 9. Decisões do Guilherme (04/11/2026)

1. **Base:** o framework e a régua do Rafael de 30/09, pela experiência dele no setor financeiro, com os sinais das quatro sessões executivas para equilibrar com empresas do agro.
2. **Estágio geral:** fica a regra da nota atual, com evidência: o estágio mais alto com evidência em ao menos três das quatro dimensões. A mediana com teto em Dados + 1, da régua do Rafael, não foi adotada.
3. **Autoavaliação na página:** entra, só no navegador.
4. **Nome da página:** "Roteiro de adoção".
5. **Trilha do campo:** vai para a Frente 3.
6. **Ata da semanal de 30/10:** feita (BIA-ACL-AT-04, rev. 00).

**Como ficou (04/11):**
- **Catálogo:** as fontes do Rafael entraram na rodada 10 (M1199 a M1252; 1.252 fontes no total). 45 delas têm cópia guardada. As 9 sem cópia (bloqueadas, pagas ou fora do ar) ficam marcadas, e os números delas não entram na nota até serem salvos à mão.
- **Nota:** [roadmap-de-adocao.md](roadmap-de-adocao.md), conferida linha a linha.

## 10. Fora deste tema

- **Edição genética com IA no melhoramento da macaúba** (pergunta de 1:11:06 na reunião): registrar como pergunta para a Frente 3, como tendência de IA em pesquisa e melhoramento.

## 11. Números que não devem ser usados (ou só com ressalva)

- **Metas dos slides do evento** (horas por mês por usuário, percentual de licenças com uso ativo, percentual que escreve o próprio prompt, casos por trimestre): sugestões comerciais do parceiro, sem base divulgada.
- **"70% numa ferramenta e 30% em outras":** fala da equipe na reunião, sem fonte.
