import click
from rich.console import Console
from .git_reader import latest_commits
from .render import to_md, to_json
from .tones import load_tone, render_one

console = Console()

@click.command(context_settings={"help_option_names": ["-h","--help"]})
@click.option("--since", default=None, help="e.g. '24 hours ago', '7 days ago'")
@click.option("--tone", default="tabloid", help="Tone pack name (yml in tonepacks/)")
@click.option("--format", "fmt", default="text", type=click.Choice(["text","md","json"]), help="Output format")
@click.option("--top", default=1, show_default=True, help="How many spicy items to show")
def main(since, tone, fmt, top):
    """Spill the tea on your repo: gossip from git history."""
    commits = latest_commits(since)
    if not commits:
        console.print("[yellow]No tea to spill ☕ (no commits found).[/yellow]")
        return

    if fmt == "text":
        tonepack = load_tone(tone)
        for c in commits[:top]:
            console.print(render_one(c, tonepack))
    elif fmt == "md":
        console.print(to_md(commits, top))
    else:
        console.print(to_json(commits, top))
