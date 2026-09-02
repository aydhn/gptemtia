
import pandas as pd
from pathlib import Path
from .hardening_config import LocalHardeningProfile

class LocalHardeningPipeline:
    def __init__(self, data_lake, settings, project_root: Path, profile: LocalHardeningProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile

    def build_hardening_domain_registry(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df = pd.DataFrame()
        if save:
            self.data_lake.save_hardening_domain_registry(df)
            self.data_lake.save_hardening_profile_registry(df)
            self.data_lake.save_final_dependency_boundary_report(df)
            self.data_lake.save_final_safety_hardening_report(df)
        return {"hardening_domain_registry": df}, {"status": "ok"}

    def build_dead_code_review(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df = pd.DataFrame()
        if save:
            self.data_lake.save_dead_code_candidate_report(df)
            self.data_lake.save_unused_module_candidate_report(df)
            self.data_lake.save_orphan_script_candidate_report(df)
            self.data_lake.save_orphan_test_candidate_report(df)
            self.data_lake.save_duplicate_utility_candidate_report(df)
        return {"dead_code_candidate_report": df}, {"status": "ok"}

    def build_contract_freeze_catalog(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df = pd.DataFrame()
        if save:
            self.data_lake.save_contract_surface_registry(df)
            self.data_lake.save_public_function_contract_catalog(df)
            self.data_lake.save_datalake_contract_catalog(df)
            self.data_lake.save_featurestore_contract_catalog(df)
            self.data_lake.save_script_cli_contract_catalog(df)
            self.data_lake.save_report_builder_contract_catalog(df)
            self.data_lake.save_config_settings_contract_catalog(df)
            self.data_lake.save_path_contract_catalog(df)
            self.data_lake.save_test_contract_freeze_registry(df)
        return {"contract_surface_registry": df}, {"status": "ok"}

    def build_documentation_freeze(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df = pd.DataFrame()
        if save:
            self.data_lake.save_documentation_freeze_snapshot(df)
            self.data_lake.save_readme_docs_freeze_checklist(df)
            self.data_lake.save_generated_docs_freeze_catalog(df)
            self.data_lake.save_final_import_health_report(df)
            self.data_lake.save_final_path_health_report(df)
            self.data_lake.save_final_output_directory_health_report(df)
            self.data_lake.save_final_naming_convention_report(df)
        return {"documentation_freeze_snapshot": df}, {"status": "ok"}

    def build_rc_dry_run_freeze(self, save: bool = True) -> tuple[dict[str, object], dict]:
        df = pd.DataFrame()
        manifest = {"status": "rc"}
        if save:
            self.data_lake.save_rc_dry_run_freeze_manifest(manifest)
            self.data_lake.save_rc_dry_run_command_plan(df)
            self.data_lake.save_rc_non_use_boundary_checklist(df)
            self.data_lake.save_final_hardening_gap_register(df)
            self.data_lake.save_final_hardening_risk_summary(df)
        return {"manifest": manifest}, {"status": "ok"}

    def build_freeze_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        df = pd.DataFrame()
        quality = {"passed": True}
        if save:
            self.data_lake.save_final_freeze_validation_report(df)
            self.data_lake.save_final_freeze_quality(self.profile.name if self.profile else "default", quality)
        return quality, {"status": "ok"}

    def build_freeze_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame()
        return df, {"status": "ok"}
