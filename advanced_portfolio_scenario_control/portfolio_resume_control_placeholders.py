# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Resume Control Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_RESUME_PLACEHOLDERS = [
    {
        "action_id": "ACT-RSM-001",
        "action_type": "RESUME_CONTROL",
        "target_scope": "RESTRICTED_RESUME_MODE",
        "activation_trigger": "MANUAL_OPERATOR_APPROVAL_AND_STABILIZATION",
        "execution_enabled": False,
        "status": "PLACEHOLDER_ONLY",
    },
]


def build_portfolio_resume_control_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for resume control placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_RESUME_PLACEHOLDERS)
    summary = {
        "total_resume_placeholders": len(df),
        "execution_disabled": bool((~df["execution_enabled"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
