---
type: moc
tags: [moc, sordulo, devis]
---

# Devis & Factures — Sordulo

> Sordulo = 2 micro-entreprises. Chaque devis est rattaché à **une** des deux.
> Rangement : `DEVIS-FACTURES/{micro}/{CLIENT}/` — d'abord par **micro** (unité fiscale : numérotation + déclarations URSSAF par micro), puis un **sous-dossier par client**. Crée une fiche depuis [[Template-Devis]]. La fiche client (`SORDULO/CLIENT/`) ne **stocke pas** les PDF, elle les **relie**.

## Suivi global

| Numéro | Client | Micro | Montant HT | Statut | Émis | Payé |
| --- | --- | --- | --- | --- | --- | --- |
| [[Devis Wanafoot 2026-01\|Devis 2026-01]] | [[_WANAFOOT\|Wanafoot]] | Maël Auzenet | 2 900 € | Envoyé (à confirmer) | 21/06/2026 | — |
| [[Devis RAW STUDIO Site-Portfolio 2026-001\|Devis 2026_001]] | [[_RAW-STUDIO\|RAW-STUDIO]] | Maël Auzenet | 2 925 € | Facturé (cf. Facture 2026-001) | 18/01/2026 | — |
| [[Facture RAW STUDIO 2026-001\|Facture 2026_001]] | [[_RAW-STUDIO\|RAW-STUDIO]] | Maël Auzenet | 2 500 € | Envoyée | 10/02/2026 | — |
| [[Devis Maison Terracotta 2026-004\|Devis 2026_004]] | [[_MAISON-TERRACOTTA\|Maison Terracotta]] | Maël Auzenet | 3 800 € | Envoyé (à confirmer) | 04/03/2026 | — |
| [[Devis Maison Terracotta 2026-006\|Devis 2026_006]] | [[_MAISON-TERRACOTTA\|Maison Terracotta]] | Maël Auzenet | 2 500 € | Envoyé (à confirmer) | 04/03/2026 | — |
| [[Devis RAW STUDIO Drive 2026-005\|Devis 2026_005]] | [[_RAW-STUDIO\|RAW-STUDIO]] | Maël Auzenet | 1 200 € | Envoyé (à confirmer) | 28/03/2026 | — |
| [[Devis RAW STUDIO App 2026-007\|Devis 2026_007]] | [[_RAW-STUDIO\|RAW-STUDIO]] | Sacha Moricet | 4 900 € | Envoyé (à confirmer) | 06/05/2026 | — |

> Maison Terracotta a reçu **deux propositions alternatives** (même client, même date): 2026_004 (complet, 5 modules) **ou** 2026_006 (allégé, 3 modules). Une seule sera retenue.

> Astuce : avec le plugin **Dataview**, ce tableau peut se remplir tout seul à partir des fiches devis.

## Sacha-Moricet
`SORDULO/DEVIS-FACTURES/Sacha-Moricet/{CLIENT}/` — devis/factures émis par la micro **Sacha Moricet**.
- `RAW-STUDIO/` — devis 2026_007 (application mobile React Native)

## Maël-Auzenet
`SORDULO/DEVIS-FACTURES/Mael-Auzenet/{CLIENT}/` — devis/factures émis par la micro **Maël Auzenet**.
- `MAISON-TERRACOTTA/` — devis 2026_004 (complet) & 2026_006 (allégé)
- `RAW-STUDIO/` — devis 2026_001 (site portfolio) → facture 2026_001 · devis 2026_005 (drive)
- `WANAFOOT/` — devis 2026_01 (mobile foot)

---
[[_SORDULO|← Sordulo]] · [[ACCUEIL|Accueil]]
