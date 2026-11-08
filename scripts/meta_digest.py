"""Compact digest of a channel's yt-dlp .info.json files (one block per video, a few lines each), so the
full JSON never enters the context. python meta_digest.py <dir> [--desc 400] [--json out.json]"""
import glob, json, os, sys

d = next(a for i, a in enumerate(sys.argv[1:], 1) if not a.startswith("--") and sys.argv[i - 1] not in ("--desc", "--json"))
n = int(sys.argv[sys.argv.index("--desc") + 1]) if "--desc" in sys.argv else 400
rows = []
for f in sorted(glob.glob(os.path.join(d, "*.info.json"))):
    v = json.load(open(f, encoding="utf-8"))
    if v.get("_type") == "playlist": continue
    rows.append({k: v.get(k) for k in ("id", "upload_date", "title", "duration", "view_count", "like_count", "comment_count", "tags", "description")}
                | {"chapters": [(int(c["start_time"]), c["title"]) for c in v.get("chapters") or []]})
for r in rows:
    print(f"\n# {r['upload_date']} {r['id']} | {r['duration']}s | {r['view_count']} v | {r['like_count']} L | {r['comment_count']} C")
    print(f"T: {r['title']}  ({len(r['title'])} car.)")
    print(f"TAGS({len(r['tags'] or [])}): {', '.join(r['tags'] or [])[:300]}")
    print("CH:", " / ".join(f"{s // 60}:{s % 60:02d} {t}" for s, t in r["chapters"]))
    print("D:", (r["description"] or "")[:n].replace("\n", " / "))
if "--json" in sys.argv: json.dump(rows, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
