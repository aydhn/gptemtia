"""
Data quality validation functions.
"""
import pandas as pd
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
    price_cols = ['open', 'high', 'low', 'close']
    for col in price_cols:
        if (df[col] < 0).any():
            raise DataQualityError(f"Negative prices found in column '{col}'.")
