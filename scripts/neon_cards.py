"""Oxygen Odds neon cards for the "html" shots of shots.json, written where ancient-humans-video's build_slideshow.render
and hf_build.py look for them: <flow_dir>/html/H0001.png (shot i). python neon_cards.py shots.json flow/<video> [--selftest]
Specs (make_shots.py: H({...})):
  {"type": "choice", "a": "Hold still", "b": "Swim for the boat", "c": "Face it", "level": "LEVEL 2"}
  {"type": "level", "title": "LEVEL 2", "sub": "THE SENSE · 10 M"}
  {"type": "record", "big": "5.5 M", "small": "up to 3 of you, head to toe", "people": 3}
  {"type": "end", "title": "YOU SURVIVED", "sub": "60 SECONDS · ODDS 71%"}   (or "GAME OVER")
Black background, faint cyan hex grid, glowing cyan frames, hot-red alerts (references/identity.md §5)."""
import json, math, pathlib, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1920, 1080
CYAN, MAG, RED, WHITE, ORANGE = (0, 229, 255), (255, 47, 214), (255, 46, 77), (240, 248, 255), (255, 138, 31)
BIG = "C:/Windows/Fonts/impact.ttf"      # ponytail: Windows fonts as stand-ins for League Gothic / JetBrains Mono
MONO = "C:/Windows/Fonts/consolab.ttf"


def f(path, size): return ImageFont.truetype(path, size)


def base():
    im = Image.new("RGB", (W, H), (0, 0, 0)); d = ImageDraw.Draw(im)
    r = 60   # faint hex grid
    for row in range(-1, H // int(r * 1.5) + 2):
        for col in range(-1, W // int(r * 1.732) + 2):
            cx = col * r * 1.732 + (row % 2) * r * 0.866; cy = row * r * 1.5
            pts = [(cx + r * math.cos(math.radians(60 * k + 30)), cy + r * math.sin(math.radians(60 * k + 30))) for k in range(7)]
            d.line(pts, fill=(0, 38, 46), width=1)
    return im


def glow(im, draw_fn):
    layer = Image.new("RGB", (W, H)); draw_fn(ImageDraw.Draw(layer))
    halo = layer.filter(ImageFilter.GaussianBlur(14))
    out = Image.composite(halo, im, halo.convert("L").point(lambda v: min(255, v * 2)))
    return Image.composite(layer, out, layer.convert("L").point(lambda v: 255 if v > 10 else 0))


def centered(d, y, text, font, fill):
    d.text(((W - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)


def choice(s):
    def draw(d):
        if s.get("level"): centered(d, 90, s["level"].upper(), f(MONO, 44), CYAN)
        centered(d, 150, "CHOOSE", f(BIG, 120), WHITE)
        for k, key in enumerate("abc"):
            y = 360 + k * 210
            d.rounded_rectangle((330, y, W - 330, y + 160), radius=22, outline=CYAN, width=6)
            d.text((380, y + 22), key.upper(), font=f(BIG, 110), fill=MAG)
            d.text((520, y + 42), s[key].upper(), font=f(MONO, 64), fill=WHITE)
    return glow(base(), draw)


def level(s):
    def draw(d):
        centered(d, 360, s["title"].upper(), f(BIG, 230), CYAN)
        if s.get("sub"): centered(d, 640, s["sub"].upper(), f(MONO, 58), WHITE)
        d.line((560, 620, W - 560, 620), fill=MAG, width=5)
    return glow(base(), draw)


def record(s):
    def draw(d):
        centered(d, 150, s["big"].upper(), f(BIG, 260), CYAN)
        n, y0, hgt = int(s.get("people", 0)), 640, 230
        if n:
            gap = 30; w = n * 90 + (n - 1) * gap; x0 = (W - w) / 2
            for k in range(n):   # standing human silhouettes for scale
                x = x0 + k * (90 + gap)
                d.ellipse((x + 25, y0, x + 65, y0 + 40), outline=ORANGE, width=6)
                d.line((x + 45, y0 + 40, x + 45, y0 + 150), fill=ORANGE, width=6)
                d.line((x + 5, y0 + 75, x + 85, y0 + 75), fill=ORANGE, width=6)
                d.line((x + 45, y0 + 150, x + 15, y0 + hgt), fill=ORANGE, width=6)
                d.line((x + 45, y0 + 150, x + 75, y0 + hgt), fill=ORANGE, width=6)
        if s.get("small"): centered(d, 920, s["small"].upper(), f(MONO, 54), WHITE)
    return glow(base(), draw)


def end(s):
    col = RED if "OVER" in s["title"].upper() else CYAN
    def draw(d):
        centered(d, 330, s["title"].upper(), f(BIG, 250), col)
        if s.get("sub"): centered(d, 640, s["sub"].upper(), f(MONO, 60), WHITE)
    return glow(base(), draw)


RENDER = {"choice": choice, "level": level, "record": record, "end": end, "title": level}


def main(shots_path, flow_dir):
    out = pathlib.Path(flow_dir) / "html"; out.mkdir(parents=True, exist_ok=True); n = 0
    for s in json.load(open(shots_path, encoding="utf-8")):
        spec = s.get("html") if s.get("family") == "html" else None
        if spec and spec.get("type") in RENDER:
            RENDER[spec["type"]](spec).save(out / f"H{s['i']:04d}.png"); n += 1
    print(f"{n} neon cards -> {out}")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        for fn, spec in ((choice, {"a": "x", "b": "y", "c": "z"}), (level, {"title": "LEVEL 1"}), (record, {"big": "5 M", "people": 2}), (end, {"title": "GAME OVER"})):
            im = fn(spec); assert im.size == (W, H) and im.getbbox(), fn.__name__
        print("ok"); sys.exit()
    main(*sys.argv[1:3])
