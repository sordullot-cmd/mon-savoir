#!/usr/bin/env python3
"""Dit ce qui a changé dans les notes depuis le dernier passage de /notes.

    python3 etat.py <dossier-de-notes>                 # ce qui a changé
    python3 etat.py <dossier-de-notes> --enregistre    # acte le passage

L'état est gardé dans `etat.json`, à côté de ce script — donc hors du dossier
synchronisé : l'app ne le voit pas et ne peut pas l'effacer.

Sert à rendre un passage incrémental : plutôt que de relire les 15 notes à
fond, on sait lesquelles Sacha a modifiées dans l'app depuis la dernière fois.
"""
import hashlib
import io
import json
import os
import re
import sys

IGNORE = {"conflicts", "attachments", ".obsidian"}
BLOC = re.compile(r"<!-- tr4de:attachments -->.*?<!-- /tr4de:attachments -->", re.S)
ICI = os.path.dirname(os.path.abspath(__file__))
ETAT = os.path.join(ICI, "etat.json")
DEBUT = os.path.join(ICI, "etat-debut.json")   # état au début du passage en cours


def notes(dossier):
    for racine, dirs, fichiers in os.walk(dossier):
        dirs[:] = [d for d in dirs if d not in IGNORE]
        for n in sorted(fichiers):
            if n.endswith(".md") and not n.startswith("_"):
                yield os.path.relpath(os.path.join(racine, n), dossier)


def fiche(dossier, nom):
    t = io.open(os.path.join(dossier, nom), encoding="utf-8").read()
    fin = t.find("\n---", 3) + 4 if t.startswith("---") else 0
    entete, corps = t[:fin], BLOC.sub("", t[fin:])
    tid = re.search(r'^tr4de-id:\s*"?([^"\n]+)"?', entete, re.M)
    maj = re.search(r"^updated:\s*(\S+)", entete, re.M)
    return {
        "id": tid.group(1) if tid else None,
        "updated": maj.group(1) if maj else None,
        "hash": hashlib.sha1(corps.strip().encode("utf-8")).hexdigest()[:12],
        "mots": len(corps.split()),
    }


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    dossier = sys.argv[1]
    enregistre = "--enregistre" in sys.argv[2:]
    actuel = {n: fiche(dossier, n) for n in notes(dossier)}

    ancien = {}
    if os.path.exists(ETAT):
        ancien = json.load(io.open(ETAT, encoding="utf-8")).get("notes", {})

    if not ancien:
        print("aucun passage enregistré — le prochain est un passage complet "
              "(%d notes)" % len(actuel))
    else:
        par_id = {f["id"]: n for n, f in ancien.items() if f["id"]}
        nouvelles, modifiees, renommees, inchangees = [], [], [], []
        for n, f in sorted(actuel.items()):
            if n in ancien:
                (modifiees if f["hash"] != ancien[n]["hash"] else inchangees).append(n)
            elif f["id"] and f["id"] in par_id:
                renommees.append("%s -> %s" % (par_id[f["id"]], n))
            else:
                nouvelles.append(n)
        supprimees = [n for n in sorted(ancien)
                      if n not in actuel
                      and not any(actuel[m]["id"] == ancien[n]["id"] for m in actuel
                                  if actuel[m]["id"])]
        for titre, lot in (("modifiées depuis le dernier passage", modifiees),
                           ("nouvelles", nouvelles),
                           ("renommées", renommees),
                           ("disparues", supprimees)):
            if lot:
                print("%s (%d) :" % (titre, len(lot)))
                for n in lot:
                    print("  -", n)
        print("inchangées : %d" % len(inchangees))
        if not (modifiees or nouvelles or renommees or supprimees):
            print("rien à faire — aucune note touchée depuis le dernier passage")

    if not enregistre:
        json.dump({"notes": actuel}, io.open(DEBUT, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1, sort_keys=True)
        return 0

    # --enregistre : l'app a pu écrire pendant le passage. Ne jamais acter une
    # note qu'on n'a pas traitée : sinon son changement devient invisible pour
    # toujours (vécu le 18 août 2026 sur « recette et courses »).
    pendant = []
    if os.path.exists(DEBUT):
        debut = json.load(io.open(DEBUT, encoding="utf-8")).get("notes", {})
        for n, f in sorted(actuel.items()):
            if n in debut and f["hash"] != debut[n]["hash"]:
                pendant.append(n)
        for n in sorted(set(actuel) - set(debut)):
            pendant.append(n + " (apparue pendant le passage)")
    if pendant:
        print("\nATTENTION — ces notes ont changé pendant le passage :")
        for n in pendant:
            print("  -", n)
        print("  si c'est mon écriture, tout va bien ; si c'est l'app ou Sacha,")
        print("  les traiter avant d'acter, sinon leur changement passera à la trappe.")
    json.dump({"notes": actuel}, io.open(ETAT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, sort_keys=True)
    if os.path.exists(DEBUT):
        os.remove(DEBUT)
    print("\npassage enregistré : %d notes dans etat.json" % len(actuel))
    return 0


if __name__ == "__main__":
    sys.exit(main())
