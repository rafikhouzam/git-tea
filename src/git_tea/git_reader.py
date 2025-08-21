
import subprocess, datetime, re
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Commit:
    hash: str
    author: str
    email: str
    dt: datetime.datetime
    subject: str
    files: int
    added: int
    removed: int
    top_file: str

def _run(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)

def latest_commits(since: Optional[str] = None, maxn: int = 200) -> List[Commit]:
    """
    Parse git log with numstat. Returns commits in chronological order (newest first).
    """
    range_flag = f' --since="{since}"' if since else ""
    fmt = "%H|%an|%ae|%cI|%s"
    raw = _run(f'git log --numstat --date=iso-strict --format="{fmt}"{range_flag} -n {maxn}')
    commits: List[Commit] = []
    cur: Optional[Commit] = None
    for line in raw.splitlines():
        if "|" in line and line.count("|")>=4:
            if cur:
                commits.append(cur)
            h,a,e,dt,sub = line.split("|",4)
            try:
                dtv = datetime.datetime.fromisoformat(dt.replace("Z","+00:00")).astimezone()
            except Exception:
                dtv = datetime.datetime.now()
            cur = Commit(h,a,e,dtv,sub,0,0,0,"")
        elif cur and "\t" in line:
            parts = line.split("\t")
            if len(parts) >= 3:
                add, rem, path = parts[0], parts[1], parts[2]
                if add.strip() != "-":
                    try: cur.added += int(add)
                    except: pass
                if rem.strip() != "-":
                    try: cur.removed += int(rem)
                    except: pass
                cur.files += 1
                if not cur.top_file:
                    cur.top_file = path
    if cur:
        commits.append(cur)
    return commits
