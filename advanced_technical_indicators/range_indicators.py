from typing import Tuple, Dict, Any, Optional
import numpy as np
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile

FORBIDDEN_COLUMNS = {
    "signal", "buy", "sell", "long", "short", "position",
    "target", "label", "prediction", "recommendation",
    "future_return", "forward_return", "next_return"
}


def _validate_output_field(col: str) -> None:
    if col.lower() in FORBIDDEN_COLUMNS:
        raise ValueError(f"Forbidden column name '{col}' detected. Non-signal indicator only.")


def _validate_required(df: pd.DataFrame, fields: list[str]) -> None:
    for f in fields:
        if f not in df.columns:
            raise ValueError(f"Required field '{f}' is missing from DataFrame.")


def add_rolling_high_low_range(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field])
    col = output_field or f"rolling_hl_range_{window}"
    _validate_output_field(col)
    out = df.copy()
    r_high = out[high_field].rolling(window=window).max()
    r_low = out[low_field].rolling(window=window).min()
    out[col] = (r_high - r_low).astype(float)
    return out


def add_rolling_range_pct(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    col = output_field or f"rolling_range_pct_{window}"
    _validate_output_field(col)
    out = df.copy()
    r_high = out[high_field].rolling(window=window).max()
    r_low = out[low_field].rolling(window=window).min()
    denom = out[close_field].replace(0, np.nan)
    out[col] = ((r_high - r_low) / denom).astype(float)
    return out


def add_average_range(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field])
    col = output_field or f"average_range_{window}"
    _validate_output_field(col)
    out = df.copy()
    bar_range = out[high_field] - out[low_field]
    out[col] = bar_range.rolling(window=window).mean().astype(float)
    return out


def add_range_zscore(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field])
    col = output_field or f"range_zscore_{window}"
    _validate_output_field(col)
    out = df.copy()
    bar_range = out[high_field] - out[low_field]
    r_mean = bar_range.rolling(window=window).mean()
    r_std = bar_range.rolling(window=window).std().replace(0, np.nan)
    out[col] = ((bar_range - r_mean) / r_std).astype(float)
    return out


def build_range_indicator_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"indicator_name": "rolling_high_low_range", "output_pattern": "rolling_hl_range_{window}", "default_window": 20},
        {"indicator_name": "rolling_range_pct", "output_pattern": "rolling_range_pct_{window}", "default_window": 20},
        {"indicator_name": "average_range", "output_pattern": "average_range_{window}", "default_window": 20},
        {"indicator_name": "range_zscore", "output_pattern": "range_zscore_{window}", "default_window": 20},
    ]
    df = pd.DataFrame(rows)
    df["family"] = "family_range"
    df["non_signal"] = True
    summary = {
        "family": "family_range",
        "total_indicators": len(df),
        "status": "READY",
        "non_signal": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
