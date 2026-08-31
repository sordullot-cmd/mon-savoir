---
type: inspiration
discipline: ui-design
media: app
source: https://ultratrader.app
url_store: https://apps.apple.com/us/app/ultratrader-trading-journal/id1615206113
editeur: Pixium Labs (Toronto, Canada)
type_app: finance
plateformes: [ios, android, web]
version: 5.8.4 (2026-08-20), première sortie 2022-10-01
secteur: finance
couleur_principale: bleu #3d4dff
couleurs: ["#3d4dff", "#7b48fb", "#16d2a0", "#ea3943", "#0b0b0b", "#19191f", "#f9f9fb", "#ffa63d"]
patterns: [onboarding, paywall, tab-bar, mode-sombre, empty-state]
anime: oui
animations: [transitions-page, morphing, hover, celebration]
layout: grille
mood: [dark, bold, minimal]
typos: [Gilroy]
date_capture: 2026-08-31
tags: [inspiration, ui, dark]
---

# UltraTrader

> Le seul journal de trading du lot qui soit vraiment né mobile : apps natives iOS et Android, web app en second, et une identité bleue tenue de bout en bout. C'est la référence à regarder pour un produit financier qui doit être beau sur un écran de téléphone.

![icone](icone.png)

**Sources :** site officiel · App Store (métadonnées et 8 créas) · Google Play · variables CSS du site · trailer officiel YouTube · Product Hunt

> **Lecture** : chaque famille d'écrans est montrée par **une planche** (`<aspect>/planches/`), légendée juste dessous. Les fichiers individuels restent dans leur dossier d'aspect.

## En bref

- **Trois surfaces, une seule DA** : app iOS, app Android, web app — les mêmes verts, les mêmes rouges, le même bleu. C'est exactement ce que [[tradersync]] ne fait pas.
- **Une seule police pour tout : Gilroy**, en quatre graisses auto-hébergées. Aucune Google Font, aucune webfont tierce. 188 éléments rendus sur la home, pas une autre famille.
- **Sombre par défaut, clair en option**, piloté par un cookie `theme` — et les deux thèmes sont entièrement déclarés en variables CSS.
- **Le vert de gain est un menthe** (`#16d2a0`), pas un vert bourse. Le rouge de perte reste franc (`#ea3943`). Le couple donne une lecture immédiate du P&L sans agressivité.
- **Un seul accent chaud dans tout le système** : l'or `#ffa63d`, réservé au liseré de l'offre Premium. Une couleur, un usage.
- **Le trailer fait la moitié du travail de marque** : 46 s de narration 3D (rubans, cartes empilées, emoji en volume) avant même de montrer un écran.
- Note 4,625/5 sur l'App Store (56 avis US), 4,3/5 sur Play (553 avis), 50 K+ téléchargements. Annonce « 600+ brokers » en auto-sync. Futures non supportés.
- **Aucun designer crédité** nulle part — ni site, ni Dribbble, ni Behance. Deux co-fondateurs, un accélérateur universitaire.

## Écrans

![[ecrans/planches/planche-web-app.png]]

**La web app est un tableau de bord dense qui reste lisible parce que rien n'y est décoratif.** Sidebar à cinq entrées seulement (Dashboard, Live Trades, Finished Trades, Watchlist, Alerts), neuf tuiles de KPI avec des jauges en arc, une aire verte de P&L cumulé, un histogramme quotidien, et une liste de trades avec les logos de tokens. Le thème clair n'est pas une inversion mécanique : les verts et rouges y sont assombris (`#13b98d` et `#eb4750`) pour tenir sur blanc.

- `ecrans/webapp-dashboard-sombre.webp` — le dashboard complet, 2480 px de large.
- `ecrans/webapp-dashboard-clair.webp` — le même en clair, fond `#f9f9fb`.
- `ecrans/webapp-live-trades-sombre.webp` — les positions ouvertes multi-brokers, P&L en temps réel.

