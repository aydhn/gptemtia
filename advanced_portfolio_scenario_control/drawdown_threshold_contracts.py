# -*- coding: utf-8 -*-
"""Phase 156: Drawdown Threshold Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_DRAWDOWN_THRESHOLDS = [
    {
        "threshold_id": "THR-DD-001",
        "tier_name": "NORMAL",
        "drawdown_lower_pct": 0.0,
        "drawdown_upper_pct": 4.99,
        "mandatory_action": "NO_ACTION_FULL_ALLOCATION",
        "contract_status": "CONTRACT_ONLY",
    },
    {
        "threshold_id": "THR-DD-002",
        "tier_name": "WARNING",
        "drawdown_lower_pct": 5.0,
        "drawdown_upper_pct": 9.99,
        "mandatory_action": "FLAG_ELEVATED_RISK_MONITOR",
        "contract_status": "CONTRACT_ONLY",
    },
    {
        "threshold_id": "THR-DD-003",
        "tier_name": "BREACH",
        "drawdown_lower_pct": 10.0,
        "drawdown_upper_pct": 14.99,
        "mandatory_action": "REDUCE_GROSS_EXPOSURE_25PCT",
        "contract_status": "CONTRACT_ONLY",
    },
    {
        "threshold_id": "THR-DD-004",
        "tier_name": "CRITICAL",
        "drawdown_lower_pct": 15.0,
        "drawdown_upper_pct": 100.0,
        "mandatory_action": "FREEZE_NEW_POSITIONS_DERISK_50PCT",
        "contract_status": "CONTRACT_ONLY",
    },
]


def build_drawdown_threshold_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for drawdown thresholds."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_DRAWDOWN_THRESHOLDS)
    summary = {
        "total_threshold_tiers": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
