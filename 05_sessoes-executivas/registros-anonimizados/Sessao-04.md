# Sessão 04 — 2026-10-21

> Registro anonimizado. Sem nomes de pessoas, de empresas, de sistemas ou de fornecedores citados pelo entrevistado, e sem detalhes que permitam identificá-lo. Gravação, transcrição e anotações brutas ficam fora do Git (`05_sessoes-executivas/_originais/`) e devem ser apagadas depois deste registro.
>
> **Sem mistura com o que a empresa divulga.** O relato desta sessão não se combina com os documentos públicos da empresa: a prévia da sessão não cita documentos da empresa.

- **Perfil:** liderança de agricultura digital de um grande grupo produtor de grãos e fibras.
- **Setor:** agro (produção de grãos e fibras).
- **Formato:** conversa online de cerca de 45 minutos, conduzida pelo Guilherme; condução livre, com parte das perguntas do roteiro.
- **Estágio autodeclarado (1–5):** a régua não foi mostrada. Leitura nossa, a partir do relato: estratégia e governança no 3 (comitê de IA multidisciplinar, política de uso, registro de todos os acessos, licença por perfil); dados e infraestrutura no 3 (repositório central de dados anterior à IA e base geográfica padronizada); organização e pessoas no 3 (time de dados e IA dedicado e champions em cada gerência); aplicações e valor entre 2 e 3 (IA preditiva e visão computacional com resultados técnicos, agente corporativo em uso por todos, retorno financeiro ainda não medido). Estágio geral 3, o mais avançado das quatro sessões.
- **Gravação e transcrição brutas apagadas em:** pendente.
- **Prévia de resultados:** [BIA-ACL-RP-06](../../07_entregaveis/relatorios-parciais/previa-sessao-executiva-04_BIA-ACL-RP-06_rev00.pdf).
- Nomes de terceiros citados na conversa (colegas, startups, fabricantes e sistemas) ficam fora do registro.

## Principais insights por tema do roteiro

1. **Trajetória e estágio.** A IA clássica (aprendizado de máquina) vem de antes da IA generativa. O primeiro projeto, por volta de 2019–2020, foi um modelo que cruzava clima previsto, pesquisa interna e histórico de produção para posicionar a melhor semente em cada talhão; previa bem a produtividade por cenário climático, mas parou depois de cerca de dois anos porque as variedades mudam rápido demais e não havia histórico para as novas. Depois veio a visão computacional, com uma startup em que a empresa investe: primeiro plantas daninhas com drone, há três anos pragas e doenças. Um laboratório digital próprio, que trocou vários sistemas de mercado por sistemas próprios, ganhou há cerca de dois anos um time de dados e IA.
2. **Valor real.** Os modelos de imagem passam de 90% de acerto para algumas pragas, com "alucinação muito baixa"; nesta safra, uma fazenda testa o monitoramento integrado de pragas e doenças com robô e modelo treinado, com foco no algodão, onde o uso de defensivos é maior. Um agente que consulta toda a documentação da empresa (processos, procedimentos e políticas) já é usado por todos. No desenvolvimento, o front-end reduziu de 40% a 50% o tempo com IA; no back-end, o ganho é menor. O retorno financeiro do consumo de IA ainda não é medido: o controle é por orçamento, crédito por perfil e uso; medir o retorno deve ser o desafio de 2027. Hoje também se acompanha se a pessoa usa a IA só para melhorar um e-mail ou para gerar um resultado relevante.
3. **O que não deu certo.** O modelo de posicionamento de sementes parou porque a troca de variedades era mais rápida que o histórico; a extensão para recomendação nutricional não avançou na época. Na visão computacional, o modelo evoluiu mais que a robotização: o gargalo agora é o hardware de coleta.
4. **Alicerces e sequência.** O repositório central de dados existia antes da IA, com foco em dado correto, e isso ajudou muito. A IA generativa cria uma exigência nova: se uma política ou um manual está desatualizado, ela traz informação desatualizada; documentos e padrões operacionais precisam de atualização regular. Dado interno vale mais que recomendação genérica: os experimentos próprios, de vários anos e ambientes, geram curvas de recomendação por fazenda com mais confiança que qualquer IA externa. Manter os dados no próprio ambiente tem custo mensal elevado, mas a IA agora permite extrair valor desse volume.
5. **Governança e riscos.** Um comitê de IA multidisciplinar reúne tecnologia, treinamento e letramento, e cibersegurança. Há política sobre o que pode e o que não pode, e os guardrails estão sendo estabelecidos agora. A orientação é não colocar dado sensível em ferramentas abertas, usadas sobretudo nas fazendas para produtividade pessoal. Todo acesso a IA no ambiente interno é registrado: sabe-se quem usou, como e até quanto consumiu. Quatro ferramentas de IA atuam embutidas nos produtos de cibersegurança. O assistente corporativo atende a maioria; outro modelo está liberado para cerca de 100 pessoas, para quem comprovou a necessidade, os champions e as pessoas de referência, e a área de tecnologia tem mais licenças. Está em construção uma camada única de acesso: o usuário consulta vários agentes (do assistente corporativo, do sistema de gestão e de outros produtos) num só lugar, com acesso conforme o perfil, sem precisar saber qual IA responde. A restrição a modelos chineses ainda não foi discutida; o uso começou pelos americanos.
6. **Organização e pessoas.** O time de dados e IA centraliza os projetos (predição de plantio e colheita, recomendação nutricional, entre outros) e a organização dos agentes; cada área cria seus agentes. A estrutura de champions em cada gerência é recente: essas pessoas recebem treinamento e disseminam, "senão é muita coisa, e a empresa é grande". O desafio do próximo ano é a educação: incluir mais gente, porque o acesso ainda é restrito. Há dois letramentos: o da ferramenta e o analítico, saber analisar e saber o que pedir. O treinamento genérico qualquer fornecedor dá; o que falta é o letramento aplicado à fazenda, com quem una conhecimento agronômico e de IA.
7. **IA generativa e agentes.** Agente de documentação em uso por todos; agentes simples via assistente corporativo; cada área criando agentes; camada única de acesso em construção. A IA generativa também acelera a visão computacional: de cada imagem se geram cerca de 30 variações de luz e ângulo, o que reduziu muito a captura de campo no último ano, embora um conjunto mínimo de imagens reais continue necessário.
8. **Campo e sistemas autônomos.** A autonomia não tem volta, mas o horizonte não é curto. Drones já avançam na coleta e na aplicação; o monitoramento autônomo, cruzado com clima e armadilhas, vai ampliar a recomendação. A operação autônoma de grande porte (trator, robô de aplicação) vai demorar: muitas empresas procuram, tudo ainda em teste. Comandar uma máquina sem insumo é fácil; distribuir semente, fertilizante ou defensivo exige autorização de cada fabricante, e não há protocolo comum no Brasil. A empresa prepara a base: o mesmo talhão em todas as plataformas, projeto de linhas e taxa variável, porque a máquina autônoma terá de ler juntos a ordem de serviço, a instrução geográfica e a dose variável. "Essa capacidade geográfica vem antes da máquina autônoma."
9. **Dados, parceiros e soberania.** Visão computacional em parceria com uma startup em que a empresa investe; sempre ao menos 10 pós-graduandos de universidades ajudam a rotular as imagens, cerca de 100 mil por ano, de equipes de monitoramento, drones e câmeras em robôs. A empresa contribui com histórico de dados para uma plataforma externa. Prefere o dado interno ao externo para recomendações. Modelos chineses ainda sem política.
10. **Futuro.** Tudo muda muito rápido; "os problemas que todo mundo vai passar são os mesmos", mesmo com empresas em pontos diferentes do caminho. Para 2027: medir o retorno, ampliar o acesso e investir em educação.

