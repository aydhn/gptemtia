# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Metric Calculation Disabled Report Module.

Provides audit trail and request validator confirming metric calculation is disabled.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISABLED_EXECUTION_DOMAIN,
    EXECUTION_BLOCKED_NO_METRIC_CALCULATION,
    MONTE_CARLO_CONTRACT_READY,
)


def validate_no_monte_carlo_metric_calculation_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming requests do not attempt metric calculation."""
    req_str = str(request).lower()
    prohibited = [
        "calculate_var",
        "calculate_expected_shortfall",
        "calculate_distribution",
        "calculate_robustness",
        "compute_metric",
    ]
    for p in prohibited:
        if p in req_str:
            return {
                "execution_allowed": False,
                "reason": f"Prohibited metric calculation command detected: {p}",
                "status": EXECUTION_BLOCKED_NO_METRIC_CALCULATION,
            }
    return {
        "execution_allowed": False,
        "reason": "Metric calculation disabled under Phase 149 contract layer.",
        "status": EXECUTION_BLOCKED_NO_METRIC_CALCULATION,
    }


def build_monte_carlo_metric_calculation_disabled_report(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the metric calculation disabled report DataFrame and summary."""
    rows: List[Dict[str, Any]] = [
        {
            "capability": "real_var_calculation",
            "execution_allowed": profile.allow_var_calculation,
            "policy_reference": "POLICY_PHASE_149_ZERO_METRICS",
            "status": EXECUTION_BLOCKED_NO_METRIC_CALCULATION,
            "description": "Prohibits calculating empirical or parametric Value at Risk numbers.",
        },
        {
            "capability": "expected_shortfall_calculation",
            "execution_allowed": profile.allow_expected_shortfall_calculation,
            "policy_reference": "POLICY_PHASE_149_ZERO_METRICS",
            "status": EXECUTION_BLOCKED_NO_METRIC_CALCULATION,
            "description": "Prohibits calculating empirical Expected Shortfall (CVaR).",
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISABLED_EXECUTION_DOMAIN,
        "total_capabilities": len(df),
        "all_executions_blocked": bool((~df["execution_allowed"]).all()),
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
