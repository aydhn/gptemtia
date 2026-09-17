# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Validation Module."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_forbidden_column_policies import FORBIDDEN_COLUMNS


def validate_risk_reporting_profile_registry(df: pd.DataFrame, profile: RiskReportingProfile) -> Dict[str, Any]:
    errors = []
    if df.empty:
        errors.append("Profile registry is empty")
    if "non_production" in df.columns and not df["non_production"].all():
        errors.append("All profiles must be non_production=True")
    if "allow_live_trading" in df.columns and df["allow_live_trading"].any():
        errors.append("No profile may allow live trading")
    return {"is_valid": len(errors) == 0, "errors": errors}


def validate_risk_report_contracts(df: pd.DataFrame, profile: RiskReportingProfile) -> Dict[str, Any]:
    errors = []
    if df.empty:
        errors.append("Risk report contracts registry is empty")
    if "risk_reporting_execution_allowed" in df.columns and df["risk_reporting_execution_allowed"].any():
        errors.append("No contract may allow risk reporting execution")
    if "live_trading_allowed" in df.columns and df["live_trading_allowed"].any():
        errors.append("No contract may allow live trading")
    return {"is_valid": len(errors) == 0, "errors": errors}


def validate_exposure_attribution_contracts(df: pd.DataFrame, profile: RiskReportingProfile) -> Dict[str, Any]:
    errors = []
    if df.empty:
        errors.append("Exposure attribution contracts registry is empty")
    if "exposure_calculated" in df.columns and df["exposure_calculated"].any():
        errors.append("No contract may have exposure_calculated=True")
    if "allows_execution" in df.columns and df["allows_execution"].any():
        errors.append("No contract may allow execution")
    return {"is_valid": len(errors) == 0, "errors": errors}


def validate_limit_monitoring_contracts(df: pd.DataFrame, profile: RiskReportingProfile) -> Dict[str, Any]:
    errors = []
    if df.empty:
        errors.append("Limit monitoring contracts registry is empty")
    if "is_enforced_live" in df.columns and df["is_enforced_live"].any():
        errors.append("No contract may be enforced live")
    if "allows_alerting" in df.columns and df["allows_alerting"].any():
        errors.append("No contract may allow alerting")
    return {"is_valid": len(errors) == 0, "errors": errors}


def validate_risk_reporting_guards(df_map: Dict[str, pd.DataFrame], profile: RiskReportingProfile) -> Dict[str, Any]:
    errors = []
    for name, df in df_map.items():
        if df.empty:
            errors.append(f"Guard registry '{name}' is empty")
    return {"is_valid": len(errors) == 0, "errors": errors}


def validate_risk_reporting_manifest(df: pd.DataFrame, profile: RiskReportingProfile) -> Dict[str, Any]:
    errors = []
    if df.empty:
        errors.append("Manifest is empty")
    else:
        row = df.iloc[0]
        if row.get("current_phase") != 155:
            errors.append("current_phase must be 155")
        if row.get("target_final_phase") != 160:
            errors.append("target_final_phase must be 160")
        if row.get("next_phase") != 156:
            errors.append("next_phase must be 156")
        if bool(row.get("risk_report_generated")):
            errors.append("risk_report_generated must be False")
        if bool(row.get("exposure_attribution_generated")):
            errors.append("exposure_attribution_generated must be False")
        if bool(row.get("limit_monitoring_executed")):
            errors.append("limit_monitoring_executed must be False")
        if bool(row.get("metric_calculated")):
            errors.append("metric_calculated must be False")
        if bool(row.get("var_calculated")):
            errors.append("var_calculated must be False")
        if bool(row.get("expected_shortfall_calculated")):
            errors.append("expected_shortfall_calculated must be False")
        if bool(row.get("exposure_calculated")):
            errors.append("exposure_calculated must be False")
        if bool(row.get("alert_generated")):
            errors.append("alert_generated must be False")
        if bool(row.get("dashboard_generated")):
            errors.append("dashboard_generated must be False")
        if bool(row.get("portfolio_adjustment_generated")):
            errors.append("portfolio_adjustment_generated must be False")
        if bool(row.get("broker_order_sent")):
            errors.append("broker_order_sent must be False")
        if bool(row.get("live_order_sent")):
            errors.append("live_order_sent must be False")
    return {"is_valid": len(errors) == 0, "errors": errors}


def validate_no_forbidden_risk_reporting_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    violations = []
    check_str = ""
    if text:
        check_str += text.lower() + " "
    if df is not None and not df.empty:
        check_str += " ".join(str(c).lower() for c in df.columns) + " "
    if summary:
        check_str += str(summary).lower()

    for col in FORBIDDEN_COLUMNS:
        if f" {col} " in f" {check_str} " or f"'{col}'" in check_str or f'"{col}"' in check_str:
            violations.append(col)

    return {
        "is_safe": len(violations) == 0,
        "violations": violations,
        "action": "BLOCK" if violations else "ALLOW",
    }


def build_risk_reporting_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build composite validation report across all Phase 155 tables."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    checks = []
    if "profiles" in tables:
        v = validate_risk_reporting_profile_registry(tables["profiles"], profile)
        checks.append(("profiles_validation", v["is_valid"], v["errors"]))
    if "contracts" in tables:
        v = validate_risk_report_contracts(tables["contracts"], profile)
        checks.append(("contracts_validation", v["is_valid"], v["errors"]))
    if "exposure_contracts" in tables:
        v = validate_exposure_attribution_contracts(tables["exposure_contracts"], profile)
        checks.append(("exposure_contracts_validation", v["is_valid"], v["errors"]))
    if "limit_contracts" in tables:
        v = validate_limit_monitoring_contracts(tables["limit_contracts"], profile)
        checks.append(("limit_contracts_validation", v["is_valid"], v["errors"]))
    if "manifest" in tables:
        v = validate_risk_reporting_manifest(tables["manifest"], profile)
        checks.append(("manifest_validation", v["is_valid"], v["errors"]))

    rows = []
    for name, is_valid, errs in checks:
        rows.append({
            "check_name": name,
            "is_valid": is_valid,
            "error_count": len(errs),
            "errors": "; ".join(errs) if errs else "NONE",
            "current_phase": profile.current_phase,
            "target_final_phase": profile.target_final_phase,
            "next_phase": profile.next_phase,
        })

    df = pd.DataFrame(rows)
    all_passed = bool(df["is_valid"].all()) if not df.empty else True
    summary = {
        "total_checks": len(df),
        "all_passed": all_passed,
        "status": "RISK_REPORT_CONTRACT_READY" if all_passed else "VALIDATION_FAILED",
    }
    return df, summary
