import logging
from typing import Tuple

import numpy as np
import pandas as pd

from indicators.indicator_config import get_indicator_spec
from indicators.registry import GLOBAL_INDICATOR_REGISTRY, IndicatorRegistry
from indicators.volatility_events import build_volatility_event_frame

logger = logging.getLogger(__name__)


class VolatilityFeatureSetBuilder:
    def __init__(self, registry: IndicatorRegistry | None = None):
        self.registry = registry or GLOBAL_INDICATOR_REGISTRY
        from indicators.registry import register_builtin_indicators
        register_builtin_indicators()

    def build_volatility_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        """Build the full comprehensive set of volatility features."""

        indicators_to_build = [
            "multi_true_range",
            "multi_atr",
            "atr_percent",
            "multi_bollinger_bands",
            "multi_keltner_channels",
            "multi_donchian_channels",
            "historical_volatility_multi",
            "parkinson_volatility",
            "garman_klass_volatility",
            "range_percent",
            "gap_volatility",
            "volatility_percentile",
            "volatility_slope",
            "channel_position"
        ]

        return self._build_feature_set(df, indicators_to_build, include_events, "full")

    def build_compact_volatility_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        """Build a lighter weight compact set of volatility features for ML/Backtest."""

        # We use a custom spec or the existing ones but pick and choose what to return
        # Since our registry functions are mostly configurable, we can just call them
        # or use specific registered variants if they exist.
        indicators_to_build = [
            "true_range",
            "atr_14",
            "atr_percent",
            "bollinger_20_2",
            "keltner_20",
            "donchian_20",
            "historical_volatility_20",
            "parkinson_volatility",
            "garman_klass_volatility",
            "range_percent",
            "gap_volatility",
            "volatility_percentile",
            "volatility_slope"
        ]

        return self._build_feature_set(df, indicators_to_build, include_events, "compact")

    def _build_feature_set(self, df: pd.DataFrame, indicator_names: list[str], include_events: bool, set_type: str) -> Tuple[pd.DataFrame, dict]:

        if df.empty:
            return df, {"error": "Empty dataframe"}

        features = df.copy()
        summary = {
            "input_rows": len(df),
            "output_rows": len(df),
            "feature_columns": [],
            "event_columns": [],
            "feature_count": 0,
            "event_count": 0,
            "failed_components": [],
            "total_nan_ratio": 0.0,
            "warnings": [],
            "type": set_type
        }

        max_warmup = 0

        for name in indicator_names:
            try:
                if self.registry.exists(name):
                    func = self.registry.get(name)
                    spec = get_indicator_spec(name)

                    max_warmup = max(max_warmup, spec.warmup_period)

                    # For volatility percentile, slope, and channel pos we need inputs that we might just have created
                    # But if we're using the registered function, we just pass the dataframe
                    result_df = func(features, **spec.default_params)

                    for col in result_df.columns:
                        if col not in features.columns:
                            features[col] = result_df[col]
                            summary["feature_columns"].append(col)
                else:
                    summary["failed_components"].append(name)
            except Exception as e:
                logger.error(f"Failed to calculate volatility indicator {name}: {e}")
                summary["failed_components"].append(name)

        # Handle events if requested
        if include_events:
            try:
                event_df, event_summary = build_volatility_event_frame(features)
                for col in event_df.columns:
                    if col not in features.columns:
                        features[col] = event_df[col]
                        summary["event_columns"].append(col)

                if "notes" in event_summary:
                    summary["warnings"].append(event_summary["notes"])

            except Exception as e:
                logger.error(f"Failed to calculate volatility events: {e}")
                summary["failed_components"].append("volatility_events")

        # Clean infinities
        features = features.replace([np.inf, -np.inf], np.nan)

        summary["feature_count"] = len(summary["feature_columns"])
        summary["event_count"] = len(summary["event_columns"])

        # Calculate NaN ratios
        total_nans = features.isna().sum().sum()
        total_cells = features.size
        summary["total_nan_ratio"] = (
            float(total_nans / total_cells) if total_cells > 0 else 0.0
        )

        return features, summary

    def validate_volatility_features(self, df: pd.DataFrame) -> dict:
        """Validate the resulting feature set."""
        if df.empty:
            return {"valid": False, "reason": "Empty features DataFrame"}

        # Select only numeric types just in case
        numeric_df = df.select_dtypes(include=[np.number])
        if numeric_df.empty:
             return {"valid": False, "reason": "No numeric columns in DataFrame"}

        has_inf = np.isinf(numeric_df).values.any()
        nan_ratio = float(df.isna().sum().sum() / df.size)

        return {
            "valid": not has_inf and nan_ratio < 0.99,
            "has_inf": bool(has_inf),
            "nan_ratio": nan_ratio,
            "rows": len(df),
            "columns": len(df.columns),
        }
