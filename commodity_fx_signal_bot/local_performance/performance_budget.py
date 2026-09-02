import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_default_performance_budget_items(profile: LocalPerformanceProfile) -> pd.DataFrame:
    data = [
        {"budget_name": "cpu_budget", "budget_type": "cpu", "local_limit_hint": profile.default_cpu_budget_label, "dry_run_only": True, "manual_review_required": True, "warning_notes": "Gercek benchmark degildir."},
        {"budget_name": "memory_budget", "budget_type": "memory", "local_limit_hint": f"{profile.default_memory_budget_mb} MB", "dry_run_only": True, "manual_review_required": True, "warning_notes": ""},
        {"budget_name": "disk_budget", "budget_type": "disk", "local_limit_hint": f"{profile.default_disk_budget_mb} MB", "dry_run_only": True, "manual_review_required": True, "warning_notes": ""},
        {"budget_name": "runtime_budget", "budget_type": "runtime", "local_limit_hint": f"{profile.default_runtime_budget_minutes} min", "dry_run_only": True, "manual_review_required": True, "warning_notes": ""}
    ]
    return pd.DataFrame(data)

def classify_budget_pressure(row: pd.Series, profile: LocalPerformanceProfile) -> str:
    return "normal"

def build_final_local_performance_budget(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_performance_budget_items(profile)
    df["estimated_pressure"] = df.apply(lambda r: classify_budget_pressure(r, profile), axis=1)
    return df, summarize_performance_budget(df)

def summarize_performance_budget(budget_df: pd.DataFrame) -> dict:
    if budget_df is None or budget_df.empty: return {"total": 0}
    return {"total": len(budget_df)}

def export_performance_budget_markdown(budget_df: pd.DataFrame, summary: dict) -> str:
    return "# Final Local Performance Budget\n\nBu rapor gercek benchmark degildir."
