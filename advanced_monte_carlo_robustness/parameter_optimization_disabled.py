# -*- coding: utf-8 -*-
"""Phase 149: Parameter Optimization Disabled Report Module.

Provides audit trail and request validator confirming parameter optimization is disabled.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISABLED_EXECUTION_DOMAIN,
    EXECUTION_BLOCKED_NO_PARAMETER_OPTIMIZATION,
    MONTE_CARLO_CONTRACT_READY,
)


def validate_no_parameter_optimization_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming requests do not attempt parameter optimization."""
    req_str = str(request).lower()
    prohibited = ["optimize_parameters", "parameter_optimization", "run_optimizer", "search_parameters", "find_best_parameters"]
    for p in prohibited:
        if p in req_str:
            return {
                "execution_allowed": False,
                "reason": f"Prohibited parameter optimization command detected: {p}",
                "status": EXECUTION_BLOCKED_NO_PARAMETER_OPTIMIZATION,
            }
    return {
        "execution_allowed": False,
        "reason": "Parameter optimization disabled under Phase 149 contract layer.",
        "status": EXECUTION_BLOCKED_NO_PARAMETER_OPTIMIZATION,
    }


def build_parameter_optimization_disabled_report(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the parameter optimization disabled report DataFrame and summary."""
    rows: List[Dict[str, Any]] = [
        {
            "capability": "parameter_optimization_engine",
            "execution_allowed": profile.allow_parameter_optimization,
            "policy_reference": "POLICY_PHASE_149_ZERO_OPTIMIZER",
            "status": EXECUTION_BLOCKED_NO_PARAMETER_OPTIMIZATION,
            "description": "Prohibits gradient descent, genetic algorithms, or bayesian optimization of parameters.",
        },
        {
            "capability": "curve_fitting_routines",
            "execution_allowed": False,
            "policy_reference": "POLICY_PHASE_149_ZERO_OPTIMIZER",
            "status": EXECUTION_BLOCKED_NO_PARAMETER_OPTIMIZATION,
            "description": "Prohibits tuning strategy rules to maximize in-sample backtest metrics.",
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
