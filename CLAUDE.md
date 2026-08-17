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

- **`/ranger`** — vide et range l'INBOX automatiquement (classe, déplace, crée la fiche, met à jour les index). Mode hybride : auto-range l'évident, demande si ambigu. Voir `.claude/skills/ranger/SKILL.md`.
- **`/font`** — analyse une nouvelle police et crée sa fiche cherchable par allure (specimen + métriques objectives + descripteurs du vocabulaire canonique), **enrichie par une recherche web** (foundry, designer, année, inspirations, brandings notables — faits sourcés uniquement, rien d'inventé), met à jour l'index et réindexe MemPalace. Appelé par `/ranger` quand une font arrive. Voir `.claude/skills/font/SKILL.md`.
- **`/univers`** — à partir d'un **nom** (jeu vidéo, marque, studio, film…), recherche web en éventail et télécharge **tous les médias créatifs** de l'univers en pleine qualité (branding/logos, UI/menus, character design/concept art, illustrations/key art, trailers/animations, gameplay…) dans un **dossier de référence permanent** `INSPIRATION/UNIVERS/<slug>/` rangé par aspect, avec fiche cherchable (crédits artistes + portfolios, sources, mots-clés). Voir `.claude/skills/univers/SKILL.md`. **Frontière avec `/inspi`** : *un monde qu'on regarde* (jeu, film, studio, marque) → `/univers` ; *un produit numérique qu'on utilise* (app, SaaS, site) → `/inspi`.
- **`/inspi`** — **tout le numérique** : site web, **app**, ou post social. **Mode app** (nom d'app ou lien de store) : récupère les écrans en **résolution native** depuis App Store / Google Play (`grab-app.py`) + les flows et écrans secondaires depuis les bases type **Mobbin** (Refero, Appshots, Page Flows, UXArchive, Screensdesign, Adapty pour les paywalls…), capture le site marketing, fait les couleurs, et produit un **dossier par aspect** (`ecrans/ flows/ branding/ couleurs/ composants/ animations/ marketing/`) dans `INSPIRATION/UI-DESIGN/<slug>/`, fiche `Template-Produit`, indexé dans `_APPS.md`. C'est la fusion de `/univers` et d'`/inspi` pour les produits numériques — un site peut aussi être traité à cette profondeur (« fais-moi le dossier complet de X »). **Mode site** : capture le site (Chrome via CDP) en **pleine hauteur**, **1 screen par page mais 1 seule page par template** (pages répétées regroupées). Crée une inspiration rangée **par discipline**, génère **automatiquement** une **vidéo walkthrough** du site complet (`walkthrough.mp4`), et extrait les **composants/animations vraiment intéressants** (sélectif : rien d'original → rien) — y compris loaders/micro-anims/hover en **GIF/MP4**. Deux dossiers distincts dans le site : `<slug>/composants/` (blocs UI statiques) et `<slug>/animations/` (sections / intros / micro-anims en GIF/MP4) ; deux index transversaux qui les référencent : `INSPIRATION/COMPOSANTS/_COMPOSANTS.md` et `INSPIRATION/ANIMATIONS/_ANIMATIONS.md`. Home/pages précises uniquement si demandé. Gère aussi les **liens de posts sociaux** (X/Twitter, Instagram, Pinterest, TikTok, Behance, Dribbble, YouTube, Vimeo…) : télécharge le(s) média(s) du post en pleine qualité (`grab-post.py`, via gallery-dl/yt-dlp, `--cookies` si login requis) + fiche `Template-Inspiration-Post`, rangé dans la discipline de ce que le post **montre**. Appelé par `/ranger` pour un lien visuel. Voir `.claude/skills/inspi/SKILL.md`.

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

## Règles de travail

- **Répondre en français** (orthographe + accents corrects).
- Ne **jamais déplacer/supprimer** de contenu réel sans validation.
- Respecter le nommage existant (UPPERCASE, `_NOM.md`, frontmatter).
- En cas de doute sur le rangement, proposer plutôt que de décider seul.
