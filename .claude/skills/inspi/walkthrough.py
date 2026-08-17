#!/usr/bin/env python3
"""Vidéo walkthrough de TOUT le site : défilement auto de chaque page, assemblé en un seul MP4.

Découvre les pages (1 par template), charge le lazy-load + frames vidéo, enregistre un
scroll haut->bas de chaque page, puis concatène toutes les frames en une vidéo (ffmpeg).

Usage :
    python3 walkthrough.py <url> <out.mp4> [--fps 10] [--speed 500] [--hold 0.8]
        [--width 1440] [--max-pages 8] [--pages "/,/about"]
    --speed = vitesse de défilement en px/s (vitesse CONSTANTE quelle que soit la hauteur de page).
"""
import sys, os, re, json, time, base64, subprocess, tempfile, shutil, argparse, urllib.request
from urllib.parse import urljoin, urlparse, urldefrag
from PIL import Image
import shoot

YT_SWAP = r"""
document.querySelectorAll('iframe').forEach(function(f){try{
  var s=f.src||f.getAttribute('data-src')||'';
  var m=s.match(/(?:youtube(?:-nocookie)?\.com\/embed\/|youtu\.be\/)([\w-]{11})/);
  if(m){var b=f.getBoundingClientRect();var img=document.createElement('img');
    img.onerror=function(){this.src='https://i.ytimg.com/vi/'+m[1]+'/hqdefault.jpg';};
    img.src='https://i.ytimg.com/vi/'+m[1]+'/maxresdefault.jpg';
    img.style.width=(b.width||f.clientWidth)+'px';img.style.height=(b.height||f.clientHeight)+'px';
    img.style.objectFit='cover';img.style.display='block';
    if(f.parentNode)f.parentNode.replaceChild(img,f);}
}catch(e){}});
"""

def slugify(path):
    s = path.strip("/").lower() or "home"
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-") or "home"

def dump_dom(url, budget):
    r = subprocess.run([shoot.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        f"--user-agent={shoot.UA}",  # évite le 403/crash HeadlessChrome (pas de swiftshader ici : hang virtual-time)
        f"--virtual-time-budget={budget}", "--dump-dom", url], capture_output=True, text=True, timeout=90)
    return r.stdout or ""

def discover(url, budget, max_n):
    html = dump_dom(url, budget)
    host = urlparse(url).netloc
    paths, seen = [], set(); seen.add("/"); paths.append("/")
    for m in re.finditer(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I):
        absu, _ = urldefrag(urljoin(url, m.group(1))); pu = urlparse(absu)
        if pu.scheme not in ("http", "https") or pu.netloc != host: continue
        p = pu.path or "/"
        if any(p.lower().endswith(e) for e in (".pdf",".zip",".png",".jpg",".svg",".mp4",".webp",".gif")): continue
        if p not in seen: seen.add(p); paths.append(p)
    # 1 page par template (préfixe imbriqué avec >=2 enfants)
    groups = {}
    for p in paths:
        segs=[s for s in p.split("/") if s]
        parent="/".join(segs[:-1]) if len(segs)>=2 else None
        groups.setdefault(parent, []).append(p)
    sel=[]
    for parent, ps in groups.items():
        sel.append(ps[0] if (parent is not None and len(ps)>=2) else ps[0])
        if parent is None:
            sel += ps[1:]
    # uniques, home en tête
    sel = list(dict.fromkeys(sel))
    sel.sort(key=lambda p: (p != "/", p))
    return sel[:max_n]

