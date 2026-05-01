import logging
from dataclasses import dataclass
from typing import Optional, Tuple

import pandas as pd

from config.settings import settings

logger = logging.getLogger(__name__)


@dataclass
class DivergenceEventConfig:
    min_strength: float = 0.0
    require_recent_confirmation: bool = True
    confirmation_window: int = settings.default_divergence_confirmation_window
    group_by_direction: bool = True


def _any_in_window(series: pd.Series, window: int) -> pd.Series:
    """Returns 1 if any True/1 value occurred in the rolling window."""
    return series.rolling(window=window, min_periods=1).max().fillna(0).astype(int)


def detect_bullish_divergence_events(
    features: pd.DataFrame, config: Optional[DivergenceEventConfig] = None
) -> pd.DataFrame:
    if config is None:
        config = DivergenceEventConfig()

    out = pd.DataFrame(index=features.index)

    # Regular Bullish
    reg_bull_cols = [
        c for c in features.columns if c.startswith("div_regular_bullish_")
    ]
    if reg_bull_cols:
        out["event_regular_bullish_divergence_candidate"] = (
            features[reg_bull_cols].max(axis=1).fillna(0).astype(int)
        )

    # Hidden Bullish
    hid_bull_cols = [c for c in features.columns if c.startswith("div_hidden_bullish_")]
    if hid_bull_cols:
        out["event_hidden_bullish_divergence_candidate"] = (
            features[hid_bull_cols].max(axis=1).fillna(0).astype(int)
        )

    # Any Bullish
    all_bull_cols = reg_bull_cols + hid_bull_cols
    if all_bull_cols:
        out["event_bullish_divergence_candidate"] = (
            features[all_bull_cols].max(axis=1).fillna(0).astype(int)
        )

    return out


def detect_bearish_divergence_events(
    features: pd.DataFrame, config: Optional[DivergenceEventConfig] = None
) -> pd.DataFrame:
    if config is None:
        config = DivergenceEventConfig()

    out = pd.DataFrame(index=features.index)

    # Regular Bearish
    reg_bear_cols = [
        c for c in features.columns if c.startswith("div_regular_bearish_")
    ]
    if reg_bear_cols:
        out["event_regular_bearish_divergence_candidate"] = (
            features[reg_bear_cols].max(axis=1).fillna(0).astype(int)
        )

    # Hidden Bearish
    hid_bear_cols = [c for c in features.columns if c.startswith("div_hidden_bearish_")]
    if hid_bear_cols:
        out["event_hidden_bearish_divergence_candidate"] = (
            features[hid_bear_cols].max(axis=1).fillna(0).astype(int)
        )

    # Any Bearish
    all_bear_cols = reg_bear_cols + hid_bear_cols
    if all_bear_cols:
        out["event_bearish_divergence_candidate"] = (
            features[all_bear_cols].max(axis=1).fillna(0).astype(int)
        )

    return out


def detect_multi_indicator_divergence_cluster(
    features: pd.DataFrame, config: Optional[DivergenceEventConfig] = None
) -> pd.DataFrame:
    if config is None:
        config = DivergenceEventConfig()

    out = pd.DataFrame(index=features.index)
    window = config.confirmation_window if config.require_recent_confirmation else 1

    # Count how many DIFFERENT indicators showed divergence in the recent window
    reg_bull_cols = [
        c for c in features.columns if c.startswith("div_regular_bullish_")
    ]
    if len(reg_bull_cols) > 1:
        # Sum of indicators that fired recently
        active_count = sum([_any_in_window(features[c], window) for c in reg_bull_cols])
        out["event_regular_bullish_divergence_cluster"] = (active_count >= 2).astype(
            int
        )

    reg_bear_cols = [
        c for c in features.columns if c.startswith("div_regular_bearish_")
    ]
    if len(reg_bear_cols) > 1:
        active_count = sum([_any_in_window(features[c], window) for c in reg_bear_cols])
        out["event_regular_bearish_divergence_cluster"] = (active_count >= 2).astype(
            int
        )

    # Multi-indicator independent of direction (just general confusion/cluster)
    all_div_cols = [
        c
        for c in features.columns
        if c.startswith("div_") and not c.startswith("div_strength")
    ]
    if len(all_div_cols) > 1:
        active_count = sum([_any_in_window(features[c], window) for c in all_div_cols])
        out["event_multi_indicator_divergence_cluster"] = (active_count >= 3).astype(
            int
        )

    return out


def detect_volume_price_divergence_events(
    features: pd.DataFrame, config: Optional[DivergenceEventConfig] = None
) -> pd.DataFrame:
    if config is None:
        config = DivergenceEventConfig()

    out = pd.DataFrame(index=features.index)

    vol_bull_cols = [
        c
        for c in features.columns
        if c.startswith("div_regular_bullish_")
        and any(v in c for v in ["obv", "cmf", "mfi", "volume"])
    ]
    if vol_bull_cols:
        out["event_volume_price_bullish_divergence_candidate"] = (
            features[vol_bull_cols].max(axis=1).fillna(0).astype(int)
        )

    vol_bear_cols = [
        c
        for c in features.columns
        if c.startswith("div_regular_bearish_")
        and any(v in c for v in ["obv", "cmf", "mfi", "volume"])
    ]
    if vol_bear_cols:
        out["event_volume_price_bearish_divergence_candidate"] = (
            features[vol_bear_cols].max(axis=1).fillna(0).astype(int)
        )

    return out


def detect_momentum_weakening_events(
    features: pd.DataFrame, config: Optional[DivergenceEventConfig] = None
) -> pd.DataFrame:
    if config is None:
        config = DivergenceEventConfig()

    out = pd.DataFrame(index=features.index)

    mom_bull_cols = [
        c
        for c in features.columns
        if c.startswith("div_regular_bullish_")
        and any(m in c for m in ["rsi", "macd", "roc", "mom"])
    ]
    if mom_bull_cols:
        out["event_momentum_weakening_bullish_candidate"] = (
            features[mom_bull_cols].max(axis=1).fillna(0).astype(int)
        )

    mom_bear_cols = [
        c
        for c in features.columns
        if c.startswith("div_regular_bearish_")
        and any(m in c for m in ["rsi", "macd", "roc", "mom"])
    ]
    if mom_bear_cols:
        out["event_momentum_weakening_bearish_candidate"] = (
            features[mom_bear_cols].max(axis=1).fillna(0).astype(int)
        )

    return out


def build_divergence_event_frame(
    features: pd.DataFrame, config: Optional[DivergenceEventConfig] = None
) -> Tuple[pd.DataFrame, dict]:
    if config is None:
        config = DivergenceEventConfig()

    events = [
        detect_bullish_divergence_events(features, config),
        detect_bearish_divergence_events(features, config),
        detect_multi_indicator_divergence_cluster(features, config),
        detect_volume_price_divergence_events(features, config),
        detect_momentum_weakening_events(features, config),
    ]

    # Combine all event dataframes
    out = pd.concat(events, axis=1)
    # Deduplicate columns if any overlap
    out = out.loc[:, ~out.columns.duplicated()]

    summary = {
        "input_rows": len(features),
        "event_columns": list(out.columns),
        "total_event_count": int(out.sum().sum()),
        "event_count_by_column": {col: int(out[col].sum()) for col in out.columns},
        "active_last_row_events": [
            col for col in out.columns if len(out) > 0 and out[col].iloc[-1] > 0
        ],
        "warnings": [],
        "notes": ["These events are CANDIDATES, not direct buy/sell signals."],
    }

    return out, summary
