---
type: prompt-refonte
source: brilliant
cible: tr4de (tao trade)
cible_url: file:///Users/account/Documents/GitHub/tr4de
destination: agent-de-code
axes: [couleurs, typo, spacing, rayons, elevation, iconographie, densite, ton, theme-sombre, composants, etats]
axes_ouverts: [motion, illustration, rayon-de-champ]
date: 2026-08-25
tags: [prompt, refonte, da, ui-design, trading]
---

Prompt de refonte de **tr4de** (Next.js 15 + Tauri + Supabase, `~/Documents/GitHub/tr4de`)
dans la direction artistique de **[[brilliant]]**. Toutes les valeurs viennent du dossier
source — tokens Panda CSS relevés dans le CSS de production de brilliant.org, nuanciers
`couleurs/`, relevés de pixels sur les écrans — ou sont dérivées d'une règle écrite ici.
État de la cible au 25 août 2026 : charte **Duolingo** (Owl `#58CC02`, Cardinal `#FF4B4B`,
Fox, Macaw, Beetle), accent vert réglable `#64D741`, police Outfit, 894 hex câblés en dur
dans `app/` + `components/`. L'ironie est le sujet : la fiche source décrit Brilliant comme
**« l'anti-Duolingo sur la couleur »**.

## Le prompt — tout ce qui suit est à copier

---

# Refonte de tr4de dans la direction artistique de Brilliant

## 1. Mission

Tu refonds l'interface de **tr4de** (`~/Documents/GitHub/tr4de` — Next.js 15 App Router,
React 19, Tauri, Supabase, styles **inline** pilotés par des variables CSS) pour l'aligner
sur une direction artistique décrite intégralement ci-dessous. Cette direction est relevée
sur un produit tiers (Brilliant) : elle sert de **référence de système** — rôles de
couleur, échelle, densité, règles de feedback — et **jamais** de modèle à cloner.

Tu ne changes ni le contenu, ni les routes, ni la logique métier, ni le schéma de données.
Tu rends un diff qui passe `npm run lint:strict` et `npm test`, et qui satisfait la recette
de la section 12.

## 2. Périmètre

**Tu changes**
- `app/globals.css` — tous les tokens de couleur, rayon, élévation, clair et sombre.
- `lib/ui/tokens.ts`, `lib/ui/palette.ts`, `lib/ui/accent.ts` — les valeurs sources.
- Les **894 hex câblés en dur** dans `app/` et `components/`, ramenés aux tokens.
- Les primitives de `components/ui/` : `Button`, `Card`, `Sheet`, `EmptyState`,
  `LoadingScreen`, `Skeleton`, `TabBar`, `Sidebar`, `Stat`, `XpBar`, `form.jsx`, `da.jsx`.
- La microcopie des états vides, des erreurs et des retours de discipline (section 8).

**Tu ne touches pas**
- Les textes de contenu, les libellés de champ métier, les noms de pages.
- Les routes, les URLs, les noms de fichiers, la structure des dossiers.
- La logique métier : calculs de P&L, de patrimoine, de SRS, d'agenda, parseurs CSV,
  intégrations broker, Supabase, l'IA.
- `package.json` — **aucune dépendance ajoutée ni retirée**.
- `lib/design/tokens.ts` — fichier legacy (palette OpenAI), importé par un seul module.
  Tu le laisses tel quel : le toucher élargit le diff sans rien changer à l'écran.
- L'architecture de `lib/ui/palette.ts` : `deepen()`, `dotRing()`, `CHIP`, `PALETTE_DARK`,
  `PALETTE_LIGHT`. **Tu remplaces les teintes sources, pas la machinerie** — elle est
  correcte et elle résout déjà des problèmes que la nouvelle palette va reposer à
  l'identique.

## 3. État actuel

**Stack et style.** Next.js 15 App Router, React 19, TypeScript partiel (`.tsx` et `.jsx`
mêlés), Tauri pour le desktop, Supabase pour les données. **Pas de Tailwind utilisé pour la
DA** : le site est en `style={{ }}` inline (123 fichiers), les valeurs venant de variables
CSS via `lib/ui/tokens.ts` (85 fichiers l'importent).

**Où vivent les tokens.**
- `app/globals.css` — 2 299 lignes. `:root` pour le clair, `:root[data-theme="dark"]` pour
  le sombre. Contient aussi une longue série de rustines par sélecteur d'attribut
  (`[style*="background:#FFFFFF"]`) qui rattrapent les blancs inline en thème sombre.
- `lib/ui/tokens.ts` — l'objet `T`, chaque entrée étant `var(--token, repli)`.
- `lib/ui/type.ts` — l'échelle typo en pixels (`TS`), dix crans, avec son test de garde
  `tests/typeScale.test.ts`.
- `lib/ui/palette.ts` — les 38 teintes de la charte actuelle sous leurs noms d'animaux
  (`HUE`), puis `PALETTE` / `PALETTE_DARK` / `PALETTE_LIGHT` / `GREY` / `CHIP`.
- `lib/ui/accent.ts` — l'accent de marque réglable par l'utilisateur (Réglages →
  Apparence), deux teintes `--accent` / `--accent-2`, cinq préréglages, persistance
  `localStorage`.
- `lib/ui/buttons.ts` — `BTN`, la seule table de hauteurs de boutons.

**Ce qui est déjà bon et doit survivre intact.**
- La **discipline des tokens** : une échelle typo unique testée, une seule table de
  hauteurs de bouton, des aplats exprimés en transparence d'encre (`HAIRLINE`, `FIELD_BG`,
  `WRITING_BG`) qui suivent le thème tout seuls.
- `deepen()` et `dotRing()` : la teinte descendue vers le noir jusqu'à un ratio cible. La
  nouvelle palette en a **plus** besoin que l'ancienne, pas moins.
- `CHIP` : fonds ramenés à une luminance constante (0,75) pour que seule la teinte
  distingue deux pastilles.
- `:focus-visible` déjà câblé (clavier uniquement), et un bloc
  `@media (prefers-reduced-motion: reduce)` déjà présent.
- Les tokens de motion `--ease-*` / `--dur-*` et l'utilitaire `--tr-ui`.

**L'ampleur du câblage en dur, mesurée.** `grep` sur `app/` + `components/` :

- `#58CC02` (Owl) : 51 occurrences, 19 fichiers
- `#FF4B4B` (Cardinal) : 38 occurrences, 17 fichiers
- `#FF9600` (Fox) : 24 occurrences, 12 fichiers
- `#1CB0F6` (Macaw) : 24 occurrences, 15 fichiers
- `#CE82FF` (Beetle) : 18 occurrences, 10 fichiers
- `#7AF0F2` (Moon Jelly) : 5 · `#64D741` : 5 · `#4CC72C` : 3
- **894 hex au total**, dont `#FFFFFF` 127×, `#0D0D0D` 67×, `#E5E5E5` 53×, `#F0F0F0` 45×.

Une refonte qui ne touche que `globals.css` laissera donc **168 verts et rouges Duolingo**
à l'écran. Le balayage des hex en dur n'est pas une finition, c'est le lot le plus lourd.

**Les rayons câblés en dur** (`borderRadius: <n>` littéral) : `999` 335×, `6` 101×, `12`
78×, `10` 76×, `8` 64×, `14` 12×, plus 2, 3, 4, 5, 16, 48. L'échelle déclarée est
6 / 10 / 14 / 999 : **142 occurrences sont déjà hors échelle** avant même ta refonte.

## 4. La direction artistique

**Direction** : un outil financier dense qui se lit comme une page blanche. La couleur ne
décore rien et ne signe rien — elle ne se pose que sur ce qui porte une information, et le
reste de l'écran est blanc.

1. **Le blanc est la matière, pas le fond.** Sur les écrans de la référence, le blanc
   occupe **61,09 % de la surface** et la couleur de marque **0,16 %** (comptage de pixels,
   dossier source). → Aucune surface d'accent au-delà de ce qui est cliquable ou chiffré.
   Une carte n'a pas de fond teinté. Un en-tête n'a pas de bandeau coloré. Un état actif se
   dit par un voile à 10 %, jamais par un aplat plein.

