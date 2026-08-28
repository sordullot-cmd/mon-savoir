---
type: inspiration
discipline: ui-design
media: app
source: https://amie.so
url_store: https://apps.apple.com/fr/app/amie-todos-calendar/id1548277133
editeur: Amie GmbH — Berlin (fondateur Dennis Müller)
type_app: productivité
plateformes: [ios, web, macos, windows]
version: 1.15.20 — mise à jour le 2025-08-06 (première sortie iOS 2023-12-12)
secteur: tech
couleur_principale: gris très clair #FAFAFA
couleurs: ["#FAFAFA", "#FFFFFF", "#F5F5F5", "#EBEBEB", "#000000", "#171717", "#F6A6A6", "#FFB4B4", "#0389FF", "#11A8FF", "#CFEEFF"]
anime: oui
animations: [scroll-reveal, sticky-pin, marquee, text-anim, drag, sheet]
layout: centré
mood: [minimal, editorial, playful]
typos: [Inter, Averia Serif Libre, Caveat, Universal Sans]
patterns: [onboarding, paywall, tab-bar, recherche, parametres, empty-state, mode-sombre]
date_capture: 2026-08-28
tags: [inspiration, ui, productivité, minimal, ia]
---

# Amie

> Calendrier, todos et e-mails dans une seule timeline — devenu en 2025 un **preneur de notes de réunion par IA**. Dossier complet : six ans de DA, de la landing rose de 2020 au virage agents de 2026, avec le récit de fabrication publié par le fondateur lui-même.

![[icone.png|120]]

## En bref

- **Le rose `#F6A6A6` est toujours là, mais on ne le voit plus.** C'était la couleur d'Amie de 2020 à 2023 : fond de landing, wordmark, icône iOS. Le rebrand de janvier 2024 l'a remplacé par un ciel bleu photographique. Et pourtant le token CSS du site de 2026 s'appelle encore `--color-amie-pink: #f6a6a6`. Une marque garde ses fantômes dans son code.
- **Cinq générations visuelles en six ans**, toutes datables au fichier près : wordmark rose sur liste d'attente (2020) → beta sombre sur dégradés ambrés (mars 2022) → beta claire à pastels saturés (fin 2022) → relance « ciel bleu » (janvier 2024) → AI Note Taker (avril 2025). C'est un des rares produits où l'on peut suivre chaque bascule à la source.
- **Le symbole n'est pas né comme un logo, il est né comme une icône d'app.** Jusqu'en 2023, Amie n'a qu'un wordmark. Le quadrilobe blanc gonflé apparaît en décembre 2023 dans un fichier qu'Apple nomme littéralement `app-icon-pink`, puis prend la place du wordmark un mois plus tard.
- **Le nom de code du produit était « Coco ».** Le croquis fondateur du logo est un lettrage dessiné au doigt par-dessus la photo d'une noix de coco ouverte. Le quadrilobe en descend directement.
- **La palette rose vient d'une story Instagram**, un nuancier Pantone 16-1513 Blossom photographié avec un packaging Boy Smells, légendé « How could you not love this palette? ». Amie publie sa propre source d'inspiration couleur.
- **Le site et l'app ne codent pas le noir pareil.** Le site de 2026 titre en `#000000` pur ; les écrans de l'app s'arrêtent à `#171717`. Deux équipes, deux réflexes, une seule marque.
- **La signature de marque est une phrase animée** : « Designed by the beach », en pied de page, dont le texte est rempli par un motif de vague SVG qui défile en boucle de 1,5 s. Elle dit vrai — Amie a été conçue dans un cottage en bord de mer au Cap.
- **L'ancienne landing est toujours en ligne, rangée sous `/art`.** Amie l'a conservée telle quelle parce qu'elle ne convertissait pas : un millésime de webdesign archivé par la marque elle-même, et assumé comme une pièce d'exposition.

## DA globale

Une DA de vitrine Apple poussée à l'extrême de la retenue : gris très clair, blanc, quasi-noir,
et la couleur uniquement comme **donnée**. Tout le travail tient dans des **écarts d'un cran** —
un fond à peine plus sombre que la carte posée dessus, un noir à peine moins noir que le noir,
une ombre à peine visible doublée d'un filet de 1 px. Rien ne crie, et pourtant chaque plan se
détache.

Ce qui empêche l'ensemble d'être froid, ce sont les **irruptions manuscrites** : une flèche
tracée à la main qui pointe une réduction, une annotation au crayon posée sur une capture, un
surligneur bleu pâle passé sur trois mots. Le système est rigoureux, les commentaires sont
écrits à la main. C'est la signature d'Amie, et elle traverse les cinq générations.

