---
name: eco
description: Transforme les pages « eco gestion » du vault (Licence 1 Économie & Gestion, Angers) en fiches avec lesquelles on révise vraiment, pour réussir les examens de fin d'année. Intègre les notes d'amphi brutes déposées dans `eco gestion/_brut/` (fautes, structure en vrac, phrases interrompues) en fiches complètes, et améliore les fiches existantes. Chaque fiche est bâtie sur ce qui fait retenir : questions à réponses repliées pour se tester, tableaux de paires confusables, méthodes pas à pas, cartes Anki taillées sur la forme des questions relevée dans les annales (`~/Documents/L1/<matière>/Annales/`), les informations capitales manquantes ajoutées et tracées (marqueur ➕), et les trous restants signalés. Corrige la langue et le markdown, répare liens et ancres. Ne touche jamais un chiffre, une formule, un nom d'auteur : ce qui cloche est signalé, pas corrigé. Périmètre = toute page taguée `L1-eco-gestion`, dans `eco gestion/`, ou liant `[[00 - Plan L1 Angers]]`. Tourne aussi seul toutes les heures (LaunchAgent `com.sacha.eco-fiches`) : une page par passage, un commit par passage. Intègre aussi les sources officielles quand Sacha en dépose une (PDF de slides, syllabus) : elles font autorité sur ses notes, sont marquées 🎞️, ferment les trous et font redessiner — ou découper — les schémas du prof. Confronte enfin chaque fiche au **cours de référence de `~/Documents/L1`** (les cours des années précédentes, toutes matières) : il corrige le vocabulaire, donne les vraies définitions, raccourcit les explications, mais n'ajoute jamais un chapitre ni une grande partie — le prof a pu changer son cours, donc une partie absente de ses notes part dans « À vérifier ». À utiliser quand Sacha dit « corrige / synthétise / améliore mes cours d'éco », « fais-moi les fiches de révision », « mets mes notes d'amphi au propre », « voilà les slides / le syllabus », ou quand le passage horaire se déclenche.
---

# /eco — Des cours d'éco gestion avec lesquels on révise

Objectif unique, fixé par Sacha le 7 septembre 2026 : **qu'il apprenne plus
facilement son cours et qu'il réussisse ses examens en fin d'année.** Tout ce
qui ne sert pas ça est du décor.

Ce qui en découle : une fiche n'est pas un beau résumé, c'est un outil avec
lequel **on se teste**. Les six leviers qui font réussir un examen, et le bloc
de fiche que chacun produit, sont dans **`references/apprendre.md` — à lire
avant de toucher une page.** La forme exacte, avec des avant/après pris dans ses
vraies pages, est dans **`references/forme-fiche.md`**.

Le contenu de cours est **du savoir sourcé** (le prof, la maquette, l'INSEE).
D'où la règle qui ne bouge jamais : **aucun chiffre, aucune formule, aucun nom
d'auteur ne se corrige en silence.** Ce qui cloche se signale dans la page.

## Deux populations, deux traitements

```
python3 .claude/skills/eco/etat.py --liste
```

**Les bruts** — `eco gestion/_brut/*.md` : ses notes d'amphi telles qu'il les a
prises. C'est la **source** : elle ne se met jamais en fiche sur place, elle
produit une fiche à côté, dans `eco gestion/`, dont le frontmatter porte
`source: _brut/<nom>.md`. Un brut sans fiche est **prioritaire sur tout le
reste** : c'est du cours qui n'est pas encore révisable.

**Depuis le 9 septembre 2026, le brut se corrige — mais uniquement sur la
forme.** Sacha l'a demandé : « corrige aussi le .md de base, juste l'orthographe
et la syntaxe ». Le mot **juste** est la règle : on répare les fautes, les
accents, la ponctuation et la syntaxe markdown cassée, **ligne par ligne, à leur
place**. Tout le reste du brut est intouchable — pas une ligne ajoutée ou
supprimée, rien de déplacé, de fusionné, de renuméroté, d'explicité, et **aucun
nom propre ni sigle retouché** (`ester duflot`, `gary becker`, `smic`, `pib`
restent tels qu'il les a écrits : leur graphie se signale dans la fiche, elle ne
se corrige pas). La restructuration, elle, a sa page à côté : c'est la fiche.

**Les fiches** — les pages du vault (tag `L1-eco-gestion`, dossier
`eco gestion/`, ou lien vers le hub) : à corriger et à améliorer.

Exclus d'office : `notes/` (l'app tr4de, c'est `/notes` qui s'en occupe),
`INSPIRATION/`, `INBOX/`, tout dossier et tout fichier commençant par `_`. Une
page portant un `tr4de-id` est écartée et annoncée : la synchro la réécrirait.

## Deux façons d'être appelé

- **À la main** — « corrige mes cours d'éco », « mets telle page en fiche ». On
  peut traiter plusieurs pages dans le même passage, séquentiellement.
- **Par le LaunchAgent, toutes les heures** — le cas courant. Alors : **une
  seule chose par passage**, celle que `--suivant` désigne, et on s'arrête.

```
python3 .claude/skills/eco/etat.py --suivant
```

Il répond `rien`, ou la cible avec sa `nature:` (`brut à intégrer` ou `fiche à
améliorer`) et sa raison. L'ordre de priorité :

1. un **brut** sans fiche, ou modifié depuis sa dernière intégration ;
2. une **fiche modifiée** par Sacha depuis le dernier passage ;
3. une **fiche jamais traitée** ;
4. rien d'autre — une fiche traitée et inchangée **ne se retraite pas**.

Le point 4 est ce qui empêche le passage horaire de réécrire les mêmes pages 24
fois par jour. Rattrapage manuel : `--suivant --relance`.

Une page ou un brut touché il y a moins de **10 minutes** est reporté : il est
probablement en train d'écrire dedans, on n'écrit pas par-dessus lui.

Quand `etat.py` dit `rien`, le passage s'arrête là — une ligne de récap suffit.

## Le cours est le cours — on ne sépare pas la parole du prof

Une fiche peut mélanger trois provenances : les **notes d'amphi** de Sacha, les
**slides et le syllabus** du prof, et les **compléments** tirés du programme.
Les deux premières sont **la même chose — le cours** : elles se fondent dans un
texte continu, sans marque, sans « d'après la slide 13 », sans « le prof dit ».

