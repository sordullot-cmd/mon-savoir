---
type: inspiration
discipline: ui-design
media: app
source: https://www.tradetrack.space/en
url_store:
editeur: Oleksandr Drohomyretskyi (personne physique, Varsovie)
type_app: finance
plateformes: [web]
version: beta publique, relevée le 2026-08-31
secteur: finance
couleur_principale: noir #161616
couleurs: ["#030303", "#090909", "#161616", "#1f1f1f", "#00bc7d", "#fb2c36", "#a855f7", "#fafafa"]
patterns: [mode-sombre, empty-state, parametres, recherche]
anime: oui
animations: [scroll-reveal, transitions-page, hover, loader, text-anim, marquee]
layout: grille
mood: [dark, minimal, editorial]
typos: [Inter Tight, Geist Mono]
date_capture: 2026-08-31
tags: [inspiration, ui, dark]
---

# TradeTrack

> Journal de trading construit par une seule personne à Varsovie, encore en beta gratuite, et déjà le système de design le plus rigoureux du lot : trente-neuf animations nommées, un rail de navigation plus noir que tout le reste, et un bouton primaire qui refuse d'être coloré.

**Sources :** site officiel (captures produit servies en clair) · CSS de production (365 ko lus intégralement) · Wayback Machine (un seul snapshot) · mentions légales · RankInPublic

> **Lecture** : chaque famille d'écrans est montrée par **une planche** (`<aspect>/planches/`), légendée juste dessous. Les fichiers individuels restent dans leur dossier d'aspect.

## En bref

- **Une personne physique, pas une société.** Oleksandr Drohomyretskyi, Kopalniana 14C, Varsovie — nommé dans la Privacy Policy et les Terms. Son propre compte apparaît comme utilisateur de démo dans une capture officielle.
- **Le bouton primaire est blanc** (`#e5e5e5` en sombre, `#171717` en clair). Aucune couleur d'action : dans un produit où tout est déjà vert ou rouge, l'action doit être neutre pour rester visible.
- **Le rail de navigation est le point le plus noir du système** (`#030303`) — plus noir que l'app (`#161616`) et que la landing (`#090909`). Trois noirs, trois rôles.
- **Les bordures sont du blanc en alpha** (10 % et 15 %), jamais des gris opaques — en clair, elles redeviennent opaques (`#e5e5e5`). Le système sait qu'un même effet demande deux techniques différentes.
- **Trente-neuf `@keyframes` nommés**, avec des cascades chiffrées au centième de seconde (le hero s'ouvre en sept temps, de 120 ms à 860 ms de délai). C'est une chorégraphie écrite, pas des transitions au hasard.
- **Un seul accent coloré hors gris/vert/rouge** : le violet `#a855f7` de l'IA, découvert dans les `box-shadow` d'une animation de pastille.
- **Les couleurs de gain et de perte sont les valeurs Tailwind par défaut** (emerald et red 400-700) : le produit n'a pas de palette propriétaire pour ses données, et ça ne se voit pas.
- **Deux jeux de couleurs de charts totalement différents** entre sombre et clair — pas une inversion, un second jeu.
- **Pas d'app mobile** : « A dedicated mobile app is on our roadmap ». L'expérience mobile est même verrouillée en portrait par un écran de garde.

## Écrans

![[ecrans/planches/planche-ecrans.png]]

**L'app n'est visible que par les captures que l'éditeur publie — et il les publie bien.** Le dashboard réel (1920 × 945, servi hors pipeline d'optimisation) montre la vraie densité : rail d'icônes noir, quatre tuiles de KPI dont un win rate en jauge d'arc et un avg win/loss en barre bicolore, un `Progress tracker` en heatmap de carrés façon GitHub, une courbe de P&L cumulé, puis un calendrier mensuel coloré jour par jour avec ses totaux hebdomadaires.

