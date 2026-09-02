import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_default_safety_non_goals(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"non_goal_id": "...", "desc": "...", "warnings": "Gerçek operasyon/attack değildir."}
    ])

def build_safety_non_goals_registry(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_safety_non_goals(profile)
    summary = summarize_safety_non_goals(df)
    return df, summary

def summarize_safety_non_goals(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Safe abstract documentation."}
