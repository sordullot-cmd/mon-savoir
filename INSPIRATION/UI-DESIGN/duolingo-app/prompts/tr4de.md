---
type: prompt-refonte
source: duolingo-app
sources_secondaires: [duolingo, duolingo-2026]
cible: tr4de (taotrade)
cible_url: file:///Users/account/Documents/GitHub/tr4de
destination: agent-de-code
axes: [couleurs, typo, spacing, rayons, elevation, densite, motion, composants, etats, ton, accessibilite]
axes_ouverts: [iconographie, illustration, motion-de-celebration]
date: 2026-08-25
tags: [prompt, refonte, da, duolingo, tr4de]
---

# Prompt de refonte — tr4de dans la DA Duolingo

Ce prompt aligne l'interface de **tr4de** (`~/Documents/GitHub/tr4de`, Next.js 16 / React 19 /
Tailwind v4) sur la direction artistique de Duolingo. Les valeurs viennent de trois dossiers du
vault : [[duolingo-app]] (relevé produit — parts de surface, arêtes, composants, animations),
[[duolingo]] (charte publiée — les 38 teintes, Pantone, règles typographiques) et
[[duolingo-2026]] (identité 2026 — origine de Feather Bold, chaîne motion Rive).

**État de la cible au 25 août 2026** : tr4de porte **déjà** les 38 teintes de la charte
(`lib/ui/palette.ts`, sous leurs noms d'animaux), une échelle typographique à dix crans, une
progression d'espacement et un thème sombre complet. Ce n'est donc pas une refonte à zéro :
c'est le passage d'un habillage SaaS neutre qui *emprunte les couleurs* de Duolingo à un
système qui en reprend **la mécanique de surface** — l'arête basse solide, la bordure de 2, le
blanc comme structure. Relevé fait par lecture du code (tokens, primitives), pas par capture
d'écran : l'app exige Supabase et une session.

> **Un autre prompt vise la même cible.** `INSPIRATION/UI-DESIGN/brilliant/prompts/tr4de.md`,
> écrit le même jour, refond tr4de dans la DA de **Brilliant** — que sa propre fiche décrit comme
> « l'anti-Duolingo sur la couleur ». Les deux sont **mutuellement exclusifs** : appliquer l'un
> défait l'autre. À arbitrer avant d'en lancer un.

## Le prompt — tout ce qui suit est à copier

---

## 1. Mission

Tu refonds l'interface de **tr4de** (journal de trading + suivi de vie, Next.js 16 / React 19 /
Tailwind v4 / Tauri) pour l'aligner sur une direction artistique décrite intégralement
ci-dessous. Tu ne changes ni le contenu, ni les routes, ni la logique métier, ni le schéma de
données. Tu rends un diff qui passe `npm run lint:strict` et `npm run test`, et qui satisfait la
recette de la dernière section.

La référence est Duolingo. Elle sert de **référence de système** — mécanique de surface, rôles de
couleur, rythme, motion. Elle ne sert **jamais** de modèle à cloner : ni mascotte, ni logo, ni
illustrations, ni fontes propriétaires (voir § 10).

## 2. Périmètre

**Tu changes** : les tokens de style (`app/globals.css`, `lib/ui/tokens.ts`, `lib/ui/buttons.ts`,
`lib/ui/type.ts`), les primitives d'UI de `components/ui/`, les espacements, l'élévation, le
motion, le thème sombre, et les cinq écrans pilotes nommés au § 7.

Plus deux fichiers qui ne sont pas des pages mais portent le châssis : **`components/DashboardNew.jsx`**
(le shell — barre latérale, barre du haut, fond de page) et **`components/LandingPage.jsx`**.

**Tu ne touches pas** : les textes et libellés métier, les routes et URLs, la logique de calcul
(P&L, statistiques, Sankey), le schéma Supabase, `src-tauri/`, les fichiers de test, les
dépendances (**aucun ajout de librairie, aucune police téléchargée**), les 32 pages de
`components/pages/` non citées au § 7 — elles héritent des primitives et ne sont pas retouchées
une par une.

**La seule exception, et elle est explicite : la substitution mécanique des métriques de bouton.**
`tests/buttonMetrics.test.ts` est un garde-fou qui lit le code source au regex et compare chaque
bouton en pilule aux valeurs de `BTN`. Aujourd'hui **2 fichiers seulement importent
`lib/ui/buttons`**, contre environ **304 pilules**, **157 `padding: "8px 16px"`** et **159
`minHeight: 34`** écrits à la main : changer `BTN_HEIGHT` sans les migrer fait passer le test au
rouge sur ~247 emplacements dans ~41 fichiers, et produit à l'écran des boutons de 44 à côté de
boutons de 34 — exactement le défaut que l'audit prétendait avoir corrigé.

Donc : **tu es autorisé à traverser ces ~41 fichiers, y compris les pages hors périmètre, pour la
seule substitution des métriques de bouton** — remplacer les `minHeight: 34` / `height: 34` /
`padding: "8px 16px"` / `borderRadius: 999` de bouton par un étalement de `BTN.*`. C'est une
substitution mécanique, elle a son propre lot et son propre commit (§ 11), et **elle ne donne le
droit de rien changer d'autre dans ces fichiers** : pas une couleur, pas une taille de texte, pas
une structure. **Tu ne modifies ni n'assouplis `tests/buttonMetrics.test.ts`** — c'est lui qui
prouve que la substitution est complète.

## 3. État actuel

- **Stack** : Next.js 16 (App Router), React 19, Tailwind v4 via `@tailwindcss/postcss` — **il
  n'y a pas de `tailwind.config`**, le thème vit en variables CSS. Desktop en Tauri 2. Icônes
  `lucide-react`. Graphiques `apexcharts`, `recharts`, `lightweight-charts`.
- **Où vivent les tokens** :
  - `app/globals.css` — variables CSS sur `:root`, thème sombre sur `:root[data-theme="dark"]`.
    C'est la source des couleurs de surface, des rayons, de l'espacement, du motion.
  - `lib/ui/palette.ts` — les 38 teintes de la charte Duolingo sous leurs noms d'animaux (`HUE`),
    puis `PALETTE` (les huit principales). **Couleurs de catégorie**, volontairement identiques
    dans les deux thèmes.
  - `lib/ui/type.ts` — l'échelle typographique en pixels (le site est en styles inline).
    `app/globals.css` expose la même échelle en `rem`. **Les deux se modifient ensemble.**
  - `lib/ui/buttons.ts` — la table unique des hauteurs et marges de bouton.
  - `lib/ui/tokens.ts` — l'accès TypeScript aux couleurs sémantiques (`T.green`, `T.red`…).
    Toute variable CSS que tu ajoutes ou supprimes se répercute ici : `T.elevCard` et `T.elevPill`
    disparaissent avec leurs variables, et chaque nouveau rôle du § 5 reçoit sa clé
    (`T.arete`, `T.areteAction`, `T.areteSucces`, `T.areteAlerte`, `T.areteAttention`,
    `T.areteInfo`, `T.surfaceCreuse`, `T.encreSurCouleur`).
  - `lib/design/tokens.ts` — **un sixième fichier de tokens**, plus ancien (il contient
    `bgSubtle: "#FAFAFA"`). Ne l'étends pas et ne t'appuie pas dessus ; si un composant que tu
    touches le lit, fais-le passer par `lib/ui/tokens.ts`. Signale-le dans ton rapport, ne pars
    pas le migrer.
- **Ce qui est déjà bon et doit survivre** :
  - les 38 teintes de la charte, sous leurs noms d'origine — n'en ajoute aucune, n'en calcule
    aucune ;
  - la règle « aplat → couleur brute ; puce, trait, texte → `deepen()` / `dotRing()` » de
    `lib/ui/color` ;
  - la source unique des tailles de texte et des hauteurs de bouton — le site en est sorti après
    un audit (1 917 `fontSize` en dur, 607 boutons écrits à la main). **Ne réintroduis aucune
    valeur en dur** : tout passe par `TS`/`TYPE`, `BTN`, `T` et les variables CSS ;
  - `:focus-visible` (anneau 2 px, décalé de 2) et le bloc `prefers-reduced-motion` existants ;
  - `--accent` / `--accent-2` réglables par l'utilisateur dans Réglages → Apparence
    (`lib/ui/accent.ts`), écrits en style inline sur `<html>` ;
  - `tabular-nums` (`TABULAR` dans `lib/ui/type.ts`) sur tout montant qui peut changer.

