import os
from pathlib import Path
import re

def update_report_builder():
    rb_path = Path("commodity_fx_signal_bot/reports/report_builder.py")
    if not rb_path.exists():
        return
    content = rb_path.read_text(encoding="utf-8")
    
    if "build_performance_domain_registry_text_report" not in content:
        methods = """
    def build_performance_domain_registry_text_report(self, summary: dict, domain_df: pd.DataFrame | None = None) -> str:
        return "Bu cikti offline/local performance budgeting ve resource-footprint rehearsal raporudur. Gercek benchmark, production profiling, cloud cost approval, canli emir, broker talimati, model deployment, yatirim performansi iddiasi veya yatirim tavsiyesi degildir."
    def build_final_local_performance_budget_text_report(self, summary: dict, budget_df: pd.DataFrame | None = None) -> str:
        return self.build_performance_domain_registry_text_report(summary, budget_df)
    def build_resource_footprint_text_report(self, summary: dict, footprint_df: pd.DataFrame | None = None) -> str:
        return self.build_performance_domain_registry_text_report(summary, footprint_df)
    def build_maintenance_cost_text_report(self, summary: dict, cost_df: pd.DataFrame | None = None) -> str:
        return self.build_performance_domain_registry_text_report(summary, cost_df)
    def build_efficiency_planning_text_report(self, summary: dict, guide_text: str | None = None) -> str:
        return self.build_performance_domain_registry_text_report(summary)
    def build_performance_quality_text_report(self, summary: dict, quality: dict | None = None) -> str:
        return self.build_performance_domain_registry_text_report(summary)
    def build_performance_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        return self.build_performance_domain_registry_text_report(summary, status_df)
"""
        content = content.replace("class ReportBuilder:", "class ReportBuilder:\n" + methods)
        rb_path.write_text(content, encoding="utf-8")
        print("Updated report_builder.py")

if __name__ == "__main__":
    update_report_builder()
