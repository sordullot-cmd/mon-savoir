# Le squelette du prompt de refonte

À lire à l'**étape 6**, une fois la source lue, la cible relevée et l'écart posé.

Le fichier produit est une **note du vault** (donc frontmatter + provenance) qui contient
**un prompt à copier tel quel**. Les deux parties sont séparées nettement : Sacha doit
pouvoir sélectionner le prompt sans emporter la métadonnée.

---

## Partie 1 — l'enveloppe (la note)

```yaml
---
type: prompt-refonte
source: <slug-source>          # le dossier de DA dont ce prompt est tiré
cible: <nom de la cible>       # site, app, ou projet
cible_url:                     # URL ou chemin du dossier de code, si applicable
destination: agent-de-code     # ce prompt est écrit pour Claude Code / Cursor
axes: [couleurs, typo, spacing, motion, composants, ...]   # ce qu'il couvre vraiment
axes_ouverts: [elevation]      # ce qu'il laisse décider à l'agent
date: 2026-08-21
tags: [prompt, refonte, da]
---
```

Puis, avant le prompt, **cinq lignes maximum** : ce que ce prompt fait, d'où viennent ses
valeurs (`[[<slug-source>]]`), et l'état de la cible au moment de l'écriture. Ensuite une
ligne de séparation explicite, du genre :

```
## Le prompt — tout ce qui suit est à copier
```

---

## Partie 2 — le prompt, section par section

Ordre imposé. Une section vide est **supprimée**, jamais laissée en titre creux — sauf
« Interdits » et « Recette », qui ne sont jamais vides.

### 1. Mission

Trois phrases : qui l'agent est, ce qu'il transforme, ce qu'il rend. La source de DA est
nommée **comme référence de système, pas comme modèle à cloner**.

> Tu refonds l'interface de `<cible>` (`<stack>`) pour l'aligner sur une direction
> artistique précise, décrite intégralement ci-dessous. Tu ne changes ni le contenu, ni les
> routes, ni la logique métier. Tu rends un diff qui passe le lint et la recette de la
> dernière section.

### 2. Périmètre

Deux listes courtes et fermées. **Ce qu'on ne touche pas** est la plus importante : sans
elle, un agent de code réécrit l'application.

> **Tu changes** : tokens de style, composants d'UI, espacements, motion, thème sombre.
> **Tu ne touches pas** : textes et contenus, routes et URLs, logique métier, schéma de
> données, dépendances (aucun ajout de librairie), fichiers de config hors style.

### 3. État actuel

Le relevé de l'étape 2, factuel : stack, système de style, **où vivent les tokens**
(chemin exact), gestion du thème, ce qui existe déjà de bien et doit survivre.

> Tokens actuels : `src/styles/tokens.css` (variables CSS sur `:root`, thème sombre en
> `[data-theme="dark"]`). Composants dans `src/components/ui/`. Tailwind absent.
> À conserver : la structure de la navigation, déjà correcte au clavier.

### 4. La direction artistique

Une phrase qui tient, puis **cinq principes maximum**, chacun suivi de sa conséquence
concrète. Un principe sans conséquence est décoratif.

> **Direction** : la densité d'un outil financier avec le calme d'un écran de lecture —
> beaucoup d'information, très peu d'ornement.
>
> 1. **La surface porte la hiérarchie, pas l'ombre.** → aucune `box-shadow` sur les
>    cartes : on sépare par un aplat plus clair et une bordure 1 px.
> 2. **Un seul accent.** → le bleu ne sert qu'aux actions primaires et à l'état actif ;
>    jamais en décoration, jamais deux accents dans un écran.
> …

### 5. Le système

Le cœur. Chaque bloc donne des **valeurs**, et chaque valeur porte sa **provenance**
(`charte`, `relevé`, `déduit` — cf. règle fondatrice du SKILL).

**Couleurs — par rôle, clair et sombre.** Une palette sans rôles ne se code pas.

