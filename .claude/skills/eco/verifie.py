#!/usr/bin/env python3
"""Vérifie qu'un passage de /eco n'a rien cassé sur une page de cours.

    python3 verifie.py <page-avant.md> "<page-apres.md>"
    python3 verifie.py <brut.md> "<fiche.md>" --integration
    python3 verifie.py <avant.md> "<fiche.md>" --complement

`page-avant.md` est la copie prise avant d'écrire (ou le brut, en intégration).
`page-apres.md` est le chemin réel dans le vault (relatif ou absolu).

`--integration` = on transforme des notes d'amphi brutes en fiche : la page
grossit forcément, et le brut n'a ni tableaux alignés ni frontmatter. Les
invariants de CONTENU restent, eux : aucun chiffre, aucune formule, aucun nom
propre du cours ne doit disparaître au passage.

`--complement` = on comble des trous du cours. Sacha l'a demandé le 7 septembre
2026 : « si tu vois qu'il manque des grosses informations, des trous, des idées
capitales, notes les ». La fiche grossit donc légitimement — mais chaque ajout
reste TRAÇABLE : marqueur ➕ sur la ligne ajoutée, compteur `ajouts:` dans le
frontmatter, et un récapitulatif en fin de fiche. Sans cette trace, il
réviserait comme du cours quelque chose que son prof n'a peut-être pas dit.

Ce que ça refuse (ERREUR — on restaure depuis le snapshot) :
  - un chiffre, une formule, une clé de frontmatter, un tag ou un lien disparus
  - un titre supprimé/renommé alors qu'un lien du vault pointe sur son ancre
  - un lien [[...]] qui ne résout vers aucune page du vault
  - une ancre interne [[#…]] qui ne correspond à aucun titre de la page
  - une case à cocher cochée ou une cellule de suivi remplie à la place de Sacha
  - un tableau reformaté à contenu identique (hors intégration)
  - une page qui gonfle de plus de 30 % (60 % en complément, libre en intégration)
  - un compteur `ajouts:` qui ne correspond pas aux marqueurs ➕ du corps
  - des ajouts ➕ sans récapitulatif en fin de fiche

Ce que ça signale (ALERTE — à justifier dans le récap) :
  - une page qui gonfle de plus de 15 % (hors intégration)
  - des blocs de code ou de maths non refermés
  - une fiche sans bloc « Contrôle » : elle ne permet pas de se tester
"""
import io
import os
import re
import sys
from collections import Counter

ICI = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(ICI, "..", "..", ".."))
IGNORE = {".git", ".claude", ".obsidian", ".trash", "attachments", "conflicts"}

NOMBRE = re.compile(r"-?\d+(?:[.,]\d+)?")
MATHS = re.compile(r"\$\$.*?\$\$|\$[^$\n]+\$", re.S)
LIEN = re.compile(r"\[\[([^\]|#]+)(#[^\]|]+)?(\|[^\]]+)?\]\]")
LIEN_INTERNE = re.compile(r"\[\[#([^\]|]+)(\|[^\]]+)?\]\]")
TITRE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.M)
COCHEE = re.compile(r"^\s*[-*]\s+\[[xX]\]", re.M)
AVIDE = re.compile(r"^\s*[-*]\s+\[ \]", re.M)
AJOUT = "\u2795"          # ➕ : marque une ligne que Sacha n'avait pas notée
RECAP = re.compile(r"(?i)ce que j'ai (?:compl|ajout)")


def lit(p):
    return io.open(p, encoding="utf-8").read()


def coupe(t):
    fin = t.find("\n---", 3) + 4 if t.startswith("---") else 0
    return t[:fin], t[fin:]


def cles(entete):
    return set(re.findall(r"^([a-zA-Z_][\w-]*):", entete, re.M))


def tags(entete):
    bloc = re.search(r"^tags:\s*\n((?:\s*-\s+.+\n)+)", entete, re.M)
    if bloc:
        return set(re.findall(r"-\s+(.+?)\s*$", bloc.group(1), re.M))
    ligne = re.search(r"^tags:\s*\[(.+)\]", entete, re.M)
    if ligne:
        return set(x.strip() for x in ligne.group(1).split(","))
    return set()


def maths(t):
    return Counter(re.sub(r"\s+", "", m) for m in MATHS.findall(t))


def nom_lien(m):
    # dans un tableau, Obsidian échappe le séparateur d'alias : [[Page\|alias]]
    return m.group(1).replace("\\", "").strip()


def liens(t):
    return Counter(nom_lien(m) for m in LIEN.finditer(t))


