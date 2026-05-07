import pandas as pd
import logging
from typing import Dict, Any, Tuple, Optional, List
from data.storage.data_lake import DataLake
from config.settings import Settings
from config.symbols import SymbolSpec

from sizing.sizing_config import SizingProfile, get_default_sizing_profile
from sizing.sizing_candidate import SizingCandidate, build_sizing_candidate_from_evaluation
from sizing.sizing_pool import SizingCandidatePool
from sizing.risk_unit import calculate_theoretical_risk_amount
from sizing.atr_sizing import build_atr_sizing_candidate
from sizing.volatility_sizing import calculate_combined_sizing_adjustment, apply_sizing_adjustment
from sizing.budget_model import build_risk_budget_allocation, cap_risk_amount_by_budgets
from sizing.exposure_limits import check_exposure_limits
from sizing.sizing_filters import infer_sizing_candidate_label
from sizing.sizing_quality import build_sizing_quality_report

logger = logging.getLogger(__name__)

class SizingPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: Optional[SizingProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_sizing_profile()

    def load_risk_candidates(
        self,
        spec: SymbolSpec,
        timeframe: str,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        warnings = []
        try:
            if not self.data_lake.has_features(spec, timeframe, "risk_candidates"):
                return pd.DataFrame(), {"warnings": [f"No risk candidates found for {spec.symbol} {timeframe}"]}
            df = self.data_lake.load_features(spec, timeframe, "risk_candidates")
            return df, {"warnings": warnings}
        except Exception as e:
            logger.error(f"Failed to load risk candidates for {spec.symbol}: {e}")
            return pd.DataFrame(), {"warnings": [str(e)]}

    def load_sizing_context_frames(
        self,
        spec: SymbolSpec,
        timeframe: str,
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        frames = {}
        missing = []

        feature_sets = [
            "volatility", "volatility_events",
            "price_action", "price_action_events",
            "regime", "regime_events",
            "mtf", "mtf_events",
            "asset_profiles", "group_features"
        ]

        for fs in feature_sets:
            try:
                if self.data_lake.has_features(spec, timeframe, fs):
                    frames[fs] = self.data_lake.load_features(spec, timeframe, fs)
                else:
                    missing.append(fs)
            except Exception:
                missing.append(fs)

        # Also load OHLCV for latest close
        try:
            ohlcv = self.data_lake.load_processed_ohlcv(spec, timeframe)
            frames["ohlcv"] = ohlcv
        except Exception:
            missing.append("ohlcv")

        return frames, {"missing_context_frames": missing}

    def evaluate_risk_candidate_for_sizing(
        self,
        spec: SymbolSpec,
        timeframe: str,
        risk_row: pd.Series,
        context_frames: Dict[str, pd.DataFrame],
        existing_sizing_df: Optional[pd.DataFrame] = None,
    ) -> Tuple[SizingCandidate, Dict[str, Any]]:

        evaluation = {
            "warnings": [],
            "block_reasons": [],
            "watchlist_reasons": []
        }

        timestamp = risk_row.name if isinstance(risk_row.name, (pd.Timestamp, str)) else risk_row.get("timestamp")

        # Extract basic info
        ohlcv = context_frames.get("ohlcv", pd.DataFrame())
        vol_features = context_frames.get("volatility", pd.DataFrame())

        latest_close = None
        if not ohlcv.empty and timestamp in ohlcv.index:
            latest_close = float(ohlcv.loc[timestamp, "close"])
        elif not ohlcv.empty:
            latest_close = float(ohlcv.iloc[-1]["close"])

        atr_value = None
        atr_pct = None
        vol_pctile = None

        if not vol_features.empty and timestamp in vol_features.index:
            v_row = vol_features.loc[timestamp]
            if isinstance(v_row, pd.DataFrame):
                v_row = v_row.iloc[-1]
            atr_value = float(v_row.get("atr_14", 0.0)) if "atr_14" in v_row else None
            atr_pct = float(v_row.get("atr_14_pct", 0.0)) if "atr_14_pct" in v_row else None
            vol_pctile = float(v_row.get("volatility_percentile", 0.0)) if "volatility_percentile" in v_row else None

        evaluation["latest_close"] = latest_close
        evaluation["atr_value"] = atr_value
        evaluation["atr_pct"] = atr_pct

        # 1. Base Theoretical Risk
        equity = self.profile.theoretical_account_equity
        theoretical_risk = calculate_theoretical_risk_amount(equity, self.profile.risk_per_candidate)
        evaluation["theoretical_account_equity"] = equity
        evaluation["theoretical_risk_amount"] = theoretical_risk

        # 2. Budget Capping
        budget_alloc = build_risk_budget_allocation(self.profile)

        dir_bias = risk_row.get("directional_bias", "")
        asset_class = risk_row.get("asset_class", "")

        # Check exposures
        exp_eval = check_exposure_limits(
            {"symbol": spec.symbol, "asset_class": asset_class, "directional_bias": dir_bias},
            existing_sizing_df,
            self.profile
        )
        evaluation["exposure_eval"] = exp_eval
        if exp_eval.get("exposure_warnings"):
            evaluation["warnings"].extend(exp_eval["exposure_warnings"])

        # Hard cap by symbol/asset class remaining budgets
        sym_exp = exp_eval["symbol_exposure_proxy"]
        ac_exp = exp_eval["asset_class_exposure_proxy"]

        sym_rem = max(0.0, budget_alloc.max_symbol_risk_amount - sym_exp)
        ac_rem = max(0.0, budget_alloc.max_asset_class_risk_amount - ac_exp)
        tot_rem = budget_alloc.max_total_portfolio_risk_amount # Ignoring total for simplistic proxy

        capped_risk, cap_details = cap_risk_amount_by_budgets(theoretical_risk, sym_rem, ac_rem, tot_rem)
        evaluation["capped_theoretical_risk_amount"] = capped_risk

        # 3. Adjustments
        adj_context = {
            "atr_pct": atr_pct,
            "volatility_percentile": vol_pctile,
            "risk_readiness_score": risk_row.get("risk_readiness_score", 0.0),
            "total_pretrade_risk_score": risk_row.get("total_pretrade_risk_score", 0.0)
        }

        combined_adj = calculate_combined_sizing_adjustment(adj_context) if self.profile.use_volatility_adjustment else 1.0
        evaluation["combined_adjustment_factor"] = combined_adj

        # 4. ATR Sizing
        sizing_method = "unknown"
        base_units = 0.0
        base_notional = 0.0

        if self.profile.use_atr_based_unit and atr_value and latest_close:
            atr_res = build_atr_sizing_candidate(capped_risk, latest_close, atr_value, 1.0)
            if atr_res["valid"]:
                sizing_method = "atr_based_theoretical"
                base_units = atr_res["theoretical_units"]
                base_notional = atr_res["theoretical_notional"]
            else:
                evaluation["warnings"].extend(atr_res["warnings"])
        else:
            # Fallback to fractional
            if latest_close and latest_close > 0:
                sizing_method = "fixed_fractional_theoretical"
                base_notional = capped_risk * 10 # Arbitrary fallback
                base_units = base_notional / latest_close

        evaluation["sizing_method"] = sizing_method
        evaluation["theoretical_units"] = base_units
        evaluation["theoretical_notional"] = base_notional

        # Apply combined adjustment
        adj_units = apply_sizing_adjustment(base_units, combined_adj)
        adj_notional = adj_units * latest_close if latest_close else 0.0

        evaluation["adjusted_theoretical_units"] = adj_units
        evaluation["adjusted_theoretical_notional"] = adj_notional

        # Filter and label
        label = infer_sizing_candidate_label(risk_row, evaluation, self.profile)
        evaluation["sizing_label"] = label

        candidate = build_sizing_candidate_from_evaluation(risk_row, evaluation, spec.symbol, timeframe)
        return candidate, evaluation

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: Optional[SizingProfile] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:

        if profile:
            self.profile = profile

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "profile": self.profile.name,
            "loaded_risk_candidates": 0,
            "missing_context_frames": [],
            "sizing_candidate_count": 0,
            "passed_sizing_candidate_count": 0,
            "rejected_sizing_candidate_count": 0,
            "watchlist_sizing_candidate_count": 0,
            "warnings": []
        }

        if spec.data_source == 'synthetic' or spec.asset_class in ['macro', 'benchmark']:
            summary["warnings"].append("Skipping synthetic/macro/benchmark symbol.")
            return pd.DataFrame(), summary

        if not self.settings.sizing_candidates_enabled or not self.settings.theoretical_position_sizing_enabled:
            summary["warnings"].append("Sizing candidates are disabled in settings.")
            return pd.DataFrame(), summary

        risk_df, risk_meta = self.load_risk_candidates(spec, timeframe)
        if risk_df.empty:
            summary["warnings"].extend(risk_meta.get("warnings", []))
            return pd.DataFrame(), summary

        summary["loaded_risk_candidates"] = len(risk_df)

        context_frames, ctx_meta = self.load_sizing_context_frames(spec, timeframe)
        summary["missing_context_frames"] = ctx_meta.get("missing_context_frames", [])

        pool = SizingCandidatePool()

        for _, row in risk_df.iterrows():
            # In a real batch we'd pass existing_sizing_df to manage running exposure proxy
            # but for single symbol timeframe it's too isolated.
            candidate, eval_res = self.evaluate_risk_candidate_for_sizing(
                spec, timeframe, row, context_frames, existing_sizing_df=None
            )
            pool.add(candidate)

        df = pool.to_dataframe()
        summary["sizing_candidate_count"] = len(df)

        if not df.empty:
            summary["passed_sizing_candidate_count"] = len(df[df["sizing_label"] == "sizing_approved_candidate"])
            summary["rejected_sizing_candidate_count"] = len(df[df["sizing_label"] == "sizing_rejected_candidate"])
            summary["watchlist_sizing_candidate_count"] = len(df[df["sizing_label"] == "sizing_watchlist_candidate"])

            summary["quality_report"] = build_sizing_quality_report(df, summary)

            if save and self.settings.save_sizing_candidates:
                self.data_lake.save_features(spec, timeframe, "sizing_candidates", df)

        return df, summary

    def build_for_universe(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
        profile: Optional[SizingProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Dict[str, Any]:

        if profile:
            self.profile = profile

        universe_pool = SizingCandidatePool()
        processed = 0
        failed = 0

        for spec in specs:
            if limit and processed >= limit:
                break

            try:
                df, _ = self.build_for_symbol_timeframe(spec, timeframe, profile, save=save)
                if not df.empty:
                    pool = SizingCandidatePool.from_dataframe(df)
                    universe_pool.extend(pool.candidates)
                processed += 1
            except Exception as e:
                logger.error(f"Failed sizing build for {spec.symbol}: {e}")
                failed += 1

        u_df = universe_pool.to_dataframe()

        if save and self.settings.save_sizing_pool and not u_df.empty:
            # We assume data_lake has save_sizing_pool available
            # We will patch data_lake to include this if missing
            if hasattr(self.data_lake, "save_sizing_pool"):
                self.data_lake.save_sizing_pool(timeframe, u_df, self.profile.name)
            else:
                logger.warning("save_sizing_pool not found on DataLake. Bypassing global pool save.")

        return {
            "processed_symbols": processed,
            "failed_symbols": failed,
            "total_candidates": len(u_df),
            "summary": universe_pool.summarize() if not u_df.empty else {}
        }
