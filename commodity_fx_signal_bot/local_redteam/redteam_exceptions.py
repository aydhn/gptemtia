import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def detect_redteam_exceptions(scenario_df: pd.DataFrame, checklist_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"exception_id": "exc_1", "desc": "Example exception"}])

def build_redteam_exception_register(scenario_df: pd.DataFrame, checklist_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = detect_redteam_exceptions(scenario_df, checklist_df, no_go_df)
    return df, summarize_redteam_exceptions(df)

def summarize_redteam_exceptions(exception_df: pd.DataFrame) -> dict:
    return {"total": len(exception_df)}
