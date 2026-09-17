# -*- coding: utf-8 -*-
"""Phase 155: Liquidity Exposure Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import ExposurePlaceholder


def build_liquidity_exposure_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for liquidity exposure placeholder."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        ExposurePlaceholder(
            placeholder_name="days_to_liquidate_placeholder",
            exposure_type="liquidity",
            formula_description="Estimated days to exit position under max participation rate: |w_i|*NAV / (ADV_i * 0.10)",
            dimension="days",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump()
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"placeholder_count": len(df), "is_calculated": False}
