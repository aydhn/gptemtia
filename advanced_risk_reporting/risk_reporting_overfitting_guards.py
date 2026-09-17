# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Overfitting Guards."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingGuardItem


def build_risk_reporting_overfitting_guard_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for overfitting guards."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskReportingGuardItem(
            guard_name="risk_reporting_overfitting_guard",
            domain="overfitting_guard",
            guard_rule="Prohibits retrospective threshold tuning to artificially eliminate historical drawdowns",
            is_active=True,
            action_on_violation="BLOCK",
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"guard_count": len(df), "all_active": True}
