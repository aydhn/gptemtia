import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile

def build_default_boundary_violation_scenarios(profile: LocalRedTeamProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"pattern_id": "pt_1", "description": "Boundary violation abstract scenario", "warnings": "Gerçek payload/attack içermez."}
    ])

def build_boundary_violation_scenario_registry(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_boundary_violation_scenarios(profile)
    summary = summarize_boundary_violation_scenarios(df)
    return df, summary

def summarize_boundary_violation_scenarios(df: pd.DataFrame) -> dict:
    return {"total": len(df), "note": "Abstract patterns only, no payload."}
