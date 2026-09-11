# Ce qui fait réussir un examen — et comment ça se traduit dans la fiche

Le but d'une fiche n'est **pas** d'être un beau résumé. Une fiche qu'on relit ne
sert presque à rien : la relecture donne un sentiment de maîtrise sans laisser de
trace. Une fiche utile est celle **avec laquelle on peut se tester**, et qui est
organisée comme la question d'examen le demandera.

Six leviers, du plus rentable au moins rentable. Chaque bloc de la fiche existe
pour un levier précis — un bloc qui ne sert aucun levier est du décor.

---

## 1. Se tester plutôt que relire

C'est le levier le plus puissant et le moins utilisé. Se forcer à ressortir
l'information de sa tête fixe le savoir bien plus que de le relire.

**Traduction** : le bloc `## ✅ Contrôle` en fin de fiche, et la règle des
réponses **repliées**. Dans Obsidian, `> [!question]-` (avec le tiret) crée un
callout fermé : la question est visible, la réponse cachée jusqu'au clic.

**Le bloc doit être long.** Une question par notion réellement traitée, dans
l'ordre du cours, groupées par partie — c'est ce que Sacha a demandé le
8 septembre 2026. Une fiche de 13 sections avec huit questions laisse les deux
tiers du cours sans test : ce sont exactement les deux tiers qu'il ne révisera
pas.

```md
> [!question]- Trois éléments que réunit toute organisation ?
> Un objectif, une mobilisation d'individus avec des rôles, une structure.
```

Une fiche sans bloc de contrôle est incomplète, et `verifie.py` le signale.

## 2. Espacer les révisions

Revoir une notion à J+1, J+3, J+7 bat dix relectures d'affilée. Le système est
déjà en place chez lui : [[Anki - Formules et definitions C0-C1]].

**Traduction** : le bloc `## 🃏 Cartes à créer`, au format d'import exact de sa
fiche Anki (`Recto ; Verso ; Tags`). On n'extrait que ce qui est légitimement
une carte — **définition, formule, procédure, distinction** — jamais un
raisonnement, c'est sa propre règle.

Et depuis le 11 septembre 2026, la forme des cartes ne se devine plus : elle se
relève dans les **annales** de la matière (`~/Documents/L1/<matière>/Annales/`).
Une carte vaut si elle ressemble à une question réellement posée — sinon la
notion reste dans le corps de la fiche et dans le bloc `Contrôle`, qui ne fait
pas le même travail. Les six types de cartes et les règles de fabrication sont
dans `SKILL.md`, section « Les cartes Anki ».

Depuis le 8 septembre 2026, **l'intervalle se calcule** au lieu de se deviner :
environ **10 à 20 % du délai** avant l'épreuve (Cepeda et al., 2006), et la
relation est en U inversé — trop serré est aussi mauvais que trop espacé. Le
tableau de calcul et les études sont dans [[Methode - Comment reviser]] ; chaque
fiche en porte l'application dans son bloc `## 🔄 Comment réviser cette fiche`.

## 3. Distinguer ce qui se confond

En examen, les points se perdent presque toujours sur des paires voisines :
Laspeyres/Paasche, structure formelle/informelle, IR/IS, entreprise
individuelle/société, stratégique/opérationnel, secteur/branche. Le cerveau
retient mieux deux notions **opposées côte à côte** que deux définitions
séparées par trois pages.

**Traduction** : le bloc `## 🔁 À ne pas confondre`, un tableau à deux colonnes
par paire, avec la ligne qui tranche (« ce qui les sépare en une phrase »).

## 4. Savoir pourquoi, pas seulement quoi

Une définition rattachée à ce qu'elle sert, à quoi elle s'oppose et à un exemple
concret est retenue ; une définition seule s'oublie.

**Traduction** : dans le corps, chaque notion garde **son** exemple quand il est
dans les notes (`ex Decathlon`, `ex L'Oréal`, `licornes : Doctolib, Mistral`).
Un exemple présent dans les notes ne se supprime jamais au nom de la concision :
c'est lui qui fait tenir la notion.

**Et quand il n'y en a aucun, on en ajoute un** — Sacha l'a demandé le
8 septembre 2026 : « rajoute quelques exemples simples s'il n'y a pas d'exemple
dans l'explication ». Trois conditions, sinon l'exemple dessert :

- **un cas banal, en une ligne**, en italique, marqué ➕ et compté dans
  `ajouts:` — la boulangerie pour la valeur ajoutée, le CHU pour l'organisation
  publique, le coiffeur pour la production de services ;
- **jamais là où le prof en donne déjà un** : deux exemples pour une notion, et
  c'est le sien qui se perd ;
- **listés à part dans le récapitulatif**, sous « exemples ajoutés pour
  illustrer », avec la mention qu'ils sont à remplacer par ceux du prof. Un
  exemple inventé qu'il croirait venir de l'amphi est pire que pas d'exemple :
  il le ressortirait en copie.

