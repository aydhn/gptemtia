# -*- coding: utf-8 -*-
"""Phase 156: Resilience Output Contracts."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_RESILIENCE_OUTPUTS = [
    {
        "output_contract_id": "OUT-RES-001",
        "output_name": "portfolio_resilience_matrix",
        "schema_fields": ["dimension", "headroom_ratio", "threshold_limit", "resilience_status"],
        "frequency": "MONTHLY_RESEARCH_STUB",
        "storage_format": "csv_json",
        "materialization_allowed": False,
    },
]


def build_resilience_output_contract_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for resilience outputs."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_RESILIENCE_OUTPUTS)
    summary = {
        "total_resilience_output_contracts": len(df),
        "materialization_disabled": bool((~df["materialization_allowed"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
