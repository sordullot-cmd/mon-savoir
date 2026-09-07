---
tags:
  - L1-eco-gestion
  - cycle-0
  - module-A
  - statistiques
  - cours
notion: Indices, déflation, Laspeyres et Paasche
prerequis: taux de variation, coefficients multiplicateurs
statut: à faire
---

# 📊 Cours — Indices et déflation

**Module A7 du [[Cycle 0 - Fondations|cycle 0]] · ≈ 1 h 30 de cours + 1 h 30 d'exercices**
🏋️ [[Fiche exos - Modules A C E#SÉRIE A-III — Indices et déflation|série A-III]] · 🏠 [[00 - Plan L1 Angers]]

---

## 🎯 Pourquoi ce chapitre revient partout

| UE | Sous quelle forme |
|---|---|
| **14C Statistiques** | Un chapitre entier, avec Laspeyres et Paasche au programme |
| **11B Macroéconomie** | PIB en volume, déflateur, mesure de l'inflation |
| **13A Problèmes économiques** | Pouvoir d'achat, inflation, dissertations |
| **L2 – 24A/24C** | Séries chronologiques, comparaisons temporelles |

Et surtout : **c'est le format dans lequel l'INSEE publie presque tout.** Indice des prix, indice de production industrielle, indice du coût de la construction, PIB en volume. Sans ce chapitre, tu ne peux pas lire une seule série statistique française.

> [!tip] La question à laquelle tout ce chapitre répond
> Une grandeur a augmenté de 15 % en euros. **Est-ce que je peux en acheter plus ?**
>
> Réponse : ça dépend des prix. Tout le chapitre sert à séparer ce qui relève de la **quantité** et ce qui relève du **prix**.

---
---
# PARTIE 1 — L'indice simple

## 💡 L'idée : ramener à une base commune

Comparer 2 250 à 1 800, c'est faisable. Comparer l'évolution du PIB français à celle des ventes d'une PME, c'est impossible — les ordres de grandeur n'ont rien à voir.

**Un indice résout ça** en ramenant tout à une base commune, en général 100 :

$$\boxed{I_t = 100 \times \frac{V_t}{V_0}}$$

où $V_0$ est la valeur de l'**année de base**.

### La propriété qui fait tout l'intérêt
Un indice se lit **directement comme une variation** depuis la base :

| Indice | Lecture immédiate |
|---|---|
| $137$ | $+37\ \%$ depuis la base |
| $89$ | $-11\ \%$ depuis la base |
| $100$ | c'est l'année de base |
| $200$ | la grandeur a **doublé** |

C'est tout. **Un indice n'est rien d'autre qu'un taux de variation déguisé**, exprimé sur une échelle où l'origine vaut 100 au lieu de 0.

### Passer d'un indice à un taux, et inversement
$$t = \frac{I_t}{100} - 1 \qquad\qquad I_t = 100\,(1+t)$$

---

## 🚨 La règle d'or : on ne soustrait JAMAIS deux indices

> [!danger] L'erreur numéro un du chapitre
> Une série a un indice de **104** en 2020 et de **126** en 2024. La variation **n'est pas** $+22\ \%$.
>
> $$\frac{126}{104} - 1 = \boxed{+21{,}15\ \%}$$

### Pourquoi
Un indice mesure un rapport à **l'année de base**, pas à l'année précédente. Soustraire deux indices reviendrait à comparer deux écarts à une même référence, ce qui n'est pas la variation de l'un à l'autre.

**La seule exception** : si l'indice de départ vaut **exactement 100**, alors la différence donne bien le taux. C'est précisément parce que l'année de base vaut 100 qu'un indice de 137 se lit « +37 % » — mais uniquement **par rapport à la base**.

> [!tip] Le réflexe à installer
> Entre deux indices, on **divise**, jamais on ne soustrait.
> $$t = \frac{I_{\text{arrivée}}}{I_{\text{départ}}} - 1$$
> Le fait que les indices soient sur une échelle de 100 ne change rien : ce sont des rapports, et les rapports se composent par multiplication. **C'est la même logique que les variations successives** du [[Cours - Contributions a la croissance|module A6]].

---

## 🔄 Le changement de base (rebasage)

L'INSEE change régulièrement l'année de base de ses séries. Tu dois savoir rebaser toi-même.

### La règle
Pour rebaser une série sur l'année $n$ :
$$\boxed{I_t^{\text{nouvelle base}} = I_t^{\text{ancienne base}} \times \frac{100}{I_n^{\text{ancienne base}}}}$$

Autrement dit : **on multiplie toute la série par $\frac{100}{\text{indice de la nouvelle année de base}}$.**

### Pourquoi ça marche
Ce n'est pas une recette magique, ça se démontre en deux lignes :
$$I_t^{\text{new}} = 100\times\frac{V_t}{V_n} = 100\times\frac{V_t/V_0}{V_n/V_0} = 100\times\frac{I_t^{\text{old}}}{I_n^{\text{old}}}$$

Les $V_0$ se simplifient. **Le rebasage ne change aucune information** : il déplace seulement le point de référence.

### Exemple — rebaser en 2019
Série base 100 en 2015 : $2015 = 100$ · $2019 = 118$ · $2023 = 140$
Coefficient : $\frac{100}{118}$

| Année | Ancienne base (2015) | Nouvelle base (2019)                          |
| ----- | -------------------- | --------------------------------------------- |
| 2015  | 100                  | $100\times\frac{100}{118} = \mathbf{84{,}7}$  |
| 2019  | 118                  | $\mathbf{100}$                                |
| 2023  | 140                  | $140\times\frac{100}{118} = \mathbf{118{,}6}$ |

> [!success] La vérification en trois secondes
> La variation entre deux années doit être **identique** dans les deux bases.
> Ancienne : $\frac{140}{118}-1 = +18{,}6\ \%$ · Nouvelle : $\frac{118,6}{100}-1 = +18{,}6\ \%$ ✓
>
> Si les deux ne coïncident pas, tu t'es trompé de sens dans le coefficient.

### Le raccordement de séries
Quand l'INSEE change de base, il publie souvent les deux séries sur une **année de chevauchement**. On calcule alors un **coefficient de raccordement** = rapport des deux indices sur cette année commune, et on l'applique à toute l'ancienne série pour la prolonger. C'est exactement le même calcul que le rebasage.

---
---
# PARTIE 2 — Valeur, volume, déflation

C'est le cœur économique du chapitre.

## 💡 La décomposition fondamentale

$$\text{Valeur} = \text{Prix} \times \text{Quantité}$$

Une dépense de 552 € peut résulter d'un achat plus important **ou** simplement d'un prix plus élevé. Toute la question est de séparer les deux.

### En taux de variation
Les trois grandeurs étant multiplicatives, leurs coefficients multiplicateurs se multiplient :

$$\boxed{(1+v) = (1+p)\times(1+q)}$$

où $v$ = taux en **valeur**, $p$ = taux des **prix**, $q$ = taux en **volume**.

D'où la formule de la **déflation** :
$$\boxed{1+q = \frac{1+v}{1+p} \qquad\text{soit}\qquad q = \frac{1+v}{1+p}-1}$$

> [!tip] Tu connais déjà ce mécanisme
> C'est **exactement** la logique des variations successives : les taux ne s'additionnent pas, les coefficients se multiplient. Ici on fait l'opération inverse — on **divise** un coefficient par un autre pour retirer un effet.
>
> **Déflater, c'est diviser.** Jamais soustraire.

## 📖 Le vocabulaire — trois mots pour la même chose

| Famille « avec l'inflation » | Famille « sans l'inflation » |
| ---------------------------- | ---------------------------- |
| En **valeur**                | En **volume**                |
| En euros **courants**        | En euros **constants**       |
| **Nominal**                  | **Réel**                     |

> [!warning] C'est l'une des cinq dichotomies les plus sanctionnées du cursus
> Toute croissance annoncée doit être **qualifiée**. « Le chiffre d'affaires a progressé de 5 % » ne veut rien dire tant qu'on n'a pas précisé *en valeur* ou *en volume*.
>
> Une croissance de 3 % en valeur avec 2 % d'inflation, c'est **1 % de croissance réelle** — et une entreprise qui vend un peu plus. Une croissance de 3 % en valeur avec 4 % d'inflation, c'est une **baisse réelle** — et une entreprise qui vend moins.

## 🧮 Les deux façons de déflater

### Méthode 1 — Par les taux
$$q = \frac{1+v}{1+p}-1$$
À utiliser quand l'énoncé donne des **pourcentages**.

### Méthode 2 — Par les niveaux
$$\text{Valeur en euros constants} = \frac{\text{Valeur en euros courants}}{\text{indice de prix}/100}$$
À utiliser quand l'énoncé donne des **montants** et un **indice**.

Les deux donnent le même résultat. Exemple de l'item 8 :

|          | Méthode 1               | Méthode 2                                                 |
| -------- | ----------------------- | --------------------------------------------------------- |
| Données  | $v = +15\%$, $p = +9\%$ | 480 → 552 €, IPC 100 → 109                                |
| Calcul   | $\frac{1,15}{1,09}-1$   | $\frac{552}{1,09} = 506{,}42$ puis $\frac{506,42}{480}-1$ |
| Résultat | $+5{,}50\ \%$           | $+5{,}50\ \%$ ✓                                           |

## ⚠️ L'approximation $q \approx v - p$

Pour de **petits** taux, la division est presque équivalente à la soustraction.

| $v$ | $p$ | Approximation $v-p$ | Valeur exacte | Écart |
|---|---|---|---|---|
| $4{,}8\ \%$ | $2{,}1\ \%$ | $2{,}70\ \%$ | $2{,}64\ \%$ | $0{,}06$ pt |
| $12\ \%$ | $8\ \%$ | $4{,}00\ \%$ | $3{,}70\ \%$ | $0{,}30$ pt |
| $50\ \%$ | $30\ \%$ | $20{,}00\ \%$ | $15{,}38\ \%$ | **$4{,}62$ pt** |

> [!danger] La règle en examen
> **Calcule toujours la valeur exacte.** L'approximation ne sert qu'à vérifier l'ordre de grandeur de ton résultat. Elle devient fausse dès que les taux dépassent quelques pour cent — et c'est justement le cas en période d'inflation forte, c'est-à-dire quand la question se pose vraiment.

## 💰 Le pouvoir d'achat

$$\text{Pouvoir d'achat} = \frac{\text{Revenu}}{\text{Prix}} \qquad\Longrightarrow\qquad \boxed{t_{\text{PA}} = \frac{1+t_{\text{salaire}}}{1+t_{\text{prix}}}-1}$$

C'est la déflation appliquée au revenu. Deux cas à savoir commenter :

| Situation | Calcul | Lecture |
|---|---|---|
| Salaire $+3{,}2\%$, IPC $+1{,}8\%$ | $\frac{1,032}{1,018}-1 = +1{,}38\%$ | Le pouvoir d'achat **augmente**, mais **bien moins** que le salaire nominal |
| Salaire $+1{,}5\%$, IPC $+2{,}7\%$ | $\frac{1,015}{1,027}-1 = -1{,}17\%$ | Le salaire nominal monte et **le pouvoir d'achat baisse** |

> [!tip] La phrase qui rapporte des points en dissertation
> Le second cas explique un phénomène politiquement central : **un salarié peut voir sa fiche de paie augmenter tout en s'appauvrissant**. Cette dissociation entre perception nominale et réalité réelle est au cœur des débats sur l'inflation.

## 🧾 Le déflateur du PIB

$$\text{Déflateur} = 100\times\frac{\text{PIB nominal}}{\text{PIB réel}}$$

C'est un **indice de prix implicite** : on ne le mesure pas directement, on le déduit du rapport entre les deux mesures du PIB.

**Différence avec l'IPC** : le déflateur couvre **toute la production nationale** (y compris investissement, dépenses publiques, exportations) et pondère par les quantités **courantes**. L'IPC ne couvre que la **consommation des ménages** et pondère par les quantités d'une année de base. Les deux ne donnent donc jamais exactement le même chiffre d'inflation.

---
---
# PARTIE 3 — Les indices synthétiques

## 💡 Le problème à résoudre

Jusqu'ici, un seul bien. Mais un « panier » en contient des centaines, et **les prix ET les quantités changent en même temps**.

Comment isoler l'**effet prix** seul ? Il faut figer les quantités. **Mais lesquelles ?**
- Celles de l'**année de base** ? → **Laspeyres**
- Celles de l'**année courante** ? → **Paasche**

Il n'y a pas de réponse objectivement supérieure. C'est un choix, et chacun a un biais.

---

## 📐 Laspeyres — les quantités du passé

$$\boxed{L_p = \frac{\sum p_t\,q_0}{\sum p_0\,q_0}\times 100}$$

> **La question qu'il pose** : *« Combien coûterait **aujourd'hui** le panier d'**hier** ? »*

On garde les quantités anciennes et on ne fait varier que les prix.

## 📐 Paasche — les quantités du présent

$$\boxed{P_p = \frac{\sum p_t\,q_t}{\sum p_0\,q_t}\times 100}$$

> **La question qu'il pose** : *« Combien aurait coûté **hier** le panier d'**aujourd'hui** ? »*

> [!tip] Le mnémonique
> **P**aasche = **P**résent → quantités de la période **courante**.
> Par élimination, Laspeyres prend celles du passé.
>
> Autre repère utile : dans les deux formules, **les prix bougent toujours** (c'est un indice de prix). Ce sont les quantités qui distinguent les deux.

## 📐 Fisher — le compromis

$$\boxed{F_p = \sqrt{L_p \times P_p}}$$

Moyenne **géométrique** des deux. Pourquoi géométrique et pas arithmétique ? Parce que les indices sont des rapports, et que la moyenne géométrique est la moyenne naturelle des rapports — la même logique que le TCAM.

---

## 🔬 Pourquoi $L_p > P_p$ presque toujours

C'est le résultat le plus important de cette partie, et il faut savoir l'expliquer, pas seulement le constater.

**Le mécanisme.** Quand le prix d'un bien augmente fortement, les consommateurs s'en détournent au profit de substituts moins chers. Les quantités consommées **se déforment** en réaction aux prix.

- **Laspeyres** fige les quantités **anciennes** : il continue de donner un poids important au bien devenu cher, alors qu'on en achète moins. → **Il surestime l'inflation.**
- **Paasche** utilise les quantités **actuelles** : il sous-pondère le bien cher, précisément parce qu'on l'a fui. → **Il sous-estime l'inflation.**

**La vraie inflation est entre les deux**, et Fisher en donne une estimation raisonnable.

> [!warning] Ce qu'on attend de toi en copie
> Pas seulement « $L_p > P_p$ ». On attend l'**explication par la substitution** : quel bien a le plus augmenté, comment sa consommation a réagi, et pourquoi cela biaise chaque indice dans un sens précis.

---

## 🔗 La relation croisée

$$\boxed{\text{Indice de valeur} = L_p \times P_q = P_p \times L_q}$$

où $L_q$ et $P_q$ sont les indices de **quantité** correspondants.

> [!danger] Ne multiplie jamais deux Laspeyres entre eux
> $L_p \times L_q \neq$ indice de valeur. Il faut **croiser** un Laspeyres de prix avec un Paasche de quantité, ou l'inverse.
>
> **Pourquoi** : $L_p \times P_q = \frac{\sum p_tq_0}{\sum p_0q_0}\times\frac{\sum p_tq_t}{\sum p_tq_0}$ — le terme $\sum p_tq_0$ se simplifie et il reste $\frac{\sum p_tq_t}{\sum p_0q_0}$, qui est bien l'indice de valeur. Avec deux Laspeyres, rien ne se simplifie.

> [!success] La propriété remarquable de Fisher
> $$F_p \times F_q = \text{indice de valeur}$$
> **exactement**. Fisher est le seul des trois à satisfaire ce « test de réversibilité des facteurs ». C'est son principal argument théorique — et une vérification élégante en examen.

---

## 🏛️ Pourquoi l'IPC français est un Laspeyres

Question de cours classique, et la réponse est **pratique**, pas théorique.

Un Paasche exigerait de connaître les quantités consommées **du mois en cours** — donc d'attendre les enquêtes de consommation, soit des mois de délai. Un Laspeyres n'a besoin que des quantités d'une **année de base déjà connue** : l'indice est **publiable immédiatement**, chaque mois.

Le prix à payer est le **biais de substitution** (surestimation). L'INSEE le corrige en **mettant à jour régulièrement la composition et les pondérations du panier**.

📎 [INSEE — Introduction à la pratique des indices statistiques](https://www.insee.fr/fr/metadonnees/source/fichier/IPC_introduction_pratique_indices.pdf) · [Méthodologie de l'IPC](https://www.insee.fr/fr/metadonnees/source/indicateur/p1653/presentation)

---
---
# ✏️ L'exercice de la série, entièrement déroulé

| Bien | $p_0$ | $q_0$ | $p_t$ | $q_t$ |
|---|---|---|---|---|
| A | 15 | 80 | 18 | 70 |
| B | 6 | 250 | 6,6 | 280 |

## Les quatre sommes à calculer d'abord

> [!tip] La méthode qui évite les erreurs
> Calcule les **quatre agrégats** avant toute chose, puis compose les indices. Tu ne feras chaque produit qu'une fois.

| Somme | Calcul | Résultat |
|---|---|---|
| $\sum p_0q_0$ | $15(80)+6(250)$ | $\mathbf{2\,700}$ |
| $\sum p_tq_0$ | $18(80)+6{,}6(250)$ | $\mathbf{3\,090}$ |
| $\sum p_0q_t$ | $15(70)+6(280)$ | $\mathbf{2\,730}$ |
| $\sum p_tq_t$ | $18(70)+6{,}6(280)$ | $\mathbf{3\,108}$ |

## Les indices

**9. Laspeyres-prix** — $\dfrac{3090}{2700}\times100 = \boxed{114{,}44}$
**10. Paasche-prix** — $\dfrac{3108}{2730}\times100 = \boxed{113{,}85}$
**11. Fisher-prix** — $\sqrt{114{,}44\times113{,}85} = \boxed{114{,}14}$
**12. Indice de valeur** — $\dfrac{3108}{2700}\times100 = \boxed{115{,}11}$

### Les indices de quantité (pour la vérification)
$L_q = \dfrac{2730}{2700}\times100 = 101{,}11$ · $P_q = \dfrac{3108}{3090}\times100 = 100{,}58$

### Les vérifications
$$L_p \times P_q = 1{,}1444\times1{,}0058 = \mathbf{1{,}1511} \quad ✓$$
$$P_p \times L_q = 1{,}1385\times1{,}0111 = \mathbf{1{,}1511} \quad ✓$$
$$L_p \times L_q = 1{,}1444\times1{,}0111 = 1{,}1572 \quad ✗ \text{ (ne marche pas)}$$

## Le commentaire attendu

Le bien A a augmenté de **20 %** ($15 \to 18$), le bien B de **10 %** seulement ($6 \to 6{,}6$). Or la consommation de A a **reculé** ($80 \to 70$) tandis que celle de B a **progressé** ($250 \to 280$).

C'est un **effet de substitution** manuel : les ménages se détournent du bien dont le prix a le plus augmenté.

Laspeyres, qui fige les quantités anciennes, continue de pondérer A à hauteur de 80 unités et **surestime** donc l'inflation ($114{,}44$). Paasche, qui utilise les quantités actuelles, sous-pondère A et **sous-estime** ($113{,}85$). Fisher se place entre les deux ($114{,}14$).

L'écart est ici modeste — **0,6 point** — parce que les mouvements de quantités sont limités. Il se creuse fortement quand les substitutions sont massives.

---
---

## 🚫 Les 5 pièges du chapitre

> [!danger] 1. Soustraire deux indices
> $126 - 104 \neq$ la variation. On **divise** : $\frac{126}{104}-1$.

> [!danger] 2. Soustraire l'inflation d'une croissance en valeur
> $4{,}8\% - 2{,}1\% = 2{,}7\%$ est une **approximation**, pas le résultat. L'exact est $\frac{1,048}{1,021}-1 = 2{,}64\%$. Sur des taux élevés, l'écart devient inacceptable.

> [!danger] 3. Confondre Laspeyres et Paasche
> **P**aasche = **P**résent. Et rappelle-toi que dans les deux cas, ce sont les **prix** qui varient — seules les quantités de pondération changent.

> [!danger] 4. Multiplier deux Laspeyres
> L'indice de valeur exige un **croisement** : $L_p\times P_q$ ou $P_p\times L_q$. Jamais $L_p\times L_q$.

> [!danger] 5. Rebaser dans le mauvais sens
> On multiplie par $\frac{100}{\text{indice de la nouvelle base}}$. **La vérification** : dans la nouvelle série, l'année de base doit valoir exactement 100, et les variations entre années doivent être inchangées.

---

## ✅ Exercices d'application

- [ ] **A.** Une série vaut 2 400 en 2018 et 3 120 en 2024. Donne l'indice 2024 base 100 en 2018, puis le TCAM sur la période.
- [ ] **B.** Indices base 100 en 2016 : $2016 = 100$ · $2020 = 112$ · $2024 = 133$. Calcule la variation 2020→2024, puis rebase la série en 2020.
- [ ] **C.** Un chiffre d'affaires progresse de 6,5 % en valeur. Les prix de vente ont augmenté de 4,2 %. Quelle est l'évolution en volume ? L'entreprise a-t-elle vendu plus ?
- [ ] **D.** Un salaire passe de 2 200 € à 2 310 €. L'IPC passe de 105 à 110. Le pouvoir d'achat progresse-t-il ?
- [ ] **E.** Deux biens :

| Bien | $p_0$ | $q_0$ | $p_t$ | $q_t$ |
|---|---|---|---|---|
| X | 10 | 200 | 12 | 180 |
| Y | 25 | 40 | 26 | 50 |

Calcule $L_p$, $P_p$, $F_p$, l'indice de valeur, et vérifie la relation croisée. Commente l'écart $L_p - P_p$.

> [!success]- Corrigés A à D
> **A.** $I_{2024} = 100\times\frac{3120}{2400} = \boxed{130}$, soit $+30\%$ sur 6 ans.
> TCAM $= \left(\frac{3120}{2400}\right)^{1/6}-1 = 1{,}30^{1/6}-1 = \boxed{+4{,}47\%\ \text{par an}}$
> ⚠️ Ne surtout pas faire $\frac{30}{6} = 5\%$ : les taux se composent.
>
> **B.** Variation : $\frac{133}{112}-1 = \boxed{+18{,}75\%}$ — et non $+21$.
> Rebasage (coefficient $\frac{100}{112}$) : $2016 \to \boxed{89{,}3}$ · $2020 \to \boxed{100}$ · $2024 \to \boxed{118{,}75}$
> Vérification : $118{,}75$ correspond bien à $+18{,}75\%$ depuis 2020 ✓
>
> **C.** $q = \frac{1,065}{1,042}-1 = \boxed{+2{,}21\%}$
> **Oui, l'entreprise a vendu plus** — mais bien moins que ne le suggère la progression du chiffre d'affaires. Sur les 6,5 % de hausse, environ les deux tiers viennent des **prix** et un tiers seulement des **volumes**.
> *(L'approximation $6{,}5-4{,}2 = 2{,}3$ donne un ordre de grandeur correct, mais l'exact est 2,21.)*
>
> **D.** Salaire : $\frac{2310}{2200}-1 = +5{,}0\%$ · Prix : $\frac{110}{105}-1 = +4{,}76\%$
> Pouvoir d'achat : $\frac{1,05}{1,0476}-1 = \boxed{+0{,}23\%}$
> **Oui, mais de façon quasi négligeable** : la hausse de salaire est presque intégralement absorbée par l'inflation. C'est typiquement le cas où le salarié perçoit une augmentation de 5 % sans ressentir aucune amélioration.

> [!success]- Corrigé E
> **Les quatre sommes**
>
> | Somme | Calcul | Résultat |
> |---|---|---|
> | $\sum p_0q_0$ | $10(200)+25(40)$ | $3\,000$ |
> | $\sum p_tq_0$ | $12(200)+26(40)$ | $3\,440$ |
> | $\sum p_0q_t$ | $10(180)+25(50)$ | $3\,050$ |
> | $\sum p_tq_t$ | $12(180)+26(50)$ | $3\,460$ |
>
> $L_p = \frac{3440}{3000}\times100 = \boxed{114{,}67}$
> $P_p = \frac{3460}{3050}\times100 = \boxed{113{,}44}$
> $F_p = \sqrt{114{,}67\times113{,}44} = \boxed{114{,}05}$
> Indice de valeur $= \frac{3460}{3000}\times100 = \boxed{115{,}33}$
>
> **Vérification croisée** : $P_q = \frac{3460}{3440}\times100 = 100{,}58$, et $1{,}1467\times1{,}0058 = 1{,}1533$ ✓
>
> **Commentaire** : le bien X a augmenté de **20 %** ($10\to12$), le bien Y de **4 %** seulement ($25\to26$). La consommation de X a reculé ($200\to180$) au profit de Y ($40\to50$) — **substitution nette** vers le bien resté bon marché.
> Laspeyres, en conservant les 200 unités de X, surpondère le bien devenu cher et **surestime** l'inflation. Paasche fait l'inverse. L'écart de **1,2 point** est plus marqué que dans l'exercice du cours, parce que l'écart de prix entre les deux biens (20 % contre 4 %) est plus fort et la substitution plus nette.

---

## 🔗 Ce que ce chapitre débloque

| Où | Comment |
|---|---|
| [[Cycle 2 - Les chiffres\|UE 14C]] — statistiques | Chapitre au programme, Laspeyres et Paasche évalués directement |
| [[Cycle 1 - Moteur economique\|UE 11B]] — macro | PIB en volume, déflateur, mesure de l'inflation |
| [[Cycle 3 - Gestion et debats\|UE 13A]] — dissertations | Pouvoir d'achat, inflation, salaires réels |
| [[Cycle 2 - Les chiffres\|UE 14C]] — séries chronologiques | Toute comparaison temporelle exige de déflater |
| L2 — comptabilité nationale | Volume/valeur sur tous les agrégats |

> [!abstract] Les trois phrases à retenir
> **1.** Entre deux indices, on **divise**, jamais on ne soustrait.
> **2. Déflater, c'est diviser** : $1+q = \frac{1+v}{1+p}$. Les taux ne se soustraient pas.
> **3.** **Laspeyres surestime, Paasche sous-estime**, parce que les consommateurs substituent — et l'IPC est un Laspeyres pour une raison purement pratique de délai de publication.

---

← [[Cours - Contributions a la croissance]] · [[Cours - Tableaux de signes et inequations]] · 🏋️ [[Fiche exos - Modules A C E]] · 🏠 [[00 - Plan L1 Angers]]
