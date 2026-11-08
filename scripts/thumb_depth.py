"""Depth Theory thumbnail text + red arrow, by code (never by the image generator).
python thumb_depth.py scene.png thumbnail.jpg "IT HEARS YOU.." [--arrow=0.30,0.30,0.12,0.72] [--red=1] [--force]
Template measured on the 7 channel thumbnails (8 Nov 2026): black scratchboard engraving, text top-left in white
heavy condensed capitals, the last word(s) in red, a red hand-drawn curved arrow pointing at the tiny diver.
--arrow=x0,y0,x1,y1 : start and tip as fractions of the frame (omit = no arrow). --red=N : last N words in red."""
import re, sys
from PIL import Image, ImageDraw, ImageFont

RED, WHITE, W, H = (226, 30, 36), (245, 245, 245), 1280, 720
FONT = "C:/Windows/Fonts/impact.ttf"  # ponytail: Impact as stand-in; point to Anton/Bebas Neue .ttf if installed


def lint(text):
    words, errors = text.split(), []
    if not 2 <= len(words) <= 4: errors.append(f"{len(words)} words, 2 to 4 expected")
    if not re.search(r"(\.\.|\?)$", text.strip()): errors.append('end with ".." (IT SEES YOU..) or "?" (STILL KING?)')
    if text != text.upper() and not re.match(r"^[A-Z][a-z]+ [A-Z][a-z]+\?$", text): errors.append("capitals expected")
    return errors


def arrow(d, x0, y0, x1, y1, w=11):
    # quadratic bezier bulging to one side of the chord, then a filled head at the tip
    cx, cy = (x0 + x1) / 2 - (y1 - y0) * 0.35, (y0 + y1) / 2 + (x1 - x0) * 0.35
    pts = [((1-t)**2*x0 + 2*(1-t)*t*cx + t*t*x1, (1-t)**2*y0 + 2*(1-t)*t*cy + t*t*y1) for t in [i/40 for i in range(41)]]
    d.line(pts, fill=RED, width=w, joint="curve")
    (ax, ay), (bx, by) = pts[-4], pts[-1]
    vx, vy = bx - ax, by - ay; n = (vx*vx + vy*vy) ** 0.5 or 1; vx, vy = vx/n, vy/n
    s = 42
    d.polygon([(bx + vx*8, by + vy*8), (bx - vx*s - vy*s*0.6, by - vy*s + vx*s*0.6), (bx - vx*s + vy*s*0.6, by - vy*s - vx*s*0.6)], fill=RED)


def render(src, dst, text, arr=None, red=1):
    im = Image.open(src).convert("RGB")
    r = max(W / im.width, H / im.height); im = im.resize((round(im.width*r), round(im.height*r)))
    im = im.crop(((im.width-W)//2, (im.height-H)//2, (im.width-W)//2 + W, (im.height-H)//2 + H))
    d, words = ImageDraw.Draw(im), text.split()
    size = 120
    while size > 60:
        f = ImageFont.truetype(FONT, size)
        if d.textlength(text, font=f) <= W * 0.62: break
        size -= 4
    x, y = 40, 40
    for i, wd in enumerate(words):
        d.text((x, y), wd, font=f, fill=RED if i >= len(words) - red else WHITE, stroke_width=3, stroke_fill=(0, 0, 0))
        x += d.textlength(wd + " ", font=f)
    if arr: arrow(d, *(v * (W if i % 2 == 0 else H) for i, v in enumerate(arr)))
    im.save(dst, quality=92, optimize=True)


if __name__ == "__main__":
    flags = {a.split("=")[0]: (a.split("=", 1)[1] if "=" in a else True) for a in sys.argv[1:] if a.startswith("--")}
    if "--selftest" in flags:
        assert lint("IT HEARS YOU..") == [] and lint("Still King?") == [] and lint("IT HEARS YOU") and lint("A B C D E..")
        print("ok"); sys.exit()
    src, dst, text = [a for a in sys.argv[1:] if not a.startswith("--")][:3]
    if (e := lint(text)) and "--force" not in flags: sys.exit("thumb text: " + "; ".join(e) + "  (--force to override)")
    arr = [float(v) for v in flags["--arrow"].split(",")] if "--arrow" in flags else None
    render(src, dst, text, arr, int(flags.get("--red", 1)))
    print(dst)