## Citações anonimizadas relevantes

> "Quando ele estava posicionando uma variedade, já surgia uma nova." (liderança de agricultura digital, grande grupo de grãos e fibras, sobre o modelo de sementes que parou)

> "Vai se trabalhando mais por uso, não por retorno." (liderança de agricultura digital, grande grupo de grãos e fibras)

> "Se a política ou o manual está desatualizado, a IA generativa vai trazer informação desatualizada." (liderança de agricultura digital, grande grupo de grãos e fibras)

> "Tem um letramento que é da ferramenta, mas tem outro que é ter capacidade analítica: saber analisar, saber o que pedir." (liderança de agricultura digital, grande grupo de grãos e fibras)

> "Essa capacidade geográfica vem antes de ter a máquina autônoma." (liderança de agricultura digital, grande grupo de grãos e fibras)

> "Os problemas que todo mundo vai passar são os mesmos." (liderança de agricultura digital, grande grupo de grãos e fibras)

## Implicações por frente

- **Frente 1:** o valor técnico mais claro está na IA preditiva e na visão computacional, com anos de dados e de rotulagem; a IA generativa entrega tempo (front-end mais rápido, agente de documentação) e é controlada por uso e orçamento, não por retorno. Caso de insucesso útil: o modelo que parou porque a variável mudava mais rápido que o histórico.
- **Frente 2:** a mais madura das quatro sessões: governança, dados e pessoas no 3. A passagem para o 4 depende de medir o retorno (meta de 2027), ampliar o acesso e o letramento analítico, e manter os documentos atualizados para a IA generativa.
- **Frente 3:** autonomia certa, mas longe para operações com insumo, por falta de protocolo comum entre fabricantes; a base geográfica é o pré-requisito; dados sintéticos reduzem a captura de campo; camada única de agentes como tendência de arquitetura.

## Implicações por pilar de IA

- **IA preditiva (aprendizado de máquina):** o pilar mais antigo e com mais resultado: posicionamento de sementes (parou), visão computacional de pragas e doenças, predição de plantio e colheita, recomendação nutricional.
- **IA generativa e agentes:** agente de documentação para todos, agentes por área, camada única em construção, controle por uso e orçamento.
- **Automação e máquinas autônomas:** drones e monitoramento primeiro; operação com insumo depende de protocolos; base geográfica pronta.
- **Sustentabilidade:** não abordada.

## Para as próximas sessões

- Mostrar a régua de 5 estágios (não foi mostrada).
- Perguntar sobre sustentabilidade da IA e referências internacionais.
- Testar os sinais desta sessão: retorno medido por uso e orçamento, não por resultado; documentos atualizados como exigência da IA generativa; base geográfica antes da autonomia; letramento analítico.
