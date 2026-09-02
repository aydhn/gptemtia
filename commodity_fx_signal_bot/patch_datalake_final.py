import os

code = '''
    def save_training_domain_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "domains" / "training_domain_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_training_domain_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "domains" / "training_domain_registry.parquet"
        return self._load_parquet(path)

    def save_role_based_onboarding_paths(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "onboarding" / "role_based_onboarding_paths.parquet"
        self._save_parquet(df, path)
        return path
    def load_role_based_onboarding_paths(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "onboarding" / "role_based_onboarding_paths.parquet"
        return self._load_parquet(path)

    def save_glossary_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "glossary" / "glossary_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_glossary_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "glossary" / "glossary_registry.parquet"
        return self._load_parquet(path)

    def save_concept_map_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "concepts" / "concept_map_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_concept_map_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "concepts" / "concept_map_registry.parquet"
        return self._load_parquet(path)

    def save_local_training_report(self, profile_name, report, markdown=None):
        path = self.paths.LAKE_LOCAL_TRAINING_REPORTS_DIR / f"{profile_name}_report.json"
        self._save_json(report, path)
        return path
    def load_local_training_report(self, profile_name):
        path = self.paths.LAKE_LOCAL_TRAINING_REPORTS_DIR / f"{profile_name}_report.json"
        return self._load_json(path)

    def save_first_week_operator_curriculum(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "curriculum" / "first_week_operator_curriculum.parquet"
        self._save_parquet(df, path)
        return path
    def load_first_week_operator_curriculum(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "curriculum" / "first_week_operator_curriculum.parquet"
        return self._load_parquet(path)

    def save_knowledge_transfer_checklist(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "checklists" / "knowledge_transfer_checklist.parquet"
        self._save_parquet(df, path)
        return path
    def load_knowledge_transfer_checklist(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "checklists" / "knowledge_transfer_checklist.parquet"
        return self._load_parquet(path)

    def save_training_assessment_dry_run(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "assessment" / "training_assessment_dry_run.parquet"
        self._save_parquet(df, path)
        return path
    def load_training_assessment_dry_run(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "assessment" / "training_assessment_dry_run.parquet"
        return self._load_parquet(path)

    def save_faq_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "faq" / "faq_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_faq_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "faq" / "faq_registry.parquet"
        return self._load_parquet(path)

    def save_guided_walkthrough_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "walkthroughs" / "guided_walkthrough_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_guided_walkthrough_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "walkthroughs" / "guided_walkthrough_registry.parquet"
        return self._load_parquet(path)

    def save_local_walkthrough_lessons(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "walkthroughs" / "local_walkthrough_lessons.parquet"
        self._save_parquet(df, path)
        return path
    def load_local_walkthrough_lessons(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "walkthroughs" / "local_walkthrough_lessons.parquet"
        return self._load_parquet(path)

    def save_safe_command_lesson_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "commands" / "safe_command_lesson_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_safe_command_lesson_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "commands" / "safe_command_lesson_registry.parquet"
        return self._load_parquet(path)

    def save_report_reading_lesson_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "reports" / "report_reading_lesson_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_report_reading_lesson_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "reports" / "report_reading_lesson_registry.parquet"
        return self._load_parquet(path)

    def save_datalake_reading_lesson_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "datalake" / "datalake_reading_lesson_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_datalake_reading_lesson_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "datalake" / "datalake_reading_lesson_registry.parquet"
        return self._load_parquet(path)

    def save_cross_layer_lesson_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "cross_layer" / "cross_layer_lesson_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_cross_layer_lesson_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "cross_layer" / "cross_layer_lesson_registry.parquet"
        return self._load_parquet(path)

    def save_troubleshooting_lesson_registry(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "troubleshooting" / "troubleshooting_lesson_registry.parquet"
        self._save_parquet(df, path)
        return path
    def load_troubleshooting_lesson_registry(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "troubleshooting" / "troubleshooting_lesson_registry.parquet"
        return self._load_parquet(path)

    def save_operator_training_pack(self, text, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "operator_training_pack.txt"
        self._save_text(text, path)
        return path
    def load_operator_training_pack(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "operator_training_pack.txt"
        return self._load_text(path)

    def save_analyst_training_pack(self, text, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "analyst_training_pack.txt"
        self._save_text(text, path)
        return path
    def load_analyst_training_pack(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "analyst_training_pack.txt"
        return self._load_text(path)

    def save_developer_training_pack(self, text, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "developer_training_pack.txt"
        self._save_text(text, path)
        return path
    def load_developer_training_pack(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "developer_training_pack.txt"
        return self._load_text(path)

    def save_safe_usage_training_pack(self, text, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "safe_usage_training_pack.txt"
        self._save_text(text, path)
        return path
    def load_safe_usage_training_pack(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "safe_usage_training_pack.txt"
        return self._load_text(path)

    def save_non_use_policy_training_pack(self, text, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "non_use_policy_training_pack.txt"
        self._save_text(text, path)
        return path
    def load_non_use_policy_training_pack(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "non_use_policy_training_pack.txt"
        return self._load_text(path)

    def save_handover_education_binder(self, text, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "handover_education_binder.txt"
        self._save_text(text, path)
        return path
    def load_handover_education_binder(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "packs" / "handover_education_binder.txt"
        return self._load_text(path)

    def save_training_gap_register(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "gaps" / "training_gap_register.parquet"
        self._save_parquet(df, path)
        return path
    def load_training_gap_register(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "gaps" / "training_gap_register.parquet"
        return self._load_parquet(path)

    def save_training_risk_summary(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "risks" / "training_risk_summary.parquet"
        self._save_parquet(df, path)
        return path
    def load_training_risk_summary(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "risks" / "training_risk_summary.parquet"
        return self._load_parquet(path)

    def save_training_validation_report(self, df, summary=None):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "validation" / "training_validation_report.parquet"
        self._save_parquet(df, path)
        return path
    def load_training_validation_report(self):
        path = self.paths.LAKE_LOCAL_TRAINING_DIR / "validation" / "training_validation_report.parquet"
        return self._load_parquet(path)

    def save_training_quality(self, profile_name, quality):
        path = self.paths.LAKE_LOCAL_TRAINING_QUALITY_DIR / f"{profile_name}_quality.json"
        self._save_json(quality, path)
        return path
    def load_training_quality(self, profile_name):
        path = self.paths.LAKE_LOCAL_TRAINING_QUALITY_DIR / f"{profile_name}_quality.json"
        return self._load_json(path)

    def list_local_training_reports(self):
        import pandas as pd
        if not self.paths.LAKE_LOCAL_TRAINING_REPORTS_DIR.exists():
            return pd.DataFrame()
        files = list(self.paths.LAKE_LOCAL_TRAINING_REPORTS_DIR.glob("*_report.json"))
        return pd.DataFrame([{"report_file": f.name} for f in files])
'''

with open("data/storage/data_lake.py", "a", encoding="utf-8") as file:
    file.write(code)

