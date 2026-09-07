---
tags:
  - L1-eco-gestion
  - anki
  - cycle-0
  - cycle-1
  - reference
nb_cartes: 168
statut: à créer
---

# 🃏 Anki — Formules et définitions, cycles 0 et 1

**168 cartes · prêtes à importer**
📥 Fichier d'import : `anki-formules-C0-C1.csv`
🏠 [[00 - Plan L1 Angers]] · [[Cycle 0 - Fondations]] · [[Cycle 1 - Moteur economique]]

> [!abstract] L'essentiel
> - Anki ne stocke que **définitions, formules, procédures et distinctions** — jamais un raisonnement.
> - Un CSV au format `Recto ; Verso ; Tags`, importé en note **Basique**, séparateur **point-virgule**, HTML autorisé.
> - **Importe tout, puis suspends** `cycle1 micro`, `cycle1 macro`, `cycle1 maths` : avant la rentrée, tu n'étudies que `cycle0`.
> - **15 minutes par jour, jamais plus.** Dépasser signifie que trop de cartes sont activées.
> - Formules en texte brut Unicode : rien à installer, ni MathJax ni LaTeX.
> - Si tu n'en crées que douze, ce sont **Les 12 cartes prioritaires** — elles portent tout le reste.

---

> [!danger] La règle qui rend Anki efficace
> **Jamais de raisonnement en carte.** Anki ne stocke que des **définitions, formules, procédures et distinctions**.
>
> Une carte « Comment maximiser le profit ? » est mauvaise : c'est un raisonnement, il s'entraîne par exercices. Une carte « Condition de maximisation du profit ? → Cm = Rm » est bonne : c'est un fait à restituer instantanément.
>
> Les raisonnements se travaillent dans [[Fiche exos - Modules A C E]], [[Exercices - Cycle 0]] et [[Exercices - Cycle 1]].

## 📥 Comment importer

1. Ouvre le CSV — il est au format `Recto ; Verso ; Tags`
2. Dans Anki : **Fichier → Importer**, choisis le CSV
3. Séparateur : **point-virgule**
4. Type de note : **Basique**
5. Coche **« Autoriser le HTML dans les champs »**
6. Mappe : champ 1 → Recto · champ 2 → Verso · champ 3 → Tags

Les cartes arrivent taguées `cycle0`/`cycle1` et par module, tu peux donc filtrer et étudier par bloc.

## 📊 Répartition

| Bloc | Cartes | Tag |
|---|---|---|
| Cycle 0 — Module A (calcul, %, indices) | **36** | `cycle0 moduleA` |
| Cycle 0 — Module C (dérivation, signe) | **21** | `cycle0 moduleC` |
| Cycle 0 — Module D (log/exp) | **12** | `cycle0 moduleD` |
| Cycle 0 — Module E (dérivées partielles) | **11** | `cycle0 moduleE` |
| Cycle 0 — Module F (suites) | **5** | `cycle0 moduleF` |
| Cycle 1 — Microéconomie | **41** | `cycle1 micro` |
| Cycle 1 — Macroéconomie | **32** | `cycle1 macro` |
| Cycle 1 — Mathématiques | **10** | `cycle1 maths` |
| **Total** | **168** | |

Chaque carte porte aussi le tag `formule`, ce qui te permet de la router vers ton sous-deck `Formules`.

> [!warning] N'active pas les 168 cartes d'un coup
> Tu croulerais sous 80 révisions par jour dès la première semaine, et tu abandonnerais.
>
> **Importe tout, puis suspends** les tags `cycle1 micro`, `cycle1 macro` et `cycle1 maths`. Tu les réactiveras quand tu attaqueras le [[Cycle 1 - Moteur economique|cycle 1]].
>
> Avant la rentrée, tu n'étudies que **`cycle0`** — 85 cartes, soit une quinzaine de minutes par jour une fois le régime établi.

> [!tip] Le rythme
> **15 minutes par jour, jamais plus.** Si tu dépasses, c'est que tu as activé trop de cartes d'un coup.

## 🔤 Sur l'affichage des formules

Les cartes sont écrites en **texte brut avec symboles Unicode** (∂, √, Σ, ε, λ, ×, ≤). Elles s'affichent correctement dans Anki **sans aucune configuration** — pas de MathJax à activer, pas de LaTeX à installer.

