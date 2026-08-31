---
type: inspiration
discipline: ui-design
media: app
source: https://traderssecondbrain.com
url_store:
editeur: Igor Manuilov (fondateur seul)
type_app: finance
plateformes: [web]
version: TSB 5.0 (nom du fichier de tokens), relevé le 2026-08-31
secteur: finance
couleur_principale: teal #4DAB9A
couleurs: ["#050505", "#0b0b0b", "#0d0d0d", "#4DAB9A", "#5BC4B0", "#00f0c2", "#22c55e", "#ef4444", "#f0f0f0"]
patterns: [empty-state, mode-sombre, parametres, recherche]
anime: oui
animations: [scroll-reveal, video-bg, hover, transitions-page]
layout: bento
mood: [dark, minimal, editorial]
typos: [Instrument Sans, DM Mono]
date_capture: 2026-08-31
tags: [inspiration, ui, dark]
---

# Trader's Second Brain

> Journal de trading qui refuse d'être un carnet : il cherche la fuite d'argent dans les trades passés, la chiffre, et la transforme en règle pour la prochaine session. Dossier ouvert pour la DA — c'est la plus belle interface du secteur du journaling de trading, et la seule qui assume une esthétique de terminal plutôt que de dashboard SaaS.

**Sources :** site officiel (assets produit servis en clair) · **mode démo public sans login** · fichier de tokens `/assets/tokens.css` · screencasts de la documentation · Wayback Machine (l'ère Notion) · chaîne YouTube du fondateur

> **Lecture** : chaque famille d'écrans est montrée par **une planche** (`<aspect>/planches/`), légendée juste dessous. Les fichiers individuels restent dans leur dossier d'aspect — c'est de là qu'on récupère un écran précis.

## En bref

- **Produit web uniquement** : pas d'app mobile (vérifié : rien dans l'App Store, rien sur le site), mais une **extension de navigateur** qui journalise depuis TradingView et un EA MetaTrader 5.
- **Un seul auteur.** Igor Manuilov, trader depuis 2014, fondateur et seul nom crédité. Aucun designer, aucune agence : l'interface est dessinée par la personne qui construit le produit.
- **Le fichier de tokens s'appelle lui-même « TSB 5.0 — Design Tokens / Single source of truth for all pages »** : ce n'est pas un site avec des couleurs, c'est un système déclaré, en accès public.
- **Deux palettes cohabitent et ne doivent pas être confondues** : le teal désaturé `#4DAB9A` de l'app et du logo, et le mint saturé `#00f0c2` de la landing refaite en 2026.
- **La couleur ne couvre que 0,88 % de la surface des écrans** (mesuré au pixel sur les neuf écrans du dossier). Tout le reste est une échelle de huit noirs.
- **Chiffres en monospace, texte en sans** : DM Mono pour toute donnée (prix, P&L, dates, R), Instrument Sans pour le reste. La règle ne fléchit jamais.
- **Un mode démo public** expose l'app sur 64 trades d'exemple, sans compte — c'est rare et c'est la meilleure porte d'entrée pour étudier le produit.
- **Positionnement anti-abonnement** assumé : 299 $ une fois « yours for life », face aux 35 à 99 $/mois de TradeZella.

## Écrans

![[ecrans/planches/planche-ecrans-de-l-app.png]]

**Le produit ne montre jamais une donnée sans son verdict.** Chaque écran finit par une phrase qui tranche — `Break-even zone`, `VALIDATED`, `Building confidence`, `SAMPLE TOO SMALL` — et cette phrase est traitée typographiquement comme la valeur elle-même. C'est la différence avec les dashboards du secteur, qui empilent des KPI et laissent le trader conclure.

- `ecrans/dashboard-sombre-comportement.webp` — heatmap annuelle de setups en carrés vert/rouge (le motif GitHub, mais chaque case est un trade), puis `Setup Distribution` et un `Edge Score` en donut ambre gradué autour d'une zone de break-even.
- `ecrans/journal-cartes-trades.webp` — le journal n'est pas un tableau : quatre **cartes** de trade en grille, chacune avec son symbole, sa pastille `LONG` / `SHORT`, son P&L, entry/exit et son R. Les chiffres sont en mono, les libellés minuscules et gris.
- `ecrans/backtester-verdict-strategie.webp` — quatre cartes de questions posées au backtest (`Best Setup Only`, `Best Instrument Only`, `Long Only`, `Short Only`) au-dessus d'une comparaison de courbes d'equity. On choisit une hypothèse, pas des filtres.
- `ecrans/playbook-validation-setup.webp` — la fiche de setup : une **note en lettre** (`A`) traitée en gros, expectancy, win rate, `OPERATING READ`, et deux actions seulement — `Open setup` et `Ask AI coach`.
- `ecrans/ai-coach-audit.webp` — l'audit IA rendu en grille de jours dense, chaque cellule commentée. Beaucoup de texte, aucune illustration.
- `ecrans/ecran-review-boucle-evidence.jpg` — le même journal avec `KEEP REVIEWING` en capitales pleine largeur par-dessus : la seule pièce où le produit se met en scène.