C'est une correction explicite de Sacha, le 8 septembre 2026 : « j'aime pas le
fait que les dires ou les phrases du prof soient séparés avec l'emoji, modifie
juste les défs, les mots manquants, vocabulaire par le bon ». Une fiche hachée
par des marques de source ne se lit pas comme un cours, et c'est un cours qu'il
révise.

| Source | Dans le corps | Ce qu'on en fait |
| --- | --- | --- |
| **Slides et syllabus** | fondues, **sans marque** | La définition remplace la paraphrase, le mot juste remplace le mot approximatif, la phrase coupée est complétée |
| **Notes d'amphi** | fondues, **sans marque** | Gardées comme squelette ; ce qui diverge du prof est corrigé, pas commenté sur place |
| **Cours de référence** (`~/Documents/L1`, année dernière) | fondu **sans marque** quand il corrige un mot, une définition, une tournure | Il **précise** ce que Sacha a écrit ; il n'apporte jamais une partie que ses notes n'ont pas — voir la section suivante |
| **Compléments** hors cours | **➕** | Seule chose encore marquée : ça ne vient d'aucune source du cours |

Ce qui remplace les marques, c'est **un bloc de traçabilité en fin de fiche** :

```md
> [!success]- Ce que les slides ont corrigé dans tes notes — 11 points
> Le corps de la fiche est à jour : ces lignes disent seulement ce qui a bougé.
>
> **Vocabulaire remis au mot du cours**
> - Les ressources sont **informationnelles**, pas « immatérielles » (§ 1).
> **Chiffres tranchés**
> - ETI : le seuil est < 5 000 salariés, et le nombre d'ETI est 7 442, pas 7400.
```

Trois règles qui en découlent :

- **On corrige le mot, on ne commente pas la correction dans le cours.**
  « récentes » devient « fréquentes » à sa place, et la ligne part dans le bloc
  de traçabilité — pas dans une incise au milieu du paragraphe.
- **Un trou fermé par les slides sort de `À vérifier`** et rejoint ce bloc, avec
  les deux valeurs en conflit : ça garde les chiffres, que `verifie.py` refuse
  de voir disparaître de la page.
- **Une seule marque survit dans le corps, le ➕.** Il ne signale plus « ce que
  le prof n'a pas dit mot pour mot » mais « ce qui ne vient d'aucune source du
  cours » — donc à confirmer en amphi.

**Le compteur `ajouts:` ne compte que les ➕.** Donc le caractère ➕ ne s'écrit
jamais dans une phrase explicative : on dit « le plus vert en tête de ligne »,
sinon `verifie.py` compte des marqueurs qui n'en sont pas.

## Le dossier `~/Documents/L1` — le cours de référence, jamais le cours

**Règle posée par Sacha le 11 septembre 2026.** `~/Documents/L1` contient les
cours des quatorze matières de la L1 : les diaporamas des profs, les prises de
notes d'anciennes promos, les annales. **Tout y date d'une année antérieure**
(25-26 et avant). Le prof a pu changer son plan, sa numérotation, ses exemples,
voire couper un chapitre. Ce dossier sert donc à **corriger ce que Sacha a
écrit**, pas à écrire la fiche à sa place.

### L'ordre est non négociable : ses notes d'abord

1. **Lire ce que Sacha a écrit** — le brut, la fiche, le cahier. C'est lui qui
   fixe le plan, les parties, ce qui est dans le cours de cette année.
2. **Ouvrir ensuite le cours de référence** de la même matière, et le confronter
   section par section à ce qu'il a écrit.
3. **Corriger dans son texte**, à sa place. La fiche garde **sa** structure.

Une fiche qui suivrait le plan du dossier de référence au lieu de ses notes
serait le cours d'un autre, d'une autre année.

### Rang des sources, du plus fort au plus faible

| Rang | Source | Autorité |
| --- | --- | --- |
| 1 | **Slides et syllabus de cette année**, déposés par Sacha dans `eco gestion/fichier/` | **Pleine.** Tranchent un mot, un chiffre, une date — voir le bloc `[!success]` |
| 2 | **Ses notes d'amphi** (`_brut/`, cahier) | Elles fixent le **périmètre** : ce qui est au programme cette année |
| 3 | **`~/Documents/L1`** — diaporamas et notes d'une promo antérieure | **Limitée au mot.** Précise, reformule, raccourcit ; n'ajoute ni partie ni valeur |
| 4 | **Programme officiel de l'UE** | Repère les trous, ne remplit rien sans `➕` |

Un conflit entre le rang 1 et le rang 3 se tranche toujours pour le rang 1,
sans discussion : les slides de cette année sont le cours.

### Ce que le cours de référence a le droit de faire

- **Corriger le vocabulaire** : le terme exact remplace le terme approximatif,
  à sa place, sans incise.
- **Donner la vraie définition** là où ses notes ont une paraphrase de mémoire.
- **Raccourcir** une définition ou une explication qui traîne — mais **au cas
  par cas** : on prend la version courte quand elle dit la même chose en moins
  de mots, on garde la longue quand la courte perd une nuance. Dans le doute,
  on garde ce qu'il a écrit.
- **Compléter une phrase interrompue**, finir un exemple coupé en plein vol.
- **Nommer** l'auteur, le modèle ou le concept que ses notes désignent
  vaguement (« le type qui a fait la pyramide » → Maslow).
- **Ajouter une information manquante à l'intérieur d'une section qui existe
  déjà** — marquée `➕` et comptée dans `ajouts:`, comme tout complément.

### Ce qu'il n'a pas le droit de faire

- **Ajouter un chapitre, une partie, une grande section.** C'est la demande
  explicite de Sacha : le cours de l'an dernier n'est pas le cours de cette
  année, et une partie importée serait révisée pour rien — ou à la place de ce
  qui tombe vraiment.
- **Renuméroter ou réorganiser le plan** pour le faire ressembler à celui du
  dossier.
- **Importer une liste, une typologie, un tableau entier** que ses notes n'ont
  pas : c'est une grande partie déguisée.
- **Corriger un chiffre, une date, un nom d'auteur, une formule.** Le rang 3 a
  un an de retard : un chiffre qui diverge part dans `> [!question] À vérifier`
  avec les deux valeurs, jamais dans le corps.

### Le test, avant d'écrire une ligne

