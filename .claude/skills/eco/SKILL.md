---
name: eco
description: Corrige, synthétise et met en fiche de révision les pages « eco gestion » du vault (Licence 1 Économie & Gestion, Angers). Périmètre = toute page taguée `L1-eco-gestion`, dans le dossier `eco gestion/` ou liant `[[00 - Plan L1 Angers]]`. Corrige la langue et le markdown cassé, remet la hiérarchie de titres d'aplomb, répare les liens et les ancres, ajoute l'encadré « L'essentiel », les pièges et le bloc « Contrôle » — toujours dérivés du contenu de la page, jamais inventés. Ne touche ni aux chiffres de la maquette, ni aux formules, ni aux grilles de suivi. Tourne aussi en automatique toutes les heures (cron `eco-fiches`) : une page par passage, un commit par passage. À utiliser quand Sacha dit « corrige / synthétise / mets en fiche mes cours d'éco », « améliore telle page de L1 », « fais-moi les fiches de révision », ou quand le cron horaire se déclenche.
---

# /eco — Les cours d'éco gestion en fiches de révision

Prend les pages de la Licence 1 Économie & Gestion et les amène à l'état
**« relisible à J-1 de l'examen »** : langue correcte, structure d'aplomb, liens
qui marchent, l'essentiel en tête, les pièges rassemblés, un bloc de contrôle à
la fin. Ce sont des pages déjà denses et déjà bonnes : **on les finit, on ne les
réécrit pas.**

Le contenu de cours est **du savoir sourcé** (maquette officielle, cours, INSEE).
La règle centrale en découle : **aucun fait, chiffre ou formule ne s'invente et
aucun ne se corrige en silence.** Ce qui cloche se signale dans la page.

## Le périmètre

Trois critères, l'un suffit :
- la page est dans `eco gestion/` ;
- son frontmatter porte le tag `L1-eco-gestion` ;
- son corps lie `[[00 - Plan L1 Angers]]`.

```
python3 .claude/skills/eco/etat.py --liste
```

Exclus d'office : `notes/` (dossier de l'app tr4de, c'est `/notes` qui s'en
occupe), `INSPIRATION/`, `INBOX/`, `attachments/`, les fichiers `_*.md`. Si une
page de `notes/` porte le tag, **ne pas la traiter** — le dire, et proposer soit
de la sortir dans `eco gestion/`, soit de lui retirer le tag.

## Deux façons d'être appelé

- **À la main** — « corrige mes cours d'éco », « mets telle page en fiche ». On
  peut traiter plusieurs pages dans le même passage, séquentiellement.
- **Par le cron `eco-fiches`, toutes les heures** — le cas courant. Alors :
  **une seule page par passage**, celle que `--suivant` désigne, et on s'arrête.

```
python3 .claude/skills/eco/etat.py --suivant
```

Il répond soit `rien`, soit la page plus sa raison. L'ordre de priorité :
1. les pages que Sacha a **modifiées** depuis le dernier passage ;
2. les pages **jamais traitées** ;
3. rien d'autre — une page traitée et inchangée **ne se retraite pas**.

Ce troisième point est ce qui empêche le cron de tourner en boucle sur les mêmes
pages et de les réécrire 24 fois par jour. Pour forcer un rattrapage à la main :
`--suivant --relance`.

Une page touchée il y a moins de **10 minutes** est reportée au passage suivant :
Sacha est probablement en train d'écrire dedans, on n'écrit pas par-dessus lui.

Quand `etat.py` dit `rien`, le passage s'arrête là — pas de commit, pas de récap
long, une ligne suffit.

## Règle d'or — le savoir ne bouge pas, la forme oui

| Autorisé | Interdit |
| --- | --- |
| Fautes de frappe, accents, ponctuation, doubles espaces, tabulations orphelines | Réécrire une explication qui se comprend déjà |
| Remettre la hiérarchie de titres d'aplomb (`#` unique, `##`, `###`) | Renommer un titre ciblé par un `[[lien#ancre]]` d'une autre page |
| Réparer un tableau bancal (colonne manquante), un callout sans titre, un bloc de code non fermé | Modifier une valeur dans un tableau, remplir une cellule de suivi |
| Laisser les tableaux valides **exactement** tels quels, alignement des colonnes compris | Reformater un tableau qui marche : Obsidian aligne les colonnes, retirer ce padding ne change rien et pollue le diff (`verifie.py` le refuse) |
| Ajouter `> [!abstract] L'essentiel`, `> [!warning] Les pièges`, `## ✅ Contrôle` **dérivés de la page** | Ajouter une définition, un exemple, une règle, une date d'examen absents de la page |
| Réparer un `[[lien]]` mort vers le bon nom de fichier | Renommer un fichier (ça casse les liens du vault) |
| Signaler une incohérence dans `> [!question] À vérifier` | Corriger un chiffre, un coefficient, un total, une formule |
| Ajouter un tag qui existe déjà ailleurs dans le périmètre | Supprimer ou renommer un de ses tags, toucher aux autres champs du frontmatter |
| Laisser une page déjà propre telle quelle | Rallonger : +15 % de mots max, `verifie.py` refuse au-delà de 30 % |

