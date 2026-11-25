"""Gera o HTML-fonte da apresentação executiva do benchmark (BIA-ACL-AE-01).

É a versão para a apresentação final às lideranças (pedido da semanal de 11/11/2026): uma hora,
formato executivo, direto aos pontos do benchmark, com gráficos e diagramas no lugar de texto. O
detalhe de cada tema fica no Report Final (BIA-ACL-RF-01) e nas notas do estudo.

Regras deste deck:
- só resultado: nada de "o que foi feito" ou "o que falta";
- todo número vem de uma nota, ficha ou slide já conferido do estudo, com a mesma citação
  (ID do catálogo e página); a linha de fontes sai do catálogo;
- casos na lógica pedida pela Acelen: problema, iniciativa, resultado, consequência e lição;
- sessões executivas só no agregado, sem perfil de empresa, e nunca ao lado de documento público
  de empresa entrevistada;
- referência de mercado: não avalia nem recomenda ferramenta e não desenha solução interna;
- cores: só as que têm variável no sistema (o deck acompanha o tema claro ou escuro do site).

Uso: python gerar_apresentacao_executiva.py   (grava apresentacao-executiva.html nesta pasta)
PDF: Chrome headless, como os demais documentos (ver CLAUDE.md).
No sistema: npm run montar-apresentacao -- executiva 07_entregaveis/workshop-executivo/src/apresentacao-executiva.html
"""
from __future__ import annotations

import re
import sys
from datetime import date
from html import escape
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(RAIZ / "07_entregaveis/relatorio-final/src"))
import gerar_report_final as rf  # noqa: E402  (catálogo, linha de fontes e CSS da entrega parcial)
import graficos as g  # noqa: E402
import slides as conteudo  # noqa: E402
import slides_metodologia  # noqa: E402

SAIDA = AQUI / "apresentacao-executiva.html"
DOCUMENTO = "BIA-ACL-AE-01"
REVISAO = "Rev. 00"
VERSAO = "v0"
NOME = "Apresentação executiva do benchmark de uso de IA"
RODAPE = f"Acelen Energia Renovável · Apresentação executiva do benchmark · {DOCUMENTO} · {VERSAO}"
LOGO = "../../../docs/design-system/assets/logo-oagronomia-wordmark.png"
NOTAS_TEMATICAS = 10  # notas do estudo no acervo do sistema (web/lib/numeros.json, estudos.notas)

