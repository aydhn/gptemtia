"""Population Stability Index (PSI) Metric Placeholders for Phase 142.

Defines PSI drift metric contracts across features, predictions, and datasets
without executing binning, frequency counting, or PSI calculation.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.model_drift_models import DriftMetricPlaceholder


def build_psi_metric_placeholders() -> List[DriftMetricPlaceholder]:
    """Builds non-executing PSI metric placeholders."""
    metrics = [
        DriftMetricPlaceholder(
            metric_id="metric_psi_feature_macro",
            metric_name="Macro Features PSI Placeholder",
            metric_type="population_stability_index",
            target_scope="feature",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder="thresh_psi_standard_feature",
            description="PSI metric placeholder for macro-economic and fundamental feature shifts.",
            metadata={
                "binning_strategy": "quantile_10_bins",
                "epsilon_smoothing": 1e-4,
                "zero_division_guard": True,
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_psi_feature_technical",
            metric_name="Technical Features PSI Placeholder",
            metric_type="population_stability_index",
            target_scope="feature",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder="thresh_psi_standard_feature",
            description="PSI metric placeholder for rolling momentum, trend, and volatility feature shifts.",
            metadata={
                "binning_strategy": "uniform_10_bins",
                "epsilon_smoothing": 1e-4,
                "zero_division_guard": True,
                "execution_mode": "non_executing_contract",
            },
        ),
        DriftMetricPlaceholder(
            metric_id="metric_psi_model_predictions",
            metric_name="Model Prediction Distribution PSI Placeholder",
            metric_type="population_stability_index",
            target_scope="prediction",
            status="placeholder",
            calculation_enabled=False,
            threshold_placeholder="thresh_psi_prediction_distribution",
            description="PSI metric placeholder comparing reference and current prediction probability distributions.",
            metadata={
                "binning_strategy": "probability_deciles",
                "epsilon_smoothing": 1e-5,
                "zero_division_guard": True,
                "execution_mode": "non_executing_contract",
            },
        ),
    ]
    return metrics


def validate_psi_metric_placeholder(metric: DriftMetricPlaceholder) -> Dict[str, Any]:
    """Validates that PSI placeholder maintains non-executing rules."""
    errors = []
    if metric.calculation_enabled:
        errors.append("calculation_enabled must be False for PSI placeholders.")
    if metric.status not in ("placeholder", "contract_only", "governed"):
        errors.append(f"Invalid status: {metric.status}")
    if not metric.metric_id.startswith("metric_psi_"):
        errors.append("metric_id must start with 'metric_psi_'.")

    return {
        "valid": len(errors) == 0,
        "metric_id": metric.metric_id,
        "metric_name": metric.metric_name,
        "errors": errors,
        "metric": asdict(metric),
    }
