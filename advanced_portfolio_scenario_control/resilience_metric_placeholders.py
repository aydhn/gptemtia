# -*- coding: utf-8 -*-
"""Phase 156: Resilience Metric Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_RES_METRICS = [
    {"metric_id": "MET-RES-001", "metric_name": "stress_capital_cushion_pct", "metric_category": "CAPITAL", "formula_spec": "Unencumbered_Cash / Shocked_Margin", "is_calculated": False, "status": "PLACEHOLDER_ONLY"},
    {"metric_id": "MET-RES-002", "metric_name": "recovery_absorption_ratio", "metric_category": "ABSORPTION", "formula_spec": "Expected_Recovery_Inflow / Liquidity_Gap", "is_calculated": False, "status": "PLACEHOLDER_ONLY"},
]


def build_resilience_metric_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for resilience metric placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_RES_METRICS)
    summary = {
        "total_resilience_metrics": len(df),
        "all_uncalculated": bool((~df["is_calculated"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
