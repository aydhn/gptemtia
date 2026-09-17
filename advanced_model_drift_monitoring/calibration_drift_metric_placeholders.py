"""Calibration Drift Metric Placeholders for Phase 142.

Defines non-executing calibration drift metric contracts (Expected Calibration Error drift,
Brier score divergence, calibration slope/intercept shifts) linked to Phase 141.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftMetricPlaceholder


def build_calibration_drift_metric_placeholders() -> List[DriftMetricPlaceholder]:
    """Builds non-executing calibration drift metric placeholders."""
    metrics = [
        DriftMetricPlaceholder(
            metric_id="metric_calib_ece_drift",
            metric_name="Expected Calibration Error (ECE) Drift Placeholder",
            metric_type="ece_drift",
            target_scope="calibration",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder="thresh_ece_drift_delta",
            description="ECE degradation contract: Delta_ECE = ECE_curr - ECE_ref without calculating bin accuracies.",
            metadata={
                "linked_phase": "Phase 141",
                "calibration_methods": ["isotonic", "platt", "temperature"],
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_calib_brier_score_drift",
            metric_name="Brier Score Divergence Placeholder",
            metric_type="brier_score_drift",
            target_scope="calibration",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder="thresh_ece_drift_delta",
            description="Measures drift in probability calibration accuracy using Brier score divergence placeholder.",
            metadata={
                "linked_phase": "Phase 141",
                "scoring_rule": "strictly_proper",
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_calib_reliability_slope_drift",
            metric_name="Calibration Reliability Curve Slope Drift Placeholder",
            metric_type="calibration_slope_drift",
            target_scope="calibration",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder=None,
            description="Measures divergence of reliability diagram slope from ideal unit slope (slope=1.0).",
            metadata={
                "linked_phase": "Phase 141",
                "ideal_slope": 1.0,
                "execution_mode": "non_executing_contract",
            },
        ),
    ]
    return metrics


def validate_calibration_drift_metric_placeholder(metric: DriftMetricPlaceholder) -> Dict[str, Any]:
    """Validates that calibration drift placeholder adheres to non-executing rules."""
    errors = []
    if metric.calculation_enabled:
        errors.append("calculation_enabled must be False for calibration drift placeholders.")
    if not metric.metric_id.startswith("metric_calib_"):
        errors.append("metric_id must start with 'metric_calib_'.")

    return {
        "valid": len(errors) == 0,
        "metric_id": metric.metric_id,
        "metric_name": metric.metric_name,
        "errors": errors,
        "metric": asdict(metric),
    }
