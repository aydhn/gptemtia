import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_default_safety_coverage_items(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"coverage_area": "...", "status": "...", "warnings": "Gerçek operasyon/attack değildir."}
    ])

def build_safety_coverage_matrix(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_safety_coverage_items(profile)
    summary = summarize_safety_coverage_matrix(df)
    return df, summary

def summarize_safety_coverage_matrix(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Safe abstract documentation."}
