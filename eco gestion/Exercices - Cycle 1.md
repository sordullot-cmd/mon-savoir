---
tags:
  - L1-eco-gestion
  - cycle-1
  - exercices
nb_exercices: 52
duree_examen: 3h
statut: à faire
---

# 🏋️ Exercices — Cycle 1

**52 exercices + 1 examen blanc de 3 h (micro + macro + maths)**
📘 [[Cycle 1 - Moteur economique]] · 🏠 [[00 - Plan L1 Angers]] · ⬅️ [[Exercices - Cycle 0]]

> [!tip] Corrigés repliés
> Clique sur `> Corrigé` pour déplier. **Pose ton calcul sur papier avant.**

---
# 🛒 MICROÉCONOMIE — UE 11C

## M1 — Préférences et TMS

**M1.1** $U(x,y) = \min(x,\,2y)$. Que représentent ces préférences ? Où se situe l'optimum ?
**M1.2** Montre que deux courbes d'indifférence ne peuvent jamais se croiser.
**M1.3** $U = x^{0,5}y^{0,5}$. Classe les paniers $A(16,4)$, $B(8,8)$, $C(4,25)$.

> [!success]- Corrigés M1
> **M1.1** **Compléments parfaits** (biens consommés en proportions fixes : 1 unité de $x$ pour 0,5 de $y$). Courbes d'indifférence en **L**. Le TMS n'est pas défini aux angles. L'optimum est toujours au coude : $\boxed{x = 2y}$, quel que soit le rapport des prix.
> **M1.2** Par l'absurde. Si deux courbes $U_1 \neq U_2$ se croisaient en $A$, alors $A$ appartiendrait aux deux, donc $U_1 = U(A) = U_2$ — contradiction. Cela violerait la **transitivité** des préférences.
> **M1.3** $U(A) = \sqrt{64} = 8$ · $U(B) = \sqrt{64} = 8$ · $U(C) = \sqrt{100} = 10$
> $\boxed{C \succ A \sim B}$ — $A$ et $B$ sont sur la **même courbe d'indifférence**.

## M2 — Contrainte budgétaire

**M2.1** $R = 120$, $p_1 = 4$, $p_2 = 6$. Écris la contrainte, donne les deux intersections avec les axes et la pente.
**M2.2** $p_1$ passe à 6. Que devient la droite de budget ?
**M2.3** Compare l'effet d'une taxe **forfaitaire** de 20 € et d'une taxe **ad valorem** de 25 % sur le bien $x$ (avec $R=120$, $p_1=4$, $p_2=6$).

> [!success]- Corrigés M2
> **M2.1** $4x + 6y = 120$. Si $y=0$ : $\boxed{x_{max}=30}$. Si $x=0$ : $\boxed{y_{max}=20}$. Pente $= -\frac{p_1}{p_2} = \boxed{-\frac{2}{3}}$
> **M2.2** $6x+6y=120$ → $x_{max}$ passe de 30 à $\boxed{20}$, $y_{max}$ inchangé à 20. La droite **pivote** autour de $(0\,;20)$.
> **M2.3**
> - **Forfaitaire** : $4x+6y = 100$ → **translation** vers l'intérieur, **pente inchangée**. Pas de distorsion des prix relatifs.
> - **Ad valorem sur $x$** : $p_1 = 5$, donc $5x+6y=120$ → **pivot**, la pente passe à $-\frac{5}{6}$. **Elle déforme les prix relatifs.**
>
> **Le résultat classique** : à recette fiscale égale, la taxe forfaitaire laisse le consommateur sur une courbe d'indifférence plus élevée, car elle ne crée pas de distorsion.

## M3 — Le choix optimal (Lagrangien) ⭐⭐

**M3.1** $U = x^{0,5}y^{0,5}$, $p_1 = 2$, $p_2 = 4$, $R = 100$. Trouve $x^*$, $y^*$, $U^*$ et $\lambda$.
**M3.2** $U = x^{0,3}y^{0,7}$, $p_1 = 3$, $p_2 = 7$, $R = 210$.
**M3.3** $U = xy$, $p_1 = 5$, $p_2 = 10$, $R = 200$.
**M3.4** **Cas général** — $U = x^\alpha y^\beta$. Démontre que $x^* = \dfrac{\alpha}{\alpha+\beta}\cdot\dfrac{R}{p_1}$.
**M3.5** $U = 2x + 3y$, $p_1 = 4$, $p_2 = 9$, $R = 180$. Attention.

> [!success]- Corrigé M3.1
> $\mathcal{L} = x^{0,5}y^{0,5} + \lambda(100 - 2x - 4y)$
> $\frac{\partial\mathcal{L}}{\partial x} = 0{,}5x^{-0,5}y^{0,5} - 2\lambda = 0$ · $\frac{\partial\mathcal{L}}{\partial y} = 0{,}5x^{0,5}y^{-0,5} - 4\lambda = 0$
> En divisant : $TMS = \dfrac{y}{x} = \dfrac{2}{4} = 0{,}5 \Rightarrow y = 0{,}5x$
> Budget : $2x + 4(0{,}5x) = 100 \Rightarrow 4x = 100$
> $$\boxed{x^* = 25 \quad;\quad y^* = 12{,}5}$$
> $U^* = \sqrt{25 \times 12{,}5} = \boxed{17{,}68}$
> $\lambda = \dfrac{0{,}5x^{-0,5}y^{0,5}}{2} = \dfrac{0{,}5\sqrt{0{,}5}}{2} = \boxed{0{,}177}$
> **Interprétation de $\lambda$** : un euro de revenu supplémentaire augmenterait l'utilité de 0,177.

