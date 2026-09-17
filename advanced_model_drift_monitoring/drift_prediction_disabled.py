"""Drift Prediction Disabled Enforcer for Phase 142.

Enforces strict non-executing safety boundary preventing model inference,
prediction scoring, trading signal generation, or live market forecasting.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict

from advanced_model_drift_monitoring.model_drift_models import DriftDisabledExecutionItem


def build_drift_prediction_disabled_item() -> DriftDisabledExecutionItem:
    """Builds the disabled execution item for prediction generation."""
    return DriftDisabledExecutionItem(
        execution_id="dis_exec_prediction_005",
        execution_type="drift_prediction_disabled",
        target_component="inference_engine",
        status="active_enforcement",
        is_disabled=True,
        disabled_reason="Live inference, signal generation, and score prediction are strictly forbidden in Phase 142.",
        remediation_required="Phase 142 defines governance contracts only; no forward predictions may be computed.",
        metadata={
            "blocked_actions": ["predict", "predict_proba", "generate_signal", "infer_market_direction"],
            "allow_placeholders_only": True,
            "phase": 142,
        },
    )


def assert_drift_prediction_disabled(request_params: Dict[str, Any]) -> Dict[str, Any]:
    """Validates that a request does not attempt live predictions or signal generation.

    Raises RuntimeError if prediction is requested.
    """
    if request_params.get("predict", False) or request_params.get("predict_proba", False) or request_params.get("generate_signals", False):
        raise RuntimeError(
            "CRITICAL SAFETY VIOLATION: Inference and prediction generation are strictly disabled in Phase 142 offline research contracts."
        )

    return {
        "status": "passed",
        "prediction_blocked": True,
        "item": asdict(build_drift_prediction_disabled_item()),
    }
