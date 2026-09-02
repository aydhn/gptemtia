import pandas as pd

def build_performance_disclaimer() -> str:
    return "Bu rapor offline/local performance budgeting ve resource-footprint rehearsal ciktisidir; gercek benchmark, production profiling, cloud cost approval, canli sinyal, broker talimati, model deployment, yatirim performansi iddiasi veya yatirim tavsiyesi degildir."

def build_performance_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return f"# Performance Domain Registry\n\n{build_performance_disclaimer()}"

def build_final_local_performance_budget_markdown_report(summary: dict, budget_df: pd.DataFrame | None = None) -> str:
    return f"# Final Local Performance Budget\n\n{build_performance_disclaimer()}"

def build_resource_footprint_markdown_report(summary: dict, footprint_df: pd.DataFrame | None = None) -> str:
    return f"# Resource Footprint Rehearsal Report\n\n{build_performance_disclaimer()}"

def build_maintenance_cost_markdown_report(summary: dict, cost_df: pd.DataFrame | None = None) -> str:
    return f"# Maintenance Cost Estimate\n\n{build_performance_disclaimer()}"

def build_efficiency_planning_markdown_report(summary: dict, guide_text: str | None = None) -> str:
    return f"# Offline Efficiency Planning Guide\n\n{build_performance_disclaimer()}\n\n{guide_text or ''}"

def build_performance_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return f"# Performance Quality Report\n\n{build_performance_disclaimer()}"

def build_performance_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return f"# Performance Status\n\n{build_performance_disclaimer()}"