C'est un choix délibéré : une formule lisible partout vaut mieux qu'une formule élégante qui ne s'affiche pas sur ton téléphone.

---
---
## 🧮 CYCLE 0 — MODULE A · Calcul et pourcentages (26)

### Pourcentages et taux
| Recto                                                    | Verso                                                                                                    |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Taux de variation                                        | $t = \dfrac{V_1-V_0}{V_0}$                                                                               |
| Coefficient multiplicateur                               | $CM = 1+t$                                                                                               |
| Retrouver la valeur initiale connaissant $V_1$ et $t$    | $V_0 = \dfrac{V_1}{1+t}$                                                                                 |
| Variations successives — la règle                        | Les **coefficients se multiplient**. Les taux ne s'additionnent **jamais**. $CM_{tot} = CM_1\times CM_2$ |
| TCAM (taux de croissance annuel moyen)                   | $\left(\dfrac{V_n}{V_0}\right)^{1/n}-1$                                                                  |
| Le TCAM est-il la moyenne des taux annuels ?             | **Non.** C'est la moyenne **géométrique**, jamais l'arithmétique.                                        |
| Point de pourcentage vs pourcentage                      | De 8 % à 9 % : **+1 point** ou **+12,5 %**. Deux énoncés justes, deux sens différents.                   |
| Contribution à la croissance — formule universelle       | $\dfrac{\Delta\text{Poste}}{\text{PIB}_0}$                                                               |
| Contribution à la croissance — poste positif             | $\text{poids}\times\text{taux de croissance du poste}$                                                   |
| Pourquoi le solde extérieur exige la formule universelle | Poste **négatif** → un taux de croissance n'aurait aucun sens                                            |
| Propriété clé des contributions                          | Leur **somme égale exactement** le taux de croissance du PIB                                             |
| Unité d'une contribution                                 | En **points de croissance**, jamais en %                                                                 |

### Indices et déflation
| Recto | Verso |
|---|---|
| Indice base 100 | $I_t = 100\times\dfrac{V_t}{V_0}$ |
| Variation entre deux indices | $\dfrac{I_{\text{arrivée}}}{I_{\text{départ}}}-1$ — on **divise**, jamais on ne soustrait |
| Rebasage sur l'année $n$ | Multiplier toute la série par $\dfrac{100}{I_n}$ |
| Déflation — par les taux | $1+q = \dfrac{1+v}{1+p}$ |
| Déflation — par les niveaux | $\dfrac{\text{valeur courante}}{\text{indice de prix}/100}$ |
| Pouvoir d'achat | $\dfrac{1+t_{\text{salaire}}}{1+t_{\text{prix}}}-1$ |
| Les 3 synonymes de « avec inflation » | En **valeur** · euros **courants** · **nominal** |
| Les 3 synonymes de « sans inflation » | En **volume** · euros **constants** · **réel** |
| Indice de Laspeyres (prix) | $\dfrac{\sum p_tq_0}{\sum p_0q_0}\times100$ — quantités de **base** |
| Indice de Paasche (prix) | $\dfrac{\sum p_tq_t}{\sum p_0q_t}\times100$ — quantités **courantes** (**P** comme **P**résent) |
| Indice de Fisher | $\sqrt{L\times P}$ |
| Indice de valeur | $\dfrac{\sum p_tq_t}{\sum p_0q_0}\times100$ |
| Relation croisée | Valeur $= L_p\times P_q = P_p\times L_q$ — **jamais** $L_p\times L_q$ |
| Pourquoi $L_p > P_p$ | **Substitution** : Laspeyres fige les quantités anciennes, surpondère le bien devenu cher, surestime l'inflation |
| Déflateur du PIB | $100\times\dfrac{\text{PIB nominal}}{\text{PIB réel}}$ |

---
## 📉 CYCLE 0 — MODULE C · Dérivation (18)

### Dérivées usuelles
| Recto | Verso |
|---|---|
| Dérivée de $k$ (constante) | $0$ |
| Dérivée de $x^n$ | $nx^{n-1}$ |
| Dérivée de $\frac{1}{x}$ | $-\frac{1}{x^2}$ |
| Dérivée de $\sqrt x$ | $\frac{1}{2\sqrt x}$ |
| Dérivée de $\ln x$ | $\frac{1}{x}$ |
| Dérivée de $e^x$ | $e^x$ |

