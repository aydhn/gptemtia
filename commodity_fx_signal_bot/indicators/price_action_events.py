from dataclasses import dataclass

import pandas as pd

from config.settings import settings


@dataclass
class PriceActionEventConfig:
    large_body_percentile_threshold: float = (
        settings.default_large_body_percentile_threshold
    )
    large_range_percentile_threshold: float = (
        settings.default_large_range_percentile_threshold
    )
    small_range_percentile_threshold: float = (
        settings.default_small_range_percentile_threshold
    )
    wick_rejection_ratio: float = settings.default_wick_rejection_ratio
    strong_close_upper_threshold: float = settings.default_strong_close_upper_threshold
    strong_close_lower_threshold: float = settings.default_strong_close_lower_threshold
    gap_pct_threshold: float = 0.01  # Default fallback if not in settings
    breakout_distance_threshold: float = 0.005  # Default fallback
    min_event_strength: float = 0.0


def detect_candle_body_events(
    features: pd.DataFrame, config: PriceActionEventConfig | None = None
) -> pd.DataFrame:
    if config is None:
        config = PriceActionEventConfig()

    events = pd.DataFrame(index=features.index)
    window = settings.default_large_body_percentile_window
    col = f"candle_body_percentile_{window}"

    if col in features.columns:
        events["event_large_body_candle"] = (
            features[col] >= config.large_body_percentile_threshold
        ).astype(int)
        events["event_small_body_candle"] = (
            features[col] <= config.small_range_percentile_threshold
        ).astype(int)

    if f"candle_range_percentile_{window}" in features.columns:
        range_col = f"candle_range_percentile_{window}"
        events["event_large_range_candle"] = (
            features[range_col] >= config.large_range_percentile_threshold
        ).astype(int)

    return events


def detect_wick_rejection_events(
    features: pd.DataFrame, config: PriceActionEventConfig | None = None
) -> pd.DataFrame:
    if config is None:
        config = PriceActionEventConfig()

    events = pd.DataFrame(index=features.index)

    if (
        "upper_wick_to_range_ratio" in features.columns
        and "lower_wick_to_range_ratio" in features.columns
    ):
        events["event_upper_wick_rejection_candidate"] = (
            features["upper_wick_to_range_ratio"] >= config.wick_rejection_ratio
        ).astype(int)
        events["event_lower_wick_rejection_candidate"] = (
            features["lower_wick_to_range_ratio"] >= config.wick_rejection_ratio
        ).astype(int)

    return events


def detect_close_location_events(
    features: pd.DataFrame, config: PriceActionEventConfig | None = None
) -> pd.DataFrame:
    if config is None:
        config = PriceActionEventConfig()

    events = pd.DataFrame(index=features.index)

    if "close_pos_range" in features.columns:
        events["event_strong_close_upper"] = (
            features["close_pos_range"] >= config.strong_close_upper_threshold
        ).astype(int)
        events["event_strong_close_lower"] = (
            features["close_pos_range"] <= config.strong_close_lower_threshold
        ).astype(int)

    return events


def detect_range_expansion_compression_events(
    features: pd.DataFrame, config: PriceActionEventConfig | None = None
) -> pd.DataFrame:
    events = pd.DataFrame(index=features.index)

    # Check for compression/expansion in common windows (like 20)
    for w in [10, 20, 50]:
        comp_col = f"range_compression_{w}"
        exp_col = f"range_expansion_{w}"

        if comp_col in features.columns:
            events[f"event_small_range_compression_{w}"] = (
                features[comp_col].fillna(0).astype(int)
            )
        if exp_col in features.columns:
            events[f"event_range_expansion_{w}"] = (
                features[exp_col].fillna(0).astype(int)
            )

    return events


def detect_inside_outside_bar_events(
    features: pd.DataFrame, config: PriceActionEventConfig | None = None
) -> pd.DataFrame:
    events = pd.DataFrame(index=features.index)

    if "inside_bar" in features.columns:
        events["event_inside_bar_compression"] = (
            features["inside_bar"].fillna(0).astype(int)
        )
    if "outside_bar" in features.columns:
        events["event_outside_bar_expansion"] = (
            features["outside_bar"].fillna(0).astype(int)
        )

    return events


def detect_gap_events(
    features: pd.DataFrame, config: PriceActionEventConfig | None = None
) -> pd.DataFrame:
    if config is None:
        config = PriceActionEventConfig()

    events = pd.DataFrame(index=features.index)

    if "gap_pct" in features.columns and "abs_gap_pct" in features.columns:
        events["event_gap_up"] = (features["gap_pct"] > 0).astype(int)
        events["event_gap_down"] = (features["gap_pct"] < 0).astype(int)
        events["event_large_gap"] = (
            features["abs_gap_pct"] >= config.gap_pct_threshold
        ).astype(int)

    return events


