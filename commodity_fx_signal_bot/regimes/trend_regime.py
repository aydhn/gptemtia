"""
Trend regime detection module.
"""

import pandas as pd
import numpy as np

from regimes.regime_config import RegimeProfile, get_default_regime_profile
from regimes.regime_labels import (
    BULLISH_TREND,
    BEARISH_TREND,
    STRONG_BULLISH_TREND,
    STRONG_BEARISH_TREND,
    WEAK_TREND,
    UNKNOWN,
)
from regimes.regime_features import (
    safe_get_column,
    normalize_to_unit_interval,
    combine_scores,
)


def calculate_trend_direction_score(df: pd.DataFrame) -> pd.Series:
    """
    Calculate a trend direction score between -1 and 1.
    > 0 means bullish, < 0 means bearish.
    """
    scores = []

    # 1. ADX Direction (Plus DI vs Minus DI)
    plus_di = safe_get_column(df, ["plus_di_14"])
    minus_di = safe_get_column(df, ["minus_di_14"])

    if plus_di is not None and minus_di is not None:
        # Avoid division by zero
        total = plus_di + minus_di
        total = total.replace(0, np.nan)
        di_score = (plus_di - minus_di) / total
        scores.append(di_score)

    # 2. Moving Average Stack
    stack_bullish = safe_get_column(
        df, ["ma_stack_bullish_20_50_200", "ma_stack_bullish_10_20_50"]
    )
    stack_bearish = safe_get_column(
        df, ["ma_stack_bearish_20_50_200", "ma_stack_bearish_10_20_50"]
    )

    if stack_bullish is not None and stack_bearish is not None:
        ma_score = stack_bullish.astype(float) - stack_bearish.astype(float)
        scores.append(ma_score)

    # 3. MACD
    macd = safe_get_column(df, ["macd_hist_12_26_9", "macd_line_12_26_9"])
    if macd is not None:
        # Normalize MACD to approximately -1 to 1 based on recent history
        norm_macd = (normalize_to_unit_interval(macd) - 0.5) * 2
        scores.append(norm_macd)

    return combine_scores(scores)


def calculate_trend_strength_score(
    df: pd.DataFrame, profile: RegimeProfile | None = None
) -> pd.Series:
    """
    Calculate a trend strength score between 0 and 1.
    """
    if profile is None:
        profile = get_default_regime_profile()

    scores = []

    # 1. ADX Strength
    adx = safe_get_column(df, ["adx_14"])
    if adx is not None:
        # Cap at 50, scale so threshold = 0.5
        thresh = profile.adx_trend_threshold
        # Linearly map: 0->0, thresh->0.5, 50->1.0
        adx_score = np.where(
            adx < thresh,
            (adx / thresh) * 0.5,
            0.5 + ((adx - thresh) / (50 - thresh)) * 0.5,
        )
        adx_score = np.clip(adx_score, 0, 1)
        scores.append(pd.Series(adx_score, index=df.index))

    # 2. Aroon
    aroon_up = safe_get_column(df, ["aroon_up_14"])
    aroon_down = safe_get_column(df, ["aroon_down_14"])
    if aroon_up is not None and aroon_down is not None:
        aroon_strength = (aroon_up - aroon_down).abs() / 100.0
        scores.append(aroon_strength)

    # 3. Price Distance to MA
    dist_ma = safe_get_column(df, ["dist_close_sma_50", "dist_close_sma_20"])
    if dist_ma is not None:
        # Absolute distance percentage
        norm_dist = normalize_to_unit_interval(dist_ma.abs())
        scores.append(norm_dist)

    combined = combine_scores(scores)
    # Ensure it's between 0 and 1
    if not combined.empty:
        return combined.clip(0, 1)
    return pd.Series(np.nan, index=df.index)


def calculate_trend_regime_score(
    df: pd.DataFrame, profile: RegimeProfile | None = None
) -> pd.Series:
    """
    Combined trend score. > 0 bullish, < 0 bearish, magnitude = strength.
    """
    direction = calculate_trend_direction_score(df)
    strength = calculate_trend_strength_score(df, profile)

    return direction * strength


def detect_trend_regime(
    df: pd.DataFrame, profile: RegimeProfile | None = None
) -> tuple[pd.DataFrame, dict]:
    """
    Detect trend regimes.
    """
    if profile is None:
        profile = get_default_regime_profile()

    out_df = pd.DataFrame(index=df.index)
    summary = {"input_rows": len(df), "warnings": [], "used_columns": []}

    # Calculate scores
    direction = calculate_trend_direction_score(df)
    strength = calculate_trend_strength_score(df, profile)
    score = direction * strength

    out_df["regime_trend_direction"] = direction
    out_df["regime_trend_strength"] = strength
    out_df["regime_trend_score"] = score

    # Check for NaNs
    if direction.isna().all() or strength.isna().all():
        summary["warnings"].append("Insufficient data to calculate trend regimes.")
        out_df["regime_trend_label"] = UNKNOWN
        return out_df, summary

    # Generate labels
    is_bullish = direction > 0.1
    is_bearish = direction < -0.1

    is_strong = strength >= (profile.strong_trend_threshold / 50.0)  # approx scaling
    is_weak = strength < (profile.adx_trend_threshold / 50.0)

    out_df["regime_is_bullish_trend"] = is_bullish & ~is_weak
    out_df["regime_is_bearish_trend"] = is_bearish & ~is_weak
    out_df["regime_is_strong_bullish_trend"] = is_bullish & is_strong
    out_df["regime_is_strong_bearish_trend"] = is_bearish & is_strong
    out_df["regime_is_weak_trend"] = is_weak

    # Assign string labels
    labels = pd.Series(UNKNOWN, index=df.index)

    labels[out_df["regime_is_weak_trend"]] = WEAK_TREND
    labels[out_df["regime_is_bullish_trend"]] = BULLISH_TREND
    labels[out_df["regime_is_bearish_trend"]] = BEARISH_TREND
    labels[out_df["regime_is_strong_bullish_trend"]] = STRONG_BULLISH_TREND
    labels[out_df["regime_is_strong_bearish_trend"]] = STRONG_BEARISH_TREND

    out_df["regime_trend_label"] = labels

    return out_df, summary
