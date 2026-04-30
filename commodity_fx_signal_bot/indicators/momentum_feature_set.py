import logging
from typing import Tuple, Optional

import numpy as np
import pandas as pd

from config.settings import settings
from indicators.momentum_advanced import (
    calculate_multi_rsi,
    calculate_multi_roc,
    calculate_multi_momentum,
    calculate_multi_stochastic,
    calculate_multi_williams_r,
    calculate_cci,
    calculate_momentum_slope,
    calculate_momentum_acceleration,
)
from indicators.momentum_events import build_momentum_event_frame, MomentumEventConfig

logger = logging.getLogger(__name__)


class MomentumFeatureSetBuilder:
    def __init__(self):
        self.config = MomentumEventConfig(
            rsi_overbought=settings.default_momentum_overbought_rsi,
            rsi_oversold=settings.default_momentum_oversold_rsi,
            stochastic_overbought=settings.default_stochastic_overbought,
            stochastic_oversold=settings.default_stochastic_oversold,
        )

    def _clean_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df = df.loc[:, ~df.columns.duplicated()]
        return df

    def build_momentum_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        if df.empty:
            return df, {"error": "Empty dataframe"}
        features_list = [df]
        try:
            features_list.append(
                calculate_multi_rsi(df, windows=settings.default_momentum_windows)
            )
        except Exception as e:
            logger.warning(f"Failed to calculate multi RSI: {e}")
        try:
            features_list.append(
                calculate_multi_roc(df, windows=settings.default_roc_windows)
            )
        except Exception as e:
            logger.warning(f"Failed to calculate multi ROC: {e}")
        try:
            features_list.append(
                calculate_multi_momentum(df, windows=settings.default_roc_windows)
            )
        except Exception as e:
            logger.warning(f"Failed to calculate multi Momentum: {e}")
        try:
            features_list.append(calculate_multi_stochastic(df, windows=(14, 21)))
        except Exception as e:
            logger.warning(f"Failed to calculate multi Stochastic: {e}")
        try:
            features_list.append(calculate_multi_williams_r(df, windows=(14, 21)))
        except Exception as e:
            logger.warning(f"Failed to calculate multi Williams %R: {e}")
        try:
            features_list.append(calculate_cci(df, window=20))
        except Exception as e:
            logger.warning(f"Failed to calculate CCI: {e}")

        feature_df = pd.concat(features_list, axis=1)
        feature_df = self._clean_dataframe(feature_df)

        deriv_features = []
        if "rsi_14" in feature_df.columns:
            deriv_features.append(
                calculate_momentum_slope(feature_df, "rsi_14", window=5)
            )
            deriv_features.append(
                calculate_momentum_acceleration(feature_df, "rsi_14", window=5)
            )
        if "roc_10" in feature_df.columns:
            deriv_features.append(
                calculate_momentum_slope(feature_df, "roc_10", window=5)
            )

        if deriv_features:
            feature_df = pd.concat([feature_df] + deriv_features, axis=1)
            feature_df = self._clean_dataframe(feature_df)

        event_cols = []
        event_summary = {}

        if include_events and getattr(settings, "momentum_events_enabled", True):
            try:
                event_df, event_summary = build_momentum_event_frame(
                    feature_df, self.config
                )
                if not event_df.empty:
                    feature_df = pd.concat([feature_df, event_df], axis=1)
                    feature_df = self._clean_dataframe(feature_df)
                    event_cols = event_summary.get("event_columns", [])
            except Exception as e:
                logger.error(f"Failed to build momentum events: {e}")

        all_cols = feature_df.columns.tolist()
        input_cols = df.columns.tolist()
        feat_cols = [c for c in all_cols if c not in input_cols and c not in event_cols]

        total_nans = feature_df.isna().sum().sum()
        total_cells = feature_df.size
        nan_ratio = float(total_nans / total_cells) if total_cells > 0 else 0.0

        summary = {
            "input_rows": len(df),
            "output_rows": len(feature_df),
            "feature_columns": feat_cols,
            "event_columns": event_cols,
            "feature_count": len(feat_cols),
            "event_count": len(event_cols),
            "total_nan_ratio": nan_ratio,
            "failed_components": [],
            "warnings": [],
            "event_summary": event_summary,
        }
        return feature_df, summary

    def build_compact_momentum_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        if df.empty:
            return df, {"error": "Empty dataframe"}
        features_list = [df]
        try:
            features_list.append(calculate_multi_rsi(df, windows=(14, 21)))
            features_list.append(calculate_multi_roc(df, windows=(10, 20)))
            features_list.append(calculate_multi_momentum(df, windows=(10,)))
            features_list.append(calculate_multi_stochastic(df, windows=(14,)))
            features_list.append(calculate_multi_williams_r(df, windows=(14,)))
            features_list.append(calculate_cci(df, window=20))
        except Exception as e:
            logger.warning(f"Error building compact momentum base features: {e}")

        feature_df = pd.concat(features_list, axis=1)
        feature_df = self._clean_dataframe(feature_df)

        if "rsi_14" in feature_df.columns:
            slope_df = calculate_momentum_slope(feature_df, "rsi_14", window=5)
            feature_df = pd.concat([feature_df, slope_df], axis=1)
            feature_df = self._clean_dataframe(feature_df)

        event_cols = []
        event_summary = {}

        if include_events and getattr(settings, "momentum_events_enabled", True):
            try:
                event_df, event_summary = build_momentum_event_frame(
                    feature_df, self.config
                )
                if not event_df.empty:
                    feature_df = pd.concat([feature_df, event_df], axis=1)
                    feature_df = self._clean_dataframe(feature_df)
                    event_cols = event_summary.get("event_columns", [])
            except Exception as e:
                logger.error(f"Failed to build compact momentum events: {e}")

        all_cols = feature_df.columns.tolist()
        input_cols = df.columns.tolist()
        feat_cols = [c for c in all_cols if c not in input_cols and c not in event_cols]

        total_nans = feature_df.isna().sum().sum()
        total_cells = feature_df.size
        nan_ratio = float(total_nans / total_cells) if total_cells > 0 else 0.0

        summary = {
            "input_rows": len(df),
            "output_rows": len(feature_df),
            "feature_columns": feat_cols,
            "event_columns": event_cols,
            "feature_count": len(feat_cols),
            "event_count": len(event_cols),
            "total_nan_ratio": nan_ratio,
            "failed_components": [],
            "warnings": [],
            "event_summary": event_summary,
        }
        return feature_df, summary

    def validate_momentum_features(self, df: pd.DataFrame) -> dict:
        if df.empty:
            return {"valid": False, "reason": "Empty DataFrame"}
        has_inf = np.isinf(df.select_dtypes(include=[np.number])).values.any()
        nan_ratio = float(df.isna().sum().sum() / df.size) if df.size > 0 else 1.0
        return {
            "valid": not has_inf and nan_ratio < 0.99,
            "has_inf": bool(has_inf),
            "nan_ratio": nan_ratio,
            "rows": len(df),
            "columns": len(df.columns),
        }
