import re

with open("commodity_fx_signal_bot/ml/feature_store.py", "r") as f:
    content = f.read()

cc_methods = """
    # Phase 50: Command Center Methods
    def load_command_registry(self) -> pd.DataFrame:
        return self.data_lake.load_command_registry()

    def load_guided_workflows(self) -> pd.DataFrame:
        return self.data_lake.load_guided_workflows()

    def load_safe_runbooks(self) -> pd.DataFrame:
        return self.data_lake.load_safe_runbooks()

    def load_command_dry_run_plan(self, plan_name: str) -> pd.DataFrame:
        return self.data_lake.load_command_dry_run_plan(plan_name)

    def load_project_status(self) -> pd.DataFrame:
        return self.data_lake.load_project_status()

    def load_module_health(self) -> pd.DataFrame:
        return self.data_lake.load_module_health()

    def load_script_availability_matrix(self) -> pd.DataFrame:
        return self.data_lake.load_script_availability_matrix()

    def load_phase_coverage_matrix(self) -> pd.DataFrame:
        return self.data_lake.load_phase_coverage_matrix()

    def load_project_consolidation_report(self, profile_name: str | None = None) -> dict:
        profile = profile_name or "balanced_offline_command_center"
        return self.data_lake.load_project_consolidation_report(profile)

    def load_command_center_quality(self, profile_name: str | None = None) -> dict:
        profile = profile_name or "balanced_offline_command_center"
        return self.data_lake.load_command_center_quality(profile)

    def load_command_center_status(self) -> pd.DataFrame:
        return self.data_lake.load_command_center_status()

    def list_available_command_center_reports(self) -> dict:
        df = self.data_lake.list_command_center_reports()
        if df is None or df.empty:
            return {}
        return {"reports_found": len(df)}
"""

content = content.replace("class FeatureStore:", "class FeatureStore:\n" + cc_methods)

with open("commodity_fx_signal_bot/ml/feature_store.py", "w") as f:
    f.write(content)
