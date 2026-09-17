# -*- coding: utf-8 -*-
"""Phase 156: Backtest_Acceptance Dependency."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

def build_portfolio_scenario_backtest_acceptance_dependency_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    data = [{"dependency": "Backtest_Acceptance", "source_phase": 152, "source_module": "advanced_backtest_acceptance", "target_artifact": "acceptance_manifest", "status": "SATISFIED"}]
    df = pd.DataFrame(data)
    summary = {"status": "SATISFIED", "source_phase": 152, "dependency": "Backtest_Acceptance"}
    return df, summary
