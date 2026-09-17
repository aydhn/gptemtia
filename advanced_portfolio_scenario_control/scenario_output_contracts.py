# -*- coding: utf-8 -*-
"""Phase 156: Scenario Output Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_SCENARIO_OUTPUTS = [
    {
        "output_contract_id": "OUT-SCN-001",
        "output_name": "scenario_stress_loss_summary",
        "schema_fields": ["scenario_id", "scenario_name", "simulated_loss_pct", "var_99_shock", "recovery_days"],
        "frequency": "ON_DEMAND_RESEARCH",
        "storage_format": "csv_json",
        "materialization_allowed": False,
    },
]


def build_scenario_output_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for scenario outputs."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_SCENARIO_OUTPUTS)
    summary = {
        "total_scenario_output_contracts": len(df),
        "materialization_disabled": bool((~df["materialization_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
