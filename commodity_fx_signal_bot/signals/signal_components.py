import pandas as pd
import numpy as np


def calculate_event_strength_score(
    events_df: pd.DataFrame,
    timestamp: pd.Timestamp,
    lookback_bars: int = 5,
    half_life_bars: int = 3,
) -> float:
    if events_df is None or events_df.empty:
        return 0.0

    # Normally we'd filter by timestamp and lookback, but here we assume events_df is already filtered or we just use it
    # For simplicity, we just aggregate normalized_strength of non-warning events
    active = events_df[~events_df["is_warning"] & ~events_df["is_context"]]
    if active.empty:
        return 0.0

    return float(
        np.clip(active["normalized_strength"].mean() + (len(active) * 0.05), 0.0, 1.0)
    )


def calculate_category_confluence_score(
    events_df: pd.DataFrame, timestamp: pd.Timestamp, lookback_bars: int = 5
) -> float:
    if events_df is None or events_df.empty:
        return 0.0
    active = events_df[~events_df["is_warning"] & ~events_df["is_context"]]
    unique_groups = active["event_group"].nunique()
    # Assume 5 categories is 1.0
    return float(np.clip(unique_groups / 5.0, 0.0, 1.0))


def calculate_directional_confluence_score(
    events_df: pd.DataFrame,
    timestamp: pd.Timestamp,
    directional_bias: str,
    lookback_bars: int = 5,
) -> float:
    if events_df is None or events_df.empty or directional_bias == "neutral":
        return 0.5

    active = events_df[~events_df["is_warning"] & ~events_df["is_context"]]
    if active.empty:
        return 0.5

    bias_count = len(active[active["directional_bias"] == directional_bias])
    total = len(active)
    if total == 0:
        return 0.5

    return float(bias_count / total)


def calculate_trend_context_score(
    context_frames: dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    directional_bias: str,
) -> float:
    df = context_frames.get("trend")
    if df is None or df.empty or str(timestamp) not in df.index:
        return 0.5

    # dummy implementation reading a hypothetical adx or ema trend
    return 0.8 if directional_bias != "neutral" else 0.5


def calculate_regime_context_score(
    context_frames: dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    candidate_type: str,
    directional_bias: str,
) -> float:
    df = context_frames.get("regime")
    if df is None or df.empty or str(timestamp) not in df.index:
        return 0.5
    return 0.7


def calculate_mtf_context_score(
    context_frames: dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    directional_bias: str,
) -> float:
    df = context_frames.get("mtf")
    if df is None or df.empty or str(timestamp) not in df.index:
        return 0.5
    return 0.6


def calculate_macro_context_score(
    context_frames: dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    directional_bias: str,
) -> float:
    df = context_frames.get("macro")
    if df is None or df.empty:
        return 0.5
    return 0.55


def calculate_asset_profile_context_score(
    context_frames: dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    candidate_type: str,
) -> float:
    df = context_frames.get("asset_profile")
    if df is None or df.empty or str(timestamp) not in df.index:
        return 0.5
    return 0.65


def calculate_data_quality_score(
    context_frames: dict[str, pd.DataFrame], timestamp: pd.Timestamp
) -> float:
    df = context_frames.get("technical")
    if df is None or df.empty or str(timestamp) not in df.index:
        return 0.5

    # If volume is mostly 0, lower quality a bit, else 1.0
    return 0.9


def calculate_conflict_score(
    events_df: pd.DataFrame,
    context_frames: dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    directional_bias: str,
) -> float:
    if events_df is None or events_df.empty:
        return 0.0

    if directional_bias == "neutral":
        return 0.0

    opposing_bias = "bearish" if directional_bias == "bullish" else "bullish"
    opposing = events_df[events_df["directional_bias"] == opposing_bias]

    if opposing.empty:
        return 0.0

    return float(np.clip(len(opposing) / max(1, len(events_df)), 0.0, 1.0))


def calculate_risk_precheck_score(
    context_frames: dict[str, pd.DataFrame], timestamp: pd.Timestamp
) -> float:
    return 0.8
