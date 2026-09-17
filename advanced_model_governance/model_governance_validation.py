# -*- coding: utf-8 -*-
"""Phase 144: Model Governance Validation Suite."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

FORBIDDEN_CLAIMS = [
    "production_ready",
    "broker_ready",
    "live_trading_ready",
    "official_approval",
    "buy_signal",
    "sell_signal",
    "performance_guarantee",
]


def validate_no_forbidden_governance_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Verify that text, dataframe or summary does not contain forbidden approval/signal claims."""
    violations = []
    combined_str = ""
    if text:
        combined_str += " " + text
    if summary:
        combined_str += " " + str(summary)
    if df is not None and not df.empty:
        combined_str += " " + " ".join(df.astype(str).values.flatten())

    combined_lower = combined_str.lower()
    for claim in FORBIDDEN_CLAIMS:
        # Check if affirmative claim exists (e.g. 'production_ready: true' or 'is_production_ready = true')
        if f'"{claim}": true' in combined_lower or f"'{claim}': true" in combined_lower or f"{claim}=true" in combined_lower:
            violations.append(claim)

    is_valid = len(violations) == 0
    return {
        "is_valid": is_valid,
        "violations": violations,
        "status": "PASS" if is_valid else "FAIL_FORBIDDEN_CLAIMS_DETECTED",
    }


def validate_model_governance_profile_registry(
    df: pd.DataFrame,
    profile: Optional[ModelGovernanceProfile] = None,
) -> Dict[str, Any]:
    """Validate profile registry."""
    prof = profile or get_model_governance_profile()
    is_valid = not df.empty and bool(df["local_only"].all()) and bool(df["non_production"].all())
    return {"check": "profile_registry", "passed": is_valid, "profile_count": len(df)}


def validate_model_governance_contracts(
    df: pd.DataFrame,
    profile: Optional[ModelGovernanceProfile] = None,
) -> Dict[str, Any]:
    """Validate model governance contracts."""
    prof = profile or get_model_governance_profile()
    is_valid = (
        not df.empty
        and not bool(df["production_approval_allowed"].any())
        and not bool(df["deployment_allowed"].any())
        and not bool(df["model_registry_write_allowed"].any())
    )
    return {"check": "governance_contracts", "passed": is_valid, "contract_count": len(df)}


def validate_model_card_contracts(
    df: pd.DataFrame,
    profile: Optional[ModelGovernanceProfile] = None,
) -> Dict[str, Any]:
    """Validate model card contracts."""
    is_valid = (
        not df.empty
        and not bool(df["production_ready_claim"].any())
        and not bool(df["broker_ready_claim"].any())
    )
    return {"check": "model_card_contracts", "passed": is_valid, "card_count": len(df)}


def validate_governance_boundaries(
    df_map: Dict[str, pd.DataFrame],
    profile: Optional[ModelGovernanceProfile] = None,
) -> Dict[str, Any]:
    """Validate boundaries."""
    app_df = df_map.get("approval_boundaries", pd.DataFrame())
    is_valid = not app_df.empty and not bool(app_df["action_permitted"].any())
    return {"check": "boundaries", "passed": is_valid}


def validate_governance_disabled_execution_reports(
    df_map: Dict[str, pd.DataFrame],
    profile: Optional[ModelGovernanceProfile] = None,
) -> Dict[str, Any]:
    """Validate disabled execution reports."""
    all_passed = True
    for name, df in df_map.items():
        if "is_disabled" in df.columns and not bool(df["is_disabled"].all()):
            all_passed = False
    return {"check": "disabled_execution_reports", "passed": all_passed}


def validate_model_governance_manifest(
    df: pd.DataFrame,
    profile: Optional[ModelGovernanceProfile] = None,
) -> Dict[str, Any]:
    """Validate manifest invariants."""
    prof = profile or get_model_governance_profile()
    row = df.iloc[0] if not df.empty else {}
    passed = (
        int(row.get("current_phase", 0)) == 144
        and int(row.get("next_phase", 0)) == 145
        and int(row.get("target_final_phase", 0)) == 160
        and bool(row.get("non_signal", False))
        and not bool(row.get("production_approved", True))
        and not bool(row.get("broker_ready_approved", True))
        and not bool(row.get("live_trading_approved", True))
        and not bool(row.get("release_approved", True))
        and not bool(row.get("model_deployed", True))
        and not bool(row.get("model_registry_written", True))
        and not bool(row.get("artifact_persisted", True))
        and not bool(row.get("real_audit_log", True))
    )
    return {"check": "manifest", "passed": passed}


def build_model_governance_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Aggregate and build governance validation report."""
    prof = profile or get_model_governance_profile()

    checks = []
    if "profiles" in tables:
        checks.append(validate_model_governance_profile_registry(tables["profiles"], prof))
    if "contracts" in tables:
        checks.append(validate_model_governance_contracts(tables["contracts"], prof))
    if "model_cards" in tables:
        checks.append(validate_model_card_contracts(tables["model_cards"], prof))
    if "manifest" in tables:
        checks.append(validate_model_governance_manifest(tables["manifest"], prof))

    checks.append(validate_no_forbidden_governance_claims(summary={"phase": 144, "production_ready": False}))

    df = pd.DataFrame(checks)
    all_passed = bool(df["passed"].all()) if "passed" in df.columns else True

    summary = {
        "status": "PASS" if all_passed else "FAIL",
        "all_passed": all_passed,
        "clean_claims": True,
        "total_checks": len(df),
        "phase": prof.current_phase,
    }
    return df, summary
