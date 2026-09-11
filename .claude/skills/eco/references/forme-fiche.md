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
7. **`## 🃏 Cartes à créer`** — format `Recto ; Verso ; Tags`, **deux `;` par
   ligne et pas un de plus** (un `;` dans le verso casse l'import). Six types
   seulement — définition + fonction, discrimination, mini-cas, attribution,
   chiffre, texte à trou — et chacune doit ressembler à une question réellement
   posée en annale : voir `SKILL.md`, section « Les cartes Anki ».
8. **`## 🔄 Comment réviser cette fiche`** — cinq ou six lignes de protocole
   appliquées à cette page, renvoyant à [[Methode - Comment reviser]]. Sans ➕ :
   ce n'est pas du cours.
9. **`## ✅ Contrôle`** — questions d'abord, **réponses repliées** dans
   `> [!question]- …`, ou l'ancre de la section qui répond.
10. **`> [!success]- Ce que les slides ont corrigé dans tes notes`** — mots
    remis au vocabulaire du cours, phrases coupées complétées, chiffres
    tranchés. N'existe que si une source du prof est passée, et c'est **le seul
    endroit** où l'on dit ce qui vient d'où.
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
- **une question par notion réellement traitée** — pas de plafond : Sacha en a
  demandé davantage le 8 septembre 2026, « plus de questions sur le cours
  lui-même ». La fiche Gestion 12A en porte 45, groupées par partie du cours
  (`**La gestion, les organisations**`, `**Décider, piloter**`, …) pour qu'on
  puisse se tester sur une partie à la fois ;
- les questions suivent **l'ordre du cours**, et le groupe des compléments
  (hors programme traité) vient en dernier, annoncé comme tel ;
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

## Fondre une source du prof — avant / après

Le cours du prof ne se signale pas, il **remplace** ce qui était approximatif.

**Avant** (ce qu'il ne faut plus faire — le cours haché par ses sources) :

```md
- plus les décisions sont récentes, plus elles sont **réversibles**

🎞️ **La formule exacte de la slide 13** : « plus on descend vers l'opérationnel,
plus les décisions sont **fréquentes, réversibles et proches du terrain** ».
Tes notes ont « **récentes** » — c'est **fréquentes**.
```

**Après** (le cours d'un seul tenant, la correction tracée en fin de fiche) :

```md
- plus on descend vers l'opérationnel, plus les décisions sont **fréquentes,
  réversibles et proches du terrain**
```

```md
> [!success]- Ce que les slides ont corrigé dans tes notes — 11 points
> **Vocabulaire remis au mot du cours**
> - « Plus les décisions sont **fréquentes** » — tu avais noté « récentes » (§ 5).
```

Seul le complément hors cours reste marqué dans le corps :

```md
➕ *Ex. la boulangerie : farine, eau, électricité, travail et four (**inputs**)
→ pain vendu au comptoir (**output**).*
```

Et l'encadré de tête dit **deux** choses, pas trois — sans écrire le caractère
➕, qui serait compté :

```md
> [!note] Ce qui est du cours, et ce qui ne l'est pas
> Le corps de la fiche est **le cours** : tes notes et les slides, fondues.
> Là où elles divergeaient, c'est le mot du prof qui a été retenu — la liste des
> corrections est en fin de fiche.
> Seul ce qui **ne vient pas du cours** est marqué : un **plus vert** en tête de
> ligne. Le frontmatter en donne le compte (`ajouts:`).
```

## Les schémas — deux ou trois par chapitre, pas un de plus

Une question de cours peut demander de **refaire un schéma**, et une fiche qui
le décrit en phrases n'y prépare pas : les figures partent donc avec la fiche
sans attendre qu'on le demande. Mais **seulement celles qui portent le savoir** —
une figure se fait si le prof l'a dessinée, ou si sa géométrie (croisements,
boucle, circuit) est ce qu'il faut retenir. Une chaîne de flèches s'écrit dans
le texte ; une opposition à deux colonnes est un tableau ; une liste reste une
liste. Deux ou trois schémas par chapitre, quatre au maximum : le test complet
et l'arbitrage sont dans `SKILL.md`, section « Les schémas ».

Une fois la figure retenue, deux moyens, et le passage choisit figure par
figure : **redessiner** en SVG, ou **découper** la figure dans la slide ou la
photo du cahier et déposer l'image. On redessine une géométrie simple (boîtes,
flèches, cercles) ; on découpe une courbe, une échelle chiffrée, une figure
dense ou un croquis — redessiner un graphique, c'est risquer de déplacer une
valeur.

```md
![[gestion-developpement-durable.svg]]
*Le schéma de la slide 24. Trois cercles, trois croisements, un centre : c'est
la figure la plus demandée du chapitre.*
```

Les règles de fabrication, une fois la figure retenue :

| À faire | À ne pas faire |
| --- | --- |
| Un fichier par figure, dans `eco gestion/schemas/`, nommé `<matière>-<sujet>.svg` ou `.png` | Un gros SVG (ou un découpage) qui contient trois figures : il devient illisible sur mobile |
| Retirer une figure de trop quand on repasse sur une fiche surchargée : l'embed, sa légende, et le fichier s'il n'est embarqué nulle part ailleurs | Empiler les schémas passage après passage jusqu'à noyer les deux qui comptent |
| `<rect width= … fill="#ffffff"/>` en premier élément, et un découpage recollé sur du blanc | Un fond transparent, sombre ou coloré : le schéma disparaît dans le thème sombre d'Obsidian |
| Le numéro de slide en tête du SVG, ou dans la légende quand la figure est découpée | Un schéma sans provenance, qu'on ne pourra pas confronter au cours |
| Une légende en italique **sous** l'embed, qui dit quoi savoir en refaire | Une légende qui répète le schéma |
| `font-family: system-ui, -apple-system, 'Segoe UI', sans-serif` | Une police du vault : le SVG est lu hors Obsidian, sur le site aussi |
| Reprendre les mots du prof dans les libellés | Traduire, abréger ou « améliorer » ses termes |
| **Rasteriser le SVG et le regarder** avant de commiter (`sharp` suffit) | Le livrer sans l'avoir vu : les débordements de texte ne se voient pas dans le code |
| **Découper avec PyMuPDF** (`fitz`, seul outil PDF de la machine) la figure seule, cadrage vérifié à l'œil | Découper la slide entière avec son titre et ses puces, ou retoucher la figure (gommer, réécrire, recolorier) |

`verifie.py` résout les pièces jointes depuis le 8 septembre 2026 (constante
`JOINTES`) : un `![[schema.svg]]` ou `![[schema.png]]` qui pointe dans le vide est
une **erreur**, au même titre qu'un lien mort vers une page.
