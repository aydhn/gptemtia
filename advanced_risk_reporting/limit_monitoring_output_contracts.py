# -*- coding: utf-8 -*-
"""Phase 155: Limit Monitoring Output Contracts Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile


def build_limit_monitoring_output_contract_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for limit monitoring output contracts."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        {
            "output_name": "limit_monitoring_output_contract",
            "contract_validation_status": "limit_monitoring_contract_ready",
            "blocked_reason": "execution_contract_only",
            "manual_review_required": True,
            "actual_breach_detected": False,
            "live_alert_dispatched": False,
        }
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"output_contract_count": len(df), "status": "limit_monitoring_contract_ready"}
