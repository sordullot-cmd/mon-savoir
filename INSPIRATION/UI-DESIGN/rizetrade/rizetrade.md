---
type: inspiration
discipline: ui-design
media: app
source: https://rizetrade.com
url_store:
editeur: Trading Journal LLC (Sanford, Caroline du Nord)
type_app: finance
plateformes: [web]
version: web, aucune app native (relevé le 31 août 2026)
secteur: finance
couleur_principale: "blanc #FFFFFF"
couleurs: ["#FFFFFF", "#F2F2F2", "#0A0A0A", "#171717", "#DC2626", "#22C55E", "#3B82F6", "#059669", "#121416"]
patterns: [onboarding, paywall, recherche, parametres, empty-state, mode-sombre, gamification]
anime: léger
animations: [scroll-reveal, hover, loader]
layout: centré
mood: [minimal]
type_site: saas
typos: [Inter, Plus Jakarta Sans, Geist Mono]
date_capture: 2026-08-31
tags: [inspiration, ui, finance, trading, minimal, saas]
---

# RizeTrade

> Le concurrent frontal de [[tradezella]], construit sur la thèse inverse : pas de marque,
> pas de couleur, pas de mascotte. Un socle shadcn/ui assumé tel quel, du blanc à 86 %,
> et une seule promesse — « the edge is not the strategy, it is whether you followed it ».

**Sources :** site officiel (Next.js sur Vercel, tokens lus dans le CSS de production) · le tunnel d'onboarding **public**, déroulé écran par écran · deux annuaires SaaS · Wayback Machine + Common Crawl. Détail dans [`## Sources`](#sources).

> **Lecture** : chaque famille est montrée par **une planche** (`<aspect>/planches/`),
> légendée juste dessous. Les fichiers individuels restent dans leur dossier d'aspect.

## En bref

- **Produit de moins d'un an.** Domaine déposé le 25 février 2025, encore parqué chez Namecheap en juillet 2025, premier vrai site fin octobre 2025, `foundingDate` déclarée au 10 décembre 2025. Ce dossier attrape une DA en train de se faire.
- **Charte complète et lisible dans le code.** 55 custom properties par thème, socle **shadcn/ui** canonique en triplets HSL, plus une couche de tokens métier maison (`--profit`, `--loss`, `--score-*`, `--chart-*`). Aucun press kit, mais le CSS dit tout.
- **Aucune couleur de marque.** Le `--primary` est un quasi-noir en clair, un quasi-blanc en sombre, et le logo est rempli avec cette même variable — il change donc de couleur avec le thème. La seule couleur du produit est **fonctionnelle** : le vert du gain, le rouge de la perte, le bleu de la progression.
- **Un tunnel d'onboarding entièrement public**, sans compte : dix étapes qui posent des questions, montrent deux preuves produit, offrent une réduction à compte à rebours, et se terminent sur un paywall. C'est la pièce la plus complète du dossier.
- **Le produit lui-même reste fermé** : `/dashboard` redirige vers NextAuth, aucune vidéo de démo n'existe, aucune base d'UI ne l'indexe. **Trois vues réelles seulement** ont pu être récupérées.
- **Machine à SEO autant que produit** : 111 URLs au sitemap, dont ~40 pages « *broker* trading journal », 9 pages « *concurrent* alternative » (dont une visant TradeZella) et une cinquantaine d'articles. C'est le seul canal d'acquisition visible.
- **Le site a basculé clair → sombre → clair en dix mois**, et le thème sombre déclaré dans le CSS actuel n'est plus servi par la landing.

## Écrans

Trois vues réelles, pas une de plus — et elles ne viennent pas de l'éditeur.

![[ecrans/planches/planche-ecrans-produit.png]]

