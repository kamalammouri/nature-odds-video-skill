# depth-theory-video — Claude Code skill

A [Claude Code](https://claude.com/claude-code) skill for faceless ocean-predator explainers in the
"Why You'd Never Want To Meet A [Animal]" format: you, a tiny diver, facing a huge animal, with real
records, a real human encounter, "What would you actually do?" and a final twist. The norms were
measured on all 7 videos of @depththeoryofficial (8 Nov 2026) with yt-dlp, faster-whisper, librosa,
scenedetect and [rea-video](https://github.com/JuneYaooo/rea-video). The skill holds the method, not a topic.
The docs are in French; the scripts produce an American-English video.

## It inherits ancient-humans-video

This skill holds only what differs. The whole production pipeline comes from
[ancient-humans-video-skill](https://github.com/kamalammouri/ancient-humans-video-skill): its scripts
(ElevenLabs voice, Google Flow images through Playwright, HyperFrames edit, Real SFX, YouTube analysis)
and its agent briefs are called by path, never copied. Install both.

## Layout

- `SKILL.md` — workflow, token-saving rules, rea-video analysis.
- `references/norms.md` — measured channel norms: voice, script, editing, sound, titles, description,
  images, thumbnail, rea-video breakdown.
- `references/agents.md` — what changes in each agent brief, and which model runs it.
- `scripts/thumb_depth.py` — thumbnail text (white, last word red) and red curved arrow; `--selftest`.
- `scripts/meta_digest.py` — compact digest of a channel's yt-dlp `.info.json` files.
- Image style `depth-flat` lives in ancient-humans-video's `scripts/styles.json`.

## Install

```bash
git clone https://github.com/kamalammouri/ancient-humans-video-skill ~/.claude/skills/ancient-humans-video
git clone https://github.com/kamalammouri/depth-theory-video-skill ~/.claude/skills/depth-theory-video
```

Optional, to break reference videos down: `git clone https://github.com/JuneYaooo/rea-video ~/.local/src/rea-video`
then `python -m pip install -e ~/.local/src/rea-video` (needs ffmpeg). Run it with `PYTHONUTF8=1` on Windows.

Then ask Claude Code something like "make a Depth Theory style video about the tiger shark".

## Use responsibly

The skill learns a format (structure, pacing, packaging); it never reuses the reference channel's
footage, narration or wording. Credit every real photo or clip you use and check its license.

## License

MIT
