---
name: fiche-pdf
description: La MISE EN FORME des fiches de révision en PDF — la charte (A4, typo, couleurs, encadrés, tableaux, schémas, pied de page, bandeau « chapitre en cours ») et le script qui rend un markdown du vault en PDF prêt à imprimer. Utilisé par /condense pour chaque condensé ; à charger aussi quand Sacha veut changer l'allure des PDF (« le PDF est trop serré », « mets les titres en couleur », « change la police des fiches ») ou re-rendre un PDF sans toucher au contenu (« refais le PDF », « régénère tous les PDF »).
---

# /fiche-pdf — la mise en forme des fiches de révision

Le **contenu** d'un condensé, c'est `/condense` (quoi garder, quoi couper).
**L'allure** du PDF, c'est ici : une seule charte pour toutes les fiches, pour
qu'elles se ressemblent dans le classeur et se relisent toutes de la même façon.

## Rendre un PDF

```
node .claude/skills/fiche-pdf/pdf.mjs "eco gestion/_condenses/<nom>.md"
```

→ écrit `<nom>.pdf` à côté du `.md` et affiche le nombre de pages. Le markdown
passe par le moteur du site (`vault-gallery/scripts/markdown.mjs` : callouts,
KaTeX), les `![[schémas]]` sont cherchés dans le vault, Chrome headless
imprime. Rien à installer.

**Toujours regarder le résultat** avant de le livrer — un schéma trop grand,
un tableau coupé, une page presque vide, ça se voit, ça ne se devine pas :

```
qlmanage -t -s 1200 -o <scratchpad> "<nom>.pdf"   # vignette de la page 1
```

puis Read sur le `.png`. Pour la page 2 : rendre vers le scratchpad avec un
second argument (`pdf.mjs <md> <scratch>/x.pdf`) après avoir coupé le haut, ou
simplement ouvrir le PDF (`open`).

**Régénérer tous les PDF** (après un changement de charte) :

```
for f in "eco gestion/_condenses/"*.md; do node .claude/skills/fiche-pdf/pdf.mjs "$f"; done
```

Le contenu ne bouge pas, la date imprimée non plus (elle vient de `condense:`).

## Ce que le markdown pilote

Frontmatter lu par le script :

- `matiere:` — pied de page de chaque page (à gauche) et fin du document.
- `condense:` — la date imprimée (« condensé le … »). C'est la date du
  **contenu** : on la change quand on modifie le condensé, pas pour un simple
  re-rendu.
- `etat: en cours` — le chapitre n'est pas fini au cours : bandeau orange sous
  le titre, « Chapitre en cours — ce condensé s'arrête où en est le cours ».
- `jusqua:` — avec `etat: en cours`, où s'arrête le cours, entre parenthèses
  dans le bandeau (« partie 2, la mesure du chômage »).

Et dans le corps :

| Markdown | Rendu |
|---|---|
| `# Titre` puis une ligne | grand titre, puis sous-titre gris (UE · chapitre · épreuve) |
| `> [!abstract] L'essentiel` | encadré bleu-gris, en tête |
| `> [!warning]` / `> [!danger]` | encadré à liseré orange / rouge |
| `> [!tip]` | encadré à liseré bleu canard |
| `> **Le X** est …` (citation simple) | définition sur fond gris, filet noir |
| `## 1. Partie` | titre de partie souligné d'un trait noir |
| tableau | pleine largeur, en-tête grisé, jamais coupé entre deux pages |
| ligne vide `\| \| \|` dans un tableau | petit espace entre deux paires « à ne pas confondre » |
| `![[x.svg]]` | schéma centré, 60 % de large et 48 mm de haut au plus |
| deux `![[…]]` sur la même ligne | côte à côte |
| `![[x.svg\|300]]` | largeur imposée en px |
| `==texte==` | surligné jaune — **le** piège, un par partie |
| `$…$` / `$$…$$` | formule KaTeX |
| `<div style="break-before: page"></div>` | saut de page (assemblage de chapitres) |

## La charte

Elle vit dans le `<style>` de `pdf.mjs`. Ses choix, à garder si on la retouche :

- **A4**, marges 11 / 12 / 13 mm. Pied : matière à gauche, `page / total` à
  droite (boîtes `@page`, Chrome ≥ 131).
- **Texte 9,4 pt**, interligne 1,42, police système (San Francisco), césure
  française. Ne pas descendre sous 9 pt : un condensé trop long se **coupe**,
  il ne se tasse pas.
- **Noir et gris** pour le texte ; la couleur ne sert qu'à signaler — rouge
  (alerte), orange (prudence, chapitre en cours), vert (test), bleu canard
  (astuce), bleu nuit (l'essentiel). Une fiche imprimée en noir et blanc doit
  rester lisible : rien ne repose sur la couleur seule.
- **Rien ne se coupe entre deux pages** : encadrés, tableaux, schémas
  (`break-inside: avoid`) ; un titre ne reste jamais seul en bas de page.
- Les blocs repliés (`<details>`) sont imprimés ouverts.
- Les liens deviennent du texte : le papier ne clique pas.

Retoucher la charte = éditer le CSS de `pdf.mjs`, rendre **un** condensé vers
le scratchpad, le regarder, puis régénérer tous les PDF et les committer
ensemble (`fiche-pdf: <ce qui change>`).

## Après un rendu

Le PDF va avec son `.md` dans le même commit (voir `/condense`, section
*Après*) : le site (`/cours`) le propose en téléchargement sur le chapitre du
même nom, bouton **« Fiche condensée (PDF) »**, en haut de la fiche à côté de
« Lancer le QCM ».
