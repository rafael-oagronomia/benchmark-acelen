# Protocolo de pesquisa

Regras comuns para coletar, registrar, classificar e comparar evidências nas três frentes. O protocolo existe para garantir duas coisas: toda afirmação do estudo é rastreável até uma fonte, e duas pessoas que leem as mesmas fontes chegam à mesma nota.

**BIA-ACL-PP-01 · Rev. 00** (em elaboração). Complementa o roteiro das sessões executivas ([BIA-ACL-SE-01](../05_sessoes-executivas/roteiro.md)) e o framework de maturidade ([BIA-ACL-FM-01](../03_frente-2_maturidade-roadmaps/framework-maturidade.md)).

## 1. Perguntas de pesquisa

| Frente | Pergunta central | Produto |
|---|---|---|
| 1 — Benchmark estratégico | Como as empresas líderes usam IA como diferencial estratégico, o que funcionou, o que falhou e por quê? | Fichas por empresa e leitura transversal |
| 2 — Maturidade e roadmaps | Em que estágio cada empresa está, o que precisou existir antes de cada salto, e em que sequência e ritmo o mercado avança? | Framework, régua, posicionamento do painel, roadmaps observados |
| 3 — Tendências | Que movimentos vão moldar a IA no agro até 2030, e o que significam para uma empresa de bioenergia com cultura perene de baixa mecanização? | Leitura prospectiva, oportunidades e riscos |

## 2. Painel de empresas

### Critérios de inclusão

- **Porte:** grande empresa, entre as maiores do seu segmento no Brasil ou referência internacional no seu setor.
- **Setor:** agro, agroindústria, bioenergia, florestal ou correlato. Nas 2 a 3 referências externas: financeiro, tecnologia, farmacêutico ou energia.
- **Jornada de IA:** IA em uso ou jornada estruturada, com evidência pública.
- **Evidência suficiente:** ao menos 3 fontes independentes publicadas desde 2023, sendo pelo menos 1 de nível A (seção 3).
- **Diversidade:** o painel cobre subsetores diferentes (ex.: sucroenergético, florestal, grãos, cooperativa) e ao menos um caso internacional de destaque em mecanização, drones ou máquinas autônomas.

### Critérios de exclusão

- Fornecedores de tecnologia como empresa do painel. Eles entram como fonte, não como objeto do benchmark.
- Empresas cuja evidência depende só de material de fornecedor ou de imprensa sem atribuição.

### Composição e identificação

- 5 a 10 empresas do agro e correlatos (**E01** a **E10**) e 2 a 3 referências de outros setores (**R01** a **R03**).
- O painel é validado com a Acelen antes da coleta aprofundada. Trocas depois disso entram na semanal como ajuste de direcionamento.

## 3. Fontes

### Níveis de confiabilidade

| Nível | O que conta | Exemplos |
|---|---|---|
| **A — primária** | Quem produziu o fato: a própria empresa, para fatos da empresa; o próprio autor, para estudos, normas e dados de mercado | Relatório anual, integrado ou de sustentabilidade; formulário de referência ou 20-F; apresentação a investidores; comunicado oficial; fala de executivo nomeado em evento registrado; relatório original de consultoria, norma ou dado oficial |
| **B — secundária qualificada** | Terceiro reconhecido, com atribuição clara | Imprensa especializada com entrevista; case de fornecedor com a empresa nomeada; estudo setorial ou acadêmico que cita a empresa |
| **C — indireta** | Sinal sem confirmação de quem produziu o fato | Notícia sem atribuição; vagas de emprego; patentes; posts em redes; inferência dos consultores |

- **Janela:** prioridade para 2023–2026. Fontes mais antigas só para reconstruir trajetórias.
- **Material de fornecedor** tende a inflar resultados. Use para confirmar que uma iniciativa existe, não para medir o resultado, a menos que a própria empresa o confirme.
- **Ebook Gatua (camada 3, exclusiva):** citar com atribuição, sem reproduzir trechos longos.
- **Diagnóstico da Fundação ABC:** referência de formato e método. Nenhum dado da Fundação entra nos entregáveis da Acelen.

### Registro

