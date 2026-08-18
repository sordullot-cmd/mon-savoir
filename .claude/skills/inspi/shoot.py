#!/usr/bin/env python3
"""Capture pleine hauteur d'une page via le protocole Chrome (CDP).

Contrairement au flag --screenshot (qui ne prend que le viewport), ceci capture
TOUTE la hauteur de la page (captureBeyondViewport), en gardant la mise en page
naturelle (viewport 1920x1080 → les unités vh restent correctes).

Deux variantes de rendu, même page :
- --mobile : émule un iPhone (390x844, dpr 3, UA + touch) → le site sert sa mise
  en page responsive, pas une version desktop rétrécie.
- --sombre : émule prefers-color-scheme: dark → capture le thème sombre quand le
  site en a un (les sites qui n'en ont pas rendent une image identique au clair).

Relève aussi les POLICES réellement rendues (font-family calculée sur les
éléments porteurs de texte + familles chargées via document.fonts) → champ
"polices" du JSON, qui alimente le lien vers les fiches /font du vault.

Usage : shoot.py <url> <outfile.png> [--width W] [--budget MS] [--max-height PX]
                 [--mobile] [--sombre]
"""
import sys, os, json, time, base64, socket, subprocess, argparse, urllib.request
import websocket  # websocket-client

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# UA réaliste : beaucoup de sites (Next.js/SPA) plantent ou renvoient 403 si l'UA
# contient "HeadlessChrome" (détection anti-bot). On se fait passer pour un Chrome normal.
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
UA_MOBILE = ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 "
             "(KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1")

# iPhone 15 Pro : la mise en page mobile la plus courante en 2026.
MOBILE = {"width": 390, "height": 844, "dpr": 3}

# Relevé des polices RÉELLEMENT rendues : on compte les éléments porteurs de texte
# par famille (le 1er nom de la pile font-family, celui qui gagne), et on liste les
# familles effectivement chargées par le navigateur (webfonts). Une famille très
# utilisée = la typo du site ; une famille à 2 occurrences = un détail.
JS_POLICES = r"""
(function(){
  var c = {};
  document.querySelectorAll('body *').forEach(function(el){
    try{
      if (!el.firstChild) return;
      var direct = false;
      for (var n = el.firstChild; n; n = n.nextSibling)
        if (n.nodeType === 3 && n.nodeValue.trim()) { direct = true; break; }
      if (!direct) return;
      var f = getComputedStyle(el).fontFamily || '';
      var first = f.split(',')[0].replace(/["']/g, '').trim();
      if (!first) return;
      c[first] = (c[first] || 0) + 1;
    }catch(e){}
  });
  var loaded = [];
  try { document.fonts.forEach(function(ff){
    if (ff.status === 'loaded') loaded.push(String(ff.family).replace(/["']/g, '').trim());
  }); } catch(e) {}
  var top = Object.keys(c).sort(function(a,b){ return c[b]-c[a]; }).slice(0, 8)
              .map(function(k){ return {famille: k, elements: c[k]}; });
  return JSON.stringify({rendues: top, chargees: Array.from(new Set(loaded)).slice(0, 12)});
})()
"""

def free_port():
    s = socket.socket(); s.bind(("", 0)); p = s.getsockname()[1]; s.close(); return p

