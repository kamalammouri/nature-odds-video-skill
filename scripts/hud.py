"""Oxygen Odds game HUD layer for a HyperFrames project built by ancient-humans-video/scripts/hf_build.py.
python hud.py <project_dir> hud.json          (run after hf_build.py; idempotent)
hud.json: {"gauge": "O2" (or "ENERGY", "AIR"… for Body Swap), "keys":   [{"t": 0, "level": "LEVEL 1 · SURFACE", "o2": 100, "odds": 96, "depth": 0}, ...],
           "events": [{"t": 512.3, "text": "GAME OVER", "dur": 2.0, "color": "#ff2e4d"}, ...]}
keys: the HUD eases to each key's values in 1.2 s starting at t (o2 bar turns red under 30); events: a centred banner
(GAME OVER, YOU SURVIVED, CHOICE LOCKED…). Writes compositions/hud.html and adds its host to index.html above the scenes."""
import json, pathlib, re, sys

W, H = 1920, 1080
RED, CYAN = "#ff2e4d", "#00e5ff"


def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def hud_html(keys, events, dur, gauge="O2"):
    k0, tw = keys[0], []
    tw.append(f'tl.set("#o2f", {{width: "{k0["o2"]}%", backgroundColor: "{RED if k0["o2"] < 30 else CYAN}"}}, 0);')
    for i, k in enumerate(keys[1:], 1):
        t = k["t"]
        tw.append(f'tl.to("#o2f", {{width: "{k["o2"]}%", backgroundColor: "{RED if k["o2"] < 30 else CYAN}", duration: 1.2, ease: "power2.inOut"}}, {t:.3f});')
        for el, v in (("o2v", k["o2"]), ("oddv", k["odds"]), ("depv", k["depth"])):
            tw.append(f'tl.to("#{el}", {{innerText: {v}, snap: {{innerText: 1}}, duration: 1.2, ease: "power2.inOut"}}, {t:.3f});')
        if k.get("level") != keys[i - 1].get("level"):
            tw.append(f'tl.set("#lvl", {{innerText: "{esc(k["level"])}"}}, {t:.3f});')
            tw.append(f'tl.fromTo("#lvl", {{opacity: 0.2}}, {{opacity: 1, duration: 0.4, repeat: 2, yoyo: true, immediateRender: false}}, {t:.3f});')
    banners = []
    for n, e in enumerate(events, 1):
        a, d = e["t"], e.get("dur", 2.0)
        banners.append(f'<div id="ev{n}" class="clip ev" data-start="{a:.3f}" data-duration="{d:.3f}"><p style="color:{e.get("color", RED)}">{esc(e["text"])}</p></div>')
        tw.append(f'tl.fromTo("#ev{n} p", {{opacity: 0, scale: 1.25}}, {{opacity: 1, scale: 1, duration: 0.25, ease: "power3.out"}}, {a:.3f});')
        tw.append(f'tl.to("#ev{n} p", {{opacity: 0, duration: 0.3}}, {a + d - 0.3:.3f});')
    return f"""<template>
<style>
#root {{ position: absolute; inset: 0; font-family: "JetBrains Mono", monospace; }}
.panel {{ position: absolute; left: 48px; top: 44px; width: 660px; color: {CYAN}; text-shadow: 0 0 10px rgba(0,229,255,.7); }}
.row {{ display: flex; justify-content: space-between; font-size: 34px; font-weight: 700; letter-spacing: 2px; margin: 6px 0; }}
.bar {{ height: 30px; border: 3px solid {CYAN}; border-radius: 8px; padding: 3px; background: rgba(4,16,24,.6); box-shadow: 0 0 14px rgba(0,229,255,.5); }}
#o2f {{ height: 100%; border-radius: 4px; }}
#oddv, .odd {{ color: #f0f8ff; }}
.ev {{ position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; }}
.ev p {{ margin: 0; padding: 10px 48px; border-radius: 18px; background: rgba(0,0,0,.72); border: 3px solid currentColor; font: 400 150px "League Gothic", sans-serif; letter-spacing: 6px; text-shadow: 0 0 24px currentColor; }}
</style>
<div id="root" data-composition-id="hud" data-width="{W}" data-height="{H}">
<div id="hudp" class="clip panel" data-start="0" data-duration="{dur:.3f}">
<div class="row"><span id="lvl">{esc(k0["level"])}</span></div>
<div class="bar"><div id="o2f"></div></div>
<div class="row"><span>{esc(gauge)} <span id="o2v">{k0["o2"]}</span>%</span><span class="odd">SURVIVAL <span id="oddv">{k0["odds"]}</span>%</span></div>
<div class="row"><span>DEPTH <span id="depv">{k0["depth"]}</span> M</span></div>
</div>
{chr(10).join(banners)}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(tw)}
window.__timelines["hud"] = tl;
</script>
</template>
"""


def main(proj, spec):
    proj = pathlib.Path(proj); d = json.load(open(spec, encoding="utf-8"))
    keys, events = sorted(d["keys"], key=lambda k: k["t"]), d.get("events", [])
    idx = proj / "index.html"; html = idx.read_text(encoding="utf-8")
    dur = float(re.search(r'data-composition-id="main"[^>]*data-duration="([\d.]+)"', html).group(1))
    (proj / "compositions" / "hud.html").write_text(hud_html(keys, events, dur, d.get("gauge", "O2")), encoding="utf-8")
    if 'id="hud"' not in html:
        host = (f'<div id="hud" data-composition-id="hud" data-composition-src="compositions/hud.html" data-start="0" '
                f'data-duration="{dur:.3f}" data-track-index="5" data-track-kind="graphics" data-width="{W}" data-height="{H}" style="z-index:6"></div>\n')
        html = html.replace('<audio id="voice"', host + '<audio id="voice"', 1)
        idx.write_text(html, encoding="utf-8")
    print(f"HUD -> {proj / 'compositions' / 'hud.html'} | {len(keys)} keys, {len(events)} events, {dur:.1f} s")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        h = hud_html([{"t": 0, "level": "LEVEL 1", "o2": 100, "odds": 90, "depth": 0}, {"t": 5, "level": "LEVEL 2", "o2": 20, "odds": 10, "depth": 900}],
                     [{"t": 8, "text": "GAME OVER"}], 10, "ENERGY")
        assert 'window.__timelines["hud"]' in h and RED in h and "GAME OVER" in h and 'innerText: 900' in h and "ENERGY <span" in h
        print("ok"); sys.exit()
    main(*sys.argv[1:3])
