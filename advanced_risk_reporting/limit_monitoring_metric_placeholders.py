# -*- coding: utf-8 -*-
"""Phase 155: Limit Monitoring Metric Placeholders Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskMetricPlaceholder


DEFAULT_LIMIT_METRICS = [
    {
        "metric_name": "limit_utilization_ratio",
        "metric_domain": "limit_metrics",
        "formula_description": "Current metric value divided by hard limit threshold: Value / Limit",
        "unit": "ratio",
        "is_placeholder": True,
        "is_calculated": False,
    },
    {
        "metric_name": "breach_count_placeholder",
        "metric_domain": "limit_metrics",
        "formula_description": "Number of hard limits exceeded at evaluation timestamp",
        "unit": "count",
        "is_placeholder": True,
        "is_calculated": False,
    },
    {
        "metric_name": "warning_count_placeholder",
        "metric_domain": "limit_metrics",
        "formula_description": "Number of soft limits approaching threshold at evaluation timestamp",
        "unit": "count",
        "is_placeholder": True,
        "is_calculated": False,
    },
]


def build_limit_monitoring_metric_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for limit monitoring metric placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for m in DEFAULT_LIMIT_METRICS:
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