def record_scroll(url, width, fps, speed, hold_secs, budget, tmp, start_idx):
    """Enregistre un scroll haut->bas d'une page à VITESSE CONSTANTE (px/s) + pauses haut/bas.
    Retourne le nb de frames écrites."""
    port = shoot.free_port(); proc = shoot.launch(port, width)
    n = start_idx
    try:
        if not shoot.wait_ready(port): return 0
        target = next(t for t in json.load(urllib.request.urlopen(
            f"http://127.0.0.1:{port}/json")) if t["type"] == "page")
        c = shoot.CDP(target["webSocketDebuggerUrl"])
        c.send("Page.enable")
        c.send("Page.navigate", {"url": url})
        c.wait_event("Page.loadEventFired", timeout=20)
        time.sleep(min(budget, 14000) / 1000.0)
        ev = lambda e: c.send("Runtime.evaluate", {"expression": e})
        total = (c.send("Page.getLayoutMetrics").get("cssContentSize") or {}).get("height", 1080)
        # pré-charger lazy + frames vidéo
        y = 0
        while y < total:
            ev(f"window.scrollTo(0,{y})"); time.sleep(0.25); y += 900
        ev(YT_SWAP); ev("document.querySelectorAll('video').forEach(v=>{try{v.muted=true;v.play()}catch(e){}})")
        ev("window.scrollTo(0,0)"); time.sleep(1.2)
        total = (c.send("Page.getLayoutMetrics").get("cssContentSize") or {}).get("height", 1080)
        vp = 1080
        span = max(0, total - vp)
        step = max(20, round(speed / max(1, fps)))   # px par frame -> vitesse constante (= step * fps px/s)
        nframes = max(2, span // step + 1)
        hold = max(0, round(hold_secs * fps))         # frames de pause haut/bas
        def write(b):
            nonlocal n
            with open(os.path.join(tmp, f"{n:05d}.png"), "wb") as f: f.write(b)
            n += 1
        first_b = last_b = None
        for i in range(nframes):
            yy = min(span, i * step)
            ev(f"window.scrollTo(0,{yy})"); time.sleep(0.05)
            d = c.send("Page.captureScreenshot", {"format": "png"}).get("data")
            if not d: continue
            b = base64.b64decode(d)
            if first_b is None:                       # pause en haut
                first_b = b
                for _ in range(hold): write(first_b)
            write(b); last_b = b
        if last_b is not None:                        # pause en bas
            for _ in range(hold): write(last_b)
        c.ws.close()
    finally:
        proc.terminate()
        try: proc.wait(timeout=5)
        except Exception: proc.kill()
    return n - start_idx

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("url"); ap.add_argument("out")
    ap.add_argument("--fps", type=int, default=10)
    ap.add_argument("--speed", type=float, default=500, help="vitesse de défilement en px/s (def 500)")
    ap.add_argument("--hold", type=float, default=0.8, help="pause haut/bas en secondes (def 0.8)")
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--max-pages", type=int, default=8)
    ap.add_argument("--budget", type=int, default=16000)
    ap.add_argument("--pages", default="")
    a = ap.parse_args()

    if a.pages.strip():
        pages = [p if p.startswith("/") else "/"+p for p in
                 (x.strip() for x in a.pages.split(",")) if p.strip()]
    else:
        pages = discover(a.url, a.budget, a.max_pages)

    tmp = tempfile.mkdtemp(); idx = 0; per_page = []
    for p in pages:
        wrote = record_scroll(urljoin(a.url, p), a.width, a.fps, a.speed, a.hold, a.budget, tmp, idx)
        per_page.append({"page": p, "frames": wrote}); idx += wrote

    if idx == 0:
        print(json.dumps({"erreur": "aucune frame"})); shutil.rmtree(tmp, True); sys.exit(1)
    # normaliser en dimensions paires
    im0 = Image.open(os.path.join(tmp, sorted(os.listdir(tmp))[0]))
    w0, h0 = im0.size; w0 -= w0 % 2; h0 -= h0 % 2
    for fn in os.listdir(tmp):
        p = os.path.join(tmp, fn)
        Image.open(p).convert("RGB").resize((w0, h0)).save(p)
    subprocess.run(["ffmpeg", "-y", "-framerate", str(a.fps), "-i", os.path.join(tmp, "%05d.png"),
                    "-pix_fmt", "yuv420p", "-movflags", "+faststart", a.out], capture_output=True)
    shutil.rmtree(tmp, ignore_errors=True)
    print(json.dumps({"fichier": os.path.basename(a.out), "pages": per_page,
                      "frames_total": idx, "fps": a.fps,
                      "taille_Mo": round(os.path.getsize(a.out)/1048576, 2)}, ensure_ascii=False))
