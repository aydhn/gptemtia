import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_default_safe_refusal_templates(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"template_id": "...", "content": "...", "warnings": "Gerçek operasyon/attack değildir."}
    ])

def build_safe_refusal_templates_registry(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_safe_refusal_templates(profile)
    summary = summarize_safe_refusal_templates(df)
    return df, summary

def summarize_safe_refusal_templates(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Safe abstract documentation."}
