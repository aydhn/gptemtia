def update_data_lake():
    file_path = "data/storage/data_lake.py"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_methods = """
    # --- Local Maintenance Integration ---
    def save_maintenance_domain_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_DOMAINS_DIR / "maintenance_domain_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_maintenance_domain_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_DOMAINS_DIR / "maintenance_domain_registry.parquet"
        return self._load_parquet(in_path)

    def save_maintenance_task_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_TASKS_DIR / "maintenance_task_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_maintenance_task_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_TASKS_DIR / "maintenance_task_registry.parquet"
        return self._load_parquet(in_path)

    def save_periodic_review_calendar(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CALENDAR_DIR / "periodic_review_calendar.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_periodic_review_calendar(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CALENDAR_DIR / "periodic_review_calendar.parquet"
        return self._load_parquet(in_path)

    def save_report_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "report_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_report_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "report_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_datalake_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "datalake_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_datalake_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "datalake_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_documentation_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "documentation_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_documentation_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "documentation_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_test_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "test_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_test_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "test_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_safety_security_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "safety_security_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_safety_security_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "safety_security_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_backup_packaging_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "backup_packaging_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_backup_packaging_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "backup_packaging_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_cross_layer_refresh_cadence_registry(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "cross_layer_refresh_cadence_registry.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_cross_layer_refresh_cadence_registry(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_CADENCE_DIR / "cross_layer_refresh_cadence_registry.parquet"
        return self._load_parquet(in_path)

    def save_dependency_aging_watch_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_DEPENDENCIES_DIR / "dependency_aging_watch_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_dependency_aging_watch_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_DEPENDENCIES_DIR / "dependency_aging_watch_report.parquet"
        return self._load_parquet(in_path)

    def save_dependency_review_checklist(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_DEPENDENCY_REVIEW_DIR / "dependency_review_checklist.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_dependency_review_checklist(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_DEPENDENCY_REVIEW_DIR / "dependency_review_checklist.parquet"
        return self._load_parquet(in_path)

    def save_deprecated_artifact_watch_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_ARTIFACTS_DIR / "deprecated_artifact_watch_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_deprecated_artifact_watch_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_ARTIFACTS_DIR / "deprecated_artifact_watch_report.parquet"
        return self._load_parquet(in_path)

    def save_stale_report_watch_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_REPORTS_DIR / "stale_report_watch_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_stale_report_watch_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_REPORTS_DIR / "stale_report_watch_report.parquet"
        return self._load_parquet(in_path)

    def save_stale_documentation_watch_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_DOCS_DIR / "stale_documentation_watch_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_stale_documentation_watch_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_DOCS_DIR / "stale_documentation_watch_report.parquet"
        return self._load_parquet(in_path)

    def save_stale_test_watch_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_TESTS_DIR / "stale_test_watch_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_stale_test_watch_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_STALE_TESTS_DIR / "stale_test_watch_report.parquet"
        return self._load_parquet(in_path)

    def save_manual_review_queue(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_MANUAL_REVIEW_DIR / "manual_review_queue.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_manual_review_queue(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_MANUAL_REVIEW_DIR / "manual_review_queue.parquet"
        return self._load_parquet(in_path)

    def save_maintenance_gap_register(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_GAPS_DIR / "maintenance_gap_register.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_maintenance_gap_register(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_GAPS_DIR / "maintenance_gap_register.parquet"
        return self._load_parquet(in_path)

    def save_maintenance_risk_summary(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_RISKS_DIR / "maintenance_risk_summary.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_maintenance_risk_summary(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_RISKS_DIR / "maintenance_risk_summary.parquet"
        return self._load_parquet(in_path)

    def save_sustainability_score_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_SCORING_DIR / "sustainability_score_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_sustainability_score_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_SCORING_DIR / "sustainability_score_report.parquet"
        return self._load_parquet(in_path)

    def save_operator_periodic_review_checklist(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_OPERATOR_CHECKLISTS_DIR / "operator_periodic_review_checklist.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_operator_periodic_review_checklist(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_OPERATOR_CHECKLISTS_DIR / "operator_periodic_review_checklist.parquet"
        return self._load_parquet(in_path)

    def save_monthly_review_template(self, text: str, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_TEMPLATES_DIR / "monthly_review_template.txt"
        self._save_text(text, out_path)
        return out_path

    def load_monthly_review_template(self) -> str:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_TEMPLATES_DIR / "monthly_review_template.txt"
        return self._load_text(in_path)

    def save_quarterly_review_template(self, text: str, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_TEMPLATES_DIR / "quarterly_review_template.txt"
        self._save_text(text, out_path)
        return out_path

    def load_quarterly_review_template(self) -> str:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_TEMPLATES_DIR / "quarterly_review_template.txt"
        return self._load_text(in_path)

    def save_refresh_command_plan(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_REFRESH_COMMANDS_DIR / "refresh_command_plan.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_refresh_command_plan(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_REFRESH_COMMANDS_DIR / "refresh_command_plan.parquet"
        return self._load_parquet(in_path)

    def save_maintenance_runbook(self, text: str, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_RUNBOOKS_DIR / "maintenance_runbook.txt"
        self._save_text(text, out_path)
        return out_path

    def load_maintenance_runbook(self) -> str:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_RUNBOOKS_DIR / "maintenance_runbook.txt"
        return self._load_text(in_path)

    def save_long_term_sustainability_binder(self, text: str, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_BINDERS_DIR / "long_term_sustainability_binder.txt"
        self._save_text(text, out_path)
        return out_path

    def load_long_term_sustainability_binder(self) -> str:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_BINDERS_DIR / "long_term_sustainability_binder.txt"
        return self._load_text(in_path)

    def save_maintenance_validation_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_VALIDATION_DIR / "maintenance_validation_report.parquet"
        self._save_parquet(df, out_path)
        return out_path

    def load_maintenance_validation_report(self) -> pd.DataFrame:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_VALIDATION_DIR / "maintenance_validation_report.parquet"
        return self._load_parquet(in_path)

    def save_maintenance_quality(self, profile_name: str, quality: dict) -> Path:
        out_path = self.paths.LAKE_LOCAL_MAINTENANCE_QUALITY_DIR / f"maintenance_quality_{profile_name}.json"
        self._save_json(quality, out_path)
        return out_path

    def load_maintenance_quality(self, profile_name: str) -> dict:
        in_path = self.paths.LAKE_LOCAL_MAINTENANCE_QUALITY_DIR / f"maintenance_quality_{profile_name}.json"
        return self._load_json(in_path)
"""
    if "def save_maintenance_domain_registry" not in content:
        # insert at the end before the last empty line or at the end
        content = content + "\n" + new_methods + "\n"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

update_data_lake()
