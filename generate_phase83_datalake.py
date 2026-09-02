import os
from pathlib import Path
import re

def update_data_lake():
    lake_path = Path("commodity_fx_signal_bot/data/storage/data_lake.py")
    if not lake_path.exists():
        return
    content = lake_path.read_text(encoding="utf-8")
    
    if "save_performance_profile_registry" not in content:
        methods = """
    def save_performance_profile_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_PROFILES, "performance_profile_registry", summary)
    def load_performance_profile_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_PROFILES, "performance_profile_registry")

    def save_performance_domain_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_DOMAINS, "performance_domain_registry", summary)
    def load_performance_domain_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_DOMAINS, "performance_domain_registry")

    def save_final_local_performance_budget(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_BUDGET, "final_local_performance_budget", summary)
    def load_final_local_performance_budget(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_BUDGET, "final_local_performance_budget")

    def save_lightweight_runtime_profile(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_RUNTIME_PROFILE, "lightweight_runtime_profile", summary)
    def load_lightweight_runtime_profile(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_RUNTIME_PROFILE, "lightweight_runtime_profile")

    def save_resource_footprint_rehearsal_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_RESOURCE_FOOTPRINT, "resource_footprint_rehearsal_report", summary)
    def load_resource_footprint_rehearsal_report(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_RESOURCE_FOOTPRINT, "resource_footprint_rehearsal_report")

    def save_cpu_usage_estimate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_CPU, "cpu_usage_estimate_registry", summary)
    def load_cpu_usage_estimate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_CPU, "cpu_usage_estimate_registry")

    def save_memory_usage_estimate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_MEMORY, "memory_usage_estimate_registry", summary)
    def load_memory_usage_estimate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_MEMORY, "memory_usage_estimate_registry")

    def save_disk_usage_estimate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_DISK, "disk_usage_estimate_registry", summary)
    def load_disk_usage_estimate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_DISK, "disk_usage_estimate_registry")

    def save_report_output_growth_estimate(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_GROWTH, "report_output_growth_estimate", summary)
    def load_report_output_growth_estimate(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_GROWTH, "report_output_growth_estimate")

    def save_datalake_growth_estimate(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_GROWTH, "datalake_growth_estimate", summary)
    def load_datalake_growth_estimate(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_GROWTH, "datalake_growth_estimate")

    def save_generated_docs_growth_estimate(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_GROWTH, "generated_docs_growth_estimate", summary)
    def load_generated_docs_growth_estimate(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_GROWTH, "generated_docs_growth_estimate")

    def save_script_runtime_estimate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_SCRIPT_RUNTIME, "script_runtime_estimate_registry", summary)
    def load_script_runtime_estimate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_SCRIPT_RUNTIME, "script_runtime_estimate_registry")

    def save_test_runtime_estimate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_TEST_RUNTIME, "test_runtime_estimate_registry", summary)
    def load_test_runtime_estimate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_TEST_RUNTIME, "test_runtime_estimate_registry")

    def save_pipeline_runtime_estimate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_PIPELINE_RUNTIME, "pipeline_runtime_estimate_registry", summary)
    def load_pipeline_runtime_estimate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_PIPELINE_RUNTIME, "pipeline_runtime_estimate_registry")

    def save_maintenance_cost_estimate(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_MAINTENANCE_COST, "maintenance_cost_estimate", summary)
    def load_maintenance_cost_estimate(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_MAINTENANCE_COST, "maintenance_cost_estimate")

    def save_maintenance_effort_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_MAINTENANCE_EFFORT, "maintenance_effort_matrix", summary)
    def load_maintenance_effort_matrix(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_MAINTENANCE_EFFORT, "maintenance_effort_matrix")

    def save_operator_time_budget_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_OPERATOR_TIME, "operator_time_budget_report", summary)
    def load_operator_time_budget_report(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_OPERATOR_TIME, "operator_time_budget_report")

    def save_local_machine_suitability_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_MACHINE_SUITABILITY, "local_machine_suitability_checklist", summary)
    def load_local_machine_suitability_checklist(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_MACHINE_SUITABILITY, "local_machine_suitability_checklist")

    def save_offline_efficiency_planning_guide(self, text: str, summary: dict | None = None) -> Path:
        return self._save_text(text, self.paths.LAKE_LOCAL_PERFORMANCE_EFFICIENCY, "offline_efficiency_planning_guide", summary)
    def load_offline_efficiency_planning_guide(self) -> str:
        return self._load_text(self.paths.LAKE_LOCAL_PERFORMANCE_EFFICIENCY, "offline_efficiency_planning_guide")

    def save_efficiency_candidate_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_EFFICIENCY, "efficiency_candidate_registry", summary)
    def load_efficiency_candidate_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_EFFICIENCY, "efficiency_candidate_registry")

    def save_lightweight_mode_recommendation_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_LIGHTWEIGHT_MODE, "lightweight_mode_recommendation_registry", summary)
    def load_lightweight_mode_recommendation_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_LIGHTWEIGHT_MODE, "lightweight_mode_recommendation_registry")

    def save_heavy_output_warning_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_WARNINGS, "heavy_output_warning_registry", summary)
    def load_heavy_output_warning_registry(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_WARNINGS, "heavy_output_warning_registry")

    def save_storage_retention_rehearsal_plan(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_RETENTION, "storage_retention_rehearsal_plan", summary)
    def load_storage_retention_rehearsal_plan(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_RETENTION, "storage_retention_rehearsal_plan")

    def save_report_rotation_rehearsal_guide(self, text: str, summary: dict | None = None) -> Path:
        return self._save_text(text, self.paths.LAKE_LOCAL_PERFORMANCE_RETENTION, "report_rotation_rehearsal_guide", summary)
    def load_report_rotation_rehearsal_guide(self) -> str:
        return self._load_text(self.paths.LAKE_LOCAL_PERFORMANCE_RETENTION, "report_rotation_rehearsal_guide")

    def save_datalake_retention_rehearsal_guide(self, text: str, summary: dict | None = None) -> Path:
        return self._save_text(text, self.paths.LAKE_LOCAL_PERFORMANCE_RETENTION, "datalake_retention_rehearsal_guide", summary)
    def load_datalake_retention_rehearsal_guide(self) -> str:
        return self._load_text(self.paths.LAKE_LOCAL_PERFORMANCE_RETENTION, "datalake_retention_rehearsal_guide")

    def save_performance_no_go_safe_go_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_NO_GO_SAFE_GO, "performance_no_go_safe_go_summary", summary)
    def load_performance_no_go_safe_go_summary(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_NO_GO_SAFE_GO, "performance_no_go_safe_go_summary")

    def save_performance_exception_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_EXCEPTIONS, "performance_exception_register", summary)
    def load_performance_exception_register(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_EXCEPTIONS, "performance_exception_register")

    def save_performance_gap_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_GAPS, "performance_gap_register", summary)
    def load_performance_gap_register(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_GAPS, "performance_gap_register")

    def save_performance_risk_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_RISKS, "performance_risk_summary", summary)
    def load_performance_risk_summary(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_RISKS, "performance_risk_summary")

    def save_performance_readiness_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_SCORING, "performance_readiness_score_report", summary)
    def load_performance_readiness_score_report(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_SCORING, "performance_readiness_score_report")

    def save_performance_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_df(df, self.paths.LAKE_LOCAL_PERFORMANCE_VALIDATION, "performance_validation_report", summary)
    def load_performance_validation_report(self) -> pd.DataFrame:
        return self._load_df(self.paths.LAKE_LOCAL_PERFORMANCE_VALIDATION, "performance_validation_report")

    def save_performance_quality(self, profile_name: str, quality: dict) -> Path:
        return self._save_json(quality, self.paths.LAKE_LOCAL_PERFORMANCE_QUALITY, f"performance_quality_{profile_name}")
    def load_performance_quality(self, profile_name: str) -> dict:
        return self._load_json(self.paths.LAKE_LOCAL_PERFORMANCE_QUALITY, f"performance_quality_{profile_name}")

    def save_local_performance_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        if markdown:
            self._save_text(markdown, self.paths.LAKE_LOCAL_PERFORMANCE, f"performance_report_{profile_name}")
        return self._save_json(report, self.paths.LAKE_LOCAL_PERFORMANCE, f"performance_report_{profile_name}")
    def load_local_performance_report(self, profile_name: str) -> dict:
        return self._load_json(self.paths.LAKE_LOCAL_PERFORMANCE, f"performance_report_{profile_name}")
    def list_local_performance_reports(self) -> pd.DataFrame:
        return pd.DataFrame()
"""
        # Find where to append
        content = content.replace("class DataLake:", "class DataLake:\n" + methods)
        lake_path.write_text(content, encoding="utf-8")
        print("Updated data_lake.py")

if __name__ == "__main__":
    update_data_lake()
