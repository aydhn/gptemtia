# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Investment Advice Guards."""

from typing import Any, Dict, Tuple, Union
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingGuardItem


def build_risk_reporting_investment_advice_guard_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for investment advice guards."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskReportingGuardItem(
            guard_name="investment_advice_guard",
            domain="claim_guard",
            guard_rule="Prohibits directional trade recommendations, buy/sell calls, position adjustments, or advice",
            is_active=True,
            action_on_violation="BLOCK",
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"guard_count": len(df), "all_active": True}


def validate_risk_reporting_investment_advice_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that request contains no investment advice or trade recommendations."""
    prohibited = [
        "buy",
        "sell",
        "long",
        "short",
        "trade_recommendation",
        "investment_advice",
        "position_recommendation",
        "yavsiye",
        "al_sat",
    ]
    text = str(request).lower()
    blocked = any(p in text for p in prohibited)
    return {
        "is_blocked": blocked,
        "is_safe": not blocked,
        "action": "BLOCK" if blocked else "ALLOW",
        "reason": "Investment advice strictly prohibited" if blocked else "No violation",
    }
