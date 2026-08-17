---
type: univers
univers: BitePal
categorie: app
secteur: santé
annee: 2024 (sortie App Store le 10 juin) — v2.26 en août 2026
createurs: "Reface Lithuania UAB (éditeur) — équipe interne « Pookies » (bundle Android com.pookies.food.ai) — auteur du character design non crédité publiquement"
source: https://bitepal.app
couleur_principale: corail #FC7059
couleurs: ["#262626", "#4BA85C", "#FC7059", "#FFFFFF", "#C9C9D9", "#FCDBE4", "#AAF0DB", "#ABB1F0", "#F0ACDF", "#FFE1A6", "#FFD95D", "#A290FE", "#EDEDF2"]
mood: [playful, bold, organic]
tags: [inspiration, univers, app, ui, mascotte, gamification, illustration, playful, food]
---

# BitePal

> Un compteur de calories par IA dont tout l'édifice repose sur un raton laveur. L'app scanne une photo de repas et renvoie des macros — fonctionnellement, c'est MyFitnessPal ; émotionnellement, c'est un Tamagotchi. Ce dossier existe pour la leçon de design produit qu'il contient : comment un seul personnage, décliné en une dizaine d'humeurs, remplace toute la couche de motivation d'une app de santé — et comment une charte pastel très douce encaisse un sujet (le poids, la culpabilité alimentaire) qui d'habitude produit des interfaces froides et culpabilisantes.

