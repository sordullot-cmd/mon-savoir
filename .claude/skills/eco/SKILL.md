---
name: eco
description: Transforme les pages « eco gestion » du vault (Licence 1 Économie & Gestion, Angers) en fiches avec lesquelles on révise vraiment, pour réussir les examens de fin d'année. Intègre les notes d'amphi brutes déposées dans `eco gestion/_brut/` (fautes, structure en vrac, phrases interrompues) en fiches complètes, et améliore les fiches existantes. Chaque fiche est bâtie sur ce qui fait retenir : questions à réponses repliées pour se tester, tableaux de paires confusables, méthodes pas à pas, cartes Anki extraites, et les trous du cours signalés au lieu d'être comblés. Corrige la langue et le markdown, répare liens et ancres. Ne touche jamais un chiffre, une formule, un nom d'auteur : ce qui cloche est signalé, pas corrigé. Périmètre = toute page taguée `L1-eco-gestion`, dans `eco gestion/`, ou liant `[[00 - Plan L1 Angers]]`. Tourne aussi seul toutes les heures (LaunchAgent `com.sacha.eco-fiches`) : une page par passage, un commit par passage. À utiliser quand Sacha dit « corrige / synthétise / améliore mes cours d'éco », « fais-moi les fiches de révision », « mets mes notes d'amphi au propre », ou quand le passage horaire se déclenche.
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
prises. C'est la **source**, elle ne se modifie jamais et ne se met jamais en
fiche sur place. Elle produit une fiche à côté, dans `eco gestion/`, dont le
frontmatter porte `source: _brut/<nom>.md`. Un brut sans fiche est **prioritaire
sur tout le reste** : c'est du cours qui n'est pas encore révisable.

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

## Règle d'or — le savoir ne bouge pas, la forme et la clarté oui

| Autorisé | Interdit |
| --- | --- |
| Fautes, accents, ponctuation, phrases cassées rendues lisibles | Prêter au prof une définition qu'il n'a pas donnée |
| Hiérarchie de titres d'aplomb (`#` unique, `##`, `###`), listes, indentations | Renommer un titre ciblé par un `[[lien#ancre]]` d'une autre page |
| Transformer deux paragraphes opposés en tableau de contraste | Modifier une valeur dans un tableau, remplir une cellule de suivi |
| Ajouter les blocs qui servent à réviser (`L'essentiel`, `À ne pas confondre`, `Méthode`, `Cartes à créer`, `Contrôle`) | Remplir un de ces blocs sans matière dans la page — un bloc vide est du décor |
| Dérouler un exemple **calculable depuis une formule de la page** | Inventer un exemple, un chiffre, un coefficient, une date de partiel |
| Ajouter une notion manquante **dans un `> [!info]- Complément (absent de tes notes)`**, replié | Ajouter du cours sans ce marquage : en examen c'est le cours du prof qui est évalué |
| Signaler un trou ou une incohérence dans `> [!question] À vérifier` | Corriger un chiffre, une date, un nom d'auteur, une formule |
| Garder ses exemples et ses remarques (`ex Decathlon`, `licornes : Doctolib`) | Supprimer un exemple au nom de la concision |
| Laisser les tableaux valides tels quels, alignement compris | Reformater un tableau qui marche (`verifie.py` le refuse) |
| Ajouter un tag déjà utilisé dans le périmètre | Supprimer ou renommer un de ses tags, toucher au reste du frontmatter |

Test de relecture : **est-ce qu'il peut se tester avec cette page, seul, sans
son cahier ?** Si non, la fiche n'est pas finie. Et : **est-ce qu'il peut
distinguer ce qui vient de son amphi de ce que j'ai ajouté ?** Si non, c'est un
défaut grave — tout ajout de contenu est replié et marqué.

## Procédure d'un passage

1. **Savoir quoi traiter** : `etat.py --suivant` (à la main) — en mode
   automatique, le prompt nomme déjà la cible, ne pas redemander.
2. **Snapshot** — en mode automatique `passage.sh` l'a déjà pris dans
   `.claude/skills/eco/scratch/avant.md` et le prompt en donne le chemin. À la
   main : `cp "<cible>" <scratchpad>/avant.md`.
