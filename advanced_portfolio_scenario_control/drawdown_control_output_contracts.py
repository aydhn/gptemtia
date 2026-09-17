# -*- coding: utf-8 -*-
"""Phase 156: Drawdown Control Output Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_DRAWDOWN_OUTPUTS = [
    {
        "output_contract_id": "OUT-DD-001",
        "output_name": "drawdown_control_audit_summary",
        "schema_fields": ["control_id", "current_drawdown_tier", "active_actions", "floor_distance", "underwater_days"],
        "frequency": "DAILY_AUDIT_STUB",
        "storage_format": "csv_json",
        "materialization_allowed": False,
    },
]


def build_drawdown_control_output_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for drawdown control outputs."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_DRAWDOWN_OUTPUTS)
    summary = {
        "total_drawdown_output_contracts": len(df),
        "materialization_disabled": bool((~df["materialization_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
