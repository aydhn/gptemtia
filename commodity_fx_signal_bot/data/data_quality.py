"""
Data quality validation functions.
"""

import pandas as pd
from typing import Dict, Any
from core.exceptions import DataQualityError
from core.constants import REQUIRED_COLUMNS


def validate_ohlcv_dataframe(df: pd.DataFrame) -> None:
    """
    Validate that a DataFrame contains expected OHLCV data.

    Args:
        df: The DataFrame to validate.

    Raises:
        DataQualityError: If any validation checks fail.
    """
    if df is None or df.empty:
        raise DataQualityError("DataFrame is empty or None.")

    # Check for required columns
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise DataQualityError(f"Missing required columns: {missing_cols}")

    # Check index type
    if not isinstance(df.index, pd.DatetimeIndex):
        raise DataQualityError("DataFrame index must be a DatetimeIndex.")

    # Check for duplicate indices
    if df.index.has_duplicates:
        raise DataQualityError("DataFrame index contains duplicates.")

    # Check for negative prices (except some rare negative prices like oil in 2020, but mostly invalid)
    price_cols = ["open", "high", "low", "close"]
    for col in price_cols:
        if (df[col] < 0).any():
            raise DataQualityError(f"Negative prices found in column '{col}'.")

    # Check if high < low
    if (df["high"] < df["low"]).any():
        raise DataQualityError(
            "Invalid data found: high price is lower than low price."
        )

    # Check for all-NaN price columns
    for col in price_cols:
        if df[col].isna().all():
            raise DataQualityError(f"Column '{col}' contains entirely NaN values.")


def build_data_quality_report(
    df: pd.DataFrame, raise_on_empty: bool = False
) -> Dict[str, Any]:
    """
    Build a data quality report for an OHLCV DataFrame.

    Args:
        df: The DataFrame to analyze.
        raise_on_empty: Whether to raise DataQualityError on empty df.

    Returns:
        dict: A dictionary containing quality metrics.
    """
    if df is None or df.empty:
        if raise_on_empty:
            raise DataQualityError("DataFrame is empty or None.")
        return {
            "rows": 0,
            "start": None,
            "end": None,
            "missing_ratio_by_column": {},
            "duplicate_index_count": 0,
            "negative_price_count": 0,
            "high_low_error_count": 0,
            "last_close": None,
            "volume_missing_ratio": None,
            "close_missing_ratio": None,
            "min_close": None,
            "max_close": None,
            "error": "DataFrame is empty or None",
        }

    report = {
        "rows": len(df),
        "start": str(df.index.min()),
        "end": str(df.index.max()),
        "missing_ratio_by_column": {},
        "duplicate_index_count": int(df.index.duplicated().sum()),
        "negative_price_count": 0,
        "high_low_error_count": 0,
        "last_close": None,
        "volume_missing_ratio": None,
        "close_missing_ratio": None,
        "min_close": None,
        "max_close": None,
    }

    # Calculate missing ratios
    for col in df.columns:
        missing_count = df[col].isna().sum()
        report["missing_ratio_by_column"][col] = float(missing_count / len(df))

    if "close" in df.columns:
        report["close_missing_ratio"] = report["missing_ratio_by_column"]["close"]

    # Price specific checks
    if all(col in df.columns for col in ["open", "high", "low", "close"]):
        report["negative_price_count"] = int(
            (df[["open", "high", "low", "close"]] < 0).any(axis=1).sum()
        )
        report["high_low_error_count"] = int((df["high"] < df["low"]).sum())
        if len(df["close"].dropna()) > 0:
            report["last_close"] = float(df["close"].dropna().iloc[-1])
            report["min_close"] = float(df["close"].min())
            report["max_close"] = float(df["close"].max())

    if "volume" in df.columns:
        report["volume_missing_ratio"] = report["missing_ratio_by_column"]["volume"]

    return report


def is_dataframe_usable(df: pd.DataFrame, min_rows: int = 50) -> bool:
    """
    Check if a DataFrame is usable for backtesting or signal generation.

    Args:
        df: The DataFrame to check.
        min_rows: The minimum number of rows required.

    Returns:
        bool: True if usable, False otherwise.
    """
    try:
        validate_ohlcv_dataframe(df)
        if len(df) < min_rows:
            return False

        # Check close column NaN ratio (allow up to 5% missing)
        close_nan_ratio = df["close"].isna().sum() / len(df)
        if close_nan_ratio > 0.05:
            return False

        return True
    except DataQualityError:
        return False
