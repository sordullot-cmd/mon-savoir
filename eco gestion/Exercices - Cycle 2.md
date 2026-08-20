---
tags:
  - L1-eco-gestion
  - cycle-2
  - exercices
  - comptabilite
nb_exercices: 44
duree_examen: 3h30
statut: à faire
---

# 🏋️ Exercices — Cycle 2

**44 exercices + 1 examen blanc (2 h stats + 1 h 30 compta)**
📘 [[Cycle 2 - Les chiffres]] · 🏠 [[00 - Plan L1 Angers]] · ⬅️ [[Exercices - Cycle 1]]

> [!danger] Le ratio de travail de ce cycle
> **20 % lecture / 80 % exercices.** En comptabilité surtout : cent écritures faites valent dix chapitres lus. Fais les 44.

---
# 📊 STATISTIQUES — UE 14C

## S1 — Représentations

**S1.1** Classes d'amplitudes inégales :

| Classe | Effectif |
|---|---|
| [0 ; 10[ | 20 |
| [10 ; 20[ | 50 |
| [20 ; 40[ | 60 |
| [40 ; 80[ | 40 |

Peux-tu tracer l'histogramme directement avec ces effectifs ? Sinon, que faut-il calculer ?

> [!success]- Corrigé S1.1
> **Non.** Avec des classes d'amplitudes inégales, **c'est l'aire qui représente l'effectif, pas la hauteur**. Il faut calculer la **densité** = effectif / amplitude, ramenée à une amplitude de référence (ici 10).
>
> | Classe | Effectif | Amplitude | Densité (base 10) |
> |---|---|---|---|
> | [0 ; 10[ | 20 | 10 | **20** |
> | [10 ; 20[ | 50 | 10 | **50** |
> | [20 ; 40[ | 60 | 20 | **30** |
> | [40 ; 80[ | 40 | 40 | **10** |
>
> Tracer les effectifs bruts donnerait à tort l'impression que la classe [20;40[ est la plus dense. **C'est une erreur classique et sanctionnée.**

## S2 — Tendance centrale et dispersion

**S2.1** Salaires (k€) de 10 personnes : 18, 22, 25, 25, 28, 32, 35, 40, 45, 60.
Calcule la moyenne, la médiane, le mode, la variance, l'écart-type, le coefficient de variation, $Q_1$, $Q_3$ et l'intervalle interquartile. Commente l'écart moyenne / médiane.

> [!success]- Corrigé S2.1
> **Moyenne** $= \frac{330}{10} = \boxed{33}$
> **Médiane** $= \frac{28+32}{2} = \boxed{30}$
> **Mode** $= \boxed{25}$
> **Variance** (formule de König) : $V = \frac{\sum x^2}{n} - \bar{x}^2 = \frac{12\,316}{10} - 33^2 = 1231{,}6 - 1089 = \boxed{142{,}6}$
> **Écart-type** $= \sqrt{142{,}6} = \boxed{11{,}94}$
> **CV** $= \frac{11,94}{33} = \boxed{36{,}2\%}$
> $Q_1 = \boxed{25}$ · $Q_3 = \boxed{40}$ · $IQ = \boxed{15}$
>
> **Commentaire** : moyenne (33) **> médiane (30)** → distribution **asymétrique à droite**. Les hauts salaires (le 60) tirent la moyenne vers le haut. C'est la configuration typique des distributions de revenus : **la médiane décrit mieux la situation « typique »** que la moyenne.

**S2.2** Distribution groupée :

| Classe de salaire (€) | Effectif |
|---|---|
| [1500 ; 2000[ | 40 |
| [2000 ; 2500[ | 70 |
| [2500 ; 3500[ | 50 |
| [3500 ; 5500[ | 40 |

Calcule la moyenne et la médiane par interpolation.

> [!success]- Corrigé S2.2
> Centres : 1750, 2250, 3000, 4500. Effectif total : 200.
> **Moyenne** $= \frac{1750(40)+2250(70)+3000(50)+4500(40)}{200} = \frac{557\,500}{200} = \boxed{2787{,}50\ \text{€}}$
> **Médiane** : effectifs cumulés 40, 110, 160, 200. Le rang 100 tombe dans [2000 ; 2500[.
> $$M_e = 2000 + \frac{100-40}{70}\times 500 = 2000 + 428{,}57 = \boxed{2428{,}57\ \text{€}}$$
> Là encore, moyenne > médiane.

**S2.3** Un placement rapporte +3 %, +5 %, −2 %, +4 % sur quatre ans. Calcule le taux moyen annuel. Compare à la moyenne arithmétique et explique l'écart.

> [!success]- Corrigé S2.3
> **Moyenne géométrique** (la bonne) :
> $$\bar{t} = \sqrt[4]{1{,}03 \times 1{,}05 \times 0{,}98 \times 1{,}04} - 1 = \sqrt[4]{1{,}102265} - 1 = \boxed{+2{,}46\%}$$
> **Moyenne arithmétique** (fausse) : $\frac{3+5-2+4}{4} = \boxed{+2{,}50\%}$
> **L'écart** vient du fait que les taux se **composent** et non s'additionnent. La moyenne arithmétique **surestime toujours** le taux moyen dès qu'il y a de la variabilité. C'est le **TCAM** du [[Exercices - Cycle 0#A5–A6 — Pourcentages et taux ⭐|cycle 0]] : une seule notion, deux noms.

## S3 — Concentration (Lorenz et Gini)

**S3.1** Répartition du revenu par quintile : 8 %, 13 %, 17 %, 23 %, 39 %.
a) Construis les cumuls et décris la courbe de Lorenz.
b) Calcule l'indice de Gini par la méthode des trapèzes.
c) Interprète.

> [!success]- Corrigé S3.1
> **a)** Cumuls de population : 20, 40, 60, 80, 100 %. Cumuls de revenu : **8, 21, 38, 61, 100 %**.
> Lecture : les 20 % les plus pauvres captent 8 % du revenu ; les 20 % les plus riches en captent 39 %.
>
> **b)** Aire sous la courbe de Lorenz par trapèzes (chaque trapèze a une base de 0,2) :
> $$A = 0{,}2\times\frac{(0+8)+(8+21)+(21+38)+(38+61)+(61+100)}{2\times100} = 0{,}2 \times \frac{178}{100} = 0{,}356$$
> $$G = \frac{0{,}5 - 0{,}356}{0{,}5} = \boxed{0{,}288}$$
>
> **c)** Gini de 0,288 → **inégalités modérées**, dans l'ordre de grandeur d'un pays européen après redistribution. Un Gini de 0 signifierait l'égalité parfaite, 1 la concentration totale du revenu sur une seule personne.

## S4 — Indices ⭐

**S4.1** Reprends les données :

| Bien | $p_0$ | $q_0$ | $p_t$ | $q_t$ |
|---|---|---|---|---|
| A | 10 | 100 | 13 | 70 |
| B | 5 | 200 | 5,5 | 250 |

Calcule les indices de **quantité** de Laspeyres et de Paasche. Vérifie la relation $L_p \times P_q = $ indice de valeur.

> [!success]- Corrigé S4.1
> **Laspeyres quantités** (prix de base figés) :
> $$L_q = \frac{\sum q_t p_0}{\sum q_0 p_0}\times100 = \frac{70(10)+250(5)}{2000}\times100 = \frac{1950}{2000}\times100 = \boxed{97{,}5}$$
> **Paasche quantités** (prix courants) :
> $$P_q = \frac{\sum q_t p_t}{\sum q_0 p_t}\times100 = \frac{2285}{2400}\times100 = \boxed{95{,}21}$$
> **Indice de valeur** : $\frac{\sum p_tq_t}{\sum p_0q_0} = \frac{2285}{2000}\times100 = \boxed{114{,}25}$
> **Vérification** : $L_p \times P_q = \frac{120}{100}\times\frac{95{,}21}{100} = 1{,}1425$ ✓
> **La relation à connaître** : indice de valeur = Laspeyres-prix × Paasche-quantité (ou l'inverse croisé). **On ne multiplie jamais deux Laspeyres entre eux.**

**S4.2** Une série a pour indices : 2018 = 100, 2021 = 112, 2024 = 131. Calcule le TCAM sur 2018-2024, puis rebase la série en 2021.

> [!success]- Corrigé S4.2
> **TCAM** : $\left(\frac{131}{100}\right)^{1/6}-1 = \boxed{+4{,}60\%\ \text{par an}}$
> **Rebasage** (multiplier par $\frac{100}{112}$) : 2018 → $\boxed{89{,}3}$ · 2021 → $\boxed{100}$ · 2024 → $\boxed{117{,}0}$

## S5 — Séries chronologiques

**S5.1** Ventes trimestrielles (k€) sur 3 ans :

| | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| **Année 1** | 100 | 130 | 90 | 120 |
| **Année 2** | 110 | 140 | 100 | 130 |
| **Année 3** | 120 | 150 | 110 | 140 |

a) Le modèle est-il additif ou multiplicatif ? Justifie.
b) Calcule la moyenne mobile centrée d'ordre 4 pour T3 et T4 de l'année 1.
c) On te donne les rapports série/tendance suivants. Calcule les coefficients saisonniers corrigés.

| Trimestre | Rapports observés |
|---|---|
| T1 | 0,9462 · 0,9505 |
| T2 | 1,1789 · 1,1650 |
| T3 | 0,8090 · 0,8247 |
| T4 | 1,0549 · 1,0505 |

> [!success]- Corrigé S5.1
> **a)** L'amplitude saisonnière est **constante** en niveau (l'écart T2−T3 vaut toujours 40) alors que la tendance monte. Cela plaide pour un modèle **additif**. Si l'amplitude croissait proportionnellement à la tendance, ce serait multiplicatif.
> *(On traite ici en multiplicatif pour l'exercice, car c'est le cas le plus demandé en examen.)*
>
> **b)** MM centrée d'ordre 4 : $MM_t = \dfrac{0{,}5y_{t-2}+y_{t-1}+y_t+y_{t+1}+0{,}5y_{t+2}}{4}$
> **T3 année 1** : $\frac{0{,}5(100)+130+90+120+0{,}5(110)}{4} = \frac{445}{4} = \boxed{111{,}25}$
> **T4 année 1** : $\frac{0{,}5(130)+90+120+110+0{,}5(140)}{4} = \frac{455}{4} = \boxed{113{,}75}$
>
> **c)** Moyennes par trimestre :
> T1 : $\frac{0{,}9462+0{,}9505}{2} = 0{,}94835$ · T2 : $1{,}17195$ · T3 : $0{,}81685$ · T4 : $1{,}0527$
> Somme $= 3{,}98985$, or elle doit valoir **4**. Coefficient correcteur $= \frac{4}{3{,}98985} = 1{,}002544$.
>
> | Trimestre | **Coefficient corrigé** |
> |---|---|
> | T1 | **0,951** |
> | T2 | **1,175** |
> | T3 | **0,819** |
> | T4 | **1,055** |
>
> **Lecture** : le T2 réalise 17,5 % de plus que la tendance, le T3 18,1 % de moins. **Désaisonnaliser** = diviser chaque valeur brute par son coefficient.

**S5.2** Pourquoi l'INSEE publie-t-il des séries « CVS » ?

> [!success]- Corrigé S5.2
> Pour permettre de comparer deux périodes **consécutives** sans être trompé par la saisonnalité. Sans correction, une baisse d'activité entre décembre et janvier serait interprétée comme un retournement conjoncturel alors qu'elle est purement saisonnière. La série CVS **isole le mouvement conjoncturel réel**.

## S6 — Régression ⭐

**S6.1** Dépenses publicitaires $X$ (k€) et ventes $Y$ (k€) :

| $X$ | 2 | 4 | 6 | 8 | 10 |
|---|---|---|---|---|---|
| $Y$ | 30 | 38 | 50 | 56 | 66 |

a) Calcule $\bar{x}$, $\bar{y}$, $V(X)$, $V(Y)$, $\text{cov}(X,Y)$.
b) Détermine la droite des moindres carrés.
c) Calcule $r$ et $r^2$. Commente.
d) Prévois les ventes pour $X = 12$. Quelle réserve faut-il émettre ?

> [!success]- Corrigé S6.1
> **a)** $\bar{x} = 6$ · $\bar{y} = 48$
> $V(X) = \frac{220}{5}-36 = \boxed{8}$ · $V(Y) = \frac{12\,336}{5}-2304 = \boxed{163{,}2}$
> $\text{cov}(X,Y) = \frac{1620}{5}-6(48) = 324-288 = \boxed{36}$
>
> **b)** $a = \frac{\text{cov}}{V(X)} = \frac{36}{8} = \boxed{4{,}5}$ · $b = \bar{y}-a\bar{x} = 48-27 = \boxed{21}$
> $$\boxed{y = 4{,}5x + 21}$$
> **Interprétation** : 1 000 € de publicité en plus sont associés à 4 500 € de ventes en plus.
>
> **c)** $r = \frac{36}{\sqrt{8\times163{,}2}} = \frac{36}{36{,}13} = \boxed{0{,}996}$ · $r^2 = \boxed{0{,}993}$
> **Commentaire** : liaison linéaire positive **très forte**. 99,3 % de la variance des ventes est expliquée par la variation des dépenses publicitaires *dans cet échantillon*.
>
> **d)** $y = 4{,}5(12)+21 = \boxed{75\ \text{k€}}$
> **Deux réserves obligatoires** :
> 1. $X=12$ est **hors de l'intervalle observé** [2 ; 10] — c'est une extrapolation, la relation peut ne plus être linéaire (rendements décroissants de la publicité).
> 2. **Corrélation n'est pas causalité.** Une variable omise — par exemple la conjoncture — peut faire varier simultanément le budget publicitaire et les ventes. Un $r^2$ de 0,993 ne prouve aucun effet causal.
>
> *(Cette dernière remarque est ce qu'on te demandera de développer en économétrie en L3.)*

---
# 📒 COMPTABILITÉ GÉNÉRALE — UE 16A

## C1 — Bilan et compte de résultat

**C1.1** Reconstitue le bilan et trouve le résultat :
Capital 50 000 · Emprunt 30 000 · Matériel 45 000 · Stocks 12 000 · Créances clients 18 000 · Banque 15 000 · Dettes fournisseurs 4 000.

> [!success]- Corrigé C1.1
> **Actif** = 45 000 + 12 000 + 18 000 + 15 000 = **90 000**
> **Passif hors résultat** = 50 000 + 30 000 + 4 000 = **84 000**
> $$\text{Résultat} = 90\,000 - 84\,000 = \boxed{+6\,000\ \text{(bénéfice)}}$$
> **Le raisonnement** : le bilan est équilibré par construction. Le résultat est la variable d'ajustement, et il figure **au passif** (capitaux propres) quand il est bénéficiaire.

**C1.2** Classe : Chiffre d'affaires · Salaires · Emprunt · Stock de matières · Dotations aux amortissements · Capital · Clients · Achats de matières · Banque.

> [!success]- Corrigé C1.2
> **Bilan — Actif** : Stock de matières · Clients · Banque
> **Bilan — Passif** : Capital · Emprunt
> **Compte de résultat — Charges** : Salaires · Dotations aux amortissements · Achats de matières
> **Compte de résultat — Produits** : Chiffre d'affaires

## C2 — La partie double

**C2.1** Constitution : capital de 50 000 € libéré par 30 000 € en banque et un matériel de 20 000 €. Passe l'écriture.
**C2.2** Obtention d'un emprunt bancaire de 25 000 €.
**C2.3** Remboursement d'une annuité d'emprunt : 5 000 € de capital + 800 € d'intérêts.

> [!success]- Corrigés C2
> **C2.1**
> ```
> D 512  Banque              30 000
> D 215  Installations tech. 20 000
>     C 101  Capital social            50 000
> ```
> **C2.2**
> ```
> D 512  Banque              25 000
>     C 164  Emprunts                  25 000
> ```
> **C2.3**
> ```
> D 164  Emprunts             5 000
> D 661  Charges d'intérêts     800
>     C 512  Banque                     5 800
> ```
> **Le point clé** : seuls les **intérêts** sont une charge. Le remboursement du capital est une **diminution de dette**, pas une charge — c'est l'erreur la plus fréquente.

## C3 — Achats, ventes, TVA ⭐

**C3.1** Achat de marchandises 5 000 € HT, TVA 20 %, à crédit.
**C3.2** Vente de produits finis 12 000 € HT, TVA 20 %, à crédit.
**C3.3** Liquidation de la TVA du mois (seules les opérations ci-dessus).
**C3.4** Facture d'achat : 8 000 € HT, remise 5 %, escompte de règlement 2 %, TVA 20 %.

> [!success]- Corrigés C3
> **C3.1**
> ```
> D 607   Achats de marchandises     5 000
> D 44566 TVA déductible s/ ABS      1 000
>     C 401  Fournisseurs                     6 000
> ```
> **C3.2**
> ```
> D 411   Clients                   14 400
>     C 701  Ventes de produits finis        12 000
>     C 44571 TVA collectée                   2 400
> ```
> **C3.3** TVA à décaisser $= 2400 - 1000 = \boxed{1400}$
> ```
> D 44571 TVA collectée              2 400
>     C 44566 TVA déductible                  1 000
>     C 44551 TVA à décaisser                 1 400
> ```
> **C3.4** Net commercial $= 8000 \times 0{,}95 = 7600$. Escompte $= 7600 \times 2\% = 152$. Net financier $= 7448$. TVA $= 7448 \times 20\% = 1489{,}60$. Net à payer $= \boxed{8937{,}60}$
> ```
> D 607   Achats de marchandises     7 600,00
> D 44566 TVA déductible             1 489,60
>     C 765  Escomptes obtenus                  152,00
>     C 401  Fournisseurs                     8 937,60
> ```
> **Les deux règles** : la **remise** est déduite avant enregistrement (elle n'apparaît jamais en compte), l'**escompte** est enregistré séparément (765 en produit financier chez l'acheteur, 665 en charge chez le vendeur). La **TVA se calcule sur le net financier**.

**C3.5** Pourquoi la TVA n'est-elle ni une charge ni un produit pour l'entreprise ?

> [!success]- Corrigé C3.5
> Parce que l'entreprise n'est qu'un **collecteur pour l'État**. La TVA collectée sur les ventes est une **dette** (compte 44571), la TVA payée sur les achats une **créance** (44566). Elle transite par le bilan, jamais par le compte de résultat. Le coût réel de l'entreprise est le **montant hors taxes** — c'est pourquoi tous les comptes de charges et de produits sont tenus en HT.

## C4 — Trésorerie, effets, personnel

**C4.1** Salaires bruts 20 000 € · cotisations salariales 4 000 € · cotisations patronales 8 000 €. Passe les écritures et calcule le coût total pour l'entreprise.
**C4.2** Remise à l'escompte d'un effet de 6 000 €, agios 180 €.

> [!success]- Corrigés C4
> **C4.1**
> ```
> D 641  Rémunérations du personnel  20 000
>     C 421  Personnel - rém. dues            20 000
>
> D 645  Charges de sécurité sociale  8 000
>     C 431  Sécurité sociale                  8 000
>
> D 421  Personnel                   20 000
>     C 431  Sécurité sociale                  4 000
>     C 512  Banque (net versé)               16 000
> ```
> **Coût total employeur** $= 20\,000 + 8\,000 = \boxed{28\,000\ \text{€}}$ pour un net versé de 16 000 €.
> **L'ordre de grandeur à retenir** : le coût employeur est environ **1,75 fois** le net perçu.
> **C4.2**
> ```
> D 512  Banque                       5 820
> D 627  Services bancaires             180
>     C 5114 Effets à l'encaissement           6 000
> ```

## C5 — Amortissements ⭐

**C5.1** Machine acquise **le 1er avril N** pour 24 000 € HT, durée 5 ans, **amortissement linéaire**. Construis le tableau complet.
**C5.2** Même machine acquise **le 1er janvier N**, en **dégressif** (coefficient 1,75). Construis le tableau et indique l'année de bascule vers le linéaire.

> [!success]- Corrigé C5.1
> Annuité pleine $= \frac{24\,000}{5} = 4\,800$. Année N : prorata de **9 mois** $= 4800\times\frac{9}{12} = 3\,600$.
>
> | Année | Annuité | Cumul | VNC |
> |---|---|---|---|
> | N | **3 600** | 3 600 | 20 400 |
> | N+1 | 4 800 | 8 400 | 15 600 |
> | N+2 | 4 800 | 13 200 | 10 800 |
> | N+3 | 4 800 | 18 000 | 6 000 |
> | N+4 | 4 800 | 22 800 | 1 200 |
> | N+5 | **1 200** | 24 000 | 0 |
>
> **Le piège** : le prorata décale l'amortissement sur **6 exercices** pour une durée de 5 ans. Total = 24 000 ✓
>
> Écriture annuelle :
> ```
> D 6811 Dotations aux amortissements   3 600
>     C 2815 Amortissements des install.        3 600
> ```

> [!success]- Corrigé C5.2
> Taux linéaire $= 20\%$, taux dégressif $= 20\% \times 1{,}75 = \boxed{35\%}$
>
> | Année | Base | Taux appliqué | Annuité | VNC fin |
> |---|---|---|---|---|
> | N | 24 000 | 35 % | **8 400** | 15 600 |
> | N+1 | 15 600 | 35 % | **5 460** | 10 140 |
> | N+2 | 10 140 | 35 % | **3 549** | 6 591 |
> | N+3 | 6 591 | **50 %** (linéaire) | **3 295,50** | 3 295,50 |
> | N+4 | — | — | **3 295,50** | 0 |
>
> **La bascule a lieu en N+3.** Règle : on passe au linéaire dès que le taux linéaire sur la **durée résiduelle** dépasse le taux dégressif. En N+3, il reste 2 ans → $\frac{1}{2} = 50\% > 35\%$.
> Total $= 8400+5460+3549+3295{,}5+3295{,}5 = 24\,000$ ✓
>
> **L'intérêt du dégressif** : il concentre la charge sur les premières années, donc **réduit l'impôt à court terme**. C'est un dispositif fiscal, pas une meilleure représentation de l'usure.

## C6 — Travaux d'inventaire ⭐

**C6.1** Une créance client de 6 000 € TTC (5 000 € HT) devient douteuse. On estime la perte probable à 40 %.
**C6.2** Prime d'assurance de 1 200 € payée le 1er octobre N pour 12 mois. Régularisation au 31/12/N.
**C6.3** Stock initial de matières 8 000 €, stock final 11 000 €. Passe les deux écritures et indique l'effet sur le résultat.
**C6.4** L'entreprise est en litige prud'homal ; le risque est estimé à 15 000 €.

> [!success]- Corrigés C6
> **C6.1** La dépréciation se calcule sur le montant **HT** (la TVA sera récupérée si la créance est définitivement perdue).
> ```
> D 416   Clients douteux             6 000
>     C 411  Clients                          6 000
>
> D 68174 Dotations dépréciations     2 000
>     C 491  Dépréciation des comptes clients  2 000
> ```
> **C6.2** Sur 12 mois, **9 mois** concernent N+1 : $1200 \times \frac{9}{12} = \boxed{900}$
> ```
> D 486  Charges constatées d'avance    900
>     C 616  Primes d'assurances                900
> ```
> **Le principe** : l'**indépendance des exercices**. Seuls les 300 € correspondant à octobre-décembre N restent en charge de l'exercice N.
> **C6.3**
> ```
> D 6031 Variation des stocks          8 000
>     C 31   Stocks de matières               8 000     (annulation du SI)
>
> D 31   Stocks de matières           11 000
>     C 6031 Variation des stocks             11 000     (constatation du SF)
> ```
> Le compte 6031 est **créditeur de 3 000 €** → il vient **en diminution des charges**, donc **augmente le résultat de 3 000 €**. Logique : ce qui a été acheté mais non consommé ne doit pas peser sur l'exercice.
> **C6.4**
> ```
> D 6815 Dotations aux provisions     15 000
>     C 151  Provisions pour risques          15 000
> ```
> **Distinction à connaître** : la **provision** couvre un risque au passif (montant et échéance incertains), la **dépréciation** constate la perte de valeur d'un actif. Toutes deux sont **réversibles**, contrairement à l'amortissement.

## C7 — Clôture

**C7.1** Total des comptes de charges : 145 000 €. Total des produits : 172 000 €. L'IS est de 25 %. Calcule le résultat avant et après impôt, et passe l'écriture de virement.

> [!success]- Corrigé C7.1
> Résultat avant impôt $= 172\,000 - 145\,000 = \boxed{27\,000}$
> IS $= 27\,000 \times 25\% = \boxed{6\,750}$
> ```
> D 695  Impôts sur les bénéfices     6 750
>     C 444  État - impôt sur les bénéfices    6 750
> ```
> Résultat net $= 27\,000 - 6\,750 = \boxed{20\,250}$
> ```
> D 120  Résultat de l'exercice      20 250   (au passif du bilan)
> ```
> *(En pratique, le résultat se dégage par solde des comptes 6 et 7 dans le compte 120.)*

## C8 — Mini-cycle complet ⭐⭐

**Atelier Loire SARL**, menuiserie. TVA à 20 %. Passe les 12 écritures, puis établis le bilan et le compte de résultat.

1. Constitution : capital de 30 000 € versé en banque
2. Emprunt bancaire de 20 000 €
3. Achat d'une machine 12 000 € HT, à crédit (fournisseur d'immobilisation)
4. Paiement de la machine
5. Achat de matières 5 000 € HT, à crédit
6. Ventes de produits finis 18 000 € HT, à crédit
7. Encaissement de 15 000 € de clients
8. Paiement de 6 000 € au fournisseur
9. Salaires 7 000 € et charges patronales 3 000 €, payés en banque
10. Loyer 2 400 € payé en banque (hors TVA pour simplifier)
11. Dotation aux amortissements de la machine (5 ans, année pleine)
12. Liquidation de la TVA

> [!success]- Corrigé C8 — Écritures
> ```
> 1.  D 512 Banque              30 000  / C 101 Capital           30 000
> 2.  D 512 Banque              20 000  / C 164 Emprunts          20 000
> 3.  D 215 Machine             12 000
>     D 44562 TVA s/ immo        2 400  / C 404 Fourn. immo       14 400
> 4.  D 404 Fourn. immo         14 400  / C 512 Banque            14 400
> 5.  D 601 Achats matières      5 000
>     D 44566 TVA déductible     1 000  / C 401 Fournisseurs       6 000
> 6.  D 411 Clients             21 600  / C 701 Ventes            18 000
>                                       / C 44571 TVA collectée    3 600
> 7.  D 512 Banque              15 000  / C 411 Clients           15 000
> 8.  D 401 Fournisseurs         6 000  / C 512 Banque             6 000
> 9.  D 641 Salaires             7 000
>     D 645 Charges sociales     3 000  / C 512 Banque            10 000
> 10. D 613 Locations            2 400  / C 512 Banque             2 400
> 11. D 6811 Dotations           2 400  / C 2815 Amortissements    2 400
> 12. D 44571 TVA collectée      3 600  / C 44566                  1 000
>                                       / C 44562                  2 400
>                                       / C 44551 TVA à décaisser    200
> ```

> [!success]- Corrigé C8 — États financiers
> **Solde de la banque** : $30\,000 + 20\,000 - 14\,400 + 15\,000 - 6\,000 - 10\,000 - 2\,400 = \boxed{32\,200}$
>
> **Compte de résultat**
>
> | Charges | € | Produits | € |
> |---|---|---|---|
> | 601 Achats de matières | 5 000 | 701 Ventes | **18 000** |
> | 613 Locations | 2 400 | | |
> | 641 Salaires | 7 000 | | |
> | 645 Charges sociales | 3 000 | | |
> | 6811 Dotations aux amort. | 2 400 | | |
> | **Total charges** | **19 800** | **Total produits** | **18 000** |
> | | | **Perte** | **−1 800** |
>
> **Bilan**
>
> | Actif | € | Passif | € |
> |---|---|---|---|
> | Machine (brut 12 000 − amort. 2 400) | 9 600 | Capital | 30 000 |
> | Clients | 6 600 | Résultat | **−1 800** |
> | Banque | 32 200 | Emprunts | 20 000 |
> | | | TVA à décaisser | 200 |
> | **Total** | **48 400** | **Total** | **48 400** |
>
> ✅ **Le bilan équilibre.**
>
> **Le commentaire attendu** : l'entreprise dégage une **perte de 1 800 €** mais sa trésorerie est confortable (32 200 €). **Résultat et trésorerie ne se confondent pas** : l'amortissement est une charge sans décaissement, et le stock de clients (6 600 €) est un produit déjà comptabilisé mais non encaissé. C'est toute la différence entre le compte de résultat et le tableau de trésorerie.

---
---

# 🎯 EXAMEN BLANC — CYCLE 2

> [!warning] Conditions
> **Épreuve 1 — Statistiques : 2 heures, /40** · **Épreuve 2 — Comptabilité : 1 h 30, /40**
> Calculatrice autorisée. Sans notes.

## ÉPREUVE 1 — STATISTIQUES (2 h, /40)

**Q1. Distribution groupée (10 pts)**

| Chiffre d'affaires (k€) | Nombre d'entreprises |
|---|---|
| [0 ; 100[ | 15 |
| [100 ; 200[ | 30 |
| [200 ; 400[ | 35 |
| [400 ; 800[ | 20 |

a) Calcule la moyenne. **(2 pts)**
b) Calcule la médiane par interpolation linéaire. **(3 pts)**
c) Calcule la variance, l'écart-type et le coefficient de variation. **(4 pts)**
d) Commente l'écart moyenne / médiane. **(1 pt)**

**Q2. Concentration (8 pts)**
Répartition des revenus par quintile : 6 %, 11 %, 16 %, 23 %, 44 %.
a) Cumuls et description de la courbe de Lorenz. **(3 pts)**
b) Indice de Gini par les trapèzes. **(4 pts)**
c) Interprétation. **(1 pt)**

**Q3. Indices (10 pts)**

| Bien | $p_0$ | $q_0$ | $p_t$ | $q_t$ |
|---|---|---|---|---|
| A | 20 | 50 | 24 | 45 |
| B | 8 | 150 | 9 | 160 |

a) Laspeyres-prix. **(3 pts)**
b) Paasche-prix. **(3 pts)**
c) Fisher. **(2 pts)**
d) Explique l'écart entre Laspeyres et Paasche. **(2 pts)**

**Q4. Régression (12 pts)**

| Ancienneté $X$ (années) | 1 | 3 | 5 | 7 | 9 |
|---|---|---|---|---|---|
| Salaire $Y$ (k€) | 24 | 28 | 34 | 36 | 43 |

a) $\bar{x}$, $\bar{y}$, $V(X)$, $V(Y)$, $\text{cov}(X,Y)$. **(4 pts)**
b) Droite des moindres carrés, avec interprétation de la pente. **(3 pts)**
c) $r$ et $r^2$. **(3 pts)**
d) Salaire prévu à 12 ans d'ancienneté, et **deux réserves**. **(2 pts)**

## ÉPREUVE 2 — COMPTABILITÉ (1 h 30, /40)

**Menuiserie Anjou SARL** — TVA à 20 %, exercice N.

**Q5. Passe les écritures (24 pts)**
1. Constitution du capital : 40 000 € (25 000 € en banque, 15 000 € de matériel)
2. Emprunt bancaire de 25 000 €
3. Achat d'un véhicule utilitaire 18 000 € HT, à crédit
4. Achat de matières premières 9 000 € HT, à crédit
5. Ventes de produits finis 32 000 € HT, à crédit
6. Encaissement de 25 000 € de clients
7. Règlement de 8 000 € aux fournisseurs
8. Salaires et charges 14 000 € payés en banque
9. Assurance 1 800 € payée en banque le 1er novembre N, pour 12 mois
10. Amortissements : véhicule sur 6 ans, matériel sur 5 ans (année pleine)
11. Régularisation de l'assurance
12. Liquidation de la TVA

**Q6. États financiers (12 pts)**
Établis le compte de résultat et le bilan au 31/12/N.

**Q7. Analyse (4 pts)**
L'entreprise dégage-t-elle un résultat cohérent avec sa trésorerie ? Explique en trois lignes.

---

> [!success]- 📝 CORRIGÉ — ÉPREUVE 1 (STATISTIQUES)
>
> **Q1. (10 pts)** Centres : 50, 150, 300, 600. Effectif total : 100.
> a) $\bar{x} = \frac{50(15)+150(30)+300(35)+600(20)}{100} = \frac{27\,750}{100} = \boxed{277{,}5\ \text{k€}}$
> b) Cumuls : 15, 45, 80, 100. Le rang 50 tombe dans [200 ; 400[.
> $$M_e = 200 + \frac{50-45}{35}\times200 = 200+28{,}57 = \boxed{228{,}57\ \text{k€}}$$
> c) $\sum n_ix_i^2 = 15(2500)+30(22\,500)+35(90\,000)+20(360\,000) = 11\,062\,500$
> $V = \frac{11\,062\,500}{100} - 277{,}5^2 = 110\,625 - 77\,006{,}25 = \boxed{33\,618{,}75}$
> $\sigma = \boxed{183{,}35}$ · $CV = \frac{183,35}{277,5} = \boxed{66{,}1\%}$
> d) Moyenne (277,5) **nettement supérieure** à la médiane (228,6) → **forte asymétrie à droite**. Quelques très grandes entreprises tirent la moyenne. Un CV de 66 % confirme une **dispersion très élevée**. La médiane décrit mieux l'entreprise « typique ».
>
> **Q2. (8 pts)**
> a) Cumuls de revenu : **6, 17, 33, 56, 100 %**. Les 20 % les plus pauvres captent 6 % du revenu, les 20 % les plus riches 44 % — soit plus de 7 fois plus.
> b) $A = 0{,}2\times\frac{(0+6)+(6+17)+(17+33)+(33+56)+(56+100)}{200} = 0{,}2\times\frac{162}{100} = 0{,}324$
> $$G = \frac{0{,}5-0{,}324}{0{,}5} = \boxed{0{,}352}$$
> c) Inégalités **assez marquées**, supérieures à la moyenne européenne après redistribution. On est dans un ordre de grandeur proche d'un Gini de revenu **avant** transferts sociaux.
>
> **Q3. (10 pts)**
> $\sum p_0q_0 = 20(50)+8(150) = 2\,200$
> a) $L_p = \frac{24(50)+9(150)}{2200}\times100 = \frac{2550}{2200}\times100 = \boxed{115{,}91}$
> b) $\sum p_0q_t = 20(45)+8(160) = 2\,180$ · $\sum p_tq_t = 24(45)+9(160) = 2\,520$
> $P_p = \frac{2520}{2180}\times100 = \boxed{115{,}60}$
> c) $F = \sqrt{115{,}91\times115{,}60} = \boxed{115{,}75}$
> d) $L > P$, comme presque toujours. Le bien A a le plus augmenté (+20 % contre +12,5 %) et sa consommation a reculé (50 → 45) au profit de B. **Laspeyres fige les quantités anciennes et ne capte pas cette substitution : il surestime l'inflation.** Paasche la sous-estime symétriquement. L'écart est faible ici (0,3 point) car les mouvements de quantités sont modérés.
>
> **Q4. (12 pts)**
> a) $\bar{x} = 5$ · $\bar{y} = 33$
> $V(X) = \frac{165}{5}-25 = \boxed{8}$ · $V(Y) = \frac{5661}{5}-1089 = \boxed{43{,}2}$ · $\text{cov} = \frac{917}{5}-165 = \boxed{18{,}4}$
> b) $a = \frac{18,4}{8} = \boxed{2{,}3}$ · $b = 33-11{,}5 = \boxed{21{,}5}$ → $\boxed{y = 2{,}3x+21{,}5}$
> **Interprétation** : chaque année d'ancienneté supplémentaire est associée à **+2 300 €** de salaire annuel. L'ordonnée à l'origine (21 500 €) correspond au salaire d'embauche théorique.
> c) $r = \frac{18,4}{\sqrt{8\times43,2}} = \frac{18,4}{18,59} = \boxed{0{,}990}$ · $r^2 = \boxed{0{,}980}$ — liaison linéaire positive très forte.
> d) $y = 2{,}3(12)+21{,}5 = \boxed{49{,}1\ \text{k€}}$
> **Réserve 1** : $X = 12$ est **hors de l'intervalle observé** [1 ; 9]. Rien ne garantit que la relation reste linéaire au-delà — les grilles salariales plafonnent généralement.
> **Réserve 2** : **corrélation ≠ causalité**. L'ancienneté est corrélée à l'âge, à l'expérience et souvent aux promotions. On ne peut pas attribuer causalement 2 300 € à l'ancienneté seule sans contrôler ces variables. *(C'est exactement l'équation de Mincer, que tu estimeras en L3.)*

