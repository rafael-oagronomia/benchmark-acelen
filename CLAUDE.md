# Benchmark de uso de IA — Acelen Renováveis

Projeto da OagronomIA para a Acelen Energia Renovável: benchmarking do uso de IA como diferencial estratégico em empresas líderes do agro, bioenergia, florestal e setores correlatos. O escopo completo está em [docs/proposta/escopo-proposta.md](docs/proposta/escopo-proposta.md) — ele é a referência do que precisa ser entregue.

## Documentos de referência

- [docs/proposta/escopo-proposta.md](docs/proposta/escopo-proposta.md) — escopo contratado (proposta sem condições comerciais). É o checklist do que entregar.
- [docs/proposta/proposta-tecnica_20260722-ACL_rev00_sem-condicoes-comerciais.pdf](docs/proposta/proposta-tecnica_20260722-ACL_rev00_sem-condicoes-comerciais.pdf) — a proposta técnica completa no design system, sem as condições comerciais (fonte em `docs/proposta/src/proposta-tecnica.html`). É a versão que pode ser compartilhada (ex.: equipe de PMO da Acelen).
- [docs/especificacao-acelen/](docs/especificacao-acelen/) — Especificação Técnica GEA (03/06/2026), elaborada pela própria Acelen; deu origem à proposta. Requisitos do cliente em caso de dúvida.
- [docs/referencias/Apresentacao_Diagnostico_IA_com_Benchmark_HUMANIZADA.pdf](docs/referencias/Apresentacao_Diagnostico_IA_com_Benchmark_HUMANIZADA.pdf) — diagnóstico de IA com benchmark feito para a Fundação ABC, apresentado à Acelen na negociação e bem recebido. Referência de linguagem, profundidade e estrutura para os entregáveis.
- [docs/referencias/Gatua_Meeting_E01_2026_TI-do-Futuro.pdf](docs/referencias/Gatua_Meeting_E01_2026_TI-do-Futuro.pdf) — ebook Gatua "TI do Futuro" (maio/2026): painéis e pesquisa com 84 respondentes do agro. Fonte secundária para Frentes 1 e 3; citar com atribuição, não reproduzir. Detalhes em [docs/referencias/README.md](docs/referencias/README.md).
- [docs/acelen/repertorio-acelen.md](docs/acelen/repertorio-acelen.md) — repertório do cliente (fontes públicas, corte 30/09/2026): grupo, Acelen Renováveis, macaúba, onde atuam, tecnologia/IA, mercado, necessidades, implicações para o benchmark, perguntas a validar e temas sensíveis. Ler antes de reuniões e entregáveis. Fontes baixadas em `_triagem-pesquisa/_acelen/` (fora do Git).
- [docs/design-system/OagronomIA-DesignSystem.md](docs/design-system/OagronomIA-DesignSystem.md) — design system da OagronomIA. Fonte única de verdade visual para relatório PowerPoint, Excel, materiais parciais e workshop. Logo em `docs/design-system/assets/logo-oagronomia-wordmark.png` (fundo preto; sobre `--bg-0` usar `mix-blend-mode: lighten`).

## Gerar PDFs

Documentos em PDF saem de um HTML-fonte (pasta `src/` ao lado do PDF) impresso pelo Chrome headless:

```bash
"/c/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=15000 --print-to-pdf="<saida.pdf>" "file:///<caminho>/src/<doc>.html"
```

## Regra de confidencialidade comercial (obrigatória)

Nunca mencionar, em nenhum arquivo, commit, entregável ou resposta, as condições comerciais da proposta: valor global, honorários, horas alocadas, valor-hora, despesas, impostos, forma de pagamento ou parcelas. O PDF original da proposta contém esses dados e **não** deve ser versionado.

## Repositório leve (obrigatório)

O Git guarda só documentos leves: markdown, planilhas-índice, código, JSONs de catálogo e os PDFs finais de entregáveis. Arquivos brutos ficam fora do repositório, só na máquina do Guilherme; quem precisar (ex.: o Rafael) pede a ele. São brutos:
- PDFs e páginas baixados na pesquisa (`_triagem-pesquisa/`, inclusive `_acelen/`) e resultados do Perplexity — versionar só `LEIA-ME.md`, `ACESSO-MANUAL.md`, `CATALOGO.xlsx`, `_catalogo/*.json` de entrada e `_ferramentas/*.py`;
- originais de reuniões (.docx do Teams, gravações de áudio/vídeo) em `00_gestao/reunioes/_originais/` — versionar só a transcrição e a ata em `.md`;
- qualquer arquivo acima de ~5 MB, salvo combinado com o Guilherme.

Antes de cada commit, confira `git status` e o tamanho do que entra; o `.gitignore` já cobre esses casos.

## Convenções

- Todos os documentos em português.
- Todo entregável leva a legenda de identificação: Contratante (Acelen Energia Renovável), Nome do Documento, Número do Documento e Revisão.
- Abordagem macro, exploratória e qualitativa: não avaliar nem recomendar ferramentas específicas de IA, nem desenhar soluções internas (governança de TI da Acelen).
- Sessões executivas: nomes de executivos e empresas participantes nunca aparecem — insights só de forma agregada e anonimizada.
- Toda afirmação do benchmark deve ter fonte registrada em [06_fontes/](06_fontes/).
