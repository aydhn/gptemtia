"""Phase 132: Macro Revision Regime Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_MACRO_REVISION_CONTEXTS = [
    {
        "revision_context_id": "rev_ctx_nfp_previous",
        "context_name": "previous_value_revision_context",
        "indicator_id": "macro_us_nfp",
        "revision_cycle": "first_revision",
        "tracks_direction": True,
        "tracks_magnitude": True,
        "quality_rating": "high",
    },
    {
        "revision_context_id": "rev_ctx_gdp_benchmark",
        "context_name": "revised_value_context",
        "indicator_id": "macro_us_real_gdp_qoq",
        "revision_cycle": "annual_benchmark",
        "tracks_direction": True,
        "tracks_magnitude": True,
        "quality_rating": "high",
    },
    {
        "revision_context_id": "rev_ctx_direction_placeholder",
        "context_name": "revision_direction_placeholder",
        "indicator_id": "macro_us_cpi_yoy",
        "revision_cycle": "seasonal_adjustment",
        "tracks_direction": True,
        "tracks_magnitude": False,
        "quality_rating": "medium",
    },
    {
        "revision_context_id": "rev_ctx_magnitude_placeholder",
        "context_name": "revision_magnitude_placeholder",
        "indicator_id": "macro_us_nfp",
        "revision_cycle": "subsequent_revision",
        "tracks_direction": False,
        "tracks_magnitude": True,
        "quality_rating": "high",
    },
    {
        "revision_context_id": "rev_ctx_metadata_quality",
        "context_name": "revision_metadata_quality_context",
        "indicator_id": "macro_eu_hicp_yoy",
        "revision_cycle": "final_validation",
        "tracks_direction": True,
        "tracks_magnitude": True,
        "quality_rating": "high",
    },
]


def build_macro_revision_regime_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of macro revision regime contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_MACRO_REVISION_CONTEXTS:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_revision_contexts": len(df),
        "revision_cycles": df["revision_cycle"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_revision_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for macro revision context."""
    return {
        "total_revision_contexts": len(df),
        "indicators_tracked": df["indicator_id"].nunique() if "indicator_id" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
