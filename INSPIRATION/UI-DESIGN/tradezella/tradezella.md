---
type: inspiration
discipline: ui-design
media: app
source: https://www.tradezella.com
url_store:
editeur: TradeZella LLC (New York)
type_app: finance
plateformes: [web]
version: web, aucune app native (relevé le 31 août 2026)
secteur: finance
couleur_principale: "bleu nuit #0A0D25"
couleurs: ["#06091C", "#0A0D25", "#141730", "#644DFF", "#4C23FF", "#FF00BB", "#FF9634", "#F4F6F8", "#FFFFFF"]
patterns: [onboarding, tab-bar, recherche, parametres, empty-state, mode-sombre, gamification]
anime: oui
animations: [scroll-reveal, hover, transitions-page, marquee]
layout: bento
mood: [dark, bold]
type_site: saas
typos: [Inter, Inter Tight, Unbounded, Inconsolata, JetBrains Mono]
date_capture: 2026-08-31
tags: [inspiration, ui, finance, trading, dark, saas]
---

# TradeZella

> Le journal de trading qui s'est refondu six fois en cinq ans, et qui a fini par
> personnifier son produit : « Zella » n'est plus une marque, c'est un partenaire IA
> avec un avatar de taureau, des agents configurables et un score de discipline.

**Sources :** site officiel (Webflow) · centre d'aide Intercom (la seule source publique de vraies captures) · Wayback Machine + Common Crawl (neuf millésimes) · walkthroughs YouTube officiels et tiers · LinkedIn / Fast Company / offres d'emploi. Détail dans [`## Sources`](#sources).

> **Lecture** : chaque famille est montrée par **une planche** (`<aspect>/planches/`),
> légendée juste dessous. Les fichiers individuels restent dans leur dossier d'aspect —
> c'est de là qu'on récupère un écran précis.

## En bref

- **SaaS web pur.** Aucune app iOS ni Android sous ce nom, vérifié sur les deux stores et dans les 898 URLs du sitemap. Une app mobile est au **backlog** du board public depuis 2024. Attention : « TradeZella » est *keyword-squatté* sur l'App Store par un concurrent (Plancana) — ses captures ne sont pas celles du produit.
- **Deux thèmes complets**, clair et sombre, et ils ne partagent pas la même logique : le clair est un gris-bleu `#F4F6F8` qui porte des cartes blanches, le sombre est fait de **gris neutres** (`#171717`, `#181818`) — pas du bleu nuit de la marque.
- **La donnée est la seule couleur.** Sur 8 écrans clairs relevés, 85 % de la surface tient en deux valeurs (blanc + gris-bleu) ; le vert de gain et le rouge de perte pèsent 0,28 % à eux deux, et c'est tout ce qu'on regarde.
- **Un score noté comme un examen.** Le « Zella Score » est un radar hexagonal (Win %, Profit factor, Avg win/loss, Recovery factor, Max drawdown, Consistency) posé sur une barre-gradient rouge→vert graduée de 0 à 100. Introduit en 2023 sous forme triangulaire à 3 axes, il en a six en 2026.
- **La gamification n'est pas décorative** : Progress Tracker à heatmap annuelle façon GitHub, séries en cours, checklist quotidienne de règles, taux de suivi par règle en pourcentage coloré.
- **Six produits sous un même toit** — Journaling + Analytics, Backtesting, Zella AI, Prop Firm Sync, Trade Replay, Zella University, Spaces (communauté) — chacun avec sa page marketing et sa navigation propre dans l'app.
- **Aucun press kit, aucun logo vectoriel, aucun design system.** Le wordmark est un PNG de 484×96 ; l'entreprise a ouvert en 2026 un poste de *premier* Design Engineer pour « construire un design system de zéro ».

## Écrans

L'app vit derrière un login. Tout ce qui suit vient du **centre d'aide Intercom** (captures retina publiées par le support, jusqu'à 9150×5794) et de **frames extraites de walkthroughs vidéo** — jamais de mockups marketing.

![[ecrans/planches/planche-ecrans-theme-clair.png]]

**Le thème clair est un système de cartes blanches sur un gris-bleu, et rien d'autre ne porte la hiérarchie.** Pas d'ombre marquée, pas de bordure colorée : c'est l'écart de valeur entre `#FFFFFF` (69,4 % de la surface) et `#F4F6F8` (16,0 %) qui découpe la page. Chaque widget est une carte, chaque carte a le même rayon, et la densité monte sans jamais changer de grammaire — le Trade Log affiche onze colonnes dans la même boîte qui affichait quatre KPI plus haut.

À retenir écran par écran : `dashboard-zella-score-radar-clair.webp` (le radar + la barre-gradient, la signature du produit) · `daily-journal-clair.webp` (accordéons par journée, chacun avec sa sparkline et ses huit métriques) · `trade-log-menu-bulk-actions-clair.webp` (le menu Bulk Actions à huit entrées, y compris *Merge trades* et *Split trade*) · `progress-tracker-regles-heatmap-clair.webp` (4K : jauge de série, checklist, heatmap annuelle bleue, tableau des règles avec taux de suivi) · `prop-firm-sync-dashboard.png` (le module financier : ROI, donut de dépenses par firme, seuils de perte en pointillés).

![[ecrans/planches/planche-ecrans-theme-sombre.png]]

**Le sombre n'est pas le clair inversé : c'est là que le virage IA de 2026 se voit.** Le panneau latéral « Zella AI » y ouvre une conversation avec des pilules d'action (*Tag my last 20 trades by setup*, *Find and flag my worst pattern*), et la page « My Agents » donne trois agents automatiques déclenchés par événement (*Start my day*, *On every imported trade*) avec un champ de prompt libre et un historique de vingt exécutions. Un journal de trading qui se pilote en langage naturel.

Détails : `dashboard-sombre-zella-score-ai.webp` · `zella-agents-sombre.png` (les agents et leur run history) · `reports-sombre-tags.webp` (deux rangées de filtres en pilules — Setup Type, Session, Execution Quality, et jusqu'à « LISTENING TO MUSIC ») · `backtesting-graphique-ordre-sombre.webp` (le backtesting devient une plateforme de trading complète : outils de dessin, panneau Place order, replay 1x) · `notebook-editeur-texte-sombre.jpg` (162 notes classées en dossiers, éditeur de texte riche complet).

![[ecrans/planches/planche-ecrans-etats-vides-et-formulaires.png]]

**Les états vides sont illustrés et proposent une sortie, jamais un message seul.** Strategies vide ouvre sur un personnage plat devant un panneau de badges et un bouton violet ; Backtesting propose un choix entre deux grandes cartes illustrées (« Backtest on your own » / « AI Automated Backtesting ») plus un encart vidéo de 5 min. Le constructeur de stratégie, lui, est un formulaire long assumé : six groupes de règles repliables (Entry Criteria, Break & Retest, Exit Criteria, Trail stop, Risk Management, Move stop loss to breakeven), chacun avec son sélecteur de condition.

## Flows

![[flows/planches/planche-onboarding-et-mentor.png]]

**L'ajout de trades est traité comme un onboarding à part entière, sur un fond dégradé blanc-lilas qui sort du reste de l'app.** Barre de progression fine, sur-titre, recherche parmi 500+ brokers avec leurs logos, puis trois cartes de méthode (Auto-sync avec badge *Recommended*, File upload, Add manually). Le « Mentor Mode » applique la même recette au choix de rôle : deux cartes, trois arguments à pastille verte, et un titre vert menthe qui n'existe nulle part ailleurs dans le produit.

## Branding

![[branding/planches/planche-logotypes.png]]

**Le taureau a survécu à cinq refontes, la typographie non.** En 2021, le logotype opposait un « TRADE » serif à fortes modulations à un « ZELLA » sans-serif ultra-light en dégradé, avec un taureau low-poly en guise de A. En 2026 il ne reste que le taureau facetté — dégradé cyan sur les cornes, magenta sur les pattes — et un wordmark en capitales serif filiformes. À côté, une **mascotte 3D** entièrement nouvelle : un petit taureau-robot bleu-gris à cornes violettes, qui sert d'avatar à Zella AI, d'illustration de backtesting et d'avatar d'espace communautaire. Les deux registres coexistent sans qu'aucun document ne les articule.

Fichiers : `branding/wordmark-taureau-lowpoly.png` (484×96, le seul lockup servi) · `branding/mark-taureau-lowpoly.png` (588×588, fond transparent) · `branding/mascotte-3d-zella-nav.png` · `branding/wordmark-2021-serif-et-degrade.png` (recadré depuis l'archive : le PNG d'origine est mort avec le projet Webflow de 2021).

**Typographie — quatre familles, toutes en Google Fonts, aucune police propriétaire.** Relevées au rendu sur les neuf pages capturées : **Inter** (5 595 éléments, le corps et l'UI), **JetBrains Mono** (662, les chiffres et labels de la page Backtesting), **Inter Tight** (286, certains titres), **Inconsolata** (36, les sur-titres en petites capitales espacées) et **Unbounded** (chargée sur toutes les pages, utilisée en accroche). Le site n'auto-héberge que les trois woff2 de Font Awesome.

## Couleurs

![[couleurs/palette-declaree-variables-webflow.svg]]

**L'éditeur ne publie aucune charte, mais il en écrit une dans son CSS — et elle se contredit.** Les 25 variables du projet Webflow sont nommées par leur teinte apparente, pas par leur rôle : la variable qui porte tous les CTA du site s'appelle `--blue` et vaut `#644DFF`, un violet franc. Le seul noir neutre du lot (`--black-3 #1D1D1D`) coexiste avec quatre noirs bleutés. Deux teintes déclarées ne sont quasiment jamais servies (`--ice-green`, `--dodger-blue`), et une seule est réservée à un produit précis : l'orange `#FF9634` de Prop Firm Sync.

**Fonds et encres**

| Nom de variable | Hex | Usage |
| --- | --- | --- |
| `--black` | `#06091C` | le noir de marque, bleuté |
| `--darker-blue` | `#0A0D25` | fond dominant du site — 13,4 % de la surface relevée sur six pages |
| `--dark-blue` | `#141730` | surface de section |
| `--black-2` | `#161828` | carte sur fond noir |
| `--black-3` | `#1D1D1D` | le seul noir neutre déclaré |

**Accents**

| Nom de variable | Hex | Usage |
| --- | --- | --- |
| `--blue` | `#644DFF` | tous les CTA — nommé « blue », c'est un violet |
| `--rich-purple` | `#4C23FF` | dégradés, boutons d'époque 2022 |
| `--pink` | `#FF00BB` | fin de dégradé sur les titres |
| `--pink-2` | `#FF00F7` | magenta encore plus saturé |
| `--bright-orange` | `#FF9634` | réservé à Prop Firm Sync |
| `--ice-green` | `#8EFFF2` | déclaré, quasi jamais servi |
| `--dodger-blue` | `#1378D1` | jeu « accessible-components » |

![[couleurs/palette-relevee-app-clair-contre-sombre.svg]]

**Le produit est beaucoup plus sobre que son site.** Le site marketing est à 13,4 % de bleu nuit et 9,6 % de blanc, saturé de dégradés violet→magenta. L'app, elle, est à 69,4 % de blanc et 16,0 % de gris-bleu en thème clair : la marque n'y entre que par la sidebar (`#303249`) et le bouton d'ajout (`#6257A1`). Et le thème sombre abandonne complètement le bleu nuit pour des **gris neutres** — `#171717` à 15,4 %, `#181818` à 10,1 %, `#000000` à 5,4 % — le violet de marque n'y survit que dans un `#282233` à 0,96 %.

**Thème clair (relevé sur 8 écrans)**

| Nom de rôle | Hex | Part | Usage relevé |
| --- | --- | --- | --- |
| Blanc de carte | `#FFFFFF` | 69,4 % | tous les widgets |
| Gris-bleu de page | `#F4F6F8` | 16,0 % | le fond sur lequel les cartes flottent |
| Lilas de survol | `#F3F2F7` | 1,1 % | lignes actives, hover de tableau |
| Bleu de lien | `#3558D3` | 0,27 % | |
| Navy de sidebar | `#303249` | 0,27 % | le rail de navigation |
| Violet de CTA | `#6257A1` | 0,21 % | bouton « + Add trade » |
| Vert de gain | `#74BEA5` | 0,18 % | désaturé — pas le vert vif du marketing |
| Rouge de perte | `#DD7E80` | 0,10 % | |

**Thème sombre (relevé sur 11 écrans)**

| Nom de rôle | Hex | Part | Usage relevé |
| --- | --- | --- | --- |
| Gris 17 | `#171717` | 15,4 % | surface de carte |
| Gris 18 | `#181818` | 10,1 % | |
| Gris 16 | `#161616` | 8,2 % | |
| Gris 0F | `#0F0F0F` | 7,1 % | fond de page |
| Blanc de texte | `#FFFFFF` | 6,1 % | |
| Noir pur | `#000000` | 5,4 % | graphiques plein cadre |
| Violet résiduel | `#282233` | 0,96 % | la seule trace du violet de marque |

## Composants

![[composants/planches/planche-composants.png]]

**Trois blocs sortent du lot, et tous les trois transforment une donnée brute en verdict.** Le radar Zella Score note six dimensions et les résume en un chiffre posé sur une barre-gradient rouge→vert — ce n'est plus un tableau de bord, c'est un bulletin. La rangée de KPI mélange trois grammaires dans une seule ligne (chiffre nu, jauge en arc, donut bicolore) et l'accepte. La topbar, elle, met « Ask Zella AI » à droite dans un bouton bordé violet, à égalité visuelle avec Filters et Date range : l'IA est une entrée de navigation, pas une fonctionnalité enfouie.

Fichiers indexés dans [[_COMPOSANTS]] : `composants/carte-zella-score-radar_tradezella.png` · `composants/rangee-kpi-jauges-arc_tradezella.png` · `composants/topbar-filtres-et-ask-zella-ai_tradezella.png`.

## Animations

![[animations/scroll-six-produits-un-hub_tradezella.gif]]

**Le site n'anime pas des objets, il anime des changements de fond.** Le défilement fait alterner sections blanches et sections noires plein écran, chaque bascule ré-éclairant les captures produit posées dessus. Les titres arrivent en dégradé bleu→magenta déjà composé, sans effet de tracé. Transitions normalisées dans le CSS à `.2s` et `.25s ease-out` pour les états, `.3s`/`.35s cubic-bezier(.25,.46,.45,.94)` pour les mouvements amples.

`animations/hero-au-chargement_tradezella.gif` — l'entrée du hero. Rien de spectaculaire : le contenu est là d'emblée, seul le mockup de dashboard se pose. Un site qui ne fait pas attendre.

## Marketing

![[marketing/planches/planche-pages-du-site.png]]

**Neuf pages, un seul rythme : une page par produit, chacune bâtie sur la même alternance clair/sombre.** Le site est un Webflow tenu depuis 2022 (le même projet, `630df394ff44d46a174df570`) et il se lit comme un catalogue : nav à sept entrées produit, page dédiée pour chacune, et une page `/solutions` qui redécoupe la même offre par profil de trader (Unprofitable, Developing, Profitable, Prop Firm, Communities). Preuve sociale partout : *20.2B trades journaled*, *100K+ traders*, *500+ brokers*, *4.8 Trustpilot*.

![[marketing/planches/planche-cartes-produit.png]]

**Les six cartes produit de la home 2026 sont la meilleure pièce de DA du site.** Chacune est un collage : un fragment d'interface réel (tableau de trades, courbe d'équity, chandeliers) posé sur fond noir, augmenté de **toasts flottants** qui racontent ce que le produit vient de faire tout seul — « AUTO-SYNC SUCCESSFUL — 32 trades pulled from Topstep », « AUTO-TAGGED — Strategies auto-tagged on 32 trades », « You're on tilt. Losses up 2.37x ». Le produit ne se montre pas : il se met en scène en train d'agir.

Aussi : `marketing/hero-dashboard-app-clair.webp` (1992×1647, le dashboard entier en visuel de hero) et les versions mobiles de chaque page (`*-mobile.jpg`).

**Campagne en cours, hors registre.** Une page teaser vit à `/wtfistradezelladoing` : esthétique terminal et dossier classifié (« A New Era is Coming to TradeZella », script `operator_admit.sh`, CLEARANCE REQUIRED, attribution d'un Agent ID `ZA-XXXX-XXX`, déblocage par partage forcé sur X et Instagram). Aucun rapport visuel avec le produit actuel — signal d'un lancement ou d'un rebranding imminent, à re-regarder dans quelques mois.

## Archive

![[archive/planches/planche-millesimes-2021-2026.png]]

**Six directions artistiques en cinq ans, et le pendule fait trois allers-retours entre le clair et le sombre.** (1) **Avril 2021 → mars 2022** : hero violet plein `#4F2879`, page courte de 3 655 px, un seul bouton « Join Wait List Now », DM Sans + Montserrat — le produit n'est pas ouvert. (2) **~juin 2022** : bascule au blanc, accent indigo `#5138EE`, page multipliée par 2,3, titres en *Eudoxussans Display* — la seule display jamais utilisée, abandonnée en quelques mois. (3) **~septembre 2022** : hero sombre à dégradé mesh violet/bleu/magenta sur encre `#252841`, Inter seul, CTA « Apply for early access » — l'accès est sur candidature. (4) **2e semestre 2023** : retour au blanc, énorme blob circulaire en dégradé derrière le mockup, surlignage lavande sur les mots-clés du titre. (5) **2024** : le blob disparaît, arrivée du **texte en dégradé** bleu→magenta et du CTA en dégradé, mockup éclaté en cartes flottantes sur halo rose. (6) **fin 2025 / début 2026** : le hero passe de centré à **asymétrique deux colonnes**, les captures entrent dans un cartouche en dégradé violet→magenta, et Unbounded rejoint Inter.

Preuve technique de la rupture de 2022 : le site a **changé de projet Webflow**. L'ancien (`6053c55ad1417a6135ff02b6`, créé le 19 mars 2021) a été supprimé — tous ses assets renvoient 403. Le nouveau (`630df394ff44d46a174df570`, 30 août 2022) est toujours en production et **sert encore toutes ses feuilles de style historiques**, ce qui a permis de rejouer localement les millésimes que la Wayback ne rendait plus.

![[archive/planches/planche-app-2021-2023.png]]

**Le produit, lui, n'a jamais changé de grammaire : sidebar + cartes + vert/rouge.** L'app de mars 2021 affiche déjà sa roadmap dans le menu (*Simulator — COMING SOON*, *Zella University — COMING 2021*, *Zella Community — COMING 2021*) et son accent est le même violet que le site. En 2022, la sidebar passe au sombre `#141730`, la palette data se fixe (vert `#4ECDA4`, rouge saumon) et **la modale « Your daily Zella Insights » apparaît, coiffée de l'avatar taureau** : la personnification du produit date de là, pas de 2026. En 2023, le Zella Score arrive sous forme de **radar triangulaire à 3 axes** noté 81 — il en aura six en 2024.

## Ce que je retiens

- **Un score composite comme objet central d'un dashboard.** Six métriques disparates réduites à un chiffre sur une échelle de 0 à 100, avec le radar juste à côté pour montrer *d'où* vient la note. C'est la seule chose qu'on regarde en arrivant, et ça rend le reste du tableau de bord secondaire — au bon sens du terme.
- **La règle de couleur la plus stricte que j'aie relevée sur un dashboard** : 85 % de la surface en deux gris, toute la couleur réservée à la donnée. À copier tel quel dès qu'un produit affiche des chiffres.
- **Les toasts narratifs des cartes produit.** Montrer un fragment d'interface *plus* la notification que le produit vient d'émettre — ça raconte une action au lieu d'exposer une fonctionnalité, et ça marche mieux qu'un mockup complet.
- **Deux thèmes qui n'obéissent pas à la même charte** est un vrai défaut, pas une liberté : le sombre neutre casse la continuité de marque du clair. À ne pas reproduire.
- **Un onboarding qui sort du chrome de l'app** (fond dégradé, barre de progression, pleine page) pour une tâche récurrente comme l'import de trades : le geste rare mérite son propre espace.

## À réutiliser pour

Tout produit à données financières ou à suivi de performance : dashboards, outils d'analyse, tableaux de bord d'agence. La grammaire clair/sombre, la sobriété chromatique et le score composite se transposent tels quels. Les six millésimes de landing servent aussi de cas d'école sur la maturation d'un SaaS bootstrappé — de la waitlist violette à la vitrine à sept produits.

## Sources

- **Site officiel** — [www.tradezella.com](https://www.tradezella.com) : neuf pages capturées en pleine hauteur, desktop et mobile, le 31 août 2026 (`capture-site.py`). Les 25 variables de couleur et les quatre familles typographiques viennent de sa feuille Webflow de production. 20 pages au-delà de la limite fixée n'ont pas été capturées (blog et pages SEO).
- **Centre d'aide Intercom** — [help.tradezella.com](https://help.tradezella.com) : 20 collections, 125 articles, images retina sur `downloads.intercomcdn.com`. **C'est la seule source publique de vraies captures de l'app derrière le login** ; 15 écrans en viennent.
- **Walkthroughs vidéo** — chaîne officielle [@TradeZella](https://www.youtube.com/@TradeZella) (« Zella AI Full Walkthrough », `tXienOjcbl8` ; « How To Use TradeZella Backtesting In 5 Minutes », `zv7dL7k43W4`) et review tierce de Timothy B. (`g_0Tx5OAioY`). 18 frames extraites à `ffmpeg`, vidéos supprimées ensuite.
- **Wayback Machine** — millésimes 2021-04, 2022-03 et 2022-06 capturés directement pendant les fenêtres de disponibilité du service.
- **Common Crawl** — millésimes 2022-11, 2023-06, 2023-12, 2024-12, 2025-06 et 2026-03 reconstruits depuis le HTML d'époque (`index.commoncrawl.org`), rendus localement avec le CSS et les images d'époque encore servis par le CDN Webflow.
- **Board public de features** — [tradezella.com/changelog](https://www.tradezella.com/changelog) : 101 demandes, 44 améliorations, 21 intégrations, et l'app mobile toujours au backlog.
- **Presse et emploi** — Fast Company, 7 nov. 2024 (lu via le miroir [Yahoo Finance](https://finance.yahoo.com/news/built-one-own-tradezella-lets-090000826.html)) · [careers.tradezella.com](https://careers.tradezella.com) · l'annonce Product Designer sur [jobs.weekday.works](https://jobs.weekday.works/tradezella-product-designer).
- **Sources vides, vérifiées** — App Store et Google Play (aucune app), Mobbin, Refero (API énumérée), Screensdesign, Appshots, SaaS Landing Page, Webframe, Awwwards, One Page Love, Godly, Httpster, FWA, Minimal Gallery : **aucune trace de TradeZella**. Land-book, SiteInspire et CSSDA sont restés inaccessibles (Cloudflare) — non tranchés.

## Crédits

- **Umar Ashraf** — fondateur et CEO. Trader devenu éditeur faute de trouver un journal à son goût ; sans profil technique, il a d'abord fait coder le produit par une agence avant d'internaliser l'équipe. C'est aussi le visage marketing du produit (chaîne YouTube de trading à 750 000+ abonnés). [X @UmarAshraf](https://x.com/UmarAshraf) · [page auteur du blog](https://www.tradezella.com/blog-author/umar-ashraf)
- **Khadija Ashraf** — co-fondatrice et Head of Product, entrée à 19 ans. C'est le poste le plus proche du design dans l'équipe fondatrice. [LinkedIn](https://www.linkedin.com/in/khadija-ashraf-7106bb18b/)
- **Saira Ashraf** — co-fondatrice. [LinkedIn](https://www.linkedin.com/in/saira-ashraf-572238202/) — TradeZella est une entreprise familiale (Fast Company confirme deux sœurs du fondateur dans l'équipe).
- **Michael Arias** — Product Lead. [LinkedIn](https://www.linkedin.com/in/michael-arias-%F0%9F%A6%84-4a016b297/)
- **Zoia Khan** — Head of Zella University. [LinkedIn](https://www.linkedin.com/in/zoia-khan-63733b304/)
- **Aucun designer n'est crédité publiquement, nulle part.** `dribbble.com/tradezella` renvoie 404, Behance ne remonte qu'un concept non commandé, aucun portfolio ne revendique le produit, et aucune galerie ne crédite le site. L'entreprise a ouvert en 2026 un poste de **premier Design Engineer**, décrit comme devant « construire un design system de bout en bout, à partir de zéro » — traduction : en 2026 il n'y en a pas encore.
- **Attribution à ne pas faire** : Theo Tkachuk (Kyiv) a publié un projet Behance « TradeZella Dashboard » le 17 avril 2024 — sans description, sans tag, sans mention de commande. Très probablement un redesign personnel. [Le projet](https://www.behance.net/gallery/196449519/TradeZella-Dashboard) est intéressant à regarder, ce n'est pas un crédit.

## Mots-clés

journal de trading, trading journal, trade journal, carnet de trades, day trading, prop firm, backtesting, trade replay, P&L, profit and loss, calendrier de P&L, equity curve, courbe d'équité, win rate, profit factor, drawdown, R multiple, MAE MFE, tags d'erreur, playbook, discipline, streak, série, heatmap annuelle, GitHub contribution graph, score composite, radar chart, graphe en radar, hexagone de score, jauge en arc, donut bicolore, dashboard financier, data viz vert rouge, dashboard sombre, dark mode, thème clair thème sombre, sidebar navy, bento, cartes flottantes, toasts narratifs, mascotte 3D, taureau, bull, low poly, dégradé violet magenta, gradient text, texte en dégradé, Webflow, Inter, Unbounded, Inconsolata, JetBrains Mono, Intercom, assistant IA, agents IA, AI trading partner, prompt en langage naturel, SaaS finance, bootstrappé, TradeZella, Zella AI, Zella Score, Zella University, Spaces, Prop Firm Sync, Progress Tracker, Mentor Mode

---

Dossier créé par `/inspi` le 31 août 2026 · [[_APPS|← Apps & produits]] · [[_INSPIRATION|← Inspiration]]
