import pandas as pd
from dataclasses import dataclass


@dataclass
class AssetClassEventConfig:
    relative_strength_leader_threshold: float = 0.80
    relative_strength_laggard_threshold: float = 0.20
    high_dispersion_threshold: float = 0.75
    high_correlation_threshold: float = 0.70
    low_correlation_threshold: float = 0.30
    group_momentum_threshold: float = 0.0
    confidence_threshold: float = 0.55


def detect_asset_behavior_events(
    df: pd.DataFrame, config: AssetClassEventConfig | None = None
) -> pd.DataFrame:
    config = config or AssetClassEventConfig()
    events = pd.DataFrame(index=df.index)
    if df.empty:
        return events

    if "asset_behavior_regime_label" in df.columns:
        events["event_asset_low_volume_confidence_warning"] = (
            df["asset_behavior_regime_label"] == "asset_low_volume_confidence"
        ).astype(int)
        events["event_asset_high_gap_risk_warning"] = (
            df["asset_behavior_regime_label"] == "asset_high_gap_risk"
        ).astype(int)

    if "asset_profile_confidence" in df.columns:
        events["event_asset_profile_low_confidence_warning"] = (
            df["asset_profile_confidence"] < config.confidence_threshold
        ).astype(int)

    return events


def detect_group_regime_events(
    df: pd.DataFrame, config: AssetClassEventConfig | None = None
) -> pd.DataFrame:
    config = config or AssetClassEventConfig()
    events = pd.DataFrame(index=df.index)
    if df.empty:
        return events

    if "asset_group_regime_label" in df.columns:
        events["event_asset_group_uptrend_context"] = (
            df["asset_group_regime_label"] == "group_uptrend"
        ).astype(int)
        events["event_asset_group_downtrend_context"] = (
            df["asset_group_regime_label"] == "group_downtrend"
        ).astype(int)

    return events


def detect_relative_strength_events(
    df: pd.DataFrame, config: AssetClassEventConfig | None = None
) -> pd.DataFrame:
    config = config or AssetClassEventConfig()
    events = pd.DataFrame(index=df.index)
    if df.empty:
        return events

    if "asset_relative_strength_regime_label" in df.columns:
        events["event_asset_group_leader_candidate"] = (
            df["asset_relative_strength_regime_label"] == "asset_group_leader"
        ).astype(int)
        events["event_asset_group_laggard_candidate"] = (
            df["asset_relative_strength_regime_label"] == "asset_group_laggard"
        ).astype(int)

    return events


def detect_correlation_events(
    df: pd.DataFrame, config: AssetClassEventConfig | None = None
) -> pd.DataFrame:
    config = config or AssetClassEventConfig()
    events = pd.DataFrame(index=df.index)
    if df.empty:
        return events

    if "asset_correlation_regime_label" in df.columns:
        events["event_asset_high_group_correlation"] = (
            df["asset_correlation_regime_label"] == "asset_high_group_correlation"
        ).astype(int)
        events["event_asset_group_decoupling"] = (
            df["asset_correlation_regime_label"] == "asset_group_decoupling"
        ).astype(int)

    # Example macro event
    macro_cols = [
        c for c in df.columns if "corr_symbol_inflation" in c or "usdtry" in c
    ]
    if macro_cols:
        events["event_asset_macro_sensitive_pressure"] = (
            df[macro_cols[0]] > config.high_correlation_threshold
        ).astype(int)

    return events


def detect_dispersion_events(
    df: pd.DataFrame, config: AssetClassEventConfig | None = None
) -> pd.DataFrame:
    config = config or AssetClassEventConfig()
    events = pd.DataFrame(index=df.index)
    if df.empty:
        return events

    disp_cols = [c for c in df.columns if "dispersion_high" in c]
    if disp_cols:
        events["event_asset_high_dispersion_context"] = (df[disp_cols[0]] == 1).astype(
            int
        )

    disp_low_cols = [c for c in df.columns if "dispersion_low" in c]
    if disp_low_cols:
        events["event_asset_low_dispersion_context"] = (
            df[disp_low_cols[0]] == 1
        ).astype(int)

    return events


def build_asset_class_event_frame(
    df: pd.DataFrame, config: AssetClassEventConfig | None = None
) -> tuple[pd.DataFrame, dict]:
    """Combine all asset class events into a single frame."""
    config = config or AssetClassEventConfig()
    summary = {"warnings": []}

    events_list = [
        detect_asset_behavior_events(df, config),
        detect_group_regime_events(df, config),
        detect_relative_strength_events(df, config),
        detect_correlation_events(df, config),
        detect_dispersion_events(df, config),
    ]

    events = pd.concat(events_list, axis=1)

    summary["rows"] = len(events)
    summary["columns"] = list(events.columns)

    return events, summary
