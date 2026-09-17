# -*- coding: utf-8 -*-
"""Phase 156: Control Action Metric Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_ACT_METRICS = [
    {"metric_id": "MET-ACT-001", "metric_name": "derisk_action_count", "metric_category": "ACTION_AUDIT", "formula_spec": "sum(active_derisk_triggers)", "is_calculated": False, "status": "PLACEHOLDER_ONLY"},
    {"metric_id": "MET-ACT-002", "metric_name": "hedge_action_trigger_count", "metric_category": "ACTION_AUDIT", "formula_spec": "sum(active_hedge_triggers)", "is_calculated": False, "status": "PLACEHOLDER_ONLY"},
]


def build_control_action_metric_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for control action metric placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_ACT_METRICS)
    summary = {
        "total_action_metrics": len(df),
        "all_uncalculated": bool((~df["is_calculated"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
