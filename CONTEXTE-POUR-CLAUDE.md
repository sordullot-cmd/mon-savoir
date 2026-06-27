# Fiche de contexte — Second cerveau de Sacha (handoff Claude)

> À lire en entier avant d'agir. Ce document permet à un autre Claude de reprendre le travail sans repartir de zéro.

---

## 1. Qui est l'utilisateur

**Sacha Moricet** — designer product / UI / UX / brand, un peu de motion. **Répondre en français.**

Emails :
- Perso : `sacha.moricet@gmail.com`
- Unowhy : `smoricet@unowhy.com` (uniquement pour le travail salarié)
- Sordulo : `sordulo.contact@gmail.com` (l'agence)

Ses univers :
- **Unowhy** : son travail salarié.
- **Sordulo**: son agence avec son co-fondateur **Maël Auzenet**. Pas d'entité juridique « Sordulo »: ce sont **2 micro-entreprises** distinctes (*Sacha Moricet* & *Maël Auzenet*). Les devis/factures partent de l'une OU l'autre micro selon le projet.
- **ICAN** : son école (2e année en 2026).
- **Inspiration** & **Assets** : ressources de designer.

---

## 2. Le projet

Construire un **second cerveau** = **vault Obsidian** local en markdown, dans `/Users/smoricet/Documents/KNOWLEDGE`.

Décisions validées avec lui :
- Support : **Obsidian** (markdown local).
- Usages : référence/archive + gestion de projets + suivi business/devis + veille inspi.
- Sordulo : **marque unifiée en façade**, mais devis séparés par micro-entreprise (Sacha / Maël).
- Inspiration & Assets : rangés **par type** puis par **tags**.
- **Inbox** unique de capture rapide. **Templates** : Projet, Client, Devis, Inspiration.
- Il voulait **remplir avec son vrai contenu** (pas juste une structure vide).

---

## 3. Ce qui a DÉJÀ été fait

Structure montée **par-dessus son existant** (il avait déjà des dossiers UPPERCASE). Convention : **dossiers top-niveau en UPPERCASE**, notes d'index nommées **`_NOM.md`** (MOC), tableau de bord = **`ACCUEIL.md`**.

```
ACCUEIL.md                 ← dashboard central
INBOX/À-PROPOS.md          ← capture rapide
UNOWHY/_UNOWHY.md          ← Projets: Hackthon, Powerbank, Self-care | BRAND/ | DS/
SORDULO/_SORDULO.md
   ├─ CLIENT/RAW-STUDIO/   ← client (app iOS + site)
   ├─ DEVIS-FACTURES/_DEVIS-FACTURES.md  ← split Sacha-Moricet / Maël-Auzenet
   ├─ DA/  ├─ ADMINISTRATIF/
ICAN/_ICAN.md              ← 2e année / 3e trimestre / Motion Design, Soutenance
INSPIRATION/_INSPIRATION.md ← IMAGES / VIDÉOS / LIENS-ARTICLES + système de tags
ASSETS/_ASSETS.md          ← FONTS (déjà fourni) / MOCKUPS / ICONS / TEXTURES-PATTERNS / TEMPLATES-DESIGN / LOGOS
TEMPLATES/                 ← Template-Projet / -Client / -Devis / -Inspiration
```

Détails utiles :
- Typo corrigé : `SORDULO/ADMINSTRATIF` → `SORDULO/ADMINISTRATIF`.
- Aucun contenu réel n'a été déplacé/supprimé.
- Mémoire persistante écrite : `user-sacha-profile`, `project-second-brain` (+ index MEMORY.md).

---

## 4. RÈGLE D'ARCHITECTURE (résolu) — code vs notes

**Le code ne vit PAS dans le vault. Le cerveau ne contient que des notes + assets design.**
- Le **code** vit hors du vault, dans ses dossiers de dev locaux.
- **`~/Documents/UNOWHY/Projet/`** = projets Unowhy (Powerbank, Hackthon, Self-care).
- Le vault `KNOWLEDGE` garde une **fiche projet** par projet qui pointe vers le dossier local (`file://...`). Voir les fiches créées: `UNOWHY/Projet/{Powerbank,Hackthon,Self-care}.md`, `SORDULO/CLIENT/RAW-STUDIO/_RAW-STUDIO.md`.
- Pourquoi : `node_modules` (auto-généré, régénérable via `npm install`) faisait exploser Obsidian. Obsidian ignore déjà les dossiers en `.` (`.git`, `.next`). Si un projet doit rester dans le vault, exclure `node_modules` via Réglages → Fichiers et liens → Fichiers exclus.

**Fait :** vault nettoyé de **723 Mo / 70 413 fichiers → 125 Mo / 541 fichiers**. Doublons de code retirés (Hackthon, Self-care, Powerbank, RAW-STUDIO) après vérif `diff` = 0 différence.

---

## 5. Reste à faire ensuite (remplissage réel)

L'utilisateur veut créer ses vraies fiches. Lui demander / récupérer :
1. **Devis Sordulo** (RAW-STUDIO + autres) : montants, statut, rattachés à quelle micro (Sacha/Maël).
2. **Projets en cours** à épingler dans « En cours » de `ACCUEIL.md`.
3. **ICAN** : liste des matières/rendus du trimestre.
4. **Contact client RAW-STUDIO** pour sa fiche.

Plugins Obsidian conseillés : **Templates** (core) et **Dataview** (communautaire, pour auto-générer les tableaux devis/inspi).
