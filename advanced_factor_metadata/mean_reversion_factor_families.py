"""Phase 122 Mean Reversion Factor Families Registry.

Defines z-scores, distance-to-moving-average, percentile rank, and Bollinger
reversion factors. Strictly non-signal and research-only.
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

MEAN_REVERSION_FACTOR_METADATA: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_mean_reversion_zscore_context",
        "factor_family": "mean_reversion",
        "input_features": ["mean_reversion__rolling_zscore_20"],
        "calculation_type": "standardized_zscore",
        "non_signal_usage": "Measures standard deviations from mean without generating reversal trade.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_mean_reversion_distance_to_ma_context",
        "factor_family": "mean_reversion",
        "input_features": ["mean_reversion__dist_sma_50", "mean_reversion__dist_ema_50"],
        "calculation_type": "percentage_distance_to_mean",
        "non_signal_usage": "Measures gap from moving average baseline.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_mean_reversion_percentile_placeholder",
        "factor_family": "mean_reversion",
        "input_features": ["mean_reversion__percentile_rank_100"],
        "calculation_type": "rolling_percentile_position",
        "non_signal_usage": "Percentile ranking context within lookback distribution.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_mean_reversion_bollinger_context",
        "factor_family": "mean_reversion",
        "input_features": ["volatility__bb_upper_20", "volatility__bb_lower_20", "close"],
        "calculation_type": "bollinger_percent_b",
        "non_signal_usage": "Position within standard deviation envelope.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
]


def build_mean_reversion_factor_family_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Mean Reversion Factor Family Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in MEAN_REVERSION_FACTOR_METADATA]
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


def summarize_mean_reversion_factor_family(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize mean reversion factor family DataFrame."""
    return {
        "total_factors": len(df),
        "status": FACTOR_READY,
        "non_signal": True,
    }
