import pandas as pd
from typing import Dict, Tuple, List, Optional
from config.symbols import SymbolSpec
from config.settings import Settings
from data.storage.data_lake import DataLake
from ml.feature_store import FeatureStore
from risk.risk_config import RiskPrecheckProfile, get_default_risk_precheck_profile
from risk.pretrade_risk import PreTradeRiskEvaluator
from risk.risk_filters import infer_risk_candidate_label
from risk.risk_candidate import build_risk_candidate_from_evaluation
from risk.risk_pool import RiskCandidatePool
from risk.risk_quality import build_risk_quality_report
from core.logger import get_logger

logger = get_logger(__name__)


class RiskPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: Optional[RiskPrecheckProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_risk_precheck_profile()
        self.feature_store = FeatureStore(data_lake)
        self.evaluator = PreTradeRiskEvaluator(self.profile)

    def load_rule_candidates(
        self, spec: SymbolSpec, timeframe: str
    ) -> Tuple[pd.DataFrame, Dict]:
        try:
            if self.data_lake.has_features(spec, timeframe, "strategy_rule_candidates"):
                return (
                    self.data_lake.load_features(
                        spec, timeframe, "strategy_rule_candidates"
                    ),
                    {},
                )
        except Exception as e:
            return pd.DataFrame(), {"error": str(e)}
        return pd.DataFrame(), {"error": "Feature not found"}

    def load_risk_context_frames(
        self, spec: SymbolSpec, timeframe: str
    ) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        frames = {}
        missing = []
        feature_sets = [
            "regime",
            "regime_events",
            "mtf",
            "mtf_events",
            "macro",
            "macro_events",
            "asset_profiles",
            "asset_profile_events",
            "volatility",
            "volatility_events",
            "volume",
            "volume_events",
            "price_action",
            "price_action_events",
        ]
        for fs in feature_sets:
            if self.data_lake.has_features(spec, timeframe, fs):
                frames[fs] = self.data_lake.load_features(spec, timeframe, fs)
            else:
                missing.append(fs)
        return frames, {"missing": missing}

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: Optional[RiskPrecheckProfile] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict]:
        use_profile = profile or self.profile
        if spec.sub_class.lower() in ["synthetic", "macro", "benchmark"]:
            return pd.DataFrame(), {
                "skipped": True,
                "reason": f"Skipped subclass {spec.sub_class}",
            }
        rules_df, rules_meta = self.load_rule_candidates(spec, timeframe)
        if rules_df.empty:
            return pd.DataFrame(), {"warning": "No rule candidates found", **rules_meta}
        context_frames, ctx_meta = self.load_risk_context_frames(spec, timeframe)
        evaluations, _ = self.evaluator.evaluate_rule_frame(
            spec.symbol, timeframe, rules_df, context_frames
        )
        pool = RiskCandidatePool()
        for eval_dict in evaluations:
            label = infer_risk_candidate_label(eval_dict, use_profile)
            severity = "low"
            row = eval_dict["_source_row"]
            candidate = build_risk_candidate_from_evaluation(
                row, eval_dict, spec.symbol, timeframe, label, severity
            )
            pool.add(candidate)
        candidates_df = pool.to_dataframe()
        summary = pool.summarize()
        quality_report = build_risk_quality_report(candidates_df, summary)
        if save and self.settings.save_risk_candidates and not candidates_df.empty:
            self.data_lake.save_features(
                spec, timeframe, "risk_candidates", candidates_df
            )
        return candidates_df, {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "profile": use_profile.name,
            "loaded_rule_candidates": len(rules_df),
            "missing_context_frames": ctx_meta.get("missing", []),
            "risk_candidate_count": summary["total_risk_candidates"],
            "passed_risk_candidate_count": summary["passed_risk_candidates"],
            "rejected_risk_candidate_count": summary["rejected_risk_candidates"],
            "watchlist_risk_candidate_count": summary["watchlist_risk_candidates"],
            "quality_report": quality_report,
            "warnings": [],
        }

    def build_for_universe(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
        profile: Optional[RiskPrecheckProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Dict:
        use_profile = profile or self.profile
        pool = RiskCandidatePool()
        summaries = {}
        for i, spec in enumerate(specs):
            if limit and i >= limit:
                break
            try:
                df, summary = self.build_for_symbol_timeframe(
                    spec, timeframe, use_profile, save
                )
                if not df.empty:
                    pool.extend(
                        [
                            build_risk_candidate_from_evaluation(
                                row,
                                row.to_dict(),
                                spec.symbol,
                                timeframe,
                                row.get("risk_label", ""),
                                row.get("risk_severity", ""),
                            )
                            for _, row in df.iterrows()
                        ]
                    )
                summaries[spec.symbol] = summary
            except Exception as e:
                logger.error(f"Error processing {spec.symbol} for risk: {e}")
                summaries[spec.symbol] = {"error": str(e)}
        pool_df = pool.to_dataframe()
        if save and self.settings.save_risk_pool and not pool_df.empty:
            self.data_lake.save_risk_pool(timeframe, pool_df, use_profile.name)
        return {
            "processed": len(summaries),
            "total_candidates": len(pool_df),
            "symbol_summaries": summaries,
        }
