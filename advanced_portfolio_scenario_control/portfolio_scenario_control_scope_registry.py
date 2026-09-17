# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Control Scope Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_SCOPES = [
    {"scope_id": "SCP-156-001", "domain_name": "portfolio_scenario_testing", "scope_name": "historical_crisis_scenarios", "status": "ACTIVE"},
    {"scope_id": "SCP-156-002", "domain_name": "portfolio_scenario_testing", "scope_name": "hypothetical_tail_shocks", "status": "ACTIVE"},
    {"scope_id": "SCP-156-003", "domain_name": "portfolio_scenario_testing", "scope_name": "regime_shift_shocks", "status": "ACTIVE"},
    {"scope_id": "SCP-156-004", "domain_name": "portfolio_scenario_testing", "scope_name": "volatility_spike_shocks", "status": "ACTIVE"},
    {"scope_id": "SCP-156-005", "domain_name": "portfolio_scenario_testing", "scope_name": "liquidity_crunch_shocks", "status": "ACTIVE"},
    {"scope_id": "SCP-156-006", "domain_name": "portfolio_scenario_testing", "scope_name": "correlation_breakdown_shocks", "status": "ACTIVE"},
    {"scope_id": "SCP-156-007", "domain_name": "portfolio_scenario_testing", "scope_name": "currency_shocks", "status": "ACTIVE"},
    {"scope_id": "SCP-156-008", "domain_name": "portfolio_scenario_testing", "scope_name": "spread_widening_shocks", "status": "ACTIVE"},
    {"scope_id": "SCP-156-009", "domain_name": "portfolio_scenario_testing", "scope_name": "transaction_cost_shocks", "status": "ACTIVE"},
    {"scope_id": "SCP-156-010", "domain_name": "portfolio_scenario_testing", "scope_name": "slippage_shocks", "status": "ACTIVE"},
    {"scope_id": "SCP-156-011", "domain_name": "portfolio_drawdown_control", "scope_name": "peak_to_trough_drawdown", "status": "ACTIVE"},
    {"scope_id": "SCP-156-012", "domain_name": "portfolio_drawdown_control", "scope_name": "rolling_window_drawdown", "status": "ACTIVE"},
    {"scope_id": "SCP-156-013", "domain_name": "portfolio_drawdown_control", "scope_name": "underwater_duration_control", "status": "ACTIVE"},
    {"scope_id": "SCP-156-014", "domain_name": "portfolio_drawdown_control", "scope_name": "warning_threshold_monitoring", "status": "ACTIVE"},
    {"scope_id": "SCP-156-015", "domain_name": "portfolio_drawdown_control", "scope_name": "breach_tier_monitoring", "status": "ACTIVE"},
    {"scope_id": "SCP-156-016", "domain_name": "portfolio_drawdown_control", "scope_name": "recovery_plan_orchestration", "status": "ACTIVE"},
    {"scope_id": "SCP-156-017", "domain_name": "portfolio_control_action", "scope_name": "exposure_reduction_policy", "status": "ACTIVE"},
    {"scope_id": "SCP-156-018", "domain_name": "portfolio_control_action", "scope_name": "de_risking_policy", "status": "ACTIVE"},
    {"scope_id": "SCP-156-019", "domain_name": "portfolio_control_action", "scope_name": "hedge_control_policy", "status": "ACTIVE"},
    {"scope_id": "SCP-156-020", "domain_name": "portfolio_control_action", "scope_name": "rebalance_control_policy", "status": "ACTIVE"},
    {"scope_id": "SCP-156-021", "domain_name": "portfolio_control_action", "scope_name": "portfolio_freeze_resume_policy", "status": "ACTIVE"},
]


def build_portfolio_scenario_control_scope_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Phase 156 scopes."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_SCOPES)
    summary = {
        "total_scopes": len(df),
        "active_scopes": int((df["status"] == "ACTIVE").sum()) if not df.empty else 0,
        "current_phase": profile.current_phase,
    }
    return df, summary