### Règles
| Recto | Verso |
|---|---|
| $(u+v)'$ | $u'+v'$ |
| $(uv)'$ | $u'v+uv'$ |
| $\left(\frac{u}{v}\right)'$ | $\dfrac{u'v-uv'}{v^2}$ |
| $(u\circ v)'$ — fonction composée | $v'(x)\times u'(v(x))$ |
| $(\ln u)'$ | $\dfrac{u'}{u}$ |
| $(e^u)'$ | $u'e^u$ |
| $(u^n)'$ | $nu'u^{n-1}$ |
| $(\sqrt u)'$ | $\dfrac{u'}{2\sqrt u}$ |

### Optimisation et signe
| Recto | Verso |
|---|---|
| Condition du 1er ordre | $f'(x^*)=0$ — donne un **point critique**, pas un extremum |
| Condition du 2nd ordre | $f''<0$ → **maximum** · $f''>0$ → **minimum** |
| Signe d'un facteur affine $ax+b$ | Racine en $-\frac{b}{a}$, signe de $a$ **après** |
| Signe d'un trinôme $\Delta>0$ | Signe de $a$ **à l'extérieur** des racines, signe de $-a$ **entre** |

---
## 📈 CYCLE 0 — MODULE D · Logarithme et exponentielle (8)

| Recto | Verso |
|---|---|
| $\ln(ab)$ | $\ln a+\ln b$ |
| $\ln(a^n)$ | $n\ln a$ |
| $e^{a+b}$ | $e^a\times e^b$ |
| Résoudre $a^x=b$ | $x = \dfrac{\ln b}{\ln a}$ |
| Temps de doublement à un taux $t$ | $n = \dfrac{\ln 2}{\ln(1+t)}$ |
| Règle de 70 | $n \approx \dfrac{70}{t\%}$ |
| Croissance continue au taux $g$ | $V(t)=V_0e^{gt}$, et $\ln V(t)$ est une droite de pente $g$ |
| Log-linéarisation d'une Cobb-Douglas | $\ln Y=\ln A+\alpha\ln K+\beta\ln L$ |
| Signe de $e^u$ | **Strictement positif, toujours** — on le supprime d'un tableau de signes |

---
## 🔀 CYCLE 0 — MODULE E · Dérivées partielles (8)

| Recto | Verso |
|---|---|
| Principe de la dérivée partielle | Dériver par rapport à $x$ en traitant $y$ **comme une constante** |
| Courbe de niveau — les 2 autres noms | La **courbe d'indifférence** (consommateur) et l'**isoquante** (producteur) |
| TMS | $\dfrac{\partial U/\partial x}{\partial U/\partial y}$ |
| TMS d'une Cobb-Douglas $x^\alpha y^\beta$ | $\dfrac{\alpha}{\beta}\times\dfrac{y}{x}$ |
| Différentielle totale | $df=\dfrac{\partial f}{\partial x}dx+\dfrac{\partial f}{\partial y}dy$ |
| Pente d'une courbe de niveau | $\dfrac{dy}{dx}=-\dfrac{\partial f/\partial x}{\partial f/\partial y}$ (car $df=0$) |
| Fonction homogène de degré $k$ | $f(\lambda x,\lambda y)=\lambda^k f(x,y)$ |
| Rendements d'échelle d'une Cobb-Douglas | $\alpha+\beta$ : $=1$ constants · $>1$ croissants · $<1$ décroissants |
| Théorème d'Euler | $x f_x + y f_y = k\,f$ pour $f$ homogène de degré $k$ |

---
## 🔢 CYCLE 0 — MODULE F · Suites (4)

| Recto                                       | Verso                                                                                    |
| ------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Suite arithmétique                          | $u_n=u_0+nr$                                                                             |
| Suite géométrique                           | $u_n=u_0q^n$                                                                             |
| Somme d'une suite géométrique finie         | $S_n=u_0\dfrac{1-q^{n+1}}{1-q}$                                                          |
| Limite de la somme géométrique si $\|q\|<1$ | $S=\dfrac{u_0}{1-q}$ — c'est **le multiplicateur keynésien** et la **rente perpétuelle** |