> **Est-ce que ça change un mot de ce qu'il a écrit, ou est-ce que ça ajoute
> une brique qu'il n'a pas ?**
>
> Un mot, une définition, une tournure → **on corrige**, dans son texte.
> Une brique — un chapitre, une partie, une notion entière absente de ses
> notes → **on ne l'écrit pas**, on pose la question dans `À vérifier`.

```md
> [!question] À vérifier
> - Le cours 2025-2026 avait une partie « Les styles de direction » (chapitre 6)
>   qu'aucune de tes notes ne mentionne — le prof l'a-t-il gardée cette année ?
```

Une question par partie manquante, pas une par paragraphe : c'est une liste à
poser en amphi, pas un inventaire du cours de l'an dernier.

### La traçabilité — un bloc à lui, distinct des slides

Les slides de cette année ont `> [!success]- Ce que les slides ont corrigé`. Le
cours de référence a le sien, plus bas, pour que Sacha voie d'un coup d'œil ce
qui vient d'une source qui peut être périmée :

```md
> [!info]- Ce que le cours de référence a précisé — 6 points
> Corrections tirées de `L1/Introduction à la gestion/CM1-CM2-CM3 - intro gestion.docx`
> (promo 2021-2022). Le corps de la fiche est à jour ; ces lignes disent ce qui a bougé.
>
> **Vocabulaire** — « les parties prenantes », et non « les gens autour » (§ 2).
> **Définition exacte** — une organisation est un ensemble de moyens structurés
> en vue d'un but commun (ta note s'arrêtait à « des gens et un but »).
> **Raccourci** — la définition de la compétitivité tenait en six lignes, elle
> en fait deux : rien n'a été perdu, la phrase de contexte était déjà au-dessus.
```

Le bloc **nomme le fichier et son année**. Sans ça, Sacha ne peut pas juger si
la correction vaut encore.

### Où chercher — la matière et son dossier

| Fiche / UE | Dossier de référence |
| --- | --- |
| `11A` Introduction à l'économie | `L1/Introduction à l_économie/` |
| `12A` Introduction à la gestion | `L1/Introduction à la gestion/` |
| `13A` Problèmes économiques contemporains | `L1/Problèmes économiques contemporains/` |
| `18C` Méthodologie du travail universitaire | *aucun — la fiche reste sur ses seules notes* |
| Comptabilité générale | `L1/Comptabilité générale/` |
| Management et théorie des organisations | `L1/Management et théorie des organisations/` |
| Principes de micro / macroéconomie | `L1/Principes de microéconomie/`, `L1/Principes de macroéconomie/` |
| Marketing, Droit, Sociologie, Statistiques, Maths, Analyse historique | dossier du même nom dans `L1/` |

Dans chaque dossier : `CM/` ou `diaporama/` = le prof (le plus fiable des trois),
un `.docx` à la racine = les notes d'une promo (utile pour le vocabulaire, pas
pour trancher), `Annales/` = les sujets.

**Une matière sans dossier n'est pas un problème** : la fiche se fait sur ses
notes seules, comme avant. On ne va pas chercher un dossier voisin « qui
ressemble ».

### Lire les fichiers

Le dossier mélange `.pdf`, `.docx`, `.odt`, `.pptx` et des photos. Un seul
outil, qui sort le texte de n'importe lequel :

```
python3 .claude/skills/eco/lire.py "<fichier>"              # tout le texte
python3 .claude/skills/eco/lire.py "<fichier>" --pages 1-12  # un PDF long
```

Il passe par **PyMuPDF** pour les PDF, **textutil** (macOS) pour `.docx` et
`.odt`, et ouvre le zip pour les `.pptx`, que textutil ne lit pas. Une image
n'est pas du texte : il le dit, et on l'ouvre avec l'outil Read.

**Un chapitre à la fois.** Ces fichiers font des centaines de pages : on ouvre
celui qui correspond à la section traitée, pas la matière entière.

### Les annales ne touchent pas au cours

`Annales/`, `Ancien partiel/`, `qcm entrainement/` servent au bloc `Contrôle` :
ils disent **quel type de question tombe** (QCM, définition, question de cours,
calcul). Ils ne fournissent jamais de contenu de cours — une réponse d'annale
recopiée dans la fiche, c'est du savoir non sourcé et daté.

## Les cartes Anki — taillées sur ce que les annales demandent vraiment

**Règle posée par Sacha le 11 septembre 2026 : « les cartes que tu me proposes
ne sont pas vraiment pertinentes ni bien faites ».** Le défaut était réel et il
avait trois causes, toutes corrigées ici : des cartes qui **récitent une liste**,
des cartes qui **répètent un titre de section**, et des cartes qui ne
correspondent à **aucune question réellement posée en examen**.

### D'abord lire les annales — c'est la source, pas le cours

Avant d'écrire une seule carte, on ouvre les annales de la matière :
`~/Documents/L1/<matière>/Annales/`, `Ancien partiel/`, et tout fichier dont le
nom contient `CC`, `CT`, `examen`, `sujet`, `QCM` ou un millésime.

```
python3 .claude/skills/eco/lire.py "<annale>.pdf"                       # si elle a du texte
python3 .claude/skills/eco/lire.py "<annale>.pdf" --images <scratchpad> # si elle est scannée
```

**La plupart des annales sont des scans** : `lire.py` le détecte, le dit, et
`--images` rend les pages en PNG — qu'on ouvre ensuite avec l'outil Read pour
les lire à l'œil. Un sujet corrigé (les bonnes réponses entourées) vaut trois
sujets vierges : il montre **quelle** formulation était la bonne.

On en retire trois choses, dans cet ordre :

1. **Le format et le barème** — QCM ou rédaction, une ou plusieurs bonnes
   réponses, points négatifs ou non. Ça change la forme des cartes.
2. **La forme des questions** — une définition à réciter ? un mini-cas à
   classer ? un auteur à nommer ? deux formulations à départager ?
3. **Les notions qui reviennent** d'une année sur l'autre. Elles passent en
   premier, et leurs cartes sont taguées `annale`.

### Ce que les annales de cette licence disent déjà

