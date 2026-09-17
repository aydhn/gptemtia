# -*- coding: utf-8 -*-
"""Phase 142: Prediction Distribution Drift Placeholders Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)

PREDICTION_DISTRIBUTION_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "placeholder_name": "predicted_label_distribution_drift_placeholder",
        "output_type": "categorical_label",
        "target_model_family": "candidate_classifiers",
        "statistical_method": "chi_square_or_js_divergence",
        "prediction_executed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
    {
        "placeholder_name": "predicted_probability_histogram_drift_placeholder",
        "output_type": "continuous_probability",
        "target_model_family": "calibrated_classifiers",
        "statistical_method": "psi_or_wasserstein",
        "prediction_executed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
    {
        "placeholder_name": "score_percentile_shift_placeholder",
        "output_type": "continuous_score",
        "target_model_family": "ensemble_models",
        "statistical_method": "ks_test_or_percentile_delta",
        "prediction_executed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
    {
        "placeholder_name": "binary_classification_threshold_drift_placeholder",
        "output_type": "decision_boundary",
        "target_model_family": "baseline_classifiers",
        "statistical_method": "operating_point_shift",
        "prediction_executed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
]


def build_prediction_distribution_drift_placeholder_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for prediction distribution drift placeholders."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(PREDICTION_DISTRIBUTION_PLACEHOLDERS)
    summary = summarize_prediction_distribution_drift_placeholders(df)
    return df, summary


def summarize_prediction_distribution_drift_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize prediction distribution drift placeholders DataFrame."""
    return {
        "total_placeholders": len(df),
        "placeholders": df["placeholder_name"].tolist() if not df.empty else [],
        "all_predictions_unexecuted": bool((~df["prediction_executed"]).all()) if not df.empty else True,
        "all_drift_calculation_disabled": bool((~df["drift_calculation_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }


def validate_prediction_distribution_drift_placeholder(placeholder: Any) -> Dict[str, Any]:
    """Validate a prediction distribution drift placeholder."""
    issues = []

    def _get(key, default):
        if isinstance(placeholder, dict):
            return placeholder.get(key, default)
        return getattr(placeholder, key, default)

    if _get("prediction_executed", False):
        issues.append("prediction_executed must be False")
    if _get("drift_calculation_allowed", False):
        issues.append("drift_calculation_allowed must be False")
    valid = len(issues) == 0
    name = _get("placeholder_name", "unknown")
    cid = _get("contract_id", name)
    return {
        "contract_id": cid,
        "placeholder_name": name,
        "valid": valid,
        "is_valid": valid,
        "issues": issues,
        "errors": issues,
        "non_signal": True,
    }


def build_prediction_distribution_drift_placeholders() -> List[Any]:
    """Return list of DriftMonitoringContract objects for prediction distribution drift."""
    from advanced_model_drift_monitoring.model_drift_models import DriftMonitoringContract
    return [
        DriftMonitoringContract(
            contract_id=c.get("placeholder_name"),
            contract_name=c.get("placeholder_name"),
            drift_family="prediction_distribution_drift",
            candidate_model_contract_ref=c.get("target_model_family", ""),
            ensemble_contract_ref="",
            calibration_contract_ref="",
            uncertainty_contract_ref="",
            dataset_contract_ref="",
            featurestore_contract_ref="",
            reference_window_policy_ref="",
            current_window_policy_ref="",
            threshold_placeholder_ref="",
            required_no_lookahead_guard_ref="guard_no_lookahead_drift",
            required_metadata_only_news_guard_ref="guard_metadata_only_news_drift",
            required_source_preservation_guard_ref="guard_source_preservation_drift",
            drift_calculation_allowed=c.get("drift_calculation_allowed", False),
            metric_calculation_allowed=False,
            alerting_allowed=False,
            retraining_trigger_allowed=False,
            model_action_allowed=False,
            signal_generation_allowed=False,
            non_signal_required=True,
            manual_review_required=True,
            status=c.get("status", "drift_contract_placeholder_only"),
            execution_mode="non_executing_contract",
        )
        for c in PREDICTION_DISTRIBUTION_PLACEHOLDERS
    ]

