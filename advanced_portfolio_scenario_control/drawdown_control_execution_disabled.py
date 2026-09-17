# -*- coding: utf-8 -*-
"""Phase 156: Drawdown_Control_Execution_Disabled Disabled Execution Report."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

def build_drawdown_control_execution_disabled_report(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    data = [{"operation": "LIVE_DRAWDOWN_CONTROL", "execution_attempted": False, "execution_blocked": True, "status": "DISABLED"}]
    df = pd.DataFrame(data)
    summary = {"operation": "LIVE_DRAWDOWN_CONTROL", "execution_executed": False, "disabled": True, "status": "DISABLED"}
    return df, summary
