import logging

import numpy as np
import pandas as pd

from config.settings import settings
from indicators.price_action_advanced import (
    calculate_body_features,
    calculate_breakout_distance,
    calculate_breakout_levels,
    calculate_candle_anatomy,
    calculate_candle_percentiles,
    calculate_candle_ratios,
    calculate_close_location_features,
    calculate_consecutive_candle_features,
    calculate_false_breakout_features,
    calculate_gap_features,
    calculate_inside_outside_bars,
    calculate_price_action_context,
    calculate_range_compression_expansion,
    calculate_range_features,
    calculate_wick_features,
)
from indicators.price_action_events import build_price_action_event_frame

logger = logging.getLogger(__name__)


class PriceActionFeatureSetBuilder:
    def __init__(self):
        self.windows = settings.default_price_action_windows
        self.breakout_windows = settings.default_breakout_windows
        self.percentile_window = settings.default_large_body_percentile_window

    def validate_price_action_features(self, df: pd.DataFrame) -> dict:
        """Validate input data."""
        if df is None or df.empty:
            return {"valid": False, "reason": "Empty dataframe"}
        required_cols = ["open", "high", "low", "close"]
        if not all(col in df.columns for col in required_cols):
            return {"valid": False, "reason": "Missing OHLC columns"}
        return {"valid": True, "reason": ""}

    def build_price_action_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        """Build the full price action feature set."""
        val_res = self.validate_price_action_features(df)
        if not val_res["valid"]:
            logger.warning(f"Validation failed: {val_res['reason']}")
            return pd.DataFrame(), {"warnings": [val_res["reason"]]}

        features_list = []
        failed_components = []

        try:
            features_list.append(calculate_candle_anatomy(df))
        except Exception as e:
            failed_components.append(f"anatomy: {str(e)}")

        try:
            features_list.append(calculate_candle_ratios(df))
        except Exception as e:
            failed_components.append(f"ratios: {str(e)}")

        try:
            features_list.append(calculate_close_location_features(df))
        except Exception as e:
            failed_components.append(f"close_location: {str(e)}")

        try:
            features_list.append(calculate_range_features(df, self.windows))
        except Exception as e:
            failed_components.append(f"range: {str(e)}")

        try:
            features_list.append(calculate_body_features(df, self.windows))
        except Exception as e:
            failed_components.append(f"body: {str(e)}")

        try:
            features_list.append(calculate_wick_features(df, (5, 10, 20)))
        except Exception as e:
            failed_components.append(f"wick: {str(e)}")

        try:
            features_list.append(calculate_gap_features(df))
        except Exception as e:
            failed_components.append(f"gap: {str(e)}")

        try:
            features_list.append(calculate_inside_outside_bars(df))
        except Exception as e:
            failed_components.append(f"inside_outside: {str(e)}")

        try:
            features_list.append(calculate_breakout_levels(df, self.breakout_windows))
        except Exception as e:
            failed_components.append(f"breakout_levels: {str(e)}")

        try:
            features_list.append(calculate_breakout_distance(df, self.breakout_windows))
        except Exception as e:
            failed_components.append(f"breakout_distance: {str(e)}")

        try:
            features_list.append(
                calculate_false_breakout_features(df, self.breakout_windows)
            )
        except Exception as e:
            failed_components.append(f"false_breakout: {str(e)}")

        try:
            features_list.append(
                calculate_range_compression_expansion(df, 20, self.percentile_window)
            )
        except Exception as e:
            failed_components.append(f"compression_expansion: {str(e)}")

        try:
            features_list.append(
                calculate_candle_percentiles(df, self.percentile_window)
            )
        except Exception as e:
            failed_components.append(f"percentiles: {str(e)}")

        try:
            features_list.append(calculate_consecutive_candle_features(df))
        except Exception as e:
            failed_components.append(f"consecutive: {str(e)}")

        try:
            features_list.append(calculate_price_action_context(df, (20, 50)))
        except Exception as e:
            failed_components.append(f"context: {str(e)}")

        # Combine
        if not features_list:
            return pd.DataFrame(), {"failed_components": failed_components}

        result_df = pd.concat(features_list, axis=1)

        # Remove duplicates if any
        result_df = result_df.loc[:, ~result_df.columns.duplicated()]

        # Clean infinities
        result_df = result_df.replace([np.inf, -np.inf], np.nan)

        event_cols = []
        if include_events:
            event_df, event_summary = build_price_action_event_frame(result_df)
            result_df = pd.concat([result_df, event_df], axis=1)
            event_cols = event_summary.get("event_columns", [])

        summary = {
            "input_rows": len(df),
            "output_rows": len(result_df),
            "feature_columns": [c for c in result_df.columns if c not in event_cols],
            "event_columns": event_cols,
            "feature_count": len([c for c in result_df.columns if c not in event_cols]),
            "event_count": len(event_cols),
            "total_nan_ratio": (
                result_df.isna().sum().sum() / (result_df.shape[0] * result_df.shape[1])
                if not result_df.empty
                else 0
            ),
            "warnings": [
                "Gap and breakout features may vary significantly depending on asset class (FX vs Commodities)."
            ],
            "failed_components": failed_components,
        }

        return result_df, summary

    def build_compact_price_action_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        """Build a smaller, essential price action feature set."""
        full_df, summary = self.build_price_action_features(df, include_events)
        if full_df.empty:
            return full_df, summary

        # Define compact columns
        compact_cols = [
            "candle_body",
            "candle_body_pct",
            "candle_range",
            "candle_range_pct",
            "body_to_range_ratio",
            "upper_wick_to_range_ratio",
            "lower_wick_to_range_ratio",
            "close_pos_range",
            "gap_pct",
            "abs_gap_pct",
            "inside_bar",
            "outside_bar",
            "dist_to_breakout_high_20",
            "dist_to_breakout_low_20",
            "false_breakout_upper_20",
            "false_breakout_lower_20",
            "range_compression_20",
            "range_expansion_20",
            f"candle_range_percentile_{self.percentile_window}",
            f"candle_body_percentile_{self.percentile_window}",
            "consecutive_up_closes",
            "consecutive_down_closes",
        ]

        # Select existing columns from the full set
        selected_cols = [c for c in compact_cols if c in full_df.columns]

        if include_events:
            selected_cols.extend(summary.get("event_columns", []))

        compact_df = full_df[selected_cols].copy()

        # Update summary
        event_cols = summary.get("event_columns", []) if include_events else []
        summary["feature_columns"] = [
            c for c in compact_df.columns if c not in event_cols
        ]
        summary["feature_count"] = len(summary["feature_columns"])
        summary["total_nan_ratio"] = (
            compact_df.isna().sum().sum() / (compact_df.shape[0] * compact_df.shape[1])
            if not compact_df.empty
            else 0
        )

        return compact_df, summary
