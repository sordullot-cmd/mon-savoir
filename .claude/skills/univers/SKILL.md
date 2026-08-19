---
name: univers
description: À partir d'un NOM (jeu vidéo, marque, studio, film, série…), fait une recherche web en éventail pour rapatrier tous les médias créatifs de cet univers (branding/logos, UI/menus, character design/concept art, illustrations/key art, animations/trailers, gameplay/produit) en pleine qualité, génère les nuanciers de couleurs en images (palette déclarée + couleurs réellement relevées dans les écrans), et crée un dossier de référence permanent dans INSPIRATION/UNIVERS/ avec une fiche cherchable. À utiliser quand Sacha dit « fais-moi le dossier de tel jeu/marque », « recherche tout sur X », « je veux les références de X », « récupère la DA / les couleurs / l'UI de X ».
---

# /univers — Dossier de référence complet sur un univers créatif

Transforme un **nom** (pas une URL — pour une URL, c'est `/inspi`) en **dossier de référence permanent** : les médias eux-mêmes, téléchargés en pleine qualité, rangés par aspect + une fiche cherchable. Objectif : que les données **ne disparaissent jamais**, même si les sources en ligne meurent.

Marche pour **n'importe quel univers** : jeu vidéo, marque, studio, film, série, musicien, événement…

**Frontière avec `/inspi`** : *un monde qu'on regarde* (jeu, film, studio, marque) → c'est ici. *Un produit numérique qu'on utilise* (app, SaaS, site, post) → **`/inspi`**, qui produit **exactement le même dossier par aspect**, en tirant sa matière des stores, des press kits et des bases type Mobbin. Les deux skills se distinguent par la cible et par les outils de récolte, **jamais par la profondeur ni par la forme de la sortie** : si l'un des deux fait un dossier plus riche que l'autre, c'est un bug, pas une différence de nature. Si un univers a une app ou un site à documenter, appeler `/inspi` pour cette partie et ranger le résultat dans le dossier de l'univers.

## Procédure

1. **Identifier l'univers.** Si le nom est ambigu (plusieurs jeux/marques homonymes), demander. Noter le **focus** éventuel de Sacha (« surtout la DA », « juste les logos ») → il pondère la recherche.

2. **Recherche en éventail** — **un sous-agent par source, tous lancés dans un seul message**, puis table ronde (fusion, dédup, jury qualité/pertinence/couverture) : le protocole commun est décrit dans **`.claude/skills/inspi/references/recolte.md`**, le catalogue des sources dans **`.claude/skills/inspi/references/sources.md`**. Angles propres à un univers, par ordre de fiabilité :
   - **Sources officielles** : site officiel, press kit (souvent `presskit()` / page « press »), comptes officiels, pages stores (Steam, App Store…).
   - **Artistes crédités** : identifier qui a fait quoi (art director, character designer, illustrateurs, studios d'animation des trailers) et retrouver leurs **portfolios** (ArtStation, Behance, site perso) — c'est là que vivent les concept arts et process.
   - **Bases spécialisées** : Game UI Database (gameuidatabase.com) pour les UI de jeux, wikis de fans (screenshots, sprites), Fonts In Use / Brands of the World pour les marques, Art of the Title pour les génériques…
   - **Vidéo** : chaînes YouTube/Vimeo officielles (trailers, making-of, devlogs, showreels des studios d'animation).
   Chaque angle doit rendre des **URLs directes de médias** (ou de pages téléchargeables), pas des descriptions.

3. **Adapter les aspects à l'univers.** Base commune : `branding/` (logos, identité), `couleurs/` (nuanciers, cf. étape 6), `illustrations/` (key art, artworks), `animations/` (trailers, motion, GIF/MP4). Puis selon le cas :
   - **Jeu vidéo** : + `ui/` (menus, HUD, boutons, écrans), `character-design/` (mascotte, concept art, turnarounds, sprites), `gameplay/` (screenshots in-game).
   - **Marque** : + `campagnes/` (pubs, affiches, activations), `produit/` (packaging, objets), éventuellement `historique/` (anciens logos, évolutions).
   - Ne créer un sous-dossier **que s'il aura du contenu**. Autre aspect pertinent → le créer (rester sobre).

4. **Télécharger en pleine qualité** dans `INSPIRATION/UNIVERS/<slug>/<aspect>/` :
   - Images directes / press kits : `curl -L` (prendre la **plus grande résolution** disponible — fichier source du press kit, pas la vignette).
   - Portfolios (ArtStation, Behance, Pinterest…) : `gallery-dl` (cibler le **projet précis**, pas tout le compte).
   - Vidéos : `yt-dlp -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]"` → `.mp4`. Si > ~150 Mo, baisser la qualité et le signaler. Une micro-anim qui mérite la boucle → convertir un extrait en GIF (`ffmpeg`).
   - **Nommage descriptif en kebab** : `logo-principal.png`, `menu-principal.jpg`, `concept-narinder.jpg`, `trailer-lancement.mp4`… jamais `image(3).jpg`.
   - **Volume** : viser la qualité, pas l'exhaustivité — **~30 à 60 médias forts** par défaut (plus si Sacha demande « tout »). Toute troncature/échec de téléchargement → **signaler, jamais silencieux**.

5. **Regarder les images, puis ranger** — obligatoire, et pas sur un échantillon : faire la **planche de contact** de chaque aspect, la lire, et classer d'après ce qu'on voit (jamais d'après le nom du fichier ni l'ordre des pages du PDF source) :
   ```
   python3 .claude/skills/_lib/planche.py "<scratchpad>/vu-<aspect>.png" "INSPIRATION/UNIVERS/<slug>/<aspect>/*" --cols 6 --tile 200
   ```
   Ce qu'on en tire : les doublons et les visuels vides (à virer), la bonne résolution, et surtout les **familles de variantes** — même visuel à la couleur / au cadre / à la rotation près. Une famille ne donne **pas** N références : elle donne **une planche**
   ```
   python3 .claude/skills/_lib/planche.py "<aspect>/planches/planche-<famille>.png" <fichiers…> --cols 3 --bg clair --titre "…"
   ```
   qui sera le **seul embed** de la fiche pour cette famille (les fichiers restent en place comme assets). Détail de la règle : § « Gestion des images » de `.claude/skills/inspi/SKILL.md`.
   **Pourquoi c'est non négociable** : dans Obsidian un SVG sans dimensions s'affiche **pleine largeur**, donc dix embeds du même wordmark = dix pleines pages qui n'apprennent rien (cas vécu, `duolingo/branding`, août 2026). Un visuel seul se cadre avec `![[x.svg|500]]`.

6. **Faire les couleurs — en images, pas en texte.** Deux commandes, avec `palette.py` (livré avec ce skill, sans dépendance) :
   ```
   python3 .claude/skills/_lib/palette.py releve "INSPIRATION/UNIVERS/<slug>/ui/*.png"
   python3 .claude/skills/_lib/palette.py nuancier palette.json "INSPIRATION/UNIVERS/<slug>/couleurs/"
   ```
   Relever aussi la **charte publiée** si elle existe (brand guidelines, press kit, tokens du site) avec ses vrais noms et références (Pantone, CMJN). Chaque pastille porte nom + hex + une note d'usage. Reporter dans `couleur_principale` / `couleurs` et intégrer les planches dans la fiche.
   **Ne jamais inventer un hex ni un nom** : charte sourcée ou relevé de pixels — et la fiche distingue les deux (une teinte relevée absente de la charte se signale comme telle).

7. **Créer la fiche** `INSPIRATION/UNIVERS/<slug>/<slug>.md` depuis `TEMPLATES/Template-Univers.md` :
   - Frontmatter : `type: univers`, `categorie` (jeu-vidéo/marque/studio/film…), `secteur`, `annee`, `createurs`, `source` (site officiel), `couleur_principale` + `couleurs` (observées sur les médias), `mood`, `tags`.
   - **Une section par aspect** avec galerie intégrée (`![[fichier]]`) et une ligne de description par média marquant.
   - **Section « Couleurs »** : les planches de l'étape 6 en `![[…]]`, doublées d'un tableau (nom · hex · Pantone/CMJN) pour pouvoir copier les valeurs — puis, si un relevé a été fait, ce qu'il révèle sur l'usage réel.
   - **Section « Artistes & crédits »** : qui a fait quoi, avec **liens vers les portfolios** — c'est une des grandes valeurs du dossier.
   - **Sources** : lister les URLs d'origine (press kit, pages, vidéos) pour pouvoir y retourner.
   - « Pourquoi je l'aime » + « À réutiliser pour » + section `## Mots-clés` **libre et généreuse** (FR/EN, synonymes) — carburant MemPalace.

8. **Indexer** : ajouter une ligne dans `INSPIRATION/UNIVERS/_UNIVERS.md` (univers, catégorie, aspects couverts, lien `[[fiche]]`).

9. **Réindexer MemPalace** : `mempalace mine "$HOME/Documents/brain^2" --agent sacha`.

10. **Publier** : dérouler `.claude/skills/_lib/publier.md` — réindexer le site
    (`npm run index --prefix ~/Documents/GitHub/vault-gallery`), puis commiter et pousser
    **le vault et le site** (le push du site déclenche le déploiement Vercel). Non bloquant.

11. **Récapituler** : slug, aspects créés, nb de médias par aspect, artistes identifiés, vidéos (taille), source des couleurs (charte publiée / relevé / les deux), et tout échec/troncature/source inaccessible.

## Structure produite

```
INSPIRATION/UNIVERS/<slug>/
├── <slug>.md            ← fiche : sources + crédits + galeries + mood/tags + mots-clés
├── branding/            ← logos, identité, lockups (anciens logos si pertinent)
├── couleurs/            ← nuanciers SVG : palette déclarée + palette observée (`palette.py`)
├── ui/                  ← menus, HUD, boutons, écrans (jeux/apps)
├── character-design/    ← mascotte, concept art, turnarounds, sprites
├── illustrations/       ← key art, artworks, affiches
├── animations/          ← trailers, motion, micro-anims (.mp4/.gif)
└── gameplay/            ← screenshots in-game (ou campagnes/, produit/… selon l'univers)
```

## Garde-fous

- **Usage = référence personnelle** dans le vault (pas de republication) ; toujours **sourcer** chaque famille de médias dans la fiche.
- Ne pas écraser un dossier d'univers existant (même slug) → **compléter** l'existant.
- Pleine qualité d'abord : jamais une vignette quand le fichier source existe.
- Slug en kebab, sous-dossiers d'aspect en minuscules.
- Vocabulaire de tags contrôlé (`_INSPIRATION.md`) pour le frontmatter ; la section Mots-clés reste libre.
- **Couleurs : ne jamais inventer un hex ni un nom** (cf. étape 6).

## Outils du skill

- **`palette.py`** — relevé de couleurs (décodeur PNG en Python pur, sans PIL) et génération des nuanciers SVG. `python3 palette.py` sans argument affiche le mode d'emploi et le format du JSON.
