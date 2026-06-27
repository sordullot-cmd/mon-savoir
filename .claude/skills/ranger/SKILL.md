---
name: ranger
description: Vide et range intelligemment l'INBOX du vault Obsidian. Classe chaque item (devis, facture, image inspi, asset, font, vidéo, lien, note), le déplace dans le bon domaine, crée la fiche depuis le template et met à jour les index. À utiliser quand l'utilisateur dépose un nouvel item dans INBOX ou demande de « ranger / vider l'inbox / trier ».
---

# /ranger — Triage automatique de l'INBOX

Range les items de `INBOX/` dans le vault en respectant ses conventions. **Hybride** : auto-range l'évident, **demande seulement si ambigu**. Crée toujours la **fiche** + met à jour les **index**.

Deux modes selon la charge (cf. § Procédure) : **léger/séquentiel** pour quelques items, **orchestré** (un agent d'analyse par item lourd, en parallèle + un agent relations/dédup) pour les INBOX volumineuses ou lourdes. Les règles de fond sont identiques dans les deux modes ; seule l'exécution des écritures (mv, fiches, index) reste **toujours centralisée et séquentielle**.

## Procédure — deux modes

`/ranger` choisit son mode selon la taille et le poids de l'INBOX, **toujours en suivant les mêmes règles** (classement, conventions, quand demander, garde-fous, détail — sections ci-dessous, valables dans les deux modes).

1. **Lister** le contenu de `INBOX/` — ignorer `À-PROPOS.md` (c'est le guide, jamais le ranger).
2. **Choisir le mode** :
   - **Mode léger (séquentiel)** — défaut si **≤ 3 items** *ou* tous légers (notes, liens, images simples). Pas d'agents : on inspecte, on relie, on range soi-même. Bas coût, latence minimale.
   - **Mode orchestré (agents)** — si **≥ 4 items** *ou* présence d'items **lourds** (PDF multipage à rendre+lire, polices à analyser, sites à screenshoter). On parallélise l'**analyse** ; on garde l'**exécution** centralisée.

### Mode léger
2L. **Inspecter chaque item** (cf. § Inspection ci-dessous : lire le contenu, rendre les PDF, ne rien présumer).
3L. **Relations entre items** (cf. § Relations).
4L. **Classer** + niveau de **confiance** (tableau § Règles de classement).
5L. **Plan** : tableau récap `item → destination → action → confiance` ; items ambigus → UNE question groupée (§ Quand demander).
6L. **Exécuter** : `mv` (jamais `rm`/`cp`) → créer la fiche → mettre à jour index/MOC.
7L. **Réindexer MemPalace** (`mempalace mine … --agent sacha`) puis **récapituler**.

### Mode orchestré
2O. **Triage rapide** (orchestrateur, sans agent) : un coup d'œil pour typer chaque item et repérer ceux qui sont **lourds**. Sert juste à savoir quoi déléguer.
3O. **Fan-out d'analyse — un agent par item lourd, en parallèle** (plusieurs appels `Agent` dans un **même message** → ils tournent concurremment ; type `general-purpose`). Chaque agent **analyse uniquement**, ne déplace/écrit **rien** dans le vault, et renvoie un **rapport structuré** :
   - type, métadonnées (dates, montants, n°, client, **identité de facturation** lue, source), **toutes** les pages lues (cf. § Inspection),
   - destination + nom de fichier proposés, niveau de confiance, questions éventuelles,
   - indices de **relation** (même client/thème, doublon potentiel),
   - un **brouillon de fiche** prêt à coller.
   > L'agent lit TOUT (toutes les pages, tout le contenu) et ne présume rien — c'est le cœur du gain. Les items légers, l'orchestrateur les fait lui-même en parallèle de l'attente.
4O. **Agent “relations & dédup”** (après réception de tous les rapports) : il lit **les rapports** (pas les fichiers bruts) et renvoie les **doublons** à supprimer, les **regroupements** (même client/projet → même sous-dossier + fiches reliées), et les **liens croisés** à poser. C'est lui qui aurait attrapé « Maison Terracotta » (2 devis liés) et un vrai doublon.
5O. **Plan consolidé** : l'orchestrateur fusionne les rapports + les relations en un tableau récap ; items ambigus → UNE question groupée (§ Quand demander).
6O. **Exécution centralisée et SÉQUENTIELLE** (orchestrateur seul, jamais les agents) : tous les `mv`, créations de fiches et surtout les **éditions d'index/MOC partagés** (`_DEVIS-FACTURES.md`, `_ASSETS.md`, fiches client) se font **un par un** — les fichiers partagés ne doivent jamais être écrits par deux agents en parallèle (sinon écrasement). Fonts → `/font`, sites → `/inspi`, lancés **un à la fois** pour la partie qui touche l'index.
7O. **Réindexer MemPalace une seule fois** à la fin, puis **récapituler**.

> Pourquoi ce découpage : le coûteux (rendre/lire des PDF, analyser des polices) est **parallélisable et isolable** → agents. Le fragile (état partagé : index, fiches client) doit rester **sérialisé** → orchestrateur. Les agents ne corrigent l'erreur de lecture que s'ils ont le mandat strict « lis tout, ne présume rien » — il est dans le § Inspection.

## Inspection (les deux modes)

Inspecter chaque item : extension + contenu (lire le texte/PDF/docx, extraire dates, montants, client, numéro, identité de facturation, URL source).
- **PDF illisible** (texte extrait brouillé → police « sous-ensemble », pas de lib pdftotext/pypdf) : ne **jamais deviner** les montants/dates. Rendre le PDF en image puis le **lire visuellement** :
  `qlmanage -t -s 2000 "fichier.pdf" -o <scratchpad>` → lire le `.png` généré. (Fallback : `sips -s format png`.)
- **PDF multipage: `qlmanage`/`sips` ne rendent QUE la 1ʳᵉ page.** Le total, le périmètre et le bloc client sont souvent en page 2-3-4. **Toujours rendre TOUTES les pages** et toutes les lire avant de remplir une fiche. Rendu multipage via PDFKit (intégré macOS, aucun install):
  ```
  osascript -l JavaScript <<'JXA'
  ObjC.import('PDFKit'); ObjC.import('AppKit');
  var p=$.NSProcessInfo.processInfo.arguments;
  var src=ObjC.unwrap(p.objectAtIndex(4)), out=ObjC.unwrap(p.objectAtIndex(5));
  var d=$.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath(src));
  for(var i=0;i<d.pageCount;i++){var pg=d.pageAtIndex(i),r=pg.boundsForBox($.kPDFDisplayBoxMediaBox),s=2;
  var im=$.NSImage.alloc.initWithSize($.NSMakeSize(r.size.width*s,r.size.height*s));im.lockFocus;
  $.CGContextScaleCTM($.NSGraphicsContext.currentContext.CGContext,s,s);
  pg.drawWithBoxToContext($.kPDFDisplayBoxMediaBox,$.NSGraphicsContext.currentContext.CGContext);im.unlockFocus;
  var rep=$.NSBitmapImageRep.imageRepWithData(im.TIFFRepresentation);
  rep.representationUsingTypeProperties($.NSBitmapImageFileTypePNG,$.NSDictionary.dictionary).writeToFileAtomically($(out+"_p"+(i+1)+".png"),true);}
  JXA
  ```
  Appel : `osascript -l JavaScript /chemin/render.js "<pdf>" "<scratchpad>/specimen"` → lire chaque `_pN.png`.
- **Détail = ne rien présumer.** Deux fichiers au nom voisin (`… - Light`, `… v2`, `Copie de …`) **ne sont pas forcément le même document**: vérifier le **numéro**, le **montant** et le **périmètre** de chacun avant de conclure (piège vécu: un « Devis … Light » était en réalité un **autre devis** — numéro et total différents). En cas d'écart, ce sont **deux items distincts** → deux fiches.

## Relations entre items (les deux modes)

Après avoir lu *tous* les items, avant de ranger : repérer les **liens** dans le lot — doublons exacts (même fichier deux fois → n'en garder qu'un, signaler), variantes du même document (vérifier d'abord que c'en est vraiment une, cf. piège « Light »), ou items d'un **même thème/client/projet** (ex. deux devis pour le même client → fiches reliées entre elles + regroupées dans le même sous-dossier). Tenir compte de ces relations dans le rangement (regrouper, relier, dédupliquer) plutôt que traiter chaque item en aveugle. *(En mode orchestré, c'est l'agent “relations & dédup” qui produit cette analyse.)*

## Règles de classement

| Item détecté | Destination | Fiche à créer | Index à mettre à jour |
|---|---|---|---|
| `.pdf`/`.docx` contenant « devis » ou « facture » | `SORDULO/DEVIS-FACTURES/{Sacha-Moricet \| Mael-Auzenet}/{CLIENT}/` (d'abord par **micro**, puis **sous-dossier par client** en UPPERCASE) | `Template-Devis` (+ `Template-Client` si le client n'a pas encore de fiche, cf. § Client) | tableau « Suivi global » de `SORDULO/DEVIS-FACTURES/_DEVIS-FACTURES.md` |
| Image ressource réutilisable (mockup, icône, texture, logo, kit) | `ASSETS/{MOCKUPS \| ICONS \| TEXTURES-PATTERNS \| LOGOS \| TEMPLATES-DESIGN}/` | aucune | — |
| Vidéo / motion (`.mp4`, `.mov`…) ou lien vidéo d'inspi | `INSPIRATION/MOTION/` | `Template-Inspiration` (`media: vidéo`) si pertinent | — |
| Lien de **site / inspiration visuelle** (`.url`, `.webloc`, ou note ne contenant qu'une URL) | `INSPIRATION/<DISCIPLINE>/<slug>/` (webdesign, ui-design, brand-design, graphisme, motion) | **déléguer à `/inspi`** (capture tout le site + fiche) | — |
| Image d'inspiration (UI, brand, print…) | `INSPIRATION/<DISCIPLINE>/` selon le sujet | `Template-Inspiration` | — |
| Police (`.otf`, `.ttf`, `.woff`, ou dossier/zip de fonts) | `ASSETS/FONTS/` | `Template-Font` → `ASSETS/FONTS/_FICHES/<Famille>.md` | tableau « Index des fonts » de `ASSETS/_ASSETS.md` |
| Note texte / idée / réunion | domaine deviné `UNOWHY/` `SORDULO/` `ICAN/` | `Template-Projet` si c'est un projet | relier dans le `_MOC` du domaine |

## Conventions du vault (à respecter)

- **Dossiers top-niveau en UPPERCASE** ; index/MOC = `_NOM.md` ; dashboard = `ACCUEIL.md`.
- **Frontmatter YAML** en tête de toute note (voir les templates dans `TEMPLATES/`).
- **Relier** avec `[[liens]]` et `#tags`.
- **Nommage** : kebab-case lisible. Pour devis/factures, préfixer par le numéro : `2026-001_facture_<client>.pdf` ; si le devis porte sur un objet précis, l'ajouter : `2026-005_devis_<client>_<objet>.pdf` (ex. `…_drive`). Nommer la fiche `Devis <client> [<objet>] <numéro>.md` et y refléter l'objet dans le titre/description (ne pas rester générique « plateforme » si c'est en réalité « fonctionnalité drive »).
- **Rangement par micro PUIS par client** : `DEVIS-FACTURES/{micro}/{CLIENT}/`. La micro est l'**unité fiscale** (numérotation + déclarations URSSAF par micro) → on range d'abord par micro ; le sous-dossier client donne le second tri. Les PDF **restent ici** ; la fiche client (`SORDULO/CLIENT/`) ne stocke pas les binaires, elle les **relie**.
- Micro-entreprise du devis : déduire de l'émetteur/contenu (Sacha Moricet vs Maël Auzenet) — au besoin recouper avec les fiches `SORDULO/ADMINISTRATIF/Micro-Sacha-Moricet.md` et `Micro-Mael-Auzenet.md` (SIRET, n° TVA, RIB, adresse). Le dossier réel est `Mael-Auzenet` **sans accent** (l'index l'écrit avec accent — garder le dossier sans accent).
- Le **code** ne vit jamais dans le vault (notes + assets design uniquement).

### Renommer les fichiers mal nommés (d'après le contenu)

**Après avoir lu un fichier**, si son nom est vague, partiel ou auto-généré, le **renommer** d'après son contenu. **Si le nom est déjà clair et conforme → ne pas y toucher.**

Noms à corriger (exemples) : `devis_2026`, `facture`, `IMG_1234`, `Capture d'écran 2026-…`, `sans-titre`, `Untitled`, `Document`, `Final`, `v3`, `Copie de …`, `Sans nom`.

Cible = **kebab-case descriptif** avec l'info qui identifie : *type + qui/quoi + date/numéro si pertinent*.

| Avant | Après |
| --- | --- |
| `devis_2026.pdf` | `2026-001_devis_<client>.pdf` |
| `facture.pdf` | `2026-001_facture_<client>.pdf` |
| `IMG_4821.png` (réf UI) | `inspi_<sujet>_<source>.png` |
| `Capture d'écran ….png` (mockup) | `mockup_<device>_<contexte>.png` |
| `Notes réunion.md` | `<AAAA-MM-JJ>_reunion_<sujet>.md` |

Règles : garder l'**extension** ; renommer la **fiche `.md` associée** de façon cohérente avec le fichier source ; ne **jamais écraser** un fichier existant (suffixe `-2` au besoin) ; si une info manque pour nommer correctement (ex. client inconnu), la **demander** (cf. § Quand demander) plutôt que d'inventer.

## Quand demander (ambigu) — sinon ranger sans demander

Poser une question seulement dans ces cas, et **groupées** en un seul message :
- **Image** : réf d'inspiration *ou* asset réutilisable ? (et si asset, quelle catégorie)
- **Devis/facture** : micro indéterminable depuis le contenu → Sacha ou Maël ?
- **Devis/facture — client** : si le client n'est **pas renseigné** sur le document (placeholders type `[Raison sociale du client]`), ou s'il **n'a pas encore de fiche** dans `SORDULO/CLIENT/` → **demander le nom du client** (et son contact si dispo) pour pouvoir créer la fiche `Client` et la relier. Ne pas inventer ni laisser le devis « orphelin ». Cf. § Client.
- **Note texte** : domaine non évident (Unowhy / Sordulo / ICAN) → lequel.
- Tout fichier inclassable → laisser dans l'INBOX et le signaler.

> Un devis/facture sans client identifiable **n'est pas une confiance haute**: on peut ranger le fichier dans le bon dossier micro, mais il faut **demander le client avant de finaliser** la fiche (sinon la fiche et l'index restent incomplets).

## Remplissage des fiches

- **Devis** : remplir `client`, `micro-entreprise`, `numero`, `montant_ht`, `statut`, `date_emission`, `date_paiement` (si présents), et lier le PDF dans la section *Fichiers*. Ajouter la ligne correspondante au tableau de suivi global. Le champ `client` doit pointer vers une **vraie fiche client** (`[[Nom du client]]`), pas du texte libre.
- **Client** : si le client du devis/facture **n'a pas encore de fiche**, la créer depuis `Template-Client` dans `SORDULO/CLIENT/<NOM-CLIENT>/_<NOM-CLIENT>.md` (NOM en UPPERCASE, comme `RAW-STUDIO`), renseigner `micro-entreprise` + le contact connu, puis **relier dans les deux sens** : la fiche client liste le devis (section *Devis & factures*) et le devis pointe vers la fiche client. Si le client existe déjà, ne pas dupliquer : juste ajouter le devis à sa fiche. Ne jamais créer une fiche client avec un nom deviné — toujours partir du nom **confirmé par Sacha** (cf. § Quand demander).
  - **Identité de facturation** : le bloc « client » du devis/facture contient souvent l'**adresse**, le **SIRET / n° fiscal**, voire le **n° TVA** du client. Les reporter dans la section *Identité (facturation)* de la fiche client (source de vérité unique) — pas dans chaque fiche devis. Si l'info est absente (ou client étranger sans SIRET FR, ex. société marocaine), le noter explicitement plutôt que d'inventer. *(L'émetteur — SIRET/RIB/adresse de la micro — vit dans `SORDULO/ADMINISTRATIF/Micro-*.md`, pas dans la fiche client.)*
- **Inspiration** : remplir `source` (URL ou nom), `media`, et proposer `mood`/`tags` d'après le contenu. Pour une image, intégrer `![capture](chemin)`.
- **Font** : **déléguer au skill `/font`** (`.claude/skills/font/SKILL.md`) — il déplace la police dans `ASSETS/FONTS/`, l'analyse (specimen + métriques), crée la fiche descriptive dans `_FICHES/`, met à jour l'index et réindexe MemPalace. Ne pas réimplémenter ici.

## Garde-fous

- Jamais de suppression. Déplacement uniquement (`mv`).
- En cas de doute sur l'écrasement d'un fichier existant : renommer, ne pas écraser.
- **Ne jamais inventer une donnée d'un document.** Si un PDF ne s'extrait pas en texte (police « sous-ensemble », glyphes brouillés), **le regarder** : le convertir en image (`qlmanage -t -s 2000 "fichier.pdf" -o <scratchpad>`, fallback `sips -s format png`) et lire le `.png`. On ne remplit montants/dates/client qu'à partir de ce qu'on a réellement lu.
- Toujours finir par un récap clair et l'état de l'INBOX.
