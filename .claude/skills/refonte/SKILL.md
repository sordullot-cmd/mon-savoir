---
name: refonte
description: Transforme un dossier de référence du vault (la SOURCE de direction artistique — dossier /inspi ou /univers) plus une CIBLE (URL de site, app, dossier de code local, ou simple description) en PROMPT DE REFONTE précis, traçable et exécutable, destiné à un agent de code (Claude Code, Cursor). Lit vraiment la source (planches, nuanciers, écrans, animations), relève l'état actuel de la cible, calcule l'écart, traduit la DA en système (couleurs sémantiques, échelle typo, spacing, rayons, élévation, iconographie, densité, motion, ton de voix), vérifie les contrastes, et écrit le prompt dans `<dossier-source>/prompts/<cible>.md`. Aucune valeur inventée : chaque hex, police, durée est sourcée. À utiliser quand Sacha dit « fais-moi le prompt pour refondre X dans la DA de Y », « transforme ce site dans le style de telle app », « donne-moi le brief de refonte », « prompt de refonte ».
---

# /refonte — Le prompt qui transforme une cible dans une DA du vault

Prend **deux entrées** — une **source** de direction artistique (un dossier de référence
du vault) et une **cible** (le site ou l'app à transformer) — et produit **un fichier
prompt** prêt à coller dans un agent de code : direction artistique, design de l'app, UI,
branding, motion, écran par écran, avec les valeurs en dur et des critères de recette
vérifiables.

Le livrable n'est **pas** la refonte. C'est **le prompt** qui la fait faire. La refonte
elle-même se joue hors du vault, dans le dossier de code (cf. `CLAUDE.md`, § code vs notes).

## Règle fondatrice — aucune valeur inventée

Un prompt de refonte, c'est un tas de valeurs précises (`#0064FF`, `240 ms`, `radius 16`).
La tentation est d'en inventer pour que le tableau soit plein. **Interdit.** Chaque valeur
du prompt vient de l'une de ces trois provenances, et **le prompt la nomme** :

| Provenance | Comment on l'obtient |
| --- | --- |
| **charte publiée** | la fiche de la source, son press kit, ses tokens documentés |
| **relevé** | mesuré sur les médias du dossier (`palette.py releve`, lecture d'écran, comptage de frames) |
| **déduit** | dérivé d'une valeur sourcée par une règle écrite dans le prompt (« échelle 1.25 à partir du corps 16 ») |

Rien d'autre. Une valeur qu'on ne sait pas → on écrit ce qu'on sait et on marque le trou
comme **décision laissée à l'agent**, avec la contrainte qui l'encadre. Un trou signalé
coûte une question ; un hex inventé coûte une refonte à refaire.

## Router — les deux entrées

**Source de DA** (la référence) :

| Ce que donne Sacha | Ce qu'on fait |
| --- | --- |
| un slug / nom présent dans `INSPIRATION/` | on l'utilise — c'est le cas normal |
| un nom absent du vault | proposer **`/inspi`** (produit numérique) ou **`/univers`** (jeu, film, studio, marque) d'abord, puis revenir ici |
| une URL | **`/inspi`** d'abord. On n'écrit pas un prompt de DA à partir d'un onglet regardé une fois |
| plusieurs sources (« le calme de Headspace avec la densité de Toss ») | assumé : le prompt dit **quoi vient d'où**, axe par axe, et tranche les conflits explicitement |

**Cible** (ce qu'on transforme) :

| Ce que donne Sacha | Ce qu'on relève |
| --- | --- |
| URL de site | captures pleine hauteur de l'état actuel (`../inspi/capture-site.py`) |
| nom d'app / lien de store | écrans de store actuels (`../inspi/grab-app.py`) |
| dossier de code local (`~/Documents/…`) | inventaire **en lecture seule** : stack, où vivent les tokens, conventions |
| une description seule (« mon portfolio à venir ») | pas d'état actuel : le prompt devient un brief de création, et le récap le dit |

Cible absente → **demander**. Un prompt sans cible n'est pas un prompt de refonte, c'est
un résumé de la fiche source, et il existe déjà.

## Autonomie

Je décide seul : la discipline et le slug de la cible, l'ordre des axes, le périmètre
quand la cible est énorme, quels visuels d'appui joindre, quelle valeur est un trou
assumé. **Chaque décision de ce genre est écrite dans le récap.** Je m'arrête pour
demander seulement si la **cible** est ambiguë ou si la **source n'existe pas** dans le
vault.

---

## Étape 0 — préflight et résolution des entrées

```
mempalace_search "<nom de la source>"          # le dossier existe-t-il, et que contient-il
ls INSPIRATION/*/<slug> 2>/dev/null
for t in mempalace; do command -v $t >/dev/null || echo "ABSENT: $t"; done
```

- Source absente → **s'arrêter et proposer `/inspi` ou `/univers`** (§ Router).
- Source présente mais maigre (pas de `couleurs/`, deux écrans) → le dire tout de suite :
  le prompt sera borgne sur ces axes. Proposer de compléter le dossier avant.
- Cible = dossier de code → vérifier qu'il est **hors du vault**. Un dossier de code dans
  le vault est une anomalie à signaler, pas à exploiter.

## Étape 1 — lire la source pour de vrai

**On ne rédige pas un prompt de DA à partir du frontmatter.** Le frontmatter dit
`mood: [minimal, bold]` ; un agent de code ne peut rien faire de ça. Il faut les valeurs
et les règles, donc il faut **regarder**.

1. **La fiche en entier** — `<slug>.md`. C'est là que vivent les observations déjà faites
   (« le bleu du design system n'est pas le bleu de marque »). Un prompt qui rate ces
   observations refait le travail d'analyse pour rien.
2. **Les planches de chaque aspect** — les lire (`Read`), pas les lister. Un aspect sans
   planche : faire la planche de contact pour le voir d'un coup.
   ```
   python3 .claude/skills/_lib/planche.py "<scratchpad>/vu-<aspect>.png" \
       "INSPIRATION/<DISCIPLINE>/<slug>/<aspect>/*" --cols 6 --tile 200
   ```
3. **Les nuanciers** — `couleurs/palette-*.svg` : les hex y sont écrits en clair, avec
   leurs noms et leurs notes d'usage. `grep -o '#[0-9A-Fa-f]\{6\}'` pour les extraire,
   puis la fiche pour savoir **lequel sert à quoi**. Si la source n'a pas de nuancier,
   relevé : `python3 .claude/skills/_lib/palette.py releve "<slug>/ecrans/*.png"`.
4. **Les écrans** — 3 à 6 écrans clés lus vraiment, pour en tirer ce qu'aucune palette ne
   dit : densité, hiérarchie, rôle du blanc, largeur des gouttières, taille des touches.
5. **Les animations** — durée et courbe se relèvent sur les GIF/MP4 (`ffprobe`, ou
   compter les frames) : c'est ce qui permet d'écrire `220 ms` au lieu de « fluide ».
6. **Les composants** — `composants/` donne les blocs déjà isolés : ce sont les premiers
   candidats de la section « Composants » du prompt.
7. **Les typos** — le champ `typos` de la fiche et `branding/`. Police propriétaire →
   § Garde-fous (licence + substitut).

## Étape 2 — relever l'état actuel de la cible

Sans état actuel, le prompt ne peut pas dire **ce qui change** : il redécrit un idéal et
laisse l'agent deviner le point de départ.

- **Site** :
  ```
  python3 .claude/skills/inspi/capture-site.py "<url>" "<scratchpad>/cible" \
      --viewports desktop,mobile --dark
  ```
  Les captures **restent dans le scratchpad** — l'état avant d'une cible n'est pas une
  inspiration, il n'entre pas dans `INSPIRATION/`. Sauf demande de Sacha : alors
  `prompts/avant/`.
- **App** : `python3 .claude/skills/inspi/grab-app.py "<nom>" "<scratchpad>/cible"`.
- **Dossier de code — lecture seule, jamais d'édition ici** : repérer la stack et
  surtout **où la DA est branchée**, parce que le prompt devra le dire :
  ```
  ls <dossier>; cat <dossier>/package.json 2>/dev/null | head -40
  ls <dossier>/tailwind.config.* <dossier>/**/tokens.* 2>/dev/null
  grep -rl -- "--color\|:root\|theme(" <dossier>/src --include=*.css | head
  ```
  Noter : framework, système de style (Tailwind / CSS modules / styled-components),
  fichier des tokens, bibliothèque de composants, gestion du thème sombre, contraintes
  (SSR, i18n, navigateurs).

## Étape 3 — l'écart, axe par axe

Un tableau, dix lignes maximum, **écrit à partir de ce qu'on a vu aux étapes 1 et 2** :

| Axe | Aujourd'hui (cible) | Visé (source) | Ce qui change vraiment |
| --- | --- | --- | --- |
| couleurs, typo, spacing, rayons, élévation, iconographie, densité, motion, ton, thème sombre | … | … | … |

Ce tableau est la colonne vertébrale du prompt : les axes où **rien ne change** doivent y
figurer aussi, avec « inchangé ». Un axe non mentionné est un axe qu'un agent va refaire à
sa sauce.

## Étape 4 — traduire la DA en système

Le travail propre du skill : passer d'une observation (« ça respire ») à une règle
exécutable (« gouttière de 24 px entre cartes, 64 px entre sections, jamais deux
séparateurs consécutifs »). Les dix axes, et pour chacun ce qu'un agent de code attend :

| Axe | Ce que le prompt doit donner |
| --- | --- |
| **Couleurs** | des **rôles** (`surface`, `surface-elevee`, `texte`, `texte-faible`, `accent`, `accent-presse`, `succes`, `alerte`, `bordure`), chacun avec son hex clair **et** sombre. Une palette sans rôles ne se code pas |
| **Typographie** | familles (+ fallback + licence), échelle complète avec taille / graisse / interligne / interlettrage par niveau, et **quel niveau sert où** |
| **Espacement** | l'unité de base et l'échelle, plus les 3 ou 4 distances qui font l'allure (padding de carte, gouttière, rythme de section) |
| **Rayons et bordures** | rayon par famille de composant, épaisseur et couleur de bordure, quand il n'y a pas de bordure |
| **Élévation** | ombres exactes ou remplacement par un aplat / une bordure — la source tranche souvent (Toss : pas d'ombre, du contraste de surface) |
| **Iconographie et illustration** | style de trait, grille, taille, remplissage ; ce qui remplace les illustrations si la source en a et que la cible n'en a pas |
| **Densité et layout** | largeur max de contenu, colonnes, comportement mobile, densité des listes, position de la navigation |
| **Motion** | durées et courbes chiffrées par type (entrée, sortie, feuille modale, changement d'état), ce qui **ne** s'anime pas, et `prefers-reduced-motion` |
| **Branding et ton** | logo et son placement (celui de la cible, cf. garde-fous), majuscules ou pas, longueur des libellés, ton des messages d'erreur et des états vides |
| **États** | pour chaque composant : repos, survol, focus visible, pressé, désactivé, chargement, vide, erreur. C'est la moitié du travail réel et c'est toujours ce qui manque |

Un axe que la source ne documente pas → **le dire dans le prompt** comme décision laissée
à l'agent, avec sa contrainte (« pas d'ombre documentée : garder les ombres actuelles »).

## Étape 5 — vérifier avant d'écrire

1. **Contrastes** — chaque couple texte/fond du prompt, en clair **et** en sombre :
   ```
   python3 .claude/skills/refonte/contraste.py --echecs "texte=#191F28" "fond=#FFFFFF" "accent=#0064FF"
   ```
   Un couple qui échoue ne part **pas** dans le prompt tel quel : soit on prend une autre
   valeur de la source, soit le prompt écrit noir sur blanc que ce couple est réservé aux
   grands corps ou aux aplats.
2. **Polices** — la police de la source est-elle disponible pour la cible ? Propriétaire
   ou maison → substitut nommé, et le prompt le dit franchement.
3. **Faisabilité** — un effet WebGL relevé sur la source n'a rien à faire dans le prompt
   d'un site vitrine statique. Ce qui n'est pas transposable se dit en une ligne plutôt que
   de partir en tâche impossible.

## Étape 6 — écrire le prompt

Squelette imposé, section par section, avec les règles de rédaction et un exemple de
chaque : **`references/squelette.md`**. À lire à ce moment-là, pas avant.

Quatre règles qui décident de la qualité du fichier :

- **Auto-suffisant.** L'agent qui reçoit le prompt n'a **pas** le vault, ni la fiche, ni
  MemPalace. Toutes les valeurs sont en dur dans le texte. Un `[[lien wiki]]` seul ne
  transmet rien : les visuels d'appui sont cités par **chemin absolu** (5 à 8 max, les
  plus parlants), et le prompt prévient qu'il faut les joindre si l'agent tourne ailleurs.
- **Pas un adjectif seul.** « Moderne », « épuré », « premium » ne produisent rien. Chaque
  intention arrive traduite en valeur, en règle ou en interdit.
- **Vérifiable.** Le prompt finit par une recette que Sacha peut dérouler à l'œil ou en
  commande. Une exigence non vérifiable est une exigence qui ne sera pas tenue.
- **Périmètre explicite.** Ce qu'on change, et surtout **ce qu'on ne touche pas** :
  contenu, routes, logique métier, données, dépendances. Sans cette section, un agent de
  code réécrit l'application.

## Étape 7 — la relecture à froid

Un sous-agent joue **l'agent destinataire** : il reçoit le prompt **seul**, sans le vault
et sans cette conversation, et rend trois choses — ce qu'il ferait en premier, les valeurs
qui lui manquent pour commencer, les phrases qu'il peut interpréter de deux façons. Tout
ce qu'il remonte se corrige dans le prompt avant livraison. C'est la passe qui distingue
un prompt d'un résumé de fiche.

## Clôture

1. **Ranger** : `INSPIRATION/<DISCIPLINE>/<slug-source>/prompts/<slug-cible>.md`.
   Le prompt reste collé à la référence dont il est tiré. Deuxième version pour la même
   cible → suffixe daté (`<slug-cible>-2026-08-21.md`), on n'écrase pas.
2. **Lier depuis la fiche source** : une section `## Prompts de refonte` avec une ligne par
   prompt — cible, date, ce qu'il couvre, `[[lien]]`. Sans ce lien, le prompt est perdu.
3. **Réindexer MemPalace** : `mempalace mine "$HOME/Documents/brain^2" --agent sacha`
   (absent → sauter, le dire).
4. **Publier** — dérouler `.claude/skills/_lib/publier.md`. Non bloquant.
5. **Récap** : source et cible retenues · aspects de la source réellement exploités et
   ceux qui manquaient · état actuel relevé (ou non, et pourquoi) · axes traités / axes
   laissés à l'agent · couples de couleurs recalés au contraste · substitution de police ·
   ce que la relecture à froid a fait corriger · décisions prises seul.

---

## Structure produite

```
INSPIRATION/<DISCIPLINE>/<slug-source>/
├── <slug-source>.md          ← + section « ## Prompts de refonte »
└── prompts/
    ├── <slug-cible>.md       ← le prompt (le livrable)
    └── avant/                ← captures de l'état actuel, seulement si Sacha les veut
```

## Garde-fous

- **Transposer, pas plagier.** Le prompt transmet des **principes et des valeurs de
  système** (rôles de couleur, échelle, motion, densité). Il ne demande **jamais** de
  copier le logo, le nom, la mascotte, les illustrations, les assets ou les fontes
  propriétaires de la source. Une DA se transpose ; une identité appartient à quelqu'un.
- **La marque de la cible reste celle de la cible.** Logo, nom, ton propre : la refonte
  habille la cible, elle ne la déguise pas en la source.
- **Fontes** : toujours nommer la licence. Propriétaire, maison, ou non redistribuable →
  substitut explicite (et proposer `/font` pour instruire le substitut).
- **Aucune valeur inventée** (§ Règle fondatrice) — chaque valeur porte sa provenance.
- **Accessibilité non négociable** : contrastes vérifiés (étape 5), focus visible,
  cibles tactiles ≥ 44 px, `prefers-reduced-motion`. Une DA n'excuse pas un écran illisible.
- **Ne pas toucher au code.** Ce skill lit le dossier de code, il ne le modifie pas. La
  refonte est un autre run, dans le dossier de code, hors du vault.
- **Ne pas écraser un prompt existant** → compléter, ou suffixe daté.
- **Signaler les trous** : un dossier source sans `couleurs/`, une cible non capturable
  (login, paywall), un axe non documenté. Un prompt honnêtement borgne vaut mieux qu'un
  prompt qui invente.
- **Pas d'emojis** dans le prompt produit (règle du vault), y compris dans les checklists.

## Outils

| Script | Rôle |
| --- | --- |
| `contraste.py` | ratios WCAG de tous les couples de couleurs, verdicts AA/AAA (livré ici, sans dépendance) |
| `../_lib/palette.py` | relevé de couleurs quand la source n'a pas de nuancier |
| `../_lib/planche.py` | regarder la source d'un coup avant d'écrire |
| `../inspi/capture-site.py` | état actuel d'une cible web |
| `../inspi/grab-app.py` | état actuel d'une cible app |

## Références (à lire au besoin, pas d'avance)

| Fichier | Quand |
| --- | --- |
| `references/squelette.md` | étape 6 — le squelette du prompt, section par section |
| `../_lib/publier.md` | la clôture : réindexer le site, pousser les deux dépôts |
