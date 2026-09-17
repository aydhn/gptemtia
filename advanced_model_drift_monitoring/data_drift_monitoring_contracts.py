# -*- coding: utf-8 -*-
"""Phase 142: Data Drift Monitoring Contracts Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)

DATA_DRIFT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "commodity_fx_tabular_data_drift_contract",
        "dataset_family": "commodity_fx_ohlcv_time_series",
        "source_dataset_contract_ref": "ml_dataset_contract_commodity_fx_v1",
        "featurestore_catalog_ref": "featurestore_commodity_fx_catalog",
        "reference_window_policy_ref": "fixed_in_sample_reference_window_policy",
        "current_window_policy_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "data_drift_threshold_placeholder",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "macro_event_tabular_data_drift_contract",
        "dataset_family": "macro_event_news_metadata",
        "source_dataset_contract_ref": "ml_dataset_contract_macro_event_v1",
        "featurestore_catalog_ref": "featurestore_macro_catalog",
        "reference_window_policy_ref": "fixed_in_sample_reference_window_policy",
        "current_window_policy_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "data_drift_threshold_placeholder",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "cross_asset_regime_data_drift_contract",
        "dataset_family": "cross_asset_regime_matrix",
        "source_dataset_contract_ref": "ml_dataset_contract_cross_asset_regime_v1",
        "featurestore_catalog_ref": "featurestore_cross_asset_catalog",
        "reference_window_policy_ref": "fixed_in_sample_reference_window_policy",
        "current_window_policy_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "data_drift_threshold_placeholder",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "multi_window_feature_grid_data_drift_contract",
        "dataset_family": "multi_window_feature_grid",
        "source_dataset_contract_ref": "ml_dataset_contract_feature_grid_v1",
        "featurestore_catalog_ref": "featurestore_feature_grid_catalog",
        "reference_window_policy_ref": "fixed_in_sample_reference_window_policy",
        "current_window_policy_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "data_drift_threshold_placeholder",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "contract_name": "dataset_covariate_shift_contract_placeholder",
        "dataset_family": "composite_covariate_shift",
        "source_dataset_contract_ref": "ml_dataset_contract_composite_v1",
        "featurestore_catalog_ref": "featurestore_composite_catalog",
        "reference_window_policy_ref": "fixed_in_sample_reference_window_policy",
        "current_window_policy_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "data_drift_threshold_placeholder",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
    {
        "contract_name": "raw_market_distribution_drift_contract",
        "dataset_family": "raw_market_ticks_bars",
        "source_dataset_contract_ref": "ml_dataset_contract_raw_market_v1",
        "featurestore_catalog_ref": "featurestore_market_catalog",
        "reference_window_policy_ref": "fixed_in_sample_reference_window_policy",
        "current_window_policy_ref": "rolling_recent_current_window_policy",
        "threshold_placeholder_ref": "data_drift_threshold_placeholder",
        "drift_calculation_allowed": False,
        "metric_calculation_allowed": False,
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
]


def build_data_drift_monitoring_contract_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for data drift monitoring contracts."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(DATA_DRIFT_CONTRACTS)
    summary = summarize_data_drift_monitoring_contracts(df)
    return df, summary


def validate_data_drift_monitoring_contract(contract: Any) -> Dict[str, Any]:
    """Validate a data drift contract for safety compliance."""
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


def summarize_data_drift_monitoring_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize data drift monitoring contracts."""
    return {
        "total_contracts": len(df),
        "contracts": df["contract_name"].tolist() if not df.empty else [],
        "all_drift_calculation_disabled": bool((~df["drift_calculation_allowed"]).all()) if not df.empty else True,
        "all_metric_calculation_disabled": bool((~df["metric_calculation_allowed"]).all()) if not df.empty else True,
        "all_alerting_disabled": bool((~df["alerting_allowed"]).all()) if not df.empty else True,
        "all_retraining_trigger_disabled": bool((~df["retraining_trigger_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }


def build_data_drift_monitoring_contracts() -> List[Any]:
    """Return list of DriftMonitoringContract objects for data drift."""
    from advanced_model_drift_monitoring.model_drift_models import DriftMonitoringContract
    return [
        DriftMonitoringContract(
            contract_id=c.get("contract_name"),
            contract_name=c.get("contract_name"),
            drift_family=c.get("drift_family", "data_drift"),
            candidate_model_contract_ref="",
            ensemble_contract_ref="",
            calibration_contract_ref="",
            uncertainty_contract_ref="",
            dataset_contract_ref=c.get("upstream_phase_ref", ""),
            featurestore_contract_ref="",
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
        for c in DATA_DRIFT_CONTRACTS
    ]

