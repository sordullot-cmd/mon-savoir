# Avant / après — sur les vraies notes

Sept cas pris dans `notes/`. Ils montrent où s'arrête le nettoyage et où commence la réécriture (interdite).

## 1. Indentation à l'espace → listes markdown

Le seul vrai problème de ces notes : les indentations et alignements faits à l'espace ne rendent rien en markdown. On les convertit, **sans toucher un mot**.

Avant (`base trading`) :

```
liquidité externe :
        previous daily high / low
        previous weekly high / low
        equal high and low
        session high and low ( london / asia )
```

Après :

```
liquidité externe :
- previous daily high / low
- previous weekly high / low
- equal high and low
- session high and low (london / asia)
```

Ce qui a changé : des tirets, et l'espace parasite dans les parenthèses. Rien d'autre. `liquidité externe :` garde sa minuscule et ses deux points.

## 2. Colonnes de chiffres → tableau, et incohérence signalée

Avant (`plan pour passer a 100k mensuelle`) :

```
tradeify - 5 comptes lightning 15Ok  =                   50k                                   2300e
apex  - 20 compte 50k =                                              60k                                   3200e
lucid - 5 compte 50k =                                                   15k                                     620e
= 135K                                                                                                                                6k
```

Après — une ligne par prop, ses `=` comme séparateur. **Pas de tableau markdown** : l'app affiche le markdown comme du texte, Sacha n'y verrait rien (cf. SKILL.md § Structure).

```
prop = comptes = objectif = coût
tradeify = 5 comptes lightning 150k = 50k = 2300e
apex = 20 compte 50k = 60k = 3200e
lucid = 5 compte 50k = 15k = 620e
total = = 135K = 6k
```

Corrigé : `15Ok` → `150k` (faute de frappe évidente, O au lieu de zéro).
**Pas corrigé** : `50 + 60 + 15 = 125`, pas `135`. Le total reste tel qu'il l'a écrit et part dans la question groupée. On ne recalcule jamais à sa place.

## 3. Note qui mélange deux sujets → scission

`social media` contenait, après les plans tiktok/youtube, un bloc sans rapport :

```
fiscalité

prestation de service
aPE7022Z
```

Opération : ce bloc part dans sa note (`fiscalité`), `#trading` conservé, et `social media` garde un `[[fiscalité]]` en fin de note. La nouvelle note **n'a pas** de `tr4de-id` : l'app lui en attribuera un.
Le contenu reste ces trois lignes. On ne « complète » pas la fiscalité avec ce qu'on sait du régime micro.

## 4. Note épinglée trop grosse → hub + notes détaillées

`glow uppp` (`pinned: true`, `#top3`) empile cinq sujets : domaines à apprendre, peau, cheveux, muscu, symptômes d'éloquence.

Opération proposée : la note épinglée **reste en place** et devient un hub de lignes courtes,

```
glow uppp

domaine dans lesquels il faut que je m'instruise :
- ia / claude
- philosophie
- psychologie

- [[peau]]
- [[cheveux]]
- [[muscu]]
- [[eloquence]]
```

et chaque sujet part dans sa note avec **exactement** son contenu (les liens de produits, le planning muscu lundi→dimanche, les symptômes). Une note `pinned` ne se déplace pas et ne se dilue pas : elle se vide de son détail, pas de son rôle.

## 5. Anti-exemple : la réécriture (interdite)

Avant :

```
peau :
1. Cleanser =  https://www.pharmaciedesdrakkars.com/la-roche-posay-toleriane-fluide-dermo-nettoyant
```

Interdit :

```
### Routine de soin du visage
Une routine structurée en quatre étapes permet de nettoyer, hydrater puis exfolier la peau
en douceur. Étape 1 — nettoyage : privilégier un fluide dermo-nettoyant doux (La Roche-Posay
Toleriane), adapté aux peaux sensibles.
```

Trois fautes en même temps : du vocabulaire qui n'est pas le sien, des conseils qu'il n'a pas écrits, et une note trois fois plus longue. Le bon rendu est le même que l'avant, en liste propre.

## 6. Liste de tâches → cases à cocher, jamais cochées

`app` est une suite de demandes sur ses produits. Après nettoyage : regroupement par cible (page sport, page éloquence, page budget, site, stockage) et une case par demande.

```
page sport
- [ ] enlever les pointillés du graphique, grossir le trait
- [ ] ajouter les exos sans poids : suivre le nombre de répétitions max et sa courbe
```

