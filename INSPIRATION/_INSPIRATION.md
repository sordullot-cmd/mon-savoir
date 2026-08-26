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
- `secteur` — domaine métier (libre, mais privilégier un terme existant) : `tech` · `mode` · `beauté` · `food` · `sport` · `culture` · `éducation` · `finance` · `santé` · `immobilier` · `musique` · `luxe` · `gaming` · `web3` …
- `couleur_principale` — couleur dominante, **nom + hex** (ex. `noir #0A0A0A`, `bleu électrique #1A3CFF`)
- `couleurs` — palette complète (`[#000, #fff, ...]`)
- `anime` — site animé ? `oui` · `non` · `léger`
- `animations` — types présents : `scroll-reveal` · `parallaxe` · `sticky-pin` · `loader` · `hover` · `curseur-custom` · `transitions-page` · `webgl-3d` · `video-bg` · `marquee` · `drag` · `morphing` · `text-anim` · `canvas` · `sheet` · `celebration` *(récompense jouée, célébration de fin)* · `lip-sync` *(personnage animé synchronisé à la parole)*
- `layout` — structure : `grille` · `asymétrique` · `plein-écran` · `split` · `magazine` · `bento` · `centré`
- `mood` — ambiance : `minimal` · `bold` · `editorial` · `brutalist` · `retro` · `organic` · `playful` · `luxe` · `dark` …
- `typos` — polices **réellement rendues**, relevées automatiquement à la capture (pas devinées). Lier `[[la fiche font]]` si elle existe dans le vault, sinon la citer telle quelle.
- `date_capture` — date de la capture (`AAAA-MM-JJ`) : un site change, une inspi datée reste lisible des années après.

> **Manque une valeur** (un `type_site` ou un type d'`animations` non listé) ? On peut l'**ajouter ici** — cf. règle de création de catégories dans `CLAUDE.md` (rester sobre, signaler l'ajout, ne pas multiplier).

## Descripteurs propres à une app (en plus des communs)

> Voir [[Template-Produit]]. Rempli par `/inspi` en mode app.

- `type_app` — `productivité` · `social` · `finance` · `santé` · `éducation` · `média` · `commerce` · `outil` · `jeu` · `ia`
- `plateformes` — `[ios, android, web, macos, windows]`
- `editeur` · `version` · `url_store` — relevés automatiquement depuis le store
- `patterns` — écrans/parcours présents : `onboarding` · `paywall` · `tab-bar` · `navigation-gestuelle` · `feed` · `recherche` · `parametres` · `empty-state` · `mode-sombre` · `gamification`

## Une inspi = un dossier rangé par aspect (toujours)

**Il n'y a plus qu'une seule structure d'inspi**, quelle que soit la discipline et quel que
soit le point de départ (URL de site, nom d'app, lien de store, post social) : le dossier
par aspect ci-dessous, décrit en détail dans la section suivante. Un dossier plat de
captures, ou un dossier de deux fichiers parce que la cible était « juste un post », n'est
plus une sortie valide — cf. `.claude/skills/inspi/SKILL.md`, § Étape 2.

L'aspect **principal** dépend de la discipline : `ecrans/` pour `UI-DESIGN` et `WEBDESIGN`,
`visuels/` pour `GRAPHISME`, `branding/` pour `BRAND-DESIGN`, `animations/` pour `MOTION`.
Le reste du socle (`couleurs/`, `branding/`, `composants/`, `animations/`, `marketing/`,
`process/`, `archive/`) est commun.

En mode site, les captures pleine hauteur vont dans `ecrans/` et le `walkthrough.mp4` reste
à la racine du dossier. Créé par le skill **`/inspi`** (voir `CLAUDE.md`).

## La structure, en détail

Rangé par **aspect**, sur le modèle d'`UNIVERS/` mais dans la discipline de la cible —
indexé dans [[_APPS]] si la cible est un produit, dans [[_MOODBOARD]] si c'est un site de
référence :
```
<DISCIPLINE>/<slug>/
├── <slug>.md      ← fiche : une section par aspect + ## Sources + ## Crédits nominatifs
├── icone.png      ← si la cible a une icône d'app
├── walkthrough.mp4 ← mode site
├── ecrans/        ← ui-design, webdesign : écrans et captures en résolution native
│   └── planches/  ← une planche par famille — le seul embed de la fiche pour cette famille
├── visuels/       ← graphisme (à la place de ecrans/)
├── flows/         ← parcours numérotés (onboarding-01.png…) ou vidéos
├── branding/      ← logo, lockups, icône, fichiers de police récupérés
├── couleurs/      ← nuanciers (palette.py), nommés `palette-<sujet>.svg` : charte publiée et/ou relevé de pixels. Dans la fiche : embed préfixé du dossier, paragraphe en gras dessous, puis un tableau par groupe (cf. section « Palette » de [[duolingo]])
├── composants/    ← blocs remarquables, suffixés _<slug> (→ [[_COMPOSANTS]])
├── animations/    ← transitions, micro-anims, suffixées _<slug> (→ [[_ANIMATIONS]])
├── marketing/     ← site du produit, landing, page store, visuels sociaux, campagnes
├── process/       ← étapes de fabrication publiées par l'éditeur : diagnostic, explorations, directions écartées, avant/après. Rare et précieux (cf. [[duolingo-app]])
└── archive/       ← états antérieurs : refonte passée, ancienne UI, ancien site, millésimes datés
```
Sous-dossier **créé seulement s'il a du contenu** — aucun dossier vide. Un aspect qui
manque à cette liste peut être créé, en le signalant (règle de création de catégories dans
`CLAUDE.md`). Créé par **`/inspi`**, dans **tous** ses modes — c'est la seule structure
qu'il produit.

## Inspirations post social

Un lien de **post** (X/Twitter, Instagram, Pinterest, TikTok, Behance, Dribbble, YouTube…) = un **dossier par aspect** dans la discipline de ce que le post **montre** (pas de la plateforme). Le slug décrit le contenu, **sans la plateforme** (elle est dans le frontmatter `plateforme:`).
Le média du post trouve sa place **dans l'aspect qui correspond à ce qu'il montre**, comme
n'importe quel autre média du dossier ; un `post.jpg` à la racine n'est acceptable que si le
projet complet est resté introuvable, et le récap le dit. Le post n'est pas la cible, c'est
l'indice : l'agent « auteur » de la récolte remonte jusqu'au projet publié en entier
(Behance, portfolio du studio, press kit du client), et c'est lui qui remplit le dossier.

Descripteurs propres aux posts (frontmatter, voir [[Template-Inspiration-Post]]) : `plateforme` (`x` · `instagram` · `pinterest` · `tiktok` · `behance` · `dribbble` · `tumblr` · `bluesky` · `threads` · `youtube` · `vimeo`), `auteur` (handle/nom du compte), `sujet` (`ui` · `site` · `branding` · `logo` · `affiche` · `editorial` · `illustration` · `photo` · `typo` · `motion` · `3d`). Créé par **`/inspi`** (mode post social).

## Vues utiles (Dataview, optionnel)
- Inspis `#a-tester` non encore exploitées
- Inspis par discipline ou liées à un projet

---
[[ACCUEIL|← Accueil]]