2. **La couleur code la catégorie, pas la marque.** Dans la référence, les maths sont en
   bleu et l'informatique en violet : la palette sert la taxonomie du contenu. → Dans
   tr4de, la teinte d'un poste de dépense, d'une classe d'actif ou d'une section de vie
   vient de `PALETTE`, et **l'accent de marque ne s'y mêle jamais**. Un graphique ne
   contient aucune occurrence de `--accent`.

3. **Se tromper n'est pas rouge.** La référence déclare deux tokens de feedback qui ne sont
   ni verts vifs ni rouges : `lesson-feedback-correct` `#00370F` (un vert quasi noir) et
   `lesson-feedback-retryable` `#403000` (un brun). Le rouge existe dans sa charte et
   **n'est pas mobilisé pour une mauvaise réponse**. → Dans tr4de, un trade perdant reste
   rouge : c'est une grandeur signée, pas une faute. Mais une règle de discipline non
   tenue, une série rompue, un objectif manqué, une révision ratée passent au **brun
   `#403000`**, jamais au rouge. Le rouge est réservé à ce qui est réellement cassé : une
   synchronisation en échec, un import invalide, une API qui ne répond pas.

4. **La hiérarchie vient de la surface et du trait, pas de l'ombre.** La référence pose une
   ombre à 4 % d'opacité et rien d'autre ; ses conteneurs de figure sont des aplats gris
   très clairs. → Une carte = fond blanc + trait 1 px + l'ombre `elevation-subtle`. Un
   bloc dans un bloc = un gris `surface-figure`, pas une deuxième ombre. Jamais deux
   séparateurs consécutifs.

5. **On dit ce qui se passe.** L'écran de chargement de la référence est un anneau et une
   phrase — « Finding learning path recommendations based on your responses » — et ses
   paliers d'effort sont nommés (Casual, Regular, Serious, Intense) au lieu d'être
   chiffrés. → Aucun spinner muet ni squelette anonyme sur une attente de plus de 400 ms :
   un anneau et une phrase qui nomme l'opération en cours. Les paliers de tr4de (objectifs,
   niveaux de discipline, paliers de scaling) portent un nom avant leur chiffre.

## 5. Le système

Chaque valeur porte sa provenance : **charte** = token déclaré dans le CSS de production de
la référence · **relevé** = mesuré sur ses médias · **déduit** = dérivé d'une valeur sourcée
par une règle écrite ici. Aucune valeur n'a d'autre origine.

### 5.1 Couleurs — par rôle, clair et sombre

| Rôle | Clair | Sombre | Provenance | Usage |
| --- | --- | --- | --- | --- |
| `surface` | `#FFFFFF` | `#141414` | charte (`bg-primary` / `gray-950`) | fond des cartes et des panneaux |
| `surface-page` | `#F5F3F1` | `#141414` | charte (`oat-50` / `gray-950`) | fond de page, derrière les cartes |
| `surface-elevee` | `#FFFFFF` | `#1E1E1E` | charte (`dark-gray`) | cartes en sombre, feuilles modales |
| `surface-figure` | `#F2F2F2` | `#1E1E1E` | charte (`gray-100`) | conteneur de graphique, de tableau, de bloc de code |
| `surface-encart` | `#F2F9FB` | `#16242A` | relevé (3,89 %) / déduit | encart d'explication, aide contextuelle |
| `bordure-encart` | `#AACFD7` | `#3C555C` | charte (`border-quip`) / déduit | trait de l'encart d'explication |
| `texte` | `#141414` | `#FFFFFF` | charte (`gray-950`) | corps, titres, chiffres |
| `texte-faible` | `#666666` | `#B3B3B3` | charte (`gray-700` / `gray-400`) | légendes, métadonnées, unités |
| `texte-placeholder` | `#999999` | `#999999` | charte (`gray-500`) | placeholder **uniquement**, jamais du texte |
| `bordure` | `#E5E5E5` | `#383838` | charte (`gray-200` / `gray-900`) | traits, contours de champ |
| `bordure-forte` | `#CCCCCC` | `#4C4C4C` | charte (`gray-300` / `gray-800`) | contour au survol, séparateur appuyé |
| `accent` | `#29CC57` | `#29CC57` | charte (`green-500`) | aplat d'action primaire, état actif |
| `accent-presse` | `#15B441` | `#15B441` | charte (`green-600`) | bouton enfoncé, arête basse |
| `accent-encre` | `#007C23` | `#5ED981` | charte (`green-800` / `green-400`) | **le vert quand il faut du texte** |
| `accent-voile` | `#EAFAEE` | `#1C3625` | charte (`green-100`) / déduit | fond d'un item de nav actif |
| `succes-fond` | `#D4F5DD` | `#1C3625` | charte (`green-200`) / déduit | fond d'un état réussi |
| `succes-encre` | `#00370F` | `#5ED981` | charte (`lesson-feedback-correct`) | texte d'un état réussi |
| `reessai-encre` | `#403000` | `#F7C325` | charte (`lesson-feedback-retryable`) | **règle non tenue, série rompue, objectif manqué** |
| `alerte` | `#F7C325` | `#F7C325` | charte (`status-warning` = `yellow-500`) | avertissement, surlignage, série |
| `erreur` | `#FF5D5D` | `#FF5D5D` | charte (`status-error` = `red-500`) | échec réel : synchro, import, API |
| `info` | `#456DFF` | `#456DFF` | charte (`status-promo` = `blue-500`) | information, promotion, lien |
| `ancre` | `#294BC6` | `#456DFF` | charte (`blue-700`) | lien textuel — `info` ne passe pas en corps sur blanc |
| `sur-aplat` | `#141414` | `#141414` | déduit (§ 5.1.2) | **encre posée sur un aplat de couleur pleine** |

**5.1.0 — Où chaque rôle atterrit dans le code.** Les noms de rôle ci-dessus sont ceux de
ce prompt ; le code a les siens. Voici la correspondance exacte, à respecter — les
variables marquées **nouvelle** sont à créer dans `:root` **et** dans
`:root[data-theme="dark"]`, et à exposer dans `T` (`lib/ui/tokens.ts`).

| Rôle | Variable CSS | Entrée de `T` | Note |
| --- | --- | --- | --- |
| `surface` | `--color-card-bg`, `--color-bg` | `T.white`, `T.surface`, `T.bg` | les deux prennent la même valeur |
| `surface-page` | `--color-bg-subtle` | — | fond de page ; en sombre, la sidebar aussi |
| `surface-elevee` | `--color-card-bg` (sombre) | `T.surface` | `#1E1E1E`, en sombre uniquement |
| `surface-figure` | `--color-surface-figure` | `T.surfaceFigure` | **nouvelle** |
| `surface-encart` | `--color-quip-bg` | `T.quipBg` | **nouvelle** |
| `bordure-encart` | `--color-quip-bd` | `T.quipBd` | **nouvelle** |
| `texte` | `--color-text` | `T.text` | |
| `texte-faible` (1er cran) | `--color-text-sub` | `T.textSub` | `#4C4C4C` clair (`gray-800`, 8,0:1) |
| `texte-faible` (2e cran) | `--color-text-muted` | `T.textMut` | `#666666` clair (`gray-700`, 5,74:1) |
| `texte-placeholder` | `--color-text-placeholder` | `T.textPlaceholder` | **nouvelle** — placeholder seul |
| `bordure` | `--color-border` | `T.border` | |
| `bordure-forte` | `--color-border-strong` | `T.border2` | |
| `accent` | `--accent`, `--accent-2` | `T.brand`, `T.kraken` | mécanique inchangée |
| `accent-encre` | `--accent-ink` | `T.brandInk` | **nouvelle entrée de `T`** ; la variable existe déjà |
| `accent-voile` | `--accent-soft` | `T.brandSoft` | |
| `succes-fond` | `--color-feedback-ok-bg` | `T.okBg` | **nouvelle** |
| `succes-encre` | `--color-feedback-ok-ink` | `T.okInk` | **nouvelle** |
| `reessai-encre` | `--color-feedback-retry-ink` | `T.retryInk` | **nouvelle** |
| `alerte` | `--color-amber`, `--color-warning` | `T.amber` | même valeur pour les deux |
| `erreur` | `--color-red`, `--color-danger` | `T.red` | même valeur pour les deux |
| `info` | `--color-blue`, `--color-info` | `T.blue` | **`--color-info` vaut aujourd'hui `#CE82FF`, un violet** — il passe au bleu |
| `ancre` | `--color-link` | `T.link` | **nouvelle** — liens textuels |
| `sur-aplat` | `--color-on-accent` | `T.onAccent` | **nouvelle**, `#141414` |

