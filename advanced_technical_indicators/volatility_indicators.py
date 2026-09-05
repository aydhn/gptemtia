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


def add_true_range(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    output_field: str = "true_range",
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    _validate_output_field(output_field)
    out = df.copy()
    prev_close = out[close_field].shift(1)
    hl = out[high_field] - out[low_field]
    hpc = np.abs(out[high_field] - prev_close)
    lpc = np.abs(out[low_field] - prev_close)
    out[output_field] = np.maximum(hl, np.maximum(hpc, lpc)).astype(float)
    return out


def add_atr(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    window: int = 14,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    col = output_field or f"atr_{window}"
    _validate_output_field(col)
    out = df.copy()
    prev_close = out[close_field].shift(1)
    hl = out[high_field] - out[low_field]
    hpc = np.abs(out[high_field] - prev_close)
    lpc = np.abs(out[low_field] - prev_close)
    tr = np.maximum(hl, np.maximum(hpc, lpc))
    out[col] = pd.Series(tr, index=out.index).rolling(window=window).mean().astype(float)
    return out


def add_rolling_std(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"rolling_std_{window}"
    _validate_output_field(col)
    out = df.copy()
    out[col] = out[field].rolling(window=window).std().astype(float)
    return out


def add_realized_volatility(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"realized_vol_{window}"
    _validate_output_field(col)
    out = df.copy()
    log_ret = np.log((out[field] / out[field].shift(1)).replace(0, np.nan))
    out[col] = (log_ret.rolling(window=window).std() * np.sqrt(252.0)).astype(float)
    return out


def add_parkinson_volatility(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field])
    col = output_field or f"parkinson_vol_{window}"
    _validate_output_field(col)
    out = df.copy()
    ratio = (out[high_field] / out[low_field].replace(0, np.nan)).replace(0, np.nan)
    log_hl = np.log(ratio)
    factor = 1.0 / (4.0 * np.log(2.0))
    rolling_sum = (log_hl ** 2).rolling(window=window).mean()
    out[col] = (np.sqrt(factor * rolling_sum) * np.sqrt(252.0)).astype(float)
    return out


def add_garman_klass_volatility_placeholder(
    df: pd.DataFrame,
    open_field: str = "open",
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [open_field, high_field, low_field, close_field])
    col = output_field or f"garman_klass_vol_{window}"
    _validate_output_field(col)
    out = df.copy()
    log_hl = np.log((out[high_field] / out[low_field].replace(0, np.nan)).replace(0, np.nan))
    log_co = np.log((out[close_field] / out[open_field].replace(0, np.nan)).replace(0, np.nan))
    term1 = 0.5 * (log_hl ** 2)
    term2 = (2.0 * np.log(2.0) - 1.0) * (log_co ** 2)
    gk_var = term1 - term2
    out[col] = (np.sqrt(np.maximum(0, gk_var.rolling(window=window).mean())) * np.sqrt(252.0)).astype(float)
    return out


def build_volatility_indicator_expansion_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"indicator_name": "true_range", "output_pattern": "true_range", "default_window": 1},
        {"indicator_name": "atr", "output_pattern": "atr_{window}", "default_window": 14},
        {"indicator_name": "rolling_std", "output_pattern": "rolling_std_{window}", "default_window": 20},
        {"indicator_name": "realized_volatility", "output_pattern": "realized_vol_{window}", "default_window": 20},
        {"indicator_name": "parkinson_volatility", "output_pattern": "parkinson_vol_{window}", "default_window": 20},
        {"indicator_name": "garman_klass_volatility", "output_pattern": "garman_klass_vol_{window}", "default_window": 20},
    ]
    df = pd.DataFrame(rows)
    df["family"] = "family_volatility"
    df["non_signal"] = True
    summary = {
        "family": "family_volatility",
        "total_indicators": len(df),
        "status": "READY",
        "non_signal": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
