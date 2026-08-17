# Fiche de contexte — Second cerveau de Sacha (handoff Claude)

> À lire en entier avant d'agir. Ce document permet à un autre Claude de reprendre le travail sans repartir de zéro.

---

## 1. Qui est l'utilisateur

**Sacha Moricet** — designer product / UI / UX / brand, un peu de motion. **Répondre en français.**

Emails :
- Perso : `sacha.moricet@gmail.com`
- Unowhy : `smoricet@unowhy.com` (uniquement pour le travail salarié)
- Sordulo : `sordulo.contact@gmail.com` (l'agence)

Ses univers professionnels (dans sa vie, pas forcément dans le vault) :
- **Unowhy** : son travail salarié.
- **Sordulo** : son agence avec son co-fondateur **Maël Auzenet**. Pas d'entité juridique « Sordulo » : ce sont **2 micro-entreprises** distinctes (*Sacha Moricet* & *Maël Auzenet*). Les devis/factures partent de l'une OU l'autre micro selon le projet.
- **ICAN** : son école (2e année en 2026).
- **Perso** : ses projets personnels (side-projects, portfolio, expérimentations).

---

## 2. Le projet

Construire un **second cerveau** = **vault Obsidian** local en markdown, dans `~/Documents/KNOWLEDGE`.

Décisions validées avec lui :
- Support : **Obsidian** (markdown local).
- Usages : référence/archive + gestion de projets + veille inspi.
- Inspiration : rangée **par discipline** puis par **tags**.
- **Inbox** unique de capture rapide. **Templates** : Projet, Client, Devis, Inspiration, Font, Univers.
- Convention : **dossiers top-niveau en UPPERCASE**, notes d'index nommées **`_NOM.md`** (MOC), tableau de bord = **`ACCUEIL.md`**.

---

## 3. État actuel du vault (août 2026)

```
ACCUEIL.md                      ← dashboard central
INBOX/À-PROPOS.md               ← capture rapide
PERSO/_PERSO.md                 ← projets personnels (vide pour l'instant)
INSPIRATION/_INSPIRATION.md     ← index des disciplines + vocabulaire de descripteurs
   ├─ WEBDESIGN/       (vide, + _MOODBOARD.md)
   ├─ UI-DESIGN/       (vide)
   ├─ BRAND-DESIGN/    (vide)
   ├─ GRAPHISME/       (vide)
   ├─ MOTION/          (vide)
   ├─ COMPOSANTS/_COMPOSANTS.md   ← index transversal, tableau vide
   ├─ ANIMATIONS/_ANIMATIONS.md   ← index transversal, tableau vide
   └─ UNIVERS/_UNIVERS.md
        └─ duolingo/   ← 206 fichiers, seul contenu réel du vault
TEMPLATES/                      ← Projet / Client / Devis / Inspiration / Inspiration-Post / Font / Univers
```

**Important — suppressions d'août 2026.** Sacha a supprimé les domaines `UNOWHY/`, `SORDULO/` (dont `DEVIS-FACTURES/`), `ICAN/` et `ASSETS/` (dont `FONTS/`), ainsi que toutes les inspirations de sites (ribbit, air-inc, sanrita, podium, tesoroxp, newpeace, standards, more-nutrition, eliotdewolf). C'est **volontaire et définitif** : ne pas les recréer sans demande explicite. Les liens morts qui en résultaient ont été nettoyés dans `ACCUEIL.md`, `_PERSO.md`, `_COMPOSANTS.md`, `_ANIMATIONS.md`, `_MOODBOARD.md` et `duolingo.md`.

Les dossiers de discipline vides sont **conservés à dessein** : ce sont les catégories de base décrites dans `_INSPIRATION.md`, elles attendent du contenu.

---

## 4. RÈGLE D'ARCHITECTURE — code vs notes

**Le code ne vit PAS dans le vault. Le cerveau ne contient que des notes + assets design.**
- Le **code** vit hors du vault, dans ses dossiers de dev locaux.
- **`~/Documents/UNOWHY/Projet/`** = projets Unowhy (Powerbank, Hackthon, Self-care).
- Une fiche projet dans le vault pointe vers le dossier local via un lien `file://…`.
- Pourquoi : `node_modules` (auto-généré, régénérable via `npm install`) faisait exploser Obsidian. Obsidian ignore déjà les dossiers en `.` (`.git`, `.next`). Si un projet doit rester dans le vault, exclure `node_modules` via Réglages → Fichiers et liens → Fichiers exclus.

---

## 5. Skills du vault

`/ranger` (vide l'INBOX), `/inspi` (site ou post social → inspiration rangée par discipline), `/univers` (dossier de référence complet sur un univers créatif), `/font` (fiche de police).

**Attention :** `/font` écrit dans `ASSETS/FONTS/`, qui n'existe plus. Le skill recréera l'arborescence au premier usage — vérifier avec Sacha si c'est bien ce qu'il veut avant de le lancer.

---

## 6. Recherche dans le vault

**MemPalace en priorité** (`mempalace_search`) : recherche sémantique sur le contenu, pas seulement les noms de fichiers. `grep`/`find` en secours uniquement.
