#!/bin/bash
# Un passage horaire de /eco, lancé par le LaunchAgent com.sacha.eco-fiches.
#
#   .claude/skills/eco/passage.sh            # un passage
#   .claude/skills/eco/passage.sh --relance  # rattrape même si rien n'a bougé
#
# Le script fait lui-même le snapshot et le choix de la page : le modèle n'a
# donc besoin ni de `cp`, ni d'écrire hors du vault (les deux étaient refusés
# par les permissions en mode headless).
#
# Le script pousse lui-meme sur GitHub a la fin, si le passage a commite :
# c'est plus sur que de le demander au modele, et ca evite de lui ouvrir
# `git push`. Le .gitignore protege « eco gestion/fichier/ » (photos, PDF).
#
# Journal : .claude/skills/eco/passages.log

set -u
VAULT="/Users/account/Documents/brain^2"
CLAUDE="/Users/account/.local/bin/claude"
SKILL="$VAULT/.claude/skills/eco"
LOG="$SKILL/passages.log"
VERROU="$SKILL/.verrou"
SNAP="$SKILL/scratch"

cd "$VAULT" || exit 1

# Un seul passage à la fois : mkdir est atomique, contrairement à un test -f.
if ! mkdir "$VERROU" 2>/dev/null; then
  # Verrou de plus d'une heure = passage précédent mort, on le casse.
  if [ -n "$(find "$VERROU" -maxdepth 0 -mmin +60 2>/dev/null)" ]; then
    rmdir "$VERROU" 2>/dev/null && mkdir "$VERROU" 2>/dev/null || exit 0
  else
    echo "$(date '+%F %H:%M')  passage déjà en cours, sauté" >> "$LOG"
    exit 0
  fi
fi
trap 'rmdir "$VERROU" 2>/dev/null' EXIT

# Rien à faire → on n'allume pas le modèle pour rien.
PAGE=$(python3 "$SKILL/etat.py" --suivant ${1:-} 2>/dev/null | head -1)
if [ "$PAGE" = "rien" ] || [ -z "$PAGE" ] || [ ! -f "$VAULT/$PAGE" ]; then
  echo "$(date '+%F %H:%M')  rien à faire" >> "$LOG"
  exit 0
fi

# Snapshot : le filet de sécurité, pris avant que le modèle démarre.
mkdir -p "$SNAP"
AVANT="$SNAP/avant.md"
cp "$VAULT/$PAGE" "$AVANT" || exit 1

echo "$(date '+%F %H:%M')  passage sur : $PAGE" >> "$LOG"

TETE_AVANT=$(git rev-parse HEAD 2>/dev/null)

"$CLAUDE" -p "/eco passage automatique horaire.

Page à traiter : « $PAGE » — c'est etat.py --suivant qui l'a désignée, ne le rappelle pas.
Snapshot déjà pris : « $AVANT » — ne refais pas de copie, sers-t'en pour verifie.py.

Traite cette seule page, vérifie, acte avec etat.py --enregistre, commite la page
et etat.json, puis arrête-toi." \
  --permission-mode acceptEdits \
  --allowedTools "Read" "Write" "Edit" "Glob" "Grep" "Skill" \
    "Bash(python3 .claude/skills/eco/etat.py:*)" \
    "Bash(python3 .claude/skills/eco/verifie.py:*)" \
    "Bash(cp:*)" \
    "Bash(git add:*)" "Bash(git commit:*)" "Bash(git status:*)" \
    "Bash(git show:*)" "Bash(git diff:*)" "Bash(git checkout:*)" \
  >> "$LOG" 2>&1

# ---------------------------------------------------------------- push
# Sacha l'a demande le 8 septembre 2026 : un passage se termine sur GitHub,
# pas sur le disque. On ne pousse que si le modele a reellement commite.
TETE_APRES=$(git rev-parse HEAD 2>/dev/null)

if [ "$TETE_AVANT" = "$TETE_APRES" ]; then
  echo "$(date '+%F %H:%M')  rien de commite, pas de push" >> "$LOG"
elif git push --quiet origin main >> "$LOG" 2>&1; then
  echo "$(date '+%F %H:%M')  pousse -> origin/main ($TETE_APRES)" >> "$LOG"
else
  # Rejet le plus courant : quelqu'un a pousse entre-temps. On rejoue notre
  # commit par-dessus, une seule fois. En cas de conflit on abandonne le
  # rebase et on laisse le commit local : il partira au passage suivant.
  echo "$(date '+%F %H:%M')  push refuse, tentative de rebase" >> "$LOG"
  if git pull --rebase --quiet origin main >> "$LOG" 2>&1 \
     && git push --quiet origin main >> "$LOG" 2>&1; then
    echo "$(date '+%F %H:%M')  pousse apres rebase" >> "$LOG"
  else
    git rebase --abort 2>/dev/null
    echo "$(date '+%F %H:%M')  push impossible, le commit reste local" >> "$LOG"
  fi
fi

echo "$(date '+%F %H:%M')  fin du passage" >> "$LOG"
