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


def add_bollinger_bands(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    num_std: float = 2.0,
    prefix: str = "bb",
) -> pd.DataFrame:
    _validate_required(df, [field])
    upper_col = f"{prefix}_upper_{window}"
    mid_col = f"{prefix}_mid_{window}"
    lower_col = f"{prefix}_lower_{window}"
    for col in [upper_col, mid_col, lower_col]:
        _validate_output_field(col)

    out = df.copy()
    mid = out[field].rolling(window=window).mean()
    std = out[field].rolling(window=window).std()
    upper = mid + (num_std * std)
    lower = mid - (num_std * std)

    out[upper_col] = upper.astype(float)
    out[mid_col] = mid.astype(float)
    out[lower_col] = lower.astype(float)
    return out


def add_bollinger_bandwidth(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    num_std: float = 2.0,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"bb_bandwidth_{window}"
    _validate_output_field(col)
    out = df.copy()
    mid = out[field].rolling(window=window).mean()
    std = out[field].rolling(window=window).std()
    upper = mid + (num_std * std)
    lower = mid - (num_std * std)
    out[col] = ((upper - lower) / mid.replace(0, np.nan)).astype(float)
    return out


def add_bollinger_percent_b(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 20,
    num_std: float = 2.0,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"bb_percent_b_{window}"
    _validate_output_field(col)
    out = df.copy()
    mid = out[field].rolling(window=window).mean()
    std = out[field].rolling(window=window).std()
    upper = mid + (num_std * std)
    lower = mid - (num_std * std)
    denom = (upper - lower).replace(0, np.nan)
    out[col] = ((out[field] - lower) / denom).astype(float)
    return out


def add_keltner_channel_placeholder(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    window: int = 20,
    atr_window: int = 10,
    prefix: str = "keltner",
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    upper_col = f"{prefix}_upper_{window}"
    mid_col = f"{prefix}_mid_{window}"
    lower_col = f"{prefix}_lower_{window}"
    for col in [upper_col, mid_col, lower_col]:
        _validate_output_field(col)

    out = df.copy()
    mid = out[close_field].ewm(span=window, adjust=False).mean()

    prev_close = out[close_field].shift(1)
    hl = out[high_field] - out[low_field]
    hpc = np.abs(out[high_field] - prev_close)
    lpc = np.abs(out[low_field] - prev_close)
    tr = np.maximum(hl, np.maximum(hpc, lpc))
    atr = pd.Series(tr, index=out.index).rolling(window=atr_window).mean()

    upper = mid + (2.0 * atr)
    lower = mid - (2.0 * atr)

    out[upper_col] = upper.astype(float)
    out[mid_col] = mid.astype(float)
    out[lower_col] = lower.astype(float)
    return out


def add_donchian_position(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    col = output_field or f"donchian_position_{window}"
    _validate_output_field(col)
    out = df.copy()
    upper = out[high_field].rolling(window=window).max()
    lower = out[low_field].rolling(window=window).min()
    denom = (upper - lower).replace(0, np.nan)
    out[col] = ((out[close_field] - lower) / denom).astype(float)
    return out


def build_channel_indicator_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"indicator_name": "bollinger_bands", "output_pattern": "bb_upper, bb_mid, bb_lower", "default_window": 20},
        {"indicator_name": "bollinger_bandwidth", "output_pattern": "bb_bandwidth_{window}", "default_window": 20},
        {"indicator_name": "bollinger_percent_b", "output_pattern": "bb_percent_b_{window}", "default_window": 20},
        {"indicator_name": "keltner_channel", "output_pattern": "keltner_upper, keltner_mid, keltner_lower", "default_window": 20},
        {"indicator_name": "donchian_position", "output_pattern": "donchian_position_{window}", "default_window": 20},
    ]
    df = pd.DataFrame(rows)
    df["family"] = "family_channel"
    df["non_signal"] = True
    summary = {
        "family": "family_channel",
        "total_indicators": len(df),
        "status": "READY",
        "non_signal": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
