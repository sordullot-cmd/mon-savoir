# CLAUDE.md — Vault Obsidian « KNOWLEDGE » (second cerveau de Sacha)

> Instructions pour Claude Code dans ce vault. **Répondre toujours en français.**
> Pour le détail complet du contexte/handoff, voir [`CONTEXTE-POUR-CLAUDE.md`](CONTEXTE-POUR-CLAUDE.md).

## Ce que c'est

Un **vault Obsidian** local en markdown (`~/Documents/brain^2`) servant de second cerveau à **Sacha Moricet** — designer product / UI / UX / brand (+ un peu de motion).

Usages : référence/archive · gestion de projets · veille inspiration.

## Les domaines (dossiers top-niveau, UPPERCASE)

| Domaine | Quoi | Index |
| --- | --- | --- |
| `PERSO/` | Projets personnels (side-projects, portfolio, expérimentations) | `_PERSO.md` |
| `INSPIRATION/` | Refs visuelles rangées par discipline (+ `UNIVERS/`) | `_INSPIRATION.md` |

Plus : `ACCUEIL.md` (dashboard central) · `INBOX/` (capture rapide) · `TEMPLATES/` (Projet, Client, Devis, Inspiration, Inspiration-Post, Produit, Font, Univers).

> Les domaines `UNOWHY/`, `SORDULO/`, `ICAN/` et `ASSETS/` ont été **supprimés du vault** (août 2026). Ne pas les recréer sans demande explicite de Sacha. Les templates `Template-Client` / `Template-Devis` / `Template-Font` restent disponibles si un de ces domaines est relancé.

## Conventions (à respecter strictement)

- **Dossiers top-niveau en UPPERCASE.**
- **Notes d'index / MOC nommées `_NOM.md`** (ex. `_INSPIRATION.md`).
- **Tableau de bord = `ACCUEIL.md`.**
- **Frontmatter YAML** en tête de chaque note (`type`, `tags`, etc.) — voir les templates.
- **Relier les notes** avec `[[liens wiki]]` et des `#tags`.
- Inspiration : rangée **par discipline** puis par **tags**.
- Pour toute nouvelle fiche : partir d'un template de `TEMPLATES/`.
- **Images dans une note : un embed = une famille, pas un fichier.** Un SVG/PNG sans dimensions s'affiche **pleine largeur** dans Obsidian — enchaîner dix embeds d'un même visuel décliné donne dix pleines pages illisibles. Regarder les images (planche de contact via `.claude/skills/_lib/planche.py`), regrouper les variantes en **une planche** rangée dans `<aspect>/planches/`, et cadrer un visuel isolé avec `![[fichier.svg|500]]`. Les fichiers individuels restent en place comme assets.
- **Composition des visuels — la référence est `design.duolingo.com`** (mise en page du vault et du site) : une ligne **remplit toute la largeur** (un visuel seul prend tout, jamais de vide sur le côté) ; les cellules d'une même ligne sont **identiques** et toutes les lignes d'un lot ont la **même hauteur** (une ligne plus courte élargit ses cellules), le visuel étant centré dedans ; la variation vient du **contenu** — nombre de cellules selon le format, séries groupées — pas de l'envie de varier.
- **Pas d'emojis dans les `.md`.** Ne jamais ajouter d'emoji pictographique dans les notes, titres, index ou templates. Les flèches typographiques (`→`, `←`) restent autorisées car ce sont des symboles de contenu, pas des emojis.

## Règle d'architecture — code vs notes

**Le code ne vit PAS dans le vault.** Le cerveau ne contient que des **notes + assets design**.

- Le **code** vit hors du vault, dans les dossiers de dev locaux.
- Projets Unowhy → `~/Documents/UNOWHY/Projet/`
- Le vault garde une **fiche projet** qui pointe vers le dossier local (`file://…`).
- Ne jamais réimporter de `node_modules` dans le vault (ça fait exploser Obsidian).

## À propos de Sacha

