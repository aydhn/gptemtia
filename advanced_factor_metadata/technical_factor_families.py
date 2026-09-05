"""Phase 122 Technical Factor Families Registry.

Overview and foundation for technical factor families derived from Phase 117
indicators and Phase 118 multi-window feature grids.
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

TECHNICAL_FACTOR_METADATA: List[Dict[str, Any]] = [
    {
        "factor_name": "technical_factor_overview",
        "factor_family": "technical",
        "input_features": ["ohlcv_derived_indicators"],
        "calculation_type": "composite_indicator_metadata",
        "non_signal_usage": "Technical indicator feature space mapping.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "indicator_based_factor_placeholder",
        "factor_family": "technical",
        "input_features": ["rsi", "atr", "sma", "macd"],
        "calculation_type": "normalized_technical_composite",
        "non_signal_usage": "Research placeholder for multi-indicator contextual feature.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
    {
        "factor_name": "multi_window_technical_context_placeholder",
        "factor_family": "technical",
        "input_features": ["multi_window_feature_grid"],
        "calculation_type": "multi_window_cross_sectional_grid",
        "non_signal_usage": "Research placeholder for multi-window grid aggregator.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
]


def build_technical_factor_family_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Technical Factor Family Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in TECHNICAL_FACTOR_METADATA]
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


def summarize_technical_factor_family(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize technical factor family DataFrame."""
    return {
        "total_factors": len(df),
        "status": FACTOR_READY,
        "non_signal": True,
    }
