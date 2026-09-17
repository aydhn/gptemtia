# -*- coding: utf-8 -*-
"""Phase 155: Marginal Risk Contribution Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskMetricPlaceholder


def build_marginal_risk_contribution_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for marginal risk contribution placeholder."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        RiskMetricPlaceholder(
            metric_name="marginal_risk_contribution_placeholder",
            metric_domain="marginal_risk",
            formula_description="MRC_i = d(sigma_p) / d(w_i) = (Sigma * w)_i / sigma_p",
            unit="marginal_volatility",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"placeholder_count": len(df), "is_calculated": False}
