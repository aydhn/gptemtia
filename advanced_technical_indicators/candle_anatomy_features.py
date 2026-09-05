from typing import Tuple, Dict, Any
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


def add_candle_body_size(
    df: pd.DataFrame,
    open_field: str = "open",
    close_field: str = "close",
    output_field: str = "candle_body_size",
) -> pd.DataFrame:
    _validate_required(df, [open_field, close_field])
    _validate_output_field(output_field)
    out = df.copy()
    out[output_field] = np.abs(out[close_field] - out[open_field]).astype(float)
    return out


def add_candle_body_pct(
    df: pd.DataFrame,
    open_field: str = "open",
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    output_field: str = "candle_body_pct",
) -> pd.DataFrame:
    _validate_required(df, [open_field, high_field, low_field, close_field])
    _validate_output_field(output_field)
    out = df.copy()
    body = np.abs(out[close_field] - out[open_field])
    hl_range = (out[high_field] - out[low_field]).replace(0, np.nan)
    out[output_field] = (body / hl_range).astype(float)
    return out


def add_upper_wick_size(
    df: pd.DataFrame,
    open_field: str = "open",
    high_field: str = "high",
    close_field: str = "close",
    output_field: str = "upper_wick_size",
) -> pd.DataFrame:
    _validate_required(df, [open_field, high_field, close_field])
    _validate_output_field(output_field)
    out = df.copy()
    candle_max = np.maximum(out[open_field], out[close_field])
    out[output_field] = (out[high_field] - candle_max).astype(float)
    return out


def add_lower_wick_size(
    df: pd.DataFrame,
    open_field: str = "open",
    low_field: str = "low",
    close_field: str = "close",
    output_field: str = "lower_wick_size",
) -> pd.DataFrame:
    _validate_required(df, [open_field, low_field, close_field])
    _validate_output_field(output_field)
    out = df.copy()
    candle_min = np.minimum(out[open_field], out[close_field])
    out[output_field] = (candle_min - out[low_field]).astype(float)
    return out


def add_wick_balance(
    df: pd.DataFrame,
    open_field: str = "open",
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    output_field: str = "wick_balance",
) -> pd.DataFrame:
    _validate_required(df, [open_field, high_field, low_field, close_field])
    _validate_output_field(output_field)
    out = df.copy()
    candle_max = np.maximum(out[open_field], out[close_field])
    candle_min = np.minimum(out[open_field], out[close_field])
    upper_wick = out[high_field] - candle_max
    lower_wick = candle_min - out[low_field]
    hl_range = (out[high_field] - out[low_field]).replace(0, np.nan)
    out[output_field] = ((upper_wick - lower_wick) / hl_range).astype(float)
    return out


def build_candle_anatomy_feature_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"indicator_name": "candle_body_size", "output_field": "candle_body_size"},
        {"indicator_name": "candle_body_pct", "output_field": "candle_body_pct"},
        {"indicator_name": "upper_wick_size", "output_field": "upper_wick_size"},
        {"indicator_name": "lower_wick_size", "output_field": "lower_wick_size"},
        {"indicator_name": "wick_balance", "output_field": "wick_balance"},
    ]
    df = pd.DataFrame(rows)
    df["family"] = "family_candle_anatomy"
    df["non_signal"] = True
    summary = {
        "family": "family_candle_anatomy",
        "total_indicators": len(df),
        "status": "READY",
        "non_signal": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
