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
- `GRAPHISME` — print, affiches, éditorial, illustration. Indexé dans [[_GRAPHISME]]. Aspect principal `visuels/` au lieu de `ecrans/`.
- `MOTION` — motion design, transitions, showreels
- `COMPOSANTS` — **index transversal** des **blocs UI statiques** marquants ([[_COMPOSANTS]]). Les fichiers restent **dans le dossier de leur site** ; cette note ne fait que les référencer. *Sélectif, pas tout.*
- `ANIMATIONS` — **index transversal** des **sections / intros / micro-anims** (GIF / MP4) ([[_ANIMATIONS]]). Même principe : fichiers dans le dossier de leur site. *Sélectif.*
- `UNIVERS` — **dossiers de référence complets** sur un univers créatif (jeu vidéo, marque, studio, film…) : médias téléchargés en pleine qualité, rangés par aspect (branding, ui, character-design, illustrations, animations, gameplay…) ([[_UNIVERS]]). Transversal par nature (mélange les disciplines), créé par **`/univers`**.

> **Une cible peut aussi être un thème** (« des animaux stylisés et humanisés »), ni produit ni univers :
> même dossier par aspect, dans la discipline du thème, `visuels/` rangé par **familles de style**
> plutôt que par source — cf. [[animaux-humanises]] (septembre 2026).

> **Univers ou produit ?** *Un monde qu'on regarde* (jeu, film, studio, marque) → `UNIVERS/` via `/univers`. *Un produit numérique qu'on utilise* (app, SaaS, site) → sa discipline (`UI-DESIGN/`, `WEBDESIGN/`) via `/inspi`, qui produit le même dossier par aspect.

> **Besoin d'une autre discipline** (ex. `PACKAGING`, `3D`, `TYPOGRAPHIE`)? On peut **ajouter une catégorie** — cf. la règle de création de catégories dans `CLAUDE.md` (rester sobre, ne pas multiplier sans raison).

## Convention de tags

> **Vocabulaire contrôlé, à facettes.** `tags:` était une liste libre où cinq natures
> d'information se mélangeaient à plat — la structure (`inspiration`), la discipline (`ui`),
> le domaine (`finance`), le style (`dark`), le procédé (`gamification`) — plus du workflow
> perso (`a-tester`). Deux boutons pour la même chose dès qu'un accent manquait, des tags
> portés par tout le monde qui ne triaient rien, et sept journaux de trading repérables
> seulement par leur `dark`. Chaque tag appartient maintenant à **une** facette, et deux
> facettes sur quatre se déduisent du frontmatter déjà rempli.

| Facette | La question | Où l'écrire |
| --- | --- | --- |
| **domaine** | de quoi ça parle | **rien à écrire** — déduit de `type_app` / `categorie` / `secteur` |
| **sujet** | ce que le produit fait | dans `tags:`, 1 à 3 |
| **procédé** | le parti pris de design qu'on vient étudier | dans `tags:`, 0 à 4 |
| **style** | à quoi ça ressemble | **rien à écrire** — déduit de `mood:` |

**Domaine** : `finance` `santé` `productivité` `éducation` `social` `média` `commerce` `jeu` `outil` `tech`
**Sujet** : `trading` `journal` `playbook` `crypto` `banque` `budget` `habitudes` `nutrition` `méditation` `émotions` `langues` `agenda` `temps` `apprentissage` `ia`
**Procédé** : `gamification` `mascotte` `illustration` `isométrique` `3d` `motion` `data-viz` `design-system` `typo-maison` `refonte` `onboarding` `paywall`
**Style** : `minimal` `bold` `dark` `playful` `editorial` `organic` `brutalist` `retro` `luxe`

Donc, concrètement : une fiche n'écrit que **le sujet et le procédé**. Écrire un domaine ou
un style à la main ne sert qu'à corriger une déduction fausse — l'univers Duolingo est classé
`secteur: tech` mais c'est de l'`éducation` qu'on vient y chercher, alors il l'écrit.

Un tag hors vocabulaire est **écarté** de l'index du site (pas d'erreur, pas de doublon :
il disparaît, et l'oubli se voit). Les variantes sans accent (`sante`, `productivite`,
`isometrique`) sont repliées sur la forme canonique. Le vocabulaire vit dans
`vault-gallery/scripts/tags-projets.mjs` — **un terme manque ? on l'y ajoute**, plutôt que
d'inventer un synonyme dans une fiche (même règle que pour les `type_site` ci-dessous).

**Média** (frontmatter `media:`, pas un tag) : `image` `vidéo` `site` `article` `typo` `motion` `post` *(= post social : tweet, pin, reel…)*
**Usage** : `#a-tester` `#pour-sordulo` `#pour-ican` `#pour-unowhy` — dans le **corps** de la
note, pas dans `tags:`. Ce sont des marques de travail personnel : elles restent cherchables
dans Obsidian et sur `/tags`, et n'encombrent plus l'index public des projets.

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
- `plateformes` — `[ios, ipados, android, web, macos, windows, visionos]` *(`ipados` et `visionos` ajoutés en sept. 2026 : une app Apple peut être livrée sur quatre surfaces déclarées et n'en dessiner que trois — cf. [[tradingplan]])*
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
├── process/       ← étapes de fabrication publiées par l'éditeur : diagnostic, explorations, directions écartées, avant/après. Rare et précieux (cf. [[duolingo]])
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
