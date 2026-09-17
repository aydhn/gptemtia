# -*- coding: utf-8 -*-
"""Phase 156: De-Risking Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_DERISKING = [
    {
        "action_id": "ACT-DRK-001",
        "action_type": "DE_RISKING",
        "target_scope": "HIGH_BETA_ASSETS",
        "reduction_target_pct": 40.0,
        "activation_trigger": "VOLATILITY_SPIKE_AND_DD",
        "execution_enabled": False,
        "status": "PLACEHOLDER_ONLY",
    },
]


def build_de_risking_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for de-risking placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_DERISKING)
    summary = {
        "total_derisking_placeholders": len(df),
        "execution_disabled": bool((~df["execution_enabled"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
