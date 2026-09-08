# La forme d'une fiche de révision — exemples pris dans les vraies pages

À lire **avant** de toucher une page, avec `apprendre.md` qui dit *pourquoi*
chaque bloc existe. Les avant/après ci-dessous viennent de `eco gestion/`, pas
d'un exemple inventé.

---

## Les blocs, dans cet ordre

L'ordre et le levier d'apprentissage de chaque bloc sont dans le tableau de
`apprendre.md`. Un bloc absent se crée **à partir du contenu de la page** ; un
bloc déjà là ne se refait pas ; **un bloc sans matière ne se remplit pas**.

1. **Frontmatter** — `tags`, `statut`, `source:` si la fiche vient d'un brut, et
   les champs propres à la page (`notion`, `prerequis`, `modules`…).
   Intouchables sauf `statut`.
2. **Titre + ligne de contexte** — `# 📊 Cours — Indices et déflation`, puis la
   ligne des liens : module, durée, coefficient et mode d'évaluation si la MCC
   les donne, série d'exercices, retour au hub.
3. **`> [!abstract] L'essentiel`** — 5 lignes max, ce qu'il doit pouvoir dire en
   30 secondes. Uniquement des phrases dérivées du corps.
4. **Le corps du cours** — préservé, en sections numérotées, une idée par ligne,
   **ses exemples gardés**. On corrige la langue et la structure, on ne réécrit
   pas l'explication.
5. **`## 🔁 À ne pas confondre`** — un tableau par paire voisine réellement
   présente dans la page. C'est là que les points se perdent en examen.
6. **`## 🧮 Méthode`** — la procédure numérotée, si la page en contient une,
   suivie d'un exemple déroulé.
7. **`## 🃏 Cartes à créer`** — format `Recto ; Verso ; Tags`, définitions,
   formules, procédures et distinctions seulement.
8. **`## 🔄 Comment réviser cette fiche`** — cinq ou six lignes de protocole
   appliquées à cette page, renvoyant à [[Methode - Comment reviser]]. Sans ➕ :
   ce n'est pas du cours.
9. **`## ✅ Contrôle`** — questions d'abord, **réponses repliées** dans
   `> [!question]- …`, ou l'ancre de la section qui répond.
10. **`> [!success]- Ce que les slides ont résolu`** — les trous fermés par une
    source officielle, avec les valeurs qui étaient en conflit. N'existe que si
    des slides sont passées.
