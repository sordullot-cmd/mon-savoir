#!/usr/bin/env python3
"""Sort le texte d'un fichier de cours, quel que soit son format.

Le dossier ~/Documents/L1 melange .pdf (diaporamas du prof), .docx et .odt
(prises de notes d'anciennes promos), .pptx et des photos. Ce script donne le
texte de n'importe lequel, pour que le passage puisse le confronter a la fiche.

    python3 .claude/skills/eco/lire.py "<fichier>" [--pages 1-12]
    python3 .claude/skills/eco/lire.py "<fichier>" --images <dossier>

Beaucoup d'annales sont des PDF SCANNES : aucune couche de texte, `--pages` ne
rend rien. `--images` rend alors les pages en PNG dans le dossier donne, et le
passage les ouvre avec l'outil Read pour les lire a l'oeil.

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


def pdf_en_images(chemin, dossier, pages=None):
    """Rend les pages d'un PDF scanne en PNG, a lire ensuite avec Read."""
    import fitz

    doc = fitz.open(chemin)
    dossier = Path(dossier).expanduser()
    dossier.mkdir(parents=True, exist_ok=True)
    base = Path(chemin).stem.replace(" ", "-")[:40]
    debut, fin = (pages or (1, doc.page_count))
    fin = min(fin, doc.page_count)
    sorties = []
    for i in range(debut - 1, fin):
        f = dossier / f"{base}-p{i + 1}.png"
        doc[i].get_pixmap(dpi=130).save(f)
        sorties.append(str(f))
    return sorties


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
    dossier_images = None
    if "--images" in args:
        i = args.index("--images")
        dossier_images = args[i + 1]
        del args[i : i + 2]
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
        if dossier_images:
            print("\n".join(pdf_en_images(chemin, dossier_images, pages)))
            return
        texte = pdf(chemin, pages)
        # Un PDF scanne n'a pas de couche de texte : le dire plutot que de
        # rendre des pages vides, et donner la commande qui marche.
        if len(texte.split("---")) > 1 and not texte.split("]", 1)[1].strip(" -\npage0123456789"):
            sys.exit("%s est un PDF scanne (aucun texte). Rends les pages en "
                     "images :\n  python3 %s \"%s\" --images <dossier>"
                     % (chemin.name, sys.argv[0], chemin))
        print(texte)
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
