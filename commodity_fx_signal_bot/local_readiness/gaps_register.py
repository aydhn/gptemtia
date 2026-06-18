import pandas as pd
from pathlib import Path
from .readiness_config import LocalReadinessProfile

def build_known_gaps_register(project_root: Path, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"gap": "Initial gap assessment", "priority": "manual_review_medium"}])
    return df, summarize_known_gaps(df)

def collect_gaps_from_consistency_timeline_graph_metadata(project_root: Path) -> pd.DataFrame:
    return pd.DataFrame()

def classify_gap_priority(row: pd.Series) -> str:
    return "unknown_gap_priority"

def summarize_known_gaps(gap_df: pd.DataFrame) -> dict:
    return {"total_gaps": len(gap_df)}
