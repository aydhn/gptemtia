"""
Helper functions for calculating regime features across different modules.
"""

import pandas as pd
import numpy as np


def safe_get_column(df: pd.DataFrame, candidates: list[str]) -> pd.Series | None:
    """
    Safely get the first available column from a list of candidates.
    Returns None if no candidates are found.
    """
    for col in candidates:
        if col in df.columns and not df[col].isna().all():
            return df[col]
    return None


def normalize_to_unit_interval(series: pd.Series) -> pd.Series:
    """
    Normalize a series to the [0, 1] interval.
    Uses min-max scaling with a rolling window (default 120) if possible,
    otherwise uses the entire series.
    """
    if series is None or series.empty or series.isna().all():
        return pd.Series(np.nan, index=series.index if series is not None else None)

    # We use a rolling window to avoid lookahead bias and handle non-stationary data
    window = 120
    roll_min = series.rolling(window=window, min_periods=20).min()
    roll_max = series.rolling(window=window, min_periods=20).max()

    # Fill NA for the first elements where rolling cannot calculate
    roll_min = roll_min.fillna(series.expanding(min_periods=1).min())
    roll_max = roll_max.fillna(series.expanding(min_periods=1).max())

    range_val = roll_max - roll_min
    # Avoid division by zero
    range_val = range_val.replace(0, np.nan)

    normalized = (series - roll_min) / range_val
    return normalized.fillna(0.5)  # Default to middle if we can't calculate


def combine_scores(
    scores: list[pd.Series], weights: list[float] | None = None
) -> pd.Series:
    """
    Combine multiple score series into a single score.
    Averages them by default, ignoring NaNs.
    """
    # Filter out None and empty series
    valid_scores = [
        s for s in scores if s is not None and not s.empty and not s.isna().all()
    ]

    if not valid_scores:
        if scores and scores[0] is not None:
            return pd.Series(np.nan, index=scores[0].index)
        return pd.Series(dtype=float)

    df = pd.concat(valid_scores, axis=1)

    if weights is not None:
        if len(weights) != len(valid_scores):
            # If weights don't match, fall back to equal weighting
            return df.mean(axis=1)

        # Normalize weights
        w = np.array(weights)
        w = w / w.sum()

        # Calculate weighted sum, ignoring NaNs by re-weighting
        weighted_sum = pd.Series(0.0, index=df.index)
        weight_sum = pd.Series(0.0, index=df.index)

        for i, col in enumerate(df.columns):
            valid_mask = ~df[col].isna()
            weighted_sum[valid_mask] += df[col][valid_mask] * w[i]
            weight_sum[valid_mask] += w[i]

        # Avoid division by zero
        weight_sum = weight_sum.replace(0, np.nan)
        return weighted_sum / weight_sum

    return df.mean(axis=1)


def add_regime_base_features(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """
    Add base features that are common across regime detections.
    This mostly initializes columns with NaNs if they don't exist.
    """
    out_df = pd.DataFrame(index=df.index)
    summary = {"input_rows": len(df), "warnings": [], "columns_added": []}

    base_cols = [
        "regime_trend_strength_raw",
        "regime_trend_direction_raw",
        "regime_volatility_level_raw",
        "regime_momentum_direction_raw",
        "regime_range_pressure_raw",
        "regime_mean_reversion_pressure_raw",
        "regime_mtf_alignment_raw",
        "regime_conflict_raw",
    ]

    for col in base_cols:
        out_df[col] = np.nan
        summary["columns_added"].append(col)

    return out_df, summary
