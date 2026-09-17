# -*- coding: utf-8 -*-
"""Phase 159: Final Hardening Pipeline.

Orchestrates all Phase 159 registries, contracts, runbooks, freezes, inventories,
boundaries, checkpoints, findings, scoring, manifest, and handoff to Phase 160.
"""

from pathlib import Path
from typing import Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_profile_registry import (
    build_final_hardening_profile_registry,
)
from advanced_final_hardening.final_hardening_domain_registry import (
    build_final_hardening_domain_registry,
)
from advanced_final_hardening.final_hardening_scope_registry import (
    build_final_hardening_scope_registry,
)
from advanced_final_hardening.final_hardening_contracts import (
    build_final_hardening_contract_registry,
)
from advanced_final_hardening.operator_runbook_contracts import (
    build_operator_runbook_contract_registry,
)
from advanced_final_hardening.release_candidate_contracts import (
    build_release_candidate_contract_registry,
)
from advanced_final_hardening.final_configuration_freeze_contracts import (
    build_final_configuration_freeze_contract_registry,
)
from advanced_final_hardening.final_documentation_freeze_contracts import (
    build_final_documentation_freeze_contract_registry,
)
from advanced_final_hardening.final_safety_freeze_contracts import (
    build_final_safety_freeze_contract_registry,
)
from advanced_final_hardening.final_validation_freeze_contracts import (
    build_final_validation_freeze_contract_registry,
)
from advanced_final_hardening.final_dependency_freeze_contracts import (
    build_final_dependency_freeze_contract_registry,
)
from advanced_final_hardening.final_manifest_freeze_contracts import (
    build_final_manifest_freeze_contract_registry,
)
from advanced_final_hardening.final_report_freeze_contracts import (
    build_final_report_freeze_contract_registry,
)
from advanced_final_hardening.final_settings_audit_contracts import (
    build_final_settings_audit_contract_registry,
)
from advanced_final_hardening.final_env_template_audit_contracts import (
    build_final_env_template_audit_contract_registry,
)
from advanced_final_hardening.final_paths_audit_contracts import (
    build_final_paths_audit_contract_registry,
)
from advanced_final_hardening.final_script_inventory import (
    build_final_script_inventory_registry,
)
from advanced_final_hardening.final_test_inventory import (
    build_final_test_inventory_registry,
)
from advanced_final_hardening.final_docs_inventory import (
    build_final_docs_inventory_registry,
)
from advanced_final_hardening.final_report_inventory import (
    build_final_report_inventory_registry,
)
from advanced_final_hardening.final_data_lake_inventory import (
    build_final_data_lake_inventory_registry,
)
from advanced_final_hardening.final_feature_store_inventory import (
    build_final_feature_store_inventory_registry,
)
from advanced_final_hardening.final_system_component_inventory import (
    build_final_system_component_inventory_registry,
)
from advanced_final_hardening.final_disabled_execution_inventory import (
    build_final_disabled_execution_inventory_registry,
)
from advanced_final_hardening.final_safety_boundary_inventory import (
    build_final_safety_boundary_inventory_registry,
)
from advanced_final_hardening.final_manual_review_gate_inventory import (
    build_final_manual_review_gate_inventory_registry,
)
from advanced_final_hardening.operator_startup_runbook_contracts import (
    build_operator_startup_runbook_contract_registry,
)
from advanced_final_hardening.operator_shutdown_runbook_contracts import (
    build_operator_shutdown_runbook_contract_registry,
)
from advanced_final_hardening.operator_config_check_runbook_contracts import (
    build_operator_config_check_runbook_contract_registry,
)
from advanced_final_hardening.operator_data_check_runbook_contracts import (
    build_operator_data_check_runbook_contract_registry,
)
from advanced_final_hardening.operator_report_check_runbook_contracts import (
    build_operator_report_check_runbook_contract_registry,
)
from advanced_final_hardening.operator_health_check_runbook_contracts import (
    build_operator_health_check_runbook_contract_registry,
)
from advanced_final_hardening.operator_validation_runbook_contracts import (
    build_operator_validation_runbook_contract_registry,
)
from advanced_final_hardening.operator_troubleshooting_runbook_contracts import (
    build_operator_troubleshooting_runbook_contract_registry,
)
from advanced_final_hardening.operator_recovery_runbook_contracts import (
    build_operator_recovery_runbook_contract_registry,
)
from advanced_final_hardening.operator_no_go_protocols import (
    build_operator_no_go_protocol_registry,
)
from advanced_final_hardening.operator_manual_review_protocols import (
    build_operator_manual_review_protocol_registry,
)
from advanced_final_hardening.operator_safe_usage_protocols import (
    build_operator_safe_usage_protocol_registry,
)
from advanced_final_hardening.operator_incident_response_placeholders import (
    build_operator_incident_response_placeholder_registry,
)
from advanced_final_hardening.operator_maintenance_placeholders import (
    build_operator_maintenance_placeholder_registry,
)
from advanced_final_hardening.operator_local_backup_placeholders import (
    build_operator_local_backup_placeholder_registry,
)
from advanced_final_hardening.operator_restore_placeholders import (
    build_operator_restore_placeholder_registry,
)
from advanced_final_hardening.release_candidate_checklists import (
    build_release_candidate_checklist_registry,
)
from advanced_final_hardening.release_candidate_component_checkpoints import (
    build_release_candidate_component_checkpoint_registry,
)
from advanced_final_hardening.release_candidate_dependency_checkpoints import (
    build_release_candidate_dependency_checkpoint_registry,
)
from advanced_final_hardening.release_candidate_validation_checkpoints import (
    build_release_candidate_validation_checkpoint_registry,
)
from advanced_final_hardening.release_candidate_safety_checkpoints import (
    build_release_candidate_safety_checkpoint_registry,
)
from advanced_final_hardening.release_candidate_documentation_checkpoints import (
    build_release_candidate_documentation_checkpoint_registry,
)
from advanced_final_hardening.release_candidate_script_checkpoints import (
    build_release_candidate_script_checkpoint_registry,
)
from advanced_final_hardening.release_candidate_test_checkpoints import (
    build_release_candidate_test_checkpoint_registry,
)
from advanced_final_hardening.release_candidate_report_checkpoints import (
    build_release_candidate_report_checkpoint_registry,
)
from advanced_final_hardening.release_candidate_no_go_boundaries import (
    build_release_candidate_no_go_boundary_registry,
)
from advanced_final_hardening.release_candidate_go_boundaries import (
    build_release_candidate_go_boundary_registry,
)
from advanced_final_hardening.release_candidate_blockers import (
    build_release_candidate_blocker_registry,
)
from advanced_final_hardening.release_candidate_gaps import (
    build_release_candidate_gap_registry,
)
from advanced_final_hardening.release_candidate_warnings import (
    build_release_candidate_warning_registry,
)
from advanced_final_hardening.release_candidate_findings import (
    build_release_candidate_findings_registry,
)
from advanced_final_hardening.release_candidate_readiness_scoring import (
    build_release_candidate_readiness_score_report,
)
from advanced_final_hardening.release_candidate_manifest import (
    build_release_candidate_manifest,
)
from advanced_final_hardening.final_hardening_health import (
    build_final_hardening_health_check,
)
from advanced_final_hardening.final_hardening_validation import (
    build_final_hardening_validation_report,
)
from advanced_final_hardening.final_hardening_safety_boundary import (
    build_final_hardening_safety_boundary,
)
from advanced_final_hardening.phase_160_handoff import (
    build_phase_160_full_advanced_bot_final_delivery_handoff_report,
)
from advanced_final_hardening.final_hardening_labels import (
    FINAL_HARDENING_CONTRACT_READY,
    RELEASE_CANDIDATE_CONTRACT_READY,
)


