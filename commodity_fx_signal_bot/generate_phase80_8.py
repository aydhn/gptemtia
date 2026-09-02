import os

def read_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path: str, content: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def insert_after_pattern(content: str, pattern: str, insertion: str) -> str:
    parts = content.split(pattern)
    if len(parts) > 1:
        return parts[0] + pattern + "\n" + insertion + parts[1]
    return content

# data_lake.py
dl_content = read_file("data/storage/data_lake.py")

dl_methods = """
    # Phase 80: Local Closure support
    def save_closure_profile_registry(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_PROFILES, "closure_profile_registry")

    def load_closure_profile_registry(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_PROFILES)

    def save_closure_domain_registry(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_DOMAINS, "closure_domain_registry")

    def load_closure_domain_registry(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_DOMAINS)

    def save_final_project_meta_review_report(self, text: str, summary: Optional[dict] = None) -> Path:
        return self._save_text(text, Paths.LAKE_CLOSURE_META_REVIEW, "final_project_meta_review_report")

    def load_final_project_meta_review_report(self) -> str:
        return self._load_latest_text(Paths.LAKE_CLOSURE_META_REVIEW)

    def save_lessons_learned_compendium(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_LESSONS_LEARNED, "lessons_learned_compendium")

    def load_lessons_learned_compendium(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_LESSONS_LEARNED)

    def save_future_roadmap_backlog(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_ROADMAP, "future_roadmap_backlog")

    def load_future_roadmap_backlog(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_ROADMAP)

    def save_future_phase_candidate_registry(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_FUTURE_PHASES, "future_phase_candidate_registry")

    def load_future_phase_candidate_registry(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_FUTURE_PHASES)

    def save_post_project_governance_rehearsal_guide(self, text: str, summary: Optional[dict] = None) -> Path:
        return self._save_text(text, Paths.LAKE_CLOSURE_GOVERNANCE, "post_project_governance_rehearsal_guide")

    def load_post_project_governance_rehearsal_guide(self) -> str:
        return self._load_latest_text(Paths.LAKE_CLOSURE_GOVERNANCE)

    def save_v1_local_closure_dossier(self, text: str, summary: Optional[dict] = None) -> Path:
        return self._save_text(text, Paths.LAKE_CLOSURE_DOSSIER, "v1_local_closure_dossier")

    def load_v1_local_closure_dossier(self) -> str:
        return self._load_latest_text(Paths.LAKE_CLOSURE_DOSSIER)

    def save_closure_executive_recap(self, text: str, summary: Optional[dict] = None) -> Path:
        return self._save_text(text, Paths.LAKE_CLOSURE_RECAPS, "closure_executive_recap")

    def load_closure_executive_recap(self) -> str:
        return self._load_latest_text(Paths.LAKE_CLOSURE_RECAPS)

    def save_closure_technical_recap(self, text: str, summary: Optional[dict] = None) -> Path:
        return self._save_text(text, Paths.LAKE_CLOSURE_RECAPS, "closure_technical_recap")

    def load_closure_technical_recap(self) -> str:
        return self._load_latest_text(Paths.LAKE_CLOSURE_RECAPS)

    def save_closure_safety_recap(self, text: str, summary: Optional[dict] = None) -> Path:
        return self._save_text(text, Paths.LAKE_CLOSURE_RECAPS, "closure_safety_recap")

    def load_closure_safety_recap(self) -> str:
        return self._load_latest_text(Paths.LAKE_CLOSURE_RECAPS)

    def save_closure_architecture_recap(self, text: str, summary: Optional[dict] = None) -> Path:
        return self._save_text(text, Paths.LAKE_CLOSURE_RECAPS, "closure_architecture_recap")

    def load_closure_architecture_recap(self) -> str:
        return self._load_latest_text(Paths.LAKE_CLOSURE_RECAPS)

    def save_closure_evidence_recap(self, text: str, summary: Optional[dict] = None) -> Path:
        return self._save_text(text, Paths.LAKE_CLOSURE_RECAPS, "closure_evidence_recap")

    def load_closure_evidence_recap(self) -> str:
        return self._load_latest_text(Paths.LAKE_CLOSURE_RECAPS)

    def save_closure_archival_provenance_recap(self, text: str, summary: Optional[dict] = None) -> Path:
        return self._save_text(text, Paths.LAKE_CLOSURE_RECAPS, "closure_archival_provenance_recap")

    def load_closure_archival_provenance_recap(self) -> str:
        return self._load_latest_text(Paths.LAKE_CLOSURE_RECAPS)

    def save_closure_delivery_acceptance_recap(self, text: str, summary: Optional[dict] = None) -> Path:
        return self._save_text(text, Paths.LAKE_CLOSURE_RECAPS, "closure_delivery_acceptance_recap")

    def load_closure_delivery_acceptance_recap(self) -> str:
        return self._load_latest_text(Paths.LAKE_CLOSURE_RECAPS)

    def save_closure_unresolved_items_register(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_UNRESOLVED, "closure_unresolved_items_register")

    def load_closure_unresolved_items_register(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_UNRESOLVED)

    def save_closure_open_questions_register(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_OPEN_QUESTIONS, "closure_open_questions_register")

    def load_closure_open_questions_register(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_OPEN_QUESTIONS)

    def save_closure_future_improvement_backlog(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_IMPROVEMENTS, "closure_future_improvement_backlog")

    def load_closure_future_improvement_backlog(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_IMPROVEMENTS)

    def save_closure_maintenance_calendar_rehearsal(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_MAINTENANCE, "closure_maintenance_calendar_rehearsal")

    def load_closure_maintenance_calendar_rehearsal(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_MAINTENANCE)

    def save_closure_ownership_matrix_rehearsal(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_OWNERSHIP, "closure_ownership_matrix_rehearsal")

    def load_closure_ownership_matrix_rehearsal(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_OWNERSHIP)

    def save_closure_decision_log(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_DECISIONS, "closure_decision_log")

    def load_closure_decision_log(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_DECISIONS)

    def save_closure_assumptions_register(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_ASSUMPTIONS, "closure_assumptions_register")

    def load_closure_assumptions_register(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_ASSUMPTIONS)

    def save_closure_known_limitations_register(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_LIMITATIONS, "closure_known_limitations_register")

    def load_closure_known_limitations_register(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_LIMITATIONS)

    def save_closure_no_go_safe_go_summary(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_NO_GO_SAFE_GO, "closure_no_go_safe_go_summary")

    def load_closure_no_go_safe_go_summary(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_NO_GO_SAFE_GO)

    def save_closure_handoff_aftercare_guide(self, text: str, summary: Optional[dict] = None) -> Path:
        return self._save_text(text, Paths.LAKE_CLOSURE_AFTERCARE, "closure_handoff_aftercare_guide")

    def load_closure_handoff_aftercare_guide(self) -> str:
        return self._load_latest_text(Paths.LAKE_CLOSURE_AFTERCARE)

    def save_closure_faq(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_FAQ, "closure_faq")

    def load_closure_faq(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_FAQ)

    def save_closure_exception_register(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_EXCEPTIONS, "closure_exception_register")

    def load_closure_exception_register(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_EXCEPTIONS)

    def save_closure_gap_register(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_GAPS, "closure_gap_register")

    def load_closure_gap_register(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_GAPS)

    def save_closure_risk_summary(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_RISKS, "closure_risk_summary")

    def load_closure_risk_summary(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_RISKS)

    def save_closure_readiness_score_report(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_SCORING, "closure_readiness_score_report")

    def load_closure_readiness_score_report(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_SCORING)

    def save_closure_validation_report(self, df: pd.DataFrame, summary: Optional[dict] = None) -> Path:
        return self._save_csv(df, Paths.LAKE_CLOSURE_VALIDATION, "closure_validation_report")

    def load_closure_validation_report(self) -> pd.DataFrame:
        return self._load_latest_csv(Paths.LAKE_CLOSURE_VALIDATION)

    def save_closure_quality(self, profile_name: str, quality: dict) -> Path:
        return self._save_json(quality, Paths.LAKE_CLOSURE_QUALITY, f"closure_quality_{profile_name}")

    def load_closure_quality(self, profile_name: str) -> dict:
        import json
        files = list(Paths.LAKE_CLOSURE_QUALITY.glob(f"closure_quality_{profile_name}_*.json"))
        if not files:
            return {}
        latest = max(files, key=os.path.getctime)
        with open(latest, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_local_closure_report(self, profile_name: str, report: dict, markdown: Optional[str] = None) -> Path:
        return self._save_json(report, Paths.LAKE_CLOSURE_QUALITY, f"local_closure_report_{profile_name}")

    def load_local_closure_report(self, profile_name: str) -> dict:
        import json
        files = list(Paths.LAKE_CLOSURE_QUALITY.glob(f"local_closure_report_{profile_name}_*.json"))
        if not files:
            return {}
        latest = max(files, key=os.path.getctime)
        with open(latest, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_local_closure_reports(self) -> pd.DataFrame:
        records = []
        for file in Paths.LAKE_CLOSURE_QUALITY.glob("local_closure_report_*.json"):
            records.append({"file": file.name, "created_at": file.stat().st_ctime})
        return pd.DataFrame(records)
"""

