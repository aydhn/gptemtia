"""Phase 122 Cross-Asset Context Factor Families Registry.

Defines aligned cross-domain observation factors across FX, Commodities,
Macroeconomic indicators, Calendar events, and News metadata.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import (
    FACTOR_PLACEHOLDER_ONLY,
    FACTOR_READY,
)

CROSS_ASSET_CONTEXT_FACTOR_METADATA: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_fx_commodity_context",
        "factor_family": "cross_asset_context",
        "input_features": ["cross__usd_try_gold_corr_30"],
        "calculation_type": "rolling_cross_asset_correlation",
        "non_signal_usage": "Co-movement observation between currency pairs and precious metals.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_fx_macro_context",
        "factor_family": "cross_asset_context",
        "input_features": ["cross__eur_usd_rate_diff_30"],
        "calculation_type": "interest_rate_differential_context",
        "non_signal_usage": "Macro interest rate spread context aligned with FX exchange rates.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_commodity_macro_context",
        "factor_family": "cross_asset_context",
        "input_features": ["cross__oil_cpi_beta_60"],
        "calculation_type": "energy_inflation_pass_through_context",
        "non_signal_usage": "Energy price correlation with macro consumer inflation.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_macro_calendar_context",
        "factor_family": "cross_asset_context",
        "input_features": ["fusion__macro_calendar_alignment"],
        "calculation_type": "economic_surprise_event_intensity",
        "non_signal_usage": "Joint macro data and scheduled calendar event context.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_calendar_news_context",
        "factor_family": "cross_asset_context",
        "input_features": ["fusion__calendar_news_overlap"],
        "calculation_type": "event_announcement_media_intensity",
        "non_signal_usage": "News headline volume surrounding scheduled release timestamps.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_cross_domain_context_placeholder",
        "factor_family": "cross_asset_context",
        "input_features": ["fusion__cross_domain_vector"],
        "calculation_type": "multi_asset_dispersion_vector",
        "non_signal_usage": "High-dimensional cross-domain observation vector placeholder.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
]


def build_cross_asset_context_factor_family_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Cross-Asset Context Factor Family Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in CROSS_ASSET_CONTEXT_FACTOR_METADATA]
    df = pd.DataFrame(records)

    summary = {
        "active_profile": active_profile.name,
        "total_factors": len(records),
        "ready_factors": sum(1 for r in records if r["status_label"] == FACTOR_READY),
        "placeholder_factors": sum(1 for r in records if r["status_label"] == FACTOR_PLACEHOLDER_ONLY),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_READY,
    }
    return df, summary


def summarize_cross_asset_context_factor_family(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize cross-asset context factor family DataFrame."""
    return {
        "total_factors": len(df),
        "status": FACTOR_READY,
        "non_signal": True,
    }
