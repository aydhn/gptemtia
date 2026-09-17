# -*- coding: utf-8 -*-
"""Phase 155: Expected Shortfall (CVaR) Monitor Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskMetricPlaceholder


def build_expected_shortfall_monitor_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for expected shortfall monitor placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskMetricPlaceholder(
            metric_name="expected_shortfall_95_placeholder",
            metric_domain="expected_shortfall",
            formula_description="ES_95 = -E[r_p | r_p <= -VaR_95]",
            unit="ratio_to_nav",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
        RiskMetricPlaceholder(
            metric_name="expected_shortfall_99_placeholder",
            metric_domain="expected_shortfall",
            formula_description="ES_99 = -E[r_p | r_p <= -VaR_99]",
            unit="ratio_to_nav",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"placeholder_count": len(df), "is_calculated": False}
