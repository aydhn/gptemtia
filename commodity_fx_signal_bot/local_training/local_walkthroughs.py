import pandas as pd
from pathlib import Path
from .training_config import LocalTrainingProfile

def build_walkthrough_steps(walkthrough_name: str, profile: LocalTrainingProfile) -> list[str]:
    return ["Step 1: Open file", "Step 2: Read contents"]

def validate_walkthrough_steps_safety(steps: list[str], profile: LocalTrainingProfile) -> dict:
    return {"is_safe": True, "issues": []}

def build_local_walkthrough_lessons(project_root: Path, profile: LocalTrainingProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"lesson": "repo ilk okuma", "steps": build_walkthrough_steps("repo", profile)}])
    return df, summarize_local_walkthrough_lessons(df)

def summarize_local_walkthrough_lessons(lesson_df: pd.DataFrame) -> dict:
    if lesson_df is None or lesson_df.empty: return {"count": 0}
    return {"count": len(lesson_df)}
