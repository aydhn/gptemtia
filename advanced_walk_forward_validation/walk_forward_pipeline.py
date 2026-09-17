# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Validation Pipeline.

Orchestrates all Phase 147 components, registries, contracts, guards,
manifests, and reports into a unified execution flow.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_walk_forward_validation.walk_forward_config import (
    WalkForwardProfile,
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.walk_forward_profile_registry import (
    build_walk_forward_profile_registry,
)
from advanced_walk_forward_validation.walk_forward_domain_registry import (
    build_walk_forward_domain_registry,
)
from advanced_walk_forward_validation.walk_forward_scope_registry import (
    build_walk_forward_scope_registry,
)
from advanced_walk_forward_validation.walk_forward_validation_contracts import (
    build_walk_forward_validation_contract_registry,
)
from advanced_walk_forward_validation.rolling_window_validation_contracts import (
    build_rolling_window_validation_contract_registry,
)
from advanced_walk_forward_validation.expanding_window_validation_contracts import (
    build_expanding_window_validation_contract_registry,
)
from advanced_walk_forward_validation.anchored_window_validation_contracts import (
    build_anchored_window_validation_contract_registry,
)
from advanced_walk_forward_validation.purged_walk_forward_contracts import (
    build_purged_walk_forward_contract_registry,
)
from advanced_walk_forward_validation.embargo_policies import (
    build_embargo_policy_registry,
)
from advanced_walk_forward_validation.train_validation_test_split_contracts import (
    build_train_validation_test_split_contract_registry,
)
from advanced_walk_forward_validation.out_of_sample_split_contracts import (
    build_out_of_sample_split_contract_registry,
)
from advanced_walk_forward_validation.holdout_period_contracts import (
    build_holdout_period_contract_registry,
)
from advanced_walk_forward_validation.temporal_split_boundaries import (
    build_temporal_split_boundary_registry,
)
from advanced_walk_forward_validation.regime_aware_split_contracts import (
    build_regime_aware_split_contract_registry,
)
from advanced_walk_forward_validation.cross_asset_oos_split_contracts import (
    build_cross_asset_oos_split_contract_registry,
)
from advanced_walk_forward_validation.walk_forward_fold_contracts import (
    build_walk_forward_fold_contract_registry,
)
from advanced_walk_forward_validation.walk_forward_schedule_placeholders import (
    build_walk_forward_schedule_placeholder_registry,
)
from advanced_walk_forward_validation.oos_benchmark_contracts import (
    build_oos_benchmark_contract_registry,
)
from advanced_walk_forward_validation.benchmark_universe_contracts import (
    build_benchmark_universe_contract_registry,
)
from advanced_walk_forward_validation.benchmark_baseline_contracts import (
    build_benchmark_baseline_contract_registry,
)
from advanced_walk_forward_validation.benchmark_comparison_contracts import (
    build_benchmark_comparison_contract_registry,
)
from advanced_walk_forward_validation.naive_baseline_placeholders import (
    build_naive_baseline_placeholder_registry,
)
from advanced_walk_forward_validation.buy_and_hold_benchmark_placeholders import (
    build_buy_and_hold_benchmark_placeholder_registry,
)
from advanced_walk_forward_validation.cash_benchmark_placeholders import (
    build_cash_benchmark_placeholder_registry,
)
from advanced_walk_forward_validation.equal_weight_benchmark_placeholders import (
    build_equal_weight_benchmark_placeholder_registry,
)
from advanced_walk_forward_validation.regime_benchmark_placeholders import (
    build_regime_benchmark_placeholder_registry,
)
from advanced_walk_forward_validation.cost_aware_benchmark_placeholders import (
    build_cost_aware_benchmark_placeholder_registry,
)
from advanced_walk_forward_validation.benchmark_metric_placeholders import (
    build_benchmark_metric_placeholder_registry,
)
from advanced_walk_forward_validation.oos_metric_placeholders import (
    build_oos_metric_placeholder_registry,
)
from advanced_walk_forward_validation.validation_metric_placeholders import (
    build_validation_metric_placeholder_registry,
)
from advanced_walk_forward_validation.walk_forward_output_contracts import (
    build_walk_forward_output_contract_registry,
)
from advanced_walk_forward_validation.benchmark_output_contracts import (
    build_benchmark_output_contract_registry,
)
from advanced_walk_forward_validation.validation_evidence import (
    build_validation_evidence_registry,
)
from advanced_walk_forward_validation.validation_data_contracts import (
    build_validation_data_contract_registry,
)
from advanced_walk_forward_validation.validation_feature_input_contracts import (
    build_validation_feature_input_contract_registry,
)
from advanced_walk_forward_validation.validation_signal_input_contracts import (
    build_validation_signal_input_contract_registry,
)
from advanced_walk_forward_validation.validation_backtest_dependencies import (
    build_validation_backtest_dependency_registry,
)
from advanced_walk_forward_validation.validation_transaction_cost_dependencies import (
    build_validation_transaction_cost_dependency_registry,
)
from advanced_walk_forward_validation.validation_slippage_dependencies import (
    build_validation_slippage_dependency_registry,
)
from advanced_walk_forward_validation.validation_regime_dependencies import (
    build_validation_regime_dependency_registry,
)
from advanced_walk_forward_validation.validation_model_contract_dependencies import (
    build_validation_model_contract_dependency_registry,
)
from advanced_walk_forward_validation.validation_governance_dependencies import (
    build_validation_governance_dependency_registry,
)
from advanced_walk_forward_validation.validation_no_lookahead_guards import (
    build_validation_no_lookahead_guard_registry,
)
from advanced_walk_forward_validation.validation_purge_embargo_guards import (
    build_validation_purge_embargo_guard_registry,
)
from advanced_walk_forward_validation.validation_data_snooping_bias_guards import (
    build_validation_data_snooping_bias_guard_registry,
)
from advanced_walk_forward_validation.validation_overfitting_guards import (
    build_validation_overfitting_guard_registry,
)
from advanced_walk_forward_validation.validation_survivorship_bias_guards import (
    build_validation_survivorship_bias_guard_registry,
)
from advanced_walk_forward_validation.validation_multiple_testing_guards import (
    build_validation_multiple_testing_guard_registry,
)
from advanced_walk_forward_validation.validation_metadata_only_news_guards import (
    build_validation_metadata_only_news_guard_registry,
)
from advanced_walk_forward_validation.validation_source_preservation_guards import (
    build_validation_source_preservation_guard_registry,
)
from advanced_walk_forward_validation.validation_forbidden_column_policies import (
    build_validation_forbidden_column_policy_registry,
)
from advanced_walk_forward_validation.walk_forward_execution_disabled import (
    build_walk_forward_execution_disabled_report,
)
from advanced_walk_forward_validation.oos_benchmark_execution_disabled import (
    build_oos_benchmark_execution_disabled_report,
)
from advanced_walk_forward_validation.benchmark_metric_calculation_disabled import (
    build_benchmark_metric_calculation_disabled_report,
)
from advanced_walk_forward_validation.validation_optimizer_disabled import (
    build_validation_optimizer_disabled_report,
)
from advanced_walk_forward_validation.validation_model_training_disabled import (
    build_validation_model_training_disabled_report,
)
from advanced_walk_forward_validation.validation_prediction_disabled import (
    build_validation_prediction_disabled_report,
)
from advanced_walk_forward_validation.validation_live_trading_disabled import (
    build_validation_live_trading_disabled_report,
)
from advanced_walk_forward_validation.validation_broker_execution_disabled import (
    build_validation_broker_execution_disabled_report,
)
from advanced_walk_forward_validation.validation_performance_claim_disabled import (
    build_validation_performance_claim_disabled_report,
)
from advanced_walk_forward_validation.walk_forward_manual_review import (
    build_walk_forward_manual_review_queue,
)
from advanced_walk_forward_validation.walk_forward_findings import (
    build_walk_forward_findings_registry,
)
from advanced_walk_forward_validation.walk_forward_readiness_scoring import (
    build_walk_forward_readiness_score_report,
)
from advanced_walk_forward_validation.walk_forward_manifest import (
    build_walk_forward_validation_manifest,
)
from advanced_walk_forward_validation.walk_forward_health import (
    build_walk_forward_health_check,
)
from advanced_walk_forward_validation.walk_forward_validation import (
    build_walk_forward_validation_report,
)
from advanced_walk_forward_validation.walk_forward_safety_boundary import (
    build_walk_forward_safety_boundary,
)
from advanced_walk_forward_validation.phase_148_handoff import (
    build_phase_148_stress_testing_scenario_simulation_handoff_report,
)
from advanced_walk_forward_validation.walk_forward_report_builder import (
    build_walk_forward_profile_markdown_report,
    build_walk_forward_contract_markdown_report,
    build_oos_split_contract_markdown_report,
    build_benchmark_contract_markdown_report,
    build_benchmark_placeholder_markdown_report,
    build_validation_metric_placeholder_markdown_report,
    build_validation_guard_markdown_report,
    build_validation_disabled_execution_markdown_report,
    build_walk_forward_findings_markdown_report,
    build_walk_forward_readiness_score_markdown_report,
    build_walk_forward_manifest_markdown_report,
    build_walk_forward_validation_markdown_report,
    build_walk_forward_safety_markdown_report,
    build_phase_148_handoff_markdown_report,
)


class WalkForwardValidationPipeline:
    """Pipeline orchestrating all Phase 147 Walk-Forward Validation & OOS Benchmarking operations."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[WalkForwardProfile] = None,
    ):
        self.settings = settings or get_settings()
        self.data_lake = data_lake or DataLake()
        self.project_root = project_root or Path(__file__).resolve().parent.parent
        self.profile = profile or get_default_walk_forward_profile()

    def build_profiles_domains_scope(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build Phase 147 profiles, domain, and scope registries."""
        df_prof, s_prof = build_walk_forward_profile_registry(self.profile)
        df_dom, s_dom = build_walk_forward_domain_registry(self.profile)
        df_scp, s_scp = build_walk_forward_scope_registry(self.profile)

        if save:
            self.data_lake.save_walk_forward_profile_registry(df_prof, s_prof)
            self.data_lake.save_walk_forward_domain_registry(df_dom, s_dom)
            self.data_lake.save_walk_forward_scope_registry(df_scp, s_scp)

        dfs = {"profiles": df_prof, "domains": df_dom, "scopes": df_scp}
        summaries = {"profiles": s_prof, "domains": s_dom, "scopes": s_scp}
        return dfs, summaries

    def build_split_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build all walk-forward split and window contracts."""
        df_wf, s_wf = build_walk_forward_validation_contract_registry(self.profile)
        df_roll, s_roll = build_rolling_window_validation_contract_registry(self.profile)
        df_exp, s_exp = build_expanding_window_validation_contract_registry(self.profile)
        df_anc, s_anc = build_anchored_window_validation_contract_registry(self.profile)
        df_prg, s_prg = build_purged_walk_forward_contract_registry(self.profile)
        df_emb, s_emb = build_embargo_policy_registry(self.profile)
        df_splt, s_splt = build_train_validation_test_split_contract_registry(self.profile)
        df_oos, s_oos = build_out_of_sample_split_contract_registry(self.profile)
        df_hld, s_hld = build_holdout_period_contract_registry(self.profile)
        df_bnd, s_bnd = build_temporal_split_boundary_registry(self.profile)
        df_rgm, s_rgm = build_regime_aware_split_contract_registry(self.profile)
        df_crs, s_crs = build_cross_asset_oos_split_contract_registry(self.profile)
        df_fld, s_fld = build_walk_forward_fold_contract_registry(self.profile)
        df_sch, s_sch = build_walk_forward_schedule_placeholder_registry(self.profile)

        if save:
            self.data_lake.save_walk_forward_validation_contract_registry(df_wf, s_wf)
            self.data_lake.save_rolling_window_validation_contract_registry(df_roll, s_roll)
            self.data_lake.save_expanding_window_validation_contract_registry(df_exp, s_exp)
            self.data_lake.save_anchored_window_validation_contract_registry(df_anc, s_anc)
            self.data_lake.save_purged_walk_forward_contract_registry(df_prg, s_prg)
            self.data_lake.save_embargo_policy_registry(df_emb, s_emb)
            self.data_lake.save_train_validation_test_split_contract_registry(df_splt, s_splt)
            self.data_lake.save_out_of_sample_split_contract_registry(df_oos, s_oos)
            self.data_lake.save_holdout_period_contract_registry(df_hld, s_hld)
            self.data_lake.save_temporal_split_boundary_registry(df_bnd, s_bnd)
            self.data_lake.save_regime_aware_split_contract_registry(df_rgm, s_rgm)
            self.data_lake.save_cross_asset_oos_split_contract_registry(df_crs, s_crs)

        dfs = {
            "walk_forward_contracts": df_wf,
            "rolling_contracts": df_roll,
            "expanding_contracts": df_exp,
            "anchored_contracts": df_anc,
            "purged_contracts": df_prg,
            "embargo_policies": df_emb,
            "train_val_test_splits": df_splt,
            "oos_splits": df_oos,
            "holdout_periods": df_hld,
            "temporal_boundaries": df_bnd,
            "regime_splits": df_rgm,
            "cross_asset_splits": df_crs,
            "fold_contracts": df_fld,
            "schedules": df_sch,
        }
        summaries = {
            "walk_forward": s_wf,
            "rolling": s_roll,
            "expanding": s_exp,
            "anchored": s_anc,
            "purged": s_prg,
            "embargo": s_emb,
            "train_val_test": s_splt,
            "oos_splits": s_oos,
            "holdout": s_hld,
            "boundaries": s_bnd,
            "regime_splits": s_rgm,
            "cross_asset": s_crs,
            "folds": s_fld,
            "schedules": s_sch,
        }
        return dfs, summaries

    def build_oos_benchmark_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build benchmark universe, baseline, and comparison contracts."""
        df_bnch, s_bnch = build_oos_benchmark_contract_registry(self.profile)
        df_uni, s_uni = build_benchmark_universe_contract_registry(self.profile)
        df_base, s_base = build_benchmark_baseline_contract_registry(self.profile)
        df_cmp, s_cmp = build_benchmark_comparison_contract_registry(self.profile)
        df_nv, s_nv = build_naive_baseline_placeholder_registry(self.profile)
        df_bnh, s_bnh = build_buy_and_hold_benchmark_placeholder_registry(self.profile)
        df_csh, s_csh = build_cash_benchmark_placeholder_registry(self.profile)
        df_ew, s_ew = build_equal_weight_benchmark_placeholder_registry(self.profile)
        df_rgm, s_rgm = build_regime_benchmark_placeholder_registry(self.profile)
        df_cst, s_cst = build_cost_aware_benchmark_placeholder_registry(self.profile)

        if save:
            self.data_lake.save_oos_benchmark_contract_registry(df_bnch, s_bnch)
            self.data_lake.save_benchmark_universe_contract_registry(df_uni, s_uni)
            self.data_lake.save_benchmark_baseline_contract_registry(df_base, s_base)
            self.data_lake.save_benchmark_comparison_contract_registry(df_cmp, s_cmp)

        dfs = {
            "oos_benchmark_contracts": df_bnch,
            "benchmark_universe": df_uni,
            "benchmark_baseline": df_base,
            "benchmark_comparison": df_cmp,
            "naive_baseline": df_nv,
            "buy_and_hold": df_bnh,
            "cash_benchmark": df_csh,
            "equal_weight": df_ew,
            "regime_benchmark": df_rgm,
            "cost_aware_benchmark": df_cst,
        }
        summaries = {
            "benchmarks": s_bnch,
            "universes": s_uni,
            "baselines": s_base,
            "comparisons": s_cmp,
            "naive": s_nv,
            "buy_and_hold": s_bnh,
            "cash": s_csh,
            "equal_weight": s_ew,
            "regime": s_rgm,
            "cost_aware": s_cst,
        }
        return dfs, summaries

    def build_metric_placeholders_outputs(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build metric placeholder and output contract registries."""
        df_bm, s_bm = build_benchmark_metric_placeholder_registry(self.profile)
        df_oosm, s_oosm = build_oos_metric_placeholder_registry(self.profile)
        df_vm, s_vm = build_validation_metric_placeholder_registry(self.profile)
        df_wfo, s_wfo = build_walk_forward_output_contract_registry(self.profile)
        df_bmo, s_bmo = build_benchmark_output_contract_registry(self.profile)

        if save:
            self.data_lake.save_benchmark_metric_placeholder_registry(df_bm, s_bm)
            self.data_lake.save_oos_metric_placeholder_registry(df_oosm, s_oosm)
            self.data_lake.save_validation_metric_placeholder_registry(df_vm, s_vm)

        dfs = {
            "benchmark_metrics": df_bm,
            "oos_metrics": df_oosm,
            "validation_metrics": df_vm,
            "walk_forward_outputs": df_wfo,
            "benchmark_outputs": df_bmo,
        }
        summaries = {
            "benchmark_metrics": s_bm,
            "oos_metrics": s_oosm,
            "validation_metrics": s_vm,
            "wf_outputs": s_wfo,
            "bm_outputs": s_bmo,
        }
        return dfs, summaries

    def build_dependencies_and_guards(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build dependencies and security guards."""
        df_evd, s_evd = build_validation_evidence_registry(self.profile)
        df_dat, s_dat = build_validation_data_contract_registry(self.profile)
        df_ftr, s_ftr = build_validation_feature_input_contract_registry(self.profile)
        df_sig, s_sig = build_validation_signal_input_contract_registry(self.profile)
        df_bkt, s_bkt = build_validation_backtest_dependency_registry(self.profile)
        df_cst, s_cst = build_validation_transaction_cost_dependency_registry(self.profile)
        df_slp, s_slp = build_validation_slippage_dependency_registry(self.profile)
        df_rgm, s_rgm = build_validation_regime_dependency_registry(self.profile)
        df_mdl, s_mdl = build_validation_model_contract_dependency_registry(self.profile)
        df_gov, s_gov = build_validation_governance_dependency_registry(self.profile)

        df_lk, s_lk = build_validation_no_lookahead_guard_registry(self.profile)
        df_prg, s_prg = build_validation_purge_embargo_guard_registry(self.profile)
        df_snp, s_snp = build_validation_data_snooping_bias_guard_registry(self.profile)
        df_ovf, s_ovf = build_validation_overfitting_guard_registry(self.profile)
        df_srv, s_srv = build_validation_survivorship_bias_guard_registry(self.profile)
        df_mul, s_mul = build_validation_multiple_testing_guard_registry(self.profile)
        df_nws, s_nws = build_validation_metadata_only_news_guard_registry(self.profile)
        df_src, s_src = build_validation_source_preservation_guard_registry(self.profile)
        df_frb, s_frb = build_validation_forbidden_column_policy_registry(self.profile)

        if save:
            self.data_lake.save_validation_no_lookahead_guard_registry(df_lk, s_lk)
            self.data_lake.save_validation_purge_embargo_guard_registry(df_prg, s_prg)
            self.data_lake.save_validation_data_snooping_bias_guard_registry(df_snp, s_snp)
            self.data_lake.save_validation_overfitting_guard_registry(df_ovf, s_ovf)
            self.data_lake.save_validation_survivorship_bias_guard_registry(df_srv, s_srv)
            self.data_lake.save_validation_multiple_testing_guard_registry(df_mul, s_mul)
            self.data_lake.save_validation_forbidden_column_policy_registry(df_frb, s_frb)

        dfs = {
            "evidence": df_evd,
            "data_contracts": df_dat,
            "feature_contracts": df_ftr,
            "signal_contracts": df_sig,
            "backtest_dependencies": df_bkt,
            "cost_dependencies": df_cst,
            "slippage_dependencies": df_slp,
            "regime_dependencies": df_rgm,
            "model_dependencies": df_mdl,
            "governance_dependencies": df_gov,
            "no_lookahead_guards": df_lk,
            "purge_embargo_guards": df_prg,
            "data_snooping_guards": df_snp,
            "overfitting_guards": df_ovf,
            "survivorship_guards": df_srv,
            "multiple_testing_guards": df_mul,
            "news_guards": df_nws,
            "source_guards": df_src,
            "forbidden_column_policies": df_frb,
        }
        summaries = {
            "evidence": s_evd,
            "data": s_dat,
            "feature": s_ftr,
            "signal": s_sig,
            "backtest": s_bkt,
            "cost": s_cst,
            "slippage": s_slp,
            "regime": s_rgm,
            "model": s_mdl,
            "governance": s_gov,
            "no_lookahead": s_lk,
            "purge_embargo": s_prg,
            "data_snooping": s_snp,
            "overfitting": s_ovf,
            "survivorship": s_srv,
            "multiple_testing": s_mul,
            "news": s_nws,
            "source": s_src,
            "forbidden": s_frb,
        }
        return dfs, summaries

    def build_disabled_execution_reports(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build disabled execution reports."""
        df_wf, s_wf = build_walk_forward_execution_disabled_report(self.profile)
        df_bnch, s_bnch = build_oos_benchmark_execution_disabled_report(self.profile)
        df_mc, s_mc = build_benchmark_metric_calculation_disabled_report(self.profile)
        df_opt, s_opt = build_validation_optimizer_disabled_report(self.profile)
        df_trn, s_trn = build_validation_model_training_disabled_report(self.profile)
        df_prd, s_prd = build_validation_prediction_disabled_report(self.profile)
        df_liv, s_liv = build_validation_live_trading_disabled_report(self.profile)
        df_brk, s_brk = build_validation_broker_execution_disabled_report(self.profile)
        df_clm, s_clm = build_validation_performance_claim_disabled_report(self.profile)

        if save:
            self.data_lake.save_walk_forward_execution_disabled_report(df_wf, s_wf)
            self.data_lake.save_oos_benchmark_execution_disabled_report(df_bnch, s_bnch)
            self.data_lake.save_benchmark_metric_calculation_disabled_report(df_mc, s_mc)
            self.data_lake.save_validation_optimizer_disabled_report(df_opt, s_opt)
            self.data_lake.save_validation_live_trading_disabled_report(df_liv, s_liv)
            self.data_lake.save_validation_broker_execution_disabled_report(df_brk, s_brk)

        dfs = {
            "walk_forward_disabled": df_wf,
            "benchmark_disabled": df_bnch,
            "metric_calc_disabled": df_mc,
            "optimizer_disabled": df_opt,
            "training_disabled": df_trn,
            "prediction_disabled": df_prd,
            "live_trading_disabled": df_liv,
            "broker_disabled": df_brk,
            "claims_disabled": df_clm,
        }
        summaries = {
            "wf_disabled": s_wf,
            "bnch_disabled": s_bnch,
            "mc_disabled": s_mc,
            "opt_disabled": s_opt,
            "trn_disabled": s_trn,
            "prd_disabled": s_prd,
            "liv_disabled": s_liv,
            "brk_disabled": s_brk,
            "clm_disabled": s_clm,
        }
        return dfs, summaries

    def build_findings_scoring_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build findings, review queue, diagnostic score, and manifest."""
        df_fnd, s_fnd = build_walk_forward_findings_registry(self.profile)
        df_rev, s_rev = build_walk_forward_manual_review_queue(self.profile)
        df_scr, s_scr = build_walk_forward_readiness_score_report(self.profile)
        df_man, s_man = build_walk_forward_validation_manifest(self.profile)

        if save:
            self.data_lake.save_walk_forward_findings_registry(df_fnd, s_fnd)
            self.data_lake.save_walk_forward_readiness_score_report(df_scr, s_scr)
            self.data_lake.save_walk_forward_validation_manifest(df_man, s_man)

        dfs = {
            "findings": df_fnd,
            "manual_review": df_rev,
            "readiness_score": df_scr,
            "manifest": df_man,
        }
        summaries = {
            "findings": s_fnd,
            "manual_review": s_rev,
            "readiness_score": s_scr,
            "manifest": s_man,
        }
        return dfs, summaries

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build health check, validation check, safety matrix, and Phase 148 handoff."""
        df_hlth, s_hlth = build_walk_forward_health_check(self.project_root, self.profile)
        df_prof, _ = build_walk_forward_profile_registry(self.profile)
        df_wf, _ = build_walk_forward_validation_contract_registry(self.profile)
        df_bnch, _ = build_oos_benchmark_contract_registry(self.profile)
        df_grd, _ = build_validation_no_lookahead_guard_registry(self.profile)
        df_man, _ = build_walk_forward_validation_manifest(self.profile)

        tables_for_val = {
            "profiles": df_prof,
            "walk_forward_contracts": df_wf,
            "oos_benchmark_contracts": df_bnch,
            "no_lookahead_guards": df_grd,
            "manifest": df_man,
        }
        df_val, s_val = build_walk_forward_validation_report(tables_for_val, self.profile)
        df_sft, s_sft = build_walk_forward_safety_boundary(self.profile)
        df_hnd, s_hnd = build_phase_148_stress_testing_scenario_simulation_handoff_report(self.profile)

        if save:
            self.data_lake.save_walk_forward_health_check(df_hlth, s_hlth)
            self.data_lake.save_walk_forward_validation_report(df_val, s_val)
            self.data_lake.save_walk_forward_safety_boundary(df_sft, s_sft)
            self.data_lake.save_phase_148_stress_testing_scenario_simulation_handoff_report(df_hnd, s_hnd)

        dfs = {
            "health": df_hlth,
            "validation": df_val,
            "safety": df_sft,
            "phase_148_handoff": df_hnd,
        }
        summaries = {
            "health": s_hlth,
            "validation": s_val,
            "safety": s_sft,
            "phase_148_handoff": s_hnd,
        }
        return dfs, summaries

    def build_walk_forward_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Build master status report compiling all subsystems."""
        d1, s1 = self.build_profiles_domains_scope(save=save)
        d2, s2 = self.build_split_contracts(save=save)
        d3, s3 = self.build_oos_benchmark_contracts(save=save)
        d4, s4 = self.build_metric_placeholders_outputs(save=save)
        d5, s5 = self.build_dependencies_and_guards(save=save)
        d6, s6 = self.build_disabled_execution_reports(save=save)
        d7, s7 = self.build_findings_scoring_manifest(save=save)
        d8, s8 = self.build_health_validation_safety_handoff(save=save)

        status_rows = [
            {"subsystem": "Profiles & Scope", "status": "READY", "items_count": len(d1["profiles"])},
            {"subsystem": "Split Contracts", "status": "READY", "items_count": len(d2["walk_forward_contracts"])},
            {"subsystem": "Benchmark Contracts", "status": "READY", "items_count": len(d3["oos_benchmark_contracts"])},
            {"subsystem": "Metric Placeholders", "status": "READY", "items_count": len(d4["benchmark_metrics"])},
            {"subsystem": "Guards & Policies", "status": "ACTIVE", "items_count": len(d5["no_lookahead_guards"])},
            {"subsystem": "Disabled Execution", "status": "ENFORCED", "items_count": len(d6["walk_forward_disabled"])},
            {"subsystem": "Findings & Scoring", "status": "ASSESSED", "items_count": len(d7["findings"])},
            {"subsystem": "Health & Handoff", "status": "READY", "items_count": len(d8["phase_148_handoff"])},
        ]
        status_df = pd.DataFrame(status_rows)

        master_summary = {
            "phase": 147,
            "target_final_phase": 160,
            "next_phase": 148,
            "profile": self.profile.profile_name,
            "readiness_score": s7["readiness_score"]["score"],
            "validation_status": s8["validation"]["validation_status"],
            "health_status": s8["health"]["status"],
            "safety_status": s8["safety"]["safety_status"],
            "phase_148_handoff_ready": s8["phase_148_handoff"]["status"] == "READY_FOR_PHASE_148",
            "live_trading": False,
            "broker_execution": False,
            "walk_forward_executed": False,
            "benchmark_executed": False,
            "metric_calculated": False,
            "non_signal": True,
        }

        if save:
            out_dir = Path("reports/output/advanced_walk_forward_validation")
            out_dir.mkdir(parents=True, exist_ok=True)

            md_prof = build_walk_forward_profile_markdown_report(s1["profiles"], d1["profiles"])
            md_wf = build_walk_forward_contract_markdown_report(s2["walk_forward"], d2["walk_forward_contracts"])
            md_oos = build_oos_split_contract_markdown_report(s2["oos_splits"], d2["oos_splits"])
            md_bnch = build_benchmark_contract_markdown_report(s3["benchmarks"], d3["oos_benchmark_contracts"])
            md_plc = build_benchmark_placeholder_markdown_report(s3["buy_and_hold"], d3["buy_and_hold"])
            md_vm = build_validation_metric_placeholder_markdown_report(s4["benchmark_metrics"], d4["benchmark_metrics"])
            md_grd = build_validation_guard_markdown_report(s5["no_lookahead"], d5["no_lookahead_guards"])
            md_dis = build_validation_disabled_execution_markdown_report(s6["wf_disabled"], d6["walk_forward_disabled"])
            md_fnd = build_walk_forward_findings_markdown_report(s7["findings"], d7["findings"])
            md_scr = build_walk_forward_readiness_score_markdown_report(s7["readiness_score"], d7["readiness_score"])
            md_man = build_walk_forward_manifest_markdown_report(s7["manifest"], d7["manifest"])
            md_val = build_walk_forward_validation_markdown_report(s8["validation"], d8["validation"])
            md_sft = build_walk_forward_safety_markdown_report(s8["safety"], d8["safety"])
            md_hnd = build_phase_148_handoff_markdown_report(s8["phase_148_handoff"], d8["phase_148_handoff"])

            reports_to_write = [
                ("profiles.md", md_prof),
                ("walk_forward_contracts.md", md_wf),
                ("oos_splits.md", md_oos),
                ("benchmark_contracts.md", md_bnch),
                ("benchmark_placeholders.md", md_plc),
                ("metric_placeholders.md", md_vm),
                ("guards.md", md_grd),
                ("disabled_execution.md", md_dis),
                ("findings.md", md_fnd),
                ("readiness_score.md", md_scr),
                ("manifest.md", md_man),
                ("validation.md", md_val),
                ("safety.md", md_sft),
                ("phase_148_handoff.md", md_hnd),
            ]
            for fname, content in reports_to_write:
                with open(out_dir / fname, "w", encoding="utf-8") as f:
                    f.write(content)

            self.data_lake.save_walk_forward_report(
                self.profile.profile_name, master_summary, md_man
            )

        return status_df, master_summary
