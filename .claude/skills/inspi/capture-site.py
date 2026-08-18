#!/usr/bin/env python3
"""Capture un site web : découvre ses pages et fait UN screenshot par page.

Usage:
    python3 capture-site.py <url> <dossier-sortie> [--max N] [--pages /,/about,/shop] [--budget MS]

- Sans --pages : découvre les pages depuis le DOM rendu de la home (liens même domaine),
  et capture chacune (1 screen/page). C'est le comportement PAR DÉFAUT.
- Avec --pages : ne capture que les chemins listés (ex. la home : --pages /).
- Limite de sécurité --max (def 25). Toute troncature est SIGNALÉE (jamais silencieuse).

Sort un JSON : pages capturées {chemin, fichier}, pages ignorées, troncature éventuelle.
"""
import sys, os, re, json, subprocess, argparse
from urllib.parse import urljoin, urlparse, urldefrag
import shoot  # capteur pleine hauteur (CDP), même dossier

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")  # évite la détection HeadlessChrome (403/crash)

def chrome(args, timeout=90):
    # Pas de --enable-unsafe-swiftshader ici : la découverte utilise --dump-dom +
    # --virtual-time-budget, or un WebGL actif (boucle rAF) empêche le virtual-time
    # de se terminer → hang. Les liens de nav sont dans le HTML sans rendu 3D.
    # (SwiftShader reste dans shoot.py pour les captures, en temps réel.)
    return subprocess.run([CHROME, "--headless=new", "--disable-gpu",
        "--hide-scrollbars", f"--user-agent={UA}", *args],
        capture_output=True, text=True, timeout=timeout)

def rendered_html(url, budget):
    r = chrome([f"--virtual-time-budget={budget}", "--dump-dom", url])
    return r.stdout or ""

def slugify(path):
    s = path.strip("/").lower() or "home"
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "home"

def discover(url, budget, max_n):
    html = rendered_html(url, budget)
    host = urlparse(url).netloc
    paths, seen = [], set()
    # toujours inclure la home en premier
    seen.add("/"); paths.append("/")
    for m in re.finditer(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I):
        absu = urljoin(url, m.group(1))
        absu, _ = urldefrag(absu)
        pu = urlparse(absu)
        if pu.scheme not in ("http", "https") or pu.netloc != host:
            continue
        path = pu.path or "/"
        if any(path.lower().endswith(e) for e in
               (".pdf",".zip",".png",".jpg",".jpeg",".svg",".mp4",".webp",".gif",
                ".css",".js",".woff",".woff2",".ttf",".otf",".ico",".json",".xml",".txt")):
            continue
        if "/_next/" in path or path.startswith("/static/"):  # assets build (Next.js…)
            continue
        if path not in seen:
            seen.add(path); paths.append(path)
    truncated = False
    if len(paths) > max_n:
        truncated = len(paths) - max_n
        paths = paths[:max_n]
    return paths, truncated

def group_templates(paths, collapse=True):
    """Regroupe les pages 'template' (même préfixe imbriqué, ex. /works/*) et
    n'en garde qu'UNE représentative. Retourne (selection [(path,name)], rapport).
    - Pages racine (/, /about, /shop…) : toutes gardées (sections distinctes).
    - Pages imbriquées (>=2 segments) partageant le même parent : 1 seule si >=2 instances.
    """
    if not collapse:
        return [(p, slugify(p)) for p in paths], {}
    groups = {}   # parent -> [paths]
    for p in paths:
        segs = [s for s in p.split("/") if s]
        parent = "/".join(segs[:-1]) if len(segs) >= 2 else None  # None = racine
        groups.setdefault(parent, []).append(p)
    selection, report = [], {}
    for parent, ps in groups.items():
        if parent is not None and len(ps) >= 2:
            rep = ps[0]                       # 1 représentant du template
            name = f"{slugify(parent)}-template"
            selection.append((rep, name))
            report[parent] = {"instances": len(ps), "capturée": rep,
                              "ignorées": len(ps) - 1}
        else:
            for p in ps:
                selection.append((p, slugify(p)))
    # remettre la home en tête si présente
    selection.sort(key=lambda t: (t[1] != "home", t[1]))
    return selection, report

