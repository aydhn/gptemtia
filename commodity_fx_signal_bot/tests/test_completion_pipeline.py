from pathlib import Path
from local_project_completion.completion_pipeline import LocalProjectCompletionPipeline
from local_project_completion.completion_config import get_default_local_project_completion_profile

class MockDataLake:
    def save_completion_profile_registry(self, df, summary=None): pass
    def save_completion_domain_registry(self, df, summary=None): pass
    def save_completion_no_go_safe_go_summary(self, df, summary=None): pass
    def save_knowledge_freeze_boundary_registry(self, df, summary=None): pass
    def save_final_local_system_closure_dossier(self, text, summary=None): pass
    def save_project_completion_unresolved_register(self, df, summary=None): pass
    def save_project_completion_known_limitations_register(self, df, summary=None): pass
    def save_project_completion_final_risk_register(self, df, summary=None): pass
    def save_terminal_handoff_pack(self, text, summary=None): pass
    def save_final_operator_handoff_checklist(self, df, summary=None): pass
    def save_final_analyst_handoff_checklist(self, df, summary=None): pass
    def save_final_maintainer_handoff_checklist(self, df, summary=None): pass
    def save_final_codex_agent_handoff_checklist(self, df, summary=None): pass
    def save_knowledge_freeze_rehearsal_registry(self, df, summary=None): pass
    def save_knowledge_freeze_inventory(self, df, summary=None): pass
    def save_final_module_inventory(self, df, summary=None): pass
    def save_final_script_inventory(self, df, summary=None): pass
    def save_final_docs_inventory(self, df, summary=None): pass
    def save_final_reports_inventory(self, df, summary=None): pass
    def save_final_datalake_inventory(self, df, summary=None): pass
    def save_final_generated_docs_inventory(self, df, summary=None): pass
    def save_final_test_inventory(self, df, summary=None): pass
    def save_last_mile_audit_binder(self, text, summary=None): pass
    def save_last_mile_audit_checklist_registry(self, df, summary=None): pass
    def save_last_mile_audit_evidence_index(self, df, summary=None): pass
    def save_last_mile_audit_reading_order(self, df, summary=None): pass
    def save_final_command_map(self, df, summary=None): pass
    def save_final_output_map(self, df, summary=None): pass
    def save_project_completion_readiness_packet(self, text, summary=None): pass
    def save_project_completion_evidence_map(self, df, summary=None): pass
    def save_project_completion_criteria_matrix(self, df, summary=None): pass
    def save_completion_quality(self, name, q): pass

def test_pipeline():
    prof = get_default_local_project_completion_profile()
    pipe = LocalProjectCompletionPipeline(MockDataLake(), None, Path("."), prof)
    
    pipe.build_completion_domain_registry()
    pipe.build_final_system_closure_dossier()
    pipe.build_terminal_handoff_pack()
    pipe.build_knowledge_freeze_rehearsal()
    pipe.build_last_mile_audit_binder()
    pipe.build_project_completion_readiness()
    pipe.build_completion_quality_report()
    pipe.build_completion_status()
