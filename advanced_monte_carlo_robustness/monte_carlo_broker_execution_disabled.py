# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Broker Execution Disabled Report Module.

Provides audit trail and request validator confirming broker execution is disabled.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISABLED_EXECUTION_DOMAIN,
    EXECUTION_BLOCKED_NO_BROKER,
    MONTE_CARLO_CONTRACT_READY,
)


def validate_no_monte_carlo_broker_execution_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming requests do not attempt broker execution."""
    req_str = str(request).lower()
    prohibited = ["broker_order", "send_order", "place_order", "broker_api", "fix_protocol"]
    for p in prohibited:
        if p in req_str:
            return {
                "execution_allowed": False,
                "reason": f"Prohibited broker execution command detected: {p}",
                "status": EXECUTION_BLOCKED_NO_BROKER,
            }
    return {
        "execution_allowed": False,
        "reason": "Broker execution disabled under Phase 149 contract layer.",
        "status": EXECUTION_BLOCKED_NO_BROKER,
    }


def build_monte_carlo_broker_execution_disabled_report(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the broker execution disabled report DataFrame and summary."""
    rows: List[Dict[str, Any]] = [
        {
            "capability": "broker_order_transmission",
            "execution_allowed": profile.allow_broker_integration,
            "policy_reference": "POLICY_PHASE_149_ZERO_BROKER",
            "status": EXECUTION_BLOCKED_NO_BROKER,
            "description": "Prohibits transmitting order payloads to external broker or exchange endpoints.",
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