- `ecrans/dashboard.png` — le dashboard courant, la capture la plus fiable du produit.
- `ecrans/mockup-liste-trades.png` — la liste de trades en tableau très dense (douze colonnes : Date, Symbol, Account, Direction, PnL, Profit %, Result, Session, Risk, RR, Strategy…), avec un dropdown de filtre ouvert et un bouton `AI Insights` violet.
- `ecrans/mockup-ai-health-check.png` — le `Trading Health Check` : un verdict rédigé, un tag rouge `Needs attention`, et trois compteurs — 1 `CRITICAL`, 12 `WARNINGS`, 13 `WHAT'S WORKING`. Chaque constat porte son label (`RULING EVIDENCE`, `CONSISTENCY`), sa valeur (`-6.22R`) et son action.
- `ecrans/mockup-backtest-replay.png` — le mode replay : chandeliers USDJPY avec zones de stop et de target dessinées, lecteur bougie par bougie, panneau d'ordre flottant (Equity, Balance, PNL, Qty, Risk %, gros boutons Buy/Sell).
- `ecrans/mockup-ai-chat.png` — l'AI Chat : la réponse de l'IA est un **tableau plus un graphique**, pas un paragraphe. C'est le bon réflexe pour un produit de données.

Ces quatre derniers fichiers sont des mockups MacBook publiés par l'éditeur : l'app étant derrière login, c'est la seule source d'écrans. Le motif de mise en scène est constant — un MacBook carré 2560 × 2560 sur fond noir pur, avec une à trois cartes de l'UI **extraites de l'écran et flottant en avant-plan**.

## Composants

`composants/lignes-de-trades_tradetrack.webp` — le détail que l'éditeur a jugé bon d'isoler sur fond noir : les lignes du tableau de trades, avec leurs badges pilule `BUY` vert / `SELL` rouge, les P&L colorés, un fond de ligne teinté très désaturé selon le résultat, et une ligne détachée en survol avec bordure claire et ombre portée. Tout le savoir-faire du produit tient dans cette image : **la couleur informe le fond, pas seulement le texte**.

## Animations

`animations/hero-cascade-entree_tradetrack.gif` — les quatre premières secondes de la home, où se joue la cascade d'ouverture.

**Le système de motion est écrit, pas improvisé.** Relevé dans le CSS de production :

