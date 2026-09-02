import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile

def detect_forbidden_training_command_terms(command: str) -> list[str]:
    forbidden = ["buy", "sell", "live", "broker", "deploy", "daemon", "server", "delete", "rm ", "move", "overwrite", "upload", "cloud", "restore --apply", "backup --apply", "real market download", "scraping"]
    found = []
    for f in forbidden:
        if f in command.lower():
            found.append(f)
    return found

def classify_training_command_safety(command: str) -> dict:
    terms = detect_forbidden_training_command_terms(command)
    return {"is_safe": len(terms) == 0, "forbidden_terms": terms}

def build_safe_command_lesson_registry(project_root: Path, profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    commands = ["python -m scripts.run_maintenance_status", "python -m scripts.run_readiness_quality_report"]
    data = []
    for c in commands:
        data.append({"command": c, **classify_training_command_safety(c)})
    df = pd.DataFrame(data)
    return df, summarize_command_lessons(df)

def summarize_command_lessons(command_df: pd.DataFrame) -> dict:
    if command_df is None or command_df.empty: return {"count": 0}
    return {"count": len(command_df)}