CSS_EXEC = """
  /* ---- Apresentação executiva ---- */
  .capa-il { position: absolute; right: 15mm; top: 34mm; width: 122mm; height: auto; }
  .ct { font: 400 9.5px var(--font-mono); color: var(--fg-3); }
  .msg-top { margin-top: 5px; }
  .v1 h2 { font-size: 30px; }
  .panel h3 { font-size: 14px; }
  .lg { display: flex; gap: 16px; flex-wrap: wrap; font-size: 11px; color: var(--fg-3); margin-top: 6px; }
  .lg span::before { content: ""; display: inline-block; width: 10px; height: 10px; border-radius: 3px; margin-right: 6px; vertical-align: -1px; background: var(--c); }

  /* Seis números */
  .x6 { display: grid; grid-template-columns: repeat(3, 1fr); grid-auto-rows: 1fr; gap: 12px; margin: 12px 0 10px; flex: 1; min-height: 0; }
  .x6 .c { background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; padding: 13px 16px 10px; display: flex; flex-direction: column; min-height: 0; }
  .x6 .c .top { display: flex; align-items: center; gap: 10px; }
  .x6 .c .top svg.lucide { width: 26px !important; height: 26px !important; }
  .x6 .c .k { font: 500 10.5px var(--font-display); letter-spacing: 0.14em; text-transform: uppercase; color: var(--brand-green); }
  .x6 .c .n { font: 500 42px/1 var(--font-mono); color: var(--fg-1); margin-top: 10px; letter-spacing: -0.02em; white-space: nowrap; }
  .x6 .c h3 { font-size: 16.5px; margin-top: 9px; }
  .x6 .c p { font-size: 12.6px; color: var(--fg-2); margin-top: 5px; line-height: 1.4; }
  .x6 .c .ct { margin-top: auto; padding-top: 8px; }

  /* Mapa de calor do painel */
  .hm { display: grid; grid-template-columns: 1.3fr repeat(5, 1fr); gap: 5px; margin-top: 10px; }
  .hm .h { font: 500 8.6px var(--font-display); letter-spacing: 0.05em; text-transform: uppercase; color: var(--fg-3); text-align: center; align-self: end; padding-bottom: 2px; }
  .hm .e { font: 600 13.5px var(--font-display); color: var(--fg-1); align-self: center; line-height: 1.15; }
  .hm .e small { display: block; font: 500 9.5px var(--font-body); color: var(--fg-3); }
  .hm .c { border-radius: 7px; height: 42px; display: flex; align-items: center; justify-content: center; font: 600 19px var(--font-mono); }
  .hm .c.n2 { background: #2C4A22; color: var(--fg-1); }
  .hm .c.n3 { background: #3A7A2A; color: var(--fg-1); }
  .hm .c.n4 { background: #62A842; color: #0B100B; }
  .hm .c.n0 { border: 1px dashed var(--line-strong); color: var(--fg-3); font: 500 8.5px/1.2 var(--font-body); text-align: center; padding: 0 2px; }
  .hm .c.g { box-shadow: inset 0 0 0 2px var(--fg-1); }
  .fato { display: flex; gap: 10px; align-items: baseline; margin-top: 9px; font-size: 11.8px; color: var(--fg-2); line-height: 1.38; }
  .fato .n { font: 500 21px/1 var(--font-mono); color: var(--fg-1); flex: none; min-width: 74px; white-space: nowrap; }
  .fato.k .n { font: 600 10px/1.5 var(--font-display); letter-spacing: 0.1em; text-transform: uppercase; color: var(--brand-green); min-width: 72px; }

  /* Faixa de números curtos */
  .f4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 10px; }
  .f4.c3 { grid-template-columns: repeat(3, 1fr); }
  .f4 .i { background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; padding: 9px 12px; display: flex; gap: 12px; align-items: center; }
  .f4 .i .n { font: 500 22px/1 var(--font-mono); color: var(--fg-1); flex: none; white-space: nowrap; }
  .f4 .i .t { font-size: 11.6px; color: var(--fg-2); line-height: 1.36; }
  .f4 .i .t b { color: var(--fg-1); }
  .f4 .i svg.lucide { width: 24px !important; height: 24px !important; }

  /* Caso: problema, iniciativa, resultado, consequência, lição */
  .cz { display: flex; align-items: center; gap: 12px; margin-top: 12px; }
  .cz .nm { font: 600 19px var(--font-display); color: var(--fg-1); }
  .cz .oq { font-size: 12.6px; color: var(--fg-2); }
  .cz .tg { margin-left: auto; font: 600 9.5px var(--font-display); letter-spacing: 0.1em; text-transform: uppercase; border-radius: 999px; padding: 3px 11px; border: 1px solid var(--brand-green); color: var(--brand-green-bright); white-space: nowrap; }
  .cz .tg.at { border-color: var(--warning); color: var(--warning); }
  .fluxo { display: grid; grid-template-columns: 1fr 20px 1fr 20px 1fr 20px 1fr 20px 1fr; margin-top: 10px; }
  .fluxo .sx { align-self: center; text-align: center; color: var(--brand-green); font: 600 18px var(--font-mono); }
  .fluxo .et { background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; padding: 13px 14px 11px; display: flex; flex-direction: column; min-height: 276px; }
  .fluxo .et.res { border-color: var(--brand-green); background: #101A0E; }
  .fluxo .et.neg { border-color: #B85F33; }
  .fluxo .et .rt { display: flex; align-items: center; gap: 8px; font: 600 9.5px var(--font-display); letter-spacing: 0.14em; text-transform: uppercase; color: var(--fg-3); }
  .fluxo .et .rt b { width: 20px; height: 20px; border-radius: 5px; background: var(--brand-green); color: #0B100B; font: 600 12px var(--font-mono); letter-spacing: 0; display: flex; align-items: center; justify-content: center; }
  .fluxo .et svg.lucide { width: 34px !important; height: 34px !important; margin-top: 12px !important; display: block !important; }
  .fluxo .et.neg svg.lucide { color: #B85F33; }
  .fluxo .et .n { font: 500 33px/1.05 var(--font-mono); color: var(--fg-1); margin-top: 12px; letter-spacing: -0.02em; white-space: nowrap; }
  .fluxo .et .n.s { font: 600 19.5px/1.2 var(--font-display); letter-spacing: 0; white-space: normal; }
  .fluxo .et p { font-size: 13.2px; color: var(--fg-2); margin-top: 9px; line-height: 1.44; }
  .fluxo .et p b { color: var(--fg-1); }
  .fluxo .et .ct { margin-top: auto; padding-top: 8px; }

  /* Caso em coluna: as cinco etapas ao lado de um gráfico */
  .fv { display: grid; gap: 6px; align-content: start; }
  .fv .r { display: grid; grid-template-columns: 22px 1fr; gap: 10px; background: var(--bg-2); border: 1px solid var(--line); border-radius: 9px; padding: 8px 12px 9px; align-items: start; }
  .fv .r.res { border-color: var(--brand-green); background: #101A0E; }
  .fv .r .bd { width: 22px; height: 22px; border-radius: 5px; background: var(--brand-green); color: #0B100B; font: 600 12px var(--font-mono); display: flex; align-items: center; justify-content: center; margin-top: 1px; }
  .fv .r .rt { font: 600 9.5px var(--font-display); letter-spacing: 0.14em; text-transform: uppercase; color: var(--fg-3); }
  .fv .r p { font-size: 12.4px; color: var(--fg-2); line-height: 1.4; margin-top: 2px; }
  .fv .r p b { color: var(--fg-1); }

  /* Matriz de estágio: uma linha por palmeira, um ponto por estágio */
  .mz { display: grid; grid-template-columns: 26px 1fr repeat(4, 62px); column-gap: 8px; margin-top: 2px; }
  .mz > div { padding: 5px 0; border-bottom: 1px solid var(--line); display: flex; align-items: center; }
  .mz > div.h { font: 600 8.8px/1.3 var(--font-display); letter-spacing: 0.08em; text-transform: uppercase; color: var(--fg-3); justify-content: center; text-align: center; padding: 2px 0 6px; }
  .mz svg.lucide { width: 22px !important; height: 22px !important; }
  .mz > div.nm { display: block; }
  .mz .nm b { font: 600 13.5px var(--font-display); color: var(--fg-1); display: block; }
  .mz .nm span { font-size: 11px; color: var(--fg-2); line-height: 1.3; display: block; }
  .mz > div.pt { justify-content: center; }
  .mz .pt span { width: 16px; height: 16px; border-radius: 50%; box-shadow: inset 0 0 0 1.5px var(--line-strong); display: block; }
  .mz .pt span.on { background: var(--brand-green); box-shadow: none; }
  .mz > div.fim { border-bottom: 0; }

  /* Gráficos lado a lado dentro de um painel */
  .lado { display: flex; gap: 12px; align-items: center; margin-top: 6px; }
  .lado > svg { flex: 1; min-width: 0; }
  .cap { font-size: 11.6px; color: var(--fg-2); line-height: 1.38; margin-top: 6px; }
  .cap b { color: var(--fg-1); }
  .gn { font: 500 54px/1 var(--font-mono); color: var(--fg-1); letter-spacing: -0.03em; margin-top: 10px; }
  .gn small { font: 500 15px var(--font-mono); color: var(--fg-3); letter-spacing: 0; margin-left: 8px; }
  .seta2 { display: flex; align-items: center; gap: 10px; margin-top: 12px; font: 500 16px var(--font-mono); color: var(--fg-1); }
  .seta2 .ar { color: var(--brand-green); }
  .seta2 small { display: block; font: 400 10px var(--font-body); color: var(--fg-3); margin-top: 2px; }

  /* Trajetória em seis fases */
  .f6 { display: grid; grid-template-columns: repeat(6, 1fr); margin-top: 16px; position: relative; }
  .f6::before { content: ""; position: absolute; left: 8%; right: 8%; top: 21px; height: 2px; background: var(--line-strong); }
  .f6 .fz { padding: 0 5px; display: flex; flex-direction: column; position: relative; }
  .f6 .fz .no { width: 36px; height: 36px; border-radius: 50%; background: var(--brand-green); color: #0B100B; font: 600 16px var(--font-mono); display: flex; align-items: center; justify-content: center; margin: 0 auto; border: 4px solid var(--bg-0); box-sizing: content-box; position: relative; }
  .f6 .fz.cau .no { background: var(--bg-0); color: var(--warning); box-shadow: inset 0 0 0 2px var(--warning); }
  .f6 .fz .qd { text-align: center; font: 500 9.5px var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; color: var(--fg-3); margin-top: 5px; }
  .f6 .fz h3 { text-align: center; font-size: 14px; margin-top: 4px; min-height: 35px; line-height: 1.22; }
  .f6 .fz .oq { text-align: center; font-size: 11px; color: var(--fg-2); line-height: 1.34; margin-top: 4px; min-height: 45px; }
  .f6 .fz .cs { background: var(--bg-2); border: 1px solid var(--line); border-radius: 8px; padding: 7px 10px 8px; margin-top: 6px; }
  .f6 .fz .cs b { display: block; font: 600 12px var(--font-display); color: var(--fg-2); }
  .f6 .fz .cs .v { display: block; font: 500 18px/1.15 var(--font-mono); color: var(--fg-1); margin-top: 2px; white-space: nowrap; }
  .f6 .fz .cs span { display: block; font-size: 11px; color: var(--fg-2); line-height: 1.32; margin-top: 2px; }

  /* Checkpoints principais: dimensão × estágio */
  .ck { display: grid; grid-template-columns: 1.06fr repeat(4, 1fr); gap: 5px; margin-top: 12px; }
  .ck .hd { border-radius: 8px; padding: 6px 10px; display: flex; align-items: center; gap: 8px; font: 600 12.8px var(--font-display); }
  .ck .hd b { font: 600 15px var(--font-mono); }
  .ck .hd.e1 { background: var(--bg-3); color: var(--fg-2); }
  .ck .hd.e2 { background: #2C4A22; color: var(--fg-1); }
  .ck .hd.e3 { background: #3A7A2A; color: var(--fg-1); }
  .ck .hd.e4 { background: #62A842; color: #0B100B; }
  .ck .hd.e5 { background: #9BE05F; color: #0B100B; }
  .ck .dm { background: var(--bg-2); border: 1px solid var(--line); border-radius: 8px; padding: 8px 10px; display: flex; gap: 9px; align-items: flex-start; }
  .ck .dm.ia { border-style: dashed; }
  .ck .dm svg.lucide { width: 22px !important; height: 22px !important; margin-top: 1px !important; }
  .ck .dm .k { font: 600 12.8px/1.2 var(--font-display); color: var(--fg-1); }
  .ck .dm p { font-size: 10.6px; color: var(--fg-3); line-height: 1.32; margin-top: 3px; }
  .ck .c { background: var(--bg-1); border: 1px solid var(--line); border-radius: 8px; padding: 7px 10px; }
  .ck .c p { position: relative; padding-left: 11px; font-size: 11.4px; color: var(--fg-2); line-height: 1.34; }
  .ck .c p + p { margin-top: 3px; }
  .ck .c p::before { content: ""; position: absolute; left: 0; top: 7px; width: 5px; height: 2px; background: var(--brand-green); }
  .ck .c p b { color: var(--fg-1); font-weight: 600; }
  .rg { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 9px; }
  .rg span { font-size: 10.8px; color: var(--fg-2); border: 1px solid var(--line-strong); border-radius: 999px; padding: 3px 10px; white-space: nowrap; }
  .rg span b { color: var(--fg-1); font-weight: 600; }

  /* Índices do mercado: roscas dentro dos degraus */
  .lg span.sd::before { display: none; }
  .ixs { display: grid; gap: 8px; margin-top: 10px; }
  .ix { display: grid; grid-template-columns: 54px 1fr; gap: 10px; align-items: center; }
  .ix p { font-size: 11.5px; color: var(--fg-2); line-height: 1.36; }
  .ix p b { color: var(--fg-1); font-weight: 600; }

  /* Armadilhas e cartões com ícone */
  .ar4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 10px; }
  .ar4 .a { background: var(--bg-1); border: 1px solid var(--line); border-left: 3px solid var(--warning); border-radius: 8px; padding: 8px 11px; font-size: 11.6px; color: var(--fg-2); line-height: 1.38; }
  .ar4 .a b { display: block; color: var(--fg-1); font: 600 12.4px var(--font-display); margin-bottom: 2px; }

  /* Saltos da régua, em degraus */
  .saltos { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-top: 8px; }
  .saltos .sa { background: var(--bg-2); border: 1px solid var(--line); border-top: 4px solid var(--brand-green); border-radius: 10px; padding: 12px 14px; display: flex; flex-direction: column; }
  .saltos .sa:nth-child(1) { margin-top: 66px; }
  .saltos .sa:nth-child(2) { margin-top: 44px; }
  .saltos .sa:nth-child(3) { margin-top: 22px; }
  .saltos .sa .st { font: 500 30px/1 var(--font-mono); color: var(--brand-green); }
  .saltos .sa .nm { font: 600 12.5px var(--font-display); color: var(--fg-1); margin-top: 4px; }
  .saltos .sa ul.l li { font-size: 12.2px; margin-top: 5px; line-height: 1.36; }
  .saltos .sa .ev { margin-top: auto; padding-top: 10px; }
  .saltos .sa .ev .bx { background: var(--bg-1); border: 1px solid var(--line); border-radius: 8px; padding: 8px 10px; display: flex; gap: 10px; align-items: center; }
  .saltos .sa .ev .n { font: 500 27px/1 var(--font-mono); color: var(--fg-1); flex: none; }
  .saltos .sa .ev .t { font-size: 11px; color: var(--fg-2); line-height: 1.34; }

  /* Caminho em três passos */
  .cam3 { display: grid; grid-template-columns: 1fr 22px 1fr 22px 1fr; margin-top: 10px; }
  .cam3 .sx { align-self: center; text-align: center; color: var(--brand-green); font: 600 18px var(--font-mono); }
  .cam3 .p { background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; padding: 9px 12px; display: flex; gap: 12px; align-items: center; }
  .cam3 .p.on { border-color: var(--brand-green); background: #101A0E; }
  .cam3 .p svg.lucide { width: 26px !important; height: 26px !important; }
  .cam3 .p .k { font: 600 13.5px var(--font-display); color: var(--fg-1); }
  .cam3 .p p { font-size: 11.5px; color: var(--fg-2); line-height: 1.36; margin-top: 2px; }

  /* Pirâmide de papéis */
  .pir { display: flex; flex-direction: column; align-items: center; gap: 7px; margin-top: 4px; }
  .pir .cam { display: grid; gap: 8px; width: 100%; }
  .pir .cam.c1 { width: 44%; }
  .pir .cam.c3a { width: 84%; grid-template-columns: repeat(3, 1fr); }
  .pir .cam.c3b { grid-template-columns: repeat(3, 1fr); }
  .pir .cam.c2 { grid-template-columns: 1fr 1fr; }
  .pir .sep { color: var(--brand-green); font: 600 13px/1 var(--font-mono); }
  .pir .nd { background: var(--bg-2); border: 1px solid var(--line); border-radius: 9px; padding: 8px 11px; display: flex; gap: 10px; align-items: center; }
  .pir .nd.top { border-color: var(--brand-green); background: #101A0E; }
  .pir .nd svg.lucide { width: 24px !important; height: 24px !important; }
  .pir .nd h3 { font-size: 13px; line-height: 1.2; }
  .pir .nd p { font-size: 11px; color: var(--fg-2); margin-top: 2px; line-height: 1.32; }
  .ev3 { display: grid; gap: 9px; }
  .ev3 .e { background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; padding: 11px 13px; }
  .ev3 .e .n { font: 500 30px/1 var(--font-mono); color: var(--fg-1); }
  .ev3 .e p { font-size: 11.8px; color: var(--fg-2); margin-top: 5px; line-height: 1.38; }

  /* Quebras e perenes */
  .q4 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 2px; }
  .q4 .q { background: var(--bg-1); border: 1px solid var(--line); border-radius: 8px; padding: 8px 10px; }
  .q4 .q .d { font: 600 12px var(--font-mono); color: #B85F33; }
  .q4 .q .k { font: 600 13px var(--font-display); color: var(--fg-1); margin-top: 2px; line-height: 1.2; }
  .q4 .q p { font-size: 11px; color: var(--fg-2); margin-top: 3px; line-height: 1.34; }
  .tiles.ic2 .tl { display: grid; grid-template-columns: 34px 1fr; column-gap: 10px; padding: 10px 12px; }
  .tiles.ic2 .tl svg.lucide { grid-row: 1 / span 3; align-self: start; margin-top: 2px !important; }
  .tiles.ic2 .tl .n { font-size: 25px; margin-top: 3px; white-space: nowrap; }
  .tiles.ic2 .tl p { font-size: 11.4px; margin-top: 3px; }
  .tiles.t3 { grid-template-columns: repeat(3, 1fr); gap: 8px; }
  .tiles.t3 .tl { padding: 9px 11px; }
  .tiles.t3 .tl .n { font-size: 23px; margin-top: 4px; white-space: nowrap; }
  .tiles.t3 .tl p { font-size: 11px; margin-top: 3px; line-height: 1.34; }
  .pr5 { display: grid; gap: 7px; margin-top: 8px; }
  .pr5 .r { display: grid; grid-template-columns: 34px 92px 1fr; gap: 10px; align-items: center; background: var(--bg-1); border: 1px solid var(--line); border-radius: 8px; padding: 7px 11px; }
  .pr5 .r.on { border-color: var(--brand-green); background: #101A0E; }
  .pr5 .r svg.lucide { width: 26px !important; height: 26px !important; }
  .pr5 .r .k { font: 600 14px var(--font-display); color: var(--fg-1); }
  .pr5 .r p { font-size: 11.8px; color: var(--fg-2); line-height: 1.36; }
  .pr5 .r p b { color: var(--fg-1); }

  /* Três horizontes */
  .hz { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 12px; }
  .hz .col { background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; display: flex; flex-direction: column; }
  .hz .col .cb { padding: 9px 14px; display: flex; align-items: center; gap: 10px; border-bottom: 1px solid var(--line); }
  .hz .col .cb svg.lucide { width: 24px !important; height: 24px !important; color: inherit; }
  .hz .col .cb h3 { font-size: 16px; color: inherit; }
  .hz .col .cb .sb { margin-left: auto; font: 500 9.5px var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; color: inherit; }
  .hz .col.v .cb { background: #62A842; color: #0B100B; }
  .hz .col.t .cb { background: #2C4A22; color: var(--fg-1); }
  .hz .col.p .cb { background: var(--bg-3); color: var(--fg-2); }
  .hz .col .it { display: grid; grid-template-columns: 26px 1fr; gap: 10px; padding: 8px 14px; border-bottom: 1px solid var(--line); align-items: start; }
  .hz .col .it:last-child { border-bottom: 0; }
  .hz .col .it svg.lucide { width: 22px !important; height: 22px !important; margin-top: 1px !important; }
  .hz .col.p .it svg.lucide { color: var(--fg-3); }
  .hz .col .it .k { font: 600 13px var(--font-display); color: var(--fg-1); line-height: 1.22; }
  .hz .col .it p { font-size: 11.2px; color: var(--fg-2); line-height: 1.35; margin-top: 2px; }

  /* Sessões: sinais em pontos */
  .sg { display: grid; grid-template-columns: 26px 1fr 78px 30px; column-gap: 10px; align-items: center; margin-top: 4px; }
  .sg > div { padding: 6px 0; border-bottom: 1px solid var(--line); min-height: 34px; display: flex; align-items: center; }
  .sg .fr { font: 600 9.5px var(--font-mono); color: var(--brand-green-bright); }
  .sg .lb { font-size: 13.2px; color: var(--fg-1); line-height: 1.3; }
  .sg .ds { gap: 5px; }
  .sg .ds span { width: 14px; height: 14px; border-radius: 50%; box-shadow: inset 0 0 0 1.5px var(--line-strong); display: block; }
  .sg .ds span.on { background: var(--brand-green); box-shadow: none; }
  .sg .n { font: 600 12.5px var(--font-mono); color: var(--fg-1); justify-content: flex-end; }
  .fala { border-left: 2px solid var(--info); background: var(--bg-1); padding: 9px 13px; font-style: italic; font-size: 13.4px; line-height: 1.42; color: var(--fg-1); margin-top: 9px; }
  .fala small { display: block; font-style: normal; font-size: 10px; color: var(--fg-3); margin-top: 4px; }

  /* Perguntas para a conversa */
  .pg6 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 14px; }
  .pg6 .p { background: var(--bg-2); border: 1px solid var(--line); border-radius: 10px; padding: 16px 18px 13px; display: flex; flex-direction: column; min-height: 178px; }
  .pg6 .p .top { display: flex; align-items: center; gap: 10px; }
  .pg6 .p .top .no { font: 500 13px var(--font-mono); color: var(--fg-3); margin-left: auto; }
  .pg6 .p h3 { font-size: 19px; line-height: 1.22; margin-top: 12px; }
  .pg6 .p p { font-size: 13px; color: var(--fg-2); margin-top: 6px; line-height: 1.42; }
  .pg6 .p .vr { margin-top: auto; padding-top: 8px; font: 500 10px var(--font-mono); color: var(--brand-green-bright); }
"""


