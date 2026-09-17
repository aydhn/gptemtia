# -*- coding: utf-8 -*-
"""Phase 155: Slippage Monitor Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskMetricPlaceholder


def build_slippage_monitor_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for slippage monitor placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskMetricPlaceholder(
            metric_name="estimated_slippage_drag_placeholder",
            metric_domain="slippage",
            formula_description="SlippageDrag = sum(|Delta w_i| * SlippageModel(ADV_i, Vol_i))",
            unit="bps",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"placeholder_count": len(df), "is_calculated": False}