Anatomie précise des blocs, avant/après réels, liste de ce qui ne se touche
jamais : **`references/forme-fiche.md`. Le lire avant de toucher une page.**

## Procédure d'un passage

1. **Savoir quoi traiter** : `etat.py --suivant` (à la main) — **en mode
   automatique, le prompt du cron nomme déjà la page**, ne pas redemander.
   `rien` → on s'arrête et on le dit.
2. **Snapshot** — le filet, en plus de git. En mode automatique
   `passage.sh` l'a **déjà pris** dans `.claude/skills/eco/scratch/avant.md` et
   le prompt en donne le chemin : s'en servir, ne pas recopier. À la main :
   `cp "eco gestion/<page>.md" <scratchpad>/avant.md`.
3. **Lire la page en entier**, plus le hub `00 - Plan L1 Angers` et les pages
   qu'elle lie sur le même sujet. Impossible de synthétiser en ayant lu la
   moitié, et impossible de repérer une incohérence sans le hub.
4. **Relever avant d'écrire** : fautes, markdown cassé, liens et ancres morts,
   titres mal hiérarchisés, blocs manquants (essentiel / pièges / contrôle),
   incohérences de chiffres avec le hub ou entre sections.
5. **Écrire la page en une fois**, les six blocs dans l'ordre de
   `references/forme-fiche.md`.
6. **Vérifier** :
   ```
   python3 .claude/skills/eco/verifie.py <scratchpad>/avant.md "eco gestion/<page>.md"
   ```
   Une **ERREUR** → restaurer depuis le snapshot, ne pas acter, le dire. Une
   **alerte** → la justifier dans le récap ou revenir en arrière.
7. **Acter** :
   ```
   python3 .claude/skills/eco/etat.py --enregistre "eco gestion/<page>.md" "<ce qui a été fait>"
   ```
   Sans ça le passage suivant croira que la page a bougé et la retraitera.
8. **Commiter le passage**, la page et `etat.json` **seulement** :
   ```
   git add "eco gestion/<page>.md" .claude/skills/eco/etat.json
   git commit -m "eco: <page> — <résumé court>"
   ```
   Jamais `git add -A` : le vault a en permanence des modifications en cours qui
   ne sont pas les nôtres. **Pas de push** : le cron reste local, Sacha pousse
   quand il veut.
9. **Récap** : la page, ce qui a été corrigé, ce qui a été ajouté, les
   incohérences signalées, et `git show --stat --oneline HEAD`.

## Les cinq opérations

- **Corriger** — l'opération par défaut, aucune validation : langue, accents,
  ponctuation, markdown cassé, hiérarchie de titres, tableaux bancals, liens
  morts. Les noms de fichiers restent sans accent.
- **Synthétiser** — l'encadré `L'essentiel` en tête : 3 à 6 lignes, chacune
  dérivée d'une phrase du corps. C'est l'opération à plus forte valeur, et la
  plus facile à rater : une ligne qui apporte une information neuve est une
  invention, elle sort.
- **Mettre en fiche** — les pièges rassemblés dans un `[!warning]`, le bloc
  `## ✅ Contrôle` avec une question par notion et l'ancre qui répond. Huit
  questions maximum, jamais la réponse recopiée.
- **Relier** — vérifier que la page pointe vers son hub, son cycle, sa série
  d'exercices et sa fiche Anki, et que ces liens existent vraiment. Un lien
  manquant s'ajoute, un lien mort se répare.
- **Laisser tel quel** — un choix à part entière, et le bon résultat pour une
  page déjà finie. On l'acte avec `--enregistre "… " "déjà au propre"`.

## Cohérence entre pages — signaler, jamais arbitrer

Les chiffres circulent entre le hub, les cycles et les fiches : coefficients,
ECTS, heures, nombre d'exercices, nombre de cartes Anki. Quand deux pages ne
disent pas la même chose, on **ne tranche pas** : la source est la maquette
`26-27_Maquette_L1_EG.xlsx`, qu'on n'a pas. Un `> [!question] À vérifier` en fin
de page, avec les deux valeurs en conflit et où elles sont écrites.

Le bloc `À vérifier` est **remplacé** à chaque passage, jamais empilé. Une ligne
que Sacha a supprimée reste supprimée : sa suppression est une décision.

## Garde-fous

- **Jamais `rm`**, jamais de renommage de fichier, jamais de suppression de
  section entière sans validation explicite.
- **Une page par passage** en mode cron. Un passage qui touche trois pages est
  un passage qui a dérivé.
- `verifie.py` passe **avant** le commit. Erreur → restauration depuis le
  snapshot, et on le dit au lieu de forcer.
- **Ne rien remplir à sa place** : grilles d'essais, scores, cases `- [ ]`,
  `statut:`. `verifie.py` refuse une cellule de suivi remplie.
- **Ne pas se battre contre lui** : si une correction est défaite dans une page
  au passage suivant, c'est qu'il n'en voulait pas — ne pas la réappliquer,
  le noter dans le récap.
- **Ne pas toucher au reste du vault** : ni `notes/`, ni les fiches d'autres
  domaines, même si une page d'éco les lie.
- Le vault est un dépôt git : montrer `git show --stat` plutôt que décrire les
  changements de mémoire.