> [!success]- Corrigés M3.2 à M3.5
> **M3.2** Cobb-Douglas : $x^* = \frac{0,3}{1}\cdot\frac{210}{3} = \boxed{21}$ · $y^* = \frac{0,7}{1}\cdot\frac{210}{7} = \boxed{21}$
> **M3.3** $U = xy$ → $\alpha=\beta=1$, parts égales : $x^* = 0{,}5\cdot\frac{200}{5} = \boxed{20}$ · $y^* = 0{,}5\cdot\frac{200}{10} = \boxed{10}$ · $U^* = \boxed{200}$
> **M3.4** CPO : $\alpha x^{\alpha-1}y^\beta = \lambda p_1$ et $\beta x^\alpha y^{\beta-1} = \lambda p_2$. En divisant : $\frac{\alpha y}{\beta x} = \frac{p_1}{p_2}$, donc $p_2 y = \frac{\beta}{\alpha}p_1 x$. En reportant dans $p_1x + p_2y = R$ : $p_1x\left(1+\frac{\beta}{\alpha}\right) = R$, d'où $\boxed{x^* = \frac{\alpha}{\alpha+\beta}\cdot\frac{R}{p_1}}$
> **Le résultat à retenir** : avec une Cobb-Douglas, **les parts de dépense sont constantes** et ne dépendent ni des prix ni du revenu.
> **M3.5** ⚠️ **Substituts parfaits** — le Lagrangien ne s'applique pas directement (TMS constant $= \frac{2}{3}$).
> Compare l'utilité par euro : $\frac{Um_x}{p_1} = \frac{2}{4} = 0{,}5$ contre $\frac{Um_y}{p_2} = \frac{3}{9} = 0{,}33$.
> Le bien $x$ rapporte plus par euro → **solution en coin** : $\boxed{x^* = 45,\ y^* = 0,\ U^* = 90}$

## M4 — Effets substitution et revenu ⭐

**M4.1** $U = x^{0,5}y^{0,5}$, $R = 100$, $p_2 = 1$. Le prix $p_1$ passe de 1 à 4.
a) Panier initial et panier final ?
b) Décompose l'effet total sur $x$ en **effet de substitution** et **effet de revenu** (méthode de Hicks).
c) Le bien $x$ est-il normal ou inférieur ?

