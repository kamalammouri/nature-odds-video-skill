"""Clone guard: is a draft (script, title, description) ours, or too close to a reference channel?
python originality.py draft.md [--title "Can You Survive ...?"] [--ref <dir of *.txt transcripts>] [--ref-titles channel.json]
Checks, exit 1 on any hit:
  1. signature phrases of the reference channel (built-in list below + --ban "phrase|phrase")
  2. 6-word sequences shared with the reference transcripts: > 1.5 % of the draft's 6-grams, or any 10-word run
  3. title closer than 0.6 (difflib) to a reference title
Reference transcripts are never shipped with the skill (copyright): point --ref at your local analysis folder."""
import difflib, glob, json, os, re, sys

BANNED = [  # Depth Theory's own wording and packaging (measured 8 Nov 2026), not ideas: say it another way
    "why you'd never want to meet", "why you never want to meet", "would a great white survive", "every prehistoric ocean",
    "picture this", "i do actually read them", "thanks for watching this one", "what would you actually do",
    "the real danger", "it hears you", "it sees you", "it hunts you", "won't hunt you", "you're next",
    "the animal nothing hunts", "the ocean's deadliest predator never hunts you",
]


def words(t): return re.findall(r"[a-z0-9']+", t.lower().replace("’", "'"))


def grams(ws, n): return {tuple(ws[i:i + n]) for i in range(len(ws) - n + 1)}


def check(draft, title=None, ref_texts=(), ref_titles=(), extra_ban=()):
    hits, low = [], " ".join(words(draft + " " + (title or "")))
    for p in BANNED + list(extra_ban):
        if " ".join(words(p)) in low: hits.append(f'signature phrase: "{p}"')
    dw = words(draft)
    if ref_texts and len(dw) >= 6:
        ref = set().union(*(grams(words(t), 6) for t in ref_texts))
        mine = grams(dw, 6); shared = mine & ref
        if len(shared) / max(1, len(mine)) > 0.015: hits.append(f"6-gram overlap {len(shared) / len(mine):.1%} (> 1.5 %)")
        ref10 = set().union(*(grams(words(t), 10) for t in ref_texts))
        for g in sorted(grams(dw, 10) & ref10)[:5]: hits.append('10-word run copied: "' + " ".join(g) + '"')
    for rt in ref_titles if title else ():
        r = difflib.SequenceMatcher(None, title.lower(), rt.lower()).ratio()
        if r > 0.6: hits.append(f'title {r:.2f} close to "{rt}"')
    return hits


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        ref = ["So let's talk about why you'd never want to be in the water with one of these huge animals today."]
        assert check("Picture this. A whale.")
        assert check("so let's talk about why you'd never want to be in the water with one", ref_texts=ref)
        assert check("x", title="Why You'd Never Want To Meet A Tiger Shark", ref_titles=["Why You'd Never Want To Meet A Sperm Whale"])
        assert check("Level one. Your oxygen reads ninety percent and the water is warm.", title="Can You Survive 60 Seconds Next To A Tiger Shark?",
                     ref_texts=ref, ref_titles=["Why You'd Never Want To Meet A Sperm Whale"]) == []
        print("ok"); sys.exit()
    a = sys.argv[1:]; opt = lambda k: a[a.index(k) + 1] if k in a else None
    path = next(x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or not a[i - 1].startswith("--")))
    draft = open(path, encoding="utf-8").read()
    texts = [open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(opt("--ref"), "*.txt"))] if opt("--ref") else []
    titles = [v["title"] for v in json.load(open(opt("--ref-titles"), encoding="utf-8"))] if opt("--ref-titles") else []
    hits = check(draft, opt("--title"), texts, titles, (opt("--ban") or "").split("|") if opt("--ban") else ())
    print("\n".join(hits) if hits else f"original: 0 hit ({len(words(draft))} words checked against {len(texts)} transcripts)")
    sys.exit(1 if hits else 0)
