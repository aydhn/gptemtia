"""Categorical Drift Metric Placeholders for Phase 142.

Defines non-executing categorical distribution drift contracts (Chi-Square, TVD,
novel category appearance) without aggregating or modifying discrete categories.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftMetricPlaceholder


def build_categorical_drift_metric_placeholders() -> List[DriftMetricPlaceholder]:
    """Builds non-executing categorical drift metric placeholders."""
    metrics = [
        DriftMetricPlaceholder(
            metric_id="metric_cat_chi_square",
            metric_name="Categorical Chi-Square Goodness-of-Fit Placeholder",
            metric_type="chi_square_goodness_of_fit",
            target_scope="feature",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder=None,
            description="Chi-Square statistic placeholder comparing category frequencies in current vs reference windows.",
            metadata={
                "min_expected_count": 5,
                "degrees_of_freedom": "k - 1",
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_cat_total_variation_distance",
            metric_name="Total Variation Distance (TVD) Placeholder",
            metric_type="total_variation_distance",
            target_scope="feature",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder=None,
            description="TVD metric placeholder: 0.5 * sum(|p_curr(x) - p_ref(x)|) across category labels.",
            metadata={
                "bounded_range": "[0, 1]",
                "handling_novel_categories": "assign_to_new_bin",
                "execution_mode": "non_executing_contract",
            },
        ),
    ]
    return metrics


def validate_categorical_drift_metric_placeholder(metric: DriftMetricPlaceholder) -> Dict[str, Any]:
    """Validates that categorical drift placeholder adheres to non-executing rules."""
    errors = []
    if metric.calculation_enabled:
        errors.append("calculation_enabled must be False for categorical drift placeholders.")
    if not metric.metric_id.startswith("metric_cat_"):
        errors.append("metric_id must start with 'metric_cat_'.")

    return {
        "valid": len(errors) == 0,
        "metric_id": metric.metric_id,
        "metric_name": metric.metric_name,
        "errors": errors,
        "metric": asdict(metric),
    }
