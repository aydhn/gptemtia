# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Pipeline Module.

Orchestrates the entire Phase 151 benchmark evaluation contract generation,
validation, diagnostics, readiness scoring, manifest signing, and Phase 152 handoff.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    BenchmarkEvaluationProfile,
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_BENCHMARK_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)
from advanced_benchmark_evaluation.benchmark_evaluation_profile_registry import (
    build_benchmark_evaluation_profile_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_domain_registry import (
    build_benchmark_evaluation_domain_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_scope_registry import (
    build_benchmark_evaluation_scope_registry,
)
from advanced_benchmark_evaluation.benchmark_comparison_report_contracts import (
    build_benchmark_comparison_report_contract_registry,
)
from advanced_benchmark_evaluation.strategy_evaluation_report_contracts import (
    build_strategy_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.benchmark_universe_report_contracts import (
    build_benchmark_universe_report_contract_registry,
)
from advanced_benchmark_evaluation.benchmark_baseline_report_contracts import (
    build_benchmark_baseline_report_contract_registry,
)
from advanced_benchmark_evaluation.strategy_vs_benchmark_report_contracts import (
    build_strategy_vs_benchmark_report_contract_registry,
)
from advanced_benchmark_evaluation.cost_adjusted_evaluation_report_contracts import (
    build_cost_adjusted_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.slippage_adjusted_evaluation_report_contracts import (
    build_slippage_adjusted_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.regime_aware_evaluation_report_contracts import (
    build_regime_aware_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.walk_forward_evaluation_report_contracts import (
    build_walk_forward_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.oos_evaluation_report_contracts import (
    build_oos_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.stress_aware_evaluation_report_contracts import (
    build_stress_aware_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.monte_carlo_robustness_evaluation_report_contracts import (
    build_monte_carlo_robustness_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.parameter_stability_evaluation_report_contracts import (
    build_parameter_stability_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.governance_aware_evaluation_report_contracts import (
    build_governance_aware_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.bias_control_evaluation_report_contracts import (
    build_bias_control_evaluation_report_contract_registry,
)
from advanced_benchmark_evaluation.result_disclosure_report_contracts import (
    build_result_disclosure_report_contract_registry,
)
from advanced_benchmark_evaluation.strategy_evaluation_summary_placeholders import (
    build_strategy_evaluation_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.benchmark_comparison_summary_placeholders import (
    build_benchmark_comparison_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.metric_summary_placeholders import (
    build_metric_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.risk_summary_placeholders import (
    build_risk_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.cost_impact_summary_placeholders import (
    build_cost_impact_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.slippage_impact_summary_placeholders import (
    build_slippage_impact_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.regime_performance_summary_placeholders import (
    build_regime_performance_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.stress_result_summary_placeholders import (
    build_stress_result_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.monte_carlo_result_summary_placeholders import (
    build_monte_carlo_result_summary_placeholder_registry,
)
from advanced_benchmark_evaluation.strategy_limitation_placeholders import (
    build_strategy_limitation_placeholder_registry,
)
from advanced_benchmark_evaluation.benchmark_limitation_placeholders import (
    build_benchmark_limitation_placeholder_registry,
)
from advanced_benchmark_evaluation.report_disclaimers import (
    build_report_disclaimer_registry,
)
from advanced_benchmark_evaluation.strategy_evaluation_metric_placeholders import (
    build_strategy_evaluation_metric_placeholder_registry,
)
from advanced_benchmark_evaluation.benchmark_comparison_metric_placeholders import (
    build_benchmark_comparison_metric_placeholder_registry,
)
from advanced_benchmark_evaluation.relative_performance_metric_placeholders import (
    build_relative_performance_metric_placeholder_registry,
)
from advanced_benchmark_evaluation.risk_adjusted_metric_placeholders import (
    build_risk_adjusted_metric_placeholder_registry,
)
from advanced_benchmark_evaluation.cost_adjusted_metric_placeholders import (
    build_cost_adjusted_metric_placeholder_registry,
)
from advanced_benchmark_evaluation.robustness_metric_placeholders import (
    build_robustness_metric_placeholder_registry,
)
from advanced_benchmark_evaluation.evaluation_input_data_contracts import (
    build_evaluation_input_data_contract_registry,
)
from advanced_benchmark_evaluation.evaluation_feature_input_contracts import (
    build_evaluation_feature_input_contract_registry,
)
from advanced_benchmark_evaluation.evaluation_signal_input_contracts import (
    build_evaluation_signal_input_contract_registry,
)
from advanced_benchmark_evaluation.evaluation_backtest_dependencies import (
    build_evaluation_backtest_dependency_registry,
)
from advanced_benchmark_evaluation.evaluation_walk_forward_dependencies import (
    build_evaluation_walk_forward_dependency_registry,
)
from advanced_benchmark_evaluation.evaluation_stress_dependencies import (
    build_evaluation_stress_dependency_registry,
)
from advanced_benchmark_evaluation.evaluation_monte_carlo_dependencies import (
    build_evaluation_monte_carlo_dependency_registry,
)
from advanced_benchmark_evaluation.evaluation_governance_dependencies import (
    build_evaluation_governance_dependency_registry,
)
from advanced_benchmark_evaluation.evaluation_benchmark_dependencies import (
    build_evaluation_benchmark_dependency_registry,
)
from advanced_benchmark_evaluation.evaluation_no_lookahead_guards import (
    build_evaluation_no_lookahead_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_result_claim_guards import (
    build_evaluation_result_claim_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_performance_claim_guards import (
    build_evaluation_performance_claim_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_strategy_approval_guards import (
    build_evaluation_strategy_approval_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_benchmark_selection_bias_guards import (
    build_evaluation_benchmark_selection_bias_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_data_snooping_bias_guards import (
    build_evaluation_data_snooping_bias_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_overfitting_guards import (
    build_evaluation_overfitting_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_multiple_testing_guards import (
    build_evaluation_multiple_testing_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_metadata_only_news_guards import (
    build_evaluation_metadata_only_news_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_source_preservation_guards import (
    build_evaluation_source_preservation_guard_registry,
)
from advanced_benchmark_evaluation.evaluation_forbidden_column_policies import (
    build_evaluation_forbidden_column_policy_registry,
)
from advanced_benchmark_evaluation.benchmark_report_execution_disabled import (
    build_benchmark_report_execution_disabled_report,
)
from advanced_benchmark_evaluation.strategy_evaluation_execution_disabled import (
    build_strategy_evaluation_execution_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_metric_calculation_disabled import (
    build_evaluation_metric_calculation_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_result_claim_disabled import (
    build_evaluation_result_claim_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_strategy_approval_disabled import (
    build_evaluation_strategy_approval_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_optimizer_disabled import (
    build_evaluation_optimizer_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_model_training_disabled import (
    build_evaluation_model_training_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_prediction_disabled import (
    build_evaluation_prediction_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_live_trading_disabled import (
    build_evaluation_live_trading_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_broker_execution_disabled import (
    build_evaluation_broker_execution_disabled_report,
)
from advanced_benchmark_evaluation.evaluation_deployment_disabled import (
    build_evaluation_deployment_disabled_report,
)
from advanced_benchmark_evaluation.benchmark_evaluation_dependencies import (
    build_benchmark_evaluation_dependency_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_validation_evidence import (
    build_benchmark_evaluation_validation_evidence_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_manual_review import (
    build_benchmark_evaluation_manual_review_queue,
)
from advanced_benchmark_evaluation.benchmark_evaluation_findings import (
    build_benchmark_evaluation_findings_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_readiness_scoring import (
    build_benchmark_evaluation_readiness_score_report,
)
from advanced_benchmark_evaluation.benchmark_evaluation_manifest import (
    build_benchmark_evaluation_manifest,
)
from advanced_benchmark_evaluation.benchmark_evaluation_health import (
    build_benchmark_evaluation_health_check,
)
from advanced_benchmark_evaluation.benchmark_evaluation_validation import (
    build_benchmark_evaluation_validation_report,
)
from advanced_benchmark_evaluation.benchmark_evaluation_safety_boundary import (
    build_benchmark_evaluation_safety_boundary,
)
from advanced_benchmark_evaluation.phase_152_handoff import (
    build_phase_152_backtest_acceptance_report_handoff_report,
)


class BenchmarkEvaluationPipeline:
    """Master pipeline managing all contracts, placeholders, guards, and handoffs for Phase 151."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[BenchmarkEvaluationProfile] = None,
    ):
        self.data_lake = data_lake or DataLake()
        self.settings = settings or Settings()
        self.project_root = project_root or Path(__file__).resolve().parent.parent
        self.profile = profile or get_default_benchmark_evaluation_profile()

    def build_profiles_domains_scope(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Stage 1: Build profile, domain, and scope registries."""
        df_prof, s_prof = build_benchmark_evaluation_profile_registry(self.profile)
        df_dom, s_dom = build_benchmark_evaluation_domain_registry(self.profile)
        df_scope, s_scope = build_benchmark_evaluation_scope_registry(self.profile)

        if save and hasattr(self.data_lake, "save_benchmark_evaluation_profile_registry"):
            self.data_lake.save_benchmark_evaluation_profile_registry(df_prof, s_prof)
            self.data_lake.save_benchmark_evaluation_domain_registry(df_dom, s_dom)
            self.data_lake.save_benchmark_evaluation_scope_registry(df_scope, s_scope)

        tables = {"profiles": df_prof, "domains": df_dom, "scopes": df_scope}
        summary = {"stage": "profiles_domains_scope", "status": STATUS_EVALUATION_CONTRACT_READY, "non_signal": True}
        return tables, summary

    def build_report_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Stage 2: Build benchmark & strategy report contracts, universe, baseline, and comparison contracts."""
        df_bc, s_bc = build_benchmark_comparison_report_contract_registry(self.profile)
        df_se, s_se = build_strategy_evaluation_report_contract_registry(self.profile)
        df_bu, s_bu = build_benchmark_universe_report_contract_registry(self.profile)
        df_bb, s_bb = build_benchmark_baseline_report_contract_registry(self.profile)
        df_svb, s_svb = build_strategy_vs_benchmark_report_contract_registry(self.profile)

        if save:
            if hasattr(self.data_lake, "save_benchmark_comparison_report_contract_registry"):
                self.data_lake.save_benchmark_comparison_report_contract_registry(df_bc, s_bc)
            if hasattr(self.data_lake, "save_strategy_evaluation_report_contract_registry"):
                self.data_lake.save_strategy_evaluation_report_contract_registry(df_se, s_se)
            if hasattr(self.data_lake, "save_benchmark_universe_report_contract_registry"):
                self.data_lake.save_benchmark_universe_report_contract_registry(df_bu, s_bu)
            if hasattr(self.data_lake, "save_benchmark_baseline_report_contract_registry"):
                self.data_lake.save_benchmark_baseline_report_contract_registry(df_bb, s_bb)
            if hasattr(self.data_lake, "save_strategy_vs_benchmark_report_contract_registry"):
                self.data_lake.save_strategy_vs_benchmark_report_contract_registry(df_svb, s_svb)

        tables = {
            "benchmark_contracts": df_bc,
            "strategy_contracts": df_se,
            "universe_contracts": df_bu,
            "baseline_contracts": df_bb,
            "strategy_vs_benchmark": df_svb,
        }
        summary = {"stage": "report_contracts", "status": STATUS_EVALUATION_CONTRACT_READY, "non_signal": True}
        return tables, summary

    def build_specialized_evaluation_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Stage 3: Build cost, slippage, regime, walk-forward, OOS, stress, Monte Carlo, and governance contracts."""
        df_cost, s_cost = build_cost_adjusted_evaluation_report_contract_registry(self.profile)
        df_slip, s_slip = build_slippage_adjusted_evaluation_report_contract_registry(self.profile)
        df_reg, s_reg = build_regime_aware_evaluation_report_contract_registry(self.profile)
        df_wf, s_wf = build_walk_forward_evaluation_report_contract_registry(self.profile)
        df_oos, s_oos = build_oos_evaluation_report_contract_registry(self.profile)
        df_stress, s_stress = build_stress_aware_evaluation_report_contract_registry(self.profile)
        df_mc, s_mc = build_monte_carlo_robustness_evaluation_report_contract_registry(self.profile)
        df_param, s_param = build_parameter_stability_evaluation_report_contract_registry(self.profile)
        df_gov, s_gov = build_governance_aware_evaluation_report_contract_registry(self.profile)
        df_bias, s_bias = build_bias_control_evaluation_report_contract_registry(self.profile)
        df_disc, s_disc = build_result_disclosure_report_contract_registry(self.profile)

        if save:
            if hasattr(self.data_lake, "save_cost_adjusted_evaluation_report_contract_registry"):
                self.data_lake.save_cost_adjusted_evaluation_report_contract_registry(df_cost, s_cost)
            if hasattr(self.data_lake, "save_slippage_adjusted_evaluation_report_contract_registry"):
                self.data_lake.save_slippage_adjusted_evaluation_report_contract_registry(df_slip, s_slip)
            if hasattr(self.data_lake, "save_regime_aware_evaluation_report_contract_registry"):
                self.data_lake.save_regime_aware_evaluation_report_contract_registry(df_reg, s_reg)
            if hasattr(self.data_lake, "save_walk_forward_evaluation_report_contract_registry"):
                self.data_lake.save_walk_forward_evaluation_report_contract_registry(df_wf, s_wf)
            if hasattr(self.data_lake, "save_oos_evaluation_report_contract_registry"):
                self.data_lake.save_oos_evaluation_report_contract_registry(df_oos, s_oos)
            if hasattr(self.data_lake, "save_stress_aware_evaluation_report_contract_registry"):
                self.data_lake.save_stress_aware_evaluation_report_contract_registry(df_stress, s_stress)
            if hasattr(self.data_lake, "save_monte_carlo_robustness_evaluation_report_contract_registry"):
                self.data_lake.save_monte_carlo_robustness_evaluation_report_contract_registry(df_mc, s_mc)
            if hasattr(self.data_lake, "save_governance_aware_evaluation_report_contract_registry"):
                self.data_lake.save_governance_aware_evaluation_report_contract_registry(df_gov, s_gov)

        tables = {
            "cost_contracts": df_cost,
            "slippage_contracts": df_slip,
            "regime_contracts": df_reg,
            "walk_forward_contracts": df_wf,
            "oos_contracts": df_oos,
            "stress_contracts": df_stress,
            "monte_carlo_contracts": df_mc,
            "parameter_stability_contracts": df_param,
            "governance_contracts": df_gov,
            "bias_control_contracts": df_bias,
            "disclosure_contracts": df_disc,
        }
        summary = {"stage": "specialized_contracts", "status": STATUS_EVALUATION_CONTRACT_READY, "non_signal": True}
        return tables, summary

    def build_summary_placeholders(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Stage 4: Build summary and limitation placeholders and disclaimers."""
        df_ss, s_ss = build_strategy_evaluation_summary_placeholder_registry(self.profile)
        df_bs, s_bs = build_benchmark_comparison_summary_placeholder_registry(self.profile)
        df_ms, s_ms = build_metric_summary_placeholder_registry(self.profile)
        df_rs, s_rs = build_risk_summary_placeholder_registry(self.profile)
        df_ci, s_ci = build_cost_impact_summary_placeholder_registry(self.profile)
        df_si, s_si = build_slippage_impact_summary_placeholder_registry(self.profile)
        df_rp, s_rp = build_regime_performance_summary_placeholder_registry(self.profile)
        df_st, s_st = build_stress_result_summary_placeholder_registry(self.profile)
        df_mcr, s_mcr = build_monte_carlo_result_summary_placeholder_registry(self.profile)
        df_slim, s_slim = build_strategy_limitation_placeholder_registry(self.profile)
        df_blim, s_blim = build_benchmark_limitation_placeholder_registry(self.profile)
        df_disc, s_disc = build_report_disclaimer_registry(self.profile)

        if save:
            if hasattr(self.data_lake, "save_strategy_evaluation_summary_placeholder_registry"):
                self.data_lake.save_strategy_evaluation_summary_placeholder_registry(df_ss, s_ss)
            if hasattr(self.data_lake, "save_benchmark_comparison_summary_placeholder_registry"):
                self.data_lake.save_benchmark_comparison_summary_placeholder_registry(df_bs, s_bs)

        tables = {
            "strategy_summaries": df_ss,
            "benchmark_summaries": df_bs,
            "metric_summaries": df_ms,
            "risk_summaries": df_rs,
            "cost_impacts": df_ci,
            "slippage_impacts": df_si,
            "regime_performances": df_rp,
            "stress_results": df_st,
            "monte_carlo_results": df_mcr,
            "strategy_limitations": df_slim,
            "benchmark_limitations": df_blim,
            "disclaimers": df_disc,
        }
        summary = {"stage": "summary_placeholders", "status": STATUS_EVALUATION_CONTRACT_READY, "non_signal": True}
        return tables, summary

    def build_metric_placeholders(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Stage 5: Build uncalculated metric placeholders."""
        df_sm, s_sm = build_strategy_evaluation_metric_placeholder_registry(self.profile)
        df_bm, s_bm = build_benchmark_comparison_metric_placeholder_registry(self.profile)
        df_rm, s_rm = build_relative_performance_metric_placeholder_registry(self.profile)
        df_ram, s_ram = build_risk_adjusted_metric_placeholder_registry(self.profile)
        df_cam, s_cam = build_cost_adjusted_metric_placeholder_registry(self.profile)
        df_rob, s_rob = build_robustness_metric_placeholder_registry(self.profile)

        if save:
            if hasattr(self.data_lake, "save_strategy_evaluation_metric_placeholder_registry"):
                self.data_lake.save_strategy_evaluation_metric_placeholder_registry(df_sm, s_sm)
            if hasattr(self.data_lake, "save_benchmark_comparison_metric_placeholder_registry"):
                self.data_lake.save_benchmark_comparison_metric_placeholder_registry(df_bm, s_bm)
            if hasattr(self.data_lake, "save_relative_performance_metric_placeholder_registry"):
                self.data_lake.save_relative_performance_metric_placeholder_registry(df_rm, s_rm)

        tables = {
            "strategy_metrics": df_sm,
            "benchmark_metrics": df_bm,
            "relative_metrics": df_rm,
            "risk_adjusted_metrics": df_ram,
            "cost_adjusted_metrics": df_cam,
            "robustness_metrics": df_rob,
        }
        summary = {"stage": "metric_placeholders", "status": STATUS_EVALUATION_CONTRACT_READY, "non_signal": True}
        return tables, summary

    def build_dependencies_and_guards(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Stage 6: Build input data contracts, phase dependencies, and boundary guards."""
        df_inp_d, s_inp_d = build_evaluation_input_data_contract_registry(self.profile)
        df_inp_f, s_inp_f = build_evaluation_feature_input_contract_registry(self.profile)
        df_inp_s, s_inp_s = build_evaluation_signal_input_contract_registry(self.profile)

        df_dep_bt, s_dep_bt = build_evaluation_backtest_dependency_registry(self.profile)
        df_dep_wf, s_dep_wf = build_evaluation_walk_forward_dependency_registry(self.profile)
        df_dep_st, s_dep_st = build_evaluation_stress_dependency_registry(self.profile)
        df_dep_mc, s_dep_mc = build_evaluation_monte_carlo_dependency_registry(self.profile)
        df_dep_gov, s_dep_gov = build_evaluation_governance_dependency_registry(self.profile)
        df_dep_bench, s_dep_bench = build_evaluation_benchmark_dependency_registry(self.profile)

        df_g_look, s_g_look = build_evaluation_no_lookahead_guard_registry(self.profile)
        df_g_res, s_g_res = build_evaluation_result_claim_guard_registry(self.profile)
        df_g_perf, s_g_perf = build_evaluation_performance_claim_guard_registry(self.profile)
        df_g_app, s_g_app = build_evaluation_strategy_approval_guard_registry(self.profile)
        df_g_bsel, s_g_bsel = build_evaluation_benchmark_selection_bias_guard_registry(self.profile)
        df_g_dsnoop, s_g_dsnoop = build_evaluation_data_snooping_bias_guard_registry(self.profile)
        df_g_overfit, s_g_overfit = build_evaluation_overfitting_guard_registry(self.profile)
        df_g_mtest, s_g_mtest = build_evaluation_multiple_testing_guard_registry(self.profile)
        df_g_news, s_g_news = build_evaluation_metadata_only_news_guard_registry(self.profile)
        df_g_src, s_g_src = build_evaluation_source_preservation_guard_registry(self.profile)
        df_forbid, s_forbid = build_evaluation_forbidden_column_policy_registry(self.profile)

        if save:
            if hasattr(self.data_lake, "save_evaluation_result_claim_guard_registry"):
                self.data_lake.save_evaluation_result_claim_guard_registry(df_g_res, s_g_res)
            if hasattr(self.data_lake, "save_evaluation_performance_claim_guard_registry"):
                self.data_lake.save_evaluation_performance_claim_guard_registry(df_g_perf, s_g_perf)
            if hasattr(self.data_lake, "save_evaluation_strategy_approval_guard_registry"):
                self.data_lake.save_evaluation_strategy_approval_guard_registry(df_g_app, s_g_app)
            if hasattr(self.data_lake, "save_evaluation_forbidden_column_policy_registry"):
                self.data_lake.save_evaluation_forbidden_column_policy_registry(df_forbid, s_forbid)

        tables = {
            "input_data": df_inp_d,
            "input_features": df_inp_f,
            "input_signals": df_inp_s,
            "guards_lookahead": df_g_look,
            "guards_result_claim": df_g_res,
            "guards_performance_claim": df_g_perf,
            "guards_strategy_approval": df_g_app,
            "forbidden_columns": df_forbid,
        }
        summary = {"stage": "dependencies_and_guards", "status": STATUS_EVALUATION_CONTRACT_READY, "non_signal": True}
        return tables, summary

    def build_disabled_execution_reports(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Stage 7: Build all 11 disabled execution reports."""
        df_d_br, s_d_br = build_benchmark_report_execution_disabled_report(self.profile)
        df_d_se, s_d_se = build_strategy_evaluation_execution_disabled_report(self.profile)
        df_d_mc, s_d_mc = build_evaluation_metric_calculation_disabled_report(self.profile)
        df_d_rc, s_d_rc = build_evaluation_result_claim_disabled_report(self.profile)
        df_d_sa, s_d_sa = build_evaluation_strategy_approval_disabled_report(self.profile)
        df_d_opt, s_d_opt = build_evaluation_optimizer_disabled_report(self.profile)
        df_d_trn, s_d_trn = build_evaluation_model_training_disabled_report(self.profile)
        df_d_prd, s_d_prd = build_evaluation_prediction_disabled_report(self.profile)
        df_d_lt, s_d_lt = build_evaluation_live_trading_disabled_report(self.profile)
        df_d_brk, s_d_brk = build_evaluation_broker_execution_disabled_report(self.profile)
        df_d_dep, s_d_dep = build_evaluation_deployment_disabled_report(self.profile)

        if save:
            if hasattr(self.data_lake, "save_benchmark_report_execution_disabled_report"):
                self.data_lake.save_benchmark_report_execution_disabled_report(df_d_br, s_d_br)
            if hasattr(self.data_lake, "save_strategy_evaluation_execution_disabled_report"):
                self.data_lake.save_strategy_evaluation_execution_disabled_report(df_d_se, s_d_se)
            if hasattr(self.data_lake, "save_evaluation_metric_calculation_disabled_report"):
                self.data_lake.save_evaluation_metric_calculation_disabled_report(df_d_mc, s_d_mc)
            if hasattr(self.data_lake, "save_evaluation_result_claim_disabled_report"):
                self.data_lake.save_evaluation_result_claim_disabled_report(df_d_rc, s_d_rc)
            if hasattr(self.data_lake, "save_evaluation_strategy_approval_disabled_report"):
                self.data_lake.save_evaluation_strategy_approval_disabled_report(df_d_sa, s_d_sa)
            if hasattr(self.data_lake, "save_evaluation_live_trading_disabled_report"):
                self.data_lake.save_evaluation_live_trading_disabled_report(df_d_lt, s_d_lt)
            if hasattr(self.data_lake, "save_evaluation_broker_execution_disabled_report"):
                self.data_lake.save_evaluation_broker_execution_disabled_report(df_d_brk, s_d_brk)

        tables = {
            "benchmark_report_disabled": df_d_br,
            "strategy_evaluation_disabled": df_d_se,
            "metric_calculation_disabled": df_d_mc,
            "result_claim_disabled": df_d_rc,
            "strategy_approval_disabled": df_d_sa,
            "optimizer_disabled": df_d_opt,
            "training_disabled": df_d_trn,
            "prediction_disabled": df_d_prd,
            "live_trading_disabled": df_d_lt,
            "broker_disabled": df_d_brk,
            "deployment_disabled": df_d_dep,
        }
        summary = {"stage": "disabled_execution_reports", "status": STATUS_EVALUATION_CONTRACT_READY, "non_signal": True}
        return tables, summary

    def build_findings_scoring_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Stage 8: Build findings, manual review queue, readiness score, and manifest."""
        df_dep, s_dep = build_benchmark_evaluation_dependency_registry(self.profile)
        df_evid, s_evid = build_benchmark_evaluation_validation_evidence_registry(self.profile)
        df_rev, s_rev = build_benchmark_evaluation_manual_review_queue(self.profile)
        df_find, s_find = build_benchmark_evaluation_findings_registry(self.profile)
        df_score, s_score = build_benchmark_evaluation_readiness_score_report(self.profile)
        df_man, s_man = build_benchmark_evaluation_manifest(self.profile)

        if save:
            if hasattr(self.data_lake, "save_benchmark_evaluation_dependencies"):
                self.data_lake.save_benchmark_evaluation_dependencies(df_dep, s_dep)
            if hasattr(self.data_lake, "save_benchmark_evaluation_validation_evidence"):
                self.data_lake.save_benchmark_evaluation_validation_evidence(df_evid, s_evid)
            if hasattr(self.data_lake, "save_benchmark_evaluation_manual_review_queue"):
                self.data_lake.save_benchmark_evaluation_manual_review_queue(df_rev, s_rev)
            if hasattr(self.data_lake, "save_benchmark_evaluation_findings_registry"):
                self.data_lake.save_benchmark_evaluation_findings_registry(df_find, s_find)
            if hasattr(self.data_lake, "save_benchmark_evaluation_readiness_score_report"):
                self.data_lake.save_benchmark_evaluation_readiness_score_report(df_score, s_score)
            if hasattr(self.data_lake, "save_benchmark_evaluation_manifest"):
                self.data_lake.save_benchmark_evaluation_manifest(df_man, s_man)

        tables = {
            "dependencies": df_dep,
            "evidence": df_evid,
            "manual_review": df_rev,
            "findings": df_find,
            "readiness_score": df_score,
            "manifest": df_man,
        }
        summary = {"stage": "findings_scoring_manifest", "status": STATUS_EVALUATION_CONTRACT_READY, "non_signal": True}
        return tables, summary

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Stage 9: Build health check, validation report, safety boundary, and Phase 152 handoff."""
        df_health, s_health = build_benchmark_evaluation_health_check(self.project_root, self.profile)
        t_rep, _ = self.build_report_contracts(save=False)
        t_man, _ = self.build_findings_scoring_manifest(save=False)
        combined_tables = {**t_rep, **t_man}

        df_val, s_val = build_benchmark_evaluation_validation_report(combined_tables, self.profile)
        df_safe, s_safe = build_benchmark_evaluation_safety_boundary(self.profile)
        df_hnd, s_hnd = build_phase_152_backtest_acceptance_report_handoff_report(self.profile)

        if save:
            if hasattr(self.data_lake, "save_benchmark_evaluation_health_check"):
                self.data_lake.save_benchmark_evaluation_health_check(df_health, s_health)
            if hasattr(self.data_lake, "save_benchmark_evaluation_validation_report"):
                self.data_lake.save_benchmark_evaluation_validation_report(df_val, s_val)
            if hasattr(self.data_lake, "save_benchmark_evaluation_safety_boundary"):
                self.data_lake.save_benchmark_evaluation_safety_boundary(df_safe, s_safe)
            if hasattr(self.data_lake, "save_phase_152_backtest_acceptance_report_handoff_report"):
                self.data_lake.save_phase_152_backtest_acceptance_report_handoff_report(df_hnd, s_hnd)

        tables = {
            "health": df_health,
            "validation": df_val,
            "safety": df_safe,
            "handoff": df_hnd,
        }
        summary = {"stage": "health_validation_safety_handoff", "status": STATUS_EVALUATION_CONTRACT_READY, "non_signal": True}
        return tables, summary

    def build_benchmark_evaluation_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Generate high-level status across all 9 pipeline stages."""
        s1_t, s1 = self.build_profiles_domains_scope(save=save)
        s2_t, s2 = self.build_report_contracts(save=save)
        s3_t, s3 = self.build_specialized_evaluation_contracts(save=save)
        s4_t, s4 = self.build_summary_placeholders(save=save)
        s5_t, s5 = self.build_metric_placeholders(save=save)
        s6_t, s6 = self.build_dependencies_and_guards(save=save)
        s7_t, s7 = self.build_disabled_execution_reports(save=save)
        s8_t, s8 = self.build_findings_scoring_manifest(save=save)
        s9_t, s9 = self.build_health_validation_safety_handoff(save=save)

        status_rows = [
            {"stage_num": 1, "stage_name": "profiles_domains_scope", "status": s1["status"]},
            {"stage_num": 2, "stage_name": "report_contracts", "status": s2["status"]},
            {"stage_num": 3, "stage_name": "specialized_contracts", "status": s3["status"]},
            {"stage_num": 4, "stage_name": "summary_placeholders", "status": s4["status"]},
            {"stage_num": 5, "stage_name": "metric_placeholders", "status": s5["status"]},
            {"stage_num": 6, "stage_name": "dependencies_and_guards", "status": s6["status"]},
            {"stage_num": 7, "stage_name": "disabled_execution_reports", "status": s7["status"]},
            {"stage_num": 8, "stage_name": "findings_scoring_manifest", "status": s8["status"]},
            {"stage_num": 9, "stage_name": "health_validation_safety_handoff", "status": s9["status"]},
        ]
        df_status = pd.DataFrame(status_rows)
        all_ready = bool((df_status["status"] == STATUS_EVALUATION_CONTRACT_READY).all())

        summary = {
            "domain": LABEL_BENCHMARK_EVALUATION_DOMAIN,
            "pipeline_name": "benchmark_evaluation_pipeline",
            "current_phase": 151,
            "next_phase": 152,
            "all_stages_ready": all_ready,
            "status": STATUS_EVALUATION_CONTRACT_READY if all_ready else "PIPELINE_INCOMPLETE",
            "non_signal": True,
        }
        return df_status, summary
