# -*- coding: utf-8 -*-
"""Phase 142: Uncertainty Drift Contracts Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)

UNCERTAINTY_DRIFT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "interval_width_drift_contract",
        "uncertainty_metric_ref": "mean_interval_width_placeholder",
        "upstream_phase_ref": "Phase 141",
        "reference_window_ref": "fixed_in_sample_reference_window_policy",
        "current_window_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "uncertainty_drift_threshold_placeholder",
        "uncertainty_estimation_allowed": False,
        "prediction_interval_allowed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "interval_coverage_drift_contract",
        "uncertainty_metric_ref": "empirical_coverage_rate_placeholder",
        "upstream_phase_ref": "Phase 141",
        "reference_window_ref": "fixed_in_sample_reference_window_policy",
        "current_window_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "uncertainty_drift_threshold_placeholder",
        "uncertainty_estimation_allowed": False,
        "prediction_interval_allowed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "ensemble_variance_drift_contract",
        "uncertainty_metric_ref": "ensemble_variance_dispersion_placeholder",
        "upstream_phase_ref": "Phase 141",
        "reference_window_ref": "fixed_in_sample_reference_window_policy",
        "current_window_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "uncertainty_drift_threshold_placeholder",
        "uncertainty_estimation_allowed": False,
        "prediction_interval_allowed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "conformal_coverage_drift_contract",
        "uncertainty_metric_ref": "conformal_miscoverage_rate_placeholder",
        "upstream_phase_ref": "Phase 141",
        "reference_window_ref": "fixed_in_sample_reference_window_policy",
        "current_window_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "uncertainty_drift_threshold_placeholder",
        "uncertainty_estimation_allowed": False,
        "prediction_interval_allowed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "quantile_dispersion_drift_contract",
        "uncertainty_metric_ref": "interquartile_dispersion_drift_placeholder",
        "upstream_phase_ref": "Phase 141",
        "reference_window_ref": "fixed_in_sample_reference_window_policy",
        "current_window_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "uncertainty_drift_threshold_placeholder",
        "uncertainty_estimation_allowed": False,
        "prediction_interval_allowed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
]


def build_uncertainty_drift_contract_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for uncertainty drift contracts."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(UNCERTAINTY_DRIFT_CONTRACTS)
    summary = summarize_uncertainty_drift_contracts(df)
    return df, summary


def summarize_uncertainty_drift_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize uncertainty drift contracts DataFrame."""
    return {
        "total_contracts": len(df),
        "contracts": df["contract_name"].tolist() if not df.empty else [],
        "all_uncertainty_estimation_disabled": bool((~df["uncertainty_estimation_allowed"]).all()) if not df.empty else True,
        "all_prediction_interval_disabled": bool((~df["prediction_interval_allowed"]).all()) if not df.empty else True,
        "all_drift_calculation_disabled": bool((~df["drift_calculation_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }


def validate_uncertainty_drift_contract(contract: Any) -> Dict[str, Any]:
    """Validate an uncertainty drift contract."""
    issues = []

    def _get(key, default):
        if isinstance(contract, dict):
            return contract.get(key, default)
        return getattr(contract, key, default)

    if _get("uncertainty_estimation_allowed", False):
        issues.append("uncertainty_estimation_allowed must be False")
    if _get("prediction_interval_allowed", False):
        issues.append("prediction_interval_allowed must be False")
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


def build_uncertainty_drift_contracts() -> List[Any]:
    """Return list of DriftMonitoringContract objects for uncertainty drift."""
    from advanced_model_drift_monitoring.model_drift_models import DriftMonitoringContract
    return [
        DriftMonitoringContract(
            contract_id=c.get("contract_name"),
            contract_name=c.get("contract_name"),
            drift_family="uncertainty_drift",
            candidate_model_contract_ref="",
            ensemble_contract_ref="",
            calibration_contract_ref="",
            uncertainty_contract_ref=c.get("uncertainty_metric_ref", ""),
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
        for c in UNCERTAINTY_DRIFT_CONTRACTS
    ]

