# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Manual Review Queue."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_MANUAL_REVIEWS = [
    {
        "review_id": "REV-156-001",
        "topic": "tail_scenario_parameter_audit",
        "review_requirement": "Hipotetik sok carpanlarinin asiri iyimser veya kotumser olmamasi denetimi",
        "assigned_role": "RISK_ANALYST",
        "review_status": "PENDING_OPERATOR_REVIEW",
        "blocking": False,
    },
]

def build_portfolio_scenario_manual_review_queue(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    df = pd.DataFrame(DEFAULT_MANUAL_REVIEWS)
    summary = {
        "total_review_items": len(df),
        "blocking_count": int(df["blocking"].sum()) if not df.empty else 0,
        "current_phase": profile.current_phase,
    }
    return df, summary