| UE | Format relevé | Ce que la question teste vraiment |
| --- | --- | --- |
| **11A** Introduction à l'économie | **QCM 1 h, une seule bonne réponse, −0,5 point par erreur** | Un énoncé court suivi de **quatre formulations très proches** — « les données statistiques servent à *invalider* / *expliquer* / *tester* les théories ». Et **« aucune des propositions n'est exacte » est souvent la bonne réponse.** C'est du mot à mot, pas de la compréhension générale |
| **12A** Introduction à la gestion | **2 h, trois parties** : QCM 6 pts (**plusieurs réponses possibles**, 0,5 pt par question, **tout ou rien**), questions de cours 7 pts, cas 7 pts | Le QCM donne un **mini-cas à classer** (« Virgin dans la boisson, la musique, les librairies : quel type de diversification ? ») ou demande **à qui on doit un modèle**. La question de cours demande de **définir *et* d'expliquer à quoi ça sert** (« qu'est-ce qu'un business model, et à quelles questions répond-il ? ») |
| **13A** Problèmes économiques | 2 h : QCM 30 %, questions de cours courtes 30 %, question de réflexion | Concepts, mécanismes, et **analyse d'un graphique ou d'un tableau** |

Deux conséquences qui traversent tout :

- **Le mot exact fait la note.** Un verso approximatif ne prépare pas un QCM où
  trois propositions sur quatre sont la bonne phrase avec un mot changé.
- **Avec un barème négatif, savoir qu'on ne sait pas vaut des points.** Une
  carte dont on ne peut pas juger si la réponse est exacte est une carte nuisible.

### Les six types de cartes, et rien d'autre

| Type | Recto | Verso |
| --- | --- | --- |
| **Définition + fonction** | « Que dit exactement le rapport Brundtland ? » | La phrase du cours, **et** à quoi la notion sert — c'est ce que la question de cours demande |
| **Discrimination** | « Les données statistiques servent à quoi, au mot près ? » | Le mot juste, **et** pourquoi le voisin est faux : « à TESTER les théories — pas à les expliquer ni à les invalider » |
| **Application (mini-cas)** | Un cas d'une ligne : « Virgin : boisson, musique, librairies, téléphonie » | La catégorie **et le critère qui tranche** : « diversification non liée — les métiers n'ont aucun lien entre eux » |
| **Attribution** | « À qui doit-on le modèle des 5 forces ? » — et l'inverse : « Porter, pour quoi ? » | Le nom, l'année si le cours la donne |
| **Chiffre ou seuil** | « Combien d'ETI en France ? » | **Un seul chiffre**, avec son année et sa source |
| **Texte à trou** | « VA = production − … » | Le mot ou le terme manquant, seul |

Une carte qui ne rentre dans aucune de ces six lignes ne se fait pas.

### Les règles de fabrication

| À faire | À ne pas faire |
| --- | --- |
| **Une carte = un fait.** Une liste de sept éléments donne sept cartes, ou aucune | « Cite les 7 fonctions de l'entreprise ? » — impossible à noter, et on la rate toujours sur le septième |
| Une carte-liste **seulement** si l'examen la demande comme liste, et si elle tient en **trois éléments** | Une carte-liste de cinq, six, huit items : le tableau de la fiche fait ce travail, pas Anki |
| Le recto est une **question**, avec son contexte | Un recto qui est un titre de section — « Développement durable ? » — ou qui répète le plan du chapitre |
| Le verso est **autosuffisant** et tient en une phrase | Un verso qui renvoie à la fiche, ou qui empile trois faits |
| Le mot qui fait la note est **entre guillemets ou en capitales** | Un verso où le mot décisif est noyé |
| **Le `;` sépare les trois champs, et rien d'autre** : `Recto ; Verso ; Tags`, deux `;` par ligne, jamais un de plus. À l'intérieur d'un champ : `·` ou une virgule | Un `;` dans le verso — l'import Anki le lit comme un quatrième champ et **la carte arrive cassée**. C'est la première cause de cartes inutilisables |
| Tags : `<matière> <UE>`, plus `complement` si la carte vient d'un ➕, plus `annale <année>` si la question est **réellement tombée** | Une carte issue d'un ajout non taguée `complement` : elle serait révisée comme du cours du prof |

### Le test avant d'écrire une carte

> **Cette carte, sous cette forme, ressemble-t-elle à une question qu'on a
> réellement posée dans une annale de cette matière ?**
>
> Oui → on l'écrit. Non → on ne l'écrit pas, même si la notion est importante :
> elle est déjà dans le corps de la fiche et dans le bloc `Contrôle`.

Le bloc `Contrôle` et le bloc `Cartes` ne font pas le même travail : **Contrôle**
teste la restitution structurée, à voix haute, longuement ; **Anki** teste le
grain fin, en deux secondes. Une question de Contrôle n'est presque jamais une
bonne carte telle quelle.

### Quand on repasse sur une fiche qui a déjà des cartes

On ne complète pas, on **refait le bloc** : chaque carte existante passe le test
ci-dessus, celles qui échouent sont supprimées ou découpées, et le compteur
`cartes:` du frontmatter suit. Une fiche qui perd quinze mauvaises cartes pour
en gagner dix bonnes a progressé.

## Les schémas — peu, et seulement ceux qui portent le savoir

**Règle corrigée par Sacha le 11 septembre 2026 : les passages faisaient trop de
schémas.** Une figure par idée, ce n'est plus une fiche, c'est un diaporama :
les deux ou trois figures qui comptent vraiment se noient dans les autres, et le
passage a passé son temps à dessiner ce qu'une phrase ou un tableau disait déjà
mieux. Ce qui reste vrai, c'est qu'**un chapitre ne sort pas sans les figures
qui portent son savoir** — pas qu'il sort avec toutes.

### Le test — une figure se fait si elle répond oui à l'une des deux

1. **Le prof l'a dessinée.** Elle existe comme figure dans la slide, au tableau
   ou dans le cahier — donc elle peut tomber en « refaites le schéma ».
2. **La géométrie *est* le savoir.** Ce qu'il faut retenir, ce sont des
   positions relatives, des croisements, une boucle, un circuit fermé : les trois
   cercles du développement durable et leurs intersections ne s'écrivent pas en
   phrases sans perdre l'essentiel.

Deux « non » : pas de schéma. On ne dessine pas pour illustrer, on dessine parce
que le texte n'y arrive pas.

**Ce qui ne devient pas un schéma** — c'est là que les passages dérapaient :

- une **chaîne de flèches** qui tient sur une ligne (`rareté → contrainte →
  choix`) : elle s'écrit dans le texte, en gras, et se cherche ;
- une **opposition à deux ou trois colonnes** (planifiée ↔ marché, micro contre
  macro) : c'est un **tableau markdown** — lisible sur mobile, cherchable, sans
  fichier à maintenir ;
