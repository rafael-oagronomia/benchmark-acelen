# -*- coding: utf-8 -*-
"""
Converte a transcrição exportada do Teams (.docx) em markdown leve para versionar.

Uso:
    python converter_transcricao.py _originais/ARQUIVO.docx 2026-09-29_kickoff_transcricao.md --titulo "Kick-off"
    python converter_transcricao.py ... --omitir 25:44 26:17   # omite falas (ex.: trechos administrativos de pagamento)

O original (.docx, gravação) fica em _originais/, fora do Git. Só o .md é versionado.
Regra do projeto: nunca versionar valores, forma de pagamento ou parcelas — use --omitir.
"""
import argparse
import html
import re
import zipfile
from collections import OrderedDict
from pathlib import Path

LINHA = re.compile(r"^\d*(.+?)\s{2,}(\d{1,2}:\d{2}(?::\d{2})?)(.*)$")


def paragrafos(docx):
    xml = zipfile.ZipFile(docx).read("word/document.xml").decode("utf-8")
    xml = re.sub(r"</w:p>", "\n", xml)
    texto = html.unescape(re.sub(r"<[^>]+>", "", xml))
    return [l.strip() for l in texto.splitlines() if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("saida")
    ap.add_argument("--titulo", required=True)
    ap.add_argument("--omitir", nargs="*", default=[], help="marcas de tempo das falas a omitir")
    a = ap.parse_args()

    linhas = paragrafos(a.docx)
    cabecalho = linhas[:3]  # nome da gravação, data/hora, duração
    falas, participantes = [], OrderedDict()
    for l in linhas[3:]:
        m = LINHA.match(l)
        if not m:
            continue
        nome, tempo, fala = m.group(1).strip(), m.group(2), m.group(3).strip()
        participantes[nome] = True
        if tempo in a.omitir:
            fala = "[trecho administrativo omitido nesta versão; ver original fora do Git]"
        falas.append((tempo, nome, fala))

    out = [f"# {a.titulo}", "",
           f"- **Gravação:** {cabecalho[0]}",
           f"- **Data:** {cabecalho[1] if len(cabecalho) > 1 else ''}",
           f"- **Duração:** {cabecalho[2] if len(cabecalho) > 2 else ''}",
           f"- **Participantes na transcrição:** {', '.join(participantes)}",
           "",
           "> Transcrição automática do Teams, sem revisão: há palavras soltas em inglês e trechos truncados "
           "gerados pelo reconhecimento de voz. O original está em `_originais/`, fora do Git.",
           ""]
    for tempo, nome, fala in falas:
        out.append(f"**{nome}** `{tempo}` — {fala}  ")
    Path(a.saida).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(falas)} falas, {len(participantes)} participantes, {len(a.omitir)} omitidas -> {a.saida}")


if __name__ == "__main__":
    main()
