# -*- coding: utf-8 -*-
"""Phase 156: Scenario Metric Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_SCENARIO_METRICS = [
    {"metric_id": "MET-SCN-001", "metric_name": "scenario_pnl_impact_pct", "metric_category": "LOSS", "formula_spec": "NAV_shock / NAV_initial - 1.0", "is_calculated": False, "status": "PLACEHOLDER_ONLY"},
    {"metric_id": "MET-SCN-002", "metric_name": "worst_case_tail_loss_pct", "metric_category": "EXTREME_LOSS", "formula_spec": "min(all_scenario_pnls)", "is_calculated": False, "status": "PLACEHOLDER_ONLY"},
]


def build_scenario_metric_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for scenario metric placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_SCENARIO_METRICS)
    summary = {
        "total_scenario_metrics": len(df),
        "all_uncalculated": bool((~df["is_calculated"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
