"""Master Drift Metric Placeholders Aggregator for Phase 142.

Combines all statistical, divergence, missingness, correlation, calibration,
and uncertainty drift metric placeholders into a single governed registry.
Strictly non-executing and contract-only.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, List

from advanced_model_drift_monitoring.calibration_drift_metric_placeholders import (
    build_calibration_drift_metric_placeholders,
)
from advanced_model_drift_monitoring.categorical_drift_metric_placeholders import (
    build_categorical_drift_metric_placeholders,
)
from advanced_model_drift_monitoring.correlation_drift_metric_placeholders import (
    build_correlation_drift_metric_placeholders,
)
from advanced_model_drift_monitoring.js_divergence_metric_placeholders import (
    build_js_divergence_metric_placeholders,
)
from advanced_model_drift_monitoring.ks_metric_placeholders import (
    build_ks_metric_placeholders,
)
from advanced_model_drift_monitoring.missingness_drift_metric_placeholders import (
    build_missingness_drift_metric_placeholders,
)
from advanced_model_drift_monitoring.model_drift_models import DriftMetricPlaceholder
from advanced_model_drift_monitoring.numerical_drift_metric_placeholders import (
    build_numerical_drift_metric_placeholders,
)
from advanced_model_drift_monitoring.psi_metric_placeholders import (
    build_psi_metric_placeholders,
)
from advanced_model_drift_monitoring.uncertainty_drift_metric_placeholders import (
    build_uncertainty_drift_metric_placeholders,
)
from advanced_model_drift_monitoring.wasserstein_metric_placeholders import (
    build_wasserstein_metric_placeholders,
)


def build_all_drift_metric_placeholders() -> List[DriftMetricPlaceholder]:
    """Builds the comprehensive list of all drift metric placeholders."""
    all_metrics: List[DriftMetricPlaceholder] = []
    all_metrics.extend(build_psi_metric_placeholders())
    all_metrics.extend(build_ks_metric_placeholders())
    all_metrics.extend(build_js_divergence_metric_placeholders())
    all_metrics.extend(build_wasserstein_metric_placeholders())
    all_metrics.extend(build_correlation_drift_metric_placeholders())
    all_metrics.extend(build_missingness_drift_metric_placeholders())
    all_metrics.extend(build_categorical_drift_metric_placeholders())
    all_metrics.extend(build_numerical_drift_metric_placeholders())
    all_metrics.extend(build_calibration_drift_metric_placeholders())
    all_metrics.extend(build_uncertainty_drift_metric_placeholders())
    return all_metrics


def summarize_drift_metric_placeholders(
    metrics: List[DriftMetricPlaceholder],
) -> Dict[str, Any]:
    """Generates a summary breakdown of drift metric placeholders."""
    by_type: Dict[str, int] = {}
    by_scope: Dict[str, int] = {}
    any_executing = False

    for m in metrics:
        by_type[m.metric_type] = by_type.get(m.metric_type, 0) + 1
        by_scope[m.target_scope] = by_scope.get(m.target_scope, 0) + 1
        if m.calculation_enabled:
            any_executing = True

    return {
        "total_metrics": len(metrics),
        "by_type": by_type,
        "by_scope": by_scope,
        "all_calculation_disabled": not any_executing,
        "non_executing_compliance": not any_executing,
        "metrics": [asdict(m) for m in metrics],
    }
