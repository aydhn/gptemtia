"""Missingness Drift Metric Placeholders for Phase 142.

Defines non-executing missingness rate shift contracts across features and datasets
without counting NaNs or modifying underlying tabular data.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftMetricPlaceholder


def build_missingness_drift_metric_placeholders() -> List[DriftMetricPlaceholder]:
    """Builds non-executing missingness drift metric placeholders."""
    metrics = [
        DriftMetricPlaceholder(
            metric_id="metric_missing_rate_delta",
            metric_name="Feature Missingness Rate Delta Placeholder",
            metric_type="missingness_rate_delta",
            target_scope="feature",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder="thresh_missingness_delta",
            description="Measures absolute change in feature missingness proportion |rate_curr - rate_ref|.",
            metadata={
                "baseline_source": "phase_123_quality_report",
                "missing_indicators": ["nan", "null", "none"],
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_missing_surge_detector",
            metric_name="Dataset Missingness Surge Placeholder",
            metric_type="missingness_surge_check",
            target_scope="dataset",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder="thresh_missingness_delta",
            description="Detects sudden block-level missingness spikes across multi-asset feature columns.",
            metadata={
                "baseline_source": "phase_124_featurestore_catalog",
                "surge_multiplier": 2.0,
                "execution_mode": "non_executing_contract",
            },
        ),
    ]
    return metrics


def validate_missingness_drift_metric_placeholder(metric: DriftMetricPlaceholder) -> Dict[str, Any]:
    """Validates that missingness drift placeholder adheres to non-executing rules."""
    errors = []
    if metric.calculation_enabled:
        errors.append("calculation_enabled must be False for missingness drift placeholders.")
    if not metric.metric_id.startswith("metric_missing_"):
        errors.append("metric_id must start with 'metric_missing_'.")

    return {
        "valid": len(errors) == 0,
        "metric_id": metric.metric_id,
        "metric_name": metric.metric_name,
        "errors": errors,
        "metric": asdict(metric),
    }
