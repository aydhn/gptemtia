import logging

import pandas as pd

from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from strategies.strategy_config import (
    StrategySelectionProfile,
    get_default_strategy_selection_profile,
)
from strategies.strategy_context import StrategyContextLoader
from strategies.strategy_pool import StrategyCandidatePool
from strategies.strategy_quality import build_strategy_quality_report
from strategies.strategy_selector import StrategySelector

logger = logging.getLogger(__name__)


class StrategyPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: StrategySelectionProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_strategy_selection_profile()
        self.loader = StrategyContextLoader(data_lake)
        self.selector = StrategySelector(self.profile)

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: StrategySelectionProfile | None = None,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        active_profile = profile or self.profile

        if spec.asset_class in ("synthetic", "macro", "benchmark"):
            logger.info(
                f"Skipping strategy build for {spec.symbol} (asset class: {spec.asset_class})"
            )
            return pd.DataFrame(), {"skipped": True, "reason": "invalid_asset_class"}

        decisions_df, decision_summary = self.loader.load_decision_candidates(
            spec, timeframe, active_profile.name
        )
        if decisions_df.empty:
            return pd.DataFrame(), {
                "symbol": spec.symbol,
                "timeframe": timeframe,
                "profile": active_profile.name,
                "loaded_decision_candidates": 0,
                "missing_context_frames": decision_summary.get(
                    "missing_decision_candidates", True
                ),
                "strategy_candidate_count": 0,
                "passed_strategy_candidate_count": 0,
            }

        context_frames, context_summary = self.loader.load_strategy_context_frames(
            spec, timeframe
        )

        candidates, selector_summary = self.selector.select_for_decision_frame(
            spec.symbol, timeframe, decisions_df, context_frames
        )

        pool = StrategyCandidatePool()
        pool.extend(candidates)
        pool_summary = pool.summarize()

        df = pool.to_dataframe()

        quality_report = build_strategy_quality_report(df, pool_summary)

        if save and not df.empty and self.settings.save_strategy_candidates:
            try:
                self.data_lake.save_features(spec, timeframe, df, "strategy_candidates")
            except Exception as e:
                logger.error(
                    f"Failed to save strategy candidates for {spec.symbol}: {e}"
                )

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "profile": active_profile.name,
            "loaded_decision_candidates": len(decisions_df),
            "missing_context_frames": context_summary.get("missing_context_frames", []),
            "strategy_candidate_count": pool_summary.get(
                "total_strategy_candidates", 0
            ),
            "passed_strategy_candidate_count": pool_summary.get(
                "passed_strategy_candidates", 0
            ),
            "latest_strategy_candidates": len(candidates),
            "quality_report": quality_report,
            "warnings": [],
        }

        return df, summary

    def build_for_universe(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: StrategySelectionProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> dict:
        active_profile = profile or self.profile
        universe_pool = StrategyCandidatePool()

        processed = 0
        success = 0
        failed = 0

        for spec in specs:
            if limit and processed >= limit:
                break

            if spec.asset_class in ("synthetic", "macro", "benchmark"):
                continue

            processed += 1
            try:
                df, summary = self.build_for_symbol_timeframe(
                    spec, timeframe, active_profile, save
                )
                if not df.empty:
                    local_pool = StrategyCandidatePool.from_dataframe(df)
                    universe_pool.extend(local_pool.strategies)
                    success += 1
            except Exception as e:
                logger.error(
                    f"Error processing {spec.symbol} in strategy pipeline: {e}"
                )
                failed += 1

        universe_df = universe_pool.to_dataframe()
        universe_summary = universe_pool.summarize()

        if save and not universe_df.empty and self.settings.save_strategy_pool:
            try:
                self.data_lake.save_strategy_pool(
                    timeframe, universe_df, active_profile.name
                )
            except Exception as e:
                logger.error(f"Failed to save universe strategy pool: {e}")

        return {
            "timeframe": timeframe,
            "profile": active_profile.name,
            "processed_symbols": processed,
            "success_symbols": success,
            "failed_symbols": failed,
            "total_strategy_candidates": universe_summary.get(
                "total_strategy_candidates", 0
            ),
            "passed_strategy_candidates": universe_summary.get(
                "passed_strategy_candidates", 0
            ),
            "universe_summary": universe_summary,
        }