- **Cascade du hero** : `heroBadgeIn` .3s → `heroFadeIn` .35s (délai .12s) → trois `.3s` aux délais .28s / .42s / .52s → quatre `heroStatIn` .25s aux délais .62s / .7s / .78s / .86s. Sept temps, une seconde en tout.
- **Transitions de page** : `vt-page-out` .16s ease-out, `vt-page-in` .22s ease-out (View Transitions API).
- **Header** : `headerSlide` .35s `cubic-bezier(.4,0,.2,1)`, délai 50 ms.
- **Pastille IA** : `ai-pill-beam-spin` 3.2s linear infinite — avec un `@property --ai-beam-angle` de type `<angle>` animé de 0 à 360°, plus `ai-pill-orb-pulse` 2.8s et `ai-pill-label-sheen` 3.2s. Trois animations superposées pour un seul bouton.
- **Boucles ambiantes** : `heroFloat` 3s, `heroPulse` 2s, `heroDrip` 2s, `phone-rotate` 2s, `spin-slow` 3s linear, `gradient-text-flow` 3s.
- **États** : `skeleton-shimmer` 1.8s, `tradeCellSaving` 1.2s linear (le retour visuel de sauvegarde d'une cellule), `caret-blink` 1.25s.
- **Courbes du système** : `cubic-bezier(.4,0,.2,1)` (standard), `cubic-bezier(.22,1,.36,1)` (overshoot doux), plus `(0,0,.2,1)`, `(.4,0,.6,1)`, `(.8,0,1,1)`.
- **Durées** : .1s / .15s / .2s / .3s / .5s / .7s / 1s.

## Branding

![[branding/planches/planche-logo.png]]

**Une fusée dans la hampe du T.** L'emblème est un carré noir à coins très arrondis contenant un T blanc dont le fût est remplacé par une fusée vue de face — hublot rond, ailerons, trois flammes. Le wordmark joue un contraste de graisse **au milieu du mot** : `Trade` en gras, `Track` en régulier. C'est le seul geste de marque un peu ludique d'un produit par ailleurs très austère, et il est servi en 8000 × 8000.

- `branding/emblem-fusee.webp` — l'emblème, 8000 px.
- `branding/wordmark-noir.png` — le logotype horizontal (original 18 751 × 5 605, ramené à 4 000 px : au-delà, le fichier est inexploitable).
- `branding/wordmark-blanc.png` — la version réellement utilisée dans le header sombre (seule taille servie : 1 400 px).

Aucun press kit : ces trois fichiers ont été trouvés dans les chemins référencés par le HTML (`/logo-emblem.webp`, `/logo-posters/…`).

## Couleurs

![[couleurs/palette-app-sombre.svg]]

**Trois noirs, trois rôles — et c'est la hiérarchie, pas la couleur, qui structure l'interface.** Le rail de navigation (`#030303`) est plus sombre que l'app (`#161616`), et la landing (`#090909`) se place entre les deux. Un utilisateur ne le remarquera jamais consciemment ; il saura pourtant toujours où il est. Les bordures en blanc alpha (10 % et 15 %) suivent le fond au lieu de le contredire.

**Fonds**

| Nom de token | Hex | Usage |
| --- | --- | --- |
| `--app-rail` | `#030303` | le rail de navigation, le plus sombre du système |
| `#landing-dark-root` | `#090909` | la landing, plus noire que l'app |
| `--sidebar` | `#0b0b0b` | colonne latérale |
| `--background` | `#161616` | le fond de l'app |
| `--card` / `--popover` | `#1f1f1f` | cartes et surcouches |
| `--secondary` / `--muted` / `--accent` | `#262626` | surfaces neutres |
| `--sidebar-accent` | `#222222` | élément actif du rail |

**Textes et actions**

| Nom de token | Hex | Usage |
| --- | --- | --- |
| `--foreground` | `#fafafa` | texte principal |
| `--sidebar-foreground` / `--primary` (sidebar) | `#eeeeee` | texte du rail |
| `--muted-foreground` | `#a1a1a1` | labels |
| `--primary` | `#e5e5e5` | **le bouton primaire est blanc**, pas coloré |
| `--primary-foreground` | `#171717` | texte sur bouton clair |
| `--destructive` | `#ff6568` | suppression |
| `--ring` | `#737373` | focus |
| `--border` / `--input` | `#ffffff` à 10 % / 15 % | bordures, en alpha |

![[couleurs/palette-app-clair.svg]]

**En thème clair, le rail reste noir.** `--app-rail: #0a0a0a` : la navigation ne suit pas le thème, elle reste l'ancre sombre de l'écran. Et le rouge de suppression change carrément de teinte (`#ff6568` en sombre, `#e40014` en clair) au lieu d'être simplement assombri.

| Nom de token | Hex clair | Usage |
| --- | --- | --- |
| `--background` / `--card` / `--sidebar` | `#ffffff` | blanc pur |
| `--secondary` / `--muted` / `--accent` | `#f5f5f5` | surfaces neutres |
| `--app-rail` | `#0a0a0a` | **le rail reste noir même en clair** |
| `--foreground` | `#0a0a0a` | texte principal |
| `--primary` | `#171717` | bouton primaire noir |
| `--border` | `#e5e5e5` | opaque, contrairement au sombre |
| `--destructive` | `#e40014` | rouge franc |

![[couleurs/palette-charts-et-donnees.svg]]

**Les deux jeux de couleurs de charts n'ont aucun rapport l'un avec l'autre.** En sombre : bleu, vert, ambre, violet, rose. En clair : orange, sarcelle, pétrole, jaune, ambre. Ce n'est pas une inversion de luminosité, c'est une seconde palette pensée pour un fond blanc — et c'est rare de voir un produit aller jusque-là. Le violet `#a855f7` de l'IA, lui, ne se trouve nulle part dans les tokens : il est **dans les `box-shadow` du keyframe `ai-pill-orb-pulse`**, à 40 % puis 70 % d'opacité.

**Charts — sombre**

| Nom de token | Hex | Rôle |
| --- | --- | --- |
| `--chart-1` | `#1447e6` | bleu |
| `--chart-2` | `#00bb7f` | vert |
| `--chart-3` | `#f99c00` | ambre |
| `--chart-4` | `#ac4bff` | violet |
| `--chart-5` | `#ff2357` | rouge-rose |

**Charts — clair**

| Nom de token | Hex | Rôle |
| --- | --- | --- |
| `--chart-1` | `#f05100` | orange |
| `--chart-2` | `#009588` | sarcelle |
| `--chart-3` | `#104e64` | pétrole |
| `--chart-4` | `#fcbb00` | jaune |
| `--chart-5` | `#f99c00` | ambre |

**Profit, perte, IA — relevés au pixel sur les captures produit**

| Nom de rôle | Hex | Note |
| --- | --- | --- |
| vert de gain | `#00bc7d` | dominant ; variantes `#00d492`, `#007a55`, `#10b981` |
| rouge de perte | `#fb2c36` | dominant ; variantes `#ff6467`, `#c10007`, `#ef4444` |
| bleu d'accent | `#2b7fff` | relevé |
| violet IA | `#a855f7` | lu dans les `box-shadow` de `ai-pill-orb-pulse` |

Ce sont les valeurs Tailwind v4 par défaut (emerald / red / blue 400-700). Fichier source conservé : `couleurs/tokens-de-production.css`.

**Géométrie** : `--radius: .625rem` (10 px) · `--app-rail-w: 3.5rem` (56 px) · `--app-topbar-h: 3.5rem` (56 px).

## Marketing

![[marketing/planches/planche-pages.png]]

**La landing est bâtie sur quatre douleurs citées à la première personne.** « I dig through spreadsheets by hand… », « I spend hours typing trades into Notion by hand… » — chacune appariée à un module du produit. Puis cinq étapes, trois cibles (Forex / Crypto / Prop firm), une FAQ. Le concurrent nommé n'est pas TradeZella : c'est **le tableur** (« The real alternative is the spreadsheet you stop updating ») et Notion.

- `marketing/landing.png` — la landing pleine hauteur.
- `marketing/mockup-signature-cartes-flottantes.png` — le motif de composition récurrent du site.
- `marketing/og-card.png` — la carte sociale.
- `marketing/poster-page-connexion.jpg` — le visuel qui habille la page de connexion : une photo d'architecture en noir et blanc, sans aucun élément de marque. Photo de stock, mais le choix est juste : rien ne concurrence le formulaire.
- `marketing/poster-blog-image-generee.webp` — **la fausse note du dossier** : une image générée (femme en costume devant un hologramme bleu de graphiques) en bannière de blog. Registre visuel à l'opposé de la sobriété du produit.
- Pages SEO : `en-about`, `en-blog`, `integrations`, `en-trading-journal-forex`, `en-trading-journal-prop-firm`, `en-auth-signup`.

Ton de voix : deuxième personne, phrases courtes, vocabulaire de trader assumé (R-multiple, expectancy, drawdown, prop firm, *demons*), promesses non enjolivées — « Every trade you don't journal is profit you'll never find » — et une section « no lock-in and no dark patterns ». Traction affichée : « 600+ active traders », « 35K+ trades logged » (la page About dit 500+ et 30K+ : les chiffres ne concordent pas d'une page à l'autre).

## Archive

![[archive/planches/planche-mars-2026.png]]

**Le site sert encore les captures de mars 2026, et elles racontent un abandon.** Le dashboard d'alors affichait deux grandes cartes `TOP INSIGHT · BETA` — une verte (« VAH/VAL is your best performing tool »), une ambre (« Avoid trading on Friday ») — remplacées depuis par le Health Check et le Progress tracker. On voit donc un module de conseil automatique passer d'une carte bien visible à un rapport dédié : la même fonction, reléguée.

- `archive/dashboard-mars-2026-top-insight.webp` — les Top Insights disparus.
- `archive/statistiques-mars-2026.webp` — l'écran Statistics d'alors : six tuiles avec chacune son icône dans un carré teinté de sa propre couleur, un donut Win/Loss, une equity curve.
- `archive/trades-mars-2026.webp` — la liste de trades, quatorze colonnes.
- `archive/landing-wayback-2026-04-10.html` et `pricing-wayback-2026-04-10.html` — le seul snapshot Wayback du domaine (10 avril 2026), conservé en HTML : l'accroche était alors « This Isn't a Journal. It's Your Personal Analyst. », et une page `/pricing` existait avec une offre unique à 0 $ — depuis supprimée du site et du sitemap.

## Typographie

Deux familles variables, auto-hébergées :

- **Inter Tight** (variable 100-900, sept sous-ensembles unicode dont le cyrillique) — toute l'interface et les titres.
- **Geist Mono** (variable 100-900) — les chiffres et les données.

Le fallback est déclaré finement : `Inter Tight Fallback` sur `local(Arial)` avec `ascent-override: 100.51%`, `descent-override: 25.03%`, `size-adjust: 96.39%`. Peu de produits vont jusqu'à corriger les métriques de leur police de secours. Échelle de graisses tokenisée : 400 / 500 / 600 / 700 / 900.

Ni l'une ni l'autre n'a de fiche dans le vault — candidates à `/font`.

## Pourquoi je l'aime

Parce qu'une personne seule, en beta gratuite, a écrit un système de design plus discipliné que la plupart des équipes financées : trois noirs hiérarchisés, un bouton primaire volontairement incolore, des bordures en alpha, deux palettes de charts, et trente-neuf animations nommées avec leurs délais. Rien n'est spectaculaire ; tout est décidé. C'est le dossier à ouvrir quand on cherche non pas une idée visuelle mais **la preuve qu'un système tient**.

Et le geste de la fusée dans le T sauve l'ensemble d'être froid — un seul endroit où la marque sourit, et il est bien choisi.

## À réutiliser pour

- **Hiérarchiser une app sombre par les noirs** : rail plus sombre que le contenu, landing entre les deux.
- **Un bouton primaire neutre** quand l'interface est déjà saturée de vert et de rouge sémantiques.
- **Des bordures en blanc alpha** en sombre, opaques en clair — deux techniques pour un même effet.
- **Chorégraphier une ouverture de page** : la cascade en sept temps du hero est directement transposable.
- **Deux palettes de charts** au lieu d'une palette inversée.
- **Un tableau de données dense qui reste lisible** : fond de ligne teinté très désaturé, badges pilule, ligne détachée au survol.
- **Une réponse d'IA rendue en tableau + graphique** plutôt qu'en paragraphe.

## Limites de la récolte

- **L'app est entièrement derrière login** : tous les écrans viennent des images que le site sert publiquement, jamais d'une session réelle.
- **Un seul snapshot Wayback** (10 avril 2026) : impossible de remonter plus haut, donc pas de millésime « v1 ».
- **Captures pleine hauteur impossibles en headless** : les sections s'animent au scroll (IntersectionObserver), donc tout ce qui est sous le hero ressort noir. Seul le hero est exploitable en capture directe — les sections basses restent à faire en pilotant Chrome avec un scroll progressif.
- **Aucune base d'UI ne référence le produit** : Refero (0 résultat), Land-book (403), SiteInspire (429), Product Hunt (403), Godly, Webframe, SaaS Landing Page — rien.
- **Aucune source de process** : pas de compte X identifié, pas de Dribbble, pas de changelog. L'aspect `process/` **est vide** ; le seul avant/après disponible est la comparaison avril 2026 (Wayback) vs août 2026, fournie dans `archive/`.
- **Instagram `@tradetrack.space` illisible** sans session (`NotFoundError` de gallery-dl).
- **Attribution du design non vérifiable** : le nom d'Oleksandr Drohomyretskyi apparaît dans les mentions légales (édition et exploitation), pas explicitement comme auteur du design. Un second nom, **Tetiana Liush**, a soumis le produit sur RankInPublic — rôle inconnu.
- **Aucune vidéo, aucune presse** : ni YouTube, ni Reddit, ni Product Hunt, ni Indie Hackers.

## Sources

- **Site officiel** — <https://www.tradetrack.space/en> : le dashboard réel (`/assets/dashboard.png`), les cinq mockups (`/assets/how-it-works/*.png` en 2560 px), le composant de lignes de trades, les logos, la carte OG, les posters.
- **CSS de production** — `/_next/static/chunks/60a795846fc5c5a8.css` (365 ko) : tous les tokens des deux thèmes, les `@font-face` réels, les 39 `@keyframes` avec durées et courbes. Conservé dans `couleurs/`.
- **Wayback Machine** — snapshots du 2026-04-10 (landing et pricing), seuls états antérieurs existants.
- **Mentions légales** — Privacy Policy et Terms of Use : la seule source nominative sur l'éditeur.
- **Sitemap** — trois locales (en, uk, ru), sept landings SEO par intégration, ~20 articles.
- **RankInPublic** — <https://rankinpublic.xyz/products/www.tradetrack.space> : 1 tournoi, 6 wins, 1re place (juin 2026).
- Captures de pages et GIF d'animation : faits maison le 2026-08-31 (`capture-site.py`, `shoot.py`, `record.py`).

## Crédits

- **Oleksandr Drohomyretskyi** (Олександр Дрогомирецький) — éditeur nommé dans les mentions légales, Kopalniana 14C, Varsovie (Pologne). Personne physique, pas de société. Son compte apparaît comme utilisateur de démo dans la capture officielle de l'AI Chat. **Aucun profil de designer public** trouvé (ni Dribbble, ni Behance, ni Read.cv, ni X, ni LinkedIn identifiable) : l'attribution du design reste une déduction, pas un fait établi.
- **Tetiana Liush** — compte ayant soumis le produit sur RankInPublic ; rôle non confirmé.
- Typographies : **Inter Tight** (Rasmus Andersson, variante Tight) et **Geist Mono** (Vercel).
- Pile : **Next.js** App Router sur **Vercel**, **Tailwind v4** + **shadcn/ui** + **Radix UI**.
- Contact public : `team@tradetrack.space` · <https://www.instagram.com/tradetrack.space>
- Le poster de la page de connexion est une photo de stock, sans crédit photographe disponible.

## Mots-clés

journal de trading, trading journal, prop firm, forex, crypto, TradeLocker, cTrader, Match Trader, MetaTrader 5, Expert Advisor, Bybit, beta gratuite, dashboard sombre, dark UI, trois noirs, rail de navigation, bouton primaire neutre, bordure en alpha, blanc en transparence, design tokens, Tailwind v4, shadcn/ui, Radix, Next.js, Vercel, View Transitions, keyframes nommés, cascade d'entrée, chorégraphie de motion, cubic-bezier, skeleton shimmer, Inter Tight, Geist Mono, police variable, size-adjust, fallback métrique, deux palettes de charts, chart-1 chart-5, emerald red Tailwind, violet IA, AI Insights, Trading Health Check, AI Chat, tableau et graphique, heatmap de progression, calendrier P&L, discipline tracker, demons, R-multiple, expectancy, drawdown, tableau dense, badges BUY SELL, fusée dans le T, Varsovie, solo founder, i18n trois langues

## À voir aussi

- [[traders-second-brain]] — l'autre journal noir du lot, en CSS maison plutôt qu'en Tailwind.
- [[ultratrader]] — la cohérence multi-plateformes, avec une vraie app native.
- [[stonk-journal]] — l'inverse exact : la typographie plutôt que le système.
- [[_APPS]] · [[_COMPOSANTS]] · [[_ANIMATIONS]]