![[ecrans/planches/planche-app-ios.png]]

**Sur mobile, chaque écran ne défend qu'une seule idée, et le titre le dit.** `Own Your Consistency` pour le calendrier P&L, `Discover Your Trading Edge` pour l'analyse, `Relive Every Move` pour le replay. Les quatre premières images sont des frames du trailer officiel — donc l'app réelle en mouvement, pas des mockups habillés.

- `ecrans/app-ios-dashboard-clair.png` — header `Funded Account`, onglets Overview / Time Metrics / Analytics / Calendar.
- `ecrans/app-ios-analytics-pnl.png` — courbe d'aire verte puis histogramme quotidien, tab bar à cinq icônes.
- `ecrans/app-ios-trade-replay-chandeliers.png` — chandeliers plein écran avec `Best Day PNL` en surimpression.
- `ecrans/app-ios-performance-strategie.png` — performance par stratégie, barre de win rate à 67 %, jauge en arc.
- `ecrans/appstore-own-your-consistency-calendrier-pnl.png` — le calendrier P&L mensuel en thème clair, cases vert menthe / rouge pâle.
- `ecrans/appstore-discover-your-edge-analyse-pnl.png` — écran Analysis, jauge de win rate à 59,46 %.
- `ecrans/appstore-web-mobile-dashboard-sombre.png` — le dashboard web mis en scène pour le store.

## Flows

![[flows/planches/planche-flows.png]]

**Deux entrées seulement pour un trade : la synchro ou la main.** La connexion broker est présentée comme une liste de logos avec des pastilles `Auto Sync` — pas de tunnel, pas d'étapes numérotées. L'ajout manuel, lui, demande la stratégie puis **note la confiance en étoiles** : c'est le seul endroit du produit où l'on mesure un état d'esprit.

- `flows/appstore-save-time-auto-sync-brokers.png` — la liste des exchanges superposée aux positions synchronisées.
- `flows/webapp-connexions-brokers-sombre.webp` — le panneau `Broker Connections` côté web.
- `flows/app-ios-formulaire-add-trade.png` — l'étape stratégie du formulaire, avec notation par étoiles.

## Composants

![[composants/planches/planche-composants.png]]

**Le calendrier P&L est le composant que tout le secteur copie, et celui-ci est le plus sobre du lot** : une grille mensuelle, une teinte par jour selon le résultat, une colonne de totaux hebdomadaires à droite. Rien d'autre. À comparer avec la même idée chez [[traders-second-brain]] (une heatmap de setups) et chez [[tradetrack]] (une heatmap de progression façon GitHub).

- `composants/calendrier-pnl_ultratrader.webp` — le calendrier de performance, en sombre.
- `composants/fiche-trade_ultratrader.webp` — deux fiches de trade côte à côte : symbole, side, stratégie, tags, mistakes, mini-chart.
- `composants/tags-et-mistakes_ultratrader.png` — le système de chips : tags bleus (Breakout, Reversal, Swing Trades, High Risk) contre `Mistakes` rouges (FOMO, Entry Late, No Stop Loss). Le codage couleur porte tout le sens.
- `composants/liste-trades-actions_ultratrader.webp` — la liste avec son menu d'actions contextuel.
- `composants/trade-replay-chandeliers_ultratrader.png` — le replay avec `Key Moments` listés sous le chart (charts TradingView).

## Animations

![[animations/planches/planche-frames-trailer.png]]

**Le trailer commence par ne pas montrer le produit.** Rubans blancs qui se plient en 3D sur dégradé bleu, un `37% — Your actual win rate` en gros chiffre, des emoji en volume, des cartes `Add Trade` empilées en perspective : quarante secondes de mise en scène avant la démo réelle. C'est le seul produit du lot qui investit dans du motion de marque plutôt que dans des captures d'écran.

