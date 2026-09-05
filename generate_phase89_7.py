import os
import re

def update_data_lake():
    path = "commodity_fx_signal_bot/data/storage/data_lake.py"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_methods = """
    # Local Long-Term Operations
    def save_longterm_profile_registry(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_profiles", "longterm_profile_registry")
    def load_longterm_profile_registry(self): return self._load_csv("local_longterm_operations_profiles", "longterm_profile_registry")
    def save_longterm_domain_registry(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_domains", "longterm_domain_registry")
    def load_longterm_domain_registry(self): return self._load_csv("local_longterm_operations_domains", "longterm_domain_registry")
    def save_final_local_longterm_operations_binder(self, text: str, summary=None):
        path = self.paths["local_longterm_operations_binder"] / "final_local_longterm_operations_binder.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path
    def load_final_local_longterm_operations_binder(self):
        path = self.paths["local_longterm_operations_binder"] / "final_local_longterm_operations_binder.md"
        return path.read_text(encoding="utf-8") if path.exists() else ""
    def save_yearly_review_calendar_registry(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_calendars", "yearly_review_calendar_registry")
    def load_yearly_review_calendar_registry(self): return self._load_csv("local_longterm_operations_calendars", "yearly_review_calendar_registry")
    def save_quarterly_review_calendar_registry(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_calendars", "quarterly_review_calendar_registry")
    def load_quarterly_review_calendar_registry(self): return self._load_csv("local_longterm_operations_calendars", "quarterly_review_calendar_registry")
    def save_monthly_maintenance_calendar_registry(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_calendars", "monthly_maintenance_calendar_registry")
    def load_monthly_maintenance_calendar_registry(self): return self._load_csv("local_longterm_operations_calendars", "monthly_maintenance_calendar_registry")
    def save_weekly_operator_review_calendar_registry(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_calendars", "weekly_operator_review_calendar_registry")
    def load_weekly_operator_review_calendar_registry(self): return self._load_csv("local_longterm_operations_calendars", "weekly_operator_review_calendar_registry")
    def save_lifecycle_maintenance_workbook(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_workbooks", "lifecycle_maintenance_workbook")
    def load_lifecycle_maintenance_workbook(self): return self._load_csv("local_longterm_operations_workbooks", "lifecycle_maintenance_workbook")
    def save_maintenance_cadence_registry(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_maintenance", "maintenance_cadence_registry")
    def load_maintenance_cadence_registry(self): return self._load_csv("local_longterm_operations_maintenance", "maintenance_cadence_registry")
    def save_maintenance_ownership_rehearsal_matrix(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_ownership", "maintenance_ownership_rehearsal_matrix")
    def load_maintenance_ownership_rehearsal_matrix(self): return self._load_csv("local_longterm_operations_ownership", "maintenance_ownership_rehearsal_matrix")
    def save_maintenance_evidence_checklist(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_evidence", "maintenance_evidence_checklist")
    def load_maintenance_evidence_checklist(self): return self._load_csv("local_longterm_operations_evidence", "maintenance_evidence_checklist")
    def save_longterm_output_retention_review_workbook(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_retention", "longterm_output_retention_review_workbook")
    def load_longterm_output_retention_review_workbook(self): return self._load_csv("local_longterm_operations_retention", "longterm_output_retention_review_workbook")
    def save_longterm_datalake_review_workbook(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_datalake_review", "longterm_datalake_review_workbook")
    def load_longterm_datalake_review_workbook(self): return self._load_csv("local_longterm_operations_datalake_review", "longterm_datalake_review_workbook")
    def save_longterm_generated_docs_review_workbook(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_generated_docs_review", "longterm_generated_docs_review_workbook")
    def load_longterm_generated_docs_review_workbook(self): return self._load_csv("local_longterm_operations_generated_docs_review", "longterm_generated_docs_review_workbook")
    def save_longterm_quality_review_workbook(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_quality_review", "longterm_quality_review_workbook")
    def load_longterm_quality_review_workbook(self): return self._load_csv("local_longterm_operations_quality_review", "longterm_quality_review_workbook")
    def save_longterm_safety_review_workbook(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_safety_review", "longterm_safety_review_workbook")
    def load_longterm_safety_review_workbook(self): return self._load_csv("local_longterm_operations_safety_review", "longterm_safety_review_workbook")
    def save_longterm_incident_redteam_governance_review_workbook(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_inc_redteam_gov_review", "longterm_incident_redteam_governance_review_workbook")
    def load_longterm_incident_redteam_governance_review_workbook(self): return self._load_csv("local_longterm_operations_inc_redteam_gov_review", "longterm_incident_redteam_governance_review_workbook")
    def save_deprecation_rehearsal_registry(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_deprecation", "deprecation_rehearsal_registry")
    def load_deprecation_rehearsal_registry(self): return self._load_csv("local_longterm_operations_deprecation", "deprecation_rehearsal_registry")
    def save_deprecation_candidate_registry(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_deprecation", "deprecation_candidate_registry")
    def load_deprecation_candidate_registry(self): return self._load_csv("local_longterm_operations_deprecation", "deprecation_candidate_registry")
    def save_non_deprecation_boundary_registry(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_deprecation", "non_deprecation_boundary_registry")
    def load_non_deprecation_boundary_registry(self): return self._load_csv("local_longterm_operations_deprecation", "non_deprecation_boundary_registry")
    def save_deprecation_decision_checklist(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_deprecation", "deprecation_decision_checklist")
    def load_deprecation_decision_checklist(self): return self._load_csv("local_longterm_operations_deprecation", "deprecation_decision_checklist")
    def save_deprecation_impact_rehearsal_matrix(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_deprecation", "deprecation_impact_rehearsal_matrix")
    def load_deprecation_impact_rehearsal_matrix(self): return self._load_csv("local_longterm_operations_deprecation", "deprecation_impact_rehearsal_matrix")
    def save_migration_readiness_rehearsal_registry(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_migration", "migration_readiness_rehearsal_registry")
    def load_migration_readiness_rehearsal_registry(self): return self._load_csv("local_longterm_operations_migration", "migration_readiness_rehearsal_registry")
    def save_migration_non_goals_registry(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_migration", "migration_non_goals_registry")
    def load_migration_non_goals_registry(self): return self._load_csv("local_longterm_operations_migration", "migration_non_goals_registry")
    def save_v1x_roadmap_governance_packet(self, text: str, summary=None):
        path = self.paths["local_longterm_operations_roadmap"] / "v1x_roadmap_governance_packet.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path
    def load_v1x_roadmap_governance_packet(self):
        path = self.paths["local_longterm_operations_roadmap"] / "v1x_roadmap_governance_packet.md"
        return path.read_text(encoding="utf-8") if path.exists() else ""
    def save_v1x_roadmap_candidate_registry(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_roadmap", "v1x_roadmap_candidate_registry")
    def load_v1x_roadmap_candidate_registry(self): return self._load_csv("local_longterm_operations_roadmap", "v1x_roadmap_candidate_registry")
    def save_v1x_roadmap_priority_matrix(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_roadmap", "v1x_roadmap_priority_matrix")
    def load_v1x_roadmap_priority_matrix(self): return self._load_csv("local_longterm_operations_roadmap", "v1x_roadmap_priority_matrix")
    def save_v1x_feature_intake_checklist(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_feature_intake", "v1x_feature_intake_checklist")
    def load_v1x_feature_intake_checklist(self): return self._load_csv("local_longterm_operations_feature_intake", "v1x_feature_intake_checklist")
    def save_v1x_change_control_rehearsal_ledger(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_change_control", "v1x_change_control_rehearsal_ledger")
    def load_v1x_change_control_rehearsal_ledger(self): return self._load_csv("local_longterm_operations_change_control", "v1x_change_control_rehearsal_ledger")
    def save_v1x_risk_benefit_review_matrix(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_risk_benefit", "v1x_risk_benefit_review_matrix")
    def load_v1x_risk_benefit_review_matrix(self): return self._load_csv("local_longterm_operations_risk_benefit", "v1x_risk_benefit_review_matrix")
    def save_v1x_roadmap_no_go_safe_go_summary(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_no_go_safe_go", "v1x_roadmap_no_go_safe_go_summary")
    def load_v1x_roadmap_no_go_safe_go_summary(self): return self._load_csv("local_longterm_operations_no_go_safe_go", "v1x_roadmap_no_go_safe_go_summary")
    def save_lifecycle_exception_register(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_exceptions", "lifecycle_exception_register")
    def load_lifecycle_exception_register(self): return self._load_csv("local_longterm_operations_exceptions", "lifecycle_exception_register")
    def save_lifecycle_gap_register(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_gaps", "lifecycle_gap_register")
    def load_lifecycle_gap_register(self): return self._load_csv("local_longterm_operations_gaps", "lifecycle_gap_register")
    def save_lifecycle_risk_summary(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_risks", "lifecycle_risk_summary")
    def load_lifecycle_risk_summary(self): return self._load_csv("local_longterm_operations_risks", "lifecycle_risk_summary")
    def save_lifecycle_readiness_score_report(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_scoring", "lifecycle_readiness_score_report")
    def load_lifecycle_readiness_score_report(self): return self._load_csv("local_longterm_operations_scoring", "lifecycle_readiness_score_report")
    def save_lifecycle_validation_report(self, df, summary=None): return self._save_csv_and_summary(df, summary, "local_longterm_operations_validation", "lifecycle_validation_report")
    def load_lifecycle_validation_report(self): return self._load_csv("local_longterm_operations_validation", "lifecycle_validation_report")
    
    def save_lifecycle_quality(self, profile_name: str, quality: dict):
        import json
        path = self.paths["local_longterm_operations_quality"] / f"{profile_name}_quality.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(quality, indent=2), encoding="utf-8")
        return path
        
    def load_lifecycle_quality(self, profile_name: str):
        import json
        path = self.paths["local_longterm_operations_quality"] / f"{profile_name}_quality.json"
        return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}

    def save_local_longterm_operations_report(self, profile_name: str, report: dict, markdown: str = None):
        import json
        path = self.paths["local_longterm_operations"] / f"{profile_name}_report.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        if markdown:
            md_path = self.paths["local_longterm_operations"] / f"{profile_name}_report.md"
            md_path.write_text(markdown, encoding="utf-8")
        return path
        
    def load_local_longterm_operations_report(self, profile_name: str):
        import json
        path = self.paths["local_longterm_operations"] / f"{profile_name}_report.json"
        return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}

    def list_local_longterm_operations_reports(self):
        reports = []
        if self.paths["local_longterm_operations"].exists():
            for p in self.paths["local_longterm_operations"].glob("*_report.json"):
                reports.append({"profile_name": p.stem.replace("_report", "")})
        import pandas as pd
        return pd.DataFrame(reports)
"""
    if "save_longterm_profile_registry" not in content:
        insert_idx = content.rfind("    # ---")
        if insert_idx == -1:
            insert_idx = len(content)
        content = content[:insert_idx] + new_methods + "\n" + content[insert_idx:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated data_lake.py")

def update_feature_store():
    path = "commodity_fx_signal_bot/ml/feature_store.py"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_methods = """
    # Local Long-Term Operations
    def load_longterm_profile_registry(self): return self.data_lake.load_longterm_profile_registry()
    def load_longterm_domain_registry(self): return self.data_lake.load_longterm_domain_registry()
    def load_final_local_longterm_operations_binder(self): return self.data_lake.load_final_local_longterm_operations_binder()
    def load_yearly_review_calendar_registry(self): return self.data_lake.load_yearly_review_calendar_registry()
    def load_quarterly_review_calendar_registry(self): return self.data_lake.load_quarterly_review_calendar_registry()
    def load_monthly_maintenance_calendar_registry(self): return self.data_lake.load_monthly_maintenance_calendar_registry()
    def load_weekly_operator_review_calendar_registry(self): return self.data_lake.load_weekly_operator_review_calendar_registry()
    def load_lifecycle_maintenance_workbook(self): return self.data_lake.load_lifecycle_maintenance_workbook()
    def load_maintenance_cadence_registry(self): return self.data_lake.load_maintenance_cadence_registry()
    def load_maintenance_ownership_rehearsal_matrix(self): return self.data_lake.load_maintenance_ownership_rehearsal_matrix()
    def load_maintenance_evidence_checklist(self): return self.data_lake.load_maintenance_evidence_checklist()
    def load_longterm_output_retention_review_workbook(self): return self.data_lake.load_longterm_output_retention_review_workbook()
    def load_longterm_datalake_review_workbook(self): return self.data_lake.load_longterm_datalake_review_workbook()
    def load_longterm_generated_docs_review_workbook(self): return self.data_lake.load_longterm_generated_docs_review_workbook()
    def load_longterm_quality_review_workbook(self): return self.data_lake.load_longterm_quality_review_workbook()
    def load_longterm_safety_review_workbook(self): return self.data_lake.load_longterm_safety_review_workbook()
    def load_longterm_incident_redteam_governance_review_workbook(self): return self.data_lake.load_longterm_incident_redteam_governance_review_workbook()
    def load_deprecation_rehearsal_registry(self): return self.data_lake.load_deprecation_rehearsal_registry()
    def load_deprecation_candidate_registry(self): return self.data_lake.load_deprecation_candidate_registry()
    def load_non_deprecation_boundary_registry(self): return self.data_lake.load_non_deprecation_boundary_registry()
    def load_deprecation_decision_checklist(self): return self.data_lake.load_deprecation_decision_checklist()
    def load_deprecation_impact_rehearsal_matrix(self): return self.data_lake.load_deprecation_impact_rehearsal_matrix()
    def load_migration_readiness_rehearsal_registry(self): return self.data_lake.load_migration_readiness_rehearsal_registry()
    def load_migration_non_goals_registry(self): return self.data_lake.load_migration_non_goals_registry()
    def load_v1x_roadmap_governance_packet(self): return self.data_lake.load_v1x_roadmap_governance_packet()
    def load_v1x_roadmap_candidate_registry(self): return self.data_lake.load_v1x_roadmap_candidate_registry()
    def load_v1x_roadmap_priority_matrix(self): return self.data_lake.load_v1x_roadmap_priority_matrix()
    def load_v1x_feature_intake_checklist(self): return self.data_lake.load_v1x_feature_intake_checklist()
    def load_v1x_change_control_rehearsal_ledger(self): return self.data_lake.load_v1x_change_control_rehearsal_ledger()
    def load_v1x_risk_benefit_review_matrix(self): return self.data_lake.load_v1x_risk_benefit_review_matrix()
    def load_v1x_roadmap_no_go_safe_go_summary(self): return self.data_lake.load_v1x_roadmap_no_go_safe_go_summary()
    def load_lifecycle_exception_register(self): return self.data_lake.load_lifecycle_exception_register()
    def load_lifecycle_gap_register(self): return self.data_lake.load_lifecycle_gap_register()
    def load_lifecycle_risk_summary(self): return self.data_lake.load_lifecycle_risk_summary()
    def load_lifecycle_readiness_score_report(self): return self.data_lake.load_lifecycle_readiness_score_report()
    def load_lifecycle_validation_report(self): return self.data_lake.load_lifecycle_validation_report()
    def load_lifecycle_quality(self, profile_name="balanced_local_longterm_operations"): return self.data_lake.load_lifecycle_quality(profile_name)
    def load_local_longterm_operations_report(self, profile_name="balanced_local_longterm_operations"): return self.data_lake.load_local_longterm_operations_report(profile_name)
    def list_available_local_longterm_operations_reports(self): return self.data_lake.list_local_longterm_operations_reports().to_dict('records')
"""
    if "load_longterm_profile_registry" not in content:
        insert_idx = content.rfind("    # ---")
        if insert_idx == -1:
            insert_idx = len(content)
        content = content[:insert_idx] + new_methods + "\n" + content[insert_idx:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated feature_store.py")

def update_report_builder():
    path = "commodity_fx_signal_bot/reports/report_builder.py"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_methods = """
    # Local Long-Term Operations
    def build_longterm_domain_registry_text_report(self, summary: dict, domain_df=None) -> str:
        return f"Long-Term Domain Registry\\n{summary}\\n\\nBu çıktı offline/local long-term operations rehearsal ve lifecycle roadmap governance raporudur. Gerçek production operations plan, official lifecycle policy, release commitment, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
        
    def build_operations_binder_text_report(self, summary: dict, binder_text: str = None) -> str:
        return f"Operations Binder\\n{binder_text or summary}\\n\\nBu çıktı offline/local long-term operations rehearsal ve lifecycle roadmap governance raporudur. Gerçek production operations plan, official lifecycle policy, release commitment, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
        
    def build_review_calendar_text_report(self, summary: dict, calendar_df=None) -> str:
        return f"Review Calendar\\n{summary}\\n\\nBu çıktı offline/local long-term operations rehearsal ve lifecycle roadmap governance raporudur. Gerçek production operations plan, official lifecycle policy, release commitment, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
        
    def build_lifecycle_workbook_text_report(self, summary: dict, workbook_df=None) -> str:
        return f"Lifecycle Workbook\\n{summary}\\n\\nBu çıktı offline/local long-term operations rehearsal ve lifecycle roadmap governance raporudur. Gerçek production operations plan, official lifecycle policy, release commitment, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
        
    def build_deprecation_rehearsal_text_report(self, summary: dict, deprecation_df=None) -> str:
        return f"Deprecation Rehearsal\\n{summary}\\n\\nBu çıktı offline/local long-term operations rehearsal ve lifecycle roadmap governance raporudur. Gerçek production operations plan, official lifecycle policy, release commitment, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
        
    def build_v1x_roadmap_governance_text_report(self, summary: dict, roadmap_text: str = None) -> str:
        return f"Roadmap Governance\\n{roadmap_text or summary}\\n\\nBu çıktı offline/local long-term operations rehearsal ve lifecycle roadmap governance raporudur. Gerçek production operations plan, official lifecycle policy, release commitment, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
        
    def build_lifecycle_quality_text_report(self, summary: dict, quality: dict = None) -> str:
        return f"Lifecycle Quality\\n{quality or summary}\\n\\nBu çıktı offline/local long-term operations rehearsal ve lifecycle roadmap governance raporudur. Gerçek production operations plan, official lifecycle policy, release commitment, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
        
    def build_lifecycle_status_report(self, status_df, summary: dict) -> str:
        return f"Lifecycle Status\\n{summary}\\n\\nBu çıktı offline/local long-term operations rehearsal ve lifecycle roadmap governance raporudur. Gerçek production operations plan, official lifecycle policy, release commitment, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
"""
    if "build_longterm_domain_registry_text_report" not in content:
        insert_idx = content.rfind("    # ---")
        if insert_idx == -1:
            insert_idx = len(content)
        content = content[:insert_idx] + new_methods + "\n" + content[insert_idx:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated report_builder.py")

if __name__ == "__main__":
    update_data_lake()
    update_feature_store()
    update_report_builder()
