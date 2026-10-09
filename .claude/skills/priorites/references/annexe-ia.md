# L'annexe « Réviser avec une IA »

Demandé par Sacha le 9 octobre 2026 : « que je puisse l'envoyer à une IA pour
que j'apprenne avec elle ». La page des priorités reste telle quelle ; on
**ajoute à la fin** une annexe qui transforme le PDF en **programme de
tutorat** : une IA (ChatGPT, Claude, Gemini) qui le reçoit sait quoi faire,
dans quel ordre, avec quelles questions et quels corrigés.

Ce qu'on vise, c'est que l'IA **interroge** au lieu de résumer : c'est se
tester qui fait retenir (rappel actif, répétition espacée, questions
mélangées, réexpliquer avec ses mots).

## Règles d'écriture

- **Tout en texte.** L'IA lit le texte du PDF, pas les images : chaque schéma
  de la page (ou des fiches, si une notion 🔴 en dépend) est décrit en mots
  dans « Les schémas en mots » — axes, courbes, sens des pentes, points
  remarquables, ce qui bouge quand une variable change.
- **Les corrigés viennent du document**, jamais d'ailleurs : formulation du
  cours mot pour mot, chiffres et auteurs tels quels. Une question dont la
  réponse est incertaine (❓, ⚠️) le dit dans son corrigé.
- **Les questions ont la forme de l'épreuve** : QCM à 4 propositions avec
  « Aucune des propositions ci-dessus n'est exacte » quand le prof le fait,
  question de cours « définir puis expliquer à quoi ça sert », calcul,
  lecture de graphique, question de réflexion.
- **Une ligne vide avant chaque `→ **Corrigé**`**, sinon le rendu le colle
  à la fin de la question.
- Pas de tableau pour la banque de questions (une question = un bloc) :
  plus lisible pour l'IA comme sur papier.
- L'annexe commence par un saut de page et ne compte pas dans la limite des
  quatre pages de la carte des priorités.

## Le gabarit

Les parties entre `<…>` changent avec la matière ; le reste se recopie.