def capture(url, outdir, path, budget, name=None, width=1920,
            mobile=False, sombre=False, suffixe=""):
    target = urljoin(url, path)
    name = (name or slugify(path)) + suffixe
    out = os.path.join(outdir, f"{name}.png")
    # éviter collision de noms
    i = 2
    while os.path.exists(out):
        out = os.path.join(outdir, f"{name}-{i}.png"); i += 1
    try:
        r = shoot.shoot(target, out, width, budget, 20000, mobile, sombre)  # PLEINE HAUTEUR
        ok = os.path.exists(out) and os.path.getsize(out) > 0
        return {"chemin": path, "url": target,
                "fichier": os.path.basename(out) if ok else None,
                "rendu": r.get("rendu"),
                "hauteur": r.get("hauteur"), "tronquee_a_max": r.get("tronquee_a_max"),
                "polices": r.get("polices")}
    except Exception as e:
        return {"chemin": path, "url": target, "fichier": None, "erreur": str(e)}


def fusionner_polices(captures):
    """Union des polices relevées sur toutes les pages, la plus utilisée d'abord."""
    total, chargees = {}, set()
    for c in captures:
        p = c.get("polices") or {}
        for f in p.get("rendues") or []:
            total[f["famille"]] = total.get(f["famille"], 0) + f.get("elements", 0)
        for f in p.get("chargees") or []:
            chargees.add(f)
    rendues = [{"famille": k, "elements": v}
               for k, v in sorted(total.items(), key=lambda kv: -kv[1])]
    if not rendues and not chargees:
        return None
    return {"rendues": rendues[:8], "chargees": sorted(chargees)[:12]}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("url"); ap.add_argument("outdir")
    ap.add_argument("--max", type=int, default=25)
    ap.add_argument("--pages", default="")
    ap.add_argument("--budget", type=int, default=16000)
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--all-pages", action="store_true",
                    help="capturer CHAQUE page (désactive le regroupement par template)")
    ap.add_argument("--viewports", default="desktop",
                    help="desktop | mobile | desktop,mobile (def desktop). "
                         "Le mobile émule un iPhone → mise en page responsive réelle.")
    ap.add_argument("--dark", action="store_true",
                    help="capturer AUSSI la home en thème sombre (home-dark.png)")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    viewports = [v.strip() for v in a.viewports.split(",") if v.strip()]

    report = {}
    if a.pages.strip():
        paths = [p if p.startswith("/") else "/"+p for p in
                 (x.strip() for x in a.pages.split(",")) if p.strip()]
        selection = [(p, slugify(p)) for p in paths]
        truncated = False
        mode = "pages-explicites"
    else:
        paths, truncated = discover(a.url, a.budget, a.max)
        selection, report = group_templates(paths, collapse=not a.all_pages)
        mode = "toutes-les-pages" if a.all_pages else "1-page-par-template"

    captured = []
    if "desktop" in viewports:
        captured += [capture(a.url, a.outdir, p, a.budget, name, a.width)
                     for p, name in selection]
    if "mobile" in viewports:
        captured += [capture(a.url, a.outdir, p, a.budget, name, a.width,
                             mobile=True, suffixe="-mobile")
                     for p, name in selection]
    # Thème sombre : la home seule. Comparer avec home.png dit si le site en a un ;
    # un site sans thème sombre rend une image identique au clair (à signaler, pas à garder).
    if a.dark:
        home = next((s for s in selection if s[1] == "home"), selection[0] if selection else None)
        if home:
            captured.append(capture(a.url, a.outdir, home[0], a.budget, home[1], a.width,
                                    sombre=True, suffixe="-dark"))
    print(json.dumps({
        "mode": mode,
        "viewports": viewports + (["dark(home)"] if a.dark else []),
        "n_pages": len(captured),
        "pages": captured,
        "polices": fusionner_polices(captured),
        "templates_regroupés": report or None,
        "troncature": (f"{truncated} page(s) au-delà de --max={a.max} NON capturées"
                       if truncated else None),
    }, ensure_ascii=False, indent=2))
