import re
from pathlib import Path

# Update DataLake
datalake_path = "commodity_fx_signal_bot/data/storage/data_lake.py"
with open(datalake_path, "r") as f:
    dl_content = f.read()

dl_injection = """
    # Phase 61: Portable Packaging
    def save_environment_snapshot(self, snapshot: dict, packages_df: pd.DataFrame, summary: dict = None) -> Path:
        out = self.paths.LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR / "environment_snapshot.json"
        import json
        with open(out, "w", encoding="utf-8") as f:
            json.dump({"snapshot": snapshot, "summary": summary}, f, indent=2)
        packages_df.to_parquet(self.paths.LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR / "installed_packages.parquet")
        return out

    def load_environment_snapshot(self) -> dict:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR / "environment_snapshot.json"
        if out.exists():
            with open(out, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_installed_packages_snapshot(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out = self.paths.LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR / "installed_packages.parquet"
        df.to_parquet(out)
        return out

    def load_installed_packages_snapshot(self) -> pd.DataFrame:
        out = self.paths.LAKE_PORTABLE_PACKAGING_ENVIRONMENT_DIR / "installed_packages.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_dependency_inventory(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out = self.paths.LAKE_PORTABLE_PACKAGING_DEPENDENCIES_DIR / "dependency_inventory.parquet"
        df.to_parquet(out)
        return out

    def load_dependency_inventory(self) -> pd.DataFrame:
        out = self.paths.LAKE_PORTABLE_PACKAGING_DEPENDENCIES_DIR / "dependency_inventory.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_requirements_export_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out = self.paths.LAKE_PORTABLE_PACKAGING_REQUIREMENTS_DIR / "requirements_export.parquet"
        df.to_parquet(out)
        return out

    def load_requirements_export_report(self) -> pd.DataFrame:
        out = self.paths.LAKE_PORTABLE_PACKAGING_REQUIREMENTS_DIR / "requirements_export.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_install_verification_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out = self.paths.LAKE_PORTABLE_PACKAGING_INSTALL_VERIFICATION_DIR / "install_verification.parquet"
        df.to_parquet(out)
        return out

    def load_install_verification_report(self) -> pd.DataFrame:
        out = self.paths.LAKE_PORTABLE_PACKAGING_INSTALL_VERIFICATION_DIR / "install_verification.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_import_verification_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out = self.paths.LAKE_PORTABLE_PACKAGING_IMPORT_VERIFICATION_DIR / "import_verification.parquet"
        df.to_parquet(out)
        return out

    def load_import_verification_report(self) -> pd.DataFrame:
        out = self.paths.LAKE_PORTABLE_PACKAGING_IMPORT_VERIFICATION_DIR / "import_verification.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_script_verification_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out = self.paths.LAKE_PORTABLE_PACKAGING_SCRIPT_VERIFICATION_DIR / "script_verification.parquet"
        df.to_parquet(out)
        return out

    def load_script_verification_report(self) -> pd.DataFrame:
        out = self.paths.LAKE_PORTABLE_PACKAGING_SCRIPT_VERIFICATION_DIR / "script_verification.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_config_template_verification(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out = self.paths.LAKE_PORTABLE_PACKAGING_CONFIG_VERIFICATION_DIR / "config_verification.parquet"
        df.to_parquet(out)
        return out

    def load_config_template_verification(self) -> pd.DataFrame:
        out = self.paths.LAKE_PORTABLE_PACKAGING_CONFIG_VERIFICATION_DIR / "config_verification.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_bundle_artifact_inventory(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out = self.paths.LAKE_PORTABLE_PACKAGING_BUNDLE_MANIFEST_DIR / "bundle_artifact_inventory.parquet"
        df.to_parquet(out)
        return out

    def load_bundle_artifact_inventory(self) -> pd.DataFrame:
        out = self.paths.LAKE_PORTABLE_PACKAGING_BUNDLE_MANIFEST_DIR / "bundle_artifact_inventory.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_portable_bundle_manifest(self, manifest: dict) -> Path:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_BUNDLE_MANIFEST_DIR / "portable_bundle_manifest.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        return out

    def load_portable_bundle_manifest(self) -> dict:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_BUNDLE_MANIFEST_DIR / "portable_bundle_manifest.json"
        if out.exists():
            with open(out, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_archive_manifest(self, manifest: dict) -> Path:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_ARCHIVE_MANIFEST_DIR / "archive_manifest.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        return out

    def load_archive_manifest(self) -> dict:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_ARCHIVE_MANIFEST_DIR / "archive_manifest.json"
        if out.exists():
            with open(out, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_source_policy(self, policy_name: str, df: pd.DataFrame, summary: dict = None) -> Path:
        out = self.paths.LAKE_PORTABLE_PACKAGING_SOURCE_POLICY_DIR / f"{policy_name}.parquet"
        df.to_parquet(out)
        return out

    def load_source_policy(self, policy_name: str) -> pd.DataFrame:
        out = self.paths.LAKE_PORTABLE_PACKAGING_SOURCE_POLICY_DIR / f"{policy_name}.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_reproducible_setup_guide(self, text: str, summary: dict = None) -> Path:
        out = self.paths.LAKE_PORTABLE_PACKAGING_SETUP_GUIDES_DIR / "reproducible_setup_guide.md"
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        return out

    def load_reproducible_setup_guide(self) -> str:
        out = self.paths.LAKE_PORTABLE_PACKAGING_SETUP_GUIDES_DIR / "reproducible_setup_guide.md"
        if out.exists():
            with open(out, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    def save_environment_drift_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out = self.paths.LAKE_PORTABLE_PACKAGING_DRIFT_DIR / "environment_drift.parquet"
        df.to_parquet(out)
        return out

    def load_environment_drift_report(self) -> pd.DataFrame:
        out = self.paths.LAKE_PORTABLE_PACKAGING_DRIFT_DIR / "environment_drift.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_packaging_safety_report(self, df: pd.DataFrame, summary: dict = None) -> Path:
        out = self.paths.LAKE_PORTABLE_PACKAGING_SAFETY_DIR / "packaging_safety.parquet"
        df.to_parquet(out)
        return out

    def load_packaging_safety_report(self) -> pd.DataFrame:
        out = self.paths.LAKE_PORTABLE_PACKAGING_SAFETY_DIR / "packaging_safety.parquet"
        if out.exists():
            return pd.read_parquet(out)
        return pd.DataFrame()

    def save_packaging_quality(self, profile_name: str, quality: dict) -> Path:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_QUALITY_DIR / f"packaging_quality_{profile_name}.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=2)
        return out

    def load_packaging_quality(self, profile_name: str) -> dict:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_QUALITY_DIR / f"packaging_quality_{profile_name}.json"
        if out.exists():
            with open(out, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_portable_packaging_report(self, profile_name: str, report: dict, markdown: str = None) -> Path:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_DIR / f"report_{profile_name}.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        if markdown:
            md_out = self.paths.LAKE_PORTABLE_PACKAGING_DIR / f"report_{profile_name}.md"
            with open(md_out, "w", encoding="utf-8") as f:
                f.write(markdown)
        return out

    def load_portable_packaging_report(self, profile_name: str) -> dict:
        import json
        out = self.paths.LAKE_PORTABLE_PACKAGING_DIR / f"report_{profile_name}.json"
        if out.exists():
            with open(out, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def list_portable_packaging_reports(self) -> pd.DataFrame:
        data = []
        if self.paths.LAKE_PORTABLE_PACKAGING_DIR.exists():
            for p in self.paths.LAKE_PORTABLE_PACKAGING_DIR.glob("report_*.json"):
                data.append({"profile": p.stem.replace("report_", ""), "path": str(p)})
        return pd.DataFrame(data)
"""
# Assuming dl_injection can be safely appended if we avoid indentation issues, or we use regex
dl_content = re.sub(r'(class DataLake:.*)', r'\1' + '\n' + dl_injection, dl_content, flags=re.DOTALL)
with open(datalake_path, "w") as f:
    f.write(dl_content)


