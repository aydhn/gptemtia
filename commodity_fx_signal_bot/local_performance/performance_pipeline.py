import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile, get_default_local_performance_profile
from .performance_domain_registry import build_performance_domain_registry
from .performance_budget import build_final_local_performance_budget
from .runtime_profile import build_lightweight_runtime_profile
from .resource_footprint import build_resource_footprint_rehearsal_report
from .maintenance_cost import build_maintenance_cost_estimate
from .efficiency_planning import build_offline_efficiency_planning_guide
from .performance_quality import build_performance_quality_report

class LocalPerformancePipeline:
    def __init__(self, data_lake, settings, project_root: Path, profile: LocalPerformanceProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_local_performance_profile()

    def build_performance_domain_registry(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, summary = build_performance_domain_registry(self.profile)
        if save and self.data_lake and hasattr(self.data_lake, "save_performance_domain_registry"):
            self.data_lake.save_performance_domain_registry(df, summary)
        return {"performance_domain_registry": df}, summary

    def build_final_local_performance_budget(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, summary = build_final_local_performance_budget(self.project_root, self.profile)
        if save and self.data_lake and hasattr(self.data_lake, "save_final_local_performance_budget"):
            self.data_lake.save_final_local_performance_budget(df, summary)
        return {"final_local_performance_budget": df}, summary

    def build_resource_footprint_rehearsal(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, summary = build_resource_footprint_rehearsal_report(self.project_root, self.profile)
        if save and self.data_lake and hasattr(self.data_lake, "save_resource_footprint_rehearsal_report"):
            self.data_lake.save_resource_footprint_rehearsal_report(df, summary)
        return {"resource_footprint_rehearsal_report": df}, summary

    def build_maintenance_cost_estimate(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df, summary = build_maintenance_cost_estimate(self.project_root, self.profile)
        if save and self.data_lake and hasattr(self.data_lake, "save_maintenance_cost_estimate"):
            self.data_lake.save_maintenance_cost_estimate(df, summary)
        return {"maintenance_cost_estimate": df}, summary

    def build_offline_efficiency_plan(self, save: bool = True) -> tuple[str, dict]:
        text, summary = build_offline_efficiency_planning_guide(self.project_root, self.profile)
        if save and self.data_lake and hasattr(self.data_lake, "save_offline_efficiency_planning_guide"):
            self.data_lake.save_offline_efficiency_planning_guide(text, summary)
        return text, summary

    def build_performance_quality_report(self, save: bool = True) -> tuple[dict, dict]:
        report = build_performance_quality_report({})
        if save and self.data_lake and hasattr(self.data_lake, "save_performance_quality"):
            self.data_lake.save_performance_quality(self.profile.name, report)
        return report, {}

    def build_performance_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"status": "ok"}])
        return df, {"total": 1}
