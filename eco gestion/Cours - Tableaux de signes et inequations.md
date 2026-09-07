---
tags:
  - L1-eco-gestion
  - cycle-0
  - module-A
  - cours
notion: Tableaux de signes et inéquations
prerequis: équations du second degré
statut: à faire
---

# 📘 Cours — Tableaux de signes et inéquations

**Module A3 du [[Cycle 0 - Fondations|cycle 0]] · ≈ 1 h 30 de cours + 1 h d'exercices**
🏋️ [[Fiche exos - Modules A C E]] (items A-I 14 à 20) · 🏠 [[00 - Plan L1 Angers]]

---

## 🎯 Pourquoi cette technique décide de tes notes

Sur le papier, c'est un chapitre de seconde. En réalité, c'est **l'outil le plus utilisé de toute ta licence**, sous trois déguisements.

### Usage 1 — Trouver un optimum
En économie, on cherche constamment un maximum : de profit, d'utilité, de production. La procédure est toujours la même :
$$\text{Dériver} \rightarrow \textbf{étudier le signe de } f' \rightarrow \text{en déduire les variations de } f$$

Or « étudier le signe de $f'$ », c'est **exactement** un tableau de signes. Quand tu écris que le profit croît puis décroît, tu as fait un tableau de signes.

### Usage 2 — Répondre à une question de rentabilité
« Pour quelles quantités l'entreprise est-elle bénéficiaire ? » est littéralement l'inéquation $\pi(q) \geq 0$. C'est l'exercice 18 de ta série, et c'est une question d'examen classique.

### Usage 3 — Déterminer un domaine de définition
Un coût moyen $CM = \frac{CT(q)}{q}$ n'existe pas en $q = 0$. Une racine carrée exige un contenu positif. Un logarithme exige un contenu strictement positif. Chaque fois, il faut résoudre une inéquation.

> [!tip] La bonne façon de voir ce chapitre
> Ce n'est pas une technique scolaire à cocher. C'est **la mécanique qui te permettra de conclure** dans tous les exercices de micro et de contrôle de gestion. Sans elle, tu sais dériver mais tu ne sais pas quoi faire du résultat.

---

## 💡 L'idée unique

Tout le chapitre repose sur **une seule observation**, et si tu la comprends, tu n'as plus rien à mémoriser.

> [!abstract] Le principe fondamental
> Un produit ou un quotient de facteurs ne peut **changer de signe** qu'en un point où **l'un de ses facteurs s'annule** (ou n'est pas défini).
>
> Entre deux tels points consécutifs, le signe est **constant**.

Pourquoi ? Parce que pour passer du positif au négatif, une expression continue doit forcément passer par zéro. Elle ne peut pas « sauter » par-dessus.

**La conséquence pratique est immédiate.** Il suffit de :
1. repérer **tous** les points où un facteur s'annule,
2. les ranger sur une droite,
3. déterminer le signe **une seule fois** dans chaque intervalle ainsi découpé.

C'est tout. Le tableau de signes n'est qu'une mise en page de ce raisonnement.

---

## 🧱 Les trois briques

Tu ne rencontreras jamais que trois types de facteurs. Apprends leur signe une fois.

### Brique 1 — Le facteur affine $ax+b$

- **Il s'annule en** $x = -\dfrac{b}{a}$
- **Après** cette racine, il a le signe de $a$
- **Avant**, il a le signe opposé

> [!tip] Le mnémonique
> Une droite **croissante** ($a>0$) est **négative puis positive**. Une droite **décroissante** ($a<0$) est **positive puis négative**. Dessine la droite dans un coin de ta copie si tu hésites : ça prend trois secondes et ça élimine l'erreur.