## 4. La direction artistique

**Direction** : la densité d'un outil de trading, posée sur la mécanique de surface de Duolingo —
du blanc, des blocs qui ont une épaisseur physique, et la couleur réservée à ce qui compte.

1. **Le blanc n'est pas un fond, c'est la structure.** Relevé : Snow occupe **82,6 %** des pixels
   des 20 écrans officiels, **sans un seul gris de remplissage**. → le fond de page passe au blanc,
   et les blocs se détachent par leur **bordure et leur arête**, et **non plus** par un gris de
   fond. C'est ce qui résout le problème documenté dans `globals.css` (« les cartes blanches ne se
   détachaient pas ») sans avoir besoin d'un gris de page.
   **Attention à l'endroit exact** : `--color-bg` vaut **déjà** `#FFFFFF` et `body` l'utilise déjà
   — il n'y a rien à y faire. Le gris que tu vois à l'écran vient de `--color-bg-subtle: #F5F5F5`,
   posé par le shell dans `components/DashboardNew.jsx` **l. 815** (le conteneur racine) et
   **l. 875** (la barre du haut). Ce sont ces deux endroits, et eux seuls, qui passent à
   `var(--color-bg)`.
2. **Un bloc a une épaisseur, pas une ombre.** Relevé : chaque bouton et chaque carte porte une
   **arête basse en aplat solide** d'un ton plus foncé de la même famille — `owl` → `treeFrog`,
   `macaw` → `whale`, blanc → `swan`.
   *(Note de vocabulaire, pour éviter une recherche infructueuse : la charte appelle le vert de
   marque « Feather Green » et le blanc « Snow ». `lib/ui/palette.ts` les nomme `owl` et n'a pas
   d'entrée pour le blanc. **Le nom qui fait foi dans ce prompt est celui du code** : `owl`
   `#58CC02`. Les noms de charte n'apparaissent qu'en rappel.) → toutes les `box-shadow` floues des cartes et des boutons
   disparaissent au profit d'un `box-shadow: 0 <arête>px 0 <couleur>`. L'ombre floue ne survit
   que sous les calques flottants (modale, menu, popover).
3. **Le vert est la couleur du succès, pas celle de l'interface.** Relevé sur les écrans de
   leçon : Macaw `#1CB0F6` est presque **quatre fois** plus présent que Feather Green `#58CC02`.
   Le vert tient la validation, la barre de progression et le CTA de progression ; le bleu porte
   tout le reste de l'interaction. → dans tr4de, le vert reste au P&L positif et au succès ; le
   bleu prend la sélection, l'état actif et les actions neutres.
4. **La couleur en petite quantité, et toujours pour dire quelque chose.** Relevé : Cardinal
   0,3 %, Bee 0,1 %, Beetle 0,1 % de la surface. → aucun aplat de couleur décoratif ; une couleur
   posée sur un écran doit être justifiable par un état.
5. **Les styles typographiques sont « minimaux et intentionnels », et le titre est toujours au
   même endroit.** Principe livré du Tab Refresh de février 2026 (Leah Lee, Lokesh Fulfagar),
   avec la taille de header **hiérarchisée selon la fonction de l'écran**. → un seul titre
   d'écran par vue, à la même position sur toutes les pages, et pas de nouveau cran typographique.

## 5. Le système

Provenances : **charte** = charte Duolingo publiée · **relevé** = mesuré sur les médias du
dossier · **déduit** = dérivé d'une valeur sourcée par la règle écrite à côté.

### Échelle du relevé

Les valeurs géométriques ci-dessous sont mesurées en pixels sur deux captures indépendantes
(1471 px et 758 px de large) puis converties en points logiques. **Calibrage** : la bordure de
carte, documentée à 2 px dans la charte, mesure 4 px sur la capture de 758 → échelle 2 px/pt,
soit une largeur logique de 379 pt (≈ 390). Les deux captures donnent les mêmes valeurs à 2 %
près, ce qui valide l'échelle.

### Couleurs — par rôle, clair et sombre

Aucune teinte nouvelle : toutes sortent de `HUE` dans `lib/ui/palette.ts`.

| Rôle | Clair | Sombre | Provenance | Usage |
| --- | --- | --- | --- | --- |
| `surface` | `#FFFFFF` Snow | `#1A1A1B` | charte / existant | fond de page **et** fond de carte — plus de gris de page |
| `surface-creuse` | `#F7F7F7` Polar | `#202022` | charte | remplissage d'un champ de saisie, piste d'un segmenté |
| `bordure` | `#E5E5E5` Swan | `#3A3A3A` | charte / existant | contour de carte et de champ, **2 px** |
| `arete` | `#E5E5E5` Swan | `#3A3A3A` | relevé | arête basse d'une carte ou d'un bouton neutre |
| `texte` | `#0D0D0D` | `#C8C8C8` | existant | corps et titres |
| `texte-faible` | `#5C5C5C` | `#909090` | existant | libellés secondaires |
| `texte-muet` | `#6B6B6B` | `#8A8A8A` | existant | métadonnées (5,7:1 sur blanc, vérifié) |
| `texte-desactive` | `#AFAFAF` Hare | `#5A5A5C` | charte | libellé d'un contrôle désactivé |
| `action` | `#1CB0F6` Macaw | `#1CB0F6` | charte | sélection, état actif, action neutre |
| `action-arete` | `#1899D6` Whale | `#1899D6` | charte | arête basse du bouton d'action |
| `succes` | `#58CC02` Owl | `#58CC02` | charte | P&L positif, validation, progression |
| `succes-arete` | `#58A700` Tree Frog | `#58A700` | charte | arête basse du bouton de succès |
| `alerte` | `#FF4B4B` Cardinal | `#FF4B4B` | charte | P&L négatif, erreur, destruction |
| `alerte-arete` | `#EA2B2B` Fire Ant | `#EA2B2B` | charte | arête basse du bouton destructif |
| `attention` | `#FF9600` Fox | `#FF9600` | charte | avertissement, tag Short |
| `attention-arete` | `#CD7900` Guinea Pig | `#CD7900` | charte | arête basse |
| `info` | `#CE82FF` Beetle | `#CE82FF` | charte | nouveauté, information |
| `info-arete` | `#9069CD` Betta | `#9069CD` | charte | arête basse |
| `recompense` | `#FFC800` Bee | `#FFC800` | charte | XP, série, jalon |
| `encre-sur-couleur` | `#0D0D0D` | `#0D0D0D` | déduit (§ contrastes) | **tout libellé posé sur un aplat de couleur pleine** |

**Les couples de contraste, vérifiés (WCAG 2.1) — et l'écart assumé avec Duolingo.**

Duolingo pose du **blanc sur ses aplats de couleur**. Ces couples ne passent pas :

- blanc sur Owl `#58CC02` → **2,09:1** — échec même en grand texte
- blanc sur Macaw `#1CB0F6` → **2,44:1** — échec
- blanc sur Fox `#FF9600` → **2,18:1** · blanc sur Bee `#FFC800` → **1,55:1** · blanc sur
  Beetle `#CE82FF` → **2,54:1** — échecs
- blanc sur Cardinal `#FF4B4B` → 3,30:1 — grand texte seulement

**Donc : le libellé posé sur un aplat de couleur pleine est en encre `#0D0D0D`, jamais en blanc.**
C'est un écart délibéré avec la référence, imposé par l'accessibilité, et il reste entièrement
dans la charte :

- encre `#0D0D0D` sur Owl → **9,30:1** (AAA)
- encre `#0D0D0D` sur Bee → **12,51:1** (AAA)

Quand un libellé **doit** être blanc (badge sombre, aplat de nuit), prends le cran foncé de la
famille, pas la principale : blanc sur Narwhal `#1453A3` → **7,51:1** · blanc sur Butterfly
`#6F4EA1` → **6,40:1**.

**La règle n'est pas « toujours l'encre » — elle est conditionnelle, et voici la condition.**
`--color-on-solid` vaut `#FFFFFF` aujourd'hui et est lu par une trentaine d'endroits, dont des
pages hors périmètre ; et surtout **l'accent est un réglage utilisateur libre** — `ACCENT_PRESETS`
de `lib/ui/accent.ts` contient « Charbon & or » à `#232323`, sur lequel l'encre `#0D0D0D` ne rend
que **1,2:1**. Une règle inconditionnelle produirait donc l'inverse du § 9.

Ce que tu fais :

