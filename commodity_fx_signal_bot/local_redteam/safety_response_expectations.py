import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_default_safety_response_expectations(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"expectation_id": "...", "scenario": "...", "warnings": "Gerçek operasyon/attack değildir."}
    ])

def build_safety_response_expectations_registry(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_safety_response_expectations(profile)
    summary = summarize_safety_response_expectations(df)
    return df, summary

def summarize_safety_response_expectations(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Safe abstract documentation."}
