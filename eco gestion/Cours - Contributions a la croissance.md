---
tags:
  - L1-eco-gestion
  - cycle-0
  - module-A
  - macroeconomie
  - cours
notion: Contributions à la croissance
prerequis: taux de variation, coefficients multiplicateurs
statut: à faire
---

# 📈 Cours — Les contributions à la croissance

**Module A6 du [[Cycle 0 - Fondations|cycle 0]] · ≈ 1 h de cours + 1 h d'exercices**
🏋️ [[Fiche exos - Modules A C E#Contributions à la croissance (21 à 25)|série A-II, items 21 à 25]] · 🏠 [[00 - Plan L1 Angers]]

---

## 🎯 Pourquoi c'est un des points les plus rentables de la L1

Cette notion apparaît dans **trois UE différentes** :

| UE | Sous quelle forme |
|---|---|
| **14C Statistiques** | Décomposition d'un agrégat, calcul de contributions |
| **11B Macroéconomie** | Analyse de l'équilibre emplois-ressources, moteurs de la croissance |
| **13A Problèmes économiques contemporains** | « Qu'est-ce qui tire la croissance française ? » en dissertation |

Et surtout : **c'est le langage dans lequel l'INSEE, l'OFCE et la Banque de France commentent la conjoncture.** Une phrase comme *« le commerce extérieur ampute la croissance de 0,3 point »* n'a aucun sens si tu ne maîtrises pas cet outil. Tu ne pourras ni lire une note de conjoncture, ni tenir ton [[00 - Plan L1 Angers#🎯 Les 6 livrables de l'année|journal de conjoncture]].

> [!tip] La question à laquelle cet outil répond
> Le PIB a augmenté de 1,2 %. **Grâce à quoi ?** La consommation ? L'investissement ? L'État ? Le commerce extérieur ?
>
> Les contributions permettent de **répartir** la croissance entre ses moteurs, et de dire lequel a poussé, lequel a freiné.

---

## 💡 D'où vient la formule

Tout part d'une **identité comptable** que tu retrouveras en macroéconomie :

$$\text{PIB} = C + I + G + (X-M)$$

Cette égalité est vraie **à chaque instant**. Donc si tout bouge entre l'année 0 et l'année 1 :

$$\Delta\text{PIB} = \Delta C + \Delta I + \Delta G + \Delta(X-M)$$

Divisons maintenant **les deux côtés par le PIB de départ** :

$$\underbrace{\frac{\Delta\text{PIB}}{\text{PIB}_0}}_{\text{taux de croissance}} = \underbrace{\frac{\Delta C}{\text{PIB}_0}}_{\text{contribution de } C} + \underbrace{\frac{\Delta I}{\text{PIB}_0}}_{\text{contribution de } I} + \underbrace{\frac{\Delta G}{\text{PIB}_0}}_{\text{contribution de } G} + \underbrace{\frac{\Delta(X-M)}{\text{PIB}_0}}_{\text{contribution du solde}}$$

> [!abstract] La définition, en une ligne
> $$\boxed{\text{Contribution d'un poste} = \frac{\text{variation absolue du poste}}{\text{PIB de l'année de départ}}}$$
>
> C'est tout. Le reste n'est qu'une réécriture.

**La propriété qui rend l'outil utile** : par construction, la **somme des contributions égale exactement le taux de croissance du PIB**. C'est cette additivité qui permet de « répartir » la croissance — et c'est aussi ta vérification gratuite.

---

## 🔀 Les deux formules

La formule ci-dessus peut se réécrire en faisant apparaître le taux de croissance du poste :

$$\frac{\Delta C}{\text{PIB}_0} = \underbrace{\frac{\Delta C}{C_0}}_{\text{taux de croissance de } C} \times \underbrace{\frac{C_0}{\text{PIB}_0}}_{\text{poids de } C}$$

D'où deux façons de calculer, **strictement équivalentes quand elles s'appliquent** :

| | Formule | Quand l'utiliser |
|---|---|---|
| **Formule 1** ⭐ | $\dfrac{\Delta\text{Poste}}{\text{PIB}_0}$ | **Toujours.** Elle ne rate jamais. |
| **Formule 2** | $\text{poids} \times \text{taux de croissance}$ | Quand l'énoncé donne un **taux** et que le poste est **positif** |

> [!danger] Pourquoi la formule 2 ne marche pas toujours
> Elle suppose qu'on puisse calculer un **taux de croissance** du poste, donc qu'on puisse diviser par $\text{Poste}_0$. Si le poste est **négatif** — comme un solde extérieur déficitaire — le « taux de croissance » n'a aucun sens.
>
> Un solde qui passe de $-56$ à $-70$ : est-ce $+25\%$ (il augmente en valeur absolue) ou $-25\%$ (il se dégrade) ? La question n'a pas de réponse. **On revient donc à la formule 1**, qui ne pose jamais ce problème.

---

## ⚠️ Le cas du solde extérieur

C'est **le** piège de l'exercice, et il tombe systématiquement.

$X-M$ n'est pas un poste comme les autres : c'est un **solde**, une différence entre deux flux. Trois conséquences.

**1. Il peut être négatif.** La France a un solde extérieur structurellement déficitaire depuis des années.

**2. On ne lui calcule jamais de taux de croissance.** Formule 1 obligatoire.

**3. Sa contribution peut être positive même s'il reste négatif.** Un déficit qui **se réduit** contribue **positivement** à la croissance, parce que la demande adressée à la production nationale augmente.

> [!tip] La bonne façon de le formuler en copie
> On ne dit pas « le solde extérieur a augmenté de tant de pour cent ». On dit :
> - *« Le commerce extérieur **contribue** pour $+0,4$ point à la croissance »* si le déficit se réduit
> - *« Le commerce extérieur **ampute** la croissance de $0,5$ point »* si le déficit se creuse
>
> C'est le vocabulaire exact des publications de l'INSEE. L'employer te distingue immédiatement.

**Variante à connaître** : on peut décomposer le solde en deux contributions séparées, celle des **exportations** (positive quand elles progressent) et celle des **importations** (négative quand elles progressent, car elles se soustraient). Leur somme redonne la contribution du solde.

---
---

# ✏️ L'exercice, entièrement déroulé

**PIB = 2 800 Md€**

| Poste | Montant | Évolution |
|---|---|---|
| Consommation $C$ | 1 512 | +1,2 % |
| Investissement $I$ | 644 | +2,8 % |
| Dépenses publiques $G$ | 700 | +0,4 % |
| Solde extérieur $X-M$ | −56 | passe à **−70** |

## Étape préalable — calculer les poids

$$\frac{1512}{2800} = 54\% \qquad \frac{644}{2800} = 23\% \qquad \frac{700}{2800} = 25\% \qquad \frac{-56}{2800} = -2\%$$

> [!success] Ta première vérification, gratuite
> $54 + 23 + 25 - 2 = \boxed{100\%}$ ✓
>
> **Les poids doivent toujours sommer à 100 %.** Si ce n'est pas le cas, tu as fait une erreur de lecture avant même de commencer. Fais ce contrôle systématiquement.

## Questions 21 à 23 — les postes positifs (formule 2)

**21. Consommation** — $0{,}54 \times 1{,}2 = \boxed{+0{,}648\ \text{point}}$
**22. Investissement** — $0{,}23 \times 2{,}8 = \boxed{+0{,}644\ \text{point}}$
**23. Dépenses publiques** — $0{,}25 \times 0{,}4 = \boxed{+0{,}100\ \text{point}}$

> [!warning] Attention à l'unité
> Une contribution s'exprime en **points de croissance**, pas en pourcentage. Écrire « la consommation contribue pour 0,648 % » est ambigu et sanctionné : cela laisse croire à un taux de croissance.
>
> C'est la même distinction points/pourcentage que pour le taux de chômage — voir [[Fiche exos - Modules A C E#Points vs pourcentage (17 à 20)|les items 17 à 20]].

## Question 24 — le solde extérieur (formule 1 obligatoire)

$$\frac{-70-(-56)}{2800} = \frac{-14}{2800} = -0{,}005 = \boxed{-0{,}50\ \text{point}}$$

Le déficit **se creuse** de 14 Md€ : le commerce extérieur **ampute** la croissance d'un demi-point.

## Question 25 — la croissance totale

$$0{,}648 + 0{,}644 + 0{,}100 - 0{,}500 = \boxed{+0{,}892\ \% \approx +0{,}89\ \%}$$

### La vérification par le calcul direct
On recalcule le PIB de l'année 1 poste par poste :

$$1512(1{,}012) + 644(1{,}028) + 700(1{,}004) - 70$$
$$= 1\,530{,}14 + 662{,}03 + 702{,}80 - 70 = 2\,824{,}98$$

$$\frac{2824{,}98}{2800} - 1 = +0{,}892\ \% \quad ✓$$

> [!success] Fais toujours cette vérification
> Elle prend une minute et confirme d'un coup les cinq réponses. Si les deux méthodes divergent, tu as une erreur — et tu la vois **avant** de rendre.

---

## 🔎 La lecture de second niveau — celle qui rapporte les points

Une fois les contributions calculées, on peut aller plus loin : **quelle part de la croissance chaque poste explique-t-il ?**

$$\text{Part dans la croissance} = \frac{\text{contribution du poste}}{\text{croissance totale}}$$

| Poste | Contribution | Part dans la croissance |
|---|---|---|
| $C$ | $+0{,}648$ | $\frac{0,648}{0,892} = \mathbf{72{,}6\ \%}$ |
| $I$ | $+0{,}644$ | $\mathbf{72{,}2\ \%}$ |
| $G$ | $+0{,}100$ | $\mathbf{11{,}2\ \%}$ |
| $X-M$ | $-0{,}500$ | $\mathbf{-56{,}1\ \%}$ |
| **Total** | $+0{,}892$ | **100 %** |

> [!tip] Ce qui surprend, et qu'il faut savoir expliquer
> La consommation et l'investissement expliquent **chacun plus de 70 %** de la croissance. Ensemble, cela fait 145 % — ce qui semble impossible.
>
> Ce n'est pas une erreur. **Quand une contribution est négative, les autres peuvent dépasser 100 %.** Ici, la demande intérieure a poussé à hauteur de 1,39 point, mais le commerce extérieur en a détruit 0,5 : il ne reste que 0,89 point de croissance effective.
>
> **La phrase de conclusion attendue en copie** : *« La croissance est intégralement portée par la demande intérieure — consommation et investissement à parts quasi égales — tandis que le commerce extérieur ampute l'activité d'un demi-point. »*

---
---

## 🚫 Les 4 pièges

> [!danger] 1. Confondre le poids et la contribution
> La consommation **pèse** 54 % du PIB mais **contribue** pour 0,648 point. Ce sont deux choses radicalement différentes. Le poids est une part, la contribution est un effet.

> [!danger] 2. Calculer un taux de croissance sur un solde négatif
> Interdit et dépourvu de sens. Pour tout solde — commerce extérieur, variation de stocks, solde public — **formule 1 uniquement**.

> [!danger] 3. Exprimer une contribution en pourcentage
> C'est en **points de croissance**. Réserve le « % » aux taux de croissance et aux parts.

> [!danger] 4. Oublier de vérifier que la somme reboucle
> $\sum$ contributions $=$ taux de croissance du PIB. C'est une **identité**, pas une approximation. Si ça ne tombe pas juste, il y a une erreur quelque part.

---

## 💡 Le résultat contre-intuitif à retenir

> [!abstract] Le poids compte autant que le taux
> Un poste qui pèse **60 %** et croît de **1 %** contribue pour $0{,}60$ point.
> Un poste qui pèse **10 %** et croît de **5 %** contribue pour $0{,}50$ point.
>
> **Le premier contribue davantage, alors qu'il croît cinq fois moins vite.**
>
> C'est pour cela que la **consommation** domine systématiquement l'analyse de la croissance française : même avec une progression modeste de 1 %, ses 54 % de poids en font le premier moteur. À l'inverse, l'investissement peut bondir de 5 % sans changer grand-chose au total.
>
> **En dissertation, ce raisonnement vaut de l'or** : il explique pourquoi une politique de soutien à la consommation a plus d'effet mécanique à court terme qu'une politique d'investissement, même plus ambitieuse en pourcentage.

---

## 📊 Les ordres de grandeur français

À connaître pour vérifier la plausibilité de tes résultats et pour tes dissertations. Ce sont des ordres de grandeur, à actualiser sur [INSEE](https://www.insee.fr/fr/statistiques).

| Poste | Poids approximatif dans le PIB |
|---|---|
| Consommation des ménages | ~53 – 54 % |
| Investissement (FBCF totale) | ~23 – 24 % |
| Dépenses publiques (consommation collective) | ~23 – 24 % |
| Solde extérieur | légèrement **négatif** |
| Variation de stocks | proche de 0, mais **volatile** |

> [!note] La variation de stocks
> Elle apparaît dans les décompositions réelles de l'INSEE : $\text{PIB} = C + I + G + \Delta\text{Stocks} + (X-M)$. Son poids est quasi nul, mais sa contribution peut être **importante et très instable** d'un trimestre à l'autre. C'est aussi un **solde** → formule 1.

---
---

## ✅ Exercices d'application

- [ ] **A.** PIB = 2 400 Md€. $C = 1\,320$ (+1,5 %) · $I = 552$ (−2 %) · $G = 576$ (+1 %) · $X-M = -48$ passe à $-24$.
Calcule les poids, vérifie qu'ils somment à 100 %, calcule les quatre contributions et la croissance totale. Vérifie par le calcul direct.

- [ ] **B.** La croissance du PIB s'établit à $+1{,}4\ \%$. La consommation contribue pour $+0{,}9$ pt, l'investissement pour $+0{,}3$ pt, les dépenses publiques pour $+0{,}4$ pt. Quelle est la contribution du commerce extérieur ?

- [ ] **C.** Une note de conjoncture indique : *« Le commerce extérieur ampute la croissance de 0,3 point, alors que les exportations progressent de 4 % »*. Comment est-ce possible ?

- [ ] **D.** Le poste A pèse 60 % du PIB et croît de 1 %. Le poste B pèse 10 % et croît de 5 %. Lequel contribue le plus à la croissance ? Commente.

- [ ] **E.** Contributions d'un trimestre : consommation $+0{,}7$ pt · investissement $+0{,}4$ pt · dépenses publiques $+0{,}1$ pt · variation de stocks $+0{,}3$ pt · commerce extérieur $-0{,}2$ pt. Quelle est la croissance du PIB ? Quelle part la demande intérieure explique-t-elle ?

> [!success]- Corrigé A
> **Poids** : $\frac{1320}{2400} = 55\%$ · $\frac{552}{2400} = 23\%$ · $\frac{576}{2400} = 24\%$ · $\frac{-48}{2400} = -2\%$
> Vérification : $55+23+24-2 = 100\%$ ✓
>
> | Poste | Calcul | Contribution |
> |---|---|---|
> | $C$ | $0{,}55\times1{,}5$ | $+0{,}825$ pt |
> | $I$ | $0{,}23\times(-2)$ | $-0{,}460$ pt |
> | $G$ | $0{,}24\times1$ | $+0{,}240$ pt |
> | $X-M$ | $\frac{-24-(-48)}{2400}$ | $+1{,}000$ pt |
>
> **Croissance totale** $= 0{,}825-0{,}460+0{,}240+1{,}000 = \boxed{+1{,}605\ \%}$
>
> **Vérification directe** : $1320(1{,}015)+552(0{,}98)+576(1{,}01)-24 = 1339{,}80+540{,}96+581{,}76-24 = 2\,438{,}52$
> $\frac{2438,52}{2400}-1 = +1{,}605\%$ ✓
>
> **Le commentaire attendu** : le moteur principal n'est pas la consommation mais **le redressement du commerce extérieur**, qui contribue à lui seul pour 1 point sur 1,6 — le déficit ayant été divisé par deux. L'investissement, en recul, freine l'activité de près d'un demi-point. C'est une croissance de nature très différente de celle de l'exercice précédent.

> [!success]- Corrigés B à E
> **B.** La somme des contributions égale le taux de croissance :
> $$1{,}4 - 0{,}9 - 0{,}3 - 0{,}4 = \boxed{-0{,}2\ \text{point}}$$
> Le commerce extérieur **ampute** la croissance de 0,2 point.
>
> **C.** Parce que la contribution du commerce extérieur est un **solde net**. Les exportations progressent bien de 4 %, mais les **importations ont progressé davantage** — en volume comme en valeur. Le déficit se creuse donc, et la demande satisfaite par la production étrangère augmente plus vite que celle adressée à la production nationale.
> **L'enseignement** : on ne peut jamais conclure sur le commerce extérieur à partir des seules exportations. Il faut **toujours** raisonner sur le solde.
>
> **D.** Poste A : $0{,}60\times1 = \boxed{0{,}60\ \text{pt}}$ · Poste B : $0{,}10\times5 = \boxed{0{,}50\ \text{pt}}$
> **A contribue davantage**, alors qu'il croît **cinq fois moins vite**.
> **Commentaire** : le poids pèse autant que le taux dans une contribution. C'est pourquoi la consommation domine l'analyse de la croissance française — ses 54 % de poids compensent largement une progression modeste. Un poste marginal peut bondir sans effet macroéconomique notable.
>
> **E.** Croissance $= 0{,}7+0{,}4+0{,}1+0{,}3-0{,}2 = \boxed{+1{,}3\ \%}$
> Demande intérieure (hors stocks) $= 0{,}7+0{,}4+0{,}1 = 1{,}2$ pt, soit $\frac{1,2}{1,3} = \boxed{92\ \%}$ de la croissance.
> En incluant les stocks, la demande intérieure totale porte $1{,}5$ pt, soit **115 %** de la croissance — le commerce extérieur en retranchant 15 %.
> **Formulation type INSEE** : *« La croissance du trimestre, à +1,3 %, est portée par la demande intérieure, tandis que le commerce extérieur ampute l'activité de 0,2 point. La variation de stocks y contribue pour 0,3 point. »*

---

## 🔗 Ce que ce chapitre débloque

| Où | Comment |
|---|---|
| [[Cycle 1 - Moteur economique\|UE 11B]] — macro | L'identité $\text{PIB} = C+I+G+(X-M)$ est le **cœur** du chapitre sur la mesure |
| [[Cycle 1 - Moteur economique\|UE 11B]] — multiplicateur | Comprendre quel poste tirer pour relancer l'activité |
| [[Cycle 3 - Gestion et debats\|UE 13A]] — dissertations | « Qu'est-ce qui tire la croissance française ? » se traite avec cet outil |
| [[Cycle 2 - Les chiffres\|UE 14C]] — statistiques | Décomposition d'un agrégat, même logique sur d'autres variables |
| Journal de conjoncture | Chaque note de l'INSEE s'appuie dessus |

> [!abstract] La phrase à retenir
> **Contribution = variation du poste ÷ PIB de départ.** Et pour un poste positif, cela revient à **poids × taux de croissance**.
> La somme des contributions **est** le taux de croissance — c'est une identité, donc ta vérification gratuite.

---

← [[Cours - Tableaux de signes et inequations]] · [[Cours - Trouver le signe, toutes les methodes]] · 🏋️ [[Fiche exos - Modules A C E]] · 🏠 [[00 - Plan L1 Angers]]
