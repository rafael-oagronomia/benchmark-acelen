# Shadow AI e governança — nota temática

> Documento de trabalho da OagronomIA · Frente 2 — Maturidade e roadmaps (com Frentes 1 e 3) · Fontes públicas do catálogo · Data de corte: 15/10/2026 · Entrega parcial em revisão — não encaminhar ao cliente sem revisão.

**Como ler.** [M###, p. N] é o item M### do catálogo e a página N do PDF; [M###, web], item só na web. Cada número diz de quem é e o que mede; dado de fornecedor de segurança ou de IA vem marcado. "Cálculo nosso" marca conta da equipe; "leitura nossa", interpretação. Ferramentas e preços são dado de mercado: a nota não recomenda fornecedor nem desenha a solução interna do cliente. Protocolo: [linha de investigação](shadow-ai-linha-de-investigacao.md).

**Termos.** *Shadow AI*: uso de IA no trabalho por fora dos canais aprovados, em geral com conta pessoal. *Licença* ou *assento*: direito de uso comprado por pessoa; não mostra se ela usa. *Microsoft 365 Copilot*: licença paga, dentro dos aplicativos da suíte; *Copilot Chat*: chat corporativo sem custo adicional para clientes da suíte [M1033, p. 2]; em 2026, viraram Microsoft Copilot e Microsoft Copilot Chat [M1032, p. 1]. *Login único* (SSO): entrar com a conta da empresa; *provisionamento* (SCIM): criar e remover usuários pelo cadastro central. *Prevenção de vazamento* (DLP): detectar ou bloquear dado sensível que sai. *Vibe coding*: pedir a um agente de IA, em linguagem comum, que construa um aplicativo com bastante autonomia, avaliando o resultado sem necessariamente ler o código [M1047, p. 1-2]. *Desenvolvedor cidadão*: quem cria aplicativos sem ser da TI [M1051, p. 1].

## 1. Resumo em uma página

- **Sim, o shadow AI é grande.** Na medição de tráfego da Netskope, fornecedora de segurança, 47% dos usuários de IA generativa usavam aplicativos pessoais em out/2025 [M1049, p. 2]; na telemetria do Verizon, que também vende segurança, 67% dos usuários de plataformas de IA usavam contas não corporativas em dispositivos da empresa em 2025, outra base [M1068, p. 60]. No Brasil, 74% dos usuários de IA levavam a própria ferramenta ao trabalho em 2024 (pesquisa de opinião da Microsoft, que vende o Copilot, e do LinkedIn) [M1042, p. 32].
- **A conta pessoal recua, mas a oficial não basta.** Na Netskope, a parcela com aplicativos pessoais caiu de 78% para 47% em um ano, enquanto a de contas da empresa subiu de 25% para 62%, sem prova de causa [M1049, p. 2-3]; numa pesquisa do Gartner, 88% dos que têm IA da empresa também usam a pessoal [M1018, web].
- **Por quê: hábito, preferência por escolher, falta de ferramenta boa, pressa e regras confusas** (seção 4). Numa pesquisa de opinião da Software AG, fornecedora de software, 53% dizem usar a própria ferramenta por preferir escolher, e 33% porque a TI não oferece a que precisam [M1062, p. 2].
- **A hipótese de partida se confirma em parte.** A base é Microsoft, o ChatGPT chegou antes e a maioria dos que usam IA recorre a ferramentas públicas; mas o Copilot lidera a aprovação nas grandes empresas americanas e a base instalada no Brasil, o Claude fica bem atrás, e a marca não é a causa mais citada (seção 11).
- **O risco tem custo estimado.** No relatório de 2025 da IBM, que vende segurança, uma em cada cinco das 600 organizações com vazamento relatou vazamento por shadow AI, e as com nível alto de shadow AI tiveram custo médio US$ 670 mil maior que as de nível baixo ou nenhum [M1023, web].
- **Proibir funciona pouco, e regra rígida não zera o uso por fora.** Na proibição nacional do ChatGPT na Itália, a parcela de buscas sobre VPN no Google subiu 52,2 pontos percentuais no primeiro dia útil [M1044, p. 11]. No Brasil, 64% dos executivos de empresas com políticas rígidas, treinamento obrigatório e ferramentas homologadas percebem possível uso por fora, contra 75% nas empresas sem regras claras (Peers e TEC.Institute, via imprensa) [M1009, p. 2]. Falta estudo que compare os caminhos.
- **Impor o Copilot não resolve sozinho: licença não é uso.** A Microsoft declara mais de 30 milhões de licenças pagas, sem dizer quantas são usadas [M1038, p. 3]. Num ministério britânico, cerca de 30% dos licenciados usaram a ferramenta por dia útil e 64% por semana [M1011, p. 16]; no Tesouro australiano, os participantes a viram como inferior a ChatGPT e Claude, em parte pelas restrições de segurança do órgão [M1012, p. 7, 27].
- **Há caminhos além do Copilot, com governança descrita pelas empresas, sem resultado medido.** Só 27% das grandes empresas americanas têm uma única plataforma principal de IA (Morning Consult) [M1045, p. 3]; bancos usam várias ferramentas ou plataforma própria de vários modelos [M413, p. 6; M437, p. 16]; e a Microsoft passou a oferecer modelos da Anthropic no Copilot [M1035, p. 2-3].
- **O custo adequado não tem prova pública.** Em 15/10/2026, a tabela de entrada ia de US$ 20 a 30 por usuário/mês: US$ 30 no Copilot, que exige a suíte (R$ 171,80 no Brasil, sem impostos, no pagamento anual), e US$ 20 ou 25, na cobrança anual ou mensal, no ChatGPT Business e no Claude Team, com teto de vagas [M1037, p. 4; M1036, p. 5; M1053, p. 1; M1002, p. 2-3]. Os planos para grandes empresas não têm preço público ou cobram o uso à parte [M1053, p. 2; M909, p. 11].
- **Vibe coding com segurança: supervisão conforme o risco.** Para o NCSC, agência britânica de segurança cibernética, em post do seu arquiteto principal de segurança, o vibe coding pleno muitas vezes é aceitável em protótipos e ferramentas internas sem dados sensíveis; autenticação, dados pessoais e credenciais pedem revisão do código [M1047, p. 1-2]. Há incidentes documentados [M1046, p. 1; M1030, p. 1; M1064, p. 1] e nenhum caso de grande empresa com resultado medido.
- **Leitura nossa.** Os casos apontam para canal oficial rápido e bom, com uma ou várias ferramentas, login único, proteção de dados, registro de uso, treinamento e caminho para levar protótipos à produção. Propomos um indicador para a régua da Frente 2 (seção 12).

## 2. A pergunta e a hipótese de partida

**Perguntas do protocolo.** (1) Por que o shadow AI cresce? (2) O que as empresas fazem para sair dele — impor a ferramenta da casa (no Brasil, quase sempre o Copilot), liberar outras com governança, proibir ou combinar — e o que dá resultado? (3) Há como usar outras ferramentas com governança, segurança e custo adequado? (4) Como usar com segurança as ferramentas de prototipação com IA?

**Hipótese de partida.**
1. Cerca de 90% das empresas usam a Microsoft como base de gestão e governança da organização.
2. O Copilot perdeu a corrida inicial da IA, e a maioria das pessoas foi para outras ferramentas, principalmente ChatGPT e Claude.
3. Por isso o shadow AI ganhou tração: a ferramenta oficial é a Microsoft, e a preferida está fora dela.

**Hipóteses concorrentes** (H2 a H7): com o veredito, na seção 11.

**Contexto e método.** O tema apareceu nas sessões executivas, e governança é a dimensão mais atrasada nas fichas do painel (leitura nossa). O dossiê tem 258 evidências de 90 itens do catálogo, conferidas na fonte; os números do resumo, das tabelas e do veredito foram reconferidos nas páginas citadas.

## 3. O tamanho do shadow AI

Há medições (tráfego ou eventos na clientela de um fornecedor de segurança) e pesquisas de opinião. Cada linha vale por si.

| Fonte | O que mede | Amostra e período | Resultado |
|---|---|---|---|
| Netskope (fornecedora de segurança) | Tráfego: usuários de IA generativa com aplicativo pessoal | Clientes, out/2024–out/2025 | 47% (78% um ano antes) [M1049, p. 2, 12] |
| Verizon DBIR (vende serviços de segurança) | Telemetria: contas usadas para acessar IA em dispositivos da empresa | 2025 | 67% com conta não corporativa (72% um ano antes) [M1068, p. 60] |
| PagerDuty (fornecedora de software) | Uso de IA achando que a política não permitia | 1.250 profissionais de escritório fora da TI, em empresas com receita de US$ 500 milhões ou mais; EUA, Reino Unido, Austrália e Japão; 2026 | 66% [M1054, p. 1-3] |
| Gartner | Quem tem IA da empresa e usa também a pessoal | 12.004 funcionários e gestores, 40 países, 1º tri/2026 | 88% [M1018, web] |
| Universidade de Melbourne e KPMG | Como os empregados que usam IA acessam as ferramentas (respostas múltiplas) | 48.340 pessoas (32.352 empregadas), 47 países, com o Brasil, nov/2024–jan/2025 | 70% públicas gratuitas; 42% do empregador [M110, p. 15, 73, 109] |
| Microsoft (vende o Copilot) e LinkedIn | Usuários de IA que levam a própria ferramenta | 31.000 trabalhadores do conhecimento, cerca de mil em cada um de 31 mercados, fev–mar/2024 | 78% no mundo; 74% no Brasil [M1042, p. 7, 27, 32] |
| MIT NANDA, via Fortune (imprensa) | Empresas, não pessoas | 52 organizações e 153 líderes, 2025 | 40% compraram assinatura oficial; em mais de 90%, há uso pessoal [M1014, p. 4] |
| Thomson Reuters (vende IA para essas profissões) | Uso de IA não aprovada | 1.816 profissionais do jurídico, tributário, contábil, compliance e risco; 62 países; mar–abr/2026 | Um terço [M1065, p. 3, 5] |
| Peers e TEC.Institute, via Convergência Digital (imprensa) | Percepção de executivos brasileiros | 120 respondentes, 2026 | 66% admitem possível uso sem aval [M1009, p. 1-2] |
| Thomson Reuters Brasil, via TI Inside (imprensa; recorte contestado) | Uso sem autorização | Amostra não informada, 2026 | 38% [M1063, p. 1] |

**Leitura.** Bases e perguntas diferem; os números vão de um terço (Thomson Reuters) a quase nove em dez (Gartner), e nenhuma fonte aponta uso por fora residual (leitura nossa). O recorte brasileiro da Thomson Reuters é contestado: a Forbes Brasil escreveu, em jun/2026, que o relatório não traz dados do Brasil [M1074, web], o release oficial não o tem, e os números de clientes atribuídos ao Brasil são iguais aos globais [M1063, p. 1; M1065, p. 2, 4]. Na pesquisa da Microsoft, cujo recorte brasileiro tem cerca de mil pessoas, os brasileiros dizem usar mais IA generativa no trabalho que a média (83% contra 75%) [M1042, p. 30].

## 4. Por que acontece

- **Hábito e preferência por escolher.** 89% dos que usam IA no trabalho a conheceram na vida pessoal (PagerDuty) [M1054, p. 2]. Na Software AG, fornecedora de software (6.000 trabalhadores do conhecimento nos EUA, Reino Unido e Alemanha, set/2024), o motivo mais citado para usar a própria ferramenta é preferir escolher (53%) [M1062, p. 2]. Muitos já usavam o ChatGPT em casa quando a Microsoft começou a vender o Copilot, e as novidades da OpenAI demoravam semanas para chegar a ele, segundo pessoas ouvidas pela Bloomberg (imprensa) [M1005, web].
- **Ferramenta oficial ausente ou pior.** Na mesma pesquisa, 33% usam a própria ferramenta porque a TI não oferece a que precisam [M1062, p. 2]. Na Thomson Reuters, 41% não têm acesso a ferramentas profissionais que protejam dados confidenciais e deem resultados verificáveis [M1065, p. 3]. Para a Netskope, o aumento de quem alterna entre conta pessoal e corporativa (de 4% para 9%) indica que a ferramenta da empresa ainda não é conveniente o bastante [M1049, p. 3].
- **Pressa.** Para o Gartner, quem tem IA da empresa usa também a pessoal muitas vezes para ganhar tempo [M1018, web]. A Microsoft chama a sobrecarga de "outro motor": 68% têm dificuldade com o ritmo e o volume de trabalho (leitura da empresa, sem teste de causa) [M1042, p. 9].
- **Regras ausentes ou confusas.** Só cerca de dois em cada cinco empregados dizem que a organização tem política sobre IA generativa, e 19% não sabem [M110, p. 73]. Nas entrevistas de um ministério britânico, muitos dos que tinham dúvida sobre as regras relataram cautela excessiva, o que limitou o uso da ferramenta oficial [M1011, p. 34].
- **Governança lenta ou rígida.** O uso não aprovado chega a 41% entre quem acha a empresa lenta em IA, contra um terço na média (associação) [M1065, p. 3]. Num relatório da MIT Technology Review Brasil, da Peers e do TEC.Institute, os autores avaliam que controles rígidos demais podem estimular usos informais e que regras só declaratórias não chegam ao dia a dia [M018, p. 29].

**Leitura nossa.** As causas se somam; a marca pesa quando a ferramenta oficial é pior, como no Tesouro australiano (seção 6). O Gartner recomenda melhorar a experiência das ferramentas corporativas para reduzir o shadow AI [M1018, web].

## 5. Risco e custo

**O que sai.** Na PagerDuty, 88% compartilharam informação de trabalho com ferramentas públicas de IA, e 34%, dados de clientes [M1054, p. 2]. As medições confirmam:
- Na Netskope, as violações de política de dados ligadas a IA generativa dobraram em um ano, para 223 por mês na organização média da clientela, contando só as detectadas; os dados mais envolvidos foram código-fonte (42%), dados regulados (32%) e propriedade intelectual (16%) [M1049, p. 5].
- No Verizon, o shadow AI virou em 2025 a terceira ação não maliciosa de funcionários mais detectada pelo seu serviço de prevenção de vazamento, quatro vezes mais que um ano antes [M1068, p. 60].
- Na Harmonic, fornecedora de controle de uso de IA, 8,5% dos prompts tinham dados sensíveis, e 63,8% dos usuários do ChatGPT estavam no plano gratuito (4º tri/2024) [M1022, p. 2, 7].

**Quanto custa.** No relatório de 2025 da IBM, feito pelo Ponemon Institute com 600 organizações que sofreram vazamento entre mar/2024 e fev/2025 (a IBM vende segurança), uma em cada cinco relatou vazamento por shadow AI; as com nível alto de shadow AI tiveram custo médio US$ 670 mil maior que as de nível baixo ou nenhum, e esses incidentes expuseram mais dados pessoais (65% contra 53% na média) e propriedade intelectual (40% contra 33%) [M1023, web]. Os números de 2026 só aparecem via terceiro: um resumo do escritório Baker Donelson diz que os incidentes com shadow AI subiram para 43%, contra 20% em 2025, e custaram US$ 5,39 milhões, "contra US$ 4,63 milhões", sem dizer a base nem a comparação [M1004, p. 2]. No release oficial de 2026, um vazamento qualquer custou em média US$ 5,2 milhões no setor de energia [M1024, web].

**LGPD.** A ANPD, autoridade de proteção de dados, lembra que usuários podem anexar a essas ferramentas documentos confidenciais, laudos médicos e atas [M1003, p. 23]; para sua equipe técnica, no desenho dos sistemas, transferir ao usuário a responsabilidade pela proteção dos dados pessoais não parece suficiente (estudo sem posição institucional) [M1003, p. 24]. O catálogo não traz caso brasileiro de sanção.

**A ferramenta oficial também traz risco.** Em palestra relatada pela imprensa, um vice-presidente do Gartner disse que mitigar riscos ao implantar o Microsoft 365 Copilot exigiu esforço "significativamente maior" que o planejado, por excesso de conteúdo, compartilhamento indevido e governança fraca do Microsoft 365, o que muitas vezes pede licenças e ferramentas extras e eleva o custo total [M1073, p. 2]. O governo britânico nota que o Copilot pode expor arquivos a que o usuário tem acesso sem dever ter [M1021, p. 4].

## 6. Copilot × outras ferramentas: licença não é uso

**O que a Microsoft divulga** (declarações da empresa, que vende o Copilot):
- **Licenças pagas:** 15 milhões em jan/2026, mais de 20 milhões em abr/2026 e mais de 30 milhões em jul/2026 [M1039, p. 4; M1040, p. 3; M1038, p. 3]. Em jan/2026, eram cerca de 3% dos mais de 450 milhões de assentos comerciais pagos do Microsoft 365 (cálculo nosso), base que cresce sobretudo em pequenas e médias empresas e trabalhadores de linha de frente [M1039, p. 6].
- **Uso:** só indicadores relativos, como usuários ativos diários 10 vezes maiores em um ano [M1039, p. 4]. A empresa chama de "alto uso" o uso ativo mensal acima de 80% da base do cliente, sem dizer quantos clientes chegam lá [M1038, p. 4].
- **Agro:** a Bayer se comprometeu com 90 mil ou mais licenças e tem plataforma própria de agentes, feita no Foundry, da Microsoft, com vários modelos e mais de 20 mil usuários ativos por mês [M1040, p. 2-3].

**O que dizem decisores e tráfego** (aprovação ou presença na empresa, não uso pelos funcionários):

| Fonte | Amostra e período | O que mede | Resultado |
|---|---|---|---|
| FGVcia | Médias e grandes empresas brasileiras, 2024/25 | Participação na base instalada de IA generativa | Copilot 40%, ChatGPT 32%, Gemini 20% [M209, p. 130] |
| Morning Consult | 500 decisores de empresas dos EUA com 5 mil ou mais funcionários, jul/2026 | Aprovado ou em uso em algum lugar da organização | Copilot 73%, Gemini 47%, ChatGPT Enterprise 44%, Claude 20%; em empresas de todos os portes, Gemini 55%, ChatGPT 48%, Copilot 45% [M1045, p. 1, 3] |
| Netskope (tráfego) | Clientes, out/2024–out/2025 | "Adoção", sem base definida | ChatGPT 77%, Gemini 69%, Microsoft 365 Copilot 52% [M1049, p. 4] |

**O uso medido.** Só as avaliações de governo medem uso entre licenciados, cada uma com um critério:

| Avaliação | Alcance | Critério | Uso | Resultado |
|---|---|---|---|---|
| Ministério de Negócios e Comércio (DBT), Reino Unido | 1.000 licenças, out–dez/2024 | Ao menos um uso no dia ou na semana, pelo painel da Microsoft, sem descontar ausências | 21% por dia (30% sem fins de semana e feriados); 64% por semana | Sem evidência de que a economia de tempo virou produtividade [M1011, p. 4-5, 16] |
| Experimento entre ministérios (GDS), Reino Unido | 20 mil licenças em 12 organizações, inclusive as do DBT, 30/09–31/12/2024 | Ao menos uma interação em 30 dias (dados de 14.500 usuários) | Cerca de 80% | Economia autodeclarada de 26 minutos por dia [M1021, p. 3-5, 7, 11] |
| Tesouro, Austrália | 218 participantes, mai–ago/2024 | Frequência autodeclarada (136 respostas) | 22% usavam 4 a 5 vezes por semana ou mais | 59% (100 respostas) disseram que ajudou a fazer melhor até um quarto da carga semanal [M1012, p. 6, 18, 20] |

Os três não se somam nem se comparam, como o próprio DBT adverte [M1011, p. 40]. Para um vice-presidente do Gartner, o padrão da Microsoft conta um uso em 28 dias; ele consideraria um uso por semana, "conservadoramente", e provavelmente um por dia para justificar a licença (imprensa) [M1073, p. 3].

**Casos.** A Amgen anunciou em 2024 planos de contratar o Copilot para 20 mil funcionários; 13 meses depois, eles usavam o ChatGPT, e o Copilot ficava mais para Outlook e Teams, segundo a Bloomberg (imprensa; sem documento da empresa) [M1005, web]. O relatório do Tesouro australiano atribui parte da desvantagem percebida diante de ChatGPT e Claude às restrições de segurança do órgão e não sabe se essas alternativas as atenderiam [M1012, p. 7, 27].

**A Microsoft abre o Copilot a outros modelos.** Desde set/2025, oferece modelos da Anthropic no Copilot, mantendo os da OpenAI como base [M1035, p. 2-3]. A Anthropic atua como subprocessadora, sob o contrato da Microsoft, salvo nos modelos "com retenção de dados", que vêm desligados [M1032, p. 1, 5-6]; os demais vêm ligados por padrão fora da Europa, inclusive no Brasil, ficam fora dos compromissos de processamento no país, e o administrador pode limitar o acesso por grupo [M1032, p. 1-2, 4]. Leitura nossa: escolher entre o Copilot e outra ferramenta passa a ser também escolher modelo e contrato.

## 7. Os caminhos das corporações

**Proibir** foi comum em 2023: a Samsung proibiu depois que um engenheiro enviou código-fonte interno ao ChatGPT, e o JPMorgan Chase restringiu a ferramenta (Forbes, com base na Bloomberg) [M1013, p. 1-2]; num estudo da Cisco, fornecedora de segurança, com 2.600 profissionais de privacidade e segurança, 27% das organizações tinham proibido a IA generativa ao menos por um tempo [M1008, p. 22]. Hoje, 90% das organizações na clientela da Netskope bloqueiam algum aplicativo de IA, em média 10, sobretudo os vistos como de risco [M1049, p. 6]; na Zscaler, também fornecedora de segurança, a parcela de transações de IA bloqueadas caiu de 59,9% para 39% de 2024 para 2025, sem explicação [M1071, p. 2; M1072, p. 3]. Para **a ferramenta única da casa**, a Microsoft propõe chat corporativo para todos e licença paga para parte dos usuários (projeção comercial) [M1033, p. 2]. **Várias ferramentas** são a regra nas grandes empresas americanas: cerca de metade mantém lista curta de aprovadas (Morning Consult) [M1045, p. 3]. **Plataformas internas** e **combinações** aparecem nos casos abaixo, declarados pelas empresas, salvo indicação.

| Empresa | Caminho | Alcance | Controles descritos | Resultado divulgado | Fonte |
|---|---|---|---|---|---|
| JPMorganChase | Plataforma própria com modelos de terceiros | Quase 250 mil com acesso (banco todo); mais de 65 mil em uso ativo, só no banco comercial e de investimento | Adesão voluntária, liberação em fases, treinamento; segurança de dados em primeiro lugar | Sem critério de uso ativo | [M025, p. 3-4; M441, p. 64] |
| BBVA | Várias ferramentas | ChatGPT Enterprise a estender a mais de 120 mil; Gemini habilitado para mais de 87 mil; 15 mil licenças de GitHub Copilot | "Ambiente corporativo seguro" | Acesso ou licença | [M413, p. 5-6] |
| Deloitte | Ferramenta fora da Microsoft | Claude disponível para mais de 470 mil pessoas | Centro de excelência e certificação de 15 mil profissionais, também para atender clientes | Não divulgado (anúncio do fornecedor) | [M1001, p. 1-2] |
| Itaú | Plataforma interna com vários modelos | Mais de 56 mil usuários das plataformas de IA generativa, sem critério | Acesso padronizado a mais de 80 modelos, escolhidos por acurácia e custo (imprensa); segurança e governança | Corte de 65% no gasto com IA generativa desde 2022, só na imprensa | [M437, p. 16; M1043, p. 1-2] |
| Banco do Brasil | Plataforma interna e catálogo | Não informado | Catálogo com avaliação de risco; ambiente para criar assistentes; restrição com dados sensíveis | Não divulgado | [M417, p. 1-3] |
| Petrobras | Plataforma própria, feita com a Microsoft, e teste do Copilot | 1,2 milhão de interações até jun/2024; 250 usuários ativos no teste | Não descritos | Não divulgado | [M517, p. 7] |
| Suzano | Copiloto corporativo feito com a Microsoft | Quase 50 mil colaboradores, 2024 | Restrito ao ambiente interno | Sem número de usuários ativos | [M334, p. 6] |
| Klabin | Copilot para todos, com comitê | Todos os colaboradores; não diz se é o chat ou a licença paga | Comitê com a área de Privacidade; critérios para o colaborador criar agentes; treinamento | Não divulgado | [M326, p. 63-65, 74] |
| São Martinho | Política e soluções homologadas | Público elegível | 99% do público elegível treinado na política | Não divulgado | [M357, p. 46] |

**O que dá resultado** (leitura nossa):
- Nenhum caso mostra, com método, a queda do uso por fora depois da mudança; o mais perto disso é a coincidência medida pela Netskope (seção 3).
- Os casos com mais governança descrita combinam plataforma, vários modelos, liberação em fases e treinamento; fases e treinamento são também o que recomendam as avaliações de governo [M1012, p. 47-48; M1021, p. 22].
- Proibir sem alternativa tende a ser contornado. Na Itália, numa proibição nacional, os usuários contornaram o bloqueio em dias [M1044, p. 13]; numa pesquisa de fornecedor, 46% dizem que não largariam as ferramentas pessoais nem sob proibição [M1062, p. 1]; e o envio de dados sensíveis a IA pública é mais comum onde a IA é proibida (67%) ou tem política de uso (56%) do que onde não há política (33%), em comparação entre grupos, com o da proibição reunindo 6% dos empregados [M110, p. 73, 77].
- Nem regras rígidas com ferramentas homologadas zeram o uso por fora percebido por executivos brasileiros [M1009, p. 2].

## 8. Os controles que aparecem nos casos e nas referências

| Controle | Para que serve | Exemplos e referências |
|---|---|---|
| Política de uso | Dizer o que pode e que dado não entra | A ANBIMA, associação do mercado financeiro, pede deixar claro se "sistemas paralelos de IA" são admitidos e como [M1000, p. 16]; o NIST, instituto de padrões dos EUA, política de uso aceitável que cubra ferramentas abertas e terceiros [M223, p. 25] |
| Login único e provisionamento | Uma identidade da empresa | Nos planos corporativos de ChatGPT e Claude [M1053, p. 2; M1002, p. 1] |
| Proteção de dados no contrato | Sem treino com os dados; retenção e local de processamento definidos | A residência de dados do ChatGPT Enterprise cobre dez regiões, sem o Brasil [M1053, p. 8]; a ANBIMA pede avaliar fornecedor e contrato [M1000, p. 16] |
| Prevenção de vazamento | Barrar dado sensível que sai | Na clientela da Netskope, metade das organizações não aplica por tecnologia a proteção de dados na IA generativa [M1049, p. 5] |
| Descoberta do uso por fora | Saber que IA se usa e com que dado | Ferramenta da Microsoft (versão clássica, já substituída) registra visitas a sites de IA de terceiros, com extensão de navegador [M1041, p. 1, 4]; o NIST sugere inventário de sistemas e lista de fornecedores aprovados [M223, p. 20, 25] |
| Registro e auditoria | Rastrear uso | Planos empresariais [M909, p. 12]; na IBM 2025, só 34% das organizações com vazamento e política de IA auditavam o uso não autorizado [M1023, web] |
| Treinamento | Uso seguro e útil | 35% dizem que o empregador não oferece treinamento (Software AG) [M1061, p. 7]; a ANBIMA pede treinar e manter canal de dúvidas [M1000, p. 16] |
| Comitê e sistema de gestão | Avaliar ferramentas e riscos | A ISO/IEC 42001 traz requisitos de sistema de gestão de IA, também para quem só usa IA (página oficial; norma paga, não lida) [M1025, p. 1-2] |

**Política sozinha não basta.** Para o Gartner, é preciso passar de políticas e treinamento a regras aplicadas por tecnologia, com inventário da IA e monitoramento contínuo (avaliação de analista, sem dados) [M1016, p. 2, 4]. Na IBM 2025, só 37% das organizações com vazamento tinham políticas para gerir IA ou detectar shadow AI [M1023, web].

## 9. Custo por usuário das opções corporativas

Preço de tabela por usuário e por mês, sem desconto de contrato.

| Opção | Preço | Condição | Consulta | Fonte |
|---|---|---|---|---|
| Microsoft 365 Copilot, Brasil | R$ 171,80 (anual) ou R$ 180,39 (mensal, com compromisso anual) | Sem impostos; exige plano qualificado do Microsoft 365 | 15/10/2026 | [M1036, p. 1, 5] |
| Microsoft 365 Copilot, EUA | US$ 30,00 (anual) ou US$ 31,50 (mensal, com compromisso anual) | Exige plano qualificado do Microsoft 365; a página não fala de impostos | 15/10/2026 | [M1037, p. 4-5] |
| Microsoft 365 Copilot Chat | Sem custo adicional para clientes comerciais do Microsoft 365; agentes por consumo | Com proteção de dados empresariais | Anúncio de jan/2025 | [M1033, p. 2, 4] |
| ChatGPT Business | R$ 100, ao lado de "$20" (anual) e "$25" (mensal) | De 2 a 200 funcionários; sem dados de impostos nem da conversão | 15/10/2026 | [M1053, p. 1-2] |
| ChatGPT Enterprise | Não publicado | Preço por créditos ou tokens | 15/10/2026 | [M1053, p. 2] |
| Claude Team | Vaga padrão a US$ 20 (anual) ou US$ 25 (mensal) | De 2 a 150 vagas; preço para clientes dos EUA, sem impostos | 15/10/2026 | [M1002, p. 2-3] |
| Claude Enterprise | US$ 20 por assento, mais o uso a preço de API | Cobrança anual; sem dados de impostos | 14/10/2026 | [M909, p. 11-12] |
| Google Workspace com Gemini, Brasil | Starter R$ 40,90; Standard R$ 81,80; Plus R$ 128,40 (contrato anual, cobrança mensal) | Suíte completa; Gemini limitado no Starter; Starter e Standard até 300 usuários; sem dados de impostos | 15/10/2026 | [M1019, p. 1-2, 4-5, 7] |
| Google Workspace Enterprise | Não publicado | Contato com vendas | 15/10/2026 | [M1019, p. 3] |

**Ressalvas.**
- **Bases diferentes.** O Copilot é complemento da suíte; o Gemini vem dentro dela; ChatGPT e Claude são assinaturas à parte, com teto de vagas nos planos de entrada; o Claude Enterprise soma o uso. Em dólar, a licença do Copilot custa mais que essas vagas (cálculo nosso).
- **Impostos e câmbio.** Só a Microsoft no Brasil e o Claude Team dizem que o preço não inclui impostos; as demais páginas não tratam do tema. A página brasileira da Microsoft exibia aviso de evento passado, sinal de atualização irregular [M1036, p. 1]. Os preços em dólar herdam o câmbio.
- **Custo além da licença.** No Tesouro australiano, o avaliador estimou que um servidor de nível médio teria de redirecionar 13 minutos por semana para pagar a licença e julgou provável que os ganhos compensem, sem medir o tempo [M1012, p. 7, 47]; o DBT não publicou a análise de custo-benefício [M1011, p. 14]; preparar o ambiente pode pedir licenças e ferramentas extras (seção 5). Nas grandes empresas americanas, o custo total é o 8º de 12 critérios de escolha, atrás de qualidade, segurança e conformidade [M1045, p. 7].

## 10. Vibe coding com governança

**Adoção.** O Lovable alcançou funcionários de quase dois terços das empresas da Fortune 500, e o Replit, de 85%: presença de usuários, não contratos (dados dos fornecedores) [M1031, p. 2; M1058, p. 3]. Na Nutanix, fornecedora de infraestrutura, 79% dos executivos de nuvem, TI e engenharia no mundo e 74% no Brasil já acharam aplicações ou agentes de IA implantados por funcionários de fora da TI, sem dizer com que ferramenta (nov/2025; recorte de 100 executivos, via imprensa) [M1050, p. 2; M1026, p. 2, 4].

**Incidentes.**
- **Lovable, 2025.** O registro CVE-2025-48757, do cadastro público de falhas de segurança, descreve regra de acesso ao banco de dados insuficiente nos sites gerados até 15/04/2025, que permitia ler ou gravar tabelas sem login; a nota 9,3, crítica, é da MITRE, que administra o cadastro, sem avaliação própria da base do governo americano [M1046, p. 1-2]. O Lovable contesta: diz que cada cliente responde pelos dados do seu aplicativo [M1046, p. 1]. Os pesquisadores acharam a falha em 170 de 1.645 projetos da vitrine do Lovable, só nas páginas iniciais [M1055, p. 3-5], e, na notificação formal, indicam como organização o Replit, concorrente do Lovable [M1055, p. 12].
- **Lovable, 2026.** Entre 03/02 e 20/04/2026, o histórico de chat e o código de projetos públicos podiam ser vistos por qualquer usuário logado com o link, e a empresa admitiu que a primeira resposta foi "desdenhosa" [M1030, p. 1-2]. Segundo a empresa, clientes Enterprise já não criavam projetos públicos desde mai/2025, e os demais só passaram a ter projetos privados por padrão em nov/2025 [M1030, p. 3, 6].
- **Replit, 2025.** Um usuário relatou que o agente apagou um banco de produção e inventou dados (imprensa) [M1064, p. 1]. O Replit usava o mesmo banco para desenvolvimento e produção e anunciou, dias depois, bancos separados, em beta para aplicativos novos [M1056, p. 1-2].

**Segurança do código.** Na Veracode, fornecedora de segurança de aplicações, o código de mais de 100 modelos trouxe, em 45% dos testes, falhas da lista OWASP Top 10, as mais críticas em aplicações web; foram 80 tarefas escolhidas por terem risco, avaliadas com a ferramenta da própria empresa [M1066, p. 1, 3]. No SusVibes, da Carnegie Mellon e outras (versão 2 do artigo no repositório arXiv, fev/2026), a combinação de agente e modelo com mais acertos funcionais resolveu 61% das 200 tarefas, mas só 10,5% de forma correta e segura, e dicas sobre a vulnerabilidade não ajudaram [M1007, p. 1, 9, 12-13]; há versão mais nova, com 186 tarefas, nos anais da conferência ICML 2026, não baixada.

**Controles por plano** (documentação dos fornecedores, out/2026):

| Ferramenta | Identidade e auditoria | Dados no treino | Publicação e outros controles | Fonte |
|---|---|---|---|---|
| Lovable | Login único no Business e no Enterprise; auditoria só no Enterprise | Fora por padrão no Business e no Enterprise | Varredura a cada publicação; bloqueio por dado pessoal só no Enterprise | [M1028, p. 2-3, 5, 7] |
| Replit | Login único e auditoria no Enterprise | O Enterprise fica fora; o Pro entra, salvo recusa | Admin pode exigir publicação privada e varredura | [M1057, p. 2-3, 9] |
| Cursor | Login único no Teams e no Enterprise; auditoria só no Enterprise | Fora por padrão no Enterprise, pelo modo de privacidade | Por padrão, comandos do agente liberados por revisão automática, com classificador de IA; residência de dados só nos EUA, 10% mais cara | [M1010, p. 4-5, 8, 11-12, 14] |
| Bolt | Login único e auditoria só no Enterprise, preço sob consulta | Não informado | Varredura do banco e controle de onde publicar no plano de equipes; permite ligar bancos de produção ao projeto | [M1006, p. 3-5, 13] |
| v0 | Login único e auditoria no Enterprise | Padrão pouco claro | Código gerado roda isolado | [M1067, p. 2-4] |

**Modelo por nível de risco do NCSC** (post do seu arquiteto principal de segurança) [M1047, p. 1-3]:

| Posição | Quando | Supervisão |
|---|---|---|
| Vibe coding pleno | Protótipos, demonstrações e ferramentas internas de pouca exposição, sem dados sensíveis nem funções de segurança | Leve |
| Lado manual | Autenticação e autorização, dados pessoais sensíveis, segredos e credenciais, sistemas críticos | Revisar e entender o código, checar vulnerabilidades, verificar o comportamento |

Quando o risco se desloca para o vibe coding pleno, o NCSC sugere considerar os requisitos básicos de segurança do ETSI, órgão europeu de normas, para sistemas de IA [M1047, p. 3]. Em blog, o CTO de Arquitetura do NCSC nota que o software como serviço em geral exige planos caros até para registros e login único [M1048, p. 2] e cita uma grande organização que exige testes e documentação até no menor projeto de vibe coding [M1048, p. 4].

**Desenvolvedor cidadão: ambiente isolado e caminho de promoção.** A OWASP, comunidade de segurança de aplicações, estendeu seu Top 10 do desenvolvimento cidadão à programação com IA e recomenda centro de governança, dono e ciclo de vida para cada aplicativo, classificação de risco em níveis e inventário [M1051, p. 1, 32]. Nas plataformas de pouco código (low-code), a Microsoft recomenda ambientes pessoais e isolados de desenvolvimento, com promoção por esteira para teste e produção, em parte sob licença premium [M1034, p. 3-5]. A Klabin define, por valor, risco e complexidade, quando o colaborador pode criar agentes [M326, p. 65].

**Casos** (relatados pelos fornecedores). A UKG, com mais de 16 mil funcionários, usa no Replit um modelo de protótipo com seu sistema de design e, segundo o fornecedor, aumentou em 400% a capacidade de colher retorno de clientes antes de investir em engenharia [M1058, p. 4]. Leitura nossa: nenhum caso de grande empresa traz governança descrita com resultado medido.

## 11. Veredito sobre as hipóteses

Régua da nota de custo: *confirmada*, evidência direta e consistente de mais de uma fonte; *confirmada em parte*, só parte se sustenta ou há evidência contrária relevante; *não se confirma*, a evidência aponta no sentido oposto; *sem evidência suficiente*, faltam dados. Pesquisa de opinião vale como percepção; causa exige comparação com método.

| Hipótese | Veredito | Evidência principal |
|---|---|---|
| Partida 1. Cerca de 90% usam a Microsoft como base | Confirmada em parte | Nas médias e grandes empresas brasileiras, 89% da base instalada de pacotes de escritório [M209, p. 11]; fora, o Microsoft 365 lidera em clientes na Okta, que vende login único, e 51% desses clientes também usam Google Workspace [M1052, p. 5, 8]; nada mede a base de governança |
| Partida 2. O Copilot perdeu a corrida inicial; a maioria foi para ChatGPT e Claude | Confirmada em parte | O ChatGPT chegou antes e tem mais presença no tráfego [M1005, web; M1049, p. 4], e a maioria dos empregados que usam IA recorre a ferramentas públicas gratuitas [M110, p. 73]; mas o Copilot lidera a aprovação nas grandes empresas americanas e a base brasileira, e o Claude fica bem atrás [M1045, p. 3; M209, p. 130] |
| Partida 3. Por isso o shadow AI ganhou tração | Confirmada em parte | A marca pesa em casos [M1005, web; M1012, p. 27]; as causas mais citadas são outras (seção 4) |
| H2. O motor é a falta de ferramenta oficial boa | Confirmada em parte | Motivo declarado [M1062, p. 2; M1065, p. 3]; queda das contas pessoais junto com a alta das corporativas [M1049, p. 2-3]; mas preferir escolher é o motivo mais citado numa pesquisa [M1062, p. 2], e 88% dos que têm IA da empresa também usam a pessoal [M1018, web] |
| H3. O Copilot ganhou a licença, não o uso | Confirmada em parte | Licenças crescem sem dado de uso por licença [M1038, p. 3-4]; caso Amgen, via imprensa [M1005, web]; nas avaliações de governo, o uso depende do critério [M1011, p. 16; M1021, p. 7] e, numa delas, a ferramenta foi vista como inferior [M1012, p. 27] |
| H4. Proibir funciona pouco; o que reduz é liberar com controle | Confirmada em parte | Contorno rápido da proibição nacional italiana [M1044, p. 11]; mais envio de dados sensíveis onde se proíbe, em associação [M110, p. 77]; a segunda parte só tem associação [M1049, p. 2-3], e regras rígidas com ferramentas homologadas reduzem pouco o uso por fora percebido [M1009, p. 2] |
| H5a. Há caminhos além do Copilot, com governança | Confirmada | Várias plataformas são a regra nas grandes empresas [M1045, p. 3]; casos com governança descrita pelas empresas [M025, p. 4; M437, p. 16; M417, p. 2-3]; Copilot aberto a outros modelos [M1032, p. 1] |
| H5b. Com custo adequado | Sem evidência suficiente | Entrada de US$ 20 a 30, com bases diferentes [M1053, p. 1; M1002, p. 2-3; M1037, p. 4]; planos empresariais sem preço público [M1053, p. 2; M1019, p. 3]; único dado de custo de plataforma via imprensa [M1043, p. 1] |
| H6. O vibe coding abre uma frente de aplicativos fora da TI | Confirmada em parte | Risco próprio documentado em incidentes [M1046, p. 1; M1030, p. 1; M1064, p. 1] e em código gerado com falhas [M1066, p. 1; M1007, p. 9]; a frente fora da TI só aparece em percepção sobre IA em geral [M1050, p. 2; M1026, p. 2] e em presença de usuários declarada pelos fornecedores [M1031, p. 2; M1058, p. 3] |
| H7. O risco é real e tem custo | Confirmada | Custo estimado pela IBM, em comparação entre grupos [M1023, web]; caso Samsung [M1013, p. 1-2]; violações medidas [M1049, p. 5; M1068, p. 60]; sem caso brasileiro de sanção |

**Hipótese de partida.** Confirma-se que a base é Microsoft, que o ChatGPT chegou antes e tem mais presença no tráfego e que a maioria dos que usam IA recorre a ferramentas públicas; não se confirma que o Copilot perdeu nas empresas, onde lidera a aprovação e a base instalada, nem que o Claude seja o destino da maioria; e a marca explica só parte do shadow AI.

**Leitura preliminar do protocolo.** Sustenta-se em parte: as causas se somam, entre elas a distância entre necessidade e oferta e a governança lenta; falta provar, com método, que o caminho visto nos casos reduz o uso por fora.

## 12. Implicações para a estratégia de IA

Leitura nossa, macro: o uso por fora é sinal de demanda e mostra o que falta.

**(a) Indicador proposto para a régua da Frente 2** (proposta para discussão; leitura nossa), em estratégia e governança, como par do indicador de gestão do custo da nota [Custo de uso da IA](../04_frente-3_tendencias/custo-da-ia.md). Segue a seção 6.2 dos [frameworks de maturidade](frameworks-de-maturidade.md): critérios cumulativos, em que cada estágio supõe os anteriores, e, do estágio 3 em diante, evidência de prática em operação; anunciar a liberação de uma ferramenta não basta.

| Estágio | Uso de IA fora dos canais oficiais | Evidência pública mínima |
|---|---|---|
| 1. Exploração | Uso individual com contas pessoais; sem diretriz, ou só proibição; ninguém sabe que ferramentas se usam nem que dado sai | Nenhuma diretriz de uso divulgada, ou só proibição |
| 2. Pilotos | Diretriz que diz o que pode e que dado não entra; ferramenta oficial em piloto para alguns grupos; bloqueios pontuais | Diretriz de uso divulgada; piloto com escopo e métrica; responsável nomeado |
| 3. Operacionalização | Canal oficial para todos, com login único, proteção de dados no contrato e registro de uso; treinamento na política; comitê que avalia ferramentas; descoberta do uso por fora | Política com percentual treinado; canal oficial para todos, com controles descritos e algum dado de uso, com unidade e período; comitê nomeado |
| 4. Escala | Catálogo de ferramentas aprovadas ou plataforma com vários modelos, sob a mesma governança; capacitação ampla no uso; uso oficial e uso por fora medidos; ambiente isolado para protótipos, com promoção pela TI | Usuários ativos com critério divulgado; plataforma ou catálogo descrito; regras para criação fora da TI |
| 5. Transformação | Regras aplicadas por tecnologia e verificadas sempre; ferramenta ou modelo novo entra por avaliação rápida; uso por fora residual; aplicativos criados fora da TI com inventário, dono e nível de risco | Rotina de avaliação e medida do uso por fora divulgadas |

Base dos critérios: [M1000, p. 16; M223, p. 20, 25; M1016, p. 4; M1012, p. 48; M1034, p. 3-5; M1051, p. 32]. Calibragem: na clientela da Netskope, metade das organizações ainda não aplica por tecnologia a proteção de dados na IA generativa [M1049, p. 5]. Como a prática interna quase não aparece em fonte pública, o indicador depende das sessões executivas; vale por área (campo, indústria, corporativo) e anda junto com o de custo, pois o registro de uso também mede consumo.

**(b) Perguntas sugeridas para as sessões executivas** (a validar com a equipe; o questionário validado com o cliente não muda):
1. Que ferramentas de IA a empresa oferece oficialmente, a quem e desde quando?
2. A empresa sabe o que se usa por fora? Como mede?
3. A política diz que dado não entra? Quantos foram treinados?
4. Diante do uso por fora, a empresa bloqueou, liberou ou ofereceu alternativa?
5. Quanto tempo leva para aprovar uma ferramenta ou um modelo novo?
6. Quem cria aplicativos ou agentes fora da TI, e como eles chegam à produção?
7. Como a empresa mede o uso real das licenças pagas?

**(c) Para uma agroindústria que estrutura a IA.**
- **Começar pelo canal oficial.** O chat corporativo com proteção de dados que vem na suíte não tem custo adicional de licença [M1033, p. 2]; para a licença paga, o Tesouro australiano recomenda liberação em fases, primeiro a quem tem uso claro [M1012, p. 47-48].
- **Deixar a porta aberta a outros modelos**, sob a mesma identidade, contrato e registro [M1032, p. 4].
- **Olhar onde os dados são processados:** algumas ofertas não incluem o Brasil [M1053, p. 8], e dado pessoal em ferramenta pública é tema de LGPD [M1003, p. 24].
- **Tratar a prototipação como desenvolvimento cidadão:** ambiente isolado, sem dado de produção, varredura antes de publicar e promoção pela TI, conforme o risco [M1047, p. 1-2; M1034, p. 3-5; M1051, p. 32].
- **Medir desde o piloto** o uso real, o uso por fora e o custo inteiro.

## 13. Números que não devem ser usados (ou só com ressalva)

| Afirmação | Problema e o que fazer | Fonte |
|---|---|---|
| "47% (Netskope) e 67% (Verizon) medem o mesmo" | Bases diferentes; citar cada um com a sua | [M1049, p. 2; M1068, p. 60] |
| "ChatGPT 77% × Copilot 52% é participação de usuários" | "Adoção" sem base definida; não usar como participação | [M1049, p. 4] |
| "Funcionários de 90% das empresas usam IA pessoal" | Via imprensa, original bloqueado, mede empresas; só com a ressalva | [M1014, p. 4] |
| "38% dos brasileiros usam IA sem autorização" | Recorte contestado e sem amostra; usar o global, um terço | [M1063, p. 1; M1065, p. 3] |
| "Proibir não reduz o uso por fora" (com base na Peers) | Percepção; o grupo de regras rígidas tem ferramentas homologadas, não proibição | [M1009, p. 2] |
| "Shadow AI em 43% dos incidentes, a US$ 5,39 milhões" | Só via terceiro, sem base nem comparação; usar a IBM 2025 | [M1004, p. 2; M1023, web] |
| "Um incidente de shadow AI custa US$ 670 mil" | É a diferença entre nível alto e baixo de shadow AI; dizer a comparação | [M1023, web] |
| "70% da Fortune 500 usam o Copilot" | Declaração da Microsoft, repetida pela McKinsey e pela Bloomberg, que não diz quantos funcionários usam | [M026, p. 8; M1005, web] |
| "80% de adoção do Copilot no governo britânico" | Um uso em 30 dias; dizer o critério, sem comparar com o DBT nem somar licenças | [M1021, p. 7; M1011, p. 40] |
| "BBVA: 87 mil usam o Gemini"; "250 mil usam a LLM Suite"; "470 mil usam o Claude" | Acesso, não uso; os 65 mil ativos do JPMorganChase são só do banco comercial e de investimento | [M413, p. 6; M025, p. 3; M441, p. 64; M1001, p. 1] |
| "O Itaú cortou 65% do custo com IA" | Só na imprensa, sem separar a queda de preço dos modelos | [M1043, p. 1] |
| "45% do código gerado por IA é inseguro" | Tarefas escolhidas por risco, com a ferramenta do fornecedor; dizer a base | [M1066, p. 3] |
| "1 em cada 5 organizações expostas" (Wiz) | Sem base, amostra nem método; não usar | [M1070, p. 1-2] |
| "Assistente para 20 mil funcionários de um grupo sucroenergético" | Conteúdo de parceiro, sem confirmação da empresa; confirmar antes | [M362, web] |
| Copilot "de 18,8% para 11,5%" como ferramenta principal; "dois terços dos clientes do Copilot usam outros assistentes" | Só em jornal pago e agregadores, ou não achado; não usar | Fora do catálogo |

## 14. Lacunas

- **Uso real do Copilot.** Não há uso ativo por licença nem dado independente de uso por ferramenta em empresas que licenciaram o Copilot, inclusive as brasileiras; a pesquisa de 2026 do Gartner é paga [M1015, web].
- **Proibir × liberar com controle.** Nenhum estudo compara os caminhos pelo mesmo método.
- **Brasil.** Não há pesquisa própria da Microsoft Brasil, da IDC Brasil ou do Cetic.br sobre shadow AI; o recorte da Thomson Reuters é contestado, e o dado da Peers não está no relatório publicado.
- **Fontes primárias.** Relatórios completos de IBM 2026, PagerDuty, Nutanix, Zscaler e Veracode, e o original do MIT NANDA.
- **Custo.** Preço de ChatGPT Enterprise, Workspace Enterprise e Gemini Enterprise (página de preços fora do ar na consulta); descontos; impostos e câmbio; custo de plataforma interna.
- **Vibe coding.** Quantos aplicativos fora da TI nascem dessas ferramentas; alcance da exposição do Lovable em 2026; versão final do SusVibes; local de processamento no Bolt e no v0; uma possível mudança de controle do Cursor, citada na pesquisa e ainda não confirmada em fonte catalogada, e seu efeito sobre termos de dados; guias da CISA, agência americana de cibersegurança, e do NIST.
- **Agro.** Nenhuma fonte pública traz shadow AI ou vibe coding com governança em agroindústrias; os casos do setor descrevem a oferta oficial.

## Fontes

<!-- fontes:inicio -->
- **M018** — MIT Technology Review Brasil, TEC.Institute e Peers Consulting + Technology (2026). Gerando valor com GenAI — Do piloto ao resultado: a rentabilidade da IA (2ª edição). [link](https://mittechreview.com.br/) · citado em p. 29
- **M025** — McKinsey & Company (Financial Services Practice) (2025). JPMorgan Chase's Derek Waldron on building an AI-first bank culture (entrevista, 29/10/2025). [link](https://www.mckinsey.com/industries/financial-services/our-insights/jpmorgan-chases-derek-waldron-on-building-an-ai-first-bank-culture) · citado em p. 3, 3-4, 4
- **M026** — McKinsey & Company (QuantumBlack) (2025). Seizing the agentic AI advantage. [link](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage) · citado em p. 8
- **M110** — University of Melbourne e KPMG International (2025). Trust, attitudes and use of artificial intelligence: A global study 2025. [link](https://kpmg.com/xx/en/our-insights/ai-and-technology/trust-attitudes-and-use-of-ai.html) · citado em p. 15, 73, 77, 109
- **M209** — FGV EAESP - FGVcia (Fernando Meirelles) (2025). Pesquisa do Uso de TI - 36ª Edição Anual, FGVcia, 2025. [link](https://eaesp.fgv.br/sites/default/files/files-eaesp/u68/pesti_fgvcia_2025.pdf) · citado em p. 11, 130
- **M223** — NIST (National Institute of Standards and Technology, EUA) (2024). Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1). [link](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) · citado em p. 20, 25
- **M326** — Klabin (2026 (ref. 2025)). Relatório de Sustentabilidade 2025. [link](https://rs2025.klabin.com.br/documents/2996966/4590388/RS+2025+A4+-+Klabin+-+v2_compressed.pdf/980d0243-ee3c-1e4d-7394-f29527a186e9?t=1788271818905) · citado em p. 63-65, 65, 74
- **M334** — Suzano (2025). Microsoft e Suzano desenvolvem solução para impulsionar eficiência industrial com IA generativa (notícia, 23/04/2025). [link](https://www.suzano.com.br/noticia/microsoft-e-suzano-desenvolvem-ia-generativa) · citado em p. 6
- **M357** — São Martinho (2026 (safra 2025/26)). Relato Integrado 2025/2026. [link](https://www.saomartinho.com.br/Download.aspx?Arquivo=8rGueYhS+9fDqXheg2ZTaQ==&IdCanal=E/5CI5hbGiTfjZ7mhu2y5w==) · citado em p. 46
- **M362** — Think Work Lab / iFood Benefícios (Acrescenta) (2025). Com IA generativa, Raízen transforma o atendimento interno (case da assistente BIA). [link](https://beneficios.ifood.com.br/acrescenta/artigos/ia-generativa-raizen) · citado em web
- **M413** — BBVA (2025). BBVA deploys 'The Eight', its strategy to transform the financial experience with AI (12/12/2025). [link](https://www.bbva.com/en/innovation/bbva-deploys-the-eight-its-strategy-to-transform-the-financial-experience-with-ai/) · citado em p. 5-6, 6
- **M417** — Banco do Brasil (2026). BB é pioneiro global em diretrizes para IA generativa e agêntica (release, 24/08/2026). [link](https://imprensa.bb.com.br/bb-e-pioneiro-global-em-diretrizes-para-ia-generativa-e-agentica/) · citado em p. 1-3, 2-3
- **M437** — Itaú Unibanco Holding (2026). Relatório Anual Integrado 2025. [link](https://api.mziq.com/mzfilemanager/v2/d/42787847-4cf6-4461-94a5-40ed237dca33/0a51b7a9-1163-000a-c8a9-f93b068ffef8?origin=2) · citado em p. 16
- **M441** — JPMorganChase (2026). Annual Report 2025 (carta do CEO Jamie Dimon, carta do COO e cartas dos negócios). [link](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/annualreport-2025.pdf) · citado em p. 64
- **M517** — Petrobras (2024). Desenvolvimento do Capital Humano - Destaques (2024). [link](https://petrobras.com.br/documents/d/f3a44542-113e-11ee-be56-0242ac120002/2024_desenvolvimento-do-capital-humano-rh-e-up-v-n1-e-ge-v-1-final?download=true) · citado em p. 7
- **M909** — Anthropic (2026 (consulta em 14/10/2026)). Plans & pricing (Claude). [link](https://claude.com/pricing) · citado em p. 11, 11-12, 12
- **M1000** — ANBIMA (Associação Brasileira das Entidades dos Mercados Financeiro e de Capitais) – Rede ANBIMA de Inovação (2024 (atualização de jul/2024)). Guia orientativo – Boas práticas para o uso de sistemas de inteligência artificial nos mercados financeiro e de capitais (atualização de jul/2024). [link](https://www.anbima.com.br/data/files/63/74/15/39/F12C091039E04909EA2BA2A8/Guia_orientativo_boas_praticas_para_o_uso_de_sistemas_de_inteligencia_artificial.pdf) · citado em p. 16
- **M1001** — Anthropic (2025 (06/10/2025)). Deloitte will make Claude available to 470,000 people across its global network (anúncio, 06/10/2025). [link](https://www.anthropic.com/news/deloitte-anthropic-partnership) · citado em p. 1, 1-2
- **M1002** — Anthropic (2026 (consulta em 15/10/2026)). What is the Team plan? (Central de Ajuda do Claude; consulta em 15/10/2026). [link](https://support.claude.com/en/articles/9266767-what-is-the-team-plan) · citado em p. 1, 2-3
- **M1003** — Autoridade Nacional de Proteção de Dados (ANPD) (2024 (nov/2024)). Radar Tecnológico nº 3 – Inteligência artificial generativa (nov/2024). [link](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos/radar_tecnologico_ia_generativa_anpd.pdf) · citado em p. 23, 24
- **M1004** — Baker Donelson (escritório de advocacia dos EUA), resumindo o relatório da IBM (2026 (30/07/2026)). Ten Takeaways from IBM's 2026 Cost of a Data Breach Report. [link](https://www.bakerdonelson.com/ten-takeaways-from-ibms-2026-cost-of-a-data-breach-report) · citado em p. 2
- **M1005** — Bloomberg (versão em português publicada pela Bloomberg Línea) (2025 (24/06/2025)). Sucesso do ChatGPT contra o Copilot alimenta a rivalidade entre OpenAI e Microsoft. [link](https://www.bloomberglinea.com.br/tech/sucesso-do-chatgpt-contra-o-copilot-alimenta-a-rivalidade-entre-openai-e-microsoft/) · citado em web
- **M1006** — Bolt (StackBlitz) (2026 (post de 18/02/2026; preços consultados em 15/10/2026)). Bolt for Teams just leveled up (post oficial) e página de preços do Bolt (plano Enterprise). [link](https://bolt.new/blog/build-together-with-enhanced-team-features) · citado em p. 3-5, 13
- **M1007** — Carnegie Mellon University (Language Technologies Institute), com Columbia University, Johns Hopkins University e HydroX AI (2025 (arXiv v1 de 02/12/2025; arquivo baixado = v2, de 16/02/2026; v3 de 21/08/2026 e v4 de 21/09/2026; publicado nos anais do ICML 2026, PMLR v306)). Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-World Tasks (benchmark SusVibes). [link](https://arxiv.org/abs/2512.03262) · citado em p. 1, 9, 12-13
- **M1008** — Cisco (2024 (25/01/2024)). Cisco 2024 Data Privacy Benchmark Study. [link](https://www.cisco.com/c/dam/en_us/about/doing_business/trust-center/docs/cisco-privacy-benchmark-study-2024.pdf) · citado em p. 22
- **M1009** — Convergência Digital (cobrindo estudo da Peers Consulting + Technology e do TEC.Institute publicado pela MIT Technology Review Brasil) (2026 (24/09/2026)). Executivos brasileiros admitem uso não autorizado de IA generativa na rotina do trabalho. [link](https://convergenciadigital.com.br/carreira/executivos-brasileiros-admitem-uso-nao-autorizado-de-ia-generativa-na-rotina-do-trabalho/) · citado em p. 1-2, 2
- **M1010** — Cursor (Anysphere) (2026 (consulta em 15/10/2026)). Cursor Enterprise — documentação oficial (visão geral, privacidade e governança de dados, segurança e controles do agente). [link](https://cursor.com/docs/enterprise) · citado em p. 4-5, 8, 11-12, 14
- **M1011** — Department for Business and Trade (DBT), Governo do Reino Unido (2025 (ago/2025)). The Evaluation of the M365 Copilot Pilot in the Department for Business and Trade (relatório de avaliação, ago/2025). [link](https://assets.publishing.service.gov.uk/media/68adbe409e1cebdd2c96a19d/dbt-microsoft-365-copilot-evaluation.pdf) · citado em p. 4-5, 14, 16, 34, 40
- **M1012** — Department of the Treasury (Austrália) – Australian Centre for Evaluation (ACE) (2025 (fev/2025)). Evaluation of a trial of generative artificial intelligence (Copilot) in The Department of the Treasury (relatório de avaliação, fev/2025). [link](https://evaluation.treasury.gov.au/sites/evaluation.treasury.gov.au/files/2025-02/evaluation-generative-artificial-intelligence.pdf) · citado em p. 6, 7, 18, 20, 27, 47, 47-48, 48
- **M1013** — Forbes (edição australiana), com base em reportagem da Bloomberg (2023 (02/05/2023)). Samsung bans ChatGPT among employees after sensitive code leak. [link](https://www.forbes.com.au/news/innovation/samsung-bans-chatgpt-among-employees-after-sensitive-code-leak/) · citado em p. 1-2
- **M1014** — Fortune (cobrindo 'The GenAI Divide: State of AI in Business 2025', do MIT NANDA) (2025 (19/08/2025)). The 'shadow AI economy' is booming: Workers at 90% of companies say they use chatbots, but most of them are hiding it from IT. [link](https://fortune.com/2025/08/19/shadow-ai-economy-mit-study-genai-divide-llm-chatbots/) · citado em p. 4
- **M1015** — Gartner (2026 (29/09/2026)). 2026 Microsoft 365 and Copilot Survey Reveals Workplace Trends. [link](https://www.gartner.com/en/documents/8443513) · citado em web
- **M1016** — Gartner (2026 (10/06/2026)). AI Governance Requires More Than Policies (artigo, 10/06/2026; na aba do navegador, 'AI Governance Needs More Than Policies'). [link](https://www.gartner.com/en/articles/ai-governance-trism) · citado em p. 2, 4
- **M1018** — Gartner (2026 (13/05/2026)). Gartner Predicts by 2027, 50% of Enterprises Without a People-Centric AI Strategy Will Lose Their Top AI Talent. [link](https://www.gartner.com/en/newsroom/press-releases/2026-05-13-gartner-predicts-by-2027-50-percent-of-enterprises-without-a-people-centric-ai-strategy-will-lose-their-top-ai-talent) · citado em web
- **M1019** — Google (2026 (consulta em 15/10/2026)). Google Workspace – compare planos e preços (página oficial no Brasil; cópia de 15/10/2026). [link](https://workspace.google.com/intl/pt-BR/pricing) · citado em p. 1-2, 3, 4-5, 7
- **M1021** — Government Digital Service (GDS), Governo do Reino Unido (2025 (jun/2025)). Microsoft 365 Copilot Experiment: Cross-Government Findings Report (jun/2025). [link](https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf) · citado em p. 3-5, 4, 7, 11, 22
- **M1022** — Harmonic Security (2025 (jan/2025; dados do 4º tri/2024)). From Payrolls to Patents: The Spectrum of Data Leaked into GenAI. [link](https://www.harmonic.security/resources/from-payrolls-to-patents-the-spectrum-of-data-leaked-into-genai) · citado em p. 2, 7
- **M1023** — IBM (pesquisa do Ponemon Institute) (2025 (30/07/2025)). IBM Report: 13% Of Organizations Reported Breaches Of AI Models Or Applications, 97% Of Which Reported Lacking Proper AI Access Controls (Cost of a Data Breach Report 2025). [link](https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls) · citado em web
- **M1024** — IBM (pesquisa do Ponemon Institute) (2026 (29/07/2026)). IBM Study: One in Four Malicious Breaches are AI-Enabled, Costing Companies $6 Million on Average (Cost of a Data Breach Report 2026). [link](https://newsroom.ibm.com/2026-07-29-ibm-study-one-in-four-malicious-breaches-are-ai-enabled,-costing-companies-6-million-on-average) · citado em web
- **M1025** — ISO/IEC (JTC 1/SC 42) (2023 (dez/2023; página consultada em 15/10/2026)). ISO/IEC 42001:2023 – Information technology – Artificial intelligence – Management system (página oficial; consulta em 15/10/2026). [link](https://www.iso.org/standard/42001) · citado em p. 1-2
- **M1026** — IT Forum (cobrindo o Enterprise Cloud Index 2026 da Nutanix) (2026 (29/06/2026)). Nutanix aponta que 81% dos executivos veem risco no uso de IA sem supervisão. [link](https://itforum.com.br/noticias/nutanix-81-executivos-risco-no-uso-de-ia/) · citado em p. 2, 4
- **M1028** — Lovable (2026 (consulta em 15/10/2026)). Lovable for Enterprise (documentação oficial do plano empresarial). [link](https://docs.lovable.dev/introduction/lovable-for-enterprise) · citado em p. 2-3, 5, 7
- **M1030** — Lovable (2026 (22/04/2026)). Our response to the April 2026 incident (resposta do Lovable ao incidente de abril de 2026). [link](https://lovable.dev/blog/our-response-to-the-april-2026-incident) · citado em p. 1, 1-2, 3, 6
- **M1031** — Lovable (2026 (12/08/2026)). We just raised $400M in Series C funding to help people run their businesses. [link](https://lovable.dev/blog/series-c) · citado em p. 2
- **M1032** — Microsoft (2026 (consulta em 15/10/2026)). Anthropic models in Microsoft Online Services (Microsoft Learn, atualizado em 18/09/2026; consulta em 15/10/2026). [link](https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor) · citado em p. 1, 1-2, 4, 5-6
- **M1033** — Microsoft (2025 (15/01/2025)). Copilot for all: Introducing Microsoft 365 Copilot Chat (blog, 15/01/2025). [link](https://www.microsoft.com/en-us/microsoft-365/blog/2025/01/15/copilot-for-all-introducing-microsoft-365-copilot-chat/) · citado em p. 2, 4
- **M1034** — Microsoft (2026 (consulta em 15/10/2026)). Develop a tenant environment strategy to adopt Power Platform at scale; Key concepts — Copilot Studio security and governance (documentação oficial). [link](https://learn.microsoft.com/en-us/power-platform/guidance/adoption/environment-strategy) · citado em p. 3-5
- **M1035** — Microsoft (2025 (24/09/2025)). Expanding model choice in Microsoft 365 Copilot (blog, 24/09/2025). [link](https://www.microsoft.com/en-us/microsoft-365/blog/2025/09/24/expanding-model-choice-in-microsoft-365-copilot/) · citado em p. 2-3
- **M1036** — Microsoft (2026 (consulta em 15/10/2026)). Microsoft 365 Copilot para grandes empresas – preços (página oficial no Brasil; cópia de 15/10/2026). [link](https://www.microsoft.com/pt-br/microsoft-365-copilot/enterprise) · citado em p. 1, 5
- **M1037** — Microsoft (2026 (consulta em 15/10/2026)). Microsoft Copilot for enterprise – pricing (página oficial nos EUA; cópia de 15/10/2026). [link](https://www.microsoft.com/en-us/copilot/solutions/enterprise) · citado em p. 4, 4-5
- **M1038** — Microsoft (2026 (29/07/2026)). Microsoft Fiscal Year 2026 Fourth Quarter Earnings Conference Call (transcrição oficial). [link](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4) · citado em p. 3, 3-4, 4
- **M1039** — Microsoft (2026 (28/01/2026)). Microsoft Fiscal Year 2026 Second Quarter Earnings Conference Call (transcrição oficial). [link](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) · citado em p. 4, 6
- **M1040** — Microsoft (2026 (29/04/2026)). Microsoft Fiscal Year 2026 Third Quarter Earnings Conference Call (transcrição oficial). [link](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3) · citado em p. 2-3, 3
- **M1041** — Microsoft (Purview) (2026 (consulta em 15/10/2026)). Learn about Data Security Posture Management for AI – classic (Microsoft Learn; consulta em 15/10/2026). [link](https://learn.microsoft.com/en-us/purview/dspm-for-ai) · citado em p. 1, 4
- **M1042** — Microsoft e LinkedIn (2024 (08/05/2024)). AI at Work Is Here. Now Comes the Hard Part (2024 Work Trend Index Annual Report). [link](https://assets-c4akfrf5b4d3f4b7.z01.azurefd.net/assets/2024/05/2024_Work_Trend_Index_Annual_Report_6_7_24_666b2e2fafceb.pdf) · citado em p. 7, 9, 27, 30, 32
- **M1043** — Mobile Time (cobertura do lançamento da ia.i, com declarações do diretor de tecnologia do Itaú Unibanco) (2026 (27/07/2026)). Itaú já reduziu em 65% o custo com IA generativa desde 2022 (reportagem, 27/07/2026). [link](https://www.mobiletime.com.br/noticias/27/07/2026/itau-custo-ia-generativa/) · citado em p. 1, 1-2
- **M1044** — Monash University (Departamento de Economia e SoDa Labs) (2023 (abr/2023)). The Unintended Consequences of Censoring Digital Technology – Evidence from Italy's ChatGPT Ban (artigo de trabalho, arXiv 2304.09339, abr/2023). [link](https://arxiv.org/abs/2304.09339) · citado em p. 11, 13
- **M1045** — Morning Consult (2026 (03/08/2026)). The State of Enterprise AI: Budgets Are Growing & Platform Lineups Remain in Flux. [link](https://morningconsult.com/articles/state-of-enterprise-ai) · citado em p. 1, 3, 7
- **M1046** — NIST — National Vulnerability Database (NVD); registro CVE atribuído pela MITRE (2025 (publicado em 30/05/2025; última modificação em 17/06/2026)). CVE-2025-48757 Detail (registro da vulnerabilidade de segurança em nível de linha nos aplicativos gerados pelo Lovable). [link](https://nvd.nist.gov/vuln/detail/CVE-2025-48757) · citado em p. 1, 1-2
- **M1047** — National Cyber Security Centre (NCSC), Reino Unido (2026 (18/06/2026)). The 'vibe coding spectrum' approach to AI-assisted software development. [link](https://www.ncsc.gov.uk/blogs/the-vibe-coding-spectrum-approach-to-ai-assisted-software-development) · citado em p. 1-2, 1-3, 3
- **M1048** — National Cyber Security Centre (NCSC), Reino Unido — CTO de Arquitetura (2026 (24/03/2026)). Vibe check: AI may replace SaaS (but not for a while). [link](https://www.ncsc.gov.uk/blogs/vibe-check-ai-may-replace-saas-but-not-for-a-while) · citado em p. 2, 4
- **M1049** — Netskope (Netskope Threat Labs) (2026). Cloud and Threat Report: 2026. [link](https://www.netskope.com/resources/cloud-and-threat-reports/cloud-and-threat-report-2026) · citado em p. 2, 2-3, 3, 4, 5, 6, 12
- **M1050** — Nutanix (pesquisa da Wakefield Research) (2026 (03/03/2026)). Nutanix Enterprise Cloud Index Finds AI Is Driving Rapid Container Adoption while Shadow IT and Organizational Silos Create AI Risks. [link](https://www.nutanix.com/press-releases/2026/nutanix-enterprise-cloud-index-finds-ai-is-driving-rapid-container-adoption) · citado em p. 2
- **M1051** — OWASP Foundation (projeto OWASP Citizen Development Top 10) (2025 (documento sem data; referências até set/2025)). OWASP Top 10 Risks for Citizen Development (riscos do desenvolvimento cidadão: low-code/no-code, programação assistida por IA e agentes). [link](https://owasp.org/www-project-citizen-development-top-10/) · citado em p. 1, 32
- **M1052** — Okta (Okta Japan) (2026 (30/04/2026)). Okta、業務アプリの利用動向に関する年次調査「Businesses at Work 2026」の結果を発表 (Okta divulga o Businesses at Work 2026). [link](https://www.okta.com/ja-jp/newsroom/press-releases/okta-businesses-at-work2026/) · citado em p. 5, 8
- **M1053** — OpenAI (2026 (consulta em 15/10/2026)). Preços para empresas – ChatGPT Business e Enterprise (página oficial em português; cópia de 15/10/2026). [link](https://openai.com/pt-BR/business/pricing/) · citado em p. 1, 1-2, 2, 8
- **M1054** — PagerDuty (pesquisa feita pela Wakefield Research) (2026 (11/06/2026)). PagerDuty Report Finds Two-Thirds (66%) of Office Professionals Have Used Unauthorized AI Tools at Work (PagerDuty Shadow AI Survey). [link](https://s206.q4cdn.com/635206389/files/doc_news/PagerDuty-Report-Finds-Two-Thirds-66-of-Office-Professionals-Have-Used-Unauthorized-AI-Tools-at-Work-2026.pdf) · citado em p. 1-3, 2
- **M1055** — Pesquisadores que registraram a CVE, em blog pessoal de um deles; na notificação formal ao Lovable, a organização indicada é o Replit (2025 (29/05/2025)). Statement on CVE-2025-48757, de Matt Palmer (declaração dos pesquisadores sobre a falha de RLS em projetos do Lovable). [link](https://mattpalmer.io/posts/statement-on-CVE-2025-48757/) · citado em p. 3-5, 12
- **M1056** — Replit (2025 (21/07/2025)). Introducing a safer way to Vibe Code with Replit Databases (separação dos bancos de desenvolvimento e de produção). [link](https://replit.com/blog/introducing-a-safer-way-to-vibe-code-with-replit-databases) · citado em p. 1-2
- **M1057** — Replit (2026 (consulta em 15/10/2026)). Replit Enterprise — documentação oficial (plano Enterprise, uso de dados para treino e configurações de privacidade e publicação). [link](https://docs.replit.com/billing/plans/replit-enterprise) · citado em p. 2-3, 9
- **M1058** — Replit (2026 (11/03/2026)). The Future is Actually Very Human — Replit raises $400 million at a $9 billion valuation. [link](https://replit.com/blog/replit-raises-400-million-dollars) · citado em p. 3, 4
- **M1061** — Software AG (Software GmbH) (2024). Chasing Shadows: Understanding and Managing Shadow AI (white paper, 2024). [link](https://web.archive.org/web/20250515123238/https://newscenter.softwareag.com/content/dam/softwareag/global/image/corporate/press/comm/shadow-ai/Shadow%20AI%20White%20Paper.pdf) · citado em p. 7
- **M1062** — Software AG (Software GmbH) (2024 (22/10/2024)). Half of all employees are Shadow AI users, new study finds (release, 22/10/2024). [link](https://web.archive.org/web/20251006225317/https://newscenter.softwareag.com/en/news-stories/press-releases/2024/1022-half-of-all-employees-use-shadow-ai.html) · citado em p. 1, 2
- **M1063** — TI Inside (cobrindo o Future of Professionals 2026, da Thomson Reuters) (2026 (08/07/2026)). 38% dos profissionais no Brasil utilizam ferramentas de IA sem autorização da empresa, aponta Thomson Reuters. [link](https://tiinside.com.br/08/07/2026/38-dos-profissionais-no-brasil-utilizam-ferramentas-de-ia-sem-autorizacao-da-empresa-aponta-thomson-reuters/) · citado em p. 1
- **M1064** — The Register (2025 (22/07/2025)). Replit makes vibe-y promise to stop its AI agents making vibe coding disasters. [link](https://www.theregister.com/2025/07/22/replit_saastr_response/) · citado em p. 1
- **M1065** — Thomson Reuters (2026 (22/06/2026)). A IA está pronta, mas os escritórios não: como o atraso na implementação de IA está custando clientes e talentos (release do Future of Professionals 2026). [link](https://www.thomsonreuters.com.br/pt/sala-de-imprensa/atraso-implementacao-ia-custa-clientes.html) · citado em p. 2, 3, 4, 5
- **M1066** — Veracode (2025 (30/07/2025)). AI-Generated Code Poses Major Security Risks in Nearly Half of All Development Tasks (comunicado do 2025 GenAI Code Security Report). [link](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/) · citado em p. 1, 3
- **M1067** — Vercel (v0) (2026 (consulta em 15/10/2026)). v0 Docs — Security e Enterprise (documentação oficial). [link](https://v0.app/docs/security) · citado em p. 2-4
- **M1068** — Verizon Business (2026). 2026 Data Breach Investigations Report (DBIR). [link](https://www.verizon.com/business/resources/Tf38/reports/2026-dbir-data-breach-investigations-report.pdf) · citado em p. 60
- **M1070** — Wiz (Wiz Research) (2025 (18/09/2025)). Wiz Research Discovers One in Five Organizations Exposed to Systemic Risks in Vibe-Coded Applications. [link](https://www.wiz.io/blog/common-security-risks-in-vibe-coded-apps) · citado em p. 1-2
- **M1071** — Zscaler (ThreatLabz) (2025 (20/03/2025; dados de fev–dez/2024)). New Zscaler AI Security Report Reveals an Over 3,000% Surge in Enterprise Use of AI/ML Tools (release, 20/03/2025). [link](https://www.zscaler.com/press/new-zscaler-ai-security-report-reveals-over-3000-surge-enterprise-use-ai-ml-tools) · citado em p. 2
- **M1072** — Zscaler (ThreatLabz) (2026 (dados de 2025)). Zscaler ThreatLabz 2026 AI Security Report (página-resumo do relatório; consulta em 15/10/2026). [link](https://www.zscaler.com/campaign/threatlabz-ai-security-report) · citado em p. 3
- **M1073** — techpartner.news (cobrindo a 2025 Gartner Microsoft 365 and Copilot Survey, apresentada em conferência do Gartner) (2025 (26/06/2025)). Gartner: Microsoft Copilot hype offset by ROI and readiness realities. [link](https://www.techpartner.news/news/gartner-microsoft-copilot-hype-offset-by-roi-and-readiness-realities-618118) · citado em p. 2, 3
- **M1074** — Forbes Brasil (Forbes Money) (2026 (jun/2026)). Entrevista com executivo da Thomson Reuters sobre o Future of Professionals 2026 (Forbes Money, jun/2026). [link](https://forbes.com.br/forbes-money/2026/06/entrevista-thomson-reuters-ia-adrian-fognini/) · citado em web
<!-- fontes:fim -->
