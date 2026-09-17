"""Wasserstein Distance Metric Placeholders for Phase 142.

Defines non-executing Wasserstein (Earth Mover's Distance) contracts for continuous
feature distributions and model risk scores.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftMetricPlaceholder


def build_wasserstein_metric_placeholders() -> List[DriftMetricPlaceholder]:
    """Builds non-executing Wasserstein distance metric placeholders."""
    metrics = [
        DriftMetricPlaceholder(
            metric_id="metric_wasserstein_spread_features",
            metric_name="Spread & Basis Features Wasserstein Distance Placeholder",
            metric_type="wasserstein_distance",
            target_scope="feature",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder="thresh_wasserstein_spread_feature",
            description="Wasserstein 1-distance placeholder for commodity spread and forex basis feature distributions.",
            metadata={
                "p_norm": 1,
                "scaling": "standardized",
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_wasserstein_model_outputs",
            metric_name="Model Output Scores Wasserstein Distance Placeholder",
            metric_type="wasserstein_distance",
            target_scope="prediction",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder="thresh_wasserstein_spread_feature",
            description="Wasserstein 1-distance placeholder measuring physical shift between baseline and current predictions.",
            metadata={
                "p_norm": 1,
                "scaling": "unit_interval",
                "execution_mode": "non_executing_contract",
            },
        ),
    ]
    return metrics


def validate_wasserstein_metric_placeholder(metric: DriftMetricPlaceholder) -> Dict[str, Any]:
    """Validates that Wasserstein placeholder maintains non-executing safety."""
    errors = []
    if metric.calculation_enabled:
        errors.append("calculation_enabled must be False for Wasserstein placeholders.")
    if not metric.metric_id.startswith("metric_wasserstein_"):
        errors.append("metric_id must start with 'metric_wasserstein_'.")

    return {
        "valid": len(errors) == 0,
        "metric_id": metric.metric_id,
        "metric_name": metric.metric_name,
        "errors": errors,
        "metric": asdict(metric),
    }
