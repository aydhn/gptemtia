# -*- coding: utf-8 -*-
"""Phase 142: Calibration Drift Contracts Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)

CALIBRATION_DRIFT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "ece_drift_contract",
        "calibration_metric_ref": "expected_calibration_error_placeholder",
        "upstream_phase_ref": "Phase 141",
        "reference_window_ref": "fixed_in_sample_reference_window_policy",
        "current_window_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "calibration_drift_threshold_placeholder",
        "calibration_fit_allowed": False,
        "calibration_transform_allowed": False,
        "probability_prediction_allowed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "brier_score_drift_contract",
        "calibration_metric_ref": "brier_score_placeholder",
        "upstream_phase_ref": "Phase 141",
        "reference_window_ref": "fixed_in_sample_reference_window_policy",
        "current_window_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "calibration_drift_threshold_placeholder",
        "calibration_fit_allowed": False,
        "calibration_transform_allowed": False,
        "probability_prediction_allowed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "platt_scaling_drift_contract",
        "calibration_metric_ref": "platt_parameter_drift_placeholder",
        "upstream_phase_ref": "Phase 141",
        "reference_window_ref": "fixed_in_sample_reference_window_policy",
        "current_window_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "calibration_drift_threshold_placeholder",
        "calibration_fit_allowed": False,
        "calibration_transform_allowed": False,
        "probability_prediction_allowed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "temperature_scaling_drift_contract",
        "calibration_metric_ref": "temperature_parameter_drift_placeholder",
        "upstream_phase_ref": "Phase 141",
        "reference_window_ref": "fixed_in_sample_reference_window_policy",
        "current_window_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "calibration_drift_threshold_placeholder",
        "calibration_fit_allowed": False,
        "calibration_transform_allowed": False,
        "probability_prediction_allowed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "isotonic_calibration_drift_contract",
        "calibration_metric_ref": "isotonic_mapping_drift_placeholder",
        "upstream_phase_ref": "Phase 141",
        "reference_window_ref": "fixed_in_sample_reference_window_policy",
        "current_window_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "calibration_drift_threshold_placeholder",
        "calibration_fit_allowed": False,
        "calibration_transform_allowed": False,
        "probability_prediction_allowed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
]


def build_calibration_drift_contract_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for calibration drift contracts."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(CALIBRATION_DRIFT_CONTRACTS)
    summary = summarize_calibration_drift_contracts(df)
    return df, summary


def summarize_calibration_drift_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize calibration drift contracts DataFrame."""
    return {
        "total_contracts": len(df),
        "contracts": df["contract_name"].tolist() if not df.empty else [],
        "all_calibration_execution_disabled": bool((~df["calibration_fit_allowed"]).all() and (~df["calibration_transform_allowed"]).all()) if not df.empty else True,
        "all_probability_prediction_disabled": bool((~df["probability_prediction_allowed"]).all()) if not df.empty else True,
        "all_drift_calculation_disabled": bool((~df["drift_calculation_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }


def validate_calibration_drift_contract(contract: Any) -> Dict[str, Any]:
    """Validate a calibration drift contract."""
    issues = []

    def _get(key, default):
        if isinstance(contract, dict):
            return contract.get(key, default)
        return getattr(contract, key, default)

    if _get("calibration_fit_allowed", False):
        issues.append("calibration_fit_allowed must be False")
    if _get("probability_prediction_allowed", False):
        issues.append("probability_prediction_allowed must be False")
    if _get("drift_calculation_allowed", False):
        issues.append("drift_calculation_allowed must be False")
    valid = len(issues) == 0
    name = _get("contract_name", "unknown")
    cid = _get("contract_id", name)
    return {
        "contract_id": cid,
        "contract_name": name,
        "valid": valid,
        "is_valid": valid,
        "issues": issues,
        "errors": issues,
        "non_signal": True,
    }


def build_calibration_drift_contracts() -> List[Any]:
    """Return list of DriftMonitoringContract objects for calibration drift."""
    from advanced_model_drift_monitoring.model_drift_models import DriftMonitoringContract
    return [
        DriftMonitoringContract(
            contract_id=c.get("contract_name"),
            contract_name=c.get("contract_name"),
            drift_family="calibration_drift",
            candidate_model_contract_ref="",
            ensemble_contract_ref="",
            calibration_contract_ref=c.get("calibration_metric_ref", ""),
            uncertainty_contract_ref="",
            dataset_contract_ref=c.get("upstream_phase_ref", ""),
            featurestore_contract_ref="",
            reference_window_policy_ref=c.get("reference_window_ref", ""),
            current_window_policy_ref=c.get("current_window_ref", ""),
            threshold_placeholder_ref=c.get("threshold_placeholder_ref", ""),
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
            status=c.get("status", "drift_contract_ready"),
            execution_mode="non_executing_contract",
        )
        for c in CALIBRATION_DRIFT_CONTRACTS
    ]