def fontes(*citacoes: tuple[str, str], compacta: bool = False) -> str:
    """Linha de fontes do slide, tirada do catálogo. Até 5 fontes, o formato dos demais decks
    (organização, título, página e domínio do link). Acima disso, forma compacta, para a linha não
    tomar o slide: organização, título curto (até 8 fontes), página e o link (↗). No site, o [M123]
    abre o PDF da fonte na página citada. `compacta` força a forma curta num slide muito cheio."""
    if len(citacoes) <= 5 and not compacta:
        return rf.fontes(*citacoes)
    com_titulo = len(citacoes) <= 8
    partes = []
    for ident, pagina in citacoes:
        it = rf.catalogo()[ident]
        inteiro = re.split(r"\s*[;(]", it.get("organizacao") or "")[0].strip()
        org = inteiro.split(",")[0].strip()
        if len(org) > 30:
            org = org[:29].rsplit(" ", 1)[0] + "…"
        elif org != inteiro:
            org += " e outros"
        titulo = ""
        if com_titulo:
            titulo = it.get("titulo") or ""
            if len(titulo) > 32:
                titulo = titulo[:30].rsplit(" ", 1)[0] + "…"
            titulo = ", " + titulo
        url = it.get("url") or ""
        link = f' <a href="{escape(url)}">↗</a>' if url else ""
        pag = f", {pagina}" if pagina and pagina != "web" else ""
        partes.append(f'<span class="f">[{ident}] {escape(org)}{escape(titulo)}{pag}{link}</span>')
    return '<div class="fontes"><b>Fontes</b>' + " ".join(partes) + "</div>"


