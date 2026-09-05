import os
import re

with open("commodity_fx_signal_bot/ml/feature_store.py", "r", encoding="utf-8") as f:
    content = f.read()

addition = """
    # Phase 93 - Local Project Atlas Forwarding
    def load_atlas_profile_registry(self) -> pd.DataFrame: return self.data_lake.load_atlas_profile_registry()
    def load_atlas_domain_registry(self) -> pd.DataFrame: return self.data_lake.load_atlas_domain_registry()
    def load_final_local_meta_index(self) -> pd.DataFrame: return self.data_lake.load_final_local_meta_index()
    def load_universal_navigation_map(self) -> pd.DataFrame: return self.data_lake.load_universal_navigation_map()
    def load_cross_phase_lookup_engine(self) -> str: return self.data_lake.load_cross_phase_lookup_engine()
    def load_cross_phase_lookup_registry(self) -> pd.DataFrame: return self.data_lake.load_cross_phase_lookup_registry()
    def load_cross_phase_output_lookup_table(self) -> pd.DataFrame: return self.data_lake.load_cross_phase_output_lookup_table()
    def load_cross_phase_script_lookup_table(self) -> pd.DataFrame: return self.data_lake.load_cross_phase_script_lookup_table()
    def load_cross_phase_docs_lookup_table(self) -> pd.DataFrame: return self.data_lake.load_cross_phase_docs_lookup_table()
    def load_cross_phase_datalake_lookup_table(self) -> pd.DataFrame: return self.data_lake.load_cross_phase_datalake_lookup_table()
    def load_cross_phase_report_lookup_table(self) -> pd.DataFrame: return self.data_lake.load_cross_phase_report_lookup_table()
    def load_cross_phase_generated_docs_lookup_table(self) -> pd.DataFrame: return self.data_lake.load_cross_phase_generated_docs_lookup_table()
    def load_cross_phase_safety_boundary_lookup_table(self) -> pd.DataFrame: return self.data_lake.load_cross_phase_safety_boundary_lookup_table()
    def load_offline_semantic_table_of_contents(self) -> str: return self.data_lake.load_offline_semantic_table_of_contents()
    def load_terminal_project_atlas(self) -> str: return self.data_lake.load_terminal_project_atlas()
    def load_atlas_module_family_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_module_family_map()
    def load_atlas_script_family_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_script_family_map()
    def load_atlas_report_family_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_report_family_map()
    def load_atlas_datalake_family_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_datalake_family_map()
    def load_atlas_docs_family_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_docs_family_map()
    def load_atlas_generated_docs_family_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_generated_docs_family_map()
    def load_atlas_phase_dependency_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_phase_dependency_map()
    def load_atlas_phase_to_output_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_phase_to_output_map()
    def load_atlas_output_to_script_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_output_to_script_map()
    def load_atlas_command_to_output_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_command_to_output_map()
    def load_atlas_reading_route_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_reading_route_map()
    def load_atlas_operator_route_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_operator_route_map()
    def load_atlas_analyst_route_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_analyst_route_map()
    def load_atlas_maintainer_route_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_maintainer_route_map()
    def load_atlas_codex_agent_route_map(self) -> pd.DataFrame: return self.data_lake.load_atlas_codex_agent_route_map()
    def load_atlas_glossary_index(self) -> pd.DataFrame: return self.data_lake.load_atlas_glossary_index()
    def load_atlas_concept_crosswalk(self) -> pd.DataFrame: return self.data_lake.load_atlas_concept_crosswalk()
    def load_atlas_no_go_safe_go_crosswalk(self) -> pd.DataFrame: return self.data_lake.load_atlas_no_go_safe_go_crosswalk()
    def load_atlas_safety_boundary_crosswalk(self) -> pd.DataFrame: return self.data_lake.load_atlas_safety_boundary_crosswalk()
    def load_atlas_maintenance_crosswalk(self) -> pd.DataFrame: return self.data_lake.load_atlas_maintenance_crosswalk()
    def load_atlas_continuity_crosswalk(self) -> pd.DataFrame: return self.data_lake.load_atlas_continuity_crosswalk()
    def load_atlas_preservation_crosswalk(self) -> pd.DataFrame: return self.data_lake.load_atlas_preservation_crosswalk()
    def load_atlas_project_completion_crosswalk(self) -> pd.DataFrame: return self.data_lake.load_atlas_project_completion_crosswalk()
    def load_atlas_longterm_operations_crosswalk(self) -> pd.DataFrame: return self.data_lake.load_atlas_longterm_operations_crosswalk()
    def load_atlas_release_candidate_crosswalk(self) -> pd.DataFrame: return self.data_lake.load_atlas_release_candidate_crosswalk()
    def load_atlas_incident_response_crosswalk(self) -> pd.DataFrame: return self.data_lake.load_atlas_incident_response_crosswalk()
    def load_atlas_redteam_governance_crosswalk(self) -> pd.DataFrame: return self.data_lake.load_atlas_redteam_governance_crosswalk()
    def load_meta_index_no_go_safe_go_summary(self) -> pd.DataFrame: return self.data_lake.load_meta_index_no_go_safe_go_summary()
    def load_meta_index_exception_register(self) -> pd.DataFrame: return self.data_lake.load_meta_index_exception_register()
    def load_meta_index_gap_register(self) -> pd.DataFrame: return self.data_lake.load_meta_index_gap_register()
    def load_meta_index_risk_summary(self) -> pd.DataFrame: return self.data_lake.load_meta_index_risk_summary()
    def load_meta_index_readiness_score_report(self) -> pd.DataFrame: return self.data_lake.load_meta_index_readiness_score_report()
    def load_meta_index_validation_report(self) -> pd.DataFrame: return self.data_lake.load_meta_index_validation_report()
    def load_meta_index_quality(self, profile_name: str | None = None) -> dict: return self.data_lake.load_meta_index_quality(profile_name or "balanced_local_project_atlas")
    def load_local_project_atlas_report(self, profile_name: str | None = None) -> dict: return self.data_lake.load_local_project_atlas_report(profile_name or "balanced_local_project_atlas")
    def list_available_local_project_atlas_reports(self) -> dict: return self.data_lake.list_local_project_atlas_reports().to_dict(orient="records") if not self.data_lake.list_local_project_atlas_reports().empty else {}
"""

if "load_atlas_profile_registry" not in content:
    content = content + "\n" + addition
    with open("commodity_fx_signal_bot/ml/feature_store.py", "w", encoding="utf-8") as f:
        f.write(content)

print("FeatureStore patched")
