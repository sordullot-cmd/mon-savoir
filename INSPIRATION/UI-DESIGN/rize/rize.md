---
type: inspiration
discipline: ui-design
media: app
source: https://rize.io
url_store:
editeur: Rize Inc. (San Francisco)
type_app: productivité
plateformes: [macos, windows, web]
version: refonte du site en Next.js relevée le 26 août 2026 — app en évolution continue (changelog)
secteur: tech
couleur_principale: noir #080808
couleurs: ["#080808", "#0D0D0D", "#121117", "#1A1A2E", "#4C3F86", "#8764A7", "#AC4BFF", "#01ECFF", "#FAFAFA", "#9F9FA9", "#00BB7F", "#FF6568", "#F99C00", "#1447E6"]
patterns: [paywall, parametres, recherche, empty-state, mode-sombre]
anime: léger
animations: [scroll-reveal, loader]
layout: centré
mood: [dark, minimal, bold]
typos: [Geist, Geist Mono, Raleway]
date_capture: 2026-08-26
tags: [inspiration, ui, ux, web, saas, dark, minimal, a-tester]
---

# Rize — le produit

> Le dossier d'un **traqueur de temps automatique** pour macOS, Windows et web : pas de minuteur, pas de feuille de temps, pas de capture d'écran — l'app lit les métadonnées de la fenêtre active et catégorise toute seule. Ce qui rend la cible intéressante pour un designer, ce n'est pas la fonction : c'est que **le produit a été dessiné par un de ses deux fondateurs, ingénieur de formation**, et qu'on peut suivre six ans de dérive de sa direction artistique image par image.

**Ce qui fait la valeur de ce dossier** : la charte n'est pas devinée, elle est **lue dans le CSS de production** — chaque token de couleur, chaque rayon, chaque police porte son nom d'auteur. Et l'archive donne le film complet : même noir, même wordmark, mais l'accent passe du **cyan électrique** au **violet en dégradé** entre 2022 et 2026.

> **Lecture** : chaque famille est montrée par **une planche** (`<aspect>/planches/`), légendée juste dessous. Les fichiers individuels restent dans leur dossier d'aspect — c'est de là qu'on récupère un écran précis, en résolution native.

---

## En bref

- **Le noir est l'invariant, l'accent est la variable.** `#080808` domine le hero sur les six millésimes archivés, de février 2020 à juillet 2026. Ce qui change, c'est uniquement ce qu'on pose dessus.
- **Toute la couche de marque n'existe que dans le thème sombre.** Les tokens propres à Rize — surfaces, violet, halo, dégradés de cartes — sont déclarés dans le seul bloc `.dark`. Le bloc `:root` est le thème **zinc par défaut de shadcn/ui**, sans une seule personnalisation. Le site force d'ailleurs `<html class="dark">` : le thème clair existe dans le CSS et n'est jamais servi.
- **Deux registres chromatiques opposés, tenus en même temps.** Le site est noir avec une aurore violette ; les captures produit qu'il affiche sont mises en scène dans un chrome de fenêtre qui **flotte au-dessus d'un dégradé pastel cyan → magenta → violet**. Le produit est lumineux, la page est nocturne.
- **Le halo est un token, pas une image.** `--glow-size: 800px` et `--glow-blur: 150px` : l'effet signature du hero est paramétré comme une variable de design system.
- **Une couleur d'accent, en quantité minuscule.** Relevé au pixel sur la refonte 2022 : le cyan `#01ECFF` occupe **0,64 %** de la surface, contre 76,5 % pour le fond. En 2026 les trois violets tiennent chacun 0,21 %.
- **Le produit s'interrompt.** Sa singularité d'interaction n'est pas un écran mais un **moment** : le « Productivity Coach » ouvre une fenêtre par-dessus le travail pour dire « Getting distracted? » ou imposer une pause en plein écran.
- **Trois positionnements successifs en six ans** — prouver son travail pour être promu (2020), outil personnel de focus (2021-2025), logiciel B2B de facturation d'agence (2026) — pour une DA qui, elle, n'a presque pas bougé.

---