> [!success]- Corrigé M4.1
> **a)** Cobb-Douglas, parts $\frac{1}{2}$ :
> Initial ($p_1=1$) : $x_0 = \frac{0,5 \times 100}{1} = \boxed{50}$, $y_0 = \boxed{50}$, $U_0 = \sqrt{2500} = \boxed{50}$
> Final ($p_1=4$) : $x_1 = \frac{0,5\times100}{4} = \boxed{12{,}5}$, $y_1 = \boxed{50}$
> **Effet total sur $x$** : $12{,}5 - 50 = \boxed{-37{,}5}$
>
> **b)** **Panier de Hicks** : le panier le moins cher qui maintient $U_0 = 50$ aux **nouveaux prix**.
> Contrainte : $\sqrt{xy} = 50 \Rightarrow xy = 2500$. Condition d'optimalité : $\frac{y}{x} = \frac{4}{1} \Rightarrow y = 4x$.
> $4x^2 = 2500 \Rightarrow x_H = \boxed{25}$, $y_H = 100$.
> - **Effet de substitution** : $25 - 50 = \boxed{-25}$
> - **Effet de revenu** : $12{,}5 - 25 = \boxed{-12{,}5}$
> - **Total** : $-25 - 12{,}5 = -37{,}5$ ✓
>
> **c)** L'effet de revenu est **négatif** suite à une perte de pouvoir d'achat → le bien est **normal**.
> *(Un bien inférieur aurait un effet de revenu positif ici ; un bien de Giffen aurait un effet de revenu positif dominant l'effet de substitution.)*

## M5 — Élasticités ⭐

**M5.1** $Q_d = 100 - 2P$. Élasticité en $P=20$, $P=25$, $P=40$. Où la recette est-elle maximale ?
**M5.2** $Q_d = \dfrac{500}{P}$. Calcule l'élasticité. Que remarques-tu ?
**M5.3** $Q_d = 200P^{-1,5}$. Élasticité ?
**M5.4** La demande passe de 400 à 360 quand le prix passe de 10 à 12. Élasticité-arc ?
**M5.5** La consommation passe de 800 à 880 quand le revenu passe de 20 000 à 22 000. Élasticité-revenu ? Nature du bien ?
**M5.6** $Q_A$ passe de 500 à 540 quand $P_B$ passe de 8 à 10. Élasticité croisée ? Relation entre A et B ?
**M5.7** Une demande a $\varepsilon = -0{,}5$. Le prix augmente de 10 %. Que devient la recette ?

> [!success]- Corrigés M5
> **M5.1** $\varepsilon = -2\cdot\frac{P}{Q}$.
> $P=20$ : $Q=60$, $\varepsilon = \boxed{-0{,}67}$ (inélastique) · $P=25$ : $Q=50$, $\varepsilon = \boxed{-1}$ (unitaire) · $P=40$ : $Q=20$, $\varepsilon = \boxed{-4}$ (très élastique)
> **La recette est maximale là où $\varepsilon = -1$**, soit $P=25$ : $RT = 25\times50 = 1250$.
> **M5.2** $\frac{dQ}{dP} = -\frac{500}{P^2}$, donc $\varepsilon = -\frac{500}{P^2}\cdot\frac{P}{500/P} = \boxed{-1}$ **partout**. Demande à **élasticité unitaire constante** : la recette $PQ = 500$ ne dépend pas du prix.
> **M5.3** Pour $Q = aP^{-b}$, l'élasticité vaut toujours $-b$, ici $\boxed{-1{,}5}$. C'est l'intérêt des formes puissance : **l'exposant EST l'élasticité**.
> **M5.4** $\varepsilon = \dfrac{-40/400}{2/10} = \dfrac{-0{,}10}{0{,}20} = \boxed{-0{,}5}$ → inélastique
> **M5.5** $\varepsilon_R = \dfrac{80/800}{2000/20\,000} = \dfrac{0{,}10}{0{,}10} = \boxed{+1}$ → **bien normal**, à élasticité-revenu unitaire (sa part dans le budget reste constante).
> **M5.6** $\varepsilon_c = \dfrac{40/500}{2/8} = \dfrac{0{,}08}{0{,}25} = \boxed{+0{,}32} > 0$ → **substituts** (faiblement).
> **M5.7** $Q$ baisse de 5 %. $RT$ : $1{,}10 \times 0{,}95 = 1{,}045 \Rightarrow \boxed{+4{,}5\%}$.
> **La règle** : quand la demande est **inélastique**, une hausse de prix **augmente** la recette.

## M6 — Production et coûts

**M6.1** $CT(q) = 100 + 2q + 0{,}5q^2$. Donne $CF$, $CV$, $CM$, $CVM$, $Cm$. Trouve le minimum de $CM$ et vérifie que $Cm$ y passe.
**M6.2** $Q = K^{0,5}L^{0,5}$, $w = 4$, $r = 9$. Minimise le coût de production de $Q = 60$.
**M6.3** $Q = 10K^{0,3}L^{0,5}$. Rendements d'échelle ?

> [!success]- Corrigés M6
> **M6.1** $CF = 100$ · $CV = 2q+0{,}5q^2$ · $CM = \frac{100}{q}+2+0{,}5q$ · $CVM = 2+0{,}5q$ · $Cm = 2+q$
> $CM' = -\frac{100}{q^2}+0{,}5 = 0 \Rightarrow q^2 = 200 \Rightarrow \boxed{q = 14{,}14}$
> $CM(14{,}14) = 7{,}07+2+7{,}07 = \boxed{16{,}14}$ · $Cm(14{,}14) = 2+14{,}14 = \boxed{16{,}14}$ ✓
> **M6.2** $TMST = \frac{Pm_L}{Pm_K} = \frac{K}{L} = \frac{w}{r} = \frac{4}{9} \Rightarrow K = \frac{4L}{9}$
> $Q = \sqrt{KL} = \sqrt{\frac{4L^2}{9}} = \frac{2L}{3} = 60 \Rightarrow \boxed{L^* = 90},\ \boxed{K^* = 40}$
> Coût minimal $= 4(90)+9(40) = \boxed{720}$
> **M6.3** $0{,}3+0{,}5 = 0{,}8 < 1$ → **rendements d'échelle décroissants**. Doubler les facteurs multiplie $Q$ par $2^{0,8} = 1{,}74$ seulement.

## M7 — Maximisation du profit

**M7.1** $CT(q) = q^3 - 12q^2 + 60q + 50$, prix de marché $p = 60$.
a) Quantité optimale ? Vérifie le second ordre.
b) Profit ?
c) Seuil de fermeture ?

> [!success]- Corrigé M7.1
> **a)** $Cm = 3q^2 - 24q + 60 = 60 \Rightarrow 3q(q-8) = 0 \Rightarrow \boxed{q^* = 8}$
> Second ordre : $Cm'(q) = 6q-24$, $Cm'(8) = 24 > 0$ ✓
> **b)** $CT(8) = 512 - 768 + 480 + 50 = 274$. $RT = 480$. $\boxed{\pi = 206}$
> **c)** $CVM = q^2-12q+60$, minimum en $q = 6$ : $CVM(6) = 36-72+60 = \boxed{24}$
> **Si $p < 24$, l'entreprise ferme** (elle ne couvre même plus ses coûts variables). Entre 24 et le minimum de $CM$, elle produit à perte mais limite ses pertes au coût fixe.

## M8 — Équilibre, taxe, monopole ⭐

Marché : $Q_d = 300 - 5P$ et $Q_s = 5P - 50$.

**M8.1** Équilibre $P^*$, $Q^*$. Calcule les deux surplus.
**M8.2** L'État instaure une **taxe de 6 € par unité** payée par le producteur. Nouvel équilibre, partage de la taxe, recette fiscale, perte sèche.
**M8.3** Le marché devient un **monopole** de coût marginal constant $Cm = 10$. Prix et quantité ? Compare à la concurrence. Calcule l'indice de Lerner.

