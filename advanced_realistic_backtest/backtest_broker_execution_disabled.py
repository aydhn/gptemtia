# -*- coding: utf-8 -*-
"""Phase 146: Backtest Broker Execution Disabled Report.

Strictly enforces zero broker connectivity, zero API key usage, and zero external order dispatch.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

BLOCKED_BROKER_ACTIONS = [
    "broker_order",
    "send_order",
    "connect_broker",
    "broker_api",
    "place_order",
    "route_order",
    "ibkr",
    "binance",
    "mt5",
]


def build_backtest_broker_execution_disabled_report(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of disabled broker execution rules."""
    rows = [
        {
            "execution_type": "BROKER_EXECUTION",
            "status": "STRICTLY_PROHIBITED",
            "reason": "Broker API connectivity and order dispatch are strictly prohibited.",
            "blocked_actions": str(BLOCKED_BROKER_ACTIONS),
            "is_blocked": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "execution_type": "BROKER_EXECUTION",
        "is_blocked": True,
        "policy_active": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_broker_execution_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that request does not attempt broker order execution."""
    req_str = str(request).lower()
    for action in BLOCKED_BROKER_ACTIONS:
        if action in req_str:
            return {
                "permitted": False,
                "action_found": action,
                "reason": f"Broker execution action '{action}' is strictly prohibited.",
            }
    return {"permitted": True, "reason": "No broker execution detected."}