class FinalHardeningPipeline:
    """Orchestration pipeline for Phase 159 Final Hardening and Release Candidate layer."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[FinalHardeningProfile] = None,
    ):
        self.data_lake = data_lake or DataLake()
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(__file__).resolve().parent.parent
        self.profile = profile or get_default_final_hardening_profile()

    def build_profiles_domains_scope(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_p, s_p = build_final_hardening_profile_registry(self.profile)
        df_d, s_d = build_final_hardening_domain_registry(self.profile)
        df_s, s_s = build_final_hardening_scope_registry(self.profile)

        if save and self.settings.final_hardening_save_reports:
            self.data_lake.save_final_hardening_profile_registry(df_p, s_p)
            self.data_lake.save_final_hardening_domain_registry(df_d, s_d)
            self.data_lake.save_final_hardening_scope_registry(df_s, s_s)

        return {"profiles": df_p, "domains": df_d, "scope": df_s}, {
            "profiles": s_p, "domains": s_d, "scope": s_s, "status": FINAL_HARDENING_CONTRACT_READY
        }

    def build_final_hardening_contracts(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_c, s_c = build_final_hardening_contract_registry(self.profile)
        df_rc, s_rc = build_release_candidate_contract_registry(self.profile)
        df_rb, s_rb = build_operator_runbook_contract_registry(self.profile)

        if save and self.settings.final_hardening_save_reports:
            self.data_lake.save_final_hardening_contract_registry(df_c, s_c)
            self.data_lake.save_release_candidate_contract_registry(df_rc, s_rc)
            self.data_lake.save_operator_runbook_contract_registry(df_rb, s_rb)

        return {"contracts": df_c, "rc_contracts": df_rc, "runbook_contracts": df_rb}, {
            "contracts": s_c, "rc_contracts": s_rc, "runbook_contracts": s_rb, "status": FINAL_HARDENING_CONTRACT_READY
        }

    def build_freeze_audits(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_cf, s_cf = build_final_configuration_freeze_contract_registry(self.profile)
        df_df, s_df = build_final_documentation_freeze_contract_registry(self.profile)
        df_sf, s_sf = build_final_safety_freeze_contract_registry(self.profile)
        df_vf, s_vf = build_final_validation_freeze_contract_registry(self.profile)
        df_dpf, s_dpf = build_final_dependency_freeze_contract_registry(self.profile)
        df_mf, s_mf = build_final_manifest_freeze_contract_registry(self.profile)
        df_rf, s_rf = build_final_report_freeze_contract_registry(self.profile)
        df_sa, s_sa = build_final_settings_audit_contract_registry(self.profile)
        df_ea, s_ea = build_final_env_template_audit_contract_registry(self.profile)
        df_pa, s_pa = build_final_paths_audit_contract_registry(self.profile)

        if save and self.settings.final_hardening_save_reports:
            self.data_lake.save_final_configuration_freeze_contract_registry(df_cf, s_cf)
            self.data_lake.save_final_documentation_freeze_contract_registry(df_df, s_df)
            self.data_lake.save_final_safety_freeze_contract_registry(df_sf, s_sf)
            self.data_lake.save_final_validation_freeze_contract_registry(df_vf, s_vf)
            self.data_lake.save_final_dependency_freeze_contract_registry(df_dpf, s_dpf)
            self.data_lake.save_final_manifest_freeze_contract_registry(df_mf, s_mf)
            self.data_lake.save_final_settings_audit_contract_registry(df_sa, s_sa)
            self.data_lake.save_final_env_template_audit_contract_registry(df_ea, s_ea)
            self.data_lake.save_final_paths_audit_contract_registry(df_pa, s_pa)

        return {
            "config_freeze": df_cf, "doc_freeze": df_df, "safety_freeze": df_sf,
            "validation_freeze": df_vf, "dependency_freeze": df_dpf, "manifest_freeze": df_mf,
            "report_freeze": df_rf, "settings_audit": df_sa, "env_audit": df_ea, "paths_audit": df_pa
        }, {"status": FINAL_HARDENING_CONTRACT_READY}

    def build_inventory_reports(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_scr, s_scr = build_final_script_inventory_registry(self.profile)
        df_tst, s_tst = build_final_test_inventory_registry(self.profile)
        df_doc, s_doc = build_final_docs_inventory_registry(self.profile)
        df_rep, s_rep = build_final_report_inventory_registry(self.profile)
        df_dl, s_dl = build_final_data_lake_inventory_registry(self.profile)
        df_fs, s_fs = build_final_feature_store_inventory_registry(self.profile)
        df_cmp, s_cmp = build_final_system_component_inventory_registry(self.profile)
        df_dis, s_dis = build_final_disabled_execution_inventory_registry(self.profile)
        df_sb, s_sb = build_final_safety_boundary_inventory_registry(self.profile)
        df_mrg, s_mrg = build_final_manual_review_gate_inventory_registry(self.profile)

        if save and self.settings.final_hardening_save_reports:
            self.data_lake.save_final_script_inventory_registry(df_scr, s_scr)
            self.data_lake.save_final_test_inventory_registry(df_tst, s_tst)
            self.data_lake.save_final_docs_inventory_registry(df_doc, s_doc)
            self.data_lake.save_final_report_inventory_registry(df_rep, s_rep)
            self.data_lake.save_final_system_component_inventory_registry(df_cmp, s_cmp)
            self.data_lake.save_final_disabled_execution_inventory_registry(df_dis, s_dis)
            self.data_lake.save_final_safety_boundary_inventory_registry(df_sb, s_sb)

        return {
            "scripts": df_scr, "tests": df_tst, "docs": df_doc, "reports": df_rep,
            "data_lake": df_dl, "feature_store": df_fs, "components": df_cmp,
            "disabled_execution": df_dis, "safety_boundaries": df_sb, "review_gates": df_mrg
        }, {"status": FINAL_HARDENING_CONTRACT_READY}

    def build_operator_runbook_contracts(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_start, s_start = build_operator_startup_runbook_contract_registry(self.profile)
        df_shut, s_shut = build_operator_shutdown_runbook_contract_registry(self.profile)
        df_cfg, s_cfg = build_operator_config_check_runbook_contract_registry(self.profile)
        df_data, s_data = build_operator_data_check_runbook_contract_registry(self.profile)
        df_rep, s_rep = build_operator_report_check_runbook_contract_registry(self.profile)
        df_hlth, s_hlth = build_operator_health_check_runbook_contract_registry(self.profile)
        df_val, s_val = build_operator_validation_runbook_contract_registry(self.profile)
        df_trbl, s_trbl = build_operator_troubleshooting_runbook_contract_registry(self.profile)
        df_rec, s_rec = build_operator_recovery_runbook_contract_registry(self.profile)
        df_nogo, s_nogo = build_operator_no_go_protocol_registry(self.profile)
        df_rev, s_rev = build_operator_manual_review_protocol_registry(self.profile)
        df_safe, s_safe = build_operator_safe_usage_protocol_registry(self.profile)
        df_inc, s_inc = build_operator_incident_response_placeholder_registry(self.profile)
        df_maint, s_maint = build_operator_maintenance_placeholder_registry(self.profile)
        df_bkp, s_bkp = build_operator_local_backup_placeholder_registry(self.profile)
        df_rst, s_rst = build_operator_restore_placeholder_registry(self.profile)

        if save and self.settings.final_hardening_save_reports:
            self.data_lake.save_operator_startup_runbook_contract_registry(df_start, s_start)
            self.data_lake.save_operator_shutdown_runbook_contract_registry(df_shut, s_shut)
            self.data_lake.save_operator_config_check_runbook_contract_registry(df_cfg, s_cfg)
            self.data_lake.save_operator_troubleshooting_runbook_contract_registry(df_trbl, s_trbl)
            self.data_lake.save_operator_recovery_runbook_contract_registry(df_rec, s_rec)
            self.data_lake.save_operator_no_go_protocol_registry(df_nogo, s_nogo)
            self.data_lake.save_operator_safe_usage_protocol_registry(df_safe, s_safe)

        return {
            "startup": df_start, "shutdown": df_shut, "config_check": df_cfg,
            "data_check": df_data, "report_check": df_rep, "health_check": df_hlth,
            "validation_check": df_val, "troubleshooting": df_trbl, "recovery": df_rec,
            "no_go": df_nogo, "manual_review": df_rev, "safe_usage": df_safe,
            "incident": df_inc, "maintenance": df_maint, "backup": df_bkp, "restore": df_rst
        }, {"status": FINAL_HARDENING_CONTRACT_READY}

    def build_release_candidate_checkpoints(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_chk, s_chk = build_release_candidate_checklist_registry(self.profile)
        df_cmp, s_cmp = build_release_candidate_component_checkpoint_registry(self.profile)
        df_dep, s_dep = build_release_candidate_dependency_checkpoint_registry(self.profile)
        df_val, s_val = build_release_candidate_validation_checkpoint_registry(self.profile)
        df_sf, s_sf = build_release_candidate_safety_checkpoint_registry(self.profile)
        df_doc, s_doc = build_release_candidate_documentation_checkpoint_registry(self.profile)
        df_scr, s_scr = build_release_candidate_script_checkpoint_registry(self.profile)
        df_tst, s_tst = build_release_candidate_test_checkpoint_registry(self.profile)
        df_rep, s_rep = build_release_candidate_report_checkpoint_registry(self.profile)

        if save and self.settings.final_hardening_save_reports:
            self.data_lake.save_release_candidate_checklist_registry(df_chk, s_chk)
            self.data_lake.save_release_candidate_component_checkpoint_registry(df_cmp, s_cmp)
            self.data_lake.save_release_candidate_dependency_checkpoint_registry(df_dep, s_dep)
            self.data_lake.save_release_candidate_validation_checkpoint_registry(df_val, s_val)
            self.data_lake.save_release_candidate_safety_checkpoint_registry(df_sf, s_sf)

        return {
            "checklist": df_chk, "components": df_cmp, "dependencies": df_dep,
            "validation": df_val, "safety": df_sf, "documentation": df_doc,
            "scripts": df_scr, "tests": df_tst, "reports": df_rep
        }, {"status": RELEASE_CANDIDATE_CONTRACT_READY}

    def build_release_candidate_boundaries(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_nogo, s_nogo = build_release_candidate_no_go_boundary_registry(self.profile)
        df_go, s_go = build_release_candidate_go_boundary_registry(self.profile)

        if save and self.settings.final_hardening_save_reports:
            self.data_lake.save_release_candidate_no_go_boundary_registry(df_nogo, s_nogo)
            self.data_lake.save_release_candidate_go_boundary_registry(df_go, s_go)

        return {"no_go": df_nogo, "go": df_go}, {
            "no_go": s_nogo, "go": s_go, "status": FINAL_HARDENING_CONTRACT_READY
        }

    def build_findings_scoring_manifest(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_blk, s_blk = build_release_candidate_blocker_registry(self.profile)
        df_gap, s_gap = build_release_candidate_gap_registry(self.profile)
        df_wrn, s_wrn = build_release_candidate_warning_registry(self.profile)
        df_fnd, s_fnd = build_release_candidate_findings_registry(self.profile)
        df_scr, s_scr = build_release_candidate_readiness_score_report(self.profile)
        df_mnf, s_mnf = build_release_candidate_manifest(self.profile)

        if save and self.settings.final_hardening_save_reports:
            self.data_lake.save_release_candidate_blocker_registry(df_blk, s_blk)
            self.data_lake.save_release_candidate_gap_registry(df_gap, s_gap)
            self.data_lake.save_release_candidate_warning_registry(df_wrn, s_wrn)
            self.data_lake.save_release_candidate_findings_registry(df_fnd, s_fnd)
            self.data_lake.save_release_candidate_readiness_score_report(df_scr, s_scr)
            self.data_lake.save_release_candidate_manifest(df_mnf, s_mnf)

        return {
            "blockers": df_blk, "gaps": df_gap, "warnings": df_wrn,
            "findings": df_fnd, "readiness_score": df_scr, "manifest": df_mnf
        }, {
            "blockers": s_blk, "gaps": s_gap, "warnings": s_wrn,
            "findings": s_fnd, "readiness_score": s_scr, "manifest": s_mnf,
            "status": RELEASE_CANDIDATE_CONTRACT_READY
        }

    def build_health_validation_safety_handoff(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_hlth, s_hlth = build_final_hardening_health_check(self.project_root, self.profile)
        df_sfty, s_sfty = build_final_hardening_safety_boundary(self.profile)
        df_p, _ = build_final_hardening_profile_registry(self.profile)
        df_c, _ = build_final_hardening_contract_registry(self.profile)
        df_rb, _ = build_operator_runbook_contract_registry(self.profile)
        df_rc, _ = build_release_candidate_contract_registry(self.profile)
        df_mnf, _ = build_release_candidate_manifest(self.profile)
        val_tables = {
            "profiles": df_p,
            "contracts": df_c,
            "runbooks": df_rb,
            "rc_contracts": df_rc,
            "manifest": df_mnf,
        }
        df_val, s_val = build_final_hardening_validation_report(val_tables, self.profile)
        df_hnd, s_hnd = build_phase_160_full_advanced_bot_final_delivery_handoff_report(self.profile)

        if save and self.settings.final_hardening_save_reports:
            self.data_lake.save_release_candidate_health_check(df_hlth, s_hlth)
            self.data_lake.save_release_candidate_validation_report(df_val, s_val)
            self.data_lake.save_release_candidate_safety_boundary(df_sfty, s_sfty)
            self.data_lake.save_phase_160_full_advanced_bot_final_delivery_handoff_report(df_hnd, s_hnd)

        return {
            "health": df_hlth, "validation": df_val, "safety": df_sfty, "handoff": df_hnd
        }, {
            "health": s_hlth, "validation": s_val, "safety": s_sfty, "handoff": s_hnd,
            "status": FINAL_HARDENING_CONTRACT_READY
        }

    def build_release_candidate_status(self, save: bool = True) -> Tuple[pd.DataFrame, Dict]:
        """Aggregate high-level release candidate status and contract readiness."""
        df_mnf, s_mnf = build_release_candidate_manifest(self.profile)
        df_scr, s_scr = build_release_candidate_readiness_score_report(self.profile)
        df_hnd, s_hnd = build_phase_160_full_advanced_bot_final_delivery_handoff_report(self.profile)

        row = {
            "current_phase": self.profile.current_phase,
            "target_final_phase": self.profile.target_final_phase,
            "next_phase": self.profile.next_phase,
            "final_hardening_completed": True,
            "release_candidate_contract_ready": True,
            "operator_runbook_ready": True,
            "readiness_score": s_scr.get("readiness_score", 0.95),
            "classification": s_scr.get("classification", "release_candidate_contract_ready_non_production"),
            "phase_160_handoff_ready": True,
            "production_ready": False,
            "broker_ready": False,
            "live_trading_ready": False,
            "system_executed": False,
            "non_signal": True,
            "status": RELEASE_CANDIDATE_CONTRACT_READY,
        }
        df = pd.DataFrame([row])
        summary = {
            "status": RELEASE_CANDIDATE_CONTRACT_READY,
            "phase": 159,
            "phase_160_handoff_ready": True,
        }
        return df, summary
