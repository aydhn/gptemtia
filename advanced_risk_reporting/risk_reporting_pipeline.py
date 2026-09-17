# -*- coding: utf-8 -*-
"""Phase 155: Master Risk Reporting Pipeline.

Coordinates the local/offline risk reporting, exposure attribution, and limit monitoring contract layer.
Ensures zero live trading, zero broker execution, zero real risk/exposure/limit calculation,
zero alert/dashboard generation, and zero portfolio adjustment.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .risk_reporting_config import (
    RiskReportingProfile,
    get_default_risk_reporting_profile,
    get_risk_reporting_profile,
)
from .risk_reporting_profile_registry import build_risk_reporting_profile_registry
from .risk_reporting_domain_registry import build_risk_reporting_domain_registry
from .risk_reporting_scope_registry import build_risk_reporting_scope_registry
from .risk_report_contracts import build_risk_report_contract_registry
from .exposure_attribution_contracts import build_exposure_attribution_contract_registry
from .limit_monitoring_contracts import build_limit_monitoring_contract_registry
from .portfolio_risk_summary_contracts import build_portfolio_risk_summary_contract_registry
from .portfolio_exposure_summary_contracts import build_portfolio_exposure_summary_contract_registry
from .gross_exposure_placeholders import build_gross_exposure_placeholder_registry
from .net_exposure_placeholders import build_net_exposure_placeholder_registry
from .long_short_exposure_placeholders import build_long_short_exposure_placeholder_registry
from .currency_exposure_placeholders import build_currency_exposure_placeholder_registry
from .cross_asset_exposure_placeholders import build_cross_asset_exposure_placeholder_registry
from .concentration_exposure_placeholders import build_concentration_exposure_placeholder_registry
from .liquidity_exposure_placeholders import build_liquidity_exposure_placeholder_registry
from .leverage_exposure_placeholders import build_leverage_exposure_placeholder_registry
from .margin_exposure_placeholders import build_margin_exposure_placeholder_registry
from .notional_exposure_placeholders import build_notional_exposure_placeholder_registry
from .regime_exposure_placeholders import build_regime_exposure_placeholder_registry
from .strategy_exposure_placeholders import build_strategy_exposure_placeholder_registry
from .asset_exposure_placeholders import build_asset_exposure_placeholder_registry
from .risk_contribution_placeholders import build_risk_contribution_placeholder_registry
from .marginal_risk_contribution_placeholders import build_marginal_risk_contribution_placeholder_registry
from .component_risk_contribution_placeholders import build_component_risk_contribution_placeholder_registry
from .drawdown_monitor_placeholders import build_drawdown_monitor_placeholder_registry
from .volatility_monitor_placeholders import build_volatility_monitor_placeholder_registry
from .var_monitor_placeholders import build_var_monitor_placeholder_registry
from .expected_shortfall_monitor_placeholders import build_expected_shortfall_monitor_placeholder_registry
from .turnover_monitor_placeholders import build_turnover_monitor_placeholder_registry
from .transaction_cost_monitor_placeholders import build_transaction_cost_monitor_placeholder_registry
from .slippage_monitor_placeholders import build_slippage_monitor_placeholder_registry
from .limit_definition_contracts import build_limit_definition_contract_registry
from .exposure_limit_monitoring_contracts import build_exposure_limit_monitoring_contract_registry
from .concentration_limit_monitoring_contracts import build_concentration_limit_monitoring_contract_registry
from .leverage_limit_monitoring_contracts import build_leverage_limit_monitoring_contract_registry
from .margin_limit_monitoring_contracts import build_margin_limit_monitoring_contract_registry
from .liquidity_limit_monitoring_contracts import build_liquidity_limit_monitoring_contract_registry
from .drawdown_limit_monitoring_contracts import build_drawdown_limit_monitoring_contract_registry
from .volatility_limit_monitoring_contracts import build_volatility_limit_monitoring_contract_registry
from .turnover_limit_monitoring_contracts import build_turnover_limit_monitoring_contract_registry
from .risk_budget_limit_monitoring_contracts import build_risk_budget_limit_monitoring_contract_registry
from .limit_breach_placeholders import build_limit_breach_placeholder_registry
from .limit_warning_placeholders import build_limit_warning_placeholder_registry
from .risk_alert_placeholders import build_risk_alert_placeholder_registry
from .alert_routing_disabled import build_alert_routing_disabled_registry
from .dashboard_contract_placeholders import build_dashboard_contract_placeholder_registry
from .monitoring_schedule_placeholders import build_monitoring_schedule_placeholder_registry
from .risk_report_output_contracts import build_risk_report_output_contract_registry
from .exposure_attribution_output_contracts import build_exposure_attribution_output_contract_registry
from .limit_monitoring_output_contracts import build_limit_monitoring_output_contract_registry
from .risk_metric_placeholders import build_risk_metric_placeholder_registry
from .exposure_metric_placeholders import build_exposure_metric_placeholder_registry
from .attribution_metric_placeholders import build_attribution_metric_placeholder_registry
from .limit_monitoring_metric_placeholders import build_limit_monitoring_metric_placeholder_registry
from .risk_reporting_dependencies import build_risk_reporting_dependency_registry
from .risk_reporting_portfolio_construction_dependencies import build_risk_reporting_portfolio_construction_dependency_registry
from .risk_reporting_portfolio_optimization_dependencies import build_risk_reporting_portfolio_optimization_dependency_registry
from .risk_reporting_backtest_acceptance_dependencies import build_risk_reporting_backtest_acceptance_dependency_registry
from .risk_reporting_model_governance_dependencies import build_risk_reporting_model_governance_dependency_registry
from .risk_reporting_regime_dependencies import build_risk_reporting_regime_dependency_registry
from .risk_reporting_featurestore_dependencies import build_risk_reporting_featurestore_dependency_registry
from .risk_reporting_no_lookahead_guards import build_risk_reporting_no_lookahead_guard_registry
from .risk_reporting_exposure_claim_guards import build_risk_reporting_exposure_claim_guard_registry
from .risk_reporting_limit_breach_claim_guards import build_risk_reporting_limit_breach_claim_guard_registry
from .risk_reporting_investment_advice_guards import build_risk_reporting_investment_advice_guard_registry
from .risk_reporting_portfolio_adjustment_guards import build_risk_reporting_portfolio_adjustment_guard_registry
from .risk_reporting_alert_claim_guards import build_risk_reporting_alert_claim_guard_registry
from .risk_reporting_data_snooping_bias_guards import build_risk_reporting_data_snooping_bias_guard_registry
from .risk_reporting_overfitting_guards import build_risk_reporting_overfitting_guard_registry
from .risk_reporting_multiple_testing_guards import build_risk_reporting_multiple_testing_guard_registry
from .risk_reporting_metadata_only_news_guards import build_risk_reporting_metadata_only_news_guard_registry
from .risk_reporting_source_preservation_guards import build_risk_reporting_source_preservation_guard_registry
from .risk_reporting_forbidden_column_policies import build_risk_reporting_forbidden_column_policy_registry
from .risk_report_execution_disabled import build_risk_report_execution_disabled_report
from .exposure_attribution_execution_disabled import build_exposure_attribution_execution_disabled_report
from .limit_monitoring_execution_disabled import build_limit_monitoring_execution_disabled_report
from .risk_metric_calculation_disabled import build_risk_metric_calculation_disabled_report
from .limit_alerting_disabled import build_limit_alerting_disabled_report
from .dashboard_generation_disabled import build_dashboard_generation_disabled_report
from .portfolio_adjustment_disabled import build_portfolio_adjustment_disabled_report
from .risk_reporting_model_training_disabled import build_risk_reporting_model_training_disabled_report
from .risk_reporting_prediction_disabled import build_risk_reporting_prediction_disabled_report
from .risk_reporting_live_trading_disabled import build_risk_reporting_live_trading_disabled_report
from .risk_reporting_broker_execution_disabled import build_risk_reporting_broker_execution_disabled_report
from .risk_reporting_deployment_disabled import build_risk_reporting_deployment_disabled_report
from .risk_reporting_validation_evidence import build_risk_reporting_validation_evidence_registry
from .risk_reporting_manual_review import build_risk_reporting_manual_review_queue
from .risk_reporting_findings import build_risk_reporting_findings_registry
from .risk_reporting_readiness_scoring import (
    calculate_risk_reporting_readiness_score,
    build_risk_reporting_readiness_score_report,
)
from .risk_reporting_manifest import build_risk_reporting_manifest
from .risk_reporting_health import build_risk_reporting_health_check
from .risk_reporting_validation import build_risk_reporting_validation_report
from .risk_reporting_safety_boundary import build_risk_reporting_safety_boundary
from .phase_156_handoff import build_phase_156_portfolio_scenario_testing_drawdown_control_handoff_report


class RiskReportingPipeline:
    """Orchestration pipeline for Phase 155 Risk Reporting contracts."""

    def __init__(
        self,
        data_lake: Optional[object] = None,
        settings: Optional[object] = None,
        project_root: Optional[Path] = None,
        profile: Optional[RiskReportingProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root or Path(__file__).resolve().parents[1]
        self.profile = profile or get_default_risk_reporting_profile()

    def build_profiles_domains_scope(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_p, s_p = build_risk_reporting_profile_registry(self.profile)
        df_d, s_d = build_risk_reporting_domain_registry(self.profile)
        df_s, s_s = build_risk_reporting_scope_registry(self.profile)
        tables = {"profiles": df_p, "domains": df_d, "scopes": df_s}
        summary = {"profile_summary": s_p, "domain_summary": s_d, "scope_summary": s_s}

        if save and self.data_lake and hasattr(self.data_lake, "save_risk_reporting_profile_registry"):
            self.data_lake.save_risk_reporting_profile_registry(df_p, s_p)
            self.data_lake.save_risk_reporting_domain_registry(df_d, s_d)
            self.data_lake.save_risk_reporting_scope_registry(df_s, s_s)
        return tables, summary

    def build_risk_report_contracts(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_rc, s_rc = build_risk_report_contract_registry(self.profile)
        df_rs, s_rs = build_portfolio_risk_summary_contract_registry(self.profile)
        df_es, s_es = build_portfolio_exposure_summary_contract_registry(self.profile)
        tables = {"contracts": df_rc, "risk_summary": df_rs, "exposure_summary": df_es}
        summary = {"contract_summary": s_rc, "risk_summary": s_rs, "exposure_summary": s_es}

        if save and self.data_lake and hasattr(self.data_lake, "save_risk_report_contract_registry"):
            self.data_lake.save_risk_report_contract_registry(df_rc, s_rc)
            self.data_lake.save_portfolio_risk_summary_contract_registry(df_rs, s_rs)
            self.data_lake.save_portfolio_exposure_summary_contract_registry(df_es, s_es)
        return tables, summary

    def build_exposure_attribution_contracts(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_eac, s_eac = build_exposure_attribution_contract_registry(self.profile)
        df_gross, s_gross = build_gross_exposure_placeholder_registry(self.profile)
        df_net, s_net = build_net_exposure_placeholder_registry(self.profile)
        df_ls, s_ls = build_long_short_exposure_placeholder_registry(self.profile)
        df_cur, s_cur = build_currency_exposure_placeholder_registry(self.profile)
        df_ca, s_ca = build_cross_asset_exposure_placeholder_registry(self.profile)
        df_conc, s_conc = build_concentration_exposure_placeholder_registry(self.profile)
        df_liq, s_liq = build_liquidity_exposure_placeholder_registry(self.profile)
        df_lev, s_lev = build_leverage_exposure_placeholder_registry(self.profile)
        df_mar, s_mar = build_margin_exposure_placeholder_registry(self.profile)
        df_not, s_not = build_notional_exposure_placeholder_registry(self.profile)
        df_reg, s_reg = build_regime_exposure_placeholder_registry(self.profile)
        df_strat, s_strat = build_strategy_exposure_placeholder_registry(self.profile)
        df_asset, s_asset = build_asset_exposure_placeholder_registry(self.profile)

        tables = {
            "exposure_contracts": df_eac,
            "gross_exposure": df_gross,
            "net_exposure": df_net,
            "long_short_exposure": df_ls,
            "currency_exposure": df_cur,
            "cross_asset_exposure": df_ca,
            "concentration_exposure": df_conc,
            "liquidity_exposure": df_liq,
            "leverage_exposure": df_lev,
            "margin_exposure": df_mar,
            "notional_exposure": df_not,
            "regime_exposure": df_reg,
            "strategy_exposure": df_strat,
            "asset_exposure": df_asset,
        }
        summary = {"exposure_contract_summary": s_eac, "gross_summary": s_gross, "net_summary": s_net}

        if save and self.data_lake and hasattr(self.data_lake, "save_exposure_attribution_contract_registry"):
            self.data_lake.save_exposure_attribution_contract_registry(df_eac, s_eac)
            self.data_lake.save_gross_exposure_placeholder_registry(df_gross, s_gross)
            self.data_lake.save_net_exposure_placeholder_registry(df_net, s_net)
            self.data_lake.save_currency_exposure_placeholder_registry(df_cur, s_cur)
            self.data_lake.save_cross_asset_exposure_placeholder_registry(df_ca, s_ca)
            self.data_lake.save_concentration_exposure_placeholder_registry(df_conc, s_conc)
            self.data_lake.save_liquidity_exposure_placeholder_registry(df_liq, s_liq)
            self.data_lake.save_leverage_exposure_placeholder_registry(df_lev, s_lev)
            self.data_lake.save_margin_exposure_placeholder_registry(df_mar, s_mar)
        return tables, summary

    def build_limit_monitoring_contracts(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_lmc, s_lmc = build_limit_monitoring_contract_registry(self.profile)
        df_ldef, s_ldef = build_limit_definition_contract_registry(self.profile)
        df_lexp, s_lexp = build_exposure_limit_monitoring_contract_registry(self.profile)
        df_lconc, s_lconc = build_concentration_limit_monitoring_contract_registry(self.profile)
        df_llev, s_llev = build_leverage_limit_monitoring_contract_registry(self.profile)
        df_lmar, s_lmar = build_margin_limit_monitoring_contract_registry(self.profile)
        df_lliq, s_lliq = build_liquidity_limit_monitoring_contract_registry(self.profile)
        df_ldd, s_ldd = build_drawdown_limit_monitoring_contract_registry(self.profile)
        df_lvol, s_lvol = build_volatility_limit_monitoring_contract_registry(self.profile)
        df_lto, s_lto = build_turnover_limit_monitoring_contract_registry(self.profile)
        df_lrb, s_lrb = build_risk_budget_limit_monitoring_contract_registry(self.profile)

        tables = {
            "limit_contracts": df_lmc,
            "limit_definitions": df_ldef,
            "exposure_limits": df_lexp,
            "concentration_limits": df_lconc,
            "leverage_limits": df_llev,
            "margin_limits": df_lmar,
            "liquidity_limits": df_lliq,
            "drawdown_limits": df_ldd,
            "volatility_limits": df_lvol,
            "turnover_limits": df_lto,
            "risk_budget_limits": df_lrb,
        }
        summary = {"limit_contract_summary": s_lmc, "definition_summary": s_ldef}

        if save and self.data_lake and hasattr(self.data_lake, "save_limit_monitoring_contract_registry"):
            self.data_lake.save_limit_monitoring_contract_registry(df_lmc, s_lmc)
            self.data_lake.save_limit_definition_contract_registry(df_ldef, s_ldef)
            self.data_lake.save_exposure_limit_monitoring_contract_registry(df_lexp, s_lexp)
            self.data_lake.save_concentration_limit_monitoring_contract_registry(df_lconc, s_lconc)
            self.data_lake.save_leverage_limit_monitoring_contract_registry(df_llev, s_llev)
            self.data_lake.save_margin_limit_monitoring_contract_registry(df_lmar, s_lmar)
            self.data_lake.save_drawdown_limit_monitoring_contract_registry(df_ldd, s_ldd)
        return tables, summary

    def build_monitor_placeholders(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_rc, s_rc = build_risk_contribution_placeholder_registry(self.profile)
        df_mrc, s_mrc = build_marginal_risk_contribution_placeholder_registry(self.profile)
        df_crc, s_crc = build_component_risk_contribution_placeholder_registry(self.profile)
        df_dd, s_dd = build_drawdown_monitor_placeholder_registry(self.profile)
        df_vol, s_vol = build_volatility_monitor_placeholder_registry(self.profile)
        df_var, s_var = build_var_monitor_placeholder_registry(self.profile)
        df_es, s_es = build_expected_shortfall_monitor_placeholder_registry(self.profile)
        df_to, s_to = build_turnover_monitor_placeholder_registry(self.profile)
        df_cost, s_cost = build_transaction_cost_monitor_placeholder_registry(self.profile)
        df_slip, s_slip = build_slippage_monitor_placeholder_registry(self.profile)
        df_breach, s_breach = build_limit_breach_placeholder_registry(self.profile)
        df_warn, s_warn = build_limit_warning_placeholder_registry(self.profile)
        df_alert, s_alert = build_risk_alert_placeholder_registry(self.profile)
        df_ard, s_ard = build_alert_routing_disabled_registry(self.profile)
        df_dash, s_dash = build_dashboard_contract_placeholder_registry(self.profile)
        df_sched, s_sched = build_monitoring_schedule_placeholder_registry(self.profile)

        tables = {
            "risk_contribution": df_rc,
            "marginal_risk": df_mrc,
            "component_risk": df_crc,
            "drawdown_monitor": df_dd,
            "volatility_monitor": df_vol,
            "var_monitor": df_var,
            "expected_shortfall_monitor": df_es,
            "turnover_monitor": df_to,
            "transaction_cost_monitor": df_cost,
            "slippage_monitor": df_slip,
            "limit_breach": df_breach,
            "limit_warning": df_warn,
            "risk_alert": df_alert,
            "alert_routing_disabled": df_ard,
            "dashboard_placeholders": df_dash,
            "monitoring_schedule": df_sched,
        }
        summary = {"risk_contribution": s_rc, "drawdown": s_dd, "var": s_var, "expected_shortfall": s_es}

        if save and self.data_lake and hasattr(self.data_lake, "save_risk_contribution_placeholder_registry"):
            self.data_lake.save_risk_contribution_placeholder_registry(df_rc, s_rc)
            self.data_lake.save_drawdown_monitor_placeholder_registry(df_dd, s_dd)
            self.data_lake.save_var_monitor_placeholder_registry(df_var, s_var)
            self.data_lake.save_expected_shortfall_monitor_placeholder_registry(df_es, s_es)
            self.data_lake.save_limit_breach_placeholder_registry(df_breach, s_breach)
            self.data_lake.save_risk_alert_placeholder_registry(df_alert, s_alert)
            self.data_lake.save_alert_routing_disabled_registry(df_ard, s_ard)
            self.data_lake.save_dashboard_contract_placeholder_registry(df_dash, s_dash)
        return tables, summary

    def build_outputs_metrics(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_roc, s_roc = build_risk_report_output_contract_registry(self.profile)
        df_eoc, s_eoc = build_exposure_attribution_output_contract_registry(self.profile)
        df_loc, s_loc = build_limit_monitoring_output_contract_registry(self.profile)
        df_rm, s_rm = build_risk_metric_placeholder_registry(self.profile)
        df_em, s_em = build_exposure_metric_placeholder_registry(self.profile)
        df_am, s_am = build_attribution_metric_placeholder_registry(self.profile)
        df_lm, s_lm = build_limit_monitoring_metric_placeholder_registry(self.profile)

        tables = {
            "risk_output_contracts": df_roc,
            "exposure_output_contracts": df_eoc,
            "limit_output_contracts": df_loc,
            "risk_metrics": df_rm,
            "exposure_metrics": df_em,
            "attribution_metrics": df_am,
            "limit_metrics": df_lm,
        }
        summary = {"risk_output": s_roc, "exposure_output": s_eoc, "limit_output": s_loc}

        if save and self.data_lake and hasattr(self.data_lake, "save_risk_report_output_contract_registry"):
            self.data_lake.save_risk_report_output_contract_registry(df_roc, s_roc)
            self.data_lake.save_exposure_attribution_output_contract_registry(df_eoc, s_eoc)
            self.data_lake.save_limit_monitoring_output_contract_registry(df_loc, s_loc)
            self.data_lake.save_risk_metric_placeholder_registry(df_rm, s_rm)
            self.data_lake.save_exposure_metric_placeholder_registry(df_em, s_em)
            self.data_lake.save_attribution_metric_placeholder_registry(df_am, s_am)
            self.data_lake.save_limit_monitoring_metric_placeholder_registry(df_lm, s_lm)
        return tables, summary

    def build_dependencies_guards(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_dep, s_dep = build_risk_reporting_dependency_registry(self.profile)
        df_pcdep, s_pcdep = build_risk_reporting_portfolio_construction_dependency_registry(self.profile)
        df_podep, s_podep = build_risk_reporting_portfolio_optimization_dependency_registry(self.profile)
        df_badep, s_badep = build_risk_reporting_backtest_acceptance_dependency_registry(self.profile)
        df_mgdep, s_mgdep = build_risk_reporting_model_governance_dependency_registry(self.profile)
        df_regdep, s_regdep = build_risk_reporting_regime_dependency_registry(self.profile)
        df_fsdep, s_fsdep = build_risk_reporting_featurestore_dependency_registry(self.profile)

        df_nlg, s_nlg = build_risk_reporting_no_lookahead_guard_registry(self.profile)
        df_ecg, s_ecg = build_risk_reporting_exposure_claim_guard_registry(self.profile)
        df_lbg, s_lbg = build_risk_reporting_limit_breach_claim_guard_registry(self.profile)
        df_iag, s_iag = build_risk_reporting_investment_advice_guard_registry(self.profile)
        df_pag, s_pag = build_risk_reporting_portfolio_adjustment_guard_registry(self.profile)
        df_acg, s_acg = build_risk_reporting_alert_claim_guard_registry(self.profile)
        df_dsg, s_dsg = build_risk_reporting_data_snooping_bias_guard_registry(self.profile)
        df_ofg, s_ofg = build_risk_reporting_overfitting_guard_registry(self.profile)
        df_mtg, s_mtg = build_risk_reporting_multiple_testing_guard_registry(self.profile)
        df_nws, s_nws = build_risk_reporting_metadata_only_news_guard_registry(self.profile)
        df_src, s_src = build_risk_reporting_source_preservation_guard_registry(self.profile)
        df_fc, s_fc = build_risk_reporting_forbidden_column_policy_registry(self.profile)
        df_evd, s_evd = build_risk_reporting_validation_evidence_registry(self.profile)

        tables = {
            "dependencies": df_dep,
            "portfolio_construction_dependencies": df_pcdep,
            "portfolio_optimization_dependencies": df_podep,
            "backtest_acceptance_dependencies": df_badep,
            "model_governance_dependencies": df_mgdep,
            "regime_dependencies": df_regdep,
            "featurestore_dependencies": df_fsdep,
            "no_lookahead_guards": df_nlg,
            "exposure_claim_guards": df_ecg,
            "limit_breach_claim_guards": df_lbg,
            "investment_advice_guards": df_iag,
            "portfolio_adjustment_guards": df_pag,
            "alert_claim_guards": df_acg,
            "data_snooping_guards": df_dsg,
            "overfitting_guards": df_ofg,
            "multiple_testing_guards": df_mtg,
            "news_guards": df_nws,
            "source_preservation_guards": df_src,
            "forbidden_columns": df_fc,
            "evidence": df_evd,
        }
        summary = {"dependency_summary": s_dep, "guard_summary": s_nlg, "evidence_summary": s_evd}

        if save and self.data_lake and hasattr(self.data_lake, "save_risk_reporting_exposure_claim_guard_registry"):
            self.data_lake.save_risk_reporting_exposure_claim_guard_registry(df_ecg, s_ecg)
            self.data_lake.save_risk_reporting_limit_breach_claim_guard_registry(df_lbg, s_lbg)
            self.data_lake.save_risk_reporting_investment_advice_guard_registry(df_iag, s_iag)
            self.data_lake.save_risk_reporting_portfolio_adjustment_guard_registry(df_pag, s_pag)
            self.data_lake.save_risk_reporting_forbidden_column_policy_registry(df_fc, s_fc)
            self.data_lake.save_risk_reporting_validation_evidence_registry(df_evd, s_evd)
        return tables, summary

    def build_disabled_execution_reports(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_rre, s_rre = build_risk_report_execution_disabled_report(self.profile)
        df_eae, s_eae = build_exposure_attribution_execution_disabled_report(self.profile)
        df_lme, s_lme = build_limit_monitoring_execution_disabled_report(self.profile)
        df_rmc, s_rmc = build_risk_metric_calculation_disabled_report(self.profile)
        df_la, s_la = build_limit_alerting_disabled_report(self.profile)
        df_dg, s_dg = build_dashboard_generation_disabled_report(self.profile)
        df_pa, s_pa = build_portfolio_adjustment_disabled_report(self.profile)
        df_mt, s_mt = build_risk_reporting_model_training_disabled_report(self.profile)
        df_pred, s_pred = build_risk_reporting_prediction_disabled_report(self.profile)
        df_lt, s_lt = build_risk_reporting_live_trading_disabled_report(self.profile)
        df_be, s_be = build_risk_reporting_broker_execution_disabled_report(self.profile)
        df_dep, s_dep = build_risk_reporting_deployment_disabled_report(self.profile)

        tables = {
            "risk_report_execution_disabled": df_rre,
            "exposure_attribution_execution_disabled": df_eae,
            "limit_monitoring_execution_disabled": df_lme,
            "risk_metric_calculation_disabled": df_rmc,
            "limit_alerting_disabled": df_la,
            "dashboard_generation_disabled": df_dg,
            "portfolio_adjustment_disabled": df_pa,
            "model_training_disabled": df_mt,
            "prediction_disabled": df_pred,
            "live_trading_disabled": df_lt,
            "broker_execution_disabled": df_be,
            "deployment_disabled": df_dep,
        }
        summary = {"risk_report": s_rre, "exposure": s_eae, "limit": s_lme, "alerting": s_la}

        if save and self.data_lake and hasattr(self.data_lake, "save_risk_report_execution_disabled_report"):
            self.data_lake.save_risk_report_execution_disabled_report(df_rre, s_rre)
            self.data_lake.save_exposure_attribution_execution_disabled_report(df_eae, s_eae)
            self.data_lake.save_limit_monitoring_execution_disabled_report(df_lme, s_lme)
            self.data_lake.save_risk_metric_calculation_disabled_report(df_rmc, s_rmc)
            self.data_lake.save_limit_alerting_disabled_report(df_la, s_la)
            self.data_lake.save_dashboard_generation_disabled_report(df_dg, s_dg)
            self.data_lake.save_portfolio_adjustment_disabled_report(df_pa, s_pa)
            self.data_lake.save_risk_reporting_live_trading_disabled_report(df_lt, s_lt)
            self.data_lake.save_risk_reporting_broker_execution_disabled_report(df_be, s_be)
        return tables, summary

    def build_findings_scoring_manifest(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_fnd, s_fnd = build_risk_reporting_findings_registry(self.profile)
        df_mrq, s_mrq = build_risk_reporting_manual_review_queue(self.profile)
        df_score, s_score = build_risk_reporting_readiness_score_report(self.profile)
        df_mnf, s_mnf = build_risk_reporting_manifest(self.profile)

        tables = {"findings": df_fnd, "manual_review": df_mrq, "scoring": df_score, "manifest": df_mnf}
        summary = {"findings": s_fnd, "scoring": s_score, "manifest": s_mnf}

        if save and self.data_lake and hasattr(self.data_lake, "save_risk_reporting_findings_registry"):
            self.data_lake.save_risk_reporting_findings_registry(df_fnd, s_fnd)
            self.data_lake.save_risk_reporting_readiness_score_report(df_score, s_score)
            self.data_lake.save_risk_reporting_manifest(df_mnf, s_mnf)
        return tables, summary

    def build_health_validation_safety_handoff(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        df_hlth, s_hlth = build_risk_reporting_health_check(self.project_root, self.profile)
        profiles_df, _ = build_risk_reporting_profile_registry(self.profile)
        contracts_df, _ = build_risk_report_contract_registry(self.profile)
        exposure_df, _ = build_exposure_attribution_contract_registry(self.profile)
        limits_df, _ = build_limit_monitoring_contract_registry(self.profile)
        manifest_df, _ = build_risk_reporting_manifest(self.profile)

        val_tables = {
            "profiles": profiles_df,
            "contracts": contracts_df,
            "exposure_contracts": exposure_df,
            "limit_contracts": limits_df,
            "manifest": manifest_df,
        }
        df_val, s_val = build_risk_reporting_validation_report(val_tables, self.profile)
        df_safe, s_safe = build_risk_reporting_safety_boundary(self.profile)
        df_hnd, s_hnd = build_phase_156_portfolio_scenario_testing_drawdown_control_handoff_report(self.profile)

        tables = {"health": df_hlth, "validation": df_val, "safety": df_safe, "handoff": df_hnd}
        summary = {"health": s_hlth, "validation": s_val, "safety": s_safe, "handoff": s_hnd}

        if save and self.data_lake and hasattr(self.data_lake, "save_risk_reporting_health_check"):
            self.data_lake.save_risk_reporting_health_check(df_hlth, s_hlth)
            self.data_lake.save_risk_reporting_validation_report(df_val, s_val)
            self.data_lake.save_risk_reporting_safety_boundary(df_safe, s_safe)
            self.data_lake.save_phase_156_portfolio_scenario_testing_drawdown_control_handoff_report(df_hnd, s_hnd)
        return tables, summary

    def build_risk_reporting_status(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Consolidate high-level status across all Phase 155 components."""
        _, s_p = self.build_profiles_domains_scope(save=save)
        _, s_rc = self.build_risk_report_contracts(save=save)
        _, s_eac = self.build_exposure_attribution_contracts(save=save)
        _, s_lmc = self.build_limit_monitoring_contracts(save=save)
        _, s_m = self.build_monitor_placeholders(save=save)
        _, s_om = self.build_outputs_metrics(save=save)
        _, s_dg = self.build_dependencies_guards(save=save)
        _, s_de = self.build_disabled_execution_reports(save=save)
        _, s_fsm = self.build_findings_scoring_manifest(save=save)
        _, s_hvsh = self.build_health_validation_safety_handoff(save=save)

        status_rows = [
            {"component": "profiles_domains_scope", "status": "READY", "details": f"{s_p['profile_summary']['profile_count']} profiles"},
            {"component": "risk_report_contracts", "status": "READY", "details": f"{s_rc['contract_summary']['contract_count']} contracts"},
            {"component": "exposure_attribution_contracts", "status": "READY", "details": f"{s_eac['exposure_contract_summary']['contract_count']} contracts"},
            {"component": "limit_monitoring_contracts", "status": "READY", "details": f"{s_lmc['limit_contract_summary']['contract_count']} contracts"},
            {"component": "monitor_placeholders", "status": "READY", "details": "all placeholders active"},
            {"component": "outputs_metrics", "status": "READY", "details": "metrics & output contracts ready"},
            {"component": "dependencies_guards", "status": "READY", "details": f"{s_dg['dependency_summary']['dependency_count']} deps satisfied"},
            {"component": "disabled_execution_reports", "status": "READY", "details": "12 disabled execution reports active"},
            {"component": "findings_scoring_manifest", "status": "READY", "details": f"Score: {s_fsm['scoring']['readiness_score']}"},
            {"component": "health_validation_safety_handoff", "status": "READY", "details": f"Handoff: {s_hvsh['handoff']['handoff_ready']}"},
        ]
        df_status = pd.DataFrame(status_rows)
        summary = {
            "current_phase": 155,
            "target_final_phase": 160,
            "next_phase": 156,
            "pipeline_status": "RISK_REPORTING_CONTRACT_READY",
            "total_components": len(df_status),
            "all_ready": True,
        }
        return df_status, summary
