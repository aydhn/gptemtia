# -*- coding: utf-8 -*-
"""Phase 158: Full-System Integration Validation.

Validates all registries, checkpoints, contracts, manifests, and claims against strict governance rules.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile


def validate_full_system_integration_profile_registry(
    df: pd.DataFrame, profile: FullSystemIntegrationProfile
) -> Dict[str, Any]:
    """Validate profile registry compliance."""
    is_valid = (
        not df.empty
        and (df["current_phase"] == 158).all()
        and (df["target_final_phase"] == 160).all()
        and (df["next_phase"] == 159).all()
        and (df["non_signal"] == True).all()
        and (df["production_ready"] == False).all()
        and (df["broker_ready"] == False).all()
        and (df["live_trading_ready"] == False).all()
    )
    return {"rule": "profile_registry_valid", "passed": bool(is_valid), "non_signal": True}


def validate_system_component_checkpoints(
    df: pd.DataFrame, profile: FullSystemIntegrationProfile
) -> Dict[str, Any]:
    """Validate component checkpoints."""
    is_valid = (
        not df.empty
        and (df["contract_only"] == True).all()
        and (df["production_ready"] == False).all()
        and (df["broker_ready"] == False).all()
        and (df["live_ready"] == False).all()
    )
    return {"rule": "component_checkpoints_valid", "passed": bool(is_valid), "non_signal": True}


def validate_system_contract_integration(
    df: pd.DataFrame, profile: FullSystemIntegrationProfile
) -> Dict[str, Any]:
    """Validate integrated contracts."""
    is_valid = (
        not df.empty
        and (df["contract_only"] == True).all()
        and (df["zero_execution_guaranteed"] == True).all()
    )
    return {"rule": "contract_integration_valid", "passed": bool(is_valid), "non_signal": True}


def validate_advanced_acceptance_rehearsal(
    df: pd.DataFrame, profile: FullSystemIntegrationProfile
) -> Dict[str, Any]:
    """Validate acceptance rehearsal checklist."""
    is_valid = (
        not df.empty
        and (df["is_satisfied"] == True).all()
        and (df["zero_execution_verified"] == True).all()
    )
    return {"rule": "acceptance_rehearsal_valid", "passed": bool(is_valid), "non_signal": True}


def validate_system_boundaries(
    df_map: Dict[str, pd.DataFrame], profile: FullSystemIntegrationProfile
) -> Dict[str, Any]:
    """Validate all boundary dataframes."""
    all_passed = True
    for name, df in df_map.items():
        if df is not None and not df.empty and "is_allowed" in df.columns:
            # At least one prohibited rule must be enforced
            if (df["is_allowed"] == False).sum() == 0:
                all_passed = False
    return {"rule": "system_boundaries_valid", "passed": all_passed, "non_signal": True}


def validate_full_system_integration_manifest(
    df: pd.DataFrame, profile: FullSystemIntegrationProfile
) -> Dict[str, Any]:
    """Validate master manifest invariants."""
    if df.empty:
        return {"rule": "manifest_valid", "passed": False, "non_signal": True}

    row = df.iloc[0]
    is_valid = (
        int(row.get("current_phase", 0)) == 158
        and int(row.get("target_final_phase", 0)) == 160
        and int(row.get("next_phase", 0)) == 159
        and bool(row.get("full_system_integration_completed")) is True
        and bool(row.get("system_executed")) is False
        and bool(row.get("end_to_end_run_executed")) is False
        and bool(row.get("live_trading_executed")) is False
        and bool(row.get("broker_execution_executed")) is False
        and bool(row.get("order_generation_executed")) is False
        and bool(row.get("signal_generation_executed")) is False
        and bool(row.get("model_training_executed")) is False
        and bool(row.get("prediction_generated")) is False
        and bool(row.get("backtest_executed")) is False
        and bool(row.get("portfolio_executed")) is False
        and bool(row.get("risk_executed")) is False
        and bool(row.get("scenario_executed")) is False
        and bool(row.get("production_deployed")) is False
        and bool(row.get("source_preserved")) is True
        and bool(row.get("manual_review_required")) is True
    )
    return {"rule": "manifest_valid", "passed": bool(is_valid), "non_signal": True}


def validate_no_forbidden_full_system_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Validate that text, data, or summary does not contain forbidden claims."""
    forbidden_terms = [
        "live trade executed",
        "broker connected",
        "official approval granted",
        "production ready",
        "broker ready",
        "trading recommendation",
    ]
    found = []
    blob = ""
    if text:
        blob += text.lower()
    if summary:
        blob += str(summary).lower()
    if df is not None:
        blob += df.to_string().lower()

    for term in forbidden_terms:
        if term in blob:
            found.append(term)

    return {
        "rule": "no_forbidden_claims",
        "passed": len(found) == 0,
        "found_terms": found,
        "non_signal": True,
    }


def build_full_system_integration_validation_report(
    tables: Dict[str, Any], profile: FullSystemIntegrationProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build consolidated validation report across all Phase 158 components."""
    checks = []

    if "profiles" in tables:
        checks.append(validate_full_system_integration_profile_registry(tables["profiles"], profile))
    if "checkpoints" in tables:
        checks.append(validate_system_component_checkpoints(tables["checkpoints"], profile))
    if "contracts" in tables:
        checks.append(validate_system_contract_integration(tables["contracts"], profile))
    if "rehearsal" in tables:
        checks.append(validate_advanced_acceptance_rehearsal(tables["rehearsal"], profile))
    if "manifest" in tables:
        checks.append(validate_full_system_integration_manifest(tables["manifest"], profile))

    checks.append(validate_no_forbidden_full_system_claims(summary=tables.get("summary")))

    df = pd.DataFrame(checks)
    all_passed = bool(df["passed"].all()) if not df.empty else True

    summary = {
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "passed_rules": int((df["passed"] == True).sum()),
        "all_passed": all_passed,
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAIL",
        "status": "full_system_integration_ready" if all_passed else "validation_blocked",
        "non_signal": True,
    }
    return df, summary
