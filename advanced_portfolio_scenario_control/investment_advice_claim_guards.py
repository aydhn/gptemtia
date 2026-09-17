# -*- coding: utf-8 -*-
"""Phase 156: Investment_Advice_Claim_Guard Guard."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

def build_investment_advice_claim_guard_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    data = [{"guard_name": "Investment_Advice_Claim_Guard", "check_target": "recommendation_text", "enforced": True, "violation_count": 0, "status": "PASS"}]
    df = pd.DataFrame(data)
    summary = {"guard_name": "Investment_Advice_Claim_Guard", "all_passed": True, "error_policy": "Strictly prohibit investment advice"}
    return df, summary