---
---
## 🛒 CYCLE 1 — MICROÉCONOMIE (34)

### Consommateur
| Recto                                  | Verso                                                                                          |
| -------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Contrainte budgétaire                  | $p_1x_1+p_2x_2\leq R$                                                                          |
| Pente de la droite de budget           | $-\dfrac{p_1}{p_2}$                                                                            |
| Lagrangien du consommateur             | $\mathcal{L}=U(x,y)+\lambda(R-p_1x-p_2y)$                                                      |
| Condition d'optimalité du consommateur | $TMS=\dfrac{p_1}{p_2}$                                                                         |
| Autre écriture de l'optimum            | $\dfrac{Um_1}{p_1}=\dfrac{Um_2}{p_2}$ — utilités marginales pondérées égalisées                |
| Interprétation de $\lambda$            | L'**utilité marginale du revenu**                                                              |
| Demande marshallienne Cobb-Douglas     | $x^*=\dfrac{\alpha}{\alpha+\beta}\times\dfrac{R}{p_1}$                                         |
| Propriété de la Cobb-Douglas           | Les **parts de dépense sont constantes** et égales aux exposants                               |
| Utilité ordinale — conséquence         | Une transformation **monotone croissante** donne les **mêmes préférences**, donc le même TMS   |
| Substituts parfaits                    | $TMS$ **constant**, courbes d'indifférence = droites, solution **en coin**                     |
| Compléments parfaits                   | Courbes en **L**, TMS non défini au coude, optimum toujours au coude                           |
| Décomposition de Slutsky               | Effet total = **effet de substitution** + **effet de revenu**                                  |
| Bien normal                            | $\dfrac{\partial x}{\partial R}>0$                                                             |
| Bien inférieur                         | $\dfrac{\partial x}{\partial R}<0$                                                             |
| Bien de Giffen                         | Effet de revenu **positif dominant** l'effet de substitution → demande croissante avec le prix |

### Élasticités
| Recto | Verso |
|---|---|
| Élasticité-prix de la demande | $\varepsilon=\dfrac{dQ}{dP}\times\dfrac{P}{Q}$ |
| Demande élastique / inélastique | $\|\varepsilon\|>1$ élastique · $\|\varepsilon\|<1$ inélastique |
| Élasticité et recette totale | Si $\|\varepsilon\|<1$, une hausse de prix **augmente** la recette |
| Recette maximale | Là où $\varepsilon=-1$ (élasticité unitaire) |
| Élasticité d'une demande $Q=aP^{-b}$ | $-b$, **constante** — l'exposant **est** l'élasticité |
| Élasticité-revenu | $\dfrac{\Delta Q/Q}{\Delta R/R}$ · $>0$ bien normal · $<0$ bien inférieur |
| Élasticité croisée | $>0$ **substituts** · $<0$ **compléments** |

### Producteur
| Recto | Verso |
|---|---|
| Coût moyen | $CM=\dfrac{CT}{q}$ |
| Coût variable moyen | $CVM=\dfrac{CV}{q}$ |
| Coût marginal | $Cm=CT'(q)$ |
| Relation $Cm$ et $CM$ | $Cm$ coupe $CM$ **en son minimum** |
| Productivité marginale du travail | $Pm_L=F'(L)$ |
| TMST (taux marginal de substitution technique) | $\dfrac{Pm_L}{Pm_K}$ |
| Condition de minimisation du coût | $\dfrac{Pm_L}{w}=\dfrac{Pm_K}{r}$ |
| Condition de maximisation du profit | $Cm=Rm$ |
| Maximisation du profit en concurrence pure et parfaite | $Cm=P$ |
| Courbe d'offre individuelle | Partie **croissante** du $Cm$ située **au-dessus du $CVM$** |
| Seuil de fermeture | Minimum du $CVM$ |
| Seuil de rentabilité | Minimum du $CM$ |

