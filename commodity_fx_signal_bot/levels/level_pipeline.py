import pandas as pd
from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from levels.level_config import LevelProfile, get_default_level_profile
from levels.level_candidate import (
    StopTargetLevelCandidate,
    build_level_candidate_from_evaluation,
)
from levels.level_pool import StopTargetLevelCandidatePool
from levels.level_quality import build_level_quality_report
from core.logger import get_logger

logger = get_logger(__name__)


class LevelPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: LevelProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_level_profile()

    def load_sizing_candidates(
        self, spec: SymbolSpec, timeframe: str
    ) -> tuple[pd.DataFrame, dict]:
        if not self.data_lake.has_features(spec, timeframe, "sizing_candidates"):
            return pd.DataFrame(), {"warnings": ["No sizing_candidates found"]}
        df = self.data_lake.load_features(spec, timeframe, "sizing_candidates")
        return df, {"warnings": []}

    def load_level_context_frames(
        self, spec: SymbolSpec, timeframe: str
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        # Minimal implementation for now
        frames = {}
        missing = []
        # Attempt to load context like regime, mtf
        for ft in ["mtf", "regime", "price_action"]:
            if self.data_lake.has_features(spec, timeframe, ft):
                frames[ft] = self.data_lake.load_features(spec, timeframe, ft)
            else:
                missing.append(ft)
        return frames, {"missing_context_frames": missing}

    def evaluate_sizing_candidate_for_levels(
        self,
        spec: SymbolSpec,
        timeframe: str,
        sizing_row: pd.Series,
        context_frames: dict[str, pd.DataFrame],
    ) -> tuple[StopTargetLevelCandidate, dict]:
        # Simulated logic
        bias = sizing_row.get("directional_bias", "neutral")
        price = sizing_row.get("latest_close")
        atr = sizing_row.get("atr_value", price * 0.01 if price else 0.0)

        evaluation = {
            "level_label": (
                "level_approved_candidate"
                if bias not in ["neutral", "no_trade_candidate"]
                else "level_zero_candidate"
            ),
            "level_method": "atr_based_theoretical",
            "latest_close": price,
            "atr_value": atr,
            "reward_risk": 2.0,
            "stop_target_readiness_score": 0.8,
            "passed_level_filters": True,
            "warnings": [],
        }

        if bias in ["long_bias_candidate", "bullish"] and price and atr:
            evaluation["theoretical_stop_level"] = price - atr * 1.5
            evaluation["theoretical_target_level"] = price + atr * 3.0
            evaluation["stop_distance"] = atr * 1.5
            evaluation["target_distance"] = atr * 3.0
        elif bias in ["short_bias_candidate", "bearish"] and price and atr:
            evaluation["theoretical_stop_level"] = price + atr * 1.5
            evaluation["theoretical_target_level"] = price - atr * 3.0
            evaluation["stop_distance"] = atr * 1.5
            evaluation["target_distance"] = atr * 3.0

        candidate = build_level_candidate_from_evaluation(
            sizing_row, evaluation, spec.symbol, timeframe
        )
        return candidate, evaluation

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: LevelProfile | None = None,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:
        prof = profile or self.profile

        if spec.asset_class in ["synthetic", "macro", "benchmark"]:
            return pd.DataFrame(), {"warnings": [f"Skipped {spec.asset_class} symbol"]}

        sizing_df, s_info = self.load_sizing_candidates(spec, timeframe)
        if sizing_df.empty:
            return pd.DataFrame(), s_info

        context_frames, c_info = self.load_level_context_frames(spec, timeframe)

        pool = StopTargetLevelCandidatePool()

        for idx, row in sizing_df.iterrows():
            cand, _ = self.evaluate_sizing_candidate_for_levels(
                spec, timeframe, row, context_frames
            )
            pool.add(cand)

        df_out = pool.to_dataframe()

        summary = pool.summarize()
        summary["symbol"] = spec.symbol
        summary["timeframe"] = timeframe
        summary["profile"] = prof.name
        summary["missing_context_frames"] = c_info.get("missing_context_frames", [])

        quality = build_level_quality_report(df_out, summary)
        summary["quality_report"] = quality

        if save and not df_out.empty:
            self.data_lake.save_features(spec, timeframe, "level_candidates", df_out)

        return df_out, summary

    def build_for_universe(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: LevelProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> dict:
        prof = profile or self.profile
        all_pool = StopTargetLevelCandidatePool()

        specs_to_run = specs[:limit] if limit else specs

        results = []
        for spec in specs_to_run:
            df_s, sum_s = self.build_for_symbol_timeframe(
                spec, timeframe, prof, save=save
            )
            if not df_s.empty:
                # Need to convert df back to candidates or just append? We can just build candidate objects again or not worry about it
                # For universe pool we can just collect dfs
                results.append(df_s)

        if results:
            universe_df = pd.concat(results, ignore_index=True)
            if "timestamp" in universe_df.columns:
                try:
                    universe_df.set_index("timestamp", inplace=True)
                except Exception:
                    pass
            if save:
                self.data_lake.save_level_pool(timeframe, universe_df, prof.name)
        else:
            universe_df = pd.DataFrame()

        return {
            "processed_symbols": len(specs_to_run),
            "generated_rows": len(universe_df),
            "profile": prof.name,
        }