> [!success]- Corrigé M8.1
> $300-5P = 5P-50 \Rightarrow 350 = 10P \Rightarrow \boxed{P^* = 35}$, $Q^* = 300-175 = \boxed{125}$
> Prix maximal (demande nulle) : $P = 60$. Prix minimal (offre nulle) : $P = 10$.
> $SC = \frac{1}{2}(60-35)(125) = \boxed{1562{,}5}$ · $SP = \frac{1}{2}(35-10)(125) = \boxed{1562{,}5}$
> Surplus total $= 3125$.

> [!success]- Corrigé M8.2
> L'offre devient $Q_s = 5(P-6)-50 = 5P-80$.
> $300-5P = 5P-80 \Rightarrow 380 = 10P \Rightarrow \boxed{P_{cons} = 38}$, $Q' = \boxed{110}$
> Prix net reçu par le producteur : $38-6 = \boxed{32}$
> **Partage de la taxe** : le consommateur paie 3 € (38 − 35), le producteur 3 € (35 − 32) → **50/50**.
> *Pourquoi ?* Les deux courbes ont la **même pente en valeur absolue** (5), donc les mêmes élasticités au point d'équilibre. Le partage suit toujours l'inverse des élasticités.
> **Recette fiscale** $= 6 \times 110 = \boxed{660}$
> **Perte sèche** $= \frac{1}{2}\times 6 \times (125-110) = \boxed{45}$

> [!success]- Corrigé M8.3
> Demande inverse : $P = 60 - \frac{Q}{5}$. Donc $RT = 60Q - \frac{Q^2}{5}$ et $Rm = 60 - \frac{2Q}{5}$.
> $Rm = Cm$ : $60 - 0{,}4Q = 10 \Rightarrow \boxed{Q_M = 125}$, $P_M = 60-25 = \boxed{35}$
> **Concurrence** ($P = Cm = 10$) : $Q_C = 300-50 = \boxed{250}$
> Le monopole produit **moitié moins** et vend **3,5 fois plus cher**.
> **Indice de Lerner** $= \dfrac{P-Cm}{P} = \dfrac{25}{35} = \boxed{0{,}714}$ — pouvoir de marché très élevé.
> **Le point à retenir** : $Rm < P$ toujours en monopole, car pour vendre une unité de plus il faut baisser le prix **sur toutes les unités**.

---
# 🌍 MACROÉCONOMIE — UE 11B

## N1 — La mesure du PIB

**N1.1** Une entreprise réalise 500 M€ de chiffre d'affaires et consomme 180 M€ de biens intermédiaires. Quelle est sa valeur ajoutée ?
**N1.2** PIB nominal : 2 300 Md€ en 2020, 2 700 Md€ en 2024. Déflateur : 100 en 2020, 112 en 2024.
a) PIB réel 2024 aux prix de 2020 ?
b) Croissance nominale, croissance réelle, inflation ? Vérifie la cohérence.
**N1.3** Pourquoi le PIB ne compte-t-il pas le travail domestique ? Cite deux autres limites.

> [!success]- Corrigés N1
> **N1.1** $VA = 500 - 180 = \boxed{320\ \text{M€}}$
> **N1.2**
> a) $\frac{2700}{1{,}12} = \boxed{2410{,}7\ \text{Md€}}$
> b) Nominale : $\frac{2700}{2300}-1 = \boxed{+17{,}39\%}$ · Réelle : $\frac{2410,7}{2300}-1 = \boxed{+4{,}81\%}$ · Inflation : $\boxed{+12\%}$
> **Vérification** : $\frac{1{,}1739}{1{,}12} = 1{,}0481$ ✓ Les taux se **composent**, ils ne s'additionnent pas.
> **N1.3** Le travail domestique n'est pas **marchand** : il n'y a ni transaction ni prix observable. Autres limites : le PIB ignore les **externalités négatives** (une marée noire augmente le PIB via les dépenses de dépollution), il ne dit rien de la **répartition**, et il ne mesure pas le patrimoine ni la soutenabilité.

## N2–N3 — Consommation et multiplicateur ⭐

**N3.1** $C = 0{,}75Y + 200$, $I = 150$, $G = 250$. Calcule le revenu d'équilibre et le multiplicateur.
**N3.2** $\Delta G = +50$. Quel est $\Delta Y$ ?
**N3.3** $C = 0{,}8(Y - T) + 100$, $T = 0{,}25Y$, $I = 200$, $G = 300$. Revenu d'équilibre et multiplicateur.
**N3.4** **Théorème de Haavelmo** — avec $c = 0{,}8$ et une taxe forfaitaire, on augmente simultanément $G$ et $T$ de 100. Quel est $\Delta Y$ ?
**N3.5** Explique le paradoxe de l'épargne.

> [!success]- Corrigés N3
> **N3.1** $Y = 0{,}75Y + 200 + 150 + 250 \Rightarrow 0{,}25Y = 600 \Rightarrow \boxed{Y^* = 2400}$, $k = \frac{1}{0,25} = \boxed{4}$
> **N3.2** $\Delta Y = 4 \times 50 = \boxed{+200}$
> **N3.3** $Y = 0{,}8(0{,}75Y) + 100 + 200 + 300 = 0{,}6Y + 600 \Rightarrow 0{,}4Y = 600 \Rightarrow \boxed{Y^* = 1500}$, $k = \boxed{2{,}5}$
> **L'enseignement** : la fiscalité proportionnelle est un **stabilisateur automatique** — elle réduit le multiplicateur de 5 à 2,5, donc amortit les chocs dans les deux sens.
> **N3.4** $\Delta Y = \frac{\Delta G}{1-c} - \frac{c\,\Delta T}{1-c} = \frac{100}{0,2} - \frac{80}{0,2} = 500 - 400 = \boxed{+100}$
> **Le multiplicateur du budget équilibré vaut 1.** Une hausse de $G$ financée par l'impôt reste expansionniste, parce que $G$ est dépensé intégralement alors que la baisse de revenu disponible n'est répercutée qu'à hauteur de $c$.
> **N3.5** Si tous les ménages augmentent leur propension à épargner, la consommation baisse, donc la demande, donc la production, donc le revenu. **L'épargne totale finale peut être inchangée ou plus faible** malgré l'effort d'épargne. Ce qui est rationnel individuellement est contre-productif collectivement.

