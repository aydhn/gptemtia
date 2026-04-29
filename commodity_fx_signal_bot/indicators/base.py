from abc import ABC, abstractmethod

import pandas as pd

from indicators.indicator_result import IndicatorResult


class BaseIndicator(ABC):
    name: str = "base"
    category: str = "base"
    required_columns: tuple[str, ...] = ()
    warmup_period: int = 0

    def validate_input(self, df: pd.DataFrame) -> None:
        """Validates that the input DataFrame has the required columns."""
        ensure_required_columns(df, self.required_columns)

    @abstractmethod
    def calculate(self, df: pd.DataFrame, **params) -> IndicatorResult:
        """Calculates the indicator and returns an IndicatorResult."""


def ensure_required_columns(
    df: pd.DataFrame, required_columns: tuple[str, ...]
) -> None:
    """Helper to check if all required columns exist in the DataFrame."""
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns for indicator: {missing}")


def calculate_nan_ratio(df: pd.DataFrame) -> float:
    """Helper to calculate the ratio of NaN values in a DataFrame."""
    if df.empty:
        return 0.0
    return float(df.isna().sum().sum() / df.size)


def safe_series_name(base_name: str, params: dict) -> str:
    """Helper to generate a safe column name from a base name and parameters."""
    if not params:
        return base_name
    param_str = "_".join(str(v) for v in params.values())
    return f"{base_name}_{param_str}"