**Sources principales :** [bitepal.app](https://bitepal.app) (site officiel — logo vectoriel, tokens CSS, assets) · [App Store US](https://apps.apple.com/us/app/bitepal-food-calorie-tracker/id6479529917) (icône 1024, 10 screenshots 1290×2796) · [Google Play](https://play.google.com/store/apps/details?id=com.pookies.food.ai) (variante Android, feature graphic) · [Screensdesign — showcase BitePal](https://screensdesign.com/showcase/bitepal-ai-calorie-tracker) (captures de l'onboarding, du paywall et du produit réel)

---

## Le système en bref

- **Un personnage, pas une illustration.** Le raton n'illustre pas l'app : il *est* l'app. Il a un nom donné par l'utilisateur (Bubba, Manuela dans les captures), quatre cœurs de vie, une garde-robe achetable en monnaie interne, et une humeur qui change selon ce que vous mangez. Le tracking devient une conséquence de s'occuper de lui.
- **Le trait avant la couleur.** Contour noir `#262626` épais et constant, formes rondes, aucun dégradé sur le personnage. La fourrure est un gris **légèrement violet** (`#C9C9D9`), jamais un gris neutre — c'est ce qui empêche le personnage de tomber dans le terne.
- **La scène change de couleur, pas le personnage.** Le raton est toujours identique ; c'est le fond derrière lui qui porte l'état émotionnel — vert jardin en régime normal, violet sur l'écran sport, corail brûlant quand le streak est en danger. Un seul asset personnage, N états lisibles.
- **Des titres énormes, tout le reste minuscule.** Les compositions store poussent une grotesque condensée ultra-grasse sur 2-3 mots (« Keep your streak »), et laissent l'écran d'app respirer en dessous. Ratio typographique très violent, assumé.
- **Pastel saturé, jamais délavé.** Menthe, lavande, rose bubblegum, sable — la palette d'accents est franchement colorée mais toujours en zone claire. Aucun noir profond, aucune couleur sourde.
- **Le corail fait tout le sale boulot.** C'est la seule couleur agressive du système, réservée à l'urgence (streak qui va tomber, alerte). Sur 18 écrans relevés il n'occupe que 1 % de la surface — mais 10 % de l'écran « streak ». Une couleur qu'on ne voit presque jamais, donc qui marche quand elle arrive.

---

## Branding

Le site officiel sert son identité **en SVG inline** : le lockup complet et le wordmark sont donc récupérés en vectoriel, aux valeurs exactes.

![[logo-lockup-mascotte-wordmark.svg]]

Le lockup officiel — tête du raton + wordmark. Quatre couleurs seulement dans tout le fichier : `#262626`, `#C9C9D9`, `#FCDBE4`, `#4BA85C`.

![[logo-wordmark.svg]]

Le wordmark seul, tel qu'il apparaît dans le header du site. Lettrage très gras à contreformes fermées, et le **point du i remplacé par une pousse à deux feuilles** en vert `#4BA85C` — le seul endroit de toute l'identité où le vert apparaît en signature. C'est le raccourci « nourriture / végétal » de la marque, posé une fois et jamais répété.

![[app-icon-1024.png]]

L'icône App Store en 1024 : la tête seule, cadrée serrée, sans wordmark. Elle tient à cette taille parce que le masque noir du raton fait office de forme forte — même logique qu'un logo animalier réduit à sa silhouette.

![[play-feature-graphic.png]]

Le feature graphic Google Play (1024×500).

![[play-icon.png]] · `favicon.ico` — déclinaisons de l'icône.

**Typographie du site** (relevée dans les `@font-face` de `bitepal.app`) :

| Rôle | Police | Détail |
| --- | --- | --- |
| Titres | **Bricolage Grotesque** | poids 700, `font-stretch: 75%–100%` (axe de largeur variable exploité) |
| Texte courant | **Inter** | variable 100–900 |

Les titres des compositions store sont dans la même famille de grotesque condensée très grasse — c'est ce qui donne leur signature typographique aux visuels marketing.

---

## Couleurs

Deux origines distinctes, jamais mélangées : ce que la marque **déclare** (valeurs lues dans le SVG du logo et dans la feuille de style du site officiel) et ce que les écrans **utilisent vraiment** (relevé pixel par pixel avec `palette.py` sur 18 captures store). BitePal ne publie aucune brand guideline — il n'y a donc ni Pantone ni CMJN à reporter, et les noms de couleurs ci-dessous sont descriptifs, pas officiels.

![[INSPIRATION/UNIVERS/bitepal/couleurs/palette-coeur-de-marque.svg]]

![[palette-mascotte.svg]]

![[palette-accents-site.svg]]

![[INSPIRATION/UNIVERS/bitepal/couleurs/palette-neutres.svg]]

**Cœur de marque** — source : SVG du logo + tokens CSS de bitepal.app

| Nom (descriptif) | Hex | Usage |
| --- | --- | --- |
| Ink | `#262626` | wordmark, titres, bouton primaire plein, contour de la mascotte |
| Leaf Green | `#4BA85C` | la pousse du logo ; variante `#4CA75C` dans un gradient CSS |
| Coral | `#FC7059` | streak, alertes, cœurs — l'accent chaud de la marque |
| White | `#FFFFFF` | cartes |
| Hot Orange | `#FF5533` | accent plus dur, usage ponctuel |
| Night Ink | `#1E1E2F` | noir légèrement bleuté, fonds sombres |

**La mascotte** — source : SVG du lockup officiel

| Nom (descriptif) | Hex | Usage |
| --- | --- | --- |
| Fur Lavender Grey | `#C9C9D9` | fourrure — gris violacé, jamais neutre |
| Mask Ink | `#262626` | masque, oreilles, contour |
| Muzzle Pink | `#FCDBE4` | langue et intérieur de la bouche |
| Belly White | `#FFFFFF` | tache du ventre, en forme de cœur |

**Accents pastel** — source : tokens CSS du site

`#AAF0DB` menthe · `#ABB1F0` lavande · `#F0ACDF` bubblegum · `#FFE1A6` sable · `#FDF6E7` crème · `#FFE7E1` pêche · `#E9F0FF` bleu glacé

**Neutres** — source : tokens CSS du site

`#EDEDF2` · `#BBBCBF` · `#8A8B8F` · `#707173`

### Ce que le relevé révèle

![[palette-observee-ecrans.svg]]

Relevé `palette.py` sur les 18 captures store (`releve --top 18 --step 4`), part moyenne de surface par image :

- **Trois couleurs tiennent 20 % de la surface** : `#F4FCFF` (7,45 %), `#262626` (6,79 %), `#FFFFFF` (6,19 %). Le fond n'est jamais un blanc pur — il tire systématiquement vers le bleu, et le blanc pur est **réservé aux cartes posées dessus**. C'est ce décalage minuscule qui fait décoller les cartes sans une seule ombre portée marquée.
- **Le personnage n'occupe que 2 % de l'écran** (`#CAC9D9`, la fourrure). Il domine la perception sans dominer la surface : contour noir épais + fond coloré derrière lui, c'est le contraste qui fait le travail, pas la taille.
- **Le grand dégradé bleu ciel** (`#B9DFF2` → `#C3E4F5` → `#CDE9F7` → `#E2F3FB`, ~7 % cumulés) est le fond des compositions App Store — **aucune de ces quatre valeurs n'est un token du site**. C'est une couleur de vitrine store, pas une couleur de marque : à ne pas recopier en croyant reprendre la charte.
- **Deux couleurs présentes à l'écran et absentes du CSS** : le violet `#A290FE` / `#CBC2FB` de la scène « calories brûlées », et le jaune `#FFD95D` de la barre de scan. Les couleurs d'état de l'app vivent en dehors de la charte web.
- **Les accents ne dépassent jamais 1 %** en moyenne (corail 1,09 %, vert 0,51 %, rose 0,49 %) — sauf sur l'écran qui les concerne, où ils explosent (corail à 10,26 % sur le streak, rose à 3,56 % sur l'hydratation). Un écran = une couleur, et le reste reste neutre.