**Le dashboard est un shadcn/ui non déguisé, et c'est exactement ce qui le rend intéressant à regarder.** Sidebar à neuf entrées (Add Trades, Dashboard, Calendar, Trades, Trading Journal, Notebook, Strategies, Discipline, Reports), en-tête personnalisé « Evening, Will », quatre cartes KPI, un graphique d'aire bicolore vert au-dessus de zéro / rose en dessous, et un radar « Trading Score » à cinq axes. Rayon `.5rem` partout, ombres quasi nulles, bordures `#D6D6D6` : rien n'a été customisé au-delà des tokens. Un produit qui assume son socle plutôt que de le maquiller.

Détail : `ecrans/dashboard-clair-reel.png` (2872×1334, récupéré en résolution native en retirant le `?w=1000` du CDN Sanity de SaaSFame) · `ecrans/discipline-heatmap-playbook.png` (les deux composants signature côte à côte : la carte de playbook avec ses règles cochées « 4/5 rules followed », et la heatmap de régularité avec son badge « 2-day streak ») · `ecrans/trade-replay-chart-onboarding.png` (un chandelier avec entrées, sorties, stop et target tracés).

## Flows

C'est ici que le dossier est le plus riche : **tout le tunnel d'inscription est servi sans compte** sur `/onboarding/*`, ce que l'éditeur n'a probablement pas prévu.

![[flows/planches/planche-tunnel-onboarding.png]]

**Le tunnel qualifie par la douleur, puis vend par l'urgence.** Étape 1 : « What's your biggest challenge in trading? », sept cartes empilées (Following My Rules, Controlling Emotions, Cutting Losses, Overtrading, Not Letting Winners Run, Finding a Profitable Strategy, Excel is Too Manual). Étape 2 : à quoi doit servir le journal. Puis deux écrans de **preuve produit** insérés au milieu des questions — un trade rejoué sur le graphique, un playbook avec sa heatmap — avant le sélecteur de broker (« Search 800+ brokers, prop firms and platforms »).

La fin bascule dans un autre registre : un écran d'attente scénarisé (anneau de progression, checklist qui se coche : *Analyzing your answers*, *Building your dashboard*, *Configuring your analytics*, *Adding finishing touches*), un interstitiel cadeau (« Psst… We've got a little surprise for you! »), une carte **20 % OFF** sur fond de confettis avec un compte à rebours de dix minutes, un récapitulatif de promesses cochées, et enfin le paywall — Pro à 39 $ barré 49 $ contre Essential à 19 $ barré 24 $, badge *RECOMMENDED*, bandeau « your welcome gift is active · 14:06 » et bouton désactivé tant que l'e-mail est vide.

**Trois prix différents selon le point de contact** : le JSON-LD du site annonce 24 $ / 49 $, la page comparatif 19 $ / 33 $ en annuel, le paywall 19 $ / 39 $ après remise. Le produit ne s'est pas encore fixé.

![[flows/planches/planche-tunnel-mobile.png]]

**Le mobile n'est pas une adaptation, c'est le même écran qui respire moins** — et c'est là qu'on lit l'état sélectionné : fond bleu très clair, bordure bleue, texte qui passe en gras. Le paywall mobile empile les deux cartes de prix au lieu de les juxtaposer et garde le CTA désactivé en gris.

Aussi : `flows/auth-signin-desktop.webp` et `flows/auth-signin-mobile.webp` — l'écran de connexion, avec témoignage à droite sur un fond de grille fine.

## Branding

![[branding/planches/planche-marque.png]]

**Le mark est une flèche montante découpée en négatif dans un carré, et il n'a pas de couleur propre.** Son dégradé va de `hsl(var(--primary))` à ce même `--primary` à 57 % d'opacité — autrement dit, il est noir sur fond clair, blanc sur fond sombre, et il suivrait n'importe quelle couleur qu'on donnerait au token. Le wordmark oppose « Rize » en gras à « Trade » en gris, en Plus Jakarta Sans. La carte sociale résume la charte entière : monochrome, cinq bénéfices à pastilles noires cochées, URL en monospace, ligne de graphique ascendante en filigrane.

![[branding/planches/planche-marque-sur-sombre.png]]

