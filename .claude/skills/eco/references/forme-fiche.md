# La forme d'une fiche de révision — exemples pris dans les vraies pages

À lire **avant** de toucher une page. Les avant/après ci-dessous viennent de
`eco gestion/`, pas d'un exemple inventé.

---

## Les six blocs, dans cet ordre

Une page d'éco gestion qui se révise a toujours cette anatomie. Un bloc absent
se crée **à partir du contenu de la page** ; un bloc déjà là ne se refait pas.

1. **Frontmatter** — `tags`, `statut`, et les champs propres à la page
   (`notion`, `prerequis`, `nb_cartes`, `modules`…). Intouchables sauf `statut`.
2. **Titre + ligne de contexte** — `# 📊 Cours — Indices et déflation`, puis la
   ligne des liens : module, durée, série d'exercices, retour au hub.
3. **`> [!abstract] L'essentiel`** — 3 à 6 lignes, la fiche dans la fiche.
   Uniquement des phrases dérivées du corps. C'est ce qu'on relit à J-1.
4. **Le corps du cours** — préservé. On corrige la langue et la structure, on ne
   réécrit pas l'explication.
5. **`> [!warning] Les pièges`** — les erreurs classiques **déjà dites** dans la
   page, remontées en un seul endroit.
6. **`## ✅ Contrôle`** — les questions de restitution, chacune avec le lien vers
   l'endroit de la page qui répond. Jamais de réponse inventée.

Et, seulement s'il y a matière : **`> [!question] À vérifier`** pour les
incohérences relevées (cf. § Ce qu'on signale sans corriger).

---

## Bloc 3 — l'essentiel, dérivé et rien d'autre

`Cours - Indices et deflation` contient déjà sa propre phrase-clé, éparpillée :
« la question à laquelle tout ce chapitre répond », « séparer ce qui relève de
la quantité et ce qui relève du prix », les deux indices Laspeyres/Paasche.

**Après** — un encadré en tête qui ne dit rien de neuf :

```md
> [!abstract] L'essentiel
> - Un indice ramène une série à une base 100 pour rendre deux évolutions comparables.
> - Tout le chapitre sert à séparer l'effet **prix** de l'effet **quantité**.
> - Laspeyres = pondérations de l'année de base · Paasche = pondérations de l'année courante.
> - Déflater = passer d'une valeur en euros courants à une valeur en volume.
> - Sans ce chapitre, aucune série INSEE n'est lisible.
```

Chacune de ces lignes est présente dans le corps. Une sixième ligne qui
ajouterait « en pratique, Laspeyres surestime l'inflation » serait **hors
limite** : ce n'est pas écrit dans la page.

---

## Bloc 6 — le contrôle, avec l'ancre qui répond

```md
## ✅ Contrôle

Réponds sans rouvrir le cours, puis vérifie au lien.

1. Écris l'indice de $x$ en base 100 sur l'année 0. → [[#💡 L'idée : ramener à une base commune]]
2. Laspeyres ou Paasche : lequel garde les pondérations de l'année de base ? → [[#PARTIE 2 — Les indices synthétiques]]
3. Un salaire monte de 15 %, les prix de 18 %. Le pouvoir d'achat ? → [[#Déflater]]
```

Règles du bloc :
- une question par notion réellement traitée, **8 maximum** ;
- toujours l'ancre de la section qui répond, jamais la réponse recopiée ;
- une question qui n'a pas de réponse dans la page ne va **pas** dans Contrôle :
  elle va dans `À vérifier`.

---

## Ce qu'on corrige — avant / après

| Avant (tel quel dans les pages) | Après |
| --- | --- |
| `\t` seul sur la ligne 10 de `Fiche exos - Modules A C E` | ligne supprimée |
| `—` collé au mot, doubles espaces, `...` | `— ` propre, espace simple, `…` |
| `deflateur`, `Economie`, `a faire` dans le **corps** | `déflateur`, `Économie`, `à faire` |
| `**Notes de support** : [[MCC]] · [[Ressources]]` avec un lien mort | lien corrigé vers le nom réel du fichier |
| trois titres `# PARTIE 1` en `#` au milieu d'une page qui a déjà un `#` | `## PARTIE 1`, hiérarchie remise d'aplomb — **sauf si une ancre pointe dessus** |
| tableau dont une ligne a une colonne de moins | colonne vide ajoutée, contenu inchangé |
| `> [!danger]` sans titre après le callout | titre court ajouté |

**Les noms de fichiers ne s'accentuent pas.** `Cours - Contributions a la
croissance.md` reste tel quel : le renommer casse tous les `[[liens]]` du vault.
On corrige l'accent dans le titre `#` de la page, pas dans son nom.

---

## Ce qu'on ne touche jamais

- **Les chiffres de la maquette** : 62 coefficients, 46 + 14 ECTS, 432 h, 24 coef
  en CC, 39 %. Source unique `26-27_Maquette_L1_EG.xlsx`. Un chiffre faux se
  signale, ne se corrige pas.
- **Les formules** `$(uv)'$`, `$$\dots$$` : rien, ni les espaces, ni les
  parenthèses. Une formule à corriger part dans `À vérifier`.
- **Les grilles de suivi** (`Essai 1 | Essai 2 | Essai 3`), les cases `- [ ]`,
  les scores cibles : ce sont **ses** données. Une cellule vide reste vide.
- **Les énoncés d'exercices** : ni la numérotation, ni les valeurs, ni l'ordre.
  On peut corriger une faute d'orthographe dans la consigne, rien d'autre.
- **Les `[[liens]]` avec ancre** qui pointent depuis d'autres pages : le titre
  visé ne se renomme pas (`verifie.py` refuse).

---

## Ce qu'on signale sans corriger

Un seul endroit, en fin de page :

```md
> [!question] À vérifier
> - Le total du tableau des cycles donne 64 coef, le frontmatter en annonce 62 — lequel est bon ?
> - `Cycle 2` annonce 108 h, le plan en annonce 96 pour le même cycle.
> - Série C-II : 10 items annoncés, 9 numérotés.
```

Trois règles : la formulation reprend les deux valeurs en conflit, jamais un
arbitrage ; le bloc est **remplacé** à chaque passage, il ne s'empile pas ; une
ligne dont Sacha a tranché disparaît (une suppression de sa part est une
décision, pas un oubli).

---

## Le ton

Les pages sont écrites en tutoiement direct, avec des emojis en tête de section
et des callouts Obsidian. C'est **sa** forme : on la garde. Pas de « il convient
de », pas d'introduction ajoutée, pas de conclusion, pas de nouvel emoji dans un
titre qui n'en avait pas.
