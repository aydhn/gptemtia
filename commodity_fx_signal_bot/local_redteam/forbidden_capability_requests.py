import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_default_forbidden_capability_requests(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"pattern_id": "pt_1", "description": "Forbidden capability abstract request", "warnings": "Gerçek payload/attack içermez."}
    ])

def build_forbidden_capability_request_registry(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_forbidden_capability_requests(profile)
    summary = summarize_forbidden_capability_requests(df)
    return df, summary

def summarize_forbidden_capability_requests(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Abstract patterns only, no payload."}