Fichiers : `branding/mark-fleche-clair.svg` et `branding/mark-fleche-sombre.svg` (extraits du DOM, `viewBox 0 0 400 400`, variables résolues) · `branding/mark-fleche-512.png` (512×512, via Startup Fame) · `branding/favicon.ico` (32×32 — **la seule icône réellement servie** : `/apple-touch-icon.png`, `/logo.svg` et `/site.webmanifest` sont déclarés dans le `<head>` mais renvoient tous 404).

**Typographie — trois familles, toutes auto-hébergées via `next/font`, aucun appel à Google Fonts.** Les fichiers woff2 sont dans `branding/fonts/` :

| Police | Rôle déclaré | Relevé au rendu |
| --- | --- | --- |
| **Inter** variable 100-900 | `--font-inter` — corps et UI | 7 706 éléments sur les pages capturées |
| **Plus Jakarta Sans** 500-800 | `--font-logo` — le wordmark et les gros titres | 298 éléments |
| **Geist Mono** variable 100-900 | `--font-geist-mono` — chiffres, P&L, URL | 3 éléments seulement sur la vitrine ; c'est dans l'app qu'elle sert |

Repli métrique déclaré proprement : « Inter Fallback » sur Arial local, `ascent-override: 90.44%`, `descent-override: 22.52%`, `size-adjust: 107.12%`. Plus Jakarta Sans apparaît en février 2026 — c'est elle qui date le changement d'identité.

## Couleurs

![[couleurs/palette-declaree-socle-shadcn.svg]]

**Une charte qui ne contient aucune couleur de marque : la seule teinte du thème clair est le rouge d'erreur.** Tout le reste est du gris, décliné en dix crans du `#F2F2F2` de page au `#0A0A0A` d'encre. Le fond n'est d'ailleurs pas blanc — `--background` vaut 95 % de luminosité, et ce sont les cartes qui sont blanches. Le thème sombre est le seul endroit où la neutralité se teinte : les gris y virent au bleu (`210 10% 8%`, `215 8% 14%`) et **la carte devient plus sombre que la page** — l'inverse exact de la logique du thème clair.

**Thème clair (`:root`)**

| Token | Hex | HSL déclaré | Usage |
| --- | --- | --- | --- |
| `--background` | `#F2F2F2` | `0 0% 95%` | fond de page — pas du blanc |
| `--card` / `--popover` | `#FFFFFF` | `0 0% 100%` | les surfaces |
| `--foreground` | `#0A0A0A` | `0 0% 3.9%` | encre |
| `--primary` | `#171717` | `0 0% 9%` | bouton principal, logo |
| `--muted` | `#E6E6E6` | `0 0% 90%` | |
| `--muted-foreground` | `#666666` | `0 0% 40%` | texte secondaire |
| `--border` / `--input` | `#D6D6D6` | `0 0% 84%` | |
| `--destructive` | `#E75A61` | `357 75% 63%` | la seule teinte du thème |
| `--radius` | `.5rem` | — | partout, sans exception |

**Thème sombre (`.dark`)**

| Token | Hex | HSL déclaré | Usage |
| --- | --- | --- | --- |
| `--background` | `#121416` | `210 10% 8%` | |
| `--card` | `#0E0F11` | `220 10% 6%` | plus sombre que la page |
| `--foreground` / `--primary` | `#FAFAFA` | `0 0% 98%` | |
| `--secondary` / `--muted` / `--accent` | `#212327` | `215 8% 14%` | une seule valeur pour trois rôles |
| `--muted-foreground` | `#A3A3A3` | `0 0% 64%` | |
| `--border` | `#232629` | `215 8% 15%` | |
| `--destructive` | `#DC2828` | `0 72% 51%` | |

![[couleurs/palette-declaree-metier-pnl-et-graphes.svg]]

**Le vert et le rouge changent de teinte selon le thème, et c'est un choix, pas une négligence.** En clair, le gain est un vert sapin `#047857` et la perte un rouge brique `#B91C1C` — lisibles sur blanc. En sombre, le gain vire au turquoise `#1EBA8B` et la perte au rose `#E5606E`, puis au framboise `#C4234F` sur les graphes. Le score de discipline a ses trois crans propres, eux aussi doublés. Les cinq séries de graphes, en revanche, sont **identiques dans les deux thèmes** : bleu, vert, cyan, orange, violet.