## Écrans

### 2026 — l'app après le virage IA

![[ecrans/planches/planche-app-2026.png]]

**La mise en scène est plus constante que l'interface.** Chaque capture est posée dans un chrome de fenêtre macOS ou un onglet de navigateur, flottant au-dessus du même dégradé pastel — c'est une règle de présentation, pas un hasard de gabarit. Sur le fond, l'app de 2026 est devenue un poste de pilotage d'agence : l'orbe violet de l'agent IA remplace l'écran d'accueil (`2026-agent-ia-accueil-orbe.webp`), les rapports sont rédigés en langage naturel avec des montants en dur (`2026-rapport-ia-rentabilite-client.webp`), et le tableau d'équipe empile membres, clients et projets sur une seule vue (`2026-dashboard-equipe-vue-globale.webp`). Les réglages ont été refondus avec un champ de recherche et une barre latérale à deux niveaux (`2026-reglages-refondus-recherche.webp`) — signe qu'ils avaient débordé.

### 2025 — l'app réelle, en thème clair

![[ecrans/planches/planche-app-2025-theme-clair.png]]

**C'est ce que le site ne montre pas.** Ces captures viennent d'un essai complet publié par un tiers, sur la vraie app : la timeline horaire à colonnes (Activity / Clients / Projects / Tasks / Sessions / Calendar), le Focus Score en donut, les tableaux de projets et de clients, et la **barre du bas persistante** qui suit l'utilisateur sur tous les écrans — bouton d'alimentation, chrono contextuel, action principale, et un lecteur de musique d'ambiance. Le widget de barre de menu macOS est là aussi (`2025-barre-menu-macos.webp`), avec son menu natif complet.

Deux écrans en thème sombre viennent d'ailleurs (`2025-teams-*-sombre.png`, galerie Product Hunt) : **le sombre de l'app n'est documenté nulle part sur le site officiel**. On y voit aussi que l'accent n'est pas fixe — un écran Clients passe au magenta parce que la couleur est portée par le client sélectionné.

### 2022 — la refonte cyan

![[ecrans/planches/planche-refonte-2022-cyan.png]]

L'état antérieur, et le plus radical chromatiquement : fond noir violacé `#131117`, un **unique cyan `#01ECFF`** pour tout ce qui compte, un violet en secondaire pour les blocs de timeline. Le même gabarit à trois colonnes encaisse les quatre échelles de temps (jour, semaine, mois, année) sans changer de structure.

---

## Flows

![[flows/planches/planche-parcours.png]]

**Le parcours le plus caractéristique de Rize est une interruption.** Deux moments, tous deux joués par-dessus le travail en cours :

- `flows/coach-01-getting-distracted.webp` — la fenêtre « Getting distracted? » du bloqueur de distraction, en-tête « RIZE · PRODUCTIVITY COACH » à l'éclair cyan, un bouton violet plein « Thanks for the reminder! » et un bouton lavande « This is not a distraction. » Le refus est proposé, mais en second.
- `flows/coach-02-take-your-break-plein-ecran.webp` — le mode pause **plein écran** : le bureau est flouté, une carte claire annonce « Take Your Break! » avec un compte à rebours. Le produit prend la main sur la machine entière.