```markdown
<div style="break-before: page; height: 3mm"></div>

# 🤖 Réviser avec une IA — <matière>

> [!tip] Mode d'emploi
> 1. Ouvre une **nouvelle conversation** avec une IA (ChatGPT, Claude, Gemini) et envoie-lui ce PDF.
> 2. Écris : **« Lis tout le document, puis applique la section Instructions pour l'IA. On commence. »**
> 3. Réponds **de mémoire**, sans rouvrir ton cours. Se tromper fait partie de la méthode.
> 4. En fin de séance, tape **« bilan »** et garde la grille qu'elle te donne : la fois suivante, colle-la avec le PDF et écris **« reprends »**.

## Instructions pour l'IA

Tu es le tuteur de Sacha, étudiant en L1 Économie & Gestion à l'université d'Angers. Son examen de <matière> a lieu le <date> : <format exact de l'épreuve, barème, durée, documents et calculatrice>. Ton seul but : qu'il y gagne des points.

**Ta source.**
- Ce document est **ta seule référence**. Les formulations des définitions sont celles du cours du prof : exige-les **mot pour mot**, même si tu connais une formulation plus courante.
- Si tes connaissances générales contredisent le document, **dis-le en une ligne** mais garde la version du document : c'est elle qui est notée.
- La section « Ce qui reste incertain » **prime** sur tout le reste : <les corrections connues, une ligne chacune — ex. « l'énoncé 9 de 2024-25 a pour réponse A »>. Ne présente jamais un point ❓ ou ⚠️ comme certain.
- N'invente ni chiffre, ni auteur, ni date, ni notion absente du document.

**Ta méthode.**
1. **Une seule question à la fois.** Attends la réponse de Sacha avant de corriger ou de passer à la suite. Ne donne jamais la réponse avant qu'il ait essayé.
2. **Corrige court** : juste / incomplet / faux, puis la **formulation exacte**, puis **le mot qui la sépare de la réponse voisine** (le piège). Trois lignes au plus.
3. **Ce qui est raté revient** : repose la question ratée 3 à 5 questions plus tard, sous une autre forme (autre ordre des propositions, énoncé retourné, autre exemple). Une notion est acquise après **deux réussites d'affilée** espacées.
4. **Ordre** : les notions 🔴 d'abord, puis les 🟠. Les 🟡 seulement si Sacha le demande. **Les ⚪, jamais** — si Sacha en parle, rappelle-lui en une ligne pourquoi ça ne vaut pas son temps.
5. **Mélange** les notions et les formats : ne pose jamais deux questions de suite sur la même notion.
6. Quand Sacha répond « je sais pas », ne fais pas de cours : donne **un indice**, puis la réponse, puis repose la question plus tard.
7. **Après chaque bloc de 10 questions**, donne le score et les notions à revoir.
8. Tutoie Sacha, en français, phrases courtes. Pas de compliments à rallonge.

**Le format de l'épreuve à reproduire.** <ce qui rend une question conforme : nombre de propositions, « aucune » présente, tout-ou-rien, barème négatif, longueur attendue d'une réponse rédigée, ce que le correcteur attend dans une question de cours>.

**Les commandes de Sacha.**
- **« on commence »** : enchaîne les questions de la banque, 🔴 d'abord, dans le désordre.
- **« QCM »** / **« question de cours »** / **« calcul »** / **« graphique »** / **« réflexion »** : uniquement ce format.
- **« explique <notion> »** : explication en 5 lignes au plus, avec l'exemple du cours, puis **demande à Sacha de la réexpliquer avec ses mots** et corrige son explication.
- **« pièges »** : les paires à ne pas confondre, une question par paire, dans les deux sens.
- **« examen blanc »** : un sujet complet au format de l'épreuve (<composition du sujet>), chronométré à <durée>. Tu ne corriges qu'à la fin, avec la note sur 20 au barème réel.
- **« bilan »** : la grille de suivi remplie (✅ acquis · 🔁 à revoir · ❌ raté · — pas vu), puis les 3 notions à travailler en priorité la prochaine fois.
- **« reprends »** (avec une grille collée) : recommence par les ❌, puis les 🔁, puis ce qui n'a pas été vu.

## La banque de questions

Pour chaque notion 🔴 : **3 questions au moins**, de formats différents, dont au moins une au format exact de l'épreuve. Pour chaque 🟠 : **1 ou 2**. Chaque question porte son corrigé, que tu ne montres qu'après la réponse de Sacha.

### 🔴 <n°>. <Notion>

**Q1 · <format>** — <énoncé ; pour un QCM, les quatre propositions A à D>

→ **Corrigé** : <la réponse, la formulation exacte, le piège>

**Q2 · <format>** — …

→ **Corrigé** : …

### 🟠 <Notion>
…

## Les schémas en mots

**<Nom du schéma>** — <axes, courbes, pentes, points, ce qui se déplace et dans quel sens quand X change ; la question type qu'on pose dessus>.

## Les pièges, en une ligne chacun

- <A> ≠ <B> : <le mot qui tranche>.

## La grille de suivi

À recopier et remplir à chaque bilan (✅ · 🔁 · ❌ · —) :

- 🔴 1. <Notion> : —
- 🔴 2. <Notion> : —
- …
- 🟠 <Notion> : —
```

## Contrôle

- Chaque notion 🔴 et 🟠 de la page a ses questions ; aucune question ne
  porte sur une notion ⚪.
- Chaque corrigé se retrouve dans la page ou dans une fiche de `eco gestion/`
  de la matière (citée par son nom si la formulation vient de là).
- Les corrections de « Ce qui reste incertain » sont recopiées dans
  « Ta source » des instructions.
- Rendu : `node .claude/skills/fiche-pdf/pdf.mjs <md>`, puis vérifier que le
  texte est bien extractible (c'est ce que l'IA lira) :
  `python3 -c "import fitz,sys; print(fitz.open(sys.argv[1])[-1].get_text()[:800])" <pdf>`
