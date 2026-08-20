#!/usr/bin/env python3
"""contraste.py — verifie les couples de couleurs d'un prompt de refonte (WCAG 2.1).

Aucune dependance. Un prompt de refonte qui donne un couple texte/fond sans l'avoir
verifie fait produire un ecran illisible, et personne ne s'en apercoit avant la recette.

Usages
------
  # un couple
  python3 contraste.py "#191F28" "#F2F4F6"

  # avec des noms (repris dans le tableau)
  python3 contraste.py "texte=#191F28" "fond=#F2F4F6"

  # trois couleurs ou plus : tous les couples, en matrice
  python3 contraste.py "#0064FF" "#FFFFFF" "#191F28" "#F2F4F6"

  # ne montrer que ce qui echoue au seuil du texte courant
  python3 contraste.py --echecs "#0064FF" "#FFFFFF" "#8B95A1"

Seuils WCAG 2.1 rappeles dans la sortie :
  4.5 texte courant (AA)  ·  3.0 grand texte (AA, >= 24px ou 18.66px gras)
  3.0 composant / bordure d'interface (AA)  ·  7.0 texte courant (AAA)
"""

import argparse
import itertools
import sys


def parse_couleur(arg):
    """« nom=#rrggbb » ou « #rgb » -> (nom, (r, g, b))."""
    nom = None
    valeur = arg
    if "=" in arg:
        nom, valeur = arg.split("=", 1)
        nom = nom.strip()
    valeur = valeur.strip().lstrip("#")
    if len(valeur) == 3:
        valeur = "".join(c * 2 for c in valeur)
    if len(valeur) != 6:
        raise ValueError(f"hex illisible : {arg!r} (attendu #rgb ou #rrggbb)")
    try:
        rgb = tuple(int(valeur[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        raise ValueError(f"hex illisible : {arg!r}")
    return nom or "#" + valeur.lower(), rgb


def luminance(rgb):
    """Luminance relative sRGB (WCAG 2.1)."""
    canaux = []
    for v in rgb:
        c = v / 255
        canaux.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = canaux
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(rgb_a, rgb_b):
    la, lb = luminance(rgb_a), luminance(rgb_b)
    clair, sombre = max(la, lb), min(la, lb)
    return (clair + 0.05) / (sombre + 0.05)


def verdicts(r):
    """Ce que le couple autorise reellement."""
    return {
        "texte AA": r >= 4.5,
        "grand AA": r >= 3.0,
        "UI AA": r >= 3.0,
        "texte AAA": r >= 7.0,
    }


def ligne(nom_a, hex_a, nom_b, hex_b, r):
    v = verdicts(r)
    ok = lambda b: "oui" if b else "NON"
    usage = []
    if v["texte AAA"]:
        usage.append("tout, y compris AAA")
    elif v["texte AA"]:
        usage.append("texte courant")
    elif v["grand AA"]:
        usage.append("grand texte, icones, bordures seulement")
    else:
        usage.append("decoratif seulement — jamais de texte")
    return (
        f"{nom_a} ({hex_a})  sur  {nom_b} ({hex_b})\n"
        f"    ratio {r:5.2f}:1   texte AA {ok(v['texte AA'])}"
        f"   grand AA {ok(v['grand AA'])}   UI AA {ok(v['UI AA'])}"
        f"   texte AAA {ok(v['texte AAA'])}\n"
        f"    -> {usage[0]}"
    )


def main():
    p = argparse.ArgumentParser(
        description="Contraste WCAG 2.1 des couples de couleurs d'un prompt de refonte.",
        epilog="Deux couleurs = un couple. Trois ou plus = tous les couples possibles.",
    )
    p.add_argument("couleurs", nargs="+", help='"#191F28" ou "texte=#191F28"')
    p.add_argument("--echecs", action="store_true",
                   help="ne lister que les couples sous 4.5:1 (texte courant AA)")
    p.add_argument("--seuil", type=float, default=None,
                   help="seuil personnalise pour --echecs (defaut 4.5)")
    a = p.parse_args()

    try:
        couleurs = [parse_couleur(c) for c in a.couleurs]
    except ValueError as e:
        print(f"erreur : {e}", file=sys.stderr)
        return 2

    if len(couleurs) < 2:
        print("erreur : il faut au moins deux couleurs.", file=sys.stderr)
        return 2

    seuil = a.seuil if a.seuil is not None else 4.5
    couples = list(itertools.combinations(couleurs, 2))
    montres = 0

    print(f"WCAG 2.1 — {len(couples)} couple(s), {len(couleurs)} couleurs\n")
    for (nom_a, rgb_a), (nom_b, rgb_b) in couples:
        r = ratio(rgb_a, rgb_b)
        if a.echecs and r >= seuil:
            continue
        hex_a = "#%02x%02x%02x" % rgb_a
        hex_b = "#%02x%02x%02x" % rgb_b
        print(ligne(nom_a, hex_a, nom_b, hex_b, r))
        print()
        montres += 1

    if a.echecs and montres == 0:
        print(f"aucun couple sous {seuil}:1 — tous passent.")
    print("Seuils : 4.5 texte courant AA · 3.0 grand texte et composants AA · 7.0 AAA.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
