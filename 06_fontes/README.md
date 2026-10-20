# Catálogo de fontes

Fontes públicas e secundárias: relatórios anuais e de resultados de companhias abertas, relatórios setoriais e de consultorias, publicações científicas e técnicas, imprensa especializada e bases de inovação.

A IA pode ser usada para acelerar varredura e triagem, sempre com curadoria e validação humana.

## Como funciona

- **Catálogo completo** (tudo o que foi levantado): [`_triagem-pesquisa/CATALOGO.xlsx`](../_triagem-pesquisa/CATALOGO.xlsx) e o índice [`LEIA-ME.md`](../_triagem-pesquisa/LEIA-ME.md). Cada fonte tem um **ID estável** (M001, M002…), guardado em `_triagem-pesquisa/_catalogo/ids.json`: um item nunca muda de ID, mesmo quando o catálogo é reconsolidado.
- **Como citar** nas notas, fichas e entregáveis: `[M123, p. 4]`, ou `[M123; M045, p. 2-3]` para mais de uma fonte. Página web: `[M123, web]`. No fim de cada documento, deixar as marcas:

  ```
  ## Fontes
  <!-- fontes:inicio -->
  <!-- fontes:fim -->
  ```

- **Registro:** `python 06_fontes/registrar_fontes.py` preenche a lista de fontes de cada documento (organização, ano, título, link e páginas citadas, sempre a partir do catálogo) e gera:
  - [fontes-citadas.md](fontes-citadas.md): registro geral das fontes usadas no estudo, com os documentos em que aparecem;
  - `fontes-citadas.json`: a mesma lista, com métricas e resumos, para a base de conhecimento do assistente de IA.

  O script aponta IDs citados que não existem no catálogo. Fonte nova entra primeiro no catálogo (rodada em `_triagem-pesquisa/_catalogo/` e `consolidar.py`), depois é citada.

O registro geral alimenta a aba de fontes da base em Excel e a base de conhecimento do assistente de IA do estudo ([07_entregaveis/assistente-ia/](../07_entregaveis/assistente-ia/)).

## Catálogo da Frente 2 e da base Excel

O framework de maturidade e a régua citam fontes por outro ID (`[F-0001]`), registradas em [catalogo-fontes.csv](catalogo-fontes.csv) com:

- ID (F-0001, F-0002…);
- título, autor ou organização, data de publicação e URL;
- tipo e nível de confiabilidade (A, B ou C);
- acesso, empresas e frentes relacionadas;
- onde foi usada, data de acesso e observações (página, trecho).

Hoje é esse catálogo que o `gerar_base.py` lê para a aba Fontes da base Excel. As regras de registro e citação estão no [protocolo de pesquisa](../01_mobilizacao/protocolo-pesquisa.md), seção 3. Os IDs F e M ainda não foram unificados.
