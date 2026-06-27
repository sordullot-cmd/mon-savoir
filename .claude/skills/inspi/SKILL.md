---
name: inspi
description: À partir d'un lien de site web, capture tout le site (un screenshot par page) et crée une inspiration rangée par discipline (dossier lien + captures + fiche cherchable). Appelé par /ranger quand un lien arrive, ou directement « ajoute ce site en inspi / screenshot ce lien ».
---

# /inspi — Inspiration depuis un lien web

Transforme une **URL** en inspiration rangée : un **dossier** (dans sa discipline) contenant le **lien + une capture par page + une fiche** décrite → cherchable par allure.

## Procédure

1. **Récupérer l'URL** (donnée par Sacha, ou depuis un `.url/.webloc/.txt` de l'INBOX, ou une note ne contenant qu'un lien).
2. **Choisir la discipline** (= dossier de destination) : `WEBDESIGN` (défaut pour un site), `UI-DESIGN`, `BRAND-DESIGN`, `GRAPHISME`, `MOTION`. Si aucune ne colle, **créer une catégorie** (cf. règle dans `CLAUDE.md` — rester sobre). Si vraiment ambigu, demander.
3. **Slug** : `<domaine>` ou `<domaine>-<sujet>` en kebab (ex. `eliotdewolf`, `linear-pricing`). Destination = `INSPIRATION/<DISCIPLINE>/<slug>/`.
4. **Lire la page** (`WebFetch`) : titre, description, secteur, style → nourrit fiche + mood/tags.
5. **Capturer le site** (chaque page = capture **pleine hauteur**, via le protocole Chrome, pas juste le viewport) :
   ```
   python3 .claude/skills/inspi/capture-site.py "<url>" "INSPIRATION/<DISCIPLINE>/<slug>"
   ```
   - **Par défaut = tout le site, MAIS 1 page par template.** Les pages qui partagent un même template (ex. les fiches projet `/works/*`, les articles `/blog/*`) sont **regroupées** : on n'en capture **qu'une seule** comme exemple (`works-template.png`), pas les 10. Les pages racine uniques (`/`, `/about`, `/shop`…) sont toutes capturées. Le JSON liste les groupes regroupés (`templates_regroupés`) → le **signaler** (ex. « 10 pages projet → 1 capturée »).
   - **Forcer chaque page** (rare) : `--all-pages`.
   - **Seulement certaines pages** si Sacha le demande : `--pages "/,/about,/shop"` (la home seule = `--pages "/"`).
   - Options : `--max N` (def 25, plafond de sécurité), `--budget MS` (def 16000, délai de rendu).
   - Le script renvoie un JSON : pages capturées + regroupements + toute **troncature** (jamais silencieuse → la signaler).
6. **Regarder les captures** (`Read` `home.png` + 1-2 pages clés) — jugement : style, mood, couleurs, ce qui est intéressant. Repérer un **cookie-wall / loader** résiduel (cf. Limites).
7. **Créer la fiche** `INSPIRATION/<DISCIPLINE>/<slug>/<slug>.md` depuis `TEMPLATES/Template-Inspiration.md` :
   - `discipline:` + `source:` (URL complète) + `media: site`
   - `mood:` + `couleurs:` d'après les captures
   - `tags:` du vocabulaire d'`INSPIRATION/_INSPIRATION.md` (discipline + mood + `#a-tester`…)
   - intégrer `![home](home.png)` + une galerie `## Pages du site` avec les autres captures
   - « Pourquoi je l'aime » + « À réutiliser pour »
8. **Extraire composants + animations** (jugement — voir § Composants et § Passe animation). **Deux dossiers distincts** dans `INSPIRATION/<DISCIPLINE>/<slug>/` :
   - **Composants statiques** → `composants/` : découper les blocs **vraiment originaux/réutilisables** (footer, hero, index, pricing…) en `.png`. Indexer dans `INSPIRATION/COMPOSANTS/_COMPOSANTS.md`.
   - **Animations** → `animations/` : passe automatique (loader / autoplay / hover / **section animée**), garder les **pépites** en GIF/MP4. Indexer dans `INSPIRATION/ANIMATIONS/_ANIMATIONS.md`.
   - Dans les deux cas : ligne dans l'index global (`![[fichier]]`) + reliée depuis la fiche.
   - **Rien d'original → rien.**
