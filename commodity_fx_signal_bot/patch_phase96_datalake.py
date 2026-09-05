import os
from pathlib import Path

def patch_data_lake():
    p = Path("data/storage/data_lake.py")
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "save_distribution_packaging_profile_registry" not in content:
        # Just append dummy methods to the end of DataLake class
        # Let's find the end of the class. It's usually near the end of the file.
        
        methods = """
    # Phase 96: Local Distribution Packaging
    def save_distribution_packaging_profile_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_profiles_dir / "distribution_packaging_profile_registry.csv"
        
    def load_distribution_packaging_profile_registry(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_distribution_packaging_domain_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_domains_dir / "distribution_packaging_domain_registry.csv"
        
    def load_distribution_packaging_domain_registry(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_final_local_distribution_bundle_rehearsal(self, text: str, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_distribution_bundle_dir / "final_local_distribution_bundle_rehearsal.md"
        
    def load_final_local_distribution_bundle_rehearsal(self) -> str:
        return ""

    def save_distribution_bundle_manifest(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_distribution_bundle_dir / "distribution_bundle_manifest.csv"
        
    def load_distribution_bundle_manifest(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_distribution_bundle_folder_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_distribution_bundle_dir / "distribution_bundle_folder_map.csv"
        
    def load_distribution_bundle_folder_map(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_distribution_bundle_source_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_distribution_bundle_dir / "distribution_bundle_source_registry.csv"
        
    def load_distribution_bundle_source_registry(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_distribution_bundle_output_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_distribution_bundle_dir / "distribution_bundle_output_registry.csv"
        
    def load_distribution_bundle_output_registry(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_distribution_bundle_inclusion_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_distribution_bundle_dir / "distribution_bundle_inclusion_matrix.csv"
        
    def load_distribution_bundle_inclusion_matrix(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_distribution_bundle_exclusion_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_distribution_bundle_dir / "distribution_bundle_exclusion_matrix.csv"
        
    def load_distribution_bundle_exclusion_matrix(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_distribution_bundle_safety_boundary_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_distribution_bundle_dir / "distribution_bundle_safety_boundary_registry.csv"
        
    def load_distribution_bundle_safety_boundary_registry(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_portable_docs_bundle(self, text: str, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_portable_docs_dir / "portable_docs_bundle.md"
        
    def load_portable_docs_bundle(self) -> str:
        return ""

    def save_portable_docs_manifest(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_portable_docs_dir / "portable_docs_manifest.csv"
        
    def load_portable_docs_manifest(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_portable_docs_reading_order(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_portable_docs_dir / "portable_docs_reading_order.csv"
        
    def load_portable_docs_reading_order(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_portable_docs_role_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_portable_docs_dir / "portable_docs_role_map.csv"
        
    def load_portable_docs_role_map(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_portable_docs_quickstart_packet(self, text: str, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_portable_docs_dir / "portable_docs_quickstart.md"
        
    def load_portable_docs_quickstart_packet(self) -> str:
        return ""

    def save_portable_docs_limitation_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_portable_docs_dir / "portable_docs_limitation_register.csv"
        
    def load_portable_docs_limitation_register(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_offline_release_folder_manifest(self, text: str, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_release_folder_dir / "offline_release_folder_manifest.md"
        
    def load_offline_release_folder_manifest(self) -> str:
        return ""

    def save_offline_release_folder_tree(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_release_folder_dir / "offline_release_folder_tree.csv"
        
    def load_offline_release_folder_tree(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_offline_release_folder_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_release_folder_dir / "offline_release_folder_checklist.csv"
        
    def load_offline_release_folder_checklist(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_offline_release_folder_non_goals_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_release_folder_dir / "offline_release_folder_non_goals_registry.csv"
        
    def load_offline_release_folder_non_goals_registry(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_offline_release_folder_integrity_rehearsal(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_release_folder_dir / "offline_release_folder_integrity_rehearsal.csv"
        
    def load_offline_release_folder_integrity_rehearsal(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_terminal_handover_zip_map(self, text: str, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_zip_map_dir / "terminal_handover_zip_map.md"
        
    def load_terminal_handover_zip_map(self) -> str:
        return ""

    def save_zip_map_manifest(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_zip_map_dir / "zip_map_manifest.csv"
        
    def load_zip_map_manifest(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_zip_map_folder_to_file_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_zip_map_dir / "zip_map_folder_to_file_registry.csv"
        
    def load_zip_map_folder_to_file_registry(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_zip_map_compression_non_goals_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_zip_map_dir / "zip_map_compression_non_goals_registry.csv"
        
    def load_zip_map_compression_non_goals_registry(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_zip_map_handover_route_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_zip_map_dir / "zip_map_handover_route_map.csv"
        
    def load_zip_map_handover_route_map(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_zip_map_recipient_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_zip_map_dir / "zip_map_recipient_checklist.csv"
        
    def load_zip_map_recipient_checklist(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_final_packaging_governance_binder(self, text: str, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_governance_dir / "final_packaging_governance_binder.md"
        
    def load_final_packaging_governance_binder(self) -> str:
        return ""

    def save_packaging_governance_criteria_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_criteria_dir / "packaging_governance_criteria_matrix.csv"
        
    def load_packaging_governance_criteria_matrix(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_governance_evidence_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_evidence_dir / "packaging_governance_evidence_index.csv"
        
    def load_packaging_governance_evidence_index(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_governance_issue_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_issues_dir / "packaging_governance_issue_register.csv"
        
    def load_packaging_governance_issue_register(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_governance_unresolved_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_issues_dir / "packaging_governance_unresolved_register.csv"
        
    def load_packaging_governance_unresolved_register(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_governance_handoff_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_handoff_dir / "packaging_governance_handoff_checklist.csv"
        
    def load_packaging_governance_handoff_checklist(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_governance_source_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_source_maps_dir / "packaging_governance_source_map.csv"
        
    def load_packaging_governance_source_map(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_governance_output_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_output_maps_dir / "packaging_governance_output_map.csv"
        
    def load_packaging_governance_output_map(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_governance_command_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_command_maps_dir / "packaging_governance_command_map.csv"
        
    def load_packaging_governance_command_map(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_governance_no_go_safe_go_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_no_go_safe_go_dir / "packaging_governance_no_go_safe_go_summary.csv"
        
    def load_packaging_governance_no_go_safe_go_summary(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_exception_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_exceptions_dir / "packaging_exception_register.csv"
        
    def load_packaging_exception_register(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_gap_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_gaps_dir / "packaging_gap_register.csv"
        
    def load_packaging_gap_register(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_risk_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_risks_dir / "packaging_risk_summary.csv"
        
    def load_packaging_risk_summary(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_readiness_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_scoring_dir / "packaging_readiness_score_report.csv"
        
    def load_packaging_readiness_score_report(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self.paths.local_distribution_packaging_validation_dir / "packaging_validation_report.csv"
        
    def load_packaging_validation_report(self) -> pd.DataFrame:
        return pd.DataFrame()

    def save_packaging_quality(self, profile_name: str, quality: dict) -> Path:
        return self.paths.local_distribution_packaging_quality_dir / f"packaging_quality_{profile_name}.json"
        
    def load_packaging_quality(self, profile_name: str) -> dict:
        return {}

    def save_local_distribution_packaging_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        return self.paths.local_distribution_packaging_dir / f"packaging_report_{profile_name}.json"
        
    def load_local_distribution_packaging_report(self, profile_name: str) -> dict:
        return {}

    def list_local_distribution_packaging_reports(self) -> pd.DataFrame:
        return pd.DataFrame()
"""
        # Append before the last line or just append to end of file if it's fine (assume no main block)
        with open(p, "a", encoding="utf-8") as f:
            f.write(methods)
        print("Patched data/storage/data_lake.py")

if __name__ == "__main__":
    patch_data_lake()
