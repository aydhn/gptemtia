with open("commodity_fx_signal_bot/indicators/feature_builder.py", "r") as f:
    content = f.read()

new_method = """
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
"""

if "build_trend_feature_set" not in content:
    content = content.replace("    def validate_feature_frame", new_method + "\n    def validate_feature_frame")
    with open("commodity_fx_signal_bot/indicators/feature_builder.py", "w") as f:
        f.write(content)

with open("commodity_fx_signal_bot/indicators/indicator_pipeline.py", "r") as f:
    content = f.read()

pipeline_methods = """
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
                if include_events and getattr(self.settings, "save_trend_events", True) and len(event_cols) > 0:
                    events_df = features[event_cols]
                    self.data_lake.save_features(spec, timeframe, events_df, "trend_events")

            summary["success"] = True
            return features, summary

        except Exception as e:
            logger.error(f"Failed building trend features for {spec.symbol} {timeframe}: {e}")
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
"""

if "build_trend_for_symbol_timeframe" not in content:
    content += pipeline_methods
    with open("commodity_fx_signal_bot/indicators/indicator_pipeline.py", "w") as f:
        f.write(content)
