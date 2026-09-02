import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_default_unsafe_output_patterns(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"pattern_id": "pt_1", "description": "Unsafe output pattern abstract description", "warnings": "Gerçek payload/attack içermez."}
    ])

def build_unsafe_output_pattern_registry(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_unsafe_output_patterns(profile)
    summary = summarize_unsafe_output_patterns(df)
    return df, summary

def summarize_unsafe_output_patterns(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Abstract patterns only, no payload."}
