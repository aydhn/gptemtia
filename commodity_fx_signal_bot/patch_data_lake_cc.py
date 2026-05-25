import re

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

cc_methods = """
    # Phase 50: Command Center Methods
    def save_command_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_REGISTRY_DIR / "command_registry.parquet", summary)

    def load_command_registry(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_REGISTRY_DIR / "command_registry.parquet")

    def save_guided_workflows(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_WORKFLOWS_DIR / "guided_workflows.parquet", summary)

    def load_guided_workflows(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_WORKFLOWS_DIR / "guided_workflows.parquet")

    def save_safe_runbooks(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_RUNBOOKS_DIR / "safe_runbooks.parquet", summary)

    def load_safe_runbooks(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_RUNBOOKS_DIR / "safe_runbooks.parquet")

    def save_command_dry_run_plan(self, plan_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_DRY_RUN_PLANS_DIR / f"{plan_name}.parquet", summary)

    def load_command_dry_run_plan(self, plan_name: str) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_DRY_RUN_PLANS_DIR / f"{plan_name}.parquet")

    def save_interactive_query_flow(self, flow_name: str, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_QUERY_FLOWS_DIR / f"{flow_name}.parquet", summary)

    def load_interactive_query_flow(self, flow_name: str) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_QUERY_FLOWS_DIR / f"{flow_name}.parquet")

    def save_project_status(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_PROJECT_STATUS_DIR / "project_status.parquet", summary)

    def load_project_status(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_PROJECT_STATUS_DIR / "project_status.parquet")

    def save_module_health(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_MODULE_HEALTH_DIR / "module_health.parquet", summary)

    def load_module_health(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_MODULE_HEALTH_DIR / "module_health.parquet")

    def save_script_availability_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_SCRIPT_DISCOVERY_DIR / "script_availability_matrix.parquet", summary)

    def load_script_availability_matrix(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_SCRIPT_DISCOVERY_DIR / "script_availability_matrix.parquet")

    def save_phase_coverage_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_PHASE_COVERAGE_DIR / "phase_coverage_matrix.parquet", summary)

    def load_phase_coverage_matrix(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_PHASE_COVERAGE_DIR / "phase_coverage_matrix.parquet")

    def save_project_consolidation_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        path = self.paths.LAKE_COMMAND_CENTER_CONSOLIDATION_DIR / f"{profile_name}_consolidation.json"
        with open(path, "w", encoding="utf-8") as f:
            json.update(report) if hasattr(json, "update") else json.dump(report, f, indent=4)
        return path

    def load_project_consolidation_report(self, profile_name: str) -> dict:
        path = self.paths.LAKE_COMMAND_CENTER_CONSOLIDATION_DIR / f"{profile_name}_consolidation.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_command_center_quality(self, profile_name: str, quality: dict) -> Path:
        path = self.paths.LAKE_COMMAND_CENTER_QUALITY_DIR / f"{profile_name}_quality.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=4)
        return path

    def load_command_center_quality(self, profile_name: str) -> dict:
        path = self.paths.LAKE_COMMAND_CENTER_QUALITY_DIR / f"{profile_name}_quality.json"
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_command_center_status(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_report(df, self.paths.LAKE_COMMAND_CENTER_DIR / "command_center_status.parquet", summary)

    def load_command_center_status(self) -> pd.DataFrame:
        return self._load_report(self.paths.LAKE_COMMAND_CENTER_DIR / "command_center_status.parquet")

    def list_command_center_reports(self) -> pd.DataFrame:
        data = []
        for p in self.paths.LAKE_COMMAND_CENTER_DIR.rglob("*.parquet"):
            data.append({"path": str(p), "type": "parquet"})
        for p in self.paths.LAKE_COMMAND_CENTER_DIR.rglob("*.json"):
            data.append({"path": str(p), "type": "json"})
        return pd.DataFrame(data)
"""

content = content.replace("class DataLake:", "class DataLake:\n" + cc_methods)

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
    f.write(content)
