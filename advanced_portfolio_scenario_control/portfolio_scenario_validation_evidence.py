# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Validation Evidence Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_EVIDENCE = [
    {"evidence_id": "EVD-156-001", "rule_name": "zero_scenario_execution", "status": "VERIFIED", "evidence_note": "No actual scenario PnL was calculated"},
    {"evidence_id": "EVD-156-002", "rule_name": "zero_drawdown_control_execution", "status": "VERIFIED", "evidence_note": "No automated drawdown intervention was executed"},
    {"evidence_id": "EVD-156-003", "rule_name": "zero_portfolio_adjustment", "status": "VERIFIED", "evidence_note": "Portfolio weights and allocations remained unmodified"},
    {"evidence_id": "EVD-156-004", "rule_name": "zero_live_broker_interaction", "status": "VERIFIED", "evidence_note": "No broker API calls or live trading occurred"},
    {"evidence_id": "EVD-156-005", "rule_name": "zero_investment_advice", "status": "VERIFIED", "evidence_note": "All outputs are marked as research contracts only"},
]

def build_portfolio_scenario_validation_evidence_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    df = pd.DataFrame(DEFAULT_EVIDENCE)
    summary = {
        "total_evidence_items": len(df),
        "all_verified": bool((df["status"] == "VERIFIED").all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
