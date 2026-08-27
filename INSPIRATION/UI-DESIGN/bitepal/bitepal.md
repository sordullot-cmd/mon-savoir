---
type: inspiration
discipline: ui-design
media: app
source: https://bitepal.app
url_store: https://apps.apple.com/fr/app/bitepal-calcul-de-calories-ia/id6479529917
editeur: REFACE LITHUANIA UAB (coquille d'édition du studio ukrainien Reface)
type_app: santé
plateformes: [ios, android, web]
version: 2.28.0 — mise à jour le 2026-08-25 (première sortie 2024-06-10)
secteur: santé
couleur_principale: vert #47B25A
couleurs: ["#47B25A", "#262626", "#EDEDF2", "#F7C563", "#FF8066", "#4F8BEC", "#FC7059", "#FFFFFF"]
patterns: [onboarding, paywall, tab-bar, parametres, empty-state, gamification]
anime: oui
animations: [loader, sheet, celebration, drag]
layout: centré
mood: [playful, bold]
typos: Bricolage Grotesque (titres) · Inter (corps) · Nanum Pen Script (annotations manuscrites) — les trois relevées dans le CSS et les @font-face servis
date_capture: 2026-08-27
tags: [inspiration, ui, santé, habitudes, playful, bold, mascotte, gamification]
---

# BitePal

> Compteur de calories par photo, avec un raton laveur qu'on nourrit, qu'on habille et qu'on peut laisser mourir de faim. La marque résume elle-même son positionnement sur une pancarte en carton : **« Duolingo but for weight loss »**.

![[icone.png|120]]

## En bref
- **Le produit est un Tamagotchi déguisé en tracker.** Le raton a une **jauge de vie en quatre cœurs** qu'on remplit en enregistrant ses repas, une **monnaie** (les BiteCoins), une **boutique d'accessoires et de décors**, et des états d'humeur. La fonction nutritionnelle est le prétexte de la boucle d'attachement.
- **Le raton n'a aucun nom de marque** : c'est un champ utilisateur (Réglages → Application → « Raccoon's name »). J'ai relevé **sept noms de démo** selon la source et l'époque — Kutie (2024), Cutey (mai 2025), Rocky (le site), Manuela (App Store FR), Tamagotchi (le funnel web), Bubba, Bandit. Le personnage, lui, se présente comme la marque : les props du composant disent littéralement « Hi, I'm BitePal ».
- **Deux bases de code, deux chartes, et le vert n'est pas le même des deux côtés** : `#47B25A` en token sémantique dans le funnel, `#4BA85C` en classe utilitaire sur la vitrine.
- **Aucun press kit, aucune charte publiée.** Tout ce qui est déclaré ici a été lu dans le CSS de production et dans les bundles JS.
- **L'app a changé de DA de fond en comble** : en août 2024 le raton était **rose**, sur un ciel violet et un sol ambre, avec des cartes pêche. Aujourd'hui il est gris sur un paysage vert et des cartes blanches.
- Le produit s'est aussi appelé **Pookies** en public jusqu'en août 2024. Le bundle iOS porte encore le nom mort : `com.pookies.food.ai`.
- **Croissance 100 % payante** : 400 K$/mois au bout de 12 mois, 700+ mots-clés en Apple Search Ads, 170+ vidéos actives sur Facebook. Le teardown qui le documente conclut : « It doesn't go viral. It doesn't have influencers. »

## DA globale

Un produit de rétention habillé en compagnon. Le système tient sur trois piliers : une
**mascotte riggée** déclinée en une dizaine d'états émotionnels, une **grotesque très
grasse** (Bricolage Grotesque) qui porte tous les titres en noir `#262626` — jamais du
noir pur —, et un **paysage illustré plat** qui sert de fond de scène. Autour de ce noyau,
tout le reste est d'une sobriété presque bancaire : cartes blanches, coins très arrondis
(`--Button-Radius: 32px`), gris `#EDEDF2` pour les surfaces neutres, et une sémantique de
couleur à trois états seulement.

La singularité est là : **la chaleur est entièrement portée par l'illustration et le ton de
voix, pas par la couleur de l'interface.** Le raton parle à la première personne
(« That's some serious fuel for my tummy! »), une police manuscrite ajoute des annotations
au crayon par-dessus l'UI, et pendant ce temps la grille reste un design system propre et
neutre. C'est exactement l'inverse d'un [[fabulous]], qui teinte tout son papier en crème.

Le revers est visible dans le même dossier : **le cadenas est un motif d'UI omniprésent**
en version gratuite (macros, score nutritionnel, fibres, récompenses, plan de jeûne
personnalisé), et le vocabulaire du code assume la mécanique — un composant `ScretchCard`
avec ses propres rouges, une roue de la fortune, une popup d'abandon de paiement. La DA est
adorable ; le tunnel est agressif. Un teardown vidéo le résume mieux que moi :
« BitePal trades accuracy for engagement. »

## Écrans

Le dossier distingue trois provenances, et le nom de fichier le dit : `store-` pour les
visuels promotionnels, `app-` pour les écrans réels de l'app, `editeur-` pour les captures
produit que l'éditeur sert lui-même dans son funnel.

![[ecrans/planches/planche-ecrans-de-store.png]]

**Une couleur de fond par fonctionnalité, sur un dégradé bleu ciel commun.** Les dix
visuels de l'App Store FR partagent le même dégradé `#F4FCFF` → `#C3E4F5` et le même titre
en Bricolage Grotesque noir, mais l'écran d'app qu'ils montrent change de couleur à chaque
fois : violet pour les calories brûlées, rose pour l'eau, bleu nuit pour le jeûne, orange
pour les défis, vert pour la boutique, corail pour la série. Deux visuels sortent du
registre illustré : le scan montre une **vraie photo d'assiette** annotée de pastilles, et
« Suis tes progrès » montre des **photos avant/après de vraies personnes** — un registre de
publicité fitness qui n'a rien à voir avec le reste.
`variante-android-badge-11m-utilisateurs.jpg` est le même visuel de couverture avec un autre
badge (« 11M+ utilisateurs » au lieu de « App du jour »).

![[ecrans/planches/planche-app-reelle-janvier-2026.png]]

**C'est ici que le produit se lit vraiment, et le store n'en montre rien.** Dix-huit écrans
réels : l'empty state du journal, les trois modes de saisie (photo avec bascule Meal/Label,
galerie, texte libre), l'état de chargement « Analyzing. Powered by AI », la fiche de repas
avec ses ingrédients détectés au gramme, le score nutritionnel sur 100, la boutique de
décors et de chapeaux avec ses prix en pièces, le portefeuille de BiteCoins, et les
réglages — dont la ligne « Raccoon's name » qui prouve que la mascotte est renommable. À
noter, le **home est un empilement de widgets réordonnables par l'utilisateur**
(`app-home-layout-widgets-reordonnables.png`), ce qui est rare dans cette catégorie.

![[ecrans/planches/planche-ecrans-servis-par-l-editeur.png]]

**Les mêmes écrans, mais retouchés pour vendre** — et c'est instructif de les comparer aux
précédents. L'éditeur sert ces captures dans son funnel web ; le nom de démo y est
« Tamagotchi », ce qui en dit long sur la référence assumée. L'écran de connexion
(`editeur-connexion-raise-virtual-pet.webp`) porte la promesse la plus nette du produit :
« Track calories. Raise virtual pet! »

## Flows

![[flows/planches/planche-onboarding-11-etapes.png]]

**Trente-sept étapes, cinq minutes, et la demande de pistage publicitaire posée à froid dès
la troisième seconde** — sans écran de préparation, par-dessus l'écran d'accueil. Ce qui est
capturé ici est la tête du parcours : splash sur lavande, accueil « Reach your weight
goals », prompt ATT, carrousel de bienvenue en cinq cartes, question d'attribution
(« How did you hear about us? »), puis **l'étape d'adoption** — « This raccoon is now your
virtual pet », le raton sortant d'une poubelle au milieu de traits dessinés à la main. Cette
étape est le pivot émotionnel de tout le produit. Le récapitulatif de plan avec la jauge
d'IMC est le dernier écran avant le paywall.

Le fichier `flows/funnel-web-config-37-etapes.json` est la **config déclarative du funnel
web**, décodée depuis le bundle : les 37 étapes dans l'ordre, avec pour chacune son type de
composant et ses props. Le funnel est un système de **40 types de composants réutilisables**
(`OptionList`, `DynamicBmi`, `WeightPicker`, `Racoon`, `PersonalizingPlan`…), et les étapes
sont conditionnées par des **feature flags GrowthBook** et par les réponses précédentes.
C'est le document le plus rare du dossier : on y lit la structure d'acquisition, pas
seulement son résultat.

![[flows/planches/planche-paywall-haut-et-bas.png]]

**Un seul paywall, très long, où la mascotte occupe tout le tiers supérieur.** Le raton y
apparaît **les yeux transformés en éclairs jaunes** sur le seul fond vert saturé du parcours
— tout le reste du paywall est blanc. La promesse est chiffrée (« Achieve your goals 4.2x
faster », le 4.2x en vert acide), le prix est en typographie sèche, puis viennent le tableau
Free contre Plus avec ses cadenas, un carrousel de témoignages, et les lauriers
« 4.7 average rating / 1M users worldwide ». Prix relevés : essai 3 jours, carte unique
badgée « Most popular » affichée **2,99 $/mois** pour un annuel réel à **35,99 $** (barré
59,99 $) ; « Show more plans » déplie un plan hebdomadaire.

![[flows/planches/planche-scan-d-un-repas.png]]

**Le geste central, en quatre écrans.** Caméra avec bascule Meal/Label → résultat éditable →
correction manuelle des portions au pavé numérique → signalement d'erreur de l'IA. Ce
dernier écran mérite l'attention : la marque a instrumenté **une boucle de confiance
complète** — un avertissement (« Sometimes AI scanner might miss or mislabel items »), une
notation de la précision en pouces, puis une taxonomie de signalement (Calories / Weight /
Ingredients / Nutrition score / Tips / Other) avec sous-question. Peu d'apps d'IA assument
autant leur marge d'erreur dans l'interface.

`flows/onboarding-en-mouvement-2025-12.mp4` — 80 s d'enregistrement d'écran du parcours en
mouvement (millésime décembre 2025).

## Branding

![[branding/planches/planche-logos-vectoriels.png]]

**Le lockup, en vectoriel, avec un détail qu'on ne voit qu'en grand : le point du « i » de
BitePal est une petite feuille verte.** Le wordmark est un Bricolage Grotesque très gras.
Le masque du raton fonctionne aussi **seul, détaché du personnage** — c'est ainsi qu'il est
utilisé en logotype dans l'annonce de lancement de l'éditeur
(`branding/masque-seul-en-logotype-annonce-linkedin.jpg`).

![[branding/planches/planche-etats-de-la-mascotte.png]]

**Le personnage est un système d'états, pas un dessin.** Relevés : debout bras levés
(accueil), hilare (succès), **ventre plein yeux plissés**, **en bavoir avec des couverts**,
**endormi couché** (jeûne trop court), **triste accroupi** (jauge de vie), yeux en éclairs
(série et paywall), lunettes-cœurs (fiche de repas). Le dossier contient aussi la
**lune à visage** qui sert de motif au jeûne.

**Le rig est disponible en Lottie** (voir § Animations) : dans tous les fichiers, le calque
de la mascotte s'appelle `img - racoon 2 Null 1` — et le voisin s'appelle `BitePal`.
L'orthographe fautive « racoon » (un seul c) est constante dans tout le code, jusqu'au nom
du composant `Racoon`.

![[branding/planches/planche-echantillon-du-systeme-d-icones.png]]

**364 icônes, extraites en SVG et renommées d'après la table de noms lue dans le bundle**
(`branding/icones/table-des-noms-lue-dans-le-bundle.txt`). Le set est presque entièrement
alimentaire, en illustration plate sur grille 40×40, et il est **localisé par cuisine** :
`food_arepa`, `food_churrasco`, `food_feijao_tutu`, `food_papas_rellenas`,
`food_chicharron_preparado`, `food_currywurst`, `food_bunuelos`. Une app qui dessine
l'arepa et le feijão tutu plutôt que de se contenter d'un burger générique en dit long sur
ses marchés.

![[branding/planches/planche-textures-de-marque.png]]

Quatre fonds de système : une texture verte granuleuse, la carte à gratter en vert foncé,
des rayons blancs sur vert, et les chevrons avant/après.

**Polices servies** (`branding/polices/`, cinq `.woff2` récupérés) : **Bricolage Grotesque**
en variable pour les titres, **Inter** en variable pour le corps, et **Nanum Pen Script**
pour les annotations manuscrites — c'est elle qui écrit « Hooman, log your food » par-dessus
le tableau de bord. Pile de repli notable dans le token du funnel :
`"Bricolage Grotesque Variable", "Noto Sans JP Variable", "Noto Sans KR Variable", "Noto Sans Arabic Variable", ui-serif`.
Aucune fiche pour ces polices dans le vault — candidates à `/font`.

![[branding/planches/planche-identite-et-editeur.png]]

L'icône, le masque seul en logotype, la carte produit chez l'éditeur (celle qui affiche
« Manuela »), et le logotype de Reface.

## Couleurs

![[couleurs/palette-declaree-tokens-du-funnel.svg]]

**Il n'y a pas de charte publiée, mais il y a un vrai design system — écrit en tokens
sémantiques dans le CSS de production.** C'est la pièce la plus précieuse du dossier : les
noms ci-dessous sont ceux du code, pas les miens. Le système est petit et discipliné : un
vert de marque, une encre unique déclinée en opacités, et **trois états sémantiques
seulement**, chacun servi en plein et en 10 %.

**Marque et texte** — le noir n'est jamais `#000000`, et le texte secondaire n'est pas un
gris mais **la même encre en transparence**.

| Nom du token | Hex | Usage |
| --- | --- | --- |
| `--Brand-Primary` | `#47B25A` | le vert de marque du funnel |
| `--Text-Primary` | `#262626` | l'encre |
| `--Text-Secondary` | `#26262699` | la même encre à 60 % |
| `--Text-Tertiary` | `#26262633` | la même encre à 20 % |
| `--Text-Inverse` | `#FFFFFF` | sur fond sombre |

**Surfaces**

| Nom du token | Hex | Usage |
| --- | --- | --- |
| `--Fill-Background` | `#FFFFFF` | le fond |
| `--Fill-Primary` | `#262626` | bouton principal |
| `--Fill-Secondary` | `#EDEDF2` | surface neutre |
| `--Fill-Tertiary` | `#2626260D` | l'encre à 5 % |
| `--Fill-Accent` | `#47B25A` | positif |
| `--Fill-Accent-Light` | `#47B25A1A` | le vert à 10 % |

**Sémantiques — trois états, pas plus**

| Nom du token | Hex | Usage |
| --- | --- | --- |
| `--Fill-Caution` / `-Light` | `#F7C563` / `#F7C56333` | attention |
| `--Fill-Warning` / `-Light` | `#FF8066` / `#FF80661A` | alerte |
| `--Fill-Accent-Alternative` / `-Light` | `#4F8BEC` / `#4F8BEC1A` | accent secondaire |

**Bordures et neutres**

| Nom du token | Hex | Usage |
| --- | --- | --- |
| `--Border-Default` | `#EDEDF2` | au repos |
| `--Border-Focus` | `#D4D4D4` | au focus |
| `--Border-Selected` | `#47B25A` | sélectionné |
| `--color-core-15` | `#262626` | échelle nommée par la clarté |
| `--color-core-45` | `#707173` | texte secondaire |
| `--color-core-75` | `#BBBCBF` | texte désactivé |

**La carte à gratter — le seul rouge de toute la charte**

| Nom du token | Hex | Usage |
| --- | --- | --- |
| `--ScretchCard-Primary` | `#DF0203` | la couche à gratter |
| `--ScretchCard-Secondary` | `#F4819F` | le dessous |

> L'orthographe `ScretchCard` est **celle du code**, telle quelle. Le dossier en compte
> d'autres, toutes en production : `Racoon` (un seul c), « Select entry categorie »,
> « I'm commited ». Équipe non anglophone, cadence de livraison rapide.

**Géométrie**, dans le même bloc `:root` : `--Button-Radius: 32px`,
`--Input-Radius: 24px`, `--Section-Padding: 32px`, `--Top-Padding: 8px`. Le rayon de 32 px
sur les boutons est ce qui donne au produit sa douceur générale.

![[couleurs/palette-declaree-site-vitrine.svg]]

**Le site vitrine n'a aucun token : ses couleurs sont écrites en dur dans des classes
Tailwind arbitraires** — et son vert n'est pas celui du funnel. Trois verts cohabitent donc
dans la même marque : `#47B25A` (token du funnel), `#4BA85C` (aplat de la vitrine),
`#4CA75C` (départ de dégradé de la vitrine). Aucun n'est une erreur d'échantillonnage : les
trois sont écrits noir sur blanc dans deux CSS différents.

![[couleurs/palette-relevee-dans-les-ecrans-de-store.svg]]

**Le relevé de pixels confirme le token et ajoute ce que la charte ne dit pas** : `#262626`
pèse 6,48 % de la surface des dix visuels, et le dégradé bleu ciel n'existe dans aucun
token — c'est une décision purement marketing, propre à la fiche de store.

![[couleurs/palette-relevee-sur-le-site.svg]]

**68 % de blanc.** La vitrine est blanche, et sa couleur tient dans une carte pastel par
bloc.

`couleurs/hex-releves-dans-les-364-icones.txt` — les 74 hex distincts trouvés dans les
attributs `fill` du set d'icônes, triés par fréquence. Ce n'est ni une charte ni un relevé
de surface : c'est un comptage de valeurs écrites en dur dans le code.

## Composants

![[composants/planches/planche-composants.png]]

Cinq blocs retenus, ceux qui ne ressemblent pas aux voisins de la catégorie → [[_COMPOSANTS]] :
- **la bulle de la mascotte** qui commente le repas par-dessus la photo, le raton passant la tête par le bord de l'écran, entouré de petits traits dessinés à la main ;
- **les puces d'ingrédients validables une à une**, avec une puce en alerte orange quand l'IA doute ;
- **le header de mascotte** : nom, jauge de vie en cœurs, compteur de série, entrée de boutique, tout sur trois centimètres ;
- **l'anneau de macros à 100 %** avec ses trois curseurs liés et la contrainte « Macronutrients must equal 100% » ;
- **le menu d'ajout rapide** en cartes noires empilées, dépliées depuis le bouton flottant.
Plus deux pièces du funnel : la barre de progression d'inscription à trois étapes et la jauge d'hydratation à six verres.

## Animations

`animations/scan-en-mouvement-coca-cola_bitepal.mp4` → [[_ANIMATIONS]]
**La seule captation du geste central en mouvement** : le masque circulaire qui se révèle
sur la canette, le label « Scanning plate… », le raton qui dépasse par le bas de l'écran,
puis la fiche produit. Réencodé (720 px, 1,3 Mo au lieu de 13) — l'original de la source
était encodé à 1 Mo/s pour 12 s.

`animations/lottie/` — **17 animations Lottie de la mascotte, en vectoriel animé et
riggées** : le hero du site (`raton-hero-site-life-3-hearts.json`, 31 calques nommés —
`3_eye`, `3_eye_closed`, `mouth`, `nose`, `ear_l`, `Leg_r`, `Hand_l`, `tail 2 Comp 1`,
`shadow`, `Head :M`), deux poses d'onboarding, et **quatre paires entrée/boucle** pour les
trois objectifs de poids et l'approche. Convention interne purement numérique : `01_in` /
`01_idle` (prise de poids), `02_*` (perte), `03_*` (maintien). S'y ajoutent les confettis,
la roue de la fortune (avec une variante hivernale) et deux Lottie localisés en français.
393×393, 60 fps — 100 fps pour `04_onboarding_pet`.

> Ce sont les **fichiers sources**, pas des aperçus rendus : Obsidian ne les affiche pas.
> Pour les voir jouer, il faut un lecteur Lottie. Aucun rendu GIF/MP4 n'a été fabriqué,
> faute de moteur de rendu Lottie sur cette machine.

## Marketing

![[marketing/planches/planche-site-desktop-et-mobile.png]]

**La vitrine est blanche, et une carte pastel par bloc porte toute sa couleur** : menthe,
abricot, rose, pervenche. Titres en Bricolage Grotesque noir, corps en Inter gris, hero en
paysage illustré plat avec la mascotte animée en Lottie et le mockup du produit encastré.
Lauriers « 4.7 average rating / 1M users worldwide ». **Pas de thème sombre** : le
`home-dark.png` capturé était identique au clair, il a été supprimé.

![[marketing/planches/planche-carrousel-tiktok-how-it-works.png]]

**Un gabarit de carrousel très tenu** : couverture rose avec le wordmark, planches
intérieures sur dégradé bleu ciel, cartes blanches, tête de raton utilisée comme puce de
liste, carte de fin rose (« Achieve your body goals, link in bio »). Le compte officiel
tient **deux registres nettement séparés** : ces carrousels brandés d'un côté, et de
l'autre du **meme natif sans aucun branding** (« kiss, marry, kill », UGC filmé au
téléphone) qui ne porte la marque **que sur la dernière planche**. Le pattern est
systématique.

![[marketing/planches/planche-illustrations-du-funnel-fr.png]]

**Douze illustrations éditoriales du funnel, dans leur version française** — et là encore
deux registres cohabitent : des diagrammes vectoriels teintés de vert (déficit calorique,
boucle déclencheur-action-récompense, camembert de macros, plan alimentaire) et des
**photos de jeunes femmes en tenue de sport** pour l'upsell. Le funnel est localisé jusque
dans ses images : les 290 assets du manifeste comportent des variantes `_fr`, `_de`, `_es`,
`_es_LATAM`, `_it`, `_pt`, `_ja`, `_ko`.

**Les deux stunts de rue de mars 2025**, et c'est la pièce que je garderais si je ne devais
en garder qu'une :
- `marketing/stunt-metro-duolingo-but-for-weight-loss.mp4` — deux personnes en masque de raton et hoodies « CLEAN CRUSH » / « TRASH PANDA » brandissent dans le métro une pancarte en carton : **« DUOLINGO BUT FOR WEIGHT LOSS »**. Le positionnement, écrit au marqueur par la marque elle-même. Légende du post : « New BitePal chapter is coming… ».
- `marketing/stunt-marathon-run-if-you-eat-after-6pm.mp4` — second volet, au bord d'un marathon : « RUN IF YOU EAT AFTER 6PM ».

Aussi : `marketing/feature-graphic-google-play.jpg` (le raton derrière une carte de suivi,
entouré de pomme, haltère, kettlebell et ballon), `marketing/variante-android-track-progress-avant-apres.png`
(un levier de conversion avant/après **absent de la fiche iOS**), les deux descriptions
longues du Play Store en FR et EN, et l'endcard « Tracking shouldn't be difficult ».

## Process

`process/funnel-layout-css-source-des-tokens.css` — **le CSS de production dont sortent tous
les tokens de la section Couleurs.** Gardé pour que la charte reste vérifiable sans refaire
la récolte.

`process/manifeste-des-290-images-du-funnel.json` — le manifeste complet des images du
funnel, avec URL CDN exacte, largeur, hauteur et format pour chacune. 38 seulement ont été
téléchargées, choisies par famille ; les 252 autres (16 photos d'âge par genre et région,
20 avant/après par tranche d'âge, 24 illustrations de type de corps, et toutes les
déclinaisons DE/ES/IT/PT/JA/KO) sont **résolues et tirables** depuis ce fichier.

Pile technique lue dans le code, utile pour situer la fabrication : Astro + Tailwind v4 +
rolldown pour les deux sites, React pour l'îlot du funnel, Tolgee pour la traduction,
Sentry, **GrowthBook pour les A/B tests**, Paddle pour le paiement, AppsFlyer OneLink. Le
CDN de l'éditeur porte le chemin `refacekek` — détail de ton interne.

## Archive

![[archive/planches/planche-quatre-millesimes-2024-a-2026.png]]

**La DA a été refaite entièrement, et le sens du changement est très lisible.** En août 2024,
le raton est **rose**, sur un ciel violet-pervenche et un sol ambre, avec une maisonnette sur
la colline et des cartes pêche. En mai 2025 il est devenu **gris** sur un vert saturé, avec
un badge « Unlock BitePal Plus » rouge. En janvier 2026 le vert s'est adouci, le feuillage
rose et menthe est apparu, le badge est passé à l'orange, et les cadenas ont colonisé les
macros. Trajectoire : d'un univers enfantin coloré vers un produit vert, plus sobre, plus
commercial.

![[archive/planches/planche-icone-pookies-2024-contre-bitepal-2026.png]]

**Le renommage Pookies → BitePal, et le passage du portrait au signe.** L'icône de mai 2024
est un portrait : tête entière, oreilles visibles, yeux ronds symétriques, fond bleu ciel,
marges généreuses. Celle de 2026 est un signe graphique : le masque recadré à outrance
déborde des quatre côtés, un œil se ferme en clin d'œil, deux dents apparaissent, le fond
passe au gris lavande. C'est le geste classique de l'icône qui doit tenir à 40 px sur un
écran d'accueil encombré.

J'ai vérifié le renommage indépendamment sur l'index Wayback : `pookies.app` répondait 200
les 26 mai et 14 juin 2024, puis 301 à partir du 2 août 2024, et redirige encore aujourd'hui
vers `bitepal.app`.

![[archive/planches/planche-millesime-2025-04-captures-play.png]]

**Le millésime avril→décembre 2025 de la fiche Play**, sur le positionnement
« Track calories. Raise virtual pet. » — fonds photo, raton plus rond et couché, et deux
choses disparues depuis : le raton qui **parle dans une bulle de dialogue** sur l'écran de
feedback, et la preuve sociale « Join 10,000+ of happy users ». À comparer au « 11M+ » de
2026.

![[archive/planches/planche-millesime-2025-05-walkthrough.png]]

**Sept arrêts sur image du parcours de mai 2025**, extraits d'un walkthrough vidéo. Deux
trouvailles : la promesse « Achieve your goals 4.2x faster » **existait déjà en mai 2025**
— elle est stable depuis quinze mois —, et il y avait un **paywall de repli** qu'aucune
autre source ne montre : offre unique à −60 %, 1,99 $/mois, sur fond sombre avec confettis,
déclenché après refus du premier prix.

`archive/millesime-2026-02-store-badges-3m-et-webby.png` — même design qu'aujourd'hui, mais
les badges disent « LOVED BY **3M** USERS » et « THE WEBBY AWARDS ». Six mois plus tard le
chiffre affiché est 11M.

**Historique des noms de store**, relevé sur snapshots datés : avril et septembre 2025
« BitePal: AI Calorie Tracker » → décembre 2025 « BitePal: Food Tracker Pet » → août 2026
« BitePal: AI Calorie Counter » (Play) et « BitePal: Food Calorie Tracker » (App Store US).
Le titre FR actuel est « Bitepal: Calcul de Calories IA ».

## Chiffres, et pourquoi ils ne s'accordent pas

Je les rapporte tels quels, sans arbitrer — l'écart est lui-même une information sur la
communication de la marque.

- App Store FR : **4,44** sur 6 972 avis · App Store US : **4,66** sur 53 710 avis
- Site et paywall : « **4.7** average rating » · « **1M** users worldwide »
- Fiche Play, visuel de couverture : « **11M+** utilisateurs » · même visuel en février 2026 : « **3M** users »
- MWM Intelligence : 5 M+ téléchargements · teardown de juillet 2025 : 100 K+ téléchargements et **400 K$/mois**
- Post d'un investisseur historique : « 400 000 downloads in 30 days » et **Webby Awards Honoree** en Health, Wellness & Fitness
- Version 2.28.0 du 25 août 2026, première sortie le 10 juin 2024, 247,9 Mo, iOS 15 minimum, gratuite avec abonnement, 4+

## Sources

- **App Store FR** — les 10 visuels en 1290×2796, l'icône 1024, et toutes les métadonnées d'éditeur : [apps.apple.com/…/id6479529917](https://apps.apple.com/fr/app/bitepal-calcul-de-calories-ia/id6479529917) · changelog via `itunes.apple.com/lookup?id=6479529917&country=fr`
- **Google Play** — [com.pookies.food.ai](https://play.google.com/store/apps/details?id=com.pookies.food.ai) : le feature graphic 1920×1080, les descriptions longues FR et EN, et deux visuels de couverture absents de l'App Store
- **`bitepal.app`** — captures pleine hauteur maison (desktop et mobile), le lockup et le badge lauriers en SVG inline, les `@font-face`, et les couleurs en classes Tailwind de `base-layout.css`
- **`quiz.bitepal.app`** — **la source la plus riche du dossier** : le funnel d'onboarding web, dont la config déclarative de 37 étapes, les tokens sémantiques de `Layout.gnkIzerQ.css`, les 364 icônes SVG, les 17 Lottie, le manifeste des 290 images, et les 5 `.woff2`
- **Uiland.design** — [entrée `bitepal`](https://uiland.design/screens/bitepal/screens/b7a15ddf-e204-4d8a-b5a7-96d43d9f593e) : 245 écrans indexés, millésime v2.5.2.328 daté du 28 janvier 2026, servis sans filigrane en 828×1792 depuis un CDN R2 public. C'est elle qui a donné la quasi-totalité des écrans réels
- **Mobbin** — 3 écrans en 1180×2556 sans filigrane et la vidéo du flow d'onboarding, millésime daté du 15 décembre 2025, via les pages `/explore/screens/<uuid>` rendues côté serveur
- **ScreensDesign** — [showcase et fiche app](https://screensdesign.com/showcase/bitepal-ai-calorie-tracker) : 16 captures en 2160×4670 (onboarding, paywall, scan), plus l'[article paywalls 2026](https://screensdesign.com/articles/mobile-app-paywall-design-examples-2026/) daté du 10 août 2026
- **TikTok officiel [@bitepal.app](https://www.tiktok.com/@bitepal.app)** — 225 900 abonnés, 9 M de likes : les carrousels brandés, les deux stunts de rue de mars 2025, la démo de scan en mouvement, et une créative UGC d'août 2024 qui contient les seules 2 s de l'UI d'origine
- **YouTube — chaîne mrhackio**, [« BitePal app - AI CALORIE TRACKER - how to use »](https://www.youtube.com/watch?v=TF32UeYIc5w) (20 mai 2025) : le walkthrough de 5 min 33 dont sont extraits les 7 arrêts sur image du millésime mai 2025
- **Wayback Machine** — l'index CDX de `pookies.app` (le renommage, vérifié de mon côté) et 6 captures Play du millésime avril 2025
- **`reface.ai`** — le portefeuille de l'éditeur, sa page équipe, la carte produit BitePal et son logotype
- **`rekvizitai.lt`** — [fiche de Reface Lithuania UAB](https://www.rekvizitai.lt/en/company/reface_lithuania) : code 306426593, dates, capital, chiffre d'affaires, effectif
- **LinkedIn @refaceapp** — le post d'annonce du 21 janvier 2025 (« BitePal app is out », « our first wellness app ») et sa couverture de carrousel
- **Growth Hacking Lab** — [« How Bitepal Scaled to $400K/Month in 12 Months »](https://thegrowthhackinglab.com/case-studies/bitepal-400k-revenue-12-months/), Thousif A, 14 juillet 2025 : la stratégie d'acquisition
- **Tinkr** — [« BitePal Review: Cute Raccoon, Terrible Calorie Counting »](https://www.youtube.com/watch?v=jlrfllNBoLM), avril 2026 : la critique argumentée du compromis engagement/précision
- **Mesure de tiers, rangée à part** : la galerie ASO `appshot.gallery` attribue à la fiche les descripteurs *Friendly, Energetic, Informative, Minimalist, Flat Design, Cartoon, White, Black, Green, Sans-Serif*. Ce n'est ni une charte ni un relevé maison — c'est le jugement d'un curateur tiers, utile seulement comme point de comparaison.

## Crédits

- **Reface** — concepteur et éditeur du produit, en interne, pas en agence. Studio d'apps mobiles IA **né à Kyiv**, actif depuis 2018, 300 M+ de téléchargements revendiqués, investisseurs **Andreessen Horowitz** et **Roosh**. `reface.ai` liste BitePal dans son propre portefeuille (aux côtés de Reface, Revive, Restyle, Ink ai, Lightly, Letsy, Memomet) et le compte officiel annonce BitePal comme « **our first wellness app** » — c'est le premier écart du studio hors divertissement, ce qui explique une DA très éloignée du reste de son catalogue. Effectif estimé à 200-800 personnes à Kyiv (DOU.ua). → [reface.ai](https://reface.ai/)
- **REFACE LITHUANIA UAB** — l'entité qui édite, et seulement cela. Société lituanienne 306426593, fondée le 19 septembre 2023, siège Gynėjų g. 4-333 à Vilnius, capital 20 000 €. Deux chiffres résument son rôle : **6 359 937 € de chiffre d'affaires en 2025 pour un seul salarié assuré**, et une perte nette de 1 425 529 €. Gérante : **Renata Kratkovska-Gušča** — fonction administrative, aucun rôle design. Filiale à 100 % d'une société du groupe, dont le nom n'est pas dans la fiche gratuite du registre.
- **Marko Ivanyk** — *Head of Design* chez Reface, d'après la page équipe officielle. **Il dirige le design des huit produits du studio ; rien ne l'attache à BitePal en particulier, et rien ne dit qu'il a dessiné la mascotte.** À citer comme responsable de la fonction, pas comme auteur.
- **Val Pieŭnioŭ** / **The Screenshot First Company** — visuels de la fiche App Store (ASO), pas la mascotte. Un shot Dribbble s'intitule exactement « App Store Screenshots | BitePal: Food Calorie Tracker ». **Confiance moyenne** : ces studios publient aussi bien des commandes réelles que des refontes spéculatives, et la page étant inaccessible je n'ai pas pu lire le texte de l'auteur pour trancher. → [dribbble.com/mamkindesigner](https://dribbble.com/mamkindesigner) · [dribbble.com/thescreenshotfirstcompany](https://dribbble.com/thescreenshotfirstcompany)
- **L'illustrateur du raton laveur : non identifié.** C'est le trou principal du dossier, et il est structurel. Behance ne renvoie que des analyses tierces, le compte `behance.net/reface` est vide, Dribbble n'a aucun shot de mascotte, il n'existe aucun compte d'équipe Reface sur ces plateformes, et les offres d'emploi publiques de l'éditeur ne nomment personne. **Aucun nom n'est proposé ici plutôt qu'un nom douteux.** Pour un produit dont l'identité repose entièrement sur un personnage, c'est le manque le plus regrettable.
- **Dirigeants nommés chez Reface**, pour situer la structure : Ivan Altsybieiev et Anton Volovyk (Co-CEO), Oles Petriv (CTO), Yaroslav Boiko (CAO), Dmytro Shamutylo (CFO), Hlib Petrov (Head of Creative Marketing & Comms), Stanislav Berkutov (Head of User Acquisition).
- **mrhackio** (YouTube) — le walkthrough de mai 2025 dont sont tirés les arrêts sur image du millésime.
- **Bases d'UI créditées pour leurs écrans**, comme l'exige la règle du vault : **Uiland.design**, **Mobbin**, **ScreensDesign**.

## Pourquoi je l'aime

Parce que c'est un cas d'école de **DA qui porte une mécanique de rétention** sans jamais
avoir l'air de le faire. Le personnage fait tout le travail émotionnel, et pendant ce temps
l'interface reste un design system propre et neutre — trois états sémantiques, une encre,
un rayon de 32 px. La leçon est là : on peut être chaleureux sans teinter toute
l'interface, à condition d'avoir un personnage assez fort pour tenir la chaleur à lui seul.

Et parce que le dossier documente une **refonte complète assumée** : le raton rose sur
ciel violet de 2024 et le raton gris sur vert de 2026 sont deux produits différents, avec
deux ans d'écart et un renommage de marque au milieu.

## À réutiliser pour

- **Un système de mascotte à états** : la grille des humeurs (heureux, hilare, triste, endormi, survitaminé) et la façon dont chaque état est accroché à un événement de données. Le rig Lottie est dans le dossier, calques nommés.
- **Une charte minimale mais complète** : le modèle « une encre en opacités + trois états sémantiques en plein et en 10 % » est directement transposable, et il tient en quinze tokens.
- **Un onboarding long qui se justifie** : 37 étapes, mais chacune produit une donnée qui alimente le récapitulatif de plan. La config déclarative est lisible dans le dossier.
- **Une boucle de confiance dans une fonction d'IA** : avertissement, notation de la précision, taxonomie de signalement. À reprendre tel quel pour toute interface qui expose une inférence.
- **Un ton de voix à la première personne** porté par un personnage, avec une police manuscrite comme second niveau de lecture par-dessus l'UI.
- **Un stunt de positionnement** : écrire sa proposition de valeur au marqueur sur un carton et la filmer coûte presque rien, et « Duolingo but for weight loss » a fait plus pour dire ce qu'est le produit que n'importe quelle landing.

## Mots-clés

compteur de calories, calorie counter, calorie tracker, suivi alimentaire, food tracking, nutrition, macros, macronutriments, scan de repas, food scan, photo de repas, reconnaissance d'image, IA, AI, jeûne intermittent, intermittent fasting, suivi de l'eau, hydratation, poids, perte de poids, weight loss, IMC, BMI, score nutritionnel, plan de repas, meal plan,
mascotte, mascot, raton laveur, raccoon, trash panda, animal virtuel, virtual pet, tamagotchi, compagnon, buddy, jauge de vie, health meter, coeurs, streak, série, monnaie in-app, BiteCoins, boutique, accessoires, skins, personnalisation, avatar, gamification, rétention, retention loop,
Bricolage Grotesque, Inter, Nanum Pen Script, manuscrit, hand-lettered, grotesque grasse, display bold, illustration plate, flat illustration, paysage illustré, vert, green, bleu ciel, sky blue, pastel, cartes blanches, coins arrondis, rayon 32px, tokens semantiques, design tokens, Tailwind, Astro, Lottie, rig, riggé,
onboarding long, funnel, quiz, paywall, soft paywall, paywall de repli, downsell, essai gratuit, free trial, ATT, App Tracking Transparency, cadenas, locked, freemium, upsell, dark pattern, carte a gratter, scratch card, roue de la fortune, GrowthBook, A/B test, ASO, Apple Search Ads, acquisition payante, UGC, TikTok, stunt, street marketing,
Reface, Reface Lithuania UAB, Kyiv, Ukraine, Vilnius, Lituanie, a16z, Roosh, Pookies, renommage, rebranding, millesime, refonte, Duolingo but for weight loss, Webby Awards

---
[[_APPS|← Apps]] · [[_INSPIRATION|← Inspiration]]
