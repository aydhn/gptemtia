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
