import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_default_manual_escalation_items(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"item_id": "...", "trigger": "...", "warnings": "Gerçek operasyon/attack değildir."}
    ])

def build_manual_escalation_checklist(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_manual_escalation_items(profile)
    summary = summarize_manual_escalation_items(df)
    return df, summary

def summarize_manual_escalation_items(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Safe abstract documentation."}