- Designer product / UI / UX / brand + motion.
- 3 univers pro : **Unowhy** (salarié), **Sordulo** (agence — **2 micro-entreprises distinctes**, Sacha Moricet & Maël Auzenet, pas d'entité juridique « Sordulo » ; devis/factures partent de l'une ou l'autre micro), **ICAN** (école).
- Emails : perso `sacha.moricet@gmail.com` · Unowhy `smoricet@unowhy.com` (travail salarié uniquement) · Sordulo `sordulo.contact@gmail.com`.

## Skills disponibles

- **`/ranger`** — vide et range l'INBOX : classe, déplace, crée la fiche, met à jour les index. Mode hybride — auto-range l'évident, demande si ambigu.
- **`/notes`** — met au propre les notes prises sur le tas (`notes/`, synchronisé avec l'app tr4de). Travail **transversal** : rassemble un sujet éparpillé sur plusieurs notes.
- **`/font`** — fiche d'une police, cherchable par allure. **Appelé par `/ranger`** quand une font arrive.
- **`/univers`** — dossier de référence d'un univers créatif, à partir d'un **nom** (jeu, film, studio, marque).
- **`/inspi`** — dossier de référence d'un **produit numérique**, à partir d'une **URL** ou d'un nom : site, app, ou post social. **Appelé par `/ranger`** quand un lien arrive.
- **`/refonte`** — transforme un **dossier de référence** (source de DA) + une **cible** (site, app, dossier de code) en **prompt de refonte** précis pour un agent de code. Sortie : `<dossier-source>/prompts/<cible>.md`. Aucune valeur inventée : chaque hex, police, durée est sourcée.

> **Frontière `/univers` ↔ `/inspi`** : *un monde qu'on regarde* (jeu, film, studio, marque) → `/univers` ; *un produit numérique qu'on utilise* (app, SaaS, site) → `/inspi`.
>
> **Même sortie pour les deux** : un dossier rangé **par aspect** (`ecrans/` ou `visuels/`, `flows/`, `branding/`, `couleurs/`, `composants/`, `animations/`, `marketing/`, `process/`, `archive/`) plus une fiche avec une section par aspect, `## Sources` et `## Crédits` nominatifs. `/inspi` le fait dans **tous** ses modes et **toutes** les disciplines — jamais un dossier plat de captures. Structure détaillée dans `INSPIRATION/_INSPIRATION.md`.

Le détail de chaque skill — sources, protocole, outils, garde-fous — vit dans son `SKILL.md` et se charge à l'invocation. Ne pas le recopier ici : la description du frontmatter suffit au routage.

## Recherche dans le vault — MemPalace d'abord

**Pour chercher quoi que ce soit dans le vault, utiliser MemPalace en priorité** (recherche sémantique qui indexe le contenu, pas juste les noms de fichiers).

- `mempalace_search` ramène directement le **contenu pertinent** (montants, statuts, liens entre notes), pas seulement un chemin de fichier à ouvrir.
- Match **sémantique** : « devis foot » suffit à trouver « Devis Wanafoot », pas besoin du nom exact.
- `grep`/`find` = **secours uniquement**, quand on connaît déjà un nom de fichier ultra-précis et qu'on veut juste son chemin.

## Créer une catégorie / un dossier quand c'est nécessaire (règle générale)

Vaut **partout dans le vault**, pas seulement pour les inspirations.

- Si un élément ne rentre dans **aucune catégorie existante**, tu **peux créer une nouvelle catégorie** (dossier, discipline, descripteur…) — n'oblige pas à tout caser de force dans une case mal adaptée.
- **Mais rester sobre** : réutiliser l'existant en priorité, préférer un terme proche déjà présent, et ne créer que si c'est vraiment justifié. **Ne pas multiplier les catégories** (fragmentation = on ne retrouve plus rien).
- Croissance **délibérée et centralisée** : une nouvelle catégorie doit être ajoutée à l'endroit qui fait référence (ex. `_INSPIRATION.md` pour une discipline) et **signalée** dans le récap, jamais laissée en doublon implicite.
- En cas de doute entre « réutiliser » et « créer », proposer plutôt que de trancher seul.

## Publier — après chaque skill

**Tout skill qui écrit dans le vault se termine en publiant** (`/inspi`, `/univers`,
`/ranger`, `/font`, `/notes`) : réindexer le site, puis **commiter et pousser les deux
dépôts** — le vault (`~/Documents/brain^2`) et le site (`~/Documents/GitHub/vault-gallery`,
dont le `git push` déclenche à lui seul le déploiement Vercel).

Procédure, ordre imposé, messages de commit et garde-fous : **`.claude/skills/_lib/publier.md`**.
Autorisation permanente de Sacha — ne pas redemander à chaque fois. Non bloquant :
un échec de push se signale dans le récap, il ne fait pas échouer le run.

## Règles de travail

- **Répondre en français** (orthographe + accents corrects).
- Ne **jamais déplacer/supprimer** de contenu réel sans validation.
- Respecter le nommage existant (UPPERCASE, `_NOM.md`, frontmatter).
- En cas de doute sur le rangement, proposer plutôt que de décider seul.