## N4 — Marché du travail

**N4.1** Population totale 67 M · population en âge de travailler (15-64 ans) 41 M · population active 30 M · chômeurs 2,4 M. Calcule le taux de chômage, le taux d'activité et le taux d'emploi.
**N4.2** Distingue chômage frictionnel, structurel, conjoncturel, classique et keynésien.

> [!success]- Corrigés N4
> **N4.1**
> Taux de chômage $= \frac{2,4}{30} = \boxed{8\%}$ *(chômeurs / actifs, jamais / population totale)*
> Taux d'activité $= \frac{30}{41} = \boxed{73{,}2\%}$
> Emploi $= 30 - 2{,}4 = 27{,}6$ M → taux d'emploi $= \frac{27,6}{41} = \boxed{67{,}3\%}$
> **N4.2**
> - **Frictionnel** : délais normaux d'appariement entre offres et demandes d'emploi. Incompressible.
> - **Structurel** : inadéquation durable entre qualifications disponibles et emplois offerts.
> - **Conjoncturel** : lié au cycle, insuffisance temporaire de la demande.
> - **Classique** : le salaire réel est trop élevé, l'offre de travail excède la demande (rigidités).
> - **Keynésien** : insuffisance de la **demande effective** — les entreprises n'embauchent pas parce qu'elles n'anticipent pas de débouchés, indépendamment du niveau des salaires.

## N5 — Monnaie et inflation

**N5.1** Le taux de réserves obligatoires est de 5 %, sans fuite en billets. Quel est le multiplicateur de crédit ? Si la base monétaire vaut 100 Md€, quelle masse monétaire ?
**N5.2** Équation quantitative : $M = 1500$, $V = 4$, $Y = 2500$. Quel est le niveau général des prix ?
**N5.3** L'IPC passe de 108 à 112,3. Taux d'inflation ?
**N5.4** Explique pourquoi la création monétaire est le fait des **banques commerciales** et non de la banque centrale.

> [!success]- Corrigés N5
> **N5.1** $m = \frac{1}{r} = \frac{1}{0,05} = \boxed{20}$. Masse monétaire $= 20 \times 100 = \boxed{2000\ \text{Md€}}$
> **N5.2** $MV = PY \Rightarrow P = \frac{1500 \times 4}{2500} = \boxed{2{,}4}$
> **N5.3** $\frac{112,3}{108}-1 = \boxed{+3{,}98\%}$
> **N5.4** **« Les crédits font les dépôts »** : quand une banque accorde un crédit, elle inscrit simultanément une créance à son actif et un dépôt au passif — elle crée de la monnaie *ex nihilo*. La banque centrale ne crée que la **monnaie centrale** (billets et réserves) et **encadre** cette création via les taux directeurs et les réserves obligatoires.
> 📎 Voir **Heu?reka** sur YouTube.

## N6 — IS-LM ⭐

On donne : $\text{IS} : Y = 3000 - 100i$ et $\text{LM} : Y = 1000 + 100i$

**N6.1** Trouve $Y^*$ et $i^*$.
**N6.2** Une relance budgétaire déplace IS de +500 : $Y = 3500 - 100i$. Nouvel équilibre ? Compare $\Delta Y$ à 500. Comment appelle-t-on l'écart ?
**N6.3** Décris ce qui se passe en **trappe à liquidité** (LM horizontale).
**N6.4** Un keynésien et un monétariste regardent le même graphique IS-LM. Pourquoi ne recommandent-ils pas la même politique ?

> [!success]- Corrigés N6
> **N6.1** $3000-100i = 1000+100i \Rightarrow 2000 = 200i \Rightarrow \boxed{i^* = 10\%}$, $\boxed{Y^* = 2000}$
> **N6.2** $3500-100i = 1000+100i \Rightarrow 2500 = 200i \Rightarrow \boxed{i^* = 12{,}5\%}$, $\boxed{Y^* = 2250}$
> $\Delta Y = 250$, alors que le déplacement de IS était de 500.
> **L'écart de 250 est l'effet d'éviction** ($crowding\ out$) : la hausse du revenu accroît la demande de monnaie, donc le taux d'intérêt, ce qui décourage l'investissement privé et annule la moitié de la relance.
> **N6.3** LM horizontale : le taux d'intérêt est au plancher, la demande de monnaie est infiniment élastique. La **politique monétaire est totalement inefficace** (déplacer LM ne change rien), et la **politique budgétaire est pleinement efficace** (aucun effet d'éviction : $\Delta Y = k\Delta G$ intégralement).
> **N6.4**
> - Le **keynésien** juge IS peu sensible au taux (investissement piloté par la demande anticipée) et LM plutôt plate → **la politique budgétaire est puissante**, l'éviction est faible.
> - Le **monétariste** juge IS très sensible au taux et LM très pentue → **l'éviction est quasi totale**, la relance budgétaire ne fait que déplacer la dépense du privé vers le public. Il privilégie une règle monétaire stable.
>
> **Le même graphique, deux jeux de pentes, deux conclusions opposées.** C'est un excellent sujet de dissertation.

