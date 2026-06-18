import pandas as pd
from pathlib import Path
from .readiness_config import LocalReadinessProfile

def build_manual_review_register(project_root: Path, gap_df: pd.DataFrame | None, limitations_df: pd.DataFrame | None, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"review_item": "Initial manual review", "status": "pending"}])
    return df, summarize_manual_review_register(df)

def prioritize_manual_review_items(review_df: pd.DataFrame) -> pd.DataFrame:
    return review_df

def summarize_manual_review_register(review_df: pd.DataFrame) -> dict:
    return {"total_review_items": len(review_df)}
