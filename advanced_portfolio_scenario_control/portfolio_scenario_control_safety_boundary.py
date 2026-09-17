# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Control Safety Boundary."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

NO_GO_RULES = [
    "No live trading or real broker execution",
    "No real-time portfolio rebalance order execution",
    "No automated de-risking or hedging order creation",
    "No actual scenario loss/PnL calculation treated as verified",
    "No live drawdown calculation trigger",
    "No alert/dashboard pushing to production channels",
    "No investment advice or trade recommendations",
]

SAFE_GO_RULES = [
    "Offline/local scenario contract registration",
    "Offline drawdown control contract definition",
    "Non-executable control action placeholder registration",
    "Output schemas and metric placeholders",
    "Phase 157 handoff readiness reporting",
]

def build_portfolio_scenario_control_safety_boundary(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    rows = [{"boundary_type": "NO_GO", "rule": r, "enforced": True} for r in NO_GO_RULES]
    rows.extend([{"boundary_type": "SAFE_GO", "rule": r, "enforced": True} for r in SAFE_GO_RULES])
    df = pd.DataFrame(rows)
    summary = {
        "status": "SAFETY_BOUNDARY_ENFORCED",
        "no_go_count": len(NO_GO_RULES),
        "safe_go_count": len(SAFE_GO_RULES),
        "current_phase": profile.current_phase,
    }
    return df, summary
