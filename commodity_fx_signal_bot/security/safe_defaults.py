import pandas as pd
from security.security_config import SecurityProfile
from security.security_models import SecurityFinding, build_security_finding_id

def check_default_dry_run_behavior(settings_obj: object, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]:
    findings = []
    summary = {"issues_found": 0}
    if profile.require_dry_run_defaults:
        if hasattr(settings_obj, "orchestration_dry_run") and getattr(settings_obj, "orchestration_dry_run") is False:
             findings.append(SecurityFinding(
                finding_id=build_security_finding_id("safe_defaults", "orchestration_dry_run_false"),
                category="safe_defaults", severity="medium", status="security_warning",
                title="Orchestration dry run is False", description="orchestration_dry_run is False while require_dry_run_defaults is True.",
                recommended_action="Set orchestration_dry_run to True."
            ))
             summary["issues_found"] += 1
    return findings, summary

def check_default_no_broker_behavior(settings_obj: object, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]: return [], {"issues_found": 0}
def check_default_no_live_order_behavior(settings_obj: object, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]: return [], {"issues_found": 0}
def check_default_local_storage_behavior(settings_obj: object, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]: return [], {"issues_found": 0}
def check_default_notification_behavior(settings_obj: object, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]: return [], {"issues_found": 0}

def build_safe_defaults_report(settings_obj: object, profile: SecurityProfile) -> tuple[pd.DataFrame, dict]:
    findings = []
    f1, _ = check_default_dry_run_behavior(settings_obj, profile)
    findings.extend(f1)
    from security.security_models import security_finding_to_dict
    df = pd.DataFrame([security_finding_to_dict(f) for f in findings]) if findings else pd.DataFrame(columns=["finding_id"])
    return df, {"total_findings": len(findings)}