**Trois pièges de correspondance, à ne pas manquer.**

1. **`--color-on-solid` ne change pas et reste `#FFFFFF`.** Il sert aussi d'encre sur le
   voile sombre des modales (`T.scrim`, cf. `NotesPage`) et sur le bouton danger : le
   basculer en `#141414` rendrait ces glyphes invisibles. C'est `--color-on-accent`
   `#141414` qui porte la règle 5.1.2, et il ne s'emploie que sur `accent`, `alerte` et
   `succes-fond`. Là où l'encre dépend d'une teinte calculée, `components/ui/form.jsx` a
   déjà le bon réflexe (`luminance(color) > 0.45 ? T.text : T.onSolid`) : réutilise-le au
   lieu d'écrire un ternaire à la main.
2. **`--color-pnl-pos` et `--color-pnl-neg` changent de nature.** Ce sont aujourd'hui les
   teintes brutes de la charte ; ce sont désormais des **encres** (§ 5.1.6) :
   `#007C23` / `#BD4545` en clair, `#29CC57` / `#FF5D5D` en sombre. Même chose pour
   `--color-cal-pos-text`, `--color-cal-neg-text`, `--color-cal-pos-sub`,
   `--color-tag-long-text` (`#007C23`) et `--color-tag-short-text` (`#A65C17`). Les
   **aplats** correspondants (`--color-cal-*-bg`, `--color-cal-*-surface`,
   `--color-tag-*-bg`, `--color-*-bg`, `--color-*-bd`) gardent leur construction en
   `color-mix` et leurs pourcentages : seule la teinte source change.
3. **Les 210 rustines par sélecteur d'attribut de `globals.css`.** Le bloc
   `:root[data-theme="dark"] [style*="background:#FFFFFF"]` et ses voisins ciblent des hex
   **littéraux** posés en style inline. Chaque fois que tu changes un fond en dur dans un
   composant, tu rends caduque ou tu casses l'une de ces règles. Traite-les dans le lot 1 :
   mets à jour la valeur de sortie (`#1A1A1B` → `#1E1E1E`, `#0F0F10` → `#141414`), et ne
   supprime une règle que si le hex qu'elle cible n'existe plus nulle part — `grep` avant
   de supprimer.

**5.1.1 — Le fond de page change de température, et c'est délibéré.** tr4de avait choisi
`#F5F5F5` après une série documentée en écart de clarté L\* sous une carte blanche, en
rejetant `#F1F2F4` parce qu'il « tirait sur le bleu et refroidissait tout l'écran ».
`oat-50` `#F5F3F1` donne **ΔL\* = 4,06** contre 3,46 pour `#F5F5F5` : un cran plus marqué,
en dessous du `#F3F3F3` (4,16) jugé trop lourd — et il est **chaud**, pas froid. Le motif du
rejet précédent ne s'applique donc pas. Si à l'écran le fond pèse trop, le repli est
`#F5F5F5`, pas `#F1F2F4`.

