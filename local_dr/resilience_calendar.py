import pandas as pd
from local_dr.profile import LocalDRProfile

def build_resilience_exercise_calendar(scenario_df: pd.DataFrame, drill_df: pd.DataFrame, profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"status": "ok"}

def build_restore_drill_review_schedule(drill_df: pd.DataFrame, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame()

def build_tabletop_review_schedule(scenario_df: pd.DataFrame, profile: LocalDRProfile) -> pd.DataFrame:
    return pd.DataFrame()

def summarize_resilience_calendar(calendar_df: pd.DataFrame) -> dict:
    return {"summary": "done"}
