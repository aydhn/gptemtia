# -*- coding: utf-8 -*-
"""Phase 155: Asset Exposure Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import ExposurePlaceholder


def build_asset_exposure_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for asset-level exposure placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        ExposurePlaceholder(
            placeholder_name="single_asset_gross_exposure_placeholder",
            exposure_type="asset_gross",
            formula_description="Single asset absolute position weight: |w_i|",
            dimension="ratio_to_nav",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
        ExposurePlaceholder(
            placeholder_name="single_asset_net_exposure_placeholder",
            exposure_type="asset_net",
            formula_description="Single asset signed position weight: w_i",
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
