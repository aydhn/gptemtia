# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Live Trading Disabled Module.

Documents and enforces prohibition against live trading or real order execution.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DISABLED_EXECUTION_DOMAIN,
    EXEC_BLOCKED_NO_LIVE_TRADING,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_LIVE_TRADING_TERMS = [
    "live_trade",
    "live_trading",
    "send_order",
    "real_money_order",
    "dispatch_order",
    "execute_live",
]


def build_evaluation_live_trading_disabled_report(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame report certifying live trading is disabled."""
    rows = [
        {
            "operation": "live_trading",
            "is_disabled": True,
            "policy_code": EXEC_BLOCKED_NO_LIVE_TRADING,
            "reason": "Phase 151 is an offline/local research phase; live trading is strictly prohibited.",
            "status": STATUS_EVALUATION_CONTRACT_READY,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DISABLED_EXECUTION_DOMAIN,
        "operation": "live_trading",
        "is_disabled": True,
        "status": EXEC_BLOCKED_NO_LIVE_TRADING,
        "non_signal": True,
    }
    return df, summary


def validate_no_evaluation_live_trading_request(request: Dict[str, Any] | str) -> Dict[str, Any]:
    """Validate request to ensure no live trading was requested."""
    text_to_check = request if isinstance(request, str) else " ".join(str(v) for v in request.values())
    text_lower = text_to_check.lower()

    detected = [term for term in FORBIDDEN_LIVE_TRADING_TERMS if term in text_lower]
    is_blocked = len(detected) > 0

    return {
        "is_permitted": not is_blocked,
        "is_blocked": is_blocked,
        "detected_terms": detected,
        "status": "PASS" if not is_blocked else EXEC_BLOCKED_NO_LIVE_TRADING,
        "policy_action": "ALLOW" if not is_blocked else "LIVE_TRADING_BLOCKED_BY_POLICY",
        "non_signal": True,
    }
