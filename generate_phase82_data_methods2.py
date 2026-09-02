import os
from pathlib import Path
import re

def patch_feature_store():
    file_path = Path("commodity_fx_signal_bot/ml/feature_store.py")
    if not file_path.exists(): return
    content = file_path.read_text(encoding="utf-8")
    if "def load_simplification_profile_registry" in content: return

    methods = """
    def load_simplification_profile_registry(self) -> pd.DataFrame:
        return self.data_lake.load_simplification_profile_registry()

    def load_simplification_domain_registry(self) -> pd.DataFrame:
        return self.data_lake.load_simplification_domain_registry()

    def load_final_modular_complexity_map(self) -> pd.DataFrame:
        return self.data_lake.load_final_modular_complexity_map()

    def load_module_family_complexity_report(self) -> pd.DataFrame:
        return self.data_lake.load_module_family_complexity_report()

    def load_folder_depth_complexity_report(self) -> pd.DataFrame:
        return self.data_lake.load_folder_depth_complexity_report()

    def load_file_count_complexity_report(self) -> pd.DataFrame:
        return self.data_lake.load_file_count_complexity_report()

    def load_function_count_complexity_report(self) -> pd.DataFrame:
        return self.data_lake.load_function_count_complexity_report()

    def load_script_sprawl_report(self) -> pd.DataFrame:
        return self.data_lake.load_script_sprawl_report()

    def load_test_sprawl_report(self) -> pd.DataFrame:
        return self.data_lake.load_test_sprawl_report()

    def load_report_output_sprawl_report(self) -> pd.DataFrame:
        return self.data_lake.load_report_output_sprawl_report()

    def load_datalake_output_sprawl_report(self) -> pd.DataFrame:
        return self.data_lake.load_datalake_output_sprawl_report()

    def load_documentation_sprawl_report(self) -> pd.DataFrame:
        return self.data_lake.load_documentation_sprawl_report()

    def load_optional_slimming_plan(self) -> pd.DataFrame:
        return self.data_lake.load_optional_slimming_plan()

    def load_safe_consolidation_candidate_registry(self) -> pd.DataFrame:
        return self.data_lake.load_safe_consolidation_candidate_registry()

    def load_duplicate_pattern_consolidation_candidate_registry(self) -> pd.DataFrame:
        return self.data_lake.load_duplicate_pattern_consolidation_candidate_registry()

    def load_naming_simplification_candidate_registry(self) -> pd.DataFrame:
        return self.data_lake.load_naming_simplification_candidate_registry()

    def load_config_simplification_candidate_registry(self) -> pd.DataFrame:
        return self.data_lake.load_config_simplification_candidate_registry()

    def load_datalake_method_simplification_candidate_registry(self) -> pd.DataFrame:
        return self.data_lake.load_datalake_method_simplification_candidate_registry()

    def load_script_cli_simplification_candidate_registry(self) -> pd.DataFrame:
        return self.data_lake.load_script_cli_simplification_candidate_registry()

    def load_test_suite_simplification_candidate_registry(self) -> pd.DataFrame:
        return self.data_lake.load_test_suite_simplification_candidate_registry()

    def load_docs_navigation_simplification_candidate_registry(self) -> pd.DataFrame:
        return self.data_lake.load_docs_navigation_simplification_candidate_registry()

    def load_repo_ergonomics_rehearsal_guide(self) -> str:
        return self.data_lake.load_repo_ergonomics_rehearsal_guide()

    def load_maintainer_onboarding_simplification_guide(self) -> str:
        return self.data_lake.load_maintainer_onboarding_simplification_guide()

    def load_local_maintainability_improvement_seed(self) -> str:
        return self.data_lake.load_local_maintainability_improvement_seed()

    def load_complexity_no_go_safe_go_summary(self) -> pd.DataFrame:
        return self.data_lake.load_complexity_no_go_safe_go_summary()

    def load_simplification_exception_register(self) -> pd.DataFrame:
        return self.data_lake.load_simplification_exception_register()

    def load_simplification_gap_register(self) -> pd.DataFrame:
        return self.data_lake.load_simplification_gap_register()

    def load_simplification_risk_summary(self) -> pd.DataFrame:
        return self.data_lake.load_simplification_risk_summary()

    def load_maintainability_readiness_score_report(self) -> pd.DataFrame:
        return self.data_lake.load_maintainability_readiness_score_report()

    def load_simplification_validation_report(self) -> pd.DataFrame:
        return self.data_lake.load_simplification_validation_report()

    def load_simplification_quality(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_simplification_quality(profile_name or "balanced_local_simplification")

    def load_local_simplification_report(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_local_simplification_report(profile_name or "balanced_local_simplification")

    def list_available_local_simplification_reports(self) -> dict:
        return {"reports": self.data_lake.list_local_simplification_reports().to_dict('records')}
"""
    content += methods
    file_path.write_text(content, encoding="utf-8")

def patch_report_builder():
    file_path = Path("commodity_fx_signal_bot/reports/report_builder.py")
    if not file_path.exists(): return
    content = file_path.read_text(encoding="utf-8")
    if "def build_simplification_domain_registry_text_report" in content: return

    methods = """
    def _build_simplification_disclaimer(self) -> str:
        return "Bu rapor offline/local modular simplification ve maintainability rehearsal ciktisidir. Gercek refactor, dosya silme/tasima, production cleanup, architecture approval, canli emir, broker talimati, model deployment veya yatirim tavsiyesi degildir.\\n\\n"

    def build_simplification_domain_registry_text_report(self, summary: dict, domain_df: pd.DataFrame | None = None) -> str:
        return "Simplification Domain Registry Text Report\\n" + self._build_simplification_disclaimer()

    def build_final_modular_complexity_map_text_report(self, summary: dict, complexity_df: pd.DataFrame | None = None) -> str:
        return "Final Modular Complexity Map Text Report\\n" + self._build_simplification_disclaimer()

    def build_optional_slimming_plan_text_report(self, summary: dict, plan_df: pd.DataFrame | None = None) -> str:
        return "Optional Slimming Plan Text Report\\n" + self._build_simplification_disclaimer()

    def build_repo_ergonomics_text_report(self, summary: dict, guide_text: str | None = None) -> str:
        return "Repo Ergonomics Text Report\\n" + self._build_simplification_disclaimer()

    def build_maintainability_seed_text_report(self, summary: dict, seed_text: str | None = None) -> str:
        return "Maintainability Seed Text Report\\n" + self._build_simplification_disclaimer()

    def build_simplification_quality_text_report(self, summary: dict, quality: dict | None = None) -> str:
        return "Simplification Quality Text Report\\n" + self._build_simplification_disclaimer()

    def build_simplification_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        return "Simplification Status Text Report\\n" + self._build_simplification_disclaimer()
"""
    content += methods
    file_path.write_text(content, encoding="utf-8")

def main():
    patch_feature_store()
    patch_report_builder()
    print("Patched FS and RB for phase 82")

if __name__ == "__main__":
    main()