def ancre(s):
    """Normalise un titre pour comparer avec l'ancre d'un lien Obsidian."""
    s = re.sub(r"[*_`]", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s.lower()


def titres(t):
    return set(ancre(x) for x in TITRE.findall(t))


def lignes_tableau(t):
    return [l for l in t.splitlines() if l.strip().startswith("|")]


def norm_tableau(l):
    return "|".join(c.strip() for c in l.strip().split("|"))


def reformatees(av, ap):
    """Lignes de tableau dont le contenu est identique mais la forme a changé.

    Obsidian aligne les colonnes ; retirer ce padding ne change rien au contenu
    et pollue le diff. Une ligne dont la version normalisée existait déjà mais
    dont la forme brute a disparu est un reformatage gratuit.
    """
    brut_av = set(lignes_tableau(av))
    norm_av = set(norm_tableau(l) for l in lignes_tableau(av))
    return [l for l in lignes_tableau(ap)
            if l not in brut_av and norm_tableau(l) in norm_av]


def cellules_vides(t):
    n = 0
    for ligne in t.splitlines():
        if ligne.strip().startswith("|") and not re.match(r"^\s*\|[\s:|-]+\|\s*$", ligne):
            n += sum(1 for c in ligne.split("|")[1:-1] if not c.strip())
    return n


def pages_du_vault():
    noms = {}
    for racine, dirs, fichiers in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in IGNORE and not d.startswith(".")]
        for n in fichiers:
            if n.endswith(".md"):
                chemin = os.path.join(racine, n)
                noms.setdefault(n[:-3], chemin)
                noms.setdefault(os.path.relpath(chemin, VAULT)[:-3], chemin)
    return noms


