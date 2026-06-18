import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def validate_consistency_check_registry(check_df: pd.DataFrame, profile: LocalConsistencyProfile) -> dict:
    return {}

def validate_consistency_findings(findings_df: pd.DataFrame, profile: LocalConsistencyProfile) -> dict:
    return {}

def validate_contradiction_report(contradiction_df: pd.DataFrame, profile: LocalConsistencyProfile) -> dict:
    return {}

def validate_reference_report(reference_df: pd.DataFrame, profile: LocalConsistencyProfile) -> dict:
    return {}

def validate_reconciliation_plan(plan_df: pd.DataFrame, profile: LocalConsistencyProfile) -> dict:
    return {}

def validate_no_auto_fix_or_live_usage(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    return {}

def build_consistency_validation_report(tables: dict[str, pd.DataFrame], profile: LocalConsistencyProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame(), {"warnings": []}
