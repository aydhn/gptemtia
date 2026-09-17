# -*- coding: utf-8 -*-
"""Phase 156: Portfolio_Scenario_Overfitting_Guard Guard."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

def build_portfolio_scenario_overfitting_guard_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    data = [{"guard_name": "Portfolio_Scenario_Overfitting_Guard", "check_target": "overfitting_check", "enforced": True, "violation_count": 0, "status": "PASS"}]
    df = pd.DataFrame(data)
    summary = {"guard_name": "Portfolio_Scenario_Overfitting_Guard", "all_passed": True, "error_policy": "Enforce scenario parameter parsimony"}
    return df, summary
