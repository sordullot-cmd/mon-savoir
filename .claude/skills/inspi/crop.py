#!/usr/bin/env python3
"""Découpe un composant depuis une capture pleine hauteur.

Usage :
    python3 crop.py <image-source> <image-sortie> --band <y_haut> <y_bas>     # bande pleine largeur
    python3 crop.py <image-source> <image-sortie> --box <x> <y> <w> <h>       # rectangle précis

Coordonnées en pixels de l'image SOURCE (pas de l'aperçu redimensionné).
"""
import argparse
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--band", nargs=2, type=int, metavar=("Y_HAUT", "Y_BAS"))
ap.add_argument("--box", nargs=4, type=int, metavar=("X", "Y", "W", "H"))
a = ap.parse_args()

im = Image.open(a.src)
W, H = im.size
if a.box:
    x, y, w, h = a.box
    crop = im.crop((x, y, min(x + w, W), min(y + h, H)))
elif a.band:
    y1, y2 = a.band
    crop = im.crop((0, max(0, y1), W, min(y2, H)))
else:
    raise SystemExit("préciser --band ou --box")
crop.save(a.out)
print(f"OK {a.out} : {crop.size[0]}x{crop.size[1]} (source {W}x{H})")
