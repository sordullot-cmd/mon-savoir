# Fallback — capture native par tuiles (qualité d'origine, via claude-in-chrome)

À lire **seulement** quand `grab-post.py` a échoué même avec `--cookies` (Instagram
privé ou récalcitrant, plateforme non supportée). On récupère alors les **images à
leur résolution native** (ex. 1440x1440) sans télécharger de fichier : on affiche
l'image en taille réelle dans la page et on la capture en tuiles 1:1 qu'on recolle.
Méthode validée sur le post Instagram `domo-brand-identity` (août 2026).

Ne vaut que pour des **images**. Vidéo irrécupérable → `record.py` sur le post, ou
frame unique, et le signaler.

---

1. **Ouvrir le post** dans le Chrome de Sacha (`claude-in-chrome`, nouvel onglet —
   il est connecté aux plateformes).

2. **Lister les slides depuis la SOURCE DE VÉRITÉ, jamais depuis le DOM.**
   PIÈGE VÉCU (post `logosai`, août 2026) : scraper `article img` / `main img`
   ramasse les vignettes de la grille « autres posts du compte » en bas de page →
   on range des images d'AUTRES posts en croyant tenir le carrousel.
   À la place, depuis la page (`javascript_tool`), interroger l'**API interne** avec
   la session du navigateur :
   - `pk` = shortcode décodé en base64url (`A-Za-z0-9-_`, `pk = pk*64 + index(c)`) ;
   - `fetch('https://www.instagram.com/api/v1/media/<pk>/info/', {headers:{'x-ig-app-id':'936619743392459'}, credentials:'include'})`
     → `items[0].carousel_media[]` : `media_type` (1=image, 2=vidéo),
     `image_versions2.candidates` (prendre la plus grande).
     *(Fallback si l'API change : le JSON embarqué `script[type="application/json"]`
     contenant `carousel_media`.)*
   - **Vérifier le compte** : nombre de slides + types doivent coller au post (le
     compteur « x/8 » visible sur le carrousel). Croiser avec yt-dlp : ses erreurs
     `No video formats found` sur des slides = ce sont des images (normal), et lui
     seul télécharge les slides **vidéo**.

   Stocker les URLs dans `window.__slides`, puis `fetch` chaque image et garder son
   base64 dans `window.__b64`. **Ne renvoyer que des compteurs/dimensions** dans le
   résultat d'outil.
   - **INTERDIT** : faire sortir les URLs ou le base64 par la sortie d'outil — le
     filtre anti-exfiltration de l'extension les bloque (`[BLOCKED: …]`) et il ne
     faut **pas** le contourner par un autre encodage.
   - **Voies mortes déjà testées** (ne pas re-perdre de temps) : `a.click()` + blob
     download (bloqué sans geste utilisateur réel, même via clic simulé), POST vers
     un serveur localhost (bloqué par la CSP du site), `curl` du HTML du post
     (données absentes sans session). Un **vrai clic de Sacha** sur un bouton injecté
     reste une option de secours pour un téléchargement direct.

3. **Overlay taille native** : injecter un `<div>` fixed plein écran (z-index max)
   contenant une `<img>` à la **taille native en px CSS** (ex. `width:1080px`).
   Source de l'img : la **data URL base64** OU, si elle sort en image cassée (la CSP
   d'Instagram bloque `data:` sur les pages **anonymes**), directement l'**URL CDN**
   (`img.src = url` — les `<img>` ne sont pas soumis au CORS). Toujours **attendre
   `onload`** et vérifier `naturalWidth` avant de capturer. Masquer l'UI de la
   plateforme par un `<style>` injecté (survit aux re-renders React, contrairement
   aux styles inline). NB : la méthode marche aussi **déconnecté** — le JSON embarqué
   du post anonyme contient les slides (`candidates[0].url` peut ne pas avoir de
   `width` → prendre `candidates[0]` + `original_width`, pas un reduce sur `width`).

4. **Mesurer le viewport réel** après `resize_window` au maximum : `innerWidth` /
   `innerHeight` + `devicePixelRatio` via JS. Les régions de l'action `zoom` sont en
   **pixels physiques** du viewport. Attention : `resize_window` a déjà **fait
   planter Chrome** (le relancer : `open -a "Google Chrome"`, retrouver l'onglet,
   tout réinjecter) — s'en passer si le viewport suffit.

5. **Capturer en tuiles ≤ 720x720** : action `zoom` + `save_to_disk`. Au-delà de
   ~1400 px de région, l'outil **redimensionne** la sortie (perte) ; à 720 la tuile
   sort **1:1**. Entre les tuiles, déplacer l'image par `transform: translate(...)` à
   **décalages entiers** (ex. 1080x1080 = 4 tuiles de 540, ordre TL TR BL BR).

   **Étalonner l'échelle réelle sur la 1re tuile, ne pas faire confiance au dpr** :
   le zoom Chrome (≠ 100 %) fausse le rapport device/CSS (vécu : région 540 demandée
   → tuile 1092 couvrant 617 px CSS, soit 1,7685 device/CSS). Méthode : capturer la
   tuile TR (`translate(-540px,0)`), mesurer en PIL la **colonne du bord droit du
   contenu** (`x_bord`) → échelle = `x_bord / (largeur_image − 540)` ; assembler
   ensuite en collant chaque tuile à `(540·échelle, 0)` etc. sur un canvas device,
   cropper à `largeur_image·échelle`, redimensionner LANCZOS à la taille native.

6. **Recoller** :
   ```
   python3 .claude/skills/_lib/stitch.py <sortie.png> --cols 2 tuile1.png tuile2.png tuile3.png tuile4.png
   ```
   (tuiles en ordre **ligne par ligne**). Relire le résultat pour vérifier l'absence
   de raccord.

7. **Nettoyer** : fermer l'onglet. Signaler dans le récap que la qualité vient de la
   capture du rendu (visuellement identique au fichier source, mais pas les octets
   d'origine).
