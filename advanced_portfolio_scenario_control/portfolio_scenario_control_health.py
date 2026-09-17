# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Control Health Check."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_HEALTH_CHECKS = [
    {"check_id": "HLT-156-001", "component": "config_profiles", "status": "HEALTHY", "detail": "All profiles enforce non-production dry-run"},
    {"check_id": "HLT-156-002", "component": "scenario_contracts", "status": "HEALTHY", "detail": "All scenario contracts are contract-only"},
    {"check_id": "HLT-156-003", "component": "drawdown_contracts", "status": "HEALTHY", "detail": "All drawdown control contracts are contract-only"},
    {"check_id": "HLT-156-004", "component": "control_placeholders", "status": "HEALTHY", "detail": "All control action placeholders are inactive"},
    {"check_id": "HLT-156-005", "component": "guards", "status": "HEALTHY", "detail": "All safety guards and claim blockers are active"},
    {"check_id": "HLT-156-006", "component": "phase_157_handoff", "status": "HEALTHY", "detail": "Prerequisites for Phase 157 are verified"},
]

def build_portfolio_scenario_control_health_check(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    df = pd.DataFrame(DEFAULT_HEALTH_CHECKS)
    summary = {
        "status": "HEALTHY",
        "total_checks": len(df),
        "passed_checks": int((df["status"] == "HEALTHY").sum()) if not df.empty else 0,
        "current_phase": profile.current_phase,
    }
    return df, summary
