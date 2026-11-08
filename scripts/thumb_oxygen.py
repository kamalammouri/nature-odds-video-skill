"""Oxygen Odds thumbnail: the game HUD drawn by code on a neon bioluminescent Flow image (never text by the generator).
python thumb_oxygen.py scene.png thumbnail.jpg "3% SURVIVAL" [--o2=0.08] [--level="LEVEL 5"] [--force] [--selftest]
Signature of the channel (references/identity.md §5): top-left a big odds readout (number in hot red, word in white),
under it an oxygen bar almost empty (red below 30 %), an optional small level tag; nothing else written.
Text: a percentage or a countdown + 1 word ("3% SURVIVAL", "0:12 LEFT", "1 IN 40") or "GAME OVER?"."""
import re, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
RED, WHITE, CYAN, DIM = (255, 46, 77), (240, 248, 255), (0, 229, 255), (20, 34, 46)
FONT = "C:/Windows/Fonts/impact.ttf"   # ponytail: Impact as stand-in; swap for a squared display font (e.g. Rajdhani Bold) once installed
SMALL = "C:/Windows/Fonts/consolab.ttf"


def lint(text):
    t, errors = text.strip(), []
    if not re.fullmatch(r"(\d{1,3}% [A-Z]+|\d:\d{2} [A-Z]+|1 IN \d{1,4}|GAME OVER\?|[A-Z]+ [A-Z]+\?)", t):
        errors.append('expected "3% SURVIVAL", "0:12 LEFT", "1 IN 40", "GAME OVER?" or two capital words + "?"')
    if re.search(r"YOU\.\.|IT \w+S YOU", t): errors.append("Depth Theory's text pattern: not ours")
    return errors


def render(src, dst, text, o2=0.08, level=None):
    im = Image.open(src).convert("RGB")
    r = max(W / im.width, H / im.height); im = im.resize((round(im.width * r), round(im.height * r)))
    im = im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H))
    d = ImageDraw.Draw(im)
    big = ImageFont.truetype(FONT, 132)
    head, _, tail = text.partition(" ")
    x, y = 44, 30
    d.text((x, y), head, font=big, fill=RED, stroke_width=4, stroke_fill=(0, 0, 0))
    x += d.textlength(head + " ", font=big)
    d.text((x, y), tail, font=big, fill=WHITE, stroke_width=4, stroke_fill=(0, 0, 0))
    # oxygen bar: dark track, coloured fill, O2 label, tick marks every 10 %
    bx, by, bw, bh = 48, 196, 520, 34
    d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=8, fill=DIM, outline=CYAN, width=3)
    fill = RED if o2 < 0.3 else CYAN
    if o2 > 0: d.rounded_rectangle((bx + 5, by + 5, bx + 5 + max(10, (bw - 10) * o2), by + bh - 5), radius=5, fill=fill)
    for k in range(1, 10): d.line((bx + bw * k / 10, by + bh - 9, bx + bw * k / 10, by + bh - 4), fill=CYAN, width=2)
    sf = ImageFont.truetype(SMALL, 30)
    d.text((bx + bw + 14, by - 1), "O2", font=sf, fill=fill)
    if level: d.text((bx, by + bh + 12), level.upper(), font=sf, fill=CYAN)
    im.save(dst, quality=92, optimize=True)


if __name__ == "__main__":
    flags = {a.split("=")[0]: (a.split("=", 1)[1] if "=" in a else True) for a in sys.argv[1:] if a.startswith("--")}
    if "--selftest" in flags:
        for ok in ("3% SURVIVAL", "0:12 LEFT", "1 IN 40", "GAME OVER?", "STILL ALIVE?"): assert lint(ok) == [], ok
        for bad in ("IT HEARS YOU..", "Why You'd Never", "3 % survival"): assert lint(bad), bad
        print("ok"); sys.exit()
    src, dst, text = [a for a in sys.argv[1:] if not a.startswith("--")][:3]
    if (e := lint(text)) and "--force" not in flags: sys.exit("thumb text: " + "; ".join(e) + "  (--force to override)")
    render(src, dst, text, float(flags.get("--o2", 0.08)), flags.get("--level"))
    print(dst)
