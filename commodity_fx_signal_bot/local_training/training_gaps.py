import pandas as pd
from .training_config import LocalTrainingProfile

def detect_missing_training_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing domains", "type": "domain"}]) if domain_df is None or domain_df.empty else pd.DataFrame()

def detect_missing_role_paths(path_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing role paths", "type": "path"}]) if path_df is None or path_df.empty else pd.DataFrame()

def detect_missing_lessons(lesson_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing lessons", "type": "lesson"}]) if lesson_df is None or lesson_df.empty else pd.DataFrame()

def detect_missing_checklist_items(checklist_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing checklist items", "type": "checklist"}]) if checklist_df is None or checklist_df.empty else pd.DataFrame()

def build_training_gap_register(domain_df, path_df, lesson_df, checklist_df, profile):
    gaps = pd.concat([
        detect_missing_training_domains(domain_df),
        detect_missing_role_paths(path_df),
        detect_missing_lessons(lesson_df),
        detect_missing_checklist_items(checklist_df)
    ], ignore_index=True)
    if gaps.empty:
        gaps = pd.DataFrame(columns=["gap", "type"])
    return gaps, summarize_training_gaps(gaps)

def summarize_training_gaps(gap_df: pd.DataFrame) -> dict:
    if gap_df is None or gap_df.empty: return {"count": 0}
    return {"count": len(gap_df)}