def ancres_attendues(nom_page):
    """Les ancres que le reste du vault attend de cette page."""
    attendues = set()
    for racine, dirs, fichiers in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in IGNORE and not d.startswith(".")]
        for n in fichiers:
            if not n.endswith(".md"):
                continue
            try:
                t = lit(os.path.join(racine, n))
            except (IOError, UnicodeDecodeError):
                continue
            for m in LIEN.finditer(t):
                if nom_lien(m).split("/")[-1] == nom_page and m.group(2):
                    attendues.add(ancre(m.group(2)[1:].replace("\\", "")))
    return attendues


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    p_avant, p_apres = sys.argv[1], sys.argv[2]
    integration = "--integration" in sys.argv[3:]
    complement = "--complement" in sys.argv[3:]
    if not os.path.isabs(p_apres):
        p_apres_abs = os.path.join(VAULT, p_apres)
    else:
        p_apres_abs = p_apres
    for p in (p_avant, p_apres_abs):
        if not os.path.exists(p):
            print("ERREUR introuvable : %s" % p)
            return 2

    av, ap = lit(p_avant), lit(p_apres_abs)
    e_av, c_av = coupe(av)
    e_ap, c_ap = coupe(ap)
    erreurs, alertes = [], []

    # frontmatter
    perdues = cles(e_av) - cles(e_ap)
    if perdues:
        erreurs.append("clés de frontmatter perdues : %s" % ", ".join(sorted(perdues)))
    t_perdus = tags(e_av) - tags(e_ap)
    if t_perdus:
        erreurs.append("tags perdus : %s" % ", ".join(sorted(t_perdus)))

    # chiffres du cours — hors numérotation de listes et de sections, qui est
    # de la structure : « 1. micro entreprise » peut devenir une puce.
    def donnees(t):
        return NOMBRE.findall(re.sub(r"(?m)^\s*(?:#{1,6}\s+)?\d+[.)]\s+", "", t))

    n_av, n_ap = Counter(donnees(c_av)), Counter(donnees(c_ap))
    manquants = {k: v - n_ap.get(k, 0) for k, v in n_av.items() if v > n_ap.get(k, 0)}
    if manquants:
        erreurs.append("chiffres disparus (occurrences) : %s"
                       % ", ".join("%s x%d" % (k, v)
                                   for k, v in sorted(manquants.items())[:12]))

    # formules
    m_av, m_ap = maths(c_av), maths(c_ap)
    f_manq = [k for k, v in m_av.items() if v > m_ap.get(k, 0)]
    if f_manq:
        erreurs.append("formules disparues : %s" % " · ".join(f_manq[:8]))

    # liens
    l_av, l_ap = liens(c_av), liens(c_ap)
    l_manq = [k for k, v in l_av.items() if v > l_ap.get(k, 0)]
    if l_manq:
        erreurs.append("liens perdus : %s" % ", ".join(l_manq[:10]))
    vault = pages_du_vault()
    casses = sorted(k for k in l_ap
                    if k not in vault and k.split("/")[-1] not in vault)
    if casses:
        erreurs.append("liens qui ne résolvent nulle part : %s" % ", ".join(casses[:10]))

    # ancres attendues par le reste du vault
    nom = os.path.basename(p_apres_abs)[:-3]
    attendues = ancres_attendues(nom)
    t_ap = titres(c_ap)
    perdues_anc = sorted(a for a in attendues if a and a not in t_ap)
    if perdues_anc:
        erreurs.append("titres ciblés par un lien du vault et disparus : %s"
                       % " · ".join(perdues_anc[:8]))

    # ne rien remplir à sa place
    if len(COCHEE.findall(c_ap)) > len(COCHEE.findall(c_av)):
        erreurs.append("des cases ont été cochées à la place de Sacha")
    if len(AVIDE.findall(c_ap)) < len(AVIDE.findall(c_av)):
        erreurs.append("des tâches non faites ont disparu")
    # ancres internes : un bloc Contrôle qui pointe vers un titre inexistant
    # est un bloc inutilisable — c'est le cœur de la révision active.
    t_ap_titres = titres(c_ap)
    mortes = sorted(set(ancre(m.group(1)) for m in LIEN_INTERNE.finditer(c_ap))
                    - t_ap_titres)
    if mortes:
        erreurs.append("ancres internes qui ne pointent sur aucun titre de la "
                       "page : %s" % " · ".join(mortes[:8]))

    reform = reformatees(c_av, c_ap) if not integration else []
    if reform:
        erreurs.append("%d ligne(s) de tableau reformatée(s) à contenu identique "
                       "— garder l'alignement des colonnes d'Obsidian : %s"
                       % (len(reform), reform[0].strip()[:60]))

    v_av, v_ap = cellules_vides(c_av), cellules_vides(c_ap)
    if v_ap < v_av:
        erreurs.append("%d cellule(s) de suivi remplie(s) à sa place (grilles de "
                       "scores, essais, notes)" % (v_av - v_ap))

    # volume
    mo_av, mo_ap = len(c_av.split()), len(c_ap.split())
    croissance = (mo_ap - mo_av) / float(mo_av or 1) * 100
    if complement:
        # combler des trous allonge la fiche : ce qu'on surveille, c'est que
        # l'ajout reste minoritaire face à ce que Sacha a noté lui-même.
        if croissance > 60:
            erreurs.append("fiche gonflée de %.0f %% (%d → %d mots) : les "
                           "compléments pèsent plus que le cours"
                           % (croissance, mo_av, mo_ap))
    elif integration:
        # une fiche fait forcément plus de mots que les notes d'amphi dont elle
        # sort : ce qu'on surveille ici, c'est le délayage.
        if croissance > 250:
            alertes.append("fiche %.0f %% plus longue que le brut (%d → %d mots) "
                           "— vérifier qu'on n'a pas délayé" % (croissance, mo_av, mo_ap))
    elif croissance > 30:
        erreurs.append("page gonflée de %.0f %% (%d → %d mots)"
                       % (croissance, mo_av, mo_ap))
    elif croissance > 15:
        alertes.append("page gonflée de %.0f %% (%d → %d mots) — à justifier"
                       % (croissance, mo_av, mo_ap))

    # Traçabilité des compléments : un ajout non marqué ou non recensé serait
    # révisé comme du cours du prof. C'est la contrepartie de l'autorisation de
    # compléter, donnée le 7 septembre 2026.
    marques = c_ap.count(AJOUT)
    declares = re.search(r"^ajouts:\s*(\d+)", e_ap, re.M)
    declares = int(declares.group(1)) if declares else None
    a_recap = bool(RECAP.search(c_ap))
    if marques and not a_recap:
        erreurs.append("%d ajout(s) ➕ dans le corps mais aucun récapitulatif "
                       "« Ce que j'ai complété » en fin de fiche" % marques)
    if declares is not None and declares != marques:
        erreurs.append("frontmatter annonce ajouts: %d, le corps porte %d "
                       "marqueur(s) ➕" % (declares, marques))
    if marques and declares is None:
        erreurs.append("%d ajout(s) ➕ dans le corps mais pas de champ "
                       "`ajouts:` dans le frontmatter" % marques)

    if "contrôle" not in c_ap.lower() and "controle" not in c_ap.lower():
        alertes.append("pas de bloc « Contrôle » : la fiche ne permet pas de se "
                       "tester, elle ne sert qu'à relire")

    # syntaxe
    if c_ap.count("```") % 2:
        alertes.append("bloc de code non refermé (``` en nombre impair)")
    if c_ap.count("$$") % 2:
        alertes.append("bloc de maths non refermé ($$ en nombre impair)")

    print("%s  %d → %d mots (%+.0f %%)%s"
          % (p_apres, mo_av, mo_ap, croissance,
             "  ·  %d ajout(s) ➕" % marques if marques else ""))
    for e in erreurs:
        print("  ERREUR  %s" % e)
    for a in alertes:
        print("  alerte  %s" % a)
    if not erreurs and not alertes:
        print("  ok — chiffres, formules, liens, ancres, grilles et volume "
              "préservés%s" % (", ajouts tracés" if marques else ""))
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
