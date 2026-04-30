import logging
from typing import Optional, Tuple

import pandas as pd

from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from indicators.feature_builder import FeatureBuilder

logger = logging.getLogger(__name__)


class IndicatorPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        feature_builder: FeatureBuilder,
        settings,
    ):
        self.data_lake = data_lake
        self.feature_builder = feature_builder
        self.settings = settings

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str,
        use_processed: bool = True,
        save: bool = True,
    ) -> Tuple[Optional[pd.DataFrame], dict]:

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "success": False,
            "skipped": False,
            "error": "",
            "source": "processed" if use_processed else "raw",
        }

        if spec.asset_class in ("synthetic", "macro") and getattr(
            self.settings, "skip_macro_downloads_in_ohlcv_pipeline", True
        ):
            summary["skipped"] = True
            summary["notes"] = (
                f"Skipping {spec.data_source} symbol for technical indicators."
            )
            return None, summary

        df = None
        try:
            if use_processed and self.data_lake.has_processed_ohlcv(spec, timeframe):
                df = self.data_lake.load_processed_ohlcv(spec, timeframe)
            elif self.data_lake.has_ohlcv(spec, timeframe):
                df = self.data_lake.load_ohlcv(spec, timeframe)
                summary["source"] = "raw"
                logger.warning(
                    f"Using RAW data for {spec.symbol} {timeframe}. Processed not found."
                )
            else:
                summary["skipped"] = True
                summary["notes"] = "No data found in Data Lake."
                return None, summary

        except Exception as e:
            logger.error(f"Error loading data for {spec.symbol} {timeframe}: {e}")
            summary["error"] = str(e)
            return None, summary

        if df is None or len(df) < getattr(
            self.settings, "default_indicator_min_rows", 100
        ):
            summary["skipped"] = True
            summary["notes"] = (
                f"Not enough rows (min: {getattr(self.settings, 'default_indicator_min_rows', 100)})"
            )
            return None, summary

        try:
            features, build_summary = self.feature_builder.build_default_feature_set(df)
            summary.update(build_summary)

            val_res = self.feature_builder.validate_feature_frame(features)
            if not val_res["valid"]:
                summary["error"] = f"Validation failed: {val_res}"
                return None, summary

            if save and getattr(self.settings, "save_indicator_features", True):
                self.data_lake.save_features(spec, timeframe, features, "technical")

            summary["success"] = True
            return features, summary

        except Exception as e:
            logger.error(f"Failed building features for {spec.symbol} {timeframe}: {e}")
            summary["error"] = str(e)
            return None, summary

    def build_for_universe(
        self,
        specs: list[SymbolSpec],
        timeframes_by_symbol: dict[str, tuple[str, ...]],
        limit: Optional[int] = None,
        use_processed: bool = True,
        save: bool = True,
    ) -> dict:

        results = {
            "total_attempts": 0,
            "success_count": 0,
            "failure_count": 0,
            "skipped_count": 0,
            "details": [],
        }

        count = 0
        for spec in specs:
            timeframes = timeframes_by_symbol.get(spec.symbol, [])
            for tf in timeframes:
                if limit and count >= limit:
                    break

                _, summary = self.build_for_symbol_timeframe(
                    spec, tf, use_processed, save
                )

                results["total_attempts"] += 1
                if summary["success"]:
                    results["success_count"] += 1
                elif summary.get("skipped"):
                    results["skipped_count"] += 1
                else:
                    results["failure_count"] += 1

                results["details"].append(summary)
                count += 1

            if limit and count >= limit:
                break

        return results

    def build_trend_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str,
        use_processed: bool = True,
        save: bool = True,
        compact: bool = True,
        include_events: bool = True,
    ) -> Tuple[Optional[pd.DataFrame], dict]:

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "success": False,
            "skipped": False,
            "error": "",
            "source": "processed" if use_processed else "raw",
        }

        if spec.asset_class in ("synthetic", "macro") and getattr(
            self.settings, "skip_macro_downloads_in_ohlcv_pipeline", True
        ):
            summary["skipped"] = True
            summary["notes"] = (
                f"Skipping {spec.data_source} symbol for trend indicators."
            )
            return None, summary

        df = None
        try:
            if use_processed and self.data_lake.has_processed_ohlcv(spec, timeframe):
                df = self.data_lake.load_processed_ohlcv(spec, timeframe)
            elif self.data_lake.has_ohlcv(spec, timeframe):
                df = self.data_lake.load_ohlcv(spec, timeframe)
                summary["source"] = "raw"
                logger.warning(
                    f"Using RAW data for {spec.symbol} {timeframe}. Processed not found."
                )
            else:
                summary["skipped"] = True
                summary["notes"] = "No data found in Data Lake."
                return None, summary

        except Exception as e:
            logger.error(f"Error loading data for {spec.symbol} {timeframe}: {e}")
            summary["error"] = str(e)
            return None, summary

        if df is None or len(df) < getattr(
            self.settings, "default_indicator_min_rows", 100
        ):
            summary["skipped"] = True
            summary["notes"] = (
                f"Not enough rows (min: {getattr(self.settings, 'default_indicator_min_rows', 100)})"
            )
            return None, summary

        try:
            features, build_summary = self.feature_builder.build_trend_feature_set(
                df, compact=compact, include_events=include_events
            )
            summary.update(build_summary)

            val_res = self.feature_builder.validate_feature_frame(features)
            if not val_res["valid"]:
                summary["error"] = f"Validation failed: {val_res}"
                return None, summary

            if save and getattr(self.settings, "save_trend_features", True):
                event_cols = summary.get("event_columns", [])
                feature_cols = summary.get("feature_columns", [])

                # We can save it all in "trend" feature_set
                self.data_lake.save_features(spec, timeframe, features, "trend")

                # Also save events separately if save_trend_events is true
                if (
                    include_events
                    and getattr(self.settings, "save_trend_events", True)
                    and len(event_cols) > 0
                ):
                    events_df = features[event_cols]
                    self.data_lake.save_features(
                        spec, timeframe, events_df, "trend_events"
                    )

            summary["success"] = True
            return features, summary

        except Exception as e:
            logger.error(
                f"Failed building trend features for {spec.symbol} {timeframe}: {e}"
            )
            summary["error"] = str(e)
            return None, summary

    def build_trend_for_universe(
        self,
        specs: list[SymbolSpec],
        timeframes_by_symbol: dict[str, tuple[str, ...]],
        limit: Optional[int] = None,
        use_processed: bool = True,
        save: bool = True,
        compact: bool = True,
        include_events: bool = True,
    ) -> dict:

        results = {
            "total_attempts": 0,
            "success_count": 0,
            "failure_count": 0,
            "skipped_count": 0,
            "details": [],
        }

        count = 0
        for spec in specs:
            timeframes = timeframes_by_symbol.get(spec.symbol, [])
            for tf in timeframes:
                if limit and count >= limit:
                    break

                _, summary = self.build_trend_for_symbol_timeframe(
                    spec, tf, use_processed, save, compact, include_events
                )

                results["total_attempts"] += 1
                if summary["success"]:
                    results["success_count"] += 1
                elif summary.get("skipped"):
                    results["skipped_count"] += 1
                else:
                    results["failure_count"] += 1

                results["details"].append(summary)
                count += 1

            if limit and count >= limit:
                break

        return results

    def build_volume_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str,
        use_processed: bool = True,
        save: bool = True,
        compact: bool = True,
        include_events: bool = True,
        disable_events_if_volume_unusable: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame()
        if (
            use_processed and self.data_lake.has_processed_ohlcv(spec, timeframe)
            if hasattr(self.data_lake, "has_processed_ohlcv")
            else self.data_lake.has_ohlcv(spec, timeframe)
        ):
            df = (
                self.data_lake.load_processed_ohlcv(spec, timeframe)
                if hasattr(self.data_lake, "load_processed_ohlcv")
                else self.data_lake.load_ohlcv(spec, timeframe)
            )
        elif self.data_lake.has_ohlcv(spec, timeframe):
            if use_processed:
                logger.warning(
                    f"Processed OHLCV missing for {spec.symbol} {timeframe}, falling back to raw."
                )
            df = self.data_lake.load_ohlcv(spec, timeframe)

        if df.empty:
            return pd.DataFrame(), {"error": "No OHLCV data available"}

        from indicators.volume_feature_set import VolumeFeatureSetBuilder

        builder = VolumeFeatureSetBuilder()

        if compact:
            features, summary = builder.build_compact_volume_features(
                df, include_events, disable_events_if_volume_unusable
            )
        else:
            features, summary = builder.build_volume_features(
                df, include_events, disable_events_if_volume_unusable
            )

        if save and not features.empty:
            self.data_lake.save_features(
                spec, timeframe, features, feature_set_name="volume"
            )
            # If events were built separately, we could save them here. Currently they are in the feature set.
            if include_events and summary.get("event_columns"):
                events_df = features[summary["event_columns"]]
                self.data_lake.save_features(
                    spec, timeframe, events_df, feature_set_name="volume_events"
                )

        return features, summary

    def build_volume_for_universe(
        self,
        specs: list[SymbolSpec],
        timeframes_by_symbol: dict[str, tuple[str, ...]],
        limit: Optional[int] = None,
        use_processed: bool = True,
        save: bool = True,
        compact: bool = True,
        include_events: bool = True,
        disable_events_if_volume_unusable: bool = True,
    ) -> dict:
        summary = {
            "total_targets": 0,
            "success_count": 0,
            "skipped_count": 0,
            "failed_count": 0,
            "details": [],
        }

        targets = []
        for spec in specs:
            if spec.sub_class in ["Synthetic", "Macro"]:
                logger.info(
                    f"Skipping volume features for macro/synthetic {spec.symbol}"
                )
                continue
            tfs = timeframes_by_symbol.get(spec.symbol, [])
            for tf in tfs:
                targets.append((spec, tf))

        if limit:
            targets = targets[:limit]

        summary["total_targets"] = len(targets)

        for spec, tf in targets:
            try:
                features, res_summary = self.build_volume_for_symbol_timeframe(
                    spec,
                    tf,
                    use_processed,
                    save,
                    compact,
                    include_events,
                    disable_events_if_volume_unusable,
                )
                if "error" in res_summary:
                    summary["failed_count"] += 1
                    summary["details"].append(
                        {
                            "symbol": spec.symbol,
                            "timeframe": tf,
                            "success": False,
                            "skipped": False,
                            "error": res_summary["error"],
                        }
                    )
                else:
                    summary["success_count"] += 1
                    summary["details"].append(
                        {
                            "symbol": spec.symbol,
                            "timeframe": tf,
                            "success": True,
                            "skipped": False,
                            "rows": len(features),
                        }
                    )
            except Exception as e:
                logger.error(f"Failed to build volume for {spec.symbol} {tf}: {e}")
                summary["failed_count"] += 1
                summary["details"].append(
                    {
                        "symbol": spec.symbol,
                        "timeframe": tf,
                        "success": False,
                        "skipped": False,
                        "error": str(e),
                    }
                )

        return summary
