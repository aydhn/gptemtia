"""Phase 122 Volatility Factor Families Registry.

Defines Average True Range (ATR), realized volatility, Bollinger Bandwidth,
and range-based dispersion factors. Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY

VOLATILITY_FACTOR_METADATA: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_volatility_atr_context",
        "factor_family": "volatility",
        "input_features": ["volatility__atr_14", "close"],
        "calculation_type": "normalized_atr_ratio",
        "non_signal_usage": "Measures price variance range normalized by price level.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_volatility_realized_context",
        "factor_family": "volatility",
        "input_features": ["volatility__realized_vol_20"],
        "calculation_type": "annualized_rolling_std",
        "non_signal_usage": "Annualized historical return variance without position sizing.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_volatility_bollinger_width_context",
        "factor_family": "volatility",
        "input_features": ["volatility__bb_bandwidth_20"],
        "calculation_type": "bollinger_bandwidth_ratio",
        "non_signal_usage": "Relative expansion/contraction of statistical bands.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "factor_name": "factor_volatility_range_context",
        "factor_family": "volatility",
        "input_features": ["volatility__parkinson_20", "volatility__garman_klass_20"],
        "calculation_type": "extremum_range_dispersion",
        "non_signal_usage": "High-low intraday range dispersion observation.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
]


def build_volatility_factor_family_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Volatility Factor Family Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in VOLATILITY_FACTOR_METADATA]
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


def summarize_volatility_factor_family(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize volatility factor family DataFrame."""
    return {
        "total_factors": len(df),
        "status": FACTOR_READY,
        "non_signal": True,
    }
