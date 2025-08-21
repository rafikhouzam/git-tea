
import json, datetime
from typing import List
from .git_reader import Commit
from .signals import heat_score, heat_word

def to_text(commits: List[Commit], top: int = 1) -> str:
    commits = commits[:top]
    lines = []
    for c in commits:
        h = heat_score(c)
        lines.append(
            f"BREAKING: {c.author} dropped +{c.added}/-{c.removed} in {c.top_file or 'various files'} at {c.dt.strftime('%-I:%M %p')}. "
            f"Heat {h}/10 — {heat_word(h)}. Subject: “{c.subject}”"
        )
    return "\n".join(lines)

def to_md(commits: List[Commit], top: int = 5, title: str = "🗞️ Repo Tabloid") -> str:
    commits = commits[:top]
    out = [f"# {title}", "", f"_{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}_", ""]
    for c in commits:
        h = heat_score(c)
        out.append(f"- **{c.author}** • +{c.added}/-{c.removed} in `{c.top_file or 'various'}` • {c.dt:%Y-%m-%d %H:%M} • Heat **{h}/10** ({heat_word(h)})  ")
        out.append(f"  > {c.subject}")
    return "\n".join(out)

def to_json(commits: List[Commit], top: int = 5) -> str:
    rows = []
    for c in commits[:top]:
        h = heat_score(c)
        rows.append({
            "author": c.author,
            "added": c.added,
            "removed": c.removed,
            "files": c.files,
            "top_file": c.top_file,
            "subject": c.subject,
            "datetime": c.dt.isoformat(),
            "heat": h,
            "heat_word": heat_word(h),
        })
    return json.dumps(rows, indent=2)
