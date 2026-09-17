# -*- coding: utf-8 -*-
"""Phase 155: Currency Exposure Placeholder Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import ExposurePlaceholder


def build_currency_exposure_placeholder_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for currency exposure placeholders."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        ExposurePlaceholder(
            placeholder_name="usd_exposure_placeholder",
            exposure_type="currency_usd",
            formula_description="Sum of weights denominated or referenced in USD",
            dimension="currency_subgroup",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
        ExposurePlaceholder(
            placeholder_name="try_exposure_placeholder",
            exposure_type="currency_try",
            formula_description="Sum of weights denominated or referenced in TRY",
            dimension="currency_subgroup",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
        ExposurePlaceholder(
            placeholder_name="eur_exposure_placeholder",
            exposure_type="currency_eur",
            formula_description="Sum of weights denominated or referenced in EUR",
            dimension="currency_subgroup",
            is_placeholder=True,
            is_calculated=False,
        ).model_dump(),
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"placeholder_count": len(df), "is_calculated": False}
