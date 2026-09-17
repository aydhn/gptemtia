# -*- coding: utf-8 -*-
"""Phase 158: Full-System Integration Pipeline.

Coordinates generation of all Phase 158 system integration registries, checkpoints,
boundaries, findings, readiness scores, manifests, health checks, validation reports,
and Phase 159 handoff documents.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from .full_system_integration_config import (
    FullSystemIntegrationProfile,
    get_default_full_system_integration_profile,
)
from .full_system_integration_profile_registry import (
    build_full_system_integration_profile_registry,
)
from .full_system_integration_domain_registry import (
    build_full_system_integration_domain_registry,
)
from .full_system_integration_scope_registry import (
    build_full_system_integration_scope_registry,
)
from .system_component_registry import (
    build_system_component_registry,
)
from .system_component_dependencies import (
    build_system_component_dependency_registry,
)
from .system_component_checkpoints import (
    build_system_component_checkpoint_registry,
)
from .system_contract_integration import (
    build_system_contract_integration_registry,
)
from .system_manifest_integration import (
    build_system_manifest_integration_registry,
)
from .system_validation_evidence import (
    build_system_validation_evidence_registry,
)
from .system_safety_boundaries import (
    build_system_safety_boundary_registry,
)
from .system_non_production_boundaries import (
    build_system_non_production_boundary_registry,
)
from .system_dry_run_boundaries import (
    build_system_dry_run_boundary_registry,
)
from .system_manual_review_gates import (
    build_system_manual_review_gate_registry,
)
from .advanced_acceptance_rehearsal import (
    build_advanced_acceptance_rehearsal_registry,
)
from .advanced_acceptance_rehearsal_checkpoints import (
    build_advanced_acceptance_rehearsal_checkpoint_registry,
)
from .advanced_acceptance_rehearsal_scripts import (
    build_advanced_acceptance_rehearsal_script_registry,
)
from .advanced_acceptance_rehearsal_documentation import (
    build_advanced_acceptance_rehearsal_documentation_registry,
)
from .data_pipeline_integration import (
    build_data_pipeline_integration_registry,
)
from .feature_factor_integration import (
    build_feature_factor_integration_registry,
)
from .regime_integration import (
    build_regime_integration_registry,
)
from .ml_governance_integration import (
    build_ml_governance_integration_registry,
)
from .backtest_acceptance_integration import (
    build_backtest_acceptance_integration_registry,
)
from .portfolio_acceptance_integration import (
    build_portfolio_acceptance_integration_registry,
)
from .risk_reporting_integration import (
    build_risk_reporting_integration_registry,
)
from .scenario_control_integration import (
    build_scenario_control_integration_registry,
)
from .reporting_integration import (
    build_reporting_integration_registry,
)
from .telegram_interface_integration_placeholders import (
    build_telegram_interface_integration_placeholder_registry,
)
from .local_paper_trading_integration_placeholders import (
    build_local_paper_trading_integration_placeholder_registry,
)
from .non_live_signal_output_boundaries import (
    build_non_live_signal_output_boundary_registry,
)
from .no_broker_boundaries import (
    build_no_broker_boundary_registry,
)
from .no_live_trading_boundaries import (
    build_no_live_trading_boundary_registry,
)
from .no_investment_advice_boundaries import (
    build_no_investment_advice_boundary_registry,
)
from .no_production_deployment_boundaries import (
    build_no_production_deployment_boundary_registry,
)
from .no_model_registry_write_boundaries import (
    build_no_model_registry_write_boundary_registry,
)
from .no_artifact_persistence_boundaries import (
    build_no_artifact_persistence_boundary_registry,
)
from .no_scraping_boundaries import (
    build_no_scraping_boundary_registry,
)
from .source_preservation_boundaries import (
    build_source_preservation_boundary_registry,
)
from .metadata_only_news_boundaries import (
    build_metadata_only_news_boundary_registry,
)
from .forbidden_column_system_policies import (
    build_forbidden_column_system_policy_registry,
)
from .system_execution_disabled import (
    build_system_execution_disabled_report,
)
from .live_trading_disabled import (
    build_live_trading_disabled_report,
)
from .broker_execution_disabled import (
    build_broker_execution_disabled_report,
)
from .production_deployment_disabled import (
    build_production_deployment_disabled_report,
)
from .model_training_disabled import (
    build_model_training_disabled_report,
)
from .model_prediction_disabled import (
    build_model_prediction_disabled_report,
)
from .backtest_execution_disabled import (
    build_backtest_execution_disabled_report,
)
from .portfolio_execution_disabled import (
    build_portfolio_execution_disabled_report,
)
from .risk_execution_disabled import (
    build_risk_execution_disabled_report,
)
from .scenario_execution_disabled import (
    build_scenario_execution_disabled_report,
)
from .order_generation_disabled import (
    build_order_generation_disabled_report,
)
from .signal_generation_disabled import (
    build_signal_generation_disabled_report,
)
from .investment_advice_disabled import (
    build_investment_advice_disabled_report,
)
from .system_integration_blockers import (
    build_system_integration_blocker_registry,
)
from .system_integration_gaps import (
    build_system_integration_gap_registry,
)
from .system_integration_warnings import (
    build_system_integration_warning_registry,
)
from .system_integration_findings import (
    build_system_integration_findings_registry,
)
from .system_integration_readiness_scoring import (
    build_system_integration_readiness_score_report,
)
from .full_system_integration_manifest import (
    build_full_system_integration_manifest,
)
from .full_system_integration_report_builder import (
    build_full_system_integration_full_markdown_report,
)
from .full_system_integration_health import (
    build_full_system_integration_health_check,
)
from .full_system_integration_validation import (
    build_full_system_integration_validation_report,
)
from .full_system_integration_safety_boundary import (
    build_full_system_integration_safety_boundary,
)
from .phase_159_handoff import (
    build_phase_159_final_hardening_operator_runbook_release_candidate_handoff_report,
)


class FullSystemIntegrationPipeline:
    """End-to-end pipeline orchestrator for Phase 158 Full-System Integration."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[FullSystemIntegrationProfile] = None,
    ):
        self.data_lake = data_lake or DataLake()
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(".")
        self.profile = profile or get_default_full_system_integration_profile()

    def build_profiles_domains_scope(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build profile, domain, and scope registries."""
        df_prof, s_prof = build_full_system_integration_profile_registry(self.profile)
        df_dom, s_dom = build_full_system_integration_domain_registry(self.profile)
        df_scp, s_scp = build_full_system_integration_scope_registry(self.profile)

        if save and hasattr(self.data_lake, "save_full_system_integration_profile_registry"):
            self.data_lake.save_full_system_integration_profile_registry(df_prof, s_prof)
            self.data_lake.save_full_system_integration_domain_registry(df_dom, s_dom)
            self.data_lake.save_full_system_integration_scope_registry(df_scp, s_scp)

        dfs = {"profiles": df_prof, "domains": df_dom, "scope": df_scp}
        summary = {"profiles": s_prof, "domains": s_dom, "scope": s_scp, "non_signal": True}
        return dfs, summary

    def build_components_dependencies_checkpoints(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build component, dependency, and checkpoint registries."""
        df_cmp, s_cmp = build_system_component_registry(self.profile)
        df_dep, s_dep = build_system_component_dependency_registry(self.profile)
        df_chk, s_chk = build_system_component_checkpoint_registry(self.profile)

        if save and hasattr(self.data_lake, "save_system_component_registry"):
            self.data_lake.save_system_component_registry(df_cmp, s_cmp)
            self.data_lake.save_system_component_dependency_registry(df_dep, s_dep)
            self.data_lake.save_system_component_checkpoint_registry(df_chk, s_chk)

        dfs = {"components": df_cmp, "dependencies": df_dep, "checkpoints": df_chk}
        summary = {"components": s_cmp, "dependencies": s_dep, "checkpoints": s_chk, "non_signal": True}
        return dfs, summary

    def build_contract_manifest_validation_integration(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build contract, manifest, and validation evidence integration registries."""
        df_cnt, s_cnt = build_system_contract_integration_registry(self.profile)
        df_mnf, s_mnf = build_system_manifest_integration_registry(self.profile)
        df_evd, s_evd = build_system_validation_evidence_registry(self.profile)

        if save and hasattr(self.data_lake, "save_system_contract_integration_registry"):
            self.data_lake.save_system_contract_integration_registry(df_cnt, s_cnt)
            self.data_lake.save_system_manifest_integration_registry(df_mnf, s_mnf)
            self.data_lake.save_system_validation_evidence_registry(df_evd, s_evd)

        dfs = {"contracts": df_cnt, "manifests": df_mnf, "evidence": df_evd}
        summary = {"contracts": s_cnt, "manifests": s_mnf, "evidence": s_evd, "non_signal": True}
        return dfs, summary

    def build_boundaries_manual_review(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build safety, non-production, dry-run boundaries and manual review gates."""
        df_sft, s_sft = build_system_safety_boundary_registry(self.profile)
        df_npb, s_npb = build_system_non_production_boundary_registry(self.profile)
        df_drb, s_drb = build_system_dry_run_boundary_registry(self.profile)
        df_mrg, s_mrg = build_system_manual_review_gate_registry(self.profile)
        df_nls, s_nls = build_non_live_signal_output_boundary_registry(self.profile)
        df_nbr, s_nbr = build_no_broker_boundary_registry(self.profile)
        df_nlt, s_nlt = build_no_live_trading_boundary_registry(self.profile)
        df_nia, s_nia = build_no_investment_advice_boundary_registry(self.profile)
        df_npd, s_npd = build_no_production_deployment_boundary_registry(self.profile)
        df_nmr, s_nmr = build_no_model_registry_write_boundary_registry(self.profile)
        df_nap, s_nap = build_no_artifact_persistence_boundary_registry(self.profile)
        df_nsc, s_nsc = build_no_scraping_boundary_registry(self.profile)
        df_spr, s_spr = build_source_preservation_boundary_registry(self.profile)
        df_nmd, s_nmd = build_metadata_only_news_boundary_registry(self.profile)
        df_fcp, s_fcp = build_forbidden_column_system_policy_registry(self.profile)

        if save and hasattr(self.data_lake, "save_system_safety_boundary_registry"):
            self.data_lake.save_system_safety_boundary_registry(df_sft, s_sft)
            self.data_lake.save_system_non_production_boundary_registry(df_npb, s_npb)
            self.data_lake.save_system_dry_run_boundary_registry(df_drb, s_drb)
            self.data_lake.save_system_manual_review_gate_registry(df_mrg, s_mrg)
            self.data_lake.save_forbidden_column_system_policy_registry(df_fcp, s_fcp)

        dfs = {
            "safety": df_sft,
            "non_production": df_npb,
            "dry_run": df_drb,
            "manual_review_gates": df_mrg,
            "non_live_signal": df_nls,
            "no_broker": df_nbr,
            "no_live_trading": df_nlt,
            "no_investment_advice": df_nia,
            "no_production_deployment": df_npd,
            "no_model_registry_write": df_nmr,
            "no_artifact_persistence": df_nap,
            "no_scraping": df_nsc,
            "source_preservation": df_spr,
            "metadata_only_news": df_nmd,
            "forbidden_columns": df_fcp,
        }
        summary = {
            "safety": s_sft,
            "non_production": s_npb,
            "dry_run": s_drb,
            "manual_review_gates": s_mrg,
            "forbidden_columns": s_fcp,
            "non_signal": True,
        }
        return dfs, summary

    def build_advanced_acceptance_rehearsal(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build acceptance rehearsal checklist, checkpoints, scripts, and documentation registries."""
        df_reh, s_reh = build_advanced_acceptance_rehearsal_registry(self.profile)
        df_rcp, s_rcp = build_advanced_acceptance_rehearsal_checkpoint_registry(self.profile)
        df_rsc, s_rsc = build_advanced_acceptance_rehearsal_script_registry(self.profile)
        df_rdc, s_rdc = build_advanced_acceptance_rehearsal_documentation_registry(self.profile)

        if save and hasattr(self.data_lake, "save_advanced_acceptance_rehearsal_registry"):
            self.data_lake.save_advanced_acceptance_rehearsal_registry(df_reh, s_reh)
            self.data_lake.save_advanced_acceptance_rehearsal_checkpoint_registry(df_rcp, s_rcp)

        dfs = {"rehearsal": df_reh, "checkpoints": df_rcp, "scripts": df_rsc, "docs": df_rdc}
        summary = {"rehearsal": s_reh, "checkpoints": s_rcp, "scripts": s_rsc, "docs": s_rdc, "non_signal": True}
        return dfs, summary

    def build_subsystem_integrations(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build integration registries for all subsystems."""
        df_dpi, s_dpi = build_data_pipeline_integration_registry(self.profile)
        df_ffi, s_ffi = build_feature_factor_integration_registry(self.profile)
        df_rgi, s_rgi = build_regime_integration_registry(self.profile)
        df_mlg, s_mlg = build_ml_governance_integration_registry(self.profile)
        df_bai, s_bai = build_backtest_acceptance_integration_registry(self.profile)
        df_pai, s_pai = build_portfolio_acceptance_integration_registry(self.profile)
        df_rri, s_rri = build_risk_reporting_integration_registry(self.profile)
        df_sci, s_sci = build_scenario_control_integration_registry(self.profile)
        df_rpi, s_rpi = build_reporting_integration_registry(self.profile)
        df_tgm, s_tgm = build_telegram_interface_integration_placeholder_registry(self.profile)
        df_ptr, s_ptr = build_local_paper_trading_integration_placeholder_registry(self.profile)

        if save and hasattr(self.data_lake, "save_data_pipeline_integration_registry"):
            self.data_lake.save_data_pipeline_integration_registry(df_dpi, s_dpi)
            self.data_lake.save_feature_factor_integration_registry(df_ffi, s_ffi)
            self.data_lake.save_regime_integration_registry(df_rgi, s_rgi)
            self.data_lake.save_ml_governance_integration_registry(df_mlg, s_mlg)
            self.data_lake.save_backtest_acceptance_integration_registry(df_bai, s_bai)
            self.data_lake.save_portfolio_acceptance_integration_registry(df_pai, s_pai)
            self.data_lake.save_risk_reporting_integration_registry(df_rri, s_rri)
            self.data_lake.save_scenario_control_integration_registry(df_sci, s_sci)
            self.data_lake.save_reporting_integration_registry(df_rpi, s_rpi)

        dfs = {
            "data_pipeline": df_dpi,
            "feature_factor": df_ffi,
            "regime": df_rgi,
            "ml_governance": df_mlg,
            "backtest_acceptance": df_bai,
            "portfolio_acceptance": df_pai,
            "risk_reporting": df_rri,
            "scenario_control": df_sci,
            "reporting": df_rpi,
            "telegram_placeholder": df_tgm,
            "paper_trading_placeholder": df_ptr,
        }
        summary = {
            "data_pipeline": s_dpi,
            "feature_factor": s_ffi,
            "regime": s_rgi,
            "ml_governance": s_mlg,
            "backtest_acceptance": s_bai,
            "portfolio_acceptance": s_pai,
            "risk_reporting": s_rri,
            "scenario_control": s_sci,
            "reporting": s_rpi,
            "telegram_placeholder": s_tgm,
            "paper_trading_placeholder": s_ptr,
            "non_signal": True,
        }
        return dfs, summary

    def build_disabled_execution_reports(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build disabled execution reports for all 13 subsystems."""
        df_sed, s_sed = build_system_execution_disabled_report(self.profile)
        df_ltd, s_ltd = build_live_trading_disabled_report(self.profile)
        df_bed, s_bed = build_broker_execution_disabled_report(self.profile)
        df_pdd, s_pdd = build_production_deployment_disabled_report(self.profile)
        df_mtd, s_mtd = build_model_training_disabled_report(self.profile)
        df_mpd, s_mpd = build_model_prediction_disabled_report(self.profile)
        df_bxd, s_bxd = build_backtest_execution_disabled_report(self.profile)
        df_pxd, s_pxd = build_portfolio_execution_disabled_report(self.profile)
        df_rxd, s_rxd = build_risk_execution_disabled_report(self.profile)
        df_sxd, s_sxd = build_scenario_execution_disabled_report(self.profile)
        df_ogd, s_ogd = build_order_generation_disabled_report(self.profile)
        df_sgd, s_sgd = build_signal_generation_disabled_report(self.profile)
        df_iad, s_iad = build_investment_advice_disabled_report(self.profile)

        if save and hasattr(self.data_lake, "save_system_execution_disabled_report"):
            self.data_lake.save_system_execution_disabled_report(df_sed, s_sed)
            self.data_lake.save_live_trading_disabled_report(df_ltd, s_ltd)
            self.data_lake.save_broker_execution_disabled_report(df_bed, s_bed)
            self.data_lake.save_production_deployment_disabled_report(df_pdd, s_pdd)
            self.data_lake.save_model_training_disabled_report(df_mtd, s_mtd)
            self.data_lake.save_model_prediction_disabled_report(df_mpd, s_mpd)
            self.data_lake.save_order_generation_disabled_report(df_ogd, s_ogd)
            self.data_lake.save_signal_generation_disabled_report(df_sgd, s_sgd)
            self.data_lake.save_investment_advice_disabled_report(df_iad, s_iad)

        dfs = {
            "system_execution_disabled": df_sed,
            "live_trading_disabled": df_ltd,
            "broker_execution_disabled": df_bed,
            "production_deployment_disabled": df_pdd,
            "model_training_disabled": df_mtd,
            "model_prediction_disabled": df_mpd,
            "backtest_execution_disabled": df_bxd,
            "portfolio_execution_disabled": df_pxd,
            "risk_execution_disabled": df_rxd,
            "scenario_execution_disabled": df_sxd,
            "order_generation_disabled": df_ogd,
            "signal_generation_disabled": df_sgd,
            "investment_advice_disabled": df_iad,
        }
        summary = {
            "system_execution": s_sed,
            "live_trading": s_ltd,
            "broker_execution": s_bed,
            "production_deployment": s_pdd,
            "model_training": s_mtd,
            "model_prediction": s_mpd,
            "backtest": s_bxd,
            "portfolio": s_pxd,
            "risk": s_rxd,
            "scenario": s_sxd,
            "order_generation": s_ogd,
            "signal_generation": s_sgd,
            "investment_advice": s_iad,
            "non_signal": True,
        }
        return dfs, summary

    def build_findings_scoring_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build blockers, gaps, warnings, findings, readiness score, and manifest."""
        df_blk, s_blk = build_system_integration_blocker_registry(self.profile)
        df_gap, s_gap = build_system_integration_gap_registry(self.profile)
        df_wrn, s_wrn = build_system_integration_warning_registry(self.profile)
        df_fnd, s_fnd = build_system_integration_findings_registry(self.profile)
        df_scr, s_scr = build_system_integration_readiness_score_report(self.profile)
        df_mnf, s_mnf = build_full_system_integration_manifest(self.profile)

        if save and hasattr(self.data_lake, "save_system_integration_findings_registry"):
            self.data_lake.save_system_integration_findings_registry(df_fnd, s_fnd)
            self.data_lake.save_system_integration_readiness_score_report(df_scr, s_scr)
            self.data_lake.save_full_system_integration_manifest(df_mnf, s_mnf)

        dfs = {
            "blockers": df_blk,
            "gaps": df_gap,
            "warnings": df_wrn,
            "findings": df_fnd,
            "scoring": df_scr,
            "manifest": df_mnf,
        }
        summary = {
            "blockers": s_blk,
            "gaps": s_gap,
            "warnings": s_wrn,
            "findings": s_fnd,
            "scoring": s_scr,
            "manifest": s_mnf,
            "non_signal": True,
        }
        return dfs, summary

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build health check, validation report, safety boundary, and Phase 159 handoff."""
        dfs_prof, _ = self.build_profiles_domains_scope(save=False)
        dfs_cmp, _ = self.build_components_dependencies_checkpoints(save=False)
        dfs_cnt, _ = self.build_contract_manifest_validation_integration(save=False)
        dfs_reh, _ = self.build_advanced_acceptance_rehearsal(save=False)
        dfs_fnd, _ = self.build_findings_scoring_manifest(save=False)

        eval_tables = {
            "profiles": dfs_prof["profiles"],
            "checkpoints": dfs_cmp["checkpoints"],
            "contracts": dfs_cnt["contracts"],
            "rehearsal": dfs_reh["rehearsal"],
            "manifest": dfs_fnd["manifest"],
            "summary": {"active_profile": self.profile.profile_name},
        }

        df_hlth, s_hlth = build_full_system_integration_health_check(self.project_root, self.profile)
        df_val, s_val = build_full_system_integration_validation_report(eval_tables, self.profile)
        df_sft, s_sft = build_full_system_integration_safety_boundary(self.profile)
        df_hnd, s_hnd = build_phase_159_final_hardening_operator_runbook_release_candidate_handoff_report(self.profile)

        if save and hasattr(self.data_lake, "save_full_system_integration_health_check"):
            self.data_lake.save_full_system_integration_health_check(df_hlth, s_hlth)
            self.data_lake.save_full_system_integration_validation_report(df_val, s_val)
            self.data_lake.save_full_system_integration_safety_boundary(df_sft, s_sft)
            self.data_lake.save_phase_159_final_hardening_operator_runbook_release_candidate_handoff_report(df_hnd, s_hnd)

        dfs = {
            "health": df_hlth,
            "validation": df_val,
            "safety": df_sft,
            "handoff": df_hnd,
        }
        summary = {
            "health": s_hlth,
            "validation": s_val,
            "safety": s_sft,
            "handoff": s_hnd,
            "non_signal": True,
        }
        return dfs, summary

    def build_full_system_integration_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Run full system integration pipeline and return status summary."""
        dfs_prof, s_prof = self.build_profiles_domains_scope(save=save)
        dfs_cmp, s_cmp = self.build_components_dependencies_checkpoints(save=save)
        dfs_cnt, s_cnt = self.build_contract_manifest_validation_integration(save=save)
        dfs_bnd, s_bnd = self.build_boundaries_manual_review(save=save)
        dfs_reh, s_reh = self.build_advanced_acceptance_rehearsal(save=save)
        dfs_sub, s_sub = self.build_subsystem_integrations(save=save)
        dfs_dis, s_dis = self.build_disabled_execution_reports(save=save)
        dfs_fnd, s_fnd = self.build_findings_scoring_manifest(save=save)
        dfs_hvs, s_hvs = self.build_health_validation_safety_handoff(save=save)

        status_records = [
            {"domain": "profiles_domains_scope", "status": "READY", "items": len(dfs_prof["profiles"])},
            {"domain": "components_dependencies_checkpoints", "status": "READY", "items": len(dfs_cmp["components"])},
            {"domain": "contract_manifest_evidence", "status": "READY", "items": len(dfs_cnt["contracts"])},
            {"domain": "boundaries_manual_review", "status": "READY", "items": len(dfs_bnd["safety"])},
            {"domain": "advanced_acceptance_rehearsal", "status": "READY", "items": len(dfs_reh["rehearsal"])},
            {"domain": "subsystem_integrations", "status": "READY", "items": len(dfs_sub)},
            {"domain": "disabled_execution_reports", "status": "READY", "items": len(dfs_dis)},
            {"domain": "findings_scoring_manifest", "status": "READY", "score": s_fnd["scoring"]["readiness_score"]},
            {"domain": "health_validation_handoff", "status": "READY", "handoff_ready": s_hvs["handoff"]["handoff_ready"]},
        ]
        status_df = pd.DataFrame(status_records)

        full_tables = {
            "components": dfs_cmp["components"],
            "dependencies": dfs_cmp["dependencies"],
            "rehearsal": dfs_reh["rehearsal"],
            "manifest": dfs_fnd["manifest"],
            "handoff": dfs_hvs["handoff"],
        }
        full_summary = {
            "active_profile": self.profile.profile_name,
            "readiness_score": s_fnd["scoring"]["readiness_score"],
            "classification": s_fnd["scoring"]["classification"],
            "meets_threshold": s_fnd["scoring"]["meets_threshold"],
            "handoff_ready": s_hvs["handoff"]["handoff_ready"],
            "status": "ACCEPTED",
            "non_signal": True,
        }

        full_md = build_full_system_integration_full_markdown_report(full_tables, full_summary)

        if save:
            out_dir = Path("reports/output/advanced_full_system_integration")
            out_dir.mkdir(parents=True, exist_ok=True)
            with open(out_dir / "full_system_integration_report.md", "w", encoding="utf-8") as f:
                f.write(full_md)
            if hasattr(self.data_lake, "save_full_system_integration_report"):
                self.data_lake.save_full_system_integration_report(
                    self.profile.profile_name,
                    full_summary,
                    full_md,
                )

        return status_df, full_summary
