# -*- coding: utf-8 -*-
"""Phase 146: Backtest Optimizer Disabled Report.

Enforces that parameter and strategy optimizers are strictly disabled.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

BLOCKED_OPTIMIZER_ACTIONS = [
    "optimize",
    "run_optimizer",
    "grid_search",
    "bayesian_optimization",
    "genetic_algorithm",
]


def build_backtest_optimizer_disabled_report(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of disabled optimizer rules."""
    rows = [
        {
            "execution_type": "STRATEGY_OPTIMIZER_EXECUTION",
            "status": "BLOCKED_BY_POLICY",
            "reason": "Parameter search and strategy optimization are strictly disabled in Phase 146.",
            "blocked_actions": str(BLOCKED_OPTIMIZER_ACTIONS),
            "is_blocked": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "execution_type": "STRATEGY_OPTIMIZER_EXECUTION",
        "is_blocked": True,
        "policy_active": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_optimizer_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that request does not request optimizer execution."""
    req_str = str(request).lower()
    for action in BLOCKED_OPTIMIZER_ACTIONS:
        if action in req_str:
            return {
                "permitted": False,
                "action_found": action,
                "reason": f"Optimizer request '{action}' is strictly blocked in Phase 146.",
            }
    return {"permitted": True, "reason": "No optimizer request detected."}
