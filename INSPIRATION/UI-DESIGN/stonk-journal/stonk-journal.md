---
type: inspiration
discipline: ui-design
media: app
source: https://stonkjournal.com
url_store:
editeur: Yevgeniy (Eugene) Vygodner, dba StonkJournal (Wisconsin, USA)
type_app: finance
plateformes: [web]
version: V2 (beta privée), landing Framer relevée le 2026-08-31
secteur: finance
couleur_principale: bleu #4B9EFF
couleurs: ["#20222D", "#18191F", "#282B37", "#4B9EFF", "#4FA5FF", "#51CA96", "#EB4B68", "#8A92A6"]
patterns: [mode-sombre, empty-state, parametres]
anime: oui
animations: [scroll-reveal, marquee, text-anim, hover]
layout: magazine
mood: [editorial, bold, brutalist, dark]
typos: [Archivo Black, Instrument Serif, JetBrains Mono, Inter]
date_capture: 2026-08-31
tags: [inspiration, ui, editorial]
---

# StonkJournal

> Le seul journal de trading du lot qui ait une voix. Là où tout le secteur empile des cartes arrondies sur du bleu nuit, celui-ci compose comme un journal papier : titres géants en grotesque noire, un mot en serif italique bleu, tout le reste en monospace, et un bandeau qui défile en promettant « no hot takes — just receipts ».

![icone](icone.png)

