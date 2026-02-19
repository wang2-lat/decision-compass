from typing import Dict
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn

def calculate_scores(answers: Dict[str, float], decision_type: str) -> Dict[str, float]:
    """Calculate risk, reward, and timing scores"""
    values = list(answers.values())
    
    if decision_type == "quit-job":
        risk = 10 - (values[0] + values[2] + values[3]) / 3
        reward = (values[1] + values[4] + values[6]) / 3
        timing = (values[5] + values[6]) / 2
    elif decision_type == "cofounder":
        risk = 10 - (values[0] + values[3] + values[5]) / 3
        reward = (values[1] + values[2] + values[6]) / 3
        timing = (values[4] + values[6]) / 2
    else:  # project
        risk = 10 - (values[0] + values[3] + values[4]) / 3
        reward = (values[2] + values[6]) / 2
        timing = (values[1] + values[5]) / 2
    
    confidence = sum(values) / len(values)
    
    return {
        "risk": round(risk, 1),
        "reward": round(reward, 1),
        "timing": round(timing, 1),
        "confidence": round(confidence, 1)
    }

def display_scores(scores: Dict[str, float], console):
    """Display scores with visual bars"""
    console.print(Panel.fit("[bold]Decision Analysis[/bold]", style="cyan"))
    
    with Progress(
        TextColumn("[bold]{task.description}"),
        BarColumn(bar_width=30),
        TextColumn("[bold]{task.fields[score]}/10"),
        console=console
    ) as progress:
        for key, value in scores.items():
            color = "red" if key == "risk" else "green"
            task = progress.add_task(
                f"[{color}]{key.title():12}[/{color}]",
                total=10,
                score=value
            )
            progress.update(task, completed=value)
    
    recommendation = get_recommendation(scores)
    console.print(f"\n[bold yellow]Recommendation:[/bold yellow] {recommendation}")

def get_recommendation(scores: Dict[str, float]) -> str:
    """Generate recommendation based on scores"""
    if scores["risk"] > 7:
        return "HIGH RISK - Consider waiting or reducing risk factors"
    elif scores["reward"] < 4:
        return "LOW REWARD - May not be worth the effort"
    elif scores["timing"] < 4:
        return "POOR TIMING - Consider delaying this decision"
    elif scores["confidence"] > 7 and scores["reward"] > 6:
        return "GO FOR IT - Strong indicators for moving forward"
    else:
        return "PROCEED WITH CAUTION - Gather more information"
