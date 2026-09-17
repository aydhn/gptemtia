"""Numerical Drift Metric Placeholders for Phase 142.

Defines non-executing statistical moments drift contracts (mean shift, variance ratio,
skewness/kurtosis changes) without performing numerical summary calculations.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftMetricPlaceholder


def build_numerical_drift_metric_placeholders() -> List[DriftMetricPlaceholder]:
    """Builds non-executing numerical drift metric placeholders."""
    metrics = [
        DriftMetricPlaceholder(
            metric_id="metric_num_mean_standardized_diff",
            metric_name="Standardized Mean Difference (SMD) Placeholder",
            metric_type="standardized_mean_difference",
            target_scope="feature",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder=None,
            description="Measures standardized mean shift (mu_curr - mu_ref) / sigma_ref for numerical feature series.",
            metadata={
                "formula": "(mean_curr - mean_ref) / std_ref",
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_num_variance_ratio",
            metric_name="Variance Ratio Shift Placeholder",
            metric_type="variance_ratio_shift",
            target_scope="feature",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder=None,
            description="Measures variance expansion or contraction var_curr / var_ref across financial volatility features.",
            metadata={
                "formula": "var_curr / var_ref",
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_num_quantile_shift",
            metric_name="Median & Interquartile Range Shift Placeholder",
            metric_type="quantile_shift",
            target_scope="feature",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder=None,
            description="Measures shifts across q25, median, and q75 for robust outlier-resistant drift profiling.",
            metadata={
                "quantiles": [0.25, 0.5, 0.75],
                "execution_mode": "non_executing_contract",
            },
        ),
    ]
    return metrics


def validate_numerical_drift_metric_placeholder(metric: DriftMetricPlaceholder) -> Dict[str, Any]:
    """Validates that numerical drift placeholder adheres to non-executing rules."""
    errors = []
    if metric.calculation_enabled:
        errors.append("calculation_enabled must be False for numerical drift placeholders.")
    if not metric.metric_id.startswith("metric_num_"):
        errors.append("metric_id must start with 'metric_num_'.")

    return {
        "valid": len(errors) == 0,
        "metric_id": metric.metric_id,
        "metric_name": metric.metric_name,
        "errors": errors,
        "metric": asdict(metric),
    }
