# Publier — étape finale commune à tous les skills qui écrivent dans le vault

Appelée à la fin de `/inspi`, `/univers`, `/ranger`, `/font` — et de toute
intervention qui crée ou modifie une fiche, un index ou un média du vault.

Deux dépôts, dans cet ordre. **Rien ici n'est bloquant** : un échec se signale
dans le récap, il ne transforme pas un run réussi en run raté.

---

## 1. Régénérer l'index du site

```bash
npm run index --prefix ~/Documents/GitHub/vault-gallery
```

Le site déployé n'a **pas** accès au vault local : il lit l'index et les médias
**commités dans son dépôt**. Cette commande copie l'un et l'autre depuis le vault.
Elle doit donc tourner **avant** le commit du site, jamais après.

## 2. Pousser le vault

```bash
cd ~/Documents/brain^2
git add -A
git commit -m "<message>"
git push
```

Dépôt `sordulocontact-ux/KNOWLEDGE`, branche `main`. C'est l'archive du second
cerveau — on commite sur `main`, pas de branche.

## 3. Pousser le site → Vercel déploie

```bash
cd ~/Documents/GitHub/vault-gallery
git add -A
git commit -m "<message>"
git push
```

Dépôt `sordullot-cmd/brain-2`, branche `main`. **Le push suffit** : Vercel est
branché sur le dépôt Git et redéploie tout seul. Pas de CLI `vercel`, pas de
`vercel --prod`. `vercel.json` lance `vite build` seul, sans réindexer — d'où
l'ordre imposé à l'étape 1.

---

## Messages de commit

Décrire **ce qui est entré dans le vault**, pas la commande lancée.

- vault : `/inspi yazio — dossier app complet (branding Koto, paywalls 2023-2026)`
- site : `maj de l'index — yazio`

Terminer chaque message par :

```
Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
```

## À dire dans le récap

Une ligne : les deux commits (ou celui qui a échoué et pourquoi), et le fait que
Vercel redéploie. Si un `git push` casse — pas de réseau, conflit avec une autre
session, dépôt trop gros — **le dire**, ne pas le passer sous silence.

## Garde-fous

- **Ne jamais `git push --force`**, ni réécrire l'historique. Plusieurs sessions
  peuvent travailler sur ces dépôts en même temps : en cas de rejet, faire un
  `git pull --rebase` et repousser, ou signaler le conflit.
- **Ne rien supprimer pour faire de la place.** Si un push échoue sur la taille,
  le remonter à Sacha — c'est sa décision, pas un ménage à faire seul.
- Si `npm run index` échoue, **pousser quand même le vault** (le contenu est le
  plus important) et signaler que le site n'a pas été mis à jour.

## Point de vigilance — la taille

`public/media/` du site est une **copie** des médias du vault : chaque dossier
`/inspi` ou `/univers` est donc stocké et poussé **deux fois**, dans deux dépôts.
Le README du site tablait sur ≈ 6,5 Mo ; on est aujourd'hui **très au-delà**.
Quand ça deviendra un problème (limites GitHub, poids du déploiement Vercel), les
deux issues déjà identifiées sont : ne publier qu'une partie des dossiers, ou
passer les médias sur un stockage externe. À arbitrer avec Sacha, pas à trancher
en cours de run.
