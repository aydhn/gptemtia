from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np
import pandas as pd


@dataclass
class VolatilityEventConfig:
    squeeze_percentile_threshold: float = 0.10
    expansion_percentile_threshold: float = 0.90
    atr_pct_high_threshold: float = 0.03
    range_pct_high_threshold: float = 0.04
    gap_pct_high_threshold: float = 0.01
    bb_width_col: str = "bb_width_20_2"
    atr_pct_col: str = "atr_pct_14"
    hist_vol_col: str = "hist_vol_20"
    min_event_strength: float = 0.0


def detect_volatility_squeeze_events(
    features: pd.DataFrame, config: Optional[VolatilityEventConfig] = None
) -> pd.DataFrame:
    if config is None:
        config = VolatilityEventConfig()

    df = pd.DataFrame(index=features.index)
    col_name = f"percentile_{config.bb_width_col}_120"

    if col_name in features.columns:
        # A squeeze is when volatility is in the lowest percentile
        df["event_volatility_squeeze_bb20"] = (
            features[col_name] < config.squeeze_percentile_threshold
        ).astype(int)

    return df


def detect_volatility_expansion_events(
    features: pd.DataFrame, config: Optional[VolatilityEventConfig] = None
) -> pd.DataFrame:
    if config is None:
        config = VolatilityEventConfig()

    df = pd.DataFrame(index=features.index)
    col_name = f"percentile_{config.bb_width_col}_120"

    if col_name in features.columns:
        # An expansion is when volatility breaks into the highest percentile
        df["event_volatility_expansion_bb20"] = (
            features[col_name] > config.expansion_percentile_threshold
        ).astype(int)

    return df


def detect_atr_regime_events(
    features: pd.DataFrame, config: Optional[VolatilityEventConfig] = None
) -> pd.DataFrame:
    if config is None:
        config = VolatilityEventConfig()

    df = pd.DataFrame(index=features.index)

    atr_col = config.atr_pct_col
    if atr_col in features.columns:
        df["event_atr_pct_high"] = (
            features[atr_col] > config.atr_pct_high_threshold
        ).astype(int)
        # Low is arbitrarily < 1% for this basic setup
        df["event_atr_pct_low"] = (features[atr_col] < 0.01).astype(int)

    slope_col = f"slope_{config.atr_pct_col}_5"
    if slope_col in features.columns:
        df["event_atr_pct_rising"] = (features[slope_col] > 0.05).astype(int)
        df["event_atr_pct_falling"] = (features[slope_col] < -0.05).astype(int)

    # Historical Volatility
    hist_col = config.hist_vol_col
    hist_pct_col = f"percentile_{hist_col}_120"
    if hist_pct_col in features.columns:
        df["event_hist_vol_high_percentile"] = (
            features[hist_pct_col] > config.expansion_percentile_threshold
        ).astype(int)
        df["event_hist_vol_low_percentile"] = (
            features[hist_pct_col] < config.squeeze_percentile_threshold
        ).astype(int)

    return df


def detect_range_shock_events(
    features: pd.DataFrame, config: Optional[VolatilityEventConfig] = None
) -> pd.DataFrame:
    if config is None:
        config = VolatilityEventConfig()

    df = pd.DataFrame(index=features.index)

    if "range_pct" in features.columns:
        df["event_range_shock_high"] = (
            features["range_pct"] > config.range_pct_high_threshold
        ).astype(int)

    return df


def detect_gap_volatility_events(
    features: pd.DataFrame, config: Optional[VolatilityEventConfig] = None
) -> pd.DataFrame:
    if config is None:
        config = VolatilityEventConfig()

    df = pd.DataFrame(index=features.index)

    if "abs_gap_pct" in features.columns:
        df["event_gap_volatility_high"] = (
            features["abs_gap_pct"] > config.gap_pct_high_threshold
        ).astype(int)

    return df


def detect_channel_compression_events(
    features: pd.DataFrame, config: Optional[VolatilityEventConfig] = None
) -> pd.DataFrame:
    if config is None:
        config = VolatilityEventConfig()

    df = pd.DataFrame(index=features.index)

    if "percentile_donchian_width_20_120" in features.columns:
        df["event_channel_compression_donchian20"] = (
            features["percentile_donchian_width_20_120"]
            < config.squeeze_percentile_threshold
        ).astype(int)

    return df


def detect_channel_breakout_setup_events(
    features: pd.DataFrame, config: Optional[VolatilityEventConfig] = None
) -> pd.DataFrame:
    if config is None:
        config = VolatilityEventConfig()

    df = pd.DataFrame(index=features.index)

    if "channel_pos_donchian20" in features.columns:
        # Candidate for breakout when price is near the channel edges (>0.95 or <0.05)
        df["event_channel_breakout_setup_upper"] = (
            features["channel_pos_donchian20"] > 0.95
        ).astype(int)
        df["event_channel_breakout_setup_lower"] = (
            features["channel_pos_donchian20"] < 0.05
        ).astype(int)

    return df


def build_volatility_event_frame(
    features: pd.DataFrame, config: Optional[VolatilityEventConfig] = None
) -> Tuple[pd.DataFrame, dict]:
    """Build the complete event frame by running all detection logic."""
    if config is None:
        config = VolatilityEventConfig()

    event_dfs = []

    event_dfs.append(detect_volatility_squeeze_events(features, config))
    event_dfs.append(detect_volatility_expansion_events(features, config))
    event_dfs.append(detect_atr_regime_events(features, config))
    event_dfs.append(detect_range_shock_events(features, config))
    event_dfs.append(detect_gap_volatility_events(features, config))
    event_dfs.append(detect_channel_compression_events(features, config))
    event_dfs.append(detect_channel_breakout_setup_events(features, config))

    # Filter out empty dataframes
    valid_dfs = [df for df in event_dfs if not df.empty and len(df.columns) > 0]

    if not valid_dfs:
        return pd.DataFrame(index=features.index), {
            "input_rows": len(features),
            "event_columns": [],
            "total_event_count": 0,
            "event_count_by_column": {},
            "active_last_row_events": [],
            "warnings": ["No volatility events could be calculated."],
            "notes": "Volatility events are candidates, not direct buy/sell signals.",
        }

    event_frame = pd.concat(valid_dfs, axis=1)

    # Fill NAs with 0 (False)
    event_frame = event_frame.fillna(0).astype(int)

    # Summary
    cols = event_frame.columns.tolist()
    counts = {col: int(event_frame[col].sum()) for col in cols}
    total = sum(counts.values())

    active_last = []
    if len(event_frame) > 0:
        last_row = event_frame.iloc[-1]
        active_last = [col for col in cols if last_row[col] > 0]

    summary = {
        "input_rows": len(features),
        "event_columns": cols,
        "total_event_count": total,
        "event_count_by_column": counts,
        "active_last_row_events": active_last,
        "warnings": [],
        "notes": "Volatility events are candidates, not direct buy/sell signals.",
    }

    return event_frame, summary
