# -*- coding: utf-8 -*-
"""Phase 155: Strategy Exposure Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import ExposurePlaceholder


def build_strategy_exposure_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for strategy exposure placeholder."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        ExposurePlaceholder(
            placeholder_name="trend_following_exposure_placeholder",
            exposure_type="strategy_trend",
            formula_description="Gross exposure allocated to trend-following rule sets",
            dimension="ratio_to_nav",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
        ExposurePlaceholder(
            placeholder_name="mean_reversion_exposure_placeholder",
            exposure_type="strategy_mean_reversion",
            formula_description="Gross exposure allocated to mean-reversion rule sets",
            dimension="ratio_to_nav",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"placeholder_count": len(df), "is_calculated": False}
