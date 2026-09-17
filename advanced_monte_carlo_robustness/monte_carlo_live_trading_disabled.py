# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Live Trading Disabled Report Module.

Provides audit trail and request validator confirming live trading is disabled.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    DISABLED_EXECUTION_DOMAIN,
    EXECUTION_BLOCKED_NO_LIVE_TRADING,
    MONTE_CARLO_CONTRACT_READY,
)


def validate_no_monte_carlo_live_trading_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming requests do not attempt live trading."""
    req_str = str(request).lower()
    prohibited = ["live_trade", "trade", "open_position", "buy", "sell", "long", "short"]
    for p in prohibited:
        if p in req_str:
            return {
                "execution_allowed": False,
                "reason": f"Prohibited live trading command detected: {p}",
                "status": EXECUTION_BLOCKED_NO_LIVE_TRADING,
            }
    return {
        "execution_allowed": False,
        "reason": "Live trading disabled under Phase 149 contract layer.",
        "status": EXECUTION_BLOCKED_NO_LIVE_TRADING,
    }


def build_monte_carlo_live_trading_disabled_report(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the live trading disabled report DataFrame and summary."""
    rows: List[Dict[str, Any]] = [
        {
            "capability": "live_trading_execution",
            "execution_allowed": profile.allow_live_trading,
            "policy_reference": "POLICY_PHASE_149_ZERO_LIVE_TRADING",
            "status": EXECUTION_BLOCKED_NO_LIVE_TRADING,
            "description": "Prohibits committing live capital or opening market positions.",
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
