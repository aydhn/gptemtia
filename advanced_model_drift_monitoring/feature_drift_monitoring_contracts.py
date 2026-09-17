# -*- coding: utf-8 -*-
"""Phase 142: Feature Drift Monitoring Contracts Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)

FEATURE_DRIFT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "technical_feature_drift_monitoring_contract",
        "feature_family": "technical_indicators",
        "namespace": "ml_feature_tech",
        "upstream_phase_ref": "Phase 117 / Phase 118",
        "metric_placeholder_ref": "psi_ks_numerical_drift_placeholder",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "macro_feature_drift_monitoring_contract",
        "feature_family": "macro_indicators",
        "namespace": "ml_feature_macro",
        "upstream_phase_ref": "Phase 113 / Phase 120",
        "metric_placeholder_ref": "numerical_missingness_drift_placeholder",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "calendar_feature_drift_monitoring_contract",
        "feature_family": "economic_calendar",
        "namespace": "ml_feature_calendar",
        "upstream_phase_ref": "Phase 111 / Phase 120",
        "metric_placeholder_ref": "categorical_missingness_drift_placeholder",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "news_metadata_feature_drift_monitoring_contract",
        "feature_family": "news_metadata_only",
        "namespace": "ml_feature_news_meta",
        "upstream_phase_ref": "Phase 112 / Phase 120",
        "metric_placeholder_ref": "categorical_frequency_drift_placeholder",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "cross_asset_feature_drift_monitoring_contract",
        "feature_family": "cross_asset_context",
        "namespace": "ml_feature_cross_asset",
        "upstream_phase_ref": "Phase 119 / Phase 131",
        "metric_placeholder_ref": "correlation_drift_placeholder",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "composite_factor_drift_monitoring_contract",
        "feature_family": "composite_factors",
        "namespace": "ml_feature_factor",
        "upstream_phase_ref": "Phase 122 / Phase 125",
        "metric_placeholder_ref": "psi_wasserstein_drift_placeholder",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
]


def build_feature_drift_monitoring_contract_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for feature drift monitoring contracts."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(FEATURE_DRIFT_CONTRACTS)
    summary = summarize_feature_drift_monitoring_contracts(df)
    return df, summary


def validate_feature_drift_monitoring_contract(contract: Any) -> Dict[str, Any]:
    """Validate a feature drift contract for safety compliance."""
    valid = True
    issues = []

    def _get(key, default):
        if isinstance(contract, dict):
            return contract.get(key, default)
        return getattr(contract, key, default)

    if _get("drift_calculation_allowed", False):
        valid = False
        issues.append("drift_calculation_allowed must be False")
    if _get("metric_calculation_allowed", False):
        valid = False
        issues.append("metric_calculation_allowed must be False")
    if _get("alerting_allowed", False):
        valid = False
        issues.append("alerting_allowed must be False")
    if _get("retraining_trigger_allowed", False):
        valid = False
        issues.append("retraining_trigger_allowed must be False")
    if _get("model_action_allowed", False):
        valid = False
        issues.append("model_action_allowed must be False")
    if not _get("non_signal", True):
        valid = False
        issues.append("non_signal must be True")

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


def summarize_feature_drift_monitoring_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize feature drift monitoring contracts."""
    return {
        "total_contracts": len(df),
        "contracts": df["contract_name"].tolist() if not df.empty else [],
        "all_drift_calculation_disabled": bool((~df["drift_calculation_allowed"]).all()) if not df.empty else True,
        "all_metric_calculation_disabled": bool((~df["metric_calculation_allowed"]).all()) if not df.empty else True,
        "all_alerting_disabled": bool((~df["alerting_allowed"]).all()) if not df.empty else True,
        "all_retraining_trigger_disabled": bool((~df["retraining_trigger_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }


def build_feature_drift_monitoring_contracts() -> List[Any]:
    """Return list of DriftMonitoringContract objects for feature drift."""
    from advanced_model_drift_monitoring.model_drift_models import DriftMonitoringContract
    return [
        DriftMonitoringContract(
            contract_id=c.get("contract_name"),
            contract_name=c.get("contract_name"),
            drift_family=c.get("feature_family", "feature_drift"),
            candidate_model_contract_ref="",
            ensemble_contract_ref="",
            calibration_contract_ref="",
            uncertainty_contract_ref="",
            dataset_contract_ref=c.get("upstream_phase_ref", ""),
            featurestore_contract_ref=c.get("namespace", ""),
            reference_window_policy_ref="",
            current_window_policy_ref="",
            threshold_placeholder_ref=c.get("metric_placeholder_ref", ""),
            required_no_lookahead_guard_ref="guard_no_lookahead_drift",
            required_metadata_only_news_guard_ref="guard_metadata_only_news_drift",
            required_source_preservation_guard_ref="guard_source_preservation_drift",
            drift_calculation_allowed=c.get("drift_calculation_allowed", False),
            metric_calculation_allowed=c.get("metric_calculation_allowed", False),
            alerting_allowed=c.get("alerting_allowed", False),
            retraining_trigger_allowed=c.get("retraining_trigger_allowed", False),
            model_action_allowed=c.get("model_action_allowed", False),
            signal_generation_allowed=False,
            non_signal_required=True,
            manual_review_required=True,
            status=c.get("status", "drift_contract_ready"),
            execution_mode="non_executing_contract",
        )
        for c in FEATURE_DRIFT_CONTRACTS
    ]