- une **liste, une typologie, une suite d'étapes** : liste numérotée ou bloc
  `Méthode` ;
- une **définition**, même centrale ;
- une figure qui **redit** une section déjà claire : c'est de la décoration.

### Combien — deux ou trois par chapitre, quatre au maximum

Au-delà, on n'ajoute pas : on **arbitre**. Priorité aux figures que le prof a
réellement dessinées, puis à celle qui a le plus de chances d'être demandée à
l'examen. Les six schémas du chapitre 1 de gestion étaient un excès, pas un
modèle.

Un passage qui repasse sur une fiche surchargée peut en **retirer** : on
supprime l'embed et sa légende, et le fichier de `schemas/` avec, s'il n'est
embarqué nulle part ailleurs. Ce qui reste ressort d'autant mieux.

### Redessiner ou découper — le passage choisit

| Plutôt redessiner en SVG | Plutôt découper dans la source |
| --- | --- |
| Boîtes, flèches, cercles, colonnes : une géométrie simple, des libellés courts | Une courbe, un graphique, une échelle chiffrée — la redessiner, c'est risquer de déplacer une valeur, ce que la règle d'or interdit |
| La figure n'existe pas comme image : elle se déduit du texte (chaîne de flèches, opposition à deux colonnes) | Une figure dense — organigramme à vingt nœuds, tableau-figure, carte — qu'un SVG rendrait faux ou illisible |
| L'original est lisible mais mal cadré, tordu, noyé dans la slide | Un croquis du cahier, une photo, une illustration : c'est l'original qui a la valeur |
| Le passage a le temps de la rasteriser et de la regarder | Le passage n'a pas ce temps : une figure découpée aujourd'hui vaut mieux qu'un SVG au passage suivant |

Le choix n'est pas définitif : un passage suivant peut remplacer une image par
son SVG (on change l'embed, on supprime l'image), et l'inverse quand un SVG
trahit la figure. Ce qui ne se fait pas, c'est **les deux pour la même figure**.

### Ce qui ne change pas, quel que soit le moyen

- Ils vivent dans **`eco gestion/schemas/`**, **un fichier par figure**, nommés
  `<matière>-<sujet>.<ext>` — `gestion-developpement-durable.svg`,
  `eco13-courbe-de-croissance.png`.
- **Fond blanc explicite** et texte foncé : sans ça, le schéma disparaît dans le
  thème sombre d'Obsidian. Une figure découpée sur un fond sombre ou coloré se
  recolle sur du blanc.
- **La provenance est écrite** : le numéro de slide en tête du SVG, ou dans la
  légende pour un découpage. Une figure sans provenance ne se confronte pas au
  cours.
- **On reproduit, on n'invente pas.** Mêmes éléments, mêmes mots, même
  disposition que la source. Une figure inventée serait un ➕ déguisé, non
  traçable.
- Chaque schéma est suivi d'une ligne en italique qui dit **ce qu'il faut savoir
  en refaire** — c'est ce qui en fait un outil de révision plutôt qu'une
  illustration.
- **On regarde le fichier avant de commiter** : le SVG rasterisé, l'image
  ouverte. Un texte qui déborde ou un cadrage qui coupe une flèche ne se voient
  pas dans le code.

### Découper, en pratique

Pas de poppler ni de Ghostscript sur cette machine : le seul outil PDF est
**PyMuPDF** (`python3 -c "import fitz"`), et **Pillow** pour les photos du
cahier.

```python
import fitz  # PyMuPDF
page = fitz.open("eco gestion/fichier/IG_Seance1-2_MAJ__2026.pdf")[23]  # slide 24
# clip en points PDF (72 dpi) : la zone de la figure, reperee d'abord sur la page entiere
page.get_pixmap(dpi=200, clip=fitz.Rect(60, 120, 700, 470)).save(
    "eco gestion/schemas/gestion-developpement-durable.png")
```

Repérer la zone en deux temps : rendre la page entière, la regarder, puis
recadrer. **PNG** pour un schéma (aplats et texte), **JPEG** seulement quand la
source est une photo.

**On recadre, on ne retouche pas.** Redresser une photo du cahier, oui ; gommer
un élément, réécrire un libellé, recolorier, non — ce serait falsifier la
source. Et on découpe **la figure**, pas la slide entière avec son titre et ses
puces : une slide recopiée en image, ce n'est pas un schéma, c'est du cours
soustrait à la fiche.

## Règle d'or — le savoir ne bouge pas, la forme et la clarté oui

