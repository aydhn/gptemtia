# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Execution Disabled Report Module.

Provides audit trail and request validator confirming true Monte Carlo simulation execution is disabled.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISABLED_EXECUTION_DOMAIN,
    EXECUTION_BLOCKED_NO_MONTE_CARLO,
    MONTE_CARLO_CONTRACT_READY,
)


def validate_no_monte_carlo_execution_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming requests do not attempt Monte Carlo simulation execution."""
    req_str = str(request).lower()
    prohibited = ["run_monte_carlo", "execute_monte_carlo", "simulate_paths", "generate_paths"]
    for p in prohibited:
        if p in req_str:
            return {
                "execution_allowed": False,
                "reason": f"Prohibited Monte Carlo execution command detected: {p}",
                "status": EXECUTION_BLOCKED_NO_MONTE_CARLO,
            }
    return {
        "execution_allowed": False,
        "reason": "Monte Carlo execution disabled under Phase 149 contract-only layer.",
        "status": EXECUTION_BLOCKED_NO_MONTE_CARLO,
    }


def build_monte_carlo_execution_disabled_report(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the Monte Carlo execution disabled report DataFrame and summary."""
    rows: List[Dict[str, Any]] = [
        {
            "capability": "true_monte_carlo_path_generation",
            "execution_allowed": profile.allow_monte_carlo_execution,
            "policy_reference": "POLICY_PHASE_149_ZERO_SIMULATION",
            "status": EXECUTION_BLOCKED_NO_MONTE_CARLO,
            "description": "Prohibits generating synthetic asset price trajectories or simulated path sets.",
        },
        {
            "capability": "multivariate_copula_simulation",
            "execution_allowed": False,
            "policy_reference": "POLICY_PHASE_149_ZERO_SIMULATION",
            "status": EXECUTION_BLOCKED_NO_MONTE_CARLO,
            "description": "Prohibits generating simulated joint asset returns from copula structures.",
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
