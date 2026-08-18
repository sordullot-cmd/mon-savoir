---
name: notes
description: Transforme les notes prises sur le tas (dossier `notes/`, synchronisé avec l'app tr4de) en vraies notes exploitables. Le coeur du travail est **transversal** : lire toutes les notes, repérer un sujet éparpillé sur plusieurs d'entre elles, et le rassembler dans une note à lui — le reste devient une ligne courte plus un lien. Nettoie, structure, consolide, **améliore la page** (classe, met en lignes lisibles, dérive ce qui est déductible, fait remonter ses questions ouvertes), scinde, tague, relie, sans jamais changer la façon d'écrire de Sacha (mots simples, concis). À utiliser quand il dit « range / synthétise / améliore / nettoie / mets au propre mes notes », « fusionne ces notes », « il faut des tags », ou qu'il pointe une note en vrac.
---

# /notes — Mettre les notes au propre

Prend des notes écrites à la volée (listes en vrac, indentations faites à l'espace, sujets mélangés, fautes de frappe) et en fait des notes qu'on retrouve et qu'on relit. **On ne réécrit pas Sacha : on range ce qu'il a écrit.**

Nettoyer note par note ne suffit pas — c'est le minimum, pas le travail. Le travail est de **lire tout le lot et de faire circuler le contenu** : un sujet éparpillé sur trois notes se rassemble dans une note à lui, une info qui appartient à une autre note y part, une note chapeau garde la **version courte** plus un lien.

Cible par défaut : `notes/` (le dossier de l'app). Sinon le chemin ou les notes qu'il indique.

## Deux façons d'être appelé

Sacha n'a pas à savoir lequel des deux il demande : le skill le détermine seul.

- **Passage complet** — première fois, ou « range / mets au propre mes notes » sans plus de précision. On lit tout, on cartographie, on consolide.
- **Passage incrémental** — le cas courant : il a modifié une note dans l'app et veut qu'elle soit rerangée (« j'ai changé ma note recette », « range ma note X », ou juste `/notes` après coup). Inutile de relire les 15 notes à fond.

**Toujours commencer par savoir ce qui a bougé :**

```
python3 .claude/skills/notes/etat.py notes
```

Il compare l'état actuel à celui du dernier passage (`etat.json`, gardé à côté du script donc hors du dossier synchronisé) et liste les notes **modifiées, nouvelles, renommées, disparues**. S'il annonce « rien à faire », on le dit et on s'arrête — pas de passage pour rien.

**Deux garde-fous appris à la dure, le 18 août 2026 :**

- **Si Sacha nomme une note, on la lit — même si l'outil dit « rien à faire ».** Ce jour-là `etat.py` annonçait 15 notes inchangées alors que Sacha venait d'ajouter onze articles à `recette et courses` : la synchro avait écrit **juste avant** l'enregistrement du passage précédent, donc sa version avait été actée sans être traitée. Sa parole bat l'outil, toujours.
- **Ne jamais acter une note qu'on n'a pas traitée.** Le run de lecture ouvre le passage en écrivant `etat-debut.json` ; `--enregistre` compare et **prévient** si une note a bougé entre-temps. Si c'est l'app ou Sacha qui a écrit pendant le passage, on traite la note **avant** d'acter — sinon son changement devient invisible pour toujours.

Un passage incrémental reste **transversal, en plus petit** : la note modifiée peut contenir du contenu qui appartient ailleurs. On lit donc la note touchée, l'index `_NOTES.md`, et les notes des sujets qu'elle aborde — pas tout le lot. Et on finit toujours par :

```
python3 .claude/skills/notes/etat.py notes --enregistre
```

sinon le passage suivant croira que tout a changé.

## Règle d'or — la voix ne change pas

| Autorisé | Interdit |
| --- | --- |
| Corriger fautes de frappe, accents, ponctuation (`exxpire` → `expire`, `ingrediens` → `ingrédients`, `virlangue` → `virelangue`) | Reformuler une phrase qui se comprend déjà |
| Convertir les indentations et alignements faits à l'espace en vraies listes markdown imbriquées | Remplacer ses mots par du vocabulaire plus « pro » ou plus long |
| Regrouper en sections **avec ses mots à lui** (`peau :`, `muscu :`, `entry trigger :`) | Ajouter une explication, une définition, un conseil, une conclusion qu'il n'a pas écrits |
| Remettre d'aplomb des colonnes alignées à la main (une ligne par élément, ses `=` comme séparateur) | Traduire ou développer son jargon (`fvg`, `ivfg`, `ob`, `rb`, `cisd`, `sdtv`, `po3`, `htf/ltf`, `rr`, `drawdown`, `payout`) |
| Fusionner, scinder, dédupliquer, renommer — **après validation** | Corriger en silence un chiffre, un total, une date, une note sur 10 |
| Ajouter des tags et des `[[liens]]` | Ajouter une phrase d'intro/conclusion, des emojis (garder les siens s'il en a mis) |
| Laisser une note propre telle quelle | Rallonger : une note nettoyée est **plus courte ou égale** à l'original (hors structure) |

Test de relecture : si on entend un rédacteur, c'est raté. On doit entendre Sacha — mots simples, phrases courtes, tirets.

Détail concret dans `references/exemples.md` (avant/après pris dans ses vraies notes). **Le lire avant de toucher une note.**

## Procédure

1. **Savoir ce qui a bougé** : `python3 .claude/skills/notes/etat.py notes` (cf. § Deux façons d'être appelé). C'est ce qui décide du périmètre.
2. **Snapshot avant** : copier le dossier ciblé dans le scratchpad (`cp -R notes <scratchpad>/notes-avant`). C'est le filet de sécurité, en plus de git — et **relire le dossier maintenant**, pas se fier à une lecture plus ancienne dans la session (cf. § Contraintes techniques : l'app peut avoir tout réécrit).
3. **Tout lire, en entier** (passage complet) ou **la note touchée et ses voisines de sujet** (passage incrémental). Impossible de décider une fusion ou une scission en ayant lu la moitié. Notes courtes → lecture directe ; au-delà de ~30 notes, paralléliser la lecture (un agent par lot, analyse seulement, aucune écriture) et garder l'écriture centralisée.
4. **Cartographier — sujets x notes, pas note par note.** Lister les **sujets** du lot, et pour chacun **toutes** les notes où il apparaît. Un sujet présent dans deux notes ou plus est un candidat à la consolidation ; un sujet seul dans une note qui parle d'autre chose est un candidat à la scission. Relever aussi, par note : tags actuels, doublons, chiffres douteux, `pinned` ou non. C'est cette table qui produit le plan — sans elle on ne fait que du nettoyage cosmétique.
5. **Décider les opérations** — récap `note → opération → tags → destination` (dans la conversation, pas dans une note).
6. **Une seule question groupée** pour tout ce qui est ambigu (§ Quand demander).
7. **Écrire une note à la fois**, séquentiellement (le dossier est synchronisé, deux écritures concurrentes se marchent dessus).
8. **Vérifier** : `python3 .claude/skills/notes/verifie.py <scratchpad>/notes-avant notes [--synthese=<chemin/nom.md>]` — il parcourt les sous-dossiers et compare par `tr4de-id`, donc un déplacement apparaît comme un renommage — invariants techniques (identifiants préservés, pièces jointes intactes, note pas rallongée, pas d'emoji ajouté). Un invariant cassé → restaurer la note depuis le snapshot.
9. **Index, état, récap** : `etat.py notes --enregistre` pour acter le passage, mettre à jour `_NOTES.md` (notes par catégorie, une ligne chacune) et récapituler ce qui a bougé, les tags créés, les questions restées ouvertes.

## Les huit opérations

- **Nettoyer** — l'opération par défaut : structure, listes, fautes de frappe, colonnes remises d'aplomb en une ligne par élément. Aucune validation nécessaire.
- **Fusionner** — seulement de vrais doublons ou deux fragments du **même** sujet. Deux notes nommées d'après leur **source** (une méthode, une personne, une vidéo) ne fusionnent pas : on perd la provenance → on les **relie** depuis une note hub. Validation obligatoire.
- **Scinder** — quand une note contient un sujet clairement étranger aux autres (exemple vécu : `social media` contenait un bloc `fiscalité`). Le sujet part dans sa note, un `[[lien]]` reste dans l'ancienne. Validation obligatoire.
- **Renommer** — seulement si le nom ne dit pas ce qu'il y a dedans. Garder ses minuscules et ses mots. Validation obligatoire (le nom voyage jusqu'à l'app).
- **Relier** — `[[liens]]` entre notes d'un même thème. Une note `pinned` reste en place et devient le **hub** : elle garde ses lignes courtes et pointe vers les notes détaillées.
- **Consolider par sujet (transversal)** — l'opération qui a le plus de valeur. Un sujet éparpillé sur plusieurs notes se rassemble dans **une** note qui le porte :
  - **une note par sujet, une seule.** Le contenu se **déplace**, il ne se recopie jamais : deux copies divergent au premier changement.
  - la note d'origine **ne meurt pas** : si c'est un journal ou une note épinglée, elle garde sa fonction (les dates, les priorités) et chaque entrée devient une ligne courte plus le lien vers la note du sujet.
  - **version courte autorisée dans une note chapeau** : `glow uppp` garde `bien parler = respiration diaphragmatique …` plus le lien, la note `bien communiquer` porte le détail. Court **et** lié, pas court **ou** lié.
  - une info qui appartient manifestement à une **autre note existante** y part, à l'endroit qui l'attend (le `trader avec le temps` du journal a rejoint la ligne `trade with time` de `base trading`).
  - **ne pas consolider ce qui n'a rien à y gagner** : deux notes de méthode ou de source différentes (`powell`, `sdtv`) restent séparées, un lien suffit. Si le regroupement ne rend rien plus facile à retrouver, ne pas le faire.
  - un sujet qui devient une note mérite en général un **tag de famille** (`#glow` pour `bien communiquer`, `meta learning`, `bien s'habiller`, `glow uppp`) — c'est ce qui rend la famille cherchable dans l'app.
- **Améliorer la page** — donner à la note la forme de ce qu'elle sert, à partir de **son** contenu et de rien d'autre :
  - **la forme du domaine.** Une page qui mélange des plats et des ingrédients devient une section `repas :` où chaque ligne est `plat = ses ingrédients`, pris dans ce qu'il a écrit. Un plat dont il n'a pas noté les ingrédients garde son `=` **vide** (`Plat japonais =`) — sa propre notation, celle de `hunter x hunter =`.
  - **classer une liste en vrac.** Une liste de courses se range par type (feculents, proteines, condiments, maison), une liste d'achats par pièce (appart, salle de bain, bureau). Les étiquettes de classement sont de la **structure**, pas du contenu — c'est permis. Ce qu'on n'arrive pas à classer va sur une ligne `a preciser :`, jamais dans une case au hasard.
  - **dériver ce qui est déductible de ses lignes.** Rattacher `Pates + poulet` aux `pate` et `poulet` de ses courses, c'est lire ce qu'il a écrit. Inventer un ingrédient pour compléter une recette, non.
  - **faire remonter les manques et les questions.** C'est la meilleure amélioration possible, et elle n'ajoute rien : `dans les repas mais pas dans les courses : poivre, saucisses, sauces tomates`, ou une section `a trancher :` qui rassemble ses propres questions (`quelle est mon A+ setup`, `je ne sais pas ce que ca veut dire`).
  - **synthèse d'un domaine étalé sur plusieurs notes** : une section par sujet, une ligne par élément, chacune finissant par `→ [[note d'origine]]`. Pas de tableau (cf. § Structure), la provenance à chaque ligne. Elle doit rester **beaucoup plus courte** que les notes qu'elle résume (`verifie.py --synthese=<nom>` refuse au-delà de 25 % du dossier) — sinon c'est une copie, et deux copies divergent.
  - **la frontière** : classer, regrouper, mettre en lignes, relier, dériver de ce qui est écrit = oui. Ajouter un ingrédient, un plat, une définition, un chiffre, un conseil = non **par défaut**. Ce qui manquerait devient une **question dans le récap** (« tu veux que je classe aussi par midi / soir ? tu ne l'as jamais écrit »).
  - **exception : compléter quand il le demande.** Sacha peut lever la règle sur une page précise — il l'a fait le 18 août 2026 pour `recette et courses` : « lorsqu'il y a un plat sans ingredient tu les rajoutes toi meme ». Alors on complète, avec trois garde-fous :
    - **au plus simple et au plus courant** : `Plat japonais = riz + sauce soja + oeuf + poulet`, pas une recette de chef. Réutiliser d'abord ce qui est déjà dans ses courses (`oeuf`, `poulet`), n'ajouter que ce qui manque vraiment.
    - **sa notation** : `plat = ingrédient + ingrédient`, comme il l'écrit.
    - **ne pas toucher à ses listes** : les ingrédients ajoutés n'entrent pas dans son `courses :`, ils apparaissent sur la ligne `dans les repas mais pas dans les courses :`. C'est lui qui décide de les acheter.
    - **dire dans le récap ce qui a été ajouté**, nommément — dans la conversation, pas dans la note. L'exception vaut pour la page nommée, elle ne se généralise pas au reste du vault.
    - **le plat déduit est permis lui aussi**, sur cette page : quand des articles ne servent dans aucun repas et forment un ensemble évident, proposer la ligne (`petit dej = skyr + flocon d'avoine + banane + beurre de cacahuete`) — validé le 18 août 2026. Le nom du plat est inventé, donc on le **demande** quand l'ensemble n'est pas évident (un gratin ou une soupe à partir de choux fleur, brocolis, lait, gruyere : trop de suppositions, on n'invente pas).
    - **ce que Sacha a supprimé reste supprimé.** Il avait enlevé la ligne des manques : on ne la remet pas au passage suivant. Une suppression est une décision, pas un oubli.
- **Laisser tel quel** — un choix à part entière. Une note déjà lisible ne se touche pas.

## Tags et catégories

- **Réutiliser d'abord l'existant** : `#trading`, `#top3`, `#appart`, `#a_regarder`. Un terme proche déjà présent vaut mieux qu'un tag neuf.
- Un **nouveau tag** seulement s'il sert **au moins deux notes** ou s'il nomme une vraie catégorie durable. Sinon, pas de tag.
- **Jamais renommer ni supprimer ses tags** sans demander : ils viennent de l'app, ils servent à filtrer là-bas aussi.
- Maximum **3 tags par note**. Pas de hiérarchie `#a/b/c` inventée.
- Les tags vivent dans le `tags:` du frontmatter. Si la note finit par une ligne `#tag` (son format), la garder cohérente avec le frontmatter — sans en semer ailleurs dans le corps.
- Une catégorie nouvelle est **signalée dans le récap** et ajoutée à `notes/_NOTES.md`, jamais laissée en doublon implicite.

## Structure d'une note propre

- **Frontmatter** : garder `tr4de-id`, `created`, `updated`, `pinned` **tels quels**. Ne jamais inventer un champ ni une date.
- **Première ligne = le titre tel qu'il l'écrit** (minuscules). Ne pas le transformer en `# Titre`.
- **Sections avec ses mots**, en ligne nue ou suivie de `:` (`peau :`, `entry trigger :`), jamais en `##` — cf. la règle du markdown brut ci-dessous.
- **Listes markdown** `- `, sous-niveaux à 2 espaces. Les indentations et alignements faits à l'espace disparaissent.
- **Tâches** → `- [ ]`. **Ne jamais cocher à sa place**, même si on sait que c'est fait : le signaler dans le récap et lui laisser cocher.
- **Pas de tableau markdown dans `notes/`.** L'app affiche le markdown comme du texte : un tableau y est illisible, Sacha ne le voit pas. Un tableau se remplace par **une ligne par élément**, champs séparés par son `=` ou par `:` — c'est sa notation (`gurren lagann = 8/10`, `cisd = cloture d'une bougie …`). Une valeur qu'il n'a pas écrite laisse le `=` **vide**, comme il le fait lui-même (`hunter x hunter =`).
- **Chiffres, plans, comptes** : une ligne par ligne d'origine, espaces multiples réduits, **valeurs recopiées à l'identique**. Jamais de recalcul.
- Ce qui vaut pour les tableaux vaut pour le reste : **écrire pour du markdown brut**. Listes `- ` et sections `mot :` passent bien. **Pas de `##` non plus** dans `notes/` : l'app affiche « ## dimanche 16 aout », la ligne nue se lit mieux — et c'est ce que Sacha écrit lui-même.
- Les tableaux restent permis dans les notes **du vault** lues dans Obsidian (`_NOTES.md`), jamais dans `notes/`.
- **Liens externes** : garder l'URL. Un mot devant si lui en a mis un, rien de plus.
- **Bloc `<!-- tr4de:attachments -->` … `<!-- /tr4de:attachments -->`** : intact, inchangé, toujours en fin de note.

## Contraintes techniques (app tr4de + sync Supabase)

- `notes/` **appartient à l'app** : garder le nom en minuscules, ne jamais sortir une note du dossier.
- **`notes/` reste PLAT — l'app ne gère pas les sous-dossiers.** Essayé le 18 août 2026 à la demande de Sacha (`notes/trading`, `notes/glow`, `notes/appart`) : quatre minutes plus tard la synchro a **re-téléchargé chaque note à la racine**, laissant les copies en sous-dossier orphelines — **deux fichiers avec le même `tr4de-id`**, ce que `verifie.py` refuse (l'app en perdrait une). Réparé en réinjectant le contenu dans la note de la racine et en supprimant les dossiers.
  - donc : **classement par tags**, et l'index `_NOTES.md` du vault joue le rôle de la vue par dossiers dans Obsidian.
  - avant de retenter des dossiers, il faut que **l'app sache les stocker** (son code est hors du vault, `~/Documents/GitHub/tr4de`). Sans ça, tout dossier créé ici est défait à la synchro suivante.
  - corollaire général : **ne pas se battre contre l'app**. Quand une mise en forme ou un rangement ne survit pas à la synchro, le dire et proposer de changer l'app, pas le refaire chaque semaine.
