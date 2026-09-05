"""Phase 122 Trend Factor Families Registry.

Defines trend persistence, moving average slope, MACD, and channel breakout
factors. Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY

TREND_FACTOR_METADATA: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_trend_ma_slope_context",
        "factor_family": "trend",
        "input_features": ["trend__sma_20", "trend__sma_50"],
        "calculation_type": "normalized_slope",
        "non_signal_usage": "Measures angle of moving average trajectories without trading recommendation.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_trend_macd_context",
        "factor_family": "trend",
        "input_features": ["trend__macd_line_12_26", "trend__macd_signal_9"],
        "calculation_type": "histogram_differential",
        "non_signal_usage": "Convergence and divergence spread context. Not a crossover buy/sell trigger.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_trend_donchian_context",
        "factor_family": "trend",
        "input_features": ["trend__donchian_high_20", "trend__donchian_low_20", "close"],
        "calculation_type": "channel_position_ratio",
        "non_signal_usage": "Relative positioning within high/low breakout bounds.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_trend_multi_window_context",
        "factor_family": "trend",
        "input_features": ["trend__sma_10", "trend__sma_20", "trend__sma_50", "trend__sma_200"],
        "calculation_type": "multi_window_trend_alignment",
        "non_signal_usage": "Cross-timeframe trend consistency observation without signal.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
]


def build_trend_factor_family_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Trend Factor Family Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in TREND_FACTOR_METADATA]
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


def summarize_trend_factor_family(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize trend factor family DataFrame."""
    return {
        "total_factors": len(df),
        "status": FACTOR_READY,
        "non_signal": True,
    }