**P&L**

| Token | Clair | Sombre |
| --- | --- | --- |
| `--profit` | `#047857` | `#1EBA8B` |
| `--profit-chart` | `#059669` | `#1EBA8B` |
| `--loss` | `#B91C1C` | `#E5606E` |
| `--loss-chart` | `#DC2626` | `#C4234F` |

**Score et séries**

| Token | Clair | Sombre |
| --- | --- | --- |
| `--score-good` | `#16A34A` | `#22C55E` |
| `--score-warn` | `#D97706` | `#FBBF24` |
| `--score-bad` | `#DC2626` | `#F87171` |
| `--chart-1` … `--chart-5` | `#0090FF` `#2CCE67` `#38BDFF` `#FFA947` `#7B61FF` | identiques |

![[couleurs/palette-relevee-dans-les-ecrans.svg]]

**Le relevé de pixels confirme la charte au token près — c'est rare.** Le `#F2F2F2` mesuré à 5,6 % est exactement le `--background` déclaré ; le `#0A0A0A` à 1,4 % est exactement le `--foreground`. 91 % de la surface tient en deux blancs. Une seule couleur échappe aux tokens : le **rouge `#DC2626` du bouton « Get Started »** dans le header, relevé au pixel — il vient d'une classe Tailwind, pas d'une variable. C'est le seul aplat saturé de tout le site, et il est le seul élément qui accroche l'œil sur la landing.

## Composants

![[composants/planches/planche-composants.png]]

**Chaque composant est un tableau déguisé, et c'est cohérent avec la thèse du produit.** Le calendrier de P&L est une grille de sept colonnes avec une colonne « Total » par semaine — pas de couleur de fond, juste le montant en vert ou en rouge et le nombre de trades en gris. La carte de P&L cumulé mélange trois tailles de chiffre dans une même valeur (`$33,989` en gros, `.51` en petit, le delta en vert à côté). Le radar « Trading Score » est un pentagone gris sans remplissage coloré. Le playbook coche ses règles en vert et barre celle qui n'a pas été suivie en rouge. Les cartes de plan du paywall mettent tout le poids sur le prix barré.

Le seul composant qui rompt la sobriété : le **header**, où le CTA rouge fait tache — délibérément.

Fichiers indexés dans [[_COMPOSANTS]] : `calendrier-pnl-mensuel_rizetrade.png` · `carte-pnl-cumule_rizetrade.png` · `radar-trading-score_rizetrade.png` · `playbook-et-heatmap-consistency_rizetrade.png` · `cartes-de-plan-paywall_rizetrade.png` · `carte-de-choix-etat-selectionne_rizetrade.png` · `rangee-kpi-donuts-et-barres_rizetrade.png` · `header-nav-cta-rouge_rizetrade.png`.

## Animations

![[animations/scroll-calendrier-et-sections_rizetrade.gif]]

**Le site anime peu et le fait bien : des révélations au scroll, rien d'autre.** Les durées sont normalisées dans le CSS à `.15s` (le défaut, couleurs et bordures), puis `.2s`, `.3s`, `.5s`, `.7s`, `1s`. Trois keyframes maison méritent le détour : `border-beam` (un faisceau qui parcourt une bordure via `offset-distance`, importé de magicui), `t-shimmer` (skeleton de chargement, 2 s linear) et `mentor-highlight-pulse` (1,3 s ease-out, joué deux fois — il existe donc un mode « mentor » avec onboarding contextuel, invisible côté public).

`animations/hero-au-chargement_rizetrade.gif` — l'arrivée du hero.