dl_content = insert_after_pattern(dl_content, "def _save_text(self, text: str, directory: Path, prefix: str) -> Path:", dl_methods)
write_file("data/storage/data_lake.py", dl_content)

fs_content = read_file("ml/feature_store.py")

fs_methods = """
    # Phase 80: Local Closure support
    def load_closure_profile_registry(self) -> pd.DataFrame:
        return self.data_lake.load_closure_profile_registry()

    def load_closure_domain_registry(self) -> pd.DataFrame:
        return self.data_lake.load_closure_domain_registry()

    def load_final_project_meta_review_report(self) -> str:
        return self.data_lake.load_final_project_meta_review_report()

    def load_lessons_learned_compendium(self) -> pd.DataFrame:
        return self.data_lake.load_lessons_learned_compendium()

    def load_future_roadmap_backlog(self) -> pd.DataFrame:
        return self.data_lake.load_future_roadmap_backlog()

    def load_future_phase_candidate_registry(self) -> pd.DataFrame:
        return self.data_lake.load_future_phase_candidate_registry()

    def load_post_project_governance_rehearsal_guide(self) -> str:
        return self.data_lake.load_post_project_governance_rehearsal_guide()

    def load_v1_local_closure_dossier(self) -> str:
        return self.data_lake.load_v1_local_closure_dossier()

    def load_closure_executive_recap(self) -> str:
        return self.data_lake.load_closure_executive_recap()

    def load_closure_technical_recap(self) -> str:
        return self.data_lake.load_closure_technical_recap()

    def load_closure_safety_recap(self) -> str:
        return self.data_lake.load_closure_safety_recap()

    def load_closure_architecture_recap(self) -> str:
        return self.data_lake.load_closure_architecture_recap()

    def load_closure_evidence_recap(self) -> str:
        return self.data_lake.load_closure_evidence_recap()

    def load_closure_archival_provenance_recap(self) -> str:
        return self.data_lake.load_closure_archival_provenance_recap()

    def load_closure_delivery_acceptance_recap(self) -> str:
        return self.data_lake.load_closure_delivery_acceptance_recap()

    def load_closure_unresolved_items_register(self) -> pd.DataFrame:
        return self.data_lake.load_closure_unresolved_items_register()

    def load_closure_open_questions_register(self) -> pd.DataFrame:
        return self.data_lake.load_closure_open_questions_register()

    def load_closure_future_improvement_backlog(self) -> pd.DataFrame:
        return self.data_lake.load_closure_future_improvement_backlog()

    def load_closure_maintenance_calendar_rehearsal(self) -> pd.DataFrame:
        return self.data_lake.load_closure_maintenance_calendar_rehearsal()

    def load_closure_ownership_matrix_rehearsal(self) -> pd.DataFrame:
        return self.data_lake.load_closure_ownership_matrix_rehearsal()

    def load_closure_decision_log(self) -> pd.DataFrame:
        return self.data_lake.load_closure_decision_log()

    def load_closure_assumptions_register(self) -> pd.DataFrame:
        return self.data_lake.load_closure_assumptions_register()

    def load_closure_known_limitations_register(self) -> pd.DataFrame:
        return self.data_lake.load_closure_known_limitations_register()

    def load_closure_no_go_safe_go_summary(self) -> pd.DataFrame:
        return self.data_lake.load_closure_no_go_safe_go_summary()

    def load_closure_handoff_aftercare_guide(self) -> str:
        return self.data_lake.load_closure_handoff_aftercare_guide()

    def load_closure_faq(self) -> pd.DataFrame:
        return self.data_lake.load_closure_faq()

    def load_closure_exception_register(self) -> pd.DataFrame:
        return self.data_lake.load_closure_exception_register()

    def load_closure_gap_register(self) -> pd.DataFrame:
        return self.data_lake.load_closure_gap_register()

    def load_closure_risk_summary(self) -> pd.DataFrame:
        return self.data_lake.load_closure_risk_summary()

    def load_closure_readiness_score_report(self) -> pd.DataFrame:
        return self.data_lake.load_closure_readiness_score_report()

    def load_closure_validation_report(self) -> pd.DataFrame:
        return self.data_lake.load_closure_validation_report()

    def load_closure_quality(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_closure_quality(profile_name or "balanced_local_closure")

    def load_local_closure_report(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_local_closure_report(profile_name or "balanced_local_closure")

    def list_available_local_closure_reports(self) -> dict:
        return self.data_lake.list_local_closure_reports().to_dict(orient="records")
"""

fs_content = insert_after_pattern(fs_content, "def __init__(self, data_lake: DataLake, settings: Settings):", fs_methods)
write_file("ml/feature_store.py", fs_content)
