# Linha de investigação — IA no campo: sistemas autônomos e IA aplicada ao agro

> Documento de trabalho da OagronomIA · Frente 3 — Tendências e perspectivas futuras · Aberto em 11/11/2026 · Protocolo do tema e estrutura da nota temática. Fica fora do assistente de IA (linha de investigação). Número novo só entra na nota depois de verificado e catalogado.

## 1. Por que o tema entra

- **Está no escopo.** Dois itens do [README da Frente 3](README.md) seguem abertos:
  - **sistemas autônomos:** agentes de IA, máquinas autônomas, drones e robótica de campo, com atenção a culturas perenes e de baixa mecanização (contexto da macaúba) e à escassez de mão de obra;
  - **IA aplicada ao agro:** agricultura de precisão, sensoriamento remoto, modelos preditivos e apoio à decisão agronômica e industrial.
- **Foi pedido na semanal de 30/10** ([transcrição anonimizada](../00_gestao/reunioes/2026-10-30_semanal_transcricao.md), 53:29 a 1:04:46; pendência 23 da ata AT-04):
  - um panorama de como a IA chega ao campo, "não olhando só para trás do computador";
  - casos de uso com resultado operacional, olhando para culturas perenes (florestal, café, citros);
  - se a IA já decide sozinha no campo, dentro de regras, ou se a decisão segue humana;
  - como as empresas juntam a mecanização e a IA: se a informação da IA já vira operação de máquina ou se as duas coisas ainda andam separadas.
- **Edição genética** (mesma transcrição, 1:11:06 a 1:12:30; pendência 28): a técnica CRISPR e o uso de IA no melhoramento, com interesse no melhoramento de uma palmeira perene em domesticação.
- **O roteiro de adoção passou a trilha do campo para cá** ([roadmap-de-adocao.md](../03_frente-2_maturidade-roadmaps/roadmap-de-adocao.md), seção 11): conectividade, dados agronômicos, processamento na borda, níveis de autonomia de máquinas, normas de segurança e culturas perenes de baixa mecanização.
- **Escopo.** Macro e de mercado: o que as empresas e os produtores fazem no campo, com que resultado e o que trava o avanço. A nota não avalia nem recomenda máquina, fornecedor ou ferramenta, e não desenha a operação de campo da Acelen (regra do projeto). Fabricante e fornecedor entram só como caso público, rotulados.

## 2. O que o acervo já tem

**A base mais pronta é a lente de campo do framework do Rafael** (ramo `origin/rafael/estruturacao-analitica-frente-2`, `framework-maturidade.md`, seção 8, para discussão). Ela traz:
- os níveis de operação de campo (enxergar, antecipar, executar com precisão, delegar tarefas, supervisionar a autonomia), montados sobre a FAO [M183], a tipologia de gêmeos digitais [M1227] e a sequência da Embrapa [M1213];
- a norma ISO 18497-1:2024, que recusou de propósito uma escala única de níveis para máquinas agrícolas [M1231];
- onde o campo está no Brasil, na América Latina e na China;
- as palmeiras de baixa mecanização, com a palma de óleo como análogo mais próximo da macaúba;
- as dependências da autonomia.

As fontes dessa seção já estão no catálogo (rodada 10). Os IDs F do Rafael viram M pelo mapa `_triagem-pesquisa/_catalogo/mapa_F_rafael_para_M.json`.

| Bloco | IDs no catálogo (ponto de partida, a reler na página) |
|---|---|
| Níveis de autonomia e normas | M183, M368, M1213, M1225, M1227, M1228, M1229, M1230, M1231 (pago) |
| Adoção no campo em números | M021, M045 (bloqueado), M006, M022, M281, M279, M307, M301, M249, M280, M273, M308, M186 |
| Conectividade e infraestrutura | M1214, M270, M179, M1218, M1220, M1222, M1224 |
| Máquinas, drones e robótica | Fichas da Deere e da DJI; M370, M391, M387, M412, M829, M825, M836, M408, M314, M325, M822, M827, M880, M838, M288 |
| IA física e robótica (mercado) | M016, M034, M061, M088, M295 |
| Casos no Brasil (campo) | Suzano (M753, M338, M749, M764, M774); SLC (M331, M332, M355, M1220); Raízen (M329); São Martinho (M356, M358, M1218); Tereos (M360); Klabin (M326); Amaggi (M321, M322); Atvos (M340, M1224); BP Bunge (M1217, M1223); Solinftec (M253, M254, M257, M385, M405, M289) |
| Perenes: café e citros | M247, M237, M241, M242, M366, M346, M348, M349 |
| Perenes: florestal | Ficha da Suzano; M324, M343, M347, M326 |
| Perenes: palma e macaúba | M375, M377, M382, M383, M384, M398, M400, M401, M402, M404, M1232, M1233, M1234, M1235, M1236; macaúba: M1226, M239 |
| Frutas e robôs de colheita | M376, M407 |
| Mão de obra | M386, M245, M246, M255, M297, M278, M317, M1235 |
| IA aplicada (precisão, preditivos, decisão) | M009, M044, M037, M180, M200, M235, M243, M275, M276, M310, M311, M298, M367, M389 |
| Melhoramento e edição genética | Ficha da Bayer (M789, M790, M791); M755 (Tetrys, Suzano); M778 (eucalipto geneticamente modificado, FuturaGene) |
| China e EUA no campo | Nota [EUA × China](eua-x-china-ia-no-agro.md): M378, M379, M380, M824, M831, M841, M1237, M823, M834, M835 |