**Sources :** site officiel (Framer) · fichiers de police réellement servis · app V2 (`v2.stonkjournal.com`) · board Sleekplan (l'annonce de la V2) · Wayback Machine (la V1 WordPress) · Product Hunt

> **Lecture** : chaque famille d'écrans est montrée par **une planche** (`<aspect>/planches/`), légendée juste dessous. Les fichiers individuels restent dans leur dossier d'aspect.

## En bref

- **Quatre polices, quatre rôles nets, aucun recouvrement.** Archivo Black pour tous les titres, Instrument Serif **en italique seulement** pour un ou deux mots par titre, JetBrains Mono pour tout le reste, Inter en secondaire.
- **La police la plus utilisée du site est une monospace** — 783 éléments contre 255 pour la grotesque des titres. Corps de texte, labels, nav, boutons, chiffres : tout en mono.
- **Le dashboard du hero n'est pas une image.** C'est un composant de code Framer de 368 ko (`Dash_Mock.mjs`) qui rejoue l'app entière et ne se monte qu'à l'entrée dans le viewport. La landing ne contient **que trois images** au total.
- **Le pricing ne met pas une carte en avant : il inverse le contraste.** `FREE $0 forever` sur fond sombre, `PRO $10/month` en aplat bleu pleine hauteur.
- **Les sections sont numérotées comme un rapport** : `001 // INTRODUCTION FY26-Q2`, `002 // DASHBOARD`, `004 // PRICING // TWO PLANS`. Le produit se présente comme un document, pas comme une page de vente.
- **Un fondateur seul**, Yevgeniy Vygodner, entreprise individuelle au Wisconsin. Lancé en 2021, 200 000+ traders revendiqués, 10,8 M de trades journalisés.
- **PWA offline-first**, pas d'app native — et les badges de l'écran d'inscription le disent (`YOUR DATA · YOURS / NO ADS · EVER / PWA · OFFLINE`).
- **La V2 a été reconstruite depuis zéro** en mai 2026, annoncée publiquement, la V1 laissée en ligne en parallèle avec migration en un clic.

## Typographie

![[typographie/planches/planche-typo-geante.png]]

**C'est ici que tout se joue, et le réglage est chirurgical.** Le `h1` fait 115 px pour un interligne de 92 px — un ratio de **0,80**, donc les lignes se touchent presque — avec un letter-spacing de **-8,05 px** (≈ -0,07 em). Ce couple 0,80 / -0,07 em est **constant à toutes les tailles** : `h2` 60/48 px et -4,2 px, `h3` 30/24 px et -2,1 px. C'est la signature du site, et elle est purement mathématique.

Par-dessus, un seul geste : **un ou deux mots par titre passent en Instrument Serif italique bleu**, à la même taille que la grotesque qui les entoure — `people.`, `total clarity`, `compound your edge`, `fire`, `easier`, `answer`. Le romain de cette police n'est jamais chargé : elle ne sert qu'à ça.

Les trois fichiers réellement servis sont conservés dans `typographie/` :

- `ArchivoBlack-Regular-latin.woff2` — **Archivo Black**, Héctor Gatti et l'équipe Omnibus-Type (fonderie Omnibus-Type, Argentine), SIL OFL. Tous les titres, `font-weight: 400`, casse déjà capitale dans le texte source.
- `InstrumentSerif-Italic-latin.woff2` — **Instrument Serif** italique, Rodrigo Fuenzalida, direction Jordan Egstad / JD Hooge / Jack De Caluwé pour le studio Instrument (Portland), SIL OFL.
- `JetBrainsMono-Regular-latin.woff2` — **JetBrains Mono**, Philipp Nurullin et Konstantin Bulenkov (JetBrains), OFL, distribué ici via Fontshare.

**Inter** (Rasmus Andersson) complète en secondaire, 252 éléments. **Fragment Mono** (Wei Huang) est déclarée en `@font-face` mais rendue sur zéro élément : un reliquat.

Aucune de ces polices n'a de fiche dans le vault — quatre candidates à `/font`, et Archivo Black en priorité.

## Écrans

![[ecrans/planches/planche-ecrans.png]]

**Le produit se montre en se jouant.** Le `Dash_Mock` de la landing est l'app V2 en fonctionnement : sidebar Dashboard / Stats / Calendar / AI Coach / Import / Settings, barre de P&L, equity curve, et une table de trades dense avec badges `WIN` / `LOSS` / `OPEN` et pastilles de marché `STK` / `OPT` / `FUT` / `FX` / `CRY`. Un bouton `Migrate from V1` traîne dans l'interface — la V1 tourne encore.

- `ecrans/app-v2-dashboard.png` — le dashboard V2, capturé après scroll (le composant ne se monte qu'en viewport).

## Flows

![[flows/planches/planche-auth.png]]

**L'écran d'inscription applique le système typographique à un formulaire, et ça marche.** Split-screen : à gauche `LOG IN. LOG A TRADE. see the truth.` — même duo Archivo Black / Instrument Serif italique — avec un aperçu de stats ; à droite le formulaire, plus les badges `Private beta · limited spots`, `Looking for V1?` et le triptyque `YOUR DATA · YOURS / NO ADS · EVER / PWA · OFFLINE`. Une page de connexion qui continue de vendre sans mentir.

- `flows/app-v2-ecran-inscription.png` · `flows/app-v2-ecran-connexion.png`

## Composants

![[composants/planches/planche-composants.png]]

**Trois composants, trois idées empruntables telles quelles.**

- `composants/ticker-defilant_stonk-journal.png` — le bandeau bleu en aplat, en monospace : `FOR THE PEOPLE --- NO ADS --- NO DATA SOLD --- NOT FINANCIAL ADVICE --- EST. 2021 --- 10.8M TRADES LOGGED --- NO HOT TAKES --- JUST RECEIPTS`. Le marquee sert de manifeste, pas de décoration.
- `composants/liste-numerotee_stonk-journal.png` — le système de lignes 01 → 07 : numéro bleu en mono à gauche, titre Archivo Black avec son mot en serif italique, puces en mono, et **à droite le vrai composant produit** (stat cards, heatmap de calendrier, sparklines de règles, liste de comptes). Chaque argument est prouvé par son écran.
- `composants/pricing-inversion-de-contraste_stonk-journal.png` — le pricing par inversion : sombre contre aplat bleu pleine hauteur. Aucune étiquette « recommandé », aucun badge, aucune ombre. Le contraste fait le travail.

## Couleurs

![[couleurs/palette-site.svg]]

**Les fonds ne sont pas des noirs mais des gris bleutés** — `#20222D`, `#18191F`, `#282B37` — ce qui est rare dans un secteur qui tire tout vers le noir pur. Et le bleu existe en **trois valeurs à un point d'écart** selon l'usage : `#4B9EFF` pour la typo et les liens, `#4A9EFF` pour l'aplat du bloc PRO, `#4FA5FF` pour le ticker. Personne ne verra la différence, mais elle est là — signe que les aplats et le texte ont été réglés séparément.

**Fonds**

| Nom de rôle | Hex | Usage |
| --- | --- | --- |
| fond principal | `#20222D` | gris-bleu, aussi le fond de l'app en sombre |
| fond alterné et footer | `#18191F` | |
| panneau élevé | `#282B37` | cartes |
| surface | `#242733` | |
| bordure et séparateur | `#2D313D` | |
| voile | `#21232E` | servi aussi à 54 % (`#21232E8A`) |

**Textes et bleu**

| Nom de rôle | Hex | Usage |
| --- | --- | --- |
| texte principal | `#FFFFFF` | les titres géants |
| texte tertiaire | `#E0E0E0` | |
| texte secondaire | `#8A92A6` | gris bleuté, tout le corps de texte |
| accent typo et liens | `#4B9EFF` | les mots en Instrument Serif italique |
| aplat du bloc PRO | `#4A9EFF` | pricing |
| aplat du ticker | `#4FA5FF` | bandeau défilant |
| bloc unique du logo | `#3C9AEF` | la seule case bleue du monogramme |

**Sémantique** : gain `#51CA96` · perte `#EB4B68` · alerte `#EAB308`.

![[couleurs/palette-app-v2.svg]]

**Les deux thèmes de l'app sont lisibles sans compte, parce que le mock de la landing embarque sa feuille de style.** Le thème clair part d'un blanc **cassé chaud** (`#FDFDFC`) et non d'un blanc pur, et seuls les quatre accents changent entre les thèmes — les structures, elles, se contentent de basculer. Une rampe primaire complète de onze valeurs est déclarée (`50` → `950`), ce qui indique un vrai système de composants derrière (Nuxt UI v3).

| Rôle | Clair | Sombre |
| --- | --- | --- |
| `--bg-main` | `#FDFDFC` | `#20222D` |
| `--bg-panel` / `--bg-input` | `#F3F3F2` | `#2A2D39` |
| `--border` | `#E1E5EA` | `#2D313D` |
| `--text-main` | `#232323` | `#C8CDD9` |
| `--text-strong` | `#0A0A0A` | `#FFFFFF` |
| `--accent-blue` | `#3C9AEF` | `#4FA5FF` |
| `--accent-green` | `#22B077` | `#52CA96` |
| `--accent-red` | `#E23B56` | `#EB4B68` |
| `--accent-yellow` | `#CA8A04` | `#EAB308` |

Rampe primaire : `#EEF6FF` · `#D9EBFF` · `#BCDDFF` · `#8EC8FF` · `#59A9FF` · **`#3C9AEF`** · `#2176D2` · `#1A5FB0` · `#1B5090` · `#1C4576` · `#152B49`. Rayon : `--ui-radius: .425rem`.

## Branding

![[branding/logo-monogramme-blocs-pixel.svg|200]]

**Un `S` construit en blocs carrés, dont un seul est bleu.** Le monogramme est en pixel art assumé — cohérent avec le monospace omniprésent et avec le nom (« stonk », le mème). L'unique bloc `#3C9AEF` au milieu du blanc suffit à créer un point de marque, sans dégradé ni effet.

- `branding/icone-app-180px.png` — l'apple-touch-icon, seule taille servie.
- Aucun press kit : ces deux fichiers plus la carte OG sont tout ce qui existe.

## Process

![[process/planches/planche-annonce-v2.png]]

**L'éditeur a annoncé publiquement qu'il jetait tout et recommençait, et il a expliqué pourquoi.** Le billet du 18 mai 2026 sur le board Sleekplan, signé Yevgeniy, dit la décision : reconstruire la V2 depuis zéro plutôt que d'étendre la V1, garder la V1 en ligne en parallèle, offrir une migration en un clic, ouvrir la beta sur invitation. Deux previews étaient joints — c'est de la matière de process rare dans ce secteur, où personne ne raconte rien.

- `process/annonce-v2-changelog-mai-2026.png` — le billet complet.
- `process/preview-v2-dashboard-annonce-mai-2026.jpg` — la preview du dashboard, en mai 2026.
- `process/preview-v2-panneau-detail-trade-annonce-mai-2026.jpg` — la preview du panneau latéral de détail d'un trade (TSLA) : Details / Risk-Reward / mini-chandelier / Executions / Journal.

## Archive

`archive/v1-2023-stats.jpg` — **l'avant, et il fait mal.** La page Stats de la V1 (asset WordPress de 2023, encore servi en janvier 2025) : cartes arrondies gris-bleu, sans-serif système, accent bleu en filet, zéro personnalité typographique. Exactement le SaaS sombre générique dont la V2 s'échappe. À regarder juste après le hero actuel — c'est le meilleur argument du dossier sur ce qu'une direction typographique change.

## Marketing

![[marketing/planches/planche-pages.png]]

**Le gabarit tient sur les pages SEO, et c'est là qu'on voit si un système est solide.** Les pages `/features/*`, `/markets/*`, `/methodology`, `/integrations` reprennent le même duo typographique et la même numérotation sur des contenus longs, sans s'effondrer. Seule `/integrations` laisse Inter passer devant la monospace.

- `marketing/landing.png` et `landing-mobile.png` — la landing pleine hauteur (8 762 px en desktop, 40 779 px en mobile : la typo géante se recasse en colonne).
- `marketing/og-card.jpg` — la carte sociale : lockup, baseline `TRADING JOURNAL FOR THE people.`, collage d'écrans en perspective.
- `marketing/blog.png` — l'index du blog, neuf articles de mai à août 2026, très orientés comparatifs (vs Tradervue, TradeSync, TradeZella).

Prix : **Free 0 $ « forever »**, sans carte, sans limite de trades · **Pro 10 $/mois** (import CSV intelligent, AI Coach, AI Chat, multi-comptes agrégé). Positionnement : « No ads. No data sold. »

Ton de voix, à citer tel quel : « No astrology. Just receipts. » · « Numbers don't care about your feelings, and neither do we. » · footer « Built by traders who lost money first. »

## Pourquoi je l'aime

Parce que c'est le seul du lot qui ait choisi **une voix plutôt qu'une interface**. Techniquement, le produit fait la même chose que les quatre autres. Mais il a décidé que son sujet était éditorial — un journal, au sens du papier — et il en a tiré toutes les conséquences : une grotesque noire, une serif italique pour l'inflexion, une monospace pour les faits, des sections numérotées comme un rapport trimestriel, un bandeau-manifeste. Le pricing par inversion de contraste et le mock jouable en guise de capture d'écran achèvent de montrer que la contrainte a été tenue jusqu'au bout.

Et la comparaison avec sa propre V1 de 2023 est la meilleure démonstration qu'on puisse offrir à un client qui doute qu'une typographie change quelque chose.

## À réutiliser pour

- **Le réglage typographique** : interligne 0,80 et tracking -0,07 em, constants à toutes les tailles. C'est copiable directement.
- **Le duo grotesque + serif italique** : un ou deux mots par titre, même corps, une couleur d'accent. Le geste le plus rentable du dossier.
- **Une monospace comme police de corps** : elle donne un ton de relevé, de preuve, de reçu — exactement ce que promet le produit.
- **Un pricing par inversion de contraste**, sans badge « recommandé ».
- **Un marquee qui dit quelque chose** au lieu de faire défiler des logos.
- **Numéroter les sections d'une landing** comme un document daté (`001 //`, `002 //`).
- **Une page d'authentification qui garde la DA** au lieu de retomber dans le formulaire neutre.

## Limites de la récolte

- **Wayback Machine très dégradée** pendant le run : impossible de **rendre** les états antérieurs de la landing (2021, 2023, 2025). Une seule image de la V1 récupérée sur dix identifiées. Les neuf autres sont connues et à reprendre : `SJ_screenshot_V5.jpg`, `Chart_V2.jpg`, `Edit_Trade_V2_1.jpg`, `Edit_Journal_V2.jpg`, `Accounts-1.jpg`, `trade_setup.jpg`, `Settings.jpg`, `OpenGraph_thumb.jpg`, `logo_text_white.png` (tous sous `web.archive.org/web/20250126122155im_/https://stonkjournal.com/wp-content/uploads/2023/08/`).
- **Le compte X `@StonkJournal`** a publié un fil d'annonce de la V2 en avril-mai 2026, repéré en recherche mais **non ouvert** (X inaccessible depuis cette machine). Source de process potentiellement riche, à faire à la main.
- **Aucune galerie de design ne référence la landing** — Land-book, Godly, SiteInspire, One Page Love, Httpster, Awwwards, Minimal Gallery, Refero, Webframe : zéro occurrence. Ce qui est étonnant vu la qualité de la DA, et explique qu'aucun studio ne soit crédité par un curateur.
- **Le board Sleekplan** n'a été parcouru que sur son billet principal ; les onglets Updates / Feedback / Roadmap restent à explorer.
- **Aucune vidéo** : rien sur YouTube, aucun fichier média servi par le site (les animations sont en CSS / Framer Motion). L'aspect `animations/` **est vide** — les mouvements du site n'ont pas été enregistrés.
- **Crunchbase en 403** : date de création et financement non vérifiés par cette voie.
- L'app « Stonk » de l'App Store (`id1558279818`) est **un autre produit**, sans lien.

## Sources

- **Site officiel** — <https://stonkjournal.com> (Framer, `generator: Framer 77cb752`) : la landing, les pages features et markets, le mock jouable du dashboard, les recadrages de composants.
- **App V2** — <https://v2.stonkjournal.com/signup> et `/login` : les deux écrans d'authentification, et la feuille de style de l'app (Nuxt + Nuxt UI v3).
- **Fichiers de police servis** : `fonts.gstatic.com` (Archivo Black, Instrument Serif italique) et `framerusercontent.com` via Fontshare (JetBrains Mono). Conservés dans `typographie/`.
- **Board Sleekplan** — <https://stonkjournal.sleekplan.app/changelog/55260> : l'annonce de la V2 du 18 mai 2026 et ses deux previews.
- **Wayback Machine** — snapshot du 2025-01-26 : la V1 WordPress (2023).
- **Product Hunt** — lancement 2021, 77 points, 4,9/5 sur 8 avis, fondateur `@donkeysticks`.
- Captures de pages : faites maison le 2026-08-31 (`capture-site.py`).

## Crédits

- **Yevgeniy « Eugene » Vygodner** — fondateur et CEO, seul opérateur. Entreprise individuelle « Yevgeniy Vygodner, doing business as StonkJournal », Wisconsin (USA). Product Hunt : `@donkeysticks` · X : <https://x.com/StonkJournal> · contact `info@stonkjournal.com`.
- **Aucun studio ni designer externe crédité** — vérifié sur toutes les galeries de design accessibles et sur le site. La direction artistique est vraisemblablement de la main du fondateur, mais ce n'est pas documenté.
- **Archivo Black** — Héctor Gatti et l'équipe Omnibus-Type, fonderie **Omnibus-Type** (Argentine), SIL OFL.
- **Instrument Serif** — Rodrigo Fuenzalida, direction Jordan Egstad / JD Hooge / Jack De Caluwé, pour le studio **Instrument** (Portland), SIL OFL.
- **JetBrains Mono** — Philipp Nurullin et Konstantin Bulenkov (**JetBrains**), OFL, servi via **Fontshare**.
- **Inter** — Rasmus Andersson.
- Pile : landing sous **Framer**, app en **Nuxt** + **Nuxt UI v3**.

## Mots-clés

journal de trading, trading journal, éditorial, editorial design, brutalisme, typographie géante, big type, Archivo Black, Omnibus-Type, Instrument Serif, studio Instrument, italique d'accent, JetBrains Mono, monospace comme corps de texte, interligne serré, tracking négatif, letter-spacing -0.07em, ratio 0.80, sections numérotées, 001 002 003, marquee, bandeau défilant, manifeste, ticker, pricing par inversion de contraste, aplat pleine hauteur, pixel art, monogramme en blocs, gris bleuté, PWA, offline first, Framer, code component, Dash_Mock, Nuxt, Nuxt UI, rampe primaire, badges WIN LOSS OPEN, STK OPT FUT FX CRY, AI Coach, AI Chat, import CSV, V1 vers V2, refonte totale, changelog public, Sleekplan, no ads no data sold, just receipts, solo founder, Wisconsin

## À voir aussi

- [[traders-second-brain]] — l'autre extrême du même secteur : tout dans le système, rien dans la voix.
- [[tradetrack]] — la rigueur du système sans le geste typographique.
- [[ultratrader]] — la cohérence multi-plateformes, DA beaucoup plus consensuelle.
- [[_APPS]] · [[_COMPOSANTS]]
