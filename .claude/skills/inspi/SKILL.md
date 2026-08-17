---
name: inspi
description: Transforme un lien OU un nom de produit numérique en référence rangée dans INSPIRATION. Site web → capture pleine hauteur de chaque page + composants + animations + walkthrough. App (nom ou lien de store) → dossier complet : écrans en pleine qualité depuis les stores et les bases type Mobbin, flows, branding, couleurs, crédits. Post social (X, Instagram, Pinterest, TikTok, Behance, Dribbble, YouTube…) → média en pleine qualité + fiche. Appelé par /ranger quand un lien arrive, ou directement « ajoute ce site/post en inspi », « fais-moi le dossier de telle app ».
---

# /inspi — Référence d'un produit numérique (site web, app, post)

Transforme une **URL** ou un **nom d'app** en référence rangée : un **dossier** (dans sa discipline) contenant la **source + les visuels + une fiche** décrite → cherchable par allure.

Ce skill couvre **tout le numérique** (sites et apps). Pour un **univers de marque ou de fiction** (jeu vidéo, film, studio, marque non-numérique) → **`/univers`**, qui fait la même chose à l'échelle d'une DA complète. Frontière simple : *un produit qu'on utilise* → `/inspi` ; *un monde qu'on regarde* → `/univers`.

## Trois modes × deux profondeurs

| Ce que donne Sacha | Mode | Profondeur par défaut |
| --- | --- | --- |
| URL de site web | **site** — § Mode site | inspi |
| Nom d'app, `apps.apple.com/…`, `play.google.com/…` | **app** — § Mode app | **dossier** |
| URL de post/pin/vidéo (`x.com`, `instagram.com`, `pinterest.*`/`pin.it`, `tiktok.com`, `behance.net`, `dribbble.com`, `tumblr.com`, `bsky.app`, `threads.net`, `youtube.com`/`youtu.be`, `vimeo.com`…) | **post** — § Mode post social | inspi |

Un lien vers le **profil** d'un compte ou la **home** d'une plateforme n'est ni un post ni un site à capturer → demander à Sacha ce qu'il veut en garder.

**Les deux profondeurs :**
- **inspi** (défaut sites et posts) — un dossier plat, la fiche + les visuels. Rapide.
- **dossier** (défaut pour une app ; sur demande pour un site : « fais-moi le dossier complet de X », « je veux tout sur X ») — la structure par **aspect** héritée de `/univers` : `ecrans/` `flows/` `branding/` `couleurs/` `composants/` `animations/` `marketing/`, plus **crédits** et **sources**. Voir § Niveau dossier.

---