11. **`> [!question] À vérifier / à récupérer`** — trous et incohérences
    (cf. § Ce qu'on signale sans corriger).
12. **`## 📚 La bibliographie du syllabus`** — quand le syllabus en donne une.
13. **`## Ce que j'ai complété`** — le récapitulatif des ➕, exemples compris.

---

## Bloc 3 — l'essentiel, dérivé et rien d'autre

`Cours - Indices et deflation` contient déjà sa propre phrase-clé, éparpillée :
« la question à laquelle tout ce chapitre répond », « séparer ce qui relève de
la quantité et ce qui relève du prix », les deux indices Laspeyres/Paasche.

**Après** — un encadré en tête qui ne dit rien de neuf :

```md
> [!abstract] L'essentiel
> - Un indice ramène une série à une base 100 pour rendre deux évolutions comparables.
> - Tout le chapitre sert à séparer l'effet **prix** de l'effet **quantité**.
> - Laspeyres = pondérations de l'année de base · Paasche = pondérations de l'année courante.
> - Déflater = passer d'une valeur en euros courants à une valeur en volume.
> - Sans ce chapitre, aucune série INSEE n'est lisible.
```

Chacune de ces lignes est présente dans le corps. Une sixième ligne qui
ajouterait « en pratique, Laspeyres surestime l'inflation » serait **hors
limite** : ce n'est pas écrit dans la page.

---

## Bloc 5 — à ne pas confondre, le bloc qui rapporte le plus

Deux notions voisines côte à côte se retiennent ; deux définitions séparées par
trois pages se confondent le jour de l'examen.

```md
## 🔁 À ne pas confondre

| Structure formelle | Structure informelle |
|---|---|
| L'organigramme, décidé | Les relations réelles, spontanées |
| Division verticale (hiérarchie) et horizontale (fonctions) | Affinités, réseaux d'entraide, circuits d'information |
| **Ce qui les sépare** : l'une est écrite et voulue, l'autre est observée. |

| Entreprise individuelle | Société |
|---|---|
| Pas de personne morale distincte | Personne morale, patrimoine propre |
| Impôt sur le revenu | Impôt sur les sociétés |
| **Ce qui les sépare** : les deux questions de choix du statut — responsabilité limitée ou non, IR ou IS. |
```

Chaque paire vient de la page. La ligne « ce qui les sépare » se dérive de ses
lignes, elle n'ajoute pas de savoir.

## Bloc 9 — le contrôle, réponses repliées

```md
## ✅ Contrôle

Réponds à voix haute avant d'ouvrir la réponse.

> [!question]- Les trois éléments que réunit toute organisation ?
> Un objectif, une mobilisation d'individus avec des rôles, une structure.

> [!question]- Laspeyres ou Paasche : lequel garde les pondérations de l'année de base ?
> Laspeyres. → [[#PARTIE 2 — Les indices synthétiques]]

> [!question]- Un salaire monte de 15 %, les prix de 18 %. Le pouvoir d'achat ?
> Il baisse : il faut déflater. → [[#Déflater]]
```

Règles du bloc :
- le `-` après `[!question]` **replie** le callout : la réponse est cachée. Sans
  lui, il n'y a pas de test, juste une relecture ;
- une question par notion réellement traitée, **8 maximum** ;
- la réponse est **dans la page**, plus l'ancre de la section quand elle existe ;
- une question sans réponse dans la page ne va **pas** dans Contrôle : elle va
  dans `À vérifier`.

---

## Ce qu'on corrige — avant / après

| Avant (tel quel dans les pages) | Après |
| --- | --- |
| `\t` seul sur la ligne 10 de `Fiche exos - Modules A C E` | ligne supprimée |
| `—` collé au mot, doubles espaces, `...` | `— ` propre, espace simple, `…` |
| `deflateur`, `Economie`, `a faire` dans le **corps** | `déflateur`, `Économie`, `à faire` |
| `**Notes de support** : [[MCC]] · [[Ressources]]` avec un lien mort | lien corrigé vers le nom réel du fichier |
| trois titres `# PARTIE 1` en `#` au milieu d'une page qui a déjà un `#` | `## PARTIE 1`, hiérarchie remise d'aplomb — **sauf si une ancre pointe dessus** |
| tableau dont une ligne a une colonne de moins | colonne vide ajoutée, contenu inchangé |
| `> [!danger]` sans titre après le callout | titre court ajouté |

**Les noms de fichiers ne s'accentuent pas.** `Cours - Contributions a la
croissance.md` reste tel quel : le renommer casse tous les `[[liens]]` du vault.
On corrige l'accent dans le titre `#` de la page, pas dans son nom.

---

## Ce qu'on ne touche jamais

- **Les chiffres de la maquette** : 62 coefficients, 46 + 14 ECTS, 432 h, 24 coef
  en CC, 39 %. Source unique `26-27_Maquette_L1_EG.xlsx`. Un chiffre faux se
  signale, ne se corrige pas.
- **Les formules** `$(uv)'$`, `$$\dots$$` : rien, ni les espaces, ni les
  parenthèses. Une formule à corriger part dans `À vérifier`.
- **Les grilles de suivi** (`Essai 1 | Essai 2 | Essai 3`), les cases `- [ ]`,
  les scores cibles : ce sont **ses** données. Une cellule vide reste vide.
- **Les énoncés d'exercices** : ni la numérotation, ni les valeurs, ni l'ordre.
  On peut corriger une faute d'orthographe dans la consigne, rien d'autre.
- **Les `[[liens]]` avec ancre** qui pointent depuis d'autres pages : le titre
  visé ne se renomme pas (`verifie.py` refuse).

---

## Ce qu'on signale sans corriger

Un seul endroit, en fin de page :

```md
> [!question] À vérifier
> - Le total du tableau des cycles donne 64 coef, le frontmatter en annonce 62 — lequel est bon ?
> - `Cycle 2` annonce 108 h, le plan en annonce 96 pour le même cycle.
> - Série C-II : 10 items annoncés, 9 numérotés.
```

Trois règles : la formulation reprend les deux valeurs en conflit, jamais un
arbitrage ; le bloc est **remplacé** à chaque passage, il ne s'empile pas ; une
ligne dont Sacha a tranché disparaît (une suppression de sa part est une
décision, pas un oubli).

---

## Le ton

Les pages sont écrites en tutoiement direct, avec des emojis en tête de section
et des callouts Obsidian. C'est **sa** forme : on la garde. Pas de « il convient
de », pas d'introduction ajoutée, pas de conclusion, pas de nouvel emoji dans un
titre qui n'en avait pas.

---

## Les trois marques, dans le texte

Ce qui n'est pas marqué vient de ses notes. Le reste se voit d'un coup d'œil :

```md
🎞️ **La formule exacte de la slide 13** : « plus on descend vers l'opérationnel,
plus les décisions sont **fréquentes, réversibles et proches du terrain** ».
Tes notes ont « plus les décisions sont **récentes** » — c'est **fréquentes**.

➕ *Ex. la boulangerie : farine, eau, électricité, travail et four (**inputs**)
→ pain vendu au comptoir (**output**).*
```

La première ligne porte la marque du prof : elle fait autorité, et elle **dit ce
que les notes disaient**, sans l'effacer. La seconde est un exemple ajouté :
italique, ➕, et comptée dans `ajouts:`.

En tête de fiche, un encadré rappelle la convention — sans écrire le caractère
➕, qui serait compté :

```md
> [!note] Trois sources dans cette fiche, trois marques
> Ce qui **n'est pas marqué** vient de tes notes d'amphi.
> **🎞️** = ce qui vient des **slides de Carole Vigeant** — ça fait autorité.
> **Un plus vert en tête de ligne** = ce que j'ai ajouté depuis le programme de
> l'UE : à confirmer en cours. Le frontmatter en donne le compte (`ajouts:`).
```

## Les schémas — un SVG par figure du prof

Une question de cours peut demander de **refaire un schéma**. Une fiche qui le
décrit en phrases n'y prépare pas.

```md
![[gestion-developpement-durable.svg]]
*Le schéma de la slide 24. Trois cercles, trois croisements, un centre : c'est
la figure la plus demandée du chapitre.*
```

Les règles, apprises en faisant les six schémas du chapitre 1 de gestion :

| À faire | À ne pas faire |
| --- | --- |
| Un fichier par figure, dans `eco gestion/schemas/`, nommé `<matière>-<sujet>.svg` | Un gros SVG qui contient trois figures : il devient illisible sur mobile |
| `<rect width= … fill="#ffffff"/>` en premier élément | Un fond transparent : le schéma disparaît dans le thème sombre d'Obsidian |
| Le numéro de slide écrit en tête du schéma | Un schéma sans provenance, qu'on ne pourra pas confronter au cours |
| Une légende en italique **sous** l'embed, qui dit quoi savoir en refaire | Une légende qui répète le schéma |
| `font-family: system-ui, -apple-system, 'Segoe UI', sans-serif` | Une police du vault : le SVG est lu hors Obsidian, sur le site aussi |
| Reprendre les mots du prof dans les libellés | Traduire, abréger ou « améliorer » ses termes |

`verifie.py` résout les pièces jointes depuis le 8 septembre 2026 (constante
`JOINTES`) : un `![[schema.svg]]` qui pointe dans le vide est une **erreur**, au
même titre qu'un lien mort vers une page.
