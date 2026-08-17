#!/usr/bin/env python3
"""Récupère le(s) média(s) d'un post social (X/Twitter, Instagram, Pinterest, TikTok,
Behance, Dribbble, Tumblr, Bluesky, YouTube, Vimeo…) + ses métadonnées.

Stratégie : gallery-dl (images/galeries, aussi vidéos X) et yt-dlp (plateformes vidéo),
avec bascule automatique de l'un à l'autre si le premier échoue. Les fichiers sont
renommés proprement (post.jpg, post-2.jpg, post.mp4…) dans le dossier de destination.

Usage : grab-post.py <url> <dossier_destination> [--cookies] [--timeout S]

--cookies : utilise les cookies du Chrome de la session (--cookies-from-browser chrome).
            Nécessaire pour Instagram et parfois X (posts derrière login). Sur macOS,
            peut déclencher UNE demande d'accès au trousseau (« Chrome Safe Storage »).

Sortie : JSON sur stdout — plateforme, outil utilisé, fichiers (renommés), meta
(auteur, texte, date, titre), erreurs éventuelles + conseil de relance.
"""
import sys, os, re, json, glob, shutil, argparse, subprocess, tempfile
from urllib.parse import urlparse

IMG_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"}
VID_EXT = {".mp4", ".webm", ".mov", ".mkv", ".m4v"}

PLATFORMS = [
    (r"(?:^|\.)((twitter|x)\.com)", "x"),
    (r"(?:^|\.)instagram\.com", "instagram"),
    (r"(?:^|\.)(pinterest\.\w+|pin\.it)", "pinterest"),
    (r"(?:^|\.)tiktok\.com", "tiktok"),
    (r"(?:^|\.)behance\.net", "behance"),
    (r"(?:^|\.)dribbble\.com", "dribbble"),
    (r"(?:^|\.)tumblr\.com", "tumblr"),
    (r"(?:^|\.)bsky\.app", "bluesky"),
    (r"(?:^|\.)threads\.(net|com)", "threads"),
    (r"(?:^|\.)(youtube\.com|youtu\.be)", "youtube"),
    (r"(?:^|\.)vimeo\.com", "vimeo"),
    (r"(?:^|\.)(are\.na)", "arena"),
    (r"(?:^|\.)savee\.it", "savee"),
    (r"(?:^|\.)cosmos\.so", "cosmos"),
]
# Plateformes où yt-dlp est meilleur en premier (contenu vidéo)
VIDEO_FIRST = {"youtube", "vimeo", "tiktok"}


def detect_platform(url):
    host = (urlparse(url).hostname or "").lower()
    for pattern, name in PLATFORMS:
        if re.search(pattern, host):
            return name
    return "autre"


def run(cmd, timeout):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except subprocess.TimeoutExpired:
        return -1, f"timeout après {timeout}s"
    except FileNotFoundError:
        return -2, f"outil introuvable : {cmd[0]}"


def try_gallery_dl(url, tmp, cookies, timeout):
    cmd = ["gallery-dl", "-D", tmp, "--write-metadata", url]
    if cookies:
        cmd[1:1] = ["--cookies-from-browser", "chrome"]
    return run(cmd, timeout)


def try_yt_dlp(url, tmp, cookies, timeout):
    cmd = ["yt-dlp", "--no-playlist", "--write-info-json",
           "-o", os.path.join(tmp, "%(id)s.%(ext)s"), url]
    if cookies:
        cmd[1:1] = ["--cookies-from-browser", "chrome"]
    return run(cmd, timeout)


