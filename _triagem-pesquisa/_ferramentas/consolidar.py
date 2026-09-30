# -*- coding: utf-8 -*-
"""
Consolida os resultados das rodadas de varredura em um catálogo para triagem.

Uso:
    python consolidar.py _catalogo/rodada1.json [_catalogo/rodada2.json ...]

Cada JSON: {"resultados": [{"grupo", "pasta", "itens": [...], "formularios": [...], "lacunas": [...]}]}

Gera em _triagem-pesquisa/:
    CATALOGO.xlsx          — planilha com todos os itens, filtros e verificação das métricas
    LEIA-ME.md             — índice legível por pasta, com métricas
    ACESSO-MANUAL.md       — materiais que exigem formulário, cadastro ou são pagos
    _catalogo/catalogo.json — base unificada (deduplicada)

Verificação automática: para cada item baixado, confere se o arquivo existe, é PDF legível e
se os números citados em cada métrica aparecem no texto do PDF.
"""
import html as htmllib
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

import pymupdf
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

pymupdf.TOOLS.mupdf_display_errors(False)
pymupdf.TOOLS.mupdf_display_warnings(False)
RAIZ = Path(__file__).resolve().parent.parent
ANOS = {str(a) for a in range(1990, 2036)}
NOME_PASTA = {
    "01_consultorias-estrategia": "Consultorias de estratégia",
    "02_big4-accenture-capgemini": "Big Four, Accenture e Capgemini",
    "03_analistas-big-techs": "Analistas e big techs",
    "04_academia-instituicoes": "Academia e instituições",
    "05_agro-brasil-instituicoes-midia": "Agro Brasil: instituições e mídia",
    "06_empresas-agro-bioenergia-florestal-br": "Empresas brasileiras de agro, bioenergia e florestal",
    "07_agro-global-perenes-autonomia": "Agro global, culturas perenes e autonomia",
    "08_setor-financeiro": "Setor financeiro",
    "09_outros-setores": "Outros setores maduros",
}


def norm_url(u):
    u = (u or "").strip().lower()
    u = re.sub(r"^https?://(www\.)?", "", u)
    return u.rstrip("/").split("#")[0]


