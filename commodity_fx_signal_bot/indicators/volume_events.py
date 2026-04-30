import logging
import pandas as pd
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class VolumeEventConfig:
    volume_spike_zscore: float = 2.5
    volume_dryup_zscore: float = -1.5
    mfi_overbought: float = 80.0
    mfi_oversold: float = 20.0
    cmf_positive_threshold: float = 0.05
    cmf_negative_threshold: float = -0.05
    relative_volume_high: float = 1.8
    relative_volume_low: float = 0.5
    min_volume_valid_ratio: float = 0.60
    disable_events_if_volume_unusable: bool = True
    min_event_strength: float = 0.0


def detect_volume_spike_events(
    features: pd.DataFrame, config: VolumeEventConfig | None = None
) -> pd.DataFrame:
    cfg = config or VolumeEventConfig()
    res = pd.DataFrame(index=features.index)
    col = "event_volume_spike"
    res[col] = 0
    if "volume_zscore_20" in features.columns:
        res.loc[features["volume_zscore_20"] > cfg.volume_spike_zscore, col] = 1
    return res


def detect_volume_dryup_events(
    features: pd.DataFrame, config: VolumeEventConfig | None = None
) -> pd.DataFrame:
    cfg = config or VolumeEventConfig()
    res = pd.DataFrame(index=features.index)
    col = "event_volume_dryup"
    res[col] = 0
    if "volume_zscore_20" in features.columns:
        res.loc[features["volume_zscore_20"] < cfg.volume_dryup_zscore, col] = 1
    return res


def detect_money_flow_events(
    features: pd.DataFrame, config: VolumeEventConfig | None = None
) -> pd.DataFrame:
    cfg = config or VolumeEventConfig()
    res = pd.DataFrame(index=features.index)
    col1 = "event_mfi_14_oversold"
    col2 = "event_mfi_14_overbought"
    res[col1] = 0
    res[col2] = 0
    if "mfi_14" in features.columns:
        res.loc[features["mfi_14"] < cfg.mfi_oversold, col1] = 1
        res.loc[features["mfi_14"] > cfg.mfi_overbought, col2] = 1
    return res


def detect_cmf_accumulation_distribution_events(
    features: pd.DataFrame, config: VolumeEventConfig | None = None
) -> pd.DataFrame:
    cfg = config or VolumeEventConfig()
    res = pd.DataFrame(index=features.index)
    res["event_cmf_accumulation"] = 0
    res["event_cmf_distribution"] = 0
    if "cmf_20" in features.columns:
        res.loc[
            features["cmf_20"] > cfg.cmf_positive_threshold, "event_cmf_accumulation"
        ] = 1
        res.loc[
            features["cmf_20"] < cfg.cmf_negative_threshold, "event_cmf_distribution"
        ] = 1
    return res


def detect_obv_confirmation_events(
    features: pd.DataFrame, config: VolumeEventConfig | None = None
) -> pd.DataFrame:
    res = pd.DataFrame(index=features.index)
    res["event_obv_rising_confirmation"] = 0
    res["event_obv_falling_confirmation"] = 0
    if "obv_slope_10" in features.columns and "close" in features.columns:
        price_slope = features["close"].diff(10) / 10
        res.loc[
            (features["obv_slope_10"] > 0) & (price_slope > 0),
            "event_obv_rising_confirmation",
        ] = 1
        res.loc[
            (features["obv_slope_10"] < 0) & (price_slope < 0),
            "event_obv_falling_confirmation",
        ] = 1
    return res


def detect_price_volume_divergence_events(
    features: pd.DataFrame, config: VolumeEventConfig | None = None
) -> pd.DataFrame:
    res = pd.DataFrame(index=features.index)
    res["event_price_volume_bullish_divergence_candidate"] = 0
    res["event_price_volume_bearish_divergence_candidate"] = 0
    if "price_volume_diverge_10_20" in features.columns:
        # Simple proxy: positive divergence means price falling but volume
        # increasing
        res.loc[
            features["price_volume_diverge_10_20"] > 0,
            "event_price_volume_bullish_divergence_candidate",
        ] = 1
        res.loc[
            features["price_volume_diverge_10_20"] < 0,
            "event_price_volume_bearish_divergence_candidate",
        ] = 1
    return res


def detect_liquidity_events(
    features: pd.DataFrame, config: VolumeEventConfig | None = None
) -> pd.DataFrame:
    res = pd.DataFrame(index=features.index)
    res["event_liquidity_thin"] = 0
    res["event_liquidity_improving"] = 0
    if (
        "liquidity_proxy_20" in features.columns
        and "liquidity_proxy_50" in features.columns
    ):
        res.loc[
            features["liquidity_proxy_20"] < features["liquidity_proxy_50"] * 0.5,
            "event_liquidity_thin",
        ] = 1
        res.loc[
            features["liquidity_proxy_20"] > features["liquidity_proxy_50"] * 1.5,
            "event_liquidity_improving",
        ] = 1
    return res


def build_volume_event_frame(
    features: pd.DataFrame, config: VolumeEventConfig | None = None
) -> tuple[pd.DataFrame, dict]:
    cfg = config or VolumeEventConfig()

    events = [
        detect_volume_spike_events(features, cfg),
        detect_volume_dryup_events(features, cfg),
        detect_money_flow_events(features, cfg),
        detect_cmf_accumulation_distribution_events(features, cfg),
        detect_obv_confirmation_events(features, cfg),
        detect_price_volume_divergence_events(features, cfg),
        detect_liquidity_events(features, cfg),
    ]

    event_df = pd.concat(events, axis=1)

    volume_usable = True
    volume_valid_ratio = 1.0
    if "volume_is_usable" in features.columns:
        volume_usable = (
            features["volume_is_usable"].iloc[-1] if not features.empty else False
        )
    if "volume_valid_ratio" in features.columns:
        volume_valid_ratio = (
            features["volume_valid_ratio"].iloc[-1] if not features.empty else 0.0
        )

    event_df["event_volume_unusable"] = 0
    if not volume_usable:
        event_df["event_volume_unusable"] = 1
        if cfg.disable_events_if_volume_unusable:
            cols_to_zero = [c for c in event_df.columns if c != "event_volume_unusable"]
            event_df[cols_to_zero] = 0

    summary = {
        "input_rows": len(features),
        "event_columns": list(event_df.columns),
        "total_event_count": int(event_df.sum().sum()),
        "event_count_by_column": event_df.sum().to_dict(),
        "active_last_row_events": (
            event_df.iloc[-1][event_df.iloc[-1] > 0].index.tolist()
            if not event_df.empty
            else []
        ),
        "volume_usable": bool(volume_usable),
        "volume_valid_ratio": float(volume_valid_ratio),
        "warnings": (
            [] if volume_usable else ["Volume data is unusable. Events suppressed."]
        ),
        "notes": "These are event candidates, not final trade signals.",
    }

    return event_df, summary
