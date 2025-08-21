import yaml, pathlib, random
from .signals import heat_score, heat_word

TONE_DIR = pathlib.Path(__file__).parent / "tonepacks"

def load_tone(name: str):
    path = TONE_DIR / f"{name}.yml"
    if not path.exists():
        raise ValueError(f"Tone pack '{name}' not found at {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def render_one(commit, tone):
    """Pick a random one_liner and fill it."""
    one_liners = tone.get("one_liners", [])
    if not one_liners:
        return f"{commit.author} committed '{commit.subject}'"
    template = random.choice(one_liners)
    return template.format(
        author=commit.author,
        added=commit.added,
        removed=commit.removed,
        files=commit.files,
        top_file=commit.top_file or "various files",
        subject=commit.subject,
        time_local=commit.dt.strftime("%-I:%M %p"),
        heat=heat_score(commit),
        heat_word=heat_word(heat_score(commit)),
        date=commit.dt.strftime("%Y-%m-%d"),
    )