| Rôle | Clair | Sombre | Provenance | Usage |
| --- | --- | --- | --- | --- |
| `surface` | `#FFFFFF` | `#191F28` | charte | fond de page |
| `surface-elevee` | `#F2F4F6` | `#202632` | charte | cartes, feuilles modales |
| `texte` | `#191F28` | `#F2F4F6` | charte | corps et titres |
| `texte-faible` | `#4E5968` | `#8B95A1` | relevé | légendes, métadonnées |
| `accent` | `#0064FF` | `#3182F6` | charte | action primaire, état actif |
| `bordure` | `#E5E8EB` | `#2A313C` | relevé | séparateurs, contours de champ |

Sous le tableau, les couples vérifiés au contraste (étape 5) et les **interdits de
couleur** : « `texte-faible` sur `accent` : 1.6:1, jamais ».

**Typographie.** Famille + fallback + licence, puis l'échelle complète : niveau, taille,
graisse, interligne, interlettrage, et **où il sert**.

> Titres et corps : `Inter` (SIL OFL) — substitut assumé de la police maison de la
> référence, non redistribuable. Chiffres en **variante tabulaire** partout où un montant
> peut changer (`font-variant-numeric: tabular-nums`).
>
> `display` 32/1.2/-0.02em semi-bold — titre d'écran, un seul par vue
> `titre` 20/1.3/-0.01em semi-bold — en-tête de carte
> `corps` 16/1.5/0 regular — texte courant, et minimum absolu pour tout texte lisible
> `legende` 13/1.4/0 regular en `texte-faible` — métadonnées

**Espacement.** L'unité, l'échelle, et les 3 ou 4 distances qui font l'allure.

> Unité 4. Échelle utilisée : 4, 8, 12, 16, 24, 32, 48, 64.
> Padding de carte 20. Gouttière entre cartes 12. Rythme entre sections 48.
> Jamais deux séparateurs consécutifs : un espace de 24 remplace le second.

**Rayons, bordures, élévation.** Par famille de composant. Si la source ne documente pas
l'élévation, le dire ici et fixer la règle de repli.

**Iconographie et illustration.** Style de trait, grille, taille, remplissage ; et ce
qu'on fait si la cible n'a pas d'illustrations.

**Densité et layout.** Largeur max de contenu, colonnes, bascule mobile, densité des
listes, position de la navigation.

**Motion.** Chiffré, avec ce qui **ne** s'anime pas.

> Entrée d'élément 220 ms `cubic-bezier(0.2, 0, 0, 1)` · sortie 160 ms `ease-in` ·
> feuille modale 320 ms depuis le bas · changement d'état 120 ms.
> N'animent jamais : les tableaux de chiffres, la navigation principale.
> `prefers-reduced-motion: reduce` → toutes les durées à 0, aucun déplacement, seule
> l'opacité reste autorisée.

### 6. Composants et états

Un bloc par composant touché, avec **tous** ses états : repos, survol, focus visible,
pressé, désactivé, chargement, vide, erreur. C'est la moitié du travail réel, et c'est
toujours ce qui manque dans un prompt bâclé.

> **Bouton primaire** — fond `accent`, texte `#FFFFFF`, hauteur 48, rayon 12, padding
> horizontal 20, `corps` semi-bold. Survol : `accent` assombri de 8 %. Focus : anneau 2 px
> `accent` décalé de 2 px, **jamais `outline: none`**. Pressé : échelle 0.98, 120 ms.
> Désactivé : `surface-elevee` + `texte-faible`, curseur par défaut. Chargement : libellé
> remplacé par un indicateur, largeur figée pour éviter le saut.

### 7. Écran par écran

Pour chaque écran ou page de la cible : ce qui change, ce qui reste, et le cas particulier
qui ne se déduit d'aucune règle. C'est ici qu'on cite les visuels d'appui.

### 8. Contenu et ton

