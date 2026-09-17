# -*- coding: utf-8 -*-
"""Phase 156: Regime Dependency."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

def build_portfolio_scenario_regime_dependency_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    data = [{"dependency": "Regime", "source_phase": 135, "source_module": "advanced_regime_acceptance", "target_artifact": "regime_acceptance_manifest", "status": "SATISFIED"}]
    df = pd.DataFrame(data)
    summary = {"status": "SATISFIED", "source_phase": 135, "dependency": "Regime"}
    return df, summary