9. **Vidéo walkthrough** (AUTOMATIQUE à chaque site) : `python3 .claude/skills/inspi/walkthrough.py "<url>" "INSPIRATION/<DISCIPLINE>/<slug>/walkthrough.mp4"` → l'intégrer dans la fiche via `![[walkthrough.mp4]]`.
10. **Réindexer MemPalace** : `mempalace mine /Users/smoricet/Documents/KNOWLEDGE --agent sacha`.
11. **Récapituler** : discipline, slug, nb de pages, composants/anims retenus (ou « aucun »), walkthrough, mood/tags, et tout cookie-wall / troncature.

## Composants statiques (sélectif)

> **Deux dossiers, deux index** : `composants/` = blocs UI statiques (`.png`) → [[_COMPOSANTS]] ; `animations/` = sections / intros / micro-anims (`.gif`/`.mp4`) → [[_ANIMATIONS]]. Une **section qui s'anime** va dans `animations/`, pas dans `composants/` (cf. § Passe animation).

- **Où** : les composants statiques vivent **dans le dossier du site** → `INSPIRATION/<DISCIPLINE>/<slug>/composants/<type>_<slug>.png` (contexte préservé, dossier site auto-suffisant). Le **suffixe `_<slug>`** garde les noms uniques pour l'index global.
- **Ne pas tout prendre** : pas un composant par section. Seulement ce qui sort du lot. **Rien d'original → rien à extraire** (le dire). Sauf si Sacha demande un composant précis.
- **Comment** : regarder les captures pleine hauteur, repérer le composant, le **découper** :
  ```
  python3 .claude/skills/inspi/crop.py "<capture.png>" "INSPIRATION/<DISCIPLINE>/<slug>/composants/<type>_<slug>.png" --box <x> <y> <w> <h>
  ```
  (ou `--band <y_haut> <y_bas>` pour une bande pleine largeur). Coordonnées en pixels de l'image **source**. Vérifier le découpage en le relisant, ajuster si besoin.
- **Indexer** : ajouter une ligne à l'index global `INSPIRATION/COMPOSANTS/_COMPOSANTS.md` (type, source `[[fiche]]`, pourquoi, `![[fichier]]`) + relier depuis la fiche d'inspi. Le fichier n'est PAS déplacé : l'index ne fait que le référencer.
- Si Sacha demande un composant précis (« prends-moi le footer »), le faire même s'il est banal.

### Passe animation — AUTOMATIQUE & sélective (GIF/MP4)

À faire **automatiquement** à chaque `/inspi`, mais en ne gardant que ce qui est **vraiment cool/stylé** (même exigence que pour les composants — rien de marquant → rien). Outil :
```
python3 .claude/skills/inspi/record.py "<url>" "INSPIRATION/<DISCIPLINE>/<slug>/animations/<type>_<slug>.gif" \
    [--seconds 4 --fps 12 --delay 0 --box x y w h --hover-selector "css" --scroll-from Y0 --scroll-to Y1]
```

**4 choses à tenter (et à juger en regardant le résultat) :**
1. **Loader** — toujours enregistrer les ~4 premières s de la home (`--delay 0`). Le **regarder** : si c'est un loader **cool/original** → garder (`loader_<slug>.gif`) ; si c'est un spinner/fondu banal → **jeter**.
2. **Animation autoplay** (hero animé, motion de fond, canvas) — si une zone bouge visiblement, l'enregistrer (cadrer avec `--box`). Garder si stylé.
3. **Hover** — survoler un **petit set** de candidats clés (nav principale, bouton/CTA, 1ʳᵉ carte projet) avec `--hover-selector`. **Cap : ~3 candidats max.** Garder seulement les hovers **vraiment stylés** (transition, reveal, déformation…), pas un simple changement de couleur.
4. **Sections animées au scroll / longues animations de section** — c'est le cœur de beaucoup de beaux sites (ex. le **header de Ribbit** qui se déploie longuement, la **carte « Process »** qui se révèle au défilement). Dès qu'une **section entière s'anime joliment** (au chargement OU au scroll), la prendre en GIF, pas juste en screenshot figé :
   - **Header / hero à longue anim** : `--delay 0 --seconds 5` (plus long que 4 s pour laisser l'anim se dérouler), éventuellement `--box` pour cadrer le hero.
   - **Section révélée au scroll** (carte, bloc qui apparaît, parallaxe, texte qui traverse) : utiliser **`--scroll-from Y0 --scroll-to Y1`** → la page défile pendant la capture et déclenche l'animation. Repérer le `Y` de la section sur la capture pleine hauteur (coordonnées pixel de l'image source) et balayer autour (ex. `--scroll-from 1800 --scroll-to 3200`).
   - Nommer par la section : `header_<slug>.gif`, `process_<slug>.gif`, `hero_<slug>.gif`…

