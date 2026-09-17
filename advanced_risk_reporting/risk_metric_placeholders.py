# -*- coding: utf-8 -*-
"""Phase 155: Risk Metric Placeholders Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskMetricPlaceholder


DEFAULT_RISK_METRICS = [
    {
        "metric_name": "portfolio_realized_volatility",
        "metric_domain": "risk_metrics",
        "formula_description": "Annualized standard deviation of daily portfolio returns: std(r_p) * sqrt(252)",
        "unit": "ratio",
        "is_placeholder": True,
        "is_calculated": False,
    },
    {
        "metric_name": "parametric_var_95",
        "metric_domain": "risk_metrics",
        "formula_description": "1-day 95% Parametric Value at Risk: 1.645 * sigma_p",
        "unit": "ratio_to_nav",
        "is_placeholder": True,
        "is_calculated": False,
    },
    {
        "metric_name": "expected_shortfall_95",
        "metric_domain": "risk_metrics",
        "formula_description": "1-day 95% Expected Shortfall (CVaR): conditional mean beyond VaR_95",
        "unit": "ratio_to_nav",
        "is_placeholder": True,
        "is_calculated": False,
    },
    {
        "metric_name": "current_drawdown",
        "metric_domain": "risk_metrics",
        "formula_description": "Percentage decline from historical peak NAV to current NAV",
        "unit": "ratio",
        "is_placeholder": True,
        "is_calculated": False,
    },
]


def build_risk_metric_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for risk metric placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for m in DEFAULT_RISK_METRICS:
        model = RiskMetricPlaceholder(**m)
        data = model.model_dump()
        data["current_phase"] = profile.current_phase
        data["target_final_phase"] = profile.target_final_phase
        data["next_phase"] = profile.next_phase
        rows.append(data)

    df = pd.DataFrame(rows)
    summary = {
        "metric_count": len(df),
        "all_placeholder": bool(df["is_placeholder"].all()) if not df.empty else True,
        "zero_calculated": bool((df["is_calculated"] == False).all()) if not df.empty else True,
    }
    return df, summary