**5.1.2 — L'encre sur un aplat est noire, pas blanche.** Relevé sur la référence : sur son
aplat lime `#D8E82E`, le texte est `#000000` ; ses boutons pleins portent une encre sombre.
Règle : encre `#141414` sur tout aplat dont le contraste avec `#141414` dépasse 4,5:1
(c'est le cas de `accent`, `alerte`, `succes-fond`, `pear`, `mint`) ; encre `#FFFFFF`
uniquement sur le bouton noir, sur `erreur` et sur le voile des modales. Cette règle
n'inverse **pas** `--color-on-solid` : voir le piège 1 de 5.1.0. Vérifiés : `#141414` sur `#29CC57` = **8,66:1**,
sur `#F7C325` = **11,22:1**, sur `#D4F5DD` = **15,71:1**.

**5.1.3 — Le vert ne peut pas être du texte.** `green-500 #29CC57` sur blanc = **2,13:1** :
il échoue même au seuil 3,0 des composants. **Interdits de couleur, à respecter à la
lettre :**

- `accent #29CC57` en texte, en icône ou en trait 1 px sur un fond clair — **jamais**.
  C'est un aplat, rien d'autre. Pour du vert lisible : `accent-encre #007C23` (5,37:1 sur
  blanc, 4,86:1 sur `oat-50`).
- `erreur #FF5D5D` en texte de corps sur un fond clair : **3,01:1**, échoue. Réservé aux
  grands corps, aux icônes et aux traits. Pour du rouge en corps clair, voir 5.1.4.
- `texte-placeholder #999999` en texte : **2,85:1** sur blanc. Placeholder seulement.
- `info #456DFF` en corps sur blanc : **4,30:1**, échoue de peu. Pour un lien textuel,
  `ancre #294BC6` (**7,20:1**). En sombre, `info` sur `#1E1E1E` = 3,88:1 : grands corps,
  icônes et traits seulement.
- `accent-encre #007C23` sur fond sombre : 3,43:1 — c'est pour cela que le sombre bascule
  sur `green-400 #5ED981` (**10,28:1** sur `#141414`).

**5.1.4 — La règle d'encre claire (déduite, et à appliquer telle quelle).** Toute teinte de
catégorie qui doit devenir du **texte, une puce, un trait ou un glyphe** sur un fond clair
est descendue vers le noir par pas de 1 % jusqu'à atteindre **4,5:1 sur `#F2F2F2`**, le plus
foncé des trois fonds clairs. C'est exactement ce que fait déjà `deepen()` dans
`lib/ui/color` : tu changes la cible de contraste et le fond de référence, pas la fonction.
Valeurs calculées pour les teintes de `PALETTE` :

- `red-500 #FF5D5D` → **`#BD4545`** (−26 %) — blanc 5,12 · oat 4,63 · figure 4,57
- `yellow-500 #F7C325` → **`#886B14`** (−45 %)
- `blue-500 #456DFF` → **`#3F63E8`** (−9 %)
- `purple-500 #9D62FF` → **`#8452D6`** (−16 %)
- `orange-500 #FF8D23` → **`#A65C17`** (−35 %)
- `teal-500 #2CB0A1` → **`#1F7B71`** (−30 %)
- `pink-500 #FF6BD5` → **`#AD4991`** (−32 %)
- `papaya-500 #FF775C` → **`#B0523F`** (−31 %)
- `mint-500 #5CF0B6` → **`#2F7A5D`** (−49 %)
- `pear-500 #D8E82E` → **`#6C7417`** (−50 %)
- Le vert fait exception : son encre est le token déclaré **`green-800 #007C23`**, pas une
  valeur calculée.

**5.1.5 — Les teintes de catégorie.** `lib/ui/palette.ts` remplace ses 38 teintes Duolingo
par les **14 teintes du cran 500 de la référence** (charte) :

`green-500 #29CC57` · `mint-500 #5CF0B6` · `pear-500 #D8E82E` · `teal-500 #2CB0A1` ·
`cyan-500 #82EDE6` · `blue-500 #456DFF` · `purple-500 #9D62FF` · `pink-500 #FF6BD5` ·
`yellow-500 #F7C325` · `orange-500 #FF8D23` · `papaya-500 #FF775C` · `red-500 #FF5D5D` ·
`gray-500 #999999` · `oat-50 #F5F3F1`

Tu gardes la structure existante : `PALETTE` = les huit servies en premier — prends
`blue`, `purple`, `orange`, `teal`, `pink`, `yellow`, `papaya`, `mint`. **`green` et `red`
n'entrent pas dans `PALETTE`** : ils sont pris par le P&L et par l'erreur, et une classe
d'actif qui hériterait du vert du gain se lirait comme un gain. Les gris : `GREY` prend
`gray-900 #383838`, `gray-700 #666666`, `gray-500 #999999`, `gray-300 #CCCCCC`,
`gray-100 #F2F2F2`, `#FFFFFF` (charte).

`PALETTE_DARK` et `PALETTE_LIGHT` : la référence ne publie que le cran 500 de ces teintes —
seule l'échelle du vert est complète dans le dossier source. **Tu ne devines pas les autres
crans.** `PALETTE_DARK` se calcule par la règle 5.1.4 (la teinte descendue vers le noir) ;
`PALETTE_LIGHT` par la règle symétrique (la teinte mélangée à `#FFFFFF` jusqu'à ce que
`#141414` posé dessus atteigne 7:1). Le commentaire du fichier doit dire que ce sont des
valeurs **calculées faute de crans publiés**, pas des valeurs de charte.

**5.1.6 — Le P&L.** C'est la couleur la plus fréquente de l'app et le seul endroit où le
rouge reste légitime.

- Gain, texte clair : `#007C23` (`green-800`, charte) — 5,37:1 sur blanc, 4,86 sur oat.
- Gain, texte sombre : `#29CC57` (`green-500`, charte) — 8,66:1 sur `#141414`.
- Perte, texte clair : `#BD4545` (déduit, règle 5.1.4) — 5,12:1 sur blanc.
- Perte, texte sombre : `#FF5D5D` (`red-500`, charte) — 6,12:1 sur `#141414`.
- Aplats du calendrier P&L : la teinte **brute** diluée, comme aujourd'hui
  (`color-mix` 7 % / 24 %), avec `#29CC57` et `#FF5D5D` en source. Les aplats gardent la
  teinte vive ; seule l'encre descend. C'est déjà la règle du fichier, tu changes les hex.
- `--color-num-muted` (les décimales grisées du chiffre héros) : `#CCCCCC` en clair
  (`gray-300`), `#4C4C4C` en sombre (`gray-800`) — charte.

**5.1.7 — L'accent réglable.** `lib/ui/accent.ts` garde son mécanisme entier. Ce qui change :

- `DEFAULT_ACCENT = "#29CC57"` (`green-500`, charte), `DEFAULT_ACCENT_2 = "#15B441"`
  (`green-600`, charte — c'est le cran dont la référence tire l'arête de son bouton).
- Les cinq préréglages sont réécrits sur les teintes de la référence :
  Vert `#29CC57` / `#15B441` · Bleu `#456DFF` / `#294BC6` · Violet `#9D62FF` / `#8452D6` ·
  Menthe `#5CF0B6` / `#48BB8E` · Charbon `#141414` / `#F7C325`.
  (`#48BB8E` = `mint-700`, charte ; `#8452D6` = règle 5.1.4.)
- **Correction obligatoire.** `--color-nav-active-text: var(--accent)` rend aujourd'hui
  **1,85:1** avec l'accent actuel et rendrait 2,13:1 avec `green-500` : l'item de nav actif
  est illisible dans les deux cas. L'encre active doit être `var(--accent-ink)`, et la
  dérivation passe de 55 % à **45 %** d'accent :
  `--accent-ink: color-mix(in srgb, var(--accent) 45%, #0B2A05)`.
  Vérifié sur les quatre préréglages colorés, sur le pire fond clair `#F2F2F2` et sur leur
  propre voile : vert 5,32 / 5,51 · violet 7,88 / 7,85 · bleu 8,27 / 8,15 · jaune 4,64 /
  4,94. À 55 % le vert tombait à 4,32 et le jaune à 3,66 — d'où le changement.
- `--accent-soft` avec `green-500` produit `#EAFAEE`, qui **est** le token `green-100` de la
  référence. Coïncidence utile : le voile de nav est déjà de la charte.

### 5.2 Typographie

**Familles.** `CoFo Brilliant`, `CoFo Robert` et `CoFo Brilliant Semi-Mono` sont **sur
mesure, propriétaires et non redistribuables** (Contrast Foundry). Elles ne sont ni
téléchargées, ni copiées, ni imitées.

- Sans (corps, titres, chiffres) : **`Outfit`** — SIL OFL, déjà chargée dans
  `app/layout.tsx` en axe variable. Substitut assumé. Critère : `CoFo Brilliant` mesuré
  dans le `.ttf` donne x-height 506/1000, cap 721/1000, **rapport x/cap = 0,702**, `n` à
  593/1000 ; Outfit est un grotesque géométrique de rapport comparable, déjà en production
  ici. Le repli reste `OpenAI Sans` puis la pile système.
- Mono (code, valeurs brutes, identifiants) : **`JetBrains Mono`** — déjà chargée,
  **inchangée**. Le `Semi-Mono` de la référence n'est d'ailleurs pas monospacé (`n` 597,
  `o` 594, `0` 636 dans le `.ttf`) : rien à transposer.
- **Pas de serif d'affichage.** La référence emploie `CoFo Robert`, un serif, pour ses
  grands titres. On ne le transpose pas : le cran `display` de tr4de porte un **montant**,
  et un serif y coûterait les chiffres tabulaires et la lisibilité d'un P&L. Non-choix
  délibéré, à ne pas « corriger ».

**Échelle : inchangée.** Les dix crans de `lib/ui/type.ts` (10, 11, 12, 13, 14, 16, 20, 24,
28, 40) restent tels quels, ainsi que leurs interlignes et leur test de garde. Raison
mesurée : sur l'écran `2026-recommandations-de-parcours.webp`, le rapport titre d'écran /
titre de carte vaut **1,46** (bandes d'encre de 57 px et 39 px au même seuil) ; dans tr4de
`title2 / headline` vaut **1,50**. La hiérarchie visée est déjà en place. Un prompt qui
changerait l'échelle ici casserait un système testé pour rien.

**Ce qui change en typographie, et c'est tout :**

1. **La méta passe en capitales espacées.** Relevé : la référence écrit ses lignes de
   métadonnées en capitales (`5 LEVELS • 9 COURSES`, bande d'encre de 18 px sans
   jambages). → Les crans `caption` (11) et `label` (12) employés comme **métadonnée**
   — sous-libellé de KPI, unité, en-tête de tableau, ligne « 3 trades · 2 gagnants » —
   prennent `text-transform: uppercase` et `letter-spacing: 0.06em`, en `texte-faible`.
   **Ne s'applique pas** aux libellés de champ de formulaire, ni à aucun texte saisi par
   l'utilisateur, ni aux noms d'instruments.
2. **Les titres passent en 700.** Relevé sur le spécimen et les écrans : les titres de la
   référence sont en Bold, pas en Semibold. → `--fw-semibold: 600` reste pour les valeurs ;
   les crans `title3`, `title2`, `title1` et `display` prennent **700**.
3. **Chiffres tabulaires partout où un montant peut changer** :
   `font-variant-numeric: tabular-nums`. Déjà présent via `TABULAR` — vérifie qu'il couvre
   les cellules de tableau, le calendrier P&L et les compteurs animés (`CountUp`).

### 5.3 Espacement

**Unité 4, échelle inchangée** : 4, 8, 12, 16, 24, 32. Les distances qui changent, toutes
relevées sur `2026-recommandations-de-parcours.webp` (capture 1080 px de large, 3x, marges
converties en points logiques, ±2 px) :

- **Padding de carte : 20 → 24.** Relevé : 68 px du bord de carte à la première encre, en
  haut comme à gauche, soit ~23 px logiques.
- **Marge latérale du contenu sur mobile : 16.** Relevé : 40 px, soit ~13 px logiques,
  arrondis au cran de l'échelle.
- **Gouttière entre cartes d'une même liste : 12.** Inchangée.
- **Rythme entre sections : 32.** La référence sépare ses sections par un intertitre centré
  et un blanc franc ; 32 est le cran haut de l'échelle existante.
- **Jamais deux séparateurs consécutifs.** Un trait suivi d'un fond gris, ou deux traits à
  moins de 24 px l'un de l'autre : tu gardes le premier et tu remplaces le second par un
  espace de 24.

### 5.4 Rayons, bordures, élévation

**Rayons.**

- `--radius-field: 6px` — **inchangé**. La référence ne publie que les bouts de son échelle
  (`sm` = `.125rem`, `3xl` = `2rem`, `full`) ; le cran des champs n'est pas documenté.
- `--radius-card: 10px → 16px` — **relevé**. Le coin de carte s'étend sur 48 px dans une
  capture 3x, soit ~16 px logiques. Le tracé n'est pas un arc de cercle : la courbe
  s'aplatit progressivement (superellipse, coin continu à la iOS). Si `border-radius`
  produit un coin trop sec à l'œil, c'est acceptable — **n'ajoute aucune dépendance pour
  tracer un squircle**.
- `--radius-modal: 14px → 32px` — **charte** (`2rem`, le cran `3xl`).
- `--radius-pill: 999px` — **inchangé**, charte (`full` = 9999px).
- Les **142 rayons hors échelle** câblés en dur (`8` 64×, `12` 78×) sont ramenés au cran le
  plus proche : `8 → 6`, `12 → 16` s'il s'agit d'une carte ou d'un panneau, `12 → 6` s'il
  s'agit d'un champ ou d'une petite pastille. Les `48` et `16` isolés vont sur `radius-card`.

**Bordures.** Trait 1 px `bordure` sur les cartes, les champs, les lignes de tableau. Au
survol d'une carte cliquable : `bordure-forte`. Pas de bordure sur un aplat de couleur
pleine. Pas de bordure gauche colorée de 3 px sur les cartes (la variante `accent` du
composant `Card`) : elle contredit le principe 1 — remplace-la par un **point de 8 px** de
la teinte, posé en tête de la première ligne de contenu (avant le titre s'il y en a un,
sinon en haut à gauche de la zone de padding).

**Élévation.**

- `--elev-rest: 0 1px 3px rgba(0, 0, 0, 0.04)` — **charte** (`elevation-subtle`, écrit
  `#0000000a` dans les tokens de la référence). C'est l'ombre de tous les blocs au repos.
- `--elev-card`, `--elev-pill` : alignés sur `--elev-rest`. Deux ombres de repos différentes
  pour deux familles de blocs n'ont plus de raison d'être.
- `--elev-hover`, `--elev-overlay` : la référence déclare `elevation-base` et
  `elevation-md` en `0 0 15px` et `0 0 25px` mais **la couleur de ces deux ombres n'a pas
  été relevée**. Garde les valeurs actuelles de tr4de en n'en changeant que le flou :
  `--elev-hover: 0 0 15px rgba(20,30,35,.10)`, `--elev-overlay: 0 0 25px rgba(20,30,35,.18)`.
- En thème sombre, l'ombre ne se voit pas : les blocs se séparent par la marche de surface
  `#141414` → `#1E1E1E` (1,11:1) **plus un filet** `0 0 0 1px rgba(255,255,255,0.05)`,
  exactement comme aujourd'hui. Le filet n'est pas optionnel : sans lui, 1,11:1 ne délimite
  rien.

### 5.5 Iconographie et illustration

- **Icônes : `lucide-react`, inchangé.** Trait 1,5 px, taille 14/16/20 selon le cran de
  texte voisin, couleur `texte-faible` au repos, `texte` à l'état actif. Aucune icône
  colorée dans la navigation.
- **Aucune illustration ajoutée.** La référence n'a pas d'illustration décorative : son
  seul système illustré est le **diagramme du contenu lui-même**, et c'est précisément ce
  qui se transpose ici. Dans tr4de, le graphique **est** l'illustration : courbe d'équité,
  calendrier P&L, Sankey de flux, anneau de patrimoine, heatmap d'heures. Ils reçoivent le
  traitement que la référence donne à ses figures : posés dans un conteneur
  `surface-figure` à `radius-card`, padding 24, la question ou le titre en gras au-dessus à
  gauche, la légende en capitales espacées.
- **Aucune mascotte, aucun personnage.** Voir section 10.
- Les émojis présents dans les libellés de navigation (`"📊 Dashboard"` dans
  `components/ui/Navigation.jsx`) sont remplacés par l'icône `lucide` correspondante : un
  émoji est un glyphe de police système qui ne suit ni le thème ni la couleur.

### 5.6 Densité et layout

**Inchangés** : largeur de la barre latérale (220 px, 56 px repliée), la bascule mobile vers
`TabBar` + `MobileHeader`, la densité des tableaux de trades, la largeur maximale du
contenu. tr4de est un outil dense ; la référence est une app de lecture. **On ne transpose
pas sa densité** — on transpose son calme, qui vient de la couleur et de l'ombre, pas de
l'air.

Ce qui change :

- La barre latérale passe sur `surface` (blanc) et la page sur `surface-page` : la sidebar
  se détache par la surface, sans trait. En sombre, sidebar `#141414` et cartes `#1E1E1E`.
- Un écran a **un seul titre au cran `title2`**, aligné à gauche, en 700.
- Les intertitres de section sont au cran `title3`, en 700, précédés de 32 px de blanc.

### 5.7 Motion

**Presque inchangé, et c'est un constat, pas un oubli.** Le dossier source ne documente
aucune durée de transition d'interface : ses tokens de motion n'ont pas été relevés, et ses
médias sont des vidéos de case study, pas des enregistrements d'UI isolés. Tu gardes donc
`--ease-*`, `--dur-*`, `--tr-ui` et le bloc `prefers-reduced-motion` **tels quels**.

Ce qui est mesuré et transposable — relevé au différentiel d'image sur
`animations/unit-1-complete-blob-vert-et-badge_brilliant.mp4` et
`animations/streak-charge-pile-eclair_brilliant.mp4`, rééchantillonnés à 30 fps, précision
±33 ms :

- Une **célébration complète** (le blob se déforme, le badge jaillit, le halo s'étend) dure
  **≈ 1,2 s** au total (mouvement continu de 870 ms à 2 100 ms), découpée en **temps de 67
  à 200 ms**. Aucun temps ne dépasse 200 ms.
- Un **jeton qui tombe et rebondit** : chute ≈ 100 ms, rebond ≈ 200 ms.

→ Dans tr4de, cela ne concerne que les moments de progression : validation d'une série de
discipline, palier de Life RPG atteint, objectif rempli, révision terminée. Une célébration
tient en **1,2 s maximum**, aucun de ses temps ne dépasse **200 ms**, et sous
`prefers-reduced-motion: reduce` elle est **remplacée par son état final**, sans
déplacement — pas seulement accélérée.

**N'animent jamais** : les tableaux de chiffres, les cellules du calendrier P&L, la
navigation principale, les valeurs qui changent au fil d'une saisie.

## 6. Composants et états

Chaque composant, tous ses états. L'état de repos ne suffit pas.

### Bouton primaire (`Button variant="primary"`, `BTN`)

Fond `#141414`, texte `#FFFFFF` (18,42:1), rayon `--radius-pill`, hauteur et padding
inchangés (`BTN`), cran `body`/`callout` en 600. **Le noir reste l'action primaire**, comme
aujourd'hui et comme sur les écrans 2026 de la référence (`Check`, `Continue`).
Survol : `#383838` (`gray-900`, charte). Focus : anneau 2 px `#141414` décalé de 2 px,
**jamais `outline: none`**. Pressé : translation Y de +1 px, 100 ms. Désactivé :
`surface-figure` + `texte-placeholder`, curseur par défaut, pas d'ombre. Chargement :
libellé remplacé par l'anneau (§ LoadingScreen), **largeur figée** pour éviter le saut.

### Bouton d'accent (nouveau rôle, `variant="accent"`)

Pour la seule action qui *fait progresser* : démarrer une session, valider une journée de
discipline, clôturer une révision. Fond `accent #29CC57`, encre **`#141414`** (8,66:1 —
pas de blanc, § 5.1.2), rayon pill. Survol : `accent-presse #15B441`. Pressé : translation
Y +1 px et l'arête basse `inset 0 -2px 0 #15B441` disparaît — c'est le bouton à arête de la
référence, en 2 px, pas en 4. Focus : anneau 2 px `#141414`. Désactivé : comme le primaire.
**Un seul bouton d'accent par écran.**

### Bouton secondaire / fantôme

Secondaire : fond `surface`, trait 1 px `bordure`, texte `texte`. Survol : trait
`bordure-forte`, fond inchangé. Fantôme : transparent, survol `color-mix(in srgb,
var(--color-text) 4%, transparent)` (le `FIELD_BG` existant). Focus identique au primaire.

### Bouton danger

Fond `erreur #FF5D5D`, texte `#FFFFFF` (3,01:1 — donc **au cran `callout` 14 en 600
minimum**, jamais plus petit). Survol : `#BD4545`. Réservé aux suppressions réelles.

### Carte (`components/ui/Card.tsx`)

Fond `surface`, trait 1 px `bordure`, rayon 16, padding 24, ombre `--elev-rest`.
Survol (si `hoverable`, pointeur fin uniquement — la garde `hasFinePointer()` reste) :
trait `bordure-forte`, ombre `--elev-hover`, **pas de translation**. Focus : anneau 2 px
`#141414` décalé de 2 px. La variante `accent` perd sa bordure gauche de 3 px au profit
d'un point de 8 px de la teinte (même règle de placement qu'en 5.4).

### Champ (`lib/ui/form.jsx`)

Fond `surface`, trait 1 px `bordure`, rayon 6, hauteur inchangée. Placeholder
`texte-placeholder`. Survol : trait `bordure-forte`. Focus : trait `#141414` + anneau 2 px
`#141414` décalé de 2 px. Erreur : trait `erreur`, message dessous au cran `caption` en
`#BD4545` (l'encre claire, pas `#FF5D5D`), précédé d'une icône de 14 px. Désactivé :
fond `surface-figure`, texte `texte-faible`.

### Ligne de liste et de tableau

Repos : fond transparent, trait bas 1 px `bordure`. Survol : `--color-row-highlight`
(inchangé). Sélectionnée : `accent-voile` + un liséré gauche 2 px `accent`. La dernière
ligne n'a pas de trait bas.

### Navigation (`Sidebar`, `TabBar`, `Navigation`)

Item au repos : texte `#555555` en clair / `#999999` en sombre (inchangé), icône de la
même couleur. Survol : fond `--color-nav-hover-bg` (inchangé). **Actif : fond
`accent-voile`, texte et icône `var(--accent-ink)`** — c'est la correction obligatoire de
5.1.7. Focus : anneau 2 px `#141414`. `TabBar` mobile : cibles ≥ 44 px, item actif en
`accent-ink`, jamais un aplat plein.

### Feuille modale (`Sheet`) et modale

Fond `surface-elevee`, rayon 32 en haut (charte, `3xl`), voile `--color-scrim` inchangé,
ombre `--elev-overlay`. Entrée depuis le bas, `--dur-modal` inchangé. Fermeture au clavier
par Échap, focus piégé, focus rendu à l'élément déclencheur.

### État vide (`EmptyState`)

Pas d'illustration. Un titre au cran `headline` en 700, une phrase au cran `body` en
`texte-faible` qui dit **ce qu'on peut faire**, et un bouton d'accent unique. Fond
`surface-figure`, rayon 16, padding 32. Interdits : « Aucune donnée », « Rien à afficher »,
« Oups ».

### Chargement (`LoadingScreen`, `Skeleton`)

**C'est le composant qui porte le plus la référence.** Toute attente de plus de 400 ms
affiche un **anneau** — 40 px, trait 4 px, `alerte #F7C325` sur piste `surface-figure`,
rotation `--dur-spin` — et **une phrase qui nomme l'opération** au cran `body` en
`texte-faible` : « Récupération des trades depuis Interactive Brokers », « Calcul du
patrimoine sur 12 mois ». Jamais un spinner muet. Les `Skeleton` restent pour le contenu
déjà structuré (une liste dont on connaît la forme) ; ils ne remplacent pas la phrase.

### Notification (`AlertToast`) et retours de discipline

Succès : fond `succes-fond #D4F5DD`, encre `succes-encre #00370F` (11,53:1), icône de
coche. Avertissement : fond `color-mix(in srgb, #F7C325 20%, transparent)`, encre
`#886B14`. Erreur **réelle** : fond `color-mix(in srgb, #FF5D5D 16%, transparent)`, encre
`#BD4545`. **Règle non tenue, série rompue, objectif manqué, révision ratée** : fond
`color-mix(in srgb, #403000 8%, transparent)`, encre `reessai-encre #403000` (12,80:1 sur
blanc) — **et aucune trace de rouge**. C'est le principe 3, et c'est le point du prompt le
plus facile à rater.

### `XpBar`, séries et paliers

Piste `surface-figure`, remplissage `accent`, rayon pill, hauteur inchangée. Le compteur en
chiffres tabulaires. La pastille de série prend `alerte #F7C325` en fond et `#141414` en
encre (11,22:1) — c'est le jaune que la référence emploie pour ses séries et ses
surlignages. Les paliers portent **un nom avant leur chiffre** (§ 8).

### Graphiques (`ApexChatNew`, `HoursHeatmap`, `SankeyFlow`, `EquityByAccount`)

Conteneur `surface-figure`, rayon 16, padding 24. Séries : `PALETTE` dans l'ordre, teinte
**brute** pour les aplats (secteur, ruban, barre), teinte **passée par `deepen()`** pour les
puces de légende, les traits fins et les libellés — la règle existante, avec les nouvelles
teintes. Grille et axes en `bordure`. Étiquettes d'axe au cran `caption2` en `texte-faible`,
en capitales espacées. Infobulle : `surface-elevee`, trait 1 px `bordure`, rayon 6, ombre
`--elev-hover`. La courbe d'équité garde `--accent-2`.

## 7. Écran par écran

28 pages passent par `DA_PAGES` dans `components/DashboardNew.jsx`. Elles se traitent par
familles : le système fait le travail, et seul le cas particulier de chaque famille est
écrit ici.

**1. Tableau de bord** (`dashboard`). Le chiffre héros P&L au cran `display` 40 en 700,
tabulaire, décimales en `--color-num-muted`. Le calendrier P&L garde ses aplats vifs et
change d'encre (§ 5.1.6). Les cartes de KPI passent en padding 24 et rayon 16, leur
sous-libellé en capitales espacées. **Cas particulier** : c'est l'écran le plus chargé en
couleur de l'app — après refonte, compte les pixels colorés. Si un aplat teinté ne porte
pas un chiffre ou un état, il n'a rien à faire là.

**2. Trades** (`trades`, `add-trade`, `trade-chart`, `calendar`). Tableaux denses,
inchangés en densité. Les tags Long / Short gardent leur construction (aplat dilué + encre
brute) sur `#29CC57` et `#FF8D23`, l'encre passant par la règle 5.1.4 :
`#007C23` pour Long, `#A65C17` pour Short. Les vignettes rondes d'instrument
(`--color-symbol-badge`, sigle blanc) sont des **logos** : elles ne changent pas et ne
passent pas par le thème — le commentaire existant du fichier le dit déjà, respecte-le.

**3. Comptes et patrimoine** (`accounts`, `account-detail`, `firm-detail`, `patrimoine*`,
`cashflow`, `budget`, `spending`, `brokers`). Les pastilles `CHIP` sont recalculées sur les
nouvelles teintes en gardant **la méthode existante** : fonds ramenés à une luminance
constante de 0,75, encre descendue jusqu'à 4,5:1 sur son propre fond. Ne remplace pas les
couples à la main. Le Sankey et les anneaux prennent `PALETTE` brut.

**4. Discipline et progression** (`discipline`, `life-rpg`, `goals`, `revisions`, `journal`,
`daily-planner`, `agenda`). **C'est ici que la référence paie le plus.** Trois changements
qui ne se déduisent d'aucune règle de couleur :
- Toute rupture — série cassée, règle non tenue, révision ratée, objectif manqué — passe au
  brun `#403000`. Cherche chaque `#FF4B4B` de ces pages : la plupart deviennent du brun,
  pas du `#FF5D5D`.
- Les paliers sont **nommés avant d'être chiffrés** (§ 8).
- La célébration d'un palier suit le budget de 1,2 s de la section 5.7.

**5. Contenu et outils** (`notes`, `strategies`, `strategy-detail`, `blueprint`, `sport`,
`eloquence`, `reading-list`, `drive`, `backtest`, `scaling`). Ces pages portent du texte
long : elles gagnent l'**encart d'explication** de la référence — fond `surface-encart
#F2F9FB`, trait 1 px `bordure-encart #AACFD7`, rayon 16, padding 24 — pour les aides, les
définitions et les rappels de méthode. `#141414` dessus rend 17,30:1. C'est le seul fond
teinté autorisé sur du texte courant.

**6. Chrome** (`Sidebar`, `MobileHeader`, `TabBar`, `CommandPalette`, `Sheet`, modales,
`SettingsPage`). Voir section 6. Dans `SettingsPage`, la section Apparence affiche les cinq
nouveaux préréglages d'accent : la pastille de chaque préréglage montre l'aplat **et** son
encre dérivée, pour qu'on voie tout de suite qu'un accent clair reste lisible.

## 8. Contenu et ton

Tu ne réécris pas le contenu métier. Tu réécris **les états vides, les messages d'erreur,
les retours de progression et les libellés de chargement**, et seulement eux.

Les principes du tuteur de la référence sont des règles de conduite, pas de style. Trois se
transposent tels quels :

- **« Ne dis pas *pas de souci* quand quelqu'un se trompe. »** Aucun message ne minimise un
  échec. Pas de « Pas grave ! », pas de « Oups », pas de « Ce n'est rien ». Une série
  rompue se dit : « Série interrompue le 12 août. 6 jours au compteur avant ça. »
- **« Confirme le progrès, ne l'explique pas. »** Un succès se constate en une phrase
  courte et factuelle, sans félicitation ni superlatif. « Journée validée. 7 jours de
  suite. » et rien de plus.
- **Nommer les paliers avant de les chiffrer.** La référence appelle ses objectifs
  quotidiens Casual, Regular, Serious, Intense plutôt que 5, 10, 15, 20 minutes. Applique-le
  aux paliers de discipline, aux niveaux de Life RPG et aux paliers de scaling : le nom
  d'abord, le chiffre en `texte-faible` derrière.

Règles de forme : phrases courtes, **aucun point d'exclamation**, aucun émoji (ni dans les
libellés, ni dans les messages, ni dans les icônes de nav), pas de tutoiement de l'outil
vers l'utilisateur là où l'app ne le fait pas déjà, montants toujours avec leur devise. Un
message d'erreur dit **ce qui a échoué et ce qu'on peut faire**, jamais un code seul.

## 9. Accessibilité

Non négociable, et déjà vérifiée pour tout ce qui est chiffré ici. Seuils : 4,5:1 texte
courant, 3,0 grand texte et composants.

- Les couples de la section 5.1 sont validés. **Les interdits de 5.1.3 sont des interdits**,
  pas des recommandations.
- Focus visible sur **tout** élément atteignable au clavier : anneau 2 px `#141414` en
  clair, `#FFFFFF` en sombre, décalé de 2 px. `:focus-visible` existe déjà — tu l'étends,
  tu ne le remplaces pas. **Aucun `outline: none` sans anneau de remplacement.**
- Cibles tactiles ≥ 44 px sur mobile, `TabBar` comprise.
- Ordre de tabulation conforme à l'ordre visuel ; focus piégé dans les modales et rendu au
  déclencheur à la fermeture.
- `prefers-reduced-motion: reduce` : aucun déplacement, aucune célébration jouée — l'état
  final directement. Seule l'opacité reste autorisée.
- Le corps de texte de tr4de est à 13 px : c'est **inchangé**, c'est un outil dense et c'est
  la décision documentée du projet. En contrepartie, aucun texte ne descend sous 10 px, et
  aucun texte sous 12 px ne porte une information qui n'existe pas ailleurs.
- Aucune information portée par la couleur seule : un gain se lit au signe, un état à son
  libellé, une série à son chiffre.

## 10. Interdits

**Anti-pastiche.** La référence est un système observé, pas une marque à emprunter.

- Ne reprends **ni le nom, ni le logo, ni le wordmark, ni l'icône** de Brilliant.
- Ne reprends **pas Koji** : ni le personnage, ni un blob à quatre pointes, ni un
  personnage à œil unique, ni « une mascotte dans le même esprit ». tr4de n'a pas de
  mascotte et n'en gagne pas une ici.
- Ne reprends **pas le style d'illustration `PIX`**, ni les cubes isométriques, ni les
  vignettes de cours, ni les badges de ligue.
- **N'installe, ne copie, ne convertis, ne recrée aucune police CoFo.** Elles sont
  propriétaires et non redistribuables. Le substitut est Outfit, déjà en place.
- N'introduis **aucun vocabulaire d'apprentissage** emprunté à la référence : pas de
  « leçon », pas de « parcours », pas de « ligue », pas de « XP » là où tr4de ne l'emploie
  pas déjà. tr4de garde ses mots.
- **tr4de reste tr4de** : son nom, son icône, son ton.

**Anti-dérive.**

- Aucune dépendance ajoutée ou retirée. Pas de librairie d'animation, pas de Rive, pas de
  bibliothèque de composants, pas de squircle.
- Aucun renommage de fichier, de route, de composant exporté ou de clé `localStorage`.
- Aucune modification de la logique métier, des calculs, des requêtes Supabase, des
  parseurs.
- Pas de refactor « tant que j'y suis » : pas de passage de `.jsx` à `.tsx`, pas de
  conversion des styles inline vers Tailwind, pas de nettoyage de `lib/design/tokens.ts`.
- Aucun nouveau token de couleur hors du tableau 5.1 et de la correspondance 5.1.0.
  Aucune **nouvelle** valeur de couleur écrite en dur dans un composant : ce que tu
  ajoutes ou modifies passe par `T` ou par une variable CSS. Les hex en dur préexistants
  qui ne sont ni une teinte de la charte Duolingo ni le doublon d'un token existant
  peuvent rester : le lot 3 les traite, il ne les épuise pas, et la recette ne vérifie
  que ce que le lot 3 promet.

## 11. Plan d'exécution

Un lot, un commit. Les tokens d'abord — sinon tu styles des composants avec des valeurs que
tu vas changer au lot suivant.

1. **Tokens** — `app/globals.css` : tous les rôles de 5.1 en clair et en sombre selon la
   correspondance 5.1.0, les variables nouvelles, les rayons de 5.4, l'élévation,
   `--accent-ink` à 45 %, `--color-nav-active-text` corrigé, `--color-info` passé au bleu,
   et la mise à jour des **210 rustines par sélecteur d'attribut** (piège 3 de 5.1.0).
   Puis `lib/ui/tokens.ts` : les replis alignés et les nouvelles entrées de `T`.
2. **Palette et accent** — `lib/ui/palette.ts` (les 14 teintes, `PALETTE` sans vert ni
   rouge, `PALETTE_DARK`/`PALETTE_LIGHT` recalculés, `CHIP` recalculé par la méthode
   existante, `GREY`) et `lib/ui/accent.ts` (défauts et cinq préréglages).
3. **Balayage des hex en dur** — les 168 occurrences des six teintes Duolingo, puis les
   blancs, noirs et gris qui doublent un token existant. Un fichier à la fois, en vérifiant
   l'écran. **C'est le lot le plus long : ne le sous-estime pas et ne le fusionne pas avec
   un autre.**
4. **Rayons hors échelle** — les 142 occurrences de `8` et `12` ramenées au cran.
5. **Primitives** — `Button` (dont la nouvelle variante `accent`), `Card`, `form.jsx`,
   `Sheet`, `EmptyState`, `LoadingScreen`, `AlertToast`, `Navigation`/`Sidebar`/`TabBar`,
   `XpBar`. **Tous les états de la section 6**, pas seulement le repos.
6. **Typographie** — capitales espacées sur la méta, titres en 700, `tabular-nums` vérifié.
7. **Écrans**, dans l'ordre des six familles de la section 7. La famille 4 (discipline) en
   dernier : c'est celle qui demande du jugement sur le brun contre le rouge.
8. **Recette** (section 12) et corrections.

## 12. Recette

Chaque ligne est vraie ou fausse.

- `grep -rn "58CC02\|FF4B4B\|FF9600\|1CB0F6\|CE82FF\|7AF0F2\|64D741\|4CC72C" app components lib` → **vide**.
- `grep -rnE "borderRadius: *(8|12|2|3|4|5|48)\b" app components` → **vide**.
- `git diff --stat package.json package-lock.json` → **vide**.
- `git diff --name-only | grep -E "^(app/api|lib/supabase|lib/brokers|lib/ai)/"` → **vide**.
- `npm run lint:strict` → 0 erreur, 0 avertissement.
- `npm test` → tout passe, `tests/typeScale.test.ts` compris.
- `grep -rn "outline: *['\"]none" app components` → chaque occurrence est suivie d'un
  `boxShadow` d'anneau dans le même objet de style.
- Aucun émoji dans les libellés de nav :
  `python3 -c "import re,sys;print([l for l in open(sys.argv[1]) if re.search(r'[\\U0001F300-\\U0001FAFF\\u2600-\\u27BF]',l)])" components/ui/Navigation.jsx`
  → `[]`.
- Thème sombre : chaque rôle du tableau 5.1 est défini dans `:root` **et** redéfini dans
  `:root[data-theme="dark"]`. Aucune couleur n'existe uniquement dans le bloc sombre.
- Chaque variable marquée **nouvelle** en 5.1.0 existe dans les deux blocs :
  `for v in surface-figure quip-bg quip-bd text-placeholder feedback-ok-bg feedback-ok-ink feedback-retry-ink link on-accent; do echo -n "$v "; grep -c -- "--color-$v:" app/globals.css; done`
  → **2** pour chacune, et chacune a son entrée dans `T`.
- `grep -n -- "--color-info:" app/globals.css` → la valeur est `#456DFF`, plus `#CE82FF`.
- À l'œil, thème clair, page `dashboard` : **aucun aplat de couleur ne porte autre chose
  qu'un chiffre, un état ou une action**. Compte-les — s'il y en a plus de cinq, le
  principe 1 n'est pas tenu.
- À l'œil, page `discipline` : **aucun rouge**. Une série rompue est brune.
- Au clavier seul, du haut de la page au bas : l'anneau de focus est visible sur chaque
  arrêt, dans les deux thèmes.
- Réglages → Apparence : chacun des cinq préréglages appliqué, l'item de nav actif reste
  lisible dans les deux thèmes.
- Une attente longue (chargement du patrimoine, import CSV) : un anneau **et** une phrase
  qui nomme l'opération.
- `prefers-reduced-motion` activé au niveau système : plus aucun déplacement, aucune
  célébration jouée.
- Mobile 375 px : aucun débordement horizontal, `TabBar` à cibles ≥ 44 px.

## 13. Visuels d'appui

Fichiers **locaux** sur la machine de Sacha. Si tu tournes ailleurs, demande-les : sans eux,
les sections 4, 5.3 et 5.4 se lisent mais ne se vérifient pas.

- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/brilliant/couleurs/palette-relevee-dans-les-ecrans.svg`
  — la preuve du principe 1 : le blanc à 61,09 %, la couleur de marque à 0,16 %. À regarder
  avant d'écrire la moindre couleur.
- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/brilliant/couleurs/palette-declaree-neutres-et-semantiques.svg`
  — les deux tokens de feedback, `#00370F` et `#403000`, avec leur note d'usage. C'est la
  source du principe 3.
- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/brilliant/ecrans/planches/planche-diagrammes-interactifs.png`
  — le conteneur gris à coins arrondis, la question en gras au-dessus à gauche, la couleur
  réservée aux objets manipulables. C'est le modèle exact du traitement des graphiques
  (§ 5.5).
- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/brilliant/ecrans/2026-recommandations-de-parcours.webp`
  — la carte : rayon, padding, trait fin, méta en capitales espacées, badge de mise en
  avant. Les mesures de 5.3 et 5.4 viennent de cet écran.
- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/brilliant/ecrans/2024-accueil-for-you-streak-et-practice.png`
  — la série et le bouton d'accent : aplat `pear` à encre noire, carte d'accent à fond très
  dilué. Attention, millésime 2024 : son CTA est lime là où 2026 met du noir.
- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/brilliant/ecrans/planches/planche-lecons-et-leagues.png`
  — le CTA noir, le classement, et l'écran de chargement en anneau jaune avec sa phrase
  (vignette 7). Le modèle de `LoadingScreen`.
- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/brilliant/branding/typo/specimen-les-trois-familles-cofo.png`
  — l'allure du sans, pour juger si Outfit tient le rôle. **Aucune de ces polices ne
  s'installe** (§ 10).
- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/brilliant/couleurs/palette-declaree-echelle-du-vert.svg`
  — l'échelle complète du vert : c'est la seule teinte dont tous les crans sont publiés,
  d'où le fait que le vert échappe à la règle de dérivation 5.1.4.

## 14. Décisions laissées à l'agent

Trous assumés. Chacun porte sa contrainte : tu décides à l'intérieur, pas au-delà.

1. **Les crans intermédiaires de rayon.** La référence ne publie que `sm` `.125rem`, `3xl`
   `2rem` et `full`. `--radius-field` reste à 6 ; si un composant demande un cran entre 6 et
   16, prends 6 ou 16, **n'en crée pas un troisième**.
2. **Les durées de transition d'interface.** Non relevées (§ 5.7). Garde `--dur-*` et
   `--ease-*` tels quels. **Ne les « harmonise » pas.**
3. **La couleur des ombres `elevation-base` et `elevation-md`.** Seul le flou est connu
   (15 px, 25 px). Garde les couleurs actuelles de tr4de.
4. **Les crans autres que 500 des 13 teintes non-vertes.** Non publiés. Calcule-les par les
   règles de 5.1.5, et dis-le en commentaire dans le fichier. **N'invente aucun hex.**
5. **Les valeurs sombres des tokens sémantiques de la référence.** Le dossier source établit
   que le système est en double thème complet mais ne donne pas les valeurs sombres au cas
   par cas. Celles du tableau 5.1 marquées « déduit » sont dérivées ; si l'une rend mal,
   corrige-la **en vérifiant le contraste**, et note la correction.
6. **Le fond de page chaud.** `oat-50 #F5F3F1` inverse une décision documentée de tr4de
   (§ 5.1.1). Si à l'écran il pèse trop, replie-toi sur `#F5F5F5` et signale-le — mais
   **pas** sur un gris bleuté.
7. **Quelles pages de la famille 5 reçoivent l'encart d'explication.** À toi de voir où une
   aide existe déjà. N'en crée pas de nouvelles : tu ne changes pas le contenu.

---

Fin du prompt.
