# -*- coding: utf-8 -*-
"""Phase 156: Drawdown Metric Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_DD_METRICS = [
    {"metric_id": "MET-DD-001", "metric_name": "maximum_drawdown_pct", "metric_category": "DRAWDOWN", "formula_spec": "(NAV_t - Peak_t) / Peak_t", "is_calculated": False, "status": "PLACEHOLDER_ONLY"},
    {"metric_id": "MET-DD-002", "metric_name": "underwater_duration_days", "metric_category": "DURATION", "formula_spec": "t - t_peak", "is_calculated": False, "status": "PLACEHOLDER_ONLY"},
]


def build_drawdown_metric_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for drawdown metric placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_DD_METRICS)
    summary = {
        "total_drawdown_metrics": len(df),
        "all_uncalculated": bool((~df["is_calculated"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
