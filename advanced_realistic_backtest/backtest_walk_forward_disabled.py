# -*- coding: utf-8 -*-
"""Phase 146: Backtest Walk-Forward Disabled Report.

Enforces that walk-forward validation execution is deferred until Phase 147.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

BLOCKED_WALK_FORWARD_ACTIONS = [
    "walk_forward",
    "run_walk_forward",
    "rolling_window_validation",
    "anchored_walk_forward",
]


def build_backtest_walk_forward_disabled_report(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of disabled walk-forward execution rules."""
    rows = [
        {
            "execution_type": "WALK_FORWARD_EXECUTION",
            "status": "DEFERRED_TO_PHASE_147",
            "reason": "Walk-forward validation is the dedicated core subject of Phase 147.",
            "blocked_actions": str(BLOCKED_WALK_FORWARD_ACTIONS),
            "is_blocked": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "execution_type": "WALK_FORWARD_EXECUTION",
        "is_blocked": True,
        "policy_active": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_walk_forward_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that request does not trigger walk-forward execution."""
    req_str = str(request).lower()
    for action in BLOCKED_WALK_FORWARD_ACTIONS:
        if action in req_str:
            return {
                "permitted": False,
                "action_found": action,
                "reason": f"Walk-forward request '{action}' is deferred to Phase 147.",
            }
    return {"permitted": True, "reason": "No walk-forward request detected."}
