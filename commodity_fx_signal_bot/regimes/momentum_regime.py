"""
Momentum regime detection module.
"""

import pandas as pd
import numpy as np

from regimes.regime_config import RegimeProfile, get_default_regime_profile
from regimes.regime_labels import (
    MOMENTUM_BULLISH,
    MOMENTUM_BEARISH,
    MOMENTUM_NEUTRAL,
    UNKNOWN,
)
from regimes.regime_features import (
    safe_get_column,
    normalize_to_unit_interval,
    combine_scores,
)


def calculate_momentum_direction_score(df: pd.DataFrame) -> pd.Series:
    """Calculate momentum direction (-1 to 1)."""
    scores = []

    rsi = safe_get_column(df, ["rsi_14"])
    if rsi is not None:
        # 50 is neutral. Map 0-100 to -1 to 1
        scores.append((rsi - 50) / 50.0)

    roc = safe_get_column(df, ["roc_10"])
    if roc is not None:
        scores.append((normalize_to_unit_interval(roc) - 0.5) * 2)

    macd_hist = safe_get_column(df, ["macd_hist_12_26_9"])
    if macd_hist is not None:
        scores.append((normalize_to_unit_interval(macd_hist) - 0.5) * 2)

    slope = safe_get_column(df, ["slope_rsi_14_5"])
    if slope is not None:
        scores.append((normalize_to_unit_interval(slope) - 0.5) * 2)

    combined = combine_scores(scores)
    if not combined.empty:
        return combined.clip(-1, 1)
    return pd.Series(np.nan, index=df.index)


def calculate_momentum_quality_score(df: pd.DataFrame) -> pd.Series:
    """Calculate strength/quality of momentum (0 to 1)."""
    direction = calculate_momentum_direction_score(df)
    return direction.abs()


def detect_momentum_regime(
    df: pd.DataFrame, profile: RegimeProfile | None = None
) -> tuple[pd.DataFrame, dict]:
    """Detect momentum regimes."""
    if profile is None:
        profile = get_default_regime_profile()

    out_df = pd.DataFrame(index=df.index)
    summary = {"input_rows": len(df), "warnings": [], "used_columns": []}

    direction = calculate_momentum_direction_score(df)
    quality = calculate_momentum_quality_score(df)

    out_df["regime_momentum_direction"] = direction
    out_df["regime_momentum_quality"] = quality
    out_df["regime_momentum_score"] = direction * quality

    if direction.isna().all():
        summary["warnings"].append("Insufficient data to calculate momentum regimes.")
        out_df["regime_momentum_label"] = UNKNOWN
        return out_df, summary

    # Thresholds
    thresh = profile.momentum_threshold if profile.momentum_threshold > 0 else 0.2

    is_bullish = direction > thresh
    is_bearish = direction < -thresh
    is_neutral = (direction <= thresh) & (direction >= -thresh)

    out_df["regime_is_momentum_bullish"] = is_bullish
    out_df["regime_is_momentum_bearish"] = is_bearish
    out_df["regime_is_momentum_neutral"] = is_neutral

    labels = pd.Series(UNKNOWN, index=df.index)

    labels[is_neutral] = MOMENTUM_NEUTRAL
    labels[is_bullish] = MOMENTUM_BULLISH
    labels[is_bearish] = MOMENTUM_BEARISH

    out_df["regime_momentum_label"] = labels

    return out_df, summary
