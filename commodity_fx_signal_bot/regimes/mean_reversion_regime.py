"""
Mean reversion regime detection module.
"""

import pandas as pd
import numpy as np

from regimes.regime_config import RegimeProfile, get_default_regime_profile
from regimes.regime_labels import MEAN_REVERSION_FRIENDLY, UNKNOWN
from regimes.regime_features import (
    safe_get_column,
    normalize_to_unit_interval,
    combine_scores,
)
from regimes.trend_regime import calculate_trend_strength_score


def calculate_mean_reversion_friendliness_score(
    df: pd.DataFrame, profile: RegimeProfile | None = None
) -> pd.Series:
    """Calculate how friendly the environment is for mean reversion (0 to 1)."""
    if profile is None:
        profile = get_default_regime_profile()

    scores = []

    # Low trend is better for mean reversion
    trend_str = calculate_trend_strength_score(df, profile)
    if trend_str is not None and not trend_str.isna().all():
        scores.append(1.0 - trend_str)

    # High extension means potential reversion
    zscore = safe_get_column(df, ["zscore_close_20"])
    if zscore is not None:
        # We want absolute z-score normalized. High z-score = high extension
        abs_z = zscore.abs()
        z_norm = np.where(
            abs_z > profile.mean_reversion_zscore_threshold,
            1.0,
            abs_z / profile.mean_reversion_zscore_threshold,
        )
        scores.append(pd.Series(z_norm, index=df.index))

    bb_pct = safe_get_column(df, ["bb_percent_b_20_2"])
    if bb_pct is not None:
        # > 1 or < 0 is outside bands
        outside = ((bb_pct > 1.0) | (bb_pct < 0.0)).astype(float)
        scores.append(outside)

    combined = combine_scores(scores)
    if not combined.empty:
        return combined.clip(0, 1)
    return pd.Series(np.nan, index=df.index)


def detect_mean_reversion_regime(
    df: pd.DataFrame, profile: RegimeProfile | None = None
) -> tuple[pd.DataFrame, dict]:
    """Detect mean reversion regimes."""
    if profile is None:
        profile = get_default_regime_profile()

    out_df = pd.DataFrame(index=df.index)
    summary = {"input_rows": len(df), "warnings": [], "used_columns": []}

    mr_score = calculate_mean_reversion_friendliness_score(df, profile)
    trend_str = calculate_trend_strength_score(df, profile)

    out_df["regime_mean_reversion_score"] = mr_score

    if mr_score.isna().all():
        summary["warnings"].append(
            "Insufficient data to calculate mean reversion regimes."
        )
        out_df["regime_mean_reversion_label"] = UNKNOWN
        return out_df, summary

    is_friendly = mr_score > 0.6

    # If there is a strong trend, mean reversion is risky
    is_risky = False
    if trend_str is not None and not trend_str.isna().all():
        is_risky = trend_str > (profile.strong_trend_threshold / 50.0)

    out_df["regime_is_mean_reversion_friendly"] = is_friendly & ~is_risky
    out_df["regime_is_reversion_risky_trend"] = is_risky

    labels = pd.Series(UNKNOWN, index=df.index)

    labels[out_df["regime_is_mean_reversion_friendly"]] = MEAN_REVERSION_FRIENDLY

    out_df["regime_mean_reversion_label"] = labels

    return out_df, summary
