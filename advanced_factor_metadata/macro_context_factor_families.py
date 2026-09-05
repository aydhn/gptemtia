"""Phase 122 Macro Context Factor Families Registry.

Defines point-in-time inflation, policy rates, economic growth, and revision context factors.
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

MACRO_CONTEXT_FACTOR_METADATA: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_macro_inflation_context",
        "factor_family": "macro_context",
        "input_features": ["fusion__macro_cpi_rate", "fusion__macro_ppi_rate"],
        "calculation_type": "point_in_time_inflation_level",
        "non_signal_usage": "Inflation environment context. Backward-asof lagged only.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_macro_rate_context",
        "factor_family": "macro_context",
        "input_features": ["fusion__macro_policy_rate", "fusion__macro_10y_yield"],
        "calculation_type": "interest_rate_level_and_slope",
        "non_signal_usage": "Monetary policy rate backdrop observation.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_macro_growth_context",
        "factor_family": "macro_context",
        "input_features": ["fusion__macro_gdp_growth", "fusion__macro_pmi"],
        "calculation_type": "macro_growth_composite",
        "non_signal_usage": "Economic expansion and business cycle observation.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_macro_revision_context",
        "factor_family": "macro_context",
        "input_features": ["fusion__macro_revision_flag"],
        "calculation_type": "vintage_revision_indicator",
        "non_signal_usage": "Data quality flag indicating post-release revision occurred.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_macro_surprise_placeholder_context",
        "factor_family": "macro_context",
        "input_features": ["fusion__macro_surprise_value"],
        "calculation_type": "actual_vs_consensus_differential",
        "non_signal_usage": "Macroeconomic release surprise placeholder.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
]


def build_macro_context_factor_family_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Macro Context Factor Family Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in MACRO_CONTEXT_FACTOR_METADATA]
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


def summarize_macro_context_factor_family(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize macro context factor family DataFrame."""
    return {
        "total_factors": len(df),
        "status": FACTOR_READY,
        "non_signal": True,
    }
