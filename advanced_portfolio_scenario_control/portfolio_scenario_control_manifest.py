# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Control Master Manifest."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

def build_portfolio_scenario_control_manifest(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    manifest_data = {
        "manifest_id": "MNF-156-001",
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "next_phase": profile.next_phase,
        "scenario_contracts_count": 10,
        "drawdown_contracts_count": 4,
        "control_placeholders_count": 7,
        "scenario_executed": False,
        "drawdown_control_executed": False,
        "portfolio_adjustment_generated": False,
        "broker_order_sent": False,
        "live_order_sent": False,
        "investment_advice_generated": False,
        "phase_157_handoff_ready": True,
        "status": "READY",
    }
    df = pd.DataFrame([manifest_data])
    return df, manifest_data