Un exemple **chiffré** (« 200 000 − 60 000 = 140 000 € ») est autorisé au même
titre : c'est un calcul déroulé depuis une formule de la page, pas un chiffre
de cours. Le récapitulatif dit alors que les nombres sont inventés pour le
calcul.

**Et le schéma vaut l'exemple — mais rarement.** Quand la notion est une figure
que le prof a dessinée (les trois cercles du développement durable, le cycle de
produit), elle rejoint `eco gestion/schemas/` et s'embarque dans la fiche —
redessinée en SVG, ou découpée dans la slide quand la redessiner déplacerait une
valeur : voir `forme-fiche.md`. Une question de cours peut demander de la
refaire. Hors de ce cas, on n'en fait pas : une chaîne de flèches, une
opposition à deux colonnes ou une liste se rendent mieux en texte et en tableau.
Deux ou trois schémas par chapitre, quatre au maximum.

## 5. Répéter la procédure, pas la théorie

Les matières à calcul (indices, dérivées, écritures comptables, contributions à
la croissance) ne se révisent pas en comprenant : elles se révisent en refaisant
jusqu'à l'automatisme.

**Traduction** : le bloc `## 🧮 Méthode`, une procédure numérotée en étapes
courtes, **suivie d'un exemple entièrement déroulé** quand les notes en
contiennent un. Et le renvoi vers la série d'exercices correspondante.

## 6. Réviser selon ce qui rapporte des points

Toutes les notions ne valent pas le même nombre de points. Le contrôle continu ne
se rattrape pas ([[00 - Plan L1 Angers]]), les coefficients sont très inégaux.

**Traduction** : la ligne de contexte en tête de fiche dit l'UE, le coefficient
et le mode d'évaluation quand [[MCC - Tableau de bord]] les donne. Rien d'inventé :
si le mode d'évaluation est inconnu, c'est une ligne dans `À vérifier`.

---

## L'ordre des blocs, et pourquoi

| Bloc | Levier | Règle |
| --- | --- | --- |
| Frontmatter | — | intouchable, plus `source:` si la fiche vient d'un brut |
| `# Titre` + ligne de contexte | 6 | UE, coefficient, mode d'évaluation, liens |
| `> [!abstract] L'essentiel` | 1 | 5 lignes max. Ce qu'il doit pouvoir dire en 30 secondes |
| Corps, en sections numérotées | 4 | une idée par ligne, les exemples restent |
| `## 🔁 À ne pas confondre` | 3 | seulement les paires réellement présentes dans la page |
| `## 🧮 Méthode` | 5 | seulement si la page contient une procédure |
| `## 🃏 Cartes à créer` | 2 | format `Recto ; Verso ; Tags` (deux `;` par ligne), une carte = un fait, la forme vient des annales |
| `## 🔄 Comment réviser cette fiche` | 1 · 2 | le protocole appliqué à cette page, sans ➕ — ce n'est pas du cours |
| `## ✅ Contrôle` | 1 | questions d'abord, réponses en callout replié |
| `> [!success]- Ce que les slides ont résolu` | — | les trous fermés par une source officielle, valeurs en conflit gardées |
| `> [!info]- Ce que le cours de référence a précisé` | — | vocabulaire, définitions exactes, raccourcis venus de `~/Documents/L1` ; nomme le fichier et son année |
| `> [!question] À vérifier` | — | trous et incohérences, remplacé à chaque passage |
| `## Ce que j'ai complété` | — | obligatoire dès qu'un ➕ est posé : compléments **et** exemples |

