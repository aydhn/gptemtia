# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Pipeline.

Coordinates generation of all Phase 153 contract registries, position sizing placeholders,
risk budgeting placeholders, limit contracts, guards, disabled execution reports, findings,
readiness scores, manifests, health checks, validation reports, and Phase 154 handoff documents.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake

from .portfolio_construction_config import (
    PortfolioConstructionProfile,
    get_default_portfolio_construction_profile,
)
from .portfolio_construction_profile_registry import (
    build_portfolio_construction_profile_registry,
)
from .portfolio_construction_domain_registry import (
    build_portfolio_construction_domain_registry,
)
from .portfolio_construction_scope_registry import (
    build_portfolio_construction_scope_registry,
)
from .portfolio_validation_evidence import (
    build_portfolio_validation_evidence_registry,
)
from .portfolio_dependencies import (
    build_portfolio_dependency_registry,
)
from .portfolio_construction_contracts import (
    build_portfolio_construction_contract_registry,
)
from .portfolio_universe_contracts import (
    build_portfolio_universe_contract_registry,
)
from .portfolio_asset_eligibility_contracts import (
    build_portfolio_asset_eligibility_contract_registry,
)
from .portfolio_signal_input_contracts import (
    build_portfolio_signal_input_contract_registry,
)
from .portfolio_risk_input_contracts import (
    build_portfolio_risk_input_contract_registry,
)
from .position_sizing_contracts import (
    build_position_sizing_contract_registry,
)
from .fixed_fractional_sizing_placeholders import (
    build_fixed_fractional_sizing_placeholder_registry,
)
from .volatility_targeting_sizing_placeholders import (
    build_volatility_targeting_sizing_placeholder_registry,
)
from .risk_parity_sizing_placeholders import (
    build_risk_parity_sizing_placeholder_registry,
)
from .drawdown_aware_sizing_placeholders import (
    build_drawdown_aware_sizing_placeholder_registry,
)
from .confidence_aware_sizing_placeholders import (
    build_confidence_aware_sizing_placeholder_registry,
)
from .regime_aware_sizing_placeholders import (
    build_regime_aware_sizing_placeholder_registry,
)
from .correlation_aware_sizing_placeholders import (
    build_correlation_aware_sizing_placeholder_registry,
)
from .liquidity_aware_sizing_placeholders import (
    build_liquidity_aware_sizing_placeholder_registry,
)
from .transaction_cost_aware_sizing_placeholders import (
    build_transaction_cost_aware_sizing_placeholder_registry,
)
from .slippage_aware_sizing_placeholders import (
    build_slippage_aware_sizing_placeholder_registry,
)
from .risk_budget_contracts import (
    build_risk_budget_contract_registry,
)
from .per_asset_risk_budget_placeholders import (
    build_per_asset_risk_budget_placeholder_registry,
)
from .per_strategy_risk_budget_placeholders import (
    build_per_strategy_risk_budget_placeholder_registry,
)
from .per_regime_risk_budget_placeholders import (
    build_per_regime_risk_budget_placeholder_registry,
)
from .portfolio_risk_budget_placeholders import (
    build_portfolio_risk_budget_placeholder_registry,
)
from .drawdown_budget_placeholders import (
    build_drawdown_budget_placeholder_registry,
)
from .volatility_budget_placeholders import (
    build_volatility_budget_placeholder_registry,
)
from .exposure_budget_placeholders import (
    build_exposure_budget_placeholder_registry,
)
from .concentration_limit_contracts import (
    build_concentration_limit_contract_registry,
)
from .exposure_limit_contracts import (
    build_exposure_limit_contract_registry,
)
from .leverage_limit_placeholders import (
    build_leverage_limit_placeholder_registry,
)
from .margin_limit_placeholders import (
    build_margin_limit_placeholder_registry,
)
from .notional_limit_placeholders import (
    build_notional_limit_placeholder_registry,
)
from .currency_exposure_limit_placeholders import (
    build_currency_exposure_limit_placeholder_registry,
)
from .cross_asset_exposure_limit_placeholders import (
    build_cross_asset_exposure_limit_placeholder_registry,
)
from .sector_group_exposure_placeholders import (
    build_sector_group_exposure_placeholder_registry,
)
from .correlation_limit_placeholders import (
    build_correlation_limit_placeholder_registry,
)
from .liquidity_limit_placeholders import (
    build_liquidity_limit_placeholder_registry,
)
from .portfolio_output_contracts import (
    build_portfolio_output_contract_registry,
)
from .position_sizing_output_contracts import (
    build_position_sizing_output_contract_registry,
)
from .risk_budget_output_contracts import (
    build_risk_budget_output_contract_registry,
)
from .portfolio_metric_placeholders import (
    build_portfolio_metric_placeholder_registry,
)
from .sizing_metric_placeholders import (
    build_sizing_metric_placeholder_registry,
)
from .risk_budget_metric_placeholders import (
    build_risk_budget_metric_placeholder_registry,
)
from .exposure_metric_placeholders import (
    build_exposure_metric_placeholder_registry,
)
from .concentration_metric_placeholders import (
    build_concentration_metric_placeholder_registry,
)
from .portfolio_no_lookahead_guards import (
    build_portfolio_no_lookahead_guard_registry,
)
from .portfolio_allocation_claim_guards import (
    build_portfolio_allocation_claim_guard_registry,
)
from .portfolio_position_sizing_claim_guards import (
    build_portfolio_position_sizing_claim_guard_registry,
)
from .portfolio_investment_advice_guards import (
    build_portfolio_investment_advice_guard_registry,
)
from .portfolio_risk_limit_claim_guards import (
    build_portfolio_risk_limit_claim_guard_registry,
)
from .portfolio_data_snooping_bias_guards import (
    build_portfolio_data_snooping_bias_guard_registry,
)
from .portfolio_overfitting_guards import (
    build_portfolio_overfitting_guard_registry,
)
from .portfolio_multiple_testing_guards import (
    build_portfolio_multiple_testing_guard_registry,
)
from .portfolio_metadata_only_news_guards import (
    build_portfolio_metadata_only_news_guard_registry,
)
from .portfolio_source_preservation_guards import (
    build_portfolio_source_preservation_guard_registry,
)
from .portfolio_forbidden_column_policies import (
    build_portfolio_forbidden_column_policy_registry,
)
from .portfolio_construction_execution_disabled import (
    build_portfolio_construction_execution_disabled_report,
)
from .position_sizing_execution_disabled import (
    build_position_sizing_execution_disabled_report,
)
from .risk_budget_execution_disabled import (
    build_risk_budget_execution_disabled_report,
)
from .allocation_generation_disabled import (
    build_allocation_generation_disabled_report,
)
from .portfolio_optimizer_disabled import (
    build_portfolio_optimizer_disabled_report,
)
from .portfolio_metric_calculation_disabled import (
    build_portfolio_metric_calculation_disabled_report,
)
from .portfolio_model_training_disabled import (
    build_portfolio_model_training_disabled_report,
)
from .portfolio_prediction_disabled import (
    build_portfolio_prediction_disabled_report,
)
from .portfolio_live_trading_disabled import (
    build_portfolio_live_trading_disabled_report,
)
from .portfolio_broker_execution_disabled import (
    build_portfolio_broker_execution_disabled_report,
)
from .portfolio_deployment_disabled import (
    build_portfolio_deployment_disabled_report,
)
from .portfolio_manual_review import (
    build_portfolio_manual_review_gate_registry,
)
from .portfolio_findings import (
    build_portfolio_findings_registry,
)
from .portfolio_readiness_scoring import (
    build_portfolio_readiness_score_report,
)
from .portfolio_construction_manifest import (
    build_portfolio_construction_manifest,
)
from .portfolio_construction_safety_boundary import (
    build_portfolio_construction_safety_boundary_report,
)
from .portfolio_construction_health import (
    build_portfolio_construction_health_check,
)
from .portfolio_construction_validation import (
    validate_portfolio_construction_invariants,
)
from .phase_154_handoff import (
    build_phase_154_handoff_report,
)


