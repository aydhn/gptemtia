import re
from pathlib import Path

BASE_DIR = Path("commodity_fx_signal_bot")

# 1. Update data/storage/data_lake.py
dl_path = BASE_DIR / "data/storage/data_lake.py"
with open(dl_path, "r", encoding="utf-8") as f:
    dl_content = f.read()

dl_additions = """
    # --- PHASE 77: LOCAL ACCEPTANCE ---
    def save_acceptance_profile_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_profiles"] / "acceptance_profile_registry.parquet")

    def load_acceptance_profile_registry(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_profiles"] / "acceptance_profile_registry.parquet")

    def save_acceptance_domain_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_domains"] / "acceptance_domain_registry.parquet")

    def load_acceptance_domain_registry(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_domains"] / "acceptance_domain_registry.parquet")

    def save_final_acceptance_simulation_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_simulation"] / "final_acceptance_simulation_checklist.parquet")

    def load_final_acceptance_simulation_checklist(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_simulation"] / "final_acceptance_simulation_checklist.parquet")

    def save_independent_reviewer_pack(self, text: str, summary: dict | None = None) -> Path:
        path = self.paths["lake_local_acceptance_reviewer_pack"] / "independent_reviewer_pack.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: f.write(text)
        return path

    def load_independent_reviewer_pack(self) -> str:
        path = self.paths["lake_local_acceptance_reviewer_pack"] / "independent_reviewer_pack.txt"
        if not path.exists(): return ""
        with open(path, "r", encoding="utf-8") as f: return f.read()

    def save_reviewer_question_bank(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_questions"] / "reviewer_question_bank.parquet")

    def load_reviewer_question_bank(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_questions"] / "reviewer_question_bank.parquet")

    def save_reviewer_evidence_request_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_evidence_matrix"] / "reviewer_evidence_request_matrix.parquet")

    def load_reviewer_evidence_request_matrix(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_evidence_matrix"] / "reviewer_evidence_request_matrix.parquet")

    def save_audit_style_local_evidence_trail(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_evidence_trail"] / "audit_style_local_evidence_trail.parquet")

    def load_audit_style_local_evidence_trail(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_evidence_trail"] / "audit_style_local_evidence_trail.parquet")

    def save_evidence_output_trace_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_traces"] / "evidence_output_trace_matrix.parquet")

    def load_evidence_output_trace_matrix(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_traces"] / "evidence_output_trace_matrix.parquet")

    def save_evidence_test_trace_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_traces"] / "evidence_test_trace_matrix.parquet")

    def load_evidence_test_trace_matrix(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_traces"] / "evidence_test_trace_matrix.parquet")

    def save_evidence_doc_trace_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_traces"] / "evidence_doc_trace_matrix.parquet")

    def load_evidence_doc_trace_matrix(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_traces"] / "evidence_doc_trace_matrix.parquet")

    def save_evidence_safety_boundary_trace_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_traces"] / "evidence_safety_boundary_trace_matrix.parquet")

    def load_evidence_safety_boundary_trace_matrix(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_traces"] / "evidence_safety_boundary_trace_matrix.parquet")

    def save_signoff_rehearsal_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_signoff"] / "signoff_rehearsal_checklist.parquet")

    def load_signoff_rehearsal_checklist(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_signoff"] / "signoff_rehearsal_checklist.parquet")

    def save_signoff_rehearsal_binder(self, text: str, summary: dict | None = None) -> Path:
        path = self.paths["lake_local_acceptance_binders"] / "signoff_rehearsal_binder.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: f.write(text)
        return path

    def load_signoff_rehearsal_binder(self) -> str:
        path = self.paths["lake_local_acceptance_binders"] / "signoff_rehearsal_binder.txt"
        if not path.exists(): return ""
        with open(path, "r", encoding="utf-8") as f: return f.read()

    def save_final_verification_rehearsal_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_verification"] / "final_verification_rehearsal_plan.parquet")

    def load_final_verification_rehearsal_plan(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_verification"] / "final_verification_rehearsal_plan.parquet")

    def save_final_verification_scenario_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_verification"] / "final_verification_scenario_registry.parquet")

    def load_final_verification_scenario_registry(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_verification"] / "final_verification_scenario_registry.parquet")

    def save_acceptance_criteria_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_criteria"] / "acceptance_criteria_registry.parquet")

    def load_acceptance_criteria_registry(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_criteria"] / "acceptance_criteria_registry.parquet")

    def save_acceptance_exception_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_exceptions"] / "acceptance_exception_register.parquet")

    def load_acceptance_exception_register(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_exceptions"] / "acceptance_exception_register.parquet")

    def save_acceptance_no_go_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_no_go_safe_go"] / "acceptance_no_go_register.parquet")

    def load_acceptance_no_go_register(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_no_go_safe_go"] / "acceptance_no_go_register.parquet")

    def save_acceptance_safe_go_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_no_go_safe_go"] / "acceptance_safe_go_register.parquet")

    def load_acceptance_safe_go_register(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_no_go_safe_go"] / "acceptance_safe_go_register.parquet")

    def save_acceptance_no_go_safe_go_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_no_go_safe_go"] / "acceptance_no_go_safe_go_summary.parquet")

    def load_acceptance_no_go_safe_go_summary(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_no_go_safe_go"] / "acceptance_no_go_safe_go_summary.parquet")

    def save_independent_review_notes_template(self, text: str, summary: dict | None = None) -> Path:
        path = self.paths["lake_local_acceptance_templates"] / "independent_review_notes_template.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: f.write(text)
        return path

    def load_independent_review_notes_template(self) -> str:
        path = self.paths["lake_local_acceptance_templates"] / "independent_review_notes_template.txt"
        if not path.exists(): return ""
        with open(path, "r", encoding="utf-8") as f: return f.read()

    def save_acceptance_response_template(self, text: str, summary: dict | None = None) -> Path:
        path = self.paths["lake_local_acceptance_templates"] / "acceptance_response_template.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: f.write(text)
        return path

    def load_acceptance_response_template(self) -> str:
        path = self.paths["lake_local_acceptance_templates"] / "acceptance_response_template.txt"
        if not path.exists(): return ""
        with open(path, "r", encoding="utf-8") as f: return f.read()

    def save_final_verification_evidence_binder(self, text: str, summary: dict | None = None) -> Path:
        path = self.paths["lake_local_acceptance_binders"] / "final_verification_evidence_binder.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: f.write(text)
        return path

    def load_final_verification_evidence_binder(self) -> str:
        path = self.paths["lake_local_acceptance_binders"] / "final_verification_evidence_binder.txt"
        if not path.exists(): return ""
        with open(path, "r", encoding="utf-8") as f: return f.read()

    def save_acceptance_gap_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_gaps"] / "acceptance_gap_register.parquet")

    def load_acceptance_gap_register(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_gaps"] / "acceptance_gap_register.parquet")

    def save_acceptance_risk_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_risks"] / "acceptance_risk_summary.parquet")

    def load_acceptance_risk_summary(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_risks"] / "acceptance_risk_summary.parquet")

    def save_acceptance_readiness_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_scoring"] / "acceptance_readiness_score_report.parquet")

    def load_acceptance_readiness_score_report(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_scoring"] / "acceptance_readiness_score_report.parquet")

    def save_acceptance_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_dataset(df, self.paths["lake_local_acceptance_validation"] / "acceptance_validation_report.parquet")

    def load_acceptance_validation_report(self) -> pd.DataFrame:
        return self._load_dataset(self.paths["lake_local_acceptance_validation"] / "acceptance_validation_report.parquet")

    def save_acceptance_quality(self, profile_name: str, quality: dict) -> Path:
        import json
        path = self.paths["lake_local_acceptance_quality"] / f"{profile_name}_quality.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: json.dump(quality, f, indent=2)
        return path

    def load_acceptance_quality(self, profile_name: str) -> dict:
        import json
        path = self.paths["lake_local_acceptance_quality"] / f"{profile_name}_quality.json"
        if not path.exists(): return {}
        with open(path, "r", encoding="utf-8") as f: return json.load(f)

    def save_local_acceptance_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        import json
        path = self.paths["lake_local_acceptance"] / f"{profile_name}_report.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f: json.dump(report, f, indent=2)
        if markdown:
            md_path = self.paths["lake_local_acceptance"] / f"{profile_name}_report.md"
            with open(md_path, "w", encoding="utf-8") as f: f.write(markdown)
        return path

    def load_local_acceptance_report(self, profile_name: str) -> dict:
        import json
        path = self.paths["lake_local_acceptance"] / f"{profile_name}_report.json"
        if not path.exists(): return {}
        with open(path, "r", encoding="utf-8") as f: return json.load(f)

    def list_local_acceptance_reports(self) -> pd.DataFrame:
        import pandas as pd
        path = self.paths["lake_local_acceptance"]
        files = list(path.glob("*_report.json")) if path.exists() else []
        return pd.DataFrame([{"report": f.name} for f in files])
"""
if "save_acceptance_profile_registry" not in dl_content:
    with open(dl_path, "a", encoding="utf-8") as f:
        f.write(dl_additions)

