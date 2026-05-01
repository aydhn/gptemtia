import pandas as pd
from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from mtf.mtf_config import MTFProfile, get_mtf_profile, get_default_mtf_profile
from mtf.mtf_loader import MTFFeatureLoader
from mtf.mtf_feature_joiner import MTFFeatureJoiner
from mtf.mtf_context import add_mtf_context_columns, summarize_mtf_context
from mtf.mtf_events import build_mtf_event_frame
from mtf.mtf_quality import build_mtf_quality_report


class MTFPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: MTFProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_mtf_profile()
        self.loader = MTFFeatureLoader(self.data_lake)
        self.joiner = MTFFeatureJoiner(self.profile)

    def build_for_symbol(
        self,
        spec: SymbolSpec,
        profile: MTFProfile | None = None,
        save: bool = True,
        include_events: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        prof = profile or self.profile
        summary = {
            "symbol": spec.symbol,
            "profile": prof.name,
            "base_timeframe": prof.base_timeframe,
            "context_timeframes": prof.context_timeframes,
            "feature_sets": prof.feature_sets,
            "warnings": [],
            "missing_feature_sets": [],
        }

        # Skip macro/synthetic if not appropriate, but for now we proceed
        # if spec.symbol_type in ("macro", "synthetic"):
        #     summary["warnings"].append(f"Skipping MTF for {spec.symbol_type} symbol")
        #     return pd.DataFrame(), summary

        base_df, base_summary = self.loader.load_best_available_base_frame(
            spec, prof.base_timeframe, prof.feature_sets
        )
        if base_df.empty:
            summary["warnings"].append(f"Could not load base frame for {spec.symbol}")
            return pd.DataFrame(), summary

        context_frames = self.loader.load_context_features(
            spec, prof.context_timeframes, prof.feature_sets
        )

        mtf_df, join_summary = self.joiner.build_mtf_frame(base_df, context_frames)
        summary["warnings"].extend(join_summary.get("warnings", []))

        mtf_df, ctx_summary = add_mtf_context_columns(mtf_df)
        summary["warnings"].extend(ctx_summary.get("warnings", []))

        if include_events and self.settings.mtf_events_enabled:
            event_df, ev_summary = build_mtf_event_frame(mtf_df)
            summary["event_summary"] = ev_summary

            if save and self.settings.save_mtf_events:
                self.data_lake.save_features(
                    spec, prof.base_timeframe, event_df, "mtf_events"
                )

        summary["rows"] = len(mtf_df)
        summary["columns"] = len(mtf_df.columns)

        quality_report = build_mtf_quality_report(mtf_df, summary)
        summary["quality_report"] = quality_report

        if save and self.settings.save_mtf_features:
            self.data_lake.save_features(spec, prof.base_timeframe, mtf_df, "mtf")

        return mtf_df, summary

    def build_for_universe(
        self,
        specs: list[SymbolSpec],
        profile: MTFProfile | None = None,
        limit: int | None = None,
        save: bool = True,
        include_events: bool = True,
    ) -> dict:
        results = []
        specs_to_process = specs[:limit] if limit else specs

        for spec in specs_to_process:
            try:
                _, sumry = self.build_for_symbol(spec, profile, save, include_events)
                results.append(sumry)
            except Exception as e:
                results.append({"symbol": spec.symbol, "error": str(e), "warnings": []})

        return {"batch_results": results, "total_processed": len(results)}
