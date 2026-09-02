import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_default_safety_blindspots(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"blindspot_id": "...", "desc": "...", "warnings": "Gerçek operasyon/attack değildir."}
    ])

def build_safety_blindspot_register(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_safety_blindspots(profile)
    summary = summarize_safety_blindspots(df)
    return df, summary

def summarize_safety_blindspots(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Safe abstract documentation."}