---
# 📐 MATHÉMATIQUES — UE 14B

**P.1** Maximise $f(x,y) = xy$ sous la contrainte $2x + 3y = 60$. Donne aussi $\lambda$ et son interprétation.
**P.2** Maximise $f(x,y) = x^{0,5}y^{0,5}$ sous $x + 4y = 100$.
**P.3** $f(x,y) = 4x^{0,25}y^{0,75}$. Est-elle homogène ? Vérifie le théorème d'Euler.
**P.4** Calcule le surplus du consommateur par intégration pour $Q_d = 100-2P$ à l'équilibre $P^* = 20$.
**P.5** Résoudre par inversion matricielle : $\begin{cases} 3x + 2y = 19 \\ x + 4y = 23\end{cases}$
**P.6** $f(x,y) = x^2 + 4y^2 - 2x + 8y$. Trouve le point critique et détermine sa nature (hessienne).

> [!success]- Corrigés P
> **P.1** $\mathcal{L} = xy + \lambda(60-2x-3y)$. CPO : $y = 2\lambda$ et $x = 3\lambda$, donc $\frac{x}{y} = \frac{3}{2}$, soit $x = 1{,}5y$.
> Contrainte : $2(1{,}5y)+3y = 60 \Rightarrow 6y = 60 \Rightarrow \boxed{y^* = 10,\ x^* = 15}$, $f^* = \boxed{150}$
> $\lambda = \frac{y}{2} = \boxed{5}$ → **si la contrainte passait de 60 à 61, $f$ augmenterait d'environ 5.**
> **P.2** Cobb-Douglas, parts $\frac{1}{2}$ : $x^* = \frac{0,5\times100}{1} = \boxed{50}$, $y^* = \frac{0,5\times100}{4} = \boxed{12{,}5}$, $f^* = \sqrt{625} = \boxed{25}$
> **P.3** $f(\lambda x,\lambda y) = 4\lambda^{0,25}x^{0,25}\lambda^{0,75}y^{0,75} = \lambda\,f(x,y)$ → **homogène de degré 1** (rendements constants).
> Euler : $x f_x + y f_y = x(x^{-0,75}y^{0,75}) + y(3x^{0,25}y^{-0,25}) = x^{0,25}y^{0,75} + 3x^{0,25}y^{0,75} = 4x^{0,25}y^{0,75} = f$ ✓ (degré 1)
> **P.4** Demande inverse : $P = 50 - \frac{Q}{2}$. À $P^*=20$ : $Q^* = 60$.
> $$SC = \int_0^{60}\left(50-\frac{q}{2}\right)dq - 20\times60 = \left[50q-\frac{q^2}{4}\right]_0^{60} - 1200 = (3000-900)-1200 = \boxed{900}$$
> Vérification géométrique (triangle) : $\frac{1}{2}(50-20)(60) = 900$ ✓
> **P.5** $\det = 3(4)-2(1) = 10$. $x = \frac{19(4)-2(23)}{10} = \frac{30}{10} = \boxed{3}$, $y = \frac{3(23)-19(1)}{10} = \frac{50}{10} = \boxed{5}$
> **P.6** $f_x = 2x-2 = 0 \Rightarrow x=1$ · $f_y = 8y+8 = 0 \Rightarrow y=-1$. Point critique $\boxed{(1,-1)}$.
> Hessienne : $\begin{pmatrix}2 & 0\\0 & 8\end{pmatrix}$, déterminant $= 16 > 0$ et $f_{xx} = 2 > 0$ → **minimum local**. $f(1,-1) = 1+4-2-8 = -5$

---
---

# 🎯 EXAMEN BLANC — CYCLE 1

> [!warning] Conditions
> **3 heures · sans notes · calculatrice autorisée · noté sur 60**
> Partie A micro (25) · Partie B macro (20) · Partie C maths (15)

## PARTIE A — Microéconomie (25 pts)

**A1.** Un consommateur a $U(x,y) = x^{0,4}y^{0,6}$, avec $p_x = 4$, $p_y = 3$, $R = 240$. **(8 pts)**
a) Écris le Lagrangien et les conditions du premier ordre.
b) Détermine $x^*$ et $y^*$.
c) Calcule $U^*$.
d) Vérifie que les parts de dépense correspondent bien aux exposants.

**A2.** $Q_d = 180 - 3P$. **(5 pts)**
a) Élasticité-prix en $P = 30$ et en $P = 45$.
b) À quel prix la recette est-elle maximale ? Justifie par l'élasticité.

**A3.** $CT(q) = q^3 - 15q^2 + 80q + 100$, prix de marché $p = 80$. **(7 pts)**
a) Quantité optimale et vérification du second ordre.
b) Profit.
c) Seuil de fermeture.

**A4.** Marché : $Q_d = 400 - 4P$, $Q_s = 6P - 100$. **(5 pts)**
a) Équilibre.
b) Une taxe de 5 € par unité frappe le producteur. Nouveau prix consommateur, prix producteur, et **partage de la taxe**. Commente au regard des pentes.

