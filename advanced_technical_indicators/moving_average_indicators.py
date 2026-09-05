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


def add_sma(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"sma_{window}"
    _validate_output_field(col)
    out = df.copy()
    out[col] = out[field].rolling(window=window).mean().astype(float)
    return out


def add_ema(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"ema_{window}"
    _validate_output_field(col)
    out = df.copy()
    out[col] = out[field].ewm(span=window, adjust=False).mean().astype(float)
    return out


def add_wma(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"wma_{window}"
    _validate_output_field(col)
    out = df.copy()
    weights = np.arange(1, window + 1)
    sum_weights = weights.sum()

    def _calc_wma(s):
        return np.dot(s, weights) / sum_weights

    out[col] = out[field].rolling(window=window).apply(_calc_wma, raw=True).astype(float)
    return out


def add_dema(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"dema_{window}"
    _validate_output_field(col)
    out = df.copy()
    ema1 = out[field].ewm(span=window, adjust=False).mean()
    ema2 = ema1.ewm(span=window, adjust=False).mean()
    out[col] = (2 * ema1 - ema2).astype(float)
    return out


def add_tema(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"tema_{window}"
    _validate_output_field(col)
    out = df.copy()
    ema1 = out[field].ewm(span=window, adjust=False).mean()
    ema2 = ema1.ewm(span=window, adjust=False).mean()
    ema3 = ema2.ewm(span=window, adjust=False).mean()
    out[col] = (3 * ema1 - 3 * ema2 + ema3).astype(float)
    return out


def add_moving_average_distance(
    df: pd.DataFrame,
    field: str = "close",
    ma_field: Optional[str] = None,
    window: int = 20,
    ma_type: str = "sma",
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"ma_distance_{window}"
    _validate_output_field(col)
    out = df.copy()
    if ma_field and ma_field in out.columns:
        ma_series = out[ma_field]
    else:
        if ma_type.lower() == "ema":
            ma_series = out[field].ewm(span=window, adjust=False).mean()
        else:
            ma_series = out[field].rolling(window=window).mean()
    denom = ma_series.replace(0, np.nan)
    out[col] = ((out[field] - ma_series) / denom).astype(float)
    return out


def build_moving_average_indicator_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"indicator_name": "sma", "output_pattern": "sma_{window}", "default_window": 20},
        {"indicator_name": "ema", "output_pattern": "ema_{window}", "default_window": 20},
        {"indicator_name": "wma", "output_pattern": "wma_{window}", "default_window": 20},
        {"indicator_name": "dema", "output_pattern": "dema_{window}", "default_window": 20},
        {"indicator_name": "tema", "output_pattern": "tema_{window}", "default_window": 20},
        {"indicator_name": "ma_distance", "output_pattern": "ma_distance_{window}", "default_window": 20},
    ]
    df = pd.DataFrame(rows)
    df["family"] = "family_moving_average"
    df["non_signal"] = True
    summary = {
        "family": "family_moving_average",
        "total_indicators": len(df),
        "status": "READY",
        "non_signal": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