Les **schémas** n'ont pas de bloc à eux : chaque figure retenue — deux ou trois
par chapitre — s'embarque dans la section du cours qu'elle illustre
(`![[gestion-cycle-de-produit.svg]]`, ou l'image découpée), suivie d'une ligne
qui dit quoi savoir en refaire.

Un bloc sans matière ne se remplit pas : **une fiche sans paire confusable n'a
pas de bloc « À ne pas confondre »**. Mieux vaut sept blocs justes que neuf
blocs dont deux sont du remplissage.

---

## La frontière : expliciter, oui. Inventer, non.

C'est la règle la plus importante du skill, et la plus fine. Sacha a demandé le
7 septembre 2026 que les fiches soient **vraiment faites pour apprendre**, ce qui
autorise davantage que du nettoyage — mais pas de fabriquer du cours.

**Autorisé, sans marquage** — c'est du travail sur ce qu'il a écrit :
- rendre lisible une phrase cassée : « ca permet de ezperie les taches » →
  « ça permet de répartir les tâches » ;
- nommer ce qui est implicite avec le mot technique **déjà présent ailleurs dans
  la page** ;
- transformer deux paragraphes opposés en tableau de contraste ;
- dérouler un exemple **calculable depuis une formule de la page** ;
- fabriquer les questions du bloc Contrôle, dont la réponse est dans la page ;
- extraire les cartes Anki de ses définitions.

**Attendu, avec marquage obligatoire** — combler les trous du cours.

Sacha l'a demandé le 7 septembre 2026, et c'est un renversement de la règle
précédente : « n'hésite pas à rajouter des informations capitales si tu vois
qu'elles manquent […] il y avait d'autres choses dans le cours mais je n'ai pas
eu le temps de noter […] si tu vois qu'il manque des grosses informations, des
trous, des idées capitales, notes les ».

Donc : **une information capitale absente de ses notes s'ajoute, à sa place dans
le cours, et se marque.** Elle ne part plus dans un callout replié en fin de
page — une notion cachée ne se révise pas.

La convention, en trois pièces :

1. **Le marqueur ➕ en fin de ligne ajoutée**, dans le corps, à l'endroit
   pertinent :

   ```md
   - **Entreprise publique** : l'État détient **> 50 % du capital**.
   - **Entreprise privée** : l'État en détient moins de la moitié. ➕
   ```

   Le marqueur signale du **contenu** ajouté : une ligne, une intro de bloc, une
   cellule de tableau. Jamais un titre de section (le `➕` entrerait dans le slug
   de l'ancre) ni l'étiquette d'un bloc — sinon le compteur ne veut plus rien
   dire. Pour une section entière ajoutée, le `➕` va sur sa **ligne d'intro**,
   qui dit aussi pourquoi elle est là.

2. **Le compteur `ajouts: n`** dans le frontmatter — c'est ce qui alimente le
   tableau de bord et ce que `verifie.py` recoupe.

3. **Le récapitulatif en fin de fiche**, déplié, qui liste chaque ajout avec sa
   section, pour qu'il puisse confronter à son cours d'un coup d'œil :

   ```md
   > [!info] Ce que j'ai complété (6)
   > Ces points ne viennent pas de tes notes. Vérifie-les en cours ou sur Moodle.
   > - **Les formes juridiques** (§ 11c) : SARL, SAS, SA — tes notes s'arrêtent à EI / EURL.
   > - **Les fonctions de l'entreprise** (§ 8) : le programme de l'UE les demande, tes notes n'en parlent pas.
   ```

`verifie.py --complement` refuse le passage si le compte des ➕ ne correspond pas
au frontmatter, ou si le récapitulatif manque. **Un ajout non tracé serait
révisé comme du cours du prof** — c'est la seule chose qui rende cette
autorisation sûre.

**Ce qui reste non négociable** : un ajout est du savoir **standard et vérifiable**
(seuils légaux, définitions de manuel, listes canoniques), jamais une opinion ni
une reconstitution de ce que le prof « a dû dire ». En cas de doute sur ce qui
est au programme, l'ajout va dans le récapitulatif avec une réserve explicite.

## Le programme de l'UE est la liste de contrôle

C'est ce qui permet de repérer les trous **objectivement**, au lieu de deviner :
chaque page de cycle contient le programme officiel de l'UE.
[[Cycle 3 - Gestion et debats]] liste pour l'UE 12A : l'entreprise (définition,
finalités, classification), les formes juridiques, les fonctions, les parties
prenantes, la création de valeur, les cycles d'exploitation et
d'investissement, les notions de performance, la RSE.

**Procédure** : confronter les sections de la fiche à cette liste. Un point du
programme absent des notes est un trou — donc soit un complément marqué ➕, soit
une ligne dans `À vérifier` quand le compléter demanderait d'inventer.

**Interdit** :
- corriger en silence un chiffre, une date, un nom d'auteur, une formule ;
- prêter au prof une définition qu'il n'a pas donnée ;
- supprimer un exemple ou une remarque de Sacha au nom de la concision ;
- inventer un mode d'évaluation, un coefficient, une date de partiel ;
- écrire une réponse de contrôle qui n'est pas dans la page.

## Les trous se disent, ils ne se comblent pas

Des notes d'amphi sont toujours trouées : une phrase interrompue (« construction ? »),
une définition commencée puis abandonnée (« il y a deux niveaux : »), un
« copier ce que j'ai ecris sur mon cahier ». Ce sont **les endroits où il perdra
des points**, donc le plus utile de la fiche :

```md
> [!question] À vérifier / à récupérer
> - « niveau stratégique : construction ? » — phrase interrompue, à reprendre en cours.
> - Culture d'entreprise : tes notes annoncent « deux niveaux », un seul est écrit.
> - « copier ce que j'ai écrit sur mon cahier » — reste à faire, ce bloc manque.
> - ETI : « 5 000 salariées et 15000 M » ne colle pas aux seuils PME/GE voisins.
```

Formulation : ses mots entre guillemets, le manque nommé, aucune correction
d'autorité. Ce bloc est **remplacé** à chaque passage, jamais empilé.
