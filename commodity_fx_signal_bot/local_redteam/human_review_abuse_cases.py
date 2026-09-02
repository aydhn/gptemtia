import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_default_human_review_abuse_cases(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"case_id": "...", "trigger": "...", "warnings": "Gerçek operasyon/attack değildir."}
    ])

def build_human_review_abuse_case_checklist(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_human_review_abuse_cases(profile)
    summary = summarize_human_review_abuse_cases(df)
    return df, summary

def summarize_human_review_abuse_cases(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Safe abstract documentation."}
