from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np
import pandas as pd

from config.settings import settings


@dataclass
class MeanReversionEventConfig:
    zscore_extreme: float = 2.0
    zscore_major_extreme: float = 3.0
    low_percentile_threshold: float = 0.10
    high_percentile_threshold: float = 0.90
    minmax_low_threshold: float = 0.10
    minmax_high_threshold: float = 0.90
    distance_extreme_threshold: float = 0.05
    band_reentry_threshold: float = 0.0
    min_event_strength: float = 0.0


def _get_default_config() -> MeanReversionEventConfig:
    return MeanReversionEventConfig(
        zscore_extreme=getattr(settings, "default_reversion_zscore_extreme", 2.0),
        zscore_major_extreme=getattr(
            settings, "default_reversion_zscore_major_extreme", 3.0
        ),
        low_percentile_threshold=getattr(
            settings, "default_low_percentile_threshold", 0.10
        ),
        high_percentile_threshold=getattr(
            settings, "default_high_percentile_threshold", 0.90
        ),
        distance_extreme_threshold=getattr(
            settings, "default_distance_extreme_threshold", 0.05
        ),
    )


def detect_zscore_extreme_events(
    features: pd.DataFrame, config: Optional[MeanReversionEventConfig] = None
) -> pd.DataFrame:
    cfg = config or _get_default_config()
    events = pd.DataFrame(index=features.index)

    z_cols = [c for c in features.columns if c.startswith("zscore_close_")]

    for c in z_cols:
        window = c.split("_")[-1]

        events[f"event_zscore_{window}_low_extreme"] = (
            features[c] <= -cfg.zscore_extreme
        ).astype(int)
        events[f"event_zscore_{window}_high_extreme"] = (
            features[c] >= cfg.zscore_extreme
        ).astype(int)

        events[f"event_zscore_{window}_major_low_extreme"] = (
            features[c] <= -cfg.zscore_major_extreme
        ).astype(int)
        events[f"event_zscore_{window}_major_high_extreme"] = (
            features[c] >= cfg.zscore_major_extreme
        ).astype(int)

    return events


def detect_zscore_snapback_events(
    features: pd.DataFrame, config: Optional[MeanReversionEventConfig] = None
) -> pd.DataFrame:
    cfg = config or _get_default_config()
    events = pd.DataFrame(index=features.index)

    z_cols = [c for c in features.columns if c.startswith("zscore_close_")]

    for c in z_cols:
        window = c.split("_")[-1]
        z = features[c]
        z_prev = z.shift(1)

        # Was below low extreme, now crossing above it
        events[f"event_zscore_{window}_low_snapback_candidate"] = (
            (z_prev <= -cfg.zscore_extreme) & (z > -cfg.zscore_extreme)
        ).astype(int)

        # Was above high extreme, now crossing below it
        events[f"event_zscore_{window}_high_snapback_candidate"] = (
            (z_prev >= cfg.zscore_extreme) & (z < cfg.zscore_extreme)
        ).astype(int)

    return events


def detect_percentile_extreme_events(
    features: pd.DataFrame, config: Optional[MeanReversionEventConfig] = None
) -> pd.DataFrame:
    cfg = config or _get_default_config()
    events = pd.DataFrame(index=features.index)

    p_cols = [c for c in features.columns if c.startswith("percentile_close_")]

    for c in p_cols:
        window = c.split("_")[-1]

        events[f"event_percentile_{window}_low_extreme"] = (
            features[c] <= cfg.low_percentile_threshold
        ).astype(int)
        events[f"event_percentile_{window}_high_extreme"] = (
            features[c] >= cfg.high_percentile_threshold
        ).astype(int)

    return events


def detect_minmax_position_events(
    features: pd.DataFrame, config: Optional[MeanReversionEventConfig] = None
) -> pd.DataFrame:
    cfg = config or _get_default_config()
    events = pd.DataFrame(index=features.index)

    m_cols = [c for c in features.columns if c.startswith("minmax_pos_")]

    for c in m_cols:
        window = c.split("_")[-1]

        events[f"event_minmax_{window}_low_zone"] = (
            features[c] <= cfg.minmax_low_threshold
        ).astype(int)
        events[f"event_minmax_{window}_high_zone"] = (
            features[c] >= cfg.minmax_high_threshold
        ).astype(int)

    return events


