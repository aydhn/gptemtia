# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Limit Breach Claim Guards."""

from typing import Any, Dict, Tuple, Union
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingGuardItem


def build_risk_reporting_limit_breach_claim_guard_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for limit breach claim guards."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskReportingGuardItem(
            guard_name="limit_breach_claim_guard",
            domain="claim_guard",
            guard_rule="Prohibits asserting live limit breach, alarm triggering, or live risk monitoring state",
            is_active=True,
            action_on_violation="BLOCK",
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"guard_count": len(df), "all_active": True}


def validate_limit_breach_claim_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that request does not assert live limit breach or alarm triggering."""
    prohibited = [
        "limit_breach",
        "breach_alert",
        "live_alarm",
        "trigger_breach",
        "breached_limit",
        "real_alarm",
    ]
    text = str(request).lower()
    blocked = any(p in text for p in prohibited)
    return {
        "is_blocked": blocked,
        "is_safe": not blocked,
        "action": "BLOCK" if blocked else "ALLOW",
        "reason": "Live limit breach claims prohibited in contract phase" if blocked else "No violation",
    }