**Exemples**
- $3x-9$ : $a=3>0$, racine en $3$ → négatif sur $]-\infty;3[$, positif sur $]3;+\infty[$
- $2-\dfrac{x}{5}$ : le coefficient de $x$ vaut $-\frac{1}{5}<0$, racine en $10$ → **positif** sur $]-\infty;10[$, négatif après

### Brique 2 — Le trinôme $ax^2+bx+c$

Calcule $\Delta = b^2-4ac$, puis applique :

| Cas | Signe |
|---|---|
| $\Delta > 0$ (deux racines $x_1 < x_2$) | Signe de $a$ **à l'extérieur** des racines · signe de $-a$ **entre** les racines |
| $\Delta = 0$ (racine double) | Signe de $a$ **partout**, nul en la racine |
| $\Delta < 0$ (pas de racine) | Signe de $a$ **partout**, jamais nul |

> [!tip] Pourquoi « à l'extérieur, le signe de $a$ »
> Ce n'est pas arbitraire. Quand $x \to \pm\infty$, le terme $ax^2$ écrase les autres : le trinôme prend donc le signe de $a$ aux extrémités. Et comme il ne change de signe qu'en ses racines, il ne peut prendre le signe **opposé** qu'entre les deux.
>
> **Retiens la phrase, pas le tableau** : *« signe de a à l'extérieur, contraire de a entre les racines. »*

**Exemple** — $-3x^2+12x$. Ici $a=-3<0$ et les racines sont $0$ et $4$. Donc l'expression est **positive entre** $0$ et $4$, négative à l'extérieur.

### Brique 3 — Le quotient $\dfrac{N(x)}{D(x)}$

La règle des signes est **identique** à celle du produit : $\frac{-}{-} = +$, $\frac{-}{+} = -$, etc.

**Une seule différence, mais elle est décisive** : le dénominateur ne peut pas être nul. Le point qui l'annule est une **valeur interdite**. Dans le tableau, on l'indique par une **double barre**, et elle est **exclue de la solution**, même avec une inégalité large ($\leq$ ou $\geq$).

---

## 🔧 La méthode en 5 étapes

> [!warning] Étape 0 — Ne développe jamais une expression déjà factorisée
> C'est l'erreur la plus coûteuse du chapitre. Si l'énoncé te donne $(3x-9)(x+2)$, tu as **déjà** le travail fait : les racines se lisent directement. Développer pour obtenir $3x^2-3x-18$ puis recalculer un discriminant, c'est se créer du travail et des risques d'erreur.
>
> **Le réflexe inverse est le bon** : si l'expression n'est *pas* factorisée, cherche à la factoriser.

**1. Ramener à une comparaison à zéro.**
Une inéquation se résout toujours sous la forme $\text{expression} \geq 0$ ou $\leq 0$. Si tu as $f(x) \geq g(x)$, passe tout d'un côté : $f(x)-g(x) \geq 0$.

**2. Lister les zéros et les valeurs interdites.**
Un zéro par facteur. Toute valeur annulant un dénominateur est interdite.

**3. Ranger ces valeurs par ordre croissant** sur la première ligne du tableau.

**4. Une ligne par facteur.** Pour chacun, appliquer la brique 1 ou 2.

**5. Ligne de synthèse** : multiplier les signes colonne par colonne. Puis **lire la solution en intervalles**.

> [!tip] Le choix des crochets
> - Inégalité **stricte** ($<$, $>$) → crochets **ouverts** : les racines sont exclues
> - Inégalité **large** ($\leq$, $\geq$) → crochets **fermés** : les racines sont incluses
> - **Valeur interdite** → **toujours** exclue, crochet ouvert, quelle que soit l'inégalité

---
---

# ✏️ Les 7 exercices, entièrement expliqués

## Exercice 14 — Signe de $(3x-9)(x+2)$

**Étape 1 — les zéros.** $3x-9=0 \Rightarrow x=3$ · $x+2=0 \Rightarrow x=-2$
**Étape 2 — les ranger.** $-2 < 3$

**Étape 3 — le tableau.**

| Intervalle | $]-\infty;-2[$ | $-2$ | $]-2;3[$ | $3$ | $]3;+\infty[$ |
|---|---|---|---|---|---|
| $3x-9$ | $-$ | $-$ | $-$ | $\mathbf{0}$ | $+$ |
| $x+2$ | $-$ | $\mathbf{0}$ | $+$ | $+$ | $+$ |
| **Produit** | $\boldsymbol{+}$ | $\mathbf{0}$ | $\boldsymbol{-}$ | $\mathbf{0}$ | $\boldsymbol{+}$ |

**Conclusion.** L'expression est **positive** sur $]-\infty;-2[\,\cup\,]3;+\infty[$, **nulle** en $-2$ et $3$, **négative** sur $]-2;3[$.

> [!success] Vérification en 5 secondes
> Développé, ce produit vaut $3x^2 - 3x - 18$, donc $a = 3 > 0$. La brique 2 prédit « signe de $a$ à l'extérieur des racines », soit **positif à l'extérieur** — exactement ce que donne le tableau. ✓
>
> **Prends l'habitude de ce contrôle croisé.** Il coûte trois secondes et détecte 90 % des erreurs de tableau.

---

## Exercice 15 — Signe de $\dfrac{x-4}{x+1}$

**Zéro du numérateur** : $x=4$. **Valeur interdite** : $x=-1$ (annule le dénominateur).

| Intervalle | $]-\infty;-1[$ | $-1$ | $]-1;4[$ | $4$ | $]4;+\infty[$ |
|---|---|---|---|---|---|
| $x-4$ | $-$ | $-$ | $-$ | $\mathbf{0}$ | $+$ |
| $x+1$ | $-$ | $\mathbf{0}$ | $+$ | $+$ | $+$ |
| **Quotient** | $\boldsymbol{+}$ | $\Vert$ | $\boldsymbol{-}$ | $\mathbf{0}$ | $\boldsymbol{+}$ |

**Conclusion.** Positif sur $]-\infty;-1[\,\cup\,]4;+\infty[$, négatif sur $]-1;4[$, nul en $4$, **non défini** en $-1$.

> [!warning] Les deux erreurs à ne pas commettre
> **1.** Écrire un $0$ sous $-1$ dans la ligne de synthèse. Le quotient n'y vaut pas zéro : il **n'existe pas**. D'où la double barre $\Vert$.
> **2.** Croire que le dénominateur « ne compte pas » dans le signe. Il compte exactement autant qu'un facteur du numérateur — la règle des signes est la même pour la division et la multiplication.

---

## Exercice 16 — Résoudre $x^2-9x+20 \leq 0$

Pas de factorisation apparente → **brique 2**.

$\Delta = (-9)^2 - 4(1)(20) = 81-80 = 1$, donc $\sqrt\Delta = 1$.
$$x_1 = \frac{9-1}{2} = 4 \qquad x_2 = \frac{9+1}{2} = 5$$

Ici $a = 1 > 0$. La brique 2 dit : signe de $a$ à l'extérieur, **contraire de $a$ entre les racines**. On cherche là où l'expression est **négative** → **entre les racines**.

| Intervalle | $]-\infty;4[$ | $4$ | $]4;5[$ | $5$ | $]5;+\infty[$ |
|---|---|---|---|---|---|
| $x^2-9x+20$ | $+$ | $\mathbf{0}$ | $\boldsymbol{-}$ | $\mathbf{0}$ | $+$ |

**Solution** : $\boxed{S = [4\,;5]}$ — crochets **fermés** car l'inégalité est large ($\leq$), donc $4$ et $5$ sont solutions.

---

## Exercice 17 — Résoudre $-3x^2+12x \geq 0$

Il y a deux voies. **La seconde est meilleure.**

### ❌ Voie 1 — diviser par $-3$
$$-3x^2+12x \geq 0 \quad\Longleftrightarrow\quad x^2-4x \leq 0$$
> [!danger] Le piège
> En divisant par un nombre **négatif**, l'inégalité **change de sens**. C'est l'oubli le plus fréquent de tout le chapitre. Si tu écris $x^2-4x \geq 0$, tu obtiens la solution exactement inverse.

On factorise : $x(x-4) \leq 0$, racines $0$ et $4$, $a=1>0$ → négatif entre les racines → $S = [0\,;4]$.

### ✅ Voie 2 — factoriser sans jamais diviser
$$-3x^2+12x = -3x(x-4)$$
Racines : $0$ et $4$. Coefficient dominant $a = -3 < 0$.
La brique 2 dit : signe de $a$ à l'extérieur (donc négatif), **contraire de $a$ entre** (donc **positif**).

| Intervalle | $]-\infty;0[$ | $0$ | $]0;4[$ | $4$ | $]4;+\infty[$ |
|---|---|---|---|---|---|
| $-3x^2+12x$ | $-$ | $\mathbf{0}$ | $\boldsymbol{+}$ | $\mathbf{0}$ | $-$ |

**Solution** : $\boxed{S = [0\,;4]}$

> [!tip] Pourquoi la voie 2 est meilleure
> **Ne divise pas, lis le signe de $a$.** Tu supprimes du même coup le risque d'oublier le changement de sens. Une opération en moins, une erreur possible en moins.

---

## Exercice 18 — $\pi(q) = -q^2+16q-48$ : quand l'entreprise est-elle bénéficiaire ?

**C'est l'exercice qui donne son sens à tout le chapitre.** « Être bénéficiaire » signifie $\pi(q) \geq 0$.

$\Delta = 16^2 - 4(-1)(-48) = 256-192 = 64$, donc $\sqrt\Delta = 8$.
$$q = \frac{-16 \pm 8}{2 \times (-1)} \quad\Rightarrow\quad q_1 = \frac{-8}{-2} = 4 \qquad q_2 = \frac{-24}{-2} = 12$$

$a = -1 < 0$ → le trinôme est **positif entre** les racines.

| Intervalle | $[0;4[$ | $4$ | $]4;12[$ | $12$ | $]12;+\infty[$ |
|---|---|---|---|---|---|
| $\pi(q)$ | $-$ | $\mathbf{0}$ | $\boldsymbol{+}$ | $\mathbf{0}$ | $-$ |

**Solution mathématique** : $S = [4\,;12]$
**Solution économique** : une quantité est nécessairement positive, donc on retient $\boxed{q \in [4\,;12]}$.

> [!success] La lecture économique — c'est elle qui rapporte les points
> - $q = 4$ est le **seuil de rentabilité** : en dessous, les quantités vendues ne couvrent pas les coûts fixes.
> - $q = 12$ est le **point de saturation** : au-delà, les coûts croissent plus vite que la recette et le profit redevient négatif.
> - Le **profit maximal** est au sommet de la parabole, à mi-chemin entre les racines : $q = \frac{4+12}{2} = 8$, et $\pi(8) = -64+128-48 = \boxed{16}$.
>
> **En examen, ne t'arrête jamais à $S = [4;12]$.** Termine par une phrase d'interprétation : « L'entreprise est bénéficiaire pour une production comprise entre 4 et 12 unités, avec un profit maximal de 16 atteint pour 8 unités. » Un nombre sans interprétation vaut la moitié des points.

---

## Exercice 19 — Signe de $2-\dfrac{x}{5}$

Fonction **affine**, donc brique 1. Le coefficient de $x$ est $-\frac{1}{5} < 0$ : la droite est **décroissante**.

**Zéro** : $2-\dfrac{x}{5}=0 \Rightarrow \dfrac{x}{5}=2 \Rightarrow x=10$

| Intervalle | $]-\infty;10[$ | $10$ | $]10;+\infty[$ |
|---|---|---|---|
| $2-\frac{x}{5}$ | $\boldsymbol{+}$ | $\mathbf{0}$ | $\boldsymbol{-}$ |

**Conclusion.** Positif sur $]-\infty;10[$, nul en $10$, négatif sur $]10;+\infty[$.

> [!warning] Le réflexe faux à désamorcer
> Beaucoup lisent le « $2$ » en tête et concluent « positif puis négatif… ou l'inverse ? ». **Ne regarde que le coefficient de $x$.** Ici $-\frac{1}{5}$ est négatif, donc la fonction décroît : elle est positive **avant** son zéro. La constante ne détermine que l'emplacement du zéro, jamais le sens.

---

## Exercice 20 — Résoudre $(x-1)(x-3)(x-5) > 0$

Trois facteurs, déjà factorisés. **Ne développe surtout pas** — tu obtiendrais un polynôme de degré 3 inutilisable.

**Zéros** : $1$, $3$, $5$. Ils découpent la droite en **quatre** intervalles.

| Intervalle | $]-\infty;1[$ | $1$ | $]1;3[$ | $3$ | $]3;5[$ | $5$ | $]5;+\infty[$ |
|---|---|---|---|---|---|---|---|
| $x-1$ | $-$ | $\mathbf{0}$ | $+$ | $+$ | $+$ | $+$ | $+$ |
| $x-3$ | $-$ | $-$ | $-$ | $\mathbf{0}$ | $+$ | $+$ | $+$ |
| $x-5$ | $-$ | $-$ | $-$ | $-$ | $-$ | $\mathbf{0}$ | $+$ |
| **Produit** | $\boldsymbol{-}$ | $\mathbf{0}$ | $\boldsymbol{+}$ | $\mathbf{0}$ | $\boldsymbol{-}$ | $\mathbf{0}$ | $\boldsymbol{+}$ |

**Solution** : $\boxed{S = \;]1;3[\;\cup\;]5;+\infty[}$ — crochets **ouverts** car l'inégalité est **stricte** ($>$).

> [!tip] Le raccourci de l'alternance
> Regarde la ligne du produit : $-\,+\,-\,+$. Les signes **alternent** à chaque racine.
>
> C'est toujours vrai quand toutes les racines sont **simples et distinctes**. Il suffit donc de déterminer le signe **à une seule extrémité**, puis d'alterner.
>
> **Comment trouver le signe en $+\infty$ ?** C'est le signe du produit des coefficients dominants. Ici $1 \times 1 \times 1 = +$. Donc : $+$ tout à droite, puis en remontant vers la gauche $-$, $+$, $-$.
>
> Sur un produit de trois facteurs ou plus, ce raccourci divise ton temps par trois. Le tableau complet reste utile pour la copie — mais tu connais déjà la réponse avant de le remplir.

---
---

## 🚫 Les 4 pièges qui coûtent des points

> [!danger] 1. Diviser par un négatif sans changer le sens de l'inégalité
> $-2x > 6$ donne $x < -3$, **pas** $x > -3$. **La parade** : ne divise pas, factorise et lis le signe de $a$ (voir l'exercice 17).

> [!danger] 2. Inclure une valeur interdite dans la solution
> Même avec $\leq$ ou $\geq$, un point qui annule un dénominateur est **exclu**. Le crochet reste ouvert, et le tableau porte une double barre $\Vert$ et non un $0$.

> [!danger] 3. Développer une expression déjà factorisée
> Tu détruis l'information la plus précieuse — les racines — pour la reconstruire ensuite au discriminant. Pure perte de temps et source d'erreurs.

> [!danger] 4. Oublier la contrainte économique
> En économie, $q \geq 0$, $L \geq 0$, $P \geq 0$. Une solution mathématique comme $]-\infty;-2[$ n'a aucun sens pour une quantité produite. **Vérifie toujours la pertinence économique de ton intervalle**, et dis-le explicitement en copie.

---

## 🔗 Ce que ce chapitre débloque dans la suite

| Où | Comment tu réutiliseras exactement cette technique |
|---|---|
| [[Cycle 0 - Fondations\|Module C]] — dérivation | Signe de $f'$ → tableau de variations → optimum. **Même tableau, autre nom.** |
| [[Cycle 1 - Moteur economique\|UE 11C]] — microéconomie | Zone de profit, seuil de fermeture, maximisation |
| [[Cycle 1 - Moteur economique\|UE 11B]] — macroéconomie | Conditions de stabilité, domaines de validité |
| [[Cycle 2 - Les chiffres\|UE 16A/26A]] — contrôle de gestion | **Seuil de rentabilité** : c'est l'exercice 18, avec des chiffres réels |
| L2 — calcul actuariel | Conditions de rentabilité d'un investissement, signe de la VAN |

> [!abstract] La phrase à retenir
> Un produit ne change de signe qu'où un facteur s'annule. **Tout le reste n'est que mise en page.**

---

## ✅ Auto-test — 10 minutes, sans notes

- [ ] **1.** Signe de $(2x-8)(x+5)$
- [ ] **2.** Signe de $\dfrac{3-x}{x-2}$
- [ ] **3.** Résoudre $x^2-x-6 \geq 0$
- [ ] **4.** Résoudre $-2x^2+10x-12 > 0$
- [ ] **5.** $\pi(q) = -q^2+20q-64$. Pour quelles quantités l'entreprise est-elle bénéficiaire ? Quel est le profit maximal ?

> [!success]- Corrigé de l'auto-test
> **1.** Racines $4$ et $-5$. Coefficient dominant $2>0$ → **positif à l'extérieur** : positif sur $]-\infty;-5[\,\cup\,]4;+\infty[$, négatif sur $]-5;4[$.
>
> **2.** Zéro du numérateur en $3$, **valeur interdite** en $2$.
> Attention : $3-x$ a un coefficient de $x$ **négatif**, donc il est positif **avant** $3$.
>
> | Intervalle | $]-\infty;2[$ | $2$ | $]2;3[$ | $3$ | $]3;+\infty[$ |
> |---|---|---|---|---|---|
> | $3-x$ | $+$ | $+$ | $+$ | $\mathbf{0}$ | $-$ |
> | $x-2$ | $-$ | $\mathbf{0}$ | $+$ | $+$ | $+$ |
> | **Quotient** | $\boldsymbol{-}$ | $\Vert$ | $\boldsymbol{+}$ | $\mathbf{0}$ | $\boldsymbol{-}$ |
>
> Positif sur $]2;3[$ uniquement.
>
> **3.** $\Delta = 1+24 = 25$, racines $\frac{1\pm5}{2} = 3$ et $-2$. $a=1>0$ → positif à l'extérieur.
> $\boxed{S = \;]-\infty;-2]\;\cup\;[3;+\infty[}$ — crochets fermés sur les racines car $\geq$.
>
> **4.** Factorisation : $-2(x^2-5x+6) = -2(x-2)(x-3)$. Racines $2$ et $3$, $a=-2<0$ → **positif entre**.
> $\boxed{S = \;]2;3[}$ — ouvert car inégalité stricte.
>
> **5.** $\Delta = 400-256 = 144$, $\sqrt\Delta = 12$. $q = \frac{-20\pm12}{-2}$ → $q_1 = 4$, $q_2 = 16$.
> $a = -1 < 0$ → positif entre les racines : $\boxed{q \in [4\,;16]}$
> Sommet : $q = \frac{4+16}{2} = 10$, et $\pi(10) = -100+200-64 = \boxed{36}$
> **Phrase de conclusion attendue** : « L'entreprise est bénéficiaire entre 4 et 16 unités produites. Le seuil de rentabilité est de 4 unités, le profit est maximal à 10 unités et vaut 36. »

**Barème** : 4 sur 5 pour considérer la notion acquise. Si tu rates le 2 ou le 4, relis les briques 3 et 2 — ce sont les deux pièges structurels.

→ Suite du module : [[Fiche exos - Modules A C E#SÉRIE A-II — Taux et pourcentages ⭐|série A-II, taux et pourcentages]]
