import os
from pathlib import Path

def generate_core4():
    base_dir = Path("commodity_fx_signal_bot/local_performance")
    
    # maintenance_cost.py
    (base_dir / "maintenance_cost.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def estimate_maintenance_cost_by_layer(project_root: Path, profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"layer": "docs", "cost_category": "docs review", "warning": "Parasal kesinlik degildir."}])

def build_maintenance_cost_estimate(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = estimate_maintenance_cost_by_layer(project_root, profile)
    return df, summarize_maintenance_cost(df)

def summarize_maintenance_cost(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

    # maintenance_effort.py
    (base_dir / "maintenance_effort.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def classify_maintenance_effort(row: pd.Series, profile: LocalPerformanceProfile) -> str:
    return "low"

def build_maintenance_effort_matrix(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"task": "docs review", "effort": "low"}])
    return df, summarize_maintenance_effort(df)

def summarize_maintenance_effort(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

    # operator_time_budget.py
    (base_dir / "operator_time_budget.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_default_operator_time_budget(profile: LocalPerformanceProfile) -> pd.DataFrame:
    return pd.DataFrame([{"category": "docs review", "time_budget": "1h", "warning": "Resmi is gucu plani degildir."}])

def build_operator_time_budget_report(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_operator_time_budget(profile)
    return df, summarize_operator_time_budget(df)

def summarize_operator_time_budget(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

    # machine_suitability.py
    (base_dir / "machine_suitability.py").write_text("""import pandas as pd
from pathlib import Path
from .performance_config import LocalPerformanceProfile

def build_default_machine_suitability_items(profile: LocalPerformanceProfile) -> pd.DataFrame:
    data = [
        {"item": "Python environment manageable", "status": "ok"},
        {"item": "disk budget available", "status": "ok"},
        {"item": "memory budget reasonable", "status": "ok"},
        {"item": "no cloud dependency", "status": "ok"},
        {"item": "no background daemon requirement", "status": "ok"},
        {"item": "no GPU required for reporting layer", "status": "ok"},
        {"item": "scripts are manual-run", "status": "ok"},
        {"item": "reports are file outputs", "status": "ok"},
        {"item": "heavy outputs can be skipped manually", "status": "ok"},
        {"item": "generated outputs can be reviewed offline", "status": "ok"}
    ]
    return pd.DataFrame(data)

def build_local_machine_suitability_checklist(project_root: Path, profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_machine_suitability_items(profile)
    return df, summarize_machine_suitability(df)

def summarize_machine_suitability(df: pd.DataFrame) -> dict: return {"total": len(df) if df is not None else 0}
""", encoding="utf-8")

if __name__ == "__main__":
    generate_core4()
    print("Core 4 generated")
