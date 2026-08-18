# Catalogue des sources — une source = un sous-agent

Lu par `/inspi` au moment de composer l'éventail (§ Récolte multi-sources du SKILL).
Chaque **bloc** ci-dessous est une **piste confiée à UN sous-agent**. Ne jamais donner
deux blocs au même agent : le but est que chacun creuse SA source à fond et rapporte
ce que les autres ne verront pas.

Colonnes : ce qu'on y trouve · comment y entrer · ce qui bloque.

---

## 1. Source officielle (toujours dans l'éventail)

| Source | Ce qu'on y trouve | Accès |
| --- | --- | --- |
| Stores (App Store / Play) | écrans promo en résolution native, icône, métadonnées | `grab-app.py`, public |
| Site du produit / de la marque | branding, typo, discours, captures produit | `capture-site.py` |
| **Press kit / brand assets** (`/press`, `/brand`, `/media`, `/newsroom`, `/about/brand`) | **logos vectoriels officiels, palette déclarée, règles d'usage** | souvent un ZIP direct — chercher explicitement, c'est la meilleure source de branding |
| Design system / docs publiques (`design.<marque>.com`, `<marque>.design`) | tokens, couleurs nommées, composants, règles | public quand il existe |
| Changelog / blog produit | refontes, avant/après, intentions de design | public |

## 2. Bases d'UI mobile

| Source | Ce qu'on y trouve | Accès |
| --- | --- | --- |
| [Mobbin](https://mobbin.com) | la référence : écrans indexés par app, par écran et par pattern, flows complets iOS/Android/web | compte requis, 403 en fetch direct → `claude-in-chrome` |
| [UXArchive](https://uxarchive.com) | flows mobiles + **versions historiques** d'une app (évolution du design) | public |
| [Appshots](https://appshots.design) | 120 000+ écrans, orienté **motion** (l'expérience en mouvement) | public |
| [Page Flows](https://pageflows.com) | parcours en **vidéo** + emails transactionnels | compte |
| [Screensdesign](https://screensdesign.com) | écrans + signaux MRR + tagging paywalls | public partiel |
| [Adapty](https://adapty.io) | collection dédiée aux **paywalls** (500+ apps) | public |
| [WWIT](https://www.whatwasit.co) | apps **coréennes** par industrie et pattern (DA très différente) | public |
| [Banani](https://www.banani.co/references) | écrans mobiles copiables | public |

## 3. Bases d'UI web / galeries de sites

| Source | Ce qu'on y trouve | Accès |
| --- | --- | --- |
| [Refero](https://refero.design) | ~30 000 écrans web + iOS, par page / pattern UX / élément UI | public partiel |
| [Land-book](https://land-book.com), [Godly](https://godly.website), [Minimal Gallery](https://minimal.gallery), [Httpster](https://httpster.net), [SiteInspire](https://siteinspire.com), [Lapa Ninja](https://lapa.ninja), [One Page Love](https://onepagelove.com) | le site déjà repéré et **décrit** par des curateurs (tags, catégorie, souvent le studio crédité) | public |
| [Awwwards](https://awwwards.com), [FWA](https://thefwa.com), [CSSDA](https://cssdesignawards.com) | **la fiche d'award** : studio, équipe nominative, technos, souvent une vidéo du site | public |
| [Webframe](https://webframe.io), [SaaS Landing Page](https://saaslandingpage.com) | sections et pages de SaaS découpées | public partiel |
| [Game UI Database](https://gameuidatabase.com) | si c'est un jeu — déjà utilisé par `/univers` | public |

## 4. L'auteur — le bloc le plus rentable

Un visuel isolé est presque toujours **l'extrait d'un projet complet publié ailleurs**.
Un pin Pinterest → le projet Behance de 30 images en pleine résolution. C'est cette
source qui transforme 1 image en dossier.

| Source | Ce qu'on y trouve | Accès |
| --- | --- | --- |
| [Behance](https://behance.net) | le **projet complet** : process, déclinaisons, mockups, crédits d'équipe | public |
| [Dribbble](https://dribbble.com) | shots + parfois les fichiers sources, l'auteur, ses autres travaux | public |
| Portfolio perso du designer/studio (souvent lié depuis le footer, l'award, ou la bio) | la **version haute qualité** des visuels + le contexte client | public |
| [Read.cv](https://read.cv) / [Layers](https://layers.to) | qui a fait quoi, dans quelle équipe, à quelle période | public |
| [Fonts In Use](https://fontsinuse.com) | quelle typo sur quel projet, avec l'analyse | public |
| [Brand New](https://underconsideration.com/brandnew) | **analyse critique d'une identité** : avant/après, applications, avis argumenté | partiellement payant |
| X / Instagram / Threads du studio ou du designer | making-of, previews animées, versions écartées — introuvables ailleurs | `grab-post.py`, cookies si login |

## 5. Presse et contexte design

| Source | Ce qu'on y trouve | Accès |
| --- | --- | --- |
| It's Nice That, Creative Boom, Design Week, Fast Company (Co.Design), The Brand Identity, Eye on Design | l'article de refonte : **l'intention**, les visuels officiels HD fournis par l'agence, les crédits complets | public |
| YouTube / Vimeo | product tour, design talk, case study animé, reel d'agence | `yt-dlp` |
| Wikipedia / Wikimedia Commons | **logos en SVG officiel**, historique des versions du logo, dates | public, réutilisable |
| [SVGPorn](https://svgporn.com), [Worldvectorlogo](https://worldvectorlogo.com), [Seeklogo](https://seeklogo.com) | logos vectoriels quand il n'y a pas de press kit | qualité à vérifier (redessins amateurs fréquents) |

---

## Composer l'éventail (qui envoyer, selon le mode)

Ne pas lancer les 5 blocs à chaque fois. **4 à 6 agents**, choisis selon la cible :

- **App** → officiel (1) · UI mobile (2) · auteur/équipe (4) · presse (5) · web si l'app a un pendant web (3)
- **Site** → galeries + awards (3) · auteur/studio (4) · presse (5) · réseaux du studio (4bis)
- **Post social** → auteur (4) **en priorité, dédoublé** : un agent sur le compte lui-même, un agent sur « ce même projet publié ailleurs » · marque/projet (1) · presse (5)
- **Produit web (SaaS)** → officiel (1) · web (3) · UI mobile si app compagnon (2) · auteur (4)

Toujours **au moins deux sources indépendantes** : une officielle et une tierce.
Une seule source = angle mort garanti (l'officiel ne montre que ce qu'il veut vendre ;
le tiers ne montre que ce qui a plu à un curateur).
