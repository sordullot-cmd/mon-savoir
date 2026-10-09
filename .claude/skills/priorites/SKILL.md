---
name: priorites
description: Dit QUOI RÉVISER EN PRIORITÉ dans une matière d'éco gestion pour réussir le partiel, et QUOI LAISSER. Lit le cours de référence COMPLET de `~/Documents/L1/<matière>/` (les cours des anciens élèves et les slides des profs — toutes les versions, tous les chapitres), les annales, le format d'épreuve et ce que Sacha a déjà vu cette année dans `eco gestion/`, puis classe chaque notion sur quatre niveaux (🔴 incontournable · 🟠 important · 🟡 utile · ⚪ secondaire) avec, pour chacune, POURQUOI elle est à ce niveau (les preuves : tombée aux annales, présente dans toutes les versions du cours, définition encadrée par le prof…) et COMMENT la réviser (carte mot pour mot, calcul à refaire, schéma à redessiner, mécanisme en deux phrases, paragraphe chronométré). Sort une page `eco gestion/_priorites/UE <ue> - <matière>.md` et son PDF. À utiliser quand Sacha dit « qu'est-ce que je révise en priorité », « les choses les plus importantes pour le partiel », « par quoi je commence », « qu'est-ce que je peux laisser tomber », « fais-moi la carte des priorités de telle matière », « /priorites ».
---

# /priorites — quoi réviser d'abord, quoi laisser

Demandé par Sacha le 9 octobre 2026 : « les connaissances prioritaires pour
passer les partiels de ce cours, les choses les plus importantes à réviser,
quoi, comment, et les choses moins intéressantes ».

`/eco` fait les fiches, `/condense` les réduit à deux pages. **`/priorites`
ne résume pas le cours : il le trie.** La sortie est une liste ordonnée de
notions, chacune avec son niveau, sa preuve et sa façon de la travailler. On
la lit pour savoir **où mettre la prochaine heure**.

## La cible

