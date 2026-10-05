#!/bin/bash
# Remet le site a jour apres un changement de cours, et le pousse.
# Demande de Sacha le 5 octobre 2026 : chaque cours ajoute ou modifie part sur
# git automatiquement — le vault, et le site qui le publie sur /cours.
#
#   bash .claude/skills/eco/site.sh            # a la main, apres un push du vault
#   (appele aussi par passage.sh quand un passage a commite)
#
# Ne touche QUE public/ : le code du site peut avoir des modifications en cours
# qui ne sont pas les notres. Ce que le .gitignore du vault tient prive (notes de
# camarades, PDF de _brut/) est ecarte par l'indexeur lui-meme.

SITE="${SITE_PATH:-$HOME/Documents/GitHub/vault-gallery}"
LOG="${1:-/dev/stdout}"
horo() { date '+%F %H:%M'; }

cd "$SITE" 2>/dev/null || { echo "$(horo)  site introuvable : $SITE" >> "$LOG"; exit 0; }

if ! npm run --silent index >> "$LOG" 2>&1; then
  echo "$(horo)  site : l'index a echoue, rien de pousse" >> "$LOG"
  exit 0
fi

git add -A public/vault.json public/vault-notes.json public/vault-cartes.json public/media public/derived 2>> "$LOG"
if git diff --cached --quiet; then
  echo "$(horo)  site : rien n'a change" >> "$LOG"
  exit 0
fi

git commit --quiet -m "index: cours d'eco mis a jour depuis le vault ($(date '+%F %H:%M'))" >> "$LOG" 2>&1

if git push --quiet origin main >> "$LOG" 2>&1; then
  echo "$(horo)  site : pousse ($(git rev-parse --short HEAD))" >> "$LOG"
elif git pull --rebase --quiet origin main >> "$LOG" 2>&1 && git push --quiet origin main >> "$LOG" 2>&1; then
  echo "$(horo)  site : pousse apres rebase" >> "$LOG"
else
  git rebase --abort 2>/dev/null
  echo "$(horo)  site : push impossible, le commit reste local" >> "$LOG"
fi