| Autorisé | Interdit |
| --- | --- |
| Fautes, accents, ponctuation, phrases cassées rendues lisibles | Prêter au prof une définition qu'il n'a pas donnée |
| Hiérarchie de titres d'aplomb (`#` unique, `##`, `###`), listes, indentations | Renommer un titre ciblé par un `[[lien#ancre]]` d'une autre page |
| Transformer deux paragraphes opposés en tableau de contraste | Modifier une valeur dans un tableau, remplir une cellule de suivi |
| Ajouter les blocs qui servent à réviser (`L'essentiel`, `À ne pas confondre`, `Méthode`, `Cartes à créer`, `Contrôle`) | Remplir un de ces blocs sans matière dans la page — un bloc vide est du décor |
| Dérouler un exemple **calculable depuis une formule de la page** | Inventer un exemple, un chiffre, un coefficient, une date de partiel |
| **Combler un trou du cours** : ajouter l'information capitale manquante à sa place, marquée `➕`, comptée dans `ajouts:` et reprise dans le récapitulatif de fin | Ajouter du cours **sans** cette trace : il réviserait comme parole du prof une information qui ne l'est pas |
| S'appuyer sur le programme officiel de l'UE (dans la page de cycle) pour repérer les trous | Reconstituer « ce que le prof a dû dire », ou ajouter une opinion plutôt qu'un savoir standard |
| Signaler un trou ou une incohérence dans `> [!question] À vérifier` | Corriger un chiffre, une date, un nom d'auteur, une formule |
| Garder ses exemples et ses remarques (`ex Decathlon`, `licornes : Doctolib`) | Supprimer un exemple au nom de la concision |
| **Ajouter un exemple simple là où l'explication n'en a aucun**, marqué ➕ et listé dans le récapitulatif comme exemple (pas comme cours) | Faire passer un exemple inventé pour celui du prof, ou en ajouter un là où il y en a déjà un |
| **Fondre une slide ou un syllabus déposé par Sacha** dans le texte du cours, à sa place | Recopier un PDF en vrac en fin de fiche, ou hacher le cours en « d'après la slide 13… » |
| **Corriger un mot ou un chiffre quand la source du prof le tranche**, et le dire dans le bloc de traçabilité | Corriger en silence, sans que Sacha puisse voir ce qui a changé depuis ses notes |
| **Corriger le vocabulaire, préciser une définition, raccourcir une explication** d'après `~/Documents/L1`, et le dire dans `> [!info]- Ce que le cours de référence a précisé` | Ajouter un **chapitre ou une grande partie** tirés de `~/Documents/L1` : le cours de l'an dernier a pu changer — la partie manquante va dans `À vérifier` |
| Corriger un chiffre quand **les slides de cette année** le tranchent | Corriger un chiffre, une date ou un auteur d'après `~/Documents/L1` : le rang 3 a un an de retard |
| **Redessiner en SVG _ou_ découper dans la source** les deux ou trois figures qui portent le savoir, dans `schemas/` | Faire un schéma d'une liste, d'une opposition à deux colonnes ou d'une chaîne de flèches — inventer un schéma que le prof n'a pas fait, retoucher le contenu d'une figure découpée |
| **Corriger l'orthographe et la syntaxe du brut**, ligne par ligne, à leur place | Restructurer un brut : déplacer, fusionner, renuméroter, compléter, ou retoucher un nom propre |
| Laisser les tableaux valides tels quels, alignement compris | Reformater un tableau qui marche (`verifie.py` le refuse) |
| **Supprimer une carte Anki mauvaise** et la remplacer, en ajustant `cartes:` | Garder une carte-liste de sept items parce qu'elle existait déjà |
| Écrire une carte dont la forme correspond à une question d'annale | Écrire une carte « parce que la notion est importante », sans équivalent en examen |
| Ajouter un tag déjà utilisé dans le périmètre | Supprimer ou renommer un de ses tags, toucher au reste du frontmatter |

Test de relecture : **est-ce qu'il peut se tester avec cette page, seul, sans
son cahier ?** Si non, la fiche n'est pas finie. Et : **est-ce qu'il peut
distinguer ce qui vient de son amphi de ce que j'ai ajouté ?** Si non, c'est un
défaut grave — tout ajout porte son `➕`, son compteur et sa ligne de
récapitulatif.

## Procédure d'un passage

1. **Savoir quoi traiter** : `etat.py --suivant` (à la main) — en mode
   automatique, le prompt nomme déjà la cible, ne pas redemander.
2. **Snapshot** — en mode automatique `passage.sh` l'a déjà pris dans
   `.claude/skills/eco/scratch/avant.md` et le prompt en donne le chemin. À la
   main : `cp "<cible>" <scratchpad>/avant.md`.
3. **Lire en entier** la cible, plus le hub `00 - Plan L1 Angers`, la page de
   cycle correspondante et [[MCC - Tableau de bord]] pour le mode d'évaluation.
   Impossible de prioriser sans savoir ce que la notion vaut en points.
3 ter. **Ouvrir le cours de référence** — `~/Documents/L1/<matière>/`, le
   chapitre qui correspond, lu avec `lire.py`. **Après** avoir lu ce que Sacha a
   écrit, jamais avant : ses notes fixent le périmètre, le dossier ne fait que
   corriger les mots. Pas de dossier pour cette matière : on passe.
3 quater. **Ouvrir les annales** de la même matière — `Annales/`,
   `Ancien partiel/`, les fichiers `CC`/`CT`/`examen`/`QCM`. Elles ne donnent
   pas de cours : elles disent **la forme des questions et le barème**, et c'est
   de là que se déduisent les cartes Anki. Un scan se lit avec
   `lire.py … --images <scratchpad>` puis l'outil Read.
3 bis. **Si la cible est un brut, le corriger d'abord** — orthographe, accents,
   ponctuation, syntaxe markdown, et rien d'autre. Snapshot obligatoire avant
   (`cp "<brut>" <scratchpad>/brut-avant.md`), puis :
   ```
   python3 .claude/skills/eco/verifie.py <scratchpad>/brut-avant.md "<brut>" --brut
   ```
   Ce mode refuse le passage si une ligne, un chiffre, une formule ou 2 % du
   volume ont bougé, et liste les mots corrigés pour relecture. La fiche s'écrit
   **ensuite**, depuis le brut corrigé : c'est lui que `--integration` compare.
4. **Relever avant d'écrire** : les paires confusables, les procédures, les
   définitions cartables, les phrases interrompues, les incohérences de chiffres,
   les liens et ancres morts, les blocs manquants — et, face au cours de
   référence, deux listes séparées : **les mots à corriger** (ils partent dans
   la fiche) et **les parties absentes de ses notes** (elles partent dans
   `À vérifier`, pas dans la fiche). Et, face aux annales, **la forme des
   questions** qui décidera des cartes.
5. **Écrire la page en une fois**, blocs dans l'ordre de `references/apprendre.md`.
6. **Vérifier** :
   ```
   python3 .claude/skills/eco/verifie.py <avant> "<page>"                 # fiche
   python3 .claude/skills/eco/verifie.py "eco gestion/_brut/x.md" "<fiche>" --integration
   python3 .claude/skills/eco/verifie.py <avant> "<page>" --complement    # si on a comblé des trous
   python3 .claude/skills/eco/verifie.py <brut-avant> "<brut>" --brut     # si on a corrigé le brut
   ```
   **ERREUR** → restaurer depuis le snapshot, ne pas acter, le dire. **Alerte**
   → la justifier dans le récap ou revenir en arrière.
7. **Acter** : `etat.py --enregistre "<page>" "<ce qui a été fait>"`. Le brut
   cité en `source:` est acté avec la fiche. Sans ça, tout repasse au tour
   suivant.
8. **Commiter**, la page, `etat.json` et — s'il a été corrigé — le brut :
   ```
   git add "<page>" "<brut si corrigé>" .claude/skills/eco/etat.json
   git commit -m "eco: <page> — <résumé court>"
   ```
   Jamais `git add -A` : le vault a en permanence des modifications qui ne sont
   pas les nôtres. **Un brut corrigé se commite avec la fiche** — sans ça, la
   correction écrase la seule copie de ses notes sans filet.