`/priorites <matière>` — une matière = un dossier de `~/Documents/L1/`
(« problèmes éco » → `Problèmes économiques contemporains`). Sans cible :
prendre les matières de la période d'examen en cours (voir `eco gestion/Plan -
Examen P1.md`, puis le calendrier) et les faire toutes. Une matière sans cours
complet dans `~/Documents/L1` (18C, par exemple) : le dire, et travailler
seulement sur les fiches du vault et les annales s'il y en a.

## Les sources, et ce que chacune prouve

Lire **tout**, pas un échantillon. Extraction :

```
textutil -convert txt -stdout "<fichier>.docx"
python3 -c "import fitz,sys; d=fitz.open(sys.argv[1]); print('\n'.join(p.get_text() for p in d))" "<fichier>.pdf"
```

Les images (annales photographiées) : Read sur le `.jpg`.

| Source | Où | Ce qu'elle prouve |
|---|---|---|
| **Annales** (sujets, corrigés, copies notées) | `~/Documents/L1/<matière>/Annales*/`, `Ancien partiel/` | **ce qui tombe vraiment** — le signal le plus fort |
| **Slides du prof** | `diaporama/`, `Diaporama de cours/`, `*.pdf` des CM | ce que le prof juge assez important pour l'écrire — et le millésime le plus récent |
| **Cours complets des anciens élèves** | `CM/`, `2022/`, `CM <prof>/`, `Ancien cour/`… | le **noyau stable** : une notion présente dans *toutes* les versions, d'année en année, est le cœur du cours |
| **Format d'épreuve** | `eco gestion/Plan - Examen P1.md`, en-têtes des sujets, fiches du vault (« Le format du contrôle ») | quels **types** de savoir rapportent : définition au mot près (QCM), mécanisme (question courte), calcul, argumentation |
| **Les fiches de Sacha** | `eco gestion/*.md` (frontmatter `ue:`), `eco gestion/_brut/` | ce qui est **confirmé cette année** — le prof a pu changer son cours |
| **QCM d'entraînement générés par IA** | `qcm entrainement/` | **rien** sur ce qui tombe. Ne compte pas comme preuve. |

## Le barème des priorités

Pour chaque notion du cours, relever les preuves, puis classer :

- 🔴 **Incontournable** — tombée **aux annales** (au moins une fois), **ou**
  présente dans **toutes** les versions du cours **et** dans les slides du
  prof **et** directement dans le format d'épreuve (une définition pour un
  QCM, un calcul, un mécanisme central). Ne pas la savoir, c'est perdre des
  points à coup sûr.
- 🟠 **Important** — présente dans la plupart des versions, ou mise en
  valeur par le prof (définition encadrée, « à retenir », schéma répété),
  mais jamais vue aux annales ; ou base sans laquelle une notion 🔴 ne se
  comprend pas.
- 🟡 **Utile** — exemples, chiffres, auteurs secondaires : ils nourrissent la
  question de réflexion ou départagent deux propositions de QCM, ils ne font
  pas la note seuls.
- ⚪ **Secondaire** — dans une seule version du cours, digression, anecdote,
  historique détaillé, chiffre isolé, partie que le prof a retirée. **Le dire
  franchement** : lire une fois, ne pas en faire de cartes.

Règles de tri :

- **Les annales priment sur tout.** Une notion tombée deux années de suite
  passe en tête de 🔴, même si le cours y consacre trois lignes.
- **Le cours de cette année prime sur les anciens.** Une notion des anciens
  cours absente des fiches et des slides 25-26 : la classer, mais avec ❓
  (« pas encore vue cette année — le prof a pu la retirer »). Un chapitre
  entier dans ce cas : une ligne, pas une section.
- **Pas plus de ~12 notions 🔴 par matière.** Si tout est prioritaire, rien
  ne l'est : on resserre.
- **Rien ne s'invente.** Une notion n'entre dans la liste que si elle est
  dans une source ; une preuve n'est citée que si elle existe (on nomme le
  fichier ou l'année). Aucun chiffre, aucune formule, aucun auteur ne se
  corrige : ce qui cloche entre deux versions se signale (⚠️).

## Le « comment » — une méthode par type de savoir

Chaque notion 🔴 et 🟠 reçoit **une** façon de la travailler, choisie selon ce
que l'épreuve en demande :

| Type de savoir | Comment le réviser |
|---|---|
| **Définition** (QCM, question courte) | carte recto énoncé / verso formulation **mot pour mot** + le mot qui la distingue de sa voisine |
| **Paire confusable** | travailler les deux sens (positive ↔ normative) : une carte par sens |
| **Calcul / indicateur** | le refaire de tête sur un exemple, sans calculatrice si l'épreuve l'interdit |
| **Schéma / graphique** | le redessiner de mémoire, puis le commenter en trois phrases |
| **Mécanisme** | cause → mécanisme → conséquence, en deux phrases, à voix haute |
| **Débat / opposition d'auteurs** | un tableau à deux colonnes, puis un paragraphe chronométré |
| **Exemple / chiffre** | en garder **un** par idée, le plus frappant |

Et un **temps estimé** par bloc, pour que la page se convertisse en planning.

## La page

`eco gestion/_priorites/UE <ue> - <matière>.md` (le `_` la tient hors du
passage horaire de `/eco` ; pas de clé `ue:` dans le frontmatter, pour la même
raison que `/condense`).

```markdown
---
matiere: UE 13A · Problèmes économiques contemporains
condense: 2026-10-09
sources: <liste courte des dossiers lus>
---

# Quoi réviser en priorité — <matière>

UE <ue> · <épreuve, durée, format> · examen le <date>

> [!abstract] Si tu n'as que 3 heures
> - les 5 à 7 notions 🔴 qui rapportent le plus, une ligne chacune

## Ce que l'épreuve récompense
3 à 5 lignes : le format, et ce qu'il dit sur le type de savoir à travailler.

## 🔴 Incontournable
### <Notion> · <chapitre>
- **Quoi** : ce qu'il faut savoir exactement (la définition mot pour mot, la formule, les étapes)
- **Pourquoi** : les preuves (annales 2024 · présente dans les 3 versions · encadrée sur la slide 12)
- **Comment** : la méthode, et le temps (15 min)

## 🟠 Important
(même forme, plus court : Quoi / Comment sur une ligne chacun)

## 🟡 Utile
une ligne par notion

## ⚪ Secondaire — à lire une fois, pas plus
une ligne par notion, avec la raison (« une seule version du cours », « digression »)

## L'ordre de travail
une liste numérotée qui enchaîne les blocs, avec le temps total — calée sur
les jours qui restent avant l'examen

## Ce qui reste incertain
❓ les chapitres pas encore vus cette année, ⚠️ les désaccords entre versions
```

La règle d'écriture est celle des fiches : **une idée = une ligne**, gras sur
le mot-clé, pas de phrase d'enchaînement, le tutoiement de Sacha.

## Sortir le PDF

```
node .claude/skills/fiche-pdf/pdf.mjs "eco gestion/_priorites/<nom>.md"
```

Pas de limite de pages, mais une page de priorités qui dépasse **quatre
pages** n'a pas assez trié. Regarder la vignette (voir `/fiche-pdf`) avant de
livrer.

## Après

Commit du `.md` et du `.pdf` seulement (le vault a souvent des changements en
cours qui ne sont pas les nôtres), puis push :

```
git add "eco gestion/_priorites/<nom>.md" "eco gestion/_priorites/<nom>.pdf"
git commit -m "priorites: <matière> — ce qui tombe, ce qui se laisse"
git push
```

À refaire quand une annale arrive, quand un chapitre est fini en cours, ou à
une semaine de l'examen pour recaler « L'ordre de travail » sur les jours qui
restent.
