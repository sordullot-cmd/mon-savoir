#!/usr/bin/env python3
"""Enregistre une ANIMATION d'une page (loader, micro-anim, hero animé) en GIF ou MP4.

Capture une rafale de frames dans le temps via le protocole Chrome (CDP), puis
assemble en GIF (Pillow) ou MP4 (ffmpeg) selon l'extension de sortie.

Usage :
    python3 record.py <url> <out.gif|out.mp4> [--seconds 4] [--fps 12]
        [--width 1440] [--height 900] [--box x y w h] [--delay 0] [--scale 720]
        [--scroll-from Y0] [--scroll-to Y1]

- Pour un LOADER : laisser --delay 0 (on enregistre dès la navigation).
- Pour une anim plus bas dans la page : --delay <ms> et/ou --box pour cadrer.
- Pour une SECTION ANIMÉE AU SCROLL (carte qui se révèle, header qui se déploie) :
  --scroll-from Y0 --scroll-to Y1 → la page défile linéairement de Y0 à Y1
  pendant l'enregistrement, ce qui déclenche les animations liées au scroll.
  (Y0 par défaut = position courante ; --scroll-to seul = scroll jusqu'à Y1.)
"""
import sys, os, json, time, base64, argparse, subprocess, tempfile, shutil
from PIL import Image
import shoot  # réutilise launch/CDP/free_port/wait_ready

def record(url, out, seconds, fps, width, height, box, delay, scale, hover_sel=None,
           scroll_from=None, scroll_to=None):
    import urllib.request
    port = shoot.free_port(); proc = shoot.launch(port, width)
    frames, ts = [], []
    try:
        if not shoot.wait_ready(port):
            raise RuntimeError("Chrome n'a pas démarré")
        target = next(t for t in json.load(
            urllib.request.urlopen(f"http://127.0.0.1:{port}/json")) if t["type"] == "page")
        c = shoot.CDP(target["webSocketDebuggerUrl"])
        c.send("Page.enable")
        c.send("Page.navigate", {"url": url})
        time.sleep(max(delay, 300) / 1000.0)  # warm-up minimal pour que le rendu démarre
        # hover : trouver le centre de l'élément (après scroll dans la vue)
        hover_xy = None
        if hover_sel:
            r = c.send("Runtime.evaluate", {"returnByValue": True, "expression": f"""
            (function(){{var e=document.querySelector({json.dumps(hover_sel)});
              if(!e)return null; e.scrollIntoView({{block:'center'}});
              var b=e.getBoundingClientRect();
              return {{x:Math.round(b.x+b.width/2), y:Math.round(b.y+b.height/2)}};}})()"""})
            val = (r.get("result") or {}).get("value")
            if val: hover_xy = (val["x"], val["y"]); time.sleep(0.4)
        clip = None
        if box:
            x, y, w, h = box
            clip = {"x": x, "y": y, "width": w, "height": h, "scale": 1}
        # scroll : on interpole la position de scroll sur toute la durée de capture
        # pour déclencher les animations liées au défilement (sections révélées au scroll).
        do_scroll = scroll_to is not None
        if do_scroll and scroll_from is None:
            r = c.send("Runtime.evaluate", {"returnByValue": True,
                "expression": "window.scrollY || window.pageYOffset || 0"})
            scroll_from = (r.get("result") or {}).get("value") or 0
        interval = 1.0 / fps
        total = max(seconds, 0.001)
        start_t = time.time()
        i, end = 0, start_t + seconds
        while time.time() < end:
            if hover_xy and i == 2:  # 2 frames "avant", puis on survole pour capter la transition
                c.send("Input.dispatchMouseEvent", {"type": "mouseMoved",
                        "x": hover_xy[0], "y": hover_xy[1]})
            if do_scroll:
                prog = min((time.time() - start_t) / total, 1.0)
                y = round(scroll_from + (scroll_to - scroll_from) * prog)
                c.send("Runtime.evaluate", {"expression": f"window.scrollTo(0, {y})"})
            params = {"format": "png"}
            if clip: params["clip"] = clip
            shot = c.send("Page.captureScreenshot", params)
            data = shot.get("data")
            if data: frames.append(base64.b64decode(data))
            i += 1
            time.sleep(interval)
        c.ws.close()
    finally:
        proc.terminate()
        try: proc.wait(timeout=5)
        except Exception: proc.kill()

    if not frames:
        raise RuntimeError("aucune frame capturée")
    # PIL images
    tmp = tempfile.mkdtemp()
    imgs = []
    for i, b in enumerate(frames):
        p = os.path.join(tmp, f"{i:04d}.png")
        with open(p, "wb") as f: f.write(b)
        im = Image.open(p).convert("RGB")
        if scale and im.width > scale:
            im = im.resize((scale, round(im.height * scale / im.width)))
        imgs.append(im)
    dur_ms = int(1000 / fps)
    if out.lower().endswith(".mp4"):
        # dimensions paires pour yuv420p
        w0, h0 = imgs[0].size; w0 -= w0 % 2; h0 -= h0 % 2
        for i, im in enumerate(imgs):
            im.resize((w0, h0)).save(os.path.join(tmp, f"f{i:04d}.png"))
        subprocess.run(["ffmpeg", "-y", "-framerate", str(fps), "-i",
            os.path.join(tmp, "f%04d.png"), "-pix_fmt", "yuv420p",
            "-movflags", "+faststart", out], capture_output=True)
    else:
        imgs[0].save(out, save_all=True, append_images=imgs[1:], optimize=True,
                     duration=dur_ms, loop=0, disposal=2)
    shutil.rmtree(tmp, ignore_errors=True)
    return {"fichier": os.path.basename(out), "frames": len(imgs),
            "duree_s": seconds, "fps": fps, "taille_ko": round(os.path.getsize(out)/1024)}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("url"); ap.add_argument("out")
    ap.add_argument("--seconds", type=float, default=4)
    ap.add_argument("--fps", type=int, default=12)
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--box", nargs=4, type=int, default=None)
    ap.add_argument("--delay", type=int, default=0)
    ap.add_argument("--scale", type=int, default=720)
    ap.add_argument("--hover-selector", default=None,
                    help="sélecteur CSS à survoler pour capter une anim de hover")
    ap.add_argument("--scroll-from", type=int, default=None,
                    help="position de scroll de départ (px) ; déf = position courante")
    ap.add_argument("--scroll-to", type=int, default=None,
                    help="position de scroll d'arrivée (px) : la page défile pendant la capture")
    a = ap.parse_args()
    print(json.dumps(record(a.url, a.out, a.seconds, a.fps, a.width, a.height,
                            a.box, a.delay, a.scale, a.hover_selector,
                            a.scroll_from, a.scroll_to), ensure_ascii=False))
