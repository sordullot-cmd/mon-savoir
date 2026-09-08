---
tags:
  - L1-eco-gestion
  - cycle-0
  - module-A
  - cours
notion: Trouver le signe d'une expression
statut: à faire
---

# 🔍 Cours — Trouver le signe : toutes les méthodes

**Complément du [[Cours - Tableaux de signes et inequations|cours sur les tableaux de signes]]**
🏋️ [[Fiche exos - Modules A C E]] · 🏠 [[00 - Plan L1 Angers]] · 🧠 [[Methode - Comment reviser]]

> [!abstract] Ce que tu vas apprendre ici
> Il n'existe **pas une** façon de trouver un signe, mais **quatre méthodes universelles** et **onze règles selon le type d'expression**.
>
> L'objectif n'est pas de toutes les connaître par cœur : c'est de savoir **laquelle dégainer** selon la situation, et d'en avoir toujours une seconde en réserve pour vérifier.

---
# PARTIE 1 — Les 4 méthodes universelles

Elles fonctionnent sur **n'importe quelle** expression. Elles donnent toujours le même résultat. Elles diffèrent seulement par la vitesse et le risque d'erreur.

---

## ⭐ Méthode 1 — Le test numérique
**La plus sûre. Jamais enseignée. Ne rate jamais.**

### Le principe
Puisque le signe est **constant** entre deux zéros consécutifs, il suffit de **choisir une valeur au hasard** dans chaque intervalle et de calculer. Le signe obtenu vaut pour tout l'intervalle.

### Concrètement, sur $(3x-9)(x+2)$

**Étape 1** — Les zéros : $x=3$ et $x=-2$. Ils découpent trois intervalles.

**Étape 2** — Je choisis **une valeur facile** dans chacun. Peu importe laquelle.