**Trouvaille : le produit a une mascotte, et personne ne l'a jamais vue.** La CSS de production contient six keyframes de mascotte : `mascot-blink` (clignement par `scaleY(.1)` à 95 % d'un cycle de 5,5 s), `mascot-hop` (un saut squash-and-stretch en huit étapes, `scale 1.16/.86` à l'atterrissage, 0,52 s) enchaîné sur `mascot-breathe` (respiration en boucle de 2,6 s), et trois `mascot-liquid-a/b/c` (blobs déphasés sur 3,1 / 4,3 / 5,5 s — une forme liquide type metaball). Le markup n'est ni dans la landing, ni dans l'onboarding public, ni dans les 36 chunks JS servis : **elle vit derrière le login**. Une DA sans couleur qui cache un personnage animé, c'est la contradiction la plus intéressante du dossier.

## Marketing

![[marketing/planches/planche-pages-du-site.png]]

**La landing est bâtie sur une colonne centrale bordée — la signature Vercel/shadcn — et chaque section pose un problème avant de montrer la solution.** « Can't Stop Overtrading? », « Emotions Sabotaging Your Trades? », « 90% of Traders Lose Money. Become Part of the 10% Club. » Le ton est accusateur et direct, sans détour marketing. Les maquettes ne sont **pas des images** : ce sont des composants React rendus en direct dans le DOM (calendrier d'avril 2026, checklist « VWAP Breakout 4/6 », rapport « Emotion Tags », carte « Performance Score 78 % ») — il n'existe donc aucune version pleine qualité à récupérer, ce que le site a d'ailleurs de commun avec sa propre sobriété.

La preuve sociale est minimale et assumée comme telle : trois témoignages prénom + rôle, sans photo, sans nom complet (Roger — Breakout Trader, Dave — Prop Firm Tryout, Michael — Large Cap Trader).

Les pages capturées : home, pricing (grille + tableau comparatif d'une cinquantaine de lignes en six familles + sept objections rédigées), supported-brokers, learn-to-trade, trading-journal-template, contact, et un exemple de `brokers-template` qui montre à quoi ressemblent les ~40 pages SEO. Versions mobiles pour chacune.

## Archive

![[archive/planches/planche-millesimes-2025-2026.png]]

**Dix mois, trois DA, et le pendule clair → sombre → clair.**

| Date | Ce qui change |
| --- | --- |
| **25 fév. 2025** | domaine déposé chez Namecheap |
| **juil. 2025** | encore une page de parking Sedo — `archive/landing-2025-07.png` |
| **oct. 2025** | **premier vrai site, en THÈME CLAIR.** Wordmark « Rize Trade » en **deux mots**, monogramme « RT » dans un carré noir, badge « Now in Beta », titre « The smart trading platform that helps you become a more profitable trader. » Six cartes de features, stats gonflées (10 000+ traders, 2,5 M$ analysés, 4,9/5), aucun visuel produit. Footer « © 2024 Rize Trade LLC » |
| **jan. 2026** | 99 pages d'un coup, et le site est déjà passé au **SOMBRE `#0a0a0a`**. Hero = mockup de dashboard dans une fenêtre macOS stylisée. Titre « The Trading Journal to Improve Your Profitability » |
| **fév. 2026** | **le pivot.** Le titre devient « A Trading Journal that builds discipline » — le discours passe de la performance à la discipline, et c'est encore la baseline aujourd'hui. Nav réduite de 5 à 3 entrées, Google OAuth, arrivée de Plus Jakarta Sans, le mockup macOS cède au calendrier de P&L |
| **mars-mai 2026** | bascule SEO agressive (+101 puis +275 pages), migration webpack → Turbopack, arrivée des logos de brokers en SVG |
| **juin 2026** | encore sombre, CTA « Try For Free », le blog SEO remonte en home |
| **août 2026** | **retour au CLAIR.** Le `.dark` reste déclaré dans le CSS mais la landing ne le sert plus, et elle n'écoute pas `prefers-color-scheme` : la capture en mode sombre est identique à la claire |

`archive/carrd-one-pager-sombre.webp` — une propriété satellite, `rizetrade.carrd.co`, jamais archivée par la Wayback : un one-pager de backlink en thème sombre, colonne droite restée vide, typographie différente (Sora + Inter) et dégradés or/violet/bleu qu'on ne trouve nulle part ailleurs. Une page abandonnée en cours de route.

## Ce que je retiens

- **Un produit peut se passer entièrement de couleur de marque.** Ici le `--primary` est un gris, le logo hérite de ce gris, et l'identité tient au dessin du mark et à la typographie. Sur un outil où l'utilisateur regarde des chiffres verts et rouges toute la journée, c'est probablement la bonne décision — et l'inverse exact du choix de [[tradezella]].
- **Un logo rempli avec une variable de thème** plutôt qu'avec une couleur fixe : évident une fois vu, et ça règle le problème du logo sur fond sombre sans fichier supplémentaire.
- **Le tunnel d'onboarding public** est une masterclass de qualification : questions douloureuses → preuves produit insérées au milieu → attente scénarisée → cadeau à compte à rebours → paywall. Chaque étape justifie la suivante. À étudier de près pour n'importe quel funnel d'abonnement.
- **Assumer son socle** (shadcn/ui à peine customisé, rayon `.5rem` partout) donne un produit cohérent en très peu de temps. Le prix à payer se voit : rien n'est mémorable. C'est un arbitrage, pas un accident.
- **Un token de couleur qui change de teinte selon le thème** (`--profit` vert sapin en clair, turquoise en sombre) plutôt que d'éclaircir la même teinte : plus de travail, bien meilleur résultat en lisibilité.
- **Le contre-exemple utile** : un CTA rouge Tailwind posé hors système sur une charte tokenisée au pixel près. Ça fonctionne parce que c'est le seul, mais ça révèle qu'aucune variable n'a été prévue pour l'accent d'action.

## À réutiliser pour

Tout produit à construire vite et proprement sur shadcn/ui — c'est un cas d'école de ce que donne le socle quand on n'y touche presque pas, avec ses forces (cohérence immédiate, tokens propres) et sa limite (rien ne distingue le produit d'un autre). Le tunnel d'onboarding vaut pour n'importe quel funnel d'abonnement. La discipline chromatique — toute la couleur réservée à la donnée — vaut pour tout dashboard.

