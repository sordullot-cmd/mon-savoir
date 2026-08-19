---
name: inspi
description: Transforme un lien OU un nom de produit numérique en DOSSIER DE RÉFÉRENCE RANGÉ PAR ASPECT dans INSPIRATION — même forme de dossier que /univers, pour les trois modes et toutes les disciplines (ui-design, webdesign, brand-design, graphisme, motion) : ecrans (ou visuels), flows, branding, couleurs, composants, animations, marketing, process, archive. Récolte sur PLUSIEURS sources en parallèle (officiel + press kit + bases d'UI type Mobbin + galeries + auteur/équipe design + presse), jamais une seule. Site web → captures pleine hauteur desktop/mobile/sombre + typos rendues + walkthrough. App (nom ou lien de store) → écrans pleine qualité, flows, métadonnées d'éditeur. Post social (X, Instagram, Pinterest, TikTok, Behance, Dribbble, YouTube…) → le média puis le projet complet dont il est extrait. Fiche avec une section par aspect, Sources et Crédits nominatifs. Appelé par /ranger quand un lien arrive, ou directement « ajoute ce site/post en inspi », « fais-moi le dossier de telle app ».
---

# /inspi — Dossier de référence d'un produit numérique (site, app, post)

Transforme une **URL** ou un **nom de produit** en **dossier de référence rangé par
aspect** : les médias en pleine qualité, classés par nature, plus une fiche cherchable
par allure qui cite toutes ses sources et nomme ses auteurs.

C'est **le même objet que produit `/univers`**, appliqué aux produits numériques. Les
deux skills ne se distinguent que par la cible et par les outils de récolte, jamais par
la profondeur ni par la forme de la sortie.

Pour un **univers de marque ou de fiction** (jeu, film, studio) → **`/univers`**.
Frontière : *un produit qu'on utilise* → `/inspi` ; *un monde qu'on regarde* → `/univers`.

## Règle fondatrice — jamais une seule source

Une source, c'est un angle mort garanti : l'officiel ne montre que ce qu'il veut
vendre, une galerie ne montre que ce qui a plu à un curateur, un post n'est qu'un
extrait d'un projet publié ailleurs en entier. **Toute cible passe donc par la
récolte multi-sources** (§ Étape 1) avant qu'on écrive quoi que ce soit.

## Router

Le mode change **ce qu'on va chercher et avec quels outils**. Il ne change **jamais la
forme de la sortie** : c'est toujours un **dossier de référence par aspect** (§ Étape 2),
comme celui de `/univers`.

| Ce que donne Sacha | Mode | Ce que le mode change |
| --- | --- | --- |
| URL de site web | **site** | captures pleine hauteur maison (`capture-site.py`), relevé des typos rendues, walkthrough |
| Nom d'app, `apps.apple.com/…`, `play.google.com/…` | **app** | écrans de store en natif (`grab-app.py`), métadonnées d'éditeur, bases d'UI mobile |
| URL de post/pin/vidéo (`x.com`, `instagram.com`, `pinterest.*`/`pin.it`, `tiktok.com`, `behance.net`, `dribbble.com`, `tumblr.com`, `bsky.app`, `threads.net`, `youtube.com`/`youtu.be`, `vimeo.com`…) | **post** | le média du post (`grab-post.py`), puis **le projet entier** dont il est extrait |

Cas hybrides — je tranche seul et je le signale dans le récap :
- **post qui pointe vers un produit** → le produit devient la cible, le post est une source parmi d'autres ;
- **lien vers un profil / une home de plateforme** → ce n'est pas une cible : demander quoi en garder ;
- **site d'un jeu ou d'un film** → `/univers`, pas ici.

## Autonomie

Je décide seul : la discipline, le slug, l'app visée en cas d'homonyme, le périmètre
en cas de gros volume, la création d'une catégorie ou d'une valeur de vocabulaire
inédite. **Chaque décision de ce genre est écrite dans le récap** pour être corrigée
d'un mot. Je ne m'arrête pour demander que si la cible elle-même est ambiguë
(deux produits plausibles, lien mort).

---

## Étape 0 — préflight

Vérifier ce qui est disponible et **annoncer ce qui sera dégradé**, sans planter :

```
for t in gallery-dl yt-dlp ffmpeg mempalace; do command -v $t >/dev/null || echo "ABSENT: $t"; done
python3 -c "import PIL, websocket" 2>&1 | tail -1
```

- `gallery-dl` absent → mode post en fallback tuiles (`references/fallback-tuiles.md`)
- `yt-dlp` absent → pas de vidéo de flow ni de post vidéo
- `ffmpeg` absent → `record.py` / `walkthrough.py` en GIF seulement, pas de MP4
- `mempalace` absent → sauter la réindexation, le dire
- **Pillow / websocket-client** sont indispensables (`record.py`, `crop.py`,
  `stitch.py`, `shoot.py`). Manquants → `python3 -m pip install --user pillow websocket-client`.
  Pas de Homebrew sur cette machine : les binaires ci-dessus s'installent par
  `pip install --user` (`gallery-dl`, `yt-dlp`) — `ffmpeg` demande un binaire statique.

---

## Étape 1 — récolte multi-sources (toujours)

Protocole complet, contrat des agents et format JSON attendu dans
**`references/recolte.md`** ; catalogue des sources dans **`references/sources.md`**.
En bref :

1. **Composer l'éventail** : 4 à 6 sources selon le mode, au moins une officielle et
   une tierce.
2. **Lancer un sous-agent par source, tous dans un seul message** (sinon ils partent
   en série et la parallélisation ne sert à rien). Chacun cherche, ouvre, regarde,
   télécharge dans **son** dossier de scratchpad, et rend le JSON du contrat.
3. **Table ronde** : fusion + dédup, planche de contact de tout le butin, puis trois
   jurés en parallèle (qualité · pertinence · couverture). Le juré « couverture » peut
   faire **relancer** un agent sur un aspect resté vide.
4. **Arbitrage en regardant les images**, puis classement dans le dossier final.

Rien n'entre dans le vault avant cette étape. Le scratchpad de récolte reste en place
jusqu'à ce que la fiche soit écrite.

---

## Étape 2 — le dossier par aspect (toujours, tous les modes)

**La sortie de `/inspi` est un dossier de référence rangé par aspect** — exactement la
forme que produit `/univers`, transposée aux produits numériques. Jamais un dossier plat
de captures, jamais un dossier de deux fichiers parce que la cible était « juste un
post ». Un post est le fil qu'on tire ; le dossier est ce qu'il y a au bout.

Un dossier plat coûte cher plus tard : on ne sait plus si `image-4.png` est un écran, un
logo ou une pub, la fiche ne peut plus grouper par famille, et l'index transversal
(`_COMPOSANTS`, `_ANIMATIONS`) n'a rien à référencer. L'aspect est ce qui rend le dossier
relisable dans deux ans.

### Socle commun — quelle que soit la discipline

Un sous-dossier n'est créé **que s'il a du contenu**. Aucun dossier vide, aucun
placeholder.

| Aspect | Ce qui y va |
| --- | --- |
| `<slug>.md` | la fiche, une section par aspect |
| `couleurs/` | nuanciers SVG : charte publiée **et/ou** relevé de pixels (§ Étape 4) |
| `branding/` | logo, lockups, icône, fichiers de police récupérés, évolutions du logotype |
| `composants/` | blocs remarquables, suffixés `_<slug>` → [[_COMPOSANTS]] |
| `animations/` | GIF/MP4 de sections et micro-anims, suffixés `_<slug>` → [[_ANIMATIONS]] |
| `marketing/` | site du produit, landing, page store, visuels sociaux, campagnes |
| `process/` | ce que l'éditeur publie de sa fabrication : diagnostic, explorations, directions écartées, avant/après. **Rare et précieux** — la plupart des produits ne publient rien |
| `archive/` | états antérieurs : refonte passée, ancienne UI, ancien site, millésimes datés |
| `<aspect>/planches/` | les planches de famille, dans chaque aspect qui en a besoin |

### Aspect principal — selon la discipline

Le socle ne suffit pas : il faut le dossier qui porte **la matière même** de la cible. Il
dépend de la discipline, pas du mode.

| Discipline | Aspect principal | En plus, quand la matière existe |
| --- | --- | --- |
| `UI-DESIGN` | `ecrans/` | `flows/` (parcours numérotés ou vidéos) |
| `WEBDESIGN` | `ecrans/` (les captures pleine hauteur) | `flows/`, `walkthrough.mp4` à la racine |
| `BRAND-DESIGN` | `branding/` devient le cœur | `applications/` (identité en situation), `typographie/` |
| `GRAPHISME` | `visuels/` | `typographie/`, `impression/` |
| `MOTION` | `animations/` devient le cœur | `frames/` (arrêts sur image commentés), `storyboard/` |

**Un aspect manque au tableau ?** On peut le créer — même règle que partout dans le
vault (`CLAUDE.md`) : réutiliser en priorité, ne créer que si c'est vraiment justifié,
**et le signaler dans le récap**. `process/` est né comme ça (`/inspi duolingo`,
août 2026). Un aspect nouveau qui se révèle utile deux fois se documente dans
`INSPIRATION/_INSPIRATION.md`.

### Ce que ça exige de la récolte

Le dossier par aspect n'est pas un rangement de fin de course : il **pilote l'éventail**
de l'étape 1. Le juré « couverture » juge sur cette grille — un aspect vide est un trou
à combler par une relance ciblée, pas une fatalité.

Et si un aspect reste vide malgré tout, il n'existe pas dans le dossier et **le récap le
dit**. Un dossier honnêtement borgne vaut mieux qu'un dossier rempli de hors-sujet : on
ne met pas une illustration de campagne dans `ecrans/` pour que la case soit cochée.

**Volume** : ~30 à 60 médias forts par défaut, plus si Sacha dit « tout ». La qualité,
pas l'exhaustivité.

---

## Étape 3 — ce que chaque mode va chercher

### Mode site

1. **Discipline** (= dossier) : `WEBDESIGN` (défaut), `UI-DESIGN`, `BRAND-DESIGN`,
   `GRAPHISME`, `MOTION`. **Slug** : `<domaine>` ou `<domaine>-<sujet>` en kebab.
2. **Capturer** — pleine hauteur, 1 page par template, **desktop + mobile + home sombre**.
   Les captures sont la matière de l'aspect principal : elles vont dans **`<slug>/ecrans/`**,
   pas à la racine du dossier.
   ```
   python3 .claude/skills/inspi/capture-site.py "<url>" "INSPIRATION/<DISCIPLINE>/<slug>/ecrans" \
       --viewports desktop,mobile --dark
   ```
   - Pages racine uniques toutes capturées ; pages d'un même template (`/works/*`)
     regroupées en une seule (`works-template.png`) — le JSON liste les regroupements,
     **le signaler**. `--all-pages` pour forcer, `--pages "/,/about"` pour cibler,
     `--max N` (def 25), `--budget MS` (def 16000).
   - Le mobile sort en `<page>-mobile.png` (iPhone émulé, retina), le sombre en
     `home-dark.png`. **Un `home-dark.png` identique au clair = le site n'a pas de
     thème sombre** → le supprimer et le dire.
   - Le JSON renvoie aussi **`polices`** : les font-family réellement rendues. Les
     rapprocher des fiches du vault → `[[nom-de-la-font]]` si elle existe, sinon
     mentionner la typo et proposer `/font`.
3. **Regarder les captures** (`Read` la home + 1-2 pages clés) : style, mood, couleurs.
4. **Le site n'est qu'un aspect du dossier.** L'éventail de l'étape 1 doit remplir les
   autres : `branding/` (press kit du studio ou de la marque, logotype, fichiers de
   police servis par le site), `process/` (le case study du studio sur son propre
   projet — Awwwards, Behance, article), `archive/` (le site d'avant, via Wayback ou
   une galerie qui l'a indexé), `marketing/`. Un site capturé sans rien autour, c'est
   le dossier plat qu'on ne veut plus.
5. **Composants + animations**, **walkthrough**, **couleurs** — § Étape 4.
6. **Fiche** depuis `TEMPLATES/Template-Inspiration.md` (§ Fiche).

### Mode app

Les écrans d'une app vivent dans les stores et les bases d'UI. Le dossier va dans
`INSPIRATION/UI-DESIGN/<slug>/`.

1. **Écrans de store en résolution native** (source publique la plus fiable) :
   ```
   python3 .claude/skills/inspi/grab-app.py "<nom | URL store>" "INSPIRATION/UI-DESIGN/<slug>" \
       [--store ios|android|both] [--country fr] [--ipad] [--max 20]
   ```
   Renvoie icône + écrans + un JSON de métadonnées (éditeur, bundle, catégories,
   version, dates, note, prix, site officiel) qui **remplit le frontmatter** — ne pas
   le retaper. Limite assumée : ce sont des écrans **promotionnels**, souvent habillés
   ou en mockup → c'est exactement pourquoi l'éventail de l'étape 1 est obligatoire.
2. **Le produit tourne chez Sacha ?** (app web, app Mac, miroir iOS) → meilleure
   source. Une app web se capture comme un site une fois connecté via `claude-in-chrome`.
3. **Site marketing** du produit → captures dans `marketing/`.
4. **Regarder les écrans**, puis couleurs / composants / fiche.

**Frontmatter propre à une app** (en plus des communs) : `type_app`, `plateformes`,
`editeur`, `version`, `url_store`, `patterns` — valeurs dans `INSPIRATION/_INSPIRATION.md`.

### Mode post social

Un post = **le média d'abord**, et surtout **le projet dont il est extrait** : c'est
l'agent « auteur » de l'éventail qui transforme un pin en dossier de 30 visuels.

1. **Télécharger le média dans le scratchpad**, pas encore dans le vault — on ne connaît
   ni la discipline ni l'aspect avant d'avoir regardé :
   ```
   python3 .claude/skills/inspi/grab-post.py "<url>" "<scratchpad>/post/"
   ```
   `--cookies` si login (Instagram surtout ; macOS demande UNE FOIS l'accès trousseau).
   Échec malgré les cookies → `references/fallback-tuiles.md`.
2. **Discipline d'après ce que MONTRE le post**, pas d'après la plateforme : dashboard
   → `UI-DESIGN`, affiche → `GRAPHISME`, reel de motion → `MOTION`, identité →
   `BRAND-DESIGN`.
3. **Slug** = ce que le post montre (`bartolomeu-moveis`), **jamais la plateforme**
   (elle vit dans `plateforme:`).
4. **Le post n'est pas la cible, c'est l'indice.** Dédoubler l'agent « auteur » de
   l'éventail (un sur le compte lui-même, un sur « ce projet publié ailleurs ») et
   remonter jusqu'au projet complet : Behance, portfolio du studio, press kit du client,
   article de presse. C'est ce qui remplit `visuels/` ou `ecrans/`, `branding/`,
   `process/` et `animations/` — sans quoi il n'y a pas de dossier, juste une image.
5. **Le média du post trouve sa place comme les autres** : dans l'aspect qui correspond
   à ce qu'il montre, nommé d'après son contenu. `post.jpg` à la racine n'est acceptable
   que si le projet est resté introuvable — et le récap le dit.
6. **Fiche** depuis `TEMPLATES/Template-Inspiration-Post.md`, avec la légende du post
   en citation si elle éclaire le contenu.

Cas particuliers : carrousel → tout garder (`post-1.jpg`…) ; board Pinterest entier →
borner (20 pins) et le dire ; vidéo > ~100 Mo → qualité moindre et le signaler ;
stories et posts supprimés → non récupérables.

---

## Étape 4 — commun à tous les modes

### Couleurs

```
python3 .claude/skills/_lib/palette.py releve "<dossier>/ecrans/*.png"                 # hex réellement présents
python3 .claude/skills/_lib/palette.py nuancier palette.json "<dossier>/couleurs/"     # planches SVG
```
Relever aussi la **charte publiée** si elle existe (press kit, tokens CSS) avec ses
vrais noms. **Ne jamais inventer un hex ni un nom** : soit une charte sourcée, soit un
relevé de pixels — et la fiche distingue les deux.

### Gestion des images — regarder, puis ranger

> Le rangement se décide **en regardant les images**, jamais d'après leur nom ni
> l'ordre d'arrivée.

1. **Planche de contact AVANT de classer** :
   ```
   python3 .claude/skills/_lib/planche.py "<scratchpad>/vu-<aspect>.png" "<dossier>/*" --cols 6 --tile 200
   ```
   puis la **lire**. On y voit les doublons, les vides, les illisibles.
2. **Un fichier ne se garde que s'il apporte une information nouvelle.** Même géométrie
   avec un changement de couleur/cadre = **une famille**, pas N références.
3. **Un embed dans la fiche = une famille, pas un fichier.** Un SVG sans dimensions
   s'affiche pleine largeur dans Obsidian : dix embeds du même wordmark = dix pleines
   pages inutiles (vécu, `duolingo/branding`). Une famille → **UNE planche** :
   ```
   python3 .claude/skills/_lib/planche.py "<aspect>/planches/planche-<famille>.png" <fichiers…> \
       --cols 3 --bg clair --titre "Wordmark - declinaisons"
   ```
   Les fichiers individuels restent en place comme assets.
4. **Visuel seul** : `![[x.svg|500]]`, jamais un embed nu.
5. **Séparer l'asset de la règle** : un logo utilisable et une planche « do not » ne
   jouent pas le même rôle — le nom et la légende doivent le dire.
6. **Nommer d'après ce que l'image montre**, une fois qu'on l'a vue.
7. **Composition** (relevée sur `design.duolingo.com`, référence du vault) : une ligne
   remplit toute la largeur ; les cellules d'une ligne sont identiques et toutes les
   lignes d'un lot ont la même hauteur, visuel centré et contenu dedans ; la variation
   vient du contenu, pas de l'envie de varier. `planche.py` répartit déjà sans ligne
   orpheline (10 visuels à 3 → 3-3-2-2).

### Composants (sélectif)

> `composants/` = blocs UI statiques (`.png`) → [[_COMPOSANTS]] · `animations/` =
> sections et micro-anims (`.gif` / `.mp4`) → [[_ANIMATIONS]]. Une section **qui
> s'anime** va dans `animations/`.

Ils vivent **dans le dossier du produit** : `<slug>/composants/<type>_<slug>.png`
(le suffixe garde les noms uniques pour l'index global). Découpe :
```
python3 .claude/skills/_lib/crop.py "<capture.png>" "<slug>/composants/<type>_<slug>.png" --box <x> <y> <w> <h>
```
(`--band <y_haut> <y_bas>` pour une bande pleine largeur ; coordonnées en pixels de
l'image source ; vérifier en relisant le découpage).

**Ne pas tout prendre** : seulement ce qui sort du lot, au jugement — pas de quota.
Rien d'original → rien, et le dire. Sur une app : tab bar, sheet, carte de liste,
empty state, paywall, header collant. Si Sacha demande un composant précis, le faire
même s'il est banal. **Indexer** dans `INSPIRATION/COMPOSANTS/_COMPOSANTS.md` (le
fichier n'est pas déplacé, l'index ne fait que le référencer).

### Passe animation (automatique, sélective)

```
python3 .claude/skills/inspi/record.py "<url>" "<slug>/animations/<type>_<slug>.gif" \
    [--seconds 4 --fps 12 --delay 0 --box x y w h --hover-selector "css" --scroll-from Y0 --scroll-to Y1]
```
Quatre choses à tenter, **jugées en regardant le résultat** :
1. **Loader** — toujours les ~4 premières s de la home. Original → garder, spinner banal → jeter.
2. **Autoplay** (hero animé, canvas, motion de fond) — cadrer avec `--box`.
3. **Hover** — ~3 candidats max (nav, CTA, 1re carte). Garder les hovers vraiment
   travaillés, pas un changement de couleur.
4. **Sections animées au scroll** — le cœur des beaux sites. `--scroll-from Y0 --scroll-to Y1`
   (repérer le `Y` sur la capture pleine hauteur) fait défiler pendant la capture et
   déclenche l'anim. Header / hero à longue anim : `--delay 0 --seconds 5`.

Pour une **app**, les anims viennent d'Appshots ou Page Flows (agents de l'éventail),
pas de la machine. Limites : ~4-8 fps réels sur page lourde ; hover simulé best-effort ;
vidéo YouTube non capturable en flux → on prend sa frame.

### Walkthrough (automatique en mode site)

```
python3 .claude/skills/inspi/walkthrough.py "<url>" "<slug>/walkthrough.mp4" \
    [--fps 10 --speed 500 --hold 0.8 --max-pages 8]
```
Étape la plus longue (plusieurs lancements de Chrome) → **la faire en dernier**.
L'intégrer via `![[walkthrough.mp4]]`. Gros site → `--max-pages` et le signaler.

### Fiche

Template selon le mode (`Template-Inspiration` · `Template-Produit` ·
`Template-Inspiration-Post`). **Remplir TOUS les descripteurs** — vocabulaire
**contrôlé** listé dans `INSPIRATION/_INSPIRATION.md`, pas de synonyme inventé :
`discipline`, `source`, `media`, `type_site` / `type_app`, `secteur`,
`couleur_principale` + `couleurs`, `anime` + `animations`, `layout`, `mood`, `tags`,
`typos` (relevées aux captures), `date_capture`.

Une **fiche = un maximum d'informations et de mots-clés** : qui (studio / designer +
client, avec liens), d'où (**toutes** les sources de l'éventail, pas seulement
l'officielle), quoi (chaque visuel décrit en une ligne), style, « Pourquoi je l'aime »,
« À réutiliser pour », et une section `## Mots-clés` libre et généreuse (synonymes
FR/EN) — carburant de la recherche MemPalace. Le frontmatter reste contrôlé ; les
mots-clés sont libres.

**La fiche suit les aspects du dossier** : une section `##` par aspect, dans l'ordre du
dossier, chaque famille montrée par **une planche** légendée juste dessous, et les
fichiers isolés cités par leur chemin quand ils méritent une mention. Un aspect qui
existe sur le disque et n'a pas sa section dans la fiche est un aspect perdu.

**Deux sections sont obligatoires**, reprises de `/univers` parce qu'elles font la
valeur d'un dossier de référence :

- `## Sources` — **toutes** les sources de l'éventail, avec ce que chacune a apporté et
  son URL. Un média sans provenance traçable ne rentre pas dans le dossier.
- `## Crédits` — qui a fait quoi, **avec les liens vers les portfolios** (Dribbble,
  Behance, site perso, agence, foundry). Sur un produit numérique, c'est souvent une
  équipe nommée : chercher le compte de l'équipe design, les case studies signés, les
  interviews. Nommer les gens est la moitié de l'intérêt du dossier.

Une valeur manque au vocabulaire ? l'ajouter à `_INSPIRATION.md` et le signaler.

### Clôture

1. **Indexer** — la ligne d'index nomme **les aspects couverts**, pas seulement la cible :
   - `_APPS.md` dès que la cible est **un produit** (app mobile, app web, SaaS), qu'on soit
     arrivé par un store, une URL ou un post ;
   - `_MOODBOARD.md` quand la cible est un **site de référence** (portfolio, agence, studio,
     éditorial) — c'est une inspi qu'on regarde, pas un produit qu'on utilise ;
   - `+ _COMPOSANTS.md` / `_ANIMATIONS.md` pour ce qui a été extrait.
2. **Réindexer MemPalace** : `mempalace mine "$HOME/Documents/brain^2" --agent sacha`
   (absent → sauter, le dire).
3. **Publier** — dérouler `.claude/skills/_lib/publier.md` : réindexer le site
   (`npm run index --prefix ~/Documents/GitHub/vault-gallery`), puis **commiter et pousser
   le vault ET le site** ; le push du site déclenche le déploiement Vercel.
   **Non bloquant** : un échec ne fait pas échouer un run réussi, il se signale.
4. **Récap** : sources interrogées et ce que chacune a apporté · discipline / slug ·
   **aspects créés avec le nb de médias par aspect, et les aspects restés vides** ·
   nb de médias récoltés → retenus, et pourquoi les autres sont partis · descripteurs
   remplis · typos détectées · **auteurs et studios identifiés** · composants et anims
   gardés (ou « aucun ») · décisions prises seul (dont tout aspect ou toute valeur de
   vocabulaire créé) · **toute limite rencontrée** (troncature, cookie-wall, login,
   source inaccessible).

---

## Structure produite

**Une seule structure, pour les trois modes et toutes les disciplines.** Ce qui varie,
c'est quels sous-dossiers ont de la matière — jamais la forme.

```
INSPIRATION/<DISCIPLINE>/<slug>/
├── <slug>.md            ← fiche : une section par aspect + Sources + Crédits
├── icone.png            ← si la cible a une icône d'app
├── walkthrough.mp4      ← mode site
│
├── ecrans/              ← UI-DESIGN, WEBDESIGN — l'aspect principal
│   └── planches/        ← une planche par famille (le seul embed de la fiche)
├── visuels/             ← GRAPHISME (à la place de ecrans/)
├── flows/               ← parcours numérotés ou vidéos
├── branding/            ← logo, lockups, icônes, fichiers de police
├── couleurs/            ← nuanciers SVG (charte publiée et/ou relevé)
├── composants/          ← blocs remarquables, suffixés _<slug> → [[_COMPOSANTS]]
├── animations/          ← GIF/MP4, suffixés _<slug> → [[_ANIMATIONS]]
├── marketing/           ← landing, page store, visuels sociaux, campagnes
├── process/             ← ce que l'éditeur publie de sa fabrication
└── archive/             ← états antérieurs, millésimes datés
```

Sous-dossier **créé seulement s'il a du contenu**. Aspect manquant au tableau de
l'étape 2 → on peut le créer, en le signalant.

Nommage descriptif en kebab (`onboarding-03-permissions.png`), jamais `image(3).jpg`.
Volume : la qualité, pas l'exhaustivité — ~30 à 60 médias forts, plus si Sacha dit « tout ».

## Limites (à signaler, pas à cacher)

- **Découverte des pages** = liens de la home (1 niveau) → une page profonde non liée
  peut manquer ; demander l'URL et utiliser `--pages`.
- **Lazy-load** géré (scroll avant capture) ; **embeds YouTube** remplacés par leur
  miniature ; **Vimeo / players custom** peuvent rester blancs → le signaler.
- **Cookie-walls** et **préchargeurs** : recapturer avec `--budget 25000` si une page
  sort en « loading… ».
- **Login / paywall** : pages protégées non capturables ; le derrière-le-login d'une
  app n'est pas accessible sans Sacha.
- **Bases d'UI** : presque toutes exigent un compte et bloquent le fetch direct
  (Mobbin répond 403) → `claude-in-chrome`, ou dire honnêtement ce qu'on n'a pas eu.
- **Instagram** : `--cookies` presque toujours nécessaire, et parfois insuffisant
  (cf. `references/fallback-tuiles.md`).
- **Vimeo** : `yt-dlp` échoue en `401 Unauthorized` sur le token OAuth (constaté le
  18 août 2026) → tenter `--cookies-from-browser chrome`, sinon se rabattre sur une
  frame et le signaler. YouTube, lui, passe (runtime JS Node câblé dans
  `~/.config/yt-dlp/config`).

## Garde-fous

- Ne pas écraser un dossier existant (même slug) → **compléter**, ou suffixe daté.
- Les visuels vivent dans le dossier de l'inspi ; le scratchpad n'est qu'un sas de récolte.
- Vocabulaire de tags **contrôlé** : réutiliser l'existant, pas de synonyme inventé.
- **Pleine qualité d'abord** : jamais une vignette quand l'original existe.
- Usage = **référence personnelle**, pas de republication ; **sourcer** chaque famille
  de médias et créditer la base d'UI quand un écran en vient.
- Toute limite se **signale**, jamais ne se cache.
- **Surveiller le poids du dossier.** Un dossier par aspect systématique, c'est plus de
  médias à chaque run, et les deux dépôts sont **déjà au bord** : `/inspi duolingo`
  (août 2026) a produit 168 Mo, le push du vault a d'abord renvoyé un `HTTP 408` et
  celui du site n'est pas passé. Les gros postes sont toujours les mêmes : les MP4 de
  flows et les GIF surdimensionnés. Annoncer le poids dans le récap dès qu'il dépasse
  ~50 Mo, et si un push échoue, **remonter l'arbitrage à Sacha** (cf. § « la taille » de
  `_lib/publier.md`) — ne jamais supprimer de médias pour faire de la place.

## Outils

| Script | Rôle |
| --- | --- |
| `capture-site.py` | captures pleine hauteur, 1 page/template, desktop + mobile + sombre, relevé des typos |
| `shoot.py` | le capteur CDP sous-jacent (`--mobile`, `--sombre`) |
| `walkthrough.py` | vidéo de défilement de tout le site |
| `record.py` | GIF/MP4 d'une anim (loader, hover, scroll) |
| `grab-app.py` | écrans + métadonnées d'une app depuis App Store / Google Play |
| `grab-post.py` | médias d'un post social (gallery-dl / yt-dlp) |
| `../_lib/planche.py` | planche de vignettes : pour **regarder** avant de ranger, et pour **livrer** une famille |
| `../_lib/crop.py` | découpe un composant dans une capture |
| `../_lib/palette.py` | relevé de couleurs + nuanciers SVG |
| `../_lib/stitch.py` | recolle les tuiles de la capture native |

## Références (à lire au besoin, pas d'avance)

| Fichier | Quand |
| --- | --- |
| `references/sources.md` | composer l'éventail — catalogue des sources par mode |
| `references/recolte.md` | contrat des sous-agents, format JSON, table ronde |
| `references/fallback-tuiles.md` | `grab-post.py` a échoué même avec `--cookies` |
| `../_lib/publier.md` | la clôture : réindexer le site, commiter et pousser les deux dépôts |
