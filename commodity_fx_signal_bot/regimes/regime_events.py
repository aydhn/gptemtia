"""
Regime event detection module.
"""

import pandas as pd
import numpy as np
from dataclasses import dataclass

from regimes.regime_labels import UNKNOWN

@dataclass
class RegimeEventConfig:
    transition_lookback: int = 5
    confidence_threshold: float = 0.55
    high_conflict_threshold: float = 0.60
    high_volatility_threshold: float = 0.70
    trend_strength_threshold: float = 0.60

def detect_regime_transition_events(regime_df: pd.DataFrame, config: RegimeEventConfig | None = None) -> pd.DataFrame:
    """Detect when the primary regime changes."""
    if config is None:
        config = RegimeEventConfig()

    events = pd.DataFrame(index=regime_df.index)

    if "regime_primary_label" not in regime_df.columns:
        return events

    labels = regime_df["regime_primary_label"]

    # Transition event: True when current label is different from previous label
    # Ignore transitions from/to UNKNOWN or INSUFFICIENT_DATA if possible, or just raw transitions
    shifted = labels.shift(1)

    is_transition = (labels != shifted) & (labels != UNKNOWN) & (shifted != UNKNOWN) & (~labels.isna()) & (~shifted.isna())
    events["event_regime_transition"] = is_transition.astype(int)

    # Changed recently (within lookback)
    events["event_regime_changed_recently"] = is_transition.rolling(window=config.transition_lookback, min_periods=1).max().fillna(0).astype(int)

    return events

def detect_trend_regime_events(regime_df: pd.DataFrame, config: RegimeEventConfig | None = None) -> pd.DataFrame:
    """Detect trend context events."""
    if config is None:
        config = RegimeEventConfig()

    events = pd.DataFrame(index=regime_df.index)

    if "regime_primary_label" in regime_df.columns:
        labels = regime_df["regime_primary_label"]
        events["event_bullish_trend_regime"] = (labels == "bullish_trend").astype(int)
        events["event_bearish_trend_regime"] = (labels == "bearish_trend").astype(int)
        events["event_strong_trend_regime"] = labels.isin(["strong_bullish_trend", "strong_bearish_trend"]).astype(int)
        events["event_fragile_trend_regime"] = (labels == "weak_trend").astype(int)

    return events

def detect_range_regime_events(regime_df: pd.DataFrame, config: RegimeEventConfig | None = None) -> pd.DataFrame:
    """Detect range context events."""
    if config is None:
        config = RegimeEventConfig()

    events = pd.DataFrame(index=regime_df.index)

    if "regime_primary_label" in regime_df.columns:
        labels = regime_df["regime_primary_label"]
        events["event_range_bound_regime"] = (labels == "range_bound").astype(int)
        events["event_compressed_range_regime"] = (labels == "compressed_range").astype(int)

    return events

def detect_volatility_regime_events(regime_df: pd.DataFrame, config: RegimeEventConfig | None = None) -> pd.DataFrame:
    """Detect volatility context events."""
    if config is None:
        config = RegimeEventConfig()

    events = pd.DataFrame(index=regime_df.index)

    # Volatility can be primary or secondary
    if "regime_secondary_label" in regime_df.columns:
        sec_labels = regime_df["regime_secondary_label"]
        events["event_high_volatility_regime"] = (sec_labels == "high_volatility").astype(int)
        events["event_low_volatility_regime"] = (sec_labels == "low_volatility").astype(int)
        events["event_volatility_expansion_regime"] = (sec_labels == "volatility_expansion").astype(int)

    return events

def detect_conflict_regime_events(regime_df: pd.DataFrame, config: RegimeEventConfig | None = None) -> pd.DataFrame:
    """Detect conflict events."""
    if config is None:
        config = RegimeEventConfig()

    events = pd.DataFrame(index=regime_df.index)

    if "regime_primary_label" in regime_df.columns:
        events["event_conflicting_regime"] = (regime_df["regime_primary_label"] == "conflicting_regime").astype(int)

    if "regime_confidence" in regime_df.columns:
        events["event_insufficient_regime_confidence"] = (regime_df["regime_confidence"] < config.confidence_threshold).astype(int)

    return events

def detect_mean_reversion_regime_events(regime_df: pd.DataFrame, config: RegimeEventConfig | None = None) -> pd.DataFrame:
    """Detect mean reversion friendly environments."""
    if config is None:
        config = RegimeEventConfig()

    events = pd.DataFrame(index=regime_df.index)

    if "regime_secondary_label" in regime_df.columns:
        events["event_mean_reversion_friendly_regime"] = (regime_df["regime_secondary_label"] == "mean_reversion_friendly").astype(int)

    return events

def build_regime_event_frame(regime_df: pd.DataFrame, config: RegimeEventConfig | None = None) -> tuple[pd.DataFrame, dict]:
    """
    Build the full event dataframe.
    """
    if config is None:
        config = RegimeEventConfig()

    event_dfs = [
        detect_regime_transition_events(regime_df, config),
        detect_trend_regime_events(regime_df, config),
        detect_range_regime_events(regime_df, config),
        detect_volatility_regime_events(regime_df, config),
        detect_conflict_regime_events(regime_df, config),
        detect_mean_reversion_regime_events(regime_df, config)
    ]

    # Filter out empty dataframes
    event_dfs = [df for df in event_dfs if not df.empty]

    if not event_dfs:
        return pd.DataFrame(index=regime_df.index), {
            "input_rows": len(regime_df),
            "event_columns": [],
            "total_event_count": 0,
            "event_count_by_column": {},
            "active_last_row_events": [],
            "warnings": ["No events could be generated."],
            "notes": "Events require primary and secondary regime labels."
        }

    combined_events = pd.concat(event_dfs, axis=1)

    # Fill NAs with 0
    combined_events = combined_events.fillna(0).astype(int)

    # Calculate summary statistics
    event_cols = combined_events.columns.tolist()
    event_counts = combined_events.sum().to_dict()
    total_events = sum(event_counts.values())

    active_last = []
    if not combined_events.empty:
        last_row = combined_events.iloc[-1]
        active_last = last_row[last_row > 0].index.tolist()

    summary = {
        "input_rows": len(regime_df),
        "event_columns": event_cols,
        "total_event_count": int(total_events),
        "event_count_by_column": {k: int(v) for k, v in event_counts.items()},
        "active_last_row_events": active_last,
        "warnings": [],
        "notes": "Regime events represent market context, NOT buy/sell signals."
    }

    return combined_events, summary
