import os
from pathlib import Path
import re

def update_feature_store():
    fs_path = Path("commodity_fx_signal_bot/ml/feature_store.py")
    if not fs_path.exists():
        return
    content = fs_path.read_text(encoding="utf-8")
    
    if "load_performance_profile_registry" not in content:
        methods = """
    def load_performance_profile_registry(self) -> pd.DataFrame: return self.data_lake.load_performance_profile_registry()
    def load_performance_domain_registry(self) -> pd.DataFrame: return self.data_lake.load_performance_domain_registry()
    def load_final_local_performance_budget(self) -> pd.DataFrame: return self.data_lake.load_final_local_performance_budget()
    def load_lightweight_runtime_profile(self) -> pd.DataFrame: return self.data_lake.load_lightweight_runtime_profile()
    def load_resource_footprint_rehearsal_report(self) -> pd.DataFrame: return self.data_lake.load_resource_footprint_rehearsal_report()
    def load_cpu_usage_estimate_registry(self) -> pd.DataFrame: return self.data_lake.load_cpu_usage_estimate_registry()
    def load_memory_usage_estimate_registry(self) -> pd.DataFrame: return self.data_lake.load_memory_usage_estimate_registry()
    def load_disk_usage_estimate_registry(self) -> pd.DataFrame: return self.data_lake.load_disk_usage_estimate_registry()
    def load_report_output_growth_estimate(self) -> pd.DataFrame: return self.data_lake.load_report_output_growth_estimate()
    def load_datalake_growth_estimate(self) -> pd.DataFrame: return self.data_lake.load_datalake_growth_estimate()
    def load_generated_docs_growth_estimate(self) -> pd.DataFrame: return self.data_lake.load_generated_docs_growth_estimate()
    def load_script_runtime_estimate_registry(self) -> pd.DataFrame: return self.data_lake.load_script_runtime_estimate_registry()
    def load_test_runtime_estimate_registry(self) -> pd.DataFrame: return self.data_lake.load_test_runtime_estimate_registry()
    def load_pipeline_runtime_estimate_registry(self) -> pd.DataFrame: return self.data_lake.load_pipeline_runtime_estimate_registry()
    def load_maintenance_cost_estimate(self) -> pd.DataFrame: return self.data_lake.load_maintenance_cost_estimate()
    def load_maintenance_effort_matrix(self) -> pd.DataFrame: return self.data_lake.load_maintenance_effort_matrix()
    def load_operator_time_budget_report(self) -> pd.DataFrame: return self.data_lake.load_operator_time_budget_report()
    def load_local_machine_suitability_checklist(self) -> pd.DataFrame: return self.data_lake.load_local_machine_suitability_checklist()
    def load_offline_efficiency_planning_guide(self) -> str: return self.data_lake.load_offline_efficiency_planning_guide()
    def load_efficiency_candidate_registry(self) -> pd.DataFrame: return self.data_lake.load_efficiency_candidate_registry()
    def load_lightweight_mode_recommendation_registry(self) -> pd.DataFrame: return self.data_lake.load_lightweight_mode_recommendation_registry()
    def load_heavy_output_warning_registry(self) -> pd.DataFrame: return self.data_lake.load_heavy_output_warning_registry()
    def load_storage_retention_rehearsal_plan(self) -> pd.DataFrame: return self.data_lake.load_storage_retention_rehearsal_plan()
    def load_report_rotation_rehearsal_guide(self) -> str: return self.data_lake.load_report_rotation_rehearsal_guide()
    def load_datalake_retention_rehearsal_guide(self) -> str: return self.data_lake.load_datalake_retention_rehearsal_guide()
    def load_performance_no_go_safe_go_summary(self) -> pd.DataFrame: return self.data_lake.load_performance_no_go_safe_go_summary()
    def load_performance_exception_register(self) -> pd.DataFrame: return self.data_lake.load_performance_exception_register()
    def load_performance_gap_register(self) -> pd.DataFrame: return self.data_lake.load_performance_gap_register()
    def load_performance_risk_summary(self) -> pd.DataFrame: return self.data_lake.load_performance_risk_summary()
    def load_performance_readiness_score_report(self) -> pd.DataFrame: return self.data_lake.load_performance_readiness_score_report()
    def load_performance_validation_report(self) -> pd.DataFrame: return self.data_lake.load_performance_validation_report()
    def load_performance_quality(self, profile_name: str = "default") -> dict: return self.data_lake.load_performance_quality(profile_name)
    def load_local_performance_report(self, profile_name: str = "default") -> dict: return self.data_lake.load_local_performance_report(profile_name)
    def list_available_local_performance_reports(self) -> dict: return {}
"""
        content = content.replace("class FeatureStore:", "class FeatureStore:\n" + methods)
        fs_path.write_text(content, encoding="utf-8")
        print("Updated feature_store.py")

if __name__ == "__main__":
    update_feature_store()
