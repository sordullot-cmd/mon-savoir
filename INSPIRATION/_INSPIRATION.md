---
type: moc
tags: [moc, inspiration]
---

# Inspiration

> Tout ce qui nourrit l'œil et les idées. Rangé **par discipline**, retrouvé par **tags** et par MemPalace.

## Par discipline (catégories de base)
- `WEBDESIGN` — sites web, landing pages, portfolios *(captures via `/inspi`)*
- `UI-DESIGN` — interfaces, apps, design produit, composants. Les **dossiers de référence d'app** (écrans, flows, branding, couleurs) y vivent et sont indexés dans [[_APPS]] — créés par **`/inspi`** en mode app.
- `BRAND-DESIGN` — identités, logos, branding, chartes
- `GRAPHISME` — print, affiches, éditorial, illustration
- `MOTION` — motion design, transitions, showreels
- `COMPOSANTS` — **index transversal** des **blocs UI statiques** marquants ([[_COMPOSANTS]]). Les fichiers restent **dans le dossier de leur site** ; cette note ne fait que les référencer. *Sélectif, pas tout.*
- `ANIMATIONS` — **index transversal** des **sections / intros / micro-anims** (GIF / MP4) ([[_ANIMATIONS]]). Même principe : fichiers dans le dossier de leur site. *Sélectif.*
- `UNIVERS` — **dossiers de référence complets** sur un univers créatif (jeu vidéo, marque, studio, film…) : médias téléchargés en pleine qualité, rangés par aspect (branding, ui, character-design, illustrations, animations, gameplay…) ([[_UNIVERS]]). Transversal par nature (mélange les disciplines), créé par **`/univers`**.

> **Univers ou produit ?** *Un monde qu'on regarde* (jeu, film, studio, marque) → `UNIVERS/` via `/univers`. *Un produit numérique qu'on utilise* (app, SaaS, site) → sa discipline (`UI-DESIGN/`, `WEBDESIGN/`) via `/inspi`, qui produit le même dossier par aspect.

> **Besoin d'une autre discipline** (ex. `PACKAGING`, `3D`, `TYPOGRAPHIE`)? On peut **ajouter une catégorie** — cf. la règle de création de catégories dans `CLAUDE.md` (rester sobre, ne pas multiplier sans raison).

## Convention de tags
Dans le frontmatter (`media:`, `mood:`) ou en `#tag`.

**Média** : `image` `vidéo` `site` `article` `typo` `motion` `post` *(= post social : tweet, pin, reel…)*
**Discipline (tags)** : `#ui` `#ux` `#brand` `#motion` `#typo` `#3d` `#print` `#web` `#graphisme`
**Mood / style** : `#minimal` `#bold` `#editorial` `#brutalist` `#retro` `#organic` `#playful` `#luxe` `#dark`
**Usage** : `#a-tester` `#pour-sordulo` `#pour-ican` `#pour-unowhy`

## Descripteurs d'une inspi web (recherche fine)

> Vocabulaire **contrôlé** (comme pour les fonts) : ces champs en frontmatter rendent l'inspi cherchable par caractéristique précise (« site agence animé bleu », « e-commerce minimal à parallaxe »). Réutiliser l'existant, ne pas inventer de synonyme. Rempli automatiquement par `/inspi`. Voir [[Template-Inspiration]].

- `type_site` — nature du site : `portfolio` · `agence` · `studio` · `freelance` · `saas` · `produit` · `landing` · `e-commerce` · `marketplace` · `éditorial` · `magazine` · `événementiel` · `marque` · `food` · `immobilier` · `association` · `expérimental` · `showcase`
- `secteur` — domaine métier (libre, mais privilégier un terme existant) : `tech` · `mode` · `beauté` · `food` · `sport` · `culture` · `finance` · `santé` · `immobilier` · `musique` · `luxe` · `gaming` · `web3` …
- `couleur_principale` — couleur dominante, **nom + hex** (ex. `noir #0A0A0A`, `bleu électrique #1A3CFF`)
- `couleurs` — palette complète (`[#000, #fff, ...]`)
- `anime` — site animé ? `oui` · `non` · `léger`
- `animations` — types présents : `scroll-reveal` · `parallaxe` · `sticky-pin` · `loader` · `hover` · `curseur-custom` · `transitions-page` · `webgl-3d` · `video-bg` · `marquee` · `drag` · `morphing` · `text-anim` · `canvas`
- `layout` — structure : `grille` · `asymétrique` · `plein-écran` · `split` · `magazine` · `bento` · `centré`
- `mood` — ambiance : `minimal` · `bold` · `editorial` · `brutalist` · `retro` · `organic` · `playful` · `luxe` · `dark` …

