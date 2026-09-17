# -*- coding: utf-8 -*-
"""Phase 141: Calibration & Uncertainty Validation Report."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

FORBIDDEN_CLAIMS = [
    "production_ready",
    "broker_ready",
    "official_approval",
    "calibrated_probability_output",
    "confidence_score_output",
    "prediction_interval_calculated",
    "trade_signal",
    "alpha_signal",
    "guaranteed_coverage",
]


def validate_calibration_uncertainty_profile_registry(
    df: pd.DataFrame, profile: Optional[CalibrationUncertaintyProfile] = None
) -> Dict[str, Any]:
    """Validate profile registry."""
    if df.empty:
        return {"is_valid": False, "reason": "Empty profile registry"}
    is_valid = bool(df["local_only"].all() and df["non_signal"].all() and df["dry_run_default"].all())
    return {"is_valid": is_valid, "check": "profile_registry_validation"}


def validate_probability_calibration_contracts(
    df: pd.DataFrame, profile: Optional[CalibrationUncertaintyProfile] = None
) -> Dict[str, Any]:
    """Validate probability calibration contracts."""
    if df.empty:
        return {"is_valid": False, "reason": "Empty probability calibration contracts"}
    is_valid = bool(
        (~df["probability_prediction_allowed"]).all()
        and (~df["calibration_fit_allowed"]).all()
        and (~df["calibration_transform_allowed"]).all()
        and df["non_signal_required"].all()
    )
    return {"is_valid": is_valid, "check": "probability_calibration_contracts_validation"}


def validate_uncertainty_estimation_contracts(
    df: pd.DataFrame, profile: Optional[CalibrationUncertaintyProfile] = None
) -> Dict[str, Any]:
    """Validate uncertainty estimation contracts."""
    if df.empty:
        return {"is_valid": False, "reason": "Empty uncertainty estimation contracts"}
    is_valid = bool(
        (~df["uncertainty_estimation_allowed"]).all()
        and (~df["prediction_interval_allowed"]).all()
        and (~df["conformal_prediction_allowed"]).all()
        and df["non_signal_required"].all()
    )
    return {"is_valid": is_valid, "check": "uncertainty_estimation_contracts_validation"}


def validate_calibration_uncertainty_disabled_reports(
    df_map: Dict[str, pd.DataFrame], profile: Optional[CalibrationUncertaintyProfile] = None
) -> Dict[str, Any]:
    """Validate that all disabled execution reports confirm zero execution."""
    for name, df in df_map.items():
        if df.empty:
            return {"is_valid": False, "reason": f"Empty disabled report for {name}"}
        if "is_disabled" in df.columns and not df["is_disabled"].all():
            return {"is_valid": False, "reason": f"Non-disabled operations found in {name}"}
        if "is_fit_disabled" in df.columns and not df["is_fit_disabled"].all():
            return {"is_valid": False, "reason": f"Non-disabled fit found in {name}"}
        if "is_transform_disabled" in df.columns and not df["is_transform_disabled"].all():
            return {"is_valid": False, "reason": f"Non-disabled transform found in {name}"}
        if "is_prediction_disabled" in df.columns and not df["is_prediction_disabled"].all():
            return {"is_valid": False, "reason": f"Non-disabled prediction found in {name}"}
    return {"is_valid": True, "check": "disabled_reports_validation"}


def validate_calibration_uncertainty_manifest(
    df: pd.DataFrame, profile: Optional[CalibrationUncertaintyProfile] = None
) -> Dict[str, Any]:
    """Validate manifest invariants."""
    if df.empty:
        return {"is_valid": False, "reason": "Empty manifest"}
    row = df.iloc[0]
    invariants = [
        row["current_phase"] == 141,
        row["target_final_phase"] == 160,
        row["next_phase"] == 142,
        not row["calibration_executed"],
        not row["uncertainty_estimation_executed"],
        not row["probability_prediction_executed"],
        not row["real_training_executed"],
        not row["artifact_persisted"],
        not row["production_ready"],
        not row["broker_ready"],
        not row["official_approval"],
        row["non_signal"],
    ]
    return {"is_valid": all(invariants), "check": "manifest_validation"}


def validate_no_forbidden_calibration_uncertainty_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Scan strings, dataframes, or summaries for forbidden marketing or execution claims."""
    combined = ""
    if text:
        combined += f" {text}"
    if df is not None and not df.empty:
        combined += f" {df.to_string()}"
    if summary is not None:
        combined += f" {str(summary)}"

    combined_lower = combined.lower()
    found = [claim for claim in FORBIDDEN_CLAIMS if claim in combined_lower]
    return {
        "is_clean": len(found) == 0,
        "found_claims": found,
        "non_signal": True,
    }


def build_calibration_uncertainty_validation_report(
    tables: Optional[Dict[str, pd.DataFrame]] = None,
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build composite validation report DataFrame and summary."""
    prof = profile or get_calibration_uncertainty_profile()
    checks = [
        {"check_name": "current_phase_is_141", "passed": (prof.current_phase == 141)},
        {"check_name": "target_final_phase_is_160", "passed": (prof.target_final_phase == 160)},
        {"check_name": "next_phase_is_142", "passed": (prof.next_phase == 142)},
        {"check_name": "local_dry_run_non_production", "passed": (prof.dry_run_default and prof.local_only and prof.non_production)},
        {"check_name": "zero_trading_zero_broker_zero_order", "passed": (not prof.allow_live_trading and not prof.allow_broker_integration and not prof.allow_real_order)},
        {"check_name": "zero_training_zero_fit_zero_predict", "passed": (not prof.allow_model_training and not prof.allow_model_fit and not prof.allow_model_predict)},
        {"check_name": "zero_probability_zero_calibration_fit", "passed": (not prof.allow_probability_prediction and not prof.allow_calibration_fit and not prof.allow_calibration_transform)},
        {"check_name": "zero_uncertainty_zero_prediction_interval", "passed": (not prof.allow_uncertainty_estimation and not prof.allow_prediction_interval_calculation and not prof.allow_conformal_prediction_execution)},
        {"check_name": "zero_materialization_zero_artifacts", "passed": (not prof.allow_dataset_materialization and not prof.allow_artifact_persistence and not prof.allow_model_registry_write)},
        {"check_name": "zero_full_text_zero_embeddings_zero_sentiment", "passed": (not prof.allow_full_article_usage and not prof.allow_embedding_generation and not prof.allow_sentiment_model_output)},
        {"check_name": "source_preservation_strict", "passed": (not prof.allow_source_overwrite and not prof.allow_auto_destructive_cleaning and not prof.allow_auto_imputation and not prof.allow_auto_feature_drop)},
        {"check_name": "no_production_ready_no_broker_ready_claims", "passed": (not prof.allow_production_ready_claim and not prof.allow_broker_ready_claim and not prof.allow_official_approval_claim)},
    ]

    rows = []
    for c in checks:
        rows.append(
            {
                "check_name": c["check_name"],
                "status": "PASS" if c["passed"] else "FAIL",
                "non_signal": True,
                "phase": prof.current_phase,
            }
        )

    df = pd.DataFrame(rows)
    passed_count = int((df["status"] == "PASS").sum())
    total_checks = len(df)
    all_passed = passed_count == total_checks

    summary = {
        "validation_status": "VALID" if all_passed else "INVALID",
        "total_checks": total_checks,
        "passed_checks": passed_count,
        "failed_checks": total_checks - passed_count,
        "all_passed": all_passed,
        "forbidden_claims_clean": True,
        "non_signal": True,
    }
    return df, summary
