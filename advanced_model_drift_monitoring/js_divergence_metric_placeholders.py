"""Jensen-Shannon (JS) Divergence Metric Placeholders for Phase 142.

Defines non-executing Jensen-Shannon divergence contracts for discrete feature distributions,
regime probability allocations, and calibrated score partitions.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftMetricPlaceholder


def build_js_divergence_metric_placeholders() -> List[DriftMetricPlaceholder]:
    """Builds non-executing Jensen-Shannon divergence metric placeholders."""
    metrics = [
        DriftMetricPlaceholder(
            metric_id="metric_js_regime_distribution",
            metric_name="Regime Class Probabilities JS Divergence Placeholder",
            metric_type="jensen_shannon_divergence",
            target_scope="dataset",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder="thresh_js_divergence_distribution",
            description="JS divergence placeholder comparing historical regime frequencies against current window distribution.",
            metadata={
                "base": "e",
                "bounded_range": "[0, ln(2)]",
                "symmetric": True,
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_js_categorical_features",
            metric_name="Categorical Features JS Divergence Placeholder",
            metric_type="jensen_shannon_divergence",
            target_scope="feature",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder="thresh_js_divergence_distribution",
            description="JS divergence placeholder for discrete and categorical feature distribution shifts.",
            metadata={
                "base": "2",
                "bounded_range": "[0, 1]",
                "symmetric": True,
                "execution_mode": "non_executing_contract",
            },
        ),
    ]
    return metrics


def validate_js_divergence_metric_placeholder(metric: DriftMetricPlaceholder) -> Dict[str, Any]:
    """Validates that JS divergence placeholder maintains non-executing safety."""
    errors = []
    if metric.calculation_enabled:
        errors.append("calculation_enabled must be False for JS divergence placeholders.")
    if not metric.metric_id.startswith("metric_js_"):
        errors.append("metric_id must start with 'metric_js_'.")

    return {
        "valid": len(errors) == 0,
        "metric_id": metric.metric_id,
        "metric_name": metric.metric_name,
        "errors": errors,
        "metric": asdict(metric),
    }
