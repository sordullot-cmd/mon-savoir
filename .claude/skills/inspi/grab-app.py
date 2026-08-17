#!/usr/bin/env python3
"""grab-app.py — récupère les écrans d'une app en PLEINE QUALITÉ depuis les stores.

Sources publiques, sans login :
  - App Store  → iTunes Search/Lookup API (métadonnées + screenshotUrls) ; le
                 suffixe de redimensionnement est remplacé par `0x0ss.png`
                 → PNG natif (ex. 1290x2796).
  - Google Play→ page details ; les écrans téléphone portent le marqueur
                 `=w526-h296` dans le HTML, retéléchargés en `=s0` (original).

Usage :
    python3 grab-app.py "<nom d'app | URL App Store | URL Play>" <dossier_sortie>
        [--store ios|android|both] [--country fr] [--ipad] [--max N] [--json]

Sortie : les fichiers dans <dossier_sortie>/ecrans/ (+ icone.png) et un JSON de
compte-rendu sur stdout (meta, fichiers, erreurs). Aucune dépendance externe.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
# suffixe de resize mzstatic → original
MZ_RESIZE = re.compile(r"/[0-9]+x[0-9]+(?:bb|ss|w|wa)?\.(?:jpg|png|webp)$", re.I)
PLAY_SHOT = re.compile(r"https://play-lh\.googleusercontent\.com/[\w-]+=w526-h296")
PLAY_ID = re.compile(r"[?&]id=([A-Za-z0-9_.]+)")
ITUNES_ID = re.compile(r"/id(\d+)")


def get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def full_res(url: str) -> str:
    """URL mzstatic de vignette → fichier natif."""
    return MZ_RESIZE.sub("/0x0ss.png", url)


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", (text or "").lower(), flags=re.U)
    return re.sub(r"[\s_-]+", "-", text).strip("-") or "ecran"


def download(url: str, path: str, errors: list) -> str | None:
    try:
        data = get(url, timeout=60)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        errors.append(f"telechargement {url[:80]} : {e}")
        return None
    if len(data) < 2000:
        errors.append(f"fichier suspect (trop petit, {len(data)} o) : {url[:80]}")
        return None
    if data[:4] == b"\x89PNG":
        ext = ".png"
    elif data[:3] == b"\xff\xd8\xff":
        ext = ".jpg"
    elif data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        ext = ".webp"
    else:
        ext = os.path.splitext(urllib.parse.urlparse(url).path)[1] or ".bin"
    path = os.path.splitext(path)[0] + ext
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    return path


# ---------------------------------------------------------------- App Store
def itunes_lookup(query: str, country: str) -> dict | None:
    m = ITUNES_ID.search(query)
    if m:
        url = f"https://itunes.apple.com/lookup?id={m.group(1)}&country={country}&entity=software"
    else:
        term = urllib.parse.quote(query)
        url = f"https://itunes.apple.com/search?term={term}&entity=software&limit=5&country={country}"
    try:
        results = json.loads(get(url)).get("results", [])
    except Exception:
        return None
    return results[0] if results else None


def grab_ios(query: str, outdir: str, country: str, want_ipad: bool, cap: int, report: dict):
    app = itunes_lookup(query, country) or (itunes_lookup(query, "us") if country != "us" else None)
    if not app:
        report["errors"].append(f"App Store : rien trouvé pour « {query} » (essayer le nom exact ou l'URL du store)")
        return
    report["meta"]["ios"] = {
        "nom": app.get("trackName"),
        "editeur": app.get("sellerName"),
        "bundle": app.get("bundleId"),
        "categorie": app.get("primaryGenreName"),
        "categories": app.get("genres"),
        "version": app.get("version"),
        "sortie": app.get("releaseDate"),
        "maj": app.get("currentVersionReleaseDate"),
        "note": app.get("averageUserRating"),
        "avis": app.get("userRatingCount"),
        "prix": app.get("formattedPrice"),
        "url_store": app.get("trackViewUrl"),
        "site": app.get("sellerUrl"),
        "description": (app.get("description") or "")[:1200],
    }
    if app.get("artworkUrl512"):
        p = download(full_res(app["artworkUrl512"]), os.path.join(outdir, "icone"), report["errors"])
        if p:
            report["fichiers"].append(p)

    shots = list(app.get("screenshotUrls") or [])[:cap]
    for i, u in enumerate(shots, 1):
        # le nom du fichier source est souvent parlant (Hero.png, Inbox.png…)
        src = os.path.splitext(os.path.basename(urllib.parse.urlparse(u).path.rstrip("/").rsplit("/", 1)[0]))[0]
        label = slugify(src) if src and not src[0].isdigit() else f"{i:02d}"
        p = download(full_res(u), os.path.join(outdir, "ecrans", f"ios-{i:02d}-{label}"), report["errors"])
        if p:
            report["fichiers"].append(p)
    if want_ipad:
        for i, u in enumerate(list(app.get("ipadScreenshotUrls") or [])[:cap], 1):
            p = download(full_res(u), os.path.join(outdir, "ecrans", f"ipad-{i:02d}"), report["errors"])
            if p:
                report["fichiers"].append(p)


# -------------------------------------------------------------- Google Play
def grab_android(query: str, outdir: str, country: str, cap: int, report: dict):
    m = PLAY_ID.search(query)
    pkg = m.group(1) if m else None
    if not pkg:
        # pas de package connu : on tente le bundle id trouvé côté iOS (souvent identique)
        pkg = (report.get("meta", {}).get("ios") or {}).get("bundle")
    if not pkg:
        report["errors"].append("Google Play : package inconnu (donner l'URL Play ou le bundle id)")
        return
    url = f"https://play.google.com/store/apps/details?id={pkg}&hl=fr&gl={country.upper()}"
    try:
        html = get(url).decode("utf-8", "replace")
    except Exception as e:
        report["errors"].append(f"Google Play : page inaccessible ({e}) — package « {pkg} » inexistant ?")
        return
    shots = list(dict.fromkeys(PLAY_SHOT.findall(html)))[:cap]
    if not shots:
        report["errors"].append("Google Play : aucun écran détecté (marqueur =w526-h296 absent — le HTML a peut-être changé)")
    report["meta"]["android"] = {"package": pkg, "url_store": url, "ecrans_detectes": len(shots)}
    for i, u in enumerate(shots, 1):
        p = download(u.replace("=w526-h296", "=s0"), os.path.join(outdir, "ecrans", f"android-{i:02d}"), report["errors"])
        if p:
            report["fichiers"].append(p)


def main() -> int:
    ap = argparse.ArgumentParser(description="Récupère les écrans d'une app depuis les stores, en pleine qualité.")
    ap.add_argument("query", help="nom de l'app, URL App Store ou URL Google Play")
    ap.add_argument("outdir", help="dossier de destination (ex. INSPIRATION/UI-DESIGN/linear)")
    ap.add_argument("--store", choices=["ios", "android", "both"], default="both")
    ap.add_argument("--country", default="fr")
    ap.add_argument("--ipad", action="store_true", help="garder aussi les captures iPad")
    ap.add_argument("--max", type=int, default=20, help="plafond d'écrans par store (def 20)")
    args = ap.parse_args()

    report = {"query": args.query, "outdir": args.outdir, "meta": {}, "fichiers": [], "errors": []}
    if args.store in ("ios", "both"):
        grab_ios(args.query, args.outdir, args.country, args.ipad, args.max, report)
    if args.store in ("android", "both"):
        grab_android(args.query, args.outdir, args.country, args.max, report)

    if not report["fichiers"]:
        report["errors"].append("aucun fichier récupéré")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["fichiers"] else 1


if __name__ == "__main__":
    sys.exit(main())