## PARTIE B — Macroéconomie (20 pts)

**B1.** $C = 0{,}7(Y-T) + 150$, $T = 0{,}2Y$, $I = 250$, $G = 350$. **(6 pts)**
a) Revenu d'équilibre et multiplicateur.
b) $\Delta G = +40$ : quel est $\Delta Y$ ?
c) Pourquoi le multiplicateur est-il plus faible qu'en l'absence d'impôt proportionnel ?

**B2.** PIB nominal : 2 450 Md€ en 2023, 2 620 Md€ en 2024. Déflateur : 100 puis 103,5. **(5 pts)**
a) Croissance nominale, inflation, croissance réelle.
b) La consommation pèse 53 % du PIB et croît de 1,1 % en volume. Sa contribution à la croissance ?

**B3.** IS : $Y = 4000 - 200i$ · LM : $Y = 1500 + 300i$ **(6 pts)**
a) Équilibre $Y^*$, $i^*$.
b) La banque centrale accroît l'offre de monnaie : LM devient $Y = 2000 + 300i$. Nouvel équilibre. Commente l'effet sur le taux et sur l'activité.

**B4.** En quatre lignes : pourquoi la création monétaire est-elle le fait des banques commerciales ? **(3 pts)**

## PARTIE C — Mathématiques (15 pts)

**C1.** Maximise $f(x,y) = x^{0,5}y^{0,5}$ sous $3x + 2y = 120$. Donne $\lambda$ et interprète-le. **(6 pts)**

**C2.** $Q = 6K^{0,35}L^{0,65}$. **(4 pts)**
a) Rendements d'échelle ?
b) Calcule $Pm_K$ et $Pm_L$.
c) Par combien $Q$ est-il multiplié si on triple les deux facteurs ?

**C3.** Calcule le surplus du producteur par intégration pour $Q_s = 4P - 40$ à l'équilibre $P^* = 25$. **(5 pts)**

---