![[ecrans/planches/planche-mode-demo.png]]

**Captures maison dans le mode démo, sans compte.** Le tracker de prop firm affiche un bandeau `Demo Mode / FTMO sample replay`, un stepper de cycle de vie (Challenge → Verification → FTMO Account) et une carte `Today Guard`. Six des huit routes de démo annoncées ne se rendent pas hors session navigateur réelle — voir § Limites.

## Flows

![[flows/planches/planche-flows.png]]

**Le produit documente ses propres parcours en screencast, et les sert en clair.** Cinq vidéos de la page `/docs`, entre 45 s et 59 s chacune, à regarder comme des flows :

- `flows/flow-premier-lancement.mp4` — l'onboarding complet, du compte vide au premier import.
- `flows/flow-leak-map.mp4` — la Leak Map Console en interaction, le composant signature.
- `flows/flow-ai-coach.mp4` — le drawer de conversation et le rendu des réponses.
- `flows/flow-boucle-review.mp4` — la review quotidienne de bout en bout.
- `flows/flow-edition-trade-journal.mp4` — édition d'un trade : champs, formulaires, sauvegarde.
- `flows/extension-tradingview-quick-log.webp` — l'extension navigateur : chart TradingView à gauche, panneau `TSB Quick Log` à droite, avec capture du contexte higher-timeframe.

## Composants

![[composants/planches/planche-composants.png]]

**La Leak Map est le composant qui justifie le produit, et il tient en trois temps nommés** — `FIND IT`, puis la preuve, puis `ACT`. Une grille sessions × jours (Asia / London / New York) localise la fuite, la nomme en langage de trader (`Post-loss revenge re-entry`) et la **chiffre** (`-$1,315`) ; l'étape d'action ne propose que trois décisions : `Cut`, `Press`, `Validate`. Un designer qui cherche comment rendre un diagnostic actionnable sans noyer l'utilisateur devrait partir de là.

- `composants/leak-map-revenge-trading.png` — étape 1, la grille de localisation.
- `composants/leak-map-decision-cut-press-validate.png` — étape 3, les trois décisions.
- `composants/regle-session-suivante.webp` — la preuve convertie en règle pour la session suivante.
- `composants/modal-verification-import.webp` — la modale de vérification d'import CSV, sur fond sombre.
- `composants/note-vocale-transcription.webp` — contrôles de note vocale et transcription attachés à un plan de trade.

## Animations

