import os
from pathlib import Path

def generate_core3():
    base_dir = Path("commodity_fx_signal_bot/local_performance")
    
    # growth_estimates.py
    (base_dir / "growth_estimates.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_growth_by_family(project_root: Path, base_dir_name: str, profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"family_name": base_dir_name, "current_item_count": 0, "current_size_bytes": 0, "estimated_growth_pressure": "low", "retention_note": "Manual review", "warnings": "Forecast guarantee degildir."}])

def build_report_output_growth_estimate(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = estimate_growth_by_family(project_root, "reports", profile)
    return df, summarize_growth_estimates(df)

def build_datalake_growth_estimate(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = estimate_growth_by_family(project_root, "datalake", profile)
    return df, summarize_growth_estimates(df)

def build_generated_docs_growth_estimate(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = estimate_growth_by_family(project_root, "docs", profile)
    return df, summarize_growth_estimates(df)

def summarize_growth_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

    # script_runtime_estimates.py
    (base_dir / "script_runtime_estimates.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_script_runtime_from_static_features(path: Path, project_root: Path, profile: LocalPerformanceProfile) -> dict:
    return {"script": path.name, "estimate": "runtime_estimate_low", "warning": "Komut calistirilmaz."}

def build_script_runtime_estimate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"script": "example.py", "estimate": "runtime_estimate_low"}])
    return df, summarize_script_runtime_estimates(df)

def summarize_script_runtime_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

    # test_runtime_estimates.py
    (base_dir / "test_runtime_estimates.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_test_runtime_from_static_features(path: Path, project_root: Path, profile: LocalPerformanceProfile) -> dict:
    return {"test": path.name, "estimate": "runtime_estimate_low", "warning": "Pytest calistirilmaz."}

def build_test_runtime_estimate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"test": "test_example.py", "estimate": "runtime_estimate_low"}])
    return df, summarize_test_runtime_estimates(df)

def summarize_test_runtime_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

    # pipeline_runtime_estimates.py
    (base_dir / "pipeline_runtime_estimates.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_known_pipeline_runtime_estimates(profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"pipeline": "main", "estimate": "runtime_estimate_low", "warning": "Gercek benchmark degildir."}])

def build_pipeline_runtime_estimate_registry(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_known_pipeline_runtime_estimates(profile)
    return df, summarize_pipeline_runtime_estimates(df)

def summarize_pipeline_runtime_estimates(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

if __name__ == "__main__":
    generate_core3()
    print("Core 3 generated")
