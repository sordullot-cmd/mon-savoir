---
name: univers
description: À partir d'un NOM (jeu vidéo, marque, studio, film, série…), fait une recherche web en éventail pour rapatrier tous les médias créatifs de cet univers (branding/logos, UI/menus, character design/concept art, illustrations/key art, animations/trailers, gameplay/produit) en pleine qualité, génère les nuanciers de couleurs en images (palette déclarée + couleurs réellement relevées dans les écrans), et crée un dossier de référence permanent dans INSPIRATION/UNIVERS/ avec une fiche cherchable. À utiliser quand Sacha dit « fais-moi le dossier de tel jeu/marque », « recherche tout sur X », « je veux les références de X », « récupère la DA / les couleurs / l'UI de X ».
---

# /univers — Dossier de référence complet sur un univers créatif

Transforme un **nom** (pas une URL — pour une URL, c'est `/inspi`) en **dossier de référence permanent** : les médias eux-mêmes, téléchargés en pleine qualité, rangés par aspect + une fiche cherchable. Objectif : que les données **ne disparaissent jamais**, même si les sources en ligne meurent.

Marche pour **n'importe quel univers** : jeu vidéo, marque, studio, film, série, musicien, événement…

**Frontière avec `/inspi`** : *un monde qu'on regarde* (jeu, film, studio, marque) → `/inspi` ne suffit pas, c'est ici. *Un produit numérique qu'on utilise* (app, SaaS, site) → **`/inspi`**, qui produit le même genre de dossier par aspect en tirant les écrans des stores et des bases type Mobbin. Si un univers a une app ou un site à documenter, appeler `/inspi` pour cette partie et ranger le résultat dans le dossier de l'univers.

## Procédure

1. **Identifier l'univers.** Si le nom est ambigu (plusieurs jeux/marques homonymes), demander. Noter le **focus** éventuel de Sacha (« surtout la DA », « juste les logos ») → il pondère la recherche.

2. **Recherche en éventail** (WebSearch/WebFetch ; pour un gros univers, lancer des **agents parallèles**, un par angle). Chercher dans cet ordre de fiabilité :
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

5. **Vérifier un échantillon** (`Read` sur quelques images par aspect) : bonne résolution, bon contenu, rien de hors-sujet. Virer les doublons et les vignettes basse qualité.

6. **Faire les couleurs — en images, pas en texte.** Deux commandes, avec `palette.py` (livré avec ce skill, sans dépendance) :
   ```
   python3 .claude/skills/univers/palette.py releve "INSPIRATION/UNIVERS/<slug>/ui/*.png"
   python3 .claude/skills/univers/palette.py nuancier palette.json "INSPIRATION/UNIVERS/<slug>/couleurs/"
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

10. **Sync vault-gallery** : `npm run index --prefix ~/Documents/GitHub/vault-gallery` et inclure son récap.

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
