# -*- coding: utf-8 -*-
"""Phase 155: Live Trading Disabled Report."""

from typing import Any, Dict, Tuple, Union
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingDisabledExecutionItem


def build_risk_reporting_live_trading_disabled_report(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary confirming live trading is disabled."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskReportingDisabledExecutionItem(
            component_name="live_trading_engine",
            prohibited_actions=["live_trade", "place_market_order", "execute_real_trade"],
            enforcement_mechanism="STRICT_SAFETY_GATE_LIVE_TRADING_BLOCKED",
            is_disabled=True,
            status="execution_contract_only",
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"is_disabled": True, "status": "execution_blocked_no_live_trading"}


def validate_no_risk_reporting_live_trading_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that request does not attempt live trading."""
    prohibited = ["live_trade", "place_order", "market_order", "execute_trade", "real_money"]
    text = str(request).lower()
    blocked = any(p in text for p in prohibited)
    return {
        "is_blocked": blocked,
        "is_safe": not blocked,
        "action": "BLOCK" if blocked else "ALLOW",
        "reason": "Live trading strictly prohibited" if blocked else "No violation",
    }