Les deux autres parcours sont des acceptations de suggestion : `flows/suggestion-entree-de-temps.svg` (le popover qui propose une entrée de temps rédigée par l'IA, avec ses raccourcis clavier Accept / Reject / Edit) et `flows/revue-de-feuille-de-temps.webp` (la file « To review », entrées groupées par client, un bouton Accept par ligne plus un « Accept All »). `flows/routine-ia-debut-de-journee.webp` montre la routine « Start of day » qui rédige un résumé et propose trois actions.

---

## Branding

**Le logotype n'a jamais changé.** Le wordmark `RIZE` en capitales blanches à interlettrage très large est identique de février 2020 à août 2026, sur les six millésimes archivés. En 2026 il rétrécit et se cale à gauche dans une navigation plus dense, c'est tout. C'est le seul élément vraiment stable de la marque — et il est distribué en SVG inline dans l'en-tête du site (`branding/wordmark-rize.svg`), le seul asset de marque récupérable : **il n'existe aucune page de press kit sur le domaine**, vérifié dans le sitemap et le pied de page.

`branding/texture-aurore-violette-hero.webp` — la texture de fond du hero, isolée : une aurore violette diffuse sur noir quasi pur, préchargée en priorité par le site. C'est elle qui porte toute l'ambiance de la page.

`branding/opengraph-2021-maximize-your-productivity.png` — l'image OpenGraph officielle, et elle est **restée figée dans le passé** : elle montre encore l'app de janvier 2021, en cyan, avec l'ancienne baseline. Le décalage entre l'image sociale et le site actuel est un défaut réel, utile à noter.

`branding/session-timer-anneau-cyan-2022.png` — l'écran le plus « marque » du produit : un immense anneau cyan lumineux sur noir, un compte à rebours, deux boutons. Presque aucune donnée. C'est le poster de l'ancienne DA.

`branding/favicon-rize.ico` — un `R` blanc sur carré noir.

---

## Couleurs

Aucun hex n'est deviné ici. Les deux premiers nuanciers sont une **charte publiée** au sens strict — les tokens lus dans le CSS de production servi par `rize.io` le 26 août 2026 — et le troisième est un **relevé de pixels** sur les écrans du dossier.

![[couleurs/palette-declaree-marque-2026.svg]]

**Huit crans de noir pour un site qui paraît monochrome.** C'est la couche que Rize a réellement dessinée, et elle n'existe que dans le thème sombre. Un détail vaut d'être relevé : `--surface-overlay` `#121117` est le seul cran **violacé** de la série, et c'est précisément la valeur qu'on retrouve au comptage de pixels comme fond de l'application. Le violet, lui, n'est pas une couleur mais **un dégradé déclaré en deux arrêts** — `#4C3F86` → `#8764A7` — et les cartes en ont un à trois arrêts.

**Les tokens de marque** (thème sombre uniquement)

| Nom de rôle | Hex | Usage relevé |
| --- | --- | --- |
| `background` | `#080808` | le fond du site, invariant depuis 2020 |
| `surface-alt` | `#0A0A0A` | variante de fond |
| `surface` | `#0D0D0D` | surface de base |
| `surface-overlay` | `#121117` | le seul cran violacé — c'est le fond de l'app |
| `surface-muted` | `#141414` | surface atténuée |
| `surface-elevated` | `#141419` | surface soulevée |
| `surface-raised` | `#1A1A1A` | surface haute |
| `surface-value` | `#1A1A1F` | fond d'une valeur chiffrée |
| `accent-purple-start` | `#4C3F86` | début du dégradé d'accent |
| `accent-purple-end` | `#8764A7` | fin du dégradé d'accent |
| `surface-card-start / mid / end` | `#1A1A2E` · `#16162A` · `#0D0D1A` | dégradé de carte, trois arrêts |
| `pricing-card-start / mid / end` | `#1A1625` · `#16131F` · `#14111C` | dégradé de carte de prix |

Et deux tokens qui ne sont pas des couleurs mais méritent leur ligne : **`--glow-size: 800px`** et **`--glow-blur: 150px`** — le halo du hero est un paramètre de système, pas un fichier image.

![[couleurs/palette-declaree-socle-shadcn.svg]]

**La moitié de la charte n'a pas été dessinée par Rize.** Le jeu complet `card` / `popover` / `muted` / `accent` / `destructive` / `ring` / `sidebar` / `chart-1..5`, plus `--radius: .625rem`, est le préréglage **zinc de shadcn/ui** sorti de sa boîte. C'est une observation utile en soi : un produit dont l'identité tient à trois choses — un noir, un wordmark, un halo — peut laisser tout le reste au défaut de sa bibliothèque sans que ça se voie.

**Le socle, en sombre** (ce que le site sert) : `foreground` `#FAFAFA` · `muted-foreground` `#9F9FA9` · `card` et `popover` `#18181B` · `secondary` et `accent` `#27272A` · `primary` `#E4E4E7` (clair sur sombre) · `ring` `#71717B` · `destructive` `#FF6568` · `sidebar-primary` `#1447E6`.

**Graphiques**, en sombre : `#1447E6` bleu · `#00BB7F` vert · `#F99C00` orange · `#AC4BFF` violet · `#FF2357` rouge.

![[couleurs/palette-relevee-app-2022-contre-2026.svg]]

**Le noir ne bouge pas, l'accent bascule.** En 2022, un seul cyan `#01ECFF` porte tout ce qui compte — et il n'occupe que **0,64 %** de la surface contre 76,5 % au fond `#131117`. En 2026, le cyan a été remplacé par un dégradé de trois violets (`#6B56B5`, `#7B69BD`, `#8C7CC5`), chacun à 0,21 %, et il n'en reste qu'une trace : un `#95E5F7` résiduel sur ce qui touche encore au focus. La discipline, elle, est intacte : **l'accent reste sous 1 % de la surface dans les deux millésimes**.

Les fonds clairs qui dominent le relevé 2026 (`#F7F7FC` à 19,9 %, `#FEFEFF` à 17 %) viennent de ce que la moitié des écrans publiés cette année-là sont en thème clair — l'app a les trois modes Dark / Light / System, le site n'en a qu'un.

**Mesures de tiers, à ne pas confondre avec ce qui précède** : les violets `#6555bd`, `#5b4ca5`, `#8563a6` relevés sur le millésime archivé de juillet 2026 sont une mesure faite sur une page de la Wayback Machine, recompressée — ils encadrent le dégradé déclaré sans le recouvrir exactement.

---

## Composants

Indexés dans [[_COMPOSANTS]].

![[composants/planches/planche-composants.png]]

- `composants/carte-coach-productivite_rize.svg` et `carte-rentabilite-equipe_rize.svg` — **récupérés en SVG vectoriel**, pas en capture : le site publie quatre de ses maquettes d'UI en vectoriel, donc chaque hex, chaque rayon et chaque dégradé y est lisible directement dans le fichier. C'est une ressource rare pour une refonte.
- `composants/command-bar-cmd-k_rize.webp` — la palette de commandes `Cmd+K` en surimpression sur le dashboard assombri, avec ses badges de raccourci clavier alignés à droite.
- `composants/galerie-modeles-de-rapports_rize.webp` et `galerie-modeles-objectifs_rize.webp` — deux galeries de modèles, même patron : grille de cartes à bord fin, icône, titre gras, phrase de description. Le second finit sur une ligne de deux cartes au lieu de trois.
- `composants/lignes-de-reglages-a-toggle_rize.webp` — le patron de réglage qui tient les 19 rubriques : titre gras et description grise à gauche, contrôle à droite. C'est le composant le plus réutilisé de l'app.
- `composants/segmente-periode-et-daily-summary_rize.webp` — le sélecteur Day / Week / Month / Year / Custom et la carte Daily Summary, cadrés assez près pour lire la typo et les pastilles.
- `composants/popover-musique-ambiance_rize.webp` — le popover « Music & Sounds » et sa grille 3×3 de vignettes illustrées (Lo-Fi Beats, Binaural 40 Hz, Coffee Shop…). Un lecteur de musique intégré à un outil de facturation : c'est le vestige le plus visible de l'ère « outil personnel de focus ».
- `composants/modale-mcp-connexion_rize.webp` — la modale MCP, avec ses deux boutons « Connect with one click » Claude et ChatGPT.
- `composants/menu-skills-agent_rize.webp` · `cartes-integrations_rize.webp`.
- De la refonte 2022 : `jauges-segmentees-focus-2022_rize.png` (des jauges linéaires à segments dégradés et curseur blanc — un composant qu'on ne voit nulle part ailleurs), `daily-summary-donut-2022_rize.png` (le donut à quatre segments Focus / Meetings / Breaks / Other, cadré serré : c'est là qu'on lit la palette exacte des quatre états) et `detail-objectif-grille-2022_rize.png`.

> Quatre captures de cette section portent des **annotations rouges ajoutées par l'auteur du test tiers** (rectangles de mise en évidence). Elles sont gardées parce que le composant qu'elles montrent n'existe nulle part ailleurs — mais le trait rouge n'est pas de Rize.

---

## Animations

Indexées dans [[_ANIMATIONS]].

- `animations/scroll-bascule-vers-la-section-violette_rize.gif` — le geste du site : 16 000 px de défilement, et une seule rupture, quand le noir cède la place à une **section pleine largeur en violet saturé** (« Visibility without surveillance. Productivity without micromanagement. »). C'est la première zone non noire de l'histoire du site, apparue avec la refonte 2026.
- `animations/entree-du-hero-fondu-et-halo_rize.gif` — le hero se révèle en fondu, halo puis titre puis contenu. **Deux images seulement** : la page est trop lourde pour le capteur, qui n'a pas tenu le rythme. Le GIF montre l'avant et l'après, pas la courbe entre les deux.

Ce que je n'ai **pas** pu relever : les durées et les courbes réelles. Le CSS ne publie que `--default-transition-duration: .15s` et `cubic-bezier(.4,0,.2,1)`, qui sont les valeurs par défaut de Tailwind, plus les deux paramètres du halo. Aucune valeur de motion propre à Rize n'est sourçable en l'état.

---

## Marketing

![[marketing/planches/planche-site-2026-desktop.png]]

Douze pages capturées en pleine hauteur le 26 août 2026, desktop et mobile. **Le site n'a pas de thème clair** : la capture « sombre » est sortie rigoureusement identique à la capture normale (même empreinte MD5), parce que la racine porte `class="dark"` en dur — le fichier a donc été supprimé plutôt que gardé comme faux témoin.

La home fait **16 281 px de haut**, contre 3 845 px en 2020 : la landing a quadruplé en six ans à largeur constante. Sa structure : hero à halo, bandeau de statistiques (20+%, < 5 min, 0, 100 %), preuve sociale Product Hunt, section problème en trois cartes, verticales métier en six cartes, la section violette pleine, dashboards de rentabilité, coach de productivité, intégrations, FAQ en accordéon de douze items, puis un dernier visuel isométrique où les écrans de l'app flottent sur un halo violet intense.

`marketing/hero-dashboard-4k.webp` — le visuel du hero en 3840 px de large, hors de la page.
`marketing/composition-inclinee-halo-violet.svg` — la composition finale, **en vectoriel**.
`marketing/email-rapport-quotidien.webp` — le rapport quotidien par email, un registre à part : noir sur blanc, sans halo ni violet.

**Tarifs relevés le 26 août 2026** : Basic 9,99 $/mois en annuel (12,99 $ mensuel, 500 crédits IA), Pro 23,99 $ (29,99 $ mensuel, 1000 crédits, badge « Most Popular »), Max 39,99 $ (49,99 $ mensuel, 3000 crédits, badge « Best Value »), plus Enterprise sur devis. Les **crédits IA** sont devenus l'axe de segmentation du prix.

---

## Process

![[process/planches/planche-refonte-2022.png]]

**Rize n'a publié qu'un seul texte de design en six ans**, et c'est celui-là : le changelog du 4 novembre 2022 sur la refonte du dashboard. Il argumente une vraie décision d'architecture de l'information. Avant, la hiérarchie mettait en avant les **métriques dérivées** (Work Hours, Focus Time, Break Time, Meeting Time) et reléguait les catégories au second plan. Après, « les catégories sont l'information la plus importante du dashboard », au motif qu'« une catégorisation correcte est la condition du bon fonctionnement de toutes les autres fonctions ». Conséquence de structure : un écran unique surchargé devient **six onglets** — Home, Categories, Focus & Productivity Hub, Projects, Session Timer, Goals. Simplification annexe assumée : Work Hours cesse d'être un calcul à cas particuliers pour devenir « la somme de tes catégories de travail ».

Détail que je garde parce qu'il dit quelque chose du produit : sur `process/refonte-2022-projects-timeline-sessions.png`, le projet suivi à l'écran s'appelle **« Dashboard Simplify Refactor »** — l'équipe a chronométré la refonte avec l'outil qu'elle refondait.

`process/premier-site-waitlist-2020.png` — l'état zéro, publié par le fondateur lui-même : la toute première landing, avant tout produit, avec sa liste d'attente et son compteur social (« 106 people are currently in line »). Le noir, le wordmark espacé et le cyan sont **déjà là**. Basse résolution : c'est la seule version publiée.

---

## Archive

![[archive/planches/planche-millesimes-2020-2026.png]]

Six millésimes du site, capturés en pleine hauteur sur la Wayback Machine. Le domaine était **parqué chez Sedo de 2016 à 2018** — toute recherche antérieure à 2020 est hors sujet.

Les baselines successives, relevées mot pour mot avec leur date, racontent le produit mieux qu'un résumé :

| Date | Baseline | Ce que ça dit |
| --- | --- | --- |
| 25 févr. 2020 | « Track your work. Get promoted faster. » | prouver son travail pour être promu — 243 inscrits en liste d'attente |
| 12 août 2020 | « Track your work. Level up faster. » | 1 208 inscrits |
| 5 févr. 2021 | « Your personal productivity tracker. » | l'app existe |
| 21 avr. 2021 | « Maximize Your Productivity » | tiendra quatre ans et demi |
| 21 juin 2021 | « an intelligent time tracker » | (« smart » à partir de juin 2022) |
| 2 déc. 2023 | « Maximize Your Productivity with A.I. » | Rize devient un « AI productivity coach » |
| 7 févr. 2025 | « Maximize Your Productivity » | l'IA redescend de coach à qualificatif |
| 3 nov. 2025 | « Automate Your Time Tracking » | virage B2B |
| 10 juin 2026 | « You do the work. Rize tracks the time. » | |
| 30 juil. 2026 | « Automatic time tracking that gives your whole team visibility. » | l'équipe, pas l'individu |

Trois autres faits sortent de cette série :

- **La landing s'allonge sans arrêt** : 3 845 px (2020) → 8 940 (2021) → 9 751 (2023) → 12 346 (2025) → 16 127 (2026), à largeur constante de 1920.
- **Le prix d'entrée payant double en quatre ans** : 6,99 $/mois en annuel (2021) → 9,99 $ (2023, avec l'ajout d'un palier gratuit et l'essai ramené de 14 à 7 jours) → 12,99 $ (2025) → 9,99 $ pour un Basic amputé face à un Pro à 23,99 $ (2026). La gamme passe de deux à quatre paliers.
- **La même capture d'app reste en vitrine près de cinq ans** : le screenshot daté « Friday, January 29, 2021 » sert de visuel de hero en 2021, en 2023 **et** en 2025. Il ne disparaît qu'à la refonte de 2026.

Enfin, la refonte 2026 est aussi un changement de socle technique : Raleway et Webflow disparaissent au profit de Geist et d'un build Next.js. `landing-2020-02.png` comporte deux images cassées — les assets n'ont pas été archivés à cette date.

---

## Typographie

Les trois familles sont **auto-hébergées et servies en woff2**, relevées dans les `@font-face` du CSS de production :

| Police | Rôle | Nature | Licence |
| --- | --- | --- | --- |
| **Geist** | texte et interface | variable, `font-weight: 100 900` | SIL OFL (Vercel) |
| **Geist Mono** | chiffres et code | variable | SIL OFL (Vercel) |
| **Raleway** | résiduel | variable | SIL OFL |

Deux choses à en tirer. D'abord, **les fallbacks sont métriquement ajustés**, ce qui est rare et soigné : `Geist Fallback` pointe sur `local(Arial)` avec `ascent-override: 95.94%`, `descent-override: 28.16%` et `size-adjust: 104.76%` — le texte ne bouge pas au chargement de la police. Ensuite, **Raleway est un vestige** : c'était la police du site de 2020 à 2025, du temps de Webflow. La refonte 2026 est passée à Geist, mais le token `--font-raleway` survit dans le CSS. Aucune fiche de font du vault ne couvre encore ces familles — `/font` reste à passer sur Geist si le besoin s'en présente.

---

## Sources

Cinq sources menées en parallèle, plus mes propres captures.

- **Site officiel** — `https://rize.io` : les captures produit du **changelog** (une mine : environ 200 entrées, servies en original depuis `rize-io.s3.us-west-1.amazonaws.com/assets/blog/`, jusqu'à 2994 × 1938), quatre maquettes d'UI **en SVG vectoriel** sous `rize.io/images/`, le wordmark inline, la texture du hero, et surtout le **CSS de production** d'où sortent tous les tokens et tous les `@font-face`. Sitemap de 534 URLs. Aucune page de press kit.
- **Mes captures** — `capture-site.py`, 26 août 2026 : douze pages en pleine hauteur, desktop et mobile.
- **Test tiers approfondi** — `https://dhruvirzala.com/rize-review/` (publié le 11 août 2025, mis à jour le 26 mai 2026) : environ 70 captures maison de l'app **en fonctionnement**, en 2880 × 1800. C'est la seule source qui montre l'app derrière l'écran d'accueil.
- **Product Hunt** — `https://www.producthunt.com/products/rizeio` : trois lancements (18 mai 2021, #1 du jour ; 13 octobre 2021, app Windows ; 29 juillet 2025, Rize Teams), et la seule galerie qui documente le **thème sombre** de l'app.
- **Indie Hackers** — l'AMA du 26 octobre 2021 et le post « Bootstrapping a personal productivity SaaS to $10k MRR » : c'est là que le partage des rôles de design est établi, et là qu'on trouve la première landing.
- **Wayback Machine** — 311 captures de `rize.io` entre 2016 et 2026, dont six millésimes retenus.

**Ce que je n'ai pas eu**, et qui manque vraiment : Land-book et Lapa Ninja bloquent sur Cloudflare, Mobbin exige un compte, Dribbble et Reddit refusent le fetch direct, X répond en 402 et les miroirs Nitter sont fermés, G2 répond 403. Aucune galerie de webdesign n'a jamais indexé rize.io — vérifié source par source, y compris via l'API publique de Refero (329 sites, aucun Rize).

**Trois homonymes à ne pas confondre** avec la cible, tous rencontrés pendant la récolte : `rize3d.com` (impression 3D, indexé sur Awwwards sous « Rize One »), `rize.money` (plateforme d'épargne, qui occupe la fiche AlternativeTo et la page `producthunt.com/posts/rize`), et une série « Rize App » sur Dribbble faite pour YouNow, une app de vidéo en direct.

---

## Crédits

- **Will Goto** — cofondateur, ancien CEO, aujourd'hui Chairman of the Board. **C'est lui qui a dessiné le produit.** Ingénieur logiciel devenu product designer, B.S. Materials Science & Engineering (Cornell, 2010), ancien Senior Software Engineer chez Periscope puis Twitter. Sa réponse à un lecteur d'Indie Hackers qui lui demandait si le design était fait en interne, le 26 octobre 2021 : « The initial branding work for our website was done by an agency, all other design was done in-house... by me actually. » — [LinkedIn](https://www.linkedin.com/in/wgoto/) · [Medium](https://wrgoto.medium.com/) · [X](https://twitter.com/wrgoto) · [Product Hunt](https://www.producthunt.com/@wrgoto). Son domaine personnel `wrgoto.com` ne résout plus : il n'a pas de portfolio en ligne.
- **Macgill Davis** — cofondateur, CEO aujourd'hui. Ancien ingénieur Peer puis Twitter, cofondateur de Humble Dot (2017). Côté design il est le porte-voix, pas la main : il signe la plupart des articles du blog et anime The Rize Podcast. Ses propres données servent de jeu de démonstration dans les captures du changelog (« Welcome back, Macgill! »). — [LinkedIn](https://www.linkedin.com/in/macgill-davis-74789849/) · [X](https://twitter.com/macgillbdavis).
- **L'agence du branding initial du site** — **non identifiée**. Will Goto confirme son existence sans jamais la nommer, aucune agence ne revendique Rize en étude de cas. C'est le trou principal de ce dossier.
- **Équipe élargie**, relevée sur la page Makers de Product Hunt : Glendale Acosta (frontend, ex-SentinelOne), Mirna De Jesus Cambero (software engineer), Ed Song (growth), Hyon Lee. **Aucun poste de design dans la liste** — ce qui confirme la citation par la structure.
- Le test tiers dont viennent les captures de l'app réelle est signé **Dhruvir Zala** — [dhruvirzala.com](https://dhruvirzala.com/rize-review/).

Rize Inc. est **bootstrappée et rentable**, sans levée de fonds — la société n'est pas passée par Y Combinator, contrairement à ce qu'on lit parfois ; c'est leur startup précédente, Humble Dot, qui était financée.

---

## Pourquoi je l'aime

**La discipline chromatique.** Un seul accent, jamais plus, et toujours sous 1 % de la surface — mesuré, pas ressenti. Tout le reste est du noir échelonné. C'est un système qu'on peut copier sans copier la marque.

**L'honnêteté du montage.** Rize ne cache pas qu'il monte sur shadcn/ui : il pose sa couche de marque par-dessus, en trois gestes seulement — un noir, un wordmark, un halo — et laisse tout le reste au défaut de la bibliothèque. Ça marche, et ça montre où il faut vraiment dépenser du dessin.

**Le halo en token.** `--glow-size` et `--glow-blur` : traiter un effet d'ambiance comme une variable de design system plutôt que comme une image exportée, c'est exactement la bonne décision.

**Le moment plutôt que l'écran.** La singularité du produit, c'est la fenêtre qui s'ouvre par-dessus le travail pour demander « Getting distracted? ». Un designer product a plus à apprendre de ce moment-là que de dix dashboards.

---

## À réutiliser pour

- **Une interface sombre dense** — les huit crans de noir sont un barème directement transposable, et le fait que le fond de l'app (`#121117`) soit légèrement violacé alors que le site est neutre (`#080808`) est une nuance qui se copie.
- **Un halo d'ambiance paramétré** — deux variables, pas un PNG.
- **Une landing de SaaS très longue** qui reste tenue : une seule rupture chromatique sur 16 000 px, et elle tombe sur l'argument le plus important de la page.
- **Des notifications qui interrompent sans agresser** — le vocabulaire du Productivity Coach, la hiérarchie de ses deux boutons, la pause en plein écran.
- **Un tableau de bord de chiffres** — la barre du bas persistante, le sélecteur de période segmenté, la carte de résumé à donut, les jauges segmentées de 2022.
- **Une refonte de facturation** : les écrans Teams 2026 sont un cas d'école de passage d'un produit personnel à un produit d'agence, sans changer le système visuel.

---

## Mots-clés

rize · rize.io · time tracking · traqueur de temps · suivi du temps · time tracker · automatic time tracking · productivité · productivity · focus · deep work · pomodoro · minuteur · session timer · dashboard · tableau de bord · analytics · rapports · reporting · facturation · billable hours · heures facturables · rentabilité · profitability · agence · freelance · timesheet · feuille de temps · macOS · Windows · app desktop · menu bar · barre de menu · SaaS · B2B · dark mode · thème sombre · noir · violet · purple · gradient · dégradé · halo · glow · aurore · aurora · minimal · sobre · dense · data-dense · shadcn · shadcn/ui · zinc · Tailwind · Tailwind v4 · Next.js · design tokens · variables CSS · Geist · Geist Mono · Raleway · Vercel · command palette · Cmd+K · palette de commandes · donut · anneau · segmented control · sélecteur segmenté · toggle · réglages · settings · empty state · paywall · pricing · crédits IA · AI credits · agent IA · MCP · Model Context Protocol · Claude · ChatGPT · productivity coach · distraction blocker · bloqueur de distraction · urge surfing · break mode · pause · burnout · privacy first · sans surveillance · no screenshots · Will Goto · Macgill Davis · Product Hunt · Indie Hackers · bootstrapped · Wayback · millésimes · refonte · redesign · cyan · turquoise
