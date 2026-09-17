# -*- coding: utf-8 -*-
"""Phase 141: Calibration & Uncertainty Safety Boundary."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

NO_GO_CONDITIONS = [
    "live_trading",
    "broker_integration",
    "real_order_execution",
    "investment_advice",
    "signal_generation",
    "directional_claims",
    "dataset_materialization",
    "feature_snapshot_materialization",
    "strategy_backtest_optimizer_execution",
    "real_model_training",
    "model_fit_execution",
    "model_predict_execution",
    "model_inference_execution",
    "model_transform_execution",
    "probability_prediction",
    "confidence_score_calculation",
    "calibration_fit_execution",
    "calibration_transform_execution",
    "calibration_execution",
    "uncertainty_estimation_execution",
    "prediction_interval_calculation",
    "conformal_prediction_execution",
    "supervised_unsupervised_clustering_execution",
    "ensemble_execution",
    "target_label_generation",
    "metric_calculation_performance_claim",
    "sentiment_model_output",
    "full_article_raw_html_scraping",
    "embedding_vector_generation",
    "artifact_persistence_model_registry_write",
    "official_approval_production_broker_ready_claims",
    "source_overwrite_destructive_cleaning",
    "auto_imputation_auto_feature_drop",
    "scraping_credential_output_deployment",
]

SAFE_GO_CONDITIONS = [
    "local_offline_calibration_contract_generation",
    "calibration_method_placeholders_without_execution",
    "uncertainty_method_placeholders_without_execution",
    "confidence_and_prediction_interval_placeholders_without_calculation",
    "quantile_and_conformal_placeholders_without_calculation",
    "calibration_and_uncertainty_metric_placeholders_without_evaluation",
    "disabled_execution_reports_certifying_zero_runtime",
    "calibration_and_uncertainty_quality_gates",
    "audit_trail_placeholders",
    "phase_142_model_drift_monitoring_handoff",
]


def build_calibration_uncertainty_no_go_conditions(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> List[Dict[str, Any]]:
    """Build list of strictly prohibited actions."""
    return [
        {"condition": cond, "status": "STRICTLY_PROHIBITED", "enforced": True}
        for cond in NO_GO_CONDITIONS
    ]


def build_calibration_uncertainty_safe_go_conditions(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> List[Dict[str, Any]]:
    """Build list of permitted safe dry-run operations."""
    return [
        {"condition": cond, "status": "PERMITTED_DRY_RUN", "active": True}
        for cond in SAFE_GO_CONDITIONS
    ]


def build_calibration_uncertainty_safety_boundary(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for safety boundary."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in build_calibration_uncertainty_no_go_conditions(prof):
        rows.append(
            {
                "rule_type": "NO_GO",
                "condition": item["condition"],
                "status": item["status"],
                "is_active": item["enforced"],
                "non_signal": True,
                "phase": prof.current_phase,
            }
        )
    for item in build_calibration_uncertainty_safe_go_conditions(prof):
        rows.append(
            {
                "rule_type": "SAFE_GO",
                "condition": item["condition"],
                "status": item["status"],
                "is_active": item["active"],
                "non_signal": True,
                "phase": prof.current_phase,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_calibration_uncertainty_safety_boundary(df)
    return df, summary


def summarize_calibration_uncertainty_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary DataFrame."""
    no_go_count = int((df["rule_type"] == "NO_GO").sum()) if not df.empty else 0
    safe_go_count = int((df["rule_type"] == "SAFE_GO").sum()) if not df.empty else 0
    return {
        "safety_status": "ENFORCED",
        "total_rules": len(df),
        "no_go_count": no_go_count,
        "safe_go_count": safe_go_count,
        "all_enforced": True,
        "non_signal": True,
    }


def enforce_calibration_uncertainty_safety_boundary(pipeline_result: Dict[str, Any]) -> bool:
    """Validate pipeline result against critical safety invariants."""
    if not isinstance(pipeline_result, dict):
        return False
    if pipeline_result.get("phase") != 141:
        return False
    if not pipeline_result.get("non_signal", False):
        return False
    if not pipeline_result.get("dry_run", False):
        return False
    if not pipeline_result.get("local_only", False):
        return False
    return True
