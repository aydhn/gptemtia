# -*- coding: utf-8 -*-
"""Phase 149: Parameter Sweep Execution Disabled Report Module.

Provides audit trail and request validator confirming exhaustive parameter sweeps are disabled.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISABLED_EXECUTION_DOMAIN,
    EXECUTION_BLOCKED_NO_PARAMETER_SWEEP,
    MONTE_CARLO_CONTRACT_READY,
)


def validate_no_parameter_sweep_execution_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming requests do not attempt parameter sweep execution."""
    req_str = str(request).lower()
    prohibited = ["parameter_sweep", "grid_sweep", "run_parameter_grid", "exhaustive_sweep"]
    for p in prohibited:
        if p in req_str:
            return {
                "execution_allowed": False,
                "reason": f"Prohibited parameter sweep command detected: {p}",
                "status": EXECUTION_BLOCKED_NO_PARAMETER_SWEEP,
            }
    return {
        "execution_allowed": False,
        "reason": "Parameter sweep execution disabled under Phase 149 contract layer.",
        "status": EXECUTION_BLOCKED_NO_PARAMETER_SWEEP,
    }


def build_parameter_sweep_execution_disabled_report(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the parameter sweep execution disabled report DataFrame and summary."""
    rows: List[Dict[str, Any]] = [
        {
            "capability": "exhaustive_grid_sweep",
            "execution_allowed": profile.allow_parameter_sweep_execution,
            "policy_reference": "POLICY_PHASE_149_ZERO_SWEEPS",
            "status": EXECUTION_BLOCKED_NO_PARAMETER_SWEEP,
            "description": "Prohibits evaluating large combinatoric grids of hyperparameters.",
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
