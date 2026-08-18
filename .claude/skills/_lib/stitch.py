#!/usr/bin/env python3
"""Recolle des tuiles de capture en une seule image (grille, ordre ligne par ligne).

Usage:
    python3 stitch.py <sortie.png> --cols N tuile1.png tuile2.png ...

- Les tuiles sont posées ligne par ligne (row-major) : avec --cols 2 et 4 tuiles,
  l'ordre est haut-gauche, haut-droite, bas-gauche, bas-droite.
- Les largeurs de colonnes / hauteurs de lignes s'adaptent à chaque tuile
  (utile si la dernière colonne ou ligne est plus étroite).
- Sert au fallback « capture native par tuiles » du mode post social (voir SKILL.md).
"""
import argparse
import json
import os
import sys

from PIL import Image


def main():
    p = argparse.ArgumentParser(description="Recolle des tuiles en une image.")
    p.add_argument("sortie", help="Fichier image de sortie (.png/.jpg)")
    p.add_argument("--cols", type=int, required=True, help="Nombre de colonnes de la grille")
    p.add_argument("tuiles", nargs="+", help="Tuiles en ordre ligne par ligne")
    args = p.parse_args()

    n = len(args.tuiles)
    if n % args.cols != 0:
        sys.exit(f"Erreur : {n} tuiles ne remplissent pas une grille de {args.cols} colonnes.")
    rows = n // args.cols

    imgs = [Image.open(t) for t in args.tuiles]
    grid = [imgs[r * args.cols:(r + 1) * args.cols] for r in range(rows)]

    col_w = [max(grid[r][c].width for r in range(rows)) for c in range(args.cols)]
    row_h = [max(im.height for im in grid[r]) for r in range(rows)]

    out = Image.new("RGB", (sum(col_w), sum(row_h)))
    y = 0
    for r in range(rows):
        x = 0
        for c in range(args.cols):
            out.paste(grid[r][c], (x, y))
            x += col_w[c]
        y += row_h[r]

    out.save(args.sortie, optimize=True)
    print(json.dumps({
        "sortie": args.sortie,
        "taille": list(out.size),
        "grille": f"{args.cols}x{rows}",
        "octets": os.path.getsize(args.sortie),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
