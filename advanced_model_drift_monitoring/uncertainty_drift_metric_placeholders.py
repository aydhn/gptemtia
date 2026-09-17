"""Uncertainty Drift Metric Placeholders for Phase 142.

Defines non-executing uncertainty drift contracts (predictive entropy drift,
epistemic variance shift, conformal prediction set size drift) linked to Phase 141.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftMetricPlaceholder


def build_uncertainty_drift_metric_placeholders() -> List[DriftMetricPlaceholder]:
    """Builds non-executing uncertainty drift metric placeholders."""
    metrics = [
        DriftMetricPlaceholder(
            metric_id="metric_uncert_entropy_drift",
            metric_name="Predictive Shannon Entropy Drift Placeholder",
            metric_type="predictive_entropy_drift",
            target_scope="uncertainty",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder=None,
            description="Monitors shifts in mean predictive entropy H(p) = -sum(p * log(p)) between windows.",
            metadata={
                "linked_phase": "Phase 141",
                "entropy_type": "shannon",
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_uncert_epistemic_variance_drift",
            metric_name="Ensemble Epistemic Variance Drift Placeholder",
            metric_type="epistemic_variance_drift",
            target_scope="uncertainty",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder=None,
            description="Monitors variance of candidate model outputs across ensemble members without calculation.",
            metadata={
                "linked_phase": "Phase 141",
                "variance_type": "disagreement_epistemic",
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_uncert_conformal_set_size_drift",
            metric_name="Conformal Prediction Set Size Expansion Placeholder",
            metric_type="conformal_set_size_drift",
            target_scope="uncertainty",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder=None,
            description="Monitors inflation of conformal prediction set cardinality or interval width under distribution shift.",
            metadata={
                "linked_phase": "Phase 141",
                "conformal_target_coverage": 0.90,
                "execution_mode": "non_executing_contract",
            },
        ),
    ]
    return metrics


def validate_uncertainty_drift_metric_placeholder(metric: DriftMetricPlaceholder) -> Dict[str, Any]:
    """Validates that uncertainty drift placeholder adheres to non-executing rules."""
    errors = []
    if metric.calculation_enabled:
        errors.append("calculation_enabled must be False for uncertainty drift placeholders.")
    if not metric.metric_id.startswith("metric_uncert_"):
        errors.append("metric_id must start with 'metric_uncert_'.")

    return {
        "valid": len(errors) == 0,
        "metric_id": metric.metric_id,
        "metric_name": metric.metric_name,
        "errors": errors,
        "metric": asdict(metric),
    }