def norm_titulo(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


_cache_txt = {}


def texto_pdf(rel):
    if rel in _cache_txt:
        return _cache_txt[rel]
    p = RAIZ / rel
    try:
        doc = pymupdf.open(p)
        txt = " ".join(pg.get_text() for pg in doc)
        info = (len(doc), round(p.stat().st_size / 1_048_576, 1))
        doc.close()
    except Exception:
        txt, info = None, (0, 0)
    if txt is not None:
        txt = re.sub(r"\s+", " ", txt)
    _cache_txt[rel] = (txt, info)
    return _cache_txt[rel]


def variantes(num):
    """'3,70' -> {'3,70','3.70','3,7','3.7'}; '1.450' -> {'1.450','1,450','1450'}"""
    v = {num, num.replace(",", "."), num.replace(".", ",")}
    for x in list(v):
        if re.fullmatch(r"\d+[.,]\d+", x):
            inteiro, dec = re.split(r"[.,]", x)
            dec2 = dec.rstrip("0")
            v.add(inteiro if not dec2 else f"{inteiro}.{dec2}")
            v.add(inteiro if not dec2 else f"{inteiro},{dec2}")
            if len(dec) == 3:
                v.add(inteiro + dec)
    return v


def verificar_metrica(m, txt):
    m_sem_pag = re.sub(r"\(p(á|a)?g?s?\.?\s*[\d\-–, e]+\)", "", m, flags=re.I)
    nums = [n for n in re.findall(r"\d+(?:[.,]\d+)?", m_sem_pag) if n not in ANOS and n not in {"1", "0"}]
    if not nums:
        return None
    achados = sum(1 for n in nums if any(re.search(rf"(?<![\d.,]){re.escape(x)}(?![\d])", txt) for x in variantes(n)))
    return achados / len(nums)


def carregar(arquivos):
    itens, forms, lacunas, triagem = [], [], defaultdict(list), []
    for arq in arquivos:
        dados = json.loads(Path(arq).read_text(encoding="utf-8"))
        for r in dados.get("resultados", []):
            for it in r.get("itens", []):
                it = {k: (htmllib.unescape(v) if isinstance(v, str) else
                          [htmllib.unescape(x) if isinstance(x, str) else x for x in v] if isinstance(v, list) else v)
                      for k, v in it.items()}
                arq_item = (it.get("arquivo") or "").replace("\\", "/")
                it["pasta"] = arq_item.split("/")[0] if "/" in arq_item else (it.get("pasta") or r.get("pasta", ""))
                it["grupo"] = NOME_PASTA.get(it["pasta"], r.get("grupo", ""))
                it["rodada"] = Path(arq).stem
                itens.append(it)
            for f in r.get("formularios", []):
                forms.append({**{k: htmllib.unescape(v) if isinstance(v, str) else v for k, v in f.items()},
                              "grupo": r.get("grupo", "")})
            for t in r.get("triagem", []):
                triagem.append({k: htmllib.unescape(v) if isinstance(v, str) else v for k, v in t.items()})
            lacunas[r.get("grupo", "")] += r.get("lacunas", [])
    return itens, forms, lacunas, triagem


def unir_acessos(forms, triagem, obtidos=(), status_manual=None):
    """Formulários com a triagem da rodada 2 por cima; os não triados entram como 'não triado'.
    status_manual: {url: [recomendacao, nota]} registrado à mão depois da triagem (envios feitos etc.)."""
    obtidos = {norm_url(u) for u in obtidos}
    status_manual = {norm_url(u): v for u, v in (status_manual or {}).items()}
    acessos, vistos = [], set()
    for t in triagem:
        chave = norm_url(t.get("url_formulario"))
        if chave in vistos:
            continue
        vistos.add(chave)
        acessos.append({"recomendacao": t.get("recomendacao", ""), "relevancia": t.get("relevancia", ""),
                        "organizacao": t.get("organizacao", ""), "titulo": t.get("titulo", ""),
                        "url": t.get("url_formulario", ""), "tipo_acesso": t.get("tipo_acesso", ""),
                        "campos": t.get("campos", ""), "captcha": t.get("captcha", ""),
                        "opt_in": t.get("opt_in_marketing_obrigatorio", ""),
                        "alternativa": t.get("alternativa_publica", ""), "justificativa": t.get("justificativa", ""),
                        "frentes": ", ".join(t.get("frentes") or [])})
    for f in forms:
        chave = norm_url(f.get("url"))
        if chave in vistos:
            continue
        vistos.add(chave)
        acessos.append({"recomendacao": "não triado", "relevancia": "", "organizacao": f.get("organizacao", ""),
                        "titulo": f.get("titulo", ""), "url": f.get("url", ""), "tipo_acesso": "",
                        "campos": f.get("campos_exigidos", ""), "captcha": "", "opt_in": "", "alternativa": "",
                        "justificativa": f.get("observacao", ""), "frentes": ""})
    for a in acessos:
        chave = norm_url(a["url"])
        if chave in obtidos:
            a["recomendacao"] = "já obtido"
        if chave in status_manual:
            rec, nota = status_manual[chave]
            a["recomendacao"] = rec
            if nota:
                a["justificativa"] = f"{nota} {a['justificativa']}".strip()
    ordem = {"preencher automaticamente": 0, "pedir manualmente": 1, "não triado": 2, "descartar": 3,
             "solicitado": 4, "já obtido": 5}
    ordem_rel = {"alta": 0, "media": 1, "baixa": 2}
    acessos.sort(key=lambda a: (ordem.get(a["recomendacao"], 9), ordem_rel.get(a["relevancia"], 9), a["organizacao"]))
    return acessos


def deduplicar(itens):
    vistos, saida = {}, []
    ordem_status = {"baixado": 0, "web": 1, "formulario": 2, "pago": 3, "bloqueado": 4}
    for it in itens:
        chaves = [k for k in (("arq", it.get("arquivo") or None), ("url", norm_url(it.get("url")) or None),
                              ("tit", norm_titulo(it.get("titulo")) + "|" + norm_titulo(it.get("organizacao"))
                               + "|" + (it.get("ano") or ""))) if k[1]]
        existente = next((vistos[k] for k in chaves if k in vistos), None)
        if existente is not None and existente.get("arquivo") and it.get("arquivo") \
                and existente["arquivo"] != it["arquivo"]:
            # mesma URL/título mas arquivos distintos (ex.: página salva em PDF x relatório completo): mantém os dois
            vistos[("arq", it["arquivo"])] = it
            saida.append(it)
            continue
        if existente is None:
            for k in chaves:
                vistos[k] = it
            saida.append(it)
            continue
        # mescla: fica o de melhor status; une métricas e frentes
        melhor, outro = (it, existente) if ordem_status.get(it["status"], 9) < ordem_status.get(existente["status"], 9) else (existente, it)
        melhor["metricas"] = list(dict.fromkeys((melhor.get("metricas") or []) + (outro.get("metricas") or [])))
        melhor["frentes"] = sorted(set(melhor.get("frentes") or []) | set(outro.get("frentes") or []))
        if melhor is it:
            saida[saida.index(existente)] = it
        for k in chaves:
            vistos[k] = melhor
    return saida


def main(arquivos):
    itens, forms, lacunas, triagem = carregar(arquivos)
    itens = deduplicar(itens)
    manual, obtidos, status_manual = {}, [], {}
    for arq in arquivos:
        dados = json.loads(Path(arq).read_text(encoding="utf-8"))
        manual.update(dados.get("verificacao_manual", {}))
        obtidos += dados.get("acessos_obtidos", [])
        status_manual.update(dados.get("acessos_status", {}))
    forms = unir_acessos(forms, triagem, obtidos, status_manual)

    referenciados = set()
    for it in itens:
        it["verificacao"] = ""
        it["paginas"], it["mb"] = "", ""
        if it.get("arquivo"):
            rel = it["arquivo"].replace("\\", "/")
            it["arquivo"] = rel
            referenciados.add(rel)
            if not (RAIZ / rel).exists():
                it["verificacao"] = "ARQUIVO NÃO ENCONTRADO"
                continue
            txt, (pags, mb) = texto_pdf(rel)
            it["paginas"], it["mb"] = pags, mb
            if txt is None:
                it["verificacao"] = "PDF ilegível"
                continue
            if not txt.strip():
                it["verificacao"] = "PDF sem texto (imagem) — conferir manualmente"
                continue
            notas = [verificar_metrica(m, txt) for m in it.get("metricas") or []]
            notas = [n for n in notas if n is not None]
            if not notas:
                it["verificacao"] = "sem métricas numéricas"
            else:
                ok = sum(1 for n in notas if n >= 0.5)
                it["verificacao"] = f"{ok}/{len(notas)} métricas localizadas no PDF"
        elif it.get("metricas"):
            it["verificacao"] = "métricas de página web (conferir no link)"
        if it.get("arquivo") in manual:
            it["verificacao"] = manual[it["arquivo"]]

    orfaos = []
    for p in sorted(RAIZ.rglob("*.pdf")):
        rel = str(p.relative_to(RAIZ)).replace("\\", "/")
        if rel.startswith("_") or rel in referenciados:
            continue
        orfaos.append(rel)

    ordem_rel = {"alta": 0, "media": 1, "baixa": 2}
    itens.sort(key=lambda i: (i["pasta"], ordem_rel.get(i.get("relevancia"), 9), i.get("organizacao", ""), i.get("titulo", "")))
    for n, it in enumerate(itens, 1):
        it["id"] = f"M{n:03d}"

    # destaques curados ("comece por aqui"), guardados por arquivo ou URL para sobreviver à renumeração
    destaques = []
    arq_dest = RAIZ / "_catalogo" / "destaques.json"
    if arq_dest.exists():
        por_chave = {}
        for it in itens:
            for k in (it.get("arquivo"), it.get("url")):
                if k:
                    por_chave.setdefault(k, it)
        for d in json.loads(arq_dest.read_text(encoding="utf-8")):
            it = por_chave.get(d["chave"])
            if it:
                it["destaque"] = d["secao"]
                destaques.append(it)
    for it in itens:
        it.setdefault("destaque", "")

    (RAIZ / "_catalogo").mkdir(exist_ok=True)
    (RAIZ / "_catalogo" / "catalogo.json").write_text(
        json.dumps({"itens": itens, "formularios": forms, "lacunas": lacunas, "orfaos": orfaos}, ensure_ascii=False, indent=2),
        encoding="utf-8")

    escrever_xlsx(itens, forms, lacunas, orfaos)
    escrever_md(itens, forms, lacunas, orfaos, destaques)
    c = Counter(i["status"] for i in itens)
    print(json.dumps({"itens": len(itens), "status": c, "formularios": len(forms), "orfaos": len(orfaos),
                      "verificacao_problemas": [i["id"] + " " + i["verificacao"] for i in itens
                                                if i["verificacao"].startswith(("ARQUIVO", "PDF ilegível"))
                                                or re.match(r"0/\d", i["verificacao"])]}, ensure_ascii=False, indent=1))


def escrever_xlsx(itens, forms, lacunas, orfaos):
    wb = Workbook()
    cab_fill = PatternFill("solid", fgColor="131A13")
    cab_font = Font(bold=True, color="F2F4EE")
    verde = Font(color="2F8B1F", underline="single")

    def cabecalho(ws, cols, larguras):
        ws.append(cols)
        for i, (c, w) in enumerate(zip(cols, larguras), 1):
            cel = ws.cell(row=1, column=i)
            cel.fill, cel.font = cab_fill, cab_font
            cel.alignment = Alignment(vertical="center", wrap_text=True)
            ws.column_dimensions[get_column_letter(i)].width = w
        ws.freeze_panes = "B2"

    ws = wb.active
    ws.title = "Catálogo"
    cols = ["ID", "Destaque", "Grupo", "Título", "Organização", "Ano", "Tipo de fonte", "Setor", "País/região",
            "Frentes", "Relevância", "Status", "Arquivo", "URL", "Métricas (ROI, valor, adoção)",
            "Verificação automática", "Resumo", "Páginas", "MB", "Sua avaliação"]
    cabecalho(ws, cols, [7, 24, 22, 48, 22, 7, 16, 16, 14, 9, 10, 11, 30, 30, 70, 22, 50, 8, 7, 18])
    for it in itens:
        ws.append([it["id"], it.get("destaque", ""), it["grupo"], it.get("titulo"), it.get("organizacao"), it.get("ano"),
                   it.get("tipo_fonte"), it.get("setor"), it.get("pais_regiao"), ", ".join(it.get("frentes") or []),
                   it.get("relevancia"), it.get("status"), it.get("arquivo") or "", it.get("url"),
                   "\n".join("• " + m for m in it.get("metricas") or []), it.get("verificacao"), it.get("resumo"),
                   it.get("paginas"), it.get("mb"), ""])
        r = ws.max_row
        if it.get("arquivo"):
            ws.cell(row=r, column=13).hyperlink = it["arquivo"]
            ws.cell(row=r, column=13).font = verde
        if it.get("url"):
            ws.cell(row=r, column=14).hyperlink = it["url"]
            ws.cell(row=r, column=14).font = verde
        for c in range(1, len(cols) + 1):
            ws.cell(row=r, column=c).alignment = Alignment(vertical="top", wrap_text=c in (2, 4, 15, 17))
    ws.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{ws.max_row}"

    ws2 = wb.create_sheet("Acesso manual")
    cols2 = ["Recomendação", "Relevância", "Frentes", "Organização", "Título", "URL do formulário", "Tipo de acesso",
             "Campos", "CAPTCHA", "Opt-in obrigatório", "Alternativa pública", "Justificativa"]
    cabecalho(ws2, cols2, [22, 11, 9, 22, 45, 40, 20, 40, 10, 12, 35, 55])
    for f in forms:
        ws2.append([f["recomendacao"], f["relevancia"], f["frentes"], f["organizacao"], f["titulo"], f["url"],
                    f["tipo_acesso"], f["campos"], f["captcha"], f["opt_in"], f["alternativa"], f["justificativa"]])
        if f["url"]:
            ws2.cell(row=ws2.max_row, column=6).hyperlink = f["url"]
        for c in range(1, len(cols2) + 1):
            ws2.cell(row=ws2.max_row, column=c).alignment = Alignment(vertical="top", wrap_text=True)
    ws2.auto_filter.ref = f"A1:{get_column_letter(len(cols2))}{ws2.max_row}"

    ws3 = wb.create_sheet("Resumo")
    ws3.append(["Grupo", "Itens", "Baixados", "Web", "Formulário/pago/bloqueado", "Relevância alta", "Com métricas"])
    for c in range(1, 8):
        ws3.cell(row=1, column=c).fill, ws3.cell(row=1, column=c).font = cab_fill, cab_font
        ws3.column_dimensions[get_column_letter(c)].width = 22 if c == 1 else 14
    grupos = defaultdict(list)
    for it in itens:
        grupos[it["grupo"]].append(it)
    for g, lst in grupos.items():
        ws3.append([g, len(lst), sum(i["status"] == "baixado" for i in lst), sum(i["status"] == "web" for i in lst),
                    sum(i["status"] in ("formulario", "pago", "bloqueado") for i in lst),
                    sum(i.get("relevancia") == "alta" for i in lst), sum(bool(i.get("metricas")) for i in lst)])

    ws4 = wb.create_sheet("Lacunas")
    cabecalho(ws4, ["Grupo", "O que não foi encontrado"], [30, 110])
    for g, lst in lacunas.items():
        for l in lst:
            ws4.append([g, l])
    if orfaos:
        ws5 = wb.create_sheet("PDFs sem registro")
        cabecalho(ws5, ["Arquivo"], [90])
        for o in orfaos:
            ws5.append([o])
    wb.save(RAIZ / "CATALOGO.xlsx")


def escrever_md(itens, forms, lacunas, orfaos, destaques=()):
    c = Counter(i["status"] for i in itens)
    linhas = [
        "# Material de pesquisa — triagem",
        "",
        "Material público levantado para o benchmark. Só este índice, a planilha e a lista de acesso manual vão para o Git: "
        "os PDFs ficam na máquina do Guilherme — quem precisar de um arquivo pede a ele.",
        "Planilha completa com filtros: [CATALOGO.xlsx](CATALOGO.xlsx). Materiais que dependem de formulário: [ACESSO-MANUAL.md](ACESSO-MANUAL.md).",
        "",
        f"**{len(itens)} itens** · {c.get('baixado', 0)} PDFs baixados · {c.get('web', 0)} páginas web · "
        f"{c.get('formulario', 0) + c.get('pago', 0) + c.get('bloqueado', 0)} com acesso restrito",
        "",
    ]
    if destaques:
        linhas += ["## Comece por aqui", "",
                   "Seleção dos documentos mais fortes para cada frente. A lista completa vem logo abaixo, por pasta.", ""]
        por_secao = defaultdict(list)
        for it in destaques:
            por_secao[it["destaque"]].append(it)
        for secao, lst in por_secao.items():
            linhas += [f"### {secao}", ""]
            for it in lst:
                alvo = f"[PDF]({it['arquivo']})" if it.get("arquivo") else f"[link]({it.get('url')})"
                linhas.append(f"- **{it['id']} · {it.get('organizacao')} ({it.get('ano')})** — {it.get('titulo')} · {alvo}")
                if it.get("metricas"):
                    linhas.append(f"  - {it['metricas'][0]}")
            linhas.append("")
        linhas += ["---", ""]
    por_pasta = defaultdict(list)
    for it in itens:
        por_pasta[(it["pasta"], it["grupo"])].append(it)
    for (pasta, grupo), lst in sorted(por_pasta.items()):
        linhas += [f"## {grupo}", "", f"Pasta: `{pasta}/`", ""]
        for it in lst:
            alvo = f"[PDF]({it['arquivo']})" if it.get("arquivo") else f"[link]({it.get('url')})"
            linhas.append(f"- **{it['id']} · {it.get('organizacao')} ({it.get('ano')})** — {it.get('titulo')} · "
                          f"{', '.join(it.get('frentes') or [])} · relevância {it.get('relevancia')} · {alvo}")
            if it.get("resumo"):
                linhas.append(f"  - {it['resumo']}")
            for m in (it.get("metricas") or [])[:4]:
                linhas.append(f"  - Métrica: {m}")
        linhas.append("")
    if orfaos:
        linhas += ["## PDFs sem registro no catálogo", ""] + [f"- `{o}`" for o in orfaos] + [""]
    (RAIZ / "LEIA-ME.md").write_text("\n".join(linhas), encoding="utf-8")

    am = ["# Acesso manual", "",
          "Materiais que exigem formulário, cadastro ou assinatura. Para solicitar, use seus dados de contato "
          "(e-mail e telefone comercial) e **não informe nada sobre o projeto ou o cliente**.", ""]
    titulos = {"preencher automaticamente": "Formulários simples (dá para preencher com seus dados de contato)",
               "pedir manualmente": "Pedir manualmente (CAPTCHA, cadastro com senha ou campos além do contato)",
               "não triado": "Ainda não triados",
               "descartar": "Descartados (pagos, indisponíveis ou pouco relevantes)",
               "solicitado": "Solicitados (aguardando liberação por e-mail)",
               "já obtido": "Já obtidos (baixados e catalogados)"}
    por_rec = defaultdict(list)
    for f in forms:
        por_rec[f["recomendacao"]].append(f)
    for rec in ["preencher automaticamente", "pedir manualmente", "não triado", "descartar", "solicitado", "já obtido"]:
        if not por_rec.get(rec):
            continue
        am += [f"## {titulos[rec]}", ""]
        for f in por_rec[rec]:
            rel = f" · relevância {f['relevancia']}" if f["relevancia"] else ""
            am += [f"- **{f['organizacao']} — {f['titulo']}**{rel}", f"  - Link: {f['url']}"]
            if f["campos"]:
                am.append(f"  - Campos: {f['campos']}")
            if f["captcha"] or f["opt_in"]:
                am.append(f"  - CAPTCHA: {f['captcha'] or '?'} · opt-in de marketing obrigatório: {f['opt_in'] or '?'}")
            if f["alternativa"]:
                am.append(f"  - Alternativa pública: {f['alternativa']}")
            if f["justificativa"]:
                am.append(f"  - {f['justificativa']}")
        am.append("")
    pagos = [i for i in itens if i["status"] in ("pago", "bloqueado")]
    if pagos:
        am += ["", "## Pagos ou bloqueados", ""]
        am += [f"- **{i.get('organizacao')} — {i.get('titulo')}** ({i['status']}): {i.get('url')}" for i in pagos]
    (RAIZ / "ACESSO-MANUAL.md").write_text("\n".join(am) + "\n", encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
