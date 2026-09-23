---
type: moc
tags: [moc, livres]
---

# Livres

> Ce que je lis, et surtout ce que j'en garde.

**[→ Ajouter un livre](obsidian://quickadd?choice=Ajouter%20un%20livre)** — ou palette de commandes (`Cmd+P`) → « QuickAdd: Ajouter un livre ».
Une fiche par livre, rangée ici, créée depuis [[Template-Livre]]. Ce que j'ai appris va sous `## Ce que j'ai appris`, une idée par ligne : elle remonte toute seule plus bas.

## En cours

```dataview
TABLE WITHOUT ID file.link AS "Livre", auteur AS "Auteur", debut AS "Commencé le"
FROM "LIVRES"
WHERE type = "livre" AND statut = "en cours"
SORT debut DESC
```

## Ce que j'ai appris — les dernières idées

```dataview
TABLE WITHOUT ID L.text AS "Idée", file.link AS "Livre"
FROM "LIVRES"
WHERE type = "livre"
FLATTEN file.lists AS L
WHERE meta(L.section).subpath = "Ce que j'ai appris" AND L.text != ""
SORT file.mtime DESC
LIMIT 20
```

## À appliquer

```dataview
TASK
FROM "LIVRES"
WHERE !completed AND text != "" AND meta(section).subpath = "Ce que je vais appliquer"
GROUP BY file.link
```

## Lus

```dataview
TABLE WITHOUT ID file.link AS "Livre", auteur AS "Auteur", genre AS "Genre", choice(note, note + "/5", "") AS "Note", fin AS "Fini le"
FROM "LIVRES"
WHERE type = "livre" AND statut = "lu"
SORT fin DESC
```

## À lire

```dataview
TABLE WITHOUT ID file.link AS "Livre", auteur AS "Auteur", recommande_par AS "Conseillé par", ajoute AS "Ajouté le"
FROM "LIVRES"
WHERE type = "livre" AND statut = "à lire"
SORT ajoute DESC
```

## Par année

```dataview
TABLE WITHOUT ID annee AS "Année", length(rows) AS "Livres lus", rows.file.link AS "Lesquels"
FROM "LIVRES"
WHERE type = "livre" AND statut = "lu" AND fin
GROUP BY dateformat(date(fin), "yyyy") AS annee
SORT annee DESC
```

---
[[ACCUEIL|← Accueil]]
