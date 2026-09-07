#!/usr/bin/env python3
"""Périmètre « eco gestion » et ce qui a bougé depuis le dernier passage de /eco.

    python3 etat.py                        # rapport : modifiées, nouvelles, à jour
    python3 etat.py --liste                # le périmètre, avec tailles
    python3 etat.py --suivant              # LA page à traiter maintenant (ou « rien »)
    python3 etat.py --suivant --relance    # même si rien n'a bougé (rattrapage manuel)
    python3 etat.py --enregistre "<page>" "<ce qui a été fait>"
    python3 etat.py --enregistre-tout      # acte tout le périmètre sans rien traiter

L'état vit dans `etat.json`, à côté de ce script — hors des pages, donc aucun
frontmatter pollué et aucune synchro qui l'efface.

Le passage est HORAIRE : sans état, le run réécrirait les mêmes pages en boucle.
La règle est donc « une page n'est retraitée que si Sacha l'a modifiée ».
"""
import hashlib
import io
import json
import os
import re
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(ICI, "..", "..", ".."))
ETAT = os.path.join(ICI, "etat.json")

# notes/ appartient à l'app tr4de (skill /notes, synchro Supabase) : jamais touché ici.
IGNORE = {".git", ".claude", ".obsidian", ".trash", "attachments", "conflicts",
          "notes", "INSPIRATION", "INBOX"}
TAG = "l1-eco-gestion"
HUB = "[[00 - Plan L1 Angers"
DOSSIER = "eco gestion"


def notes_de_lapp():
    """Les noms de notes qui appartiennent à l'app tr4de (dossier notes/)."""
    d = os.path.join(VAULT, "notes")
    if not os.path.isdir(d):
        return set()
    return set(n[:-3] for n in os.listdir(d) if n.endswith(".md"))


def pages():
    """Les .md du vault qui relèvent d'éco gestion, par les trois critères.

    Rend (chemin, texte) pour les pages à traiter et met de côté celles qui
    appartiennent à l'app tr4de : la synchro les réécrit, c'est /notes qui s'en
    occupe. Elles sont annoncées, jamais traitées.
    """
    app = notes_de_lapp()
    ecartees = []
    for racine, dirs, fichiers in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in IGNORE and not d.startswith(".")]
        for n in sorted(fichiers):
            if not n.endswith(".md") or n.startswith("_"):
                continue
            chemin = os.path.relpath(os.path.join(racine, n), VAULT)
            try:
                t = io.open(os.path.join(VAULT, chemin), encoding="utf-8").read()
            except (IOError, UnicodeDecodeError):
                continue
            entete = t[:t.find("\n---", 3)] if t.startswith("---") else ""
            if not (chemin.startswith(DOSSIER + os.sep)
                    or TAG in entete.lower()
                    or HUB in t):
                continue
            if "tr4de-id:" in entete or n[:-3] in app:
                ecartees.append(chemin)
                continue
            yield chemin, t
    for c in ecartees:
        print("écartée, appartient à l'app tr4de (voir /notes) : %s" % c,
              file=sys.stderr)


def fiche(chemin, texte):
    fin = texte.find("\n---", 3) + 4 if texte.startswith("---") else 0
    entete, corps = texte[:fin], texte[fin:]
    statut = re.search(r"^statut:\s*(.+)$", entete, re.M)
    return {
        "hash": hashlib.sha1(corps.strip().encode("utf-8")).hexdigest()[:12],
        "mots": len(corps.split()),
        "statut": statut.group(1).strip() if statut else None,
        "age": int(time.time() - os.path.getmtime(os.path.join(VAULT, chemin))),
    }


def charge():
    if os.path.exists(ETAT):
        return json.load(io.open(ETAT, encoding="utf-8"))
    return {"pages": {}}


def sauve(etat):
    with io.open(ETAT, "w", encoding="utf-8") as f:
        f.write(json.dumps(etat, ensure_ascii=False, indent=1, sort_keys=True))
        f.write(u"\n")


