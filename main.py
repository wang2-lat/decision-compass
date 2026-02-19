import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from questionnaire import run_questionnaire
from scoring import calculate_scores, display_scores
from storage import save_decision, load_decisions

app = typer.Typer(help="Decision Compass - Make critical decisions with clarity")
console = Console()

@app.command()
def decide(
    decision_type: str = typer.Argument(..., help="Decision type: quit-job, cofounder, or project")
):
    """Start a new decision-making process"""
    valid_types = ["quit-job", "cofounder", "project"]
    if decision_type not in valid_types:
        console.print(f"[red]Invalid decision type. Choose from: {', '.join(valid_types)}[/red]")
        raise typer.Exit(1)
    
    console.print(Panel.fit(
        f"[bold cyan]Decision Compass: {decision_type.replace('-', ' ').title()}[/bold cyan]",
        subtitle="Answer honestly for best results"
    ))
    
    answers = run_questionnaire(decision_type, console)
    scores = calculate_scores(answers, decision_type)
    
    console.print("\n")
    display_scores(scores, console)
    
    final_decision = typer.prompt("\nYour final decision (go/no-go/wait)")
    notes = typer.prompt("Additional notes (optional)", default="")
    
    save_decision(decision_type, answers, scores, final_decision, notes)
    console.print("\n[green]Decision saved successfully![/green]")

@app.command()
def history(limit: int = typer.Option(10, help="Number of recent decisions to show")):
    """View decision history"""
    decisions = load_decisions(limit)
    
    if not decisions:
        console.print("[yellow]No decisions recorded yet.[/yellow]")
        return
    
    table = Table(title="Decision History", show_header=True)
    table.add_column("Date", style="cyan")
    table.add_column("Type", style="magenta")
    table.add_column("Decision", style="green")
    table.add_column("Risk Score", justify="right")
    table.add_column("Reward Score", justify="right")
    
    for d in decisions:
        table.add_row(
            d["timestamp"][:10],
            d["type"],
            d["final_decision"],
            f"{d['scores']['risk']:.1f}",
            f"{d['scores']['reward']:.1f}"
        )
    
    console.print(table)

@app.command()
def review(index: int = typer.Argument(..., help="Decision index to review (1-based)")):
    """Review a specific decision in detail"""
    decisions = load_decisions(100)
    
    if index < 1 or index > len(decisions):
        console.print(f"[red]Invalid index. Choose between 1 and {len(decisions)}[/red]")
        raise typer.Exit(1)
    
    d = decisions[index - 1]
    
    console.print(Panel.fit(
        f"[bold]{d['type'].replace('-', ' ').title()}[/bold]\n"
        f"Date: {d['timestamp']}\n"
        f"Decision: [green]{d['final_decision']}[/green]",
        title="Decision Review"
    ))
    
    console.print("\n[bold]Scores:[/bold]")
    for key, value in d["scores"].items():
        console.print(f"  {key.title()}: {value:.1f}/10")
    
    if d.get("notes"):
        console.print(f"\n[bold]Notes:[/bold]\n{d['notes']}")

if __name__ == "__main__":
    app()
