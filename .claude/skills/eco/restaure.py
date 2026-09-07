#!/usr/bin/env python3
"""Rend les pages d'éco gestion que quelque chose a effacées du disque.

    python3 restaure.py              # dit ce qui manque, ne touche à rien
    python3 restaure.py --applique   # réécrit les fichiers absents depuis git

Pourquoi cet outil existe : le 7 septembre 2026, **les 22 fichiers de
`eco gestion/` ont disparu du disque d'un coup** pendant une session de travail
(Obsidian ouvert, plugin `supabase-vault-sync` actif sur tout le vault, avec
l'app comme autorité et un soft delete de 30 jours). Rien n'était perdu : tout
était commité. C'est le même scénario que le 18 août sur les notes de la racine.

D'où la règle du skill : **commiter chaque passage**. Le dépôt est le filet.

Ne réécrit QUE les fichiers que git voit supprimés et qui sont réellement
absents du disque : il ne peut donc écraser aucune modification en cours.
"""
import os
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(ICI, "..", "..", ".."))
CIBLE = "eco gestion/"


def dechappe(chemin):
    """git status entoure de guillemets et échappe les chemins non ASCII."""
    if chemin.startswith('"') and chemin.endswith('"'):
        chemin = chemin[1:-1]
        return chemin.encode().decode("unicode_escape").encode("latin1").decode("utf-8")
    return chemin


def manquants():
    out = subprocess.check_output(
        ["git", "status", "--porcelain", "--", CIBLE], cwd=VAULT).decode("utf-8")
    for ligne in out.splitlines():
        etat, chemin = ligne[:2], dechappe(ligne[3:].strip())
        if "D" in etat and not os.path.exists(os.path.join(VAULT, chemin)):
            yield chemin


def main():
    applique = "--applique" in sys.argv[1:]
    absents = sorted(manquants())

    if not absents:
        print("rien à restaurer — les %s pages sont sur le disque" % CIBLE)
        return 0

    print("%d fichier(s) effacé(s) du disque mais présent(s) dans git :" % len(absents))
    for c in absents:
        print("  %s" % c)

    if not applique:
        print("\nrelancer avec --applique pour les réécrire depuis HEAD")
        return 1

    for c in absents:
        contenu = subprocess.check_output(["git", "show", "HEAD:" + c], cwd=VAULT)
        plein = os.path.join(VAULT, c)
        dossier = os.path.dirname(plein)
        if dossier:
            os.makedirs(dossier, exist_ok=True)
        open(plein, "wb").write(contenu)
    print("\n%d fichier(s) rendu(s) depuis HEAD." % len(absents))
    print("Si ça se reproduit tout de suite, la synchro Supabase est en cause : "
          "il faut l'arrêter ou exclure « %s » avant de retravailler." % CIBLE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