### Marché
| Recto | Verso |
|---|---|
| Surplus du consommateur | Aire **sous** la courbe de demande et **au-dessus** du prix |
| Surplus du producteur | Aire **au-dessus** de la courbe d'offre et **sous** le prix |
| Qui supporte une taxe unitaire ? | Celui dont l'**élasticité est la plus faible** |
| Recette marginale du monopole | $Rm=P\left(1+\dfrac{1}{\varepsilon}\right)$, et toujours $Rm<P$ |
| Indice de Lerner | $\dfrac{P-Cm}{P}$ |

---
## 🌍 CYCLE 1 — MACROÉCONOMIE (26)

### Mesure
| Recto | Verso |
|---|---|
| PIB — les 3 approches | $\sum VA = C+I+G+(X-M) = \sum\text{revenus}$ |
| Pourquoi les 3 approches sont égales | **Tout emploi a une ressource** (identité comptable) |
| Valeur ajoutée | Production − consommations intermédiaires |
| PIB réel | $\dfrac{\text{PIB nominal}}{\text{déflateur}/100}$ |
| Équilibre emplois-ressources | $\text{PIB}+M = C+I+G+X$ |

### Consommation, investissement, multiplicateur
| Recto | Verso |
|---|---|
| Fonction de consommation keynésienne | $C=cY+C_0$ |
| PmC (propension marginale à consommer) | $c$ — la **pente** de la fonction de consommation |
| PMC (propension moyenne à consommer) | $\dfrac{C}{Y}$ |
| Fonction d'épargne | $S=(1-c)Y-C_0$ |
| Multiplicateur keynésien simple | $k=\dfrac{1}{1-c}$ |
| Multiplicateur avec fiscalité et importations | $k=\dfrac{1}{1-c(1-t)+m}$ |
| Effet d'une relance | $\Delta Y=k\times\Delta G$ |
| Théorème de Haavelmo | Le multiplicateur du **budget équilibré** vaut **1** |
| Stabilisateur automatique | L'impôt proportionnel **réduit** le multiplicateur, donc amortit les chocs |
| Paradoxe de l'épargne | Une hausse générale de l'épargne réduit la demande, donc le revenu, donc l'épargne totale |

### Travail
| Recto | Verso |
|---|---|
| Taux de chômage | $\dfrac{\text{chômeurs}}{\text{population active}}$ — jamais sur la population totale |
| Taux d'activité | $\dfrac{\text{population active}}{\text{population en âge de travailler}}$ |
| Taux d'emploi | $\dfrac{\text{actifs occupés}}{\text{population en âge de travailler}}$ |
| Chômage frictionnel | Délais normaux d'appariement — incompressible |
| Chômage structurel | Inadéquation durable qualifications / emplois offerts |
| Chômage classique | Salaire réel trop élevé, rigidités |
| Chômage keynésien | Insuffisance de la **demande effective** |

### Monnaie
| Recto | Verso |
|---|---|
| Équation quantitative de la monnaie | $MV=PY$ |
| Multiplicateur de crédit (sans fuite) | $\dfrac{1}{r}$ où $r$ = taux de réserves obligatoires |
| Création monétaire — le principe | **« Les crédits font les dépôts »** — la banque commerciale crée la monnaie *ex nihilo* |
| Taux d'inflation via l'IPC | $\dfrac{IPC_t}{IPC_{t-1}}-1$ |

### IS-LM
| Recto | Verso |
|---|---|
| Courbe IS | Équilibre du **marché des biens**, pente **négative** |
| Courbe LM | Équilibre du **marché de la monnaie**, pente **positive** |
| Ce qui déplace IS | $G$, $T$, $C_0$, $I_0$ |
| Ce qui déplace LM | $M$, $P$ |
| Effet d'éviction | La relance élève le taux d'intérêt, ce qui décourage l'investissement privé |
| Trappe à liquidité | LM **horizontale** → politique monétaire inefficace, politique budgétaire pleinement efficace |

---
## 📐 CYCLE 1 — MATHÉMATIQUES (10)

