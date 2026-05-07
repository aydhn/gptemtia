"""
Validation pipeline orchestrator.
"""

import logging
import pandas as pd
from typing import Optional, Tuple, Dict, Any

from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake

from validation.validation_config import ValidationProfile, get_default_validation_profile
from validation.time_splits import create_walk_forward_splits, validate_time_splits
from validation.walk_forward import WalkForwardValidator
from validation.robustness_analysis import build_robustness_report
from validation.overfitting_checks import build_overfitting_report
from validation.parameter_grid import build_profile_parameter_grid, generate_parameter_sets
from validation.parameter_sensitivity import build_parameter_result_table, build_parameter_sensitivity_report
from validation.optimizer_runner import OptimizerCandidateRunner
from validation.validation_quality import (
    check_validation_input_integrity,
    check_split_coverage,
    check_walk_forward_result_quality,
    check_parameter_result_quality,
    check_for_forbidden_live_terms_in_validation,
    build_validation_quality_report
)

logger = logging.getLogger(__name__)


class ValidationPipeline:
    """Orchestrates the entire validation and research process."""

    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: Optional[ValidationProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_validation_profile()

    def load_validation_inputs(
        self,
        spec: SymbolSpec,
        timeframe: str,
        backtest_profile_name: str,
    ) -> Tuple[Optional[pd.DataFrame], Optional[pd.DataFrame], Optional[pd.DataFrame], Optional[dict]]:
        """Loads required inputs from the data lake."""
        try:
            # For pure backtest
            trades_df = self.data_lake.load_backtest_trades(spec.symbol, timeframe, backtest_profile_name)
            equity_curve = self.data_lake.load_backtest_equity_curve(spec.symbol, timeframe, backtest_profile_name)
            summary = self.data_lake.load_backtest_summary(spec.symbol, timeframe, backtest_profile_name)

            # Load price data if available (often needed for full evaluation, though not strictly required if trades have entry/exit)
            price_df = self.data_lake.load_processed_ohlcv(spec.symbol, timeframe)

            return price_df, trades_df, equity_curve, summary
        except Exception as e:
            logger.error(f"Error loading validation inputs for {spec.symbol} {timeframe}: {e}")
            return None, None, None, None

    def run_walk_forward_validation(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        backtest_profile_name: str = "balanced_candidate_backtest",
        profile: Optional[ValidationProfile] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        """Runs walk-forward validation for a single backtest result."""
        active_profile = profile or self.profile

        price_df, trades_df, equity_curve, performance_summary = self.load_validation_inputs(
            spec, timeframe, backtest_profile_name
        )

        # Quality check inputs
        input_quality = check_validation_input_integrity(price_df, trades_df, equity_curve)
        if not input_quality["passed"]:
            logger.warning(f"Validation input integrity failed for {spec.symbol}: {input_quality['warnings']}")
            return pd.DataFrame(), {"warnings": input_quality["warnings"]}

        # Create splits based on price index or trade timestamps
        index = price_df.index if price_df is not None else pd.DatetimeIndex(trades_df['entry_time'])

        splits = create_walk_forward_splits(
            index=index,
            train_window_bars=active_profile.train_window_bars,
            test_window_bars=active_profile.test_window_bars,
            step_bars=active_profile.step_bars,
            expanding_window=active_profile.expanding_window,
            min_train_bars=active_profile.min_train_bars,
            min_test_bars=active_profile.min_test_bars
        )

        split_quality = check_split_coverage(splits)

        # Run evaluation
        validator = WalkForwardValidator(active_profile)
        wf_df, wf_summary = validator.evaluate_walk_forward(splits, trades_df, equity_curve)

        wf_quality = check_walk_forward_result_quality(wf_df)

        # Robustness & Overfitting
        robustness = build_robustness_report(wf_df)
        overfitting = build_overfitting_report(walk_forward_df=wf_df)

        # Combine summaries
        final_summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "validation_profile": active_profile.name,
            "backtest_profile": backtest_profile_name,
            **wf_summary,
            "robustness": robustness,
            "overfitting": overfitting,
        }

        forbidden_check = check_for_forbidden_live_terms_in_validation(wf_df, final_summary)

        quality_report = build_validation_quality_report({
            "input": input_quality,
            "splits": split_quality,
            "walk_forward": wf_quality,
            "forbidden_terms": forbidden_check
        })

        final_summary["quality_report"] = quality_report

        if save and self.settings.save_walk_forward_results:
             if hasattr(self.data_lake, 'save_walk_forward_results'):
                 self.data_lake.save_walk_forward_results(spec.symbol, timeframe, active_profile.name, wf_df)
             if hasattr(self.data_lake, 'save_validation_summary'):
                 self.data_lake.save_validation_summary(spec.symbol, timeframe, f"{active_profile.name}_wf", final_summary)

        return wf_df, final_summary

    def run_parameter_sensitivity(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        backtest_profile_name: str = "balanced_candidate_backtest",
        profile: Optional[ValidationProfile] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        """Runs parameter sensitivity analysis."""
        active_profile = profile or self.profile

        # In a real scenario, this would load results from multiple backtest runs
        # For now, we simulate this if multiple runs aren't available
        # We need a way to load all parameter variation results.
        # Assuming we just load the main one and maybe mock variations for structural testing

        price_df, trades_df, equity_curve, performance_summary = self.load_validation_inputs(
            spec, timeframe, backtest_profile_name
        )

        if performance_summary is None:
             return pd.DataFrame(), {"warnings": ["Missing performance summary"]}

        # Mocking parameter results for structure if none exist in a multi-run way
        # In a full implementation, you'd load multiple summaries from a sweep
        results = [performance_summary]

        result_table = build_parameter_result_table(results)

        sens_df, sens_summary = build_parameter_sensitivity_report(result_table, primary_metric=active_profile.primary_metric)

        overfitting = build_overfitting_report(sensitivity_df=sens_df)
        sens_summary["overfitting"] = overfitting

        final_summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "validation_profile": active_profile.name,
            "backtest_profile": backtest_profile_name,
            **sens_summary
        }

        forbidden_check = check_for_forbidden_live_terms_in_validation(sens_df, final_summary)

        quality_report = build_validation_quality_report({
            "parameters": check_parameter_result_quality(result_table),
            "forbidden_terms": forbidden_check
        })
        final_summary["quality_report"] = quality_report

        if save and self.settings.save_parameter_sensitivity:
            if hasattr(self.data_lake, 'save_parameter_sensitivity'):
                self.data_lake.save_parameter_sensitivity(spec.symbol, timeframe, active_profile.name, sens_df)
            if hasattr(self.data_lake, 'save_validation_summary'):
                 self.data_lake.save_validation_summary(spec.symbol, timeframe, f"{active_profile.name}_sens", final_summary)

        return sens_df, final_summary

    def run_optimizer_candidate_analysis(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        backtest_profile_name: str = "balanced_candidate_backtest",
        profile: Optional[ValidationProfile] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        """Runs candidate ranking analysis."""
        active_profile = profile or self.profile

        # In reality, this evaluates multiple generated parameter sets
        grid = build_profile_parameter_grid()
        param_sets = generate_parameter_sets(grid, max_combinations=active_profile.max_parameter_combinations)

        runner = OptimizerCandidateRunner(active_profile)

        # Load main baseline
        _, _, _, performance_summary = self.load_validation_inputs(spec, timeframe, backtest_profile_name)
        if performance_summary is None:
             return pd.DataFrame(), {"warnings": ["Missing performance summary"]}

        # Run WF for baseline to get context
        wf_df, wf_summary = self.run_walk_forward_validation(spec, timeframe, backtest_profile_name, active_profile, save=False)

        # Score each param set (mocking performance variants here, in reality would use real runs)
        results = []
        for pset in param_sets:
            # We use baseline performance for all in this mock, but they get different IDs
            # A real implementation loops over actual results per parameter set
            score_res = runner.score_parameter_set(
                pset,
                performance_summary,
                walk_forward_summary=wf_summary,
                robustness_summary=wf_summary.get('robustness', {})
            )
            results.append(score_res)

        opt_df, opt_summary = runner.build_optimizer_candidate_report(results)

        final_summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "validation_profile": active_profile.name,
            **opt_summary
        }

        forbidden_check = check_for_forbidden_live_terms_in_validation(opt_df, final_summary)

        quality_report = build_validation_quality_report({
            "forbidden_terms": forbidden_check
        })
        final_summary["quality_report"] = quality_report

        if save and hasattr(self.data_lake, 'save_optimizer_candidates'):
            self.data_lake.save_optimizer_candidates(spec.symbol, timeframe, active_profile.name, opt_df)
            if hasattr(self.data_lake, 'save_validation_summary'):
                 self.data_lake.save_validation_summary(spec.symbol, timeframe, f"{active_profile.name}_opt", final_summary)

        return opt_df, final_summary

    def run_universe_validation(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        backtest_profile_name: str = "balanced_candidate_backtest",
        profile: Optional[ValidationProfile] = None,
        limit: Optional[int] = None,
        save: bool = True,
    ) -> dict:
        """Runs validation for multiple symbols."""
        if limit:
            specs = specs[:limit]

        results = []
        for spec in specs:
            try:
                # We'll just run Walk Forward for universe batch to keep it simple and indicative
                wf_df, wf_summary = self.run_walk_forward_validation(
                    spec, timeframe, backtest_profile_name, profile, save
                )

                res = {
                    "symbol": spec.symbol,
                    "asset_class": spec.asset_class,
                    "split_count": wf_summary.get("valid_split_count", 0),
                    "robustness_score": wf_summary.get("robustness", {}).get("robustness_score", 0.0),
                    "overfitting_risk_score": wf_summary.get("overfitting", {}).get("aggregate_overfitting_risk_score", 1.0),
                    "stability_score": wf_summary.get("test_positive_ratio", 0.0),
                    "quality_passed": wf_summary.get("quality_report", {}).get("passed", False),
                }

                # Determine pseudo status
                if not res["quality_passed"]:
                    res["validation_status"] = "validation_failed"
                elif res["split_count"] < 2:
                    res["validation_status"] = "insufficient_data"
                elif res["overfitting_risk_score"] > 0.7:
                     res["validation_status"] = "overfitting_risk_high"
                elif res["robustness_score"] < 0.5:
                     res["validation_status"] = "robustness_low"
                else:
                     res["validation_status"] = "validation_passed"

                results.append(res)
            except Exception as e:
                logger.error(f"Error in universe validation for {spec.symbol}: {e}")
                results.append({
                    "symbol": spec.symbol,
                    "asset_class": spec.asset_class,
                    "validation_status": "unknown_validation_status"
                })

        ranking_df = pd.DataFrame(results)
        if not ranking_df.empty and 'robustness_score' in ranking_df.columns:
            ranking_df = ranking_df.sort_values(by="robustness_score", ascending=False).reset_index(drop=True)

        return {
            "processed_count": len(results),
            "passed_count": len([r for r in results if r.get("validation_status") == "validation_passed"]),
            "ranking": ranking_df.to_dict(orient="records") if not ranking_df.empty else []
        }
