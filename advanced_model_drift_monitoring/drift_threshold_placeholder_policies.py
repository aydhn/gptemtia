# -*- coding: utf-8 -*-
"""Phase 142: Drift Threshold Placeholder Policies Registry."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)

DRIFT_THRESHOLD_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "threshold_name": "psi_standard_drift_threshold_placeholder",
        "drift_family": "distribution_stability",
        "warning_threshold_placeholder": 0.10,
        "critical_threshold_placeholder": 0.25,
        "metric_type_ref": "psi",
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
    {
        "threshold_name": "ks_pvalue_drift_threshold_placeholder",
        "drift_family": "statistical_distribution_test",
        "warning_threshold_placeholder": 0.05,
        "critical_threshold_placeholder": 0.01,
        "metric_type_ref": "ks_pvalue",
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
    {
        "threshold_name": "js_divergence_drift_threshold_placeholder",
        "drift_family": "information_divergence",
        "warning_threshold_placeholder": 0.15,
        "critical_threshold_placeholder": 0.30,
        "metric_type_ref": "js_divergence",
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
    {
        "threshold_name": "wasserstein_normalized_drift_threshold_placeholder",
        "drift_family": "earth_movers_distance",
        "warning_threshold_placeholder": 0.20,
        "critical_threshold_placeholder": 0.40,
        "metric_type_ref": "wasserstein_normalized",
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
    {
        "threshold_name": "missingness_delta_drift_threshold_placeholder",
        "drift_family": "feature_quality_drift",
        "warning_threshold_placeholder": 0.05,
        "critical_threshold_placeholder": 0.15,
        "metric_type_ref": "missing_rate_delta",
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
    {
        "threshold_name": "calibration_ece_drift_threshold_placeholder",
        "drift_family": "calibration_drift",
        "warning_threshold_placeholder": 0.08,
        "critical_threshold_placeholder": 0.15,
        "metric_type_ref": "ece_delta",
        "alerting_allowed": False,
        "retraining_trigger_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
]


def build_drift_threshold_placeholder_policy_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for drift threshold placeholder policies."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(DRIFT_THRESHOLD_PLACEHOLDERS)
    summary = summarize_drift_threshold_placeholder_policies(df)
    return df, summary


def validate_drift_threshold_placeholder_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request against unauthorized alerting, retraining, or model actions."""
    req_text = str(request).lower()
    blocked = False
    reasons = []

    prohibited_actions = [
        "alert",
        "send_alert",
        "trigger_alert",
        "retrain",
        "trigger_retraining",
        "retraining_trigger",
        "model_action",
        "disable_model",
        "enable_model",
        "replace_model",
        "trade_action",
        "close_position",
        "open_position",
    ]

    for term in prohibited_actions:
        if term in req_text:
            blocked = True
            reasons.append(f"Prohibited action keyword detected: {term}")

    return {
        "valid": not blocked,
        "request_blocked": blocked,
        "action_permitted": not blocked,
        "reasons": reasons,
        "errors": reasons,
        "execution_status": "execution_blocked_by_policy" if blocked else "contract_placeholder_only",
        "non_signal": True,
    }


def summarize_drift_threshold_placeholder_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize drift threshold placeholder policies DataFrame."""
    return {
        "total_threshold_policies": len(df),
        "thresholds": df["threshold_name"].tolist() if not df.empty else [],
        "all_alerting_disabled": bool((~df["alerting_allowed"]).all()) if not df.empty else True,
        "all_retraining_trigger_disabled": bool((~df["retraining_trigger_allowed"]).all()) if not df.empty else True,
        "all_model_action_disabled": bool((~df["model_action_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }


def validate_drift_threshold_placeholder(record: Any) -> Dict[str, Any]:
    """Validate drift threshold placeholder record."""
    def _get(key, default=None):
        if isinstance(record, dict):
            return record.get(key, default)
        return getattr(record, key, default)

    valid = (
        not _get("alerting_allowed", False)
        and not _get("retraining_trigger_allowed", False)
        and not _get("model_action_allowed", False)
        and not _get("execution_enabled", False)
        and _get("non_signal", True) is True
    )
    return {
        "valid": valid,
        "is_valid": valid,
        "threshold_name": _get("threshold_name", "unknown"),
        "non_signal": True,
    }


def build_drift_threshold_placeholders() -> List[Any]:
    """Return list of DriftThresholdPlaceholder objects."""
    from advanced_model_drift_monitoring.model_drift_models import DriftThresholdPlaceholder
    return [
        DriftThresholdPlaceholder(
            threshold_id=t.get("threshold_name"),
            threshold_name=t.get("threshold_name"),
            drift_family=t.get("drift_family", "distribution_stability"),
            warning_threshold_placeholder=t.get("warning_threshold_placeholder", 0.1),
            critical_threshold_placeholder=t.get("critical_threshold_placeholder", 0.25),
            metric_type_ref=t.get("metric_type_ref", "psi"),
            alerting_allowed=False,
            retraining_trigger_allowed=False,
            model_action_allowed=False,
            non_signal=True,
            status=t.get("status", "drift_contract_placeholder_only"),
            execution_enabled=False,
        )
        for t in DRIFT_THRESHOLD_PLACEHOLDERS
    ]


validate_drift_threshold_request = validate_drift_threshold_placeholder_request