def launch(port, width, mobile=False):
    return subprocess.Popen([CHROME, "--headless=new", "--disable-gpu",
        # WebGL logiciel : les sites Three.js/WebGL plantent ("Application error")
        # sans contexte WebGL ; Chrome récent l'exige pour le fallback SwiftShader.
        "--enable-unsafe-swiftshader",
        # masque navigator.webdriver : la connexion CDP le met à true et certains
        # sites (Next.js/SPA) plantent alors avec une "Application error".
        "--disable-blink-features=AutomationControlled",
        "--hide-scrollbars", "--no-first-run", "--no-default-browser-check",
        "--remote-allow-origins=*", "--autoplay-policy=no-user-gesture-required",
        "--mute-audio", f"--user-agent={UA_MOBILE if mobile else UA}",
        f"--remote-debugging-port={port}",
        f"--window-size={MOBILE['width'] if mobile else width},{MOBILE['height'] if mobile else 1080}",
        "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def wait_ready(port, timeout=15):
    end = time.time() + timeout
    while time.time() < end:
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version", timeout=0.5)
            return True
        except Exception:
            time.sleep(0.2)
    return False

class CDP:
    def __init__(self, ws_url):
        self.ws = websocket.create_connection(ws_url, max_size=None, timeout=180)
        self._id = 0
    def send(self, method, params=None):
        self._id += 1; mid = self._id
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == mid:
                return msg.get("result", {})
    def wait_event(self, name, timeout=20):
        end = time.time() + timeout
        while time.time() < end:
            try:
                msg = json.loads(self.ws.recv())
            except Exception:
                return
            if msg.get("method") == name:
                return msg

def shoot(url, out, width, budget, max_h, mobile=False, sombre=False):
    port = free_port(); proc = launch(port, width, mobile)
    try:
        if not wait_ready(port):
            raise RuntimeError("Chrome n'a pas démarré")
        target = next(t for t in json.load(
            urllib.request.urlopen(f"http://127.0.0.1:{port}/json")) if t["type"] == "page")
        c = CDP(target["webSocketDebuggerUrl"])
        c.send("Page.enable")
        c.send("Runtime.enable")
        if mobile:
            # setDeviceMetricsOverride AVANT navigate : sinon le site sert d'abord
            # sa version desktop et beaucoup de SPA ne re-layoutent pas au resize.
            c.send("Emulation.setDeviceMetricsOverride", {
                "width": MOBILE["width"], "height": MOBILE["height"],
                "deviceScaleFactor": MOBILE["dpr"], "mobile": True})
            c.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
        if sombre:
            c.send("Emulation.setEmulatedMedia", {"features": [
                {"name": "prefers-color-scheme", "value": "dark"}]})
        c.send("Page.navigate", {"url": url})
        c.wait_event("Page.loadEventFired", timeout=20)
        time.sleep(min(budget, 14000) / 1000.0)  # laisser les préchargeurs finir
        # 1) scroller toute la page pour déclencher le lazy-load des images
        ev = lambda expr: c.send("Runtime.evaluate", {"expression": expr})
        total = (c.send("Page.getLayoutMetrics").get("cssContentSize") or {}).get("height", 1080)
        step, y, n = 900, 0, 0
        while y < total and n < 60:
            ev(f"window.scrollTo(0,{y})"); time.sleep(0.45); y += step; n += 1
        # 2a) remplacer les embeds YouTube (qui ne se rendent pas en headless) par leur miniature = frame de la vidéo
        ev(r"""
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
        """)
        # 2b) lancer les vidéos HTML5 en muet pour afficher une frame
        ev("document.querySelectorAll('video').forEach(v=>{try{v.muted=true;v.play()}catch(e){}});")
        time.sleep(3.0)
        # 3) revenir en haut et laisser tout se stabiliser
        ev("window.scrollTo(0,0)"); time.sleep(1.0)
        m = c.send("Page.getLayoutMetrics")
        size = m.get("cssContentSize") or m.get("contentSize") or {}
        h = int(min(size.get("height", 1080) or 1080, max_h))
        w = int(size.get("width", width) or width)
        # 4) relever les polices rendues AVANT la capture (même état de page)
        polices = None
        try:
            r = c.send("Runtime.evaluate", {"expression": JS_POLICES, "returnByValue": True})
            polices = json.loads((r.get("result") or {}).get("value") or "null")
        except Exception:
            pass
        shot = c.send("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": True,
            "clip": {"x": 0, "y": 0, "width": w, "height": h, "scale": 1}})
        with open(out, "wb") as f:
            f.write(base64.b64decode(shot["data"]))
        c.ws.close()
        return {"fichier": os.path.basename(out), "hauteur": h, "largeur": w,
                "tronquee_a_max": h >= max_h,
                "rendu": ("mobile" if mobile else "desktop") + ("-sombre" if sombre else ""),
                "polices": polices}
    finally:
        proc.terminate()
        try: proc.wait(timeout=5)
        except Exception: proc.kill()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("url"); ap.add_argument("out")
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--budget", type=int, default=16000)
    ap.add_argument("--max-height", type=int, default=20000)
    ap.add_argument("--mobile", action="store_true", help="émuler un iPhone (390x844, dpr 3)")
    ap.add_argument("--sombre", action="store_true", help="émuler prefers-color-scheme: dark")
    a = ap.parse_args()
    print(json.dumps(shoot(a.url, a.out, a.width, a.budget, a.max_height,
                           a.mobile, a.sombre), ensure_ascii=False))
