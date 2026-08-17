---
type: univers
univers: Kraken
categorie: marque
secteur: finance
annee: 2011 (fondation) — 2019 (passage au violet) — design system actuel
createurs: "Kraken / Payward, Inc. — fondée par Jesse Powell (2011) · rebranding 2019 : illustrations Rune Fisker, agence BBH New York · identité et design system actuels : équipe Brand & Creative interne (aucun crédit public trouvé)"
source: https://www.kraken.com
couleur_principale: violet Brand #7132F5
couleurs: ["#7132F5", "#5B1ECF", "#8A61FF", "#00ADFE", "#101114", "#F6F5F9", "#686B82", "#08844F", "#D11D45", "#C39621", "#FF3B29"]
mood: [minimal, bold, dark]
tags: [inspiration, univers, brand, ui, web, typo, 3d, finance, crypto, web3, design-system, dark]
---

# Kraken

> Le dossier de référence sur l'univers Kraken — l'exchange crypto (Payward, Inc.), pas l'équipe de hockey ni les agences homonymes. Ce qui rend ce cas intéressant : **tout le design system est lisible dans le CSS servi par kraken.com**. 519 tokens de couleur nommés, 8 thèmes, 3 familles typographiques maison, une échelle typo complète. On n'a pas de brand book PDF ici — on a mieux : le système tel qu'il tourne en production, plus le relevé au pixel de ce qui s'affiche vraiment à l'écran, et l'écart entre les deux.

