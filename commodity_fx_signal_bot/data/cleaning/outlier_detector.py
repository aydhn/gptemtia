from dataclasses import dataclass
from typing import Any, Dict, Tuple

import numpy as np
import pandas as pd

from core.logger import get_logger

logger = get_logger(__name__)


@dataclass
class OutlierDetectionConfig:
    zscore_threshold: float = 6.0
    return_threshold: float = 0.20
    rolling_window: int = 50
    atr_multiplier_threshold: float = 8.0
    enabled_methods: Tuple[str, ...] = ("return", "zscore", "rolling_mad")


def calculate_returns(df: pd.DataFrame) -> pd.Series:
    """Calculate percentage returns of the close price."""
    if "close" not in df.columns:
        return pd.Series(dtype=float)
    return df["close"].pct_change().fillna(0.0)


def detect_return_outliers(df: pd.DataFrame, threshold: float = 0.20) -> pd.DataFrame:
    """Detect outliers based on absolute percentage returns."""
    returns = calculate_returns(df)
    if returns.empty:
        return pd.DataFrame()

    outlier_mask = returns.abs() > threshold
    return df[outlier_mask].copy()


def detect_zscore_outliers(df: pd.DataFrame, threshold: float = 6.0) -> pd.DataFrame:
    """Detect outliers based on z-score of returns."""
    returns = calculate_returns(df)
    if returns.empty or len(returns) < 2:
        return pd.DataFrame()

    mean = returns.mean()
    std = returns.std()

    if std == 0:
        return pd.DataFrame()

    zscores = (returns - mean) / std
    outlier_mask = zscores.abs() > threshold
    return df[outlier_mask].copy()


def detect_rolling_mad_outliers(
    df: pd.DataFrame, window: int = 50, threshold: float = 8.0
) -> pd.DataFrame:
    """Detect outliers based on rolling Median Absolute Deviation."""
    returns = calculate_returns(df)
    if returns.empty or len(returns) < window:
        return pd.DataFrame()

    rolling_median = returns.rolling(window=window).median()
    # MAD = median(|Xi - median(X)|)
    # Using pandas equivalent
    rolling_mad = returns.rolling(window=window).apply(
        lambda x: np.median(np.abs(x - np.median(x)))
    )

    # Avoid division by zero
    rolling_mad = rolling_mad.replace(0, np.nan)

    modified_zscore = 0.6745 * (returns - rolling_median) / rolling_mad
    outlier_mask = modified_zscore.abs() > threshold
    return df[outlier_mask].copy()


def build_outlier_report(
    df: pd.DataFrame, config: OutlierDetectionConfig | None = None
) -> Dict[str, Any]:
    """Build a comprehensive outlier detection report."""
    if config is None:
        config = OutlierDetectionConfig()

    if df is None or df.empty or "close" not in df.columns:
        return {"total_outliers": 0, "outliers_by_method": {}, "details": []}

    outliers_found = {}

    if "return" in config.enabled_methods:
        ret_outliers = detect_return_outliers(df, config.return_threshold)
        outliers_found["return"] = ret_outliers.index.tolist()

    if "zscore" in config.enabled_methods:
        z_outliers = detect_zscore_outliers(df, config.zscore_threshold)
        outliers_found["zscore"] = z_outliers.index.tolist()

    if "rolling_mad" in config.enabled_methods:
        mad_outliers = detect_rolling_mad_outliers(
            df, config.rolling_window, config.atr_multiplier_threshold
        )
        outliers_found["rolling_mad"] = mad_outliers.index.tolist()

    # Combine all unique outlier indices
    all_outlier_indices = set()
    for indices in outliers_found.values():
        all_outlier_indices.update(indices)

    details = []
    returns = calculate_returns(df)

    for idx in sorted(all_outlier_indices):
        methods_detected = [
            m for m, indices in outliers_found.items() if idx in indices
        ]
        details.append(
            {
                "timestamp": str(idx),
                "close": float(df.loc[idx, "close"]),
                "return": float(returns.loc[idx]),
                "methods": methods_detected,
            }
        )

    return {
        "total_outliers": len(all_outlier_indices),
        "outliers_by_method": {k: len(v) for k, v in outliers_found.items()},
        "details": details,
        "notes": "FX and Commodity pairs may have different volatility profiles; these are just flags.",
    }


def add_outlier_flags(
    df: pd.DataFrame, config: OutlierDetectionConfig | None = None
) -> pd.DataFrame:
    """Add boolean flag columns indicating outliers."""
    if df is None or df.empty or "close" not in df.columns:
        return df

    if config is None:
        config = OutlierDetectionConfig()

    flagged_df = df.copy()
    flagged_df["is_outlier"] = False

    if "return" in config.enabled_methods:
        ret_outliers = detect_return_outliers(df, config.return_threshold)
        flagged_df.loc[ret_outliers.index, "is_outlier"] = True

    if "zscore" in config.enabled_methods:
        z_outliers = detect_zscore_outliers(df, config.zscore_threshold)
        flagged_df.loc[z_outliers.index, "is_outlier"] = True

    if "rolling_mad" in config.enabled_methods:
        mad_outliers = detect_rolling_mad_outliers(
            df, config.rolling_window, config.atr_multiplier_threshold
        )
        flagged_df.loc[mad_outliers.index, "is_outlier"] = True

    return flagged_df
