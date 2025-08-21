# git-tea ☕

**Spill the tea on your repo.** `git-tea` turns your git history into cheeky tabloid one-liners and daily/weekly wrap-ups.

https://github.com/yourname/git-tea (replace with your repo)

## Install (dev)

```bash
pipx install -e .
# or
pip install -e .
```

## Usage

```bash
git tea                 # latest commit gossip
git tea --since 24h     # daily tabloid
git tea --since 7d      # weekly wrap
git tea --tone petty    # tone pack: tabloid | wholesome | petty
git tea --format md     # output format: text | md | json
git tea --top 5         # show top 5 spicy items
```

> Note: `git tea` works inside a git repo. It reads **local** history and never phones home.

## Examples

```bash
git add . && git commit -m "hotfix: patch prod"
git tea
# BREAKING: You dropped +123/-7 in api/router.py at 2:14 AM. Heat 8/10. Rumors of a secret launch swirl…
```

## Tones

Tones live in YAML at `git_tea/tonepacks/*.yml`. Ship PRs with new tones!

## GitHub Action (optional)

See `.github/workflows/gossip-on-merge.yml` for a comment bot that posts gossip on merged PRs.

## License

MIT
