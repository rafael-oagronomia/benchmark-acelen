# Gestão do projeto

Reuniões semanais de acompanhamento (remotas, ~45 min) com a Estratégia Agrícola: registro de avanço, próximos passos e pontos de decisão. Toda reunião é gravada, transcrita e compartilhada com a Acelen.

## Cronograma

| Período | Atividades | Marco |
|---|---|---|
| Semana 1 — 17–21/08 | Mobilização, kick-off, validação do painel e do protocolo, agenda das sessões executivas | Kick-off · Painel e protocolo aprovados |
| Semanas 2–3 — 24/08–04/09 | Frente 1: coleta e análise; início das sessões executivas; primeiras fichas | Reuniões semanais |
| Semana 4 — 07–11/09 | Frente 2: framework, estágios, capacidades, dependências e roadmaps; fim das sessões | Entrega parcial (≈ 11/09) |
| Semana 5 — 14–18/09 | Frente 3: tendências; síntese analítica; estrutura do relatório | Prévia do relatório |
| Semana 6 — 21–29/09 | Fechamento do PowerPoint e do Excel; alinhamento prévio; workshop | Workshop Executivo — 29/09 |

## Pastas

- `reunioes/` — todas as reuniões do projeto (kick-off, semanais, entrega parcial, workshop). Um arquivo por reunião e tipo:
  - `AAAA-MM-DD_<tipo>_transcricao.md` — transcrição em texto (tipo: `kickoff`, `semanal`, `entrega-parcial`, `workshop`);
  - `AAAA-MM-DD_<tipo>_ata.md` — ata com decisões e próximos passos, quando houver.
  - `_originais/` — .docx exportado do Teams e gravações. **Fica fora do Git**; quem precisar pede ao Guilherme.
  - Para converter uma nova transcrição do Teams: `python converter_transcricao.py _originais/ARQUIVO.docx AAAA-MM-DD_tipo_transcricao.md --titulo "..."`. Use `--omitir <tempos>` para retirar trechos sobre pagamento ou condições comerciais, que nunca vão para o repositório.

| Data | Reunião | Arquivos |
|---|---|---|
| 29/09/2026 | Kick-off | [transcrição](reunioes/2026-09-29_kickoff_transcricao.md) |

## Gestão de dados

Ao final, todos os dados, registros e artefatos vão para a Acelen; a OagronomIA mantém cópia por 90 dias e depois exclui. Dados sensíveis só com o ponto focal indicado pela Acelen.
