import json
import os
from datetime import datetime
from typing import Dict, List

STORAGE_FILE = os.path.expanduser("~/.decision_compass.json")

def save_decision(decision_type: str, answers: Dict, scores: Dict, final_decision: str, notes: str):
    """Save decision to storage"""
    decisions = _load_all_decisions()
    
    decision_record = {
        "timestamp": datetime.now().isoformat(),
        "type": decision_type,
        "answers": answers,
        "scores": scores,
        "final_decision": final_decision,
        "notes": notes
    }
    
    decisions.append(decision_record)
    
    with open(STORAGE_FILE, "w") as f:
        json.dump(decisions, f, indent=2)

def load_decisions(limit: int = 10) -> List[Dict]:
    """Load recent decisions"""
    decisions = _load_all_decisions()
    return decisions[-limit:][::-1]

def _load_all_decisions() -> List[Dict]:
    """Load all decisions from storage"""
    if not os.path.exists(STORAGE_FILE):
        return []
    
    try:
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []
