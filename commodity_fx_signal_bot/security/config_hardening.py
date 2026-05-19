import pandas as pd
from security.security_config import SecurityProfile
from security.security_models import SecurityFinding, build_security_finding_id

def check_boolean_safe_defaults(settings_obj: object, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]:
    return [], {"issues_found": 0}

def check_live_trading_flags(settings_obj: object, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]:
    findings = []
    summary = {"issues_found": 0}
    for attr in dir(settings_obj):
        if attr.startswith("_"): continue
        if "live_trading" in attr.lower() or "broker_credential" in attr.lower() or attr.startswith("broker_"):
            val = getattr(settings_obj, attr)
            if isinstance(val, bool) and val is True:
                if (attr == "live_trading_enabled" and not profile.allow_live_trading) or \
                   (attr == "security_allow_live_trading" and not profile.allow_live_trading) or \
                   ("broker" in attr.lower() and not profile.allow_broker_credentials):
                    findings.append(SecurityFinding(
                        finding_id=build_security_finding_id("config_hardening", f"unsafe_live_flag_{attr}"),
                        category="config_hardening", severity="critical", status="security_failed",
                        title=f"Unsafe live trading flag: {attr}", description=f"Setting {attr} is True, which violates the security profile.",
                        recommended_action=f"Set {attr} to False", blocking=profile.fail_on_unsafe_live_flags
                    ))
                    summary["issues_found"] += 1
    return findings, summary

def check_telegram_flags(settings_obj: object, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]:
    findings = []
    summary = {"issues_found": 0}
    if hasattr(settings_obj, "telegram_enabled") and getattr(settings_obj, "telegram_enabled") is True:
        if not profile.allow_telegram_send:
            findings.append(SecurityFinding(
                finding_id=build_security_finding_id("config_hardening", "telegram_enabled_without_profile_permission"),
                category="config_hardening", severity="warning" if profile.enabled else "low", status="security_warning",
                title="Telegram enabled without profile permission", description="telegram_enabled is True, but profile.allow_telegram_send is False.",
                recommended_action="Set telegram_enabled to False or use a profile that allows it.", blocking=False
            ))
            summary["issues_found"] += 1
        if hasattr(settings_obj, "telegram_dry_run") and getattr(settings_obj, "telegram_dry_run") is False:
             if profile.require_dry_run_defaults:
                  findings.append(SecurityFinding(
                        finding_id=build_security_finding_id("config_hardening", "telegram_live_send_violation"),
                        category="config_hardening", severity="high", status="security_failed",
                        title="Telegram live send violation", description="telegram_dry_run is False while profile.require_dry_run_defaults is True.",
                        recommended_action="Set telegram_dry_run to True.", blocking=profile.fail_on_unsafe_live_flags
                    ))
                  summary["issues_found"] += 1
    return findings, summary

def check_network_related_flags(settings_obj: object, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]:
    return [], {"issues_found": 0}
def check_file_write_flags(settings_obj: object, profile: SecurityProfile) -> tuple[list[SecurityFinding], dict]:
    return [], {"issues_found": 0}

def build_config_hardening_report(settings_obj: object, profile: SecurityProfile) -> tuple[pd.DataFrame, dict]:
    findings = []
    f1, _ = check_live_trading_flags(settings_obj, profile)
    f2, _ = check_telegram_flags(settings_obj, profile)
    findings.extend(f1); findings.extend(f2)
    from security.security_models import security_finding_to_dict
    df = pd.DataFrame([security_finding_to_dict(f) for f in findings]) if findings else pd.DataFrame(columns=["finding_id"])
    return df, {"total_findings": len(findings)}
