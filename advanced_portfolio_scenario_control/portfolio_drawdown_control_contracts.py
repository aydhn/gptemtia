# -*- coding: utf-8 -*-
"""Phase 156: Master Portfolio Drawdown Control Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_DRAWDOWN_CONTROL_CONTRACTS = [
    {
        "contract_id": "DD-CON-156-001",
        "control_name": "Peak to Trough Drawdown Control Contract",
        "drawdown_metric_target": "PEAK_TO_TROUGH_DD_PCT",
        "warning_threshold_pct": 5.0,
        "breach_threshold_pct": 10.0,
        "critical_threshold_pct": 15.0,
        "control_policy": "STEPPED_EXPOSURE_REDUCTION",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "contract_id": "DD-CON-156-002",
        "control_name": "Rolling Window Drawdown Control Contract",
        "drawdown_metric_target": "ROLLING_30D_DD_PCT",
        "warning_threshold_pct": 4.0,
        "breach_threshold_pct": 8.0,
        "critical_threshold_pct": 12.0,
        "control_policy": "DYNAMIC_DE_RISKING",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "contract_id": "DD-CON-156-003",
        "control_name": "Underwater Duration Control Contract",
        "drawdown_metric_target": "UNDERWATER_DURATION_DAYS",
        "warning_threshold_pct": 30.0,
        "breach_threshold_pct": 60.0,
        "critical_threshold_pct": 90.0,
        "control_policy": "PORTFOLIO_REVIEW_FREEZE",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
    {
        "contract_id": "DD-CON-156-004",
        "control_name": "Capital Preservation Soft Floor Contract",
        "drawdown_metric_target": "NAV_FLOOR_DISTANCE_PCT",
        "warning_threshold_pct": 6.0,
        "breach_threshold_pct": 12.0,
        "critical_threshold_pct": 18.0,
        "control_policy": "SYSTEMATIC_DERISKING_FLOOR",
        "contract_status": "CONTRACT_ONLY",
        "execution_allowed": False,
    },
]


def build_portfolio_drawdown_control_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for drawdown control contracts."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_DRAWDOWN_CONTROL_CONTRACTS)
    summary = {
        "total_drawdown_control_contracts": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "all_execution_disabled": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
        "status": "DRAWDOWN_CONTROL_CONTRACT_READY",
    }
    return df, summary
