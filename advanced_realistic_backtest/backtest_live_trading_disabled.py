# -*- coding: utf-8 -*-
"""Phase 146: Backtest Live Trading Disabled Report.

Strictly enforces zero live trading, zero position execution, and zero capital deployment.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

BLOCKED_LIVE_TRADING_ACTIONS = [
    "live_trade",
    "live_trading",
    "real_money",
    "deploy_capital",
    "open_real_position",
    "buy",
    "sell",
    "long",
    "short",
]


def build_backtest_live_trading_disabled_report(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of disabled live trading rules."""
    rows = [
        {
            "execution_type": "LIVE_TRADING_EXECUTION",
            "status": "STRICTLY_PROHIBITED",
            "reason": "Live trading is categorically prohibited across all development and research phases.",
            "blocked_actions": str(BLOCKED_LIVE_TRADING_ACTIONS),
            "is_blocked": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "execution_type": "LIVE_TRADING_EXECUTION",
        "is_blocked": True,
        "policy_active": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_live_trading_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that request does not attempt live trading."""
    req_str = str(request).lower()
    for action in BLOCKED_LIVE_TRADING_ACTIONS:
        if action in req_str:
            return {
                "permitted": False,
                "action_found": action,
                "reason": f"Live trading action '{action}' is strictly prohibited.",
            }
    return {"permitted": True, "reason": "No live trading detected."}
