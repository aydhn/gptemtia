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


def infer_quality_grade(report: Dict[str, Any]) -> str:
    """Infer a letter grade for data quality based on the report."""
    if report.get("rows", 0) == 0 or report.get("error"):
        return "F"

    rows = report.get("rows", 0)
    missing_close = report.get("close_missing_ratio", 0.0) or 0.0
    duplicates = report.get("duplicate_index_count", 0)
    negatives = report.get("negative_price_count", 0)
    high_low_errors = report.get("high_low_error_count", 0)

    if (
        rows < 50
        or missing_close > 0.05
        or duplicates > 5
        or negatives > 0
        or high_low_errors > 0
    ):
        return "D"

    if missing_close > 0.01 or duplicates > 0:
        return "C"

    if missing_close > 0.0:
        return "B"

    return "A"


def compare_dataframes_basic(
    old_df: pd.DataFrame, new_df: pd.DataFrame
) -> Dict[str, Any]:
    """Basic comparison between an existing DataFrame and a newly downloaded one."""
    old_rows = len(old_df) if old_df is not None and not old_df.empty else 0
    new_rows = len(new_df) if new_df is not None and not new_df.empty else 0

    old_start = str(old_df.index.min()) if old_rows > 0 else None
    old_end = str(old_df.index.max()) if old_rows > 0 else None
    new_start = str(new_df.index.min()) if new_rows > 0 else None
    new_end = str(new_df.index.max()) if new_rows > 0 else None

    added_rows = max(0, new_rows - old_rows)

    overlap_rows_estimate = 0
    if old_rows > 0 and new_rows > 0:
        # Simple estimate: how many indices match
        overlap_rows_estimate = len(old_df.index.intersection(new_df.index))

    changed_last_close = False
    if (
        old_rows > 0
        and new_rows > 0
        and "close" in old_df.columns
        and "close" in new_df.columns
    ):
        old_last_close = (
            old_df["close"].dropna().iloc[-1]
            if not old_df["close"].dropna().empty
            else None
        )
        new_last_close = (
            new_df["close"].dropna().iloc[-1]
            if not new_df["close"].dropna().empty
            else None
        )

        if old_last_close is not None and new_last_close is not None:
            # Check if last close values differ significantly
            changed_last_close = (
                abs(old_last_close - new_last_close) / old_last_close > 0.001
            )

    return {
        "old_rows": old_rows,
        "new_rows": new_rows,
        "added_rows": added_rows,
        "old_start": old_start,
        "old_end": old_end,
        "new_start": new_start,
        "new_end": new_end,
        "overlap_rows_estimate": overlap_rows_estimate,
        "changed_last_close": changed_last_close,
    }
