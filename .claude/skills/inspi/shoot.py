#!/usr/bin/env python3
"""Capture pleine hauteur d'une page via le protocole Chrome (CDP).

Contrairement au flag --screenshot (qui ne prend que le viewport), ceci capture
TOUTE la hauteur de la page (captureBeyondViewport), en gardant la mise en page
naturelle (viewport 1920x1080 → les unités vh restent correctes).

Usage : shoot.py <url> <outfile.png> [--width W] [--budget MS] [--max-height PX]
"""
import sys, os, json, time, base64, socket, subprocess, argparse, urllib.request
import websocket  # websocket-client

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def free_port():
    s = socket.socket(); s.bind(("", 0)); p = s.getsockname()[1]; s.close(); return p

def launch(port, width):
    return subprocess.Popen([CHROME, "--headless=new", "--disable-gpu",
        "--hide-scrollbars", "--no-first-run", "--no-default-browser-check",
        "--remote-allow-origins=*", "--autoplay-policy=no-user-gesture-required",
        "--mute-audio",
        f"--remote-debugging-port={port}", f"--window-size={width},1080", "about:blank"],
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

def shoot(url, out, width, budget, max_h):
    port = free_port(); proc = launch(port, width)
    try:
        if not wait_ready(port):
            raise RuntimeError("Chrome n'a pas démarré")
        target = next(t for t in json.load(
            urllib.request.urlopen(f"http://127.0.0.1:{port}/json")) if t["type"] == "page")
        c = CDP(target["webSocketDebuggerUrl"])
        c.send("Page.enable")
        c.send("Runtime.enable")
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
        shot = c.send("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": True,
            "clip": {"x": 0, "y": 0, "width": w, "height": h, "scale": 1}})
        with open(out, "wb") as f:
            f.write(base64.b64decode(shot["data"]))
        c.ws.close()
        return {"fichier": os.path.basename(out), "hauteur": h, "largeur": w,
                "tronquee_a_max": h >= max_h}
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
    a = ap.parse_args()
    print(json.dumps(shoot(a.url, a.out, a.width, a.budget, a.max_height), ensure_ascii=False))