## Mode site

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
7. **Créer la fiche** `INSPIRATION/<DISCIPLINE>/<slug>/<slug>.md` depuis `TEMPLATES/Template-Inspiration.md`. **Remplir TOUS les descripteurs** (c'est ce qui rend la recherche fine) — vocabulaire **contrôlé** listé dans `INSPIRATION/_INSPIRATION.md`, ne pas inventer de synonyme :
   - `discipline:` + `source:` (URL complète) + `media: site`
   - `type_site:` — déduit du contenu/WebFetch (portfolio, agence, saas, e-commerce, éditorial…)
   - `secteur:` — domaine métier (tech, mode, food, luxe…)
   - `couleur_principale:` + `couleurs:` — cf. § Couleurs
   - `anime:` (`oui`/`non`/`léger`) + `animations:` — les types réellement repérés à la **passe animation** (§ ci-dessous) : `scroll-reveal`, `parallaxe`, `loader`, `hover`, `webgl-3d`, `video-bg`, `marquee`… (cohérent avec ce qui est gardé en GIF/MP4). Si site statique → `anime: non`, `animations: []`.
   - `layout:` — structure dominante (grille, asymétrique, plein-écran, split, bento…)
   - `mood:` — ambiance
   - `tags:` du vocabulaire d'`INSPIRATION/_INSPIRATION.md` (discipline + mood + `#a-tester`…)
   - intégrer `![home](home.png)` + une galerie `## Pages du site` avec les autres captures
   - « Pourquoi je l'aime » + « À réutiliser pour »
   - **Fiche = maximum d'informations et de mots-clés** : qui (studio/créateur + client, liens), d'où (URL source), quoi (chaque visuel décrit en une ligne), style — et une section `## Mots-clés` libre et généreuse (synonymes FR/EN) en fin de fiche, carburant de la recherche MemPalace.
   - **Une valeur manque au vocabulaire** (type_site/animation inédit) ? l'ajouter à `_INSPIRATION.md` et le **signaler** dans le récap (cf. `CLAUDE.md` — rester sobre).
8. **Extraire composants + animations** — § Composants et § Passe animation. **Rien d'original → rien.**
9. **Vidéo walkthrough** (AUTOMATIQUE à chaque site) : `python3 .claude/skills/inspi/walkthrough.py "<url>" "INSPIRATION/<DISCIPLINE>/<slug>/walkthrough.mp4"` → l'intégrer dans la fiche via `![[walkthrough.mp4]]`.
10. **Réindexer MemPalace** : `mempalace mine "$HOME/Documents/brain^2" --agent sacha`.
11. **Récapituler** : discipline, slug, nb de pages, composants/anims retenus (ou « aucun »), walkthrough, **descripteurs remplis**, et tout cookie-wall / troncature / valeur de vocabulaire ajoutée.

**Site demandé en profondeur « dossier »** : faire les étapes ci-dessus, puis § Niveau dossier (les captures de pages vont dans `marketing/`, les écrans de l'app web dans `ecrans/`).

---

## Mode app

Une app ne se capture pas au protocole Chrome : ses écrans vivent **dans les stores** et dans les **bases d'UI type Mobbin**. Le résultat est donc toujours un **dossier** (§ Niveau dossier), rangé dans **`INSPIRATION/UI-DESIGN/<slug>/`** (discipline « interfaces, apps, design produit »).

1. **Identifier l'app.** Homonymes (« Arc », « Halide », « Structured ») → demander, ou trancher avec l'éditeur. Noter le **focus** de Sacha s'il y en a un (« surtout l'onboarding », « juste les paywalls ») : il pondère tout le reste.

2. **Écrans des stores en pleine qualité** — c'est la source la plus fiable, publique, sans login :
   ```
   python3 .claude/skills/inspi/grab-app.py "<nom | URL store>" "INSPIRATION/UI-DESIGN/<slug>" \
       [--store ios|android|both] [--country fr] [--ipad] [--max 20]
   ```
   - Récupère l'**icône** + les **écrans** en résolution native (App Store : PNG 1290×2796 ; Play : original via `=s0`) dans `<slug>/ecrans/`, nommés `ios-01-<nom-source>.png` / `android-01.png`.
   - Renvoie un JSON de **métadonnées** (nom, éditeur, bundle/package, catégories, version, date de sortie et de MAJ, note, prix, URL store, site officiel, description) → il remplit directement le frontmatter, ne pas le retaper à la main.
   - Le package Play est déduit du bundle iOS quand il est identique ; sinon **donner l'URL Play** pour l'avoir. Un store absent est signalé dans `errors`, ce n'est pas un échec.
   - Limite assumée : ce sont les écrans **choisis par l'éditeur pour vendre l'app** (souvent habillés, parfois dans un mockup de téléphone) — excellents pour la DA et les écrans phares, insuffisants pour les **flows** et les écrans secondaires. D'où l'étape 3.

3. **Bases d'UI (type Mobbin)** — pour les flows, les écrans secondaires, les patterns. Aucune n'a d'API : chercher par le web (`WebSearch` / `WebFetch`), et si le contenu est derrière login ou anti-bot, passer par **`claude-in-chrome`** dans le Chrome de Sacha (il y est peut-être connecté) plutôt que d'insister en fetch direct.
   - **[Mobbin](https://mobbin.com)** — la référence : iOS/Android/web, écrans indexés par app, par écran et par pattern, flows complets. Compte requis, anti-bot en fetch direct (403) → `claude-in-chrome`.
   - **[Refero](https://refero.design)** — ~30 000 écrans web + iOS, rangés en trois axes : pages d'app, patterns UX, éléments UI. Très bon pour « comment les autres font ce composant ».
   - **[Appshots](https://appshots.design)** — 120 000+ écrans, 400+ apps ; orienté **motion** (l'expérience telle qu'elle se déroule, pas l'écran figé).
   - **[Page Flows](https://pageflows.com)** — flows en **vidéo** (web + mobile) et emails transactionnels : le meilleur pour un parcours (onboarding, checkout, suppression de compte).
   - **[UXArchive](https://uxarchive.com)** — flows mobiles, avec les **versions historiques** d'une app (utile pour montrer une évolution de design).
   - **[Screensdesign](https://screensdesign.com)** — écrans + signaux de revenus/MRR et tagging des paywalls.
   - **[Banani](https://www.banani.co/references)** — gratuit, écrans mobiles copiables.
   - **[Adapty](https://adapty.io)** — collection dédiée aux **paywalls** mobiles (500+ apps) : à ouvrir dès qu'on cherche un écran d'abonnement.
   - **[Webframe](https://webframe.io)** et **[SaaS Landing Page](https://saaslandingpage.com)** — côté web/produit, pages et sections de SaaS.
   - **[WWIT](https://www.whatwasit.co)** — apps **coréennes**, classées par industrie et par pattern (DA très différente de l'occidentale).
   - **Game UI Database** (`gameuidatabase.com`) — si l'app est un jeu, c'est là (déjà utilisé par `/univers`).
   - **Toujours créditer la source** de chaque écran repris d'une de ces bases dans la fiche (elles-mêmes republient : citer la base *et* l'app).

4. **Le produit tourne sur la machine de Sacha ?** (app web, app Mac, ou app iOS via miroir) → c'est la meilleure source. Une **app web** se capture comme un site (`capture-site.py`, `record.py`, `walkthrough.py`) une fois connecté via `claude-in-chrome`. Sinon, demander à Sacha 2-3 captures des écrans qu'il veut garder plutôt que d'inventer.

5. **Site marketing du produit** (souvent trouvé dans le champ `site` du JSON store) → le capturer en mode site, captures dans `marketing/`. C'est là que vivent le branding, la typo et le discours.

6. **Regarder les écrans** (`Read`) — jugement : navigation, densité, typo, arrondis, ombres, ce qui est vraiment singulier. Puis § Niveau dossier pour les couleurs, les composants et la fiche.

**Frontmatter propre à une app** (en plus des descripteurs communs — vocabulaire dans `_INSPIRATION.md`) : `type_app` (`productivité` · `social` · `finance` · `santé` · `média` · `commerce` · `outil` · `jeu` · `ia`), `plateformes` (`ios` · `android` · `web` · `macos`), `editeur`, `version`, `url_store`, `patterns` (`onboarding` · `paywall` · `tab-bar` · `navigation-gestuelle` · `feed` · `recherche` · `parametres` · `empty-state` · `mode-sombre`).

---

## Niveau dossier (app, ou site sur demande)

Le principe de `/univers` appliqué à un produit numérique : **les médias ne doivent jamais disparaître**, même si la source meurt. Sous-dossiers **créés seulement s'ils ont du contenu** :

```
ecrans/       écrans de l'app / de l'app web (stores, bases d'UI, captures)
flows/        parcours : suites d'écrans numérotées (onboarding-01.png…) ou vidéos
branding/     logo, icône, lockups, typo, éléments d'identité
couleurs/     nuanciers (cf. § Couleurs)
composants/   blocs UI remarquables découpés (cf. § Composants)
animations/   transitions, micro-anims, loaders en GIF/MP4 (cf. § Passe animation)
marketing/    site du produit, landing, App Store, campagnes
```

- **Nommage descriptif en kebab** : `onboarding-03-permissions.png`, `paywall-annuel.png`, `logo-monogramme.svg` — jamais `image(3).jpg`.
- **Volume** : la qualité, pas l'exhaustivité — **~20 à 50 médias forts** par défaut (plus si Sacha demande « tout »). Toute troncature ou échec de téléchargement se **signale**.
- **Vérifier un échantillon** par aspect (`Read`) : bonne résolution, bon contenu, pas de doublon ni de vignette.
- **Fiche** depuis `TEMPLATES/Template-Produit.md` : une section par aspect (galerie `![[…]]` + une ligne de description par média marquant), **crédits** (designers/studio identifiés + liens portfolio), **sources** (URLs d'origine pour pouvoir y retourner), « Pourquoi je l'aime », « À réutiliser pour », `## Mots-clés` libre.
- **Indexer** : une ligne dans `INSPIRATION/UI-DESIGN/_APPS.md` (produit, plateformes, aspects couverts, lien `[[fiche]]`) — l'équivalent de `_UNIVERS.md` pour les produits numériques. Les composants et animations vont **aussi** dans leurs index transversaux.

### Couleurs

Deux commandes, une règle :

```
python3 .claude/skills/univers/palette.py releve "<dossier>/ecrans/*.png"     # hex réellement présents
python3 .claude/skills/univers/palette.py nuancier palette.json "<dossier>/couleurs/"   # planches SVG
```

Relever aussi la **charte publiée** si elle existe (press kit, brand guidelines, tokens CSS du site) avec ses vrais noms. **Ne jamais inventer un hex ni un nom** : toute valeur vient soit d'une charte sourcée, soit d'un relevé de pixels — et la fiche distingue les deux. Reporter dans `couleur_principale` + `couleurs`, intégrer les planches dans la fiche.

---

## Mode post social (X, Instagram, Pinterest, TikTok…)

Un post = **le média d'abord** (l'image/la vidéo en pleine qualité, pas un screenshot de l'interface autour). Workflow plus court : pas de composants, pas de walkthrough.

1. **Choisir la discipline d'après ce que MONTRE le post**, pas d'après la plateforme : un tweet d'un dashboard → `UI-DESIGN` ; un pin d'affiche → `GRAPHISME` ; un reel de motion → `MOTION` ; une identité sur Behance → `BRAND-DESIGN` ; un screenshot de site → `WEBDESIGN`. (On ne connaît le contenu qu'après téléchargement → on peut lancer l'étape 2 dans un dossier provisoire du scratchpad, regarder, puis déplacer au bon endroit.)
2. **Télécharger le(s) média(s)** :
   ```
   python3 .claude/skills/inspi/grab-post.py "<url>" "INSPIRATION/<DISCIPLINE>/<slug>/"
   ```
   - Le script détecte la plateforme, essaie `gallery-dl` puis `yt-dlp` (ordre inversé pour les plateformes vidéo), renomme proprement (`post.jpg`, `post-2.jpg`, `post.mp4`…) et renvoie un JSON : fichiers + **meta** (auteur, texte/légende, date, likes) + erreurs éventuelles.
   - **Post derrière login** (Instagram surtout, parfois X) : relancer avec `--cookies` (utilise la session Chrome de Sacha ; macOS peut demander UNE FOIS l'accès trousseau « Chrome Safe Storage » — normal). **Limite connue (août 2026)** : Chrome n'exporte plus le cookie `sessionid` d'Instagram → gallery-dl échoue même avec `--cookies`, et yt-dlp ne récupère que les slides **vidéo** d'un carrousel (ses erreurs `No video formats found` signalent les slides image restantes). Dans ce cas : garder les vidéos obtenues, compter les slides, et récupérer les images par la **capture native par tuiles** (§ ci-dessous).
   - **Échec malgré les cookies** (Instagram refuse souvent ses cookies hors navigateur, post privé, plateforme non supportée) : fallback = **capture native par tuiles** (§ ci-dessous), qui donne la **pleine résolution d'origine**, pas un screenshot réduit de l'interface. Le signaler.
3. **Slug** : ce que le post **montre**, en kebab — `<marque/projet>` ou `<sujet>-<qualificatif>` (ex. `bartolomeu-moveis`, `dashboard-sombre-samdape`, `affiche-suisse-rouge`). **PAS de plateforme dans le nom** (elle vit dans le frontmatter `plateforme:`) ; l'auteur seulement s'il faut désambiguïser. Destination `INSPIRATION/<DISCIPLINE>/<slug>/`.
4. **Regarder le média** (`Read` sur les images ; pour une vidéo, extraire 1-2 frames : `ffmpeg -ss 2 -i post.mp4 -frames:v 1 frame.png`) — jugement : sujet, style, couleurs, mood.
5. **Créer la fiche** `<slug>.md` depuis `TEMPLATES/Template-Inspiration-Post.md` : `discipline`, `source` (URL complète du post), `media: post`, `plateforme`, `auteur` (handle/nom depuis le meta JSON), `sujet`, `couleur_principale` + `couleurs`, `mood`, `tags` — même vocabulaire contrôlé que le reste (`_INSPIRATION.md`). Intégrer le média (`![[post.jpg]]` / `![[post.mp4]]`) et reprendre la **légende du post** (champ `texte` du JSON) en citation si elle éclaire le contenu.
   **Fiche = maximum d'informations et de mots-clés** (demande de Sacha : c'est ce qui rend la recherche MemPalace précise). En plus du frontmatter : **qui** (créateur/studio + client/marque, avec liens), **d'où** (plateforme + URL source + compte relais s'il y a curation), **quoi** (décrire chaque média en une ligne : sujet, support, technique), **style** (courant graphique, références, époque), et une section `## Mots-clés` en fin de fiche avec une liste libre et généreuse de termes de recherche (synonymes FR/EN compris : « identité visuelle, branding, logotype, monogramme, wordmark… »). Le vocabulaire contrôlé reste la règle pour le frontmatter ; la section Mots-clés, elle, est **libre** — c'est du carburant de recherche, pas de la taxonomie.
6. **Réindexer MemPalace** puis **récapituler** : discipline, slug, nb de médias, plateforme/auteur, descripteurs remplis, et tout recours aux cookies / fallback screenshot.

**Cas particuliers** :
- **Plusieurs images dans un post** (carrousel Instagram, tweet à 4 images, board…) : tout garder (`post-1.jpg`…`post-4.jpg`), les intégrer toutes dans la fiche.
- **Lien de board/moodboard Pinterest entier** (pas un pin) : ne pas aspirer les 300 pins — demander à Sacha s'il veut le board complet (et si oui borner, ex. 20 premiers pins) ou juste quelques pins précis.
- **Vidéo YouTube/Vimeo entière** : c'est en général une inspi `MOTION` ; la vidéo peut être lourde → si > ~100 Mo, préférer une qualité moindre (`yt-dlp -f "best[height<=1080]"` à la main) et le signaler.
- **Le post pointe vers un site ou une app** (tweet « nouveau portfolio → lien ») : demander à Sacha s'il veut le post, le produit (mode site/app), ou les deux.

### Fallback — capture native par tuiles (qualité d'origine, via claude-in-chrome)

Quand `grab-post.py` échoue même avec `--cookies`, on peut quand même récupérer les **images à leur résolution native** (ex. 1440×1440 sur Instagram) sans télécharger de fichier : on affiche l'image en taille réelle dans la page et on la capture en tuiles 1:1 qu'on recolle. Méthode validée (post Instagram `domo-brand-identity`, août 2026).

1. **Ouvrir le post** dans le Chrome de Sacha (`claude-in-chrome`, nouvel onglet, il est connecté aux plateformes).
2. **Lister les slides depuis la SOURCE DE VÉRITÉ, jamais depuis le DOM.** PIÈGE VÉCU (post `logosai`, août 2026) : scraper `article img` / `main img` ramasse les vignettes de la grille « autres posts du compte » en bas de page → on range des images d'AUTRES posts en croyant tenir le carrousel. Ne jamais lister les slides en scrapant les `<img>`. À la place, depuis la page (`javascript_tool`), interroger l'**API interne** avec la session du navigateur :
   - `pk` = shortcode décodé en base64url (`A-Za-z0-9-_`, `pk = pk*64 + index(c)`) ;
   - `fetch('https://www.instagram.com/api/v1/media/<pk>/info/', {headers:{'x-ig-app-id':'936619743392459'}, credentials:'include'})` → `items[0].carousel_media[]` : `media_type` (1=image, 2=vidéo), `image_versions2.candidates` (prendre la plus grande). *(Fallback si l'API change : le JSON embarqué `script[type="application/json"]` contenant `carousel_media`.)*
   - **Vérifier le compte** : nb de slides + types doivent coller au post (le compteur « x/8 » visible sur le carrousel). Croiser avec yt-dlp : ses erreurs `No video formats found` sur des slides = ce sont des images (normal), et lui seul télécharge les slides **vidéo**.
   Stocker les URLs dans `window.__slides`, puis `fetch` chaque image et garder son base64 dans `window.__b64`. **Ne renvoyer que des compteurs/dimensions** dans le résultat d'outil.
   - **INTERDIT** : faire sortir les URLs ou le base64 par la sortie d'outil — le filtre anti-exfiltration de l'extension les bloque (`[BLOCKED: …]`) et il ne faut **pas** le contourner par un autre encodage.
   - **Voies mortes déjà testées** (ne pas re-perdre de temps) : `a.click()` + blob download (bloqué sans geste utilisateur réel, même via clic simulé), POST vers un serveur localhost (bloqué par la CSP du site), `curl` du HTML du post (données absentes sans session). Un **vrai clic de Sacha** sur un bouton injecté reste une option de secours pour un téléchargement direct.
3. **Overlay taille native** : injecter un `<div>` fixed plein écran (z-index max) contenant une `<img>` à la **taille native en px CSS** (ex. `width:1080px`). Source de l'img : la **data URL base64** OU, si elle sort en image cassée (la CSP d'Instagram bloque `data:` sur les pages **anonymes**), directement l'**URL CDN** (`img.src = url` — les `<img>` ne sont pas soumis au CORS). Toujours **attendre `onload`** et vérifier `naturalWidth` avant de capturer. Masquer l'UI de la plateforme par un `<style>` injecté (survit aux re-renders React, contrairement aux styles inline). NB : la méthode marche aussi **déconnecté** — le JSON embarqué du post anonyme contient les slides (`candidates[0].url` peut ne pas avoir de `width` → prendre `candidates[0]` + `original_width`, pas un reduce sur `width`).
4. **Mesurer le viewport réel** après `resize_window` au maximum : `innerWidth/innerHeight` + `devicePixelRatio` via JS. Les régions de l'action `zoom` sont en **pixels physiques** du viewport. Attention : `resize_window` a déjà **fait planter Chrome** (le relancer : `open -a "Google Chrome"`, retrouver l'onglet, tout réinjecter) — s'en passer si le viewport suffit.
5. **Capturer en tuiles ≤ 720×720** : action `zoom` + `save_to_disk`. Au-delà de ~1400 px de région, l'outil **redimensionne** la sortie (perte) ; à 720 la tuile sort **1:1**. Entre les tuiles, déplacer l'image par `transform: translate(...)` à **décalages entiers** (ex. 1080×1080 = 4 tuiles de 540, ordre TL TR BL BR).
   **Étalonner l'échelle réelle sur la 1ʳᵉ tuile, ne pas faire confiance au dpr** : le zoom Chrome (≠ 100 %) fausse le rapport device/CSS (vécu : région 540 demandée → tuile 1092 couvrant 617 px CSS, soit 1,7685 device/CSS). Méthode : capturer la tuile TR (`translate(-540px,0)`), mesurer en PIL la **colonne du bord droit du contenu** (`x_bord`) → échelle = `x_bord / (largeur_image − 540)` ; assembler ensuite en collant chaque tuile à `(540·échelle, 0)` etc. sur un canvas device, cropper à `largeur_image·échelle`, redimensionner LANCZOS à la taille native.
6. **Recoller** :
   ```
   python3 .claude/skills/inspi/stitch.py <sortie.png> --cols 2 tuile1.png tuile2.png tuile3.png tuile4.png
   ```
   (tuiles en ordre **ligne par ligne**). Relire le résultat pour vérifier l'absence de raccord.
7. **Nettoyer** : fermer l'onglet. Signaler dans le récap que la qualité vient de la capture du rendu (visuellement identique au fichier source, mais pas les octets d'origine).

Cette méthode ne vaut que pour des **images** — pour une vidéo irrécupérable, fallback = `record.py` sur le post ou frame unique, le signaler.

---

## Composants statiques (sélectif)

> **Deux dossiers, deux index** : `composants/` = blocs UI statiques (`.png`) → [[_COMPOSANTS]] ; `animations/` = sections / intros / micro-anims (`.gif`/`.mp4`) → [[_ANIMATIONS]]. Une **section qui s'anime** va dans `animations/`, pas dans `composants/` (cf. § Passe animation).

- **Où** : les composants statiques vivent **dans le dossier du produit** → `INSPIRATION/<DISCIPLINE>/<slug>/composants/<type>_<slug>.png` (contexte préservé, dossier auto-suffisant). Le **suffixe `_<slug>`** garde les noms uniques pour l'index global.
- **Ne pas tout prendre** : pas un composant par section. Seulement ce qui sort du lot. **Rien d'original → rien à extraire** (le dire). Sauf si Sacha demande un composant précis.
- **Comment** : regarder les captures pleine hauteur (ou les écrans d'app), repérer le composant, le **découper** :
  ```
  python3 .claude/skills/inspi/crop.py "<capture.png>" "INSPIRATION/<DISCIPLINE>/<slug>/composants/<type>_<slug>.png" --box <x> <y> <w> <h>
  ```
  (ou `--band <y_haut> <y_bas>` pour une bande pleine largeur). Coordonnées en pixels de l'image **source**. Vérifier le découpage en le relisant, ajuster si besoin.
- Sur une **app**, les composants intéressants sont souvent : tab bar, sheet/modale, carte de liste, champ de recherche, empty state, paywall, header collant.
- **Indexer** : ajouter une ligne à l'index global `INSPIRATION/COMPOSANTS/_COMPOSANTS.md` (type, source `[[fiche]]`, pourquoi, `![[fichier]]`) + relier depuis la fiche. Le fichier n'est PAS déplacé : l'index ne fait que le référencer.
- Si Sacha demande un composant précis (« prends-moi le footer »), le faire même s'il est banal.

### Passe animation — AUTOMATIQUE & sélective (GIF/MP4)

À faire **automatiquement** sur tout site (et sur toute app web accessible), mais en ne gardant que ce qui est **vraiment cool/stylé** (même exigence que pour les composants — rien de marquant → rien). Outil :
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

**Pour une app**, les animations ne s'enregistrent pas depuis la machine : les prendre chez **Appshots** ou **Page Flows** (vidéos de flows) et les rapatrier avec `yt-dlp` quand c'est possible, sinon décrire le mouvement dans la fiche et le dire. Une app web se traite comme un site.

**Sélectivité** : objectif = quelques pépites animées, pas tout filmer. Si rien ne sort du lot → ne rien garder (le dire). Mais une **section qui s'anime vraiment bien mérite presque toujours un GIF** plutôt qu'un screenshot mort.
**Sortie** : `.gif` (s'anime dans Obsidian, idéal petit format) ou `.mp4` (ffmpeg, plus léger/net en grand). Ranger dans `<slug>/animations/`, indexer dans `_ANIMATIONS.md`.

**Limites** : débit réel ~4-8 fps sur pages lourdes (`--fps` = plafond). Hover/clic = simulation best-effort (peut rater une anim complexe). **Vidéo YouTube/Vimeo** : pas récupérable en vidéo (DRM/streaming) → on prend sa **frame** (miniature), pas le flux.

### Vidéo walkthrough du site complet (AUTOMATIQUE sur un site)

**À générer systématiquement** en mode site — vidéo de tout le site (défilement auto de chaque page, assemblé en un seul MP4) :
```
python3 .claude/skills/inspi/walkthrough.py "<url>" "INSPIRATION/<DISCIPLINE>/<slug>/walkthrough.mp4" [--fps 10 --speed 500 --hold 0.8 --max-pages 8 --pages "/,/about"]
```
- Découvre les pages (1 par template), charge le lazy-load + frames vidéo, scrolle chaque page haut->bas, concatène en `walkthrough.mp4`.
- L'intégrer dans la fiche : `![[walkthrough.mp4]]`.
- C'est l'étape la plus longue (plusieurs lancements Chrome) → la faire en dernier. Sur un **très gros site**, borner avec `--max-pages` et le signaler.

---

## Structures produites

**Site (profondeur inspi)** :
```
INSPIRATION/<DISCIPLINE>/<slug>/
├── <slug>.md             ← fiche : lien + captures intégrées + mood/tags
├── home.png              ← capture PLEINE HAUTEUR
├── <page>.png …          ← pages racine uniques (about, shop…)
├── <groupe>-template.png ← 1 exemple par template (ex. works-template.png)
├── walkthrough.mp4       ← vidéo de tout le site (auto)
├── composants/           ← blocs UI statiques réutilisables
└── animations/           ← sections / intros / micro-anims marquantes

INSPIRATION/COMPOSANTS/_COMPOSANTS.md   ← INDEX transversal des composants (référence, ne stocke pas)
INSPIRATION/ANIMATIONS/_ANIMATIONS.md   ← INDEX transversal des animations (référence, ne stocke pas)
```

**App / produit (profondeur dossier)** :
```
INSPIRATION/UI-DESIGN/<slug>/
├── <slug>.md          ← fiche Template-Produit : store + écrans + couleurs + crédits + sources
├── icone.png          ← icône en pleine résolution
├── ecrans/            ← ios-01-hero.png, android-01.png, captures…
├── flows/             ← parcours numérotés (onboarding-01.png…) ou vidéos
├── branding/          ← logo, lockups, typo
├── couleurs/          ← nuanciers (palette.py)
├── composants/        ← blocs UI remarquables (→ _COMPOSANTS)
├── animations/        ← transitions, micro-anims (→ _ANIMATIONS)
└── marketing/         ← site du produit, landing, page store
```

**Post social** (structure la plus légère) :
```
INSPIRATION/<DISCIPLINE>/<slug>/          ← ex. bartolomeu-moveis (pas de plateforme dans le nom)
├── <slug>.md          ← fiche : source + média(s) intégré(s) + plateforme/auteur/mood/tags
├── post.jpg           ← média(s) du post en pleine qualité (post-2.jpg… si carrousel)
└── post.mp4           ← si le post est une vidéo (ou post.png si fallback screenshot)
```

## Limites (à signaler, pas à cacher)

- **Découverte des pages** = liens présents sur la **home** (1 niveau). Des pages profondes non liées depuis l'accueil peuvent manquer → si Sacha veut une page précise non trouvée, lui demander l'URL et utiliser `--pages`.
- **Images lazy-load** : le capteur **scrolle toute la page** avant la capture pour les déclencher (sinon zones blanches). **Vidéos** : les `<video>` HTML5 sont lancées en muet (capture d'une frame) et les **embeds YouTube sont remplacés par leur miniature** (= une frame de la vidéo, sinon ils sortent blancs en headless). Limite : **Vimeo / players custom** peuvent rester blancs → le signaler et proposer un screenshot manuel.
- **Cookie-walls / RGPD** peuvent masquer une capture. **Préchargeurs** (Framer/SPA) : le `--budget` à 16 s les évite la plupart du temps ; si une capture sort en « loading… », **recapturer** avec un budget plus long (ex. `--budget 25000`) ou demander un screenshot manuel.
- **Login / paywall** : pages protégées non capturables → le signaler.
- **Gros sites** : au-delà de `--max`, troncature signalée → demander à Sacha s'il veut tout.
- **Apps** : les écrans de store sont **promotionnels** (habillés, parfois en mockup) et ne montrent pas les écrans secondaires ni les flows. Les bases type Mobbin exigent presque toutes un **compte** et bloquent le fetch direct (Mobbin répond 403) → `claude-in-chrome`, ou dire honnêtement qu'on n'a que les écrans de store. Le **derrière-le-login** d'une app (compte requis, données réelles) n'est pas accessible sans Sacha.
- **Posts sociaux** : Instagram exige presque toujours `--cookies` ; X marche en général sans, mais peut se mettre à exiger un login (relancer avec `--cookies`). Post **privé** ou plateforme non supportée → fallback capture par tuiles. Les **stories** Instagram (éphémères) et les posts supprimés ne sont pas récupérables.

## Garde-fous

- Ne pas écraser une inspi ou un dossier existant (même slug) → **compléter** l'existant, ou suffixe.
- Les visuels vivent **dans le dossier de l'inspi** (le livrable), jamais dans le scratchpad.
- Vocabulaire de tags **contrôlé** (comme pour les fonts) : réutiliser l'existant, pas de synonyme inventé.
- **Pleine qualité d'abord** : jamais une vignette quand le fichier source existe (`grab-app.py` s'en charge côté stores).
- Usage = **référence personnelle** dans le vault, pas de republication ; toujours **sourcer** chaque famille de médias (et créditer la base d'UI quand un écran en vient).

## Outils du skill

| Script | Rôle |
| --- | --- |
| `capture-site.py` | captures pleine hauteur, 1 page par template |
| `walkthrough.py` | vidéo de défilement de tout le site |
| `record.py` | GIF/MP4 d'une anim (loader, hover, scroll) |
| `crop.py` | découpe un composant dans une capture |
| `grab-app.py` | écrans + métadonnées d'une app depuis App Store / Google Play, en résolution native |
| `grab-post.py` | médias d'un post social (gallery-dl / yt-dlp) |
| `stitch.py` | recolle les tuiles de la capture native |
| `../univers/palette.py` | relevé de couleurs + nuanciers SVG |

## Étape finale — sync vault-gallery

Après toute création ou mise à jour de fiche, lancer
`npm run index --prefix ~/Documents/GitHub/vault-gallery`
et inclure son récap (ajouté / mis à jour / supprimé) dans le compte-rendu.
