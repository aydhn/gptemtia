
import pandas as pd
from local_dr.dr_config import LocalDRProfile

def build_restore_drill_review_schedule(drill_df: pd.DataFrame, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame([{"schedule": "dummy"}])

def build_tabletop_review_schedule(scenario_df: pd.DataFrame, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame([{"schedule": "dummy"}])

def build_resilience_exercise_calendar(scenario_df: pd.DataFrame, drill_df: pd.DataFrame, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"calendar": "dummy"}]), {"total": 1}

def summarize_resilience_calendar(calendar_df: pd.DataFrame) -> dict:
    return {"total": len(calendar_df)}
