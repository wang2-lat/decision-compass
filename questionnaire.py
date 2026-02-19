from typing import Dict, List

QUESTIONS = {
    "quit-job": [
        "How many months of runway do you have? (1-10, 10=2+ years)",
        "How validated is your idea? (1-10, 10=paying customers)",
        "How strong is your current job security? (1-10, 10=very secure)",
        "How supportive is your family/partner? (1-10, 10=fully supportive)",
        "How clear is your business plan? (1-10, 10=very detailed)",
        "How much do you hate your current job? (1-10, 10=unbearable)",
        "How unique is your market opportunity? (1-10, 10=once in lifetime)",
    ],
    "cofounder": [
        "How long have you known this person? (1-10, 10=5+ years)",
        "How complementary are your skills? (1-10, 10=perfect match)",
        "How aligned are your visions? (1-10, 10=identical)",
        "How well do you handle conflicts together? (1-10, 10=excellent)",
        "How committed are they financially? (1-10, 10=all in)",
        "How much do you trust them with money? (1-10, 10=completely)",
        "How similar are your work ethics? (1-10, 10=identical)",
    ],
    "project": [
        "How much traction do you have? (1-10, 10=strong growth)",
        "How much have you invested so far? (1-10, 10=significant)",
        "How passionate are you about this? (1-10, 10=obsessed)",
        "How clear is the path to revenue? (1-10, 10=very clear)",
        "How strong is the competition? (1-10, 10=weak/none)",
        "How much time can you still commit? (1-10, 10=unlimited)",
        "How much learning have you gained? (1-10, 10=invaluable)",
    ]
}

def run_questionnaire(decision_type: str, console) -> Dict[str, float]:
    """Run questionnaire and collect answers"""
    questions = QUESTIONS[decision_type]
    answers = {}
    
    console.print("\n[bold]Answer each question on a scale of 1-10:[/bold]\n")
    
    for i, question in enumerate(questions, 1):
        while True:
            try:
                answer = console.input(f"[cyan]{i}. {question}[/cyan]\n   Your answer: ")
                score = float(answer)
                if 1 <= score <= 10:
                    answers[f"q{i}"] = score
                    break
                else:
                    console.print("[red]Please enter a number between 1 and 10[/red]")
            except ValueError:
                console.print("[red]Please enter a valid number[/red]")
    
    return answers
