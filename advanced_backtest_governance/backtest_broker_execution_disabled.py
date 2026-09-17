# -*- coding: utf-8 -*-
"""Phase 150: Backtest Broker Execution Disabled Report.

Documents the complete disabling of broker integration and gateway connectivity in Phase 150.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    DISABLED_EXECUTION_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
    EXEC_BLOCKED_NO_BROKER,
)

DISABLED_BROKER_OPS: List[Dict[str, Any]] = [
    {
        "operation_name": "connect_broker_gateway",
        "description": "Establishing live socket or FIX connection to broker execution gateway.",
        "status": "DISABLED",
    },
    {
        "operation_name": "query_broker_account",
        "description": "Fetching remote account balances or margin utilization.",
        "status": "DISABLED",
    },
    {
        "operation_name": "transmit_broker_order",
        "description": "Transmitting electronic orders to broker endpoints.",
        "status": "DISABLED",
    },
]

FORBIDDEN_BROKER_WORDS = [
    "broker_connect",
    "ibkr_client",
    "fix_gateway",
    "binance_api",
    "alpaca_trade",
    "broker_api",
    "submit_order_to_broker",
]


def validate_no_backtest_broker_execution_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request ensures zero broker connection or electronic execution."""
    text = str(request).lower()
    blocked = False
    violating_words: List[str] = []

    for word in FORBIDDEN_BROKER_WORDS:
        if word in text:
            blocked = True
            violating_words.append(word)

    return {
        "is_allowed": not blocked,
        "is_blocked": blocked,
        "violating_words": violating_words,
        "decision": EXEC_BLOCKED_NO_BROKER if blocked else "ALLOWED_CONTRACT_ONLY",
        "policy_message": (
            f"Broker execution is strictly disabled: violating words {violating_words}. Zero broker connectivity allowed."
            if blocked
            else "Complies with zero broker execution policy."
        ),
        "non_signal": True,
    }


def build_backtest_broker_execution_disabled_report(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for broker execution disabled report."""
    rows: List[Dict[str, Any]] = []
    for op in DISABLED_BROKER_OPS:
        rows.append({
            "operation_name": op["operation_name"],
            "description": op["description"],
            "status": op["status"],
            "broker_permitted": False,
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": DISABLED_EXECUTION_DOMAIN,
        "subdomain": "broker_execution_disabled",
        "total_disabled_operations": len(df),
        "all_broker_execution_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
