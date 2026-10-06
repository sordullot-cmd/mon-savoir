---
name: condense
description: Extrait d'un cours d'éco gestion (une fiche de `eco gestion/`, ou tout un cours) une FICHE DE RÉVISION CONDENSÉE de deux pages A4 au plus, et la sort en PDF prêt à imprimer. Garde ce qui tombe à l'examen — l'essentiel, les définitions exactes, les formules, les paires à ne pas confondre, les schémas à savoir refaire, les méthodes — et laisse le reste (contrôle, cartes, trous, notes de provenance). Ne touche jamais un chiffre, une formule, un nom d'auteur. À utiliser quand Sacha dit « fais-moi le condensé de tel chapitre », « une fiche de révision en PDF », « résume ce cours sur deux pages », « extrais le cours en condensé », « /condense ».
---

# /condense — le cours en deux pages, en PDF

Une fiche de `eco gestion/` est un **outil de travail** : 800 à 1 700 lignes,
avec ses questions repliées, ses cartes, ses trous. Le condensé en est l'**autre
moitié** : la feuille qu'on relit la veille de l'examen, qu'on imprime, qu'on
garde dans le classeur. Il ne remplace pas la fiche, il en sort.

## Ce qui est demandé

`/condense <cible>` — la cible est :

- **une fiche** (« le chapitre 2 de problèmes éco ») → un condensé ;
- **un cours entier** (« toute l'UE 12A ») → un condensé par chapitre, puis un
  PDF qui les assemble (voir *Plusieurs chapitres*) ;
- **rien** → demander laquelle, en listant les fiches de `eco gestion/`
  (frontmatter `ue:`), celles de la période en cours en premier.

Seules les fiches mises au propre se condensent : un brut de `_brut/` se passe
d'abord par `/eco`.

## Lire avant d'écrire

Lire **toute** la fiche, pas seulement « L'essentiel ». Les blocs qui
nourrissent le condensé, par ordre de valeur :

1. `> [!abstract] L'essentiel` — la colonne vertébrale.
2. Les **définitions en citation** (`> **Le marché du travail** est…`) — elles se
   recopient **mot pour mot** : c'est la formulation attendue à l'examen.
3. Les **formules** et les **calculs types**.
4. `## 🔁 À ne pas confondre` — les paires, qui tombent en QCM.
5. Les **schémas « À savoir refaire »** (`![[x.svg]]` suivi de *À savoir
   refaire…*) — on garde l'embed, le PDF dessine le schéma.
6. `## 🧮 Méthode` — les étapes, sans l'exemple déroulé s'il prend plus de
   trois lignes.
7. Les **auteurs, dates, chiffres** cités par le cours.

Ce qui **ne passe pas** : `## ✅ Contrôle`, `## 🃏 Cartes à créer`, `## 🔄
Comment réviser`, `## À vérifier`, `## Ce que j'ai complété`, les callouts de
provenance (« séance manquée », « cette fiche s'arrête au… »), les liens de
navigation, le blabla d'introduction (« le chapitre, et ce qu'il annonce »).

## Écrire le condensé

Fichier : `eco gestion/_condenses/<même nom que la fiche>.md` (le `_` le tient
hors du passage horaire de `/eco`, qui ne doit pas le « corriger »).

```markdown
---
source: "[[<nom de la fiche>]]"
matiere: UE 13A · Problèmes économiques contemporains
condense: 2026-10-06
---

# Marché du travail, emploi et chômage

UE 13A · chapitre 2 · écrit de 2 h

> [!abstract] L'essentiel
> - …5 puces au plus, une ligne chacune

## 1. <partie du cours>
…
## 🔁 À ne pas confondre
| | |
…
```

**Pas de clé `ue:`** dans ce frontmatter : le site range en chapitre toute
note de `eco gestion/` qui en porte une, et le condensé apparaîtrait en double
dans la carte du cours. L'UE va dans `matiere:`.

Les règles de forme :

- **Deux pages A4 au plus.** C'est la contrainte qui fait le condensé : si ça
  déborde, on coupe, on ne réduit pas la police. Le script donne le nombre de
  pages.
- **Le plan du cours** (ses parties numérotées) reste le plan du condensé :
  on retrouve la fiche, et le prof, dans le même ordre.
- **Une idée = une ligne.** Des puces, des tableaux, du gras sur le mot-clé.
  Pas de phrase d'enchaînement, pas de « il est important de noter que ».
- **Tableau dès qu'on compare** (deux approches, deux mesures, trois taux) :
  c'est ce qui se relit le plus vite.
- Les formules en `$…$` ou en `code`, comme dans la fiche.
- **Trois schémas au plus**, les « À savoir refaire » en priorité.
- `==surligné==` pour **le** piège de la partie, une fois par partie au plus.
- Si la fiche a des trous sur une partie, une seule ligne en fin de partie :
  `⚠️ Partie incomplète dans les notes : <ce qui manque>.` — on ne comble rien.

**La règle qui ne bouge jamais** (la même que `/eco`) : aucun chiffre, aucune
formule, aucun nom d'auteur, aucune définition ne se reformule ni ne se
« corrige ». Le condensé **sélectionne**, il ne réécrit pas le savoir. Un
point marqué ❓ ou « à vérifier » dans la fiche reste marqué ❓.

## Sortir le PDF

```
node .claude/skills/condense/pdf.mjs "eco gestion/_condenses/<nom>.md"
```

Le script rend le markdown avec le moteur du site (callouts, KaTeX), résout
les `![[schémas]]` dans le vault, imprime avec Chrome headless, et écrit le
`.pdf` à côté du `.md`. Il affiche le nombre de pages : **plus de 2 → couper
et relancer**. Puis **regarder le PDF** (Read sur le fichier) avant de le
livrer : un schéma trop grand, un tableau coupé, ça se voit, ça ne se devine
pas.

Enfin `open` le PDF pour Sacha.

### Plusieurs chapitres

Un condensé par chapitre, puis un fichier d'assemblage
`eco gestion/_condenses/UE <ue> - <matière>.md` qui reprend les corps à la
suite, chacun commençant par son `# titre` précédé de
`<div style="break-before: page"></div>` (sauf le premier). On rend ce
fichier-là : un PDF par cours, chaque chapitre sur sa page.

## Après

Commit des fichiers du condensé (le `.md` et le `.pdf`, rien d'autre — le
vault a souvent des changements en cours qui ne sont pas les nôtres) et push,
comme pour les fiches d'éco :

```
git add "eco gestion/_condenses/<nom>.md" "eco gestion/_condenses/<nom>.pdf"
git commit -m "condense: <chapitre> en deux pages"
git push
```

Un condensé se **refait** quand la fiche a changé (nouvelles slides, trous
comblés) : `condense:` dans le frontmatter dit de quand il date, à comparer au
`revu:` de la fiche.
