from dataclasses import dataclass
import pandas as pd
import numpy as np


@dataclass
class MTFEventConfig:
    trend_alignment_threshold: float = 0.60
    momentum_alignment_threshold: float = 0.60
    conflict_threshold: float = 0.60
    stale_context_threshold: float = 0.30
    cluster_threshold: float = 0.50
    min_event_strength: float = 0.0


def _detect_event(
    mtf_df: pd.DataFrame, score_col: str, threshold: float, event_name: str
) -> pd.DataFrame:
    df = pd.DataFrame(index=mtf_df.index)
    if score_col in mtf_df.columns:
        df[event_name] = (mtf_df[score_col].abs() > threshold).astype(int)
    else:
        df[event_name] = 0
    return df


def detect_mtf_trend_alignment_events(
    mtf_df: pd.DataFrame, config: MTFEventConfig | None = None
) -> pd.DataFrame:
    config = config or MTFEventConfig()
    return _detect_event(
        mtf_df,
        "mtf_trend_alignment_score",
        config.trend_alignment_threshold,
        "event_mtf_trend_alignment_candidate",
    )


def detect_mtf_momentum_alignment_events(
    mtf_df: pd.DataFrame, config: MTFEventConfig | None = None
) -> pd.DataFrame:
    config = config or MTFEventConfig()
    return _detect_event(
        mtf_df,
        "mtf_momentum_alignment_score",
        config.momentum_alignment_threshold,
        "event_mtf_momentum_alignment_candidate",
    )


def detect_mtf_pullback_context_events(
    mtf_df: pd.DataFrame, config: MTFEventConfig | None = None
) -> pd.DataFrame:
    config = config or MTFEventConfig()
    df = pd.DataFrame(index=mtf_df.index)
    df["event_mtf_pullback_context_candidate"] = 0
    return df


def detect_mtf_volatility_context_events(
    mtf_df: pd.DataFrame, config: MTFEventConfig | None = None
) -> pd.DataFrame:
    config = config or MTFEventConfig()
    df = pd.DataFrame(index=mtf_df.index)
    df["event_mtf_volatility_breakout_context"] = 0
    return df


def detect_mtf_conflict_events(
    mtf_df: pd.DataFrame, config: MTFEventConfig | None = None
) -> pd.DataFrame:
    config = config or MTFEventConfig()
    return _detect_event(
        mtf_df,
        "mtf_conflict_score",
        config.conflict_threshold,
        "event_mtf_high_conflict",
    )


def detect_mtf_stale_context_events(
    mtf_df: pd.DataFrame, config: MTFEventConfig | None = None
) -> pd.DataFrame:
    config = config or MTFEventConfig()
    return _detect_event(
        mtf_df,
        "mtf_stale_context_ratio",
        config.stale_context_threshold,
        "event_mtf_stale_context_warning",
    )


def detect_mtf_event_cluster_events(
    mtf_df: pd.DataFrame, config: MTFEventConfig | None = None
) -> pd.DataFrame:
    config = config or MTFEventConfig()
    return _detect_event(
        mtf_df,
        "mtf_event_cluster_score",
        config.cluster_threshold,
        "event_mtf_multi_timeframe_cluster",
    )


def build_mtf_event_frame(
    mtf_df: pd.DataFrame, config: MTFEventConfig | None = None
) -> tuple[pd.DataFrame, dict]:
    config = config or MTFEventConfig()

    events = []
    events.append(detect_mtf_trend_alignment_events(mtf_df, config))
    events.append(detect_mtf_momentum_alignment_events(mtf_df, config))
    events.append(detect_mtf_pullback_context_events(mtf_df, config))
    events.append(detect_mtf_volatility_context_events(mtf_df, config))
    events.append(detect_mtf_conflict_events(mtf_df, config))
    events.append(detect_mtf_stale_context_events(mtf_df, config))
    events.append(detect_mtf_event_cluster_events(mtf_df, config))

    event_df = pd.concat(events, axis=1)

    summary = {
        "input_rows": len(mtf_df),
        "event_columns": list(event_df.columns),
        "total_event_count": int(event_df.sum().sum()),
        "event_count_by_column": event_df.sum().to_dict(),
        "active_last_row_events": (
            event_df.iloc[-1][event_df.iloc[-1] > 0].index.tolist()
            if not event_df.empty
            else []
        ),
        "warnings": [],
        "notes": "These are context candidates, NOT trade signals.",
    }

    return event_df, summary