def tri(actuel, ancien):
    """(modifiées par Sacha, jamais traitées, à jour)."""
    modifiees, neuves, ajour = [], [], []
    for chemin, f in sorted(actuel.items()):
        vu = ancien.get(chemin)
        if not vu:
            neuves.append(chemin)
        elif vu.get("hash") != f["hash"]:
            modifiees.append(chemin)
        else:
            ajour.append(chemin)
    return modifiees, neuves, ajour


def main():
    args = sys.argv[1:]
    etat = charge()
    ancien = etat.get("pages", {})
    actuel = {c: fiche(c, t) for c, t in pages()}

    if "--enregistre-tout" in args:
        for c, f in actuel.items():
            f = dict(f)
            f.pop("age", None)
            f["passage"] = time.strftime("%Y-%m-%d %H:%M")
            f["fait"] = ancien.get(c, {}).get("fait", "état initial, non traité")
            ancien[c] = f
        etat["pages"] = ancien
        sauve(etat)
        print("périmètre acté sans traitement : %d pages" % len(actuel))
        return 0

    if "--enregistre" in args:
        reste = [a for a in args if not a.startswith("--")]
        if not reste:
            print("il faut la page : --enregistre \"<page>\" \"<ce qui a été fait>\"")
            return 2
        page, fait = reste[0], (reste[1] if len(reste) > 1 else "")
        if page not in actuel:
            print("hors périmètre ou introuvable : %s" % page)
            return 2
        f = dict(actuel[page])
        f.pop("age", None)
        f["passage"] = time.strftime("%Y-%m-%d %H:%M")
        f["fait"] = fait
        ancien[page] = f
        etat["pages"] = ancien
        sauve(etat)
        print("acté : %s (%d mots) — %s" % (page, f["mots"], fait or "sans détail"))
        return 0

    if "--liste" in args:
        for c, f in sorted(actuel.items()):
            vu = ancien.get(c, {})
            print("%-52s %5d mots  statut=%-10s dernier passage=%s"
                  % (c, f["mots"], f["statut"] or "-", vu.get("passage", "jamais")))
        print("%d pages dans le périmètre" % len(actuel))
        return 0

    modifiees, neuves, ajour = tri(actuel, ancien)

    if "--suivant" in args:
        file_ = modifiees + neuves
        if not file_ and "--relance" in args:
            file_ = sorted(ajour, key=lambda c: ancien.get(c, {}).get("passage", ""))
        # une page touchée il y a moins de 10 minutes : il est probablement dedans,
        # on la laisse au passage suivant plutôt que d'écrire par-dessus lui.
        chaudes = [c for c in file_ if actuel[c]["age"] < 600]
        file_ = [c for c in file_ if c not in chaudes]
        if not file_:
            print("rien")
            for c in chaudes:
                print("en cours d'écriture, reporté: %s (%d s)" % (c, actuel[c]["age"]))
            return 0
        page = file_[0]
        raison = ("modifiée depuis le dernier passage" if page in modifiees
                  else "jamais traitée" if page in neuves else "rattrapage")
        print(page)
        print("raison: %s" % raison)
        print("mots: %d" % actuel[page]["mots"])
        print("dernier passage: %s" % ancien.get(page, {}).get("passage", "jamais"))
        print("fait la dernière fois: %s" % ancien.get(page, {}).get("fait", "-"))
        print("reste ensuite: %d" % (len(file_) - 1))
        return 0

    if not ancien:
        print("aucun passage enregistré — %d pages dans le périmètre, toutes à "
              "traiter" % len(actuel))
        for c in sorted(actuel):
            print("  %s" % c)
        return 0

    for titre, lot in (("modifiées depuis le dernier passage", modifiees),
                       ("nouvelles dans le périmètre", neuves)):
        if lot:
            print("%s (%d) :" % (titre, len(lot)))
            for c in lot:
                print("  %s" % c)
    disparues = [c for c in sorted(ancien) if c not in actuel]
    if disparues:
        print("sorties du périmètre ou supprimées (%d) :" % len(disparues))
        for c in disparues:
            print("  %s" % c)
    if not modifiees and not neuves:
        print("rien à faire — %d pages à jour" % len(ajour))
    else:
        print("%d pages à jour par ailleurs" % len(ajour))
    return 0


if __name__ == "__main__":
    sys.exit(main())
