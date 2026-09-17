# -*- coding: utf-8 -*-
"""Phase 142: Model Drift Monitoring Contracts Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)
from advanced_model_drift_monitoring.model_drift_models import DriftMonitoringContract


MODEL_DRIFT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "candidate_model_drift_monitoring_contract",
        "drift_family": "model_concept_drift",
        "candidate_model_contract_ref": "candidate_model_contract_v1",
        "ensemble_contract_ref": "ensemble_model_contract_placeholder",
        "calibration_contract_ref": "calibration_contract_ref_v1",
        "uncertainty_contract_ref": "uncertainty_contract_ref_v1",
        "dataset_contract_ref": "ml_dataset_contract_commodity_fx_v1",
        "featurestore_contract_ref": "featurestore_commodity_fx_catalog",
        "reference_window_policy_ref": "fixed_in_sample_reference_window_policy",
        "current_window_policy_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "candidate_model_drift_threshold_placeholder",
        "required_no_lookahead_guard_ref": "guard_no_lookahead_drift",
        "required_metadata_only_news_guard_ref": "guard_metadata_only_news_drift",
        "required_source_preservation_guard_ref": "guard_source_preservation_drift",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "signal_generation_allowed": False,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "ensemble_model_drift_monitoring_contract",
        "drift_family": "ensemble_weight_drift",
        "candidate_model_contract_ref": "candidate_model_contract_v1",
        "ensemble_contract_ref": "ensemble_model_contract_v1",
        "calibration_contract_ref": "calibration_contract_ref_v1",
        "uncertainty_contract_ref": "uncertainty_contract_ref_v1",
        "dataset_contract_ref": "ml_dataset_contract_commodity_fx_v1",
        "featurestore_contract_ref": "featurestore_ensemble_catalog",
        "reference_window_policy_ref": "fixed_in_sample_reference_window_policy",
        "current_window_policy_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "ensemble_drift_threshold_placeholder",
        "required_no_lookahead_guard_ref": "guard_no_lookahead_drift",
        "required_metadata_only_news_guard_ref": "guard_metadata_only_news_drift",
        "required_source_preservation_guard_ref": "guard_source_preservation_drift",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "signal_generation_allowed": False,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "calibration_drift_monitoring_contract",
        "drift_family": "probability_calibration_drift",
        "candidate_model_contract_ref": "candidate_model_contract_v1",
        "ensemble_contract_ref": "ensemble_model_contract_v1",
        "calibration_contract_ref": "calibration_contract_ref_v1",
        "uncertainty_contract_ref": "uncertainty_contract_ref_v1",
        "dataset_contract_ref": "ml_dataset_contract_commodity_fx_v1",
        "featurestore_contract_ref": "featurestore_calibration_catalog",
        "reference_window_policy_ref": "fixed_in_sample_reference_window_policy",
        "current_window_policy_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "calibration_drift_threshold_placeholder",
        "required_no_lookahead_guard_ref": "guard_no_lookahead_drift",
        "required_metadata_only_news_guard_ref": "guard_metadata_only_news_drift",
        "required_source_preservation_guard_ref": "guard_source_preservation_drift",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "signal_generation_allowed": False,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "uncertainty_drift_monitoring_contract",
        "drift_family": "epistemic_aleatoric_uncertainty_drift",
        "candidate_model_contract_ref": "candidate_model_contract_v1",
        "ensemble_contract_ref": "ensemble_model_contract_v1",
        "calibration_contract_ref": "calibration_contract_ref_v1",
        "uncertainty_contract_ref": "uncertainty_contract_ref_v1",
        "dataset_contract_ref": "ml_dataset_contract_commodity_fx_v1",
        "featurestore_contract_ref": "featurestore_uncertainty_catalog",
        "reference_window_policy_ref": "fixed_in_sample_reference_window_policy",
        "current_window_policy_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "uncertainty_drift_threshold_placeholder",
        "required_no_lookahead_guard_ref": "guard_no_lookahead_drift",
        "required_metadata_only_news_guard_ref": "guard_metadata_only_news_drift",
        "required_source_preservation_guard_ref": "guard_source_preservation_drift",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "signal_generation_allowed": False,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "prediction_distribution_drift_contract",
        "drift_family": "prediction_output_distribution_drift",
        "candidate_model_contract_ref": "candidate_model_contract_v1",
        "ensemble_contract_ref": "ensemble_model_contract_v1",
        "calibration_contract_ref": "calibration_contract_ref_v1",
        "uncertainty_contract_ref": "uncertainty_contract_ref_v1",
        "dataset_contract_ref": "ml_dataset_contract_commodity_fx_v1",
        "featurestore_contract_ref": "featurestore_output_catalog",
        "reference_window_policy_ref": "fixed_in_sample_reference_window_policy",
        "current_window_policy_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "prediction_drift_threshold_placeholder",
        "required_no_lookahead_guard_ref": "guard_no_lookahead_drift",
        "required_metadata_only_news_guard_ref": "guard_metadata_only_news_drift",
        "required_source_preservation_guard_ref": "guard_source_preservation_drift",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "signal_generation_allowed": False,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "model_stability_monitoring_contract_placeholder",
        "drift_family": "temporal_stability_drift",
        "candidate_model_contract_ref": "candidate_model_contract_v1",
        "ensemble_contract_ref": "ensemble_model_contract_v1",
        "calibration_contract_ref": "calibration_contract_ref_v1",
        "uncertainty_contract_ref": "uncertainty_contract_ref_v1",
        "dataset_contract_ref": "ml_dataset_contract_commodity_fx_v1",
        "featurestore_contract_ref": "featurestore_stability_catalog",
        "reference_window_policy_ref": "fixed_in_sample_reference_window_policy",
        "current_window_policy_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "stability_drift_threshold_placeholder",
        "required_no_lookahead_guard_ref": "guard_no_lookahead_drift",
        "required_metadata_only_news_guard_ref": "guard_metadata_only_news_drift",
        "required_source_preservation_guard_ref": "guard_source_preservation_drift",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "signal_generation_allowed": False,
        "non_signal_required": True,
        "manual_review_required": True,
        "status": "drift_contract_placeholder_only",
    },
]


def build_model_drift_monitoring_contract_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model drift monitoring contracts."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(MODEL_DRIFT_CONTRACTS)
    summary = summarize_model_drift_monitoring_contracts(df)
    return df, summary


def validate_model_drift_monitoring_contract(contract: Any) -> Dict[str, Any]:
    """Validate a single model drift monitoring contract for safety invariants."""
    valid = True
    issues = []

    def _get(key, default):
        if isinstance(contract, dict):
            return contract.get(key, default)
        return getattr(contract, key, default)

    if _get("drift_calculation_allowed", False):
        valid = False
        issues.append("drift_calculation_allowed must be False")
    if _get("alerting_allowed", False):
        valid = False
        issues.append("alerting_allowed must be False")
    if _get("retraining_trigger_allowed", False):
        valid = False
        issues.append("retraining_trigger_allowed must be False")
    if _get("model_action_allowed", False):
        valid = False
        issues.append("model_action_allowed must be False")
    if _get("signal_generation_allowed", False):
        valid = False
        issues.append("signal_generation_allowed must be False")
    if not _get("non_signal_required", True):
        valid = False
        issues.append("non_signal_required must be True")

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


def summarize_model_drift_monitoring_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model drift monitoring contracts."""
    return {
        "total_contracts": len(df),
        "contracts": df["contract_name"].tolist() if not df.empty else [],
        "all_drift_calculation_disabled": bool((~df["drift_calculation_allowed"]).all()) if not df.empty else True,
        "all_alerting_disabled": bool((~df["alerting_allowed"]).all()) if not df.empty else True,
        "all_retraining_trigger_disabled": bool((~df["retraining_trigger_allowed"]).all()) if not df.empty else True,
        "all_model_action_disabled": bool((~df["model_action_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal_required"].all()) if not df.empty else True,
    }


def build_model_drift_monitoring_contracts() -> List[DriftMonitoringContract]:
    """Return list of DriftMonitoringContract objects."""
    from advanced_model_drift_monitoring.model_drift_models import DriftMonitoringContract
    return [
        DriftMonitoringContract(
            contract_id=c.get("contract_name"),
            contract_name=c.get("contract_name"),
            drift_family=c.get("drift_family"),
            candidate_model_contract_ref=c.get("candidate_model_contract_ref", ""),
            ensemble_contract_ref=c.get("ensemble_contract_ref", ""),
            calibration_contract_ref=c.get("calibration_contract_ref", ""),
            uncertainty_contract_ref=c.get("uncertainty_contract_ref", ""),
            dataset_contract_ref=c.get("dataset_contract_ref", ""),
            featurestore_contract_ref=c.get("featurestore_contract_ref", ""),
            reference_window_policy_ref=c.get("reference_window_policy_ref", ""),
            current_window_policy_ref=c.get("current_window_policy_ref", ""),
            threshold_placeholder_ref=c.get("threshold_placeholder_ref", ""),
            required_no_lookahead_guard_ref=c.get("required_no_lookahead_guard_ref", ""),
            required_metadata_only_news_guard_ref=c.get("required_metadata_only_news_guard_ref", ""),
            required_source_preservation_guard_ref=c.get("required_source_preservation_guard_ref", ""),
            drift_calculation_allowed=c.get("drift_calculation_allowed", False),
            metric_calculation_allowed=c.get("metric_calculation_allowed", False),
            alerting_allowed=c.get("alerting_allowed", False),
            retraining_trigger_allowed=c.get("retraining_trigger_allowed", False),
            model_action_allowed=c.get("model_action_allowed", False),
            signal_generation_allowed=c.get("signal_generation_allowed", False),
            non_signal_required=c.get("non_signal_required", True),
            manual_review_required=c.get("manual_review_required", True),
            status=c.get("status", "drift_contract_ready"),
            execution_mode="non_executing_contract",
        )
        for c in MODEL_DRIFT_CONTRACTS
    ]


validate_drift_monitoring_contract = validate_model_drift_monitoring_contract


