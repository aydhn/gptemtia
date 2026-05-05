import pandas as pd
import logging
from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from signals.signal_config import (
    SignalScoringProfile,
    get_default_signal_scoring_profile,
)
from signals.event_loader import EventLoader
from signals.event_normalizer import normalize_many_event_frames
from signals.signal_scoring import SignalScorer
from signals.signal_pool import SignalCandidatePool
from signals.signal_quality import build_signal_quality_report

logger = logging.getLogger(__name__)


class SignalPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: SignalScoringProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_signal_scoring_profile()
        self.loader = EventLoader(data_lake)
        self.scorer = SignalScorer(self.profile)

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: SignalScoringProfile | None = None,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        prof = profile or self.profile

        # Skip macro and benchmark symbols
        if spec.asset_class in ["macro", "benchmark", "synthetic"]:
            logger.info(
                f"Skipping signal build for {spec.asset_class} symbol: {spec.symbol}"
            )
            return pd.DataFrame(), {
                "status": "skipped",
                "reason": "macro/benchmark symbol",
            }

        try:
            event_frames, event_sum = self.loader.load_event_frames(
                spec, timeframe, prof.enabled_event_groups
            )
            context_frames, context_sum = self.loader.load_context_frames(
                spec, timeframe
            )

            norm_df, norm_sum = normalize_many_event_frames(
                spec.symbol, timeframe, event_frames
            )

            candidates, score_sum = self.scorer.score_timestamps(
                spec.symbol, timeframe, norm_df, context_frames
            )

            pool = SignalCandidatePool()
            pool.extend(candidates)
            cand_df = pool.to_dataframe()

            q_report = build_signal_quality_report(cand_df, {})

            if save and not cand_df.empty and self.settings.save_signal_candidates:
                self.data_lake.save_features(
                    spec, timeframe, cand_df, "signal_candidates"
                )

            summary = {
                "symbol": spec.symbol,
                "timeframe": timeframe,
                "profile": prof.name,
                "loaded_event_groups": event_sum.get("loaded_groups", []),
                "missing_event_groups": event_sum.get("missing_event_groups", []),
                "candidate_count": len(candidates),
                "passed_candidate_count": sum(
                    1 for c in candidates if c.passed_pre_filters
                ),
                "latest_candidates": (
                    [c.candidate_id for c in candidates[-5:]] if candidates else []
                ),
                "quality_report": q_report,
                "warnings": [],
            }
            if event_sum.get("missing_event_groups"):
                summary["warnings"].append(
                    f"Missing event groups: {event_sum['missing_event_groups']}"
                )

            return cand_df, summary

        except Exception as e:
            logger.error(f"Error building signals for {spec.symbol}: {e}")
            return pd.DataFrame(), {"status": "error", "error": str(e)}

    def build_for_universe(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: SignalScoringProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> dict:

        prof = profile or self.profile
        universe_pool = SignalCandidatePool()
        summary = {
            "processed": 0,
            "skipped": 0,
            "errors": 0,
            "total_candidates": 0,
            "symbols_with_candidates": 0,
        }

        to_process = specs[:limit] if limit else specs

        for spec in to_process:
            if spec.asset_class in ["macro", "benchmark", "synthetic"]:
                summary["skipped"] += 1
                continue

            df, res = self.build_for_symbol_timeframe(spec, timeframe, prof, save)

            if res.get("status") == "skipped":
                summary["skipped"] += 1
            elif res.get("status") == "error":
                summary["errors"] += 1
            else:
                summary["processed"] += 1
                if not df.empty:
                    summary["symbols_with_candidates"] += 1
                    # Convert df back to pool to extend universe pool
                    sym_pool = SignalCandidatePool.from_dataframe(df)
                    universe_pool.extend(sym_pool.candidates)

        summary["total_candidates"] = len(universe_pool.candidates)

        if save and universe_pool.candidates and self.settings.save_signal_pool:
            pool_df = universe_pool.to_dataframe()
            self.data_lake.save_signal_pool(timeframe, pool_df, prof.name)

        return summary