def cabeca(rotulo: str) -> str:
    return f'<div class="head"><img src="{LOGO}" alt="OagronomIA"><span class="label">{rotulo}</span></div>'


def capa(fontes_no_acervo: int) -> str:
    milhar = f"{fontes_no_acervo:,}".replace(",", ".")
    metricas = [(milhar, "fontes públicas no catálogo"), ("4", "empresas com ficha de benchmark"),
                (str(NOTAS_TEMATICAS), "notas temáticas"), ("4", "sessões executivas")]
    grade = "".join(f'<div class="metric"><div class="v">{v}</div><div class="lb" style="margin-top:5px">{r}</div></div>' for v, r in metricas)
    return f"""<section class="slide cover">
  <img class="logo" src="{LOGO}" alt="OagronomIA">
  {g.capa_ilustracao()}
  <div class="eyebrow" style="margin-top:13mm">Benchmarking de uso de IA como diferencial estratégico · apresentação executiva</div>
  <h1>O que o mercado<br>já fez com IA</h1>
  <p class="lead" style="max-width:168mm">Onde estão as empresas líderes do agro, da bioenergia e de setores vizinhos, como chegaram lá e para onde a IA aponta no campo.</p>
  <div class="grid4" style="max-width:168mm;margin-top:18px">{grade}</div>
  <div class="legend" style="margin-bottom:6mm;max-width:168mm">
    <div class="label">Contratante</div><div>Acelen Energia Renovável</div>
    <div class="label">Documento</div><div>{NOME}</div>
    <div class="label">Nº / Versão</div><div style="font-family:var(--font-mono)">{DOCUMENTO} · {REVISAO} · versão de trabalho {VERSAO}</div>
    <div class="label">Data</div><div>{date.today():%d/%m/%Y}</div>
  </div>
</section>"""


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")  # o -I ignora PYTHONIOENCODING
    fonte = rf.PARCIAL.read_text(encoding="utf-8")
    css = re.search(r"<style>([\s\S]*?)</style>", fonte).group(1)
    slides = conteudo.slides(fontes, g)
    total = len(slides) + 1

    partes = [capa(len(rf.catalogo()))]
    zooms: set[int] = set()
    for n, s in enumerate(slides, 2):
        msg = f'<p class="msg-top">{s["msg"]}</p>' if s.get("msg") else ""
        # Ampliação do corpo do slide: ocupa a folga vertical com gráficos e textos maiores. Vai pela
        # classe da seção (regra em css_zoom), sem um div a mais: o site anima os blocos um a um.
        zoom = round(s.get("zoom", 1) * 100)
        classe = "slide v1" + (f" z{zoom}" if zoom != 100 else "")
        zooms.add(zoom)
        partes.append(f"""<section class="{classe}">
  {cabeca(s["parte"])}
  <div class="eyebrow">{s["olho"]}</div>
  <h2>{s["titulo"]}</h2>
  {msg}
  {s["corpo"]}
  {s["fontes"]}
  <div class="foot"><span>{RODAPE}</span><span class="mono">{n:02d} / {total:02d}</span></div>
</section>""")

    cabecalho = fonte[: fonte.index("<style>")]
    cabecalho = re.sub(r"<title>[\s\S]*?</title>", "<title>Apresentação executiva</title>", cabecalho)
    fixos = ":not(.head):not(.eyebrow):not(h2):not(.msg-top):not(.fontes):not(.foot)"
    css_zoom = "".join(f"  .slide.z{z} > {fixos} {{ zoom: {z / 100}; }}\n" for z in sorted(zooms - {100}))
    html = (cabecalho + "<style>" + css + CSS_EXEC + slides_metodologia.CSS + css_zoom + "</style>\n</head>\n<body>\n\n" + "\n".join(partes)
            + '\n\n<script src="https://unpkg.com/lucide@0.469.0/dist/umd/lucide.min.js"></script>\n<script>if (window.lucide) lucide.createIcons();</script>\n</body>\n</html>\n')

    # Só cores com variável no sistema (o site troca cada uma pelo tema); o resto é erro de digitação ou cor nova.
    mapeadas = {"#050805", "#0B100B", "#131A13", "#1C241B", "#2A3328", "#3A4537", "#F2F4EE", "#B8BFB1", "#7C8678", "#52C937", "#6FE34F",
                "#2F8B1F", "#E8B33B", "#4FB7C9", "#E5524A", "#62A842", "#3A7A2A", "#2C4A22", "#9BE05F", "#3A8FBF", "#6FB8C9", "#1FB8CD",
                "#B88A28", "#B85F33", "#D97757", "#1F2B1C", "#101A0E", "#16210F"}
    novas = "\n".join(partes) + CSS_EXEC + slides_metodologia.CSS
    fora = sorted({c.upper() for c in re.findall(r"#[0-9a-fA-F]{6}\b", novas)} - mapeadas)
    if fora:
        raise SystemExit(f"Cores sem variável no sistema: {', '.join(fora)}")

    SAIDA.write_text(html, encoding="utf-8", newline="\n")
    print(f"{SAIDA.name}: {total} slides")
    for n, s in enumerate(slides, 2):
        print(f"  {n:02d}  {s['parte']:<34} {s['titulo']}")


if __name__ == "__main__":
    main()
