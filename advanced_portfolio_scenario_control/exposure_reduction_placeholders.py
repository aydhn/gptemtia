# -*- coding: utf-8 -*-
"""Phase 156: Exposure Reduction Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_EXP_REDUCTION = [
    {
        "action_id": "ACT-RED-001",
        "action_type": "EXPOSURE_REDUCTION",
        "target_scope": "GROSS_PORTFOLIO_EXPOSURE",
        "reduction_target_pct": 25.0,
        "activation_trigger": "DRAWDOWN_BREACH_10PCT",
        "execution_enabled": False,
        "status": "PLACEHOLDER_ONLY",
    },
]


def build_exposure_reduction_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for exposure reduction placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_EXP_REDUCTION)
    summary = {
        "total_reduction_placeholders": len(df),
        "execution_disabled": bool((~df["execution_enabled"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
