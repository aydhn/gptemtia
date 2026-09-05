"""Phase 122 Momentum Factor Families Registry.

Defines RSI velocity, Rate of Change (ROC), Stochastic oscillator, and multi-window
momentum factors. Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY

MOMENTUM_FACTOR_METADATA: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_momentum_rsi_context",
        "factor_family": "momentum",
        "input_features": ["momentum__rsi_14"],
        "calculation_type": "normalized_oscillator_level",
        "non_signal_usage": "Measures relative strength speed. Zero buy/sell or overbought/oversold signal.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_momentum_roc_context",
        "factor_family": "momentum",
        "input_features": ["momentum__roc_10", "momentum__roc_20"],
        "calculation_type": "percentage_rate_of_change",
        "non_signal_usage": "Tracks price change velocity across trailing windows.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_momentum_stochastic_context",
        "factor_family": "momentum",
        "input_features": ["momentum__stoch_k_14_3", "momentum__stoch_d_14_3"],
        "calculation_type": "stochastic_range_position",
        "non_signal_usage": "Normalized high-low range velocity context.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_momentum_multi_window_context",
        "factor_family": "momentum",
        "input_features": ["momentum__roc_5", "momentum__roc_10", "momentum__roc_20", "momentum__roc_60"],
        "calculation_type": "composite_rate_of_change_vector",
        "non_signal_usage": "Multi-horizon momentum acceleration vector observation.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
]


def build_momentum_factor_family_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Momentum Factor Family Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in MOMENTUM_FACTOR_METADATA]
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


def summarize_momentum_factor_family(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize momentum factor family DataFrame."""
    return {
        "total_factors": len(df),
        "status": FACTOR_READY,
        "non_signal": True,
    }
