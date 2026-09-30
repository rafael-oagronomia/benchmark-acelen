# Lista de documentos

Registro de todos os documentos do projeto, com número e revisão. A Especificação Técnica da Acelen exige em todo documento uma legenda com Contratante, Nome do Documento, Número do Documento e Revisão. Esta lista evita números repetidos entre os dois consultores.

## Numeração

`BIA-ACL-<TIPO>-<NN> · Rev. <RR>`

- **BIA-ACL**: Benchmarking de uso de IA para a Acelen.
- **TIPO**: código de duas letras da tabela abaixo.
- **NN**: sequencial dentro do tipo, a partir de 01.
- **Rev.**: começa em 00. Sobe uma revisão (01, 02…) a cada nova emissão de um documento que a Acelen já recebeu. Ajustes internos antes da primeira emissão não mudam a revisão.

| Tipo | Documento |
|---|---|
| GP | Gestão do projeto |
| PP | Protocolo de pesquisa |
| SE | Sessões executivas |
| FM | Framework de maturidade e roadmaps |
| BD | Base de dados em Excel |
| RP | Relatórios parciais |
| RF | Relatório final em PowerPoint |
| WS | Workshop Executivo |

## Registro

| Número | Rev. | Documento | Arquivo | Situação |
|---|---|---|---|---|
| BIA-ACL-SE-01 | 00 | Roteiro das sessões executivas | [roteiro-sessoes-executivas.pdf](../05_sessoes-executivas/roteiro-sessoes-executivas.pdf) | Uso interno |
| BIA-ACL-PP-01 | 00 | Protocolo de pesquisa e ficha padrão de benchmark | [protocolo-pesquisa.md](../01_mobilizacao/protocolo-pesquisa.md) | Em elaboração |
| BIA-ACL-FM-01 | 00 | Framework de maturidade em IA | [framework-maturidade.pdf](../03_frente-2_maturidade-roadmaps/framework-maturidade.pdf) | Em elaboração |
| BIA-ACL-BD-01 | 00 | Base de dados do benchmark | [base-dados-excel/](../07_entregaveis/base-dados-excel/) | Estrutura pronta, sem fichas |
| BIA-ACL-WS-01 | 00 | Desenho e roteiro de condução do Workshop Executivo | [desenho-workshop.md](../07_entregaveis/workshop-executivo/desenho-workshop.md) | Em elaboração |

**Situação:** em elaboração → revisão interna → emitido para a Acelen → aprovado. "Uso interno" indica documento que não vai para a Acelen.

Ao criar um documento, reserve o número aqui no mesmo commit.
