"""Phase 122 Composite Factor Placeholders Registry.

Defines multi-family feature aggregation containers for cross-disciplinary research.
Explicitly NOT a strategy rule engine or signal generator.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_PLACEHOLDER_ONLY

COMPOSITE_FACTOR_METADATA: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_composite_technical_context_placeholder",
        "factor_family": "composite",
        "input_families": ["trend", "momentum", "volatility"],
        "non_signal_usage": "Technical dimensions combination placeholder. No strategy execution.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_composite_macro_event_context_placeholder",
        "factor_family": "composite",
        "input_families": ["macro_context", "calendar_event", "news_attention"],
        "non_signal_usage": "Macroeconomic and media attention confluence placeholder.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_composite_cross_asset_context_placeholder",
        "factor_family": "composite",
        "input_families": ["cross_asset_context", "volatility", "macro_context"],
        "non_signal_usage": "Cross-domain multi-asset correlation and volatility matrix placeholder.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
]


def build_composite_factor_placeholder_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Composite Factor Placeholder Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in COMPOSITE_FACTOR_METADATA]
    df = pd.DataFrame(records)

    summary = {
        "active_profile": active_profile.name,
        "total_factors": len(records),
        "placeholder_factors": len(records),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_PLACEHOLDER_ONLY,
    }
    return df, summary


def summarize_composite_factor_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize composite factor placeholders DataFrame."""
    return {
        "total_factors": len(df),
        "status": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
        "non_signal": True,
    }
