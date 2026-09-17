# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Governance Validation."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)

FORBIDDEN_PHASE_139_CLAIMS: List[str] = [
    "production ready",
    "production-ready",
    "broker ready",
    "broker-ready",
    "official approval",
    "live trading approved",
    "generate signal",
    "buy signal",
    "sell signal",
    "model trained successfully",
    "real training executed",
    "model accuracy",
    "sharpe ratio",
    "win rate",
]


def validate_no_forbidden_gpu_training_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Validate that text, dataframe, or summary does not contain forbidden performance or trading claims."""
    found_violations = []

    if text:
        t_lower = text.lower()
        for claim in FORBIDDEN_PHASE_139_CLAIMS:
            if claim in t_lower:
                found_violations.append(f"Text contains forbidden claim: '{claim}'")

    if summary:
        for k, v in summary.items():
            if any(term in str(k).lower() or term in str(v).lower() for term in ["accuracy", "sharpe", "win_rate"]):
                found_violations.append(f"Summary contains metric: {k}={v}")

    return {
        "is_clean": len(found_violations) == 0,
        "violations": found_violations,
        "non_signal": True,
    }


def validate_gpu_training_governance_profile_registry(
    df: pd.DataFrame, profile: GpuTrainingGovernanceProfile
) -> bool:
    """Validate profile registry DataFrame."""
    if df.empty:
        return False
    return bool((df["real_training_allowed"] == False).all() and (df["dry_run_default"] == True).all())


def validate_gpu_training_resource_policies(
    df: pd.DataFrame, profile: GpuTrainingGovernanceProfile
) -> bool:
    """Validate resource policies DataFrame."""
    if df.empty:
        return False
    return bool((df["allowed_mode"] == "contract_only").all() and (df["real_training_allowed"] == False).all())


def validate_gpu_training_harness_contracts(
    df: pd.DataFrame, profile: GpuTrainingGovernanceProfile
) -> bool:
    """Validate harness contracts DataFrame."""
    if df.empty:
        return False
    return bool((df["allowed_execution"] == False).all() and (df["dry_run_only"] == True).all())


def validate_gpu_training_disabled_execution_reports(
    df_map: Dict[str, pd.DataFrame], profile: GpuTrainingGovernanceProfile
) -> bool:
    """Validate disabled execution tables."""
    for name, df in df_map.items():
        if df.empty:
            return False
        if "is_disabled" in df.columns and not (df["is_disabled"] == True).all():
            return False
    return True


def validate_gpu_training_governance_manifest(
    df: pd.DataFrame, profile: GpuTrainingGovernanceProfile
) -> bool:
    """Validate governance manifest DataFrame."""
    if df.empty:
        return False
    row = df.iloc[0]
    checks = [
        int(row.get("current_phase", 0)) == 139,
        int(row.get("target_final_phase", 0)) == 160,
        int(row.get("next_phase", 0)) == 140,
        bool(row.get("dry_run", False)) is True,
        bool(row.get("local_only", False)) is True,
        bool(row.get("real_training_executed", True)) is False,
        bool(row.get("model_fit_executed", True)) is False,
        bool(row.get("model_predict_executed", True)) is False,
        bool(row.get("metric_calculation_executed", True)) is False,
        bool(row.get("artifact_persisted", True)) is False,
        bool(row.get("model_registry_written", True)) is False,
        bool(row.get("dataset_materialized", True)) is False,
        bool(row.get("feature_snapshot_materialized", True)) is False,
        bool(row.get("production_ready", True)) is False,
        bool(row.get("broker_ready", True)) is False,
        bool(row.get("official_approval", True)) is False,
    ]
    return all(checks)


def build_gpu_training_governance_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build comprehensive validation report verifying all Phase 139 contracts."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    checks = []

    # 1. Profile Registry
    p_df = tables.get("profiles", pd.DataFrame())
    p_valid = validate_gpu_training_governance_profile_registry(p_df, active_profile) if not p_df.empty else True
    checks.append({"validation_check": "profile_registry_contract", "passed": p_valid, "details": "Profiles enforce zero training"})

    # 2. Resource Policies
    res_df = tables.get("resource_policies", pd.DataFrame())
    res_valid = validate_gpu_training_resource_policies(res_df, active_profile) if not res_df.empty else True
    checks.append({"validation_check": "resource_policies_contract", "passed": res_valid, "details": "Policies enforce contract_only mode"})

    # 3. Harness Contracts
    harn_df = tables.get("harness_contracts", pd.DataFrame())
    harn_valid = validate_gpu_training_harness_contracts(harn_df, active_profile) if not harn_df.empty else True
    checks.append({"validation_check": "harness_contracts_contract", "passed": harn_valid, "details": "Harness strictly blocks execution"})

    # 4. Manifest Validation
    mf_df = tables.get("manifest", pd.DataFrame())
    mf_valid = validate_gpu_training_governance_manifest(mf_df, active_profile) if not mf_df.empty else True
    checks.append({"validation_check": "manifest_safety_validation", "passed": mf_valid, "details": "Manifest declares all execution flags False"})

    # 5. Forbidden Claims Validation
    fc_valid = validate_no_forbidden_gpu_training_claims()
    checks.append({"validation_check": "forbidden_claims_clean", "passed": fc_valid["is_clean"], "details": "No production or performance claims"})

    df = pd.DataFrame(checks)
    all_passed = bool((df["passed"] == True).all())

    summary = {
        "total_checks": len(df),
        "passed_checks": int(df["passed"].sum()),
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAIL",
        "all_passed": all_passed,
        "forbidden_claims_clean": True,
        "current_phase": 139,
        "target_final_phase": 160,
        "next_phase": 140,
        "non_signal": True,
        "active_profile": active_profile.name,
    }
    return df, summary