# 2. Update ml/feature_store.py
fs_path = BASE_DIR / "ml/feature_store.py"
with open(fs_path, "r", encoding="utf-8") as f:
    fs_content = f.read()

fs_additions = """
    # --- PHASE 77: LOCAL ACCEPTANCE ---
    def load_acceptance_profile_registry(self) -> pd.DataFrame: return self.data_lake.load_acceptance_profile_registry()
    def load_acceptance_domain_registry(self) -> pd.DataFrame: return self.data_lake.load_acceptance_domain_registry()
    def load_final_acceptance_simulation_checklist(self) -> pd.DataFrame: return self.data_lake.load_final_acceptance_simulation_checklist()
    def load_independent_reviewer_pack(self) -> str: return self.data_lake.load_independent_reviewer_pack()
    def load_reviewer_question_bank(self) -> pd.DataFrame: return self.data_lake.load_reviewer_question_bank()
    def load_reviewer_evidence_request_matrix(self) -> pd.DataFrame: return self.data_lake.load_reviewer_evidence_request_matrix()
    def load_audit_style_local_evidence_trail(self) -> pd.DataFrame: return self.data_lake.load_audit_style_local_evidence_trail()
    def load_evidence_output_trace_matrix(self) -> pd.DataFrame: return self.data_lake.load_evidence_output_trace_matrix()
    def load_evidence_test_trace_matrix(self) -> pd.DataFrame: return self.data_lake.load_evidence_test_trace_matrix()
    def load_evidence_doc_trace_matrix(self) -> pd.DataFrame: return self.data_lake.load_evidence_doc_trace_matrix()
    def load_evidence_safety_boundary_trace_matrix(self) -> pd.DataFrame: return self.data_lake.load_evidence_safety_boundary_trace_matrix()
    def load_signoff_rehearsal_checklist(self) -> pd.DataFrame: return self.data_lake.load_signoff_rehearsal_checklist()
    def load_signoff_rehearsal_binder(self) -> str: return self.data_lake.load_signoff_rehearsal_binder()
    def load_final_verification_rehearsal_plan(self) -> pd.DataFrame: return self.data_lake.load_final_verification_rehearsal_plan()
    def load_final_verification_scenario_registry(self) -> pd.DataFrame: return self.data_lake.load_final_verification_scenario_registry()
    def load_acceptance_criteria_registry(self) -> pd.DataFrame: return self.data_lake.load_acceptance_criteria_registry()
    def load_acceptance_exception_register(self) -> pd.DataFrame: return self.data_lake.load_acceptance_exception_register()
    def load_acceptance_no_go_register(self) -> pd.DataFrame: return self.data_lake.load_acceptance_no_go_register()
    def load_acceptance_safe_go_register(self) -> pd.DataFrame: return self.data_lake.load_acceptance_safe_go_register()
    def load_acceptance_no_go_safe_go_summary(self) -> pd.DataFrame: return self.data_lake.load_acceptance_no_go_safe_go_summary()
    def load_independent_review_notes_template(self) -> str: return self.data_lake.load_independent_review_notes_template()
    def load_acceptance_response_template(self) -> str: return self.data_lake.load_acceptance_response_template()
    def load_final_verification_evidence_binder(self) -> str: return self.data_lake.load_final_verification_evidence_binder()
    def load_acceptance_gap_register(self) -> pd.DataFrame: return self.data_lake.load_acceptance_gap_register()
    def load_acceptance_risk_summary(self) -> pd.DataFrame: return self.data_lake.load_acceptance_risk_summary()
    def load_acceptance_readiness_score_report(self) -> pd.DataFrame: return self.data_lake.load_acceptance_readiness_score_report()
    def load_acceptance_validation_report(self) -> pd.DataFrame: return self.data_lake.load_acceptance_validation_report()
    def load_acceptance_quality(self, profile_name: str | None = None) -> dict: return self.data_lake.load_acceptance_quality(profile_name or "default")
    def load_local_acceptance_report(self, profile_name: str | None = None) -> dict: return self.data_lake.load_local_acceptance_report(profile_name or "default")
    def list_available_local_acceptance_reports(self) -> dict: return self.data_lake.list_local_acceptance_reports().to_dict("records")
"""
if "load_acceptance_profile_registry" not in fs_content:
    with open(fs_path, "a", encoding="utf-8") as f:
        f.write(fs_additions)