`animations/trailer-app-intro_ultratrader.mp4` — le trailer officiel (46 s, 1080 × 1920 à l'origine, réencodé à 720 px de large). Le CSS déclare par ailleurs une durée d'animation globale : `--default-animation-duration: .35s`.

## Branding

![[branding/logo-ultratrader.svg|300]]

**Un double chevron ascendant, construit en trois volumes** — un chapeau plein et deux ailes — qui lit comme une flèche vers le haut sans jamais dessiner un graphique. L'icône d'app le pose en blanc sur un carré bleu-violet dégradé. Le wordmark du carton final est en Gilroy bold, la même police que tout le site.

- `branding/icone-ultratrader-1024.png` — l'icône App Store en 1024 px.
- `branding/trailer-logo-lockup-final.png` — le lockup symbole + wordmark, avec les badges de stores.
- Aucun press kit : `/press`, `/brand`, `/media`, `/about` renvoient 404. Ces trois fichiers sont tout ce qui existe.

## Couleurs

![[couleurs/palette-marque.svg]]

**Un bleu tient toute l'identité, et il n'apparaît presque jamais dans les données.** `#3d4dff` est partout — icône, boutons, hero, dégradés marketing — mais le dashboard, lui, ne parle qu'en vert et rouge. La marque et la donnée occupent deux registres chromatiques séparés, ce qui évite qu'un accent de marque soit confondu avec un signal de performance.

**Le bleu et ses voisins**

| Nom de token | Hex | Usage |
| --- | --- | --- |
| `--primary` / `--blue` | `#3d4dff` | la couleur de marque, servie aussi à 25 % (`#3d4dff40`) |
| `--light-royal-blue` | `#4c2fff` | renfort du dégradé |
| `--purple` | `#7b48fb` | second accent |
| `--dodger-blue` | `#46d1fd` | bleu clair d'appoint |

**Neutres et accent chaud**

| Nom de token | Hex | Usage |
| --- | --- | --- |
| `--gray` | `#9ba1af` | texte secondaire, dans les deux thèmes |
| `--dark` | `#1a1d2e` | bleu-noir de fond |
| `--dark-blue` / `--dark-blue2` | `#22263e` / `#1b1e30` | cartes bleutées |
| `--gold` | `#ffa63d` | liseré de l'offre Premium — **seul usage** |
| `--goldSecondary` | `#ff9500` | servi à 20 % (`#ff950033`) |

Le dégradé signature du marketing va de `#16d2a0` (le vert de gain) à `#3d4dff` (le bleu de marque) : la promesse du produit, littéralement mise en couleur.

![[couleurs/palette-app-sombre.svg]]

**Le thème sombre n'est pas noir, il est bleuté.** Les cartes sont en `#19191f` — un gris qui tire vers le bleu — et les pastilles de gain et de perte ont leur propre fond sourd (`#173c3a`, `#421d27`) plutôt qu'une transparence. C'est plus de travail à maintenir, mais le résultat ne bave pas sur les fonds.

| Nom de token | Hex | Usage |
| --- | --- | --- |
| `--background` | `#0b0b0b` | fond de page |
| `--componentBackground` | `#131313` | composants |
| `--cardBackground` | `#19191f` | cartes, légèrement bleutées |
| `--fourthDark` / `--thirdDark` | `#1e2029` / `#363947` | surfaces basses, bordures |
| `--blueSecondary` | `#1a1c3b` | fond d'accent bleu |
| `--textMain` / `--textSecondary` | `#ffffff` / `#d2d2d2` | textes |
| `--priceGreen` / `--greenSecondary` | `#16d2a0` / `#173c3a` | gain et son fond de pastille |
| `--priceRed` / `--redSecondary` | `#ea3943` / `#421d27` | perte et son fond de pastille |

![[couleurs/palette-app-clair.svg]]

**En clair, le texte principal n'est jamais du noir pur** (`#383838`), et les pastilles passent en pastel (`#b9f1e2`, `#f9c4c7`). Le vert descend de `#16d2a0` à `#13b98d` : la teinte est conservée, la luminosité recalculée pour le contraste. C'est la bonne méthode.

| Nom de token | Hex clair | Usage |
| --- | --- | --- |
| `--background` | `#f9f9fb` | fond de page, blanc bleuté |
| `--componentBackground` | `#ffffff` | composants |
| `--cardBackground` | `#f7f7fb` | cartes |
| `--thirdDark` | `#d6d8e1` | bordures |
| `--textMain` / `--textSecondary` | `#383838` / `#666666` | textes |
| `--priceGreen` / `--greenSecondary` | `#13b98d` / `#b9f1e2` | gain |
| `--priceRed` / `--redSecondary` | `#eb4750` / `#f9c4c7` | perte |

## Marketing

![[marketing/planches/planche-store-et-site.png]]

**Les huit créas de store sont strictement identiques sur App Store et Google Play** — mêmes fichiers, même ordre, diff pixel à zéro. Un seul jeu produit pour deux écosystèmes : économie assumée, au prix des conventions propres à chaque store. À noter, une coquille dans la créa officielle n° 7 : `Master Your Minset`.

- `marketing/appstore-cover-professional-trading-journal.png` — la carte de couverture, badge `#1` avec lauriers dorés.
- `marketing/appstore-iphone-3d-dashboard-note-4-7.png` — mockup iPhone en perspective, icône en volume, note 4,7.
- `marketing/site-landing-sombre.png` / `-clair.png` — la landing dans les deux thèmes (9 148 px de haut).
- `marketing/site-landing-mobile.png` — le rendu iPhone.
- `marketing/site-pricing-sombre.png` — le pricing : Basic 0 $ contre Premium 9 $/mois annualisé (carte mise en avant par un liseré doré), paiement crypto accepté (USDT, USDC, Litecoin).

Hero : « The Best Trading Journal for Web & Mobile », mention `Backed by YSpace` (l'accélérateur de York University), « Join +100K active traders ».

## Typographie

**Gilroy, et rien d'autre.** Quatre graisses auto-hébergées — Light 300 en `.otf`, Medium 500, SemiBold 600, Bold 700 en `.ttf`. Aucune Google Font, aucun appel externe. Sur la home, 188 éléments sont rendus en Gilroy et aucune autre famille n'est chargée. Pas de fiche dans le vault — candidate à `/font`.

## Pourquoi je l'aime

Parce que c'est de la **discipline plutôt que de l'idée**. Il n'y a rien d'inventif dans UltraTrader : un bleu, un menthe, un rouge, une police, deux thèmes. Mais tout est appliqué partout, sans exception, sur trois plateformes — et le résultat est le produit le plus cohérent du lot. C'est la démonstration qu'un système chromatique tenu bat une direction artistique brillante mal appliquée (voir [[tradersync]], qui fait exactement l'inverse avec trois systèmes qui s'ignorent).

Et le trailer prouve quelque chose d'utile : un outil financier a le droit d'être joyeux avant d'être sérieux, tant que la joie reste dans la communication et jamais dans l'interface.

## À réutiliser pour

- **Un produit multi-plateformes** : la méthode « une teinte, deux luminosités » pour passer un vert ou un rouge d'un thème sombre à un thème clair sans changer la couleur perçue.
- **Un système de tags de qualification** : chips bleus pour ce qu'on a fait exprès, chips rouges pour ce qu'on a raté. Deux couleurs, tout est dit.
- **Un accent chaud à usage unique** : l'or réservé au palier payant, jamais ailleurs.
- **Un trailer produit vertical** : narration abstraite d'abord, démo réelle ensuite, carton logo à la fin.
- **Un calendrier P&L mensuel** : le composant de référence du secteur, ici dans sa version la plus dépouillée.

## Limites de la récolte

- **Wayback Machine hors service** pendant le run (28 snapshots identifiés entre 2022 et 2026, aucun rejouable) : `archive/` **est vide**. Snapshots à reprendre : `20220429131207` (avant le lancement iOS), `20240718052843`, `20250118174538`, `20260122005527`.
- **Aucune base d'UI ne référence l'app** : Mobbin (0 résultat), UXArchive (403), Appshots, Screensdesign, Refero, Godly — rien. Les flows viennent donc des créas de store et du trailer, pas d'une exploration libre.
- **Pas de paywall in-app récolté** : rien chez Adapty ; la page `/pricing` du site en est le plus proche.
- **Aucune capture iPad** : Apple n'en déclare aucune.
- `process/` **est vide** : l'éditeur ne publie rien sur sa fabrication.

## Sources

- **App Store** — <https://apps.apple.com/us/app/ultratrader-trading-journal/id1615206113> : icône 1024, 8 créas en 1242 × 2688, métadonnées complètes (bundle `com.pixiumlabs.ultratrader`, version 5.8.4).
- **Google Play** — package `com.ultratrader` : mêmes créas, 553 avis, fourchettes d'achats in-app.
- **Site officiel** — <https://ultratrader.app> : les captures de la web app en `.webp` (pipeline Astro), la landing dans les deux thèmes, le pricing.
- **Feuille de style du site** : toutes les variables de couleur des deux thèmes, la durée d'animation globale, les quatre fichiers Gilroy.
- **Trailer officiel** — <https://www.youtube.com/watch?v=lk9tzomxjbk> (46 s, publié le 2026-07-27) : la meilleure source d'écrans réels en mouvement.
- **Product Hunt** — fiche existante mais lancement confidentiel (3 points), aucun média inédit.
- **Blog** — <https://blog.ultratrader.app> (Astro) : signature éditoriale quasi unique.

## Crédits

- **Emad Kazemi** — co-fondateur.
- **Kaveh Vajedsamie** — co-fondateur, full-stack.
- **Pixium Labs** — la structure éditrice (bundle `com.pixiumlabs.ultratrader`, contact `hello@pixiumlabs.com`), fondée en 2022, basée à Toronto / Markham (Canada), non financée.
- **YSpace** — accélérateur de York University, affiché dans le hero.
- **Ghazaleh Zeynali** — autrice de la majorité des articles du blog.
- **Aucun designer crédité** : vérifié sur le site, Dribbble, Behance et LinkedIn. Le design n'est attribué à personne publiquement.
- Typographie : **Gilroy** (auto-hébergée). Charts du replay : **TradingView**.
- Comptes officiels : <https://instagram.com/ultratrader.app> · <https://twitter.com/ultratraderapp> · <https://t.me/UltraTraderSupport>

## Mots-clés

journal de trading, trading journal, app mobile finance, mobile-first fintech, iOS Android web, multi-plateforme, auto-sync broker, 600 brokers, Binance Bybit OKX MT4 MT5 cTrader, calendrier P&L, PNL calendar, heatmap mensuelle, win rate, profit factor, R tracking, trade replay, TradingView, tags et mistakes, FOMO, chips de qualification, thème sombre thème clair, cookie theme, Gilroy, police auto-hébergée, bleu électrique, mint, vert menthe, or Premium, dégradé vert vers bleu, trailer produit vertical, motion 3D, narration avant démo, Astro, Tailwind, webp, paiement crypto, USDT USDC Litecoin, Toronto, Pixium Labs, YSpace, freemium

## À voir aussi

- [[traders-second-brain]] — l'inverse : monochrome, web only, une seule personne.
- [[tradetrack]] — même sobriété sombre, mais en Tailwind/shadcn et sans app native.
- [[tradersync]] — l'autre produit à apps natives du lot, et le contre-exemple de cohérence.
- [[_APPS]] · [[_COMPOSANTS]] · [[_ANIMATIONS]]
