# -*- coding: utf-8 -*-
"""Phase 149: Bootstrap Execution Disabled Report Module.

Provides audit trail and request validator confirming physical bootstrap sampling is disabled.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISABLED_EXECUTION_DOMAIN,
    EXECUTION_BLOCKED_NO_BOOTSTRAP,
    MONTE_CARLO_CONTRACT_READY,
)


def validate_no_bootstrap_execution_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming requests do not attempt bootstrap sampling execution."""
    req_str = str(request).lower()
    prohibited = ["bootstrap_returns", "resample_returns", "shuffle_trades", "draw_bootstrap_sample"]
    for p in prohibited:
        if p in req_str:
            return {
                "execution_allowed": False,
                "reason": f"Prohibited bootstrap execution command detected: {p}",
                "status": EXECUTION_BLOCKED_NO_BOOTSTRAP,
            }
    return {
        "execution_allowed": False,
        "reason": "Bootstrap sampling execution disabled under Phase 149 contract layer.",
        "status": EXECUTION_BLOCKED_NO_BOOTSTRAP,
    }


def build_bootstrap_execution_disabled_report(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the bootstrap execution disabled report DataFrame and summary."""
    rows: List[Dict[str, Any]] = [
        {
            "capability": "physical_bootstrap_sampling",
            "execution_allowed": profile.allow_bootstrap_execution,
            "policy_reference": "POLICY_PHASE_149_ZERO_BOOTSTRAP",
            "status": EXECUTION_BLOCKED_NO_BOOTSTRAP,
            "description": "Prohibits drawing actual bootstrap resamples from return histories.",
        },
        {
            "capability": "block_bootstrap_generation",
            "execution_allowed": False,
            "policy_reference": "POLICY_PHASE_149_ZERO_BOOTSTRAP",
            "status": EXECUTION_BLOCKED_NO_BOOTSTRAP,
            "description": "Prohibits generating simulated block bootstrap synthetic time series.",
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
