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


def add_simple_return(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 1,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"simple_return_{window}"
    _validate_output_field(col)
    out = df.copy()
    shifted = out[field].shift(window)
    out[col] = ((out[field] / shifted) - 1.0).astype(float)
    return out


def add_log_return(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 1,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"log_return_{window}"
    _validate_output_field(col)
    out = df.copy()
    shifted = out[field].shift(window)
    ratio = (out[field] / shifted).replace(0, np.nan)
    out[col] = np.log(ratio).astype(float)
    return out


def add_cumulative_return(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"cumulative_return_{window}"
    _validate_output_field(col)
    out = df.copy()
    shifted = out[field].shift(window)
    out[col] = ((out[field] / shifted) - 1.0).astype(float)
    return out


def add_rolling_return_sum(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"rolling_return_sum_{window}"
    _validate_output_field(col)
    out = df.copy()
    s_ret = (out[field] / out[field].shift(1)) - 1.0
    out[col] = s_ret.rolling(window=window).sum().astype(float)
    return out


def add_return_volatility_ratio(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"return_vol_ratio_{window}"
    _validate_output_field(col)
    out = df.copy()
    s_ret = (out[field] / out[field].shift(1)) - 1.0
    r_mean = s_ret.rolling(window=window).mean()
    r_std = s_ret.rolling(window=window).std().replace(0, np.nan)
    out[col] = (r_mean / r_std).astype(float)
    return out


def build_return_indicator_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"indicator_name": "simple_return", "output_pattern": "simple_return_{window}", "default_window": 1},
        {"indicator_name": "log_return", "output_pattern": "log_return_{window}", "default_window": 1},
        {"indicator_name": "cumulative_return", "output_pattern": "cumulative_return_{window}", "default_window": 20},
        {"indicator_name": "rolling_return_sum", "output_pattern": "rolling_return_sum_{window}", "default_window": 20},
        {"indicator_name": "return_volatility_ratio", "output_pattern": "return_vol_ratio_{window}", "default_window": 20},
    ]
    df = pd.DataFrame(rows)
    df["family"] = "family_returns"
    df["non_signal"] = True
    summary = {
        "family": "family_returns",
        "total_indicators": len(df),
        "status": "READY",
        "non_signal": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