`animations/hero-dashboard-anime.mp4` — 30 s de parcours animé du dashboard avec un curseur, servi en autoplay dans le hero de la landing : rangée de KPI, Daily P/L en barres, calendrier P&L mensuel, panneaux `Instruments` / `Setups` / `Best Time to Trade`. Réencodé à 1280 px de large (l'original faisait 15,8 Mo pour 1954 px).

Le système de motion est déclaré dans les tokens : `--ease-out cubic-bezier(0.16, 1, 0.3, 1)`, `--ease-spring cubic-bezier(0.34, 1.56, 0.64, 1)`, et trois durées seulement — 120 ms, 200 ms, 350 ms.

## Branding

**Un logotype vectorisé à partir d'une image, et c'est écrit dans le fichier.** Le `<desc>` interne du SVG dit « Vectorized from supplied logo image » : la marque n'a jamais été dessinée en vectoriel d'origine. Le symbole 32 × 32, lui, est construit proprement avec deux dégradés linéaires teal — `#2F7C70` à 90 % d'opacité vers `#4DAB9A`, et `#348A7C` vers `#4DAB9A`.

![[branding/logo-tsb-wordmark.svg|420]]

- `branding/logo-tsb-symbole.svg` — le symbole, en dégradés teal.
- Aucun press kit : `/press`, `/brand`, `/media`, `/brand-assets` renvoient tous 404. Ces deux SVG sont les seuls assets de marque récupérables.

## Couleurs

![[couleurs/palette-app-sombre.svg]]

**Huit niveaux de noir, et un seul accent.** Le système ne se construit pas sur une couleur mais sur l'écart entre `#050505` (le fond de page) et `#151515` (un champ de saisie) : dix unités de luminosité pour hiérarchiser toute une application. Les bordures ne sont pas des gris mais du blanc en alpha (6 %, 7 %, 10 %, 12 %) — donc elles suivent le fond au lieu de le contredire.

**Fonds — huit niveaux de noir**

| Nom de token | Hex | Usage |
| --- | --- | --- |
| `--app-bg-page` | `#050505` | fond de page, le point le plus noir |
| `--bg-void` | `#060606` | vide de mise en page |
| `--bg-primary` / `--app-bg-shell` | `#0b0b0b` | la coque de l'app |
| `--app-surface-card` | `#0d0d0d` | cartes, sections alternées |
| `--bg-secondary` | `#101010` | sections |
| `--bg-elevated` / `card-hover` | `#111111` | survol d'une carte |
| `--bg-surface` | `#121212` | surfaces |
| `--app-surface-control` | `#151515` | champs et contrôles |

**Textes**

| Nom de token | Hex | Usage |
| --- | --- | --- |
| `--text-primary` | `#f0f0f0` | titres et valeurs |
| `--text-secondary` | `#adadad` | texte courant |
| `--text-tertiary` | `#6b6b6b` | labels |
| `--text-muted` | `#5c5c5c` | mentions |

**Accent et sémantique**

| Nom de token | Hex | Usage |
| --- | --- | --- |
| `--accent` | `#4DAB9A` | le teal de marque, glow `rgba(77,171,154,0.4)` |
| `--accent-light` / `--accent-secondary` | `#5BC4B0` | survol |
| `--app-action-primary-color` | `#9fe4d8` | texte d'action primaire |
| `--green` / `--green-light` | `#22c55e` / `#4ade80` | gain |
| `--red` / `--red-light` | `#ef4444` / `#f87171` | perte |
| `--warn` / `--warn-light` | `#f59e0b` / `#fbbf24` | avertissement |
| `--info` / `--info-light` | `#60a5fa` / `#93c5fd` | information |

![[couleurs/palette-app-clair.svg]]

**Le thème clair existe vraiment, et il ne se contente pas d'inverser.** L'accent teal ne bouge pas d'un point (`#4DAB9A` dans les deux thèmes) mais les **actions** passent à `#0f766e` — un teal beaucoup plus foncé, parce que le premier ne tient pas sur blanc. C'est la bonne façon de faire : la couleur d'identité reste stable, la couleur d'interaction s'adapte au contraste.

| Nom de token | Hex clair | Usage |
| --- | --- | --- |
| `--app-bg-page` / `--bg-void` | `#fafafa` | fond de page |
| `--bg-primary` / `card` / `shell` | `#ffffff` | cartes et coque |
| `--bg-secondary` / `control` | `#f5f5f7` | sections et contrôles |
| `--text-primary` | `#09090b` | titres |
| `--text-secondary` | `#525252` | texte courant |
| `--accent` | `#4DAB9A` | identique au sombre |
| `--app-action-primary-color` | `#0f766e` | action, assombrie pour le blanc |

![[couleurs/palette-landing-2026.svg]]

**La landing de 2026 pousse un mint que l'app n'utilise jamais.** `#00f0c2` et `#36ffd8` sont dans un second fichier de tokens (`landing-v2.css`) : le marketing crie, le produit murmure. C'est un écart délibéré, et il vaut d'être noté avant de reprendre l'un pour l'autre — le logo, lui, est du côté du teal sourd.

| Nom de rôle | Hex | Usage |
| --- | --- | --- |
| `--lz-accent` | `#00f0c2` | l'accent des titres et CTA |
| `--lz-accent-strong` | `#36ffd8` | renfort |
| `--lz-surface-base` | `#050505` | fond général |
| section « story » | `#010101` | le plus noir du site |
| `--lz-text` | `#f5f5f5` | texte |
| vert / rouge | `#18d67a` / `#ef6b6b` | gain / perte sur la landing |
| section « perspective » | `#ece9e1` sur `#171917` | beige papier, **seule section claire de tout le site** |

![[couleurs/palette-relevee-dans-les-ecrans.svg]]

**Mesuré, pas estimé : 0,88 % de la surface des écrans porte une couleur** (delta de saturation > 40). Le teal d'accent culmine à 0,045 % de la surface, et le rouge de perte relevé (`#502020`) est bien plus sourd que le `#ef4444` du token — parce qu'il n'apparaît qu'en fond de pastille, jamais en aplat. Une DA de journal de trading peut donc être « colorée » dans son système et quasi monochrome à l'écran.

Fichier source conservé : `couleurs/tokens-charte-tsb-5.css` (11,7 ko, commenté par l'auteur).

## Marketing

![[marketing/planches/planche-pages-du-site.png]]

**Le site est un site de SEO déguisé en produit, et ça se voit dans les pages.** À côté de la landing, l'essentiel du volume est éditorial — guides, comparatifs de prop firms, listes de brokers, template Notion. La DA y tient (même noir, même typo), mais ces pages sont des tunnels d'acquisition, pas du design produit.

- `marketing/landing.png` — la landing pleine hauteur (17 077 px). Hero `Stop changing strategies. Find out what actually works.`, chapitrage narratif en trois temps `Find the pattern. Prove it. Act on it.`, puis `Know what to change before the next session.`
- `marketing/landing-mobile.png` — la même en rendu iPhone.
- Pages éditoriales : `guides-trading-journals`, `notion-template`, `prop-firm-challenges`, `prop-firms`, `supported-brokers`.

Prix affichés au relevé : gratuit (30 trades/mois) · **299 $ une fois, à vie** · ou 49 $/mois · −10 % en crypto. Preuve sociale : « 2 100+ traders · 600 K+ imported trades ».

## Archive

![[archive/planches/planche-ere-notion-2024.png]]

**En avril 2024, ce produit était un template Notion vendu depuis un WordPress.** Même promesse, même nom, même fondateur — et une DA sans rapport. C'est le meilleur avant/après du dossier : il montre qu'un produit de journaling peut passer de « base de données bien rangée » à « terminal qui rend un verdict » sans changer d'une ligne son argument de vente.

- `archive/archive-2024-dashboard-notion.webp` — le « dashboard » de l'époque Notion.
- `archive/archive-2024-journal-notion.webp` — l'exemple de journal dans le template.

Dix-sept snapshots intermédiaires existent entre avril 2024 et mai 2026 pour reconstituer la bascule ; l'Internet Archive est tombé en cours de run (voir § Limites).

## Typographie

Deux familles seulement, chargées via Google Fonts depuis le fichier de tokens :

- **Instrument Sans** (400, 500, 600, 700) — toute l'interface et les titres. 545 à 552 éléments rendus sur la home.
- **DM Mono** (400, 500) — **tous les chiffres** : prix, P&L, dates, R-multiples. Fallback `JetBrains Mono`.

Aucune police auto-hébergée, aucun `@font-face` maison. Ni l'une ni l'autre n'a de fiche dans le vault — candidates à `/font`.

## Géométrie et motion

Relevés dans les tokens, utiles pour une reprise :

- Rayons : cartes 10 px, sections 12 px, contrôles 10 px ; échelle générale 8 → 24 px ; landing : action 9 px, interactif 14 px, carte de preuve 20 px, média 24 px, pilule 999 px.
- Spacing : 4 / 8 / 12 / 16 / 20 / 24 / 32 / 40.
- Ombres : `0 2px 8px`, `0 4px 16px`, `0 8px 32px` de noir.
- Motion : `--ease-out cubic-bezier(0.16,1,0.3,1)`, `--ease-spring cubic-bezier(0.34,1.56,0.64,1)`, durées 120 / 200 / 350 ms.
- Pile : PHP sur nginx, icônes Lucide 0.475.0, classes préfixées `lz-` (landing) et `app-` / `pf-` (produit).

## Pourquoi je l'aime

Parce que c'est la seule interface du secteur qui ait compris que **le luxe, dans un outil de données, c'est le vide**. Tout le monde met des dégradés, des glows et des cartes flottantes sur un dashboard de trading ; celui-ci met huit noirs, une typo mono pour les chiffres, un teal qui n'occupe rien, et met toute son énergie sur une seule chose — la phrase qui dit quoi faire. Et le vocabulaire est du design : `Leak Map`, `Today Guard`, `Operating read`, `Rule fit /100`. Nommer, c'est déjà concevoir.

## À réutiliser pour

- **Un dashboard sombre qui doit rester lisible longtemps** : reprendre l'échelle de huit noirs et les bordures en blanc alpha plutôt que des gris opaques.
- **Faire dire quelque chose à une donnée** : le triptyque `FIND IT → preuve chiffrée → ACT` avec trois décisions maximum.
- **La règle mono/sans** : toute donnée en monospace, tout le reste en sans. Elle tient à elle seule la crédibilité d'un outil financier.
- **Un thème clair qui ne trahit pas la marque** : accent stable, couleur d'action recalculée.
- **Un tunnel de review** : les cinq screencasts de `/docs` sont un modèle de documentation de flow.

## Limites de la récolte

- **Six des huit routes du mode démo** (`/dashboard`, `/journal` hors celui capturé, `/coach`, `/backtester`, `/playbook`, `/reports`, `/setup`) rendent une page vide hors session navigateur réelle : seuls `journal` et `prop-firm` ont pu être capturés. Les six autres écrans du dossier viennent des assets servis par le site.
- **Internet Archive hors service** pendant une partie du run (« Internet Archive services are temporarily offline ») : les millésimes intermédiaires 2024 → 2026 n'ont pas pu être capturés, seuls deux visuels de l'ère Notion ont été récupérés.
- **Le compte X du produit** (`x.com/TSB_app`) est le canal build-in-public le plus probable et reste inexploré (402 en fetch). À ouvrir à la main dans Arc.
- **Aucune base d'UI ne référence ce produit** (Refero, SaaS Landing Page, Screensdesign, Godly, Land-book en 403) : trop récent ou trop niche. La source d'écrans reste le site lui-même.
- `process/` **est vide** : l'auteur ne publie rien sur sa fabrication, hormis les screencasts de doc. Les cinq vidéos YouTube sur l'ère Notion racontent la bascule mais n'ont pas été téléchargées.

## Sources

- **Site officiel** — <https://traderssecondbrain.com> : les six écrans de produit (`/assets/tsb-*.webp`), les composants de Leak Map, la landing, les pages éditoriales.
- **Mode démo public** — <https://traderssecondbrain.com/demo> : huit routes `?mode=demo` sur 64 trades d'exemple, sans compte. Deux écrans capturés.
- **Fichier de tokens** — <https://traderssecondbrain.com/assets/tokens.css> : toute la palette, la géométrie, le motion. Conservé dans `couleurs/`.
- **Second fichier de tokens** — `/assets/landing-v2.css` : la palette mint de la landing 2026.
- **Documentation** — <https://traderssecondbrain.com/docs> : les cinq screencasts de flow.
- **Page À propos** — <https://traderssecondbrain.com/about> : le seul crédit nominatif.
- **Wayback Machine** — snapshot du 2024-04-02 : l'ère du template Notion.
- **Chaîne YouTube** — <https://www.youtube.com/channel/UCXHkeL0AfvFU755ZLtogfJg> : 13 vidéos, dont « I Tracked Trades in Notion for 2 Years. Then Built This (Free) » qui raconte le passage au produit.
- Captures pleine hauteur et écrans de démo : faites maison le 2026-08-31 (`capture-site.py`, `shoot.py`).

## Crédits

- **Igor Manuilov** — fondateur, trader depuis 2014, **seul nom crédité sur le produit** : conception, design et développement. Sa page À propos dit avoir construit TSB « to make execution review more evidence-based and less dependent on memory, scattered spreadsheets, or vague journaling ». X : <https://x.com/TSB_app> · YouTube : <https://www.youtube.com/channel/UCXHkeL0AfvFU755ZLtogfJg>
- **Aucun designer, studio ou agence tiers** identifié — vérifié sur Dribbble, Behance, Product Hunt et les galeries web. Ce dossier documente donc le travail d'une seule personne.
- Typographies : **Instrument Sans** et **DM Mono**, servies via Google Fonts.
- Icônes : **Lucide** 0.475.0.
- Charts du produit : intégration **TradingView** (via l'extension navigateur).

## Mots-clés

journal de trading, trading journal, trade review, prop firm tracker, FTMO, leak map, edge score, playbook, backtester, AI coach, dashboard sombre, dark UI, terminal aesthetic, monospace numbers, DM Mono, Instrument Sans, teal, mint, huit noirs, eight shades of black, bordure en alpha, alpha border, design tokens, single source of truth, thème clair thème sombre, light and dark theme, heatmap de setups, GitHub contribution grid, cartes de trade, trade cards, verdict, grade en lettre, letter grade, expectancy, win rate, R-multiple, drawdown, revenge trading, FOMO, session Asia London New York, extension navigateur TradingView, EA MetaTrader 5, Notion vers app, licence à vie, lifetime licence, anti-abonnement, solo founder, build in public, finance, fintech, SaaS sobre, bento, scroll reveal, video hero

## À voir aussi

- [[tradetrack]] — l'autre journal sombre du lot, en Tailwind/shadcn plutôt qu'en CSS maison.
- [[ultratrader]] — le pendant mobile natif, DA bleue et beaucoup plus démonstrative.
- [[_APPS]] · [[_COMPOSANTS]] · [[_ANIMATIONS]]
