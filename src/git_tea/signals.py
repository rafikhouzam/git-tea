
from .git_reader import Commit
import math

def heat_score(c: Commit) -> int:
    night = 2 if (c.dt.hour < 7 or c.dt.hour > 22) else 0
    size = min((c.added + c.removed) // 80, 7)
    drama = 0
    subj = c.subject.lower()
    for kw, pts in [("hotfix",3),("revert",3),("urgent",2),("temp",1),("wip",1),("hack",1)]:
        if kw in subj:
            drama = max(drama, pts)
    return max(0, min(10, size + drama + night))

def heat_word(score: int) -> str:
    buckets = [
        (2, "quiet whispers"),
        (4, "light buzz"),
        (6, "heating up"),
        (8, "scorching"),
        (10,"meltdown"),
    ]
    for cap, word in buckets:
        if score <= cap:
            return word
    return "???"
