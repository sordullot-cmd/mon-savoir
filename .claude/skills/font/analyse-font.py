#!/usr/bin/env python3
"""Analyse une police (fichier ou dossier) : métriques objectives + specimen visuel.

Usage:
    python3 analyse-font.py <chemin-font-ou-dossier> <png-de-sortie>

Sort un JSON sur stdout (métriques) + écrit un specimen PNG.
Les métriques OBJECTIVES (mono, largeur, hauteur d'x, graisses) sont mesurées ;
le jugement subjectif (forme ronde/carrée, mood) reste à faire à l'œil sur le PNG.
"""
import sys, os, glob, json
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

WIDTH_CLASS = {1:"condensée",2:"condensée",3:"condensée",4:"étroite",
               5:"normale",6:"large",7:"large",8:"large",9:"large"}

def faces(path):
    if os.path.isfile(path):
        return [path]
    hits = [h for h in glob.glob(os.path.join(path,"**","*"),recursive=True)
            if h.lower().endswith((".otf",".ttf"))]
    return sorted(hits, key=len)

def pick_regular(fs):
    pref = ["regular","book","normal-400","normal-475","medium","-400-"]
    for p in pref:
        for f in fs:
            if p in os.path.basename(f).lower() and "ital" not in os.path.basename(f).lower():
                return f
    nonital = [f for f in fs if "ital" not in os.path.basename(f).lower()]
    return (nonital or fs)[0]

def name(font, *ids):
    for i in ids:
        try:
            v = font["name"].getDebugName(i)
            if v: return v
        except Exception: pass
    return None

def analyse(path):
    fs = faces(path)
    out = {"chemin": path, "n_fichiers": len(fs), "graisses": [], "metriques": {}, "specimen_source": None}
    if not fs:
        out["erreur"] = "aucun .otf/.ttf trouvé"; return out, None
    reg = pick_regular(fs)
    out["specimen_source"] = os.path.basename(reg)
    # graisses présentes (depuis tous les fichiers)
    weights = set()
    for f in fs:
        try:
            sub = name(TTFont(f, lazy=True), 17, 2)
            if sub: weights.add(sub.strip())
        except Exception: pass
    out["graisses"] = sorted(weights)
    # métriques objectives sur la face regular
    try:
        ft = TTFont(reg, lazy=True)
        out["famille"] = name(ft,16,1)
        upm = ft["head"].unitsPerEm or 1000
        os2 = ft["OS/2"] if "OS/2" in ft else None
        post = ft["post"] if "post" in ft else None
        mono = bool(getattr(post,"isFixedPitch",0)) if post else False
        # repli : PANOSE bProportion == 9 => monospaced (certaines fontes ne posent pas isFixedPitch)
        if not mono and os2 is not None:
            p = getattr(os2,"panose",None)
            if p is not None and getattr(p,"bProportion",0) == 9:
                mono = True
        # dernier repli : MESURER les avances. Certaines fontes (ex. PP Supply Mono)
        # ne posent ni isFixedPitch ni PANOSE bProportion alors qu'elles sont bien
        # à chasse fixe. On teste a-z A-Z 0-9 : mêmes avances => monospace.
        if not mono:
            try:
                cmap = ft.getBestCmap() or {}
                hmtx = ft["hmtx"]
                chars = ([chr(c) for c in range(ord("a"), ord("z")+1)] +
                         [chr(c) for c in range(ord("A"), ord("Z")+1)] +
                         [chr(c) for c in range(ord("0"), ord("9")+1)])
                adv = set()
                for c in chars:
                    g = cmap.get(ord(c))
                    if g and g in hmtx.metrics:
                        w = hmtx[g][0]
                        if w: adv.add(w)
                if len(adv) == 1 and len(chars) >= 40:
                    mono = True
            except Exception: pass
        out["metriques"]["mono"] = mono
        if os2:
            wc = getattr(os2,"usWidthClass",5)
            out["metriques"]["classe_largeur"] = wc
            out["metriques"]["proportions"] = "monospace" if mono else WIDTH_CLASS.get(wc,"normale")
            xh = getattr(os2,"sxHeight",0) or 0
            ch = getattr(os2,"sCapHeight",0) or 0
            if xh:
                ratio = xh/upm
                out["metriques"]["ratio_hauteur_x"] = round(ratio,3)
                out["metriques"]["hauteur"] = "haute" if ratio>=0.52 else ("basse" if ratio<0.46 else "moyenne")
            if ch: out["metriques"]["ratio_capitales"] = round(ch/upm,3)
            p = getattr(os2,"panose",None)
            if p is not None:
                pan = [getattr(p,a,0) for a in ("bFamilyType","bSerifStyle","bWeight",
                       "bProportion","bContrast","bStrokeVariation","bArmStyle",
                       "bLetterForm","bMidline","bXHeight")]
                out["metriques"]["panose"] = pan
                # bContrast PANOSE : 2=none/faible, 3-4=low, 5-6=medium, 7-8=high
                out["metriques"]["contraste_panose"] = pan[4]
        out["metriques"]["n_glyphes"] = len(ft.getGlyphOrder())
    except Exception as e:
        out["metriques"]["erreur"] = str(e)
    return out, reg

def specimen(reg, png_out):
    W = 1400
    img = Image.new("RGB",(W,300),"white"); d = ImageDraw.Draw(img)
    try:
        big = ImageFont.truetype(reg, 70)
        d.text((20,20),"Ronde Haute Carrée Ag", font=big, fill="black")
        med = ImageFont.truetype(reg, 44)
        d.text((20,130),"AaBbGgOoRrQqSs 0123 — Sphinx", font=med, fill="black")
        sm = ImageFont.truetype(reg, 28)
        d.text((20,210),"Portez ce vieux whisky au juge blond qui fume.", font=sm, fill="#333")
    except Exception as e:
        d.text((20,20),f"[rendu impossible: {e}]", fill="red")
    img.save(png_out)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: analyse-font.py <font-ou-dossier> <png-sortie>"); sys.exit(1)
    res, reg = analyse(sys.argv[1])
    if reg: specimen(reg, sys.argv[2]); res["specimen_png"] = sys.argv[2]
    print(json.dumps(res, ensure_ascii=False, indent=2))