def collect_meta(tmp):
    """Fusionne les métadonnées des .json écrits par gallery-dl / yt-dlp."""
    meta = {}
    for j in sorted(glob.glob(os.path.join(tmp, "*.json"))):
        try:
            with open(j, encoding="utf-8") as f:
                d = json.load(f)
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        for k_out, keys in [
            ("auteur", ["uploader", "username", "account", "channel", "blog_name", "author_name"]),
            ("texte", ["content", "description", "caption", "text", "title"]),
            ("titre", ["title", "fullTitle", "grid_title"]),
            ("date", ["upload_date", "date", "timestamp", "created_at"]),
            ("likes", ["like_count", "favorite_count", "likes", "appreciations"]),
        ]:
            if meta.get(k_out) in (None, ""):
                for k in keys:
                    v = d.get(k)
                    if isinstance(v, dict):
                        v = v.get("name") or v.get("nick") or v.get("full_name")
                    if v not in (None, "", []):
                        meta[k_out] = str(v)[:500] if k_out == "texte" else v
                        break
        # auteur en dict (gallery-dl twitter: author={name,nick})
        a = d.get("author") or d.get("user") or d.get("owner")
        if isinstance(a, dict) and not meta.get("auteur"):
            meta["auteur"] = a.get("name") or a.get("nick") or a.get("username") or a.get("full_name")
    return {k: v for k, v in meta.items() if v not in (None, "")}


def rename_media(tmp, dest):
    """Déplace les médias de tmp vers dest avec des noms propres post[-N].ext."""
    media = []
    for f in sorted(glob.glob(os.path.join(tmp, "**", "*"), recursive=True)):
        ext = os.path.splitext(f)[1].lower()
        if os.path.isfile(f) and ext in IMG_EXT | VID_EXT:
            media.append(f)
    out = []
    for i, src in enumerate(media, 1):
        ext = os.path.splitext(src)[1].lower()
        name = "post" + ("" if len(media) == 1 else f"-{i}") + ext
        target = os.path.join(dest, name)
        n = 2
        while os.path.exists(target):  # jamais écraser
            target = os.path.join(dest, f"post-{i}-{n}{ext}")
            n += 1
        shutil.move(src, target)
        out.append({"fichier": os.path.basename(target),
                    "type": "video" if ext in VID_EXT else "image",
                    "octets": os.path.getsize(target)})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("dest")
    ap.add_argument("--cookies", action="store_true",
                    help="cookies du Chrome de la session (Instagram, X derrière login)")
    ap.add_argument("--timeout", type=int, default=180)
    a = ap.parse_args()

    platform = detect_platform(a.url)
    os.makedirs(a.dest, exist_ok=True)
    erreurs, outil = [], None

    with tempfile.TemporaryDirectory() as tmp:
        tools = [("yt-dlp", try_yt_dlp), ("gallery-dl", try_gallery_dl)] \
            if platform in VIDEO_FIRST else \
            [("gallery-dl", try_gallery_dl), ("yt-dlp", try_yt_dlp)]

        for name, fn in tools:
            code, log = fn(a.url, tmp, a.cookies, a.timeout)
            has_media = any(os.path.splitext(f)[1].lower() in IMG_EXT | VID_EXT
                            for f in glob.glob(os.path.join(tmp, "**", "*"), recursive=True))
            if has_media:
                outil = name
                break
            # garder la fin du log (l'erreur utile y est en général)
            erreurs.append({name: log.strip().splitlines()[-3:] if log.strip() else f"code {code}"})

        meta = collect_meta(tmp)
        fichiers = rename_media(tmp, a.dest)

    result = {"plateforme": platform, "outil": outil, "fichiers": fichiers, "meta": meta}
    if not fichiers:
        result["erreurs"] = erreurs
        blob = json.dumps(erreurs, ensure_ascii=False).lower()
        if not a.cookies and any(k in blob for k in
                                 ("login", "log in", "auth", "cookie", "rate-limit", "403", "401", "private")):
            result["conseil"] = "relancer avec --cookies (session Chrome) — le post semble derrière un login"
        else:
            result["conseil"] = ("téléchargement impossible → fallback : screenshot du post via le "
                                 "Chrome de Sacha (claude-in-chrome), il est connecté aux plateformes")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