# 3. Update reports/report_builder.py
rb_path = BASE_DIR / "reports/report_builder.py"
with open(rb_path, "r", encoding="utf-8") as f:
    rb_content = f.read()

rb_additions = """
    # --- PHASE 77: LOCAL ACCEPTANCE ---
    def _acceptance_disclaimer(self) -> str:
        return "Bu çıktı offline/local final acceptance simulation ve verification rehearsal raporudur. Resmi audit, resmi sign-off, production release, compliance sertifikası, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n"

    def build_acceptance_domain_registry_text_report(self, summary: dict, domain_df: pd.DataFrame | None = None) -> str:
        return f"Acceptance Domain Registry\\n{self._acceptance_disclaimer()}\\nTotal domains: {summary.get('total_domains', 0)}\\n"

    def build_final_acceptance_simulation_text_report(self, summary: dict, checklist_df: pd.DataFrame | None = None) -> str:
        return f"Final Acceptance Simulation\\n{self._acceptance_disclaimer()}\\nTotal items: {summary.get('total_items', 0)}\\n"

    def build_independent_reviewer_pack_text_report(self, summary: dict, pack_text: str | None = None) -> str:
        return f"Independent Reviewer Pack\\n{self._acceptance_disclaimer()}\\n{pack_text or ''}\\n"

    def build_acceptance_evidence_trail_text_report(self, summary: dict, evidence_df: pd.DataFrame | None = None) -> str:
        return f"Audit-Style Local Evidence Trail\\n{self._acceptance_disclaimer()}\\nTotal evidence: {summary.get('total_evidence_items', 0)}\\n"

    def build_signoff_rehearsal_text_report(self, summary: dict, binder_text: str | None = None) -> str:
        return f"Sign-off Rehearsal Binder\\n{self._acceptance_disclaimer()}\\n{binder_text or ''}\\n"

    def build_acceptance_quality_text_report(self, summary: dict, quality: dict | None = None) -> str:
        return f"Acceptance Quality Report\\n{self._acceptance_disclaimer()}\\nPassed: {quality.get('passed', False) if quality else False}\\n"

    def build_acceptance_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        return f"Acceptance Status Report\\n{self._acceptance_disclaimer()}\\nStatus: OK\\n"
"""
if "build_acceptance_domain_registry_text_report" not in rb_content:
    with open(rb_path, "a", encoding="utf-8") as f:
        f.write(rb_additions)
