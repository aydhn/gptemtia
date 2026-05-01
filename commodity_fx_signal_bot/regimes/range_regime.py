"""
Range regime detection module.
"""

import pandas as pd
import numpy as np

from regimes.regime_config import RegimeProfile, get_default_regime_profile
from regimes.regime_labels import (
    RANGE_BOUND, COMPRESSED_RANGE, VOLATILE_RANGE, UNKNOWN
)
from regimes.regime_features import safe_get_column, normalize_to_unit_interval, combine_scores

def calculate_range_bound_score(df: pd.DataFrame, profile: RegimeProfile | None = None) -> pd.Series:
    """
    Calculate how range-bound the market is (0 to 1).
    High score = strong range.
    """
    if profile is None:
        profile = get_default_regime_profile()

    scores = []

    # 1. ADX (Low ADX = Range)
    adx = safe_get_column(df, ["adx_14"])
    if adx is not None:
        thresh = profile.range_adx_threshold
        # Linearly map: 0->1.0, thresh->0.5, 50->0.0
        adx_score = np.where(
            adx < thresh,
            1.0 - (adx / thresh) * 0.5,
            0.5 - ((adx - thresh) / (50 - thresh)) * 0.5
        )
        scores.append(pd.Series(np.clip(adx_score, 0, 1), index=df.index))

    # 2. ADX components (Plus DI and Minus DI close together)
    plus_di = safe_get_column(df, ["plus_di_14"])
    minus_di = safe_get_column(df, ["minus_di_14"])
    if plus_di is not None and minus_di is not None:
        diff = (plus_di - minus_di).abs()
        # Smaller difference = more range bound
        di_range_score = 1.0 - normalize_to_unit_interval(diff)
        scores.append(di_range_score)

    # 3. Bollinger Bandwidth (Low bandwidth = compression/range)
    bb_width_pctile = safe_get_column(df, ["percentile_bb_width_20_2_120"])
    if bb_width_pctile is not None:
        scores.append(1.0 - bb_width_pctile)

    combined = combine_scores(scores)
    if not combined.empty:
        return combined.clip(0, 1)
    return pd.Series(np.nan, index=df.index)

def calculate_compression_score(df: pd.DataFrame) -> pd.Series:
    """Calculate price compression (0 to 1)."""
    scores = []

    # Range compression
    comp = safe_get_column(df, ["range_compression_20"])
    if comp is not None:
        scores.append(normalize_to_unit_interval(comp))

    candle_pct = safe_get_column(df, ["candle_range_percentile_120"])
    if candle_pct is not None:
        scores.append(1.0 - candle_pct)

    combined = combine_scores(scores)
    if not combined.empty:
        return combined.clip(0, 1)
    return pd.Series(np.nan, index=df.index)

def detect_range_regime(df: pd.DataFrame, profile: RegimeProfile | None = None) -> tuple[pd.DataFrame, dict]:
    """Detect range regimes."""
    if profile is None:
        profile = get_default_regime_profile()

    out_df = pd.DataFrame(index=df.index)
    summary = {
        "input_rows": len(df),
        "warnings": [],
        "used_columns": []
    }

    range_score = calculate_range_bound_score(df, profile)
    compression = calculate_compression_score(df)

    # Need volatility context
    from regimes.volatility_regime import calculate_volatility_level_score
    vol_score = calculate_volatility_level_score(df, profile)

    out_df["regime_range_score"] = range_score
    out_df["regime_compression_score"] = compression

    if range_score.isna().all():
        summary["warnings"].append("Insufficient data to calculate range regimes.")
        out_df["regime_range_label"] = UNKNOWN
        return out_df, summary

    is_range = range_score > 0.6
    is_compressed = is_range & (compression > 0.7)
    is_volatile = is_range & (vol_score > profile.high_volatility_percentile)

    out_df["regime_is_range_bound"] = is_range
    out_df["regime_is_compressed_range"] = is_compressed
    out_df["regime_is_volatile_range"] = is_volatile

    labels = pd.Series(UNKNOWN, index=df.index)

    labels[is_range] = RANGE_BOUND
    labels[is_volatile] = VOLATILE_RANGE
    labels[is_compressed] = COMPRESSED_RANGE

    out_df["regime_range_label"] = labels

    return out_df, summary