| Recto | Verso |
|---|---|
| Lagrangien général | $\mathcal{L}=f(x,y)+\lambda\big(c-g(x,y)\big)$ |
| Conditions du 1er ordre du Lagrangien | $\dfrac{\partial\mathcal{L}}{\partial x}=\dfrac{\partial\mathcal{L}}{\partial y}=\dfrac{\partial\mathcal{L}}{\partial\lambda}=0$ |
| Interprétation économique de $\lambda$ | La **valeur marginale du relâchement de la contrainte** |
| Point critique à 2 variables | $\dfrac{\partial f}{\partial x}=\dfrac{\partial f}{\partial y}=0$ |
| Conditions du 2nd ordre à 2 variables | Hessienne : $\det>0$ et $f_{xx}>0$ → **minimum** · $\det>0$ et $f_{xx}<0$ → **maximum** |
| Point selle | $\det$ de la hessienne $<0$ |
| Surplus du consommateur par intégration | $\displaystyle\int_0^{Q^*}P_d(q)\,dq - P^*Q^*$ |
| Résolution 2×2 par Cramer | $x=\dfrac{\begin{vmatrix}c_1&b_1\\c_2&b_2\end{vmatrix}}{\det}$ |
| Signe de $u^2$, $\sqrt u$ | $\geq 0$ toujours — ne change **jamais** le signe d'un produit |
| Signe de $\ln u$ | $<0$ si $u<1$ · $=0$ si $u=1$ · $>0$ si $u>1$ |

---
---

## 🎯 Les 12 cartes prioritaires

Si tu ne crées que douze cartes avant la rentrée, ce sont celles-là. Elles portent tout le reste.

1. Taux de variation et coefficient multiplicateur
2. **Les taux ne s'additionnent jamais** — les coefficients se multiplient
3. TCAM
4. Contribution à la croissance = poids × taux
5. Déflation : $1+q=\frac{1+v}{1+p}$
6. Les 6 dérivées usuelles
7. **$(u\circ v)' = v'\times u'(v)$** — la composée
8. Conditions du 1er et du 2nd ordre
9. Dérivée partielle : traiter l'autre variable comme constante
10. TMS d'une Cobb-Douglas
11. **$\frac{1}{1-q}$** = somme géométrique = multiplicateur keynésien
12. Élasticité-prix

---

## ✅ Contrôle

Réponds sans rouvrir la page, puis vérifie au lien.

1. Deux hausses successives : qu'est-ce qui se multiplie, qu'est-ce qui ne s'additionne jamais ? → [[#Pourcentages et taux]]
2. Laspeyres ou Paasche : lequel fige les quantités de l'année de base ? → [[#Indices et déflation]]
3. Le produit, le quotient et la composée : les trois règles de dérivation. → [[#Règles]]
4. Les conditions du 1er et du 2nd ordre. → [[#Optimisation et signe]]
5. Le TMS d'une Cobb-Douglas, et ce que vaut $\alpha+\beta$. → [[#🔀 CYCLE 0 — MODULE E · Dérivées partielles (8)]]
6. La condition d'optimalité du consommateur, dans ses deux écritures. → [[#Consommateur]]
7. Le multiplicateur keynésien simple, puis avec fiscalité et importations. → [[#Consommation, investissement, multiplicateur]]
8. Ce qui déplace IS, ce qui déplace LM. → [[#IS-LM]]

---

> [!abstract] Le rappel
> Anki installe les **automatismes**, pas la compréhension. Il te permet de ne plus perdre 30 secondes à retrouver $(uv)'$ en examen. La compréhension, elle, se construit dans les exercices — [[Fiche exos - Modules A C E]] et [[Exercices - Cycle 1]].
>
> **15 minutes par jour. Jamais plus.**

> [!question] À vérifier
> - Trois comptages différents pour le même deck : le frontmatter et le tableau de Répartition annoncent **168** cartes (36 + 21 + 12 + 11 + 5 + 41 + 32 + 10), les titres de section en annoncent **134** (26 + 18 + 8 + 8 + 4 + 34 + 26 + 10), et les tableaux de cartes en alignent **148** lignes.
> - Le callout d'activation annonce **85** cartes pour `cycle0` (le total de la Répartition), les cinq modules du cycle 0 en alignent **67**.
> - [[00 - Plan L1 Angers]] prévoit **~80** cartes au sous-deck `Formules` et ~380 en tout, alors qu'ici les **168** cartes portent toutes le tag `formule` et iraient donc dans ce seul sous-deck.

← [[Cycle 0 - Fondations]] · [[Cycle 1 - Moteur economique]] · 🏠 [[00 - Plan L1 Angers]]
