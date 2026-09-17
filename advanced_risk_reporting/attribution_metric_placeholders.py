# -*- coding: utf-8 -*-
"""Phase 155: Attribution Metric Placeholders Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskMetricPlaceholder


DEFAULT_ATTRIBUTION_METRICS = [
    {
        "metric_name": "marginal_risk_contribution",
        "metric_domain": "attribution_metrics",
        "formula_description": "First derivative of portfolio volatility with respect to asset weight",
        "unit": "volatility_derivative",
        "is_placeholder": True,
        "is_calculated": False,
    },
    {
        "metric_name": "percentage_risk_contribution",
        "metric_domain": "attribution_metrics",
        "formula_description": "Fraction of total portfolio risk attributed to a specific asset or factor",
        "unit": "ratio",
        "is_placeholder": True,
        "is_calculated": False,
    },
    {
        "metric_name": "herfindahl_concentration_index",
        "metric_domain": "attribution_metrics",
        "formula_description": "Concentration measure based on sum of squared weights: sum(w_i^2)",
        "unit": "index",
        "is_placeholder": True,
        "is_calculated": False,
    },
]


def build_attribution_metric_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for attribution metric placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for m in DEFAULT_ATTRIBUTION_METRICS:
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