Même quand une ligne est manifestement déjà faite (« fusionne le skill univers et inspirations » l'est), **on ne coche pas** : on le signale dans le récap, il coche.

## 7. Notes chiffrées → deux sections, trous conservés

Avant (`anime manga film`) : notes sur 10 mélangées avec une liste à regarder, films en bas.

Après : sections `vus`, `a regarder`, `films` — ses mots, ses notes à l'identique. Et :

```
hunter x hunter =
```

reste comme ça. Pas de note inventée, pas de ligne supprimée.

## Corrections de frappe relevées dans ces notes

À corriger : `exxpire`, `ingrediens`, `virlangue` (virelangue), `imagien`, `collone`, `parralleles`, `enregirstre`, `plusierus`, `servetn`, `obvisious`, `formeel`, `basqiue`, `bleau marine`, `addidas`, `shapooing`, `philoshopie`, `physco`.

À **ne pas** toucher : `fvg`, `ivfg`, `ifvg`, `ob`, `rb`, `bc`, `cisd`, `mss`, `bos`, `sdtv`, `stdv`, `po3`, `amd`, `smt`, `htf`, `ltf`, `rr`, `hod`, `lod`, `pd array`, `whick`, `soup`, `drawdown`, `payout`, `sweep`, `fomo`, `tdbp`. C'est son vocabulaire de travail — même quand l'orthographe varie d'une note à l'autre, on n'unifie pas sans lui demander.

## 8. Consolidation : un sujet éparpillé sur trois notes

Le cas le plus important, et celui qu'un nettoyage note par note rate complètement.

**Avant**, la communication était partout :

| Où | Quoi |
| --- | --- |
| `apprentissage de la journée` — dimanche 16 aout | respiration, posture, machoire, ton et rythme, articulation, routine |
| `apprentissage de la journée` — mercredi 15 juillet | humour : raconter des histoires, silences, exageration, comedians |
| `apprentissage de la journée` — mardi 14 (fin) | « je veux reussir a faire rire mes amis / inconnues », « concepts clé de l'humour » |
| `glow uppp` — competence a apprendre | « bien perler = respiration diaphragmatique … » |
| `glow uppp` — symptome | eloquence : manque de vocabulaire, debit incontrolable, mauvaise diction |
| `app` — page eloquence | les mêmes exos, comme specs de la page à construire |

**Après** :

- **`bien communiquer`** (note neuve, `#glow`) porte tout : `symptome :` d'abord — c'est le pourquoi —, puis les 5 exercices, la routine, l'humour. Contenu **déplacé**, mot pour mot.
- **`glow uppp`** garde la version **courte** : `bien parler = respiration diaphragmatique, 4s … → [[bien communiquer]]` et `symptome : - eloquence → [[bien communiquer]]`. La note chapeau reste lisible d'un coup d'oeil.
- **`apprentissage de la journée`** reste le **journal** : chaque date garde une ligne de rappel plus le lien.

```
dimanche 16 aout - bien communiquer

respiration, posture, machoire, ton et rythme, articulation → [[bien communiquer]]
```

- **`app`** garde ses cases à cocher (c'est une specs de page à construire, pas du savoir) et pointe vers `[[bien communiquer]]`.
- Le `mardi 14 - meta learning` est devenu **`meta learning`**, qui a récupéré au passage la ligne `video = (…)` que `glow uppp` gardait à part.
- Le `vendredi 10` était du trading : ses deux lignes ont rejoint la ligne **`trade with time`** de `base trading`, qui existait déjà et n'attendait que ça.

Ce qui n'a **pas** été consolidé : `powell` et `sdtv` gardent leurs propres `entry trigger` malgré le recoupement avec `base trading`. Ce sont des méthodes distinctes, les mélanger ferait perdre qui dit quoi. Un `voir aussi` suffit.

Repères chiffrés du passage : `apprentissage de la journée` 576 → 71 mots, `base trading` 133 → 182, `glow uppp` 175 → 131, et **total du dossier 1909 → 1973 mots** (+3 %, uniquement des liens et des titres de section). Un total qui s'envole voudrait dire qu'on a réécrit au lieu de déplacer.

## 9. Améliorer la page : une liste en vrac devient utilisable

`recette et courses` contenait deux blocs collés : une liste de courses, puis une liste de repas dont les ingrédients étaient noyés dans le nom du plat.

Avant :

```
sucre
sel
papier toilette
pate
...
-Patates douces
-Lentilles + sel + poivre + saucisses + 
-Pates + poulet ( + sauces tomates ) ❤️
```

Après — les courses classées par type, les repas en tableau avec **ses** ingrédients rattachés :

```
courses :
- feculents : pate, patate / douches, lentilles
- proteines : poulet, oeuf
- condiments : sucre, sel, miel, herbe de provinces / curry
- maison : papier toilette, sac poubelle

repas :
- Patates douces = patate / douches
- Lentilles = sel + poivre + saucisses +
- Plat japonais =
- Pates + poulet ❤️ = pate, poulet, sauces tomates
- Ramen chinois =

dans les repas mais pas dans les courses : poivre, saucisses, sauces tomates
```

Trois choses à voir :

- `Plat japonais` et `Ramen chinois` gardaient d'abord un `=` **vide** : il n'avait pas écrit leurs ingrédients, on ne les inventait pas. Puis il a demandé l'inverse pour cette page — « lorsqu'il y a un plat sans ingredient tu les rajoutes toi meme » — donc ils ont été complétés au plus courant, en réutilisant ce qui était déjà dans ses courses :

```
- Plat japonais = riz + sauce soja + oeuf + poulet
- Ramen chinois = nouilles + bouillon + oeuf + poulet + sauce soja
```

  Les quatre ingrédients qui n'existaient pas dans sa liste (`riz`, `sauce soja`, `nouilles`, `bouillon`) sont **restés hors de son `courses :`** et sont apparus sur la ligne des manques — c'est lui qui décide de les acheter. Et l'ajout a été annoncé nommément dans le récap. L'exception vaut pour cette page, pas pour le vault.
- Le rattachement `Pates + poulet` → `pate`, `poulet` vient de **sa** liste de courses. C'est de la lecture, pas de l'ajout.
- La dernière ligne est **dérivée** : trois ingrédients apparaissent dans ses repas et manquent dans ses courses. Rien d'inventé, et c'est ce qui rend la page utile.

Ce qui a été **demandé** au lieu d'être décidé : classer les repas par midi / soir. Il ne l'a jamais écrit, donc c'est une question, pas une déduction.

Même traitement pour `achat` : classé par pièce (appart, salle de bain, bureau / tech), et les deux items qu'on ne sait pas placer sur une ligne à part — `a preciser : tanquarville, tapis de touche` — plutôt que rangés au hasard.

## 10. Quand l'app écrase tout

Le 18 août 2026, le passage complet du matin (11 notes nettoyées, `bien communiquer` et `meta learning` créées, `recette et ingrediens` renommée) a été **entièrement effacé** vers 15h par une synchro descendante : notes revenues à l'indentation à l'espace, notes neuves supprimées, et deux renommages faits par Sacha dans l'app entre-temps (`appartement` → `achat`, `recette et ingrediens` → `recette et courses`).

Ce qu'il faut en retenir, dans l'ordre :

1. **Relire le disque avant d'écrire**, à chaque passage. La lecture faite deux heures plus tôt ne vaut plus rien.
2. **Ne pas rejouer le plan en aveugle.** Ici, rejouer aurait recréé `appartement` alors que Sacha l'avait renommée `achat`, et recréé des notes que la synchro allait resupprimer.
3. **Le dire, chiffres à l'appui** (tailles, `updated`, contenu de `notes/conflicts/`), et **demander** avant de refaire.
4. Les copies perdues sont dans `notes/conflicts/` sous la forme `<nom> (obsidian <horodatage>).md` — c'est là qu'on récupère le travail local, pas dans sa mémoire.

## 11. Les dossiers : tentés, défaits par l'app

Sacha a demandé de ranger les notes en dossiers Obsidian. Fait : `notes/trading`, `notes/glow`, `notes/appart`, les notes sans famille laissées à la racine.

**Quatre minutes plus tard**, la synchro avait re-téléchargé chacune de ces notes à la racine de `notes/`, en version brute, sans supprimer mes copies en sous-dossier. Résultat : deux fichiers par note, **avec le même `tr4de-id`**. C'est exactement ce que le contrôle d'unicité attrape :

```
ERREUR trading/social media.md : même tr4de-id que social media.md ("1778067247835.3635")
        — deux notes ne peuvent pas partager une identité, l'app en perdra une
```

Réparation : réinjecter le contenu de la version en sous-dossier dans la note de la racine (en gardant le frontmatter que l'app venait d'écrire), supprimer les copies, supprimer les dossiers.

La leçon n'est pas « les dossiers c'est mal », c'est : **l'app décide de la forme du dossier `notes/`**. Une organisation qu'elle ne sait pas stocker ne survit pas quatre minutes. Le bon geste est de le dire à Sacha et de proposer de faire évoluer l'app — pas de refaire le rangement à chaque passage.

## 12. « rien à faire » alors que la note avait changé

`/notes page recette`, 18 août 2026. `etat.py` répond « 15 notes, aucune touchée ». Le disque, lui, montrait onze articles ajoutés dans `recette et courses` (`slyr`, `flocon d'avoine`, `bannane`, `pommes`, `beurre de cacahuete`, `choux fleur`, `brocolis`, `oignon`, `ails`, `lait`, `gruyere`), les titres passés en minuscules et le ❤️ retiré.

Cause : la synchro avait écrit la version de Sacha **quelques secondes avant** que le passage précédent ne soit acté avec `--enregistre`. L'état enregistré contenait donc déjà sa modification, sans qu'elle ait été traitée. Un changement réel devenu invisible.

Deux corrections :

1. **Sa parole bat l'outil.** Quand il nomme une note, on la lit, point.
2. `etat.py` ouvre maintenant le passage (`etat-debut.json`) et **refuse de mentir** : à `--enregistre`, il liste les notes qui ont bougé pendant le passage.

```
ATTENTION — ces notes ont changé pendant le passage :
  - powell.md
  si c'est mon écriture, tout va bien ; si c'est l'app ou Sacha,
  les traiter avant d'acter, sinon leur changement passera à la trappe.
```

Morale utile bien au-delà de ce skill : un outil de détection qui se trompe en silence est pire que pas d'outil. Il doit dire quand il n'est pas sûr.
