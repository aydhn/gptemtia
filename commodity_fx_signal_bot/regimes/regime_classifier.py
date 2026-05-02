"""
Central regime classifier to combine sub-regimes.
"""

import pandas as pd
import numpy as np
from dataclasses import dataclass

from regimes.regime_config import RegimeProfile, get_default_regime_profile
from regimes.regime_labels import UNKNOWN, INSUFFICIENT_DATA, CONFLICTING_REGIME


@dataclass
class RegimeClassificationResult:
    dataframe: pd.DataFrame
    summary: dict


class RegimeClassifier:
    def __init__(self, profile: RegimeProfile | None = None):
        self.profile = profile or get_default_regime_profile()

    def classify(self, df: pd.DataFrame) -> RegimeClassificationResult:
        out_df = pd.DataFrame(index=df.index)
        summary = {"input_rows": len(df), "warnings": []}

        # We assume the input df already contains the feature columns
        # from the sub-detectors (regime_trend_label, regime_volatility_label, etc.)

        primary_label = pd.Series(UNKNOWN, index=df.index)
        secondary_label = pd.Series(UNKNOWN, index=df.index)
        confidence = pd.Series(0.0, index=df.index)

        # Check if we have the minimum required columns to classify
        required_scores = []
        if "regime_trend_score" in df.columns:
            required_scores.append(df["regime_trend_score"])
            out_df["regime_trend_component"] = df["regime_trend_score"]
        else:
            out_df["regime_trend_component"] = np.nan

        if "regime_volatility_score" in df.columns:
            required_scores.append(df["regime_volatility_score"])
            out_df["regime_volatility_component"] = df["regime_volatility_score"]
        else:
            out_df["regime_volatility_component"] = np.nan

        if "regime_range_score" in df.columns:
            out_df["regime_range_component"] = df["regime_range_score"]
        else:
            out_df["regime_range_component"] = np.nan

        if "regime_momentum_score" in df.columns:
            out_df["regime_momentum_component"] = df["regime_momentum_score"]
        else:
            out_df["regime_momentum_component"] = np.nan

        if "regime_mean_reversion_score" in df.columns:
            out_df["regime_mean_reversion_component"] = df[
                "regime_mean_reversion_score"
            ]
        else:
            out_df["regime_mean_reversion_component"] = np.nan

        if "regime_mtf_score" in df.columns:
            out_df["regime_mtf_component"] = df["regime_mtf_score"]
        else:
            out_df["regime_mtf_component"] = np.nan

        if "regime_is_mtf_conflict" in df.columns:
            out_df["regime_conflict_component"] = df["regime_is_mtf_conflict"].astype(
                float
            )
        else:
            out_df["regime_conflict_component"] = np.nan

        if not required_scores:
            summary["warnings"].append("No regime scores found. Cannot classify.")
            primary_label[:] = INSUFFICIENT_DATA
            out_df["regime_primary_label"] = primary_label
            out_df["regime_secondary_label"] = secondary_label
            out_df["regime_confidence"] = confidence
            return RegimeClassificationResult(out_df, summary)

        # Determine labels based on hierarchy

        # 1. MTF Conflict is highest priority if present
        if "regime_mtf_label" in df.columns:
            mask = df["regime_mtf_label"] == "mtf_conflict"
            primary_label[mask] = CONFLICTING_REGIME
            confidence[mask] = 0.8

        # 2. Strong Trend
        if "regime_trend_label" in df.columns:
            mask = df["regime_trend_label"].isin(
                ["strong_bullish_trend", "strong_bearish_trend"]
            ) & (primary_label == UNKNOWN)
            primary_label[mask] = df.loc[mask, "regime_trend_label"]
            if "regime_trend_strength" in df.columns:
                confidence[mask] = df.loc[mask, "regime_trend_strength"].clip(0.5, 1.0)

        # 3. Range
        if "regime_range_label" in df.columns:
            mask = df["regime_range_label"].isin(
                ["compressed_range", "range_bound"]
            ) & (primary_label == UNKNOWN)
            primary_label[mask] = df.loc[mask, "regime_range_label"]
            if "regime_range_score" in df.columns:
                confidence[mask] = df.loc[mask, "regime_range_score"].clip(0.5, 1.0)

        # 4. Normal Trend
        if "regime_trend_label" in df.columns:
            mask = df["regime_trend_label"].isin(
                ["bullish_trend", "bearish_trend", "weak_trend"]
            ) & (primary_label == UNKNOWN)
            primary_label[mask] = df.loc[mask, "regime_trend_label"]
            if "regime_trend_strength" in df.columns:
                confidence[mask] = df.loc[mask, "regime_trend_strength"].clip(0.3, 0.8)

        # 5. Volatility as secondary label
        if "regime_volatility_label" in df.columns:
            mask = df["regime_volatility_label"] != UNKNOWN
            secondary_label[mask] = df.loc[mask, "regime_volatility_label"]

        # 6. Mean Reversion as secondary if no volatility
        if "regime_mean_reversion_label" in df.columns:
            mask = (df["regime_mean_reversion_label"] != UNKNOWN) & (
                secondary_label == UNKNOWN
            )
            secondary_label[mask] = df.loc[mask, "regime_mean_reversion_label"]

        out_df["regime_primary_label"] = primary_label
        out_df["regime_secondary_label"] = secondary_label
        out_df["regime_confidence"] = confidence

        return RegimeClassificationResult(out_df, summary)

    def classify_latest(self, df: pd.DataFrame) -> dict:
        """Convenience method to just get the latest classification."""
        if df.empty:
            return {"primary_label": INSUFFICIENT_DATA, "confidence": 0.0}

        # If it doesn't have the labels yet, classify it
        if "regime_primary_label" not in df.columns:
            res = self.classify(df)
            classified_df = res.dataframe
        else:
            classified_df = df

        last_row = classified_df.iloc[-1]

        return {
            "primary_label": last_row.get("regime_primary_label", UNKNOWN),
            "secondary_label": last_row.get("regime_secondary_label", UNKNOWN),
            "confidence": last_row.get("regime_confidence", 0.0),
        }

    def validate_regime_frame(self, df: pd.DataFrame) -> dict:
        """Validate if a dataframe has required regime components."""
        has_primary = "regime_primary_label" in df.columns
        has_confidence = "regime_confidence" in df.columns

        return {
            "valid": has_primary and has_confidence,
            "has_primary": has_primary,
            "has_confidence": has_confidence,
        }
