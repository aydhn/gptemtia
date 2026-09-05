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


def add_momentum(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 10,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"momentum_{window}"
    _validate_output_field(col)
    out = df.copy()
    out[col] = (out[field] - out[field].shift(window)).astype(float)
    return out


def add_roc(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 10,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"roc_{window}"
    _validate_output_field(col)
    out = df.copy()
    shifted = out[field].shift(window).replace(0, np.nan)
    out[col] = (((out[field] - shifted) / shifted) * 100.0).astype(float)
    return out


def add_rsi(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 14,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"rsi_{window}"
    _validate_output_field(col)
    out = df.copy()
    delta = out[field].diff()
    gain = np.where(delta > 0, delta, 0.0)
    loss = np.where(delta < 0, -delta, 0.0)

    avg_gain = pd.Series(gain, index=out.index).ewm(alpha=1.0 / window, adjust=False).mean()
    avg_loss = pd.Series(loss, index=out.index).ewm(alpha=1.0 / window, adjust=False).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)
    rsi_series = 100.0 - (100.0 / (1.0 + rs))
    out[col] = rsi_series.astype(float)
    return out


def add_cmo(
    df: pd.DataFrame,
    field: str = "close",
    window: int = 14,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"cmo_{window}"
    _validate_output_field(col)
    out = df.copy()
    delta = out[field].diff()
    gain = np.where(delta > 0, delta, 0.0)
    loss = np.where(delta < 0, -delta, 0.0)

    sum_gain = pd.Series(gain, index=out.index).rolling(window=window).sum()
    sum_loss = pd.Series(loss, index=out.index).rolling(window=window).sum()
    denom = (sum_gain + sum_loss).replace(0, np.nan)
    out[col] = (100.0 * (sum_gain - sum_loss) / denom).astype(float)
    return out


def add_tsi_placeholder(
    df: pd.DataFrame,
    field: str = "close",
    long_window: int = 25,
    short_window: int = 13,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [field])
    col = output_field or f"tsi_{long_window}_{short_window}"
    _validate_output_field(col)
    out = df.copy()
    diff = out[field].diff()
    smooth1 = diff.ewm(span=long_window, adjust=False).mean()
    smooth2 = smooth1.ewm(span=short_window, adjust=False).mean()

    abs_diff = np.abs(diff)
    abs_smooth1 = abs_diff.ewm(span=long_window, adjust=False).mean()
    abs_smooth2 = abs_smooth1.ewm(span=short_window, adjust=False).mean()

    denom = abs_smooth2.replace(0, np.nan)
    out[col] = (100.0 * (smooth2 / denom)).astype(float)
    return out


def build_momentum_indicator_expansion_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"indicator_name": "momentum", "output_pattern": "momentum_{window}", "default_window": 10},
        {"indicator_name": "roc", "output_pattern": "roc_{window}", "default_window": 10},
        {"indicator_name": "rsi", "output_pattern": "rsi_{window}", "default_window": 14},
        {"indicator_name": "cmo", "output_pattern": "cmo_{window}", "default_window": 14},
        {"indicator_name": "tsi", "output_pattern": "tsi_{long}_{short}", "default_window": 25},
    ]
    df = pd.DataFrame(rows)
    df["family"] = "family_momentum"
    df["non_signal"] = True
    summary = {
        "family": "family_momentum",
        "total_indicators": len(df),
        "status": "READY",
        "non_signal": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
