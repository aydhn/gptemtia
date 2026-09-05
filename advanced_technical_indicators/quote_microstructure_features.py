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


def add_quote_mid(
    df: pd.DataFrame,
    bid_field: str = "bid",
    ask_field: str = "ask",
    output_field: str = "quote_mid",
) -> pd.DataFrame:
    _validate_required(df, [bid_field, ask_field])
    _validate_output_field(output_field)
    out = df.copy()
    out[output_field] = ((out[bid_field] + out[ask_field]) / 2.0).astype(float)
    return out


def add_quote_spread(
    df: pd.DataFrame,
    bid_field: str = "bid",
    ask_field: str = "ask",
    output_field: str = "quote_spread",
) -> pd.DataFrame:
    _validate_required(df, [bid_field, ask_field])
    _validate_output_field(output_field)
    out = df.copy()
    out[output_field] = (out[ask_field] - out[bid_field]).astype(float)
    return out


def add_quote_spread_pct(
    df: pd.DataFrame,
    bid_field: str = "bid",
    ask_field: str = "ask",
    output_field: str = "quote_spread_pct",
) -> pd.DataFrame:
    _validate_required(df, [bid_field, ask_field])
    _validate_output_field(output_field)
    out = df.copy()
    mid = ((out[bid_field] + out[ask_field]) / 2.0).replace(0, np.nan)
    out[output_field] = ((out[ask_field] - out[bid_field]) / mid).astype(float)
    return out


def add_bid_ask_ratio_placeholder(
    df: pd.DataFrame,
    bid_field: str = "bid",
    ask_field: str = "ask",
    output_field: str = "bid_ask_ratio_placeholder",
) -> pd.DataFrame:
    _validate_required(df, [bid_field, ask_field])
    _validate_output_field(output_field)
    out = df.copy()
    ask_denom = out[ask_field].replace(0, np.nan)
    out[output_field] = (out[bid_field] / ask_denom).astype(float)
    return out


def add_quote_staleness_placeholder(
    df: pd.DataFrame,
    timestamp_field: str = "timestamp",
    output_field: str = "quote_staleness_placeholder",
) -> pd.DataFrame:
    _validate_required(df, [timestamp_field])
    _validate_output_field(output_field)
    out = df.copy()
    ts = pd.to_datetime(out[timestamp_field])
    diff_sec = ts.diff().dt.total_seconds().fillna(0.0)
    out[output_field] = diff_sec.astype(float)
    return out


def build_quote_microstructure_feature_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"indicator_name": "quote_mid", "output_field": "quote_mid"},
        {"indicator_name": "quote_spread", "output_field": "quote_spread"},
        {"indicator_name": "quote_spread_pct", "output_field": "quote_spread_pct"},
        {"indicator_name": "bid_ask_ratio_placeholder", "output_field": "bid_ask_ratio_placeholder"},
        {"indicator_name": "quote_staleness_placeholder", "output_field": "quote_staleness_placeholder"},
    ]
    df = pd.DataFrame(rows)
    df["family"] = "family_quote_microstructure"
    df["non_signal"] = True
    summary = {
        "family": "family_quote_microstructure",
        "total_indicators": len(df),
        "status": "READY",
        "non_signal": True,
        "current_phase": profile.current_phase,
    }
    return df, summary
