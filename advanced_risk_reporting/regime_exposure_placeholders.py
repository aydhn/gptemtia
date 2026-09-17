# -*- coding: utf-8 -*-
"""Phase 155: Regime Exposure Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import ExposurePlaceholder


def build_regime_exposure_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime exposure placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        ExposurePlaceholder(
            placeholder_name="high_volatility_regime_exposure_placeholder",
            exposure_type="regime_high_vol",
            formula_description="Portfolio exposure conditioned on high volatility market regime context",
            dimension="conditional_ratio",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
        ExposurePlaceholder(
            placeholder_name="trending_regime_exposure_placeholder",
            exposure_type="regime_trending",
            formula_description="Portfolio exposure conditioned on trending/directional market regime context",
            dimension="conditional_ratio",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"placeholder_count": len(df), "is_calculated": False}
