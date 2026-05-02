"""
Base classes for regime detection modules.
"""

from abc import ABC, abstractmethod
import pandas as pd


class BaseRegimeDetector(ABC):
    """Abstract base class for all regime detectors."""

    name: str = "base_regime"
    required_columns: tuple[str, ...] = ()

    def validate_input(self, df: pd.DataFrame) -> dict:
        """
        Check if required columns exist in the dataframe.
        Returns a dictionary with validation results and warnings.
        """
        missing = [col for col in self.required_columns if col not in df.columns]

        return {
            "valid": len(missing) == 0,
            "missing_columns": missing,
            "warnings": (
                [f"Missing required column: {m}" for m in missing] if missing else []
            ),
        }

    @abstractmethod
    def detect(self, df: pd.DataFrame, **kwargs) -> tuple[pd.DataFrame, dict]:
        """
        Run the regime detection logic.
        Returns a dataframe with regime features and a summary dictionary.
        """
        pass

    def safe_column_exists(self, df: pd.DataFrame, column: str) -> bool:
        """Safely check if a column exists and is not entirely NaN."""
        if column not in df.columns:
            return False
        if df[column].isna().all():
            return False
        return True
