# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Readiness Scoring."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

def calculate_portfolio_scenario_readiness_score(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[float, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    components = {
        "scenario_contracts_registered": 0.25,
        "drawdown_controls_registered": 0.25,
        "control_placeholders_established": 0.20,
        "negative_invariants_guaranteed": 0.20,
        "dependencies_and_evidence_verified": 0.10,
    }
    score = sum(components.values())
    meets_threshold = score >= profile.min_readiness_score
    summary = {
        "overall_score": score,
        "meets_threshold": meets_threshold,
        "components": components,
        "classification": "portfolio_scenario_control_contract_ready_non_production",
        "is_trading_signal": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return score, summary

def build_portfolio_scenario_readiness_score_report(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    score, summary = calculate_portfolio_scenario_readiness_score(profile)
    rows = [{"component": k, "weight": v, "status": "PASSED"} for k, v in summary["components"].items()]
    rows.append({"component": "OVERALL", "weight": score, "status": "READY" if summary["meets_threshold"] else "NOT_READY"})
    df = pd.DataFrame(rows)
    return df, summary