**Sélectivité** : objectif = quelques pépites animées, pas tout filmer. Si rien ne sort du lot → ne rien garder (le dire). Mais une **section qui s'anime vraiment bien mérite presque toujours un GIF** plutôt qu'un screenshot mort.
**Sortie** : `.gif` (s'anime dans Obsidian, idéal petit format) ou `.mp4` (ffmpeg, plus léger/net en grand). Ranger dans `<site>/animations/` (PAS `composants/`), indexer dans `_ANIMATIONS.md`.

**Limites** : débit réel ~4-8 fps sur pages lourdes (`--fps` = plafond). Hover/clic = simulation best-effort (peut rater une anim complexe). **Vidéo YouTube/Vimeo** : pas récupérable en vidéo (DRM/streaming) → on prend sa **frame** (miniature), pas le flux.

### Vidéo walkthrough du site complet (AUTOMATIQUE)

**À générer systématiquement** à chaque `/inspi` — vidéo de tout le site (défilement auto de chaque page, assemblé en un seul MP4) :
```
python3 .claude/skills/inspi/walkthrough.py "<url>" "INSPIRATION/<DISCIPLINE>/<slug>/walkthrough.mp4" [--fps 10 --speed 500 --hold 0.8 --max-pages 8 --pages "/,/about"]
```
- Découvre les pages (1 par template), charge le lazy-load + frames vidéo, scrolle chaque page haut->bas, concatène en `walkthrough.mp4`.
- L'intégrer dans la fiche : `![[walkthrough.mp4]]`.
- C'est l'étape la plus longue (plusieurs lancements Chrome) → la faire en dernier. Sur un **très gros site**, borner avec `--max-pages` et le signaler.

## Structure produite

```
INSPIRATION/<DISCIPLINE>/<slug>/
├── <slug>.md             ← fiche : lien + captures intégrées + mood/tags
├── home.png              ← capture PLEINE HAUTEUR
├── <page>.png …          ← pages racine uniques (about, shop…)
├── <groupe>-template.png ← 1 exemple par template (ex. works-template.png)
├── walkthrough.mp4       ← vidéo de tout le site (auto)
├── composants/           ← blocs UI statiques réutilisables (dans le projet)
│   └── <type>_<slug>.png
└── animations/           ← sections / intros / micro-anims marquantes (dans le projet)
    └── <type>_<slug>.gif|mp4

INSPIRATION/COMPOSANTS/_COMPOSANTS.md   ← INDEX transversal des composants (référence, ne stocke pas)
INSPIRATION/ANIMATIONS/_ANIMATIONS.md   ← INDEX transversal des animations (référence, ne stocke pas)
```

## Limites (à signaler, pas à cacher)

- **Découverte des pages** = liens présents sur la **home** (1 niveau). Des pages profondes non liées depuis l'accueil peuvent manquer → si Sacha veut une page précise non trouvée, lui demander l'URL et utiliser `--pages`.
- **Images lazy-load** : le capteur **scrolle toute la page** avant la capture pour les déclencher (sinon zones blanches). **Vidéos** : les `<video>` HTML5 sont lancées en muet (capture d'une frame) et les **embeds YouTube sont remplacés par leur miniature** (= une frame de la vidéo, sinon ils sortent blancs en headless). Limite : **Vimeo / players custom** peuvent rester blancs → le signaler et proposer un screenshot manuel.
- **Cookie-walls / RGPD** peuvent masquer une capture. **Préchargeurs** (Framer/SPA) : le `--budget` à 16 s les évite la plupart du temps ; si une capture sort en « loading… », **recapturer** avec un budget plus long (ex. `--budget 25000`) ou demander un screenshot manuel.
- **Login / paywall** : pages protégées non capturables → le signaler.
- **Gros sites** : au-delà de `--max`, troncature signalée → demander à Sacha s'il veut tout.

## Garde-fous

- Ne pas écraser une inspi existante (même slug) → mettre à jour ou suffixe.
- Les captures vivent **dans le dossier de l'inspi** (le livrable), jamais dans le scratchpad.
- Vocabulaire de tags **contrôlé** (comme pour les fonts) : réutiliser l'existant, pas de synonyme inventé.
