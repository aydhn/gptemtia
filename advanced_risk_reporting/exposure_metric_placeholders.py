# -*- coding: utf-8 -*-
"""Phase 155: Exposure Metric Placeholders Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskMetricPlaceholder


DEFAULT_EXPOSURE_METRICS = [
    {
        "metric_name": "gross_exposure_ratio",
        "metric_domain": "exposure_metrics",
        "formula_description": "Total absolute position notional divided by portfolio net asset value",
        "unit": "ratio",
        "is_placeholder": True,
        "is_calculated": False,
    },
    {
        "metric_name": "net_exposure_ratio",
        "metric_domain": "exposure_metrics",
        "formula_description": "Net directional position notional (longs minus shorts) divided by NAV",
        "unit": "ratio",
        "is_placeholder": True,
        "is_calculated": False,
    },
    {
        "metric_name": "leverage_ratio",
        "metric_domain": "exposure_metrics",
        "formula_description": "Gross exposure divided by portfolio equity",
        "unit": "ratio",
        "is_placeholder": True,
        "is_calculated": False,
    },
]


def build_exposure_metric_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for exposure metric placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for m in DEFAULT_EXPOSURE_METRICS:
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
