---
name: font
description: Analyse une nouvelle police et crée sa fiche descriptive cherchable par allure (forme, hauteur, mood…). Génère un specimen, mesure les caractéristiques objectives, choisit les descripteurs dans le vocabulaire canonique, fait une recherche web sur la font (foundry, designer, année, inspirations, brandings notables) pour enrichir la fiche, crée la fiche, met à jour l'index et réindexe MemPalace. Appelé par /ranger quand une font arrive, ou directement « analyse cette font / crée la fiche de telle police ».
---

# /font — Analyse & fiche d'une police

Transforme une police brute en **fiche cherchable par allure** (« typo ronde et haute », « grotesque condensée »…). Vocabulaire **contrôlé** : on réutilise l'existant, on n'invente pas de mots-clés à la volée.

## Procédure

1. **Localiser / préparer** la police dans `ASSETS/FONTS/` :
   - **Dossier ou fichier `.otf/.ttf`** → le déplacer dans `ASSETS/FONTS/` (depuis `INBOX/` le cas échéant).
   - **Zip** → l'extraire dans `ASSETS/FONTS/<Famille>/` (`unzip -q`), puis **supprimer le zip** (le binaire ne sert plus). Si le zip crée un sous-dossier unique fourre-tout, remonter les fontes d'un niveau pour garder une arbo propre.
   - Nettoyer les fichiers parasites macOS (`__MACOSX/`, `.DS_Store`).
2. **Analyser** — lancer le script (métriques objectives + specimen visuel) :
   ```
   python3 .claude/skills/font/analyse-font.py "<chemin de la font>" "<scratchpad>/specimen.png"
   ```
   Il renvoie un JSON : `famille`, `graisses`, et `metriques` { `mono`, `proportions` (classe de largeur), `hauteur` + `ratio_hauteur_x`, `contraste_panose`, `panose`, `n_glyphes` }.
