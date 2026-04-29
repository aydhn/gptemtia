from dataclasses import dataclass
from typing import Any, Dict, Tuple

import pandas as pd

from core.constants import REQUIRED_COLUMNS
from core.logger import get_logger

logger = get_logger(__name__)


@dataclass
class CleaningOptions:
    drop_duplicate_index: bool = True
    sort_index: bool = True
    fix_column_order: bool = True
    fill_missing_volume: bool = True
    remove_negative_prices: bool = False
    repair_high_low_inconsistency: bool = False
    forward_fill_small_gaps: bool = False
    max_forward_fill_gap: int = 2
    keep_original_attrs: bool = True


class OHLCVCleaner:
    """Central class for cleaning OHLCV DataFrames."""

    def __init__(self, options: CleaningOptions | None = None):
        self.options = options or CleaningOptions()

    def clean(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """
        Clean the OHLCV DataFrame according to the configured options.
        Returns a new DataFrame and a summary dictionary.
        """
        if df is None or df.empty:
            return df, {
                "input_rows": 0,
                "output_rows": 0,
                "warnings": ["Empty DataFrame"],
            }

        # Create a copy so we don't mutate the original
        cleaned_df = df.copy(deep=True)

        summary: Dict[str, Any] = {
            "input_rows": len(df),
            "output_rows": len(df),
            "duplicate_rows_removed": 0,
            "columns_standardized": False,
            "missing_volume_filled": False,
            "sorted_index": False,
            "warnings": [],
            "errors": [],
        }

        try:
            if self.options.drop_duplicate_index:
                cleaned_df, dup_count = self.drop_duplicate_timestamps(cleaned_df)
                summary["duplicate_rows_removed"] = dup_count

            if self.options.sort_index:
                cleaned_df = self.sort_datetime_index(cleaned_df)
                summary["sorted_index"] = True

            if self.options.fix_column_order:
                cleaned_df = self.standardize_columns(cleaned_df)
                cleaned_df = self.ensure_column_order(cleaned_df)
                summary["columns_standardized"] = True

            if self.options.fill_missing_volume:
                cleaned_df = self.fill_missing_volume_column(cleaned_df)
                summary["missing_volume_filled"] = True

            if self.options.remove_negative_prices:
                # We won't automatically remove negative prices by default as instructed
                pass

            if self.options.repair_high_low_inconsistency:
                # We won't automatically fix high/low by default as instructed
                pass

        except Exception as e:
            logger.error(f"Error during OHLCV cleaning: {e}")
            summary["errors"].append(str(e))

        summary["output_rows"] = len(cleaned_df)
        return cleaned_df, summary

    def standardize_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Ensure column names are lowercase."""
        df.columns = [str(col).lower() for col in df.columns]
        return df

    def sort_datetime_index(self, df: pd.DataFrame) -> pd.DataFrame:
        """Sort the DatetimeIndex."""
        if not df.index.is_monotonic_increasing:
            df = df.sort_index()
        return df

    def drop_duplicate_timestamps(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, int]:
        """Remove rows with duplicate index values (keeping the last)."""
        duplicates = df.index.duplicated(keep="last")
        dup_count = duplicates.sum()
        if dup_count > 0:
            df = df[~duplicates]
        return df, int(dup_count)

    def ensure_column_order(self, df: pd.DataFrame) -> pd.DataFrame:
        """Reorder columns to match REQUIRED_COLUMNS where possible."""
        existing_required = [col for col in REQUIRED_COLUMNS if col in df.columns]
        other_cols = [col for col in df.columns if col not in REQUIRED_COLUMNS]
        return df[existing_required + other_cols]

    def fill_missing_volume_column(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fill missing volume values with 0.0."""
        if "volume" in df.columns:
            df["volume"] = df["volume"].fillna(0.0)
        return df
