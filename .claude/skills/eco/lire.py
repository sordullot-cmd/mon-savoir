#!/usr/bin/env python3
"""Sort le texte d'un fichier de cours, quel que soit son format.

Le dossier ~/Documents/L1 melange .pdf (diaporamas du prof), .docx et .odt
(prises de notes d'anciennes promos), .pptx et des photos. Ce script donne le
texte de n'importe lequel, pour que le passage puisse le confronter a la fiche.

    python3 .claude/skills/eco/lire.py "<fichier>" [--pages 1-12]

Les images (.jpg, .png) ne sont pas du texte : le script le dit et le passage
les ouvre avec l'outil Read.
"""
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree

TEXTUTIL = (".docx", ".odt", ".doc", ".rtf", ".rtfd", ".html", ".txt")
IMAGES = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic")


def pdf(chemin, pages=None):
    import fitz  # PyMuPDF, seul outil PDF de la machine

    doc = fitz.open(chemin)
    debut, fin = (pages or (1, doc.page_count))
    fin = min(fin, doc.page_count)
    morceaux = [f"[{doc.page_count} pages au total]"]
    for i in range(debut - 1, fin):
        morceaux.append(f"\n--- page {i + 1} ---\n{doc[i].get_text()}")
    return "".join(morceaux)


def pptx(chemin):
    """textutil ne lit pas le .pptx : on ouvre le zip et on prend les <a:t>."""
    dml = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    morceaux = []
    with zipfile.ZipFile(chemin) as z:
        slides = sorted(
            (n for n in z.namelist() if n.startswith("ppt/slides/slide")),
            key=lambda n: int("".join(c for c in n if c.isdigit())),
        )
        for n in slides:
            arbre = ElementTree.fromstring(z.read(n))
            lignes = []
            # un paragraphe <a:p> est decoupe en runs <a:t> : on les recolle,
            # sinon un mot ressort lettre par lettre.
            for para in arbre.iter(dml + "p"):
                texte = "".join(t.text or "" for t in para.iter(dml + "t"))
                if texte.strip():
                    lignes.append(texte)
            numero = "".join(c for c in n if c.isdigit())
            morceaux.append(f"\n--- diapo {numero} ---\n" + "\n".join(lignes))
    return "".join(morceaux)


def main():
    args = sys.argv[1:]
    pages = None
    if "--pages" in args:
        i = args.index("--pages")
        debut, _, fin = args[i + 1].partition("-")
        pages = (int(debut), int(fin or debut))
        del args[i : i + 2]
    if not args:
        sys.exit(__doc__)

    chemin = Path(args[0]).expanduser()
    if not chemin.exists():
        sys.exit(f"introuvable : {chemin}")
    ext = chemin.suffix.lower()

    if ext == ".pdf":
        print(pdf(chemin, pages))
    elif ext == ".pptx":
        print(pptx(chemin))
    elif ext in TEXTUTIL:
        sortie = subprocess.run(
            ["textutil", "-convert", "txt", "-stdout", str(chemin)],
            capture_output=True, text=True,
        )
        if sortie.returncode or not sortie.stdout.strip():
            sys.exit(f"textutil n'a rien rendu : {sortie.stderr.strip()}")
        print(sortie.stdout)
    elif ext in IMAGES:
        sys.exit(f"{chemin.name} est une image : l'ouvrir avec l'outil Read.")
    else:
        sys.exit(f"format non gere : {ext}")


if __name__ == "__main__":
    main()
