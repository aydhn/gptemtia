import logging
from typing import Tuple

import numpy as np
import pandas as pd

from config.settings import settings
from indicators.divergence import DivergenceConfig, build_divergence_feature_frame
from indicators.divergence_events import (
    DivergenceEventConfig,
    build_divergence_event_frame,
)
from indicators.divergence_pivots import PivotConfig, build_pivot_frame

logger = logging.getLogger(__name__)


class DivergenceFeatureSetBuilder:
    def __init__(self):
        self.div_config = DivergenceConfig()
        self.event_config = DivergenceEventConfig()
        self.pivot_config = PivotConfig(
            left=self.div_config.pivot_left, right=self.div_config.pivot_right
        )

    def build_divergence_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        """Builds the full divergence feature set including pivots, divergence values, and events."""
        out_df = pd.DataFrame(index=df.index)
        summary = {
            "input_rows": len(df),
            "output_rows": 0,
            "feature_columns": [],
            "event_columns": [],
            "feature_count": 0,
            "event_count": 0,
            "total_nan_ratio": 0.0,
            "missing_indicator_columns": [],
            "warnings": [],
            "failed_components": [],
        }

        if df.empty:
            summary["warnings"].append("Empty DataFrame provided.")
            return out_df, summary

        # Optional: Include OHLCV columns if desired, but we'll stick to just features

        # 1. Build Pivots
        try:
            pivot_df = build_pivot_frame(
                df,
                price_col="close",
                indicator_cols=list(self.div_config.indicator_columns),
                config=self.pivot_config,
            )
            out_df = out_df.join(pivot_df)
        except Exception as e:
            logger.error(f"Failed to build pivot frame: {e}")
            summary["failed_components"].append("pivots")

        # 2. Build Divergence Features
        try:
            div_df, div_summary = build_divergence_feature_frame(
                df, config=self.div_config
            )
            out_df = out_df.join(div_df)
            summary["missing_indicator_columns"] = div_summary.get(
                "missing_indicator_columns", []
            )
            summary["warnings"].extend(div_summary.get("warnings", []))
            summary["warnings"].extend(div_summary.get("notes", []))
        except Exception as e:
            logger.error(f"Failed to build divergence features: {e}")
            summary["failed_components"].append("divergence_features")
            div_df = pd.DataFrame()

        # 3. Build Events
        if include_events and not div_df.empty:
            try:
                event_df, event_summary = build_divergence_event_frame(
                    div_df, config=self.event_config
                )
                out_df = out_df.join(event_df)
                summary["event_columns"] = event_summary.get("event_columns", [])
                summary["warnings"].extend(event_summary.get("warnings", []))
            except Exception as e:
                logger.error(f"Failed to build divergence events: {e}")
                summary["failed_components"].append("divergence_events")

        # Cleanup
        out_df = out_df.replace([np.inf, -np.inf], np.nan)
        out_df = out_df.loc[:, ~out_df.columns.duplicated()]

        summary["output_rows"] = len(out_df)
        summary["feature_columns"] = [
            c for c in out_df.columns if not c.startswith("event_")
        ]
        summary["feature_count"] = len(summary["feature_columns"])
        summary["event_count"] = len(summary["event_columns"])
        summary["total_nan_ratio"] = (
            float(out_df.isna().mean().mean())
            if len(out_df) > 0 and len(out_df.columns) > 0
            else 0.0
        )

        return out_df, summary

    def build_compact_divergence_features(
        self,
        df: pd.DataFrame,
        include_events: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        """Builds a smaller, more focused set of divergence features."""
        # For now, just generate everything and filter columns
        # In a real setup, we might optimize computation
        full_df, summary = self.build_divergence_features(
            df, include_events=include_events
        )

        if full_df.empty:
            return full_df, summary

        compact_cols = [
            c
            for c in full_df.columns
            if c.startswith("div_regular_")
            or c.startswith("div_strength_")
            or c.startswith("event_")
        ]

        out_df = full_df[compact_cols]

        summary["feature_columns"] = [
            c for c in out_df.columns if not c.startswith("event_")
        ]
        summary["feature_count"] = len(summary["feature_columns"])
        summary["total_nan_ratio"] = (
            float(out_df.isna().mean().mean())
            if len(out_df) > 0 and len(out_df.columns) > 0
            else 0.0
        )

        return out_df, summary

    def validate_divergence_features(self, df: pd.DataFrame) -> dict:
        """Validates the structure and content of divergence features."""
        result = {"valid": True, "errors": [], "warnings": [], "nan_ratios": {}}

        if df.empty:
            result["valid"] = False
            result["errors"].append("DataFrame is empty")
            return result

        for col in df.columns:
            nan_ratio = df[col].isna().mean()
            result["nan_ratios"][col] = nan_ratio
            if nan_ratio == 1.0:
                result["warnings"].append(f"Column {col} is 100% NaN")

            if np.isinf(df[col]).any():
                result["valid"] = False
                result["errors"].append(f"Column {col} contains infinite values")

            if (
                col.startswith("event_")
                or col.startswith("div_regular_")
                or col.startswith("div_hidden_")
            ):
                unique_vals = set(df[col].dropna().unique())
                if not unique_vals.issubset({0, 1, 0.0, 1.0}):
                    result["warnings"].append(
                        f"Column {col} contains values other than 0 and 1: {unique_vals}"
                    )

        return result
