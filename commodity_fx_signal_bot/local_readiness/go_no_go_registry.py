import pandas as pd
from pathlib import Path
from .readiness_config import LocalReadinessProfile

def build_no_go_condition_registry(profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    conditions = [
        "raw secret output detected", "live/broker/deploy command present as safe",
        "investment advice claim present", "production release claim present",
        "model deployment claim present", "missing SAFE_USAGE_GUIDE",
        "missing OPERATOR_MANUAL", "missing consistency quality report",
        "missing secrets hygiene report", "destructive action recommendation present"
    ]
    df = pd.DataFrame({"condition": conditions, "status": "ok"})
    return df, summarize_go_no_go_conditions(df)

def build_safe_go_condition_registry(profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    conditions = [
        "all reports local-only", "dry-run default confirmed", "non-use policy present",
        "no raw secret confirmed", "no live/broker/deploy confirmed", "handoff manifest present",
        "final operator checklist present", "known gaps registered"
    ]
    df = pd.DataFrame({"condition": conditions, "status": "ok"})
    return df, summarize_go_no_go_conditions(df)

def evaluate_go_no_go_conditions(findings_df: pd.DataFrame, gate_df: pd.DataFrame, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {}

def summarize_go_no_go_conditions(go_df: pd.DataFrame) -> dict:
    return {"total_conditions": len(go_df)}
