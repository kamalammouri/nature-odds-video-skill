# oxygen-odds-video — Claude Code skill

A [Claude Code](https://claude.com/claude-code) skill for **Oxygen Odds**, an ocean survival-game channel:
every video is a run. You dive with 100 % oxygen, a neon HUD shows your gauge, depth and survival odds,
you choose A, B or C at each of five levels, and every choice is settled by a sourced fact about the
animal (sperm whale, tiger shark, giant squid, the Mariana Trench…). It ends on GAME OVER or YOU SURVIVED,
then a short debrief on what actually keeps people safe. The docs are in French; the videos are in
American English.

Four rotating formats (60 Seconds, Descent, Body Swap, Real Run) and a new HUD mechanic per episode keep
every video different, which is what YouTube's inauthentic-content policy asks for. A clone guard checks
every script, title and description against the channels studied during research, and a compliance
checklist (reused content, AI disclosure, licenses, safety, metadata) gates publication.

## It inherits ancient-humans-video

The production pipeline comes from
[ancient-humans-video-skill](https://github.com/kamalammouri/ancient-humans-video-skill): ElevenLabs voice,
Google Flow images through Playwright, the HyperFrames edit, Real SFX, YouTube analysis tools and the
agent briefs are called by path, never copied. Install both. The `oxygen-neon` image style lives in that
repo's `scripts/styles.json`.

## Layout

- `SKILL.md` — the three rules (original, never repetitive, YouTube-compliant), workflow, token-saving rules.
- `references/identity.md` — channel bible: player and narrator, formats, run structure, writing, visuals,
  sound, description template, Shorts.
- `references/agents.md` — per-agent changes and which model runs each one (incl. the Originality checker).
- `references/youtube-compliance.md` — pre-publication checklist with its sources.
- `references/reference-depth-theory.md` — market study of the niche: principles kept, forms never reused.
- `scripts/hud.py` — game HUD layer (oxygen bar, odds, depth, level, GAME OVER banners) for a HyperFrames
  project; `--selftest`.
- `scripts/thumb_oxygen.py` — thumbnail HUD (odds readout + oxygen bar); `--selftest`.
- `scripts/originality.py` — clone guard: signature phrases, shared 6/10-word runs, title similarity; `--selftest`.
- `scripts/meta_digest.py` — compact digest of a channel's yt-dlp `.info.json` files.

## Install

```bash
git clone https://github.com/kamalammouri/ancient-humans-video-skill ~/.claude/skills/ancient-humans-video
git clone https://github.com/kamalammouri/oxygen-odds-video-skill ~/.claude/skills/oxygen-odds-video
```

Optional, to break reference videos down: `git clone https://github.com/JuneYaooo/rea-video ~/.local/src/rea-video`
then `python -m pip install -e ~/.local/src/rea-video` (needs ffmpeg). Run it with `PYTHONUTF8=1` on Windows.

Then ask Claude Code something like "make an Oxygen Odds run about the tiger shark".

## Use responsibly

Research looks at other channels to learn why a niche works, never to copy their titles, thumbnails,
wording or footage; the clone guard enforces it. Credit every real photo or clip and check its license,
declare synthetic voice in YouTube Studio, and present survival odds as a game score, not a statistic.

## License

MIT
