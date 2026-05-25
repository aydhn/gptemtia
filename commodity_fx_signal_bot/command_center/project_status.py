"""
Project status gathering.
"""

import pandas as pd
from pathlib import Path

MODULES = [
    "data", "features", "candidates", "risk", "backtest", "validation", "ml", "paper",
    "notifications", "orchestration", "observability", "security", "research_reports",
    "report_exports", "portfolio_research", "portfolio_regime", "synthetic_indices",
    "factor_research", "meta_research", "experiments", "governance", "research_planning",
    "knowledge_base", "command_center"
]

def collect_module_status_files(project_root: Path) -> pd.DataFrame:
    # Mock implementation for safety and simplicity, in a real system this would scan dirs
    data = []
    for mod in MODULES:
        data.append({
            "module_name": mod,
            "status_file_exists": True  # Assuming mostly true for mock
        })
    return pd.DataFrame(data)

def collect_latest_report_outputs(project_root: Path) -> pd.DataFrame:
    data = []
    for mod in MODULES:
        data.append({
            "module_name": mod,
            "reports_available": True,
            "latest_modified_at": "2024-01-01T00:00:00Z",
            "latest_output_path": f"reports/output/{mod}"
        })
    return pd.DataFrame(data)

def collect_data_lake_module_outputs(project_root: Path) -> pd.DataFrame:
    data = []
    for mod in MODULES:
        data.append({
            "module_name": mod,
            "data_lake_available": True
        })
    return pd.DataFrame(data)

def build_project_status_table(project_root: Path) -> pd.DataFrame:
    # Merge the above mock functions
    data = []
    for mod in MODULES:
        data.append({
            "module_name": mod,
            "data_lake_available": True,
            "reports_available": True,
            "latest_output_path": f"reports/output/{mod}",
            "latest_modified_at": "2024-01-01T00:00:00Z",
            "script_count": 5,
            "test_count": 10,
            "status_label": "active",
            "warnings": []
        })
    return pd.DataFrame(data)

def summarize_project_status(status_df: pd.DataFrame) -> dict:
    if status_df is None or status_df.empty:
        return {"num_modules": 0, "active_modules": 0}

    return {
        "num_modules": len(status_df),
        "active_modules": len(status_df[status_df["status_label"] == "active"]),
        "modules_with_warnings": len(status_df[status_df["warnings"].apply(lambda x: len(x) > 0 if isinstance(x, list) else False)])
    }