- **Aplats fixes de la charte** (`succes`, `action`, `alerte`, `attention`, `info`, `recompense`) :
  libellé en encre `#0D0D0D`, en dur dans la variante du composant. C'est la table du § 6.
- **Aplat de l'accent utilisateur**, qui peut être n'importe quelle teinte : l'encre se **choisit
  à l'exécution**, en comparant les deux ratios et en gardant le meilleur. `lib/ui/color.ts` porte
  déjà les utilitaires de manipulation de teinte : ajoutes-y une fonction qui rend l'encre lisible
  d'un fond, et sers-t'en. **N'écris pas de seuil arbitraire** : compare encre contre blanc, prends
  le plus contrasté.
- **`--color-on-solid` ne change pas de valeur.** Elle reste `#FFFFFF` et garde ses consommateurs
  existants — dont `T.symbolBadgeText`, un blanc volontaire documenté dans `tokens.ts`. Tu ajoutes
  `--color-encre-sur-couleur: #0D0D0D` à côté, et ce sont les variantes du § 6 qui la lisent.

**Deux autres couples à régler, qui échouent aujourd'hui :**

- **Libellé de navigation actif** : `--color-nav-active-text: var(--accent)` sur
  `--color-nav-active-bg: var(--accent-soft)` (l'accent à 10 % sur blanc) rend environ **2,5:1**
  avec Macaw. → le libellé actif passe par **`deepen()`** de `lib/ui/color` — la fonction existe
  exactement pour ça (« puce, trait, texte, glyphe → `deepen()` / `dotRing()` ») et elle garde la
  teinte en la descendant vers le noir, donc l'accent reste reconnaissable quel que soit le
  réglage de l'utilisateur. L'aplat `--accent-soft`, lui, ne bouge pas.
- **Anneau de focus** : `globals.css` pose `outline: 2px solid var(--color-info)`, c'est-à-dire
  **violet Beetle** — la couleur que le § 5 attribue à l'information. → l'anneau passe à
  `var(--color-action)` Macaw. La mécanique `:focus-visible` (2 px, décalé de 2, clavier
  seulement) ne change pas, seule la couleur change.

**Un nom canonique par rôle.** `--color-danger` et `--color-red` coexistent avec la même valeur :
**`--color-red` est le nom canonique** (c'est celui qui porte le nom de charte, Cardinal), et
`--color-danger` reste comme alias pour ses appelants. N'en crée pas un troisième.

**Interdits de couleur** (mesurés) : Wolf `#777777` sur blanc → 4,48:1, réservé au grand texte
et aux traits — jamais pour du texte courant. Hare `#AFAFAF` ne sert **jamais** de texte sur une
surface claire : 2,19:1 sur blanc, 2,05:1 sur Polar, 1,74:1 sur Swan.

**Le seul cas où Hare est autorisé comme texte est le contrôle désactivé**, et c'est explicite :
WCAG 2.1 exempte de son critère 1.4.3 le texte d'un composant d'interface **inactif**. Un libellé
désactivé Hare sur un fond Polar (2,05:1) est donc conforme parce qu'il est inactif — pas parce
qu'il est lisible. Corollaire à respecter : **un contrôle désactivé ne doit jamais porter la seule
information d'un écran**, et si un texte gris doit rester lisible tout en paraissant secondaire,
c'est `texte-muet` `#6B6B6B` (5,7:1) qu'on prend, jamais Hare. Les huit principales de la charte
rendent 5 à 11:1 sur `#1A1A1B` (Owl 8,33 · Cardinal 5,27 · Macaw 7,11 · Fox 7,96) : **ne crée
aucune version éclaircie pour le thème sombre**, c'est déjà la règle du fichier.

### Typographie

**Familles.** Duolingo emploie **Feather Bold** (display, dessinée par Krista Radoeva chez
Fontsmith, *exclusive à Duolingo — aucune licence tierce possible*) et **Duolingo Sans** (UI,
variable, sur mesure par Bézier Inc.). Les deux sont propriétaires : **elles ne peuvent pas être
utilisées**, et rien de leur dessin ne doit être imité.

Substitut, et il est sourcé par le comportement de Duolingo lui-même : quand Feather Bold ne
couvre pas une langue (russe, ukrainien, vietnamien — 409 points de code seulement), le code de
l'app fait pointer « feather900 » vers **Duolingo Sans en graisse 900**. Autrement dit, la
référence elle-même remplace son display par sa police d'UI poussée en graisse.

→ **tr4de garde Outfit** (déjà en place, Google Fonts, SIL OFL) et crée son rôle display **par la
graisse**, pas par une seconde famille. Concrètement : **pas de `--font-display`** — une custom
property de `font-family` ne transporte pas une graisse, et les rôles typographiques de tr4de
passent par `TYPE` en styles inline, qui n'a pas de champ `fontFamily`. Ce qui change est la
**graisse** des rôles de titre dans `lib/ui/type.ts` (table ci-dessous), plus un
`--fw-display: 800` à côté des `--fw-*` existants de `globals.css` pour la feuille de style. Zéro
police ajoutée, zéro dépendance, zéro token orphelin. La charte nomme par ailleurs **Nunito** (SIL OFL) comme
substitut officiel de sa police de texte : si un jour un vrai display arrondi est voulu, c'est
celle-là et aucune autre — mais **pas dans ce lot**.

**Échelle.** Les dix **tailles** de `lib/ui/type.ts` ne changent pas : elles viennent d'un audit,
elles sont testées (`tests/typeScale.test.ts`), et une app de trading n'a pas la densité d'une app
d'apprentissage. Le rôle `display` **existe déjà** — tu n'ajoutes aucun rôle et aucune taille. Ce
qui change, ce sont les **graisses** et les **interlignes**, et les deux sont sourcés.

*Les interlignes viennent de la charte*, qui donne deux régimes et deux seulement : **100-110 %
pour le display** (Feather Bold) et **140 % pour le texte** (DIN Next Rounded). Appliqués, ils
donnent la colonne ci-dessous — et ils remplacent bien les valeurs actuelles, qui sont un dégradé
continu de 1,0 à 1,4 sans règle.

*Les graisses des rôles de titre* sont **déduites**, par une règle qu'il faut lire en entier : sur
la référence, la hiérarchie d'un écran est portée par une **seconde famille** (le display), pas
par une taille de plus — la charte l'écrit à l'envers (« la police de texte ne doit jamais être
plus grande que Feather Bold quand les deux cohabitent »). tr4de n'a qu'une famille (§ Familles) :
il simule donc cette seconde famille **par la graisse**, et uniquement sur les rôles de titre.

*Les interlettrages ne changent pas* : ce sont ceux de `lib/ui/type.ts`, calculés à l'audit en
fonction de la taille. Aucune raison sourcée de les toucher.

| Rôle | Taille | Graisse | Interligne | Interlettrage | Où |
| --- | --- | --- | --- | --- | --- |
| `display` | 40 | **800** (déduit) | **1,0** (charte) | -0,02em (existant) | le P&L héros du tableau de bord, et lui seul |
| `title1` | 28 | **800** (déduit) | **1,1** (charte) | -0,02em | chiffre héros d'une carte |
| `title2` | 24 | **700** (déduit) | **1,1** (charte) | -0,015em | titre d'écran — un seul par vue |
| `title3` | 20 | **700** (déduit) | **1,1** (charte) | -0,01em | titre de section |
| `headline` | 16 | 500 (existant) | **1,4** (charte) | -0,005em | titre de carte |
| `callout` | 14 | 500 (existant) | **1,4** (charte) | 0 | onglet, ligne à lire d'abord |
| `body` | 13 | 400 (existant) | 1,4 (existant) | 0 | socle : valeur, texte courant |
| `label` | 12 | 500 (existant) | **1,4** (charte) | 0 | libellé de champ, en-tête de tableau |
| `caption` | 11 | 500 (existant) | **1,4** (charte) | 0,005em | légende, unité |
| `caption2` | 10 | 500 (existant) | **1,4** (charte) | 0,01em | axe de graphique |

Quatre rôles gardent donc exactement ce qu'ils ont aujourd'hui en graisse. **Les graisses de
`callout` et de `caption` ne montent pas** : le bouton primaire et le badge posent leur propre
graisse 700 localement (§ 6), parce que c'est la **casse capitale** qui la justifie, pas le rôle.

**Section en capitales.** Relevé sur tous les écrans de la référence : les libellés de section
(« SKILLS ») et les libellés de bouton (« CONTINUE », « REVIEW +20 XP ») sont en **capitales,
graisse 700, et nettement espacés** — en gris pour une section, en encre sur un aplat pour un
bouton. La casse et la graisse sont donc relevées ; **la valeur d'interlettrage, elle, est
déduite : +0,08em**, non mesurée sur les captures. La contrainte qui l'accompagne compte autant
que le chiffre : cette valeur est **la seule** de tout le système, elle ne se décline pas par
taille, et si elle est ajustée elle l'est partout à la fois.

Où la casse capitale s'applique, et sa graisse — la liste est fermée :

- **libellé de bouton primaire** : capitales, graisse **700** ;
- **en-tête de section d'écran** (« STRATÉGIES », « COMPTES ») : capitales, graisse **700**,
  couleur `texte-faible` ;
- **en-tête de colonne de tableau et libellé de `Stat`** : capitales, graisse **500** — et c'est
  une exception assumée à la règle du 700. Une grille dense empile des dizaines d'en-têtes ; à
  700 ils pèsent plus que les chiffres qu'ils annoncent, ce qui est exactement l'inverse de ce
  qu'on veut. La casse et l'interlettrage, eux, sont les mêmes.

Nulle part ailleurs : jamais sur un titre, jamais sur un montant, jamais sur du texte courant. 
**Chiffres.** `TABULAR` (`font-variant-numeric: tabular-nums`) sur tout montant, tout pourcentage
et toute cellule de tableau. Déjà la règle : ne la casse pas.

### Espacement

Unité 4, échelle inchangée : `--space-1` 4 · `-2` 8 · `-3` 12 · `-4` 16 · `-6` 24 · `-8` 32.

Les quatre distances qui font l'allure, relevées puis converties (§ Échelle du relevé) :

- **Gouttière latérale d'écran : 16** (relevé 64,5 px / 1471 = 4,4 % de la largeur). Elle vit dans
  le shell : `components/DashboardNew.jsx` l. 875 pose aujourd'hui `padding: "0 28px …"`, et 28
  n'est pas sur l'échelle. Passe-le à 16, des deux côtés, et sur les deux variantes de la ligne
  (celle de `dashboard` et l'autre).
- **Écart entre deux cartes d'une liste : 8** (relevé 16 px / 758).
- **Padding de carte : 16** (déduit — le cran de la gouttière, pour que le contenu d'une carte
  s'aligne sur la marge de l'écran). Remplace le `padding: 20` actuel de `Card.tsx`.
- **Rythme entre sections : 32** (déduit — le double du padding de carte, cran existant de
  l'échelle).

Jamais deux séparateurs consécutifs : un espace de 24 remplace le second. (Cette règle-là se juge
à l'œil sur les écrans du § 7 — elle n'est pas dans la recette, aucun `grep` ne la mesure.) Un principe livré du
Tab Refresh : « le blanc utilisé volontairement plutôt que des conteneurs forcés » — si un bloc
peut être séparé par du vide, il ne prend pas de carte.

### Rayons, bordures, élévation

**Rayons** — relevé : le CTA plein mesure 42 px de rayon sur 173 px de hauteur (24,3 %), soit
**12 pt** à l'échelle. La famille :

| Rôle | Valeur | Provenance |
| --- | --- | --- |
| `--radius-field` | **8** | déduit (un cran de 4 sous le rayon relevé) — champs, petits chips |
| `--radius-card` | **12** | relevé — cartes, boutons, panneaux |
| `--radius-modal` | **16** | déduit (un cran de 4 au-dessus) — modales, feuilles |
| `--radius-pill` | 999 | inchangé — barre de progression, badges de statut |

Les valeurs actuelles (6 / 10 / 14) montent donc chacune d'un cran.

**Bordures** : **2 px** partout où il y en a une (relevé 4 px / 758 = 2 pt ; la charte documente
« bordures 2 px des cartes »). Couleur `bordure`. Le `1px solid` actuel de `Card.tsx` et de
`Button.tsx` passe à `2px`.

**Élévation — c'est le changement de mécanique central.** Il n'y a **pas d'ombre floue** sur un
élément posé. Un élément posé a une **arête basse en aplat solide**, mesurée :

| Élément | Corps | Arête | Ratio | Provenance |
| --- | --- | --- | --- | --- |
| CTA texte pleine largeur | 44 | **4** | 9,1 % | relevé (88 px / 8 px sur 758) |
| Carte de liste | 52 | **6** | 11,5 % | relevé (104 px / 12 px sur 758) |
| Gros bouton carré (icône) | 40 | **8** | 20 % | relevé (151 px / 30 px sur 1471) |

Règle à coder : `box-shadow: 0 <arête>px 0 <couleur-arête>` — **jamais de flou, jamais de
décalage horizontal**.

Les variables CSS à écrire dans `:root` de `app/globals.css`, avec les valeurs exactes (les
couleurs d'arête colorées sont les mêmes dans les deux thèmes — cf. § Couleurs) :

```css
--color-arete: #E5E5E5;              /* Swan — surfaces neutres. Sombre : #3A3A3A */
--color-arete-action:    #1899D6;    /* Whale      */
--color-arete-succes:    #58A700;    /* Tree Frog  */
--color-arete-alerte:    #EA2B2B;    /* Fire Ant   */
--color-arete-attention: #CD7900;    /* Guinea Pig */
--color-arete-info:      #9069CD;    /* Betta      */

--arete-carte:  0 6px 0 var(--color-arete);
--arete-bouton: 0 4px 0 var(--color-arete);   /* variante neutre ; une variante colorée
                                                 recompose la valeur avec sa propre couleur,
                                                 p. ex. box-shadow: 0 4px 0 var(--color-arete-action) */
```

**Ce que deviennent les tokens actuels.** `--elev-overlay` est **conservé tel quel** (58 sites
d'appel : modales, menus, popovers — ils flottent vraiment, l'ombre floue y est légitime).
`--elev-card` (4 appels), `--elev-pill` (3), `--elev-rest` (8) et `--elev-hover` (10) sont
**supprimés**, et leurs 25 sites d'appel migrés : `--arete-carte` sur une carte ou une pastille
posée, **rien du tout** sur un élément qui ne se soulève plus (les `--elev-hover` de survol
disparaissent sans remplacement — voir la règle de survol des cartes au § 6). Ne laisse aucune
variable définie mais inutilisée, ni aucun appel à une variable supprimée.

**Conséquence sur le fond de page, et ce qu'il ne faut surtout pas faire.** Le gris de page
disparaît **aux deux endroits nommés au principe 1** (`DashboardNew.jsx` l. 815 et 875), qui
passent de `var(--color-bg-subtle)` à `var(--color-bg)`.

**Tu ne changes ni la valeur ni le rôle de `--color-bg-subtle` elle-même.** Elle a une douzaine
d'autres consommateurs hors périmètre (`app/login`, `app/not-found`, `CommandPalette`,
`Skeleton`, `LegalLayout`, `components/charts/*`, `SportPage`…), et surtout **son rôle s'inverse
en thème sombre** : elle y vaut `#0F0F10`, plus **foncé** que les cartes, avec le commentaire
« nav/sidebar — PLUS FONCÉ que les pages ». La repeindre en Polar casserait ces usages et
retournerait le thème sombre.

Le creux de champ reçoit donc **sa propre variable**, nouvelle et sans consommateur historique :

```css
--color-surface-creuse: #F7F7F7;   /* Polar — clair  */
/* dans :root[data-theme="dark"] */
--color-surface-creuse: #202022;   /* sombre */
```

C'est elle que lisent les champs de saisie, la piste d'un segmenté, la boîte d'icône d'un état
vide et le fond d'un bouton désactivé. `--color-bg-subtle` reste ce qu'elle est.

En thème sombre, l'arête reste un aplat : la couleur d'arête neutre est `#3A3A3A`, et les
couleurs d'arête colorées sont **les mêmes qu'en clair** (elles rendent déjà 5 à 11:1 sur
`#1A1A1B`).

**Si l'arête neutre ne se voit pas.** Swan `#E5E5E5` sur blanc ne fait que **1,19:1** : sur la
référence, ce qui rend la carte lisible, c'est la bordure de 2 **et** l'arête de 6 ensemble, pas
l'arête seule. Si à l'écran un bloc ne se détache toujours pas, le repli est nommé et il reste
dans la charte : **Hare `#AFAFAF`** (2,19:1 sur blanc), le neutre suivant. Tu changes alors
`--color-arete` **une fois**, pour tous les blocs — jamais au cas par cas. N'invente aucun gris
intermédiaire.

### Iconographie

`lucide-react` reste — c'est une bibliothèque de traits, là où Duolingo emploie des illustrations
pleines et personnifiées. **Ne cherche pas à imiter les illustrations de la référence** (§ 10).
Règles : trait 2 px (la valeur par défaut de lucide, alignée sur l'épaisseur de bordure), taille
16 dans un bouton `sm`/`md`, 20 dans un bouton `lg`, 20 dans une ligne de liste. Une icône prend
la couleur de son texte, sauf dans une pastille d'état où elle prend `encre-sur-couleur`.

### Densité et layout

Inchangés, et c'est **délibéré** : Duolingo est une app d'apprentissage à un objet par écran,
tr4de affiche des tableaux de trades. Ce qu'on importe est la mécanique de surface, pas la
densité. Concrètement : largeur de barre latérale 220 / 56 repliée, socle de texte 13,
tableaux à leur densité actuelle.

Deux exceptions, imposées par le § 9 :

- **hauteur de bouton 34 → 44** (relevé : 44 corps + 4 arête = 48 total ; l'actuel 34 est sous le
  seuil de cible tactile de 44) ;
- **hauteur de ligne d'une liste cliquable : 52 minimum** (relevé carte de liste). À ne pas
  confondre avec la **ligne de tableau**, qui reste à 44 (§ 6, tableau de trades) : une ligne de
  tableau est une rangée de données dans une grille, une ligne de liste est un bloc posé avec sa
  bordure et son arête. Les deux respectent le seuil de 44.

### Motion

Les durées et les courbes actuelles sont **conservées** — elles sont cohérentes et déjà
tokenisées : `--dur-instant` 100 · `--dur-fast` 150 · `--dur-base` 200 · `--dur-modal` 220 ·
`--dur-slow` 280 ; `--ease-out` `cubic-bezier(0.23,1,0.32,1)` · `--ease-spring`
`cubic-bezier(0.34,1.56,0.64,1)`.

Ce que tu ajoutes, sourcé par relevé sur les médias du dossier :

- **`--dur-celebration: 570ms`** — et il **remplace** les quatre durées de célébration écrites en
  dur dans `globals.css` (`.anim-level-pop` 620 ms, `.anim-bar-flash` 700 ms, `.anim-xp-burst`
  700 ms, `.anim-xp-float` 900 ms), dont trois disparaissent (§ 6, `XpBar`). Mesuré image par
  image sur
  `animations/officiel-label-hard-exercise_duolingo-app.gif` : 17 frames à 30 fps entre
  l'apparition et l'immobilité, avec un pic d'amplitude aux frames 4 à 9 puis décroissance —
  c'est-à-dire un **dépassement puis stabilisation**. Courbe : `--ease-spring`, qui a déjà ce
  profil. Réservé aux moments de récompense : atteinte d'un objectif, série tenue, jalon,
  validation d'un plan de trading. **Un par écran au maximum.**
- **L'enfoncement d'un bouton se joue sur l'arête, pas sur l'échelle.** Relevé : l'arête basse est
  ce qui donne l'effet « touche de clavier ». À l'appui, l'arête passe de sa valeur à `0` et le
  bouton descend d'autant (`transform: translateY(<arête>px)`), en `--dur-instant` 100 ms. Le
  `transform: scale()` actuel disparaît des boutons.

**N'animent jamais** : les tableaux de trades, les montants (hors `CountUp` existant), la
navigation principale, les graphiques au changement de période.

**`prefers-reduced-motion: reduce`** : toutes les durées à 0, aucun déplacement, aucune
célébration — seule l'opacité reste. Le bloc existe déjà dans `globals.css` : étends-le aux
nouveaux tokens plutôt que d'en écrire un second.

## 6. Composants et états

Tous les états, à chaque fois. Les couleurs sont des rôles du § 5.

### Bouton — `components/ui/Button.tsx` + `lib/ui/buttons.ts` + `PillButton` de `components/ui/form.jsx`

Métrique commune (`BTN`) : hauteur de corps **44** (relevé), arête **4** (relevé), rayon **12**
(relevé) — le `borderRadius: 999` actuel disparaît, la pilule n'est plus la forme de bouton, elle
reste celle des badges et de la barre de progression.

Padding **`12px 16px`**, gap **8**, texte `callout` 14/600 : déduits, et par une règle qui les
garde sur l'échelle. Le 16 horizontal est le cran de la gouttière d'écran relevée, ce qui aligne
le texte d'un bouton pleine largeur sur la marge de la page. Le 12 vertical est ce qui reste :
12 + (14 × 1,4) + 12 = 43,6, soit la hauteur de 44 sans la forcer. **Aucune des deux valeurs
n'est hors de l'échelle d'espacement** — c'est la contrainte qui les a choisies. `BTN_PADDING`
passe donc de `"8px 16px"` à `"12px 16px"`. Le bouton primaire est en **capitales,
graisse 700, interlettrage +0,08em**.

Les quatre variantes, chacune = un aplat + son arête :

| Variante | Fond | Libellé | Arête |
| --- | --- | --- | --- |
| `primary` | `action` `#1CB0F6` | `encre-sur-couleur` `#0D0D0D` | `#1899D6` |
| `success` (nouvelle) | `succes` `#58CC02` | `encre-sur-couleur` | `#58A700` |
| `secondary` | `surface` blanc, bordure 2 `bordure` | `texte` | **`#D4D4D4`** (`--color-border-strong`) |
| `ghost` | transparent, pas de bordure | `texte` | aucune |
| `danger` | `alerte` `#FF4B4B` | `encre-sur-couleur` | `#EA2B2B` |

`primary` remplace l'actuel aplat noir `#0D0D0D` : le CTA prend une couleur d'action.
`--color-btn-primary-bg` / `-hover` / `-text` deviennent sans objet — supprime-les avec leurs
appelants, ne les laisse pas pointer dans le vide.

Trois précisions qui évitent trois impasses :

- **L'arête d'un `secondary` n'est pas sa bordure.** Un bouton blanc à bordure `#E5E5E5` et arête
  `#E5E5E5` ne montre aucune épaisseur — l'arête se confond avec le bord. D'où
  `--color-border-strong` `#D4D4D4` (valeur existante) pour l'arête, un cran sous la bordure.
- **`success` est une variante disponible, pas une variante à répandre.** Aucun appelant ne la
  demande aujourd'hui : tu l'ajoutes au type `Variant` et tu la sers **uniquement** là où l'action
  conclut une progression (valider un plan de trading, clore un objectif). Partout ailleurs, le
  CTA est `primary`. Ne convertis aucun bouton existant sans cette raison.
- **`BTN.sm` / `md` / `lg` gardent leurs trois clés et la même métrique**, comme aujourd'hui : seul
  `lg` garde son texte d'un cran au-dessus (`TS.callout` contre `TS.body`). Ne supprime aucune clé,
  des appelants les utilisent.

`ButtonMetrics` (`lib/ui/buttons.ts`) n'a aucun champ pour l'arête : ajoute-lui **`arete: number`**
(le nombre de pixels, pas une chaîne de `box-shadow`), pour que la couleur reste au composant qui
connaît sa variante. C'est le composant qui compose
`boxShadow: \`0 ${BTN.md.arete}px 0 ${couleurArete}\``.

États, pour toutes les variantes :

- **repos** : comme ci-dessus, arête pleine.
- **survol** (pointeur fin uniquement, `hasFinePointer()` existe déjà) : fond mélangé à 8 % vers
  la couleur d'arête, en **`color-mix(in srgb, …)`** — l'espace déjà employé partout dans
  `globals.css`, on n'en introduit pas un second. L'arête ne bouge pas. Pas de `translateY`. Les
  couleurs de survol écrites en dur disparaissent avec cette règle, dont le `#DC2626` de
  `Button.tsx` (un hex qui n'est même pas dans `HUE`).
- **focus visible** : anneau 2 px `action` décalé de 2 — la règle `:focus-visible` de
  `globals.css` s'applique déjà, **ne pose jamais `outline: none`**.
- **pressé** : arête à 0 et `translateY(4px)`, 100 ms `--ease-out`. Le bouton s'enfonce.
- **désactivé** : fond `surface-creuse` `#F7F7F7`, libellé `texte-desactive` `#AFAFAF`, **aucune
  arête**, curseur par défaut. (Relevé : le CONTINUE désactivé de Duolingo est un aplat Swan sans
  arête.) Supprime l'`opacity: 0.55` actuel — il salit la couleur au lieu de la remplacer.
- **chargement** : libellé remplacé par le `Loader2` existant, **largeur figée** pour éviter le
  saut.
- **`ghost`** : pas d'arête, pas de bordure ; au survol, fond `surface-creuse`. **Désactivé, un
  `ghost` reste transparent** — il ne prend pas le fond `surface-creuse` de la règle générale,
  seul son libellé passe en `texte-desactive`. Un `secondary` désactivé, lui, garde sa bordure,
  en `bordure` (pas en `border-strong`).

`BTN_ICON` : carré de 44 × 44, rayon 12 (plus `50%` — un bouton d'icône rond à côté d'un bouton
de texte à rayon 12 fait deux formes), **arête 4 comme tous les boutons**. Le relevé de 8 cité au
§ 5 vient d'un bouton de micro de 40 de côté, qui est un objet plein écran, pas un bouton de barre
d'outils : à 44, c'est 4.

### Carte — `components/ui/Card.tsx`

Fond `surface` blanc, **bordure 2 px** `bordure`, rayon 12, padding 16, arête basse
`0 6px 0 var(--color-arete)`. Le `boxShadow: var(--elev-rest)` disparaît.

- **survol** (si `hoverable`, pointeur fin) : la bordure passe à `--color-border-strong`, l'arête
  ne change pas, **pas de `translateY(-1px)`** — un bloc à arête ne lévite pas, il est posé.
- **pressé** (si cliquable) : arête à 0 et `translateY(6px)`, 100 ms.
- **accent** : le liseré gauche de 3 px actuel passe à **4 px** et prend la couleur du rôle
  (`succes`, `alerte`, `attention`, `info`), pour rester sur la grille de 4.
- La logique de sauvegarde/restauration des valeurs de survol dans `dataset` est correcte :
  garde-la, adapte seulement les valeurs.

### Champ de saisie — `components/ui/form.jsx`, `ComboInput`, `SearchableSelect`, `DateRangePicker`

Fond `surface-creuse` `#F7F7F7` (relevé : Polar est le remplissage des champs, 2,6 % de la
surface), bordure 2 `bordure`, rayon 8, hauteur 44, texte `body` 13, padding horizontal 12.
Pas d'arête sur un champ — un champ est un creux, pas un objet posé.

- **focus** : bordure `action` `#1CB0F6` + anneau `:focus-visible`, fond `surface` blanc.
- **erreur** : bordure `alerte`, message dessous en `caption` `alerte`, **jamais de texte
  d'erreur posé sur un aplat rouge**.
- **désactivé** : fond `surface-creuse`, texte `texte-desactive`.

### Barre de progression — `components/ui/XpBar.tsx`

Relevé sur la référence : hauteur **16**, rayon pilule, piste `bordure` Swan, remplissage `succes`
Owl, pas d'arête, pas de dégradé. Mais ce relevé vient d'une barre qui traverse un écran mobile
entier ; `XpBar` fait aujourd'hui **6** de haut et sert aussi en ligne dans des listes. D'où deux
valeurs, et pas une :

- **barre principale** (l'objet central d'un écran — l'objectif en cours de `DisciplinePage` ou de
  `LifeRpgPage`) : hauteur **16**, valeur relevée.
- **barre en ligne** (dans une ligne de liste, une carte de statistique) : hauteur **6**,
  inchangée — la monter ferait exploser la densité des listes.

Le reste est commun aux deux, et vient du relevé : rayon 999 (c'est, avec les badges, le seul
composant qui garde la pilule), aucune arête, aucun dégradé. La transition de largeur actuelle
(`--dur-slow`) ne change pas.

Deux points de plomberie, à ne pas manquer :

- **`fillColor` et `trackColor` sont des props**, pas des tokens : c'est l'appelant qui décide.
  Tu ne supprimes pas les props (elles servent à colorer une barre par catégorie) ; tu leur donnes
  **`succes` et `bordure` comme valeurs par défaut**, et tu ajustes l'unique appelant,
  `components/pages/LifeRpgPage.jsx`, s'il passe autre chose sans raison.
- **`XpBar` déclenche aujourd'hui plusieurs célébrations à la fois** (`.anim-level-pop` 620 ms,
  `.anim-bar-flash` 700 ms, `.anim-xp-burst` 700 ms, `.anim-xp-float` 900 ms, toutes définies dans
  `globals.css`). C'est exactement ce que le § 14 interdit. → **n'en garde qu'une**, celle du
  passage de niveau, retimée à `--dur-celebration` 570 ms avec `--ease-spring` ; supprime les
  trois autres avec leurs `@keyframes` et leurs classes. Une célébration, un élément, un moment.

### Barre d'onglets et navigation — `components/ui/TabBar.tsx`, `components/ui/Sidebar.tsx`, `components/ui/Navigation.jsx`

Item actif : fond `--accent-soft`, libellé `--accent` (mécanique existante, à conserver — l'accent
est réglable par l'utilisateur). Rayon 12 — `TabBar.tsx` l'a déjà, la sidebar et la nav doivent
s'aligner dessus. Hauteur **44** (`TabBar` est à 38 aujourd'hui : c'est sous le seuil du § 9).
**Ne pose aucune arête sur un item de navigation** : la nav est une surface, pas un objet.
Survol : `--color-nav-hover-bg`, inchangé.

**Le défaut de `--accent` passe à `#1CB0F6` Macaw** (charte). L'actuel `#64D741` / `#4CC72C` est
la seule couleur de l'app qui ne vient pas de la charte : garde-le comme préréglage nommé dans
`lib/ui/accent.ts`, au même titre que « Violet (d'origine) », mais ne le sers plus par défaut.

### Feuille et modale — `components/ui/Sheet.tsx`, `components/ui/Popover.tsx`, `components/modals/`

Rayon 16, fond `surface`, `--elev-overlay` (l'ombre floue est légitime ici : ça flotte
vraiment), voile `--color-scrim` inchangé. Entrée `--dur-modal` 220 ms depuis le bas,
`--ease-drawer`. Bordure 2 en haut seulement si la feuille touche un bord.

### État vide — `components/ui/EmptyState.tsx`

Composition relevée sur les écrans de la référence : un visuel, un titre court, une phrase, un
seul bouton. Le composant a **déjà** cette structure et ses tailles sont bonnes (boîte d'icône
36/44/56, icône 18/22/28, titre 14/16/18, description 13) : **ne les change pas**. Trois
retouches seulement :

- `strokeWidth` de l'icône passe de `1.75` à **2** (l'épaisseur de trait du § 5) ;
- le bouton d'action passe de `variant="secondary" size="sm"` à **`variant="primary" size="md"`** —
  un état vide propose une action, il ne la range pas au second plan ;
- la boîte d'icône prend le fond `surface-creuse` et le rayon 12, sans arête.

Pas d'illustration, pas de personnage (§ 10). Voir § 8 pour le ton du titre et de la phrase.

### Carte de statistique — `components/ui/Stat.tsx`

Elle hérite de `Card` : bordure 2, rayon 12, padding 16, `--arete-carte`. Le libellé passe en
`label` 12/500 capitales `texte-faible` interlettrage +0,08em ; la valeur garde son cran actuel
et son `tabular-nums` ; la tendance prend `succes` ou `alerte`. La variante `flat` (plusieurs
`Stat` dans un conteneur commun) ne porte **ni bordure ni arête** — c'est le conteneur qui les
porte. Le `CountUp` existant reste, c'est le seul chiffre animé de l'app.

### Badge et pastille de statut

Rayon 999 (la pilule reste ici), hauteur 24, padding `4px 8px`, texte à la taille de `caption`
(11) mais en **graisse 700 posée localement** — le rôle `caption` reste à 500 (§ 5), c'est la
casse capitale du badge qui justifie la graisse, pas le rôle. Capitales, interlettrage +0,08em. Fond = la principale diluée à 12 % (`--color-*-bg`, mécanique
existante), texte = la principale brute. **Pas d'arête sur un badge.**

### Tableau de trades — `components/ui/tradesList.jsx`, `components/TradesManager.jsx`

En-têtes en `label` 12/500 capitales `texte-faible`, interlettrage +0,08em. Lignes de 44 de haut.
Séparateur : 1 px `bordure` (pas 2 — un séparateur de tableau n'est pas un contour de bloc).
Ligne survolée : `--color-row-highlight`, inchangé. **Aucune arête, aucune ombre dans un
tableau.** Montants en `tabular-nums`, positifs `succes`, négatifs `alerte`.

## 7. Écran par écran

Six écrans pilotes. Les autres pages de `components/pages/` héritent des primitives et **ne
sont pas retouchées dans ce lot**.

1. **`components/pages/DashboardPage.jsx`** + **`components/DashboardNew.jsx`** (le shell) — le P&L héros passe en `display` 40/800. Les cartes de KPI prennent
   bordure 2 + arête 6 et perdent leur ombre. Le fond de page passe au blanc : vérifie que les
   cartes restent lisibles une fois le shell passé au blanc (c'est le test du principe 1 ; si ça
   ne tient pas, la réponse est le repli d'arête nommé au § 5 — Hare `#AFAFAF` — appliqué une
   fois pour tous les blocs, **pas** un retour du gris de page). Le
   calendrier P&L garde ses aplats dilués actuels.
2. **`components/pages/TradesPage.jsx`** — tableau : voir § 6. C'est l'écran qui prouve que la densité survit à la
   nouvelle mécanique : rien ne doit grossir sauf la hauteur de ligne.
3. **`components/pages/LifeRpgPage.jsx`** — l'écran où la référence apporte le plus, parce qu'il
   est déjà gamifié et qu'il est **le seul appelant de `XpBar`**. Barre principale à 16, pilule,
   `succes` ; série et XP en `recompense` Bee ; une célébration `--dur-celebration`, et une seule,
   sur l'atteinte d'un objectif. **Pas de mascotte, pas de personnage** (§ 10).
4. **`components/pages/DisciplinePage.jsx`** — même famille, mais **il n'y a aucune barre de
   progression dans ce fichier** : ne va pas en chercher une. Ce qui s'y applique est le socle —
   cartes à bordure 2 et arête 6, boutons 44, capitales de section, titre d'écran à la même place
   que sur les quatre autres.
5. **`components/pages/SettingsPage.jsx`** — listes de réglages en lignes de 52, bordure 2, arête 6, un seul titre
   d'écran. C'est le contrôle du principe 5 : le titre au même endroit que sur les quatre autres.
6. **`components/LandingPage.jsx`** (hors `components/pages/`) — le seul écran public. CTA `primary` Macaw, encre `#0D0D0D` dessus, et
   **rien du lexique visuel de Duolingo** : ni hibou, ni vert de marque en aplat plein cadre, ni
   copie de sa mise en page.

## 8. Contenu et ton

Tu ne réécris **pas** le contenu métier. Tu ajustes uniquement la microcopie des **états vides**,
des **messages d'erreur** et des **libellés de bouton**.

Ce que la référence fait, relevé : elle **annonce et minimise l'engagement** (« Just 7 quick
questions before we start »), elle **nomme le bénéfice dans le bouton** (« REVIEW +20 XP » plutôt
que « Continuer »), et son ton est encourageant sans être puéril.

Règles :

- **Libellé de bouton** : verbe à l'infinitif, 1 à 3 mots, en capitales pour le bouton primaire.
  Quand une action rapporte quelque chose de chiffré, le chiffre est dans le libellé.
- **État vide** : une phrase qui dit quoi faire, pas ce qui manque. « Aucun trade enregistré »
  devient « Enregistre ton premier trade pour voir tes statistiques ».
- **Erreur** : ce qui s'est passé + ce qu'on peut faire. Jamais de code technique visible.
- **Tutoiement**, comme le reste de l'app. Français correct, accents compris.
- **Interdits de ton** : « Oups », le point d'exclamation, le jargon (« payload », « token »,
  « sync »), et **toute imitation de la voix de marque de la référence** (§ 10).
- **Pas d'emojis.**

## 9. Accessibilité

Non négociable et vérifiable :

- **Contrastes** : les couples du § 5 sont déjà mesurés. Tout libellé sur aplat de couleur pleine
  est en encre `#0D0D0D`. Aucun texte de métadonnée sous 4,5:1.
- **Cibles tactiles ≥ 44 px** : c'est pourquoi la hauteur de bouton passe de 34 à 44 et
  `BTN_ICON` à 44 × 44. Vérifie aussi les boutons d'icône des barres d'outils de tableaux.
- **Focus visible** sur tout élément atteignable au clavier, y compris les cartes cliquables et
  les lignes de tableau. `:focus-visible` existe : ne le neutralise nulle part.
- **`prefers-reduced-motion`** : aucune célébration, aucun déplacement, aucun enfoncement de
  bouton — seule l'opacité.
- **L'arête n'est jamais le seul porteur d'une information** : elle est décorative. Un état se lit
  aussi au libellé ou à la couleur du texte.
- Le socle de texte reste à 13 px : c'est la densité assumée d'un outil de trading, et
  `app/globals.css` expose l'échelle en `rem`, donc elle suit le réglage système de
  l'utilisateur. Ne repasse pas les tailles en pixels figés dans la feuille de style.

## 10. Interdits

**Anti-pastiche** — la marque de tr4de reste celle de tr4de :

- Aucune mascotte, aucun personnage, aucun hibou, aucune illustration inspirée de la référence.
- Aucun logo, aucun wordmark, aucun élément d'identité de la référence.
- **Aucune fonte propriétaire** : ni Feather Bold, ni Duolingo Sans, ni imitation de leur dessin
  (les terminaisons en bec, le `g` à lunettes). Outfit en 800 est le rôle display, point.
- Aucun système de gamification copié tel quel (couronnes, ligues, cœurs, flamme de série
  dessinée comme la sienne). tr4de a déjà ses objets — `XpBar`, `LifeRpgPage`, `DisciplinePage` :
  tu les habilles, tu n'en importes pas d'autres.
- Aucune reprise de sa voix de marque ni de ses formules.

**Anti-dérive** :

- **Aucune dépendance ajoutée**, aucune police téléchargée, aucun fichier de config créé.
- **Aucune nouvelle teinte.** Les couleurs d'état, de catégorie et d'accent sortent toutes de
  `HUE` dans `lib/ui/palette.ts`. Les **neutres** — `#FFFFFF`, l'encre `#0D0D0D`, les gris de
  texte `#5C5C5C` / `#6B6B6B`, et les gris sombres `#1A1A1B` / `#202022` / `#3A3A3A` / `#C8C8C8` —
  ne sont **pas** dans `HUE` et n'ont pas à y entrer : ce sont ceux de `globals.css`, tu les
  reprends tels quels. Ce que la règle interdit, c'est d'**inventer une teinte de plus**, pas
  d'utiliser les neutres qui existent.
- Aucune nouvelle taille de texte : les dix crans de `lib/ui/type.ts` sont fermés.
- Aucun renommage de fichier, de composant, de route.
- Aucune retouche des 32 pages non citées au § 7.
- Aucune valeur en dur : ni hex, ni px de texte, ni hauteur de bouton hors des tables existantes.
- Pas de « tant que j'y suis » : pas de refactor, pas de migration, pas de nettoyage annexe.

## 11. Plan d'exécution

Un commit par lot, dans cet ordre — les tokens d'abord, sinon tu styles des composants avec des
valeurs que tu changeras ensuite.

1. **Tokens** (`app/globals.css`) : rôles de couleur clair + sombre, `--arete-*` en remplacement
   de `--elev-card` / `--elev-pill` / `--elev-rest` / `--elev-hover`, rayons 8/12/16/999, fond de
   shell au blanc (`DashboardNew.jsx` l. 815 et 875), `--color-surface-creuse`,
   `--color-encre-sur-couleur`, `--dur-celebration`, `--fw-display`, anneau de focus en
   `--color-action`. Répercute dans `lib/ui/tokens.ts`.
2. **Métriques** : `lib/ui/buttons.ts` (44 + arête 4, rayon 12, `BTN_ICON` 44 carré, champ
   `arete` dans `ButtonMetrics`, `BTN_PADDING` en `"12px 16px"`) et, dans `lib/ui/type.ts`, les
   **graisses et interlignes** de `TYPE` selon la table du § 5 — aucune taille ne bouge, aucun
   rôle n'est ajouté. `tests/typeScale.test.ts` doit rester vert.
   **`tests/buttonMetrics.test.ts` passe au rouge à la fin de ce lot, et c'est attendu** : il ne
   redeviendra vert qu'au lot 4. C'est la seule fenêtre où un test est légitimement rouge, et
   elle se ferme dans le même run.
3. **Primitives**, tous les états du § 6 : `components/ui/Button.tsx`, `Card.tsx`, `form.jsx`
   (`PillButton`, champs), `TabBar.tsx`, `Sidebar.tsx`, `Navigation.jsx`, `Sheet.tsx`,
   `Popover.tsx`, `EmptyState.tsx`, `XpBar.tsx`, `Stat.tsx`.
4. **Substitution des métriques de bouton**, dans son propre commit et rien d'autre dedans :
   les ~247 emplacements des ~41 fichiers passent de leurs valeurs en dur à un étalement de
   `BTN.*` (§ 2). Le lot est fini quand `npx vitest run tests/buttonMetrics.test.ts` est vert.
   Si tu ne peux pas le finir, **arrête-toi et dis-le** : ne remets pas `BTN_HEIGHT` à 34 pour
   faire passer le test, et ne touche pas au test.
5. **Écrans pilotes**, dans l'ordre du § 7.
6. **Motion** : enfoncement à l'arête, `--dur-celebration`, suppression des trois célébrations
   surnuméraires, extension du bloc `prefers-reduced-motion`.
7. **Recette** (§ 12) et corrections.

## 12. Recette

Chaque ligne est vraie ou fausse.

- `grep -rn -- "--elev-card\|--elev-pill\|--elev-rest\|--elev-hover" app/ components/ lib/` → vide (les 25 sites d'appel sont migrés, les 4 variables supprimées).
- `grep -rn -- "--elev-overlay" app/ components/ lib/ | wc -l` → toujours 58 (les calques flottants n'ont pas bougé).
- Aucune `box-shadow` avec un rayon de flou hors `--elev-overlay` : `grep -rn "boxShadow\|box-shadow" components/ app/globals.css | grep -v "elev-overlay\|arete-\|0 [0-9]*px 0"` → vide.
- `npx vitest run tests/buttonMetrics.test.ts` → vert, sans que le test ait été modifié
  (`git diff tests/` → vide).
- `grep -rn "borderRadius: 999" components/ | wc -l` → a **fortement baissé** (il y en a environ
  304 aujourd'hui, presque tous des boutons). Les seuls qui restent sont `XpBar`, les badges et
  les pastilles de statut ; un bouton en pilule qui subsiste est un oubli du lot 4.
- `grep -rn -- "--color-btn-primary" app components lib` → vide (la variante `primary` a une
  couleur d'action, plus un aplat noir).
- `grep -rn "outline: 2px solid var(--color-info)" app/globals.css` → vide (l'anneau de focus est
  passé à `--color-action`).
- `grep -n "anim-bar-flash\|anim-xp-burst\|anim-xp-float" app/globals.css components/ui/XpBar.tsx` → vide.
- **Pas de régression sur les valeurs en dur.** L'app en porte aujourd'hui, hors de ce
  périmètre, un stock connu : **315** hex sur des lignes sans `var()`
  (`grep -rn '#[0-9a-fA-F]\{6\}' app components --include='*.tsx' --include='*.jsx' | grep -v 'var(--' | wc -l`,
  dont **206** dans `components/ui/`) et **1 529** tailles de texte en dur
  (`grep -rn 'fontSize: [0-9]' components | grep -v 'TS\.\|TYPE\.' | wc -l`). Ces deux
  compteurs doivent **baisser ou rester égaux**, jamais monter. Ne pars pas les résorber :
  c'est hors périmètre (§ 2).
- **Dans les fichiers que tu as touchés**, en revanche, le compte est à zéro :
  `git diff --name-only | grep -E '\.(tsx|jsx)$' | xargs grep -n '#[0-9a-fA-F]\{6\}' | grep -v 'var(--'` → vide,
  et le même enchaînement avec `'fontSize: [0-9]'` filtré de `TS\.`/`TYPE\.` → vide.
- `grep -n "bg-subtle" app/globals.css` → `--color-bg-subtle` vaut `#F7F7F7` et n'est plus le fond de page (`--color-bg` = `#FFFFFF`).
- `grep -n "minHeight\|BTN_HEIGHT" lib/ui/buttons.ts` → `BTN_HEIGHT` vaut 44.
- Thème sombre : chaque rôle du § 5 est redéfini ou hérité explicitement ; aucune couleur n'est définie **seulement** dans le bloc sombre.
- Aucun libellé blanc posé sur Owl, Macaw, Fox, Bee ou Beetle (recherche visuelle sur les cinq écrans pilotes).
- Au clavier : chaque bouton, carte cliquable et ligne de tableau reçoit un anneau de focus visible.
- Au doigt : aucun élément interactif sous 44 px de haut.
- `prefers-reduced-motion` activé dans les préférences système : plus aucun déplacement ni célébration, l'app reste utilisable.
- `npm run lint:strict` → 0 erreur, 0 warning. `npm run test` → vert.
- `git diff package.json` → vide.

## 13. Visuels d'appui

Fichiers **locaux** : si tu tournes ailleurs que sur cette machine, demande qu'ils soient joints.

- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/duolingo-app/ecrans/feature-practice-hub-2026-onglet-entrainement.png`
  — **le visuel le plus important** : c'est de lui que sortent l'arête basse (CTA 88/8 px), la
  bordure de 2 et la carte de liste 104/12. Regarde comment les cartes de la liste sont *posées*.
- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/duolingo-app/ecrans/exercice-09-speak-this-sentence-micro-bleu.png`
  — le bouton désactivé (aplat Swan, libellé Hare, **aucune arête**) et l'arête Whale sous le
  bouton Macaw. Le blanc qui tient tout l'écran.
- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/duolingo-app/couleurs/palette-relevee-interface-de-lecon.svg`
  — les parts de surface réelles : le blanc à 82,6 %, le bleu quatre fois plus présent que le
  vert. C'est la justification des principes 1, 3 et 4.
- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/duolingo-app/ecrans/planches/planche-exercices-duolingo.png`
  — les 14 exercices : le même châssis, seule la zone du milieu change. Le modèle de constance
  qu'on vise entre les 37 pages de tr4de.
- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/duolingo-app/composants/headers-espacement-nettoye_duolingo-app.png`
  — les règles de header livrées par le Tab Refresh (principe 5).
- `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/duolingo-app/animations/officiel-label-hard-exercise_duolingo-app.gif`
  — la source de `--dur-celebration` : 570 ms, dépassement puis stabilisation.
- `/Users/account/Documents/brain^2/INSPIRATION/UNIVERS/duolingo/couleurs/palette-teintes-completes.svg`
  — les 38 teintes de la charte avec leurs noms. Le référentiel de `lib/ui/palette.ts`.

## 14. Décisions laissées à l'agent

Chacune avec sa contrainte. Ce sont des trous assumés, pas des oublis.

- **Durées de micro-transition d'UI** (survol, changement d'état, ouverture de menu) : les médias
  du dossier ne contiennent que des célébrations de 2,5 à 10 s, pas de micro-transitions
  mesurables. → **garde les durées actuelles de tr4de** (100 / 150 / 200 / 220 / 280 ms), qui
  sont cohérentes. N'en invente pas d'autres.
- **Iconographie** : la référence emploie des illustrations pleines, non transposables à une
  bibliothèque de traits et de toute façon interdites (§ 10). → garde `lucide-react` avec les
  règles du § 5. Si un écran a besoin d'un visuel, c'est une icône agrandie, pas une
  illustration.
- **Élévation des menus déroulants et popovers** : la référence ne documente pas ce cas (elle
  n'a presque pas de menus). → garde `--elev-overlay` tel quel, sans l'accentuer.
- **Thème sombre des aplats de couleur** : la maquette Figma d'origine de tr4de ne couvre que le
  clair, et la référence n'a pas de nuancier sombre publié. → applique la règle déjà écrite dans
  `globals.css` : une seule valeur par couleur dans les deux thèmes, puisque les principales
  rendent 5 à 11:1 sur `#1A1A1B`.
- **Ampleur de la célébration** (ce qui bouge exactement pendant les 570 ms) : non transposable
  depuis un personnage animé sous Rive. → une seule propriété animée (échelle **ou** opacité),
  jamais un déplacement d'écran, jamais plus d'un élément à la fois.
- **Le préréglage d'accent par défaut** : passer `--accent` de `#64D741` à Macaw `#1CB0F6` est le
  choix de charte, mais c'est un réglage utilisateur visible. → applique-le comme **valeur par
  défaut** et conserve l'ancien comme préréglage nommé ; ne touche pas à un accent déjà choisi
  par un utilisateur existant.
