# -*- coding: utf-8 -*-
"""
Converte a transcrição exportada do Teams (.docx) em markdown leve para versionar.

Uso:
    python converter_transcricao.py _originais/ARQUIVO.docx 2026-09-29_kickoff_transcricao.md --titulo "Kick-off"
    python converter_transcricao.py _originais/ARQUIVO.pdf ...   # também aceita a transcrição exportada em PDF pelo Word
    python converter_transcricao.py ... --omitir 25:44 26:17   # omite falas (ex.: trechos administrativos de pagamento)
    python converter_transcricao.py ... --anonimizar "Fulano de Tal" Beltrano   # troca nomes por [nome omitido]
    python converter_transcricao.py ... --omitir-cargo "gerente de IA da região X"  # troca o trecho por [cargo omitido]

O original (.docx, gravação) fica em _originais/, fora do Git. Só o .md é versionado.
Regras do projeto: nunca versionar valores, forma de pagamento ou parcelas — use --omitir;
nomes de executivos que possam participar das sessões executivas nunca entram — use --anonimizar.
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


CABECALHO_FALA = re.compile(r"^\d*(.+?)\s{2,}(\d{1,2}:\d{2}(?::\d{2})?)\s*$")
DATA = re.compile(r"^\d{1,2} de \w+ de \d{4}")


def paragrafos_pdf(pdf):
    """No PDF exportado pelo Word, nome e tempo vêm numa linha e a fala nas linhas seguintes.
    Devolve o mesmo formato do .docx: título, data, duração e uma linha 'nome  tempo fala' por fala."""
    import pymupdf
    linhas = [l.strip() for p in pymupdf.open(pdf) for l in p.get_text().splitlines()]
    cab, falas = [], []
    for l in linhas:
        if not l or re.search(r"(começou|parou) a transcrição$", l):
            continue
        if CABECALHO_FALA.match(l):
            falas.append([l])
        elif falas:
            falas[-1].append(l)
        else:
            cab.append(l)
    i = next((k for k, l in enumerate(cab) if DATA.match(l)), len(cab))
    cabecalho = [" ".join(cab[:i]), *cab[i:i + 2]]
    return cabecalho + [f"{f[0]} {' '.join(f[1:])}" for f in falas]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("saida")
    ap.add_argument("--titulo", required=True)
    ap.add_argument("--omitir", nargs="*", default=[], help="marcas de tempo das falas a omitir")
    ap.add_argument("--anonimizar", nargs="*", default=[], help="nomes a trocar por [nome omitido] (palavra inteira)")
    ap.add_argument("--omitir-cargo", nargs="*", default=[], help="trechos que descrevem o cargo de um possível entrevistado")
    a = ap.parse_args()
    nomes = [(re.compile(rf"\b{re.escape(n)}\b", re.IGNORECASE), "[nome omitido]") for n in a.anonimizar]
    nomes += [(re.compile(re.escape(c), re.IGNORECASE), "[cargo omitido]") for c in a.omitir_cargo]
    trocas = 0

    linhas = paragrafos_pdf(a.docx) if a.docx.lower().endswith(".pdf") else paragrafos(a.docx)
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
        for padrao, rotulo in nomes:
            fala, n = padrao.subn(rotulo, fala)
            trocas += n
        falas.append((tempo, nome, fala))

    out = [f"# {a.titulo}", "",
           f"- **Gravação:** {cabecalho[0]}",
           f"- **Data:** {cabecalho[1] if len(cabecalho) > 1 else ''}",
           f"- **Duração:** {cabecalho[2] if len(cabecalho) > 2 else ''}",
           f"- **Participantes na transcrição:** {', '.join(participantes)}",
           "",
           "> Transcrição automática do Teams, sem revisão: há palavras soltas em inglês e trechos truncados "
           "gerados pelo reconhecimento de voz. O original está em `_originais/`, fora do Git."
           + (" Nomes e cargos de possíveis entrevistados das sessões executivas aparecem como [nome omitido] e [cargo omitido]."
              if trocas else ""),
           ""]
    for tempo, nome, fala in falas:
        out.append(f"**{nome}** `{tempo}` — {fala}  ")
    Path(a.saida).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(falas)} falas, {len(participantes)} participantes, {len(a.omitir)} omitidas, "
          f"{trocas} nomes anonimizados -> {a.saida}")


if __name__ == "__main__":
    main()