def detect_breakout_setup_events(
    features: pd.DataFrame, config: PriceActionEventConfig | None = None
) -> pd.DataFrame:
    if config is None:
        config = PriceActionEventConfig()

    events = pd.DataFrame(index=features.index)

    for w in [10, 20, 55]:
        dist_high_col = f"dist_to_breakout_high_{w}"
        dist_low_col = f"dist_to_breakout_low_{w}"

        if dist_high_col in features.columns:
            # Distance is calculated as (breakout_high - close) / close
            # Positive means we are below it. Small positive means near.
            # Negative means we broke out.

            # Near breakout: distance is between 0 and threshold
            events[f"event_near_breakout_high_{w}"] = (
                (features[dist_high_col] >= 0)
                & (features[dist_high_col] <= config.breakout_distance_threshold)
            ).astype(int)
            events[f"event_near_breakout_low_{w}"] = (
                (features[dist_low_col] >= 0)
                & (features[dist_low_col] <= config.breakout_distance_threshold)
            ).astype(int)

            # Breakout candidate: we broke out (distance < 0)
            events[f"event_breakout_high_{w}_candidate"] = (
                features[dist_high_col] < 0
            ).astype(int)
            events[f"event_breakout_low_{w}_candidate"] = (
                features[dist_low_col] < 0
            ).astype(int)

    return events


def detect_false_breakout_events(
    features: pd.DataFrame, config: PriceActionEventConfig | None = None
) -> pd.DataFrame:
    events = pd.DataFrame(index=features.index)

    for w in [10, 20, 55]:
        upper_col = f"false_breakout_upper_{w}"
        lower_col = f"false_breakout_lower_{w}"

        if upper_col in features.columns:
            events[f"event_false_breakout_upper_{w}_candidate"] = (
                features[upper_col].fillna(0).astype(int)
            )
        if lower_col in features.columns:
            events[f"event_false_breakout_lower_{w}_candidate"] = (
                features[lower_col].fillna(0).astype(int)
            )

    return events


def detect_consecutive_candle_events(
    features: pd.DataFrame, config: PriceActionEventConfig | None = None
) -> pd.DataFrame:
    events = pd.DataFrame(index=features.index)

    if "consecutive_up_closes" in features.columns:
        events["event_consecutive_up_closes"] = (
            features["consecutive_up_closes"] >= 3
        ).astype(int)
    if "consecutive_down_closes" in features.columns:
        events["event_consecutive_down_closes"] = (
            features["consecutive_down_closes"] >= 3
        ).astype(int)
    if "consecutive_higher_highs" in features.columns:
        events["event_higher_high_sequence"] = (
            features["consecutive_higher_highs"] >= 3
        ).astype(int)
    if "consecutive_lower_lows" in features.columns:
        events["event_lower_low_sequence"] = (
            features["consecutive_lower_lows"] >= 3
        ).astype(int)

    return events


def build_price_action_event_frame(
    features: pd.DataFrame, config: PriceActionEventConfig | None = None
) -> tuple[pd.DataFrame, dict]:
    """Build the full set of price action candidate events."""
    if config is None:
        config = PriceActionEventConfig()

    events_list = []

    # 1. Body/Range Percentile Events
    events_list.append(detect_candle_body_events(features, config))

    # 2. Wick Rejection Events
    events_list.append(detect_wick_rejection_events(features, config))

    # 3. Close Location Events
    events_list.append(detect_close_location_events(features, config))

    # 4. Expansion/Compression Events
    events_list.append(detect_range_expansion_compression_events(features, config))

    # 5. Inside/Outside Bar Events
    events_list.append(detect_inside_outside_bar_events(features, config))

    # 6. Gap Events
    events_list.append(detect_gap_events(features, config))

    # 7. Breakout Setup Events
    events_list.append(detect_breakout_setup_events(features, config))

    # 8. False Breakout Events
    events_list.append(detect_false_breakout_events(features, config))

    # 9. Consecutive Candle Events
    events_list.append(detect_consecutive_candle_events(features, config))

    # Combine
    if events_list:
        event_df = pd.concat(events_list, axis=1)
    else:
        event_df = pd.DataFrame(index=features.index)

    # Ensure all columns are int
    for col in event_df.columns:
        event_df[col] = event_df[col].fillna(0).astype(int)

    # Summary
    event_counts = event_df.sum().to_dict() if not event_df.empty else {}
    active_last_row = (
        event_df.iloc[-1][event_df.iloc[-1] > 0].index.tolist()
        if not event_df.empty
        else []
    )

    summary = {
        "input_rows": len(features),
        "event_columns": list(event_df.columns),
        "total_event_count": sum(event_counts.values()) if event_counts else 0,
        "event_count_by_column": event_counts,
        "active_last_row_events": active_last_row,
        "warnings": ["These are candidate events, NOT final buy/sell signals."],
        "notes": "Price action event frame successfully built.",
    }

    return event_df, summary
