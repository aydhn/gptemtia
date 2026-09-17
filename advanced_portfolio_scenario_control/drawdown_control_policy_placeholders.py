# -*- coding: utf-8 -*-
"""Phase 156: Drawdown Control Policy Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_POLICIES = [
    {
        "policy_id": "POL-DD-001",
        "policy_name": "stepped_de_risking_policy",
        "description": "Kademeli risk azaltma politikasi tanimi",
        "rule_type": "CONTRACT_POLICY",
        "execution_active": False,
    },
    {
        "policy_id": "POL-DD-002",
        "policy_name": "hard_freeze_policy",
        "description": "Asiri kayiplarda portfoy dondurma politikasi tanimi",
        "rule_type": "CONTRACT_POLICY",
        "execution_active": False,
    },
]


def build_drawdown_control_policy_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for control policies."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_POLICIES)
    summary = {
        "total_control_policies": len(df),
        "all_execution_disabled": bool((~df["execution_active"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
