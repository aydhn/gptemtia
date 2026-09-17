# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Library Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_LIBRARIES = [
    {
        "library_id": "LIB-156-001",
        "library_name": "historical_macro_crisis_library",
        "category": "HISTORICAL",
        "scenario_count": 5,
        "historical_count": 5,
        "hypothetical_count": 0,
        "dry_run_fixture": "fixtures.historical_crises",
        "contract_status": "CONTRACT_ONLY",
    },
    {
        "library_id": "LIB-156-002",
        "library_name": "hypothetical_tail_risk_library",
        "category": "HYPOTHETICAL",
        "scenario_count": 5,
        "historical_count": 0,
        "hypothetical_count": 5,
        "dry_run_fixture": "fixtures.hypothetical_tails",
        "contract_status": "CONTRACT_ONLY",
    },
    {
        "library_id": "LIB-156-003",
        "library_name": "market_microstructure_shock_library",
        "category": "MICROSTRUCTURE",
        "scenario_count": 4,
        "historical_count": 0,
        "hypothetical_count": 4,
        "dry_run_fixture": "fixtures.microstructure_shocks",
        "contract_status": "CONTRACT_ONLY",
    },
]


def build_portfolio_scenario_library_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for scenario libraries."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_LIBRARIES)
    summary = {
        "total_libraries": len(df),
        "total_scenarios_in_libraries": int(df["scenario_count"].sum()) if not df.empty else 0,
        "all_contract_only": bool((df["contract_status"] == "CONTRACT_ONLY").all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