Le prix à payer reste le même depuis 2024 : **sorti du symbole, rien dans ces écrans ne dit
« Amie » plutôt qu'une autre app bien dessinée**. La marque a échangé son rose contre une
neutralité irréprochable.

## Écrans

### Les visuels de store

![[ecrans/planches/planche-ecrans-de-store.png]]

**Cinq visuels, quatre en composition sage et un qui casse tout.** Split view, listes, comptes
multiples et intégrations posent leurs cartes en pile verticale centrée ; le visuel des widgets
les jette en désordre avec des rotations et des mentions manuscrites au crayon. Chaque visuel
porte un **label coloré en surtitre** au-dessus d'une phrase noire — orange pour Split View,
violet pour Widgets, vert pour Lists, bleu pour Integrations. C'est exactement le dispositif
qu'on retrouve sur le site de 2026, section par section.

### L'app iOS, écrans réels

![[ecrans/planches/planche-app-ios.png]]

**Ce que les visuels de store ne montrent jamais.** Le bandeau de jours `S M T W T F S` collé en
haut de la timeline avec le jour actif en pastille ; la ligne rouge de l'heure courante ; la
pilule flottante « Today » et la capsule « VIEW » posées au-dessus de la barre d'onglets ; et
surtout le fait que **presque tout passe par des feuilles modales** — sélecteur de mois,
rappels, réglages. Les écrans sombres montrent une app qui bascule en `#272428` sans rien
perdre de sa structure. Millésime début 2025 (le jeu de données des captures est daté de
janvier 2025).

### L'app desktop, millésime 2026

![[ecrans/planches/planche-app-desktop.png]]

**L'app d'aujourd'hui n'a plus de calendrier sur son écran d'accueil.** Un rail d'icônes étroit
à gauche, une liste de notes groupée par « Yesterday / Last week / Previous 30 days / Past », la
note de réunion avec ses onglets Private notes / Summary / Transcript, et une barre « Ask Amie »
flottante en bas. La capture de l'appel Google Meet illustre le parti-pris qui structure tout le
produit de 2026 : **pas de bot dans l'appel**, l'UI d'enregistrement vit dans l'encoche du Mac.

## Flows

![[flows/planches/planche-onboarding.png]]

**L'onboarding fait choisir l'icône d'app avant même d'avoir montré le produit.** Écran d'accueil
sur un nuage de post-it manuscrits flous, « Continue with Google » en bouton noir plein et rien
d'autre ; passage par la webview Google ; puis, sous le surtitre jaune `CUSTOMIZATION`, le choix
entre trois icônes (Peachy rose, Gray, Black) ; et le paywall. Faire personnaliser l'icône avant
la conversion est un pari inhabituel : on demande un geste d'appropriation avant de demander de
l'argent.

![[flows/planches/planche-creation.png]]

**Créer, planifier, connecter.** La fiche d'événement en champs `Tap to add`, la recherche
d'invité en état vide assumé, la barre d'outils noire flottante au-dessus du clavier pour le
quick-add de tâche (date, récurrence, priorité, Add), et l'écran de langage naturel saisi en
pleine animation de morphing — « Meet with Peter 1h after my bank appointment » qui se change en
carte d'événement. La dernière vignette est une autorisation Apple Health : les intégrations
passent par les dialogues système, pas par des écrans maison.

Le parcours complet, écran par écran, est dans la vidéo :

![[flows/walkthrough-app-ios_amie.mp4]]

**Neuf minutes de session réelle**, chapitrées : onboarding 00:00-01:29, création d'événement
02:08-03:04, création de tâche 04:02-05:08, gestion des listes 06:35-07:46, préférences
08:01-08:57. C'est la seule source qui donne les transitions et les feuilles modales en
mouvement.

## Branding

![[branding/planches/planche-symbole.png]]

**Le symbole se lit comme un « coco ».** Quatre cercles fusionnés en quadrilobe, percés d'une
barre verticale arrondie au centre — et quand on connaît le croquis d'origine (voir `process/`),
on ne voit plus que ça. Il est décliné en trois matières : **vectoriel plat** (contour `#EBEBEB`)
dans le site, **gonflé 3D blanc mat** comme une pâte pour l'icône d'app et l'og:image, et
**irisé violet-bleu-rose** dans le schéma d'intégrations. Le wordmark de la keynote 2022, lui,
était une sérif crème sur noir — plus rien n'en subsiste.

Le pied de page porte la seule signature verbale de la marque :

![[branding/signature-designed-by-the-beach.svg|280]]

**« Designed by the beach », et le texte est vraiment une vague.** Le remplissage du lettrage est
un motif SVG animé en `animateTransform`, translation 0 → 40 en 1,5 s, en boucle, doublé d'un
calque dégradé `#000` → `#595447` à 40 % d'opacité. Un détail que personne ne remarque et que
tout le monde ressent.

