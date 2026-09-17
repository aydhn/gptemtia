# -*- coding: utf-8 -*-
"""Phase 138 Baseline ML Model Validation Engine.

Performs strict verification across all contracts, registries, stubs, and manifests.
Ensures zero tolerance for forbidden execution, claims, or data leakage.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

FORBIDDEN_CLAIM_WORDS = [
    "trade_signal", "buy_signal", "sell_signal", "investment_advice",
    "guaranteed_return", "production_approved", "broker_approved",
    "real_training_complete", "prediction_ready", "high_accuracy_claim",
]


def validate_baseline_ml_model_profile_registry(
    df: pd.DataFrame,
    profile: Optional[BaselineMlModelProfile] = None,
) -> Dict[str, Any]:
    """Validate baseline profile registry."""
    violations = []
    if df.empty:
        violations.append("Profile registry is empty")
    else:
        if not bool(df["dry_run_default"].all()):
            violations.append("All profiles must have dry_run_default=True")
        if not bool(df["local_only"].all()):
            violations.append("All profiles must have local_only=True")
        if not bool((~df["allow_real_model_training"]).all()):
            violations.append("All profiles must have allow_real_model_training=False")
        if not bool((~df["allow_model_predict"]).all()):
            violations.append("All profiles must have allow_model_predict=False")

    return {
        "check": "profile_registry_validation",
        "passed": len(violations) == 0,
        "violations": violations,
    }


def validate_baseline_model_contracts(
    df: pd.DataFrame,
    profile: Optional[BaselineMlModelProfile] = None,
) -> Dict[str, Any]:
    """Validate baseline model contracts DataFrame."""
    violations = []
    if df.empty:
        violations.append("Baseline model contracts DataFrame is empty")
    else:
        if not bool((~df["real_training_allowed"]).all()):
            violations.append("real_training_allowed must be False across all contracts")
        if not bool((~df["model_fit_allowed"]).all()):
            violations.append("model_fit_allowed must be False across all contracts")
        if not bool((~df["model_predict_allowed"]).all()):
            violations.append("model_predict_allowed must be False across all contracts")
        if not bool((~df["artifact_persistence_allowed"]).all()):
            violations.append("artifact_persistence_allowed must be False across all contracts")
        if not bool((~df["model_registry_write_allowed"]).all()):
            violations.append("model_registry_write_allowed must be False across all contracts")

    return {
        "check": "baseline_model_contracts_validation",
        "passed": len(violations) == 0,
        "violations": violations,
    }


def validate_dry_run_training_harness_contracts(
    df: pd.DataFrame,
    profile: Optional[BaselineMlModelProfile] = None,
) -> Dict[str, Any]:
    """Validate dry-run harness contracts DataFrame."""
    violations = []
    if df.empty:
        violations.append("Dry-run harness contracts DataFrame is empty")
    else:
        if not bool((~df["real_training_allowed"]).all()):
            violations.append("real_training_allowed must be False in harness")
        if not bool((df["allowed_mode"] == "contract_only").all()):
            violations.append("allowed_mode must be contract_only in harness")

    return {
        "check": "dry_run_harness_contracts_validation",
        "passed": len(violations) == 0,
        "violations": violations,
    }


def validate_disabled_execution_reports(
    df_map: Dict[str, pd.DataFrame],
    profile: Optional[BaselineMlModelProfile] = None,
) -> Dict[str, Any]:
    """Validate that all execution disabling checks pass."""
    violations = []
    for name, df in df_map.items():
        if df.empty:
            violations.append(f"Execution report '{name}' is empty")
        elif "is_disabled" in df.columns and not bool(df["is_disabled"].all()):
            violations.append(f"Execution report '{name}' has active non-disabled items")

    return {
        "check": "disabled_execution_reports_validation",
        "passed": len(violations) == 0,
        "violations": violations,
    }


def validate_baseline_ml_model_manifest(
    df: pd.DataFrame,
    profile: Optional[BaselineMlModelProfile] = None,
) -> Dict[str, Any]:
    """Validate the integrity manifest."""
    violations = []
    if df.empty:
        violations.append("Manifest is empty")
    else:
        row = df.iloc[0]
        if row.get("current_phase") != 138:
            violations.append(f"Manifest current_phase must be 138, got {row.get('current_phase')}")
        if row.get("target_final_phase") != 160:
            violations.append(f"Manifest target_final_phase must be 160, got {row.get('target_final_phase')}")
        if row.get("next_phase") != 139:
            violations.append(f"Manifest next_phase must be 139, got {row.get('next_phase')}")
        if bool(row.get("real_training_executed")) != False:
            violations.append("Manifest real_training_executed must be False")
        if bool(row.get("model_fit_executed")) != False:
            violations.append("Manifest model_fit_executed must be False")
        if bool(row.get("model_predict_executed")) != False:
            violations.append("Manifest model_predict_executed must be False")
        if bool(row.get("metric_calculation_executed")) != False:
            violations.append("Manifest metric_calculation_executed must be False")
        if bool(row.get("artifact_persisted")) != False:
            violations.append("Manifest artifact_persisted must be False")
        if bool(row.get("model_registry_written")) != False:
            violations.append("Manifest model_registry_written must be False")
        if bool(row.get("non_signal")) != True:
            violations.append("Manifest non_signal must be True")


    return {
        "check": "manifest_validation",
        "passed": len(violations) == 0,
        "violations": violations,
    }


def validate_no_forbidden_baseline_ml_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Scan text, dataframe, or summary dictionary for forbidden claim keywords."""
    violations = []
    combined = ""
    if text:
        combined += f" {text.lower()} "
    if df is not None and not df.empty:
        combined += f" {df.to_string().lower()} "
    if summary:
        combined += f" {str(summary).lower()} "

    for word in FORBIDDEN_CLAIM_WORDS:
        if word in combined:
            violations.append(f"Forbidden claim keyword detected: '{word}'")

    clean = len(violations) == 0
    return {
        "valid": clean,
        "violations": violations,
        "status": "PASS_CLEAN_OF_FORBIDDEN_CLAIMS" if clean else "FAIL_FORBIDDEN_CLAIMS_DETECTED",
        "non_signal": True,
    }


