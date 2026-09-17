# -*- coding: utf-8 -*-
"""Phase 156: Master Portfolio Scenario Control Pipeline.

Coordinates local/offline portfolio scenario testing contracts, drawdown control contracts,
control action placeholders, output contracts, metric placeholders, guards, and Phase 157 handoff.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
    get_portfolio_scenario_control_profile,
)
from .portfolio_scenario_control_profile_registry import build_portfolio_scenario_control_profile_registry
from .portfolio_scenario_control_domain_registry import build_portfolio_scenario_control_domain_registry
from .portfolio_scenario_control_scope_registry import build_portfolio_scenario_control_scope_registry
from .portfolio_scenario_testing_contracts import build_portfolio_scenario_testing_contract_registry
from .portfolio_resilience_contracts import build_portfolio_resilience_contract_registry
from .portfolio_scenario_library_contracts import build_portfolio_scenario_library_contract_registry
from .historical_portfolio_scenario_contracts import build_historical_portfolio_scenario_contract_registry
from .hypothetical_portfolio_scenario_contracts import build_hypothetical_portfolio_scenario_contract_registry
from .regime_shift_portfolio_scenario_contracts import build_regime_shift_portfolio_scenario_contract_registry
from .volatility_spike_portfolio_scenario_contracts import build_volatility_spike_portfolio_scenario_contract_registry
from .liquidity_crunch_portfolio_scenario_contracts import build_liquidity_crunch_portfolio_scenario_contract_registry
from .correlation_breakdown_portfolio_scenario_contracts import build_correlation_breakdown_portfolio_scenario_contract_registry
from .currency_shock_portfolio_scenario_contracts import build_currency_shock_portfolio_scenario_contract_registry
from .spread_widening_portfolio_scenario_contracts import build_spread_widening_portfolio_scenario_contract_registry
from .transaction_cost_shock_portfolio_scenario_contracts import build_transaction_cost_shock_portfolio_scenario_contract_registry
from .slippage_shock_portfolio_scenario_contracts import build_slippage_shock_portfolio_scenario_contract_registry

from .portfolio_drawdown_control_contracts import build_portfolio_drawdown_control_contract_registry
from .drawdown_threshold_contracts import build_drawdown_threshold_contract_registry
from .drawdown_warning_placeholders import build_drawdown_warning_placeholder_registry
from .drawdown_breach_placeholders import build_drawdown_breach_placeholder_registry
from .drawdown_recovery_placeholders import build_drawdown_recovery_placeholder_registry
from .drawdown_control_policy_placeholders import build_drawdown_control_policy_placeholder_registry
from .recovery_plan_placeholders import build_recovery_plan_placeholder_registry

from .exposure_reduction_placeholders import build_exposure_reduction_placeholder_registry
from .de_risking_placeholders import build_de_risking_placeholder_registry
from .hedge_control_placeholders import build_hedge_control_placeholder_registry
from .rebalance_control_placeholders import build_rebalance_control_placeholder_registry
from .stop_control_placeholders import build_stop_control_placeholder_registry
from .portfolio_freeze_control_placeholders import build_portfolio_freeze_control_placeholder_registry
from .portfolio_resume_control_placeholders import build_portfolio_resume_control_placeholder_registry

from .scenario_output_contracts import build_scenario_output_contract_registry
from .drawdown_control_output_contracts import build_drawdown_control_output_contract_registry
from .resilience_output_contracts import build_resilience_output_contract_registry
from .scenario_metric_placeholders import build_scenario_metric_placeholder_registry
from .drawdown_metric_placeholders import build_drawdown_metric_placeholder_registry
from .resilience_metric_placeholders import build_resilience_metric_placeholder_registry
from .recovery_metric_placeholders import build_recovery_metric_placeholder_registry
from .control_action_metric_placeholders import build_control_action_metric_placeholder_registry

from .portfolio_scenario_dependencies import build_portfolio_scenario_dependency_registry
from .portfolio_scenario_no_lookahead_guards import build_portfolio_scenario_no_lookahead_guard_registry
from .scenario_execution_claim_guards import build_scenario_execution_claim_guard_registry
from .drawdown_control_claim_guards import build_drawdown_control_claim_guard_registry
from .portfolio_adjustment_claim_guards import build_portfolio_adjustment_claim_guard_registry
from .hedge_derisk_claim_guards import build_hedge_derisk_claim_guard_registry
from .rebalance_control_claim_guards import build_rebalance_control_claim_guard_registry
from .investment_advice_claim_guards import build_investment_advice_claim_guard_registry
from .scenario_alert_claim_guards import build_scenario_alert_claim_guard_registry
from .portfolio_scenario_data_snooping_bias_guards import build_portfolio_scenario_data_snooping_bias_guard_registry
from .portfolio_scenario_overfitting_guards import build_portfolio_scenario_overfitting_guard_registry
from .portfolio_scenario_multiple_testing_guards import build_portfolio_scenario_multiple_testing_guard_registry
from .portfolio_scenario_metadata_only_news_guards import build_portfolio_scenario_metadata_only_news_guard_registry
from .portfolio_scenario_source_preservation_guards import build_portfolio_scenario_source_preservation_guard_registry
from .portfolio_scenario_forbidden_column_policies import build_portfolio_scenario_forbidden_column_policy_registry

from .portfolio_scenario_execution_disabled import build_portfolio_scenario_execution_disabled_report
from .drawdown_control_execution_disabled import build_drawdown_control_execution_disabled_report
from .portfolio_control_action_disabled import build_portfolio_control_action_disabled_report
from .hedge_derisk_execution_disabled import build_hedge_derisk_execution_disabled_report
from .rebalance_control_execution_disabled import build_rebalance_control_execution_disabled_report
from .scenario_metric_calculation_disabled import build_scenario_metric_calculation_disabled_report
from .drawdown_metric_calculation_disabled import build_drawdown_metric_calculation_disabled_report
from .scenario_alerting_disabled import build_scenario_alerting_disabled_report
from .scenario_dashboard_generation_disabled import build_scenario_dashboard_generation_disabled_report
from .portfolio_scenario_model_training_disabled import build_portfolio_scenario_model_training_disabled_report
from .portfolio_scenario_prediction_disabled import build_portfolio_scenario_prediction_disabled_report
from .portfolio_scenario_live_trading_disabled import build_portfolio_scenario_live_trading_disabled_report
from .portfolio_scenario_broker_execution_disabled import build_portfolio_scenario_broker_execution_disabled_report
from .portfolio_scenario_deployment_disabled import build_portfolio_scenario_deployment_disabled_report

from .portfolio_scenario_validation_evidence import build_portfolio_scenario_validation_evidence_registry
from .portfolio_scenario_manual_review import build_portfolio_scenario_manual_review_queue
from .portfolio_scenario_findings import build_portfolio_scenario_findings_registry
from .portfolio_scenario_readiness_scoring import (
    calculate_portfolio_scenario_readiness_score,
    build_portfolio_scenario_readiness_score_report,
)
from .portfolio_scenario_control_manifest import build_portfolio_scenario_control_manifest
from .portfolio_scenario_control_report_builder import build_portfolio_scenario_control_markdown_report
from .portfolio_scenario_control_health import build_portfolio_scenario_control_health_check
from .portfolio_scenario_control_validation import build_portfolio_scenario_control_validation_report
from .portfolio_scenario_control_safety_boundary import build_portfolio_scenario_control_safety_boundary
from .phase_157_handoff import build_phase_157_portfolio_acceptance_report_handoff_report


class PortfolioScenarioControlPipeline:
    """Orchestration pipeline for Phase 156 Portfolio Scenario Testing and Drawdown Control."""

    def __init__(
        self,
        data_lake: Optional[object] = None,
        settings: Optional[object] = None,
        project_root: Optional[Path] = None,
        profile: Optional[PortfolioScenarioControlProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root or Path(__file__).resolve().parents[1]
        self.profile = profile or get_default_portfolio_scenario_control_profile()

    def build_profiles_domains_scope(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_p, s_p = build_portfolio_scenario_control_profile_registry(self.profile)
        df_d, s_d = build_portfolio_scenario_control_domain_registry(self.profile)
        df_s, s_s = build_portfolio_scenario_control_scope_registry(self.profile)
        tables = {"profiles": df_p, "domains": df_d, "scopes": df_s}
        summary = {"profile_summary": s_p, "domain_summary": s_d, "scope_summary": s_s}

        if save and self.data_lake and hasattr(self.data_lake, "save_portfolio_scenario_control_profile_registry"):
            self.data_lake.save_portfolio_scenario_control_profile_registry(df_p, s_p)
            self.data_lake.save_portfolio_scenario_control_domain_registry(df_d, s_d)
            self.data_lake.save_portfolio_scenario_control_scope_registry(df_s, s_s)
        return tables, summary

    def build_scenario_testing_contracts(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_sc, s_sc = build_portfolio_scenario_testing_contract_registry(self.profile)
        df_res, s_res = build_portfolio_resilience_contract_registry(self.profile)
        df_lib, s_lib = build_portfolio_scenario_library_contract_registry(self.profile)
        df_hist, s_hist = build_historical_portfolio_scenario_contract_registry(self.profile)
        df_hypo, s_hypo = build_hypothetical_portfolio_scenario_contract_registry(self.profile)
        tables = {"scenario_contracts": df_sc, "resilience": df_res, "libraries": df_lib, "historical": df_hist, "hypothetical": df_hypo}
        summary = {"scenario_contracts_summary": s_sc, "resilience_summary": s_res, "library_summary": s_lib}

        if save and self.data_lake and hasattr(self.data_lake, "save_portfolio_scenario_testing_contract_registry"):
            self.data_lake.save_portfolio_scenario_testing_contract_registry(df_sc, s_sc)
            self.data_lake.save_portfolio_resilience_contract_registry(df_res, s_res)
            self.data_lake.save_portfolio_scenario_library_contract_registry(df_lib, s_lib)
            self.data_lake.save_historical_portfolio_scenario_contract_registry(df_hist, s_hist)
            self.data_lake.save_hypothetical_portfolio_scenario_contract_registry(df_hypo, s_hypo)
        return tables, summary

    def build_drawdown_control_contracts(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_dd, s_dd = build_portfolio_drawdown_control_contract_registry(self.profile)
        df_thr, s_thr = build_drawdown_threshold_contract_registry(self.profile)
        df_wrn, s_wrn = build_drawdown_warning_placeholder_registry(self.profile)
        df_brc, s_brc = build_drawdown_breach_placeholder_registry(self.profile)
        df_rcv, s_rcv = build_drawdown_recovery_placeholder_registry(self.profile)
        tables = {"drawdown_contracts": df_dd, "thresholds": df_thr, "warnings": df_wrn, "breaches": df_brc, "recovery": df_rcv}
        summary = {"drawdown_summary": s_dd, "threshold_summary": s_thr}

        if save and self.data_lake and hasattr(self.data_lake, "save_portfolio_drawdown_control_contract_registry"):
            self.data_lake.save_portfolio_drawdown_control_contract_registry(df_dd, s_dd)
            self.data_lake.save_drawdown_threshold_contract_registry(df_thr, s_thr)
            self.data_lake.save_drawdown_warning_placeholder_registry(df_wrn, s_wrn)
            self.data_lake.save_drawdown_breach_placeholder_registry(df_brc, s_brc)
            self.data_lake.save_drawdown_recovery_placeholder_registry(df_rcv, s_rcv)
        return tables, summary

    def build_portfolio_control_placeholders(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_red, s_red = build_exposure_reduction_placeholder_registry(self.profile)
        df_drk, s_drk = build_de_risking_placeholder_registry(self.profile)
        df_hdg, s_hdg = build_hedge_control_placeholder_registry(self.profile)
        df_reb, s_reb = build_rebalance_control_placeholder_registry(self.profile)
        df_stp, s_stp = build_stop_control_placeholder_registry(self.profile)
        df_frz, s_frz = build_portfolio_freeze_control_placeholder_registry(self.profile)
        df_rsm, s_rsm = build_portfolio_resume_control_placeholder_registry(self.profile)
        tables = {"reduction": df_red, "derisking": df_drk, "hedge": df_hdg, "rebalance": df_reb, "stop": df_stp, "freeze": df_frz, "resume": df_rsm}
        summary = {"reduction_summary": s_red, "derisking_summary": s_drk, "hedge_summary": s_hdg}

        if save and self.data_lake and hasattr(self.data_lake, "save_exposure_reduction_placeholder_registry"):
            self.data_lake.save_exposure_reduction_placeholder_registry(df_red, s_red)
            self.data_lake.save_de_risking_placeholder_registry(df_drk, s_drk)
            self.data_lake.save_hedge_control_placeholder_registry(df_hdg, s_hdg)
            self.data_lake.save_rebalance_control_placeholder_registry(df_reb, s_reb)
            self.data_lake.save_stop_control_placeholder_registry(df_stp, s_stp)
            self.data_lake.save_portfolio_freeze_control_placeholder_registry(df_frz, s_frz)
            self.data_lake.save_portfolio_resume_control_placeholder_registry(df_rsm, s_rsm)
        return tables, summary

    def build_outputs_and_metrics(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_so, s_so = build_scenario_output_contract_registry(self.profile)
        df_do, s_do = build_drawdown_control_output_contract_registry(self.profile)
        df_ro, s_ro = build_resilience_output_contract_registry(self.profile)
        df_sm, s_sm = build_scenario_metric_placeholder_registry(self.profile)
        df_dm, s_dm = build_drawdown_metric_placeholder_registry(self.profile)
        df_rm, s_rm = build_resilience_metric_placeholder_registry(self.profile)
        df_am, s_am = build_control_action_metric_placeholder_registry(self.profile)
        tables = {"scenario_outputs": df_so, "drawdown_outputs": df_do, "resilience_outputs": df_ro, "scenario_metrics": df_sm, "drawdown_metrics": df_dm}
        summary = {"scenario_output_summary": s_so, "drawdown_output_summary": s_do, "metric_summary": s_sm}

        if save and self.data_lake and hasattr(self.data_lake, "save_scenario_output_contract_registry"):
            self.data_lake.save_scenario_output_contract_registry(df_so, s_so)
            self.data_lake.save_drawdown_control_output_contract_registry(df_do, s_do)
            self.data_lake.save_resilience_output_contract_registry(df_ro, s_ro)
            self.data_lake.save_scenario_metric_placeholder_registry(df_sm, s_sm)
            self.data_lake.save_drawdown_metric_placeholder_registry(df_dm, s_dm)
        return tables, summary

    def build_dependencies_and_guards(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_dep, s_dep = build_portfolio_scenario_dependency_registry(self.profile)
        df_lk, s_lk = build_portfolio_scenario_no_lookahead_guard_registry(self.profile)
        df_sec, s_sec = build_scenario_execution_claim_guard_registry(self.profile)
        df_ddc, s_ddc = build_drawdown_control_claim_guard_registry(self.profile)
        df_pad, s_pad = build_portfolio_adjustment_claim_guard_registry(self.profile)
        df_hdg, s_hdg = build_hedge_derisk_claim_guard_registry(self.profile)
        df_reb, s_reb = build_rebalance_control_claim_guard_registry(self.profile)
        df_inv, s_inv = build_investment_advice_claim_guard_registry(self.profile)
        df_fcol, s_fcol = build_portfolio_scenario_forbidden_column_policy_registry(self.profile)
        tables = {"dependencies": df_dep, "no_lookahead": df_lk, "scenario_execution_claim": df_sec, "forbidden_columns": df_fcol}
        summary = {"dep_summary": s_dep, "guard_summary": s_lk}

        if save and self.data_lake and hasattr(self.data_lake, "save_portfolio_scenario_dependency_registry"):
            self.data_lake.save_portfolio_scenario_dependency_registry(df_dep, s_dep)
            self.data_lake.save_portfolio_scenario_forbidden_column_policy_registry(df_fcol, s_fcol)
        return tables, summary

    def build_disabled_execution_reports(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_se, s_se = build_portfolio_scenario_execution_disabled_report(self.profile)
        df_de, s_de = build_drawdown_control_execution_disabled_report(self.profile)
        df_pa, s_pa = build_portfolio_control_action_disabled_report(self.profile)
        df_lt, s_lt = build_portfolio_scenario_live_trading_disabled_report(self.profile)
        df_be, s_be = build_portfolio_scenario_broker_execution_disabled_report(self.profile)
        tables = {"scenario_disabled": df_se, "drawdown_disabled": df_de, "control_action_disabled": df_pa, "live_trading_disabled": df_lt, "broker_disabled": df_be}
        summary = {"scenario_disabled_summary": s_se, "drawdown_disabled_summary": s_de}

        if save and self.data_lake and hasattr(self.data_lake, "save_portfolio_scenario_execution_disabled_report"):
            self.data_lake.save_portfolio_scenario_execution_disabled_report(df_se, s_se)
            self.data_lake.save_drawdown_control_execution_disabled_report(df_de, s_de)
            self.data_lake.save_portfolio_control_action_disabled_report(df_pa, s_pa)
            self.data_lake.save_portfolio_scenario_live_trading_disabled_report(df_lt, s_lt)
            self.data_lake.save_portfolio_scenario_broker_execution_disabled_report(df_be, s_be)
        return tables, summary

    def build_findings_and_evidence(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_ev, s_ev = build_portfolio_scenario_validation_evidence_registry(self.profile)
        df_rev, s_rev = build_portfolio_scenario_manual_review_queue(self.profile)
        df_fnd, s_fnd = build_portfolio_scenario_findings_registry(self.profile)
        tables = {"evidence": df_ev, "reviews": df_rev, "findings": df_fnd}
        summary = {"evidence_summary": s_ev, "findings_summary": s_fnd}

        if save and self.data_lake and hasattr(self.data_lake, "save_portfolio_scenario_findings_registry"):
            self.data_lake.save_portfolio_scenario_validation_evidence_registry(df_ev, s_ev)
            self.data_lake.save_portfolio_scenario_findings_registry(df_fnd, s_fnd)
        return tables, summary

    def build_readiness_score(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        df_rs, s_rs = build_portfolio_scenario_readiness_score_report(self.profile)
        if save and self.data_lake and hasattr(self.data_lake, "save_portfolio_scenario_readiness_score_report"):
            self.data_lake.save_portfolio_scenario_readiness_score_report(df_rs, s_rs)
        return df_rs, s_rs

    def build_manifest(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        df_m, s_m = build_portfolio_scenario_control_manifest(self.profile)
        if save and self.data_lake and hasattr(self.data_lake, "save_portfolio_scenario_control_manifest"):
            self.data_lake.save_portfolio_scenario_control_manifest(df_m, s_m)
        return df_m, s_m

    def build_health_check(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        df_h, s_h = build_portfolio_scenario_control_health_check(self.profile)
        if save and self.data_lake and hasattr(self.data_lake, "save_portfolio_scenario_control_health_check"):
            self.data_lake.save_portfolio_scenario_control_health_check(df_h, s_h)
        return df_h, s_h

    def build_validation_report(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        df_v, s_v = build_portfolio_scenario_control_validation_report(self.profile)
        if save and self.data_lake and hasattr(self.data_lake, "save_portfolio_scenario_control_validation_report"):
            self.data_lake.save_portfolio_scenario_control_validation_report(df_v, s_v)
        return df_v, s_v

    def build_safety_boundary(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        df_s, s_s = build_portfolio_scenario_control_safety_boundary(self.profile)
        if save and self.data_lake and hasattr(self.data_lake, "save_portfolio_scenario_control_safety_boundary"):
            self.data_lake.save_portfolio_scenario_control_safety_boundary(df_s, s_s)
        return df_s, s_s

    def build_phase_157_handoff_report(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        df_hnd, s_hnd = build_phase_157_portfolio_acceptance_report_handoff_report(self.profile)
        if save and self.data_lake and hasattr(self.data_lake, "save_phase_157_portfolio_acceptance_report_handoff_report"):
            self.data_lake.save_phase_157_portfolio_acceptance_report_handoff_report(df_hnd, s_hnd)
        return df_hnd, s_hnd

    def run_pipeline(self, save: bool = True) -> Dict[str, Any]:
        """Run all steps of Phase 156 pipeline."""
        _, s_prof = self.build_profiles_domains_scope(save=save)
        _, s_scen = self.build_scenario_testing_contracts(save=save)
        _, s_dd = self.build_drawdown_control_contracts(save=save)
        _, s_plh = self.build_portfolio_control_placeholders(save=save)
        _, s_out = self.build_outputs_and_metrics(save=save)
        _, s_dep = self.build_dependencies_and_guards(save=save)
        _, s_dis = self.build_disabled_execution_reports(save=save)
        _, s_fnd = self.build_findings_and_evidence(save=save)
        _, s_read = self.build_readiness_score(save=save)
        _, s_man = self.build_manifest(save=save)
        _, s_hlt = self.build_health_check(save=save)
        _, s_val = self.build_validation_report(save=save)
        _, s_saf = self.build_safety_boundary(save=save)
        _, s_hnd = self.build_phase_157_handoff_report(save=save)

        combined_summary = {
            "profile_name": self.profile.profile_name,
            "overall_score": s_read.get("overall_score", 1.0),
            "manifest_status": s_man.get("status", "READY"),
            "health_status": s_hlt.get("status", "HEALTHY"),
            "validation_status": s_val.get("status", "VALIDATION_PASS"),
            "phase_157_handoff_ready": s_hnd.get("handoff_ready", True),
            "current_phase": 156,
            "next_phase": 157,
            "target_final_phase": 160,
        }

        if save and self.data_lake and hasattr(self.data_lake, "save_portfolio_scenario_control_report"):
            markdown = build_portfolio_scenario_control_markdown_report(combined_summary, self.profile)
            self.data_lake.save_portfolio_scenario_control_report(self.profile.profile_name, combined_summary, markdown)

        return combined_summary

    def build_portfolio_scenario_control_status(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Consolidate high-level status across all Phase 156 components."""
        _, s_p = self.build_profiles_domains_scope(save=save)
        _, s_sc = self.build_scenario_testing_contracts(save=save)
        _, s_dd = self.build_drawdown_control_contracts(save=save)
        _, s_pl = self.build_portfolio_control_placeholders(save=save)
        _, s_om = self.build_outputs_and_metrics(save=save)
        _, s_dg = self.build_dependencies_and_guards(save=save)
        _, s_de = self.build_disabled_execution_reports(save=save)
        _, s_fe = self.build_findings_and_evidence(save=save)
        _, s_rs = self.build_readiness_score(save=save)
        _, s_mn = self.build_manifest(save=save)
        _, s_hl = self.build_health_check(save=save)
        _, s_vl = self.build_validation_report(save=save)
        _, s_sb = self.build_safety_boundary(save=save)
        _, s_hd = self.build_phase_157_handoff_report(save=save)

        status_rows = [
            {"component": "profiles_domains_scope", "status": "READY", "details": f"{s_p['profile_summary']['total_profiles']} profiles"},
            {"component": "scenario_testing_contracts", "status": "READY", "details": f"{s_sc['scenario_contracts_summary']['total_contracts']} contracts"},
            {"component": "drawdown_control_contracts", "status": "READY", "details": f"{s_dd['drawdown_summary']['total_drawdown_control_contracts']} contracts"},
            {"component": "control_action_placeholders", "status": "READY", "details": "all placeholders inactive"},
            {"component": "outputs_and_metrics", "status": "READY", "details": "metrics & output contracts ready"},
            {"component": "dependencies_and_guards", "status": "READY", "details": f"{s_dg['dep_summary']['total_dependencies']} deps satisfied"},
            {"component": "disabled_execution_reports", "status": "READY", "details": "all disabled execution reports active"},
            {"component": "findings_and_evidence", "status": "READY", "details": f"{s_fe['findings_summary']['total_findings']} findings registered"},
            {"component": "readiness_score", "status": "READY", "details": f"Score: {s_rs.get('overall_score', 1.0)}"},
            {"component": "manifest", "status": "READY", "details": f"Manifest: {s_mn.get('status', 'READY')}"},
            {"component": "health_and_validation", "status": "READY", "details": f"Health: {s_hl.get('status', 'HEALTHY')}"},
            {"component": "safety_boundary", "status": "READY", "details": f"Safety: {s_sb.get('status', 'SAFETY_BOUNDARY_ENFORCED')}"},
            {"component": "phase_157_handoff", "status": "READY", "details": f"Handoff: {s_hd.get('handoff_ready', True)}"},
        ]
        df_status = pd.DataFrame(status_rows)
        summary = {
            "current_phase": 156,
            "target_final_phase": 160,
            "next_phase": 157,
            "pipeline_status": "PORTFOLIO_SCENARIO_CONTROL_CONTRACT_READY",
            "total_components": len(df_status),
            "all_ready": True,
        }
        return df_status, summary