**Typographie** — deux familles servies par `next/font`, plus une troisième en réserve :

| Rôle | Police | Auteur | Détail |
| --- | --- | --- | --- |
| Corps et UI | **Inter** (variable, `100 900`, v4.001) | Rasmus Andersson | pile déclarée `Inter var, ui-sans-serif, system-ui, -apple-system` |
| Accroches | **Averia Serif Libre** Regular (v1.002) | Dan Sayers | sérif « moyenne » générée depuis toute la bibliothèque Font Squirrel |
| Manuscrit | **Caveat** | Impallari Type | classe utilitaire `.font-[Caveat]`, pour les annotations |
| Historique | **Universal Sans** | Family Type | la police du site de 2020-2021, abandonnée |

La variable CSS des accroches s'appelle encore `--font-instrument-serif` : **ils étaient sur
Instrument Serif avant et ont gardé le nom**. Aucune fiche `/font` n'existe encore dans le vault
pour ces familles.

## Couleurs

![[couleurs/palette-marque.svg]]

**Amie ne publie qu'un seul nom de couleur, et c'est celui d'une couleur qu'elle n'utilise
plus.** `--color-amie-pink: #f6a6a6` est le seul token de marque du CSS ; tout le reste du site
est en valeurs arbitraires Tailwind, sans thème sémantique. Les autres hex ci-dessous sont
relevés à la pipette sur les assets officiels, pas déclarés.

**Nommée par Amie**

| Nom | Hex | Usage |
| --- | --- | --- |
| `amie-pink` | `#F6A6A6` | couleur de marque 2020-2023, seul token nommé encore présent en 2026 |

**Dégradés officiels**

| Nom de rôle | Hex | Usage |
| --- | --- | --- |
| Rose haut | `#FFB4B4` | haut du dégradé de l'icône iOS |
| Rose bas | `#FF9C9C` | bas du dégradé de l'icône iOS |
| Bleu profond | `#0389FF` | haut du ciel de l'og:image, depuis janvier 2024 |
| Bleu pâle | `#85C6FF` | bas du ciel |

**Divers officiels**

| Nom de rôle | Hex | Usage |
| --- | --- | --- |
| Blanc cassé chaud | `#F8F7F4` | fond de la page `/download` |
| Or des étoiles | `#FF9D00` | notation des avis |
| Gris de bord | `#EBEBEB` | contour du symbole vectoriel |

![[couleurs/palette-relevee-sur-le-site.svg]]

**84 % du site tient dans un seul gris.** `#FAFAFA` couvre la page, le blanc n'intervient que
pour les cartes, et l'unique bouton coloré de tout le site est un bleu `#11A8FF` qui pèse 0,13 %
de la surface. Relevé par comptage de pixels sur la home pleine hauteur et la page pricing,
août 2026.

**Fonds**

| Nom de rôle | Hex | Part | Usage |
| --- | --- | --- | --- |
| Gris de page | `#FAFAFA` | 84,18 % | fond général |
| Blanc | `#FFFFFF` | 6,71 % | cartes et encarts |
| Gris de section | `#F2F2F2` | 1,24 % | respirations |
| Gris de bord | `#EBEBEB` | 0,26 % | filets de carte, 1 px |

**Texte**

| Nom de rôle | Hex | Part | Usage |
| --- | --- | --- | --- |
| Noir pur | `#000000` | 0,49 % | titres — le site ose le noir pur, l'app non |
| Gris de sous-titre | `#5C5C5C` | 0,10 % | corps secondaire |
| Gris tertiaire | `#737373` | 0,05 % | légendes |

**Accents**

| Nom de rôle | Hex | Part | Usage |
| --- | --- | --- | --- |
| Bleu d'action | `#11A8FF` | 0,13 % | le seul bouton coloré du site |
| Bleu de surlignage | `#CFEEFF` | 0,05 % | effet surligneur sur un mot |

![[couleurs/palette-relevee-dans-les-ecrans.svg]]

**L'app décale tout d'un cran par rapport au site.** Fond `#F5F5F5` au lieu de `#FAFAFA`, encre
`#171717` au lieu de `#000000`. 62 % de la surface tient dans deux gris qui se distinguent d'un
cran, les couleurs cumulées font moins de 6 %, et elles n'y sont jamais décoratives : elles
étiquettent.

**Fonds**

| Nom de rôle | Hex | Part | Usage |
| --- | --- | --- | --- |
| Gris très clair | `#F5F5F5` | 37,92 % | fond des visuels |
| Blanc | `#FFFFFF` | 24,69 % | surface des cartes |
| Gris de bord | `#EBEBEB` | 4,18 % | contour de carte, 1 px |

