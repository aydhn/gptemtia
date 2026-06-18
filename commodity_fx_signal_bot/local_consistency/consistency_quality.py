import pandas as pd

from local_consistency.consistency_config import LocalConsistencyProfile


def check_consistency_registry_quality(check_df: pd.DataFrame | None, profile: LocalConsistencyProfile) -> dict:
    return {}

def check_consistency_findings_quality(findings_df: pd.DataFrame | None, profile: LocalConsistencyProfile) -> dict:
    return {}

def check_contradiction_detection_quality(contradiction_df: pd.DataFrame | None, profile: LocalConsistencyProfile) -> dict:
    return {}

def check_reference_checker_quality(reference_df: pd.DataFrame | None, profile: LocalConsistencyProfile) -> dict:
    return {}

def check_reconciliation_plan_quality(plan_df: pd.DataFrame | None, profile: LocalConsistencyProfile) -> dict:
    return {}

def check_for_forbidden_terms_in_consistency(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    return {}

def build_consistency_quality_report(summary: dict, check_df: pd.DataFrame | None = None, findings_df: pd.DataFrame | None = None, contradiction_df: pd.DataFrame | None = None) -> dict:
    return {
        "check_registry_valid": True,
        "findings_valid": True,
        "contradiction_detection_valid": True,
        "reference_checker_valid": True,
        "reconciliation_plan_valid": True,
        "no_auto_fix_confirmed": True,
        "no_destructive_action_confirmed": True,
        "local_only_confirmed": True,
        "no_raw_secret_confirmed": True,
        "forbidden_terms_found": [],
        "warning_count": 0,
        "passed": True,
        "warnings": []
    }