9. **Pousser** — Sacha l'a demandé le 8 septembre 2026 : un passage se termine
   sur GitHub, pas sur le disque.
   ```
   git push origin main
   ```
   En mode automatique, **`passage.sh` s'en charge lui-même** après l'appel au
   modèle : il ne pousse que si `HEAD` a bougé, et si le push est refusé (un
   autre poste a poussé entre-temps) il rejoue le commit par-dessus avec
   `git pull --rebase`, une seule fois. En cas de conflit il abandonne le rebase
   et laisse le commit local — il partira au passage suivant. Le modèle n'a donc
   **pas besoin** de `git push` dans ses outils autorisés.
   > **`mon-savoir` est un dépôt public.** Ce qui est commité est publié, sans
   > relecture. D'où deux règles : `git add` ne prend **que** la page traitée et
   > `etat.json`, et `eco gestion/fichier/` (photos de cahier, PDF de slides)
   > est au `.gitignore` — la matière première personnelle reste locale.
10. **Récap** : ce qui a été corrigé, ce qui a été ajouté (**nommément**, surtout
   les `Complément`), les trous signalés, et `git show --stat --oneline HEAD`.

## Les sept opérations

- **Intégrer un brut** — l'opération à plus forte valeur. Des notes d'amphi
  deviennent une fiche complète dans `eco gestion/`, avec `source:` vers le
  brut. Nom de fiche : `<Matière> - <Sujet> (CM).md`, sans accent dans le nom de
  fichier (un renommage casse les liens du vault).
- **Corriger le brut** — orthographe, accents, ponctuation, syntaxe markdown, à
  leur place dans ses notes. Se fait **avant** la mise en fiche, se vérifie avec
  `--brut`, se commite avec la fiche. Le fond, l'agencement et les noms propres
  ne bougent pas : ce fichier reste la trace de ce que le prof a dit.
- **Corriger** — langue, markdown, hiérarchie, tableaux bancals, liens morts.
  Aucune validation nécessaire.
- **Rendre révisable** — les blocs qui servent les six leviers : `L'essentiel`
  (5 lignes), `À ne pas confondre`, `Méthode`, `Cartes à créer`, `Contrôle` avec
  réponses repliées `> [!question]-`. Uniquement là où il y a matière.
- **Compléter les trous** — autorisé et attendu depuis le 7 septembre 2026 :
  « n'hésite pas à rajouter des informations capitales si tu vois qu'elles
  manquent […] je n'ai pas eu le temps de noter ». L'information va **à sa place
  dans le cours**, pas dans un encadré caché — une notion qu'on ne voit pas ne se
  révise pas. Trois pièces obligatoires : le marqueur **`➕`** en fin de ligne,
  le compteur **`ajouts: n`** au frontmatter, et le bloc
  **`> [!info] Ce que j'ai complété (n)`** en fin de fiche qui liste chaque ajout
  avec sa section. La **liste de contrôle des trous, c'est le programme de l'UE**
  écrit dans la page de cycle. Détail et frontière : `references/apprendre.md`.
- **Intégrer une source officielle** — un PDF de slides ou un syllabus déposé
  par Sacha. C'est l'opération qui rapporte le plus après l'intégration d'un
  brut : elle **ferme des trous** au lieu de les signaler. Procédure : extraire
  le texte du PDF, le confronter section par section à la fiche, poser le contenu à
  sa place dans le cours **sans marque de source**, déplacer les trous fermés et
  les mots corrigés dans `> [!success]- Ce que les slides ont corrigé`, redessiner **ou découper** dans `schemas/` les
  figures qui passent le test, et reporter ce que le syllabus dit du **mode d'évaluation** dans
  la fiche **et** dans [[MCC - Tableau de bord]]. Le plan du syllabus devient la
  nouvelle liste de contrôle des trous, en tête de fiche, séance par séance.
- **Relier** — vérifier que la fiche pointe vers son hub, son cycle, sa série
  d'exercices, sa fiche Anki, sa page de méthode, et que ces liens résolvent.
- **Laisser tel quel** — un choix à part entière pour une page déjà finie. On
  l'acte avec `--enregistre "…" "déjà au propre"`.

## La méthode de révision a sa page, et un bloc dans chaque fiche

Sacha a demandé le 8 septembre 2026 que les techniques de révision soient
« dans les fiches de cours ». Elles y sont, en deux endroits :

- **[[Methode - Comment reviser]]** — la page de référence : effet test,
  espacement, réapprentissage successif, interleaving, pretesting, avec les
  chiffres et les références qu'il a fournis, plus le tableau qui **calcule**
  l'intervalle (10 à 20 % du délai avant l'épreuve). C'est là que vont les
  ajouts sur la méthode, **pas** dans les fiches.
- **`## 🔄 Comment réviser cette fiche`** — dans chaque fiche de cours, juste
  avant son bloc `Contrôle` ou `Auto-test` : cinq ou six lignes qui appliquent
  le protocole **à cette page-là** (le nombre de cartes qu'elle contient, les
  fiches avec lesquelles l'entrelacer, ce qui tombe à l'examen), et qui
  renvoient à la page de référence.

Deux règles pour ce bloc : il commence par « *Méthode de révision, pas du
cours* » — il ne doit jamais se confondre avec le contenu évalué — et il **ne
porte pas de ➕**, pour la même raison : ce n'est pas du cours ajouté, donc ça
ne rentre pas dans le compteur `ajouts:`.

## Cohérence entre pages — signaler, jamais arbitrer

Les chiffres circulent entre le hub, les cycles et les fiches : coefficients,
ECTS, heures, nombres d'exercices et de cartes. Quand deux pages divergent, on
**ne tranche pas** : la source est la maquette `26-27_Maquette_L1_EG.xlsx`,
qu'on n'a pas. Un `> [!question] À vérifier` en fin de page, avec les deux
valeurs et où elles sont écrites.

Ce bloc est **remplacé** à chaque passage, jamais empilé. Une ligne que Sacha a
supprimée reste supprimée : c'est une décision, pas un oubli.

## L'automatisation horaire — installation et pannes

Le passage tourne via un **LaunchAgent macOS**, `~/Library/LaunchAgents/com.sacha.eco-fiches.plist`
(copie dans le skill), qui lance `passage.sh` **toutes les heures à :17** (pas
à :00 : tout le monde y est).

