import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_default_redteam_reading_order(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"order_index": "...", "document": "...", "warnings": "Gerçek operasyon/attack değildir."}
    ])

def build_redteam_reading_order(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_redteam_reading_order(profile)
    summary = summarize_redteam_reading_order(df)
    return df, summary

def summarize_redteam_reading_order(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Safe abstract documentation."}
