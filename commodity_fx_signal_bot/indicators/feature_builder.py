import logging
from typing import Optional, Tuple

import numpy as np
import pandas as pd

from indicators.indicator_config import get_indicator_spec
from indicators.registry import GLOBAL_INDICATOR_REGISTRY, IndicatorRegistry

logger = logging.getLogger(__name__)


class FeatureBuilder:
    def __init__(self, registry: Optional[IndicatorRegistry] = None):
        self.registry = registry or GLOBAL_INDICATOR_REGISTRY
        from indicators.registry import register_builtin_indicators

        register_builtin_indicators()

    def build_features(
        self,
        df: pd.DataFrame,
        indicator_names: Optional[list[str]] = None,
        drop_warmup: bool = False,
    ) -> Tuple[pd.DataFrame, dict]:

        if df.empty:
            return df, {"error": "Empty dataframe"}

        features = df.copy()
        summary = {
            "input_rows": len(df),
            "output_rows": len(df),
            "feature_columns": [],
            "indicator_count": 0,
            "failed_indicators": [],
            "nan_ratio_by_column": {},
            "total_nan_ratio": 0.0,
            "warmup_max": 0,
        }

        if not indicator_names:
            return features, summary

        max_warmup = 0

        for name in indicator_names:
            try:
                func = self.registry.get(name)
                spec = get_indicator_spec(name)

                max_warmup = max(max_warmup, spec.warmup_period)

                result_df = func(features, **spec.default_params)

                # Check for duplicates and add to features
                for col in result_df.columns:
                    if col in features.columns:
                        col_name = f"{col}_dup"
                        features[col_name] = result_df[col]
                        summary["feature_columns"].append(col_name)
                    else:
                        features[col] = result_df[col]
                        summary["feature_columns"].append(col)

                summary["indicator_count"] += 1

            except Exception as e:
                logger.error(f"Failed to calculate indicator {name}: {e}")
                summary["failed_indicators"].append(name)

        # Clean infinities
        features.replace([np.inf, -np.inf], np.nan, inplace=True)

        summary["warmup_max"] = max_warmup

        if drop_warmup and max_warmup > 0:
            features = features.iloc[max_warmup:].copy()
            summary["output_rows"] = len(features)

        # Calculate NaN ratios
        total_nans = features.isna().sum().sum()
        total_cells = features.size
        summary["total_nan_ratio"] = (
            float(total_nans / total_cells) if total_cells > 0 else 0.0
        )

        for col in features.columns:
            summary["nan_ratio_by_column"][col] = float(features[col].isna().mean())

        return features, summary

    def build_default_feature_set(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, dict]:
        default_indicators = [
            "rsi_14",
            "sma_20",
            "sma_50",
            "ema_20",
            "ema_50",
            "macd_12_26_9",
            "atr_14",
            "bollinger_20_2",
            "historical_volatility_20",
            "zscore_close_20",
            "distance_from_sma_20",
            "candle_body",
            "candle_range",
            "close_position_in_range",
            "return_1",
            "return_5",
            "log_return_1",
            "volume_sma_20",
            "volume_zscore_20",
        ]

        # Filter available ones
        available = [name for name in default_indicators if self.registry.exists(name)]
        return self.build_features(df, indicator_names=available)

    def build_trend_feature_set(
        self,
        df: pd.DataFrame,
        compact: bool = True,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:

        from indicators.trend_feature_set import TrendFeatureSetBuilder

        builder = TrendFeatureSetBuilder()
        if compact:
            return builder.build_compact_trend_features(df, include_events)
        else:
            return builder.build_trend_features(df, include_events)

    def build_volatility_feature_set(
        self,
        df: pd.DataFrame,
        compact: bool = True,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:

        from indicators.volatility_feature_set import VolatilityFeatureSetBuilder

        builder = VolatilityFeatureSetBuilder()
        if compact:
            return builder.build_compact_volatility_features(df, include_events)
        else:
            return builder.build_volatility_features(df, include_events)

    def build_divergence_feature_set(
        self,
        df: pd.DataFrame,
        compact: bool = True,
        include_events: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        """
        Builds divergence feature set (regular/hidden divergences, pivots, events).
        """
        from indicators.divergence_feature_set import DivergenceFeatureSetBuilder

        builder = DivergenceFeatureSetBuilder()
        if compact:
            features, summary = builder.build_compact_divergence_features(
                df, include_events=include_events
            )
            summary["type"] = "compact_divergence"
        else:
            features, summary = builder.build_divergence_features(
                df, include_events=include_events
            )
            summary["type"] = "full_divergence"

        return features, summary

    def validate_feature_frame(self, features: pd.DataFrame) -> dict:
        if features.empty:
            return {"valid": False, "reason": "Empty features DataFrame"}

        has_inf = np.isinf(features.select_dtypes(include=[np.number])).values.any()
        nan_ratio = float(features.isna().sum().sum() / features.size)

        return {
            "valid": not has_inf and nan_ratio < 0.99,
            "has_inf": bool(has_inf),
            "nan_ratio": nan_ratio,
            "rows": len(features),
            "columns": len(features.columns),
        }

    def build_mean_reversion_feature_set(
        self,
        df: pd.DataFrame,
        compact: bool = True,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        from indicators.mean_reversion_feature_set import MeanReversionFeatureSetBuilder

        builder = MeanReversionFeatureSetBuilder()
        if compact:
            return builder.build_compact_mean_reversion_features(
                df, include_events=include_events
            )
        else:
            return builder.build_mean_reversion_features(
                df, include_events=include_events
            )

    def build_price_action_feature_set(
        self,
        df: pd.DataFrame,
        compact: bool = True,
        include_events: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        from indicators.price_action_feature_set import PriceActionFeatureSetBuilder
        builder = PriceActionFeatureSetBuilder()
        if compact:
            return builder.build_compact_price_action_features(
                df, include_events=include_events
            )
        return builder.build_price_action_features(df, include_events=include_events)

    def build_price_action_feature_set(
        self,
        df: pd.DataFrame,
        compact: bool = True,
        include_events: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        from indicators.price_action_feature_set import PriceActionFeatureSetBuilder
        builder = PriceActionFeatureSetBuilder()
        if compact:
            return builder.build_compact_price_action_features(
                df, include_events=include_events
            )
        return builder.build_price_action_features(df, include_events=include_events)

    def build_price_action_feature_set(
        self,
        df: pd.DataFrame,
        compact: bool = True,
        include_events: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        from indicators.price_action_feature_set import PriceActionFeatureSetBuilder
        builder = PriceActionFeatureSetBuilder()
        if compact:
            return builder.build_compact_price_action_features(
                df, include_events=include_events
            )
        return builder.build_price_action_features(df, include_events=include_events)

    def build_price_action_feature_set(
        self,
        df: pd.DataFrame,
        compact: bool = True,
        include_events: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        from indicators.price_action_feature_set import PriceActionFeatureSetBuilder

        from indicators.price_action_feature_set import PriceActionFeatureSetBuilder
        builder = PriceActionFeatureSetBuilder()
        if compact:
            return builder.build_compact_price_action_features(
                df, include_events=include_events
            )
        return builder.build_price_action_features(df, include_events=include_events)