**Texte**

| Nom de rôle | Hex | Part | Usage |
| --- | --- | --- | --- |
| Quasi-noir | `#171717` | 3,10 % | titres et corps — jamais `#000000` |

**Accents de catégorie**

| Nom de rôle | Hex | Part | Usage |
| --- | --- | --- | --- |
| Cyan | `#0FA5EA` | 2,56 % | le seul accent saturé (label, sélection) |
| Bleu pâle | `#BAE7FE` | 0,95 % | événement de calendrier |
| Lavande | `#EAD5FF` | 0,80 % | événement de calendrier |
| Rose pâle | `#FEF0F0` | 0,88 % | événement de calendrier |

Le nombre de couleurs d'événement est un chiffre de produit, pas de charte : le changelog #120
du 7 mai 2025 le fait passer de **8 à 11**, plafonné par ce que Google Calendar accepte.

**Mesure de tiers** — Mobbin publie une page de couleurs de marque pour Amie, réduite à trois
valeurs (`amie-ff9d9c`, `amie-bfbfbf`, `amie-171717`). Ce n'est ni une charte ni un relevé
maison, c'est l'échantillonnage d'un curateur : [mobbin.com/colors/brand/amie](https://mobbin.com/colors/brand/amie).

## Composants

![[composants/planches/planche-composants.png]]

**Ce qui sort du lot, et pourquoi.** La barre d'enregistrement dans l'encoche est le composant
signature de 2026 : une pilule sombre « Amie Weekly · 00:07 · play · pause · Stop » posée
par-dessus Google Meet, qui matérialise la promesse « no bots in calls » en un seul objet. Le
champ de prompt IA (pilule blanche à bord fin, icônes `@` et trombone, bouton rond bleu à flèche
montante) et le tableau d'auto-tagging à trois colonnes viennent de la même génération.

À côté, deux composants montrent la manière Amie de **relier deux objets par un trait** : la
todo « Send newsletter » reliée en pointillé bleu au créneau qu'elle vient de créer, et la carte
de todo avec sa pilule minuteur « 48m ». La feuille de rappels iOS est l'exemple type du reste :
cartes grises arrondies, toggles système, aucune invention.

La carte menubar de 2024 est gardée pour comparaison — même fonction, langage visuel opposé
(objet flottant incliné sur fond noir avec halo).

## Animations

![[animations/scroll-sections-home_amie.mp4]]

**Le site anime peu, mais il anime au bon endroit.** Les sections apparaissent en fondu au
scroll, la bande de salutations multilingues défile en marquee, et les captures produit sont
serties dans des **cadres en dégradé irisé** qui bougent lentement. Enregistré sur la home,
défilement 5200 → 9200 px.

![[animations/scroll-page-art_amie.mp4]]

**La page `/art` est la seule pièce vraiment cinématique** : la capture de l'app y est épinglée
et mise à l'échelle au fil du scroll, le texte se révèle par-dessus. C'est aussi l'ancienne
landing, conservée en ligne (voir `## Archive`).

![[animations/integrations-vers-logo_amie.mp4]]

**Dix secondes du film « Amie 2.0 »** : les icônes d'intégrations envoient des chemins de points
animés vers le symbole corail, puis l'image morphe vers le tableau d'auto-tagging. Le mécanisme
de marque en une phrase visuelle — tout converge vers Amie.

## Marketing

![[marketing/planches/planche-launch-film-2025.jpg]]

**Le film de lancement de 2025 assume une DA de mode, pas de SaaS.** Dennis Müller sur cyclorama
monochrome saturé (bleu ciel, puis vert-jaune), veste crème et foulard imprimé ; en contrepoint,
des intérieurs béton chaleureux en lumière naturelle et des tricots crème. La palette
vestimentaire est imposée d'un bout à l'autre. Produit par Episode Film and Media Productions,
réalisé par Alex Kibb.

![[marketing/planches/planche-film-amie-2-0-2025.jpg]]

**Le film « Amie 2.0 » est un plan-séquence animé sans coupe**, monté en screen-recording
composité sur un bureau macOS : le notetaker s'incruste dans Google Meet, une checklist s'anime,
l'e-mail se rédige tout seul, les avis App Store défilent. Aucune voix, aucun présentateur — le
produit se démontre.

Le site marketing lui-même est capturé en pleine hauteur : `marketing/home.png` (1920 × 14 265),
`marketing/home-mobile.png` (1170 × 45 924), `marketing/pricing.png`, `marketing/changelog.png`
et `marketing/art.png`. Deux visuels produits officiels complètent : le hero 2026
(`marketing/visuel-hero-2026.png`, 2676 × 1726) et le schéma
`marketing/schema-integrations.png`, qui range les outils en `SOURCES → VIA AMIE →
DESTINATIONS`.

