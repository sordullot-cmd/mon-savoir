#!/usr/bin/env python3
"""Vérifie qu'un passage de /notes n'a rien cassé.

    python3 verifie.py <dossier-avant> <dossier-apres>

Compare le snapshot pris avant l'intervention et l'état actuel, puis vérifie :
  - tr4de-id / created / pinned inchangés (identité de la note côté app)
  - bloc <!-- tr4de:attachments --> intact
  - note pas rallongée (plus de +15 % de mots = réécriture, pas nettoyage)
  - aucun emoji ajouté
  - frontmatter toujours délimité par ---
  - notes nouvelles sans tr4de-id inventé
  - notes disparues signalées (une suppression se propage à l'app)
Sortie 1 si un invariant dur est cassé.
"""
import os
import re
import sys

CHAMPS_FIGES = ("tr4de-id", "created", "pinned")
BLOC = re.compile(r"<!-- tr4de:attachments -->.*?<!-- /tr4de:attachments -->", re.S)
EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U0001F000-\U0001F2FF☀-➿️⬀-⯿]"
)
NOMBRE = re.compile(r"\d+(?:[.,]\d+)?")
# caractères de structure markdown : ils ne comptent pas comme des mots
STRUCTURE = re.compile(r"[|\-*#>\[\]()=:]+")


def decoupe(texte):
    """Renvoie (dict frontmatter, corps)."""
    if not texte.startswith("---"):
        return {}, texte
    fin = texte.find("\n---", 3)
    if fin == -1:
        return {}, texte
    entete, corps = texte[3:fin], texte[fin + 4:]
    champs, cle = {}, None
    for ligne in entete.splitlines():
        if not ligne.strip():
            continue
        if re.match(r"^\s+-\s", ligne) and cle:            # élément de liste YAML
            champs[cle].append(ligne.strip()[1:].strip())
        elif ":" in ligne and not ligne.startswith(" "):
            cle, _, valeur = ligne.partition(":")
            cle, valeur = cle.strip(), valeur.strip()
            champs[cle] = valeur if valeur else []
        cle = cle if isinstance(champs.get(cle), list) else cle
    return champs, corps


LIENS = re.compile(r"^voir aussi ?:.*$", re.M)


def sans_liens(corps):
    """Retire les liens et le bloc de pieces jointes."""
    return re.sub(r"\[\[[^\]]*\]\]", "", LIENS.sub("", BLOC.sub("", corps)))


def mots(corps):
    """Mots du contenu : les liens [[...]] et les lignes « voir aussi » sont de
    la structure, pas de la prose — ils ne comptent pas."""
    return len(STRUCTURE.sub(" ", sans_liens(corps)).split())


def lire(chemin):
    with open(chemin, encoding="utf-8") as f:
        return f.read()


IGNORE = {"conflicts", "attachments", ".obsidian"}


