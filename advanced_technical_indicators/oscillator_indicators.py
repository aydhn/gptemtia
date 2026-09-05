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


def add_stochastic_oscillator(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    k_window: int = 14,
    d_window: int = 3,
    prefix: str = "stoch",
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    k_col = f"{prefix}_k_{k_window}"
    d_col = f"{prefix}_d_{k_window}_{d_window}"
    for col in [k_col, d_col]:
        _validate_output_field(col)

    out = df.copy()
    lowest_low = out[low_field].rolling(window=k_window).min()
    highest_high = out[high_field].rolling(window=k_window).max()
    denom = (highest_high - lowest_low).replace(0, np.nan)
    stoch_k = 100.0 * (out[close_field] - lowest_low) / denom
    stoch_d = stoch_k.rolling(window=d_window).mean()

    out[k_col] = stoch_k.astype(float)
    out[d_col] = stoch_d.astype(float)
    return out


def add_williams_r(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    window: int = 14,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    col = output_field or f"williams_r_{window}"
    _validate_output_field(col)
    out = df.copy()
    highest_high = out[high_field].rolling(window=window).max()
    lowest_low = out[low_field].rolling(window=window).min()
    denom = (highest_high - lowest_low).replace(0, np.nan)
    out[col] = (-100.0 * (highest_high - out[close_field]) / denom).astype(float)
    return out


def add_cci(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    window: int = 20,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    col = output_field or f"cci_{window}"
    _validate_output_field(col)
    out = df.copy()
    tp = (out[high_field] + out[low_field] + out[close_field]) / 3.0
    sma_tp = tp.rolling(window=window).mean()

    def _mean_dev(s):
        return np.mean(np.abs(s - np.mean(s)))

    md = tp.rolling(window=window).apply(_mean_dev, raw=True).replace(0, np.nan)
    out[col] = ((tp - sma_tp) / (0.015 * md)).astype(float)
    return out


def add_ultimate_oscillator_placeholder(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    prefix: str = "ultimate_osc",
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    col = prefix
    _validate_output_field(col)
    out = df.copy()
    prev_close = out[close_field].shift(1)
    true_low = np.minimum(out[low_field], prev_close)
    true_high = np.maximum(out[high_field], prev_close)

    bp = out[close_field] - true_low
    tr = true_high - true_low

    avg7 = bp.rolling(7).sum() / tr.rolling(7).sum().replace(0, np.nan)
    avg14 = bp.rolling(14).sum() / tr.rolling(14).sum().replace(0, np.nan)
    avg28 = bp.rolling(28).sum() / tr.rolling(28).sum().replace(0, np.nan)

    out[col] = (100.0 * (4 * avg7 + 2 * avg14 + avg28) / 7.0).astype(float)
    return out


def add_mfi_placeholder(
    df: pd.DataFrame,
    high_field: str = "high",
    low_field: str = "low",
    close_field: str = "close",
    volume_field: str = "volume",
    window: int = 14,
    output_field: Optional[str] = None,
) -> pd.DataFrame:
    _validate_required(df, [high_field, low_field, close_field])
    col = output_field or f"mfi_{window}"
    _validate_output_field(col)
    out = df.copy()

    if volume_field not in out.columns:
        # Graceful warning / NaN placeholder if volume not available
        out[col] = np.nan
        return out

    tp = (out[high_field] + out[low_field] + out[close_field]) / 3.0
    raw_money_flow = tp * out[volume_field]
    tp_diff = tp.diff()

    pos_mf = np.where(tp_diff > 0, raw_money_flow, 0.0)
    neg_mf = np.where(tp_diff < 0, raw_money_flow, 0.0)

    pos_sum = pd.Series(pos_mf, index=out.index).rolling(window=window).sum()
    neg_sum = pd.Series(neg_mf, index=out.index).rolling(window=window).sum()

    mr = pos_sum / neg_sum.replace(0, np.nan)
    mfi = 100.0 - (100.0 / (1.0 + mr))
    out[col] = mfi.astype(float)
    return out


def build_oscillator_indicator_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"indicator_name": "stochastic", "output_pattern": "stoch_k, stoch_d", "parameters": {"k": 14, "d": 3}},
        {"indicator_name": "williams_r", "output_pattern": "williams_r_{window}", "parameters": {"window": 14}},
        {"indicator_name": "cci", "output_pattern": "cci_{window}", "parameters": {"window": 20}},
        {"indicator_name": "ultimate_oscillator", "output_pattern": "ultimate_osc", "parameters": {}},
        {"indicator_name": "mfi", "output_pattern": "mfi_{window}", "parameters": {"window": 14}},
    ]
    df = pd.DataFrame(rows)
    df["family"] = "family_oscillator"
    df["non_signal"] = True
    summary = {
        "family": "family_oscillator",
        "total_indicators": len(df),
        "status": "READY",
        "non_signal": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