## 3. Perguntas centrais

1. **Onde a IA está no campo hoje,** por nível de operação e por tipo de cultura (grãos, cana, florestal, perenes de fruto)?
2. **Que casos têm resultado operacional publicado** (custo, produtividade, perdas, mão de obra, tempo até a decisão), com escopo e classe de evidência?
3. **A IA decide sozinha no campo?** Onde a decisão segue humana, onde a máquina executa uma prescrição e onde há autonomia supervisionada?
4. **O que trava a passagem para a autonomia:** conectividade e sinal de posicionamento, processamento na máquina, normas e segurança, custo, dados agronômicos, pessoas, terreno e cultura?
5. **Culturas perenes e de baixa mecanização** (palma, café, citros, frutas, florestal, e a macaúba como cultura de interesse): o que é viável hoje, o que está perto do mercado e o que segue em pesquisa? Que tentativas não vingaram?
6. **Mão de obra:** qual o tamanho da escassez no Brasil e nas perenes, e o que a automação resolve de fato?
7. **Adoção em números:** existe pesquisa de mercado sobre o uso de IA no campo na era da IA generativa (2024 a 2026), no Brasil e no mundo, por cultura ou porte?
8. **Melhoramento e edição genética:** como a IA acelera o melhoramento (seleção genômica, fenotipagem, desenho da edição)? Onde já há produto ou resultado? Como o Brasil regula a edição genética? O que existe em perenes e palmeiras?
9. **Infraestrutura que destrava:** processamento na própria máquina (borda) e conectividade direta por satélite. O que já está em operação no Brasil?

## 4. Hipóteses de partida

O Guilherme não trouxe hipótese própria (11/11/2026). As hipóteses abaixo vêm das falas da equipe na semanal de 30/10 e da lente de campo do framework do Rafael. Servem para testar, não para afirmar.

| # | Hipótese | De onde vem | O que confirmaria ou derrubaria |
|---|---|---|---|
| H1 | **A IA encurta o tempo até a decisão, mas a decisão segue humana.** O mapa de falhas de plantio passou de cerca de um mês para um dia | Fala da equipe (56:12 a 58:05) | Casos com o tempo antes e depois; casos em que a máquina decide sozinha dentro de regras |
| H2 | **A cadeia "IA diagnostica, central decide, máquina executa" ainda não opera integrada como rotina.** Na lente: executar com precisão (nível 3) é maduro; delegar tarefas (4) está perto do mercado; supervisionar a autonomia (5) está em protótipo | Fala da equipe (59:32); framework do Rafael, seção 8 | Frotas autônomas em operação regular, com área ou horas; prescrição que vai da imagem à máquina sem etapa manual |
| H3 | **O processamento vai para a máquina (borda),** porque levar gigabytes de imagem ao escritório atrasa a decisão | Fala da equipe (59:51 a 1:01:43) | Equipamentos com processamento embarcado em operação; ganho de tempo medido |
| H4 | **A conectividade direta por satélite começa a superar a falta de sinal em escala.** Uma operadora lançou, com a Starlink, conexão do celular direto ao satélite | Fala da equipe (1:01:58 a 1:02:52) | Data, cobertura e limites da oferta; uso em máquinas e sensores, não só em celular; dados de cobertura rural |
| H5 | **Não há número de mercado sobre adoção de IA no campo na era da IA generativa,** por cultura | Fala da equipe (1:04:23 a 1:04:46) | Pesquisas com produtores de 2024 a 2026; já há uma: 26% dos grandes produtores da América Latina usavam IA generativa em 2026 [M021] |
| H6 | **Nas palmeiras de baixa mecanização, enxergar e antecipar já são viáveis; executar existe na aplicação por drone; a colheita autônoma está em pesquisa há mais de 20 anos** | Framework do Rafael [M1233; M1234; M1235; M1236; M1232] | Casos comerciais de colheita mecanizada ou robótica em palma; números de mecanização da colheita |
| H7 | **A fundação de campo vem antes da IA de campo e leva de 3 a 5 anos** (conectividade e centro de operações) | Framework do Rafael; nota do roteiro, seção 4 | Jornadas datadas de empresas brasileiras |
| H8 | **A escassez de mão de obra é o motor da automação nas perenes** | M245; M255; M402; M1235 | Dados de escassez por cultura; casos em que a automação substituiu tarefa manual, com número |
| H9 | **A IA acelera o desenho e a simulação no melhoramento, mas produto editado em cultura perene ainda é raro;** o gargalo é o ciclo longo da cultura e a regulação | Fala da equipe (1:12:30); M789; M778 | Produtos editados aprovados por país e cultura; casos de IA no melhoramento de perenes com ganho medido |

