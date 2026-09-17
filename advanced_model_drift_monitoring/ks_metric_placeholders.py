"""Kolmogorov-Smirnov (KS) Metric Placeholders for Phase 142.

Defines non-executing KS statistic drift metric contracts for continuous feature
and prediction distributions without performing statistical hypothesis testing.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftMetricPlaceholder


def build_ks_metric_placeholders() -> List[DriftMetricPlaceholder]:
    """Builds non-executing KS test metric placeholders."""
    metrics = [
        DriftMetricPlaceholder(
            metric_id="metric_ks_continuous_features",
            metric_name="Continuous Features KS Test Placeholder",
            metric_type="kolmogorov_smirnov",
            target_scope="feature",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder="thresh_ks_continuous_feature",
            description="Two-sample KS statistic placeholder for continuous financial and returns feature distributions.",
            metadata={
                "test_type": "two_sample_ks",
                "alternative": "two-sided",
                "alpha": 0.05,
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_ks_prediction_scores",
            metric_name="Model Prediction Scores KS Test Placeholder",
            metric_type="kolmogorov_smirnov",
            target_scope="prediction",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder="thresh_ks_continuous_feature",
            description="KS statistic placeholder measuring empirical CDF divergence in output prediction probabilities.",
            metadata={
                "test_type": "two_sample_ks",
                "alternative": "two-sided",
                "alpha": 0.01,
                "execution_mode": "non_executing_contract",
            },
        ),
    ]
    return metrics


def validate_ks_metric_placeholder(metric: DriftMetricPlaceholder) -> Dict[str, Any]:
    """Validates that KS test placeholder maintains non-executing safety."""
    errors = []
    if metric.calculation_enabled:
        errors.append("calculation_enabled must be False for KS placeholders.")
    if not metric.metric_id.startswith("metric_ks_"):
        errors.append("metric_id must start with 'metric_ks_'.")

    return {
        "valid": len(errors) == 0,
        "metric_id": metric.metric_id,
        "metric_name": metric.metric_name,
        "errors": errors,
        "metric": asdict(metric),
    }
