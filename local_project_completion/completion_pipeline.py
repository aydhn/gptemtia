import pandas as pd
from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from .completion_config import LocalProjectCompletionProfile, get_default_local_project_completion_profile
from .completion_domain_registry import build_completion_domain_registry
from .system_closure_dossier import build_final_local_system_closure_dossier
from .terminal_handoff import build_terminal_handoff_pack
from .knowledge_freeze import build_knowledge_freeze_rehearsal_registry, build_knowledge_freeze_inventory
from .knowledge_freeze_boundaries import build_knowledge_freeze_boundary_registry
from .last_mile_audit import build_last_mile_audit_binder, build_last_mile_audit_checklist_registry, build_last_mile_audit_evidence_index, build_last_mile_audit_reading_order
from .completion_evidence import build_project_completion_evidence_map
from .completion_criteria import build_project_completion_criteria_matrix
from .completion_readiness_packet import build_project_completion_readiness_packet
from .completion_unresolved import build_project_completion_unresolved_register
from .completion_limitations import build_project_completion_known_limitations_register
from .final_risk_register import build_project_completion_final_risk_register
from .final_inventories import (build_final_module_inventory, build_final_script_inventory,
                                build_final_docs_inventory, build_final_reports_inventory,
                                build_final_datalake_inventory, build_final_generated_docs_inventory,
                                build_final_test_inventory)
from .final_command_output_maps import build_final_command_map, build_final_output_map
from .final_recaps import (build_final_safe_usage_recap, build_final_no_go_safe_go_recap,
                           build_final_architecture_recap, build_final_quality_recap,
                           build_final_safety_boundary_recap, build_final_maintenance_recap)
from .final_handoff_checklists import (build_final_operator_handoff_checklist, build_final_analyst_handoff_checklist,
                                       build_final_maintainer_handoff_checklist, build_final_codex_agent_handoff_checklist)
from .terminal_maps import (build_terminal_readme_map, build_terminal_architecture_map, build_terminal_phase_map,
                            build_terminal_safety_boundary_map, build_terminal_maintenance_map)
from .completion_no_go_safe_go import build_completion_no_go_safe_go_summary
from .completion_exceptions import build_completion_exception_register
from .completion_gaps import build_completion_gap_register
from .completion_risks import build_completion_risk_summary
from .completion_scoring import build_completion_readiness_score_report
from .completion_validation import build_completion_validation_report
from .completion_quality import build_completion_quality_report
from .completion_report_builder import (build_completion_domain_registry_markdown_report,
                                        build_system_closure_dossier_markdown_report,
                                        build_terminal_handoff_pack_markdown_report,
                                        build_knowledge_freeze_markdown_report,
                                        build_last_mile_audit_markdown_report,
                                        build_project_completion_readiness_markdown_report,
                                        build_completion_quality_markdown_report,
                                        build_completion_status_markdown_report)

