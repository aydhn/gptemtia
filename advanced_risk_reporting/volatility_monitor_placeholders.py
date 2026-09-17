# -*- coding: utf-8 -*-
"""Phase 155: Volatility Monitor Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskMetricPlaceholder


def build_volatility_monitor_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for volatility monitor placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskMetricPlaceholder(
            metric_name="realized_volatility_placeholder",
            metric_domain="volatility",
            formula_description="sigma_ann = std(r_t) * sqrt(252)",
            unit="annualized_ratio",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
        RiskMetricPlaceholder(
            metric_name="rolling_volatility_placeholder",
            metric_domain="volatility",
            formula_description="rolling_sigma_21d = std(r_{t-20:t}) * sqrt(252)",
            unit="annualized_ratio",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"placeholder_count": len(df), "is_calculated": False}
