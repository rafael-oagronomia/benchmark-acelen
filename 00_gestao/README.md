# Gestão do projeto

Reuniões semanais de acompanhamento (remotas, ~45 min) com a Estratégia Agrícola: registro de avanço, próximos passos e pontos de decisão. Toda reunião é gravada, transcrita e compartilhada com a Acelen.

## Cronograma (rev. 02, 22/10/2026)

Rev. 00 de 30/09, depois do kick-off; rev. 01 de 09/10, com a situação da semanal de 09/10 e o assistente de IA do estudo entre os entregáveis; rev. 02 de 22/10, com as quatro sessões executivas concluídas (13 a 21/10) e o foco das semanas seguintes na compilação (fichas, notas, sessões e os aprofundamentos pedidos em 16/10) e no assistente de IA do estudo (RAG com os estudos). Versões para o cliente: [PDF](cronograma/cronograma_BIA-ACL-CR-01_rev02.pdf) e [planilha](cronograma/cronograma_BIA-ACL-CR-01_rev02.xlsx), com a situação de cada atividade; as revisões anteriores ficam na pasta como histórico. Fonte em `cronograma/src/` (sempre a revisão vigente).

| Período | Atividades | Marco |
|---|---|---|
| S1 — 29/09–02/10 | Kick-off, cronograma, roteiro das sessões executivas, painel e protocolo | Semanal 02/10: cronograma, roteiro e lista de empresas (pauta tratada em 09/10) |
| S2 — 05–09/10 | Frente 1: fichas, casos de sucesso e insucesso; preparação das sessões executivas | Semanal 09/10: questionário validado; Suzano e Bayer indicadas |
| S3 — 13–16/10 | Frente 1: fichas da Suzano e da Bayer, indicadores, Deere e DJI; Frente 2: revisão de frameworks; sessão executiva 1; início do assistente de IA | Semanal 16/10: prévia da Frente 1 (feita) |
| S4 — 19–23/10 | Sessões executivas 2 a 4 (concluídas); Frente 2: régua, governança e bancos; início da compilação e da base do assistente (RAG) | Semanal 23/10: **entrega parcial** |
| S5 — 26–30/10 | Frente 3: tendências; compilação e síntese analítica; estrutura do relatório; testes do assistente | Semanal 30/10: prévia do relatório |
| S6 — 03–06/11 | Fechamento do PowerPoint, do Excel e do assistente de IA | Semanal 06/11: **relatório final** e assistente de IA |
| 09/11 → workshop | Absorção pela Acelen, ajustes e preparação do workshop | — |
| Provável 1ª semana de dez | Workshop Executivo presencial no team building, em Montes Claros | Dia a confirmar pela Acelen (até 23/10) |

Feriados no período: 12/10 e 02/11. Semanais às sextas, cerca de 1 hora; horário a confirmar no convite da Acelen.

## Pastas

- `reunioes/` — todas as reuniões do projeto (kick-off, semanais, entrega parcial, workshop). Um arquivo por reunião e tipo:
  - `AAAA-MM-DD_<tipo>_transcricao.md` — transcrição em texto (tipo: `kickoff`, `semanal`, `entrega-parcial`, `workshop`);
  - `AAAA-MM-DD_<tipo>_ata.md` — ata com decisões e próximos passos, quando houver; versão para o cliente em PDF (`..._ata_BIA-ACL-AT-NN_revNN.pdf`), gerada de `src/`.
  - `_originais/` — .docx exportado do Teams e gravações. **Fica fora do Git**; quem precisar pede ao Guilherme.
  - Para converter uma nova transcrição do Teams: `python converter_transcricao.py _originais/ARQUIVO.docx AAAA-MM-DD_tipo_transcricao.md --titulo "..."`. Use `--omitir <tempos>` para retirar trechos sobre pagamento ou condições comerciais, que nunca vão para o repositório, e `--anonimizar "Nome"` para trocar por [nome omitido] o nome de executivos que possam participar das sessões executivas.

  - `AAAA-MM-DD_<tipo>_pauta.md` — preparação interna da reunião.

| Data | Reunião | Arquivos |
|---|---|---|
| 29/09/2026 | Kick-off | [ata e pendências](reunioes/2026-09-29_kickoff_ata.md) ([PDF rev. 01](reunioes/2026-09-29_kickoff_ata_BIA-ACL-AT-01_rev01.pdf); a rev. 00 fica como histórico) · [transcrição](reunioes/2026-09-29_kickoff_transcricao.md) |
| 02/10/2026 | Semanal (pauta) | [preparação](reunioes/2026-10-02_semanal-01_pauta.md); os itens foram tratados na semanal de 09/10 |
| 09/10/2026 | Semanal | [ata e pendências](reunioes/2026-10-09_semanal_ata.md) ([PDF rev. 01](reunioes/2026-10-09_semanal_ata_BIA-ACL-AT-02_rev01.pdf), com a situação das pendências em 15/10; a rev. 00 fica como histórico) · [transcrição](reunioes/2026-10-09_semanal_transcricao.md) |
| 13/10/2026 | Interna (Guilherme × Rafael) | [notas](reunioes/2026-10-13_interna_notas.md): leitura da sessão 1, pilares de IA e o que a Acelen quer |
| 16/10/2026 | Semanal | [ata e pendências](reunioes/2026-10-16_semanal_ata.md) ([PDF](reunioes/2026-10-16_semanal_ata_BIA-ACL-AT-03_rev00.pdf)) · [transcrição](reunioes/2026-10-16_semanal_transcricao.md) · [preparação](reunioes/2026-10-16_semanal_pauta.md) |
| 23/10/2026 | Semanal (entrega parcial) | [preparação](reunioes/2026-10-23_semanal_pauta.md) · [roteiro do bloco dos bancos (Rafael)](reunioes/2026-10-23_semanal_roteiro-bancos.md) |

- `cronograma/` — cronograma para o cliente (PDF e planilha) e HTML-fonte.

## Gestão de dados

Ao final, todos os dados, registros e artefatos vão para a Acelen; a OagronomIA mantém cópia por 90 dias e depois exclui. Dados sensíveis só com o ponto focal indicado pela Acelen.