La refonte touche la microcopie même quand elle ne touche pas le contenu : libellés de
boutons, états vides, messages d'erreur. Longueur, capitalisation, personne, interdits
(« Oups », le point d'exclamation, le jargon).

### 9. Accessibilité

Non négociable, et vérifiable : contrastes déjà validés (rappeler les seuils), focus
visible sur tout élément atteignable au clavier, cibles tactiles ≥ 44 px, ordre de
tabulation, `prefers-reduced-motion`, texte jamais sous 16 px pour le corps.

### 10. Interdits

Jamais vide. Deux familles :

- **Anti-pastiche** : ne pas copier le logo, le nom, la mascotte, les illustrations ni les
  fontes propriétaires de la référence ; la marque de la cible reste la sienne.
- **Anti-dérive** : pas de nouvelle dépendance, pas de refonte du contenu, pas de
  renommage de fichiers ou de routes, pas de « tant que j'y suis ».

### 11. Plan d'exécution

Par lots, dans l'ordre, un commit par lot. Les tokens d'abord — sinon l'agent style des
composants avec des valeurs qu'il va changer ensuite.

> 1. Tokens (`tokens.css`) : rôles clair + sombre, échelle typo, spacing, rayons.
> 2. Primitives : bouton, champ, carte, liste — tous les états.
> 3. Écrans, dans l'ordre de la section 7.
> 4. Motion et `prefers-reduced-motion`.
> 5. Passe de recette (section 12) et corrections.

### 12. Recette

Une checklist que Sacha déroule à l'œil ou en commande. Chaque ligne est **vraie ou
fausse**, jamais « ça rend mieux ».

> - Aucune valeur de couleur en dur hors du fichier de tokens (`grep -rn "#[0-9a-fA-F]\{6\}" src/ --include=*.tsx` → vide).
> - Thème sombre : chaque rôle redéfini, aucune couleur définie seulement dans le bloc sombre.
> - Focus visible sur tous les éléments interactifs, au clavier uniquement.
> - Aucun texte de corps sous 16 px.
> - `prefers-reduced-motion` : plus aucun déplacement.
> - Aucune dépendance ajoutée (`git diff package.json` → vide).

### 13. Visuels d'appui

5 à 8 chemins **absolus** vers les visuels les plus parlants du dossier source, chacun
avec une ligne disant **ce qu'il faut y regarder**. Plus la mention que ces fichiers sont
locaux : si l'agent tourne ailleurs, il faut les joindre.

> `/Users/account/Documents/brain^2/INSPIRATION/UI-DESIGN/toss/ecrans/planches/planche-accueil.png`
> — la densité visée : beaucoup de lignes, aucune ombre, séparation par surface.

### 14. Décisions laissées à l'agent

Les trous assumés, chacun avec sa **contrainte**. Une liste franche ici vaut mieux qu'une
valeur inventée ailleurs.

> Élévation des menus déroulants : non documentée par la référence. Garder l'ombre
> actuelle, sans l'accentuer.

---

## Le test du prompt, avant de livrer

Six questions. Une réponse « non » se corrige, elle ne se justifie pas.

1. Un agent qui n'a **jamais vu** la référence peut-il exécuter chaque ligne ?
2. Chaque valeur chiffrée porte-t-elle sa provenance, et aucune n'est-elle inventée ?
3. La section « ce qu'on ne touche pas » est-elle là, et fermée ?
4. Tous les états de composant sont-ils écrits, pas seulement le repos ?
5. La recette est-elle **vérifiable** ligne par ligne ?
6. Reste-t-il un adjectif seul (« moderne », « épuré », « premium ») sans conséquence
   concrète ? Alors il est à traduire ou à supprimer.

Et la règle de longueur : **un prompt long est bon, un prompt qui se répète ne l'est pas.**
Si deux sections disent la même chose, la valeur vit dans « Le système » et les autres y
renvoient.