- La synchro est **immédiate** (`syncOnSave`) et **bidirectionnelle** : toute écriture part dans l'app, une suppression s'y propage (soft delete 30 jours). Donc **suppression, fusion et renommage = validation obligatoire**.
- **L'app gagne les conflits.** Vécu le 18 août 2026 : un passage complet (11 notes nettoyées, 2 consolidations, 1 renommage) a été **entièrement écrasé** quelques heures plus tard par la version de l'app — les notes remises en indentation à l'espace, et les **notes neuves supprimées** parce qu'elles n'existaient pas côté app. Le plugin garde des copies dans `notes/conflicts/` (`… (obsidian …).md` = la version locale perdue). Conséquences concrètes :
  - **relire l'état du dossier avant d'écrire**, même si on l'a lu plus tôt dans la session : comparer les `updated` et la taille des fichiers, une note peut avoir été réécrite ou renommée dans l'app entre-temps (`appartement` est devenue `achat`, `recette et ingrediens` est devenue `recette et courses`).
  - **ne jamais réappliquer un plan en aveugle** depuis des brouillons de session : le contenu de référence est celui du disque à l'instant présent.
  - **une note créée localement remonte bien** : le plugin lui attribue un `tr4de-id` quelques instants après l'écriture (constaté sur `bien communiquer`, `meta learning`, `bien s'habiller`). Donc un `tr4de-id` sur une note qu'on vient de créer n'est pas une faute — mais **deux notes qui partagent un id** en est une, et `verifie.py` la refuse.
  - en revanche une note locale **peut disparaître dans un conflit** : si la synchro descendante gagne avant que la montante ait eu lieu, elle est supprimée. Le signaler à Sacha plutôt que de la recréer en boucle.
  - après un écrasement, **ne pas refaire le travail en silence** : dire ce qui a été perdu, où sont les copies, et demander avant de rejouer.
- `tr4de-id` est l'**identité** de la note : jamais modifié, jamais recopié dans une autre note. Une note issue d'une scission **n'a pas** de `tr4de-id` — l'app lui en donnera un, on n'en invente pas.
- Les `[[liens]]` s'affichent en **texte brut** dans l'app. Demander **une fois** avant d'en mettre partout.
- Le vault entier est un dépôt git : montrer `git diff --stat` dans le récap plutôt que de décrire les changements de mémoire.

## Quand demander (une seule question groupée)

- Toute **fusion, scission, suppression, renommage**.
- Le **plan de consolidation** : quels sujets deviennent des notes, ce qui part d'où. Présenter la table sujets x notes, pas seulement la liste des opérations.
- **Chiffre ou total incohérent** (exemple vécu : `50k + 60k + 15k` annoncé `= 135K`). On signale, on ne corrige pas.
- Note **trop cryptique** (deux mots sans contexte) : ce qu'elle veut dire, plutôt que deviner.
- Un **nouveau tag** qui devient une catégorie durable.
- Sujet qui n'entre dans aucune catégorie : proposer, ne pas trancher seul.

## Garde-fous

- Jamais `rm` : snapshot d'abord, suppression seulement après validation explicite.
- Une note à la fois, séquentiel.
- `verifie.py` passe avant de récapituler. Invariant cassé → restaurer depuis le snapshot et le dire.
- **Une note qui grossit n'est pas forcément une faute** : quand du contenu arrive d'une autre note, c'est normal. Ce qui ne doit pas grossir, c'est le **total du dossier** — déplacer du contenu ne l'augmente pas. `verifie.py` fait exactement cette distinction (alerte par note, erreur sur le total).
- **Ne rien combler.** Un manque reste un manque : `hunter x hunter =` sans note reste sans note.
- Ne pas toucher aux notes du reste du vault (fiches, index, templates) : ce skill ne traite que les notes brutes.

## Étape finale — publier

Une fois les notes remises au propre, dérouler **`.claude/skills/_lib/publier.md`** :
réindexer le site puis **commiter et pousser le vault et le site** (le push du site
déclenche le déploiement Vercel). Non bloquant — un échec se signale dans le récap.
