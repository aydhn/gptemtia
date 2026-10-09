from dataclasses import dataclass

import numpy as np
import pandas as pd

from signals.signal_taxonomy import (
    infer_candidate_type,
    infer_directional_bias,
    infer_event_group,
    is_context_event,
    is_warning_event,
)


@dataclass
class NormalizedEvent:
    symbol: str
    timeframe: str
    timestamp: str
    event_name: str
    event_group: str
    directional_bias: str
    candidate_type: str
    is_warning: bool
    is_context: bool
    raw_value: float
    normalized_strength: float
    source_feature_set: str


def normalize_event_frame(
    symbol: str,
    timeframe: str,
    event_group: str,
    event_df: pd.DataFrame,
) -> tuple[pd.DataFrame, dict]:
    """
    Convert an event dataframe (boolean/numeric columns over time)
    into a standard 'normalized event' table.
    """
    if event_df is None or event_df.empty:
        return pd.DataFrame(), {"event_count": 0}

    normalized_rows = []

    columns = event_df.columns
    # Pre-calculate mapping dictionaries for functions since the set of columns is small
    bias_map = {col: infer_directional_bias(col) for col in columns}
    type_map = {col: infer_candidate_type(col) for col in columns}
    group_map = {col: event_group if event_group else infer_event_group(col) for col in columns}
    warning_map = {col: is_warning_event(col) for col in columns}
    context_map = {col: is_context_event(col) for col in columns}

    # Process row by row for the timeframe using itertuples
    for row in event_df.itertuples():
        timestamp_str = str(row[0])

        # Iterate over values (skipping index at row[0])
        for idx, val in enumerate(row[1:]):
            if pd.isna(val) or val == 0 or val is False:
                continue

            col = columns[idx]
            raw_value = float(val)
            normalized_strength = (
                1.0
                if isinstance(val, (bool, np.bool_))
                else min(max(abs(raw_value), 0.0), 1.0)
            )

            normalized_rows.append(
                {
                    "symbol": symbol,
                    "timeframe": timeframe,
                    "timestamp": timestamp_str,
                    "event_name": col,
                    "event_group": group_map[col],
                    "directional_bias": bias_map[col],
                    "candidate_type": type_map[col],
                    "is_warning": warning_map[col],
                    "is_context": context_map[col],
                    "raw_value": raw_value,
                    "normalized_strength": normalized_strength,
                    "source_feature_set": f"{group_map[col]}_events",
                }
            )

    if not normalized_rows:
        return pd.DataFrame(), {"event_count": 0}

    df_normalized = pd.DataFrame(normalized_rows)
    return df_normalized, {"event_count": len(normalized_rows)}


def normalize_many_event_frames(
    symbol: str,
    timeframe: str,
    event_frames: dict[str, pd.DataFrame],
) -> tuple[pd.DataFrame, dict]:
    """
    Combine multiple event frames into one normalized table.
    """
    all_normalized = []
    total_events = 0

    for group, df in event_frames.items():
        norm_df, summary = normalize_event_frame(symbol, timeframe, group, df)
        if not norm_df.empty:
            all_normalized.append(norm_df)
            total_events += summary["event_count"]

    if not all_normalized:
        return pd.DataFrame(), {"total_events": 0}

    combined_df = pd.concat(all_normalized, ignore_index=True)
    return combined_df, {"total_events": total_events}
