"""Oxygen Odds sound pass (references/identity.md §6) on a rendered video: voice compressed, a low bubble/regulator bed ducked
under the voice, synthesized HUD beeps, sonar pings and choice locks placed from hud.json, master at -14 LUFS / -1.5 dBTP.
python mix_oxygen.py render.mp4 hud.json bed.mp3 out.mp4 [--sonar 8.7,38.0] [--bed-vol 0.22] [--fx-vol 0.55]
Beep on every hud.json key after the first (and at 0.15 s), lock on every event whose text starts with "CHOICE", alarm on every
key whose o2 drops under 30, ping at each --sonar time (creature reveals). Measured on the 8 Nov 2026 demo: -14.1 LUFS, -1.4 dBTP."""
import json, pathlib, re, subprocess, sys, tempfile

FF = __import__("imageio_ffmpeg").get_ffmpeg_exe()
SYNTH = {  # lavfi source, filter: exact, license-free sounds
    "beep": ("sine=f=1760:d=0.09", "afade=t=out:st=0.06:d=0.03,volume=0.5"),
    "sonar": ("sine=f=1150:d=0.25", "afade=t=out:st=0.05:d=0.2,aecho=0.8:0.6:300|600:0.45|0.25,apad=pad_dur=1.2,volume=0.7"),
    "lock": ("sine=f=1400:d=0.14", "afade=t=out:st=0.08:d=0.06,volume=0.6"),
    "alarm": ("sine=f=880:d=0.6", "volume='if(lt(mod(t,0.3),0.15),0.45,0)':eval=frame"),
}


def cues(hud, sonar):
    keys, out = sorted(hud["keys"], key=lambda k: k["t"]), [("beep", 0.15)]
    for prev, k in zip(keys, keys[1:]):
        out.append(("alarm" if k["o2"] < 30 <= prev["o2"] else "beep", k["t"]))
    out += [("lock", e["t"]) for e in hud.get("events", []) if e["text"].upper().startswith("CHOICE")]
    out += [("sonar", t) for t in sonar]
    loud = [t for n, t in out if n != "beep"]   # a beep under a ping, lock or alarm is noise: drop it
    out = [(n, t) for n, t in out if n != "beep" or all(abs(t - u) > 0.3 for u in loud)]
    return sorted(out, key=lambda c: c[1])


def duration(path):
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", subprocess.run([FF, "-i", path], capture_output=True, text=True).stderr).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def main(render, hud_path, bed, out, sonar=(), bed_vol=0.22, fx_vol=0.55):
    cs, dur = cues(json.load(open(hud_path, encoding="utf-8")), sonar), duration(render)
    tmp = pathlib.Path(tempfile.mkdtemp())
    for name, (src, flt) in SYNTH.items():
        subprocess.run([FF, "-y", "-loglevel", "error", "-f", "lavfi", "-i", src, "-af", flt, str(tmp / f"{name}.wav")], check=True)
    ins = ["-i", render, "-stream_loop", "-1", "-i", bed] + sum((["-i", str(tmp / f"{n}.wav")] for n, _ in cs), [])
    fc = ["[0:a]highpass=f=70,acompressor=threshold=-20dB:ratio=3:attack=5:release=120:makeup=3dB,asplit=2[v][k]",
          f"[1:a]atrim=0:{dur:.2f},volume={bed_vol},afade=t=out:st={max(0, dur - 3):.2f}:d=3[bed]",
          "[bed][k]sidechaincompress=threshold=0.02:ratio=6:attack=15:release=350[bd]"]
    fc += [f"[{i + 2}:a]adelay={int(t * 1000)}:all=1[e{i}]" for i, (_, t) in enumerate(cs)]
    fc.append("".join(f"[e{i}]" for i in range(len(cs))) + f"amix=inputs={len(cs)}:normalize=0,volume={fx_vol}[fx]")
    fc.append("[v][bd][fx]amix=inputs=3:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=9[a]")
    subprocess.run([FF, "-y", "-loglevel", "error", *ins, "-filter_complex", ";".join(fc), "-map", "0:v", "-map", "[a]",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out], check=True)
    print(f"{out} | {len(cs)} effects ({len(cs) / dur * 60:.1f}/min): " + ", ".join(f"{n}@{t:.1f}" for n, t in cs))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        c = cues({"keys": [{"t": 0, "o2": 100}, {"t": 5, "o2": 80}, {"t": 7, "o2": 70}, {"t": 9, "o2": 20}], "events": [{"t": 7, "text": "CHOICE LOCKED · B"}]}, [3.0])
        assert [n for n, _ in c] == ["beep", "sonar", "beep", "lock", "alarm"], c
        print("ok"); sys.exit()
    a = sys.argv[1:]; opt = lambda k, d: a[a.index(k) + 1] if k in a else d
    pos = [x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or not a[i - 1].startswith("--"))]
    main(*pos[:4], [float(x) for x in opt("--sonar", "").split(",") if x], float(opt("--bed-vol", 0.22)), float(opt("--fx-vol", 0.55)))
