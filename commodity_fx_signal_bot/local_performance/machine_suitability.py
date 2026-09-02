import pandas as pd
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