---

## Character design

Un seul modèle de raton, décliné en humeurs. Portraits recadrés depuis les captures en pleine résolution.

![[mascotte-clin-doeil.png]]

L'expression canonique : clin d'œil, patte à la joue, bouche ouverte. Noter la construction de l'œil ouvert — pupille noire pleine + **deux points blancs de tailles différentes**, et un arc blanc épais sur la paupière supérieure. C'est ce arc, pas la pupille, qui donne le regard.

![[mascotte-essouffle-sport.png]]

Version essoufflée / à la corde à sauter : sourcils froncés en accent circonflexe **fusionnés au masque**, yeux réduits à deux fentes blanches, souffle en volute bleue. Le masque noir sert de porte-expression — pas besoin de sourcils séparés.

![[mascotte-boudeur-streak.png]]

La version boudeuse, sur la notification d'écran verrouillé quand le streak va tomber : sourcils tombants, bouche en accent grave, patte sous le menton, fond corail. Le seul moment où le personnage exprime la déception — jamais l'app elle-même.

![[mascotte-outfit-manuela.png]]

Le système d'habillage : nœud à pois, lunettes surdimensionnées, collier de fleurs. Les accessoires sont dessinés au **même contour et au même poids de trait** que le personnage, ce qui les fait tenir ensemble quelle que soit la combinaison. Ils se posent en couches indépendantes (tête / yeux / cou / fond) — d'où les quatre onglets de la boutique.

Grille d'humeurs observée dans le produit : joyeux, clin d'œil, gourmand, essoufflé, boudeur, contrarié, endormi, célébration (confettis), « super-héros » sur le paywall. Chacune est un asset plein corps, jamais un montage.

---

## UI

### Le produit réel

Captures du produit tel qu'il tourne (source : Screensdesign — **le watermark « screensdesign » en haut de ces huit images n'est pas dans l'app**).

![[flow-home-dashboard.webp]]

Le home : le raton en scène plein cadre occupe le tiers haut, son nom et ses cœurs de vie juste dessous, puis les macros dans une carte blanche remontée par-dessus. Barre d'onglets flottante en pilule, bouton `+` noir plein en flottant. La hiérarchie est inversée par rapport à toutes les apps de tracking : **le personnage passe avant les chiffres.**

![[flow-scanner-camera.webp]]

Le scanner : caméra plein écran, viseur circulaire adouci, deux chips `Meal` / `Label` pour choisir le mode. Trois entrées seulement en bas (Gallery, déclencheur, Type).

![[flow-resultat-scan-macros.webp]]

Le résultat de scan — et le moment clé de l'app : le raton apparaît en petit format sur le côté et **commente le repas dans une bulle** (« Veggies and beans? My tummy is doing a happy dance! ») avant que les macros n'apparaissent. La donnée arrive après la réaction. En dessous, macros à trois couleurs et ingrédients en chips validables.