> [!success]- 📝 CORRIGÉ COMPLET DE L'EXAMEN BLANC
>
> ## PARTIE A (25 pts)
>
> **A1.** *(8 pts)*
> a) $\mathcal{L} = x^{0,4}y^{0,6} + \lambda(240-4x-3y)$
> CPO : $0{,}4x^{-0,6}y^{0,6} = 4\lambda$ · $0{,}6x^{0,4}y^{-0,4} = 3\lambda$
> b) En divisant : $TMS = \frac{0,4}{0,6}\cdot\frac{y}{x} = \frac{4}{3} \Rightarrow \frac{2y}{3x} = \frac{4}{3} \Rightarrow y = 2x$
> Budget : $4x + 3(2x) = 240 \Rightarrow 10x = 240 \Rightarrow \boxed{x^* = 24,\ y^* = 48}$
> *(Vérification par la formule Cobb-Douglas : $x^* = 0{,}4\times\frac{240}{4} = 24$ ✓ · $y^* = 0{,}6\times\frac{240}{3} = 48$ ✓)*
> c) $U^* = 24^{0,4}\times48^{0,6} = \boxed{36{,}38}$
> d) Dépense en $x$ : $4\times24 = 96$, soit $\frac{96}{240} = \boxed{40\%}$ ✓ Dépense en $y$ : $3\times48 = 144$, soit $\boxed{60\%}$ ✓
> **Les parts de dépense égalent exactement les exposants** — propriété fondamentale de la Cobb-Douglas.
>
> **A2.** *(5 pts)*
> a) $\varepsilon = -3\cdot\frac{P}{Q}$. En $P=30$ : $Q = 90$, $\varepsilon = \boxed{-1}$. En $P=45$ : $Q = 45$, $\varepsilon = \boxed{-3}$.
> b) **La recette est maximale là où $\varepsilon = -1$, soit $P = 30$.** $RT = 30\times90 = \boxed{2700}$.
> **Justification** : tant que $|\varepsilon|<1$, une hausse de prix augmente la recette ; dès que $|\varepsilon|>1$, elle la diminue. Le maximum est donc au point d'élasticité unitaire.
>
> **A3.** *(7 pts)*
> a) $Cm = 3q^2-30q+80 = 80 \Rightarrow 3q(q-10) = 0 \Rightarrow \boxed{q^* = 10}$
> $Cm'(q) = 6q-30$, $Cm'(10) = 30 > 0$ ✓ maximum de profit.
> b) $CT(10) = 1000-1500+800+100 = 400$. $RT = 800$. $\boxed{\pi = 400}$
> c) $CVM = q^2-15q+80$, minimum en $q = 7{,}5$ : $CVM(7{,}5) = 56{,}25-112{,}5+80 = \boxed{23{,}75}$
> **En dessous de $p = 23{,}75$, l'entreprise ferme.**
>
> **A4.** *(5 pts)*
> a) $400-4P = 6P-100 \Rightarrow 500 = 10P \Rightarrow \boxed{P^* = 50}$, $Q^* = \boxed{200}$
> b) Offre taxée : $Q_s = 6(P-5)-100 = 6P-130$.
> $400-4P = 6P-130 \Rightarrow 530 = 10P \Rightarrow \boxed{P_{cons} = 53}$, $Q' = \boxed{188}$
> Prix net producteur : $53-5 = \boxed{48}$
> **Partage** : consommateur $+3$ (53−50), producteur $-2$ (50−48) → **60 % / 40 %**.
> **Commentaire** : l'offre a une pente de 6, la demande de 4 (en valeur absolue). **L'offre est plus élastique**, donc le producteur échappe davantage à la taxe. La charge pèse toujours le plus sur le côté le moins élastique — ici le consommateur.
>
> ## PARTIE B (20 pts)
>
> **B1.** *(6 pts)*
> a) $Y = 0{,}7(0{,}8Y)+150+250+350 = 0{,}56Y + 750 \Rightarrow 0{,}44Y = 750 \Rightarrow \boxed{Y^* = 1704{,}5}$
> $k = \frac{1}{0,44} = \boxed{2{,}27}$
> b) $\Delta Y = 2{,}27\times40 = \boxed{+90{,}9}$
> c) Sans impôt proportionnel, $k = \frac{1}{1-0,7} = 3{,}33$. **L'impôt proportionnel est une fuite** : une partie de chaque euro de revenu supplémentaire est prélevée avant d'être consommée, ce qui casse la chaîne du multiplicateur. C'est le mécanisme du **stabilisateur automatique**.
>
> **B2.** *(5 pts)*
> a) Nominale : $\frac{2620}{2450}-1 = \boxed{+6{,}94\%}$ · Inflation : $\boxed{+3{,}5\%}$ · Réelle : $\frac{1,0694}{1,035}-1 = \boxed{+3{,}32\%}$
> b) $0{,}53 \times 1{,}1 = \boxed{+0{,}58\ \text{point}}$ — la consommation explique environ **18 % de la croissance** ($\frac{0,58}{3,32}$).
>
> **B3.** *(6 pts)*
> a) $4000-200i = 1500+300i \Rightarrow 2500 = 500i \Rightarrow \boxed{i^* = 5\%}$, $Y^* = 4000-1000 = \boxed{3000}$
> b) $4000-200i = 2000+300i \Rightarrow 2000 = 500i \Rightarrow \boxed{i^* = 4\%}$, $Y^* = 4000-800 = \boxed{3200}$
> **Commentaire** : l'expansion monétaire **fait baisser le taux d'intérêt** (de 5 % à 4 %), ce qui **stimule l'investissement** et donc l'activité (+200, soit +6,7 %). C'est le **canal du taux d'intérêt** de la politique monétaire. Contrairement à la relance budgétaire, il n'y a **pas d'effet d'éviction** — au contraire, l'investissement privé est encouragé.
>
> **B4.** *(3 pts)*
> Quand une banque commerciale accorde un crédit, elle inscrit une créance à son actif et **crée simultanément un dépôt au passif** du client. La monnaie naît de cette double écriture, sans qu'aucune épargne préalable ne soit nécessaire : **« les crédits font les dépôts »**. La banque centrale ne crée que la monnaie centrale (billets, réserves) et n'encadre cette création qu'indirectement, par les taux directeurs et les réserves obligatoires.
>
> ## PARTIE C (15 pts)
>
> **C1.** *(6 pts)*
> $\mathcal{L} = x^{0,5}y^{0,5} + \lambda(120-3x-2y)$
> $TMS = \frac{y}{x} = \frac{3}{2} \Rightarrow y = 1{,}5x$. Budget : $3x + 2(1{,}5x) = 120 \Rightarrow 6x = 120$
> $$\boxed{x^* = 20,\ y^* = 30}$$
> $f^* = \sqrt{600} = \boxed{24{,}49}$
> $\lambda = \frac{0,5x^{-0,5}y^{0,5}}{3} = \frac{0,5\sqrt{30/20}}{3} = \frac{0,5\times1,2247}{3} = \boxed{0{,}204}$
> **Interprétation** : un euro de revenu supplémentaire augmenterait l'utilité maximale d'environ **0,204**.
>
> **C2.** *(4 pts)*
> a) $0{,}35+0{,}65 = 1$ → **rendements d'échelle constants**
> b) $Pm_K = 2{,}1\,K^{-0,65}L^{0,65}$ · $Pm_L = 3{,}9\,K^{0,35}L^{-0,35}$
> c) $3^1 = \boxed{3}$ — tripler les facteurs triple exactement la production.
>
> **C3.** *(5 pts)*
> Offre inverse : $P = \frac{Q+40}{4} = 10 + \frac{Q}{4}$. À $P^* = 25$ : $Q^* = 4(25)-40 = 60$.
> $$SP = P^*Q^* - \int_0^{60}\left(10+\frac{q}{4}\right)dq = 1500 - \left[10q+\frac{q^2}{8}\right]_0^{60} = 1500 - (600+450) = \boxed{450}$$
> Vérification géométrique : $\frac{1}{2}(25-10)(60) = 450$ ✓

---

## 🎓 Barème de décision

| Note /60 | Verdict |
|---|---|
| **48–60** | ✅ Passe au [[Cycle 2 - Les chiffres]] |
| **36–47** | ⚠️ Passe, mais reprends les modules où tu as perdu plus de 40 % des points |
| **< 36** | 🛑 Reprends le [[Cycle 1 - Moteur economique]] sur les semaines faibles avant d'avancer |

> [!danger] Rappel
> Micro, macro et maths sont évaluées en **période 4**, avec **CC (coef 2) + CT (coef 3)** chacune. Le CC est **reporté en session 2** : il ne se rattrape pas. Fais tes exercices de TD **avant** les séances.

→ Exercices suivants : [[Exercices - Cycle 2]]
