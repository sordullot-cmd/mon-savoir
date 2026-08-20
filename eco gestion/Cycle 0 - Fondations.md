---
tags:
  - L1-eco-gestion
  - cycle-0
  - quantitatif
semaines: S1-S4
heures: 48
UE: 14A Bases de maths, 18C Méthodologie
coefficients: 4
periode: P1, P2
statut: à faire
---

# 🧱 Cycle 0 — Fondations

**S1 → S4 · 48 h · UE 14A Bases de maths (coef 2, CC, P2) + 18C Méthodologie (coef 2, CC, P1)**
← [[00 - Plan L1 Angers]] · → [[Cycle 1 - Moteur economique]] · 📚 [[Ressources - Bibliotheque de liens]]

> [!abstract] Objectif unique et mesurable
> À la fin de la semaine 4, tu dois pouvoir calculer les deux dérivées partielles d'une fonction Cobb-Douglas **de tête, en moins de 30 secondes, sans notes**.
>
> Tout le reste du cycle 0 existe pour rendre ça possible.

---

## ⚠️ Pourquoi ce cycle décide de l'année

UE 14A vaut **2 coefficients sur 62**. C'est presque rien. Et pourtant elle conditionne **16 ECTS** : Microéconomie (5), Mathématiques (5), Statistiques (5).

En économie, on ne fait presque jamais de mathématiques difficiles. On fait des mathématiques de niveau première-terminale, **appliquées vite, sous pression, dans un contexte qui les déguise**. Un étudiant qui hésite sur $(uv)'$ ne rate pas un point de maths : il rate le calcul du coût marginal, donc l'optimum du producteur, donc l'exercice entier.

**Le goulot d'étranglement de la L1 éco-gestion n'est pas la difficulté conceptuelle, c'est la fluidité de calcul.**

> [!danger] Deux particularités de la maquette officielle
> **1. UE 14A est évaluée en CONTRÔLE CONTINU** (coef 2, P2), pas par un examen final. Tu ne peux pas la bachoter : elle se joue en TD, semaine après semaine, dès le début de l'année.
>
> **2. UE 18C Méthodologie pèse 2 coefficients pour 1 crédit**, elle est évaluée en CC dès la **période 1** — c'est ta toute première note — et elle appartient au **socle transversal non compensable**. Ce n'est pas une formalité administrative.

> [!warning] Le contre-sens à éviter
> « Les maths, je verrai ça en cours. » Non. En cours, l'enseignant de microéconomie **supposera** les dérivées partielles acquises et passera à autre chose en trois minutes. Personne ne reviendra en arrière pour toi. Ces quatre semaines sont les seules où tu peux te le permettre.

---

## 🗺️ Les 7 modules

| Module | Contenu | h | Débloque |
|---|---|---|---|
| **A** | Calcul algébrique et pourcentages | 12 h | Statistiques, macro, tous les calculs chiffrés |
| **B** | Fonctions et systèmes | 6 h | Micro, équilibre de marché |
| **C** | Dérivation | 9 h | **Tout le raisonnement marginal** |
| **D** | Logarithme et exponentielle | 3 h | Croissance, élasticités, stats |
| **E** | Dérivées partielles | 6 h | Optimisation du consommateur, TMS |
| **F** | Suites | 1 h 30 | Multiplicateur keynésien, actualisation |
| **G** | Reconnaissance, méthode, test | 10 h 30 | Le reste du plan |

**Priorité si tu manques de temps** : A → C → E. Les modules B, D, F sont rattrapables en [[Cycle 1 - Moteur economique|cycle 1]].

---

# 📅 SEMAINE 1 — Reconnaissance + calcul algébrique

