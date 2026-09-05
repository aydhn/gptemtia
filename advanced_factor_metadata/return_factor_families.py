"""Phase 122 Return Factor Families Registry.

Defines historical trailing return factors across short, medium, and multi-horizon windows.
Strictly non-signal, research-only, and lookahead-free.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY

RETURN_FACTOR_METADATA: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_return_short_window_context",
        "factor_family": "return",
        "input_features": ["return__simple_1d", "return__simple_3d", "return__simple_5d"],
        "calculation_type": "trailing_simple_return",
        "non_signal_usage": "Short-term historical performance observation without forward return.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_return_medium_window_context",
        "factor_family": "return",
        "input_features": ["return__simple_10d", "return__simple_20d"],
        "calculation_type": "trailing_compound_return",
        "non_signal_usage": "Medium-term trailing price performance metric.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_return_multi_horizon_context",
        "factor_family": "return",
        "input_features": ["return__simple_1d", "return__simple_5d", "return__simple_20d", "return__simple_60d"],
        "calculation_type": "multi_horizon_return_vector",
        "non_signal_usage": "Multi-horizon trailing return vector. Strictly zero lookahead or future shifts.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
]


def build_return_factor_family_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Return Factor Family Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in RETURN_FACTOR_METADATA]
    df = pd.DataFrame(records)

    summary = {
        "active_profile": active_profile.name,
        "total_factors": len(records),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_READY,
    }
    return df, summary


def summarize_return_factor_family(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize return factor family DataFrame."""
    return {
        "total_factors": len(df),
        "status": FACTOR_READY,
        "non_signal": True,
    }