> **Manque une valeur** (un `type_site` ou un type d'`animations` non listé) ? On peut l'**ajouter ici** — cf. règle de création de catégories dans `CLAUDE.md` (rester sobre, signaler l'ajout, ne pas multiplier).

## Descripteurs propres à une app (en plus des communs)

> Voir [[Template-Produit]]. Rempli par `/inspi` en mode app.

- `type_app` — `productivité` · `social` · `finance` · `santé` · `média` · `commerce` · `outil` · `jeu` · `ia`
- `plateformes` — `[ios, android, web, macos]`
- `editeur` · `version` · `url_store` — relevés automatiquement depuis le store
- `patterns` — écrans/parcours présents : `onboarding` · `paywall` · `tab-bar` · `navigation-gestuelle` · `feed` · `recherche` · `parametres` · `empty-state` · `mode-sombre`

## Inspirations site (dossier + captures)
Une inspi web = un **dossier** dans sa discipline contenant la **fiche + 1 screenshot par page** :
```
WEBDESIGN/<slug>/
├── <slug>.md         ← fiche (lien source + captures + mood/tags)
├── home.png          ← 1 capture pleine hauteur par page (1/template)
├── <page>.png …
├── walkthrough.mp4   ← vidéo de défilement de tout le site
├── composants/       ← blocs UI statiques réutilisables (référencés dans [[_COMPOSANTS]])
└── animations/       ← sections / intros / micro-anims en GIF/MP4 (référencées dans [[_ANIMATIONS]])
```
Créé par le skill **`/inspi`** (voir `CLAUDE.md`).

## Dossier de référence d'un produit (app, ou site en profondeur « dossier »)

Rangé par **aspect**, sur le modèle d'`UNIVERS/` mais dans la discipline du produit — indexé dans [[_APPS]] :
```
UI-DESIGN/<slug>/
├── <slug>.md      ← fiche [[Template-Produit]] : store + écrans + couleurs + crédits + sources
├── icone.png
├── ecrans/        ← écrans en résolution native (stores, bases d'UI, captures)
├── flows/         ← parcours numérotés (onboarding-01.png…) ou vidéos
├── branding/      ← logo, lockups, typo
├── couleurs/      ← nuanciers (palette.py)
├── composants/    ← blocs UI remarquables (→ [[_COMPOSANTS]])
├── animations/    ← transitions, micro-anims (→ [[_ANIMATIONS]])
└── marketing/     ← site du produit, landing, page store
```
Créé par **`/inspi`** en mode app (ou sur un site quand Sacha demande « le dossier complet »).

## Inspirations post social (dossier + média)

Un lien de **post** (X/Twitter, Instagram, Pinterest, TikTok, Behance, Dribbble, YouTube…) = un **dossier** dans la discipline de ce que le post **montre** (pas de la plateforme), contenant la **fiche + le(s) média(s) en pleine qualité**. Le slug décrit le contenu, **sans la plateforme** (elle est dans le frontmatter `plateforme:`) :
```
BRAND-DESIGN/bartolomeu-moveis/
├── <slug>.md      ← fiche (source + plateforme + auteur + média intégré + mood/tags)
├── post.jpg       ← média du post (post-2.jpg… si carrousel)
└── post.mp4       ← si vidéo
```
Descripteurs propres aux posts (frontmatter, voir [[Template-Inspiration-Post]]) : `plateforme` (`x` · `instagram` · `pinterest` · `tiktok` · `behance` · `dribbble` · `tumblr` · `bluesky` · `threads` · `youtube` · `vimeo`), `auteur` (handle/nom du compte), `sujet` (`ui` · `site` · `branding` · `logo` · `affiche` · `editorial` · `illustration` · `photo` · `typo` · `motion` · `3d`). Créé par **`/inspi`** (mode post social).

## Vues utiles (Dataview, optionnel)
- Inspis `#a-tester` non encore exploitées
- Inspis par discipline ou liées à un projet

---
[[ACCUEIL|← Accueil]]
