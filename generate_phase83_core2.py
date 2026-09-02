import os
from pathlib import Path

def generate_core2():
    base_dir = Path("commodity_fx_signal_bot/local_performance")
    
    # performance_budget.py
    (base_dir / "performance_budget.py").write_text("""import pandas as pd
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
    return "# Final Local Performance Budget\\n\\nBu rapor gercek benchmark degildir."
""", encoding="utf-8")

    # runtime_profile.py
    (base_dir / "runtime_profile.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_runtime_profile_items(profile: LocalPerformanceProfile) -> pd.DataFrame:
    data = [
        {"mode_name": "full_local_report_generation", "description": "Full generation", "dry_run_only": True},
        {"mode_name": "lightweight_status_only", "description": "Status only", "dry_run_only": True},
        {"mode_name": "manual_review_mode", "description": "Manual review", "dry_run_only": True}
    ]
    return pd.DataFrame(data)

def classify_runtime_mode(row: pd.Series, profile: LocalPerformanceProfile) -> str:
    return row["mode_name"]

def build_lightweight_runtime_profile(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_runtime_profile_items(profile)
    df["classified_mode"] = df.apply(lambda r: classify_runtime_mode(r, profile), axis=1)
    return df, summarize_lightweight_runtime_profile(df)

def summarize_lightweight_runtime_profile(profile_df: pd.DataFrame) -> dict:
    return {"total": len(profile_df) if profile_df is not None else 0}
""", encoding="utf-8")

    # resource_footprint.py
    (base_dir / "resource_footprint.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def discover_resource_footprint_items(project_root: Path, profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"item": "reports", "type": "disk", "warning": "Gercek profiler degildir."}])

def build_resource_footprint_rehearsal_report(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = discover_resource_footprint_items(project_root, profile)
    return df, summarize_resource_footprint(df)

def summarize_resource_footprint(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

    # cpu_estimates.py
    (base_dir / "cpu_estimates.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_cpu_pressure_for_file(path: Path, project_root: Path, profile: LocalPerformanceProfile) -> dict:
    return {"file": str(path.name), "pressure": "cpu_estimate_low", "warning": "Gercek CPU olcumu degildir."}

def build_cpu_usage_estimate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"layer": "scripts", "pressure": "cpu_estimate_low"}])
    return df, summarize_cpu_estimates(df)

def summarize_cpu_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

    # memory_estimates.py
    (base_dir / "memory_estimates.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_memory_pressure_for_layer(layer_name: str, item_count: int, profile: LocalPerformanceProfile) -> dict:
    return {"layer": layer_name, "pressure": "memory_estimate_low", "warning": "Gercek memory profiler degildir."}

def build_memory_usage_estimate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([estimate_memory_pressure_for_layer("datalake", 10, profile)])
    return df, summarize_memory_estimates(df)

def summarize_memory_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

    # disk_estimates.py
    (base_dir / "disk_estimates.py").write_text("""import pandas as pd
import os
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_disk_usage_by_layer(project_root: Path, profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"layer": "datalake", "size_mb": 10, "warning": "Dosya icerigi okunmaz."}])

def build_disk_usage_estimate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = estimate_disk_usage_by_layer(project_root, profile)
    return df, summarize_disk_estimates(df)

def summarize_disk_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

if __name__ == "__main__":
    generate_core2()
    print("Core 2 generated")