> [!success]- 📝 CORRIGÉ — ÉPREUVE 2 (COMPTABILITÉ)
>
> **Q5. Écritures (24 pts)**
> ```
> 1.  D 512 Banque              25 000
>     D 215 Matériel            15 000  / C 101 Capital           40 000
> 2.  D 512 Banque              25 000  / C 164 Emprunts          25 000
> 3.  D 2182 Matériel transport 18 000
>     D 44562 TVA s/ immo        3 600  / C 404 Fourn. immo       21 600
> 4.  D 601 Achats matières      9 000
>     D 44566 TVA déductible     1 800  / C 401 Fournisseurs      10 800
> 5.  D 411 Clients             38 400  / C 701 Ventes            32 000
>                                       / C 44571 TVA collectée    6 400
> 6.  D 512 Banque              25 000  / C 411 Clients           25 000
> 7.  D 401 Fournisseurs         8 000  / C 512 Banque             8 000
> 8.  D 641/645 Personnel       14 000  / C 512 Banque            14 000
> 9.  D 616 Assurances           1 800  / C 512 Banque             1 800
> 10. D 6811 Dotations           6 000  / C 28182 Amort. transport 3 000
>                                       / C 2815 Amort. matériel   3 000
> 11. D 486 CCA                  1 500  / C 616 Assurances         1 500
> 12. D 44571 TVA collectée      6 400  / C 44566                  1 800
>                                       / C 44562                  3 600
>                                       / C 44551 TVA à décaisser  1 000
> ```
> **Détails de calcul** :
> - Amortissements : véhicule $\frac{18\,000}{6} = 3\,000$ · matériel $\frac{15\,000}{5} = 3\,000$
> - CCA : sur 12 mois à partir du 1er novembre, **10 mois** concernent N+1 → $1800\times\frac{10}{12} = 1\,500$
> - TVA à décaisser : $6\,400 - (1\,800 + 3\,600) = 1\,000$
>
> **Q6. États financiers (12 pts)**
> Banque : $25\,000+25\,000+25\,000-8\,000-14\,000-1\,800 = \boxed{51\,200}$
> Fournisseurs : $21\,600 + 10\,800 - 8\,000 = \boxed{24\,400}$
> Clients : $38\,400 - 25\,000 = \boxed{13\,400}$
>
> **Compte de résultat**
>
> | Charges | € | Produits | € |
> |---|---|---|---|
> | 601 Achats de matières | 9 000 | 701 Ventes | **32 000** |
> | 616 Assurances (1 800 − 1 500) | 300 | | |
> | 641/645 Personnel | 14 000 | | |
> | 6811 Dotations aux amortissements | 6 000 | | |
> | **Total** | **29 300** | **Total** | **32 000** |
> | **Bénéfice** | **2 700** | | |
>
> **Bilan au 31/12/N**
>
> | Actif | € | Passif | € |
> |---|---|---|---|
> | Matériel (15 000 − 3 000) | 12 000 | Capital | 40 000 |
> | Véhicule (18 000 − 3 000) | 15 000 | Résultat | **2 700** |
> | Clients | 13 400 | Emprunts | 25 000 |
> | Banque | 51 200 | Fournisseurs | 24 400 |
> | Charges constatées d'avance | 1 500 | TVA à décaisser | 1 000 |
> | **Total** | **93 100** | **Total** | **93 100** |
>
> ✅ **Équilibré.**
>
> **Q7. Analyse (4 pts)**
> Le bénéfice est modeste (2 700 €) alors que la trésorerie est très confortable (51 200 €). **Il n'y a pas de contradiction** : la trésorerie est gonflée par des ressources **non liées à l'activité** — l'apport en capital et l'emprunt (65 000 € au total). Par ailleurs, l'amortissement (6 000 €) est une **charge sans décaissement**, et 13 400 € de ventes sont comptabilisés en produit mais **pas encore encaissés**. Résultat et trésorerie mesurent deux choses différentes.

---

## 🎓 Barème de décision

| Note /80 | Verdict |
|---|---|
| **64–80** | ✅ Passe au [[Cycle 3 - Gestion et debats]] |
| **48–63** | ⚠️ Passe, mais refais la mission du cycle comptable complet |
| **< 48** | 🛑 Si le bilan n'équilibre pas sans notes, reprends [[Cycle 2 - Les chiffres#C2 — La partie double (S15) ⭐\|la partie double]] avant tout |

→ Exercices suivants : [[Exercices - Cycle 3]]