![[flow-onboarding-adoption-raton.webp]]

L'onboarding traite l'arrivée comme une **adoption** : « This raccoon is now your virtual pet », entouré de déchets alimentaires dessinés (banane, arête, trognon) — le clin d'œil au raton fouilleur de poubelles, assumé dès la première minute.

![[flow-onboarding-intro-scan.webp]] · ![[flow-onboarding-resume-bmi.webp]] · ![[flow-onboarding-attribution.webp]]

Le reste du parcours : carte produit avec calories flottantes en bulles, résumé personnalisé (IMC sur une échelle en dégradé, verdict en carte verte), question d'attribution. Le parcours complet compte **une trentaine d'étapes** — long, et c'est la principale critique qui lui est faite.

![[flow-paywall-plus.webp]]

Le paywall « BitePal Plus » : raton en super-héros sur fond vert, promesse chiffrée (« Achieve your goals **4.2x** faster », le multiplicateur en vert), essai 3 jours puis 35,99 $/an affiché barré depuis 59,99 $ et redécoupé en « 2,99 $ per month », puis tableau comparatif Free / Plus. Bouton d'action noir flottant, ancré bas. Paiement web géré par **Paddle** (script chargé sur le site).

### Les compositions App Store

Dix visuels 1290×2796, une fonctionnalité par visuel, titre en 2-3 mots.

![[appstore-01-scanner.png]] · ![[appstore-02-scan-repas.png]] · ![[appstore-03-progres.png]]

![[appstore-04-calories-brulees.png]] · ![[appstore-05-water.png]] · ![[appstore-06-plans.png]]

![[appstore-07-fasting.png]] · ![[appstore-08-challenges.png]] · ![[appstore-09-outfits.png]]

![[appstore-10-streak.png]]

Deux méritent le détour :

- **`appstore-04-calories-brulees`** — la scène passe en violet et le raton saute à la corde, essoufflé. Deux notifications iOS empilées sont composées **par-dessus** le mockup, débordant du cadre du téléphone. Composition en couches qui casse le rectangle.
- **`appstore-10-streak`** — l'écran verrouillé iOS comme argument de vente : le fond d'écran vire au corail, la Live Activity affiche un compte à rebours (« 2:29:16 — Your last chance! ») et le raton boudeur. Vendre la notification plutôt que l'app.

### La variante Android

![[play-01.png]] · `play-02.jpg` → `play-08.jpg`

Même système, arguments différents : fond vert au lieu du bleu, plats photographiés flous en arrière-plan, et une revendication de volume (« Loved by 11M+ users ») absente de la version iOS.

---

## Illustrations

![[site-og-image.jpg]] — l'image Open Graph du site.

![[play-editorial-banner.jpg]] — bannière éditoriale 1920×1080 (mise en avant Google Play).

---

## Site officiel

Assets récupérés depuis `bitepal.app` (dossier `site/`) : `hero-bg.webp`, `feature-1/2/3.webp`, `review-1/2/3.webp`, `badges-laurels.svg`. Le site est une page unique Astro, très courte : hero, trois features, trois reviews, badges de stores. Il ne fait que rediriger vers les stores — toute la marque vit dans l'app.

---

## Artistes & crédits

- **Éditeur : Reface Lithuania UAB.** Même entité que **Reface**, l'app de face-swap par IA, qui a annoncé le lancement de BitePal sur son [LinkedIn](https://www.linkedin.com/company/refaceapp). Le bundle Android `com.pookies.food.ai` révèle un nom d'équipe interne : **Pookies**.
- **Character design : non crédité publiquement.** Aucun nom d'illustrateur, d'AD ou de studio n'apparaît sur le site, les stores, ou dans les recherches — pas de page ArtStation ou Behance rattachée au raton. Point à recreuser si l'auteur sort de l'ombre ; c'est le seul manque réel de ce dossier.
- **Attention aux fausses pistes :** `mwm.ai` et `homefromcollege.com` publient des fiches BitePal mais sont des **sites éditoriaux tiers** (MWM le précise explicitement) — ils ne sont ni éditeurs ni ayants droit. Le domaine `bite-pal.com` n'est pas le site officiel : c'est `bitepal.app`.

