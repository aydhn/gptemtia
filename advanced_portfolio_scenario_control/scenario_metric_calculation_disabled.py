# -*- coding: utf-8 -*-
"""Phase 156: Scenario_Metric_Calculation_Disabled Disabled Execution Report."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

def build_scenario_metric_calculation_disabled_report(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    data = [{"operation": "SCENARIO_METRIC_CALCULATION", "execution_attempted": False, "execution_blocked": True, "status": "DISABLED"}]
    df = pd.DataFrame(data)
    summary = {"operation": "SCENARIO_METRIC_CALCULATION", "execution_executed": False, "disabled": True, "status": "DISABLED"}
    return df, summary
