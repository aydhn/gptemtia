# -*- coding: utf-8 -*-
"""Phase 144: Governance Live Trading Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

FORBIDDEN_LIVE_TRADING_TERMS = [
    "live_trading",
    "live_trading_ready",
    "submit_order",
    "open_position",
    "close_position",
    "real_order",
]


def build_governance_live_trading_disabled_report(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled live trading."""
    prof = profile or get_model_governance_profile()
    records = [
        {"action": "live_trading", "is_disabled": True, "reason": "Live trading execution is permanently disabled in this repository."},
        {"action": "order_submission", "is_disabled": True, "reason": "Real exchange order submission is strictly prohibited."},
    ]
    for r in records:
        r["status"] = "BLOCKED_BY_POLICY"
        r["phase"] = prof.current_phase

    df = pd.DataFrame(records)
    summary = summarize_governance_live_trading_disabled(df)
    return df, summary


def summarize_governance_live_trading_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize live trading disabled report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "LIVE_TRADING_DISABLED_ENFORCED",
    }


def validate_no_live_trading_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate and intercept any live trading requests."""
    req_str = str(request).lower()
    violation = any(term in req_str for term in FORBIDDEN_LIVE_TRADING_TERMS)
    return {
        "request": str(request),
        "allowed": False,
        "blocked": True,
        "violation_detected": violation,
        "status": "BLOCKED_BY_POLICY",
        "message": "Live trading is strictly prohibited.",
    }
