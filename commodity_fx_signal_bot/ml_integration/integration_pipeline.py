"""
ML Context Integration Pipeline

Orchestrates loading candidates, building alignment and conflict frames,
and applying score adjustments.
"""

import logging
import pandas as pd
from typing import Dict, Optional, Tuple, List

from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake

from .integration_config import MLIntegrationProfile, get_default_ml_integration_profile
from .context_loader import MLContextIntegrationLoader
from .model_context_components import build_ml_context_component_frame
from .model_signal_alignment import build_model_signal_alignment_frame
from .model_decision_alignment import build_model_decision_alignment_frame
from .model_strategy_alignment import build_model_strategy_alignment_frame
from .model_conflict_filter import build_ml_conflict_filter_frame
from .model_uncertainty_filter import build_ml_uncertainty_filter_frame
from .model_aware_scoring import (
    apply_model_aware_adjustment_to_signal_candidates,
    apply_model_aware_adjustment_to_decision_candidates,
    apply_model_aware_adjustment_to_strategy_candidates,
)
from .integration_quality import check_ml_context_coverage, build_ml_integration_quality_report


logger = logging.getLogger(__name__)


class MLContextIntegrationPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: Optional[MLIntegrationProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_ml_integration_profile()
        self.loader = MLContextIntegrationLoader(data_lake)

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: Optional[MLIntegrationProfile] = None,
        save: bool = True,
    ) -> Tuple[Dict, Dict]:
        """Run ML integration for a single symbol and timeframe."""
        active_profile = profile or self.profile

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "integration_profile": active_profile.name,
            "ml_context_available": False,
            "signal_alignment_rows": 0,
            "decision_alignment_rows": 0,
            "strategy_alignment_rows": 0,
            "conflict_rows": 0,
            "high_conflict_count": 0,
            "high_uncertainty_count": 0,
            "adjustment_applied_layers": [],
            "warnings": [],
        }

        frames = {}

        try:
            # 1. Load ML Context
            ml_context_df, ml_summary = self.loader.load_ml_prediction_context(spec, timeframe, active_profile.name)
            summary["ml_context_available"] = not ml_context_df.empty

            if ml_context_df.empty:
                summary["warnings"].append("ML prediction context unavailable")
                # Continue anyway, pipeline gracefully handles empty ML context by producing neutral/unavailable

            # 2. Load candidate frames
            candidate_frames, cand_summary = self.loader.load_candidate_context_frames(spec, timeframe)
            if cand_summary.get("warnings"):
                summary["warnings"].extend(cand_summary["warnings"])

            coverage_info = check_ml_context_coverage(ml_context_df, candidate_frames.get("signal_candidates"))
            summary["coverage_ratio"] = coverage_info.get("coverage_ratio", 0.0)

            # 3. Model-Signal Alignment
            if "signal_candidates" in candidate_frames and not candidate_frames["signal_candidates"].empty:
                sig_align, _ = build_model_signal_alignment_frame(candidate_frames["signal_candidates"], ml_context_df, active_profile)
                frames["signal_alignment"] = sig_align
                summary["signal_alignment_rows"] = len(sig_align)

                if active_profile.enable_signal_scoring:
                    adj_sig, _ = apply_model_aware_adjustment_to_signal_candidates(candidate_frames["signal_candidates"], sig_align, active_profile)
                    frames["adjusted_signal_candidates"] = adj_sig
                    summary["adjustment_applied_layers"].append("signal")

                # Conflict filter
                sig_conflict, _ = build_ml_conflict_filter_frame(candidate_frames["signal_candidates"], ml_context_df, active_profile, "signal")
                frames["signal_conflict"] = sig_conflict

            # 4. Model-Decision Alignment
            if "decision_candidates" in candidate_frames and not candidate_frames["decision_candidates"].empty:
                dec_align, _ = build_model_decision_alignment_frame(candidate_frames["decision_candidates"], ml_context_df, active_profile)
                frames["decision_alignment"] = dec_align
                summary["decision_alignment_rows"] = len(dec_align)

                if active_profile.enable_decision_scoring:
                    adj_dec, _ = apply_model_aware_adjustment_to_decision_candidates(candidate_frames["decision_candidates"], dec_align, active_profile)
                    frames["adjusted_decision_candidates"] = adj_dec
                    summary["adjustment_applied_layers"].append("decision")

                # Conflict filter
                dec_conflict, dec_conf_summary = build_ml_conflict_filter_frame(candidate_frames["decision_candidates"], ml_context_df, active_profile, "decision")
                frames["decision_conflict"] = dec_conflict
                summary["conflict_rows"] += len(dec_conflict)
                summary["high_conflict_count"] += dec_conf_summary.get("conflict_count", 0)

            # 5. Model-Strategy Alignment
            if "strategy_candidates" in candidate_frames and not candidate_frames["strategy_candidates"].empty:
                str_align, _ = build_model_strategy_alignment_frame(candidate_frames["strategy_candidates"], ml_context_df, active_profile)
                frames["strategy_alignment"] = str_align
                summary["strategy_alignment_rows"] = len(str_align)

                if active_profile.enable_strategy_scoring:
                    adj_str, _ = apply_model_aware_adjustment_to_strategy_candidates(candidate_frames["strategy_candidates"], str_align, active_profile)
                    frames["adjusted_strategy_candidates"] = adj_str
                    summary["adjustment_applied_layers"].append("strategy")

            # 6. Uncertainty Filter
            uncert_frame, uncert_summary = build_ml_uncertainty_filter_frame(ml_context_df, active_profile)
            frames["uncertainty_filter"] = uncert_frame
            summary["high_uncertainty_count"] = uncert_summary.get("high_uncertainty_count", 0)

            # 7. Quality Report
            # use signal_alignment and adjusted_signal_candidates as representative
            quality_report = build_ml_integration_quality_report(
                summary,
                frames.get("signal_alignment"),
                frames.get("adjusted_signal_candidates")
            )
            summary["quality_report"] = quality_report

            if not quality_report["passed"]:
                summary["warnings"].extend(quality_report["warnings"])

            # 8. Save Integration Outputs
            if save and self.settings.ml_context_save_alignment_reports:
                try:
                    for layer in ["signal", "decision", "strategy"]:
                        align_df = frames.get(f"{layer}_alignment")
                        if align_df is not None and not align_df.empty:
                            self.data_lake.save_ml_alignment_report(spec.symbol, timeframe, active_profile.name, align_df, layer)

                    dec_conf = frames.get("decision_conflict")
                    if dec_conf is not None and not dec_conf.empty:
                        self.data_lake.save_ml_conflict_report(spec.symbol, timeframe, active_profile.name, dec_conf)

                    self.data_lake.save_ml_integration_quality(spec.symbol, timeframe, active_profile.name, quality_report)

                    # Note: saving adjusted feature frames is usually done by feature store integration,
                    # we can simulate it with generic integration feature saving if needed:
                    if self.settings.ml_context_save_integration_features:
                        for layer in ["signal", "decision", "strategy"]:
                            adj_df = frames.get(f"adjusted_{layer}_candidates")
                            if adj_df is not None and not adj_df.empty:
                                self.data_lake.save_ml_integration_features(spec.symbol, timeframe, active_profile.name, adj_df, layer)
                except AttributeError as e:
                    logger.debug(f"DataLake save method missing: {e}. Skipping saves for {spec.symbol}")

        except Exception as e:
            logger.error(f"Error building ML integration for {spec.symbol}: {e}")
            summary["warnings"].append(str(e))
            summary["quality_report"] = {"passed": False, "warnings": [str(e)]}

        return summary, frames

    def build_for_universe(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
        profile: Optional[MLIntegrationProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Dict:
        """Run ML integration for multiple symbols."""
        active_profile = profile or self.profile

        batch_summary = {
            "processed": 0,
            "timeframe": timeframe,
            "integration_profile": active_profile.name,
            "symbols": [],
        }

        targets = specs[:limit] if limit else specs

        for spec in targets:
            # Skip synthetic/macro/benchmark
            if spec.symbol.startswith("SYN_") or spec.asset_class in ["macro", "benchmark"]:
                continue

            summary, _ = self.build_for_symbol_timeframe(spec, timeframe, active_profile, save)

            # Extract key metrics
            quality_passed = summary.get("quality_report", {}).get("passed", False)

            batch_summary["symbols"].append({
                "symbol": spec.symbol,
                "asset_class": spec.asset_class,
                "ml_context_available": summary["ml_context_available"],
                "signal_alignment_rows": summary["signal_alignment_rows"],
                "decision_alignment_rows": summary["decision_alignment_rows"],
                "strategy_alignment_rows": summary["strategy_alignment_rows"],
                "high_conflict_count": summary["high_conflict_count"],
                "high_uncertainty_count": summary["high_uncertainty_count"],
                "quality_passed": quality_passed,
            })
            batch_summary["processed"] += 1

        return batch_summary
