import logging
from typing import Tuple

import numpy as np
import pandas as pd

from config.settings import settings
from indicators.mean_reversion_advanced import (
    calculate_bollinger_reversion_features,
    calculate_channel_deviation_features,
    calculate_multi_ema_distance,
    calculate_multi_percentile_rank,
    calculate_multi_rolling_mean_distance,
    calculate_multi_sma_distance,
    calculate_multi_zscore_close,
    calculate_overextension_score,
    calculate_range_position_features,
    calculate_reversion_half_life_proxy,
    calculate_rolling_minmax_position,
    calculate_rolling_percentile_rank,
    calculate_snapback_pressure,
)
from indicators.mean_reversion_events import build_mean_reversion_event_frame

logger = logging.getLogger(__name__)


class MeanReversionFeatureSetBuilder:
    def __init__(self):
        self.default_windows = getattr(
            settings, "default_reversion_windows", (20, 50, 100)
        )
        self.zscore_windows = getattr(settings, "default_zscore_windows", (20, 50, 100))
        self.percentile_window = getattr(settings, "default_percentile_window", 120)

    def build_mean_reversion_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        return self._build(df, compact=False, include_events=include_events)

    def build_compact_mean_reversion_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        return self._build(df, compact=True, include_events=include_events)

    def _build(
        self,
        df: pd.DataFrame,
        compact: bool,
        include_events: bool,
    ) -> Tuple[pd.DataFrame, dict]:
        features = df.copy()
        failed = []

        try:
            if compact:
                z = calculate_multi_zscore_close(df, windows=(20, 50))
            else:
                z = calculate_multi_zscore_close(df, windows=self.zscore_windows)
            features = pd.concat([features, z], axis=1)
        except Exception as e:
            failed.append(f"zscore: {e}")

        try:
            if compact:
                rmd = calculate_multi_rolling_mean_distance(df, windows=(20,))
            else:
                rmd = calculate_multi_rolling_mean_distance(
                    df, windows=self.default_windows
                )
            features = pd.concat([features, rmd], axis=1)
        except Exception as e:
            failed.append(f"rolling_mean_distance: {e}")

        try:
            if compact:
                sma_d = calculate_multi_sma_distance(df, windows=(20, 50))
            else:
                sma_d = calculate_multi_sma_distance(df, windows=(20, 50, 100, 200))
            features = pd.concat([features, sma_d], axis=1)
        except Exception as e:
            failed.append(f"sma_distance: {e}")

        try:
            if compact:
                ema_d = calculate_multi_ema_distance(df, windows=(20,))
            else:
                ema_d = calculate_multi_ema_distance(df, windows=(20, 50, 100, 200))
            features = pd.concat([features, ema_d], axis=1)
        except Exception as e:
            failed.append(f"ema_distance: {e}")

        try:
            if compact:
                p = calculate_rolling_percentile_rank(df, window=120)
            else:
                p = calculate_multi_percentile_rank(df, windows=(60, 120, 252))
            features = pd.concat([features, p], axis=1)
        except Exception as e:
            failed.append(f"percentile_rank: {e}")

        try:
            if compact:
                m = calculate_rolling_minmax_position(df, windows=(50,))
            else:
                m = calculate_rolling_minmax_position(df, windows=self.default_windows)
            features = pd.concat([features, m], axis=1)
        except Exception as e:
            failed.append(f"minmax_position: {e}")

        try:
            if compact:
                bb = calculate_bollinger_reversion_features(df, windows=(20,))
            else:
                bb = calculate_bollinger_reversion_features(df, windows=(20, 50))
            features = pd.concat([features, bb], axis=1)
        except Exception as e:
            failed.append(f"bollinger_reversion: {e}")

        try:
            if compact:
                cd = calculate_channel_deviation_features(df, windows=(20,))
            else:
                cd = calculate_channel_deviation_features(df, windows=(20, 55))
            features = pd.concat([features, cd], axis=1)
        except Exception as e:
            failed.append(f"channel_deviation: {e}")

        try:
            oes = calculate_overextension_score(df, window=20)
            features = pd.concat([features, oes], axis=1)
        except Exception as e:
            failed.append(f"overextension_score: {e}")

        try:
            sp = calculate_snapback_pressure(features, zscore_col="zscore_close_20")
            features = pd.concat([features, sp], axis=1)
        except Exception as e:
            failed.append(f"snapback_pressure: {e}")

        if not compact:
            try:
                hlp = calculate_reversion_half_life_proxy(df, window=50)
                features = pd.concat([features, hlp], axis=1)
            except Exception as e:
                failed.append(f"half_life_proxy: {e}")

        try:
            if compact:
                rp = calculate_range_position_features(df, windows=(50,))
            else:
                rp = calculate_range_position_features(df, windows=self.default_windows)
            features = pd.concat([features, rp], axis=1)
        except Exception as e:
            failed.append(f"range_position: {e}")

        # Remove duplicate columns if any
        features = features.loc[:, ~features.columns.duplicated()]

        # Replace infinity
        features = features.replace([np.inf, -np.inf], np.nan)

        event_cols = []
        event_count = 0
        if include_events:
            events_df, events_summary = build_mean_reversion_event_frame(features)
            if not events_df.empty:
                features = pd.concat([features, events_df], axis=1)
                event_cols = events_summary.get("event_columns", [])
                event_count = events_summary.get("total_event_count", 0)

        # Exclude OHLCV from feature columns list for summary, but keep them in dataframe
        base_cols = ["open", "high", "low", "close", "adj_close", "volume"]
        feature_cols = [
            c for c in features.columns if c not in base_cols and c not in event_cols
        ]

        total_nan = features[feature_cols].isna().sum().sum()
        total_cells = len(features) * len(feature_cols)
        nan_ratio = float(total_nan / total_cells) if total_cells > 0 else 0.0

        warnings = []
        warnings.append(
            "Mean reversion events are candidates, not direct buy/sell signals."
        )
        warnings.append(
            "Mean reversion can be extremely risky during strong trends. Use trend filters."
        )

        summary = {
            "type": "compact" if compact else "full",
            "input_rows": len(df),
            "output_rows": len(features),
            "feature_columns": feature_cols,
            "event_columns": event_cols,
            "feature_count": len(feature_cols),
            "event_count": event_count,
            "total_nan_ratio": nan_ratio,
            "warnings": warnings,
            "failed_components": failed,
        }

        return features, summary

    def validate_mean_reversion_features(self, df: pd.DataFrame) -> dict:
        has_inf = np.isinf(df.select_dtypes(include=[np.number])).any().any()
        return {
            "valid": True,
            "has_inf": bool(has_inf),
        }