3. **Lire en entier** la cible, plus le hub `00 - Plan L1 Angers`, la page de
   cycle correspondante et [[MCC - Tableau de bord]] pour le mode d'évaluation.
   Impossible de prioriser sans savoir ce que la notion vaut en points.
4. **Relever avant d'écrire** : les paires confusables, les procédures, les
   définitions cartables, les phrases interrompues, les incohérences de chiffres,
   les liens et ancres morts, les blocs manquants.
5. **Écrire la page en une fois**, blocs dans l'ordre de `references/apprendre.md`.
6. **Vérifier** :
   ```
   python3 .claude/skills/eco/verifie.py <avant> "<page>"                 # fiche
   python3 .claude/skills/eco/verifie.py "eco gestion/_brut/x.md" "<fiche>" --integration
   ```
   **ERREUR** → restaurer depuis le snapshot, ne pas acter, le dire. **Alerte**
   → la justifier dans le récap ou revenir en arrière.
7. **Acter** : `etat.py --enregistre "<page>" "<ce qui a été fait>"`. Le brut
   cité en `source:` est acté avec la fiche. Sans ça, tout repasse au tour
   suivant.
8. **Commiter**, la page et `etat.json` **seulement** :
   ```
   git add "<page>" .claude/skills/eco/etat.json
   git commit -m "eco: <page> — <résumé court>"
   ```
   Jamais `git add -A` : le vault a en permanence des modifications qui ne sont
   pas les nôtres. **Pas de push** : le passage reste local.
9. **Récap** : ce qui a été corrigé, ce qui a été ajouté (**nommément**, surtout
   les `Complément`), les trous signalés, et `git show --stat --oneline HEAD`.

## Les six opérations

- **Intégrer un brut** — l'opération à plus forte valeur. Des notes d'amphi
  deviennent une fiche complète dans `eco gestion/`, avec `source:` vers le
  brut. Le brut reste **intact**. Nom de fiche : `<Matière> - <Sujet> (CM).md`,
  sans accent dans le nom de fichier (un renommage casse les liens du vault).
- **Corriger** — langue, markdown, hiérarchie, tableaux bancals, liens morts.
  Aucune validation nécessaire.
- **Rendre révisable** — les blocs qui servent les six leviers : `L'essentiel`
  (5 lignes), `À ne pas confondre`, `Méthode`, `Cartes à créer`, `Contrôle` avec
  réponses repliées `> [!question]-`. Uniquement là où il y a matière.
- **Compléter, marqué** — une notion indispensable et absente part dans un
  `> [!info]- Complément (absent de tes notes)`, replié, jamais fondue dans le
  cours. Toujours annoncé dans le récap.
- **Relier** — vérifier que la fiche pointe vers son hub, son cycle, sa série
  d'exercices, sa fiche Anki, et que ces liens résolvent.
- **Laisser tel quel** — un choix à part entière pour une page déjà finie. On
  l'acte avec `--enregistre "…" "déjà au propre"`.

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

## Garde-fous

- **Jamais `rm`**, jamais de renommage de fichier, jamais de suppression d'une
  section entière sans validation explicite.
- **Un brut ne se modifie jamais.** C'est la seule trace de ce que le prof a
  dit. Toute amélioration vit dans la fiche.
- **Une cible par passage** en mode automatique. Un passage qui touche trois
  pages est un passage qui a dérivé.
- `verifie.py` passe **avant** le commit. Erreur → restauration depuis le
  snapshot, et on le dit au lieu de forcer.
- **Ne rien remplir à sa place** : grilles d'essais, scores, cases `- [ ]`,
  `statut:`. `verifie.py` refuse une cellule de suivi remplie.
- **Tout ajout de contenu est replié et marqué.** Un complément fondu dans le
  cours est un défaut grave : il réviserait quelque chose que son prof n'a pas
  dit.
- **Ne pas se battre contre lui** : si une amélioration est défaite au passage
  suivant, c'est qu'il n'en voulait pas — ne pas la réappliquer, le noter.
- **Ne pas toucher au reste du vault** : ni `notes/`, ni les fiches d'autres
  domaines, même si une page d'éco les lie.
- Le vault est un dépôt git : montrer `git show --stat` plutôt que décrire les
  changements de mémoire.