3. **Regarder le specimen** (`Read` le PNG) — c'est l'étape de jugement : forme (ronde/géométrique/carrée/anguleuse/organique), classification, casse (capitales-only ?), mood, usage. Croiser avec les métriques (ex. `mono:true` → monospace ; `proportions:condensée` + `hauteur:haute` → display étroit).
4. **Choisir les descripteurs** — **uniquement dans le vocabulaire canonique** de `ASSETS/_ASSETS.md` (§ « Chercher une fonte par allure »).
   - Les champs objectifs (`proportions`, `hauteur`, `contraste`, `mono`/classification, `graisses`) viennent du script.
   - Les champs de jugement (`forme`, `mood`, `usage`, `role`) viennent du specimen.
   - `role` = rôle recommandé : **titre** (display/capitales/fort contraste/hauteur d'x basse → réservé aux gros mots), **texte** (lisible en corps courant), **polyvalente** (les deux). Indice objectif : hauteur d'x **basse** + contraste **fort** penchent vers `titre` ; hauteur d'x **moyenne/haute** + contraste **faible** + bicamérale penchent vers `texte`/`polyvalente`. Ne jamais interdire un usage, juste recommander.
5. **Rechercher la font sur le web** (`WebSearch`, puis `WebFetch` sur les pages pertinentes) pour enrichir la fiche au-delà de l'analyse visuelle :
   - **Foundry / créateur·rice** : qui a dessiné la font, quelle fonderie la distribue, page officielle de la famille.
   - **Année de sortie** et contexte de création.
   - **Inspirations / histoire** : de quoi elle s'inspire (revival ? époque ? autre typo ?), anecdotes de design.
   - **Utilisations notables** : brandings, identités, sites ou produits connus qui l'utilisent. Deux sources à croiser systématiquement : **Fonts In Use** (fontsinuse.com) **et le blog « in use » / showcase de la foundry elle-même** (ex. `pangrampangram.com/blogs/font-in-use/tagged/<font>`) — la foundry met souvent en avant des cas absents de Fonts In Use. Retenir 2 à 5 exemples détaillés, les plus parlants ; les autres peuvent être listés en une ligne.
   - **Images des utilisations** : pour chaque exemple retenu dans « Vue dans », télécharger **1 image représentative** (2 max si le cas est très riche) depuis la page source — en général l'`og:image` ou l'image principale de l'article (`curl -sL` la page, extraire l'URL de l'image, puis `curl -sL -o`). Les ranger dans `ASSETS/FONTS/<Famille>/in-use/`, nommées `<famille>-in-use-<slug-du-cas>.<ext>` (kebab, nom unique dans le vault). Vérifier que le fichier téléchargé est bien une image (`file`), et recompresser si > ~1,5 Mo (`sips -Z 1600 --setProperty formatOptions 80`). Dans la fiche, embarquer chaque image **sous la puce de son exemple** avec `![[<nom-du-fichier>]]`. Pas d'image fiable trouvée → puce sans image ; **jamais d'image hors-sujet ou d'un autre projet**.
   - **Articles / reviews** intéressants (foundry, Typographica, It's Nice That…).
   - Requêtes types : `"<Famille>" font typeface`, `"<Famille>" foundry designer`, `"<Famille>" fonts in use`, `site:fontsinuse.com "<Famille>"`.
   - **Règle d'or : ne rien inventer.** Beaucoup de fonts gratuites/amateur n'ont aucune histoire documentée → dans ce cas laisser les champs à `inconnu` et omettre les sections web de la fiche, plutôt que de broder. Attention aux homonymes : vérifier que les résultats parlent bien de CETTE font (croiser avec le specimen / la foundry).
   - Cette recherche peut aussi aider à trancher la **licence** (étape licence ci-dessous) si le dossier ne contient pas d'EULA.
6. **Créer la fiche** depuis `TEMPLATES/Template-Font.md` → `ASSETS/FONTS/_FICHES/<Famille>.md` (nom kebab). Inclure une **phrase descriptive en langage naturel** (c'est ce que la recherche sémantique exploite : y glisser les mots « ronde », « haute », « condensée », etc.). Remplir les champs de provenance (`foundry`, `designer`, `annee`, `site`) et les sections « Histoire & inspirations », « Vue dans » (avec les images `![[…]]` téléchargées à l'étape précédente) et « Liens » avec les résultats de la recherche web — sections omises si rien de fiable n'a été trouvé.
7. **Mettre à jour l'index** : ajouter la ligne au tableau « Index des fonts » de `ASSETS/_ASSETS.md`, ajouter le `[[lien]]` de la fiche dans la liste des fiches, renseigner licence + **commercial** (`à vérifier` si aucun EULA trouvé dans le dossier).
8. **Réindexer MemPalace** : `mempalace mine "$HOME/Documents/brain^2" --agent sacha`.
9. **Récapituler** : famille, descripteurs retenus, commercial oui/non, provenance trouvée (foundry/designer/année) ou « rien de documenté », et tout nouveau descripteur ajouté (cf. règle ci-dessous).

## Vocabulaire contrôlé (règle dure)

La cohérence du vocabulaire prime sur l'expressivité. Donc :
- **Réutiliser** en priorité les valeurs déjà listées dans `_ASSETS.md` (`forme`, `proportions`, `hauteur`, `contraste`, `casse`, `mood`, `usage`).
- Préférer un terme proche existant plutôt qu'un synonyme neuf (`technique` plutôt que `techy`/`tech`).
- **Créer un nouveau descripteur seulement si rien ne convient vraiment.** Dans ce cas :
  1. le proposer explicitement dans le récap,
  2. l'**ajouter à la liste canonique** dans `ASSETS/_ASSETS.md` (un seul endroit de vérité) **et** dans `TEMPLATES/Template-Font.md`,
  3. ne jamais le laisser exister uniquement dans une fiche isolée.
- Croissance **délibérée et centralisée**, jamais sauvage.

## Licence / commercial

- Chercher un EULA/LICENSE/OFL/README dans le dossier de la font pour déterminer la licence.
- `commercial: oui` seulement si la licence l'autorise clairement (OFL, domaine public, licence achetée). Sinon `non` (perso/demo/trial) ou `à vérifier` (aucune info).

## Garde-fous

- Ne pas deviner les caractéristiques sans avoir regardé le specimen.
- Recherche web : **jamais d'info non sourcée** dans la fiche (pas de designer « probable », pas d'année devinée, pas de branding inventé). Un fait douteux = omis. Toujours garder le lien source dans la section « Liens ».
- La recherche web enrichit la fiche mais ne remplace jamais le jugement sur le specimen : les descripteurs d'allure restent basés sur ce qu'on voit, pas sur le marketing de la foundry.
- Ne pas dupliquer une fiche existante : si la famille a déjà une fiche, la **mettre à jour** (y compris compléter la provenance web si elle manque).
- Le specimen est un fichier temporaire (scratchpad), pas à ranger dans le vault. Les images « in use », elles, sont du contenu durable : elles vivent dans `ASSETS/FONTS/<Famille>/in-use/` et sont référencées par la fiche.

## Étape finale — publier

Après toute création ou mise à jour de fiche, dérouler
**`.claude/skills/_lib/publier.md`** : réindexer le site
(`npm run index --prefix ~/Documents/GitHub/vault-gallery`), puis **commiter et
pousser les deux dépôts** — le vault (`~/Documents/brain^2`) et le site
(`~/Documents/GitHub/vault-gallery`, dont le push déclenche le déploiement Vercel).
Non bloquant : un échec se signale dans le récap, il ne fait pas échouer le run.