- Toda fonte entra no [catálogo de fontes](../06_fontes/catalogo-fontes.csv) **antes** de ser usada, com ID sequencial (F-0001, F-0002…).
- No texto, a afirmação termina com o ID entre colchetes: "assistente interno para toda a força de trabalho [F-0042]".
- Afirmação sem ID não entra em entregável. Leitura própria dos consultores é sinalizada como "leitura OagronomIA".
- Guarde a URL exata e a data de acesso. Em PDFs, anote a página nas observações.

## 4. Coleta

1. **Varredura** por empresa × dimensão, com apoio de IA (buscas estruturadas e lista de fontes candidatas).
2. **Triagem:** descartar duplicadas e fontes sem data; priorizar nível A.
3. **Curadoria humana:** abrir a fonte, confirmar o trecho e anotar a página.
4. **Registro** no catálogo e na ficha.
5. **Classificação** pela régua (seção 6).
6. **Revisão cruzada** pelo outro consultor.

A IA acelera a varredura e a triagem. A confirmação de cada fato é sempre humana.

## 5. Ficha padrão de benchmark

Uma ficha por empresa, em `02_frente-1_benchmark-estrategico/fichas-benchmark/<ID>_<empresa>.md`, copiada do [modelo](../02_frente-1_benchmark-estrategico/fichas-benchmark/_modelo-ficha.md). O cabeçalho (entre as linhas `---`) guarda os campos comparáveis que alimentam a base Excel. O corpo guarda as evidências e a narrativa.

| Bloco | Conteúdo | Aba da base Excel |
|---|---|---|
| Identificação | ID, empresa, setor, subsetor, país, tipo de capital, porte | Painel |
| Trajetória | Linha do tempo de marcos de IA (ano, marco, fonte) | — |
| Dimensões | Evidências, nota de 1 a 5 e confiança (A, B ou C) em governança, dados, organização e aplicações | Classificação |
| Lentes | Nível de 0 a 5 em IA generativa e em campo e sistemas autônomos | Classificação |
| Casos | O que funcionou, o que não funcionou e a causa principal, lições | — |
| Estágio consolidado | Calculado pela regra da régua | Classificação |
| Fontes | IDs do catálogo | Fichas |

**Regras de preenchimento**

- Toda evidência termina com o ID da fonte.
- **Sem evidência, sem nota.** Se não houver evidência pública para uma dimensão, a nota fica vazia e a lacuna é registrada. Falta de evidência pública não equivale a nota 1.
- Causa principal de casos que não deram certo, com a mesma taxonomia do roteiro das sessões: dados, infraestrutura, governança, pessoas, fornecedor ou expectativa.
- Aplicações descritas de forma genérica: sem marcas nem modelos de maquinário, sem avaliar ferramentas.
- Situação da ficha: rascunho → revisada (pelo outro consultor) → validada (depois de apresentada na semanal).

## 6. Classificação

- Use a [régua de classificação](../03_frente-2_maturidade-roadmaps/regua-classificacao.md).
- Cada dimensão recebe a nota do **maior nível cujos critérios são todos atendidos** com evidência.
- **Confiança da nota:** o nível da evidência mais forte que sustenta o critério do nível atribuído. Notas 4 e 5 exigem ao menos uma evidência A.
- **Estágio consolidado:** calculado pela regra da régua, a partir das quatro notas.
- **Dupla leitura:** um consultor classifica e o outro revisa. Divergência de mais de 1 ponto é discutida e o motivo fica registrado na ficha.

## 7. Sessões executivas

- Seguem o roteiro BIA-ACL-SE-01. Registros anonimizados em `05_sessoes-executivas/registros-anonimizados/`.
- Os insights entram agregados, atribuídos a "sessões executivas". Nunca servem de base para a nota de uma empresa do painel.
- O estágio autodeclarado nas sessões é comparado com a régua como leitura "declarado × evidenciado".

## 8. Qualidade

Antes de uma ficha ou seção entrar em entregável:

- [ ] Toda afirmação tem ID de fonte registrado no catálogo.
- [ ] Números com unidade, ano e base amostral.
- [ ] Nenhuma marca ou modelo de máquina; nenhuma avaliação de ferramenta.
- [ ] Nenhum dado das sessões que identifique pessoa ou empresa.
- [ ] Nenhuma condição comercial da proposta.
- [ ] Revisão cruzada feita.
