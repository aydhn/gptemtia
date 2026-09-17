# -*- coding: utf-8 -*-
"""Phase 155: Turnover Monitor Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskMetricPlaceholder


def build_turnover_monitor_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for turnover monitor placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskMetricPlaceholder(
            metric_name="portfolio_turnover_placeholder",
            metric_domain="turnover",
            formula_description="Turnover_t = 0.5 * sum(|w_{i,t} - w_{i,t-1}|)",
            unit="ratio_per_rebalance",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"placeholder_count": len(df), "is_calculated": False}
