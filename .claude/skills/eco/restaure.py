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
import hashlib
import io
import os
import re
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


def doublons():
    """Fichiers non suivis dont le contenu est celui d'une fiche deja suivie.

    Signature de la synchro Supabase : elle redescend une fiche fraichement
    commitee sous un nom tronque — « Gestion - Introduction UE 12A.md » est
    revenue en « Gestion - Introduction.md », meme contenu, meme seconde que le
    commit. Deux fiches vivantes du meme cours, et un passage suivant qui
    traiterait la mauvaise.
    """
    out = subprocess.check_output(
        ["git", "status", "--porcelain", "--", CIBLE], cwd=VAULT).decode("utf-8")
    # Le test porte sur le chemin déchappé : git entoure de guillemets tout
    # chemin non ASCII ou à espaces, donc la ligne brute ne finit pas par « .md ».
    inconnus = [c for c in (dechappe(l[3:].strip()) for l in out.splitlines()
                            if l[:2] == "??")
                if c.endswith(".md") and "/_brut/" not in c]

    suivis = [c for c in subprocess.check_output(
        ["git", "ls-files", "--", CIBLE], cwd=VAULT).decode("utf-8").splitlines()
        if c.endswith(".md") and os.path.exists(os.path.join(VAULT, c))]

    # Toute fiche produite par le skill est commitee dans la foulee : un .md non
    # suivi dans ce dossier est donc suspect par nature. On cherche ensuite son
    # jumeau pour dire de quoi il est la copie.
    trouves = []
    for c in inconnus:
        plein = os.path.join(VAULT, c)
        if not os.path.exists(plein):
            continue
        emp, ident = empreinte(plein), identite(plein)
        nom = os.path.basename(c)[:-3]
        indice, jumeau = "non suivi par git, contenu inconnu", None
        for s in suivis:
            s_plein = os.path.join(VAULT, s)
            s_nom = os.path.basename(s)[:-3]
            if empreinte(s_plein) == emp:
                indice, jumeau = "corps identique", s
                break
            if s_nom.startswith(nom) or nom.startswith(s_nom):
                indice, jumeau = "nom tronqué", s
                break
            if ident and identite(s_plein) == ident:
                indice, jumeau = "même UE et même source dans le frontmatter", s
                break
        trouves.append((c, jumeau, indice))
    return trouves


def identite(chemin):
    """(ue, source) du frontmatter : deux fiches ne peuvent pas les partager."""
    t = io.open(chemin, encoding="utf-8", errors="replace").read()
    if not t.startswith("---"):
        return None
    entete = t[:t.find("\n---", 3)]
    ue = re.search(r"(?m)^ue:\s*(.+)$", entete)
    src = re.search(r"(?m)^source:\s*(.+)$", entete)
    if not ue and not src:
        return None
    return (ue.group(1).strip() if ue else "", src.group(1).strip() if src else "")


def empreinte(chemin):
    """Le corps seul : la synchro rajoute ou retire des lignes de frontmatter."""
    t = io.open(chemin, encoding="utf-8", errors="replace").read()
    fin = t.find("\n---", 3) + 4 if t.startswith("---") else 0
    return hashlib.sha1(t[fin:].strip().encode("utf-8")).hexdigest()


def main():
    applique = "--applique" in sys.argv[1:]
    absents = sorted(manquants())

    for inconnu, jumeau, indice in doublons():
        print("DOUBLON  « %s »" % inconnu)
        if jumeau:
            print("         %s que « %s », suivi par git." % (indice, jumeau))
        else:
            print("         %s." % indice)
        print("         Signature de la synchro, qui redescend une fiche sous un")
        print("         nom tronqué. Deux fiches vivantes du même cours : à")
        print("         supprimer après vérification — le skill ne supprime jamais.")
        print("")

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