def detect_band_extension_events(
    features: pd.DataFrame, config: Optional[MeanReversionEventConfig] = None
) -> pd.DataFrame:
    cfg = config or _get_default_config()
    events = pd.DataFrame(index=features.index)

    l_cols = [c for c in features.columns if c.startswith("bb_lower_extension_")]
    u_cols = [c for c in features.columns if c.startswith("bb_upper_extension_")]

    for c in l_cols:
        parts = c.split("_")
        window = parts[-2]
        events[f"event_bb{window}_lower_extension"] = (features[c] > 0).astype(int)

    for c in u_cols:
        parts = c.split("_")
        window = parts[-2]
        events[f"event_bb{window}_upper_extension"] = (features[c] > 0).astype(int)

    return events


def detect_band_reentry_events(
    features: pd.DataFrame, config: Optional[MeanReversionEventConfig] = None
) -> pd.DataFrame:
    cfg = config or _get_default_config()
    events = pd.DataFrame(index=features.index)

    b_cols = [c for c in features.columns if c.startswith("bb_percent_b_")]

    for c in b_cols:
        parts = c.split("_")
        window = parts[-2]
        pct_b = features[c]
        pct_b_prev = pct_b.shift(1)

        events[f"event_bb{window}_lower_reentry_candidate"] = (
            (pct_b_prev < 0) & (pct_b >= 0)
        ).astype(int)

        events[f"event_bb{window}_upper_reentry_candidate"] = (
            (pct_b_prev > 1) & (pct_b <= 1)
        ).astype(int)

    return events


def detect_distance_overextension_events(
    features: pd.DataFrame, config: Optional[MeanReversionEventConfig] = None
) -> pd.DataFrame:
    cfg = config or _get_default_config()
    events = pd.DataFrame(index=features.index)

    d_cols = [c for c in features.columns if c.startswith("dist_sma_")]

    for c in d_cols:
        window = c.split("_")[-1]

        events[f"event_dist_sma_{window}_negative_overextension"] = (
            features[c] <= -cfg.distance_extreme_threshold
        ).astype(int)
        events[f"event_dist_sma_{window}_positive_overextension"] = (
            features[c] >= cfg.distance_extreme_threshold
        ).astype(int)

    return events


def detect_snapback_pressure_events(
    features: pd.DataFrame, config: Optional[MeanReversionEventConfig] = None
) -> pd.DataFrame:
    cfg = config or _get_default_config()
    events = pd.DataFrame(index=features.index)

    sp_cols = [c for c in features.columns if c.startswith("snapback_pressure_")]

    for c in sp_cols:
        parts = c.split("_")
        window = parts[-1]

        # High pressure (e.g. top quartile of absolute pressure, or simply positive)
        # We define event as positive pressure > threshold
        events[f"event_snapback_pressure_positive_{window}"] = (
            features[c] > cfg.min_event_strength
        ).astype(int)
        events[f"event_snapback_pressure_negative_{window}"] = (
            features[c] < -cfg.min_event_strength
        ).astype(int)

    return events


def build_mean_reversion_event_frame(
    features: pd.DataFrame, config: Optional[MeanReversionEventConfig] = None
) -> Tuple[pd.DataFrame, dict]:
    cfg = config or _get_default_config()
    events_list = []

    try:
        events_list.append(detect_zscore_extreme_events(features, cfg))
        events_list.append(detect_zscore_snapback_events(features, cfg))
        events_list.append(detect_percentile_extreme_events(features, cfg))
        events_list.append(detect_minmax_position_events(features, cfg))
        events_list.append(detect_band_extension_events(features, cfg))
        events_list.append(detect_band_reentry_events(features, cfg))
        events_list.append(detect_distance_overextension_events(features, cfg))
        events_list.append(detect_snapback_pressure_events(features, cfg))
    except Exception as e:
        import logging

        logging.getLogger(__name__).warning(
            f"Error detecting mean reversion events: {e}"
        )

    if not events_list:
        return pd.DataFrame(index=features.index), {
            "input_rows": len(features),
            "event_columns": [],
            "total_event_count": 0,
            "event_count_by_column": {},
            "active_last_row_events": [],
            "warnings": ["No events built."],
            "notes": "These events are candidates, not direct buy/sell signals.",
        }

    event_df = pd.concat(events_list, axis=1)

    # Fill NaN with 0 for events
    event_df = event_df.fillna(0).astype(int)

    event_counts = event_df.sum().to_dict()
    total_events = sum(event_counts.values())

    active_last = []
    if not event_df.empty:
        last_row = event_df.iloc[-1]
        active_last = last_row[last_row > 0].index.tolist()

    summary = {
        "input_rows": len(features),
        "event_columns": event_df.columns.tolist(),
        "total_event_count": int(total_events),
        "event_count_by_column": event_counts,
        "active_last_row_events": active_last,
        "warnings": [],
        "notes": "These events are candidates, not direct buy/sell signals.",
    }

    return event_df, summary
