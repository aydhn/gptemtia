# -*- coding: utf-8 -*-
"""Phase 156: Recovery Metric Placeholders."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_REC_METRICS = [
    {"metric_id": "MET-REC-001", "metric_name": "rebound_velocity_days", "metric_category": "RECOVERY", "formula_spec": "Days to recover 50% of drawdown", "is_calculated": False, "status": "PLACEHOLDER_ONLY"},
]


def build_recovery_metric_placeholder_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for recovery metric placeholders."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    df = pd.DataFrame(DEFAULT_REC_METRICS)
    summary = {
        "total_recovery_metrics": len(df),
        "all_uncalculated": bool((~df["is_calculated"]).all()) if not df.empty else True,
        "current_phase": profile.current_phase,
    }
    return df, summary
