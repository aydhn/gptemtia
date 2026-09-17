# -*- coding: utf-8 -*-
"""Phase 146: Backtest Execution Disabled Report.

Enforces that actual backtest execution is strictly disabled in Phase 146 contract layer.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

BLOCKED_BACKTEST_ACTIONS = [
    "run_backtest",
    "execute_backtest",
    "run_simulation",
    "execute_strategy",
]


def build_backtest_execution_disabled_report(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of disabled backtest execution rules."""
    rows = [
        {
            "execution_type": "REAL_BACKTEST_EXECUTION",
            "status": "BLOCKED_BY_POLICY",
            "reason": "Phase 146 is strictly contract, cost, and slippage modeling. Execution is blocked.",
            "blocked_actions": str(BLOCKED_BACKTEST_ACTIONS),
            "is_blocked": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "execution_type": "REAL_BACKTEST_EXECUTION",
        "is_blocked": True,
        "policy_active": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_backtest_execution_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming request does not trigger backtest execution."""
    req_str = str(request).lower()
    for action in BLOCKED_BACKTEST_ACTIONS:
        if action in req_str:
            return {
                "permitted": False,
                "action_found": action,
                "reason": f"Execution request '{action}' is strictly blocked in Phase 146.",
            }
    return {"permitted": True, "reason": "No execution request detected."}