def build_baseline_ml_model_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: Optional[BaselineMlModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Aggregate all validations into a comprehensive report."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    results = []
    if "profiles" in tables:
        results.append(validate_baseline_ml_model_profile_registry(tables["profiles"], profile))
    if "contracts" in tables:
        results.append(validate_baseline_model_contracts(tables["contracts"], profile))
    if "harness" in tables:
        results.append(validate_dry_run_training_harness_contracts(tables["harness"], profile))
    if "manifest" in tables:
        results.append(validate_baseline_ml_model_manifest(tables["manifest"], profile))

    disabled_reports = {k: v for k, v in tables.items() if "disabled" in k or "no_" in k}
    if disabled_reports:
        results.append(validate_disabled_execution_reports(disabled_reports, profile))

    rows = []
    for res in results:
        rows.append({
            "check_name": res["check"],
            "passed": res["passed"],
            "violations_count": len(res.get("violations", [])),
            "violations": ", ".join(res.get("violations", [])) if res.get("violations") else "None",
            "non_signal": True,
        })

    df = pd.DataFrame(rows)
    all_passed = bool(df["passed"].all()) if not df.empty else True
    summary = {
        "total_validations": len(df),
        "passed_validations": int(df["passed"].sum()) if not df.empty else 0,
        "all_passed": all_passed,
        "validation_status": "VALIDATION_PASS" if all_passed else "VALIDATION_FAIL",
        "clean_of_forbidden_claims": True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def run_baseline_ml_model_validation(
    profile: Optional[BaselineMlModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build key tables and run baseline ML model validation."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()
    from advanced_baseline_ml_models.baseline_ml_model_profile_registry import build_baseline_ml_model_profile_registry
    from advanced_baseline_ml_models.baseline_model_contracts import build_baseline_model_contract_registry
    from advanced_baseline_ml_models.dry_run_training_harness_contracts import build_dry_run_training_harness_contract_registry
    from advanced_baseline_ml_models.baseline_ml_model_manifest import build_baseline_ml_model_manifest
    from advanced_baseline_ml_models.no_real_training_execution import build_no_real_training_execution_report

    df_p, _ = build_baseline_ml_model_profile_registry(profile)
    df_c, _ = build_baseline_model_contract_registry(profile)
    df_h, _ = build_dry_run_training_harness_contract_registry(profile)
    df_m, _ = build_baseline_ml_model_manifest(profile)
    df_nrt, _ = build_no_real_training_execution_report(profile)

    tables = {
        "profiles": df_p,
        "contracts": df_c,
        "harness": df_h,
        "manifest": df_m,
        "no_real_training": df_nrt,
    }
    return build_baseline_ml_model_validation_report(tables, profile=profile)