**Chiffres, en l'état d'août 2026** — ils ne concordent pas d'une source à l'autre, donc à citer avec leur origine :

| Source | Note | Volume |
| --- | --- | --- |
| API App Store US | 4,66 / 5 | 52 968 notes |
| Google Play | 4,53 / 5 | 382 097 notes · 1 M+ téléchargements |
| Site officiel (auto-déclaré) | 4,7 / 5 | « 1M users worldwide » |
| Screenshots Play (marketing) | — | « Loved by 11M+ users » |

Sortie App Store le **10 juin 2024**, version 2.26.0 au **10 août 2026** — deux ans de cadence de mise à jour très soutenue.

---

## Pourquoi je l'aime

- **La donnée arrive après l'émotion.** Le raton réagit au repas avant que les macros ne s'affichent. Dans une catégorie qui n'affiche que des chiffres, inverser cet ordre est un choix de design produit fort, et copiable ailleurs (finance, apprentissage, santé).
- **Un asset, dix états.** Le personnage ne bouge pas de style ; c'est la scène de fond qui porte l'état. Système économique à produire, immédiatement lisible à l'usage.
- **Le masque noir comme porte-expression.** Toute l'expressivité passe par la déformation d'une forme noire déjà présente dans l'anatomie du personnage. Excellente contrainte de character design.
- **Une palette qui désamorce un sujet dur.** Pastels saturés, aucun rouge sauf en urgence réelle, pas un seul gris froid. Une app de poids qui ne ressemble pas à un dossier médical.
- **Le contraste typographique des visuels store.** Trois mots gigantesques en grotesque condensée, puis un écran calme. Recette efficace pour une vitrine.
- **La notification comme argument de vente.** Vendre l'écran verrouillé plutôt que l'app : peu de monde le fait.

## À réutiliser pour

- Projet : [[ ]] — système de mascotte à humeurs pour une app produit (un personnage, N fonds d'état).
- Projet : [[ ]] — onboarding « adoption » : faire nommer quelque chose à l'utilisateur avant de lui demander ses données.
- Projet : [[ ]] — feedback conversationnel avant affichage de données (bulle du personnage → chiffres).
- Projet : [[ ]] — direction pastel saturée sur un sujet anxiogène (santé, finance, admin).
- Projet : [[ ]] — compositions de screenshots App Store : titre 2-3 mots, ratio typographique extrême, notifications composées par-dessus le mockup.
- À rapprocher de [[duolingo]] : même famille (mascotte + streak + gamification), mais Duolingo publie tout son système et BitePal ne publie rien — deux modèles opposés de gestion de marque.

## Mots-clés

BitePal, bite pal, raton laveur, raccoon, raccoon mascot, mascotte app, virtual pet, animal de compagnie virtuel, tamagotchi, pet app, gamification, gamified app, streak, série, flamme, cœurs de vie, lives, monnaie in-app, outfits, accessoires, dress up, habillage de personnage, character design, character system, humeurs, expressions, mood states, contour épais, thick outline, chunky illustration, flat illustration, kawaii, cute, mignon, playful, pastel, pastel saturé, menthe, lavande, corail, coral, vert feuille, gris violacé, calorie tracker, compteur de calories, calories, macros, macronutriments, nutrition, food tracking, food scanner, scanner de repas, AI scanner, photo de repas, jeûne intermittent, intermittent fasting, hydratation, water tracking, poids, weight loss, santé, health app, fitness, wellness, onboarding, onboarding long, quiz onboarding, adoption, paywall, subscription, essai gratuit, free trial, Paddle, App Store screenshots, store composition, feature graphic, Live Activity, notification écran verrouillé, lock screen widget, dashboard, bottom bar flottante, pilule, carte blanche, bulle de dialogue, speech bubble, Bricolage Grotesque, Inter, grotesque condensée, titre ultra gras, Reface, Reface Lithuania, Pookies, MyFitnessPal alternative, Duolingo pour la bouffe, Gen Z app, Bubba, Manuela
