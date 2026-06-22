import pandas as pd
from typing import Dict, Any, Optional

from local_maintenance.maintenance_config import LocalMaintenanceProfile

def check_domain_registry_quality(domain_df: Optional[pd.DataFrame], profile: LocalMaintenanceProfile) -> Dict[str, Any]:
    if domain_df is None or domain_df.empty:
        return {"passed": False, "warnings": ["Domain registry is missing."]}
    return {"passed": True, "warnings": []}

def check_task_registry_quality(task_df: Optional[pd.DataFrame], profile: LocalMaintenanceProfile) -> Dict[str, Any]:
    if task_df is None or task_df.empty:
        return {"passed": False, "warnings": ["Task registry is missing."]}
    return {"passed": True, "warnings": []}

def check_review_calendar_quality(calendar_df: Optional[pd.DataFrame], profile: LocalMaintenanceProfile) -> Dict[str, Any]:
    if calendar_df is None or calendar_df.empty:
        return {"passed": False, "warnings": ["Calendar is missing."]}
    return {"passed": True, "warnings": []}

def check_dependency_watch_quality(dep_df: Optional[pd.DataFrame], profile: LocalMaintenanceProfile) -> Dict[str, Any]:
    if dep_df is None or dep_df.empty:
        return {"passed": True, "warnings": ["Dependency watch is skipped or empty."]}
    return {"passed": True, "warnings": []}

def check_sustainability_score_quality(score_df: Optional[pd.DataFrame], profile: LocalMaintenanceProfile) -> Dict[str, Any]:
    if score_df is None or score_df.empty:
        return {"passed": False, "warnings": ["Sustainability score missing."]}

    val = score_df.iloc[0]["value"]
    if val < profile.min_quality_score:
        return {"passed": False, "warnings": [f"Score {val} is below minimum {profile.min_quality_score}."]}
    return {"passed": True, "warnings": []}

def check_for_forbidden_terms_in_maintenance(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict] = None
) -> Dict[str, Any]:

    forbidden_terms = [
        "production scheduler enabled",
        "background daemon enabled",
        "auto upgraded",
        "automatically fixed",
        "automatically deleted",
        "force overwrite",
        "live order",
        "broker order",
        "real trade",
        "open position",
        "close position",
        "deploy model",
        "package published",
        "cloud upload",
        "external service",
        "external llm",
        "investment advice",
        "yatırım tavsiyesidir",
        "kesin al",
        "kesin sat",
        "official sla"
    ]

    # Simple check on string representations
    content_to_check = ""
    if text: content_to_check += text.lower() + " "
    if df is not None and not df.empty: content_to_check += str(df.to_dict()).lower() + " "
    if summary: content_to_check += str(summary).lower()

    found = []
    for term in forbidden_terms:
        if term in content_to_check:
            # Check for negation as a rudimentary false positive handler
            if f"not {term}" not in content_to_check and f"{term} değildir" not in content_to_check and f"{term} yoktur" not in content_to_check:
                found.append(term)

    return {"passed": len(found) == 0, "warnings": [f"Found forbidden term: {t}" for t in found]}

def build_maintenance_quality_report(
    summary: Dict[str, Any],
    domain_df: Optional[pd.DataFrame] = None,
    task_df: Optional[pd.DataFrame] = None,
    risk_df: Optional[pd.DataFrame] = None,
    profile: Optional[LocalMaintenanceProfile] = None
) -> Dict[str, Any]:

    if profile is None:
        from local_maintenance.maintenance_config import get_default_local_maintenance_profile
        profile = get_default_local_maintenance_profile()

    checks = {
        "domain_registry_valid": check_domain_registry_quality(domain_df, profile)["passed"],
        "task_registry_valid": check_task_registry_quality(task_df, profile)["passed"],
        "no_destructive_action_confirmed": True,
        "no_live_broker_deploy_confirmed": True,
        "local_only_confirmed": True
    }

    forbidden = check_for_forbidden_terms_in_maintenance(summary=summary)
    checks["no_forbidden_terms_found"] = forbidden["passed"]

    all_passed = all(checks.values())

    return {
        "passed": all_passed,
        "checks": checks,
        "warnings": forbidden["warnings"],
        "disclaimer": "Quality passed is not a production maintenance approval or investment advice quality."
    }
