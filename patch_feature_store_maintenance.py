import re

with open("commodity_fx_signal_bot/ml/feature_store.py", "r") as f:
    content = f.read()

maintenance_methods = """
    # --- MAINTENANCE SUPPORT ---
    def load_storage_inventory(self) -> pd.DataFrame:
        return self.data_lake.load_storage_inventory()

    def load_retention_policies(self) -> pd.DataFrame:
        return self.data_lake.load_retention_policies()

    def load_cleanup_candidates(self) -> pd.DataFrame:
        return self.data_lake.load_cleanup_candidates()

    def load_cleanup_dry_run_plan(self) -> pd.DataFrame:
        return self.data_lake.load_cleanup_dry_run_plan()

    def load_archive_candidates(self) -> pd.DataFrame:
        return self.data_lake.load_archive_candidates()

    def load_archive_manifest(self, archive_id: str) -> dict:
        return self.data_lake.load_archive_manifest(archive_id)

    def load_archive_dry_run_plan(self) -> pd.DataFrame:
        return self.data_lake.load_archive_dry_run_plan()

    def load_report_rotation_plan(self) -> pd.DataFrame:
        return self.data_lake.load_report_rotation_plan()

    def load_log_rotation_plan(self) -> pd.DataFrame:
        return self.data_lake.load_log_rotation_plan()

    def load_cache_pruning_plan(self) -> pd.DataFrame:
        return self.data_lake.load_cache_pruning_plan()

    def load_duplicate_artifact_report(self) -> pd.DataFrame:
        return self.data_lake.load_duplicate_artifact_report()

    def load_stale_artifact_report(self) -> pd.DataFrame:
        return self.data_lake.load_stale_artifact_report()

    def load_large_artifact_report(self) -> pd.DataFrame:
        return self.data_lake.load_large_artifact_report()

    def load_storage_growth_report(self) -> pd.DataFrame:
        return self.data_lake.load_storage_growth_report()

    def load_storage_lifecycle_health(self) -> pd.DataFrame:
        return self.data_lake.load_storage_lifecycle_health()

    def load_maintenance_quality(self, profile_name: str | None = None) -> dict:
        if profile_name is None:
            profile_name = "balanced_local_maintenance"
        return self.data_lake.load_maintenance_quality(profile_name)

    def load_maintenance_report(self, profile_name: str | None = None) -> dict:
        if profile_name is None:
            profile_name = "balanced_local_maintenance"
        return self.data_lake.load_maintenance_report(profile_name)

    def list_available_maintenance_reports(self) -> dict:
        df = self.data_lake.list_maintenance_reports()
        return {"count": len(df), "files": df["file_name"].tolist() if not df.empty else []}
"""

if "def load_storage_inventory" not in content:
    # Just append to the class at the end
    content = re.sub(r'(\s*)$', r'\n\n' + maintenance_methods, content)
    with open("commodity_fx_signal_bot/ml/feature_store.py", "w") as f:
        f.write(content)
    print("feature_store.py patched")
else:
    print("feature_store.py already patched")