| Intervalle | Je teste | Calcul | Résultat | Signe |
|---|---|---|---|---|
| $]-\infty;-2[$ | $x=-10$ | $(-39)\times(-8)$ | $+312$ | $\boldsymbol{+}$ |
| $]-2;3[$ | $x=0$ | $(-9)\times(2)$ | $-18$ | $\boldsymbol{-}$ |
| $]3;+\infty[$ | $x=10$ | $(21)\times(12)$ | $+252$ | $\boldsymbol{+}$ |

**Terminé.** Aucune règle mémorisée, aucun risque de confusion sur le signe de $a$.

> [!tip] Comment choisir la valeur test
> Prends la plus **simple** de l'intervalle, pas la plus « au milieu ». $0$ est presque toujours le meilleur choix quand il est disponible : tout se calcule de tête.
> Pour l'intervalle de gauche, prends un nombre franchement négatif ($-10$, $-100$). Pour celui de droite, un nombre franchement positif.

> [!success] Quand utiliser cette méthode
> - **Quand tu doutes** de ton tableau — c'est ta vérification
> - Quand l'expression est **inhabituelle** et que tu n'as pas de règle sous la main
> - Quand tu es **sous pression** en examen et que tu veux zéro risque
>
> Son seul défaut : elle est un peu plus lente. Mais un tableau juste et lent bat un tableau rapide et faux.

---

## Méthode 2 — La règle facteur par facteur
**La plus rapide sur un produit factorisé. C'est celle qu'on t'enseignera.**

Tu appliques à chaque facteur sa règle (affine, trinôme…), tu écris une ligne par facteur, tu multiplies les signes colonne par colonne.

C'est la méthode détaillée dans le [[Cours - Tableaux de signes et inequations#🔧 La méthode en 5 étapes|cours principal]]. Son avantage : elle **montre le raisonnement** au correcteur, ce que le test numérique ne fait pas. Son inconvénient : chaque ligne est une occasion de se tromper.

> [!warning] Le compromis intelligent en examen
> **Rédige avec la méthode 2** (c'est ce qui est attendu), mais **vérifie avec la méthode 1** avant de conclure. Trois secondes de test numérique sur un intervalle, et tu sais si ton tableau tient.

---

## Méthode 3 — Le dessin mental
**La plus intuitive. Idéale quand tu bloques.**

Tu ne calcules rien : tu **visualises** la courbe de chaque facteur.

| Expression | Ce que tu dessines | Ce que tu lis |
|---|---|---|
| $3x-9$ | Une droite qui **monte**, coupant l'axe en $3$ | Sous l'axe avant $3$, au-dessus après |
| $2-\frac{x}{5}$ | Une droite qui **descend**, coupant en $10$ | Au-dessus avant $10$, sous l'axe après |
| $x^2-9x+20$ | Une parabole **souriante** ($a>0$), racines $4$ et $5$ | Sous l'axe **entre** les racines |
| $-q^2+16q-48$ | Une parabole **triste** ($a<0$), racines $4$ et $12$ | Au-dessus de l'axe **entre** les racines |

> [!tip] Le mnémonique des paraboles
> $a>0$ → parabole **souriante** 🙂 → elle plonge sous l'axe **entre** ses racines
> $a<0$ → parabole **triste** 🙁 → elle passe au-dessus de l'axe **entre** ses racines
>
> Un croquis de trois secondes dans la marge élimine l'erreur de sens. Ne t'en prive pas parce que « ça fait scolaire ».

---

## Méthode 4 — Le comportement à l'infini + alternance
**La plus rapide sur un produit de trois facteurs ou plus.**

### Le principe en deux temps
**Temps 1** — Quel est le signe **tout à droite**, quand $x \to +\infty$ ?
C'est le signe du **produit des coefficients dominants**.

**Temps 2** — Les signes **alternent** à chaque racine simple, en remontant vers la gauche.

### Concrètement, sur $(x-1)(x-3)(x-5)$
Coefficients dominants : $1 \times 1 \times 1 = +$. Donc **positif** en $+\infty$.
Puis on alterne en revenant vers la gauche :

$$\underbrace{-}_{]-\infty;1[} \quad\big|\; 1 \;\big|\quad \underbrace{+}_{]1;3[} \quad\big|\; 3 \;\big|\quad \underbrace{-}_{]3;5[} \quad\big|\; 5 \;\big|\quad \underbrace{+}_{]5;+\infty[}$$

Trois secondes, contre trois lignes de tableau.

> [!danger] La condition de validité
> L'alternance n'est vraie que si toutes les racines sont **simples et distinctes**.
>
> Si une racine est **double** — par exemple $(x-2)^2$ — le signe **ne change pas** en ce point : l'expression touche l'axe et repart du même côté. Idem pour toute puissance **paire**.
>
> Exemple : $(x-1)(x-3)^2$ → racines $1$ et $3$, mais le signe ne change qu'en $1$. Il vaut $-$ avant $1$, puis $+$ sur $]1;3[$ **et** sur $]3;+\infty[$.

---

## 🧭 Quelle méthode choisir ?

```
L'expression est-elle factorisée ?
│
├── OUI ──► Combien de facteurs ?
│           ├── 1 ou 2  ──► MÉTHODE 2 (règle par facteur)
│           └── 3 ou +  ──► MÉTHODE 4 (alternance)
│
└── NON ──► Peux-tu la factoriser ?
            ├── OUI (Δ, facteur commun) ──► factorise, puis MÉTHODE 2
            └── NON ──► MÉTHODE 1 (test numérique)
                        ou étude de fonction par dérivation

Dans TOUS les cas : vérifie avec la MÉTHODE 1 sur un intervalle.
```

---
---
# PARTIE 2 — Le signe selon le type d'expression

Le catalogue complet. Onze cas, et tu ne rencontreras jamais rien d'autre en L1.

---

## 1️⃣ Une constante $k$
Signe de $k$, **partout**, et jamais nulle.
Exemple : $-7$ est négatif sur $\mathbb{R}$ tout entier. Ça paraît trivial, mais c'est ce qui permet de **supprimer** les constantes d'un tableau (voir Partie 3).

## 2️⃣ Un facteur affine $ax+b$
- **Racine** : $x = -\dfrac{b}{a}$
- **Après** la racine : signe de $a$ · **avant** : signe opposé

| Exemple | $a$ | Racine | Signe |
|---|---|---|---|
| $3x-9$ | $+3$ | $3$ | $-$ puis $+$ |
| $-2x+8$ | $-2$ | $4$ | $+$ puis $-$ |
| $2-\frac{x}{5}$ | $-\frac{1}{5}$ | $10$ | $+$ puis $-$ |
| $5x$ | $+5$ | $0$ | $-$ puis $+$ |

> [!warning] Ne regarde **que** le coefficient de $x$
> Dans $2-\frac{x}{5}$, le « $2$ » ne dit rien du sens de variation. Seul $-\frac{1}{5}$ compte. La constante ne fait que déplacer la racine.

## 3️⃣ Un trinôme $ax^2+bx+c$
Calcule $\Delta = b^2-4ac$.

| Cas | Signe |
|---|---|
| $\Delta>0$ | Signe de $a$ **à l'extérieur** des racines, signe de $-a$ **entre** |
| $\Delta=0$ | Signe de $a$ **partout**, nul en la racine double |
| $\Delta<0$ | Signe de $a$ **partout**, jamais nul |

> [!tip] Le cas $\Delta<0$ est un cadeau
> Si $\Delta<0$, le trinôme **ne change jamais de signe**. Tu peux donc le **retirer du tableau** en notant simplement son signe constant. Exemple : $x^2+x+1$ a $\Delta = 1-4 = -3 < 0$ et $a=1>0$ → **strictement positif partout**. Dans un produit, il ne joue plus aucun rôle.

## 4️⃣ Une puissance **paire** : $u^2$, $u^4$, $(x-3)^2$…
$$\boxed{u^{2n} \geq 0 \quad \text{toujours}}$$
Elle est nulle uniquement là où $u=0$, et **positive partout ailleurs**.

**Conséquence majeure** : dans un produit ou un quotient, une puissance paire **ne change jamais le signe**. Elle ne peut que l'annuler ponctuellement. Tu peux donc l'ignorer dans le tableau (en notant juste où elle s'annule).

## 5️⃣ Une puissance **impaire** : $u^3$, $u^5$…
Elle a **exactement le même signe que $u$**. $x^3$ est négatif si $x<0$, positif si $x>0$.

## 6️⃣ Une racine carrée $\sqrt u$
$$\boxed{\sqrt u \geq 0 \quad \text{toujours}}$$
Et elle **exige** $u \geq 0$ pour exister — d'où une contrainte de domaine à vérifier.
Comme la puissance paire : elle ne change jamais le signe d'un produit.

## 7️⃣ Une exponentielle $e^u$ ⭐
$$\boxed{e^u > 0 \quad \text{TOUJOURS, quel que soit } u}$$

> [!success] La simplification la plus rentable de toute la L1
> $e^{-x}$, $e^{x^2}$, $e^{-1000}$ : **strictement positif**, sans exception, jamais nul.
>
> Donc dans un produit ou un quotient, tu **supprimes purement et simplement l'exponentielle** du tableau de signes. Elle ne peut ni changer le signe, ni l'annuler.
>
> **Tu utiliseras ça à chaque exercice d'optimisation en micro.**

## 8️⃣ Un logarithme $\ln u$
Contrairement à l'exponentielle, il **change** de signe.

| Si | Alors $\ln u$ |
|---|---|
| $0 < u < 1$ | **négatif** |
| $u = 1$ | **nul** |
| $u > 1$ | **positif** |

Et il exige $u > 0$ strictement.
**Le point de bascule est $u=1$**, pas $u=0$. C'est l'erreur classique.

## 9️⃣ Un inverse $\dfrac{1}{u}$
**Même signe que $u$**. Un inverse ne renverse pas le signe, il le conserve. (Avec la valeur interdite là où $u=0$.)

## 🔟 Un produit ou un quotient
Règle des signes classique, **identique** pour les deux opérations :
$$(+)(+) = + \qquad (+)(-) = - \qquad (-)(-) = +$$
Seule différence pour le quotient : la **valeur interdite** au dénominateur.

## 1️⃣1️⃣ Une **somme** ⚠️
> [!danger] Il n'existe **aucune** règle pour le signe d'une somme
> $x^2 - 9x + 20$ ne se lit pas terme à terme. Tu ne peux **rien** dire de $A+B$ à partir des signes de $A$ et $B$, sauf dans un seul cas : si $A$ et $B$ sont **de même signe**, la somme aussi.
>
> **C'est toute la raison d'être de la factorisation.** On transforme une somme (illisible) en produit (lisible). Quand tu factorises, tu ne fais pas un exercice de style : tu rends le signe accessible.
>
> **Les deux issues quand ça ne se factorise pas** : le test numérique (méthode 1), ou l'étude de la fonction par dérivation.

---
---
# PARTIE 3 — Les simplifications qui font gagner du temps

**Avant** de construire ton tableau, élimine tout ce qui ne peut pas changer le signe.

| Ce que tu vois | Ce que tu fais | Pourquoi |
|---|---|---|
| $e^u$ | **Supprime-le** | Toujours $>0$ |
| $u^2$, $u^4$, $\sqrt u$ | **Supprime-le**, note juste où il s'annule | Toujours $\geq 0$ |
| Constante **positive** ($3$, $\frac{1}{2}$) | **Supprime-la** | Ne change rien |
| Constante **négative** ($-3$) | Supprime-la et **inverse toute la conclusion** | Renverse tous les signes |
| Trinôme avec $\Delta<0$ | Supprime-le, note son signe constant | Ne change jamais de signe |

## Exemple complet — la puissance de la simplification

Soit $f(x) = x^2e^{-x}$. On cherche son maximum, donc le signe de $f'$.

$$f'(x) = 2xe^{-x} - x^2e^{-x} = e^{-x}\big(2x-x^2\big) = \underbrace{e^{-x}}_{>0 \text{ toujours}} \times\; x(2-x)$$

> [!success] Le raisonnement en une ligne
> $e^{-x} > 0$ toujours → **je le supprime**. Le signe de $f'$ est **exactement** celui de $x(2-x)$.
>
> Racines $0$ et $2$. Développé, $x(2-x) = -x^2+2x$ donc $a = -1 < 0$ → **positif entre les racines**.

| Intervalle | $]-\infty;0[$ | $0$ | $]0;2[$ | $2$ | $]2;+\infty[$ |
|---|---|---|---|---|---|
| $f'(x)$ | $-$ | $\mathbf{0}$ | $\boldsymbol{+}$ | $\mathbf{0}$ | $-$ |
| $f(x)$ | ↘ | min | ↗ | **max** | ↘ |

$f$ atteint son **maximum en $x=2$**, où $f(2) = 4e^{-2} \approx 0{,}541$.

**Sans la simplification**, tu aurais mis $e^{-x}$ dans une ligne du tableau — travail inutile et occasion de te tromper.

## Second exemple — le dénominateur qui disparaît

Soit $f(x) = \dfrac{\ln x}{x}$ (définie pour $x>0$).

$$f'(x) = \frac{\frac{1}{x}\cdot x - \ln x \cdot 1}{x^2} = \frac{1-\ln x}{\underbrace{x^2}_{>0}}$$

Le dénominateur $x^2$ est **strictement positif** sur le domaine → **je le supprime**. Le signe de $f'$ est celui de $1-\ln x$.

$$1-\ln x = 0 \iff \ln x = 1 \iff x = e$$

Et comme $\ln$ est croissante, $1-\ln x$ est **décroissante** : positive avant $e$, négative après.

| Intervalle | $]0;e[$ | $e$ | $]e;+\infty[$ |
|---|---|---|---|
| $f'(x)$ | $\boldsymbol{+}$ | $\mathbf{0}$ | $\boldsymbol{-}$ |
| $f(x)$ | ↗ | **max** | ↘ |

Maximum en $x = e \approx 2{,}718$, valant $\frac{1}{e} \approx 0{,}368$.

---
---
# PARTIE 4 — Que faire quand rien ne marche

Tu tombes sur une expression qui ne se factorise pas et dont aucune règle ne s'applique. Trois issues, dans cet ordre.

## Issue 1 — Le test numérique sur l'expression entière
Tu ne cherches plus les zéros par le calcul : tu **balayes** des valeurs pour les localiser.
Exemple : $g(x) = x^3 - 2x - 1$. Je teste $g(-2)=-5$, $g(-1)=0$ ✓ (racine trouvée), $g(0)=-1$, $g(2)=3$. Il y a donc un changement de signe entre $0$ et $2$.

## Issue 2 — L'étude de fonction par dérivation
**C'est la méthode de L1.** Si tu ne sais pas lire le signe de $f$ directement, étudie $f'$ : tu obtiens les variations de $f$, donc son minimum, et si ce minimum est positif, $f$ l'est partout.

**Exemple type** — Montrer que $e^x \geq x+1$ pour tout $x$.
Impossible à lire directement. On pose $g(x) = e^x-x-1$ et on étudie :
$g'(x) = e^x-1$, qui s'annule en $x=0$, négatif avant, positif après.
Donc $g$ atteint son **minimum global** en $0$, et $g(0) = 1-0-1 = 0$.
Le minimum vaut $0$ → $g(x) \geq 0$ partout → $e^x \geq x+1$ ✓

## Issue 3 — La reconnaissance de forme
Parfois, il suffit de voir que **tous les termes sont positifs**.
$x^2 + e^x + 1$ : somme de $\geq 0$, de $>0$ et de $>0$ → **strictement positif**, aucun calcul nécessaire.

---
---
# 📋 Le tableau récapitulatif

| Expression | Signe | Change de signe ? |
|---|---|---|
| Constante $k$ | Signe de $k$ | Non |
| $ax+b$ | Signe de $a$ après $-\frac{b}{a}$ | **Oui**, une fois |
| $ax^2+bx+c$, $\Delta>0$ | $a$ à l'extérieur, $-a$ entre | **Oui**, deux fois |
| $ax^2+bx+c$, $\Delta\leq0$ | Signe de $a$ partout | Non |
| $u^2$, $u^4$, $\sqrt u$ | $\geq 0$ | Non |
| $u^3$, $u^5$ | Signe de $u$ | Comme $u$ |
| $e^u$ | $> 0$ **toujours** | **Non** ⭐ |
| $\ln u$ | $<0$ si $u<1$ · $>0$ si $u>1$ | **Oui**, en $u=1$ |
| $\frac{1}{u}$ | Signe de $u$ | Comme $u$ |
| Produit / quotient | Règle des signes | Aux zéros des facteurs |
| **Somme** | **Aucune règle** ⚠️ | Il faut factoriser ou dériver |

---

## 🎯 Les 4 réflexes à emporter

1. **Face à une somme, factorise.** C'est la seule façon de rendre le signe lisible.
2. **Supprime tout ce qui est toujours positif** avant de faire le tableau : exponentielles, carrés, racines, constantes positives.
3. **Sur trois facteurs ou plus, utilise l'alternance** plutôt que trois lignes de tableau.
4. **Vérifie toujours par un test numérique.** Trois secondes, et tu détectes 90 % des erreurs.

> [!abstract] La hiérarchie, en une phrase
> La méthode 2 est celle qu'on te demande de **rédiger**, la méthode 4 celle qui te fait **gagner du temps**, et la méthode 1 celle qui t'évite de **rendre une bêtise**.

---

## 🔄 Comment réviser cette fiche

*Méthode de révision, pas du cours. Le détail des études est dans [[Methode - Comment reviser]].*

1. **Refaire, pas relire** — [[#✅ Auto-test — 12 minutes|l'auto-test ci-dessous]], sans notes. Se tester retient **61 %** du contenu à une semaine, contre **40 %** en relisant.
2. **Jusqu'à 3 réussites de suite** sur un même type d'exercice — une réussite isolée ne veut pas dire acquis.
3. **Puis 3 reprises espacées** — intervalle ≈ **10 à 20 % du délai** avant l'épreuve : à six semaines, tous les 4 à 8 jours. Ce sont exactement les colonnes « Essai 1 / 2 / 3 » de [[Fiche exos - Modules A C E]].
4. **Mélange les types d'exercices** — c'est ici que ça compte le plus : 61 % en pratique entrelacée contre 38 % en pratique bloquée (d = 0,83). Enchaîner dix exercices du même type n'entraîne que l'exécution ; en examen, l'énoncé ne dit pas quelle méthode appliquer.
5. **Tire une expression au hasard sans regarder de quelle famille elle relève, puis choisis ta méthode : c'est tout l'enjeu de cette fiche, et c'est ce que fait l'examen.**

## ✅ Auto-test — 12 minutes

Détermine le signe, en indiquant à chaque fois **quelle méthode** tu utilises et **ce que tu as pu supprimer**.

- [ ] **1.** $f(x) = (x+4)e^{2x}$
- [ ] **2.** $f(x) = \dfrac{x-3}{(x+1)^2}$
- [ ] **3.** $f(x) = x^2(x-5)$
- [ ] **4.** $f(x) = (x^2+x+1)(2x-6)$
- [ ] **5.** $f(x) = \dfrac{2-\ln x}{x}$ sur $]0;+\infty[$
- [ ] **6.** $f'(q) = -3q^2+18q$ où $q$ est une quantité produite. Où le profit croît-il ?

> [!success]- Corrigé de l'auto-test
> **1.** $e^{2x} > 0$ toujours → **je le supprime**. Le signe est celui de $x+4$ : **négatif** sur $]-\infty;-4[$, nul en $-4$, **positif** sur $]-4;+\infty[$.
>
> **2.** $(x+1)^2 \geq 0$ → ne change pas le signe, mais **valeur interdite en $-1$**. Le signe est celui de $x-3$ : **négatif** sur $]-\infty;-1[\cup]-1;3[$, nul en $3$, **positif** sur $]3;+\infty[$.
> ⚠️ Le point $-1$ n'annule pas $f$ — il l'empêche d'exister. Double barre.
>
> **3.** $x^2 \geq 0$ → ne change pas le signe, s'annule en $0$. Le signe est celui de $x-5$ : **négatif** sur $]-\infty;0[\cup]0;5[$, nul en $0$ **et** en $5$, **positif** sur $]5;+\infty[$.
> ⚠️ Piège de l'alternance : le signe **ne change pas** en $0$, car la racine est double.
>
> **4.** $x^2+x+1$ : $\Delta = 1-4 = -3 < 0$ et $a=1>0$ → **strictement positif partout**, je le supprime. Le signe est celui de $2x-6$ : **négatif** avant $3$, **positif** après.
>
> **5.** $x > 0$ sur le domaine → **je supprime le dénominateur**. Le signe est celui de $2-\ln x$.
> $2-\ln x = 0 \iff \ln x = 2 \iff x = e^2 \approx 7{,}39$
> $\ln$ croissante donc $2-\ln x$ décroissante : **positive** sur $]0;e^2[$, **négative** sur $]e^2;+\infty[$.
>
> **6.** $f'(q) = -3q(q-6)$. Racines $0$ et $6$, coefficient dominant $-3<0$ → **positif entre les racines**.
> Le profit **croît** pour $q \in\ ]0;6[$, **décroît** au-delà de $6$.
> **Interprétation économique** : le profit est **maximal pour $q = 6$**. Produire davantage le ferait baisser. C'est exactement la condition du premier ordre $\pi'(q) = 0$ avec vérification du second ordre par le changement de signe.

**Barème** : 5 sur 6. Si tu rates le 2 ou le 3, revois les puissances paires — c'est le piège structurel du chapitre.

---

← [[Cours - Tableaux de signes et inequations]] · 🏋️ [[Fiche exos - Modules A C E]] · 🏠 [[00 - Plan L1 Angers]]