## Sources

- **Site officiel** — [rizetrade.com](https://rizetrade.com) : pages capturées en pleine hauteur, desktop et mobile, le 31 août 2026 (`capture-site.py`). Les 55 tokens par thème viennent de `/_next/static/chunks/324edf7ce01f2ccc.css`, les `@font-face` et les trois woff2 de `/_next/static/chunks/37a6d569aa9f1aac.css` et `/_next/static/media/`. 19 pages au-delà de la limite fixée n'ont pas été capturées (pages SEO). Trois pages SEO capturées puis écartées pour le poids (`trading-indicators`, `trading-patterns`, `trading-strategies`).
- **Tunnel d'onboarding public** — `rizetrade.com/onboarding/*` : dix étapes déroulées en pilotant Chrome par CDP, desktop et mobile. Ces routes sont servies sans compte ; le paywall en marque la fin.
- **SaaSFame** — [saasfame.com/item/rizetrade](https://saasfame.com/item/rizetrade) : la **seule** source d'un écran de dashboard réel, en 2872×1334 (obtenu en retirant le `?w=1000` du CDN Sanity).
- **Startup Fame** — [startupfa.me/s/rizetrade](https://startupfa.me/s/rizetrade) : le logomark en 512×512, assets déposés le 11 juillet 2026.
- **Wayback Machine** — millésimes de juillet et octobre 2025 (`web.archive.org/web/20250714134325if_/` et `/20251027100850if_/`). Le service a été en panne globale pendant l'essentiel de la récolte.
- **Common Crawl** — millésimes de janvier, février, mars, avril, mai et juin 2026 récupérés en HTML brut (`index.commoncrawl.org`, collections CC-MAIN-2026-04 à -25) : la copy, la structure, les couleurs inline et les polices, mais **pas l'image rendue** — les feuilles de style de ces builds ne sont plus servies par Vercel (404) et la Wayback n'a jamais rendu ces snapshots malgré une vingtaine de tentatives.
- **Mentions légales** — `/terms` et `/privacy` : Trading Journal LLC, 500 Westover Dr #32164, Sanford NC 27330, mises à jour le 18 novembre 2025 ; prestataires déclarés Stripe, Polygon.io, Resend, PostHog, Ferndesk, UploadThing.
- **Sources vides, vérifiées** — App Store et Google Play (aucune app ; API iTunes et recherche Play, cinq packages testés en direct) · Refero (les 427 sites et 303 apps de l'index énumérés un par un) · Screensdesign, Appshots, SaaS Landing Page, Webframe, Mobbin · **ProductHunt** (« No products found ») · Awwwards, SiteInspire, Minimal Gallery, One Page Love, Godly, Httpster, CSSDA, FWA, Dark Mode Design : **aucune galerie de design ne référence ce site**. Land-book et StartupRanking sont restés inaccessibles (Cloudflare) — non tranchés.
- **Vidéo : aucune.** Le seul résultat YouTube (`DhYQj8dTFgY`, chaîne à 2 abonnés) est un clip SEO générique de 50 s, sans un seul écran produit et avec un logo appartenant à une autre marque. Vérifié image par image, puis supprimé.

## Crédits

- **Trading Journal LLC** — l'éditeur, nommé cinq fois dans les CGU et dans le pied de page. Siège de domiciliation à Sanford, Caroline du Nord. Support : `support@rizetrade.com`.
- **Aucun fondateur, aucun designer, aucune équipe n'est publié nulle part.** Pas de page `/about`, pas de page équipe, aucune adresse, aucun lien social dans le pied de page. Le compte [X @rizetrade](https://x.com/rizetrade) existe depuis avril 2026 avec **zéro post et zéro abonné** ; la chaîne YouTube existe et est vide.
- **Deux noms apparaissent, tous deux en rédaction** — **Timothy Cahill**, `dc:creator` des 54 articles du flux RSS et utilisateur CMS `timothycahill` ; **Will Nash**, `<meta name="author">` des pages éditoriales. Aucun profil public rattachable à l'un ou l'autre : à traiter comme des signatures SEO, pas comme des crédits produit.
- **Piste non recoupée** : EarlyHunt affiche « Created by Melissa Durrah » et Sidehunt « Built by durrahmelissa92 » pour les soumissions du 24 juin 2026. Sur ces plateformes, le nom affiché est celui du compte qui soumet — cela peut être une agence de lancement. **À ne pas écrire comme un fait.**
- **Les trois polices sont des libres** : [Inter](https://rsms.me/inter/) (Rasmus Andersson), [Plus Jakarta Sans](https://github.com/tokotype/PlusJakartaSans) (Tokotype — Gumpita Rahayu), [Geist Mono](https://vercel.com/font) (Vercel). Le socle d'interface est [shadcn/ui](https://ui.shadcn.com), le composant `border-beam` vient de [magicui](https://magicui.design).

## Mots-clés

journal de trading, trading journal, carnet de trades, discipline, playbook compliance, règles suivies, rule adherence, consistency tracker, heat map de régularité, streak, P&L, calendrier de P&L, courbe cumulée, radar de score, trading score, emotion tags, revenge trade, FOMO, overtrading, broker sync, import CSV, prop firm, shadcn, shadcn/ui, Tailwind, tokens HSL, design tokens, custom properties, radius 0.5rem, monochrome, sans couleur de marque, achromatique, minimal, blanc, neutral grey, next.js, App Router, Vercel, Turbopack, next/font, Inter, Plus Jakarta Sans, Geist Mono, magicui, border beam, skeleton shimmer, mascotte cachée, keyframes de mascotte, squash and stretch, metaball, onboarding public, funnel d'abonnement, tunnel de qualification, paywall, compte à rebours, urgence, remise 20 %, essai gratuit, SEO longue traîne, pages alternative, concurrent de TradeZella, RizeTrade, Rize Trade, Trading Journal LLC

---

Dossier créé par `/inspi` le 31 août 2026 · [[_APPS|← Apps & produits]] · [[_INSPIRATION|← Inspiration]]
