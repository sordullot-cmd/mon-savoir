---
type: moc
tags: [moc, inspiration, composants]
---

# Composants

> Index **transversal** des **blocs UI statiques réutilisables** repérés dans les inspirations (footer, hero, index, pricing…).
> Les fichiers **restent dans le dossier de leur site** (`INSPIRATION/<DISCIPLINE>/<slug>/composants/`) ; cette note ne fait que les **référencer**. Sélectif : seulement ce qui sort du lot.
> Pour les sections / intros / micro-animations (GIF / MP4) → voir [[_ANIMATIONS]].

## Composants

| Type | Source | Pourquoi | Aperçu |
| --- | --- | --- | --- |
| Tableau de marchés à onglets | [[kraken]] | Dense et lisible sans une seule bordure : la hiérarchie tient au seul espacement. Onglets pilule pour changer de marché. | `UI-DESIGN/kraken/composants/tableau-marches-onglets_kraken.png` |
| Feuille d'actions (bottom sheet) | [[kraken]] | Buy / Sell / Convert / Deposit / Withdraw, une ligne par action avec icône cerclée **et sous-titre explicatif**. Le menu qui explique au lieu de lister. | `UI-DESIGN/kraken/composants/feuille-actions-buy-sell-convert_kraken.png` |
| Carte produit pleine largeur (VIP, chrome) | [[kraken]] | Une carte arrondie par univers produit, chacune avec sa 3D et sa dominante. Présente plusieurs offres sans faire une grille tiède. | `UI-DESIGN/kraken/composants/carte-produit-vip-chrome_kraken.png` |
| Carte produit pleine largeur (Krak, cartes bancaires) | [[kraken]] | Même gabarit, autre matière — montre comment le système tient sur plusieurs sujets. | `UI-DESIGN/kraken/composants/carte-produit-krak-cartes_kraken.png` |
| Footer six colonnes | [[kraken]] | Assume une densité SEO énorme sans devenir illisible. | `UI-DESIGN/kraken/composants/footer-multicolonnes_kraken.png` |
| Cartes de série, deux états (feu / gelée) | [[yazio]] | Le même composant en récompense et en pénalité, joué par la mascotte : météore de feu vs prisonnier d'un glaçon. Le gel de série n'est pas une punition, c'est une autre scène. | `UI-DESIGN/yazio/composants/cartes-streak-feu-et-glace_yazio.png` |
| Bandeau plein aplat chevauché par un carrousel | [[yazio]] | Le bandeau menthe est coupé net par les cartes qui débordent dessus — une seule couleur, deux plans. | `UI-DESIGN/yazio/composants/bandeau-mint-carrousel-cartes_yazio.png` |
| Bento de quatre fonctionnalités | [[yazio]] | Grille stricte, la variation vient uniquement de l'aplat pastel et de l'illustration de mascotte. | `UI-DESIGN/yazio/composants/bento-4-fonctionnalites_yazio.png` |
| Bento de témoignages avant/après | [[yazio]] | Blocs de texte sur aplat mêlés à des photos, badge de résultat en pilule noire posée sur l'image. | `UI-DESIGN/yazio/composants/temoignages-avant-apres_yazio.png` |
| Bouton en pilule à arête basse | [[duolingo-app]] | Une arête de 4 px d'un ton plus foncé sous chaque bouton plein (`#1899D6` sous le bleu, `#4EAD10` sous le vert). Sensation de bouton enfonçable, sans ombre ni dégradé. Visible sur tous les écrans d'exercice. | `UI-DESIGN/duolingo-app/ecrans/planches/planche-exercices-duolingo.png` |
| Tableau comparatif à une seule coche | [[duolingo-app]] | FREE vs SUPER en cinq lignes, dont **une seule** cochée côté gratuit. Plus lisible et plus violent qu'une liste d'avantages. | `UI-DESIGN/duolingo-app/composants/tableau-comparatif-free-vs-super_duolingo-app.jpg` |
| Panneau de cœurs avec upsell (server-driven) | [[duolingo-app]] | Refill / SUPER Unlimited dans une même feuille. Duolingo documente que ce composant est **rendu depuis le serveur** : l'upsell change sans mise à jour de l'app. | `UI-DESIGN/duolingo-app/composants/panneau-coeurs-upsell-super_duolingo-app.png` |
| Labels de difficulté au-dessus de la consigne | [[duolingo-app]] | PREVIOUS MISTAKE (orange) et HARD EXERCISE (rouge), posés au-dessus de la consigne. Un composant minuscule qui recadre la lecture de tout l'écran. | `UI-DESIGN/duolingo-app/composants/labels-de-difficulte-exercice_duolingo-app.png` |
| Neuf blasons de ligue | [[duolingo-app]] | Une seule plume déclinée en matière et en forme — nacre, bronze, argent, cuivre, or, platine, puis trois hexagones. La progression se lit à la matière avant le nom. | `UI-DESIGN/duolingo-app/composants/badges-neuf-ligues_duolingo-app.png` |
| Grille d'états d'un widget | [[duolingo-app]] | Une trentaine d'états : la mascotte change d'humeur **et** de couleur de fond selon l'état de la série. Le composant le plus expressif du produit, et il vit hors de l'app. | `UI-DESIGN/duolingo-app/composants/widget-grille-complete-des-etats_duolingo-app.png` |
| Coffre en trois états | [[duolingo-app]] | Le même objet fermé, verrouillé, ouvert. Le minimum pour qu'une récompense se raconte. | `UI-DESIGN/duolingo-app/composants/coffre-trois-etats_duolingo-app.png` |
| Accueil V1 : tab bar + trois actions rondes | [[monobank]] | Le solde en grand, trois actions rondes dessous, l'historique en liste, et une tab bar à quatre entrées. L'état de l'art de 2018, utile pour mesurer ce qui a changé. | `UI-DESIGN/monobank/composants/2018-accueil-tab-bar-actions-rondes_monobank.png` |
| Variables Figma : primitives + tokens sémantiques | [[headspace]] | Deux collections séparées — les valeurs brutes d'un côté, les rôles light/dark de l'autre. 85 % des fichiers de design tirés du système. | `UI-DESIGN/headspace/composants/design-system-variables-figma-primitives-et-tokens_headspace.png` |
| Bottom sheet « Choose your teacher » | [[headspace]] | Carte carrousel avec portrait et bio du professeur, pagination trois points, par-dessus le player assombri. Choisir une voix, pas un réglage. | `UI-DESIGN/headspace/composants/bottom-sheet-choose-your-teacher_headspace.png` |
| Système « sprite » : photo détourée + visage | [[headspace]] | Une photo dans une forme de cadrage, plus un visage graphique. Règle associée : « apply sprites sparingly, leaving ample time between their appearances ». | `UI-DESIGN/headspace/composants/systeme-sprite-photo-detouree-et-visage_headspace.png` |
| 269 bâtiments, 13 catégories × 8 niveaux | [[fortune-city]] | La montée en niveau suit toujours la même grammaire : plus d'étages + un aménagement de parcelle + un objet-enseigne géant en toiture. Une catégorie = une gamme chromatique. | `UI-DESIGN/fortune-city/composants/planches/planche-les-13-categories-de-batiments.png` |
| Gabarit de carte produit décliné 269 fois | [[fortune-city]] | Le même cadre — dégradé turquoise, silhouettes en filigrane, logo en bas à droite — pour chaque item du catalogue. Un système de présentation, pas des images une par une. | `UI-DESIGN/fortune-city/composants/gabarit-carte-produit-d-un-batiment_fortune-city.jpg` |
| Chaîne d'évolution d'un bâtiment | [[fortune-city]] | L'étal devient supérette 24 h, le fleuriste passe de la graine au tournesol géant, la série se termine par un point d'interrogation. | `UI-DESIGN/fortune-city/composants/chaine-d-evolution-d-un-batiment_fortune-city.jpg` |
| Échelle d'humeur 1→5, en deux variantes | [[finch]] | Le même contenu dessiné deux fois pour deux contextes : version bouton et version calendrier. | `UI-DESIGN/finch/composants/emotes-et-echelle-d-humeur_finch.png` |
| 1 017 icônes d'inventaire (le vestiaire) | [[finch]] | Chapeaux, perruques, chaussures, accessoires — tout en SVG, servi publiquement par le portail Guardians. La profusion comme décision d'architecture. | `UI-DESIGN/finch/composants/icones-d-inventaire-le-vestiaire_finch.png` |
| Coffres et monnaie en trois matières | [[finch]] | Bois / argent / or, fermés et ouverts, avec cadenas ou tête de mort. Plus les trois mascottes marchandes. | `UI-DESIGN/finch/composants/economie-pierre-arc-en-ciel-et-coffres_finch.png` |
| Liste réordonnable au doigt, avec tooltip de geste | [[toss]] | Titre pédagogique, poignées de drag, et un tooltip qui **enseigne** le geste. Pattern rare et très « Toss ». | `UI-DESIGN/toss/composants/liste-reordonnable-au-doigt-avec-tooltip_toss.png` |
| Ponctuation dessinée comme icônes de navigation | [[toss]] | Les chevrons et les flèches de Toss Product Sans servent de boutons dans l'app. La typo et l'iconographie sont le même objet. | `UI-DESIGN/toss/composants/ponctuation-dessinee-comme-icones-de-nav_toss.png` |
| Bottom sheet : grille de logos de banques | [[toss]] | Quatre colonnes, tout le secteur bancaire coréen dans une seule feuille. Choisir une banque au logo, pas au nom. | `UI-DESIGN/toss/composants/bottom-sheet-grille-de-banques_toss.png` |

---
[[_INSPIRATION|← Inspiration]]
