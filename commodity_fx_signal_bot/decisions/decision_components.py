import pandas as pd
from typing import Dict
from .directional_bias import calculate_directional_consensus_score


def calculate_signal_score_component(candidates_df: pd.DataFrame) -> float:
    if candidates_df is None or candidates_df.empty:
        return 0.0
    if "signal_score" in candidates_df.columns:
        return candidates_df["signal_score"].max()
    return 0.5


def calculate_directional_consensus_component(
    candidates_df: pd.DataFrame, target_direction: str
) -> float:
    if candidates_df is None or candidates_df.empty:
        return 0.0
    consensus = calculate_directional_consensus_score(candidates_df)
    return consensus


def calculate_regime_confirmation_component(
    context_frames: Dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    target_direction: str,
    candidate_type: str,
) -> float:
    if "regime" not in context_frames or context_frames["regime"].empty:
        return 0.5

    df = context_frames["regime"]
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)

    idx = df.index.asof(timestamp)
    if pd.isna(idx):
        return 0.5

    row = df.loc[idx]

    # Placeholder logic, adjust based on actual regime context
    if target_direction == "bullish":
        if "regime_label" in row and "bull" in str(row["regime_label"]).lower():
            return 1.0
        elif "trend" in str(row.get("regime_label", "")).lower():
            return 0.8
    elif target_direction == "bearish":
        if "regime_label" in row and "bear" in str(row["regime_label"]).lower():
            return 1.0
        elif "trend" in str(row.get("regime_label", "")).lower():
            return 0.8

    return 0.5


def calculate_mtf_confirmation_component(
    context_frames: Dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    target_direction: str,
) -> float:
    if "mtf" not in context_frames or context_frames["mtf"].empty:
        return 0.5

    df = context_frames["mtf"]
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)

    idx = df.index.asof(timestamp)
    if pd.isna(idx):
        return 0.5

    row = df.loc[idx]

    if target_direction == "bullish":
        if row.get("mtf_trend_alignment", 0) > 0:
            return 1.0
    elif target_direction == "bearish":
        if row.get("mtf_trend_alignment", 0) < 0:
            return 1.0

    return 0.5


def calculate_macro_context_component(
    context_frames: Dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    target_direction: str,
) -> float:
    if "macro" not in context_frames or context_frames["macro"].empty:
        return 0.5

    df = context_frames["macro"]
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)

    idx = df.index.asof(timestamp)
    if pd.isna(idx):
        return 0.5

    row = df.loc[idx]
    # Implement macro logic here
    return 0.5


def calculate_asset_profile_fit_component(
    context_frames: Dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    candidate_type: str,
) -> float:
    if "asset_profiles" not in context_frames or context_frames["asset_profiles"].empty:
        return 0.5

    df = context_frames["asset_profiles"]
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)

    idx = df.index.asof(timestamp)
    if pd.isna(idx):
        return 0.5

    # Implement asset profile fit logic
    return 0.5


def calculate_quality_component(
    candidates_df: pd.DataFrame,
    context_frames: Dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
) -> float:
    # Basic quality logic
    if candidates_df is None or candidates_df.empty:
        return 0.0
    return min(1.0, len(candidates_df) * 0.2 + 0.5)


def calculate_risk_precheck_component(
    candidates_df: pd.DataFrame,
    context_frames: Dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
) -> float:
    # Not real risk management
    return 0.5


def calculate_strategy_readiness_score(components: Dict[str, float]) -> float:
    if not components:
        return 0.0
    return sum(components.values()) / len(components)