**Prix** — deux plans seulement, essai gratuit de 7 jours, -20 % à l'année : **Pro à 20 €** par
utilisateur et par mois, **Business à 40 €**. Sur iOS, le paywall in-app est resté sur l'ancienne
grille : 14,99 $ par mois ou 99,99 $ par an, avec un bandeau rouge « Save 36 % » et le plan
annuel présélectionné.

## Process

**C'est la pièce rare de ce dossier.** Amie publie sur `amie.so/stories` deux récits photo signés
par son fondateur — l'un à Los Angeles avant le début, l'autre au Cap pendant la conception —
avec une légende par image. Photos argentiques, majoritairement Portra 400. Très peu de produits
publient ça.

![[process/planches/planche-decisions-de-design.png]]

**Les décisions, dans l'ordre où elles ont été prises.** Le croquis du logo « coco » tracé au
doigt dans l'app Photos pendant un trajet en voiture vers Lake Tahoe — « Creative processes are
inflated. You need no fancy tools, WhatsApp might suffice. » La couverture du deck Coco. La story
Instagram du nuancier Pantone Blossom, source du rose. Le carnet Moleskine et les post-it 3M des
deux semaines de concept, avec Google Calendar détourné en prototype. Le fichier Figma, et la
phrase qui vaut la lecture : **« I started with components, not screens. It paid back in speed
quickly. »** Puis le stack ranking des fonctionnalités — « Products die from obesity much rather
than from starvation » — le test des mots par e-mail, et les questions d'entretien inspirées de
The Mom Test.

![[process/planches/planche-references-et-etalons.png]]

**Les étalons revendiqués, nommément.** RIMOWA pour le niveau de qualité (« What's the value of a
lifetime? »), Baggu pour la fabrication produit (« better handles, thicker material… So
buttery »), les musées pour l'œil — **« Amie's aesthetic is made of countless museum visits »**.
Plus les lectures annotées (Creativity Inc.), la citation Netflix sur le fil du rasoir entre
succès et échec total, et celle sur la photographie : « the biggest difference between an amateur
and a professional is the size of the wastebasket ». Le cottage du Cap et les deux semaines de
concept au coucher du soleil ferment la série — et expliquent « Designed by the beach ».

Le panorama des apps d'habitudes concurrentes est gardé en GIF
(`process/panorama-des-apps-d-habitudes.gif`) avec sa légende d'origine : « Full of slightly
competing products. None matched my high bar for UX. A great invitation. »

## Archive

