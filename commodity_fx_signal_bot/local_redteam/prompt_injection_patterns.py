import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_default_prompt_injection_patterns(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"pattern_id": "pt_1", "description": "Prompt injection risk abstract pattern", "warnings": "Gerçek payload/attack içermez."}
    ])

def build_prompt_injection_risk_pattern_registry(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_prompt_injection_patterns(profile)
    summary = summarize_prompt_injection_patterns(df)
    return df, summary

def summarize_prompt_injection_patterns(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Abstract patterns only, no payload."}
