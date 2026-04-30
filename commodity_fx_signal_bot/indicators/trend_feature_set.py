from typing import Tuple

import numpy as np
import pandas as pd

from indicators.trend_advanced import (
    calculate_multi_sma,
    calculate_multi_ema,
    calculate_wma,
    calculate_multi_wma,
    calculate_multi_hma,
    calculate_multi_macd,
    calculate_multi_adx,
    calculate_multi_aroon,
    calculate_ichimoku_full,
    calculate_price_ma_distances,
    calculate_ma_slopes,
    calculate_ma_stack_state,
    calculate_trend_persistence,
)
from indicators.trend_events import build_trend_event_frame


class TrendFeatureSetBuilder:
    def __init__(self):
        pass

    def build_trend_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:

        if df.empty:
            return df.copy(), {"error": "Empty dataframe"}

        features_list = []

        # Keep OHLCV base
        features_list.append(df.copy())

        try:
            features_list.append(calculate_multi_sma(df))
            features_list.append(calculate_multi_ema(df))
            features_list.append(calculate_wma(df, window=20))
            features_list.append(calculate_multi_wma(df))
            features_list.append(calculate_multi_hma(df))
            features_list.append(calculate_multi_macd(df))
            features_list.append(calculate_multi_adx(df))
            features_list.append(calculate_multi_aroon(df))
            features_list.append(calculate_ichimoku_full(df))
        except Exception as e:
             return df.copy(), {"error": f"Failed to calculate core indicators: {e}"}

        # Combine so far to calculate derivations
        combined_core = pd.concat(features_list, axis=1)
        # remove duplicate columns
        combined_core = combined_core.loc[:, ~combined_core.columns.duplicated()]

        deriv_list = []
        try:
            deriv_list.append(calculate_price_ma_distances(
                combined_core,
                ["sma_20", "sma_50", "sma_200", "ema_20", "ema_50"]
            ))
            deriv_list.append(calculate_ma_slopes(
                combined_core,
                ["sma_20", "ema_20"],
                slope_window=5
            ))
            deriv_list.append(calculate_ma_stack_state(
                combined_core,
                "ema_20", "ema_50", "ema_200"
            ))
            if "close" in combined_core.columns:
                deriv_list.append(calculate_trend_persistence(
                    combined_core["close"], window=10
                ))
        except Exception as e:
             return combined_core, {"error": f"Failed to calculate derived indicators: {e}"}

        features_list.extend(deriv_list)

        features = pd.concat(features_list, axis=1)
        features = features.loc[:, ~features.columns.duplicated()]

        features.replace([np.inf, -np.inf], np.nan, inplace=True)

        event_columns = []
        event_count = 0
        if include_events:
            events_df, events_summary = build_trend_event_frame(features)
            if not events_df.empty:
                event_columns = events_df.columns.tolist()
                event_count = events_summary["total_event_count"]
                features = pd.concat([features, events_df], axis=1)
                features = features.loc[:, ~features.columns.duplicated()]

        feature_cols = [c for c in features.columns if c not in df.columns and c not in event_columns]

        total_nans = features.isna().sum().sum()
        total_cells = features.size
        nan_ratio = float(total_nans / total_cells) if total_cells > 0 else 0.0

        summary = {
            "input_rows": len(df),
            "output_rows": len(features),
            "feature_columns": feature_cols,
            "event_columns": event_columns,
            "feature_count": len(feature_cols),
            "event_count": event_count,
            "total_nan_ratio": nan_ratio,
            "warnings": ["WARNING: Ichimoku chikou span introduces forward-looking data (leakage). Use with caution."],
            "failed_components": []
        }

        return features, summary

    def build_compact_trend_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:

        if df.empty:
            return df.copy(), {"error": "Empty dataframe"}

        features_list = []
        features_list.append(df.copy())

        try:
            features_list.append(calculate_multi_sma(df, windows=(20, 50, 200)))
            features_list.append(calculate_multi_ema(df, windows=(20, 50, 200)))
            features_list.append(calculate_multi_macd(df, configs=((12, 26, 9),)))
            features_list.append(calculate_multi_adx(df, windows=(14,)))
            features_list.append(calculate_multi_aroon(df, windows=(25,)))
        except Exception as e:
             return df.copy(), {"error": f"Failed to calculate core indicators: {e}"}

        combined_core = pd.concat(features_list, axis=1)
        combined_core = combined_core.loc[:, ~combined_core.columns.duplicated()]

        deriv_list = []
        try:
            deriv_list.append(calculate_price_ma_distances(
                combined_core,
                ["ema_20", "ema_50", "sma_200"]
            ))
            deriv_list.append(calculate_ma_slopes(
                combined_core,
                ["ema_20", "sma_50"],
                slope_window=5
            ))
            deriv_list.append(calculate_ma_stack_state(
                combined_core,
                "ema_20", "ema_50", "ema_200"
            ))
        except Exception as e:
             return combined_core, {"error": f"Failed to calculate derived indicators: {e}"}

        features_list.extend(deriv_list)

        features = pd.concat(features_list, axis=1)
        features = features.loc[:, ~features.columns.duplicated()]

        features.replace([np.inf, -np.inf], np.nan, inplace=True)

        event_columns = []
        event_count = 0
        if include_events:
            events_df, events_summary = build_trend_event_frame(features)
            if not events_df.empty:
                event_columns = events_df.columns.tolist()
                event_count = events_summary["total_event_count"]
                features = pd.concat([features, events_df], axis=1)
                features = features.loc[:, ~features.columns.duplicated()]

        feature_cols = [c for c in features.columns if c not in df.columns and c not in event_columns]

        total_nans = features.isna().sum().sum()
        total_cells = features.size
        nan_ratio = float(total_nans / total_cells) if total_cells > 0 else 0.0

        summary = {
            "input_rows": len(df),
            "output_rows": len(features),
            "feature_columns": feature_cols,
            "event_columns": event_columns,
            "feature_count": len(feature_cols),
            "event_count": event_count,
            "total_nan_ratio": nan_ratio,
            "warnings": [],
            "failed_components": []
        }

        return features, summary

    def validate_trend_features(self, df: pd.DataFrame) -> dict:
        if df.empty:
            return {"valid": False, "reason": "Empty features DataFrame"}

        has_inf = np.isinf(df.select_dtypes(include=[np.number])).values.any()
        nan_ratio = float(df.isna().sum().sum() / df.size)

        return {
            "valid": not has_inf and nan_ratio < 0.99,
            "has_inf": bool(has_inf),
            "nan_ratio": nan_ratio,
            "rows": len(df),
            "columns": len(df.columns),
        }