## 5. Estrutura proposta da nota temática

Arquivo: `04_frente-3_tendencias/ia-no-campo.md`. Entra no assistente: incluir `E-ia-no-campo` em `liberados` no `config/acervo.json` do RAG. Mesmo formato das demais notas: citação [M###, p. N], "leitura nossa", números que não devem ser usados e lacunas.

1. **Resumo em uma página.**
2. **Como ler.** A lente de níveis de operação de campo; as classes de evidência; anúncio não é resultado; piloto não é produção.
3. **Onde o campo está.** Adoção em números no Brasil, na América Latina, no mundo e na China; agtechs (oferta não é adoção); conectividade.
4. **Quem decide no campo.** Quem diagnostica, quem decide e quem executa, com casos por nível de operação.
5. **Casos com resultado operacional, por cultura.** Grãos e cana, florestal, café, citros, palma, frutas. Tabela com resultado, escopo, classe da evidência e fonte.
6. **Máquinas autônomas, drones e robótica.** O que está em operação, perto do mercado e em pesquisa; normas e segurança; tentativas que não vingaram.
7. **Culturas perenes e de baixa mecanização.** O caso das palmeiras; a macaúba como agenda de pesquisa pública, sem diagnóstico da Acelen.
8. **Mão de obra.** O tamanho da escassez e o que a automação resolve.
9. **IA no melhoramento e a edição genética.** O que a IA faz no melhoramento; a edição genética (CRISPR) e a regulação no Brasil; as perenes.
10. **A infraestrutura que destrava.** Conectividade terrestre e por satélite, sinal de posicionamento, processamento na borda, dados agronômicos.
11. **Leitura para o estudo** (leitura nossa, macro). O que é tendência consolidada e o que é sinal emergente; o que muda na lente de campo da régua (Frente 2).
12. **Números que não devem ser usados (ou só com ressalva); Lacunas; Fontes.**

**Regras desta nota:**
- referência de mercado, nunca desenho da operação da Acelen;
- não avalia nem recomenda máquina, fornecedor ou ferramenta: fabricante só como caso público, rotulado;
- dado de fabricante e de fornecedor é marcado como tal (classe D nas fichas);
- sessões executivas só no agregado, sem números e sem ligar relato a empresa;
- nada das reuniões com a Acelen;
- documento público sobre a própria Acelen fica fora: a macaúba entra pela pesquisa pública sobre a cultura.

## 6. Fontes a levantar (rodada 11 do catálogo)

**A. Máquinas autônomas, drones e robótica; mão de obra; infraestrutura**
- Máquinas autônomas e robôs em operação comercial: unidades, área ou horas, por fabricante e por país; o que exige supervisão no local.
- Tentativas que não vingaram: robôs de colheita e de lavoura que fecharam ou recuaram, com a causa declarada.
- Normas e segurança de máquinas autônomas em 2025 e 2026.
- Processamento embarcado em máquinas e drones, com ganho medido.
- Conectividade direta por satélite no Brasil (operadora e satélite): data, cobertura e limites; parcerias de conectividade de fabricantes de máquinas.
- Escassez de mão de obra no campo: números do Brasil e de outros países, por cultura.

**B. Culturas perenes e adoção em números**
- Casos com resultado operacional em palma, café, citros, frutas, florestal e cana: mecanização da colheita, drones, visão computacional, previsão de safra, detecção de doença.
- Macaúba: pesquisa pública sobre domesticação, manejo e mecanização (2020 a 2026).
- Pesquisas com produtores sobre o uso de IA (2024 a 2026), no Brasil e no mundo, com amostra e método.

**C. Melhoramento e edição genética**
- IA no melhoramento: seleção genômica, fenotipagem e desenho de edição, com ganho medido.
- Editores genéticos desenhados por IA e o uso de modelos de proteína no desenho.
- Regulação da edição genética no Brasil (CTNBio) e em outros mercados: situação em 2025 e 2026 e produtos aprovados.
- Perenes: palma (genoma e seleção genômica), eucalipto, café, citros, macaúba.

**Regras das buscas** (as do método, seção 9 do descritivo):
- nunca citar a Acelen nem o projeto;
- só fontes oficiais ou primárias; imprensa serve para localizar ou entra marcada;
- cada documento com link, organização e data, e cada número com a página de onde saiu;
- documento que pede cadastro: registrar o formulário para a equipe decidir, sem preencher;
- sem contornar login nem paywall.

## 7. Como será feito

Mesmo caminho das pesquisas dirigidas anteriores (seção 9 do descritivo da metodologia):

1. **Pesquisadores** (três agentes, A, B e C, um por bloco da seção 6). Cada um relê na página as fontes do catálogo do seu bloco, busca as novas e grava `_triagem-pesquisa/_dossies/_bruto_campo_X.json`, no formato dos dossiês anteriores: itens novos, evidências com fonte e página, formulários e lacunas.
2. **Pré-checagem** por programa: procura cada número na página citada e aponta o que não achou (`_prechecagem_campo_X.json`).
3. **Verificadores**, outros agentes. Abrem cada fonte, conferem cada afirmação e confirmam, corrigem ou retiram (`_verificado_campo_X.json`). Rodam em sequência, para não estourar o limite de uso.
4. **Catálogo:** as fontes novas entram na `rodada11.json`, e a consolidação dá os IDs.
5. **Redator,** outro agente: escreve a nota só com o que passou pela verificação, citando ID e página.
6. **Revisor,** outro agente: lê a nota tentando derrubá-la.
7. **Conferência linha a linha** por programa: IDs, páginas e números. Depois, o registro das fontes citadas e os pipelines do sistema.
8. **Report Final:** os slides de resultado dos itens 3.3 e 3.4 entram no gerador quando a nota estiver aprovada.

## Fontes
<!-- fontes:inicio -->
- **M021** — McKinsey & Company (Agriculture Practice) (2026). Global Farmer Insights 2026. [link](https://www.mckinsey.com/industries/agriculture/our-insights/global-farmer-insights)
- **M183** — FAO (2022). The State of Food and Agriculture 2022: Leveraging automation in agriculture for transforming agrifood systems. [link](https://www.fao.org/3/cb9479en/cb9479en.pdf)
- **M1213** — Embrapa; UFRPE (M. A. A. Leite, S. M. F. S. Massruhá, K. J. Coral) (2024). Agricultura digital, inovação e aplicações (cap. 2 de Inovação e desenvolvimento em cana-de-açúcar). [link](https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/1166995/1/PL-Agricultura-digital-2024.pdf)
- **M1227** — C. Verdouw, B. Tekinerdogan, A. Beulens, S. Wolfert (Wageningen) — Agricultural Systems 189 (2021 (abr/2021)). Digital twins in smart farming. [link](https://edepot.wur.nl/541204)
- **M1231** — ISO/TC 23/SC 19 (2024 (jul/2024)). ISO 18497-1:2024 — Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery — Part 1: Machine design principles and vocabulary. [link](https://www.iso.org/standard/82684.html)
- **M1232** — K. Yarak et al. — Agriculture 11(2):183 (2021 (22/02/2021)). Oil Palm Tree Detection and Health Classification on High-Resolution Imagery Using Deep Learning. [link](https://www.mdpi.com/2077-0472/11/2/183)
- **M1233** — MPOB (A. R. Shuib et al.) (2004 (jun/2004)). Development of a machine for harvesting tall palms (MPOB TT 217). [link](https://palmoilis.mpob.gov.my/publications/TOT/TT-217.pdf)
- **M1234** — MPOB; Universiti Teknologi Malaysia (2023). The Potential of Robotics for Efficient and Sustainable Harvesting (Palm Oil Engineering Bulletin 142). [link](https://palmoilis.mpob.gov.my/publications/POEB/poeb142-athif.pdf)
- **M1235** — New Straits Times, republicado pelo MPOB (Malaysian Palm Oil Board) (2024 (28/02/2024)). Palm oil industry loses RM7.9b annually due to worker shortage. [link](https://prestasisawit.mpob.gov.my/en/palmnews/news/36344)
- **M1236** — W. Li, H. Fu, L. Yu, A. Cracknell — Remote Sensing 9(1):22 (2016 (29/12/2016)). Deep Learning Based Oil Palm Tree Detection and Counting for High-Resolution Remote Sensing Images. [link](https://www.mdpi.com/2072-4292/9/1/22)
<!-- fontes:fim -->
