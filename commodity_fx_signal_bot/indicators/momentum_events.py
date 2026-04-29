import re
from dataclasses import dataclass
from typing import Optional, Tuple

import pandas as pd


@dataclass
class MomentumEventConfig:
    rsi_overbought: float = 70.0
    rsi_oversold: float = 30.0
    stochastic_overbought: float = 80.0
    stochastic_oversold: float = 20.0
    cci_upper: float = 100.0
    cci_lower: float = -100.0
    roc_neutral: float = 0.0
    min_event_strength: float = 0.0


def _get_columns_by_prefix(df: pd.DataFrame, prefix: str) -> list[str]:
    return [c for c in df.columns if c.startswith(prefix)]


def detect_rsi_zone_events(
    features: pd.DataFrame, config: Optional[MomentumEventConfig] = None
) -> pd.DataFrame:
    config = config or MomentumEventConfig()
    events = pd.DataFrame(index=features.index)
    rsi_cols = _get_columns_by_prefix(features, "rsi_")
    for col in rsi_cols:
        window_match = re.search(r"rsi_(\d+)", col)
        if not window_match:
            continue
        window = window_match.group(1)
        events[f"event_rsi_{window}_oversold"] = (
            features[col] < config.rsi_oversold
        ).astype(int)
        events[f"event_rsi_{window}_overbought"] = (
            features[col] > config.rsi_overbought
        ).astype(int)
    return events


def detect_rsi_crossback_events(
    features: pd.DataFrame, config: Optional[MomentumEventConfig] = None
) -> pd.DataFrame:
    config = config or MomentumEventConfig()
    events = pd.DataFrame(index=features.index)
    rsi_cols = _get_columns_by_prefix(features, "rsi_")
    for col in rsi_cols:
        window_match = re.search(r"rsi_(\d+)", col)
        if not window_match:
            continue
        window = window_match.group(1)
        rsi_series = features[col]
        prev_rsi = rsi_series.shift(1)
        events[f"event_rsi_{window}_recovery_cross"] = (
            (prev_rsi <= config.rsi_oversold) & (rsi_series > config.rsi_oversold)
        ).astype(int)
        events[f"event_rsi_{window}_bearish_crossback"] = (
            (prev_rsi >= config.rsi_overbought) & (rsi_series < config.rsi_overbought)
        ).astype(int)
    return events


def detect_stochastic_cross_events(
    features: pd.DataFrame, config: Optional[MomentumEventConfig] = None
) -> pd.DataFrame:
    config = config or MomentumEventConfig()
    events = pd.DataFrame(index=features.index)
    k_cols = _get_columns_by_prefix(features, "stoch_k_")
    for k_col in k_cols:
        parts = k_col.split("_")
        if len(parts) >= 4:
            window = parts[2]
            d_col = k_col.replace("stoch_k_", "stoch_d_")
            if d_col in features.columns:
                k_series = features[k_col]
                d_series = features[d_col]
                prev_k = k_series.shift(1)
                prev_d = d_series.shift(1)
                events[f"event_stoch_{window}_bullish_cross"] = (
                    (prev_k <= prev_d) & (k_series > d_series)
                ).astype(int)
                events[f"event_stoch_{window}_bearish_cross"] = (
                    (prev_k >= prev_d) & (k_series < d_series)
                ).astype(int)
    return events


def detect_roc_shift_events(
    features: pd.DataFrame, config: Optional[MomentumEventConfig] = None
) -> pd.DataFrame:
    config = config or MomentumEventConfig()
    events = pd.DataFrame(index=features.index)
    roc_cols = _get_columns_by_prefix(features, "roc_")
    for col in roc_cols:
        window_match = re.search(r"roc_(\d+)", col)
        if not window_match:
            continue
        window = window_match.group(1)
        roc_series = features[col]
        prev_roc = roc_series.shift(1)
        events[f"event_roc_{window}_positive_shift"] = (
            (prev_roc <= config.roc_neutral) & (roc_series > config.roc_neutral)
        ).astype(int)
        events[f"event_roc_{window}_negative_shift"] = (
            (prev_roc >= config.roc_neutral) & (roc_series < config.roc_neutral)
        ).astype(int)
    return events


def detect_cci_zone_events(
    features: pd.DataFrame, config: Optional[MomentumEventConfig] = None
) -> pd.DataFrame:
    config = config or MomentumEventConfig()
    events = pd.DataFrame(index=features.index)
    cci_cols = _get_columns_by_prefix(features, "cci_")
    for col in cci_cols:
        window_match = re.search(r"cci_(\d+)", col)
        if not window_match:
            continue
        window = window_match.group(1)
        events[f"event_cci_{window}_oversold"] = (
            features[col] < config.cci_lower
        ).astype(int)
        events[f"event_cci_{window}_overbought"] = (
            features[col] > config.cci_upper
        ).astype(int)
    return events


def detect_momentum_slope_events(features: pd.DataFrame) -> pd.DataFrame:
    events = pd.DataFrame(index=features.index)
    slope_cols = _get_columns_by_prefix(features, "slope_")
    for col in slope_cols:
        events[col.replace("slope_", "event_momentum_slope_positive_")] = (
            features[col] > 0
        ).astype(int)
        events[col.replace("slope_", "event_momentum_slope_negative_")] = (
            features[col] < 0
        ).astype(int)
    return events


def build_momentum_event_frame(
    features: pd.DataFrame, config: Optional[MomentumEventConfig] = None
) -> Tuple[pd.DataFrame, dict]:
    config = config or MomentumEventConfig()
    event_dfs = [
        detect_rsi_zone_events(features, config),
        detect_rsi_crossback_events(features, config),
        detect_stochastic_cross_events(features, config),
        detect_roc_shift_events(features, config),
        detect_cci_zone_events(features, config),
        detect_momentum_slope_events(features),
    ]
    event_df = pd.concat(event_dfs, axis=1)
    event_df.fillna(0, inplace=True)
    event_df = event_df.astype(int)
    event_columns = event_df.columns.tolist()
    active_last_row = []
    if not event_df.empty:
        last_row = event_df.iloc[-1]
        active_last_row = last_row[last_row == 1].index.tolist()
    event_count_by_column = event_df.sum().to_dict()
    summary = {
        "input_rows": len(features),
        "event_columns": event_columns,
        "total_event_count": int(event_df.sum().sum()),
        "event_count_by_column": event_count_by_column,
        "active_last_row_events": active_last_row,
        "warnings": [],
        "notes": "Generated candidate events based on momentum indicators. These are not trade signals.",
    }
    return event_df, summary
