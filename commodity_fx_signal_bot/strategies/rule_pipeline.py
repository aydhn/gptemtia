import pandas as pd
import logging
from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from .rule_config import StrategyRuleProfile, get_default_strategy_rule_profile
from .rule_evaluator import StrategyRuleEvaluator
from .rule_pool import StrategyRuleCandidatePool
from .rule_quality import build_rule_quality_report

logger = logging.getLogger(__name__)

class StrategyRulePipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: StrategyRuleProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_strategy_rule_profile()
        self.evaluator = StrategyRuleEvaluator(self.profile)

    def load_strategy_candidates(
        self,
        spec: SymbolSpec,
        timeframe: str,
    ) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame()
        warnings = []
        try:
            from ml.feature_store import FeatureStore
            store = FeatureStore(self.data_lake)
            df = store.load_strategy_candidates(spec, timeframe)
            if df.empty:
                warnings.append("Strategy candidates dataframe is empty")
        except Exception as e:
            warnings.append(f"Failed to load strategy candidates: {e}")
        return df, {"warnings": warnings}

    def load_rule_context_frames(
        self,
        spec: SymbolSpec,
        timeframe: str,
    ) -> tuple[dict[str, pd.DataFrame], dict]:

        frames = {}
        missing = []

        from ml.feature_store import FeatureStore
        store = FeatureStore(self.data_lake)

        loaders = {
            "decision_candidates": store.load_decision_candidates,
            "signal_candidates": store.load_signal_candidates,
            "regime": store.load_regime_features,
            "regime_events": store.load_regime_events,
            "mtf": lambda s, t: store.load_mtf_features(s, t),
            "mtf_events": lambda s, t: store.load_mtf_events(s, t),
            "macro": lambda s, t: store.load_macro_features(),
            "macro_events": lambda s, t: store.load_macro_events(),
            "asset_profiles": store.load_asset_profile_features,
            "asset_profile_events": store.load_asset_profile_events,
        }

        for name, loader in loaders.items():
            try:
                df = loader(spec, timeframe)
                if df is not None and not df.empty:
                    frames[name] = df
                else:
                    missing.append(name)
            except Exception:
                missing.append(name)

        return frames, {"missing_context_frames": missing}

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: StrategyRuleProfile | None = None,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        prof = profile or self.profile

        if spec.asset_class in ["benchmark", "synthetic", "macro"]:
            return pd.DataFrame(), {"warnings": [f"Skipped {spec.symbol} (asset_class: {spec.asset_class})"]}

        strat_df, strat_meta = self.load_strategy_candidates(spec, timeframe)
        if strat_df.empty:
            return pd.DataFrame(), {"warnings": strat_meta["warnings"]}

        ctx_frames, ctx_meta = self.load_rule_context_frames(spec, timeframe)

        evaluator = StrategyRuleEvaluator(prof)
        candidates, eval_summary = evaluator.evaluate_strategy_frame(
            spec.symbol, timeframe, strat_df, ctx_frames
        )

        pool = StrategyRuleCandidatePool()
        pool.extend(candidates)
        df = pool.to_dataframe()

        pool_summary = pool.summarize()
        quality_report = build_rule_quality_report(df, eval_summary)

        if save and not df.empty and self.settings.save_strategy_rule_candidates:
            try:
                self.data_lake.save_features(spec, "strategy_rule_candidates", timeframe, df)
                if self.settings.save_entry_exit_candidates:
                    self.data_lake.save_features(spec, "entry_exit_candidates", timeframe, df)
            except Exception as e:
                logger.error(f"Failed to save rule candidates for {spec.symbol}: {e}")

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "profile": prof.name,
            "loaded_strategy_candidates": len(strat_df),
            "missing_context_frames": ctx_meta["missing_context_frames"],
            "rule_candidate_count": pool_summary["total_rule_candidates"],
            "passed_rule_candidate_count": pool_summary["passed_rule_candidates"],
            "quality_report": quality_report,
            "warnings": strat_meta["warnings"] + eval_summary["warnings"],
            "latest_rule_candidates": pool_summary["top_rule_candidates"]
        }

        return df, summary

    def build_for_universe(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: StrategyRuleProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> dict:

        prof = profile or self.profile
        universe_pool = StrategyRuleCandidatePool()

        processed = 0
        failed = 0

        target_specs = specs[:limit] if limit else specs

        for spec in target_specs:
            try:
                df, _ = self.build_for_symbol_timeframe(spec, timeframe, prof, save)
                if not df.empty:
                    pool = StrategyRuleCandidatePool.from_dataframe(df)
                    universe_pool.extend(pool.candidates)
                    processed += 1
            except Exception as e:
                logger.error(f"Error building rule candidates for {spec.symbol}: {e}")
                failed += 1

        summary = universe_pool.summarize()
        summary["processed_symbols"] = processed
        summary["failed_symbols"] = failed

        if save and self.settings.save_strategy_rule_pool:
            try:
                df_pool = universe_pool.to_dataframe()
                if not df_pool.empty:
                    if hasattr(self.data_lake, 'save_strategy_rule_pool'):
                        self.data_lake.save_strategy_rule_pool(timeframe, df_pool, prof.name)
            except Exception as e:
                logger.error(f"Failed to save strategy rule pool: {e}")

        return summary
