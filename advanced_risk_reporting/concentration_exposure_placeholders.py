# -*- coding: utf-8 -*-
"""Phase 155: Concentration Exposure Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import ExposurePlaceholder


def build_concentration_exposure_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for concentration exposure placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        ExposurePlaceholder(
            placeholder_name="hhi_concentration_placeholder",
            exposure_type="herfindahl_hirschman_index",
            formula_description="Sum of squared portfolio weights: sum(w_i^2)",
            dimension="index",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
        ExposurePlaceholder(
            placeholder_name="top3_concentration_placeholder",
            exposure_type="top_k_ratio",
            formula_description="Sum of 3 largest absolute position weights: sum_{top 3}(|w_i|)",
            dimension="ratio",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"placeholder_count": len(df), "is_calculated": False}