## Session 1 (1 h 30) — Reconnaissance administrative
- [ ] Mail à `l1deg@univ-angers.fr` : **dates des périodes P1-P4**, **nature de chaque CC**, **règle de compensation intra-socle**, **annales**
- [ ] Inscription au **dispositif DARRE** (tutorat + accompagnement, gratuit, toute l'année)
- [ ] BU Belle-Beille : accès annales + vérifier l'accès [Cairn.info](https://www.cairn.info/)
- [ ] Repérer l'association étudiante de la Faculté DEG (banque de sujets)
- [ ] Moodle UA : plans de cours et bibliographies

## Sessions 2–3 (3 h) — Mission 0 : rétro-ingénierie
Sur les annales de **trois UE** (macro, micro, statistiques), produis **une page par UE** :
- [ ] Quels **types** de questions reviennent, dans quelles **proportions** ?
- [ ] Quel **barème apparent** ?
- [ ] Quelles notions n'ont **jamais** été demandées en 3 ans ?
- [ ] Le sujet est-il **structuré à l'identique** d'une année sur l'autre ?

📎 **En attendant les annales** : passe le test [Faq2Sciences](https://www.faq2sciences.fr/), module Mathématiques. 40 minutes pour une carte objective de tes lacunes.

## Session 4 (1 h 30) — Monter le système
- [ ] Arborescence de fiches : **une page A4, recto seulement**, par UE
- [ ] [Anki](https://apps.ankiweb.net/) — 4 sous-decks : `Définitions` · `Formules` · `Auteurs` · `Écritures comptables`
- [ ] **Tes 15 premières cartes** : les dérivées usuelles et les 4 règles, depuis le [formulaire Exo7](http://exo7.emath.fr/cours/formules.pdf). Tu les verras 21 fois avant la semaine 4.

---

## Sessions 5–8 (6 h) — MODULE A₁ : calcul algébrique

### A1 — Fractions et puissances (1 h 30)
- [ ] Fractions : addition, multiplication, division, simplification
- [ ] Puissances : $a^m \cdot a^n = a^{m+n}$ · $(a^m)^n = a^{mn}$ · $a^{-n} = \frac{1}{a^n}$ · $a^{1/n} = \sqrt[n]{a}$
- [ ] Racines : $\sqrt{ab} = \sqrt{a}\sqrt{b}$, et savoir que $\sqrt{a+b} \neq \sqrt{a} + \sqrt{b}$

📎 [Khan Academy](https://fr.khanacademy.org/math/cycle-4-v2) · [Maths et tiques](https://www.maths-et-tiques.fr/) · [WIMS](https://wims.math.cnrs.fr/wims/) → « calcul algébrique »

**Maîtrise** : simplifier $\dfrac{(x^3y^{-2})^2}{x^{-1}y^3}$ sans hésitation.

> [!tip] Pourquoi ça compte
> Les fonctions de production et d'utilité en économie sont presque toutes des **fonctions puissance** (Cobb-Douglas : $Y = A K^\alpha L^\beta$). Si les exposants ne sont pas fluides, la micro devient impraticable.

### A2 — Développement, factorisation, équations (2 h)
- [ ] Identités remarquables : $(a+b)^2$, $(a-b)^2$, $(a+b)(a-b)$
- [ ] Factorisation par le facteur commun
- [ ] Équations du 1er degré
- [ ] **2nd degré** : $\Delta = b^2 - 4ac$, racines, factorisation, somme et produit

📎 [Maths et tiques](https://www.maths-et-tiques.fr/) → « Second degré » · [Exo7 fic00097](http://exo7.emath.fr/ficpdf/fic00097.pdf) · [WIMS](https://wims.math.cnrs.fr/wims/)

**Maîtrise** : résoudre $2x^2 - 7x + 3 = 0$ en moins d'une minute.

### A3 — Inéquations et tableaux de signes (1 h 30)
- [ ] Inéquations du 1er et 2nd degré
- [ ] **Tableau de signes** d'un produit et d'un quotient
- [ ] Signe selon les valeurs d'un paramètre

📎 [Exo7 fic00087](http://exo7.emath.fr/ficpdf/fic00087.pdf) · [WIMS](https://wims.math.cnrs.fr/wims/)

> [!tip] Ce n'est pas un exercice scolaire
> Le tableau de signes est l'outil qui, en [[Cycle 1 - Moteur economique|cycle 1]], te servira à déterminer où une dérivée est positive — donc où le profit augmente, donc où se trouve l'optimum. C'est *la* technique de recherche d'optimum.

### A4 — Consolidation (1 h)
- [ ] 40 exercices mélangés, chronométrés, sur [WIMS](https://wims.math.cnrs.fr/wims/). Objectif : **35/40**.

---

# 📅 SEMAINE 2 — Pourcentages, taux, fonctions

## Sessions 1–4 (6 h) — MODULE A₂ : pourcentages et taux

> [!danger] Lis cet avertissement
> C'est **ici**, et nulle part ailleurs, que les étudiants d'éco-gestion perdent le plus de points sur toute leur licence. Pas en calcul différentiel — en pourcentages. Parce que tout le monde croit maîtriser, et presque personne ne maîtrise.

### A5 — Proportions et taux de variation (1 h 30)
- [ ] Proportion, part, répartition en %
- [ ] **Taux de variation** : $t = \dfrac{V_1 - V_0}{V_0}$
- [ ] **Coefficient multiplicateur** : $CM = 1 + t$ — passer de l'un à l'autre instantanément
- [ ] Retrouver $V_0$ connaissant $V_1$ et $t$ (le calcul « à l'envers », très fréquent)

📎 **La meilleure ressource pour ce point** : [Khan Academy — Automatismes : proportions, pourcentages, évolutions](https://fr.khanacademy.org/math/premieres-technologiques/xe0f38a7ca0048ef2:automatismes) — le module de la filière technologique, exactement calibré pour l'éco.
📎 S'entraîner : [Khan — problèmes de pourcentages](https://fr.khanacademy.org/math/be-1ere-secondaire2/xe5303a9b201c0f84:nombres-proportionnalite-et-pourcentages/xe5303a9b201c0f84:problemes-de-pourcentages/e/percentage_word_problems_1) · [Annales2Maths](https://www.annales2maths.com/2nd-exercices-corriges-pourcentages-et-calcul-de-variations/)

### A6 — Les quatre pièges classiques (2 h)
- [ ] **Variations successives** : $CM_{total} = CM_1 \times CM_2$. Une hausse de 12 % suivie d'une baisse de 8 % donne **+3,04 %**, pas +4 %. *Les taux ne s'additionnent jamais.*
- [ ] **Point vs pourcentage** : le chômage passe de 8 % à 9 % → **+1 point**, ou **+12,5 %**. Les deux sont justes, ils ne disent pas la même chose.
- [ ] **TCAM** : $\text{TCAM} = \left(\dfrac{V_n}{V_0}\right)^{1/n} - 1$. **Ce n'est pas la moyenne arithmétique des taux annuels.**
- [ ] **Contribution à la croissance** : consommation à 54 % du PIB croissant de 2 % → $0{,}54 \times 2 = 1{,}08$ point.

📎 [Khan — Automatismes](https://fr.khanacademy.org/math/premieres-technologiques/xe0f38a7ca0048ef2:automatismes) · [Melchior](https://www.melchior.fr/) · [INSEE — Découvrir, apprendre, enseigner](https://www.insee.fr/fr/information/2021852)

### A7 — Indices (1 h 30)
- [ ] Indice base 100 : $I_t = 100 \times \dfrac{V_t}{V_0}$
- [ ] Passer d'un indice à un taux de variation, et l'inverse
- [ ] **Changement de base** (raccordement de séries)
- [ ] **Déflation** : passer de la valeur (euros courants) au volume (euros constants)

📎 **La référence, gratuite, écrite par les praticiens** : 📄 [INSEE — Introduction à la pratique des indices statistiques](https://www.insee.fr/fr/metadonnees/source/fichier/IPC_introduction_pratique_indices.pdf)
📎 Laspeyres / Paasche en profondeur : 📄 [INSEE — Le calcul des indices : l'agrégation](https://www.insee.fr/fr/statistiques/fichier/4186908/imet133-f.pdf)

> [!warning] La dichotomie nominal / réel
> C'est l'une des cinq erreurs les plus sanctionnées du cursus. Une variable « en valeur » intègre l'inflation, une variable « en volume » l'a retirée. Une croissance de 3 % en valeur avec 2 % d'inflation, c'est **1 % de croissance réelle**.

### A8 — Consolidation sur données réelles (1 h)
- [ ] Sur [INSEE](https://www.insee.fr/fr/statistiques) (base BDM), télécharge le PIB français en valeur et en volume sur 20 ans
- [ ] Calcule : taux annuels, TCAM, indice base 100 = 2010, déflateur implicite du PIB
- [ ] Vérifie contre les publications INSEE

---

## Sessions 5–8 (6 h) — MODULE B : fonctions

### B1 — Notion de fonction et lecture graphique (1 h 30)
- [ ] Domaine de définition, image, antécédent
- [ ] Lecture graphique : image, antécédent, signe, variations, extremum
- [ ] Résolution graphique de $f(x) = k$ et $f(x) = g(x)$

📎 [Khan — Les fonctions](https://fr.khanacademy.org/math/cycle-4-v2/xd933de08ca5f2cb4:les-fonctions) · 📄 [Exo7 — ch_fonctions](http://exo7.emath.fr/cours/ch_fonctions.pdf)

### B2 — Fonction affine et interprétation économique (1 h 30)
- [ ] $f(x) = ax + b$ : $a$ = pente, $b$ = ordonnée à l'origine
- [ ] Déterminer une fonction affine à partir de deux points
- [ ] **Les quatre traductions économiques à retenir définitivement** :

| Fonction | Formule | Ce qu'est la pente |
|---|---|---|
| Coût total | $CT(q) = CF + c_v q$ | Le coût variable unitaire |
| Demande | $Q_d = a - bP$ | Négative |
| Offre | $Q_s = c + dP$ | Positive |
| Consommation keynésienne | $C = cY + C_0$ | **La propension marginale à consommer** |

> [!tip] Le point clé
> Dans ces quatre fonctions, la pente est *la même idée* — l'effet d'une unité supplémentaire. **C'est le raisonnement marginal, avant même d'avoir vu une dérivée.** Comprends ça maintenant et la dérivée n'aura rien de mystérieux la semaine prochaine.

📎 [Citéco](https://www.citeco.fr/) · [Melchior](https://www.melchior.fr/) → « coûts de l'entreprise », « offre et demande »

### B3 — Fonctions quadratiques et rationnelles (1 h 30)
- [ ] Parabole : sommet, axe de symétrie, concavité, racines
- [ ] **Trouver le sommet = trouver l'optimum.** $\pi(q) = RT(q) - CT(q)$ est souvent une parabole
- [ ] Hyperbole : $CM(q) = \dfrac{CT(q)}{q}$ — le coût moyen
- [ ] Asymptotes, comportement quand $q \to \infty$ et $q \to 0$

📎 📄 [Exo7 fic00106 — Étude de fonctions](http://exo7.emath.fr/ficpdf/fic00106.pdf) · [WIMS](https://wims.math.cnrs.fr/wims/)

### B4 — Systèmes d'équations (1 h 30)
- [ ] Système 2×2 par substitution **et** par combinaison
- [ ] Interprétation graphique : intersection de deux droites
- [ ] **L'application qui compte** : équilibre de marché en résolvant $Q_d = Q_s$, puis $P^*$ et $Q^*$
- [ ] Notion de système 3×3 (pivot de Gauss) — survol suffisant

📎 📄 [Exo7 — ch_syslin](http://exo7.emath.fr/cours/ch_syslin.pdf) · 🎥 [playlist](https://www.youtube.com/playlist?list=PL024XGD7WCIFSxatDf77naZwvNPiPbAe4) · 📄 [fic00101](http://exo7.emath.fr/ficpdf/fic00101.pdf) · 📄 [fic00160](http://exo7.emath.fr/ficpdf/fic00160.pdf)

**Maîtrise S2** : résoudre $\{Q_d = 100 - 2P \; ; \; Q_s = 20 + 3P\}$, trouver $P^*$ et $Q^*$, tracer, et dire ce qui se passe si $Q_d = 120 - 2P$.

---

# 📅 SEMAINE 3 — Dérivation et logarithmes

> [!abstract] La semaine centrale du cycle
> **La dérivée est le langage de l'économie.** Chaque fois qu'un économiste dit « marginal », il dit « dérivée ».

## Sessions 1–6 (9 h) — MODULE C : dérivation

### C1 — Comprendre avant de calculer (1 h 30)
- [ ] Taux d'accroissement $\dfrac{f(x+h) - f(x)}{h}$, puis passage à la limite
- [ ] Interprétation géométrique : la dérivée est la **pente de la tangente**
- [ ] **Interprétation économique, à graver** : $f'(x)$ = l'effet sur $f$ d'une unité supplémentaire de $x$

| Notation | Signification |
|---|---|
| $CT'(q) = Cm(q)$ | Coût marginal |
| $RT'(q) = Rm(q)$ | Recette marginale |
| $U'(x) = Um(x)$ | Utilité marginale |
| $F'(L) = Pm_L$ | Productivité marginale du travail |

📎 [Khan — Dérivée d'une fonction](https://fr.khanacademy.org/math/be-5eme-secondaire4h2/xe8f0cb2c937e9fc1:derivee-d-une-fonction) · 📄 [Exo7 ch_derivee](http://exo7.emath.fr/cours/ch_derivee.pdf) · 🎥 [playlist](https://www.youtube.com/playlist?list=PLD702C0EC85AB2A5A) · 📄 [Maths et tiques — Dérivation](https://www.maths-et-tiques.fr/telech/19Deri2TM.pdf)

> [!warning] Ne saute pas cette session
> La différence entre un étudiant qui *calcule* des dérivées et un étudiant qui *comprend le marginal* se voit à chaque copie de microéconomie. Elle se joue dans ces 90 minutes.

### C2 — Les dérivées usuelles (1 h 30)

| $f(x)$ | $f'(x)$ |
|---|---|
| $k$ | $0$ |
| $x^n$ | $n x^{n-1}$ |
| $\frac{1}{x}$ | $-\frac{1}{x^2}$ |
| $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ |
| $\ln(x)$ | $\frac{1}{x}$ |
| $e^x$ | $e^x$ |

📎 📄 [Formulaire Exo7](http://exo7.emath.fr/cours/formules.pdf) · [WIMS → dérivées](https://wims.math.cnrs.fr/wims/) (données aléatoires : parfait pour enchaîner 50 dérivées)

### C3 — Les quatre règles (2 h)
- [ ] Somme : $(u+v)' = u' + v'$
- [ ] Produit : $(uv)' = u'v + uv'$
- [ ] Quotient : $\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}$
- [ ] **Composée** : $(u \circ v)'(x) = v'(x) \cdot u'(v(x))$ — la plus utilisée en économie, la moins maîtrisée

📎 [Khan — Composition de fonctions](https://fr.khanacademy.org/math/be-5eme-secondaire4h2/xe8f0cb2c937e9fc1:combinaison-et-composition-de-fonctions) · 📄 [**Exo7 fic00104 — ta fiche principale**](http://exo7.emath.fr/ficpdf/fic00104.pdf) · 📄 [fic00013](http://exo7.emath.fr/ficpdf/fic00013.pdf)

**Maîtrise** : **40 dérivées justes d'affilée** en 30 minutes. Ne quitte pas cette session avant.

### C4 — Variations et extremum (2 h)
- [ ] Signe de $f'$ → sens de variation de $f$
- [ ] **Tableau de variations complet**
- [ ] Condition du 1er ordre : $f'(x) = 0$
- [ ] Convexité ($f'' > 0$) / concavité ($f'' < 0$)
- [ ] **Condition du 2nd ordre** : $f'' < 0 \Rightarrow$ maximum ; $f'' > 0 \Rightarrow$ minimum

> [!tip] La mécanique complète de l'optimisation économique
> Maximiser le profit, minimiser le coût, maximiser l'utilité : **toujours la même procédure en trois temps** — dériver, annuler, vérifier le second ordre. Tu la répéteras cinquante fois en L1 et en L2.

### C5 — Applications économiques dirigées (2 h)
- [ ] $CT(q) = q^3 - 6q^2 + 15q + 20$. Calculer $Cm$, $CM$, $CVM$. Montrer que $Cm$ coupe $CM$ au minimum de $CM$
- [ ] Montrer que le profit est maximal quand $Cm = Rm$
- [ ] $Q_d(P) = 100 - 2P$ : calculer $\varepsilon = \dfrac{dQ}{dP}\cdot\dfrac{P}{Q}$ en $P = 20$ et interpréter
- [ ] $F(L) = 10\sqrt{L}$ : productivité marginale, montrer qu'elle est décroissante

📎 **La ressource idéale** : [Captain Economics — Lagrange partie 1](https://www.captaineconomics.fr/-optmisation-utilite-bien-etre-multiplicateur-lagrange) et [partie 2](https://www.captaineconomics.fr/-methode-lagrangien-economie-maximisation-minimisation-fonction). **Tu prends une semaine d'avance sur le [[Cycle 1 - Moteur economique|cycle 1]].**
📎 [Marginal Revolution University](https://mru.org/) · [MIT OCW 14.01](https://ocw.mit.edu/)

---

## Sessions 7–8 (3 h) — MODULE D : log et exponentielle

### D1 — Propriétés et calcul (1 h 30)
- [ ] $e^{a+b} = e^a e^b$, $(e^u)' = u' e^u$
- [ ] $\ln(ab) = \ln a + \ln b$, $\ln(a^n) = n \ln a$, $(\ln u)' = \dfrac{u'}{u}$
- [ ] Réciprocité : $\ln(e^x) = x$, $e^{\ln x} = x$
- [ ] Résoudre $a^x = b \Rightarrow x = \dfrac{\ln b}{\ln a}$

📎 📄 [Maths et tiques — Exponentielle](https://www.maths-et-tiques.fr/telech/19ExpoPM.pdf) · [Khan — exp et log](https://fr.khanacademy.org/math/be-6eme-secondaire4h2/x874e280f2deebfaf:liens-entre-l-exponentielle-et-le-logarithme) · 📄 [Exo7 fic00083](http://exo7.emath.fr/ficpdf/fic00083.pdf)

### D2 — Les trois applications économiques (1 h 30)
- [ ] **Temps de doublement** : $n = \dfrac{\ln 2}{\ln(1+t)}$, et la **règle de 70** : $n \approx \dfrac{70}{t\%}$. À 3,5 %/an, un PIB double en 20 ans.
- [ ] **Croissance continue** : $V(t) = V_0 e^{gt}$, donc $\ln V(t)$ est une droite de pente $g$. C'est pourquoi les économistes tracent en échelle logarithmique.
- [ ] **Log-linéarisation** : $\ln Y = \ln A + \alpha \ln K + \beta \ln L$ — la Cobb-Douglas multiplicative devient linéaire, donc estimable par régression. Tu retrouveras ça en économétrie en L3.

**Maîtrise S3** : dériver $x^2\ln x$, $\dfrac{e^{3x}}{1+x}$, $\ln(3x^2+1)$ — sans notes, en moins de 3 minutes.

---

# 📅 SEMAINE 4 — Dérivées partielles, suites, convergence

## Sessions 1–4 (6 h) — MODULE E : fonctions à deux variables

> [!abstract] L'objectif final du cycle 0
> Tout ce qui précède servait à arriver ici.

### E1 — Courbes de niveau (1 h 30)
- [ ] Notion de $f(x, y)$, représentation dans l'espace
- [ ] **Courbe de niveau** : l'ensemble des $(x,y)$ tels que $f(x,y) = k$

> [!tip] La révélation à retenir
> **La courbe de niveau *est* la courbe d'indifférence** en théorie du consommateur, et ***est* l'isoquante** en théorie du producteur. Un seul objet mathématique, deux noms économiques.
>
> Cette identification vaut à elle seule une dizaine d'heures sur l'année. Le graphe « deux biens + une contrainte linéaire » sert ensuite pour l'arbitrage consommation/loisir, le choix inter-temporel, le choix risque/rendement, et la combinaison de deux facteurs. **Dessine-le une seule fois, très proprement, et réutilise-le partout.**

📎 [Khan — Fonctions de plusieurs variables](https://fr.khanacademy.org/math/multivariable-calculus) (commence par les courbes de niveau, arrête-toi avant les intégrales multiples)

### E2 — Dérivées partielles (2 h)
- [ ] Principe : dériver par rapport à $x$ **en traitant $y$ comme une constante**
- [ ] Notations : $\dfrac{\partial f}{\partial x}$, $f'_x$, $f_x$
- [ ] Dérivées partielles secondes et croisées
- [ ] Le gradient

📎 📄 [**Exo7 fic00116 — la fiche clé du module**](http://exo7.emath.fr/ficpdf/fic00116.pdf) · [Khan — multivariable](https://fr.khanacademy.org/math/multivariable-calculus) · [WIMS](https://wims.math.cnrs.fr/wims/)

**Batterie obligatoire** — les deux dérivées partielles de :
$3x^2y$ · $x^2+y^2$ · $xy$ · $\frac{x}{y}$ · $\ln x + \ln y$ · $x^{0,5}y^{0,5}$ · $x^{0,3}y^{0,7}$ · $(x+y)^2$ · $e^{xy}$ · $x^\alpha y^\beta$

**Les dix, justes, en moins de 10 minutes.**

### E3 — Cobb-Douglas et TMS (1 h 30)
- [ ] $U(x,y) = x^\alpha y^\beta$ : calculer $\dfrac{\partial U}{\partial x}$ et $\dfrac{\partial U}{\partial y}$ **de tête**
- [ ] **Le TMS** : $TMS = \dfrac{\partial U/\partial x}{\partial U/\partial y}$ = valeur absolue de la pente de la courbe d'indifférence
- [ ] Cas $U = x^{0,5}y^{0,5}$ : montrer que $TMS = \dfrac{y}{x}$
- [ ] Interprétation : la quantité de $y$ qu'on abandonne pour une unité de $x$ de plus, à satisfaction constante

📎 [Captain Economics — Lagrange 1](https://www.captaineconomics.fr/-optmisation-utilite-bien-etre-multiplicateur-lagrange) et [2](https://www.captaineconomics.fr/-methode-lagrangien-economie-maximisation-minimisation-fonction) · 📄 [Notes L1 sciences éco — optimisation](https://leonard.perso.math.cnrs.fr/teaching/L1%20sceco-analyse%202-notes%20de%20cours.pdf)

> [!success] Tu viens de faire le premier tiers du cours de microéconomie de L1
> En semaine 5, quand ton enseignant écrira « à l'optimum, $TMS = \frac{p_1}{p_2}$ », tu comprendras d'où ça vient au lieu de le recopier.

### E4 — Différentielle et homogénéité (1 h)
- [ ] Différentielle totale : $df = \dfrac{\partial f}{\partial x}dx + \dfrac{\partial f}{\partial y}dy$
- [ ] Le long d'une courbe de niveau, $df = 0$, donc $\dfrac{dy}{dx} = -\dfrac{\partial f/\partial x}{\partial f/\partial y}$
- [ ] Fonction homogène de degré $k$ : $f(\lambda x, \lambda y) = \lambda^k f(x,y)$
- [ ] **Rendements d'échelle** : $\alpha + \beta$ dans une Cobb-Douglas → constants si $=1$, croissants si $>1$, décroissants si $<1$

---

## Session 5 (1 h 30) — MODULE F : suites
- [ ] Suite arithmétique : $u_n = u_0 + nr$
- [ ] Suite géométrique : $u_n = u_0 q^n$
- [ ] **Somme géométrique** : $S_n = u_0 \dfrac{1 - q^{n+1}}{1-q}$
- [ ] Limite si $|q| < 1$ : $S = \dfrac{u_0}{1-q}$

📎 📄 [Exo7 ch_suites](http://exo7.emath.fr/cours/ch_suites.pdf) · 🎥 [playlist](https://www.youtube.com/playlist?list=PL20E5F69BB88FEDEE) · 📄 [fic00092](http://exo7.emath.fr/ficpdf/fic00092.pdf) — **fais uniquement les calculs de sommes et limites simples**, ignore la convergence théorique.

> [!tip] Pourquoi 90 minutes suffisent, et pourquoi elles sont capitales
> La formule $\dfrac{1}{1-q}$ est **exactement** le multiplicateur keynésien $\dfrac{1}{1-c}$ que tu verras en semaine 8. Et **exactement** la formule d'actualisation d'une rente perpétuelle que tu verras en L2 en calcul actuariel.
>
> **Un seul objet mathématique, trois cours différents.** Repère-le maintenant et tu ne l'apprendras jamais deux fois.

## Session 6 (1 h 30) — MODULE G : méthode (UE 18C, coef 2, CC en P1)
- [ ] **Le rappel actif** : démarrer chaque session par 10 min de restitution sans notes
- [ ] **La fiche A4** : une UE = une page recto
- [ ] **La prise de notes en CM** : structure hiérarchique, abréviations, et repérage des « ça, c'est important » de l'enseignant — ce sont des annonces d'examen
- [ ] Finaliser le dossier de l'UE 18C

> [!warning] UE 18C n'est pas une formalité
> Coef 2 pour 1 crédit, évaluée en CC dès la **période 1**, dans le **socle transversal non compensable**. Rends ton dossier tôt et propre.

## Sessions 7–8 (3 h) — Test de sortie et bilan
- [ ] Faire le test ci-dessous
- [ ] Reconstruire ta fiche A4 « Maths L1 » **de mémoire**, puis comparer à celle écrite au fil des semaines. **Les écarts sont exactement tes fragilités.**

---

# ✅ Test de sortie — 45 min, sans notes

**1. Dérivation** (10 pts) — dériver $x^2\ln x$ · $\dfrac{e^{3x}}{1+x}$ · $(2x+1)^5$ · $\sqrt{x^2+1}$ · $\dfrac{x^3}{x-2}$

**2. Dérivées partielles** (5 pts) — $U(x,y) = x^{0,3}y^{0,7}$ : les deux dérivées partielles, puis le TMS simplifié

**3. Systèmes** (5 pts) — résoudre $\{Q_d = 100-2P \; ; \; Q_s = 20+3P\}$. Puis si $Q_s = 10+3P$. Commenter.

**4. Pourcentages** (10 pts)
- PIB de 2 500 à 2 580 Md€ : taux de croissance ?
- Puis +12 % puis −8 % : variation totale ? *(ce n'est pas +4 %)*
- PIB de 2 000 à 2 800 Md€ en 8 ans : TCAM ?
- Consommation à 54 % du PIB croissant de 1,8 % : contribution en points ?
- Chômage de 7,5 % à 8,1 % : en points, puis en pourcentage ?

**5. Optimisation** (5 pts) — $CT(q) = q^3-6q^2+15q+20$, $p = 15$. Quantité qui maximise le profit ? Vérifier le 2nd ordre.

**6. Log et suites** (5 pts)
- Années pour doubler à 3,5 %/an ? (formule exacte + approximation)
- $\lim (1 + 0{,}8 + 0{,}8^2 + \ldots)$ ? À quelle notion économique cette somme correspond-elle ?

## Barème de décision

| Score | Verdict |
|---|---|
| **32–40** | ✅ Passe au [[Cycle 1 - Moteur economique]] |
| **26–31** | ⚠️ Passe, **mais** garde 2 h/semaine de rattrapage maths jusqu'en S8 |
| **< 26** | 🛑 **Ne passe pas.** Refais S3 et S4 en ciblant tes erreurs. |

> [!danger] Le seul point du plan où je te demande de ne pas avancer
> Partout ailleurs, avancer imparfaitement vaut mieux que stagner. Ici, non : le coût d'un cycle 0 raté se paie sur **16 ECTS**.

---

# 🚫 Les 7 erreurs qui coûtent le plus de points

À relire avant **chaque** examen de la L1. Coût : 3 minutes. Rendement : 1 à 2 points.

1. **Additionner des taux de variation.** Les taux ne s'additionnent jamais ; les coefficients se multiplient.
2. **Confondre point de pourcentage et pourcentage.** De 8 % à 9 % : +1 point, ou +12,5 %.
3. **Prendre la moyenne arithmétique des taux annuels** au lieu du TCAM.
4. **Confondre valeur et volume.** Toute croissance annoncée doit être qualifiée.
5. **Oublier la composée.** $(\ln(3x^2))' \neq \frac{1}{3x^2}$ — il manque le $6x$.
6. **Oublier la condition du 2nd ordre.** $f'(x)=0$ donne un point critique, pas un maximum. C'est souvent barémé.
7. **Ne pas interpréter le résultat.** Un nombre sans phrase d'interprétation vaut la moitié des points. Termine par « ce qui signifie que… ».

---

# 📌 Récapitulatif

**Ce que tu sauras faire** : dériver toute fonction d'une variable · calculer des dérivées partielles et un TMS · trouver un optimum avec vérification du 2nd ordre · résoudre un équilibre de marché · manipuler taux, indices, TCAM et contributions · déflater une série · reconnaître une somme géométrique

**Les 3 identités à retenir absolument**
1. **La dérivée = le marginal.** Toute la microéconomie en découle.
2. **Courbe de niveau = courbe d'indifférence = isoquante.** Un objet, trois noms.
3. $\dfrac{1}{1-q}$ = **somme géométrique = multiplicateur keynésien = rente perpétuelle.** Une formule, trois cours.

**Les 2 livrables**
- [ ] 3 pages de rétro-ingénierie des annales
- [ ] Fiche A4 « Maths L1 » reconstituée de mémoire

**Ce qui démarre ici et ne s'arrête plus** : Anki 15 min/jour · Journal de conjoncture 30 min le dimanche · Une fiche « ABC de l'économie » par jour

→ Suite : [[Cycle 1 - Moteur economique]]
