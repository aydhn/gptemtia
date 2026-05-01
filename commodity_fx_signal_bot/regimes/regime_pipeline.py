"""
Regime pipeline to orchestrate loading features, running classification, and saving results.
"""

import pandas as pd
import logging

from config.symbols import SymbolSpec
from config.settings import Settings
from data.storage.data_lake import DataLake

from regimes.regime_config import RegimeProfile, get_default_regime_profile
from regimes.trend_regime import detect_trend_regime
from regimes.volatility_regime import detect_volatility_regime
from regimes.range_regime import detect_range_regime
from regimes.momentum_regime import detect_momentum_regime
from regimes.mean_reversion_regime import detect_mean_reversion_regime
from regimes.mtf_regime import detect_mtf_regime
from regimes.regime_classifier import RegimeClassifier
from regimes.regime_events import build_regime_event_frame
from regimes.regime_quality import build_regime_quality_report

logger = logging.getLogger(__name__)

class RegimePipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: RegimeProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_regime_profile()
        self.classifier = RegimeClassifier(self.profile)

    def build_input_frame(
        self,
        spec: SymbolSpec,
        timeframe: str,
        feature_sets: tuple[str, ...],
    ) -> tuple[pd.DataFrame, dict]:
        """Build the combined input dataframe from various feature sets."""
        summary = {"missing_feature_sets": [], "loaded_feature_sets": []}

        # Load processed OHLCV as a base
        if not self.data_lake.has_ohlcv(spec, timeframe, processed=True):
            # Try raw if processed not available
            if self.data_lake.has_ohlcv(spec, timeframe):
                base_df = self.data_lake.load_ohlcv(spec, timeframe)
            else:
                return pd.DataFrame(), summary
        else:
            base_df = self.data_lake.load_ohlcv(spec, timeframe, processed=True)

        dfs_to_join = [base_df]

        # Load requested feature sets
        for fs in feature_sets:
            if self.data_lake.has_features(spec, timeframe, fs):
                df = self.data_lake.load_features(spec, timeframe, fs)
                dfs_to_join.append(df)
                summary["loaded_feature_sets"].append(fs)

                # Also try to load the events for this feature set if they exist
                event_fs = f"{fs}_events"
                if self.data_lake.has_features(spec, timeframe, event_fs):
                    event_df = self.data_lake.load_features(spec, timeframe, event_fs)
                    dfs_to_join.append(event_df)
                    summary["loaded_feature_sets"].append(event_fs)
            else:
                summary["missing_feature_sets"].append(fs)

        # Join all dataframes on index
        if not dfs_to_join:
            return pd.DataFrame(), summary

        combined = pd.concat(dfs_to_join, axis=1)

        # Remove duplicate columns
        combined = combined.loc[:, ~combined.columns.duplicated()]

        return combined, summary

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: RegimeProfile | None = None,
        save: bool = True,
        include_events: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        """Build regime features and events for a single symbol and timeframe."""

        # Skip synthetic or macro symbols
        if spec.is_synthetic() or spec.is_macro():
            return pd.DataFrame(), {
                "status": "skipped",
                "reason": "Synthetic or macro symbol",
                "warnings": ["Synthetic or macro symbol"]
            }

        prof = profile or self.profile

        # Build input frame
        input_df, load_summary = self.build_input_frame(spec, timeframe, prof.feature_sets)

        if input_df.empty:
            return pd.DataFrame(), {
                "status": "error",
                "error": "Could not load base data",
                "warnings": ["Could not load base data"]
            }

        # Run sub-detectors
        trend_df, trend_sum = detect_trend_regime(input_df, prof)
        vol_df, vol_sum = detect_volatility_regime(input_df, prof)
        range_df, range_sum = detect_range_regime(input_df, prof)
        mom_df, mom_sum = detect_momentum_regime(input_df, prof)
        mr_df, mr_sum = detect_mean_reversion_regime(input_df, prof)
        mtf_df, mtf_sum = detect_mtf_regime(input_df, prof)

        # Combine sub-detector outputs
        detectors_out = [trend_df, vol_df, range_df, mom_df, mr_df, mtf_df]
        regime_features = pd.concat(detectors_out, axis=1)

        # Remove duplicate columns if any
        regime_features = regime_features.loc[:, ~regime_features.columns.duplicated()]

        # Classify
        classifier = RegimeClassifier(prof)
        class_res = classifier.classify(regime_features)

        final_regime_df = class_res.dataframe

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "profile": prof.name,
            "feature_sets": prof.feature_sets,
            "rows": len(final_regime_df),
            "columns": len(final_regime_df.columns),
            "missing_feature_sets": load_summary["missing_feature_sets"],
            "status": "success",
            "warnings": [],
            "error": None
        }

        # Collect warnings
        all_warnings = (
            load_summary.get("warnings", []) +
            trend_sum.get("warnings", []) +
            vol_sum.get("warnings", []) +
            range_sum.get("warnings", []) +
            mom_sum.get("warnings", []) +
            mr_sum.get("warnings", []) +
            mtf_sum.get("warnings", []) +
            class_res.summary.get("warnings", [])
        )
        summary["warnings"] = list(set(all_warnings))

        # Latest regime status
        latest_status = classifier.classify_latest(final_regime_df)
        summary["latest_regime"] = latest_status.get("primary_label")
        summary["latest_confidence"] = latest_status.get("confidence")

        # Quality report
        qr = build_regime_quality_report(final_regime_df, summary)
        summary["quality_report"] = qr

        if not qr["passed"]:
            summary["warnings"].append("Regime quality checks failed.")

        # Save features
        if save and self.settings.save_regime_features:
            self.data_lake.save_features(spec, timeframe, final_regime_df, "regime")

        # Events
        if include_events and self.settings.regime_events_enabled:
            event_df, event_sum = build_regime_event_frame(final_regime_df)
            summary["event_summary"] = event_sum

            if save and self.settings.save_regime_events:
                self.data_lake.save_features(spec, timeframe, event_df, "regime_events")
        else:
            summary["event_summary"] = {}

        return final_regime_df, summary

    def build_for_universe(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: RegimeProfile | None = None,
        limit: int | None = None,
        save: bool = True,
        include_events: bool = True,
    ) -> dict:
        """Run batch build for multiple symbols."""

        summary = {}
        count = 0

        for spec in specs:
            if limit and count >= limit:
                break

            try:
                logger.info(f"Building regimes for {spec.symbol} {timeframe}")
                _, sym_summary = self.build_for_symbol_timeframe(
                    spec, timeframe, profile, save, include_events
                )

                if spec.symbol not in summary:
                    summary[spec.symbol] = {}

                summary[spec.symbol][timeframe] = sym_summary

                if sym_summary.get("status") == "success":
                    count += 1

            except Exception as e:
                logger.error(f"Error building regimes for {spec.symbol}: {e}")
                if spec.symbol not in summary:
                    summary[spec.symbol] = {}
                summary[spec.symbol][timeframe] = {
                    "status": "error",
                    "error": str(e)
                }

        return summary
