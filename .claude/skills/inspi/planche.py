#!/usr/bin/env python3
"""planche.py — assemble des visuels en une PLANCHE de vignettes légendées (PNG).

Deux usages, un seul outil :
  1. REGARDER — construire une planche de tout un dossier dans le scratchpad, la
     lire (`Read`), et juger sur pièces : quoi est quoi, quoi est un doublon,
     quoi ne montre rien. C'est le préalable obligatoire au rangement.
  2. LIVRER — assembler les variantes d'un même visuel (un wordmark en 6 couleurs,
     une mascotte en 4 poses) en UNE planche rangée dans le vault, au lieu de 6
     fichiers quasi identiques.

Rend n'importe quoi que Chrome sait afficher : SVG, PNG, JPG, WEBP, GIF.

Usage :
    python3 planche.py <sortie.png> <fichier|glob> [...] [--cols 5] [--tile 260]
        [--bg damier|clair|sombre] [--titre "..."] [--sans-legende] [--largeur 1600]

Exemples :
    # regarder tout un dossier avant de ranger
    python3 planche.py /tmp/scratch/vu-branding.png "INSPIRATION/UNIVERS/duolingo/branding/*.svg"
    # livrer une planche de variantes
    python3 planche.py "…/branding/planche-wordmark-couleurs.png" "…/wordmark-*.svg" --cols 3 --titre "Wordmark — variantes de couleur"
"""
from __future__ import annotations

import argparse
import glob as globmod
import html
import json
import os
import struct
import sys
import tempfile
import urllib.parse
import zlib

_ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _ICI)
sys.path.insert(0, os.path.join(os.path.dirname(_ICI), "univers"))
import shoot    # capteur pleine hauteur (CDP), même dossier
import palette  # read_png (décodeur PNG pur Python), skill univers

FONDS = {
    # damier : rend visibles les visuels blancs ET les visuels noirs
    "damier": ("#ffffff", "#111", """
        background-color:#fff;
        background-image:linear-gradient(45deg,#e9e9e9 25%,transparent 25%,transparent 75%,#e9e9e9 75%),
                         linear-gradient(45deg,#e9e9e9 25%,transparent 25%,transparent 75%,#e9e9e9 75%);
        background-size:16px 16px;background-position:0 0,8px 8px;"""),
    "clair": ("#ffffff", "#111", "background:#fff;"),
    "sombre": ("#141414", "#eee", "background:#141414;"),
}


def collect(motifs: list[str]) -> list[str]:
    fichiers: list[str] = []
    for m in motifs:
        if os.path.isdir(m):
            m = os.path.join(m, "*")
        trouves = sorted(globmod.glob(m)) if any(c in m for c in "*?[") else [m]
        for f in trouves:
            if os.path.isfile(f) and os.path.splitext(f)[1].lower() in (
                    ".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif"):
                fichiers.append(os.path.abspath(f))
    return list(dict.fromkeys(fichiers))


def build_html(fichiers, cols, tile, bg, titre, legende) -> str:
    page_bg, fg, tile_css = FONDS[bg]
    cases = []
    for i, f in enumerate(fichiers, 1):
        src = "file://" + urllib.parse.quote(f)
        nom = html.escape(os.path.basename(f))
        poids = os.path.getsize(f) / 1024
        cap = f'<figcaption><b>{i}</b> · {nom}<span>{poids:.0f} ko</span></figcaption>' if legende else ""
        cases.append(f'<figure><div class="box"><img src="{src}" loading="eager"></div>{cap}</figure>')
    entete = f"<h1>{html.escape(titre)}</h1>" if titre else ""
    return f"""<!doctype html><meta charset="utf-8">
<style>
  *{{box-sizing:border-box}}
  body{{margin:0;padding:24px;background:{page_bg};color:{fg};
       font:13px/1.35 -apple-system,BlinkMacSystemFont,"Helvetica Neue",sans-serif}}
  h1{{font-size:18px;margin:0 0 18px;font-weight:600}}
  .grille{{display:grid;grid-template-columns:repeat({cols},1fr);gap:18px}}
  figure{{margin:0}}
  .box{{{tile_css}height:{tile}px;border:1px solid rgba(128,128,128,.35);border-radius:8px;
        display:flex;align-items:center;justify-content:center;padding:12px;overflow:hidden}}
  .box img{{max-width:100%;max-height:100%;object-fit:contain}}
  figcaption{{margin-top:6px;font-size:11px;line-height:1.3;word-break:break-word;opacity:.85}}
  figcaption b{{opacity:1}}
  figcaption span{{display:block;opacity:.55}}
</style>
{entete}<div class="grille">{''.join(cases)}</div>"""