Six ans, cinq générations. Chaque planche est un millésime daté à la source (Wayback, presse
d'époque, ou assets encore servis par le site).

![[archive/planches/planche-2020-le-wordmark-rose.png]]

**2020-2021 : le rose, le wordmark, et rien d'autre.** Fond `#F6A6A6` plein, le mot « Amie » en
Universal Sans, la baseline « The joyful productivity app » et un formulaire de liste d'attente.
La web-app existe déjà et elle est **entièrement grise** — aucune couleur d'événement. Deux
détails survivent jusqu'à aujourd'hui : la saisie par `/commands`, présente dès 2020, et le
positionnement « joyful ». La landing ne bouge pas d'un pixel pendant dix-huit mois.

![[archive/planches/planche-2022-la-beta.png]]

**2022 : la beta, du sombre au clair, dans la même année.** En mars, le press kit envoyé à
TechCrunch est **sombre sur dégradés ambrés**, avec des annotations manuscrites numérotées et
fléchées en vert, rose, orange et bleu. Le produit revendique alors une **couche sociale** —
profils, « 22 times together this year », post-it de notes sur un contact — aujourd'hui
entièrement disparue. En fin d'année, tout a basculé en clair : pastels saturés, dock d'avatars
Memoji, cartes flottantes détachées de l'app. La command palette, les liens de partage et la
création « copy from history » datent de là.

![[archive/planches/planche-keynote-beta-2022.jpg]]

**La keynote de mars 2022 est une mise en scène façon Apple** : hangar noir, néons verticaux
bleus, écran géant, silhouettes en contre-jour. Chaque écran produit y est présenté sur un
dégradé pastel plein cadre différent — jaune beurre, vert d'eau, rose bonbon, lavande, pêche.
C'est le nuancier de marque de 2022, montré et jamais écrit.

![[archive/planches/planche-2024-le-rebrand-ciel.png]]

**Décembre 2023 - janvier 2024 : le symbole naît, le rose meurt.** L'icône `app-icon-pink` sort
avec l'app iOS le 12 décembre 2023 ; six semaines plus tard, le même quadrilobe est posé sur un
ciel bleu photographique et devient le logo. Le site de 2024 fait flotter la fenêtre de l'app
au-dessus de nuages, intègre l'e-mail, et pose un post-it manuscrit « Call grandma » par-dessus
l'interface. L'e-mail de lancement du 24 janvier, capturé dans l'app elle-même, dit tout :
« labours of love take time – after 2 years in beta we're today introducing a new Amie ».

![[archive/planches/planche-2025-le-virage-ia.png]]

**2025 : le calendrier quitte l'écran d'accueil.** La refonte d'avril remplace la grille par une
liste de notes de réunion et une barre « Ask Amie ». Le titre de la page passe de « Amie - Joyful
productivity » à **« Amie - AI Note Taker »**. La fiche App Store, elle, n'a pas suivi : elle est
figée depuis août 2025 sur l'ancienne promesse et l'icône rose — **le store vend encore le
produit d'avant**.

Deux pièces isolées méritent d'être ouvertes en grand :
`archive/2022-11-landing-pleine-hauteur.png` (1440 × 7700, la landing de novembre 2022 en
entier) et `archive/2022-semaine-claire-pleine-resolution.png` (2160 × 1440, la meilleure
capture existante de l'UI de 2022).

Les trois démos vidéo du site de 2024 sont conservées telles quelles :
`archive/2024-glisser-deposer-planifier.mp4` (l'interaction signature de l'époque : un e-mail
glissé dans la grille pour être planifié), `archive/2024-email-vers-todo.mp4` et
`archive/2024-integrations.mp4`.

## Pourquoi je l'aime

Parce que c'est un cas d'école de **discipline sur les écarts d'un cran** : deux gris à peine
distincts qui suffisent à créer de la profondeur sans une seule ombre marquée. Et parce que la
rigueur y est constamment cassée par de l'écrit à la main — une flèche, un surligneur, un post-it.
La combinaison est rare : la plupart des produits choisissent l'un ou l'autre.

Parce que c'est aussi, à l'inverse, un **avertissement lisible** : à force d'affiner la
neutralité, Amie a effacé sa couleur. Le rose de 2020 était identifiable en une image. Le gris de
2026 ne l'est plus.

## À réutiliser pour

- **Le label coloré en surtitre au-dessus d'une phrase noire** : une couleur par section, jamais
  deux dans le même bloc de texte. Système immédiat, coût nul.
- **Le décalage fond/carte d'un seul cran** (`#FAFAFA` sur `#FFFFFF`), doublé d'un filet 1 px
  plutôt que d'une ombre. Marche partout où l'on veut de la profondeur sans lourdeur.
- **L'annotation manuscrite en surimpression** pour commenter une capture produit — flèche
  tracée, mot souligné, post-it. Réchauffe instantanément une DA trop propre.
- **La couleur réservée à la donnée** : si la couleur n'étiquette rien, elle ne sert à rien.
- **Le récit de fabrication comme contenu de marque** : `amie.so/stories` est un modèle de
  transparence de process, et un excellent gabarit pour une page « comment c'est fait ».
- **Faire choisir une personnalisation avant le paywall** (l'icône d'app) pour installer un
  geste d'appropriation.

## Sources

- **Site officiel `amie.so`** — captures maison pleine hauteur (home, `/art`, `/pricing`,
  `/changelog`, mobile), relevé des polices réellement rendues, tokens CSS, logo vectoriel
  inline, fichiers `.woff2`, signature animée du pied de page : [amie.so](https://amie.so)
- **`amie.so/stories`** — les deux récits de fabrication signés Dennis Müller, 31 photos
  légendées : [/stories/early-design](https://amie.so/stories/early-design/) ·
  [/stories/design](https://amie.so/stories/design/)
- **`amie.so/art`** — l'ancienne landing de 2024 conservée en ligne par la marque, avec ses
  assets sous `/2024/` et ses vidéos Cloudinary de janvier 2024 : [amie.so/art](https://amie.so/art)
- **`amie.so/changelog`** — 131 mises à jour datées jusqu'au 27 août 2026, dont les trois
  refontes : [amie.so/changelog](https://amie.so/changelog)
- **`amie.so/calendar`** — frise chronologique publique 2019-2023, avec les dates d'arrivée
  nominatives de l'équipe : [amie.so/calendar](https://amie.so/calendar)
- **App Store** — les 5 visuels de store en résolution native et les métadonnées d'éditeur :
  [apps.apple.com/…/id1548277133](https://apps.apple.com/fr/app/amie-todos-calendar/id1548277133)
- **Screensdesign** — les 8 écrans réels non floutés en 1080 × 2336 (page `/showcase/`) et le
  walkthrough vidéo de 8 min 59 : [screensdesign.com/showcase/amie-todos-calendar](https://screensdesign.com/showcase/amie-todos-calendar/)
- **TechCrunch** — trois articles de Romain Dillet (mars 2022, novembre 2022, janvier 2024) avec
  les press kits annotés fournis par Amie : [beta 2022](https://techcrunch.com/2022/03/17/amie-is-a-new-calendar-app-with-a-social-twist/) ·
  [levée 7 M$](https://techcrunch.com/2022/11/28/amie-grabbed-7-million-for-its-opinionated-calendar-and-todo-app/) ·
  [relance 2024](https://techcrunch.com/2024/01/24/amie-brings-your-email-inbox-to-its-calendar-app/)
- **Inverse** — interview de Raymond Wong et triptyque iOS des intégrations Health/Spotify :
  [inverse.com/tech/amie-calendar-app-dennis-muller-ceo-interview](https://www.inverse.com/tech/amie-calendar-app-dennis-muller-ceo-interview)
- **The Verge** — interview de David Pierce, janvier 2024 :
  [theverge.com/2024/1/24/24048981](https://www.theverge.com/2024/1/24/24048981/amie-calendar-app-ios-mac-web)
- **YouTube (chaîne de Dennis Müller)** — trois films officiels : [Amie Beta Launch, mars 2022](https://www.youtube.com/watch?v=OGe1NYKhZE8) ·
  [Amie 2.0 Launch, avril 2025](https://www.youtube.com/watch?v=CqJd_2hZyGk) ·
  [Amie Launch Film, septembre 2025](https://www.youtube.com/watch?v=h2bDjXAetpY)
- **Wayback Machine** — les millésimes de 2020, 2022 et 2024-2025, datés par les digests de
  snapshot : [web.archive.org/web/\*/amie.so](https://web.archive.org/web/*/amie.so)
- **SaaS Landing Page** — la landing de novembre 2022 en pleine hauteur (1440 × 7700) :
  [saaslandingpage.com/amie](https://saaslandingpage.com/amie/)
- **Mobbin** — page de couleurs de marque uniquement (l'app n'est pas dans l'index public
  d'écrans) : [mobbin.com/colors/brand/amie](https://mobbin.com/colors/brand/amie)
- **Hacker News** — la discussion qui explique pourquoi `/art` existe :
  [news.ycombinator.com/item?id=47979351](https://news.ycombinator.com/item?id=47979351)

## Crédits

- **Dennis Müller** — fondateur, CEO et designer d'Amie ; ex product manager chez N26. Auteur des
  deux récits de `/stories`, du croquis du logo, du design system d'origine et des films
  officiels publiés sur sa propre chaîne. Photographe argentique (« I am shooting for my photo
  book. It's fully shot on film, mostly Portra 400 »).
  [X @tryamie](https://x.com/tryamie) · [chaîne YouTube](https://www.youtube.com/watch?v=CqJd_2hZyGk)
- **Amie GmbH** — éditeur, Berlin. 11 personnes en novembre 2022, 14 en janvier 2024.
- **L'équipe, telle qu'Amie la nomme sur sa propre frise** (prénoms seuls, c'est tout ce qui est
  publié) : Eric (juillet 2020), Ivo et Agnes (janvier 2021), Stefan (avril 2021), Antoine
  (juin 2021), Polly (septembre 2021), Fahyik (mai 2022), Sofia (juillet 2022), Louis
  (septembre 2022), Mikael et Christian (novembre 2022) — [amie.so/calendar](https://amie.so/calendar)
- **Amie Launch Film (2025)** — production **Episode Film and Media Productions**, réalisation
  **Alex Kibb**, chef opérateur **Robin Taylor**.
- **Typographie** — **Inter** par [Rasmus Andersson](https://rsms.me/inter/) ; **Averia Serif
  Libre** par Dan Sayers ; **Caveat** par Impallari Type ; **Universal Sans** (site 2020-2021)
  par Family Type.
- **Investisseurs** — seed de 7 M$ mené par **Spark Capital** (clôturé juin 2022, annoncé
  novembre 2022), avec Creandum (déjà au pre-seed de 2020), Guillermo Rauch (Vercel), Hanno
  Renner (Personio) et Quick Coffee Ventures. Total levé : 8 M$.
- **Journalistes** — Romain Dillet (TechCrunch), David Pierce (The Verge), Raymond Wong (Inverse).
- **Les « executive producers »** remerciés nommément en fin du récit `/stories/design` : une
  trentaine de personnes, dont Eduard Wieandt, Malte Berresheim, Timo Meyer, Julian Lehr.

## Ce que Dennis Müller dit de son produit

> « The relationship most people have with their calendars is transactional. I open it to get the
> information of where I need to be next, then I close it. I hope to combat this feeling of the
> calendar being this place that's just the launchpad to the next meeting. »
> — [Inverse](https://www.inverse.com/tech/amie-calendar-app-dennis-muller-ceo-interview)

> « The initial spark came from this one sentence: how would Google Maps look if it was designed
> to reach personal goals? Not like "New York to Boston," but "I know nothing about music and I
> want to play the saxophone." »
> — [The Verge](https://www.theverge.com/2024/1/24/24048981/amie-calendar-app-ios-mac-web)

> « I started with components, not screens. It paid back in speed quickly. Every team should
> invest highly in their design system. »
> — [amie.so/stories/design](https://amie.so/stories/design/)

> « Products die from obesity much rather than from starvation. »
> — [amie.so/stories/design](https://amie.so/stories/design/)

Et le contrechamp, sur Hacker News en mai 2026, à propos de `/art` :

> « There was a company, Amie, that had this as their landing page initially, without the /art
> path. Guess what, visitors didn't convert, and then the company redid their landing page to
> actually explain and convert customers. They literally host their prior landing page as "art"
> because it was so terrible at acquiring customers. »
> — [news.ycombinator.com](https://news.ycombinator.com/item?id=47979351)

## Limites de ce dossier

- **Aucun press kit, aucune charte publiée.** Les URLs `/press`, `/brand`, `/media`, `/newsroom`,
  `/brand-assets`, `/design` et `design.amie.so` renvoient toutes 404, et il n'y a aucun DAM
  (Lingo, Frontify, Brandfolder, Bynder) à interroger. Le seul « kit » est le SVG inline du
  symbole. Toutes les couleurs de ce dossier sont donc soit un token CSS, soit un relevé de
  pixels — jamais une charte.
- **Pas d'app Android** : tous les packages plausibles renvoient 404 sur Google Play. La page
  `/download` n'annonce que macOS, iOS et Windows.
- **L'app web (`calendar.amie.so`) est derrière un login** et n'a pas pu être capturée. La seule
  piste identifiée — une capture de son écran de connexion sur Land-book — est bloquée par
  Cloudflare : [land-book.com/websites/56516-login-amie](https://land-book.com/websites/56516-login-amie).
  À ouvrir à la main dans Arc si le sujet revient.
- **Amie n'est pas dans l'index public d'écrans de Mobbin** — seule sa page de couleurs de marque
  existe. Les 79 écrans indexés par Screensdesign sont derrière « Unlock Pro » ; seuls les 8 du
  showcase sont libres.
- **Le site n'a pas de thème sombre** : la capture en `prefers-color-scheme: dark` est identique
  à la claire, elle a été supprimée. L'app iOS, elle, en a un (voir `ecrans/ios-sombre-*`).
- **Les captures de store plafonnent à 1242 × 2208** — c'est la résolution uploadée par
  l'éditeur, et il n'y a pas de captures iPad.
- **Les écrans Screensdesign portent un léger filigrane** en haut à gauche, conservé tel quel
  plutôt que recadré.
- **Product Hunt est resté inaccessible** (403 Cloudflare) : Amie y a eu plusieurs lancements
  commentés par son fondateur, autant de millésimes non récupérés.
- **L'angle « auteur » de la récolte n'a rien donné.** X, Dribbble, Behance et Instagram sont
  inaccessibles depuis cette machine (Cloudflare, 403), donc aucune exploration écartée, aucun
  avant/après posté par l'équipe, aucun shot signé. Les crédits ci-dessus viennent tous de
  sources officielles ou de presse. Ce serait le seul vrai gain d'une reprise du dossier.
- **Aucune fiche `/font`** n'existe encore dans le vault pour Inter, Averia Serif Libre ou Caveat.

## Mots-clés

calendrier, calendar, agenda, to-do, todo, e-mail, email, notes de réunion, meeting notes, AI
note taker, preneur de notes, transcription, MCP, agent IA, split view, timeline, widget,
onboarding, paywall, feuille modale, sheet, quick add, langage naturel, natural language,
drag and drop, glisser-déposer, gris clair, off-white, quasi-noir, near-black, noir pur, rose,
pink, blossom, pastel, carte flottante, ombre douce, contour 1px, filet, label coloré, surtitre,
catégorisation par couleur, annotation manuscrite, handwritten, surligneur, highlighter, post-it,
composition éparpillée, scattered cards, dégradé irisé, iridescent, quadrilobe, squircle, coco,
noix de coco, Inter, Averia Serif Libre, Caveat, Universal Sans, Instrument Serif, minimal Apple,
Berlin, Cape Town, designed by the beach, argentique, Portra 400, joyful productivity, refonte,
rebrand, millésime, archive, process, design system, Dennis Müller, Amie GmbH, Spark Capital

---
[[_APPS|← Apps]] · [[_INSPIRATION|← Inspiration]]
