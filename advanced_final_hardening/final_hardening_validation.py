# -*- coding: utf-8 -*-
"""Phase 159: Final Hardening Validation.

Validates all Phase 159 registries, contracts, runbooks, boundaries, and manifests
against strict non-production, no-live-trading, and non-signal constraints.
"""

from typing import Dict, List, Optional, Tuple, Union
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    VALIDATION_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

FORBIDDEN_RELEASE_CANDIDATE_CLAIMS: List[str] = [
    "production_ready=True",
    "production_ready: True",
    "broker_ready=True",
    "broker_ready: True",
    "live_trading_ready=True",
    "live_trading_ready: True",
    "official_approval=True",
    "official_approval: True",
    "live trade signal",
    "definite buy signal",
    "definite sell signal",
    "investment advice approved",
    "broker execution authorized",
    "live deployment authorized",
    "real order generated",
]


def validate_final_hardening_profile_registry(
    df: pd.DataFrame,
    profile: FinalHardeningProfile | None = None,
) -> Dict:
    """Validate profile registry DataFrame."""
    violations = []
    if df.empty:
        violations.append("Profile registry is empty")
    if "allow_live_trading" in df.columns and df["allow_live_trading"].any():
        violations.append("Found profile with allow_live_trading=True")
    if "local_only" in df.columns and not df["local_only"].all():
        violations.append("Found profile with local_only=False")

    return {"passed": len(violations) == 0, "violations": violations}


def validate_final_hardening_contracts(
    df: pd.DataFrame,
    profile: FinalHardeningProfile | None = None,
) -> Dict:
    """Validate hardening contracts DataFrame."""
    violations = []
    if df.empty:
        violations.append("Contracts DataFrame is empty")
    if "system_execution_allowed" in df.columns and df["system_execution_allowed"].any():
        violations.append("Contracts allow system execution")
    if "live_trading_allowed" in df.columns and df["live_trading_allowed"].any():
        violations.append("Contracts allow live trading")

    return {"passed": len(violations) == 0, "violations": violations}


def validate_operator_runbook_contracts(
    df: pd.DataFrame,
    profile: FinalHardeningProfile | None = None,
) -> Dict:
    """Validate operator runbook contracts DataFrame."""
    violations = []
    if df.empty:
        violations.append("Operator runbook DataFrame is empty")
    if "live_bot_execution_allowed" in df.columns and df["live_bot_execution_allowed"].any():
        violations.append("Runbook contracts allow live bot execution")

    return {"passed": len(violations) == 0, "violations": violations}


def validate_release_candidate_contracts(
    df: pd.DataFrame,
    profile: FinalHardeningProfile | None = None,
) -> Dict:
    """Validate release candidate contracts DataFrame."""
    violations = []
    if df.empty:
        violations.append("Release candidate contracts DataFrame is empty")
    if "production_ready" in df.columns and df["production_ready"].any():
        violations.append("Release candidate claims production_ready=True")
    if "broker_ready" in df.columns and df["broker_ready"].any():
        violations.append("Release candidate claims broker_ready=True")

    return {"passed": len(violations) == 0, "violations": violations}


def validate_release_candidate_boundaries(
    df_map: Dict[str, pd.DataFrame],
    profile: FinalHardeningProfile | None = None,
) -> Dict:
    """Validate release candidate no-go and go boundaries."""
    violations = []
    no_go_df = df_map.get("release_candidate_no_go_boundaries")
    if no_go_df is not None and not no_go_df.empty:
        if not no_go_df["enforced"].all():
            violations.append("Not all NO-GO boundaries are enforced")

    return {"passed": len(violations) == 0, "violations": violations}


def validate_release_candidate_manifest(
    df: pd.DataFrame,
    profile: FinalHardeningProfile | None = None,
) -> Dict:
    """Validate release candidate manifest DataFrame."""
    violations = []
    if df.empty:
        violations.append("Manifest DataFrame is empty")
    row = df.iloc[0].to_dict() if not df.empty else {}
    if row.get("current_phase") != 159:
        violations.append(f"Manifest current_phase is {row.get('current_phase')}, expected 159")
    if row.get("target_final_phase") != 160:
        violations.append(f"Manifest target_final_phase is {row.get('target_final_phase')}, expected 160")
    if row.get("production_ready", False):
        violations.append("Manifest production_ready must be False")
    if row.get("broker_ready", False):
        violations.append("Manifest broker_ready must be False")
    if row.get("live_trading_ready", False):
        violations.append("Manifest live_trading_ready must be False")
    if row.get("system_executed", False):
        violations.append("Manifest system_executed must be False")
    if row.get("model_training_executed", False):
        violations.append("Manifest model_training_executed must be False")
    if row.get("prediction_generated", False):
        violations.append("Manifest prediction_generated must be False")
    if row.get("artifact_persisted", False):
        violations.append("Manifest artifact_persisted must be False")
    if row.get("model_registry_written", False):
        violations.append("Manifest model_registry_written must be False")

    return {"passed": len(violations) == 0, "violations": violations}


def validate_no_forbidden_release_candidate_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict] = None,
) -> Dict:
    """Scan string or data structures for forbidden claims."""
    target_str = ""
    if text:
        target_str += text.lower() + " "
    if df is not None:
        target_str += df.to_string().lower() + " "
    if summary:
        target_str += str(summary).lower() + " "

    violations = []
    for claim in FORBIDDEN_RELEASE_CANDIDATE_CLAIMS:
        if claim.lower() in target_str:
            violations.append(f"Forbidden claim detected: '{claim}'")

    return {"passed": len(violations) == 0, "violations": violations}


def build_final_hardening_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build consolidated validation report across all Phase 159 components."""
    active_profile = profile or get_default_final_hardening_profile()

    checks = [
        ("profile_registry", validate_final_hardening_profile_registry(tables.get("profiles", pd.DataFrame()))),
        ("hardening_contracts", validate_final_hardening_contracts(tables.get("contracts", pd.DataFrame()))),
        ("operator_runbooks", validate_operator_runbook_contracts(tables.get("runbooks", pd.DataFrame()))),
        ("release_candidate_contracts", validate_release_candidate_contracts(tables.get("rc_contracts", pd.DataFrame()))),
        ("rc_manifest", validate_release_candidate_manifest(tables.get("manifest", pd.DataFrame()))),
        ("forbidden_claims", validate_no_forbidden_release_candidate_claims(df=tables.get("manifest"))),
    ]

    rows = []
    for name, res in checks:
        rows.append({
            "check_name": name,
            "passed": res["passed"],
            "violations_count": len(res.get("violations", [])),
            "violations": "; ".join(res.get("violations", [])) if res.get("violations") else "None",
            "domain": VALIDATION_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": "PASS" if res["passed"] else "FAIL",
        })

    df = pd.DataFrame(rows)
    all_passed = bool(df["passed"].all())
    summary = {
        "total_checks": len(rows),
        "passed_checks": int(df["passed"].sum()),
        "all_passed": all_passed,
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAIL",
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY if all_passed else "VALIDATION_FAILED",
    }
    return df, summary