```
launchctl load -w   ~/Library/LaunchAgents/com.sacha.eco-fiches.plist   # activer
launchctl unload -w ~/Library/LaunchAgents/com.sacha.eco-fiches.plist   # couper
launchctl list | grep eco-fiches                                       # état
launchctl kickstart -k gui/$(id -u)/com.sacha.eco-fiches               # forcer un tir
bash .claude/skills/eco/passage.sh                                     # un passage à la main
```

**Le piège d'installation, vécu le 7 septembre 2026 :** `launchctl list`
renvoyait un statut **126** et `launchd.log` disait
`getcwd: cannot access parent directories: Operation not permitted`.
Ce n'est ni le plist ni le script : c'est **TCC**, la protection de macOS. Un job
lancé par launchd n'a **aucun accès à `~/Documents`** — donc au vault — tant que
son exécutable n'a pas l'**Accès complet au disque** (Réglages Système →
Confidentialité et sécurité → Accès complet au disque → `+` → `Cmd+Shift+G` →
`/bin/bash`). Sans cet accès, l'automatisation ne peut passer que par une session
Claude Code ouverte (`/loop 1h /eco`), qui hérite des droits du terminal.

**Diagnostic dans l'ordre** : `launchd.log` (le job a-t-il démarré),
`passages.log` (qu'a fait le passage), `launchctl list | grep eco` (dernier
code), `git log --oneline` (a-t-il commité).

Deux journaux et un verrou, tous git-ignorés : `passages.log`, `launchd.log`,
`.verrou/` (un dossier, créé par `mkdir` atomique — deux passages ne peuvent pas
se chevaucher ; un verrou de plus d'une heure est cassé automatiquement).

## Quand une page disparaît du disque

Vécu le 7 septembre 2026 : **les 22 fichiers de `eco gestion/` se sont volatilisés
d'un coup** en pleine session (Obsidian ouvert, plugin `supabase-vault-sync`
actif sur **tout** le vault — `vaultId: brain2`, `syncOnSave: true`, soft delete
30 jours, l'app faisant autorité). Même scénario que le 18 août sur les notes de
la racine. Rien n'était perdu : tout était commité.

```
python3 .claude/skills/eco/restaure.py             # dit ce qui manque
python3 .claude/skills/eco/restaure.py --applique   # les rend depuis HEAD
```

`restaure.py` ne réécrit que les fichiers que git voit supprimés **et** réellement
absents : il ne peut rien écraser. Trois règles qui en découlent :

- **commiter chaque passage, sans exception** — c'est ce qui rend la perte
  réparable, et c'est la seule raison pour laquelle l'incident n'a rien coûté ;
- **avant d'écrire, vérifier que la page est là** (`ls`), pas se fier à une
  lecture faite plus tôt dans la session ;
- **après un passage, si la page a disparu**, ne pas la réécrire de mémoire :
  `restaure.py --applique`, puis le dire — si ça recommence aussitôt, la synchro
  est en cause et il faut l'arrêter ou exclure `eco gestion/` avant de continuer.

## Garde-fous

- **Jamais `rm`**, jamais de renommage de fichier, jamais de suppression d'une
  section entière sans validation explicite.
- **Un brut ne se corrige que sur la forme.** C'est la seule trace de ce que le
  prof a dit : l'orthographe et la syntaxe se réparent, le fond, l'agencement et
  les noms propres ne bougent pas, et `--brut` le vérifie. Toute amélioration —
  structure, blocs, compléments — vit dans la fiche.
- **Une cible par passage** en mode automatique. Un passage qui touche trois
  pages est un passage qui a dérivé.
- `verifie.py` passe **avant** le commit. Erreur → restauration depuis le
  snapshot, et on le dit au lieu de forcer.
- **Ne rien remplir à sa place** : grilles d'essais, scores, cases `- [ ]`,
  `statut:`. `verifie.py` refuse une cellule de suivi remplie.
- **Tout ajout de contenu est marqué `➕`, compté et récapitulé.** Un complément
  fondu dans le cours sans trace est un défaut grave : il réviserait comme parole
  du prof une information qui ne l'est pas. `verifie.py --complement` refuse le
  passage si le compte ne tombe pas juste.
- **Ne pas se battre contre lui** : si une amélioration est défaite au passage
  suivant, c'est qu'il n'en voulait pas — ne pas la réappliquer, le noter.
- **Ne pas toucher au reste du vault** : ni `notes/`, ni les fiches d'autres
  domaines, même si une page d'éco les lie.
- **Quand des pages disparaissent, on nettoie les liens qui les visaient.** Une
  page supprimée par Sacha laisse des `[[liens]]` morts dans celles qui restent :
  on **délie** en gardant le texte (`[[Cycle 3 - Gestion et debats]]` →
  `**Cycle 3 - Gestion et debats**`), on ne supprime pas la phrase. `verifie.py`
  distingue désormais un lien perdu vers une page **existante** (erreur : on a
  cassé un chemin) d'un lien mort **délié** (alerte : c'est le ménage).
  Attention : ce ménage ne touche pas les **embeds de schémas**
  (`![[…​.svg]]`) — une pièce jointe n'est pas une page supprimée.
- **Le caractère ➕ ne s'écrit que sur une ligne réellement ajoutée.** Dans une
  phrase qui parle des ajouts, écrire « le plus vert », jamais le signe :
  `verifie.py` compte les occurrences et refuse le passage si le compte ne tombe
  pas juste.
- **Un doublon ne se supprime pas, il se signale.** `restaure.py` repère les
  fiches que la synchro redescend sous un nom tronqué (vécu le 8 septembre :
  `Gestion - Introduction.md` en face de `Gestion - Introduction UE 12A.md`).
  La vivante est **celle que git suit** ; l'autre reste sur le disque jusqu'à ce
  que Sacha tranche, et on ne travaille jamais dessus.
- **Le site lit ces fiches.** `~/Documents/GitHub/vault-gallery` publie le
  dossier sur `/cours` : les fiches d'UE y sont groupées par période avec leur
  coefficient, leurs trous et leurs cartes, lus dans le **frontmatter**. Un champ
  mal orthographié disparaît donc silencieusement du tableau de bord du site.
  Après un passage qui compte, `npm run index` dans ce dépôt remet le site à
  jour.
- Le vault est un dépôt git : montrer `git show --stat` plutôt que décrire les
  changements de mémoire.
