import os
import re

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r", encoding="utf-8") as f:
    content = f.read()

# I will add a single large chunk of methods to the DataLake class

addition = """
    # Phase 93 - Local Project Atlas
    def save_atlas_profile_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/profiles", "atlas_profile_registry")
    def load_atlas_profile_registry(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/profiles/atlas_profile_registry.csv")
    def save_atlas_domain_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/domains", "atlas_domain_registry")
    def load_atlas_domain_registry(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/domains/atlas_domain_registry.csv")
    def save_final_local_meta_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/meta_index", "final_local_meta_index")
    def load_final_local_meta_index(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/meta_index/final_local_meta_index.csv")
    def save_universal_navigation_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/navigation", "universal_navigation_map")
    def load_universal_navigation_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/navigation/universal_navigation_map.csv")
    def save_cross_phase_lookup_engine(self, text: str, summary: dict | None = None) -> Path:
        p = self.lake_dir / "local_project_atlas/lookup/cross_phase_lookup_engine.txt"
        with open(p, "w", encoding="utf-8") as f: f.write(text)
        return p
    def load_cross_phase_lookup_engine(self) -> str:
        p = self.lake_dir / "local_project_atlas/lookup/cross_phase_lookup_engine.txt"
        return p.read_text(encoding="utf-8") if p.exists() else ""
    def save_cross_phase_lookup_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/lookup", "cross_phase_lookup_registry")
    def load_cross_phase_lookup_registry(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/lookup/cross_phase_lookup_registry.csv")
    def save_cross_phase_output_lookup_table(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/lookup", "cross_phase_output_lookup_table")
    def load_cross_phase_output_lookup_table(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/lookup/cross_phase_output_lookup_table.csv")
    def save_cross_phase_script_lookup_table(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/lookup", "cross_phase_script_lookup_table")
    def load_cross_phase_script_lookup_table(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/lookup/cross_phase_script_lookup_table.csv")
    def save_cross_phase_docs_lookup_table(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/lookup", "cross_phase_docs_lookup_table")
    def load_cross_phase_docs_lookup_table(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/lookup/cross_phase_docs_lookup_table.csv")
    def save_cross_phase_datalake_lookup_table(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/lookup", "cross_phase_datalake_lookup_table")
    def load_cross_phase_datalake_lookup_table(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/lookup/cross_phase_datalake_lookup_table.csv")
    def save_cross_phase_report_lookup_table(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/lookup", "cross_phase_report_lookup_table")
    def load_cross_phase_report_lookup_table(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/lookup/cross_phase_report_lookup_table.csv")
    def save_cross_phase_generated_docs_lookup_table(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/lookup", "cross_phase_generated_docs_lookup_table")
    def load_cross_phase_generated_docs_lookup_table(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/lookup/cross_phase_generated_docs_lookup_table.csv")
    def save_cross_phase_safety_boundary_lookup_table(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/lookup", "cross_phase_safety_boundary_lookup_table")
    def load_cross_phase_safety_boundary_lookup_table(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/lookup/cross_phase_safety_boundary_lookup_table.csv")
    def save_offline_semantic_table_of_contents(self, text: str, summary: dict | None = None) -> Path:
        p = self.lake_dir / "local_project_atlas/semantic_toc/offline_semantic_table_of_contents.txt"
        with open(p, "w", encoding="utf-8") as f: f.write(text)
        return p
    def load_offline_semantic_table_of_contents(self) -> str:
        p = self.lake_dir / "local_project_atlas/semantic_toc/offline_semantic_table_of_contents.txt"
        return p.read_text(encoding="utf-8") if p.exists() else ""
    def save_terminal_project_atlas(self, text: str, summary: dict | None = None) -> Path:
        p = self.lake_dir / "local_project_atlas/terminal_atlas/terminal_project_atlas.txt"
        with open(p, "w", encoding="utf-8") as f: f.write(text)
        return p
    def load_terminal_project_atlas(self) -> str:
        p = self.lake_dir / "local_project_atlas/terminal_atlas/terminal_project_atlas.txt"
        return p.read_text(encoding="utf-8") if p.exists() else ""
    
    def save_atlas_module_family_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/family_maps", "atlas_module_family_map")
    def load_atlas_module_family_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/family_maps/atlas_module_family_map.csv")
    def save_atlas_script_family_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/family_maps", "atlas_script_family_map")
    def load_atlas_script_family_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/family_maps/atlas_script_family_map.csv")
    def save_atlas_report_family_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/family_maps", "atlas_report_family_map")
    def load_atlas_report_family_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/family_maps/atlas_report_family_map.csv")
    def save_atlas_datalake_family_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/family_maps", "atlas_datalake_family_map")
    def load_atlas_datalake_family_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/family_maps/atlas_datalake_family_map.csv")
    def save_atlas_docs_family_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/family_maps", "atlas_docs_family_map")
    def load_atlas_docs_family_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/family_maps/atlas_docs_family_map.csv")
    def save_atlas_generated_docs_family_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/family_maps", "atlas_generated_docs_family_map")
    def load_atlas_generated_docs_family_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/family_maps/atlas_generated_docs_family_map.csv")
    def save_atlas_phase_dependency_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/phase_maps", "atlas_phase_dependency_map")
    def load_atlas_phase_dependency_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/phase_maps/atlas_phase_dependency_map.csv")
    def save_atlas_phase_to_output_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/phase_maps", "atlas_phase_to_output_map")
    def load_atlas_phase_to_output_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/phase_maps/atlas_phase_to_output_map.csv")
    def save_atlas_output_to_script_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/phase_maps", "atlas_output_to_script_map")
    def load_atlas_output_to_script_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/phase_maps/atlas_output_to_script_map.csv")
    def save_atlas_command_to_output_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/phase_maps", "atlas_command_to_output_map")
    def load_atlas_command_to_output_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/phase_maps/atlas_command_to_output_map.csv")
    
    def save_atlas_reading_route_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/route_maps", "atlas_reading_route_map")
    def load_atlas_reading_route_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/route_maps/atlas_reading_route_map.csv")
    def save_atlas_operator_route_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/route_maps", "atlas_operator_route_map")
    def load_atlas_operator_route_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/route_maps/atlas_operator_route_map.csv")
    def save_atlas_analyst_route_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/route_maps", "atlas_analyst_route_map")
    def load_atlas_analyst_route_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/route_maps/atlas_analyst_route_map.csv")
    def save_atlas_maintainer_route_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/route_maps", "atlas_maintainer_route_map")
    def load_atlas_maintainer_route_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/route_maps/atlas_maintainer_route_map.csv")
    def save_atlas_codex_agent_route_map(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/route_maps", "atlas_codex_agent_route_map")
    def load_atlas_codex_agent_route_map(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/route_maps/atlas_codex_agent_route_map.csv")
    
    def save_atlas_glossary_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/glossary", "atlas_glossary_index")
    def load_atlas_glossary_index(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/glossary/atlas_glossary_index.csv")
    
    def save_atlas_concept_crosswalk(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/crosswalks", "atlas_concept_crosswalk")
    def load_atlas_concept_crosswalk(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/crosswalks/atlas_concept_crosswalk.csv")
    def save_atlas_no_go_safe_go_crosswalk(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/crosswalks", "atlas_no_go_safe_go_crosswalk")
    def load_atlas_no_go_safe_go_crosswalk(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/crosswalks/atlas_no_go_safe_go_crosswalk.csv")
    def save_atlas_safety_boundary_crosswalk(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/crosswalks", "atlas_safety_boundary_crosswalk")
    def load_atlas_safety_boundary_crosswalk(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/crosswalks/atlas_safety_boundary_crosswalk.csv")
    def save_atlas_maintenance_crosswalk(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/crosswalks", "atlas_maintenance_crosswalk")
    def load_atlas_maintenance_crosswalk(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/crosswalks/atlas_maintenance_crosswalk.csv")
    def save_atlas_continuity_crosswalk(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/crosswalks", "atlas_continuity_crosswalk")
    def load_atlas_continuity_crosswalk(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/crosswalks/atlas_continuity_crosswalk.csv")
    def save_atlas_preservation_crosswalk(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/crosswalks", "atlas_preservation_crosswalk")
    def load_atlas_preservation_crosswalk(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/crosswalks/atlas_preservation_crosswalk.csv")
    def save_atlas_project_completion_crosswalk(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/crosswalks", "atlas_project_completion_crosswalk")
    def load_atlas_project_completion_crosswalk(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/crosswalks/atlas_project_completion_crosswalk.csv")
    def save_atlas_longterm_operations_crosswalk(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/crosswalks", "atlas_longterm_operations_crosswalk")
    def load_atlas_longterm_operations_crosswalk(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/crosswalks/atlas_longterm_operations_crosswalk.csv")
    def save_atlas_release_candidate_crosswalk(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/crosswalks", "atlas_release_candidate_crosswalk")
    def load_atlas_release_candidate_crosswalk(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/crosswalks/atlas_release_candidate_crosswalk.csv")
    def save_atlas_incident_response_crosswalk(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/crosswalks", "atlas_incident_response_crosswalk")
    def load_atlas_incident_response_crosswalk(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/crosswalks/atlas_incident_response_crosswalk.csv")
    def save_atlas_redteam_governance_crosswalk(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/crosswalks", "atlas_redteam_governance_crosswalk")
    def load_atlas_redteam_governance_crosswalk(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/crosswalks/atlas_redteam_governance_crosswalk.csv")
    
    def save_meta_index_no_go_safe_go_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/no_go_safe_go", "meta_index_no_go_safe_go_summary")
    def load_meta_index_no_go_safe_go_summary(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/no_go_safe_go/meta_index_no_go_safe_go_summary.csv")
    
    def save_meta_index_exception_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/exceptions", "meta_index_exception_register")
    def load_meta_index_exception_register(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/exceptions/meta_index_exception_register.csv")
    
    def save_meta_index_gap_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/gaps", "meta_index_gap_register")
    def load_meta_index_gap_register(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/gaps/meta_index_gap_register.csv")
    
    def save_meta_index_risk_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/risks", "meta_index_risk_summary")
    def load_meta_index_risk_summary(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/risks/meta_index_risk_summary.csv")
    
    def save_meta_index_readiness_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/scoring", "meta_index_readiness_score_report")
    def load_meta_index_readiness_score_report(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/scoring/meta_index_readiness_score_report.csv")
    
    def save_meta_index_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path: return self._save_csv_and_summary(df, summary, "local_project_atlas/validation", "meta_index_validation_report")
    def load_meta_index_validation_report(self) -> pd.DataFrame: return self._load_csv("local_project_atlas/validation/meta_index_validation_report.csv")
    
    def save_meta_index_quality(self, profile_name: str, quality: dict) -> Path: return self._save_json(quality, "local_project_atlas/quality", f"meta_index_quality_{profile_name}")
    def load_meta_index_quality(self, profile_name: str) -> dict: return self._load_json(f"local_project_atlas/quality/meta_index_quality_{profile_name}.json")
    
    def save_local_project_atlas_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        if markdown:
            md_path = self.lake_dir / f"local_project_atlas/reports/local_project_atlas_report_{profile_name}.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            with open(md_path, "w", encoding="utf-8") as f: f.write(markdown)
        return self._save_json(report, "local_project_atlas/reports", f"local_project_atlas_report_{profile_name}")
    def load_local_project_atlas_report(self, profile_name: str) -> dict: return self._load_json(f"local_project_atlas/reports/local_project_atlas_report_{profile_name}.json")
    
    def list_local_project_atlas_reports(self) -> pd.DataFrame:
        reports_dir = self.lake_dir / "local_project_atlas/reports"
        if not reports_dir.exists(): return pd.DataFrame()
        return pd.DataFrame([{"report_file": f.name} for f in reports_dir.glob("*.json")])
"""

if "save_atlas_profile_registry" not in content:
    # insert before the end of the class
    last_def = content.rfind("    def ")
    end_of_class = content.find("\n", last_def)
    # wait, just append to the end
    content = content + "\n" + addition
    with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w", encoding="utf-8") as f:
        f.write(content)

print("DataLake patched")
