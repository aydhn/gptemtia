# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Resilience Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_RESILIENCE_CONTRACTS = [
    {
        "resilience_contract_id": "RES-CON-156-001",
        "resilience_dimension": "CAPITAL_PRESERVATION",
        "description": "Ekstrem senaryolarda sermaye erimesini sinirlama sozlesmesi",
        "target_metric": "MAX_CAPITAL_EROSION_PCT",
        "threshold_limit_pct": 20.0,
        "contract_status": "CONTRACT_ONLY",
        "evaluation_enabled": False,
    },
    {
        "resilience_contract_id": "RES-CON-156-002",
        "resilience_dimension": "LIQUIDITY_BUFFER",
        "description": "Piyasa tikanmalarinda nakit ve teminat tamponu sozlesmesi",
        "target_metric": "MIN_LIQUIDITY_BUFFER_PCT",
        "threshold_limit_pct": 25.0,
        "contract_status": "CONTRACT_ONLY",
        "evaluation_enabled": False,
    },
    {
        "resilience_contract_id": "RES-CON-156-003",
        "resilience_dimension": "MARGIN_HEADROOM",
        "description": "Margin call riskine karsi serbest teminat payi sozlesmesi",
        "target_metric": "MIN_MARGIN_HEADROOM_PCT",
        "threshold_limit_pct": 35.0,
        "contract_status": "CONTRACT_ONLY",
        "evaluation_enabled": False,
    },
    {
        "resilience_contract_id": "RES-CON-156-004",
        "resilience_dimension": "RECOVERY_TRAJECTORY",
        "description": "Sok sonrasi toparlanma suresi ve patikasi sozlesmesi",
        "target_metric": "MAX_RECOVERY_HORIZON_DAYS",
        "threshold_limit_pct": 60.0,
        "contract_status": "CONTRACT_ONLY",
        "evaluation_enabled": False,
    },
]


def build_portfolio_resilience_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for resilience contracts."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_RESILIENCE_CONTRACTS)
    summary = {
        "total_resilience_contracts": len(df),
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "all_evaluation_disabled": bool((~df["evaluation_enabled"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
