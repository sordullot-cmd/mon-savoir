---
name: font
description: Analyse une nouvelle police et crée sa fiche descriptive cherchable par allure (forme, hauteur, mood…). Génère un specimen, mesure les caractéristiques objectives, choisit les descripteurs dans le vocabulaire canonique, crée la fiche, met à jour l'index et réindexe MemPalace. Appelé par /ranger quand une font arrive, ou directement « analyse cette font / crée la fiche de telle police ».
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
5. **Créer la fiche** depuis `TEMPLATES/Template-Font.md` → `ASSETS/FONTS/_FICHES/<Famille>.md` (nom kebab). Inclure une **phrase descriptive en langage naturel** (c'est ce que la recherche sémantique exploite : y glisser les mots « ronde », « haute », « condensée », etc.).
6. **Mettre à jour l'index** : ajouter la ligne au tableau « Index des fonts » de `ASSETS/_ASSETS.md`, ajouter le `[[lien]]` de la fiche dans la liste des fiches, renseigner licence + **commercial** (`à vérifier` si aucun EULA trouvé dans le dossier).
7. **Réindexer MemPalace** : `mempalace mine /Users/smoricet/Documents/KNOWLEDGE --agent sacha`.
8. **Récapituler** : famille, descripteurs retenus, commercial oui/non, et tout nouveau descripteur ajouté (cf. règle ci-dessous).

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
- Ne pas dupliquer une fiche existante : si la famille a déjà une fiche, la **mettre à jour**.
- Le specimen est un fichier temporaire (scratchpad), pas à ranger dans le vault.