def _write_png(path, w, h, nch, brut):
    ct = {1: 0, 2: 4, 3: 2, 4: 6}[nch]

    def chunk(typ, data):
        return (struct.pack(">I", len(data)) + typ + data
                + struct.pack(">I", zlib.crc32(typ + data) & 0xFFFFFFFF))

    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, ct, 0, 0, 0)))
        f.write(chunk(b"IDAT", zlib.compress(brut, 6)))
        f.write(chunk(b"IEND", b""))


def trim_bas(path, marge=22):
    """Coupe le vide en bas : Chrome renvoie la hauteur du VIEWPORT quand la page
    est plus courte que lui, ce qui laisse une grande bande de fond sous la grille."""
    try:
        w, h, nch, px = palette.read_png(path)
    except Exception:
        return None
    stride = w * nch
    ligne_fond = px[(h - 1) * stride:h * stride]
    if len(set(ligne_fond[i:i + nch] for i in range(0, stride, nch))) != 1:
        return None  # la dernière ligne n'est pas uniforme : rien à couper
    dernier = h - 1
    while dernier > 0 and px[dernier * stride:(dernier + 1) * stride] == ligne_fond:
        dernier -= 1
    nouvelle_h = min(h, dernier + 1 + marge)
    if nouvelle_h >= h:
        return None
    brut = b"".join(b"\x00" + px[y * stride:(y + 1) * stride] for y in range(nouvelle_h))
    _write_png(path, w, nouvelle_h, nch, brut)
    return nouvelle_h


def main() -> int:
    ap = argparse.ArgumentParser(description="Assemble des visuels en une planche de vignettes légendées.")
    ap.add_argument("sortie", help="PNG de sortie")
    ap.add_argument("motifs", nargs="+", help="fichiers, globs ou dossiers")
    ap.add_argument("--cols", type=int, default=5)
    ap.add_argument("--tile", type=int, default=260, help="hauteur d'une case en px (def 260)")
    ap.add_argument("--bg", choices=list(FONDS), default="damier")
    ap.add_argument("--titre", default="")
    ap.add_argument("--sans-legende", action="store_true")
    ap.add_argument("--largeur", type=int, default=1600)
    a = ap.parse_args()

    fichiers = collect(a.motifs)
    if not fichiers:
        print(json.dumps({"erreur": "aucun fichier image trouvé", "motifs": a.motifs}, ensure_ascii=False))
        return 1

    page = build_html(fichiers, a.cols, a.tile, a.bg, a.titre, not a.sans_legende)
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
    tmp.write(page)
    tmp.close()
    os.makedirs(os.path.dirname(os.path.abspath(a.sortie)) or ".", exist_ok=True)
    try:
        # budget court : page locale, rien à charger en réseau
        res = shoot.shoot("file://" + urllib.parse.quote(tmp.name), a.sortie, a.largeur, 1200, 30000)
    finally:
        os.unlink(tmp.name)
    coupe = trim_bas(a.sortie)
    if coupe:
        res["hauteur"] = coupe
    res.update({"visuels": len(fichiers), "colonnes": a.cols,
                "fichiers": [os.path.basename(f) for f in fichiers]})
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
