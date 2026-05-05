import pandas as pd
from typing import Dict, List, Tuple, Optional
from config.settings import Settings
from data.storage.data_lake import DataLake
from config.symbols import SymbolSpec
from .decision_config import DecisionProfile, get_default_decision_profile
from .decision_inputs import DecisionInputLoader
from .decision_engine import DecisionEngine
from .decision_pool import DecisionCandidatePool
from .decision_quality import build_decision_quality_report
import logging

logger = logging.getLogger(__name__)


class DecisionPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: Optional[DecisionProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_decision_profile()
        self.input_loader = DecisionInputLoader(data_lake)
        self.engine = DecisionEngine(self.profile)

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: Optional[DecisionProfile] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:
        prof = profile or self.profile
        engine = DecisionEngine(prof) if profile else self.engine

        # Skip synthetic/macro/benchmark
        if spec.sub_class in ["Synthetic", "Macro", "Benchmark", "Macro Indicators"]:
            return pd.DataFrame(), {
                "skipped": True,
                "reason": "Not a tradable asset class",
            }

        candidates_df, candidates_summary = self.input_loader.load_signal_candidates(
            spec, timeframe, prof.name
        )
        if candidates_df.empty:
            return pd.DataFrame(), {
                "skipped": True,
                "reason": "No signal candidates found",
            }

        context_frames, context_summary = self.input_loader.load_decision_context(
            spec, timeframe
        )

        decisions, engine_summary = engine.build_decisions(
            spec.symbol, timeframe, candidates_df, context_frames
        )

        pool = DecisionCandidatePool()
        pool.extend(decisions)

        df = pool.to_dataframe()
        pool_summary = pool.summarize()

        quality_report = build_decision_quality_report(df, pool_summary)

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "profile": prof.name,
            "loaded_signal_candidates": candidates_summary["count"],
            "missing_context_frames": context_summary["missing_frames"],
            "decision_count": pool_summary["total_decisions"],
            "passed_decision_count": pool_summary["passed_decisions"],
            "latest_decisions": pool_summary["top_decisions"],
            "quality_report": quality_report,
            "warnings": [],
        }

        if not quality_report["passed"]:
            summary["warnings"].append("Quality report failed")

        if save and not df.empty and self.settings.save_decision_candidates:
            try:
                self.data_lake.save_features(spec, timeframe, df, "decision_candidates")
            except Exception as e:
                logger.error(
                    f"Failed to save decision candidates for {spec.symbol}: {e}"
                )
                summary["warnings"].append("Failed to save candidates")

        return df, summary

    def build_for_universe(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
        profile: Optional[DecisionProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Dict:
        prof = profile or self.profile

        universe_pool = DecisionCandidatePool()
        processed = 0
        successful = 0
        failed = 0

        for spec in specs:
            if limit and processed >= limit:
                break

            processed += 1
            try:
                df, summary = self.build_for_symbol_timeframe(
                    spec, timeframe, prof, save
                )
                if not df.empty and not summary.get("skipped", False):
                    pool = DecisionCandidatePool.from_dataframe(df)
                    universe_pool.extend(pool.decisions)
                    successful += 1
            except Exception as e:
                logger.error(f"Error processing {spec.symbol}: {e}")
                failed += 1

        pool_df = universe_pool.to_dataframe()
        pool_summary = universe_pool.summarize()

        if save and not pool_df.empty and self.settings.save_decision_pool:
            try:
                self.data_lake.save_decision_pool(timeframe, pool_df, prof.name)
            except Exception as e:
                logger.error(f"Failed to save universe decision pool: {e}")

        return {
            "timeframe": timeframe,
            "profile": prof.name,
            "processed_symbols": processed,
            "successful_symbols": successful,
            "failed_symbols": failed,
            "total_decisions": pool_summary["total_decisions"],
            "passed_decisions": pool_summary["passed_decisions"],
            "summary": pool_summary,
        }
