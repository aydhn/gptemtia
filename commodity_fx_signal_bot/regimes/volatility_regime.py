"""
Volatility regime detection module.
"""

import pandas as pd
import numpy as np

from regimes.regime_config import RegimeProfile, get_default_regime_profile
from regimes.regime_labels import (
    HIGH_VOLATILITY,
    LOW_VOLATILITY,
    VOLATILITY_EXPANSION,
    VOLATILITY_COMPRESSION,
    UNKNOWN,
)
from regimes.regime_features import (
    safe_get_column,
    normalize_to_unit_interval,
    combine_scores,
)


def calculate_volatility_level_score(
    df: pd.DataFrame, profile: RegimeProfile | None = None
) -> pd.Series:
    """
    Calculate volatility level score between 0 and 1.
    """
    scores = []

    # 1. ATR Percentile
    atr_pctile = safe_get_column(df, ["percentile_atr_pct_14_120"])
    if atr_pctile is not None:
        scores.append(atr_pctile)
    else:
        atr_pct = safe_get_column(df, ["atr_pct_14", "atr_14"])
        if atr_pct is not None:
            scores.append(normalize_to_unit_interval(atr_pct))

    # 2. Bollinger Bandwidth
    bb_width_pctile = safe_get_column(df, ["percentile_bb_width_20_2_120"])
    if bb_width_pctile is not None:
        scores.append(bb_width_pctile)
    else:
        bb_width = safe_get_column(df, ["bb_width_20_2"])
        if bb_width is not None:
            scores.append(normalize_to_unit_interval(bb_width))

    # 3. Historical Volatility
    hist_vol = safe_get_column(df, ["hist_vol_20"])
    if hist_vol is not None:
        scores.append(normalize_to_unit_interval(hist_vol))

    combined = combine_scores(scores)
    if not combined.empty:
        return combined.clip(0, 1)
    return pd.Series(np.nan, index=df.index)


def calculate_volatility_change_score(df: pd.DataFrame) -> pd.Series:
    """
    Calculate volatility change (expansion/compression).
    > 0 means expansion, < 0 means compression.
    """
    scores = []

    # Use pre-calculated events if available
    squeeze = safe_get_column(df, ["event_volatility_squeeze_bb20"])
    expansion = safe_get_column(df, ["event_volatility_expansion_bb20"])

    if squeeze is not None and expansion is not None:
        # These are usually 0/1 boolean-like
        change = expansion.astype(float) - squeeze.astype(float)
        scores.append(change)

    # Rate of change of ATR
    atr = safe_get_column(df, ["atr_14"])
    if atr is not None:
        # Simple 5-bar ROC of ATR
        atr_roc = atr.pct_change(5)
        # Normalize to roughly -1 to 1
        atr_roc_norm = (normalize_to_unit_interval(atr_roc) - 0.5) * 2
        scores.append(atr_roc_norm)

    return combine_scores(scores)


def detect_volatility_regime(
    df: pd.DataFrame, profile: RegimeProfile | None = None
) -> tuple[pd.DataFrame, dict]:
    """
    Detect volatility regimes.
    """
    if profile is None:
        profile = get_default_regime_profile()

    out_df = pd.DataFrame(index=df.index)
    summary = {"input_rows": len(df), "warnings": [], "used_columns": []}

    level = calculate_volatility_level_score(df, profile)
    change = calculate_volatility_change_score(df)

    out_df["regime_volatility_level"] = level
    out_df["regime_volatility_change"] = change
    out_df["regime_volatility_score"] = level  # Primary score is the level

    if level.isna().all():
        summary["warnings"].append("Insufficient data to calculate volatility regimes.")
        out_df["regime_volatility_label"] = UNKNOWN
        return out_df, summary

    is_high = level > profile.high_volatility_percentile
    is_low = level < profile.low_volatility_percentile

    is_expanding = change > 0.2
    is_compressing = change < -0.2

    out_df["regime_is_high_volatility"] = is_high
    out_df["regime_is_low_volatility"] = is_low
    out_df["regime_is_volatility_expansion"] = is_expanding
    out_df["regime_is_volatility_compression"] = is_compressing

    labels = pd.Series(UNKNOWN, index=df.index)

    labels[is_compressing] = VOLATILITY_COMPRESSION
    labels[is_low] = LOW_VOLATILITY
    labels[is_expanding] = VOLATILITY_EXPANSION
    labels[is_high] = HIGH_VOLATILITY

    out_df["regime_volatility_label"] = labels

    return out_df, summary
