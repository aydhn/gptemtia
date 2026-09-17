"""Drift Metric Calculation Disabled Enforcer for Phase 142.

Enforces strict non-executing safety boundary preventing live statistical calculations,
hypothesis testing, or numerical divergence computations on data series.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict

from advanced_model_drift_monitoring.model_drift_models import DriftDisabledExecutionItem


def build_drift_metric_calculation_disabled_item() -> DriftDisabledExecutionItem:
    """Builds the disabled execution item for drift metric calculation."""
    return DriftDisabledExecutionItem(
        execution_id="dis_exec_metric_calc_001",
        execution_type="drift_calculation_disabled",
        target_component="drift_metric_calculators",
        status="active_enforcement",
        is_disabled=True,
        disabled_reason="Phase 142 establishes drift contracts only. Real-time metric computations are strictly forbidden.",
        remediation_required="Do not invoke numerical calculators or hypothesis testing algorithms.",
        metadata={
            "blocked_metrics": ["psi", "ks", "js", "wasserstein", "correlation_drift", "ece_drift"],
            "allow_placeholders_only": True,
            "phase": 142,
        },
    )


def assert_drift_metric_calculation_disabled(request_params: Dict[str, Any]) -> Dict[str, Any]:
    """Validates that a request does not attempt live metric calculation.

    Raises RuntimeError if live calculation is explicitly requested.
    """
    if request_params.get("calculate_drift", False) or request_params.get("run_ks_test", False) or request_params.get("compute_psi", False):
        raise RuntimeError(
            "CRITICAL SAFETY VIOLATION: Drift metric calculation is strictly disabled in Phase 142 offline research contracts."
        )

    return {
        "status": "passed",
        "calculation_blocked": True,
        "item": asdict(build_drift_metric_calculation_disabled_item()),
    }
