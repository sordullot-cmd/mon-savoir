---
tags:
  - L1-eco-gestion
  - hub
---

# 🎓 Mes cours — où j'en suis

> [!abstract] Comment lire cette page
> Elle se remplit toute seule à partir du frontmatter des fiches : rien à tenir à jour à la main. `Trous` = le nombre de points listés dans le bloc **À vérifier / à récupérer** de la fiche — c'est là qu'il y a des points à perdre.

🏠 [[00 - Plan L1 Angers]] · 📋 [[MCC - Tableau de bord]] · 🃏 [[Anki - Formules et definitions C0-C1]] · 🔗 [[Ressources - Bibliotheque de liens]]

---

## 📌 Les fiches d'UE, dans l'ordre où elles tombent

```dataview
TABLE WITHOUT ID
  file.link AS "Fiche",
  "P" + periode AS "Période",
  "coef " + coef AS "Poids",
  statut AS "Statut",
  a_verifier AS "Trous",
  cartes AS "Cartes",
  revu AS "Revue le"
FROM "eco gestion"
WHERE ue
SORT periode ASC, coef DESC
```

## ⚠️ Ce qu'il reste à récupérer

Les fiches dont le cours est incomplet. Une ligne ici = du contenu qui manque, pas une fiche mal écrite.

```dataview
TABLE WITHOUT ID
  file.link AS "Fiche",
  a_verifier AS "Points à vérifier",
  revu AS "Relevé le"
FROM "eco gestion"
WHERE a_verifier > 0
SORT a_verifier DESC
```

## 📓 Notes d'amphi en attente

Tout ce qui est déposé ici est mis en fiche au prochain passage de `/eco`, en priorité sur le reste.

```dataview
LIST WITHOUT ID file.link + " — " + file.size + " o, modifié le " + dateformat(file.mtime, "dd/MM")
FROM "eco gestion/_brut"
SORT file.mtime DESC
```

## 📚 Le reste du dossier

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  statut AS "Statut",
  revu AS "Dernière revue"
FROM "eco gestion"
WHERE !ue
  AND !contains(file.folder, "_brut")
  AND file.name != "_Accueil - mes cours"
SORT revu ASC, file.name ASC
```

## ✅ Ce qui reste à cocher

Les cases non faites des pages de cycle et des fiches d'exercices.

```dataview
TASK
FROM "eco gestion"
WHERE !completed AND !contains(file.folder, "_brut")
GROUP BY file.link
LIMIT 10
```

---

> [!question]- Comment ça marche, derrière
> Le skill `/eco` passe toutes les heures sur une page : il corrige, met en forme de fiche (essentiel, paires à ne pas confondre, méthode, cartes Anki, contrôle à réponses repliées) et **signale les trous sans les combler**. Il tient les champs `revu`, `a_verifier` et `cartes` du frontmatter — c'est ce qui alimente les tableaux ci-dessus.
>
> Un passage = un commit git. Si une page disparaît du vault (déjà arrivé le 7 septembre 2026, la synchro a vidé le dossier), elle se récupère avec `python3 .claude/skills/eco/restaure.py --applique`.
