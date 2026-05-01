import logging

import numpy as np
import pandas as pd

from indicators.volume_advanced import (
    calculate_accumulation_distribution,
    calculate_chaikin_oscillator,
    calculate_cmf_multi,
    calculate_dollar_volume_proxy,
    calculate_liquidity_proxy,
    calculate_mfi_multi,
    calculate_multi_volume_sma,
    calculate_multi_volume_zscore,
    calculate_obv_advanced,
    calculate_obv_slope,
    calculate_price_volume_trend,
    calculate_relative_volume,
    calculate_volume_percentile,
    calculate_volume_price_confirmation,
    detect_volume_usability,
)
from indicators.volume_events import VolumeEventConfig, build_volume_event_frame

logger = logging.getLogger(__name__)


class VolumeFeatureSetBuilder:
    def __init__(self):
        pass

    def build_volume_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
        disable_events_if_volume_unusable: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        if df.empty:
            return pd.DataFrame(), {}

        features = df.copy()

        comps = [
            detect_volume_usability(features),
            calculate_multi_volume_sma(features),
            calculate_multi_volume_zscore(features),
            calculate_relative_volume(features),
            calculate_obv_advanced(features),
            calculate_obv_slope(features),
            calculate_mfi_multi(features),
            calculate_cmf_multi(features),
            calculate_accumulation_distribution(features),
            calculate_chaikin_oscillator(features),
            calculate_price_volume_trend(features),
            calculate_volume_price_confirmation(features),
            calculate_dollar_volume_proxy(features),
            calculate_liquidity_proxy(features),
            calculate_volume_percentile(features),
        ]

        for comp in comps:
            for col in comp.columns:
                features[col] = comp[col]

        events = pd.DataFrame()
        event_summary = {}
        if include_events:
            cfg = VolumeEventConfig(
                disable_events_if_volume_unusable=disable_events_if_volume_unusable
            )
            events, event_summary = build_volume_event_frame(features, cfg)
            for col in events.columns:
                features[col] = events[col]

        features = features.replace([np.inf, -np.inf], np.nan)

        summary = self.validate_volume_features(features)
        summary["event_columns"] = list(events.columns) if include_events else []
        summary["event_count"] = int(events.sum().sum()) if include_events else 0

        return features, summary

    def build_compact_volume_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
        disable_events_if_volume_unusable: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        if df.empty:
            return pd.DataFrame(), {}

        features = df.copy()

        comps = [
            detect_volume_usability(features),
            calculate_multi_volume_sma(features, windows=(20,)),
            calculate_multi_volume_zscore(features, windows=(20,)),
            calculate_relative_volume(features, windows=(20,)),
            calculate_obv_advanced(features),
            calculate_obv_slope(features, window=10),
            calculate_mfi_multi(features, windows=(14,)),
            calculate_cmf_multi(features, windows=(20,)),
            calculate_accumulation_distribution(features),
            calculate_price_volume_trend(features),
            calculate_volume_price_confirmation(
                features, price_window=10, volume_window=20
            ),
            calculate_dollar_volume_proxy(features, windows=(20,)),
            calculate_liquidity_proxy(features, windows=(20,)),
            calculate_volume_percentile(features, source_col="volume", window=120),
        ]

        for comp in comps:
            for col in comp.columns:
                features[col] = comp[col]

        events = pd.DataFrame()
        event_summary = {}
        if include_events:
            cfg = VolumeEventConfig(
                disable_events_if_volume_unusable=disable_events_if_volume_unusable
            )
            events, event_summary = build_volume_event_frame(features, cfg)
            for col in events.columns:
                features[col] = events[col]

        features = features.replace([np.inf, -np.inf], np.nan)

        summary = self.validate_volume_features(features)
        summary["event_columns"] = list(events.columns) if include_events else []
        summary["event_count"] = int(events.sum().sum()) if include_events else 0

        return features, summary

    def validate_volume_features(self, df: pd.DataFrame) -> dict:
        total_cells = df.size
        nans = int(df.isna().sum().sum())
        usable = (
            df["volume_is_usable"].iloc[-1]
            if "volume_is_usable" in df.columns and not df.empty
            else False
        )
        ratio = (
            df["volume_valid_ratio"].iloc[-1]
            if "volume_valid_ratio" in df.columns and not df.empty
            else 0.0
        )

        warnings = []
        if not usable:
            warnings.append("Volume is flagged as unusable.")

        return {
            "input_rows": len(df),
            "output_rows": len(df),
            "feature_columns": [c for c in df.columns if not c.startswith("event_")],
            "feature_count": len([c for c in df.columns if not c.startswith("event_")]),
            "total_nan_ratio": nans / total_cells if total_cells > 0 else 0.0,
            "volume_usable": bool(usable),
            "volume_valid_ratio": float(ratio),
            "warnings": warnings,
            "failed_components": [],
        }
