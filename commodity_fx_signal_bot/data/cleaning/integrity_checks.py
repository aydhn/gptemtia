from typing import Any, Dict, List

import pandas as pd

from core.constants import REQUIRED_COLUMNS
from core.logger import get_logger

logger = get_logger(__name__)


def check_required_columns(df: pd.DataFrame) -> List[str]:
    """Check if all required columns are present."""
    if df is None or df.empty:
        return ["DataFrame is empty or None"]

    errors = []
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            errors.append(f"Missing required column: {col}")
    return errors


def check_datetime_index(df: pd.DataFrame) -> List[str]:
    """Check if the DataFrame has a valid DatetimeIndex."""
    if df is None or df.empty:
        return []

    errors = []
    if not isinstance(df.index, pd.DatetimeIndex):
        errors.append(f"Index is not a DatetimeIndex, but {type(df.index)}")
    elif not df.index.is_monotonic_increasing:
        errors.append("DatetimeIndex is not monotonic increasing")
    return errors


def check_duplicate_index(df: pd.DataFrame) -> List[str]:
    """Check for duplicate index values."""
    if df is None or df.empty:
        return []

    errors = []
    if df.index.has_duplicates:
        dup_count = df.index.duplicated().sum()
        errors.append(f"Found {dup_count} duplicate index values")
    return errors


def check_price_consistency(df: pd.DataFrame) -> List[str]:
    """Check general price consistency (e.g., all NaN)."""
    if df is None or df.empty:
        return []

    errors = []
    price_cols = [col for col in ["open", "high", "low", "close"] if col in df.columns]

    for col in price_cols:
        if df[col].isna().all():
            errors.append(f"Column '{col}' is entirely NaN")

    return errors


def check_negative_or_zero_prices(df: pd.DataFrame) -> List[str]:
    """Check for negative or zero prices."""
    if df is None or df.empty:
        return []

    errors = []
    price_cols = [col for col in ["open", "high", "low", "close"] if col in df.columns]

    for col in price_cols:
        neg_count = (df[col] < 0).sum()
        if neg_count > 0:
            errors.append(f"Found {neg_count} negative prices in column '{col}'")

        zero_count = (df[col] == 0).sum()
        if zero_count > 0:
            errors.append(f"Found {zero_count} zero prices in column '{col}'")

    return errors


def check_high_low_relationship(df: pd.DataFrame) -> List[str]:
    """Check that high is always >= low."""
    if df is None or df.empty or "high" not in df.columns or "low" not in df.columns:
        return []

    errors = []
    # Using float precision safe comparison
    invalid_mask = df["high"] < (df["low"] - 1e-10)
    invalid_count = invalid_mask.sum()

    if invalid_count > 0:
        errors.append(f"Found {invalid_count} rows where high < low")

    return errors


def check_open_close_within_high_low(df: pd.DataFrame) -> List[str]:
    """Check that open and close are within the high-low range."""
    if df is None or df.empty:
        return []

    if not all(col in df.columns for col in ["open", "high", "low", "close"]):
        return []

    warnings = []

    # Open > High
    open_high_mask = df["open"] > (df["high"] + 1e-10)
    if open_high_mask.sum() > 0:
        warnings.append(f"Found {open_high_mask.sum()} rows where open > high")

    # Open < Low
    open_low_mask = df["open"] < (df["low"] - 1e-10)
    if open_low_mask.sum() > 0:
        warnings.append(f"Found {open_low_mask.sum()} rows where open < low")

    # Close > High
    close_high_mask = df["close"] > (df["high"] + 1e-10)
    if close_high_mask.sum() > 0:
        warnings.append(f"Found {close_high_mask.sum()} rows where close > high")

    # Close < Low
    close_low_mask = df["close"] < (df["low"] - 1e-10)
    if close_low_mask.sum() > 0:
        warnings.append(f"Found {close_low_mask.sum()} rows where close < low")

    return warnings


def check_minimum_rows(df: pd.DataFrame, min_rows: int) -> List[str]:
    """Check if the DataFrame has the minimum required number of rows."""
    if df is None:
        return [f"DataFrame is None (min {min_rows} required)"]

    errors = []
    if len(df) < min_rows:
        errors.append(f"DataFrame has {len(df)} rows, minimum required is {min_rows}")

    return errors


def run_integrity_checks(df: pd.DataFrame, min_rows: int = 50) -> Dict[str, Any]:
    """Run all integrity checks and return a summary report."""
    errors = []
    warnings = []

    # Hard errors
    errors.extend(check_required_columns(df))
    errors.extend(check_datetime_index(df))
    errors.extend(check_duplicate_index(df))
    errors.extend(check_price_consistency(df))
    errors.extend(check_high_low_relationship(df))
    errors.extend(check_minimum_rows(df, min_rows))

    # Soft errors (warnings)
    warnings.extend(check_negative_or_zero_prices(df))
    warnings.extend(check_open_close_within_high_low(df))

    check_count = 8  # Number of check functions called

    return {
        "passed": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "check_count": check_count,
        "error_count": len(errors),
        "warning_count": len(warnings),
    }
