"""Correlation Drift Metric Placeholders for Phase 142.

Defines non-executing correlation drift contracts (Frobenius norm, max pairwise drift,
eigenstructure shifts) without computing actual covariance/correlation matrices.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftMetricPlaceholder


def build_correlation_drift_metric_placeholders() -> List[DriftMetricPlaceholder]:
    """Builds non-executing correlation drift metric placeholders."""
    metrics = [
        DriftMetricPlaceholder(
            metric_id="metric_corr_frobenius_norm",
            metric_name="Correlation Matrix Frobenius Norm Drift Placeholder",
            metric_type="correlation_matrix_frobenius_drift",
            target_scope="feature",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder=None,
            description="Measures Frobenius norm divergence ||R_ref - R_curr||_F across monitored feature blocks.",
            metadata={
                "norm_type": "frobenius",
                "regularization": "ledoit_wolf_placeholder",
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_corr_max_pairwise_drift",
            metric_name="Maximum Pairwise Correlation Drift Placeholder",
            metric_type="max_pairwise_correlation_drift",
            target_scope="feature",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder=None,
            description="Identifies maximum absolute change in pairwise correlation max|rho_ref(i,j) - rho_curr(i,j)|.",
            metadata={
                "metric": "max_abs_diff",
                "clip_range": [-1.0, 1.0],
                "execution_mode": "non_executing_contract",
            },
        ),
    ]
    return metrics


def validate_correlation_drift_metric_placeholder(metric: DriftMetricPlaceholder) -> Dict[str, Any]:
    """Validates that correlation drift placeholder adheres to non-executing rules."""
    errors = []
    if metric.calculation_enabled:
        errors.append("calculation_enabled must be False for correlation drift placeholders.")
    if not metric.metric_id.startswith("metric_corr_"):
        errors.append("metric_id must start with 'metric_corr_'.")

    return {
        "valid": len(errors) == 0,
        "metric_id": metric.metric_id,
        "metric_name": metric.metric_name,
        "errors": errors,
        "metric": asdict(metric),
    }
