# -*- coding: utf-8 -*-
"""Phase 146: Backtest Performance Claim Disabled Report.

Enforces zero performance guarantees, zero return claims, and prohibition of broker/production readiness claims.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

BLOCKED_PERFORMANCE_CLAIMS = [
    "guaranteed_return",
    "sharpe_claim",
    "win_rate_claim",
    "production_ready",
    "broker_ready",
    "live_trading_approved",
    "guaranteed_profit",
    "official_approval",
]


def build_backtest_performance_claim_disabled_report(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of disabled performance claim rules."""
    rows = [
        {
            "execution_type": "PERFORMANCE_CLAIM_ASSERTION",
            "status": "STRICTLY_PROHIBITED",
            "reason": "Performance claims, return guarantees, and production/broker readiness claims are strictly prohibited.",
            "blocked_actions": str(BLOCKED_PERFORMANCE_CLAIMS),
            "is_blocked": True,
            "non_signal": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "execution_type": "PERFORMANCE_CLAIM_ASSERTION",
        "is_blocked": True,
        "policy_active": True,
        "non_signal": True,
    }
    return df, summary


def validate_no_performance_claim_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that request does not assert forbidden performance claims."""
    req_str = str(request).lower()
    for claim in BLOCKED_PERFORMANCE_CLAIMS:
        if claim in req_str:
            return {
                "permitted": False,
                "claim_found": claim,
                "reason": f"Performance claim '{claim}' is strictly prohibited.",
            }
    return {"permitted": True, "reason": "No forbidden performance claim detected."}
