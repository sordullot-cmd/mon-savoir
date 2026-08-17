#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
palette.py — outil couleurs du skill /univers.

Deux usages :

  1) RELEVE — compter les couleurs réellement utilisées dans des images
     python3 palette.py releve "INSPIRATION/UNIVERS/<slug>/ui/*.png" [--top 24] [--step 5]
     Décodeur PNG en Python pur (zlib seulement, aucune dépendance) : marche sans PIL.
     Sort les couleurs dominantes par image, puis l'agrégat trié.

  2) NUANCIER — générer les planches de couleurs en SVG
     python3 palette.py nuancier palette.json INSPIRATION/UNIVERS/<slug>/couleurs/
     Le JSON décrit une liste de planches :
     [
       {
         "fichier": "palette-coeur-de-marque.svg",
         "titre": "Couleurs cœur de marque",
         "sous_titre": "Prises directement sur la mascotte.",
         "colonnes": 4,
         "groupes": [
           {"nom": "", "couleurs": [
               {"nom": "Feather Green", "hex": "#58CC02", "note": "PMS 361 C|CMJN 58 0 96 0"}
           ]}
         ]
       }
     ]
     "note" : lignes séparées par des « | » (Pantone, CMJN, usage observé…).

Les SVG produits sont autonomes, en UTF-8, lisibles directement dans Obsidian.
"""
import os, io, sys, glob, json, zlib, struct
from collections import Counter

FONT = "'DIN Next Rounded','Nunito','Avenir Next','Helvetica Neue',Arial,sans-serif"


# --------------------------------------------------------------- relevé PNG
def read_png(path):
    """Décode un PNG 8 bits (gris/RGB/RGBA/palette non gérée) sans dépendance."""
    d = open(path, 'rb').read()
    if d[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError(f'{path} : pas un PNG')
    pos, idat, w, h, bd, ct = 8, b'', None, None, None, None
    while pos < len(d):
        ln = struct.unpack('>I', d[pos:pos + 4])[0]
        typ, data = d[pos + 4:pos + 8], d[pos + 8:pos + 8 + ln]
        if typ == b'IHDR':
            w, h, bd, ct = struct.unpack('>IIBB', data[:10])
        elif typ == b'IDAT':
            idat += data
        elif typ == b'IEND':
            break
        pos += 12 + ln
    if bd != 8 or ct == 3:
        raise ValueError(f'{path} : profondeur {bd} / type {ct} non géré')
    nch = {0: 1, 2: 3, 4: 2, 6: 4}[ct]
    raw = zlib.decompress(idat)
    stride = w * nch
    out = bytearray(h * stride)
    prev = bytearray(stride)
    p = 0
    for y in range(h):
        f = raw[p]; p += 1
        line = bytearray(raw[p:p + stride]); p += stride
        if f == 1:
            for i in range(nch, stride):
                line[i] = (line[i] + line[i - nch]) & 255
        elif f == 2:
            for i in range(stride):
                line[i] = (line[i] + prev[i]) & 255
        elif f == 3:
            for i in range(stride):
                a = line[i - nch] if i >= nch else 0
                line[i] = (line[i] + ((a + prev[i]) >> 1)) & 255
        elif f == 4:
            for i in range(stride):
                a = line[i - nch] if i >= nch else 0
                b = prev[i]
                c = prev[i - nch] if i >= nch else 0
                pa, pb, pc = abs(b - c), abs(a - c), abs(a + b - 2 * c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[i] = (line[i] + pr) & 255
        out[y * stride:(y + 1) * stride] = line
        prev = line
    return w, h, nch, bytes(out)


def dominant(path, step=5, top=24):
    w, h, nch, px = read_png(path)
    c = Counter()
    for y in range(0, h, step):
        base = y * w * nch
        for x in range(0, w, step):
            i = base + x * nch
            if nch >= 3:
                c[(px[i], px[i + 1], px[i + 2])] += 1
            else:
                g = px[i]; c[(g, g, g)] += 1
    tot = sum(c.values()) or 1
    return [('#%02X%02X%02X' % k, v / tot) for k, v in c.most_common(top)], c, tot


def cmd_releve(pattern, top=24, step=5):
    files = sorted(glob.glob(pattern))
    if not files:
        print(f'aucun fichier pour {pattern}'); return
    total = Counter()
    for f in files:
        try:
            rows, c, tot = dominant(f, step, top)
        except Exception as e:
            print(f'### {os.path.basename(f)} — ignoré ({e})'); continue
        print(f'### {os.path.basename(f)}')
        for hx, pct in rows:
            print(f'  {hx} {pct * 100:5.2f}%')
        for k, v in c.items():
            total[k] += v / tot
    print('\n### AGREGAT (moyenne des parts par image)')
    for k, v in total.most_common(top * 2):
        print('  #%02X%02X%02X %5.2f%%' % (k[0], k[1], k[2], v / len(files) * 100))


# ------------------------------------------------------------- nuancier SVG
def _lum(h):
    r, g, b = int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16)
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255


def _esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def sheet(out_dir, fichier, titre, sous_titre, groupes, colonnes=4, cw=250, ch=150, pad=28):
    gap, y, body = 12, pad + 46 + (24 if sous_titre else 0), []
    for g in groupes:
        gname, items = g.get('nom', ''), g['couleurs']
        if gname:
            body.append(f'<text x="{pad}" y="{y+14}" font-family="{FONT}" font-size="15" '
                        f'font-weight="700" fill="#777777">{_esc(gname.upper())}</text>')
            y += 30
        lines = (len(items) + colonnes - 1) // colonnes
        for i, it in enumerate(items):
            name, hx, note = it['nom'], it['hex'].upper(), it.get('note', '')
            cx = pad + (i % colonnes) * (cw + gap)
            cy = y + (i // colonnes) * (ch + gap)
            fg = '#FFFFFF' if _lum(hx) < 0.62 else '#4B4B4B'
            stroke = ' stroke="#E5E5E5" stroke-width="2"' if _lum(hx) > 0.93 else ''
            body.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="16" fill="{hx}"{stroke}/>')
            body.append(f'<text x="{cx+18}" y="{cy+34}" font-family="{FONT}" font-size="19" '
                        f'font-weight="700" fill="{fg}">{_esc(name)}</text>')
            body.append(f'<text x="{cx+18}" y="{cy+60}" font-family="{FONT}" font-size="17" '
                        f'fill="{fg}" opacity="0.92">{hx}</text>')
            if note:
                parts = note.split('|')
                for j, ln in enumerate(parts):
                    ly = cy + ch - 16 - (len(parts) - 1 - j) * 19
                    body.append(f'<text x="{cx+18}" y="{ly}" font-family="{FONT}" font-size="13" '
                                f'fill="{fg}" opacity="0.8">{_esc(ln)}</text>')
        y += lines * (ch + gap) + 14
    w = pad * 2 + colonnes * cw + (colonnes - 1) * gap
    h = y + pad - 14
    head = (f'<text x="{pad}" y="{pad+30}" font-family="{FONT}" font-size="28" '
            f'font-weight="700" fill="#4B4B4B">{_esc(titre)}</text>')
    if sous_titre:
        head += (f'<text x="{pad}" y="{pad+56}" font-family="{FONT}" font-size="15" '
                 f'fill="#777777">{_esc(sous_titre)}</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
           f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>{head}{"".join(body)}</svg>')
    os.makedirs(out_dir, exist_ok=True)
    io.open(os.path.join(out_dir, fichier), 'w', encoding='utf-8').write(svg)
    print(f'{fichier}  {w}x{h}')


def cmd_nuancier(json_path, out_dir):
    spec = json.load(io.open(json_path, encoding='utf-8'))
    for pl in spec:
        sheet(out_dir, pl['fichier'], pl['titre'], pl.get('sous_titre', ''),
              pl['groupes'], pl.get('colonnes', 4),
              pl.get('largeur_case', 250), pl.get('hauteur_case', 150))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'releve':
        kw = {}
        if '--top' in sys.argv: kw['top'] = int(sys.argv[sys.argv.index('--top') + 1])
        if '--step' in sys.argv: kw['step'] = int(sys.argv[sys.argv.index('--step') + 1])
        cmd_releve(sys.argv[2], **kw)
    elif cmd == 'nuancier':
        cmd_nuancier(sys.argv[2], sys.argv[3])
    else:
        print(__doc__); sys.exit(1)
