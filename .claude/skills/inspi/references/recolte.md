# Récolte multi-sources — protocole des sous-agents

Deux temps, jamais un seul : **l'éventail** (N agents cherchent en parallèle, un par
source) puis **la table ronde** (les résultats sont fusionnés, jugés, éliminés,
classés). Aucun fichier n'entre dans le vault avant la table ronde.

---

## Temps 1 — l'éventail

Composer la liste des sources avec `references/sources.md`, puis lancer **4 à 6
sous-agents en parallèle, un par source, dans UN SEUL message** (sinon ils
s'exécutent en série et on perd tout l'intérêt).

Chaque agent reçoit le contrat ci-dessous, avec `<CIBLE>`, `<SOURCE>` et
`<SCRATCH>` remplis. `<SCRATCH>` = `<scratchpad>/recolte/<source>/`, propre à cet
agent : deux agents n'écrivent jamais dans le même dossier.

### Contrat (à copier dans le prompt de chaque agent)

```
Tu es l'agent « <SOURCE> » d'une récolte multi-sources sur : <CIBLE>.
Tu es le SEUL à couvrir cette source. Un autre agent couvre chacune des autres —
ne va pas sur leur terrain, creuse la tienne à fond.

TA SOURCE : <SOURCE> — <ce qu'on y trouve, comment y entrer, ce qui bloque>

CE QUE TU FAIS
1. Cherche la cible sur ta source (WebSearch/WebFetch ; si login ou anti-bot,
   passe par claude-in-chrome dans le Chrome de Sacha plutôt que d'insister).
2. Pour chaque trouvaille, OUVRE la page et REGARDE avant de la retenir.
3. Télécharge les médias retenus dans <SCRATCH> UNIQUEMENT. Jamais dans le vault :
   c'est la table ronde qui décide de ce qui y entre.
4. Nomme d'après ce que l'image MONTRE (paywall-annuel.png), pas d'après l'URL.

RÈGLES DURES
- Pleine qualité obligatoire : jamais une vignette si l'original existe (chercher
  le lien « original / download / view full size », le CDN sans paramètre de
  resize, ou le `=s0` / `@2x` de la plateforme).
- Aucune URL inventée : tout lien que tu rapportes, tu l'as ouvert.
- Un média qui ressemble à ce qu'une autre source aura forcément (l'icône, le logo
  principal) n'est pas ta valeur ajoutée — rapporte ce qu'on ne trouve QUE chez toi.
- Ce qui bloque (login, paywall, 403) se REMONTE, ne se contourne pas en douce.
- 25 médias maximum. Au-delà, choisis.

CE QUE TU RENDS — uniquement ce JSON, rien d'autre :
{
  "source": "<SOURCE>",
  "cible_confirmee": "nom exact trouvé sur la source, ou null si tu n'as pas trouvé",
  "trouvailles": [
    {"fichier": "<SCRATCH>/nom.png",   // null si tu n'as pas pu télécharger
     "url_page": "page où tu l'as vu",
     "url_media": "URL directe du fichier",
     "montre": "une ligne : ce que l'image montre vraiment",
     "aspect": "ecrans|flows|branding|couleurs|composants|animations|marketing|process",
     "resolution": "1290x2796 ou null",
     "credit": "designer/studio si la source le donne, sinon null",
     "unique": true,   // introuvable ailleurs selon toi
     "confiance": "haute|moyenne|faible"}
  ],
  "signaux": ["faits utiles à la fiche : année de refonte, agence, typo citée, palette annoncée…"],
  "bloque": ["ce que tu n'as pas pu atteindre et pourquoi"],
  "vide": false   // true si ta source n'a rien sur cette cible (réponse parfaitement valable)
}
```

**« vide: true » est un bon résultat.** Un agent qui ne trouve rien et le dit vaut
mieux qu'un agent qui ramène du hors-sujet pour ne pas rentrer les mains vides.

---

## Temps 2 — la table ronde

### 2a. Fusion mécanique (fait par l'orchestrateur, pas par un agent)

1. **Dédup par média** : même visuel chez deux sources → garder **la meilleure
   résolution**, et créditer **les deux** provenances dans la fiche.
2. **Planche de contact de TOUT le butin**, une par aspect :
   ```
   python3 .claude/skills/_lib/planche.py "<scratchpad>/recolte/vu-<aspect>.png" \
       "<scratchpad>/recolte/*/*" --cols 6 --tile 200
   ```
   puis la **lire**. C'est le seul moment où l'on voit vraiment ce qu'on a : doublons,
   vignettes, captures d'écran d'interface au lieu du média, hors-sujet.
3. **Éliminer sans état d'âme** : vignette quand l'original existe, watermark,
   mockup de téléphone quand l'écran à plat existe, recadrage d'un visuel déjà eu,
   image illisible.

### 2b. Le jury (sous-agents, en parallèle, une lentille chacun)

Envoyer aux jurés la **liste fusionnée** (chemin + `montre` + source + résolution)
et les **planches de contact**. Trois lentilles, trois agents :

- **Qualité** — résolution réelle, compression, recadrage, doublons qui restent.
  Verdict par média : garder / remplacer par la version d'une autre source / jeter.
- **Pertinence** — est-ce que ça apprend quelque chose à un designer product/UI/brand ?
  Un écran de plus qui répète le précédent ne vaut pas une ligne dans la fiche.
- **Couverture** — l'inverse des deux autres : **quel aspect n'a rien ?** Pas de
  branding ? Pas un seul flow ? Aucune couleur relevée ? Il désigne les trous et
  propose la source à relancer.

Le juge « couverture » peut **rouvrir l'éventail** : s'il manque un aspect entier,
relancer 1 ou 2 agents ciblés plutôt que de livrer un dossier borgne.

### 2c. Arbitrage et classement (orchestrateur)

- Deux jurés d'accord pour jeter → on jette. Désaccord → l'orchestrateur tranche
  **en regardant l'image**, jamais sur les arguments seuls.
- Chaque média retenu part dans `<slug>/<aspect>/` avec son nom descriptif.
- Chaque média retenu garde sa **provenance** (source + URL) : elle nourrit la section
  `## Sources` de la fiche. Un média sans provenance traçable ne rentre pas.
- Le scratchpad de récolte n'est **pas** nettoyé avant que la fiche soit écrite —
  c'est le seul filet si un juge s'est trompé.

---

## Ce qui se dit dans le récap

- combien d'agents lancés, sur quelles sources ;
- ce que chaque source a **réellement apporté** (et lesquelles étaient vides) ;
- combien de médias récoltés → combien retenus, et **pourquoi** les autres sont partis ;
- les aspects restés vides malgré tout ;
- ce qui a bloqué (login, 403, paywall) — jamais silencieux.