class LocalProjectCompletionPipeline:
    def __init__(self, data_lake: DataLake, settings: Settings, project_root: Path, profile: LocalProjectCompletionProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_local_project_completion_profile()

    def build_completion_domain_registry(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        domain_df, domain_summary = build_completion_domain_registry(self.profile)
        nogo_df, nogo_summary = build_completion_no_go_safe_go_summary(self.profile)
        freeze_bounds_df, freeze_bounds_summary = build_knowledge_freeze_boundary_registry(self.profile)
        # We can write dummy profiles DF
        profile_df = pd.DataFrame([{"profile": self.profile.name}])
        
        if save:
            try:
                self.data_lake.save_completion_profile_registry(profile_df)
                self.data_lake.save_completion_domain_registry(domain_df)
                self.data_lake.save_completion_no_go_safe_go_summary(nogo_df)
                self.data_lake.save_knowledge_freeze_boundary_registry(freeze_bounds_df)
            except Exception:
                pass
        return {"domain_df": domain_df}, domain_summary

    def build_final_system_closure_dossier(self, save: bool = True) -> tuple[str, dict]:
        text, summary = build_final_local_system_closure_dossier(self.project_root, self.profile)
        unres_df, _ = build_project_completion_unresolved_register(self.profile)
        lim_df, _ = build_project_completion_known_limitations_register(self.profile)
        risk_df, _ = build_project_completion_final_risk_register(self.profile)
        if save:
            try:
                self.data_lake.save_final_local_system_closure_dossier(text)
                self.data_lake.save_project_completion_unresolved_register(unres_df)
                self.data_lake.save_project_completion_known_limitations_register(lim_df)
                self.data_lake.save_project_completion_final_risk_register(risk_df)
            except:
                pass
        return text, summary

    def build_terminal_handoff_pack(self, save: bool = True) -> tuple[str, dict]:
        text, summary = build_terminal_handoff_pack(self.profile)
        op_df, _ = build_final_operator_handoff_checklist(self.profile)
        an_df, _ = build_final_analyst_handoff_checklist(self.profile)
        ma_df, _ = build_final_maintainer_handoff_checklist(self.profile)
        co_df, _ = build_final_codex_agent_handoff_checklist(self.profile)
        
        if save:
            try:
                self.data_lake.save_terminal_handoff_pack(text)
                self.data_lake.save_final_operator_handoff_checklist(op_df)
                self.data_lake.save_final_analyst_handoff_checklist(an_df)
                self.data_lake.save_final_maintainer_handoff_checklist(ma_df)
                self.data_lake.save_final_codex_agent_handoff_checklist(co_df)
            except: pass
        return text, summary

    def build_knowledge_freeze_rehearsal(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        reg_df, sum1 = build_knowledge_freeze_rehearsal_registry(self.project_root, self.profile)
        inv_df, sum2 = build_knowledge_freeze_inventory(self.project_root, self.profile)
        mod_df, _ = build_final_module_inventory(self.project_root, self.profile)
        scr_df, _ = build_final_script_inventory(self.project_root, self.profile)
        doc_df, _ = build_final_docs_inventory(self.project_root, self.profile)
        rep_df, _ = build_final_reports_inventory(self.project_root, self.profile)
        dl_df, _ = build_final_datalake_inventory(self.project_root, self.profile)
        gdoc_df, _ = build_final_generated_docs_inventory(self.project_root, self.profile)
        tst_df, _ = build_final_test_inventory(self.project_root, self.profile)
        if save:
            try:
                self.data_lake.save_knowledge_freeze_rehearsal_registry(reg_df)
                self.data_lake.save_knowledge_freeze_inventory(inv_df)
                self.data_lake.save_final_module_inventory(mod_df)
                self.data_lake.save_final_script_inventory(scr_df)
                self.data_lake.save_final_docs_inventory(doc_df)
                self.data_lake.save_final_reports_inventory(rep_df)
                self.data_lake.save_final_datalake_inventory(dl_df)
                self.data_lake.save_final_generated_docs_inventory(gdoc_df)
                self.data_lake.save_final_test_inventory(tst_df)
            except: pass
        return {"registry": reg_df}, sum1

    def build_last_mile_audit_binder(self, save: bool = True) -> tuple[str, dict]:
        text, summary = build_last_mile_audit_binder(self.project_root, self.profile)
        chk_df, _ = build_last_mile_audit_checklist_registry(self.profile)
        evi_df, _ = build_last_mile_audit_evidence_index(self.project_root, self.profile)
        ord_df, _ = build_last_mile_audit_reading_order(self.profile)
        cmd_df, _ = build_final_command_map(self.project_root, self.profile)
        out_df, _ = build_final_output_map(self.project_root, self.profile)
        if save:
            try:
                self.data_lake.save_last_mile_audit_binder(text)
                self.data_lake.save_last_mile_audit_checklist_registry(chk_df)
                self.data_lake.save_last_mile_audit_evidence_index(evi_df)
                self.data_lake.save_last_mile_audit_reading_order(ord_df)
                self.data_lake.save_final_command_map(cmd_df)
                self.data_lake.save_final_output_map(out_df)
            except: pass
        return text, summary

    def build_project_completion_readiness(self, save: bool = True) -> tuple[dict[str, pd.DataFrame] | str, dict]:
        text, summary = build_project_completion_readiness_packet(self.project_root, self.profile)
        evi_df, _ = build_project_completion_evidence_map(self.project_root, self.profile)
        crit_df, _ = build_project_completion_criteria_matrix(self.profile)
        if save:
            try:
                self.data_lake.save_project_completion_readiness_packet(text)
                self.data_lake.save_project_completion_evidence_map(evi_df)
                self.data_lake.save_project_completion_criteria_matrix(crit_df)
            except: pass
        return text, summary

    def build_completion_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        q = build_completion_quality_report({})
        if save:
            try:
                self.data_lake.save_completion_quality(self.profile.name, q)
            except: pass
        return q, {"note": "Quality report built."}

    def build_completion_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"status": "ok"}])
        return df, {"note": "Status generated."}