class PortfolioConstructionPipeline:
    """End-to-end pipeline orchestrator for Phase 153 Portfolio Construction Contract block."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[PortfolioConstructionProfile] = None,
    ):
        self.data_lake = data_lake or DataLake()
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(".")
        self.profile = profile or get_default_portfolio_construction_profile()

    def build_profiles_domains_scope(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build profile, domain, and scope registries."""
        df_prof, s_prof = build_portfolio_construction_profile_registry(self.profile)
        df_dom, s_dom = build_portfolio_construction_domain_registry(self.profile)
        df_scp, s_scp = build_portfolio_construction_scope_registry(self.profile)

        if save and hasattr(self.data_lake, "save_portfolio_construction_profile_registry"):
            self.data_lake.save_portfolio_construction_profile_registry(df_prof, s_prof)

        dfs = {"profiles": df_prof, "domains": df_dom, "scope": df_scp}
        summary = {"profiles": s_prof, "domains": s_dom, "scope": s_scp, "non_signal": True}
        return dfs, summary

    def build_portfolio_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build portfolio construction contracts (universe, eligibility, signals, risks)."""
        df_con, s_con = build_portfolio_construction_contract_registry(self.profile)
        df_uni, s_uni = build_portfolio_universe_contract_registry(self.profile)
        df_eli, s_eli = build_portfolio_asset_eligibility_contract_registry(self.profile)
        df_sig, s_sig = build_portfolio_signal_input_contract_registry(self.profile)
        df_rsk, s_rsk = build_portfolio_risk_input_contract_registry(self.profile)

        if save and hasattr(self.data_lake, "save_portfolio_construction_contract_registry"):
            self.data_lake.save_portfolio_construction_contract_registry(df_con, s_con)
            self.data_lake.save_portfolio_universe_contract_registry(df_uni, s_uni)
            self.data_lake.save_portfolio_asset_eligibility_contract_registry(df_eli, s_eli)
            self.data_lake.save_portfolio_signal_input_contract_registry(df_sig, s_sig)
            self.data_lake.save_portfolio_risk_input_contract_registry(df_rsk, s_rsk)

        dfs = {
            "contracts": df_con,
            "universe": df_uni,
            "eligibility": df_eli,
            "signals": df_sig,
            "risks": df_rsk,
        }
        summary = {
            "contracts": s_con,
            "universe": s_uni,
            "eligibility": s_eli,
            "signals": s_sig,
            "risks": s_rsk,
            "non_signal": True,
        }
        return dfs, summary

    def build_position_sizing_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build position sizing contracts and placeholders."""
        df_sz, s_sz = build_position_sizing_contract_registry(self.profile)
        df_ff, s_ff = build_fixed_fractional_sizing_placeholder_registry(self.profile)
        df_vt, s_vt = build_volatility_targeting_sizing_placeholder_registry(self.profile)
        df_rp, s_rp = build_risk_parity_sizing_placeholder_registry(self.profile)
        df_dd, s_dd = build_drawdown_aware_sizing_placeholder_registry(self.profile)

        if save and hasattr(self.data_lake, "save_position_sizing_contract_registry"):
            self.data_lake.save_position_sizing_contract_registry(df_sz, s_sz)

        dfs = {
            "sizing_contracts": df_sz,
            "fixed_fractional": df_ff,
            "volatility_targeting": df_vt,
            "risk_parity": df_rp,
            "drawdown_aware": df_dd,
        }
        summary = {"sizing": s_sz, "non_signal": True}
        return dfs, summary

    def build_risk_budget_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build risk budget contracts and placeholders."""
        df_rb, s_rb = build_risk_budget_contract_registry(self.profile)
        df_ast, s_ast = build_per_asset_risk_budget_placeholder_registry(self.profile)
        df_str, s_str = build_per_strategy_risk_budget_placeholder_registry(self.profile)
        df_reg, s_reg = build_per_regime_risk_budget_placeholder_registry(self.profile)
        df_prt, s_prt = build_portfolio_risk_budget_placeholder_registry(self.profile)

        if save and hasattr(self.data_lake, "save_risk_budget_contract_registry"):
            self.data_lake.save_risk_budget_contract_registry(df_rb, s_rb)

        dfs = {
            "risk_budget_contracts": df_rb,
            "per_asset": df_ast,
            "per_strategy": df_str,
            "per_regime": df_reg,
            "portfolio": df_prt,
        }
        summary = {"risk_budget": s_rb, "non_signal": True}
        return dfs, summary

    def build_limits_placeholders(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build exposure, concentration, leverage, and margin limit contracts."""
        df_conc, s_conc = build_concentration_limit_contract_registry(self.profile)
        df_exp, s_exp = build_exposure_limit_contract_registry(self.profile)
        df_lev, s_lev = build_leverage_limit_placeholder_registry(self.profile)
        df_mrg, s_mrg = build_margin_limit_placeholder_registry(self.profile)
        df_not, s_not = build_notional_limit_placeholder_registry(self.profile)

        if save and hasattr(self.data_lake, "save_concentration_limit_contract_registry"):
            self.data_lake.save_concentration_limit_contract_registry(df_conc, s_conc)
            self.data_lake.save_exposure_limit_contract_registry(df_exp, s_exp)

        dfs = {
            "concentration": df_conc,
            "exposure": df_exp,
            "leverage": df_lev,
            "margin": df_mrg,
            "notional": df_not,
        }
        summary = {"concentration": s_conc, "exposure": s_exp, "non_signal": True}
        return dfs, summary

    def build_dependencies_guards(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build dependency evidence and safety guards."""
        df_dep, s_dep = build_portfolio_dependency_registry(self.profile)
        df_evi, s_evi = build_portfolio_validation_evidence_registry(self.profile)
        df_look, s_look = build_portfolio_no_lookahead_guard_registry(self.profile)
        df_alc, s_alc = build_portfolio_allocation_claim_guard_registry(self.profile)
        df_adv, s_adv = build_portfolio_investment_advice_guard_registry(self.profile)

        dfs = {
            "dependencies": df_dep,
            "evidence": df_evi,
            "lookahead_guard": df_look,
            "allocation_guard": df_alc,
            "advice_guard": df_adv,
        }
        summary = {"dependencies": s_dep, "non_signal": True}
        return dfs, summary

    def build_disabled_execution_reports(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build disabled execution reports certifying non-production status."""
        df_pc, s_pc = build_portfolio_construction_execution_disabled_report(self.profile)
        df_sz, s_sz = build_position_sizing_execution_disabled_report(self.profile)
        df_rb, s_rb = build_risk_budget_execution_disabled_report(self.profile)
        df_al, s_al = build_allocation_generation_disabled_report(self.profile)
        df_opt, s_opt = build_portfolio_optimizer_disabled_report(self.profile)
        df_met, s_met = build_portfolio_metric_calculation_disabled_report(self.profile)
        df_trn, s_trn = build_portfolio_model_training_disabled_report(self.profile)
        df_prd, s_prd = build_portfolio_prediction_disabled_report(self.profile)
        df_liv, s_liv = build_portfolio_live_trading_disabled_report(self.profile)
        df_brk, s_brk = build_portfolio_broker_execution_disabled_report(self.profile)
        df_dep, s_dep = build_portfolio_deployment_disabled_report(self.profile)

        dfs = {
            "disabled_pc": df_pc,
            "disabled_sz": df_sz,
            "disabled_rb": df_rb,
            "disabled_al": df_al,
            "disabled_opt": df_opt,
            "disabled_met": df_met,
            "disabled_trn": df_trn,
            "disabled_prd": df_prd,
            "disabled_liv": df_liv,
            "disabled_brk": df_brk,
            "disabled_dep": df_dep,
        }
        summary = {"total_disabled": len(dfs), "all_disabled": True, "non_signal": True}
        return dfs, summary

    def build_findings_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build findings, readiness score, and master manifest."""
        df_fnd, s_fnd = build_portfolio_findings_registry(self.profile)
        df_sco, s_sco = build_portfolio_readiness_score_report(findings_df=df_fnd, profile=self.profile)
        df_mnf, s_mnf = build_portfolio_construction_manifest(self.profile)

        if save and hasattr(self.data_lake, "save_portfolio_findings_registry"):
            self.data_lake.save_portfolio_findings_registry(df_fnd, s_fnd)
            self.data_lake.save_portfolio_readiness_score_report(df_sco, s_sco)
            self.data_lake.save_portfolio_construction_manifest(df_mnf, s_mnf)

        dfs = {"findings": df_fnd, "readiness_score": df_sco, "manifest": df_mnf}
        summary = {"findings": s_fnd, "readiness": s_sco, "manifest": s_mnf, "non_signal": True}
        return dfs, summary

    def build_health_check(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Build health check report."""
        df_hlth, s_hlth = build_portfolio_construction_health_check(
            project_root=self.project_root, profile=self.profile
        )
        if save and hasattr(self.data_lake, "save_portfolio_construction_health_check"):
            self.data_lake.save_portfolio_construction_health_check(df_hlth, s_hlth)
        return df_hlth, s_hlth

    def build_validation_report(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Build validation report."""
        df_val, s_val = validate_portfolio_construction_invariants(self.profile)
        if save and hasattr(self.data_lake, "save_portfolio_construction_validation_report"):
            self.data_lake.save_portfolio_construction_validation_report(df_val, s_val)
        return df_val, s_val

    def build_portfolio_construction_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Build consolidated status across all Phase 153 outputs."""
        df_fnd, _ = build_portfolio_findings_registry(self.profile)
        df_sco, s_sco = build_portfolio_readiness_score_report(findings_df=df_fnd, profile=self.profile)
        df_mnf, s_mnf = build_portfolio_construction_manifest(self.profile)
        df_hnd, s_hnd = build_phase_154_handoff_report(self.profile)

        records = [{
            "profile_name": self.profile.profile_name,
            "current_phase": self.profile.current_phase,
            "next_phase": self.profile.next_phase,
            "target_final_phase": self.profile.target_final_phase,
            "readiness_score": s_sco["overall_score"],
            "classification": s_sco["classification"],
            "meets_threshold": s_sco["meets_threshold"],
            "phase_154_handoff_ready": s_mnf["phase_154_handoff_ready"],
            "status": "PORTFOLIO_CONTRACT_READY",
            "non_signal": True,
        }]
        df = pd.DataFrame(records)
        summary = {
            "active_profile": self.profile.profile_name,
            "current_phase": self.profile.current_phase,
            "next_phase": self.profile.next_phase,
            "target_final_phase": self.profile.target_final_phase,
            "readiness_score": s_sco["overall_score"],
            "classification": s_sco["classification"],
            "status": "PORTFOLIO_CONTRACT_READY",
            "non_signal": True,
        }
        return df, summary

    def run_all(self, save: bool = True) -> Dict[str, Any]:
        """Execute the entire portfolio construction contract pipeline."""
        return run_portfolio_construction_pipeline(
            profile=self.profile, save_artifacts=save, data_lake=self.data_lake
        )


def run_portfolio_construction_pipeline(
    profile: Optional[PortfolioConstructionProfile] = None,
    save_artifacts: bool = True,
    data_lake: Optional[DataLake] = None,
) -> Dict[str, Any]:
    """Execute complete Phase 153 contract registry pipeline."""
    active = profile or get_default_portfolio_construction_profile()
    lake = data_lake or DataLake()

    results: Dict[str, Any] = {}

    # Core Registries
    profiles_df, profiles_sum = build_portfolio_construction_profile_registry(active)
    domains_df, domains_sum = build_portfolio_construction_domain_registry(active)
    scopes_df, scopes_sum = build_portfolio_construction_scope_registry(active)
    evidence_df, evidence_sum = build_portfolio_validation_evidence_registry(active)
    dependencies_df, dependencies_sum = build_portfolio_dependency_registry(active)

    # Portfolio Contracts
    contracts_df, contracts_sum = build_portfolio_construction_contract_registry(active)
    universe_df, universe_sum = build_portfolio_universe_contract_registry(active)
    eligibility_df, eligibility_sum = build_portfolio_asset_eligibility_contract_registry(active)
    signals_df, signals_sum = build_portfolio_signal_input_contract_registry(active)
    risks_df, risks_sum = build_portfolio_risk_input_contract_registry(active)

    # Sizing Contracts & Placeholders
    sizing_df, sizing_sum = build_position_sizing_contract_registry(active)
    fixed_frac_df, fixed_frac_sum = build_fixed_fractional_sizing_placeholder_registry(active)
    vol_target_df, vol_target_sum = build_volatility_targeting_sizing_placeholder_registry(active)
    risk_parity_df, risk_parity_sum = build_risk_parity_sizing_placeholder_registry(active)
    drawdown_aware_df, drawdown_aware_sum = build_drawdown_aware_sizing_placeholder_registry(active)
    confidence_aware_df, confidence_aware_sum = build_confidence_aware_sizing_placeholder_registry(active)
    regime_aware_df, regime_aware_sum = build_regime_aware_sizing_placeholder_registry(active)
    corr_aware_df, corr_aware_sum = build_correlation_aware_sizing_placeholder_registry(active)
    liq_aware_df, liq_aware_sum = build_liquidity_aware_sizing_placeholder_registry(active)
    cost_aware_df, cost_aware_sum = build_transaction_cost_aware_sizing_placeholder_registry(active)
    slip_aware_df, slip_aware_sum = build_slippage_aware_sizing_placeholder_registry(active)

    # Risk Budget Contracts & Placeholders
    risk_budget_df, risk_budget_sum = build_risk_budget_contract_registry(active)
    per_asset_rb_df, per_asset_rb_sum = build_per_asset_risk_budget_placeholder_registry(active)
    per_strat_rb_df, per_strat_rb_sum = build_per_strategy_risk_budget_placeholder_registry(active)
    per_reg_rb_df, per_reg_rb_sum = build_per_regime_risk_budget_placeholder_registry(active)
    port_rb_df, port_rb_sum = build_portfolio_risk_budget_placeholder_registry(active)
    dd_budget_df, dd_budget_sum = build_drawdown_budget_placeholder_registry(active)
    vol_budget_df, vol_budget_sum = build_volatility_budget_placeholder_registry(active)
    exp_budget_df, exp_budget_sum = build_exposure_budget_placeholder_registry(active)

    # Limit Contracts & Placeholders
    concentration_df, concentration_sum = build_concentration_limit_contract_registry(active)
    exposure_df, exposure_sum = build_exposure_limit_contract_registry(active)
    leverage_df, leverage_sum = build_leverage_limit_placeholder_registry(active)
    margin_df, margin_sum = build_margin_limit_placeholder_registry(active)
    notional_df, notional_sum = build_notional_limit_placeholder_registry(active)
    currency_df, currency_sum = build_currency_exposure_limit_placeholder_registry(active)
    cross_asset_df, cross_asset_sum = build_cross_asset_exposure_limit_placeholder_registry(active)
    sector_df, sector_sum = build_sector_group_exposure_placeholder_registry(active)
    corr_limit_df, corr_limit_sum = build_correlation_limit_placeholder_registry(active)
    liq_limit_df, liq_limit_sum = build_liquidity_limit_placeholder_registry(active)

    # Output & Metric Contracts
    port_out_df, port_out_sum = build_portfolio_output_contract_registry(active)
    sizing_out_df, sizing_out_sum = build_position_sizing_output_contract_registry(active)
    risk_out_df, risk_out_sum = build_risk_budget_output_contract_registry(active)
    port_metric_df, port_metric_sum = build_portfolio_metric_placeholder_registry(active)
    sizing_metric_df, sizing_metric_sum = build_sizing_metric_placeholder_registry(active)
    rb_metric_df, rb_metric_sum = build_risk_budget_metric_placeholder_registry(active)
    exp_metric_df, exp_metric_sum = build_exposure_metric_placeholder_registry(active)
    conc_metric_df, conc_metric_sum = build_concentration_metric_placeholder_registry(active)

    # Guards
    lookahead_g_df, lookahead_g_sum = build_portfolio_no_lookahead_guard_registry(active)
    alloc_claim_g_df, alloc_claim_g_sum = build_portfolio_allocation_claim_guard_registry(active)
    sizing_claim_g_df, sizing_claim_g_sum = build_portfolio_position_sizing_claim_guard_registry(active)
    advice_g_df, advice_g_sum = build_portfolio_investment_advice_guard_registry(active)
    risk_claim_g_df, risk_claim_g_sum = build_portfolio_risk_limit_claim_guard_registry(active)
    snoop_g_df, snoop_g_sum = build_portfolio_data_snooping_bias_guard_registry(active)
    overfit_g_df, overfit_g_sum = build_portfolio_overfitting_guard_registry(active)
    mult_test_g_df, mult_test_g_sum = build_portfolio_multiple_testing_guard_registry(active)
    news_g_df, news_g_sum = build_portfolio_metadata_only_news_guard_registry(active)
    source_g_df, source_g_sum = build_portfolio_source_preservation_guard_registry(active)
    forbid_col_df, forbid_col_sum = build_portfolio_forbidden_column_policy_registry(active)

    # Disabled Execution Reports
    dis_pc_df, dis_pc_sum = build_portfolio_construction_execution_disabled_report(active)
    dis_sz_df, dis_sz_sum = build_position_sizing_execution_disabled_report(active)
    dis_rb_df, dis_rb_sum = build_risk_budget_execution_disabled_report(active)
    dis_al_df, dis_al_sum = build_allocation_generation_disabled_report(active)
    dis_opt_df, dis_opt_sum = build_portfolio_optimizer_disabled_report(active)
    dis_met_df, dis_met_sum = build_portfolio_metric_calculation_disabled_report(active)
    dis_trn_df, dis_trn_sum = build_portfolio_model_training_disabled_report(active)
    dis_prd_df, dis_prd_sum = build_portfolio_prediction_disabled_report(active)
    dis_liv_df, dis_liv_sum = build_portfolio_live_trading_disabled_report(active)
    dis_brk_df, dis_brk_sum = build_portfolio_broker_execution_disabled_report(active)
    dis_dep_df, dis_dep_sum = build_portfolio_deployment_disabled_report(active)

    # Governance, Readiness, Manifest, Boundaries, Handoff
    review_df, review_sum = build_portfolio_manual_review_gate_registry(active)
    findings_df, findings_sum = build_portfolio_findings_registry(active)
    readiness_df, readiness_sum = build_portfolio_readiness_score_report(findings_df=findings_df, profile=active)
    manifest_df, manifest_sum = build_portfolio_construction_manifest(active)
    safety_df, safety_sum = build_portfolio_construction_safety_boundary_report(active)
    health_df, health_sum = build_portfolio_construction_health_check(profile=active)
    validation_df, validation_sum = validate_portfolio_construction_invariants(active)
    handoff_df, handoff_sum = build_phase_154_handoff_report(active)

    results = {
        "profiles": (profiles_df, profiles_sum),
        "domains": (domains_df, domains_sum),
        "scopes": (scopes_df, scopes_sum),
        "evidence": (evidence_df, evidence_sum),
        "dependencies": (dependencies_df, dependencies_sum),
        "contracts": (contracts_df, contracts_sum),
        "universe": (universe_df, universe_sum),
        "eligibility": (eligibility_df, eligibility_sum),
        "signals": (signals_df, signals_sum),
        "risks": (risks_df, risks_sum),
        "position_sizing": (sizing_df, sizing_sum),
        "fixed_fractional": (fixed_frac_df, fixed_frac_sum),
        "volatility_targeting": (vol_target_df, vol_target_sum),
        "risk_parity": (risk_parity_df, risk_parity_sum),
        "drawdown_aware": (drawdown_aware_df, drawdown_aware_sum),
        "confidence_aware": (confidence_aware_df, confidence_aware_sum),
        "regime_aware": (regime_aware_df, regime_aware_sum),
        "correlation_aware": (corr_aware_df, corr_aware_sum),
        "liquidity_aware": (liq_aware_df, liq_aware_sum),
        "cost_aware": (cost_aware_df, cost_aware_sum),
        "slippage_aware": (slip_aware_df, slip_aware_sum),
        "risk_budget": (risk_budget_df, risk_budget_sum),
        "per_asset_risk_budget": (per_asset_rb_df, per_asset_rb_sum),
        "per_strategy_risk_budget": (per_strat_rb_df, per_strat_rb_sum),
        "per_regime_risk_budget": (per_reg_rb_df, per_reg_rb_sum),
        "portfolio_risk_budget": (port_rb_df, port_rb_sum),
        "drawdown_budget": (dd_budget_df, dd_budget_sum),
        "volatility_budget": (vol_budget_df, vol_budget_sum),
        "exposure_budget": (exp_budget_df, exp_budget_sum),
        "concentration_limits": (concentration_df, concentration_sum),
        "exposure_limits": (exposure_df, exposure_sum),
        "leverage_limits": (leverage_df, leverage_sum),
        "margin_limits": (margin_df, margin_sum),
        "notional_limits": (notional_df, notional_sum),
        "currency_limits": (currency_df, currency_sum),
        "cross_asset_limits": (cross_asset_df, cross_asset_sum),
        "sector_limits": (sector_df, sector_sum),
        "correlation_limits": (corr_limit_df, corr_limit_sum),
        "liquidity_limits": (liq_limit_df, liq_limit_sum),
        "portfolio_outputs": (port_out_df, port_out_sum),
        "sizing_outputs": (sizing_out_df, sizing_out_sum),
        "risk_outputs": (risk_out_df, risk_out_sum),
        "portfolio_metrics": (port_metric_df, port_metric_sum),
        "sizing_metrics": (sizing_metric_df, sizing_metric_sum),
        "risk_metrics": (rb_metric_df, rb_metric_sum),
        "exposure_metrics": (exp_metric_df, exp_metric_sum),
        "concentration_metrics": (conc_metric_df, conc_metric_sum),
        "guards_lookahead": (lookahead_g_df, lookahead_g_sum),
        "guards_alloc_claim": (alloc_claim_g_df, alloc_claim_g_sum),
        "guards_sizing_claim": (sizing_claim_g_df, sizing_claim_g_sum),
        "guards_advice": (advice_g_df, advice_g_sum),
        "guards_risk_claim": (risk_claim_g_df, risk_claim_g_sum),
        "guards_snoop": (snoop_g_df, snoop_g_sum),
        "guards_overfit": (overfit_g_df, overfit_g_sum),
        "guards_multiple_test": (mult_test_g_df, mult_test_g_sum),
        "guards_news": (news_g_df, news_g_sum),
        "guards_source": (source_g_df, source_g_sum),
        "guards_forbidden_col": (forbid_col_df, forbid_col_sum),
        "disabled_pc": (dis_pc_df, dis_pc_sum),
        "disabled_sz": (dis_sz_df, dis_sz_sum),
        "disabled_rb": (dis_rb_df, dis_rb_sum),
        "disabled_al": (dis_al_df, dis_al_sum),
        "disabled_opt": (dis_opt_df, dis_opt_sum),
        "disabled_met": (dis_met_df, dis_met_sum),
        "disabled_trn": (dis_trn_df, dis_trn_sum),
        "disabled_prd": (dis_prd_df, dis_prd_sum),
        "disabled_liv": (dis_liv_df, dis_liv_sum),
        "disabled_brk": (dis_brk_df, dis_brk_sum),
        "disabled_dep": (dis_dep_df, dis_dep_sum),
        "manual_review": (review_df, review_sum),
        "findings": (findings_df, findings_sum),
        "readiness_score": (readiness_df, readiness_sum),
        "manifest": (manifest_df, manifest_sum),
        "safety_boundary": (safety_df, safety_sum),
        "health": (health_df, health_sum),
        "validation": (validation_df, validation_sum),
        "handoff_phase_154": (handoff_df, handoff_sum),
    }

    if save_artifacts and hasattr(lake, "save_portfolio_construction_table"):
        for table_key, (df_data, _) in results.items():
            try:
                lake.save_portfolio_construction_table(table_key, df_data)
            except Exception:
                pass

    return results
