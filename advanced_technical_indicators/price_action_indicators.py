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


def add_high_low_range(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    output_field: str = "high_low_range",
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field])
    _validate_output_field(output_field)
    out = df.copy()
    out[output_field] = (out[high_field] - out[low_field]).astype(float)
    return out


def add_close_open_range(
    df: pd.DataFrame,
    close_field: str = "close",
    open_field: str = "open",
    output_field: str = "close_open_range",
) -> pd.DataFrame:
    _validate_required(df, [close_field, open_field])
    _validate_output_field(output_field)
    out = df.copy()
    out[output_field] = (out[close_field] - out[open_field]).astype(float)
    return out


def add_range_pct(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    output_field: str = "range_pct",
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    _validate_output_field(output_field)
    out = df.copy()
    denom = out[close_field].replace(0, np.nan)
    out[output_field] = ((out[high_field] - out[low_field]) / denom).astype(float)
    return out


def add_gap_from_previous_close(
    df: pd.DataFrame,
    open_field: str = "open",
    close_field: str = "close",
    output_field: str = "gap_from_prev_close",
) -> pd.DataFrame:
    _validate_required(df, [open_field, close_field])
    _validate_output_field(output_field)
    out = df.copy()
    prev_close = out[close_field].shift(1)
    out[output_field] = (out[open_field] - prev_close).astype(float)
    return out


def add_close_location_value(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    output_field: str = "close_location_value",
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    _validate_output_field(output_field)
    out = df.copy()
    hl_range = out[high_field] - out[low_field]
    denom = hl_range.replace(0, np.nan)
    out[output_field] = (((out[close_field] - out[low_field]) - (out[high_field] - out[close_field])) / denom).astype(float)
    return out


def build_price_action_indicator_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"indicator_name": "high_low_range", "output_field": "high_low_range", "required_fields": ["high", "low"]},
        {"indicator_name": "close_open_range", "output_field": "close_open_range", "required_fields": ["close", "open"]},
        {"indicator_name": "range_pct", "output_field": "range_pct", "required_fields": ["high", "low", "close"]},
        {"indicator_name": "gap_from_prev_close", "output_field": "gap_from_prev_close", "required_fields": ["open", "close"]},
        {"indicator_name": "close_location_value", "output_field": "close_location_value", "required_fields": ["high", "low", "close"]},
    ]
    df = pd.DataFrame(rows)
    df["family"] = "family_price_action"
    df["non_signal"] = True
    summary = {
        "family": "family_price_action",
        "total_indicators": len(df),
        "status": "READY",
        "non_signal": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
