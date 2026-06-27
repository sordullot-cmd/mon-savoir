---
type: moc
tags: [moc, inspiration]
---

# Inspiration

> Tout ce qui nourrit l'œil et les idées. Rangé **par discipline**, retrouvé par **tags** et par MemPalace.

## Par discipline (catégories de base)
- `WEBDESIGN` — sites web, landing pages, portfolios *(captures via `/inspi`)*
- `UI-DESIGN` — interfaces, apps, design produit, composants
- `BRAND-DESIGN` — identités, logos, branding, chartes
- `GRAPHISME` — print, affiches, éditorial, illustration
- `MOTION` — motion design, transitions, showreels
- `COMPOSANTS` — **index transversal** des **blocs UI statiques** marquants ([[_COMPOSANTS]]). Les fichiers restent **dans le dossier de leur site** ; cette note ne fait que les référencer. *Sélectif, pas tout.*
- `ANIMATIONS` — **index transversal** des **sections / intros / micro-anims** (GIF / MP4) ([[_ANIMATIONS]]). Même principe : fichiers dans le dossier de leur site. *Sélectif.*

> **Besoin d'une autre discipline** (ex. `PACKAGING`, `3D`, `TYPOGRAPHIE`)? On peut **ajouter une catégorie** — cf. la règle de création de catégories dans `CLAUDE.md` (rester sobre, ne pas multiplier sans raison).

## Convention de tags
Dans le frontmatter (`media:`, `mood:`) ou en `#tag`.

**Média** : `image` `vidéo` `site` `article` `typo` `motion`
**Discipline (tags)** : `#ui` `#ux` `#brand` `#motion` `#typo` `#3d` `#print` `#web` `#graphisme`
**Mood / style** : `#minimal` `#bold` `#editorial` `#brutalist` `#retro` `#organic` `#playful` `#luxe`
**Usage** : `#a-tester` `#pour-sordulo` `#pour-ican` `#pour-unowhy`

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

## Vues utiles (Dataview, optionnel)
- Inspis `#a-tester` non encore exploitées
- Inspis par discipline ou liées à un projet

---
[[ACCUEIL|← Accueil]]
