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


def add_rolling_zscore(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"rolling_zscore_{window}"
    _validate_output_field(col)
    out = df.copy()
    mean = out[field].rolling(window=window).mean()
    std = out[field].rolling(window=window).std().replace(0, np.nan)
    out[col] = ((out[field] - mean) / std).astype(float)
    return out


def add_distance_to_sma(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"dist_to_sma_{window}"
    _validate_output_field(col)
    out = df.copy()
    sma = out[field].rolling(window=window).mean().replace(0, np.nan)
    out[col] = ((out[field] - sma) / sma).astype(float)
    return out


def add_distance_to_ema(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"dist_to_ema_{window}"
    _validate_output_field(col)
    out = df.copy()
    ema = out[field].ewm(span=window, adjust=False).mean().replace(0, np.nan)
    out[col] = ((out[field] - ema) / ema).astype(float)
    return out


def add_rolling_percentile_rank_placeholder(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 100,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"rolling_percentile_rank_{window}"
    _validate_output_field(col)
    out = df.copy()

    def _pct_rank(s):
        last_val = s[-1]
        return float(np.sum(s <= last_val) / len(s) * 100.0)

    out[col] = out[field].rolling(window=window).apply(_pct_rank, raw=True).astype(float)
    return out


def add_rolling_deviation_ratio(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"rolling_deviation_ratio_{window}"
    _validate_output_field(col)
    out = df.copy()
    mean = out[field].rolling(window=window).mean()
    std = out[field].rolling(window=window).std().replace(0, np.nan)
    out[col] = (np.abs(out[field] - mean) / std).astype(float)
    return out


def build_mean_reversion_indicator_expansion_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"indicator_name": "rolling_zscore", "output_pattern": "rolling_zscore_{window}", "default_window": 20},
        {"indicator_name": "distance_to_sma", "output_pattern": "dist_to_sma_{window}", "default_window": 20},
        {"indicator_name": "distance_to_ema", "output_pattern": "dist_to_ema_{window}", "default_window": 20},
        {"indicator_name": "rolling_percentile_rank", "output_pattern": "rolling_percentile_rank_{window}", "default_window": 100},
        {"indicator_name": "rolling_deviation_ratio", "output_pattern": "rolling_deviation_ratio_{window}", "default_window": 20},
    ]
    df = pd.DataFrame(rows)
    df["family"] = "family_mean_reversion"
    df["non_signal"] = True
    summary = {
        "family": "family_mean_reversion",
        "total_indicators": len(df),
        "status": "READY",
        "non_signal": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
