# -*- coding: utf-8 -*-
"""Phase 150: Backtest Live Trading Disabled Report.

Documents the complete disabling of live trading, order routing, and execution in Phase 150.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    DISABLED_EXECUTION_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
    EXEC_BLOCKED_NO_LIVE_TRADING,
)

DISABLED_LIVE_OPS: List[Dict[str, Any]] = [
    {
        "operation_name": "place_live_order",
        "description": "Routing live market or limit orders to exchanges.",
        "status": "DISABLED",
    },
    {
        "operation_name": "manage_live_position",
        "description": "Dynamic risk adjustments on active live brokerage accounts.",
        "status": "DISABLED",
    },
    {
        "operation_name": "rebalance_live_portfolio",
        "description": "Real-time portfolio rebalancing execution.",
        "status": "DISABLED",
    },
]

FORBIDDEN_LIVE_WORDS = [
    "live_trade",
    "live_execution",
    "place_order",
    "market_order",
    "limit_order",
    "real_money",
    "execute_order",
    "send_order",
]


def validate_no_backtest_live_trading_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request ensures zero live trading, order execution, or real money routing."""
    text = str(request).lower()
    blocked = False
    violating_words: List[str] = []

    for word in FORBIDDEN_LIVE_WORDS:
        if word in text:
            blocked = True
            violating_words.append(word)

    return {
        "is_allowed": not blocked,
        "is_blocked": blocked,
        "violating_words": violating_words,
        "decision": EXEC_BLOCKED_NO_LIVE_TRADING if blocked else "ALLOWED_CONTRACT_ONLY",
        "policy_message": (
            f"Live trading is strictly disabled: violating words {violating_words}. System is local offline research only."
            if blocked
            else "Complies with zero live trading policy."
        ),
        "non_signal": True,
    }


def build_backtest_live_trading_disabled_report(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for live trading disabled report."""
    rows: List[Dict[str, Any]] = []
    for op in DISABLED_LIVE_OPS:
        rows.append({
            "operation_name": op["operation_name"],
            "description": op["description"],
            "status": op["status"],
            "live_permitted": False,
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISABLED_EXECUTION_DOMAIN,
        "subdomain": "live_trading_disabled",
        "total_disabled_operations": len(df),
        "all_live_trading_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
