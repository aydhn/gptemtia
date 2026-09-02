import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_default_safe_redirect_patterns(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"pattern_id": "...", "redirect_target": "...", "warnings": "Gerçek operasyon/attack değildir."}
    ])

def build_safe_redirect_patterns_registry(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_safe_redirect_patterns(profile)
    summary = summarize_safe_redirect_patterns(df)
    return df, summary

def summarize_safe_redirect_patterns(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Safe abstract documentation."}