**Sources principales :** [kraken.com](https://www.kraken.com) · [kraken.com/press/kraken-images](https://www.kraken.com/press/kraken-images) (ZIP officiels : logos Krak, visuels presse par produit) · design tokens extraits de `kraken.com/_static/css/ccc864ce.css` · App Store (captures produit haute résolution) · [blog.kraken.com — Kraken rebranding](https://blog.kraken.com/news/kraken-rebranding-do-you-like-it) (janvier 2019) · [Agent Pekka — Kraken Brand Illustrations](https://agentpekka.com/project/kraken-brand-illustrations/)

---

## Le système en bref

- **Une couleur de marque, utilisée comme une ponctuation.** Le violet `#7132F5` occupe **0,57 % des pixels de la home** (relevé au pixel, cf. plus bas). Tout le reste est neutre. C'est l'inverse du réflexe habituel : la marque n'est pas la surface, elle est l'accent — boutons primaires, liens, badges, contours de focus.
- **Sortir du bleu, délibérément.** Le billet de blog de janvier 2019 dit la stratégie en toutes lettres : la finance et la tech utilisent le bleu « pour ses associations de confiance et de fiabilité, mais trop d'entreprises l'utilisent ». Kraken part sur un violet plus audacieux, « qui évoque la richesse et le prestige ».
- **Aucun gris pur du côté Kraken.** Toute la rampe de neutres est tirée vers le bleu-violet : `#686B82` (730 occurrences dans le CSS), `#9497A9`, `#484B5E`, `#101114`. C'est ce qui empêche une interface aussi sobre de paraître froide ou générique.
- **Huit thèmes dans un seul système.** `.light-theme`, `.magic-light-theme`, `.magic-dark-theme`, `.trade-dark-theme`, `.pay-light-theme`, `.pay-dark-theme`, `.payward-light-theme`, `.payward-dark-theme` — même grammaire de tokens (~537 par thème), quatre accents de marque différents.
- **Un accent qui ne bouge jamais.** `--text-color-ds-brand-breakout: #00ADFE` est **identique dans les huit thèmes**. C'est le seul accent non violet du système : le bleu cyan sert de sortie de route quand le violet ne suffit pas.
- **Krak est le contre-exemple assumé.** L'app de paiement lancée en juin 2025 tourne sur le même design system, mais en `.pay-*` : corail `#FF3B29`, neutres **gris purs**, aucun violet. Une famille de produits, deux mondes chromatiques.
- **Les images de marque sont en verre, pas en dessin.** L'imagerie actuelle est du rendu 3D : éclats de verre irisés, dispersion, chrome. Le symbole lui-même est décliné en volume chromé (`spot-illustration-beast.png`).

---

## Couleurs

Deux sources, jamais mélangées : la **palette déclarée** vient des tokens du design system servi par kraken.com (chaque pastille porte le nom exact du token) ; la **palette relevée** vient d'un comptage de pixels sur les médias rapatriés. Les valeurs relevées absentes de tout token sont marquées **HORS CHARTE**.

### Palette déclarée — tokens du design system

![[palette-coeur-de-marque.svg]]

![[palette-semantique-light.svg]]

![[palette-neutres.svg]]

![[palette-etats-hausse-baisse.svg]]

![[palette-krak-corail.svg]]

**Cœur de marque**

| Nom | Hex | Token | Rôle |
| --- | --- | --- | --- |
| Brand | `#7132F5` | `--colors-ds-brand` | Boutons primaires, liens, badges, focus (269 occurrences) |
| Brand hover | `#5B1ECF` | `--background-color-ds-button-primary-high-hover` | Survol du bouton primaire |
| Brand press | `#471CA0` | `--colors-ds-textlink-hover-brand` | État le plus foncé |
| Brand clair | `#855BFB` | `--background-color-ds-progressbar-primary` | Base des voiles translucides (alpha `29` / `3d` / `52`) |
| Trade dark brand | `#8A61FF` | `--colors-ds-brand` (`.trade-dark-theme`) | Le violet de Kraken Pro |
| Magic dark brand | `#9D82FE` | `--colors-ds-brand` (`.magic-dark-theme`) | Le plus clair des quatre |
| Brand breakout | `#00ADFE` | `--text-color-ds-brand-breakout` | Identique dans les 8 thèmes |

**Rôles sémantiques** (`.light-theme`) — la grammaire de tout le produit

| Rôle | Hex | Token |
| --- | --- | --- |
| Primary | `#101114` | `--colors-ds-primary` |
| Neutral | `#686B82` | `--colors-ds-neutral` |
| Dimmed | `#9497A9` | `--colors-ds-dimmed` |
| Disabled | `#C6C7D2` | `--colors-ds-disabled` |
| Inverted | `#FFFFFF` | `--colors-ds-inverted` |
| Positive | `#08844F` | `--colors-ds-positive` |
| Negative | `#D11D45` | `--colors-ds-negative` |
| Warning | `#C39621` | `--colors-ds-warning` |
| Info | `#0079B4` | `--colors-ds-info` |
| Fond de page | `#F6F5F9` | `--ds-bg-color` |

**Rampes complètes** — chaque rôle existe en version claire (pour les thèmes sombres) et foncée (pour le thème clair) :
- Positive : `#35DF8D` · `#149E61` · `#08844F` · `#026B3F` · `#005531`
- Negative : `#FF7386` · `#F5395E` · `#D11D45` · `#AA0132` · `#840125`
- Warning : `#FFCD60` · `#E8B100` · `#C39621` · `#A67C1D` · `#553C00` · `#3B2A00`
- Info : `#00ADFE` · `#0092D8` · `#0079B4` · `#006394`
- Neutres Kraken : `#FFFFFF` · `#F6F5F9` · `#F7F7FA` · `#C6C7D2` · `#9497A9` · `#686B82` · `#484B5E` · `#22232D` · `#101114`
- Neutres Krak / Payward (gris purs) : `#F5F5F5` · `#9E9E9E` · `#757575` · `#0D0D0D` · `#A7A7A7` · `#7D7D7D` · `#414141` · `#717171`

**Krak** — `.pay-light-theme` / `.pay-dark-theme` : brand `#FF3B29` (identique en clair et en sombre), negative `#E51806` / `#FF6557`, primary `#0D0D0D`, inverted `#F5F5F5`. Le fichier de logo officiel du press kit s'appelle littéralement `KRAK LOGO CORAL`.

### Palette relevée — ce que les pixels disent

![[palette-relevee.svg]]

Comptage au pixel (`palette.py releve`) sur la home capturée, les 8 visuels App Store, les 8 écrans Kraken Pro et les 9 écrans Krak. Ce que ça révèle, et qu'aucune guideline n'écrit :

- **Le violet tient sur un demi pour cent.** Home : fond `#F6F5F9` 26,11 % · blanc 16,98 % · brand `#7132F5` **0,57 %**. Le token de fond de page est respecté au hex exact — mais la couleur de marque est réduite à l'état de signal.
- **Deux noirs non documentés arrivent avant le token officiel.** Sur la home : `#141414` (4,28 %) et `#0B041A` (4,08 %) devancent `#101114` (1,30 %), qui est pourtant *le* noir du système. Les sections sombres du site marketing ne parlent pas la même langue que le produit.
- **Le marketing a son propre noir violet.** Les visuels App Store sont posés à 47,14 % sur `#09041A` — un violet-noir profond qui n'existe dans aucun token. Le fond clair de ces mêmes visuels, `#F6F5FA`, est à un chiffre de `--ds-bg-color` `#F6F5F9`.
- **Le sombre de Kraken Pro est violet, pas gris.** `#161220` (14,40 %), `#0C0612` (6,31 %), `#201E2C` (3,35 %) — aucun n'est un token. Le terminal garde la teinte de la marque jusque dans ses fonds. Le vert de hausse relevé, `#36DF8E`, est à un chiffre du token `#35DF8D`.
- **Krak est plus noir que son propre token.** `#000000` occupe 39,34 % des écrans, devant `#0D0D0D` (13,54 %) qui est le `primary` déclaré. Et le corail `#FF3B29` — la couleur de marque — **ne passe même pas le top 20**.

---

## Typographie

Trois familles maison, servies en OTF depuis `kraken.com/_assets/fonts/`. Les fichiers ne sont pas rapatriés dans le vault (polices propriétaires, pas de licence de rediffusion) — seul le système est documenté ici.

| Famille | Coupes | Usage |
| --- | --- | --- |
| **Kraken-Brand** | Light 300 · Regular 400 · Medium 500 · Bold 700 · Black 900 · ExtraBlack 950, chacune + oblique | Display, titres de marque |
| **Kraken-Product** | Regular 400 · Medium 500 · SemiBold 600 · Bold 700, chacune + oblique | UI et texte courant |
| **Kraken-Mono** | Regular 400 · Medium 500, chacune + oblique | Chiffres, prix, données de marché |

- **Fallback révélateur** : la pile est toujours `Kraken-*, "IBM Plex Sans" / "IBM Plex Mono", Helvetica, Arial, sans-serif`. IBM Plex en premier recours, pas Helvetica — les coupes maison sont pensées dans cette famille de proportions.
- **Échelle en rôles, pas en tailles** : `brand1–4` · `display1–4` · `heading1–6` · `body1–4` · `bodyMono1–3` · `caption1–2`.
- **Le display est massif et serré.** `brand1` monte à **10rem (160 px)**, et jusqu'à `12.5rem (200 px)` aux grands breakpoints — avec un `line-height` de `8.75rem (140 px)`, donc **inférieur à la taille du texte**. Interlettrage négatif jusqu'à `-4px` sur `brand1` selon le jeu de thème (`-2.5px` et `-1px` ailleurs). Résultat : un bloc de titre compact, sans air, qui se lit comme une masse.
- **Le corps est léger.** Plusieurs jeux de thèmes posent `body1–4` en `font-weight: 300`. Sur `#686B82`, ça donne le gris discret typique de leurs pages.
- **Deux jeux typographiques cohabitent** : `.text-theme-set-pay` (Krak) utilise Kraken-Brand jusque dans le corps de texte, et `.text-theme-set-payward` sort complètement du système maison pour **Söhne** (corps, titres, mono) et **Financier Display** (display et brand) — deux polices de Klim Type Foundry (Kris Sowersby). La maison mère Payward parle une autre langue typographique que ses produits.

---

## Branding

43 fichiers, majoritairement vectoriels, tous issus de sources officielles (press kit ZIP + CDN du site).

**Le symbole.** Une forme de tentacule/calmar stylisée qui fonctionne comme un « m » à trois jambes arrondies — le même glyphe sert de symbole Kraken, d'icône d'app, et de marque sur la Krak Card. Décliné en rendu 3D chromé irisé pour l'imagerie de marque :

![[illustrations/spot-illustration-beast.png]]

**Logotypes Kraken** — `kraken-logotype-officiel.svg` (le fichier du press kit, violet `#7132F5` dans le path), `kraken-logo-horizontal.svg`, plus les lockups de la gamme : `kraken-pro-logo.svg` · `kraken-institutional-logo.svg` · `kraken-vip-logo.svg` · `kraken-prime-logo.svg` · `kraken-otc-logo.svg`.

**Icônes d'app en vectoriel 1024** — `icone-app-kraken-1024.svg` · `icone-app-kraken-pro-1024.svg` · `icone-app-kraken-desktop-1024.svg` · `icone-app-krak-1024.svg`. Rare de trouver des icônes d'app en SVG : utile pour voir la construction, pas juste le rendu.

**Le jeu d'icônes produit** (36–48 px, un par produit de la maison) : `icone-produit-kraken.svg` · `-kraken-pro` · `-kraken-desktop` · `-kraken-cli` · `-kraken-institutional` · `-krak`, plus `kraken-360-protocoles-icone.svg` et `payward-services-icone.svg`. Vu ensemble, c'est la cartographie de l'écosystème.

**Krak** — le press kit officiel livre le jeu complet, en SVG et PNG @2x : icône et logo en `black` / `white` / `coral`, plus deux versions **duotone** (une pour fond clair, une pour fond sombre) et l'icône d'app. `krak-logo-coral.svg`, `krak-logo-duotone-fond-sombre.svg`, `krak-symbole.svg`…

---

## Illustrations

L'imagerie de marque actuelle est du **verre en 3D** : plaques irisées, dispersion chromatique, arêtes nettes. Une matière, déclinée en compositions.

![[illustrations/eclats-de-verre-home-4109px.png]]

- `eclats-de-verre-home-4109px.png` — la composition de la home, en pleine résolution (4109 px). Une volée de plaques de verre en perspective, du bleu-cyan au violet profond.
- `eclats-de-verre-institutional-4109px.png` · `eclats-de-verre-2908px.png` · `eclats-de-verre-2800px.png` — les variantes par page. Même matière, cadrages et densités différents.
- `decor-vip-4800px.png` — le visuel du programme VIP, 4800 px de large.
- `krak-lettrage-spend.svg` / `krak-lettrage-send.svg` — le lettrage vectoriel de Krak (« send », « spend »), utilisé en display sur la page produit.
- `krak-fleche-symbole.png` — le symbole de flèche de Krak.

**Le set de 2019, en revanche, était dessiné** — illustrations sci-fi / mythologie du kraken signées Rune Fisker (voir crédits). Le visuel d'annonce d'époque n'a pas été rapatrié en pleine qualité : les seules copies accessibles sont les images du billet de blog en 900 px, et la page portfolio d'Agent Pekka est protégée par Cloudflare (403). À retenter si la référence devient utile.

---

## UI

56 écrans. Deux natures à ne pas confondre.

**Captures App Store en pleine résolution (1290 × 2796)** — les visuels marketing des quatre apps, récupérés via l'API iTunes :
- `kraken-app-screen-01` → `08` — l'app grand public (v3.76.0)
- `kraken-pro-screen-01` → `08` — le terminal de trading mobile (v5.67.0)
- `kraken-wallet-screen-01` → `06` — le wallet auto-custodial (v1.29.0)
- `krak-screen-01` → `09` — l'app de paiement (v1.55.2)

À noter : ce sont des visuels **composés** (téléphone tenu en main, fond dégradé), pas des captures brutes. On y lit la direction artistique autant que l'interface.

![[ui/kraken-pro-screen-02.png]]

**Écrans produit du site** — plus proches de l'UI réelle :
- Kraken Pro : `web-kraken-pro-terminal-3528px.png` (le terminal complet, 3528 px)
- Kraken Desktop : `web-desktop-multifenetres-3083px.png`, `web-desktop-ladder-trading.png`, `web-desktop-layouts-modulaires.png`, `web-desktop-themes-1` → `4` (le système de thèmes de l'app, montré explicitement), `web-desktop-share-board.png`, `web-desktop-performance.png`
- Institutional : `web-institutional-exchange.png`, `-subaccounts`, `-api`, `-market-data`
- Krak : `web-krak-telephone.png`, `web-krak-earn.png`, `web-krak-grab-the-app-1` → `4`
- Onboarding : `web-onboarding-creation-compte.jpg`, `web-onboarding-verification-identite.jpg` — les écrans de KYC, rarement montrés

---

## Web

Captures pleine hauteur de kraken.com (Chrome via CDP, août 2026) — 5 pages, 8 000 à 10 000 px de haut chacune.

- `site-home.png` — la home complète. La référence pour voir comment le violet est rationné sur toute la longueur d'une page.
- `site-krak.png` — la page produit Krak : le basculement complet vers le corail et le noir pur.
- `site-institutions.png` — la même marque en registre institutionnel.
- `site-staking.png` · `site-desktop.png` — deux pages produit.

Trois pages tentées n'existent plus (`/pro`, `/features/crypto-wallet`, `/features/kraken-pro` renvoient une 404) — captures écartées. La page 404 elle-même a une jolie spot illustration violette, si le besoin s'en présente.

---

## Animations & vidéos

Quatre fichiers, tirés directement du CDN du site (pas de réencodage, fichiers sources).

- `desktop-demo.mp4` (11 Mo) — la démo de Kraken Desktop : manipulation des fenêtres, layouts, thèmes.
- `krak-demo.mp4` (3,0 Mo) — la démo de l'app Krak.
- `institutional-hero.mov` (3,4 Mo) et `institutional-hero.webm` (708 Ko) — le hero animé de la page institutionnelle, dans les deux formats servis par le site. Comparer les deux est instructif sur leur arbitrage poids/qualité.

Pas de trailer ni de film de marque rapatrié : `yt-dlp` et `ffmpeg` ne sont pas installés sur cette machine. Les vidéos ci-dessus sont passées parce qu'elles sont servies en fichiers directs.

---

## Produit

- `krak-card-2176px.png` — **la Krak Card en trois finitions** : corail, noir, argent brossé. Symbole Kraken embossé + « krak » en bas de casse. Le dégradé du corail est concentrique, pas linéaire.
- `krak-card-vertical.png` · `krak-card-1200px.png` — autres cadrages.
- `press-visual-*` (12 fichiers) — les visuels presse officiels, un ou deux par produit : Consumer, Pro, Desktop, Wallet, Institutional, Bank. Mockups d'appareils sur fond de marque, en version A et B.
- `kraken-desktop-icones-os.png` — les icônes de plateforme (Mac, Windows, Linux, Debian).

---

## L'écosystème de marque

Le CSS et le jeu d'icônes révèlent la gamme complète, ce qu'aucune page ne montre d'un coup :

| Produit | Registre | Accent |
| --- | --- | --- |
| Kraken (grand public) | `.light-theme` | violet `#7132F5` |
| Kraken Pro | `.trade-dark-theme` | violet `#8A61FF` sur sombre violacé |
| Kraken Desktop | app native, thèmes personnalisables | — |
| Kraken Wallet | auto-custodial | violet |
| Kraken Institutional (+ Prime, OTC, 360) | institutionnel | violet |
| Kraken Bank | bancaire | violet |
| Kraken CLI | outil développeur | — |
| **Krak** | `.pay-*` — app de paiement mondiale (lancée le 26 juin 2025) | **corail `#FF3B29`** |
| Payward, Inc. | maison mère | Söhne + Financier Display |

---

## Artistes & crédits

- **Rune Fisker** — illustrateur, Copenhague. Auteur du set d'illustrations du relaunch de 2019 (inspiré de la SF et de la mythologie du kraken). Agence : **BBH New York**. Représenté par **Agent Pekka**. Aussi co-fondateur du studio d'animation Benny Box et co-propriétaire de Studio X Kitchen. Clients : Apple, Mozilla, Nike, Google, The New Yorker, Wired, The New York Times.
  - Portfolio : [runefisker.com](https://runefisker.com/) (503 au moment de la collecte) · [agentpekka.com/artist/rune-fisker](https://agentpekka.com/artist/rune-fisker/) · Instagram [@rfisker](https://www.instagram.com/rfisker/)
- **Kraken / Payward, Inc.** — fondée le 28 juillet 2011 par **Jesse Powell**, trading ouvert en 2013. Co-CEO en 2025 : **Arjun Sethi** et **Dave Ripley**.
- **Identité et design system actuels** : produits par l'équipe **Brand & Creative** interne (un poste d'Executive Creative Director, Head of Brand, rattaché au CMO, pilote la direction créative sur toutes les surfaces — site, produit, publicité, social). **Aucun crédit public individuel ni agence externe trouvé** pour le travail actuel (imagerie 3D verre, design system, typographies maison) : ne rien attribuer sans nouvelle source.
- **Klim Type Foundry** (Kris Sowersby) — **Söhne** et **Financier Display**, utilisées par le jeu de thème Payward.

---

## Sources

- Site officiel : `https://www.kraken.com` (pages home, /krak, /institutions, /features/staking, /desktop)
- Press kit images : `https://www.kraken.com/press/kraken-images` — ZIP par produit sur `cdn.sanity.io/files/51n36hrp/facade/…` et `assets.kraken.com/marketing/krak/krak-images-2025-06-25.zip`
- Assets CDN : `https://assets-cms.kraken.com/images/51n36hrp/facade/…` (Sanity)
- Design tokens et `@font-face` : `https://www.kraken.com/_static/css/ccc864ce.css`
- Captures produit : API iTunes (`itunes.apple.com/lookup?id=…`) — apps `1481947260`, `1473024338`, `1626327149`, `6738051700`
- Rebranding 2019 : `https://blog.kraken.com/news/kraken-rebranding-do-you-like-it`
- Crédits illustration : `https://agentpekka.com/project/kraken-brand-illustrations/`
- Krak (lancement 26 juin 2025) : `https://www.businesswire.com/news/home/20250626762957/en/Krak-Is-Here-Kraken-Launches-New-All-in-One-Global-Money-App`

---

## Pourquoi je l'aime

- **La leçon de rationnement.** Une seule couleur de marque, tenue à moins d'un pour cent de la surface, et pourtant l'interface est immédiatement identifiable. C'est la démonstration qu'une identité forte ne se joue pas au volume de couleur mais à la constance de son emploi.
- **Les gris ne sont pas gris.** Toute la rampe neutre est tirée vers le bleu-violet. C'est un détail invisible et c'est exactement ce qui différencie leur sobriété d'une sobriété froide. À voler.
- **Un système, plusieurs marques.** Huit thèmes, quatre accents, une seule grammaire de tokens. Krak est corail et noir pur sans jamais sortir du système. Le bon modèle quand un client a plusieurs produits.
- **Le display serré.** 160 px de titre avec 140 px d'interligne et −4 px d'interlettrage : les titres deviennent des masses, pas des lignes. Radical et très efficace sur les hero.
- **L'écart entre la charte et la production.** Trois noirs différents cohabitent (`#101114` déclaré, `#141414` et `#0B041A` sur le site, `#09041A` en marketing). C'est aussi utile que le système lui-même : ça montre où un design system se fissure en vrai, dans les mains du marketing.
- **Le verre irisé comme matière de marque.** Une seule matière 3D, déclinée en compositions, remplace toute une bibliothèque d'illustrations. Économe et distinctif.

## À réutiliser pour

- Projet : [[ ]] — tout produit finance / fintech / web3 à sortir du bleu.
- Modèle de **design system multi-marques** : un jeu de tokens sémantiques (`brand`, `primary`, `neutral`, `dimmed`, `positive`, `negative`, `warning`, `info`) décliné en thèmes nommés plutôt qu'un thème par marque.
- Modèle de **nommage de tokens** : `--<propriété>-ds-<composant>-<variante>-<intensité>-<état>` (ex. `--background-color-ds-button-primary-high-hover`). Verbeux mais totalement prévisible.
- Recette de **hero typographique** : famille display maison, interligne sous la taille de police, interlettrage franchement négatif, une seule couleur d'accent.
- Direction **3D verre / dispersion** pour de l'imagerie de marque abstraite (alternative à l'illustration dessinée).
- Référence de **système de thèmes montré comme argument produit** (`web-desktop-themes-1` → `4`).

## Mots-clés

kraken, kraken.com, payward, krak, kraken pro, kraken desktop, kraken wallet, kraken institutional, kraken bank, kraken cli, kraken vip, kraken prime, kraken otc, kraken 360, jesse powell, arjun sethi, dave ripley, crypto, cryptomonnaie, cryptocurrency, bitcoin, exchange, bourse crypto, trading, terminal de trading, trading terminal, order book, carnet d'ordres, candlestick, chandelier japonais, ladder trading, fintech, finance, banque, banking, paiement, payments, wallet, portefeuille, web3, blockchain, stablecoin, kraktag, carte bancaire, debit card, krak card, violet, purple, violet #7132f5, 7132f5, mauve, indigo, corail, coral, #ff3b29, ff3b29, rouge orangé, cyan, bleu électrique, #00adfe, sortir du bleu, anti-bleu, noir violacé, dark mode, thème sombre, light mode, thème clair, huit thèmes, multi-thème, multi-marque, design system, design tokens, tokens sémantiques, semantic tokens, nommage de tokens, token naming, palette, nuancier, swatch, couleur de marque, brand color, accent, ponctuation chromatique, gris bleuté, neutres teintés, rampe de couleur, color ramp, hausse baisse, positive negative, vert de hausse, rouge de baisse, kraken-brand, kraken-product, kraken-mono, typographie maison, custom typeface, police propriétaire, ibm plex, söhne, financier display, klim type foundry, kris sowersby, display serré, tight tracking, interlettrage négatif, negative letter-spacing, interligne serré, tight leading, échelle typographique, type scale, brand1, display, heading, body, caption, mono, chiffres tabulaires, éclats de verre, glass shards, verre irisé, iridescent glass, dispersion, chrome, 3d, rendu 3d, matière de marque, spot illustration, mascotte, symbole tentacule, tentacle, calmar, squid, octopus, poulpe, mythologie, sci-fi, rune fisker, agent pekka, bbh new york, illustration sci-fi, rebranding 2019, rebrand, refonte de marque, brand refresh, press kit, media kit, logo svg, logotype, lockup, icône d'app, app icon, duotone, jeu d'icônes, icon set, écosystème de marque, brand architecture, sous-marques, product suite, onboarding, kyc, vérification d'identité, app store, captures d'écran, screenshots, ui mobile, ui web, terminal, dashboard, tableau de bord, relevé de couleurs, comptage de pixels, écart charte production, brand vs production
