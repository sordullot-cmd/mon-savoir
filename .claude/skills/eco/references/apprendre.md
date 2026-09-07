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
| `## 🃏 Cartes à créer` | 2 | format `Recto ; Verso ; Tags`, jamais un raisonnement |
| `## ✅ Contrôle` | 1 | questions d'abord, réponses en callout replié |
| `> [!question] À vérifier` | — | trous et incohérences, remplacé à chaque passage |

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

**Autorisé, avec marquage obligatoire** — quand une notion est indispensable
pour comprendre et absente de ses notes :

```md
> [!info]- Complément (absent de tes notes)
> Les seuils INSEE de l'ETI : 250 à 4 999 salariés, CA < 1,5 Md€.
> À confronter à ton cours : tes notes disent « 5 000 salariées et 15000 M ».
```

Le callout `[!info]-` est **replié** et dit « absent de tes notes ». Il ne se
confond donc jamais avec son cours — ce qui compte, parce qu'en examen c'est le
cours du prof qui est évalué, pas la culture générale.

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
