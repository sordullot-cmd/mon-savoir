---
type: inspiration
discipline: ui-design
media: app
source: https://streaks.app
url_store: https://apps.apple.com/fr/app/streaks/id963034692
editeur: Crunchy Bagel Pty Ltd
type_app: santé
plateformes: [ios, macos]
version: 11.3.9 — mise à jour le 2026-08-19 (sortie 2015-06-01)
secteur: santé
couleur_principale: vert pomme #78B01D
couleurs: ["#78B01D", "#FF704C", "#FDFF6F", "#37B8D4", "#F9A7CD", "#FA114F", "#FFFFFF", "#000000"]
patterns: [parametres, gamification]
anime:
animations:
layout: grille
mood: [bold, playful]
typos: Roboto Condensed (relevée sur streaks.app — le site, pas l'app)
date_capture: 2026-08-27
tags: [inspiration, ui, habitudes, bold, playful]
---

# Streaks

> Suivi d'habitudes primé (Apple Design Award), payant, une couleur par écran. Dossier court : **la DA globale seulement** — écrans de store, couleurs relevées, rien de plus.

![[icone.png|120]]

## En bref
- **Un écran = une couleur, en dégradé plein cadre.** Vert pomme, corail, jaune acide, cyan, rose, framboise : chaque écran de l'app baigne dans un dégradé qui va d'un bord à l'autre, sans bandeau, sans carte, sans fond neutre.
- Résultat mesurable : **aucune couleur ne domine** le relevé. Le blanc arrive premier à 9,54 %, suivi de six teintes entre 5 % et 1 %. C'est le seul dossier de ce lot où la palette est **plate** — c'est précisément le système.
- Le **blanc est le seul encreur** : pictos, texte, filets, tout est blanc sur la couleur. Aucune nuance intermédiaire, aucun gris.
- La grille de tâches est faite de **cercles à picto monochrome** + un libellé en capitales condensées dessous. Le picto est un pictogramme de sport ou d'hygiène, jamais une icône d'interface.
- Le dégradé n'est pas décoratif : il **encode la progression** (l'anneau autour du picto se remplit dans la même famille de couleur).
- **Payant, 6,99 €**, sans version gratuite — la seule app payante du lot avec Things 3. Ça change la DA : rien à vendre dans les écrans, donc pas de paywall, pas de bandeau promo.
- Les trois derniers visuels sortent de l'app : **widgets d'écran d'accueil** et **Live Activity** d'écran verrouillé, sur fond noir et fond d'écran iOS.

## DA globale

Une DA qui remplace l'interface par la couleur. Il n'y a pas de chrome : pas de barre
d'onglets visible, pas de carte, pas d'élévation — juste un dégradé saturé bord à bord et
du blanc dessus. Ça marche parce que la contrainte est totale (un seul encreur, un seul
niveau de surface) et parce que les pictos sont dessinés au même poids partout. C'est le
contre-pied exact d'Amie : là où Amie travaille des écarts d'un cran, Streaks travaille
en pleine saturation et supprime tous les crans intermédiaires.

## Écrans

![[ecrans/planches/planche-ecrans-de-store.png]]

**Dix écrans, dix ambiances chromatiques, une seule grammaire.** Grille de tâches en
dégradé violet-magenta, statistiques sur blanc (le seul écran clair, où la couleur passe
dans les courbes), note du jour en rose, ajout de tâche en vert, confirmation en corail,
notifications en jaune acide, partage en cyan — puis les widgets et la Live Activity.
Le passage au blanc de l'écran de statistiques est le seul écart, et il est logique :
c'est le seul écran où la couleur doit rester lisible **en tant que donnée**.

## Couleurs

![[couleurs/palette-relevee-dans-les-ecrans.svg]]

**Une palette délibérément plate** — six teintes entre 5,2 % et 0,4 %, aucune dominante.
La marque n'a pas de couleur : elle a un système où chaque écran prend la sienne. Le seul
constant du relevé, c'est le blanc (9,54 %), qui sert d'encre sur tout.

**Les fonds pleine page (un par écran)**

| Nom de rôle | Hex | Part | Usage |
| --- | --- | --- | --- |
| Vert pomme | `#78B01D` | 5,23 % | ajout de tâche |
| Corail | `#FF704C` | 5,12 % | confirmation de tâche |
| Jaune acide | `#FDFF6F` | 4,86 % | notifications |
| Cyan | `#37B8D4` | 1,16 % | tâche partagée |
| Rouge framboise | `#FA114F` | 0,79 % | statistiques (courbes) |
| Rose | `#F9A7CD` | 0,40 % | note du jour |

**Les seconds tons du dégradé**

| Nom de rôle | Hex | Part | Usage |
| --- | --- | --- | --- |
| Vert clair | `#85C420` | 2,74 % | second cran du vert |
| Jaune-olive | `#E4E664` | 3,73 % | second cran du jaune |
| Corail foncé | `#E66544` | 2,45 % | second cran du corail |

**Neutres**

| Nom de rôle | Hex | Part | Usage |
| --- | --- | --- | --- |
| Blanc | `#FFFFFF` | 9,54 % | pictos, texte, filets — le seul encreur |
| Noir | `#000000` | 0,58 % | fond des widgets |

## Branding

L'icône (`icone.png`) est un anneau de progression. Aucun press kit publié.
`streaks.app` charge **Roboto Condensed** depuis Google Fonts — c'est la typo du **site**,
pas nécessairement celle de l'app, et la fiche ne prétend pas l'inverse.

## Sources
- **App Store (FR)** — les 10 écrans en résolution native + les métadonnées d'éditeur : [apps.apple.com/…/id963034692](https://apps.apple.com/fr/app/streaks/id963034692)
- **`streaks.app`** — la police chargée par le site (Roboto Condensed via Google Fonts).
- **Google Play** — sans objet : Streaks n'existe pas sur Android.

## Crédits
- **Crunchy Bagel Pty Ltd** — éditeur, Australie. Studio indépendant.
- Aucun designer nommé publiquement sur ce dossier court.

## Limites de ce dossier
Dossier volontairement court (demande : la DA globale seulement). Pas de récolte
multi-sources, pas de flows, pas de composants découpés, pas de relevé d'animation.
**Premier essai de récolte erroné** : la recherche par nom « Streaks habit » a renvoyé une
autre app (*Habit Tracker* de Inner Grow Limited) — corrigé en repartant de l'URL de store
directe. La typo de l'app elle-même reste non relevée.

## Limite du modèle
Une DA sans couleur de marque est difficile à décliner hors de l'app : rien ici ne peut
servir de bandeau, de landing ou de packaging sans choisir arbitrairement une des six teintes.

## Mots-clés
habitudes, habit tracker, série, streak, routine, santé, dégradé plein cadre, full-bleed gradient, saturé, vert pomme, corail, jaune acide, cyan, framboise, picto monochrome, cercle, anneau de progression, capitales condensées, condensed caps, Roboto Condensed, widget iOS, Live Activity, écran verrouillé, Apple Design Award, app payante, sans chrome

---
[[_APPS|← Apps]] · [[_INSPIRATION|← Inspiration]]