def notes(dossier):
    """Chemins relatifs de toutes les notes, sous-dossiers compris."""
    trouvees = set()
    for racine, dirs, fichiers in os.walk(dossier):
        dirs[:] = [d for d in dirs if d not in IGNORE]
        for n in fichiers:
            if n.endswith(".md") and not n.startswith("_"):
                chemin = os.path.relpath(os.path.join(racine, n), dossier)
                trouvees.add(chemin)
    return trouvees


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    avant_d, apres_d = sys.argv[1], sys.argv[2]
    syntheses = [a.split("=", 1)[1] for a in sys.argv[3:] if a.startswith("--synthese=")]
    erreurs, alertes, ok = [], [], []

    a, b = notes(avant_d), notes(apres_d)

    def ident(dossier, nom):
        return decoupe(lire(os.path.join(dossier, nom))).__getitem__(0).get("tr4de-id")

    partis = {ident(avant_d, n): n for n in a - b if ident(avant_d, n)}
    renommees = {}
    for nom in sorted(b - a):
        champs, _ = decoupe(lire(os.path.join(apres_d, nom)))
        tid = champs.get("tr4de-id")
        if tid and tid in partis:
            renommees[partis[tid]] = nom
        elif tid:
            alertes.append(f"{nom} : note nouvelle avec un tr4de-id ({tid}) — normal "
                           f"si la synchro l'a attribué depuis l'écriture, faute si on "
                           f"l'a inventé")
        else:
            ok.append(f"{nom} : nouvelle note, pas de tr4de-id inventé")

    for nom in sorted(a - b):
        if nom in renommees:
            alertes.append(f"{nom} : renommée en {renommees[nom]} — le nom part "
                           f"dans l'app, à valider")
        else:
            alertes.append(f"{nom} : note disparue (supprimée) — la suppression "
                           f"se propage à l'app, à valider")

    paires = [(n, n) for n in sorted(a & b)] + sorted(renommees.items())
    for nom, nom_ap in paires:
        av, ap = lire(os.path.join(avant_d, nom)), lire(os.path.join(apres_d, nom_ap))
        if av == ap:
            ok.append(f"{nom} : inchangée")
            continue
        cav, corps_av = decoupe(av)
        cap, corps_ap = decoupe(ap)
        souci = []

        if not ap.startswith("---") and av.startswith("---"):
            souci.append("frontmatter perdu")
        for champ in CHAMPS_FIGES:
            if cav.get(champ) != cap.get(champ):
                souci.append(f"{champ} modifié ({cav.get(champ)!r} -> {cap.get(champ)!r})")

        bav, bap = BLOC.search(av), BLOC.search(ap)
        if bav and (not bap or bav.group(0) != bap.group(0)):
            souci.append("bloc tr4de:attachments modifié ou perdu")

        emojis = set(EMOJI.findall(corps_ap)) - set(EMOJI.findall(corps_av))
        if emojis:
            souci.append("emoji ajouté : " + " ".join(sorted(emojis)))

        mav, map_ = mots(corps_av), mots(corps_ap)
        if mav and map_ > mav * 1.15:
            alertes.append(f"{nom_ap} : note rallongée {mav} -> {map_} mots "
                           f"(+{round((map_ / mav - 1) * 100)} %) — contenu déplacé depuis "
                           f"une autre note, classement / tableau ajouté, ou réécriture ?")

        if souci:
            erreurs.append(f"{nom} : " + " ; ".join(souci))
            continue

        nav = NOMBRE.findall(sans_liens(corps_av))
        nap = NOMBRE.findall(sans_liens(corps_ap))
        if sorted(nav) != sorted(nap):
            ecarts = []
            for x in sorted(set(nav) | set(nap), key=lambda v: -nav.count(v)):
                cav, cap_ = nav.count(x), nap.count(x)
                if cav != cap_:
                    ecarts.append(f"{x} ({cav} -> {cap_})")
            alertes.append(f"{nom} : chiffres modifiés — " + ", ".join(ecarts)
                           + " — vérifier que c'est voulu")
        ok.append(f"{nom} : nettoyée, {mav} -> {map_} mots")

    vus = {}
    for nom in sorted(b):
        tid = ident(apres_d, nom)
        if tid and tid in vus:
            erreurs.append(f"{nom} : même tr4de-id que {vus[tid]} ({tid}) — deux notes "
                           f"ne peuvent pas partager une identité, l'app en perdra une")
        elif tid:
            vus[tid] = nom

    def total(dossier, sauf=()):
        return sum(mots(decoupe(lire(os.path.join(dossier, n)))[1])
                   for n in notes(dossier) if n not in sauf)

    tav, tap = total(avant_d, syntheses), total(apres_d, syntheses)
    for s in syntheses:
        m = mots(decoupe(lire(os.path.join(apres_d, s)))[1])
        if m > tap * 0.25:
            erreurs.append(f"{s} : synthèse de {m} mots pour {tap} mots de notes "
                           f"— une synthèse plus courte que ses sources, sinon c'est "
                           f"une copie")
        else:
            ok.append(f"{s} : synthèse de {m} mots (hors total, {round(m / tap * 100)} "
                      f"% des notes)")
    if tav and tap > tav * 1.10:
        erreurs.append(f"total du dossier : {tav} -> {tap} mots "
                       f"(+{round((tap / tav - 1) * 100)} %) — déplacer du contenu "
                       f"ne l'augmente pas, donc c'est de la réécriture")
    else:
        ok.append(f"total du dossier : {tav} -> {tap} mots")

    for ligne in ok:
        print("  ok    " + ligne)
    for ligne in alertes:
        print("  ALERTE " + ligne)
    for ligne in erreurs:
        print("  ERREUR " + ligne)
    print(f"\n{len(ok)} ok, {len(alertes)} alertes, {len(erreurs)} erreurs")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