# Update FeatureStore
fs_path = "commodity_fx_signal_bot/ml/feature_store.py"
with open(fs_path, "r") as f:
    fs_content = f.read()

fs_injection = """
    # Phase 61: Portable Packaging
    def load_environment_snapshot(self) -> dict:
        return self.data_lake.load_environment_snapshot()

    def load_installed_packages_snapshot(self) -> pd.DataFrame:
        return self.data_lake.load_installed_packages_snapshot()

    def load_dependency_inventory(self) -> pd.DataFrame:
        return self.data_lake.load_dependency_inventory()

    def load_requirements_export_report(self) -> pd.DataFrame:
        return self.data_lake.load_requirements_export_report()

    def load_install_verification_report(self) -> pd.DataFrame:
        return self.data_lake.load_install_verification_report()

    def load_import_verification_report(self) -> pd.DataFrame:
        return self.data_lake.load_import_verification_report()

    def load_script_verification_report(self) -> pd.DataFrame:
        return self.data_lake.load_script_verification_report()

    def load_config_template_verification(self) -> pd.DataFrame:
        return self.data_lake.load_config_template_verification()

    def load_bundle_artifact_inventory(self) -> pd.DataFrame:
        return self.data_lake.load_bundle_artifact_inventory()

    def load_portable_bundle_manifest(self) -> dict:
        return self.data_lake.load_portable_bundle_manifest()

    def load_archive_manifest(self) -> dict:
        return self.data_lake.load_archive_manifest()

    def load_source_policy(self, policy_name: str) -> pd.DataFrame:
        return self.data_lake.load_source_policy(policy_name)

    def load_reproducible_setup_guide(self) -> str:
        return self.data_lake.load_reproducible_setup_guide()

    def load_environment_drift_report(self) -> pd.DataFrame:
        return self.data_lake.load_environment_drift_report()

    def load_packaging_safety_report(self) -> pd.DataFrame:
        return self.data_lake.load_packaging_safety_report()

    def load_packaging_quality(self, profile_name: str = None) -> dict:
        from config.settings import settings
        p = profile_name or settings.default_portable_packaging_profile
        return self.data_lake.load_packaging_quality(p)

    def load_portable_packaging_report(self, profile_name: str = None) -> dict:
        from config.settings import settings
        p = profile_name or settings.default_portable_packaging_profile
        return self.data_lake.load_portable_packaging_report(p)

    def list_available_portable_packaging_reports(self) -> dict:
        df = self.data_lake.list_portable_packaging_reports()
        return df.to_dict(orient="records") if not df.empty else {}
"""
fs_content = re.sub(r'(class FeatureStore:.*)', r'\1' + '\n' + fs_injection, fs_content, flags=re.DOTALL)
with open(fs_path, "w") as f:
    f.write(fs_content)
